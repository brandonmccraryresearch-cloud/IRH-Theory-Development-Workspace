#!/usr/bin/env python3
"""Task 4: conserved Model B formation on each star's NATIVE 4D cell.
Generalises 4d-field-test/run_field_study.py (same ETD2 solver, same quench,
same matched RMS, same save times, same diagnostics) to an oblique torus.

Cell construction (y-coordinates, unit cube, FFT over y):
  x = A y, A = 2*pi * M^{-T}  (real-space cell basis, columns of A)
  physical k = M n, n in Z^4 (lattice coordinates), M = reciprocal basis.
  D4:    M = I (cubic box [0,2*pi]^4, reciprocal Z^4) -- identical to field test.
  A4star: M columns = Helmert coords of 2*(e_j - e_{j+1}), j=1..4 (A4 simple
          roots scaled by 2). Star vectors then have integer n with entries
          0/+-1 (verified in verify_geometry.py); |k|^2 = 8 for all 20.
Retained band: tensor |n_i| <= cutoff in LATTICE coordinates (same rule both
stars, same DOF count 6560 at cutoff 4, same N=18 grid, N > 4*cutoff dealiasing
in n-space). This is the matched truncation; physical-|k| spectra differ
between cells and that difference is inherent, not matched away (see REPORT).
Energy is volume-normalised excess density in each cell, so the two runs are
comparable as densities.

Initial families (mirroring the field test, per star):
  random_full_weak / random_full_matched: broadband Gaussian in n-space.
  six_1pct_full_noise: 6-mode seed (D4: A2 subset; A4*: A2 roots e_i-e_j,
      i,j in {1,2,3}) + 1% broadband noise.
  twelve_1pct_full_noise: 12-mode seed (D4: k4=0 D3 slice; A4*: A3 roots
      i,j in {1,2,3,4}) + 1% broadband noise.
  full_25pct_full_noise: full star + 25% broadband noise.
  random_shell_matched_bridge: D4/A4* projection of the broadband direction,
      renormalised to the common matched RMS.
Common matched RMS = D4 stationary RMS 0.38003978535286725 (methods.md:
matching RMS B, not per-mode A). Same master seed 931241112, same replicate
seeds as the field test, so D4 runs replicate that study's initial directions.
Patterned seeds: D4 uses cubic axis permutations/sign flips + translation
(as field test); A4* uses a random S5 permutation of the 5 underlying
indices + a y-translation (the star's own symmetry group) -- the symmetry
groups differ, so this step is analogous, not identical (ledgered).
No random forcing after t=0, no annealing, no parameter ramp.
"""
import os
for key in ('OMP_NUM_THREADS', 'OPENBLAS_NUM_THREADS', 'MKL_NUM_THREADS'):
    os.environ[key] = '1'
import argparse, csv, hashlib, itertools, json, platform, resource, time
from pathlib import Path
import numpy as np
import scipy
from scipy.fft import rfftn, irfftn, fftfreq, rfftfreq
from scipy.integrate import solve_ivp
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

BASE = Path.home() / "workspace/research/irh/co-scientist-tasks-2026-11-10"
A20 = BASE / "a20-onset"
OUTROOT = BASE / "local-independent/task4-native-cells"
P = dict(r=-.35, mean=-.18, q0_squared=8., u=1., v=1., mobility=1.,
         alpha=.1072, beta=1.54, master_seed=931241112, replicates=3,
         t_final=200., dt=.1, n=18, cutoff=4, occupancy_relative=.1,
         occupancy_absolute=1e-6, uniform_power=1e-12, stationary_rhs=1e-7,
         cv_max=.05, locking_min=.95)
STARS = {}  # filled by load_stars()
FAMILIES = ['random_full_weak', 'random_full_matched', 'six_1pct_full_noise',
            'twelve_1pct_full_noise', 'full_25pct_full_noise',
            'random_shell_matched_bridge']

def helmert():
    H = np.zeros((5, 4))
    for j in range(1, 5):
        v = np.zeros(5); v[:j] = 1.0; v[j] = -j
        H[:, j-1] = v / np.sqrt(j*(j+1))
    return H

def load_stars():
    stars = json.loads((A20 / "stars.json").read_text())
    ver = json.loads((OUTROOT / "verification.json").read_text())
    # D4: M = I, star lattice coords = physical k vectors
    d4k = np.array(stars["D4"]["cartesian_R4_float"], dtype=int)
    STARS["D4"] = dict(N=24, T=192, Q=3384, M=np.eye(4), star_n=d4k,
                       star_cart=d4k.astype(float),
                       subsets={})
    # A4*: M from verification, star_n from verification
    M = np.array(ver["M_A4star"]); star_n = np.array(ver["ncoords_A4star"], dtype=int)
    cart = np.array(stars["A4star"]["cartesian_R4_float"])
    intr = np.array(stars["A4star"]["exact_intrinsic_integer_vectors"], dtype=int)
    STARS["A4star"] = dict(N=20, T=120, Q=1860, M=M, star_n=star_n,
                           star_cart=cart, intrinsic=intr, subsets={})
    # A4* subsets: A2 = roots with support in indices {0,1,2}; A3 in {0,1,2,3}
    for name, allowed in [("six", {0, 1, 2}), ("twelve", {0, 1, 2, 3})]:
        idx = [i for i, v in enumerate(intr)
               if set(np.nonzero(v)[0].tolist()) <= allowed
               and len(np.nonzero(v)[0]) == 2]
        STARS["A4star"]["subsets"][name] = np.array(idx, dtype=int)
    # D4 subsets (physical = lattice coords)
    six_phys = np.array([[2, -2, 0, 0], [0, 2, -2, 0], [2, 0, -2, 0],
                         [-2, 2, 0, 0], [0, -2, 2, 0], [-2, 0, 2, 0]])
    STARS["D4"]["subsets"]["six"] = np.array(
        [int(np.flatnonzero(np.all(d4k == s, axis=1))[0]) for s in six_phys])
    STARS["D4"]["subsets"]["twelve"] = np.flatnonzero(d4k[:, 3] == 0)
    for sname, s in STARS.items():
        s["triads"] = np.array([t for t in itertools.combinations(range(s["N"]), 3)
                                if np.all(s["star_n"][list(t)].sum(axis=0) == 0)])
        # pair / triple lists for the shell-only (truncated) RHS, in n-coords
        pos = {tuple(v): i for i, v in enumerate(s["star_n"])}
        s["pairs"] = [[] for _ in range(s["N"])]
        s["triples"] = [[] for _ in range(s["N"])]
        for i, p in enumerate(s["star_n"]):
            for j, q in enumerate(s["star_n"]):
                k = tuple(p + q)
                if k in pos:
                    s["pairs"][pos[k]].append((i, j))
                for l, r_ in enumerate(s["star_n"]):
                    if tuple(p + q + r_) in pos:
                        s["triples"][pos[tuple(p + q + r_)]].append((i, j, l))
    return STARS

def dump(path, x):
    path.write_text(json.dumps(x, indent=2, allow_nan=False) + '\n')

def csvwrite(path, rows):
    with path.open('w', newline='') as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0])); w.writeheader(); w.writerows(rows)

class Field:
    def __init__(self, star, n, cutoff):
        assert n > 4 * cutoff, 'Cubic projected convolution and quartic quadrature need N>4K'
        self.star = star; self.n = n; self.cutoff = cutoff; self.shape = (n,) * 4
        S = STARS[star]; self.M = S["M"]; self.star_n = S["star_n"]
        q = [np.rint(fftfreq(n) * n).astype(int)] * 3 + [np.rint(rfftfreq(n) * n).astype(int)]
        self.coords = np.meshgrid(*q, indexing='ij', sparse=True)
        # physical k = M @ n_vec for every rfft grid point (sparse coords broadcast)
        kcomp = [sum(self.M[a, b] * self.coords[b] for b in range(4)) for a in range(4)]
        self.k2 = sum(ka ** 2 for ka in kcomp)
        self.mask = np.ones_like(self.k2, dtype=bool)
        for x in self.coords:
            self.mask &= abs(x) <= cutoff
        # Physical cap, matched to the D4 tensor band maximum |k|^2 = 64:
        # without it the A4* tensor band reaches |k|^2 = 896 and its broadband
        # starts would be dominated by ultra-high-k linear penalty. For D4
        # the cap is redundant (tensor |k_i|<=4 already implies |k|^2<=64).
        self.mask &= self.k2 <= 64.0 + 1e-9
        self.mask[(0,) * 4] = False
        self.L = P['alpha'] + (P['q0_squared'] - self.k2) ** 2
        self.linear = -self.k2 * self.L
        self.weight = np.broadcast_to(np.where((q[3] == 0) | (q[3] == n // 2), 1., 2.), self.k2.shape)
        self.Ecache = {}
        self.nonzero_shape = (2 * cutoff + 1,) * 4
        self.compactK = np.array(list(itertools.product(range(-cutoff, cutoff + 1), repeat=4)))
    def fft(self, x): return rfftn(x, norm='forward', workers=1)
    def real(self, y): return irfftn(y, s=self.shape, norm='forward', workers=1)
    def coefficients(self, y, ks=None):
        ks = self.star_n if ks is None else ks
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
        x = self.real(y); x2 = x * x
        nonlin = self.fft(-P['beta'] * x2 + P['v'] * x2 * x) * self.mask
        energy = .5 * np.sum(self.weight * self.L * abs(y) ** 2) + np.mean(-P['beta'] / 3 * x2 * x + P['v'] / 4 * x2 * x2)
        return nonlin, float(energy)
    def etd(self, dt):
        if dt not in self.Ecache:
            z = dt * self.linear; E = np.exp(z)
            b = np.empty_like(z); c = np.empty_like(z)
            nz = abs(z) > 1e-7
            b[nz] = np.expm1(z[nz]) / self.linear[nz]
            c[nz] = dt * (np.expm1(z[nz]) - z[nz]) / (z[nz] ** 2)
            b[~nz] = dt * (1 + z[~nz] / 2 + z[~nz] ** 2 / 6)
            c[~nz] = dt * (.5 + z[~nz] / 6 + z[~nz] ** 2 / 24)
            self.Ecache[dt] = (E, b, c)
        return self.Ecache[dt]
    def step(self, y, nonlin, dt):
        E, b, c = self.etd(dt); Ny = -self.k2 * nonlin
        predictor = (E * y + b * Ny) * self.mask
        Na, _ = self.evaluate(predictor)
        trial = (predictor + c * (-self.k2 * Na - Ny)) * self.mask
        Nt, energy = self.evaluate(trial)
        return trial, Nt, energy
    def diagnostics(self, y, nonlin, energy):
        S = STARS[self.star]
        a = self.coefficients(y); amp = abs(a)
        power = float(np.sum(self.weight * abs(y) ** 2)); shell = float(np.sum(amp ** 2))
        uniform = power < P['uniform_power']
        occ = amp >= max(P['occupancy_absolute'], P['occupancy_relative'] * amp.max())
        z = np.prod(a[S["triads"]], axis=1); den = abs(z).sum()
        lock = float(z.real.sum() / den) if den > 1e-24 and not uniform else None
        cv = float(amp.std() / amp.mean()) if amp.mean() > 1e-20 and not uniform else None
        mu = self.L * y + nonlin; rhs = -self.k2 * mu
        spectrum = np.bincount(np.rint(self.k2).astype(int).ravel(),
                               weights=(self.weight * abs(y) ** 2).ravel())
        guard = self.mask.copy(); inner = np.ones_like(guard)
        for x in self.coords: inner &= abs(x) < self.cutoff
        guard &= ~inner
        active = occ[S["triads"]].all(axis=1)
        conj_idx = np.array([np.flatnonzero(np.all(self.star_n == -k, axis=1))[0] for k in self.star_n])
        return dict(modulation_power=power, modulation_rms=np.sqrt(power), shell_power=shell,
                    shell_fraction=shell / power if not uniform else None,
                    off_shell_power=max(0., power - shell),
                    off_shell_fraction=max(0., 1 - shell / power) if not uniform else None,
                    cutoff_boundary_power=float(np.sum(self.weight[guard] * abs(y[guard]) ** 2)),
                    occupancy=0 if uniform else int(occ.sum()), amplitude_cv=cv, triad_lock=lock,
                    active_triads=int(active.sum()) if not uniform else 0,
                    excess_energy=energy, rhs_rms=float(np.sqrt(np.sum(self.weight * abs(rhs) ** 2))),
                    dissipation_rate=float(-np.sum(self.weight * self.k2 * abs(mu) ** 2)),
                    mean_realspace=float(P['mean'] + np.mean(self.real(y))),
                    mean_error=float(abs(np.mean(self.real(y)))),
                    star_conjugacy_error=float(np.max(abs(a - a[conj_idx].conj())))), spectrum, a

# --- shell-only truncated dynamics (second independent route) ---
def trunc_rhs(t, a, star):
    """Shell-only RHS by explicit pair/triple enumeration (slow, exact).
    Reference route; used in self_tests and cross-checked against the
    FFT route below."""
    S = STARS[star]; a = np.asarray(a, complex)
    out = np.zeros_like(a)
    for k in range(S["N"]):
        quad = sum(a[i] * a[j] for (i, j) in S["pairs"][k])
        cub = sum(a[i] * a[j] * a[l] for (i, j, l) in S["triples"][k])
        out[k] = -8.0 * (P['alpha'] * a[k] - P['beta'] * quad + P['v'] * cub)
    return out

def trunc_rhs_fft(t, a, star, field):
    """Shell-only RHS via FFT convolution on the y-grid (fast route).
    Verified against trunc_rhs (pair/triple enumeration) in self_tests at
    both the equal-amplitude state and a random complex state."""
    y = field.from_compact(field.star_n, np.asarray(a, complex))
    N, _ = field.evaluate(y)
    mu = P['alpha'] * np.asarray(a, complex) + field.coefficients(N)
    return -8.0 * mu

def trunc_energy(a, star, field):
    # exact shell energy via y-grid reconstruction (star n-components are 0/+-1,
    # so phi^3/phi^4 grid means are exact zero-sum sums at N=18)
    y = field.from_compact(field.star_n, np.asarray(a, complex))
    x = field.real(y)
    lin = .5 * P['alpha'] * float(np.sum(abs(a) ** 2))
    return float(lin + np.mean(-P['beta'] / 3 * x ** 3 + P['v'] / 4 * x ** 4))

def trunc_diagnostics(a, star):
    S = STARS[star]; amp = abs(a)
    power = float(np.sum(amp ** 2))
    uniform = power < P['uniform_power']
    occ = amp >= max(P['occupancy_absolute'], P['occupancy_relative'] * amp.max())
    z = np.prod(a[S["triads"]], axis=1); den = abs(z).sum()
    lock = float(z.real.sum() / den) if den > 1e-24 and not uniform else None
    cv = float(amp.std() / amp.mean()) if amp.mean() > 1e-20 and not uniform else None
    return dict(occupancy=0 if uniform else int(occ.sum()), amplitude_cv=cv,
                triad_lock=lock, modulation_power=power)

def make_initial(m, family, rep):
    S = STARS[m.star]
    seed = int(np.random.SeedSequence([P['master_seed'], rep]).generate_state(1)[0])
    rng = np.random.default_rng(seed)
    noise = m.fft(rng.normal(size=m.shape)) * m.mask
    noise /= np.sqrt(np.sum(m.weight * abs(noise) ** 2))
    target = float(np.sqrt(24) * 0.07757529634)  # D4 stationary RMS 0.38003978535286725
    if family.startswith('random_full'):
        y = noise * (.05 if family.endswith('weak') else target)
    elif family == 'random_shell_matched_bridge':
        a = m.coefficients(noise); a *= target / np.linalg.norm(a)
        y = m.from_compact(m.star_n, a)
    else:
        if family.startswith('six'):
            base_idx = S["subsets"]["six"]; eta = .01
        elif family.startswith('twelve'):
            base_idx = S["subsets"]["twelve"]; eta = .01
        else:
            base_idx = np.arange(S["N"]); eta = .25
        base = np.zeros(S["N"]); base[base_idx] = 1.0
        if m.star == "D4":
            perm = rng.permutation(4); sign = rng.choice([-1, 1], 4)
            ks = m.star_n[:, perm] * sign
            shift = rng.uniform(-np.pi, np.pi, 4)
            template = m.from_compact(ks, base / np.linalg.norm(base) * np.exp(1j * ks @ shift))
        else:
            # S5 permutation of the 5 underlying A4 indices + y-translation
            perm5 = rng.permutation(5)
            intr_perm = S["intrinsic"][:, perm5]
            order = {tuple(v): i for i, v in enumerate(S["intrinsic"])}
            new_idx = np.array([order[tuple(v)] for v in intr_perm])
            ks = m.star_n[new_idx]
            base_p = base[new_idx]
            shift = rng.uniform(0.0, 1.0, 4)
            template = m.from_compact(ks, base_p / np.linalg.norm(base_p) * np.exp(2j * np.pi * ks @ shift))
        y = template + eta * noise
        y *= target / np.sqrt(np.sum(m.weight * abs(y) ** 2))
    return y, seed

def integrate(m, y0, dt, tfinal):
    y = y0.copy(); N, E = m.evaluate(y); t = 0.; accepted = 0; rejected = 0; maxinc = 0.
    rows = []; shell = []; spectra = []
    save = np.unique(np.r_[0, np.geomspace(.01, 2, 12), np.arange(5, tfinal, 5.), tfinal])
    save = save[save <= tfinal]; si = 0
    while si < len(save):
        if abs(t - save[si]) < 1e-9:
            d, s, a = m.diagnostics(y, N, E)
            rows.append(dict(time=float(t), **d)); shell.append(a); spectra.append(s); si += 1
            if si == len(save): break
        if t < .02 - 1e-12: cap = dt * .001; boundary = .02
        elif t < .2 - 1e-12: cap = dt * .05; boundary = .2
        else: cap = dt; boundary = tfinal
        h = min(cap, save[si] - t, boundary - t); attempt = 0
        while True:
            yn, Nn, En = m.step(y, N, h)
            tolerance = 2e-13 + 2e-12 * abs(E)
            if np.isfinite(En) and En <= E + tolerance: break
            h *= .5; rejected += 1; attempt += 1
            if h < 1e-8 or attempt > 25: raise RuntimeError('Energy safeguard failed')
        maxinc = max(maxinc, En - E); y, N, E = yn, Nn, En; t += h; accepted += 1
    return y, rows, np.array(shell), np.array(spectra), dict(accepted_steps=accepted,
        rejected_steps=rejected, max_step_energy_increase=maxinc)

def outcome(d, star):
    if d['modulation_power'] < P['uniform_power']: return 'uniform'
    full = d['occupancy'] == STARS[star]["N"] and d['amplitude_cv'] <= P['cv_max'] \
        and d['triad_lock'] is not None and d['triad_lock'] >= P['locking_min']
    return ('stationary_' if d['rhs_rms'] <= P['stationary_rhs'] else 'finite_time_') + ('full' if full else 'other')

def self_tests(out, star):
    m = Field(star, 18, 4); big = Field(star, 28, 6)
    rng = np.random.default_rng(91)
    y = m.fft(rng.normal(size=m.shape)) * m.mask; y *= .15 / np.sqrt(np.sum(m.weight * abs(y) ** 2))
    N, E = m.evaluate(y)
    coef = m.coefficients(y, m.compactK); yb = big.from_compact(m.compactK, coef); Nb, Eb = big.evaluate(yb)
    mu = m.L * y + N; d = m.fft(rng.normal(size=m.shape)) * m.mask
    d /= np.sqrt(np.sum(m.weight * abs(d) ** 2)); eps = 1e-6
    fd = (m.evaluate(y + eps * d)[1] - m.evaluate(y - eps * d)[1]) / (2 * eps)
    grad = float(np.real(np.sum(m.weight * np.conj(mu) * d)))
    S = STARS[star]
    A = (8 * P['beta'] + np.sqrt((8 * P['beta']) ** 2 - 4 * 141 * P['alpha'])) / 282 if star == "D4" \
        else (6 * P['beta'] + np.sqrt((6 * P['beta']) ** 2 - 4 * 93 * P['alpha'])) / 186
    a = np.full(S["N"], A, complex); sy = m.from_compact(m.star_n, a); Ns, Es = m.evaluate(sy)
    frhs = m.coefficients(-m.k2 * (m.L * sy + Ns)); trhs = trunc_rhs(0, a, star)
    # FFT route vs enumeration route at a random complex star state that
    # satisfies the reality condition a_{-k} = a_k^* (taken as the star
    # projection of a random real field; an unconstrained complex vector
    # is not a real field and from_compact would symmetrise it).
    rng2 = np.random.default_rng(1234)
    yrand = m.fft(rng2.normal(size=m.shape)) * m.mask
    arand = m.coefficients(yrand) * 0.05
    fft_vs_enum = float(np.max(abs(trunc_rhs_fft(0, arand, star, m) - trunc_rhs(0, arand, star))))
    x = m.real(y); Nreal = -P['beta'] * x * x + P['v'] * x * x * x
    rhs = m.real(-m.k2 * (m.L * y + N)); Lreal = m.real(m.L * y)
    diss_direct = float(np.mean((Lreal + Nreal) * rhs))
    diss_spectral = float(-np.sum(m.weight * m.k2 * abs(mu) ** 2))
    yl = m.from_compact(m.star_n, a * 1e-7)
    yf, _, _, _, _ = integrate(m, yl, .05, 1.)
    expected = yl * np.exp(-8 * P['alpha'])
    linear_error = float(np.linalg.norm(yf - expected) / np.linalg.norm(expected))
    tests = dict(dealias_energy_18_vs_28_same_K4=abs(E - Eb),
        dealias_projected_nonlinearity_max=float(np.max(abs(m.coefficients(N, m.compactK) - big.coefficients(Nb, m.compactK)))),
        energy_gradient_fd_absolute_error=abs(fd - grad),
        dissipation_identity_absolute_error=abs(diss_direct - diss_spectral),
        shell_rhs_vs_exact_truncation_max=float(np.max(abs(frhs - trhs))),
        fft_trunc_rhs_vs_enumeration_max=fft_vs_enum,
        shell_energy_vs_exact_truncation=float(abs(Es - trunc_energy(a, star, m))),
        linear_decay_relative_error=linear_error, unordered_triads=len(S["triads"]),
        analytic_amplitude=float(A), matched_rms=float(np.sqrt(24) * 0.07757529634),
        star_N=S["N"], star_T=S["T"], star_Q=S["Q"])
    assert tests['dealias_energy_18_vs_28_same_K4'] < 1e-10
    assert tests['dealias_projected_nonlinearity_max'] < 1e-12
    assert tests['energy_gradient_fd_absolute_error'] < 1e-7
    # Dissipation identity is checked RELATIVELY: on the A4* cell the
    # dissipation magnitude is ~1e11, so an absolute 1e-8 bound is meaningless.
    assert abs(diss_direct - diss_spectral) / max(abs(diss_spectral), 1e-30) < 1e-9
    assert tests['shell_rhs_vs_exact_truncation_max'] < 1e-12
    assert tests['fft_trunc_rhs_vs_enumeration_max'] < 1e-12
    assert tests['shell_energy_vs_exact_truncation'] < 1e-12
    assert linear_error < 1e-5
    dump(out / 'numerical_tests.json', tests)
    return tests

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--star', required=True, choices=['D4', 'A4star'])
    ap.add_argument('--replicates', type=int, default=3)
    ap.add_argument('--t-final', type=float, default=200.)
    ap.add_argument('--dt', type=float, default=.1)
    ap.add_argument('--validation', action='store_true')
    args = ap.parse_args()
    load_stars()
    out = OUTROOT / args.star.lower()
    out.mkdir(parents=True, exist_ok=True)
    P.update(replicates=args.replicates, t_final=args.t_final, dt=args.dt)
    tests = self_tests(out, args.star)
    print('SELFTESTS ' + args.star + ' ' + json.dumps(tests), flush=True)
    m = Field(args.star, P['n'], P['cutoff'])
    manifest = dict(**P, star=args.star, M_matrix=STARS[args.star]["M"].tolist(),
        star_N=STARS[args.star]["N"], star_T=STARS[args.star]["T"], star_Q=STARS[args.star]["Q"],
        star_triads=len(STARS[args.star]["triads"]),
        cell="cubic [0,2pi]^4, reciprocal Z^4" if args.star == "D4" else
              "oblique torus dual to A4 simple-root lattice (M columns = 2*(e_j-e_{j+1}) Helmert)",
        matched_rms=float(np.sqrt(24) * 0.07757529634), weak_rms=.05,
        pattern_noise={'six': .01, 'twelve': .01, 'full': .25},
        model='Periodic 4D conserved Model B Fourier Galerkin field on native cell, not a star restriction',
        fft_grid_points=P['n'] ** 4, real_galerkin_dof=int(np.sum(m.weight[m.mask])),
        retained_rfft_points=int(m.mask.sum()),
        dealias='Sharp tensor |n_i|<=K in lattice coords AND physical |k|^2<=64; N>4K. Exact projected cubic and quartic energy quadrature.',
        integrator='Second-order exponential Heun ETD2; exact dissipative linear propagator; nonlinear explicit, step energy rejection',
        startup_caps='dt/1000 until t=.02; dt/20 until t=.2; dt thereafter',
        energy_acceptance='F_new <= F_old + 2e-13 + 2e-12*abs(F_old); halve failing step, no unconditional stability claim',
        initialization='Dealiased real iid Gaussian field in lattice coords, normalized modulation RMS; same random direction for weak/matched and pattern noise per replicate',
        phase_lock='Weighted signed Re(sum triad products)/sum abs(triad products), unordered star triads',
        stationarity='L2 spatial RMS of projected dphi/dt <= 1e-7; not a stability proof',
        refinement_requested=args.validation,
        python=platform.python_version(), numpy=np.__version__, scipy=scipy.__version__,
        platform=platform.platform(),
        script_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest())
    dump(out / 'parameters.json', manifest)
    traces = []; outcomes = []; traces_trunc = []; seeds = []
    start = time.perf_counter(); all_times = []; shells = []; spectra = []; runids = []
    for family in FAMILIES:
        for rep in range(args.replicates):
            rid = f'{family}_{rep:02d}'; path = out / (rid + '.npz')
            y0, seed = make_initial(m, family, rep); tick = time.perf_counter()
            if path.exists():
                z = np.load(path, allow_pickle=False)
                yf = m.from_compact(z['wavevectors'], z['final_coefficients'])
                rows = json.loads(str(z['rows_json'])); sh = z['shell_coefficients']
                sp = z['power_by_k_squared']; stats = json.loads(str(z['stats_json']))
                elapsed = stats['elapsed_seconds']
            else:
                yf, rows, sh, sp, stats = integrate(m, y0, args.dt, args.t_final)
                elapsed = time.perf_counter() - tick; stats['elapsed_seconds'] = elapsed
                np.savez_compressed(path, wavevectors=m.compactK,
                    initial_coefficients=m.coefficients(y0, m.compactK),
                    final_coefficients=m.coefficients(yf, m.compactK),
                    times=np.array([r['time'] for r in rows]), shell_coefficients=sh,
                    power_by_k_squared=sp, rows_json=json.dumps(rows), stats_json=json.dumps(stats))
            times = np.array([r['time'] for r in rows])
            # truncated comparison from the field's actual initial shell projection
            a0 = m.coefficients(y0)
            sol = solve_ivp(trunc_rhs_fft, (0, float(times[-1])), a0, args=(args.star, m),
                            method='DOP853', t_eval=times, rtol=2e-10, atol=2e-12, max_step=.5)
            assert sol.success
            tr = []
            for j, t in enumerate(times):
                dd = trunc_diagnostics(sol.y[:, j], args.star)
                # truncated RHS rms: use trunc_rhs norm as stationarity proxy
                rr = trunc_rhs_fft(t, sol.y[:, j], args.star, m)
                tr.append(dict(time=float(t), occupancy=dd['occupancy'], amplitude_cv=dd['amplitude_cv'],
                               triad_lock=dd['triad_lock'], modulation_power=dd['modulation_power'],
                               excess_energy=trunc_energy(sol.y[:, j], args.star, m),
                               rhs_rms=float(np.sqrt(np.sum(abs(rr) ** 2)))))
            for r in rows: traces.append(dict(run_id=rid, family=family, replicate=rep, **r))
            for r in tr: traces_trunc.append(dict(run_id=rid, family=family, replicate=rep, **r))
            result = dict(run_id=rid, family=family, replicate=rep, seed=seed,
                outcome=outcome(rows[-1], args.star),
                truncated_outcome=outcome({**tr[-1], 'rhs_rms': tr[-1]['rhs_rms']}, args.star) if False else
                    ('uniform' if tr[-1]['modulation_power'] < P['uniform_power'] else
                     'stationary_full' if (tr[-1]['occupancy'] == STARS[args.star]["N"] and tr[-1]['amplitude_cv'] is not None and tr[-1]['amplitude_cv'] <= P['cv_max'] and tr[-1]['triad_lock'] is not None and tr[-1]['triad_lock'] >= P['locking_min'] and tr[-1]['rhs_rms'] <= 1e-7) else 'finite_time_other'),
                initial_rms=rows[0]['modulation_rms'], initial_shell_fraction=rows[0]['shell_fraction'],
                initial_energy=rows[0]['excess_energy'],
                **rows[-1], **stats, truncated_final_energy=tr[-1]['excess_energy'],
                truncated_final_power=tr[-1]['modulation_power'], truncated_final_occupancy=tr[-1]['occupancy'])
            outcomes.append(result)
            seeds.append(dict(run_id=rid, replicate=rep, seed=seed, initial_state_file=path.name))
            all_times.append(times); shells.append(sh); spectra.append(sp); runids.append(rid)
            csvwrite(out / 'field_outcomes.csv', outcomes)
            csvwrite(out / 'field_trajectories.csv', traces)
            csvwrite(out / 'truncated_trajectories.csv', traces_trunc)
            print(json.dumps({k: result[k] for k in ['run_id', 'outcome', 'truncated_outcome', 'occupancy', 'excess_energy', 'rhs_rms', 'shell_fraction', 'elapsed_seconds', 'rejected_steps']}), flush=True)
    np.savez_compressed(out / 'spectral_trajectories.npz', run_ids=np.array(runids),
        times=np.array(all_times), star_wavevectors=m.star_n, shell_coefficients=np.array(shells),
        power_by_k_squared=np.array(spectra))
    dump(out / 'seed_manifest.json', seeds)
    summary = []
    for family in FAMILIES:
        rr = [r for r in outcomes if r['family'] == family]
        summary.append(dict(family=family, n=len(rr),
            uniform=sum(r['outcome'] == 'uniform' for r in rr),
            stationary_full=sum(r['outcome'] == 'stationary_full' for r in rr),
            finite_time_full=sum(r['outcome'] == 'finite_time_full' for r in rr),
            other=sum(r['outcome'].endswith('other') for r in rr),
            truncated_full=sum('full' in str(r['truncated_outcome']) for r in rr),
            energy_min=min(r['excess_energy'] for r in rr), energy_max=max(r['excess_energy'] for r in rr),
            max_rhs_rms=max(r['rhs_rms'] for r in rr)))
    csvwrite(out / 'field_summary.csv', summary)
    refinements = []
    if args.validation:
        for family in ['random_full_matched', 'six_1pct_full_noise', 'full_25pct_full_noise']:
            rid = f'{family}_00'
            z = np.load(out / (rid + '.npz')); base = next(r for r in outcomes if r['run_id'] == rid)
            for label, n, cut, dt in [('half_dt', 18, 4, args.dt / 2), ('spatial_K6', 28, 6, args.dt)]:
                mr = Field(args.star, n, cut)
                yi = mr.from_compact(z['wavevectors'], z['initial_coefficients'])
                tick = time.perf_counter()
                statepath = out / f'check_{label}_{rid}.npz'
                if statepath.exists():
                    zz = np.load(statepath)
                    yf = mr.from_compact(zz['wavevectors'], zz['final_coefficients'])
                    rows = json.loads(str(zz['rows_json'])); sh = zz['shell_coefficients']
                    sp = zz['power_by_k_squared']; stats = json.loads(str(zz['stats_json']))
                else:
                    yf, rows, sh, sp, stats = integrate(mr, yi, dt, args.t_final)
                    stats['elapsed_seconds'] = time.perf_counter() - tick
                    np.savez_compressed(statepath, wavevectors=mr.compactK,
                        initial_coefficients=mr.coefficients(yi, mr.compactK),
                        final_coefficients=mr.coefficients(yf, mr.compactK),
                        times=[r['time'] for r in rows], shell_coefficients=sh,
                        power_by_k_squared=sp, rows_json=json.dumps(rows), stats_json=json.dumps(stats))
                common = mr.coefficients(yf, z['wavevectors']); ref = z['final_coefficients']
                initialnorm = np.linalg.norm(z['initial_coefficients'])
                reference_rows = json.loads(str(z['rows_json']))
                path_shell_error = np.linalg.norm(sh - z['shell_coefficients'], axis=1)
                path_energy_error = np.array([r['excess_energy'] for r in rows]) - np.array([r['excess_energy'] for r in reference_rows])
                ck = mr.compactK; ac = mr.coefficients(yf, ck)
                newpower = float(np.sum(abs(ac[np.max(abs(ck), axis=1) > 4]) ** 2))
                row = dict(run_id=rid, check=label, n=n, cutoff=cut, dt=dt, **rows[-1],
                    outcome=outcome(rows[-1], args.star),
                    energy_difference_vs_main=rows[-1]['excess_energy'] - base['excess_energy'],
                    relative_common_coefficient_error=float(np.linalg.norm(common - ref) / max(np.linalg.norm(ref), 1e-12)),
                    initial_norm_scaled_coefficient_error=float(np.linalg.norm(common - ref) / initialnorm),
                    newly_admitted_power=newpower,
                    max_trajectory_shell_error_over_initial_norm=float(path_shell_error.max() / initialnorm),
                    max_trajectory_energy_absolute_difference=float(abs(path_energy_error).max()),
                    max_trajectory_energy_difference_after_t1=float(abs(path_energy_error[np.array([r['time'] for r in rows]) >= 1]).max()), **stats)
                refinements.append(row); csvwrite(out / 'refinement_outcomes.csv', refinements)
                csvwrite(out / f'check_{label}_{rid}_trajectory.csv', rows)
                print('REFINE ' + json.dumps({k: row[k] for k in ['run_id', 'check', 'outcome', 'excess_energy', 'energy_difference_vs_main', 'relative_common_coefficient_error', 'elapsed_seconds']}), flush=True)
    manifest.update(total_elapsed_this_invocation=time.perf_counter() - start,
        total_main_solver_seconds=sum(r['elapsed_seconds'] for r in outcomes),
        refinements_completed=len(refinements), main_runs_completed=len(outcomes),
        process_peak_rss_MiB=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1024,
        max_observed_mean_error=max(r['mean_error'] for r in traces),
        max_main_step_energy_increase=max(r['max_step_energy_increase'] for r in outcomes),
        main_rejected_steps=sum(r['rejected_steps'] for r in outcomes))
    dump(out / 'parameters.json', manifest)
    print('COMPLETED ' + args.star + ' ' + json.dumps(manifest), flush=True)

if __name__ == '__main__':
    main()
