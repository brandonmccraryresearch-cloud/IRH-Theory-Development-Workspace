"""Shared D4 model module for workstream A (core computations).

Grounding (all parameters from the manuscript / repo verification code, nothing
invented):
  - Manuscript: IRH_v93_1_source_rebuilt.txt (v93.1), esp. Part II.
  - Repo verification: ~/workspace/research/IRH-Theory-Development-Workspace/
    verification/{verify_claims.py, sim6_units.py, sim7_fairtest.py}.
  - Free energy: F[psi] = int d^4x [ 1/2 psi (r + (q0^2 + nabla^2)^2) psi
    - (u/3) psi^3 + (v/4) psi^4 ], r = -0.35, u = v = 1.
  - D4 shell (scaled): {(+-2,+-2,0,0) and perms}, 24 modes, |k|^2 = 8.
    T = 192 ordered triads, Q = 3384 ordered quadruples (verify_claims.py).
  - One-mode Landau functional (verify_claims.py, checked against the
    manuscript's Fmod up to the pdftotext "N/2" -> "N2" layout artefact):
        F_mod(A) = (N/2) r_eff A^2 - (T/3) u_eff A^3 + (v Q/4) A^4
                   (+ (w6 H/6) A^6 when sixth-order terms are included)
        r_eff = r - 2 u psibar + 3 v psibar^2
        u_eff = u - 3 v psibar
    with N = 24, T = 192, Q = 3384, H = 911040 (manuscript §II.7; H is
    verified in checks/check_model.py by two independent exact routes).
  - Model B dynamics: sim6_units.py semi-implicit spectral scheme,
    L = pi, q0^2 = 8.0, N = 16, dt = 0.005 (attractor run).

Every function that returns a load-bearing number is checked in
checks/check_model.py with a quoted tool verdict.
"""

import itertools
import math

import numpy as np

# ---------------------------------------------------------------- parameters
R = -0.35          # quench depth (bare), manuscript §II.6/II.7
U = 1.0            # cubic coupling
V = 1.0            # quartic coupling
Q0SQ_TUNED = 8.0   # q0^2 tuned onto the D4 shell, §II.7
Q0SQ_SIM7 = 7.5    # q0^2 in the sim7 fair test, §II.6
PSIBAR = -0.18     # baseline tension, §II.7/II.8
A_STAR = 0.0776    # ordered-branch amplitude at (psibar, r) = (-0.18, -0.35)
GAMMA = 1.2        # damping, §II.6
N_MODES = 24
T_TRIADS = 192
Q_QUADS = 3384
H_SEXTIC = 911040  # manuscript §II.7; verified in checks/check_model.py

# ---------------------------------------------------------------- roots
def d4_roots(unscaled=True):
    """The 24 D4 roots +-e_i +- e_j. Unscaled: |a|^2 = 2; scaled (x2):
    |g|^2 = 8, the reciprocal-shell vectors of §II.6."""
    v = []
    for i, j in itertools.combinations(range(4), 2):
        for s1, s2 in itertools.product([1, -1], repeat=2):
            a = [0] * 4
            a[i] = s1
            a[j] = s2
            v.append(tuple(a))
    assert len(v) == 24
    if not unscaled:
        v = [tuple(2 * x for x in a) for a in v]
    return v

ROOTS = d4_roots(unscaled=True)    # |a|^2 = 2
SHELL = d4_roots(unscaled=False)   # |g|^2 = 8

# ---------------------------------------------------------------- exact counts
def count_tuples_bruteforce(vectors, k):
    """Number of ordered k-tuples of `vectors` summing to zero, by direct
    enumeration. Exact integer. Feasible for k <= 4 (24^4 = 331776)."""
    n = 0
    arr = np.array(vectors, dtype=int)
    for tup in itertools.product(range(len(vectors)), repeat=k):
        if not arr[list(tup)].sum(axis=0).any():
            n += 1
    return n

def triple_sum_counts(vectors):
    """dict: vector sum -> number of ordered triples of `vectors` with that
    sum. Exact integer; 24^3 = 13824 triples."""
    counts = {}
    for a, b, c in itertools.product(vectors, repeat=3):
        s = (a[0] + b[0] + c[0], a[1] + b[1] + c[1],
             a[2] + b[2] + c[2], a[3] + b[3] + c[3])
        counts[s] = counts.get(s, 0) + 1
    return counts

def count_tuples_via_triples(vectors):
    """Number of ordered 6-tuples summing to zero, as
    H = sum_v n3(v) * n3(-v) where n3(v) counts ordered triples summing to v.
    Exact integer, independent of any FFT route. (The n3(v)^2 form is only
    valid for negation-closed sets; tri3 is not, so the product form is
    used.)"""
    n3 = triple_sum_counts(vectors)
    neg = lambda v: (-v[0], -v[1], -v[2], -v[3])
    return sum(n * n3.get(neg(v), 0) for v, n in n3.items())

def count_tuples_via_fft(vectors, k=6, half=12):
    """Number of ordered k-tuples summing to zero via FFT convolution of the
    root indicator on a [-half, half]^4 grid. Exact integer after rounding
    (values are small integers; FFT rounding error << 0.5 is asserted by the
    caller comparing against the triples route). half must cover the
    k-fold sum range: components in [-2,2] summed k times need half >= 2k
    (12 for k = 6); a smaller grid aliases by wraparound."""
    size = 2 * half + 1
    f = np.zeros((size,) * 4, dtype=float)
    for g in vectors:
        f[tuple(x + half for x in g)] = 1.0
    F = np.fft.fftn(f)
    conv = np.fft.ifftn(F ** k).real
    # The indicator is shifted by `half` per factor, so the zero-sum
    # coefficient sits at shifted index (k*half) mod size in each axis.
    idx = (k * half) % size
    return int(round(conv[(idx,) * 4]))

def shell_stats(vectors):
    """(N, T, Q, H) for a set of shell vectors: mode count, ordered triads,
    ordered quadruples, ordered sextuples summing to zero (all exact)."""
    n = len(vectors)
    t = count_tuples_bruteforce(vectors, 3)
    q = count_tuples_bruteforce(vectors, 4)
    h = count_tuples_via_triples(vectors)
    return n, t, q, h

# ---------------------------------------------------------------- moments
def moment(kvec, order):
    """sum_alpha (k . alpha)^order over the 24 unscaled roots. Exact float
    (integer-valued for integer k)."""
    k = np.asarray(kvec, dtype=float)
    dots = np.array(ROOTS, dtype=float) @ k
    return float((dots ** order).sum())

# ---------------------------------------------------------------- Landau functional
def r_eff(psibar, r=R, u=U, v=V):
    return r - 2 * u * psibar + 3 * v * psibar ** 2

def u_eff(psibar, u=U, v=V):
    return u - 3 * v * psibar

def f_mod(A, psibar, r=R, w6=0.0, n=N_MODES, T=T_TRIADS, Q=Q_QUADS,
          H=H_SEXTIC, u=U, v=V):
    """One-mode Landau free energy (excess over uniform state) for a pattern
    with n modes, T triads, Q quadruples, H sextuples. The w6 term uses the
    manuscript's sextic normalisation (w6*H/6) A^6; its corroboration is
    task 3 (band narrowing 11.90% -> 8.47% at w6 = 0.2)."""
    re = r_eff(psibar, r, u, v)
    ue = u_eff(psibar, u, v)
    return (n / 2 * re * A ** 2 - T / 3 * ue * A ** 3 + v * Q / 4 * A ** 4
            + w6 * H / 6 * A ** 6)

def stationary_minimum(psibar, r=R, w6=0.0, n=N_MODES, T=T_TRIADS, Q=Q_QUADS,
                       H=H_SEXTIC, u=U, v=V):
    """Minimise f_mod over A >= 0. Returns (A_min, F_min, exists) where
    exists is False when the only stationary point is A = 0 (no ordered
    branch). The derivative is a cubic in A; all real roots >= 0 are tested
    exactly via numpy roots, plus the A = 0 endpoint."""
    re = r_eff(psibar, r, u, v)
    ue = u_eff(psibar, u, v)
    # dF/dA = n*re*A - T*ue*A^2 + v*Q*A^3 + w6*H*A^5
    if w6 == 0.0:
        coeff = [v * Q, -T * ue, n * re, 0.0]  # highest power first
    else:
        coeff = [w6 * H, 0.0, v * Q, -T * ue, n * re, 0.0]
    roots = np.roots(coeff)
    cands = [0.0]
    for rt in roots:
        if abs(rt.imag) < 1e-8 and rt.real >= 0.0:
            cands.append(float(rt.real))
    vals = [(a, f_mod(a, psibar, r, w6, n, T, Q, H, u, v)) for a in cands]
    a_min, f_min = min(vals, key=lambda t: t[1])
    exists = a_min > 0.0 and f_min < 0.0
    return a_min, f_min, exists

# ---------------------------------------------------------------- sub-patterns
def hexagon_6():
    """The A2 hexagonal 6-mode sub-pattern of §II.7: +-a, +-b, +-(a+b) with
    a = (2,2,0,0), b = (0,-2,2,0). All six lie in one plane, mutual angles
    60/120 degrees."""
    a = (2, 2, 0, 0)
    b = (0, -2, 2, 0)
    c = (a[0] + b[0], a[1] + b[1], a[2] + b[2], a[3] + b[3])
    vs = [a, b, c, tuple(-x for x in a), tuple(-x for x in b),
          tuple(-x for x in c)]
    assert len(set(vs)) == 6 and all(v in SHELL for v in vs)
    return vs

def fcc_slice_12():
    """The 12 shell modes with x4 = 0 (the §II.10 FCC cross-section modes)."""
    return [g for g in SHELL if g[3] == 0]

def square_4():
    """The 4 shell modes in the (x1,x2) plane."""
    return [g for g in SHELL if g[2] == 0 and g[3] == 0]

def triad_3():
    """One closed triad: (2,2,0,0), (-2,0,2,0), (0,-2,-2,0) sums to zero."""
    vs = [(2, 2, 0, 0), (-2, 0, 2, 0), (0, -2, -2, 0)]
    assert sum(np.array(vs)) .tolist() == [0, 0, 0, 0]
    return vs

def eight_2sq():
    """8 modes: the (x1,x2)-plane square plus the (x3,x4)-plane square."""
    return [g for g in SHELL if (g[2] == 0 and g[3] == 0)
            or (g[0] == 0 and g[1] == 0)]

SUBPATTERNS = {
    "full24": SHELL,
    "hex6": hexagon_6(),
    "fcc12": fcc_slice_12(),
    "sq4": square_4(),
    "tri3": triad_3(),
    "sq8": eight_2sq(),
}

# Unscaled-root labels of the same sub-patterns, for Fourier-space seeding
# (seed_subset expects root labels n with physical k = (2*pi/L) n).
SUBPATTERN_LABELS = {
    name: [tuple(x // 2 for x in g) for g in vs]
    for name, vs in SUBPATTERNS.items()
}

# ---------------------------------------------------------------- Model B dynamics
# Semi-implicit spectral scheme of verification/sim6_units.py (L = pi,
# q0^2 = 8.0, N = 16). psi_hat is the Fourier transform with the numpy
# convention (no 1/N^4 in fftn); physical field psi = ifftn(psi_hat).real.
class ModelB:
    def __init__(self, N=16, L=math.pi, q02=Q0SQ_TUNED, r=R, u=U, v=V,
                 dt=0.005):
        self.N, self.L, self.q02, self.r, self.u, self.v, self.dt = (
            N, L, q02, r, u, v, dt)
        X = np.fft.fftfreq(N, d=L / N) * 2 * math.pi
        KX, KY, KZ, KW = np.meshgrid(X, X, X, X, indexing='ij')
        self.K2 = KX ** 2 + KY ** 2 + KZ ** 2 + KW ** 2
        self.omega2 = r + (q02 - self.K2) ** 2
        self.den = 1.0 + dt * self.K2 * self.omega2
        self.filt = (self.K2 < 200).astype(float)
        self.gidx = lambda n: tuple(x % N for x in n)

    def step(self, ph):
        p = np.fft.ifftn(ph).real
        nl = self.filt * (self.u * np.fft.fftn(p * p)
                          - self.v * np.fft.fftn(p * p * p))
        ph_new = (ph + self.dt * self.K2 * nl) / self.den
        # Enforce Hermitian symmetry (reality of the field) every step.
        # The nonlinearity is evaluated on the real part only, so the
        # anti-Hermitian (non-real) component of ph receives no nonlinear
        # stabilisation and grows at the bare shell rate 1/den ~ 1.014/step
        # from roundoff seeds: a droplet run left unsymmetrised reaches
        # NaN by ~6000 steps (anti-Hermitian shell modes ~128 by step
        # 2500, growing x1.0142/step, while the real field decays
        # cleanly). Symmetrising resets it to roundoff each step.
        # Index map: mode -g sits at (-g) mod N = reverse-then-roll-by-1.
        rev = np.roll(ph_new[::-1, ::-1, ::-1, ::-1], 1, axis=(0, 1, 2, 3))
        return 0.5 * (ph_new + np.conj(rev))

    def free_energy(self, ph):
        p = np.fft.ifftn(ph).real
        quad = 0.5 * np.sum(
            np.fft.ifftn(self.omega2 * ph).real * p) / self.N ** 4
        return quad + np.mean(-self.u / 3 * p ** 3 + self.v / 4 * p ** 4)

    def analyze(self, ph):
        """(psibar, mean|A| over shell, D4 shell power fraction, dominant
        mode count, triad phase locking <cos S> over active triads, rms
        modulation, F excess).
        Fourier indices are the UNSCALED root labels n = (+-1,+-1,0,0):
        physical k = (2*pi/L) n, so with L = pi the shell sits at |k|^2 = 8.
        (d4 is 0.0 when there is no non-zero-mode power at all.)"""
        amps = np.array([ph[self.gidx(n)] / self.N ** 4 for n in ROOTS])
        mag = np.abs(amps)
        pha = np.angle(amps)
        p = np.abs(ph) ** 2
        pnz = p.sum() - p[0, 0, 0, 0]
        d4 = float((mag ** 2).sum() / (pnz / self.N ** 8)) if pnz > 0 else 0.0
        ndom = int((mag > 0.5 * mag.max()).sum()) if mag.max() > 0 else 0
        triads = []
        vset = set(ROOTS)
        for ia, ib in itertools.combinations(range(24), 2):
            need = tuple(-ROOTS[ia][d] - ROOTS[ib][d] for d in range(4))
            if need in vset:
                ic = ROOTS.index(need)
                if ic > ib:
                    triads.append((ia, ib, ic))
        S = np.array([pha[a] + pha[b] + pha[c] for a, b, c in triads])
        # Run-12 fix (EXP-1200 R-CODE, gap G-B3; Hark F2): the shipped metric
        # averaged cos S over all 32 triads, including modes at roundoff
        # amplitude whose phases are noise, so it was platform-dependent for
        # partial patterns (hex6 0.304 / WS-C A5 0.455 vs shipped 1.000).
        # `lock` is now the mean over ACTIVE triads only: all three modes
        # active, with "active" = the same criterion as ndom
        # (mag > 0.5 * mag.max()). For the full 24-mode pattern every triad
        # is active and the value is unchanged. The old all-triad value is
        # kept as `lock_all`; `n_lock_triads` is the number of active triads.
        lock_all = float(np.mean(np.cos(S))) if len(S) else float('nan')
        active = (mag > 0.5 * mag.max()) if mag.max() > 0 else \
            np.zeros(len(mag), bool)
        act = [k for k, (a, b, c) in enumerate(triads)
               if active[a] and active[b] and active[c]]
        lock = float(np.mean(np.cos(S[act]))) if act else float('nan')
        pb = float(ph[0, 0, 0, 0].real / self.N ** 4)
        fld = np.fft.ifftn(ph).real
        rms = float(np.sqrt(((fld - fld.mean()) ** 2).mean()))
        F = self.free_energy(ph)
        pu = np.zeros_like(ph)
        pu[0, 0, 0, 0] = ph[0, 0, 0, 0]
        return dict(psibar=pb, amp=float(mag.mean()), d4=d4, ndom=ndom,
                    lock=lock, lock_all=lock_all, n_lock_triads=len(act),
                    rms=rms, Fexc=F - self.free_energy(pu),
                    mags=mag, phases=pha)

    def seed_full(self, psibar=PSIBAR, amp=A_STAR, phases=None):
        # Fourier labels are the unscaled roots; physical k = (2*pi/L) n.
        ph = np.zeros((self.N,) * 4, complex)
        ph[0, 0, 0, 0] = psibar * self.N ** 4
        for i, n in enumerate(ROOTS):
            ph[self.gidx(n)] = amp * self.N ** 4 * (
                1.0 if phases is None else np.exp(1j * phases[i]))
        return ph

    def seed_subset(self, modes, psibar=PSIBAR, amp=A_STAR, phases=None):
        # `modes` are unscaled-root labels (same convention as seed_full).
        ph = np.zeros((self.N,) * 4, complex)
        ph[0, 0, 0, 0] = psibar * self.N ** 4
        for i, n in enumerate(modes):
            ph[self.gidx(n)] = amp * self.N ** 4 * (
                1.0 if phases is None else np.exp(1j * phases[i]))
        return ph

    def seed_noise(self, psibar=PSIBAR, amp=0.05, seed=0):
        rng = np.random.default_rng(seed)
        psi = amp * rng.standard_normal((self.N,) * 4)
        psi -= psi.mean()
        psi += psibar
        return np.fft.fftn(psi)

    def seed_droplet(self, radius, amp=A_STAR, psibar=PSIBAR, sharp=4.0):
        """Uniform background psibar with a D4-ordered ball of radius `radius`
        (in box units, L = pi) and per-mode amplitude `amp`, with a smooth
        tanh envelope of width 1/sharp. Returned field is real-space psi."""
        n = self.N
        xs = np.linspace(0, self.L, n, endpoint=False)
        X1, X2, X3, X4 = np.meshgrid(xs, xs, xs, xs, indexing='ij')
        # distance from box centre (periodic: centre at L/2)
        d2 = ((X1 - self.L / 2) ** 2 + (X2 - self.L / 2) ** 2
              + (X3 - self.L / 2) ** 2 + (X4 - self.L / 2) ** 2)
        env = 0.5 * (1.0 - np.tanh(sharp * (np.sqrt(d2) - radius)))
        pattern = np.zeros_like(X1)
        for g in SHELL:
            pattern += np.cos(g[0] * X1 + g[1] * X2 + g[2] * X3 + g[3] * X4)
        psi = psibar + amp * env * pattern
        # restore the exact mean (Model B conserves it; start on-spec)
        psi += (psibar - psi.mean())
        return np.fft.fftn(psi)

# ---------------------------------------------------------------- projections
def d4_lattice_points(Rmax):
    """All D4 lattice points (integer 4-vectors with even coordinate sum)
    with |x| <= Rmax."""
    m = int(math.ceil(Rmax))
    pts = []
    for x in itertools.product(range(-m, m + 1), repeat=4):
        if sum(x) % 2 == 0 and sum(c * c for c in x) <= Rmax ** 2 + 1e-9:
            pts.append(np.array(x, dtype=float))
    return np.array(pts)

def project_points(pts, nhat):
    """Orthogonal projection of points onto the hyperplane nhat^perp.
    Returns (projected 3D coords in an orthonormal basis of the hyperplane,
    the basis)."""
    n = np.asarray(nhat, dtype=float)
    n = n / np.linalg.norm(n)
    # orthonormal basis of n^perp via QR of a matrix with n as first column
    A = np.eye(4)
    A[:, 0] = n
    Q, _ = np.linalg.qr(A)
    # Q[:,0] is parallel to n; basis is Q[:,1:]
    basis = Q[:, 1:]
    proj = pts @ basis  # (M,3): coordinates in the hyperplane basis
    return proj, basis

def structure_factor(proj, qgrid):
    """S(q) = |sum_j exp(i q.x_j)|^2 / M on a (...,3) grid of q vectors."""
    M = len(proj)
    S = np.zeros(qgrid.shape[:-1])
    it = np.nditer(S, flags=['multi_index'])
    while not it.finished:
        q = qgrid[it.multi_index]
        S[it.multi_index] = abs(np.exp(1j * (proj @ q)).sum()) ** 2 / M
        it.iternext()
    return S
