"""Shared model code for WS-C (substrate selection models + D4 convergence).

Reference implementation: repo verification/sim6_units.py (Model B / Model A
semi-implicit attractor; RK4 damped-wave quench) and sim7_fairtest.py
(semi-implicit damped wave). This module generalizes those integrators over
(N, L, q0^2, r, u, v, gamma, dt, steps, psi-bar, seed) WITHOUT changing the
discretization: same filters (K2<200 attractor, K2<64 quench), same schemes,
same diagnostics (analyze() is a verbatim port of sim6's).

Manuscript: IRH v93.1 source rebuild. Dynamics (Sec I.2):
    psi_tt + gamma psi_t = -dF/dpsi,
    F[psi] = int d^4x [ 1/2 psi (r + (q0^2 + nabla^2)^2) psi - u/3 psi^3 + v/4 psi^4 ].
Model B (conserved): psi_t = nabla^2 (dF/dpsi).  Model A: psi_t = -dF/dpsi.
D4 shell: 24 roots (+-1,+-1,0,0) and permutations; scaled shell (+-2,+-2,0,0)
in the L=2*pi box (sim7) and (+-1,+-1,0,0) in the L=pi box (sim6).
"""
import itertools
import math

import numpy as np

# ---------------------------------------------------------------- exact shell combinatorics

def d4_roots():
    """The 24 D4 roots (+-1,+-1,0,0) and permutations, as integer tuples."""
    vecs = []
    for i, j in itertools.combinations(range(4), 2):
        for s1 in (1, -1):
            for s2 in (1, -1):
                n = [0, 0, 0, 0]
                n[i] = s1
                n[j] = s2
                vecs.append(tuple(n))
    assert len(vecs) == 24
    return vecs


def shell_combinatorics(modes):
    """Exact (N, T, Q) for a set of integer mode vectors.

    N = number of modes. T = ordered triples summing to zero (closed triads).
    Q = ordered quadruples summing to zero. Computed by exhaustive enumeration
    over the mode set (exact integers, no floating point).
    """
    modes = list(modes)
    mset = set(modes)
    N = len(modes)
    T = 0
    for a in modes:
        for b in modes:
            need = tuple(-a[d] - b[d] for d in range(4))
            if need in mset:
                T += 1
    Q = 0
    for a in modes:
        for b in modes:
            for c in modes:
                need = tuple(-a[d] - b[d] - c[d] for d in range(4))
                if need in mset:
                    Q += 1
    return N, T, Q


def tau_q4_S(N, T, Q):
    """Selection quantities: tau = T / N**(3/2), q4 = Q / N**2, S = tau^2/q4.

    Returns exact rationals as (Fraction tau^2, Fraction q4, Fraction S)
    using integer arithmetic: tau^2 = T^2 / N^3, q4 = Q / N^2.
    """
    from fractions import Fraction
    tau2 = Fraction(T * T, N ** 3)
    q4 = Fraction(Q, N * N)
    S = tau2 / q4 if q4 else Fraction(0)
    return tau2, q4, S


def one_mode_free_energy(A, N, T, Q, r, u, v, psibar):
    """F_mod/V for the one-mode ansatz (manuscript Sec II.7, II.8).

    F_mod = (N/2) (r - 2 u psibar + 3 v psibar^2) A^2
            - (T/3) (u - 3 v psibar) A^3 + v Q A^4 / 4
    with A the per-mode amplitude. NOTE: `r` here is the SHELL quench depth
    r_shell = r_bare + (q0^2 - 8)^2 (manuscript Sec II.7: the effective quench
    depth includes the shell penalty); at q0^2 = 8.0, r_shell = r_bare.
    The (N/2) coefficient matches Sec II.3's F(B) with B = A sqrt(N) and is
    confirmed by the stationary values (A* = 0.0776, F = -0.00763); the
    pdftotext rendering "N2" is the fraction N/2, not N^2.
    This is the EXCESS over the uniform state (F=0 disordered).
    """
    r_eff = r - 2 * u * psibar + 3 * v * psibar ** 2
    u_eff = u - 3 * v * psibar
    return (N / 2.0 * r_eff * A ** 2
            - (T / 3.0) * u_eff * A ** 3
            + v * Q * A ** 4 / 4.0)


def stationary_amplitude(N, T, Q, r, u, v, psibar):
    """Positive stationary amplitude of the one-mode ansatz (dF/dA = 0, A != 0).

    dF/dA = 0 gives N r_eff A - T u_eff A^2 + v Q A^3 = 0, i.e.
    v Q A^2 - T u_eff A + N r_eff = 0. Returns the larger root if real
    and positive, else None. (The ordered branch.) `r` is the shell quench
    depth r_shell (see one_mode_free_energy).
    """
    r_eff = r - 2 * u * psibar + 3 * v * psibar ** 2
    u_eff = u - 3 * v * psibar
    a, b, c = v * Q, -T * u_eff, N * r_eff
    disc = b * b - 4 * a * c
    if disc < 0:
        return None
    roots = [(-b + math.sqrt(disc)) / (2 * a), (-b - math.sqrt(disc)) / (2 * a)]
    pos = [x for x in roots if x > 0]
    return max(pos) if pos else None


# ---------------------------------------------------------------- spectral grid

class Grid:
    """Spectral grid for a 4D periodic box of side L with N points per side."""

    def __init__(self, N, L):
        self.N = N
        self.L = L
        X = np.fft.fftfreq(N, d=L / N) * 2 * math.pi
        KX, KY, KZ, KW = np.meshgrid(X, X, X, X, indexing='ij')
        self.K2 = KX ** 2 + KY ** 2 + KZ ** 2 + KW ** 2
        self.kfac = (2 * math.pi / L) ** 2  # K2 = kfac * |n|^2

    def gidx(self, n):
        return tuple(x % self.N for x in n)

    def shell_index(self, n2_target):
        """Boolean mask of modes with |n|^2 == n2_target."""
        n2 = np.round(self.K2 / self.kfac).astype(int)
        return n2 == n2_target


# ---------------------------------------------------------------- diagnostics (verbatim port of sim6.analyze)

def make_analyzer(grid, q02, r, u, v, vecs):
    """Return (analyze, free_energy). analyze(psi_hat) -> dict with psibar,
    amp (mean shell |A|), d4 (shell power fraction), modes (count with
    mag > 0.5*max), lock (mean cos of the triad phase sum over ACTIVE triads:
    all three modes with mag > 0.5*mag.max(); nan if none), lock_all (old
    all-32-triad mean, platform-dependent for partial patterns),
    n_lock_triads, rms, Fexc, amp_max, amp_min. (Run-13 EXP-1306 T-L167.)"""
    N = grid.N
    K2 = grid.K2
    omega2 = r + (q02 - K2) ** 2
    vset = set(vecs)
    triads = []
    for ia, ib in itertools.combinations(range(24), 2):
        need = tuple(-vecs[ia][d] - vecs[ib][d] for d in range(4))
        if need in vset:
            ic = vecs.index(need)
            if ic > ib:
                triads.append((ia, ib, ic))

    def free_energy(psi_hat):
        p = np.fft.ifftn(psi_hat).real
        quad = 0.5 * np.sum(np.fft.ifftn(omega2 * psi_hat).real * p) / N ** 4
        return quad + np.mean(-u / 3 * p ** 3 + v / 4 * p ** 4)

    def analyze(psi_hat):
        amps = np.array([psi_hat[grid.gidx(n)] / N ** 4 for n in vecs])
        mag = np.abs(amps)
        pha = np.angle(amps)
        p = np.abs(psi_hat) ** 2
        pnz = p.sum() - p[0, 0, 0, 0]
        d4 = float((mag ** 2).sum() / (pnz / N ** 8)) if pnz > 0 else 0.0
        ndom = int((mag > 0.5 * mag.max()).sum()) if mag.max() > 0 else 0
        S = np.array([pha[a] + pha[b] + pha[c] for a, b, c in triads])
        # Run-13 fix (EXP-1306 T-L167; same defect as WS-A G-B3 / Hark F2,
        # fixed in d4model.analyze at 9dfe0b5): the ported sim6 metric
        # averaged cos S over all 32 closed triads, including triads through
        # modes at roundoff amplitude whose phases are noise, so it was
        # platform-dependent for partial patterns (G-B3 record: hex6 0.304 /
        # WS-C A5 0.455 vs shipped 1.000). `lock` is the mean over ACTIVE
        # triads only: all three modes active, "active" = mag > 0.5 * mag.max() (the same
        # threshold as `modes`). For the full 24-mode pattern every triad is
        # active and the value is unchanged. The old all-triad value is kept
        # as `lock_all`; `n_lock_triads` counts the active triads; no active
        # triad -> lock = nan (as in d4model).
        lock_all = float(np.mean(np.cos(S))) if len(S) else 0.0
        active = (mag > 0.5 * mag.max()) if mag.max() > 0 else \
            np.zeros(len(mag), bool)
        act = [k for k, (a, b, c) in enumerate(triads)
               if active[a] and active[b] and active[c]]
        lock = float(np.mean(np.cos(S[act]))) if act else float('nan')
        pb = float(psi_hat[0, 0, 0, 0].real / N ** 4)
        fld = np.fft.ifftn(psi_hat).real
        rms = float(np.sqrt(((fld - fld.mean()) ** 2).mean()))
        F = free_energy(psi_hat)
        pu = np.zeros_like(psi_hat)
        pu[0, 0, 0, 0] = psi_hat[0, 0, 0, 0]
        Fexc = F - free_energy(pu)
        return dict(psibar=pb, amp=float(mag.mean()), d4=d4, modes=ndom,
                    lock=lock, lock_all=lock_all, n_lock_triads=len(act),
                    rms=rms, Fexc=float(Fexc),
                    amp_max=float(mag.max()), amp_min=float(mag.min()))

    return analyze, free_energy


# ---------------------------------------------------------------- integrators

def run_attractor(N=16, L=math.pi, q02=8.0, r=-0.35, u=1.0, v=1.0,
                  psibar=-0.18, a_star=0.0776, dt=0.005, steps=6000,
                  model='B', seed_vecs=None, hermitian=True):
    """Seeded attractor run (sim6 test_attractor, generalized).

    Seeds all 24 D4 shell modes in phase at amplitude a_star, mean psibar.
    model='B': conserved semi-implicit (den = 1 + dt*K2*omega2, K2 factor
    on the nonlinear term). model='A': non-conserved (den = 1 + dt*omega2).
    Filter K2<200 exactly as in sim6. Returns (final psi_hat, history list
    of analyze() dicts at steps 500/1500/final, grid, analyzer).
    """
    grid = Grid(N, L)
    K2 = grid.K2
    omega2 = r + (q02 - K2) ** 2
    vecs = d4_roots()
    analyze, _ = make_analyzer(grid, q02, r, u, v, vecs)
    ph = np.zeros((N,) * 4, complex)
    ph[0, 0, 0, 0] = psibar * N ** 4
    for n in (seed_vecs if seed_vecs is not None else vecs):
        ph[grid.gidx(n)] = a_star * N ** 4
    den = 1.0 + dt * K2 * omega2
    denA = 1.0 + dt * omega2
    filt = (K2 < 200).astype(float)
    # Hermitian projection (see module docstring note): the exact dynamics
    # preserves Hermiticity (real field), but the semi-implicit update
    # amplifies the anti-Hermitian roundoff sector by 1/den > 1 at the shell
    # (den = 1 + dt*K2*omega2 = 0.986 there), so Im(ph) grows ~1.0142/step
    # from roundoff and eventually overflows (shipped sim6: t=27.5). The
    # projection ph <- fftn(ifftn(ph).real) is an exact no-op in exact
    # arithmetic (fftn of a real field is Hermitian by construction) and
    # removes only the unphysical sector; the physical field (rms, max|psi|,
    # psibar) is unaffected. Enabled by default.
    hist = []
    for step in range(1, steps + 1):
        p = np.fft.ifftn(ph).real
        nl = filt * (u * np.fft.fftn(p * p) - v * np.fft.fftn(p * p * p))
        if model == 'B':
            ph = (ph + dt * K2 * nl) / den
        else:
            ph = (ph + dt * nl) / denA
        if hermitian:
            ph = np.fft.fftn(np.fft.ifftn(ph).real)
        if step in (500, 1500, steps):
            d = analyze(ph)
            d['step'] = step
            d['t'] = step * dt
            hist.append(d)
    return ph, hist, grid, analyze


def run_quench(N=16, L=math.pi, q02=8.0, r=-0.35, u=1.0, v=1.0, gamma=1.0,
               dt=0.02, steps=2500, seed=1, psibar=0.0, noise=1e-2):
    """Noise quench with the RK4 damped-wave equation (sim6 test_quench).

    psi_tt + gamma psi_t = -omega2 psi + NL, NL = u psi^2 - v psi^3 (spectral).
    Filter K2<64 exactly as in sim6 (RK4 stability: dt*w < 2.8).
    Initial field: psibar + noise (noise std `noise`, zero mean after removal).
    Returns (final psi_hat, analyze() dict, grid).
    """
    grid = Grid(N, L)
    K2 = grid.K2
    omega2 = r + (q02 - K2) ** 2
    vecs = d4_roots()
    analyze, _ = make_analyzer(grid, q02, r, u, v, vecs)
    rng = np.random.default_rng(seed)
    psi = noise * rng.standard_normal((N,) * 4)
    psi -= psi.mean()
    psi += psibar
    ph = np.fft.fftn(psi)
    vh = np.zeros_like(ph)
    filt = (K2 < 64).astype(float)
    ph *= filt
    vh *= filt

    def rhs(a, b):
        af, bf = a * filt, b * filt
        p = np.fft.ifftn(af).real
        nl = filt * (u * np.fft.fftn(p * p) - v * np.fft.fftn(p * p * p))
        return bf, -gamma * bf - omega2 * af + nl

    for _ in range(1, steps + 1):
        k1p, k1v = rhs(ph, vh)
        k2p, k2v = rhs(ph + dt / 2 * k1p, vh + dt / 2 * k1v)
        k3p, k3v = rhs(ph + dt / 2 * k2p, vh + dt / 2 * k2v)
        k4p, k4v = rhs(ph + dt * k3p, vh + dt * k3v)
        ph += dt / 6 * (k1p + 2 * k2p + 2 * k3p + k4p)
        vh += dt / 6 * (k1v + 2 * k2v + 2 * k3v + k4v)
        ph *= filt
        vh *= filt
    return ph, analyze(ph), grid


def static_pattern_field(N=16, L=math.pi, psibar=-0.18, a_star=0.0776):
    """The STATIC account's prediction, most charitably formalized.

    The imposed interference pattern Psi(x) = psibar + A* sum_g cos(g.x)
    over the 24 D4 shell modes (g in the scaled shell for this box), i.e. the
    full 24-mode standing wave at all times, independent of parameters.
    Amplitude from the one-mode ansatz (granted to the static account; v92
    had no amplitude equation). Returns (psi_hat, grid, analyzer).
    """
    grid = Grid(N, L)
    vecs = d4_roots()
    analyze, _ = make_analyzer(grid, 8.0, -0.35, 1.0, 1.0, vecs)
    ph = np.zeros((N,) * 4, complex)
    ph[0, 0, 0, 0] = psibar * N ** 4
    for n in vecs:
        ph[grid.gidx(n)] = a_star * N ** 4
    return ph, grid, analyze
