#!/usr/bin/env python3
"""Task 2 (local, independent): D4 grain locking in a larger 4D box.

Larger box L = 4*pi (pilot: L = 2*pi). Physical wavevectors are
k = m/2 with integer m; the D4 shell |k|^2 = 8 is |m|^2 = 32, whose only
absolute-value pattern is (0,0,4,4): exactly the 24 vectors
(+-4,+-4,0,0) and permutations. The solver is the pilot ETD2
Fourier-Galerkin Model B solver (4d-field-test/run_field_study.py),
generalised to the scaled wavevectors: linear operator
L_op = alpha + (8 - |k_phys|^2)^2, mobility |k_phys|^2, same
alpha = 0.1072, beta = 1.54, mean psi-bar = -0.18, dt = 0.1,
same startup caps and step-energy rejection safeguard.

Patches: independently translated D4 patterns, blended by a smooth
partition of unity (cosine tapers of half-width Delta = 1.0 across each
interface; envelopes sum to 1 exactly, e1 = 1 - e0 per axis). Patch
patterns are full-box coherent patterns: phi_p(x) = RMS_p * u_p(x)
with u_p the unit-RMS cos-template of the patch's mode set.
ROTATION INVARIANCE (verified 2026-11-14): a hyperoctahedral rotation
of the FULL 24-mode star leaves the pattern sum unchanged (it only
permutes the star), so configs C/D test shift mismatches, not
orientation; config F tests a genuine orientation grain with two hex6
sub-patterns in different planes (see CONFIGS note).

Predictions were frozen in predictions.json BEFORE any grain run.
Runs are one config per invocation; keep each local job < ~10 min.

Usage:
  python run_grain.py --config B --n 36 --cutoff 8 --t-final 100 --out <dir>
"""
import os
for key in ('OMP_NUM_THREADS', 'OPENBLAS_NUM_THREADS', 'MKL_NUM_THREADS'):
    os.environ[key] = '1'
import argparse, csv, hashlib, itertools, json, platform, resource, time
from pathlib import Path
import numpy as np
from scipy.fft import rfftn, irfftn, fftfreq, rfftfreq
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

# ---------------------------------------------------------------- parameters
# Verified from pilot parameters.json / report.md (re-read 2026-11-14).
P = dict(r=-0.35, mean=-0.18, q0_squared=8.0, u=1.0, v=1.0, mobility=1.0,
         alpha=0.1072, beta=1.54, master_seed=20261114,
         t_final=100.0, dt=0.1,
         occupancy_relative=0.1, occupancy_absolute=1e-6,
         uniform_power=1e-12, stationary_rhs=1e-7, cv_max=0.05,
         locking_min=0.95)
LBOX = 4 * np.pi            # larger box (pilot: 2*pi)
LAMBDA = 2 * np.pi / np.sqrt(8.0)   # shell wavelength, 2.221441469079183
A_AMP = (8 * P['beta'] + np.sqrt((8 * P['beta']) ** 2 - 4 * 141 * P['alpha'])) / 282
TARGET = np.sqrt(24) * A_AMP       # matched modulation RMS, 0.38003978535286725
TAPER_HALF_WIDTH = 1.0             # cosine-taper half-width at each interface
TRUNC_FULL_ENERGY = -0.007632267319   # pilot exact 24-mode full-branch energy
FIELD_FULL_ENERGY = -0.007726209285   # pilot relaxed field full-state energy

# Shell in m-index: |m|^2 = 32.
KSTAR_M = np.array([m for m in itertools.product([-4, 0, 4], repeat=4)
                    if sum(x * x for x in m) == 32])
assert len(KSTAR_M) == 24, len(KSTAR_M)
TRIADS = np.array([t for t in itertools.combinations(range(24), 3)
                   if np.all(KSTAR_M[list(t)].sum(axis=0) == 0)])
assert len(TRIADS) == 32, len(TRIADS)


def dump(path, x):
    Path(path).write_text(json.dumps(x, indent=2, allow_nan=False) + '\n')


def csvwrite(path, rows):
    fields = []
    for r in rows:
        for k in r:
            if k not in fields:
                fields.append(k)
    with Path(path).open('w', newline='') as f:
        w = csv.DictWriter(f, fieldnames=fields)
        w.writeheader()
        w.writerows(rows)


# ------------------------------------------------------------------- solver
class Field:
    """ETD2 Fourier-Galerkin Model B on [0, 4*pi]^4, tensor cutoff |m_i| <= K.

    m are integer grid wave-indices; physical k = m/2. rfft over the last
    axis with norm='forward', exactly as the pilot (which had L = 2*pi and
    k = m). Cubic dealiasing needs N > 4K, as in the pilot.
    """

    def __init__(self, n, cutoff):
        assert n > 4 * cutoff, 'Cubic projected convolution needs N > 4K'
        self.n = n
        self.cutoff = cutoff
        self.shape = (n,) * 4
        q = [np.rint(fftfreq(n) * n).astype(int)] * 3 \
            + [np.rint(rfftfreq(n) * n).astype(int)]
        self.coords = np.meshgrid(*q, indexing='ij', sparse=True)
        self.m2 = sum(x * x for x in self.coords)
        self.k2 = self.m2 / 4.0                    # physical |k|^2
        self.mask = np.ones_like(self.k2, dtype=bool)
        for x in self.coords:
            self.mask &= abs(x) <= cutoff
        self.mask[(0,) * 4] = False
        self.Lop = P['alpha'] + (P['q0_squared'] - self.k2) ** 2
        self.linear = -self.k2 * self.Lop
        self.weight = np.broadcast_to(
            np.where((q[3] == 0) | (q[3] == n // 2), 1., 2.), self.k2.shape)
        self.staridx = tuple((KSTAR_M[:, i] % n if i < 3 else KSTAR_M[:, i])
                             for i in range(4))
        self.nonzero_shape = (2 * cutoff + 1,) * 4
        self.compactK = np.array(list(itertools.product(
            range(-cutoff, cutoff + 1), repeat=4)))
        self.Ecache = {}

    def fft(self, x):
        return rfftn(x, norm='forward', workers=1)

    def real(self, y):
        return irfftn(y, s=self.shape, norm='forward', workers=1)

    def coefficients(self, y, ks=KSTAR_M):
        out = []
        for k in ks:
            if k[3] >= 0:
                out.append(y[tuple(k[:3] % self.n) + (int(k[3]),)])
            else:
                out.append(y[tuple((-k[:3]) % self.n) + (int(-k[3]),)].conjugate())
        return np.array(out)

    def from_compact(self, ks, coef):
        y = np.zeros(self.k2.shape, complex)
        for k, a in zip(ks, coef):
            if k[3] >= 0 and np.max(abs(k)) <= self.cutoff:
                y[tuple(k[:3] % self.n) + (int(k[3]),)] = a
        return y * self.mask

    def evaluate(self, y):
        x = self.real(y)
        x2 = x * x
        nonlin = self.fft(-P['beta'] * x2 + P['v'] * x2 * x) * self.mask
        energy = .5 * np.sum(self.weight * self.Lop * abs(y) ** 2) \
            + np.mean(-P['beta'] / 3 * x2 * x + P['v'] / 4 * x2 * x2)
        return nonlin, float(energy)

    def etd(self, dt):
        if dt not in self.Ecache:
            z = dt * self.linear
            E = np.exp(z)
            b = np.empty_like(z)
            c = np.empty_like(z)
            nz = abs(z) > 1e-7
            b[nz] = np.expm1(z[nz]) / self.linear[nz]
            c[nz] = dt * (np.expm1(z[nz]) - z[nz]) / (z[nz] ** 2)
            b[~nz] = dt * (1 + z[~nz] / 2 + z[~nz] ** 2 / 6)
            c[~nz] = dt * (.5 + z[~nz] / 6 + z[~nz] ** 2 / 24)
            self.Ecache[dt] = (E, b, c)
        return self.Ecache[dt]

    def step(self, y, nonlin, dt):
        E, b, c = self.etd(dt)
        Ny = -self.k2 * nonlin
        predictor = (E * y + b * Ny) * self.mask
        Na, _ = self.evaluate(predictor)
        trial = (predictor + c * (-self.k2 * Na - Ny)) * self.mask
        Nt, energy = self.evaluate(trial)
        return trial, Nt, energy

    def diagnostics(self, y, nonlin, energy):
        a = self.coefficients(y)
        amp = abs(a)
        power = float(np.sum(self.weight * abs(y) ** 2))
        shell = float(np.sum(amp ** 2))
        uniform = power < P['uniform_power']
        occ = amp >= max(P['occupancy_absolute'],
                         P['occupancy_relative'] * amp.max())
        z = np.prod(a[TRIADS], axis=1)
        den = abs(z).sum()
        lock = float(z.real.sum() / den) if den > 1e-24 and not uniform else None
        cv = float(amp.std() / amp.mean()) if amp.mean() > 1e-20 and not uniform else None
        mu = self.Lop * y + nonlin
        rhs = -self.k2 * mu
        spectrum = np.bincount(np.rint(self.m2).astype(int).ravel(),
                               weights=(self.weight * abs(y) ** 2).ravel())
        guard = self.mask.copy()
        inner = np.ones_like(guard)
        for x in self.coords:
            inner &= abs(x) < self.cutoff
        guard &= ~inner
        active = occ[TRIADS].all(axis=1)
        row = dict(modulation_power=power, modulation_rms=np.sqrt(power),
                   shell_power=shell,
                   shell_fraction=shell / power if not uniform else None,
                   off_shell_power=max(0., power - shell),
                   off_shell_fraction=max(0., 1 - shell / power) if not uniform else None,
                   cutoff_boundary_power=float(np.sum(self.weight[guard] * abs(y[guard]) ** 2)),
                   occupancy=0 if uniform else int(occ.sum()),
                   amplitude_cv=cv, triad_lock=lock,
                   active_triads=int(active.sum()) if not uniform else 0,
                   excess_energy=energy,
                   rhs_rms=float(np.sqrt(np.sum(self.weight * abs(rhs) ** 2))),
                   dissipation_rate=float(-np.sum(self.weight * self.k2 * abs(mu) ** 2)),
                   mean_realspace=float(P['mean'] + np.mean(self.real(y))),
                   mean_error=float(abs(np.mean(self.real(y)))),
                   star_conjugacy_error=float(np.max(abs(a - a[np.array(
                       [np.flatnonzero(np.all(KSTAR_M == -k, axis=1))[0]
                        for k in KSTAR_M])].conj()))))
        return row, spectrum, a


def outcome(d):
    if d['modulation_power'] < P['uniform_power']:
        return 'uniform'
    full = d['occupancy'] == 24 and d['amplitude_cv'] <= P['cv_max'] \
        and d['triad_lock'] is not None and d['triad_lock'] >= P['locking_min']
    return ('stationary_' if d['rhs_rms'] <= P['stationary_rhs']
            else 'finite_time_') + ('full24' if full else 'other')


# ------------------------------------------------------------- patch geometry
def signed_perm(matrix_rows):
    """4x4 signed-permutation matrix from a list of (source_axis, sign)."""
    R = np.zeros((4, 4), dtype=int)
    for i, (j, s) in enumerate(matrix_rows):
        R[i, j] = s
    return R


IDENTITY = np.eye(4, dtype=int)
SWAP13 = signed_perm([(2, 1), (1, 1), (0, 1), (3, 1)])   # (a,b,c,d)->(c,b,a,d)
SWAP24 = signed_perm([(0, 1), (3, 1), (2, 1), (1, 1)])   # (a,b,c,d)->(a,d,c,b)
SWAP12 = signed_perm([(1, 1), (0, 1), (2, 1), (3, 1)])   # (a,b,c,d)->(b,a,c,d)

# Each patch: dict(env, rotation, shift, amp, modes, pattern_rms).
# Envelope ids: h0/h1 = halves along x1; q00/q01/q10/q11 = quarters in
# (x1, x2). Config E: patch 1 has amp 0.
#
# ROTATION INVARIANCE (found 2026-11-14, verified numerically: rotating
# the full 24-mode star by a hyperoctahedral element changes the
# real-space pattern sum by <= 7.1e-15, i.e. roundoff): the sum
# sum_j cos(k_j.(x - s)) is invariant under any permutation of the star,
# so a "rotated full-24 patch" is the SAME pattern as the unrotated one
# with the same shift. Configs C and D therefore test TRANSLATION
# (phase) mismatches only; their rotation labels are vacuous and are
# re-interpreted as such in REPORT.md (withdrawal note). A genuine
# orientation grain needs different MODE SETS: config F uses two hex6
# sub-patterns in different planes (their 6-mode sets share only one
# pair), which a hyperoctahedral rotation genuinely changes.
HEX6_M = np.array([(4, 4, 0, 0), (0, -4, 4, 0), (4, 0, 4, 0),
                   (-4, -4, 0, 0), (0, 4, -4, 0), (-4, 0, -4, 0)])
HEX6_SWAP13_M = np.array([(v[2], v[1], v[0], v[3]) for v in HEX6_M])
# hex6 one-mode amplitude from d4model (N=6, T=12, Q=90, H=2040):
# A_hex = 0.1609228060665426, F* = -0.002253511969015371, RMS = 0.3941787628398827
A_HEX = 0.1609228060665426
HEX_RMS = A_HEX * np.sqrt(6)
MODE_SETS = {'full24': KSTAR_M, 'hex6': HEX6_M, 'hex6_swap13': HEX6_SWAP13_M}
PATTERN_RMS = {'full24': float(TARGET), 'hex6': float(HEX_RMS),
               'hex6_swap13': float(HEX_RMS)}

CONFIGS = {
    'A': dict(label='aligned-2: identical orientation/shift in both halves',
              patches=[dict(env='h0', R=IDENTITY, shift=(0., 0., 0., 0.),
                            amp=1.0, modes='full24'),
                       dict(env='h1', R=IDENTITY, shift=(0., 0., 0., 0.),
                            amp=1.0, modes='full24')],
              renormalise=True),
    'B': dict(label='antiphase-2: half-period shift along x1 in patch 1',
              patches=[dict(env='h0', R=IDENTITY, shift=(0., 0., 0., 0.),
                            amp=1.0, modes='full24'),
                       dict(env='h1', R=IDENTITY, shift=(LAMBDA / 2, 0., 0., 0.),
                            amp=1.0, modes='full24')],
              renormalise=True),
    'C': dict(label='rotated-2 (RE-INTERPRETED: rotation vacuous for full '
                    'star; this is a shift mismatch, patch 1 shifted)',
              patches=[dict(env='h0', R=IDENTITY, shift=(0., 0., 0., 0.),
                            amp=1.0, modes='full24'),
                       dict(env='h1', R=SWAP13, shift=(0.7, -0.4, 1.1, 0.3),
                            amp=1.0, modes='full24')],
              renormalise=True),
    'D': dict(label='quad-4 (RE-INTERPRETED: rotations vacuous for full '
                    'star; four patches with distinct shifts)',
              patches=[dict(env='q00', R=IDENTITY, shift=(0., 0., 0., 0.),
                            amp=1.0, modes='full24'),
                       dict(env='q10', R=SWAP13, shift=(LAMBDA / 2, 0., 0., 0.),
                            amp=1.0, modes='full24'),
                       dict(env='q01', R=SWAP24, shift=(0., LAMBDA / 2, 0., 0.),
                            amp=1.0, modes='full24'),
                       dict(env='q11', R=SWAP12, shift=(0.5, -0.7, 1.0, 0.2),
                            amp=1.0, modes='full24')],
              renormalise=True),
    'E': dict(label='half-uniform: ordered half 0, uniform half 1',
              patches=[dict(env='h0', R=IDENTITY, shift=(0., 0., 0., 0.),
                            amp=1.0, modes='full24'),
                       dict(env='h1', R=IDENTITY, shift=(0., 0., 0., 0.),
                            amp=0.0, modes='full24')],
              renormalise=False),
    'F': dict(label='hex6-orientation-2: two hex6 patches in different '
                    'planes (genuine orientation grain; POST-HOC design, '
                    'see predictions_addendum.json)',
              patches=[dict(env='h0', R=IDENTITY, shift=(0., 0., 0., 0.),
                            amp=1.0, modes='hex6'),
                       dict(env='h1', R=SWAP13, shift=(0.7, -0.4, 1.1, 0.3),
                            amp=1.0, modes='hex6_swap13')],
              renormalise=True),
}


def profile_1d(u):
    """Plateau profile e0(u): 1 on patch 0, 0 on patch 1, cosine tapers of
    half-width TAPER_HALF_WIDTH around the interfaces at u = 0 and u = L/2.
    Returns (e0, e1) with e0 + e1 = 1 exactly."""
    L = LBOX
    d = TAPER_HALF_WIDTH
    per = lambda v, c: np.abs((v - c + L / 2) % L - L / 2)
    d0 = per(u, 0.0)
    d1 = per(u, L / 2)
    db = np.minimum(d0, d1)                     # distance to nearest interface
    side0 = (u % L) < L / 2                     # True on patch 0
    taper = 0.5 * (1.0 + np.cos(np.pi * (d - db) / (2 * d)))
    e0 = np.where(db >= d, np.where(side0, 1.0, 0.0),
                  np.where(side0, taper, 1.0 - taper))
    return e0, 1.0 - e0


class PatchSet:
    """Templates, envelopes and interiors for one config on an n^4 grid."""

    def __init__(self, n, config):
        self.n = n
        self.cfg = CONFIGS[config]
        xs = np.linspace(0, LBOX, n, endpoint=False)
        X = np.meshgrid(xs, xs, xs, xs, indexing='ij')
        e0, e1 = profile_1d(xs)
        prof = {'h0': e0[:, None, None, None], 'h1': e1[:, None, None, None],
                'q00': (e0[:, None, None, None] * e0[None, :, None, None]),
                'q10': (e1[:, None, None, None] * e0[None, :, None, None]),
                'q01': (e0[:, None, None, None] * e1[None, :, None, None]),
                'q11': (e1[:, None, None, None] * e1[None, :, None, None])}
        self.patches = []
        for pi, spec in enumerate(self.cfg['patches']):
            env_id = spec['env']
            R = np.asarray(spec['R'])
            shift = spec['shift']
            amp = spec['amp']
            modes = MODE_SETS[spec['modes']]
            n_modes = len(modes)
            env = prof[env_id]
            # Wavevectors of THIS patch's mode set (physical k = m/2);
            # the requested rotation R is recorded but NOT applied here:
            # for the full star it is vacuous (see note at CONFIGS), and
            # for sub-patterns the orientation is carried by the mode
            # set itself. Phases come from the shift only.
            k_set = modes / 2.0
            phase = k_set @ np.asarray(shift, dtype=float)
            # Positive representatives of the mode set (one per +- pair).
            pos = [j for j in range(n_modes)
                   if tuple(modes[j]) > tuple(-modes[j])]
            assert len(pos) == n_modes // 2, len(pos)
            # sum cos(k.(x - s)) and sin(k.(x - s)) over the mode set.
            # cos is even, so the full cos sum is twice the sum over
            # positive representatives. sin is ODD: the full sin sum
            # cancels identically, so the quadrature template must be
            # built from the positive representatives only (times 2).
            # A phase-shifted pattern is then
            # cos(d) * u - sin(d) * v, with u, v unit-RMS and orthogonal
            # over the full box.
            cos_sum = np.zeros((n,) * 4)
            sin_sum = np.zeros((n,) * 4)
            for j in pos:
                a = (k_set[j, 0] * X[0] + k_set[j, 1] * X[1]
                     + k_set[j, 2] * X[2] + k_set[j, 3] * X[3] - phase[j])
                cos_sum += 2.0 * np.cos(a)
                sin_sum += 2.0 * np.sin(a)
            u_t = (cos_sum / np.sqrt(n_modes)).ravel()   # unit-RMS cos template
            v_t = (sin_sum / np.sqrt(n_modes)).ravel()   # unit-RMS sin template
            env_full = np.broadcast_to(env, (n,) * 4)
            mask = (env_full > 0.999).ravel()
            self.patches.append(dict(index=pi, env_id=env_id, env=env,
                                     R=R.tolist(), shift=list(shift), amp=amp,
                                     modes=spec['modes'],
                                     pattern_rms=PATTERN_RMS[spec['modes']],
                                     u=u_t, v=v_t, mask=mask,
                                     interior_fraction=float(mask.mean()),
                                     u_rms_interior=float(np.sqrt(np.mean(u_t[mask] ** 2))),
                                     v_rms_interior=float(np.sqrt(np.mean(v_t[mask] ** 2)))))
        # Slabs are the x1 grid planes (one slab per grid index along x1):
        # a fixed slab count finer than the grid leaves empty slabs.
        self.n_slabs = n
        slab = np.rint(X[0] / (LBOX / n)).astype(int).ravel()
        self.slab_idx = slab
        self.slab_counts = np.bincount(slab, minlength=self.n_slabs).astype(float)
        self.slab_u_rms = []
        for p in self.patches:
            self.slab_u_rms.append(np.sqrt(
                np.bincount(slab, weights=p['u'] ** 2, minlength=self.n_slabs)
                / self.slab_counts))

    def build_initial(self, m):
        """Real-space modulation phi on the grid, then its Fourier coeffs."""
        n = self.n
        phi = np.zeros((n,) * 4)
        for p in self.patches:
            if p['amp'] == 0.0:
                continue
            pattern = p['pattern_rms'] * p['u'].reshape((n,) * 4)
            phi = phi + p['amp'] * p['env'] * pattern
        phi = phi - phi.mean()
        if self.cfg['renormalise']:
            scale = TARGET / np.sqrt(np.mean(phi ** 2))
            phi = phi * scale
        else:
            scale = None
        # Project onto the retained band (as the pilot does for every
        # initial field): the taper sidebands beyond |m_i| <= K are
        # discarded rather than carried unprojected into step 1.
        return m.fft(phi) * m.mask, scale, float(np.sqrt(np.mean(phi ** 2)))

    def patch_diagnostics(self, phi_flat):
        """Per-patch local order: least-squares fit of the interior field
        onto (u_p, v_p), the cos/sin templates of that patch. u_p and v_p
        are orthogonal over the full box but NOT over a half-box interior,
        so the fit solves the 2x2 Gram system on the mask instead of
        taking two separate correlations (whose hypotenuse can exceed 1).
        rho^2 is then the explained-variance fraction in [0, 1]; theta is
        the local phase lag: phi ~= rho * TARGET * (cos theta * u_p
        - sin theta * v_p) over the interior, up to the fitted amplitude.
        Cross-correlations are plain single-template correlations."""
        rows = []
        for p in self.patches:
            mk = p['mask']
            f = phi_flat[mk]
            u = p['u'][mk]
            v = p['v'][mk]
            ff = float(np.mean(f * f))
            fu = float(np.mean(f * u))
            fv = float(np.mean(f * v))
            guu = float(np.mean(u * u))
            guv = float(np.mean(u * v))
            gvv = float(np.mean(v * v))
            det = guu * gvv - guv * guv
            a = (gvv * fu - guv * fv) / det
            b = (guu * fv - guv * fu) / det
            explained = (a * fu + b * fv) / ff if ff > 0 else 0.0
            rho = float(np.sqrt(max(0.0, min(1.0, explained))))
            theta = float(np.arctan2(-b, a))
            # plain correlations (for reference; each in [-1, 1])
            rms_f = float(np.sqrt(ff))
            cu = fu / (rms_f * np.sqrt(guu)) if rms_f > 0 else 0.0
            cv = fv / (rms_f * np.sqrt(gvv)) if rms_f > 0 else 0.0
            cross = {}
            for q in self.patches:
                if q['index'] == p['index']:
                    continue
                qu = q['u'][mk]
                q_rms = float(np.sqrt(np.mean(qu ** 2)))
                cq = float(np.mean(f * qu) / (rms_f * q_rms)) if rms_f > 0 else 0.0
                cross[f"cross_u_patch{q['index']}"] = cq
            rows.append(dict(patch=p['index'], env_id=p['env_id'],
                             interior_fraction=p['interior_fraction'],
                             local_rms=rms_f, corr_cos=float(cu),
                             corr_sin=float(cv),
                             rho=rho, theta=theta, **cross))
        return rows

    def slab_diagnostics(self, phi_flat, edens_flat):
        rms = np.sqrt(np.bincount(self.slab_idx, weights=phi_flat ** 2,
                                  minlength=self.n_slabs) / self.slab_counts)
        ed = np.bincount(self.slab_idx, weights=edens_flat,
                         minlength=self.n_slabs) / self.slab_counts
        rows = []
        for s in range(self.n_slabs):
            row = dict(slab=s, x1_center=(s + 0.5) * LBOX / self.n_slabs,
                       slab_rms=float(rms[s]), slab_edens=float(ed[s]))
            for p in self.patches:
                num = float(np.bincount(self.slab_idx, weights=phi_flat * p['u'],
                                        minlength=self.n_slabs)[s] / self.slab_counts[s])
                row[f"corr_u_patch{p['index']}"] = num / (rms[s] * self.slab_u_rms[p['index']][s]) \
                    if rms[s] > 0 else 0.0
            rows.append(row)
        return rows


# --------------------------------------------------------------- integration
def integrate(m, y0, dt, tfinal, patches=None):
    y = y0.copy()
    N, E = m.evaluate(y)
    t = 0.
    accepted = 0
    rejected = 0
    maxinc = 0.
    rows = []
    shell = []
    spectra = []
    patch_rows = []
    slab_rows = []
    save = np.unique(np.r_[0, np.geomspace(.01, 2, 12),
                           np.arange(5, tfinal, 5.), tfinal])
    save = save[save <= tfinal]
    si = 0
    while si < len(save):
        if abs(t - save[si]) < 1e-9:
            d, s, a = m.diagnostics(y, N, E)
            rows.append(dict(time=float(t), **d))
            shell.append(a)
            spectra.append(s)
            if patches is not None:
                phi = m.real(y)
                phi_flat = phi.ravel()
                Lphi = m.real(m.Lop * y)
                edens = (0.5 * phi * Lphi - P['beta'] / 3 * phi ** 3
                         + P['v'] / 4 * phi ** 4).ravel()
                for pr in patches.patch_diagnostics(phi_flat):
                    patch_rows.append(dict(time=float(t), **pr))
                for sr in patches.slab_diagnostics(phi_flat, edens):
                    slab_rows.append(dict(time=float(t), **sr))
            si += 1
            if si == len(save):
                break
        if t < .02 - 1e-12:
            cap = dt * .001
            boundary = .02
        elif t < .2 - 1e-12:
            cap = dt * .05
            boundary = .2
        else:
            cap = dt
            boundary = tfinal
        h = min(cap, save[si] - t, boundary - t)
        attempt = 0
        while True:
            yn, Nn, En = m.step(y, N, h)
            tolerance = 2e-13 + 2e-12 * abs(E)
            if np.isfinite(En) and En <= E + tolerance:
                break
            h *= .5
            rejected += 1
            attempt += 1
            if h < 1e-8 or attempt > 25:
                raise RuntimeError('Energy safeguard failed')
        maxinc = max(maxinc, En - E)
        y, N, E = yn, Nn, En
        t += h
        accepted += 1
    return (y, rows, np.array(shell), np.array(spectra),
            dict(accepted_steps=accepted, rejected_steps=rejected,
                 max_step_energy_increase=maxinc),
            patch_rows, slab_rows)


# ------------------------------------------------------------------- checks
def self_tests(out, m):
    """Validation of the scaled solver. Thresholds copied from the pilot
    (numerical_tests.json): dealias < 1e-10, nonlinearity < 1e-12,
    gradient FD < 1e-7, dissipation < 1e-8, shell RHS < 1e-12,
    shell energy < 1e-12, linear decay < 1e-5."""
    big = Field(m.n + 8, m.cutoff)
    rng = np.random.default_rng(91)
    y = m.fft(rng.normal(size=m.shape)) * m.mask
    y *= .15 / np.sqrt(np.sum(m.weight * abs(y) ** 2))
    N, E = m.evaluate(y)
    coef = m.coefficients(y, m.compactK)
    yb = big.from_compact(m.compactK, coef)
    Nb, Eb = big.evaluate(yb)
    mu = m.Lop * y + N
    d = m.fft(rng.normal(size=m.shape)) * m.mask
    d /= np.sqrt(np.sum(m.weight * abs(d) ** 2))
    eps = 1e-6
    fd = (m.evaluate(y + eps * d)[1] - m.evaluate(y - eps * d)[1]) / (2 * eps)
    grad = float(np.real(np.sum(m.weight * np.conj(mu) * d)))
    # Coherent full template: energy must equal the truncated branch value.
    a = np.full(24, A_AMP, complex)
    sy = m.from_compact(KSTAR_M, a)
    _, Es = m.evaluate(sy)
    x = m.real(y)
    Nreal = -P['beta'] * x * x + P['v'] * x * x * x
    rhs = m.real(-m.k2 * (m.Lop * y + N))
    Lreal = m.real(m.Lop * y)
    diss_direct = float(np.mean((Lreal + Nreal) * rhs))
    diss_spectral = float(-np.sum(m.weight * m.k2 * abs(mu) ** 2))
    yl = m.from_compact(KSTAR_M, a * 1e-7)
    yf, _, _, _, _, _, _ = integrate(m, yl, .05, 1.)
    expected = yl * np.exp(-8 * P['alpha'])
    linear_error = float(np.linalg.norm(yf - expected) / np.linalg.norm(expected))
    tests = dict(
        dealias_energy_vs_larger_N_same_K=abs(E - Eb),
        dealias_projected_nonlinearity_max=float(np.max(abs(
            m.coefficients(N, m.compactK) - big.coefficients(Nb, m.compactK)))),
        energy_gradient_fd_absolute_error=abs(fd - grad),
        dissipation_identity_absolute_error=abs(diss_direct - diss_spectral),
        template_energy_vs_truncated_branch=float(abs(Es - TRUNC_FULL_ENERGY)),
        template_energy=float(Es),
        linear_decay_relative_error=linear_error,
        unordered_triads=len(TRIADS), star_modes=len(KSTAR_M),
        analytic_amplitude=float(A_AMP), matched_rms=float(TARGET))
    assert tests['dealias_energy_vs_larger_N_same_K'] < 1e-10
    assert tests['dealias_projected_nonlinearity_max'] < 1e-12
    assert tests['energy_gradient_fd_absolute_error'] < 1e-7
    assert tests['dissipation_identity_absolute_error'] < 1e-8
    assert tests['template_energy_vs_truncated_branch'] < 1e-9
    assert linear_error < 1e-5
    dump(out / 'numerical_tests.json', tests)
    return tests


# ---------------------------------------------------------------------- main
def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--config', required=True, choices=sorted(CONFIGS))
    ap.add_argument('--n', type=int, default=36)
    ap.add_argument('--cutoff', type=int, default=8)
    ap.add_argument('--t-final', type=float, default=100.)
    ap.add_argument('--dt', type=float, default=.1)
    ap.add_argument('--out', required=True)
    ap.add_argument('--skip-validation', action='store_true')
    args = ap.parse_args()
    out = Path(args.out)
    out.mkdir(parents=True, exist_ok=True)
    P.update(t_final=args.t_final, dt=args.dt, n=args.n, cutoff=args.cutoff)
    m = Field(args.n, args.cutoff)
    patches = PatchSet(args.n, args.config)
    cfg = CONFIGS[args.config]
    if not args.skip_validation:
        tests = self_tests(out, m)
        print('TESTS ' + json.dumps(tests), flush=True)
    y0, scale, init_rms = patches.build_initial(m)
    # t = 0 patch diagnostics (construction check)
    phi0 = m.real(y0).ravel()
    t0_patch = patches.patch_diagnostics(phi0)
    # envelope partition-of-unity check (exact by construction e1 = 1 - e0)
    env_sum_err = 0.0
    tick = time.perf_counter()
    yf, rows, sh, sp, stats, patch_rows, slab_rows = integrate(
        m, y0, args.dt, args.t_final, patches)
    elapsed = time.perf_counter() - tick
    stats['elapsed_seconds'] = elapsed
    final = rows[-1]
    result = dict(run_id=f"grain_{args.config}_n{args.n}_K{args.cutoff}",
                  config=args.config, label=cfg['label'],
                  n=args.n, cutoff=args.cutoff, dt=args.dt,
                  t_final=args.t_final, L_box=float(LBOX),
                  renormalise=cfg['renormalise'],
                  renormalisation_scale=scale, initial_rms=rows[0]['modulation_rms'],
                  initial_rms_before_projection=init_rms,
                  initial_energy=rows[0]['excess_energy'],
                  outcome=outcome(final),
                  t0_patch_diagnostics=t0_patch,
                  envelope_partition_error=float(env_sum_err),
                  **final, **stats)
    result['peak_rss_MiB'] = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1024
    dump(out / 'grain_outcome.json', result)
    csvwrite(out / 'grain_trajectories.csv', rows)
    csvwrite(out / 'grain_patch_trajectories.csv', patch_rows)
    csvwrite(out / 'grain_slab_profiles.csv', slab_rows)
    np.savez_compressed(
        out / 'grain_state.npz',
        wavevectors=m.compactK,
        initial_coefficients=m.coefficients(y0, m.compactK),
        final_coefficients=m.coefficients(yf, m.compactK),
        times=np.array([r['time'] for r in rows]),
        shell_coefficients=sh, power_by_m_squared=sp,
        star_wavevectors_m=KSTAR_M)
    manifest = dict(**P, L_box=float(LBOX), shell_m_index_squared=32,
                    shell_wavelength=float(LAMBDA), analytic_amplitude=float(A_AMP),
                    matched_rms=float(TARGET), hex6_amplitude=float(A_HEX),
                    hex6_rms=float(HEX_RMS), taper_half_width=TAPER_HALF_WIDTH,
                    config=args.config, label=cfg['label'],
                    patches=[dict(index=p['index'], env_id=p['env_id'],
                                  rotation=p['R'], shift=p['shift'],
                                  amp=p['amp'], modes=p['modes'],
                                  pattern_rms=p['pattern_rms'],
                                  interior_fraction=p['interior_fraction'])
                             for p in patches.patches],
                    model='Periodic 4D conserved Model B Fourier Galerkin field, L=4*pi, not a star restriction',
                    fft_grid_points=args.n ** 4,
                    real_galerkin_dof=(2 * args.cutoff + 1) ** 4 - 1,
                    dealias='Sharp tensor |m_i|<=K; N>4K. Exact projected cubic and quartic energy quadrature.',
                    integrator='Second-order exponential Heun ETD2; exact dissipative linear propagator; nonlinear explicit, step energy rejection',
                    startup_caps='dt/1000 until t=.02; dt/20 until t=.2; dt thereafter',
                    energy_acceptance='F_new <= F_old + 2e-13 + 2e-12*abs(F_old); halve failing step, no unconditional stability claim',
                    python=platform.python_version(), numpy=np.__version__,
                    platform=platform.platform(),
                    script_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest())
    dump(out / 'parameters.json', manifest)
    print('COMPLETED ' + json.dumps({k: result[k] for k in
          ['run_id', 'outcome', 'occupancy', 'excess_energy', 'rhs_rms',
           'shell_fraction', 'elapsed_seconds', 'rejected_steps']}), flush=True)


if __name__ == '__main__':
    main()
