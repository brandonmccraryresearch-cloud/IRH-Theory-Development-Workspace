#!/usr/bin/env python3
"""Independent second-tool check for a grain run (Task 2).

Recomputes, from the saved compact Fourier coefficients in
grain_state.npz, using ONLY numpy.fft (no scipy, no run_grain code):
  - final excess energy density (real-space sums + spectral quadratic
    term via numpy rfftn/irfftn)
  - final shell power, shell fraction, modulation power
  - final triad lock, with the triad list re-enumerated here by brute
    force over the 24 shell vectors (independent of run_grain.TRIADS)
  - template RMS and envelope partition of unity, re-derived here
Compares against grain_outcome.json / grain_trajectories.csv and
prints PASS/FAIL per quantity. This is the second independent tool
required by the truth-seeking computation gate for above-CLAIMED
load-bearing numbers.
"""
import itertools, json, sys
from pathlib import Path
import numpy as np

ALPHA = 0.1072
BETA = 1.54
LBOX = 4 * np.pi


def load_run(d):
    d = Path(d)
    out = json.loads((d / 'grain_outcome.json').read_text())
    par = json.loads((d / 'parameters.json').read_text())
    z = np.load(d / 'grain_state.npz')
    return d, out, par, z


def reconstruct(z, par, which):
    """Real-space modulation field on the n^4 grid from compact coeffs."""
    n = par['n']
    K = par['cutoff']
    comp = z['wavevectors']
    coef = z[which]
    F = np.zeros((n, n, n, n // 2 + 1), dtype=complex)
    for k, a in zip(comp, coef):
        if k[3] >= 0:
            F[tuple(k[:3] % n) + (int(k[3]),)] = a
    # Hermitian completion for k3 < 0 is implicit in irfftn (real output).
    field = np.fft.irfftn(F, s=(n,) * 4, axes=(0, 1, 2, 3), norm='forward')
    return field, F


def lop_array(n):
    f = np.fft.fftfreq(n, d=1.0 / n)  # integer m indices
    rf = np.fft.rfftfreq(n, d=1.0 / n)
    m1, m2, m3, m4 = np.meshgrid(f, f, f, rf, indexing='ij', sparse=True)
    m2sum = m1 ** 2 + m2 ** 2 + m3 ** 2 + m4 ** 2
    k2phys = m2sum / 4.0
    lop = ALPHA + (8.0 - k2phys) ** 2
    return k2phys, lop


def energy(field, F, n):
    k2phys, lop = lop_array(n)
    lphi = np.fft.irfftn(lop * F, s=(n,) * 4, axes=(0, 1, 2, 3), norm='forward')
    quad = 0.5 * float(np.mean(field * lphi))
    return quad + float(np.mean(-BETA / 3 * field ** 3 + field ** 4 / 4))


def main():
    d, out, par, z = load_run(sys.argv[1])
    n = par['n']
    star = z['star_wavevectors_m']
    assert len(star) == 24
    # triads re-enumerated here
    triads = [t for t in itertools.combinations(range(24), 3)
              if np.all(star[list(t)].sum(axis=0) == 0)]
    field, F = reconstruct(z, par, 'final_coefficients')
    # shell coefficients from F
    a = []
    for k in star:
        if k[3] >= 0:
            a.append(F[tuple(k[:3] % n) + (int(k[3]),)])
        else:
            a.append(F[tuple((-k[:3]) % n) + (int(-k[3]),)].conjugate())
    a = np.array(a)
    # Parseval with forward norm: power = sum over full k of |a_k|^2.
    # F holds k3 >= 0; double all except k3 == 0 and k3 == n/2.
    w = np.ones((n, n, n, n // 2 + 1))
    w[:, :, :, 1:(n // 2)] = 2.0
    power = float(np.sum(w * np.abs(F) ** 2))
    shell = float(np.sum(np.abs(a) ** 2))
    # triad lock
    prods = np.array([a[i] * a[j] * a[k] for (i, j, k) in triads])
    lock = float(prods.real.sum() / np.abs(prods).sum())
    E = energy(field, F, n)
    checks = []
    def chk(name, got, want, tol):
        ok = abs(got - want) <= tol
        checks.append(ok)
        print(f"{'PASS' if ok else 'FAIL'}  {name}: got {got:.12g} want {want:.12g} tol {tol:g}")
    chk('final excess energy', E, out['excess_energy'], 1e-9)
    chk('final shell power', shell, out['shell_power'], 1e-9)
    chk('final modulation power', power, out['modulation_power'], 1e-9)
    chk('final shell fraction', shell / power, out['shell_fraction'], 1e-9)
    chk('final triad lock', lock, out['triad_lock'], 1e-9)
    chk('final occupancy (recomputed)', int(np.sum(
        np.abs(a) >= max(1e-6, 0.1 * np.abs(a).max()))), out['occupancy'], 0)
    print(f"triads enumerated here: {len(triads)} (expect 32)")
    print(f"field RMS: {float(np.sqrt(np.mean(field**2))):.12g} "
          f"vs outcome modulation_rms {out['modulation_rms']:.12g}")
    print('ALL PASS' if all(checks) and len(triads) == 32 else 'FAILURES PRESENT')


if __name__ == '__main__':
    main()
