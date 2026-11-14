#!/usr/bin/env python3
"""Step 2 (Task 6): Bloch linearization about the harmonically relaxed D4 field.
Physics (derivation in REPORT.md):
  psi*(x) stationary, mean m=-0.18, box [0,2pi]^4.
  Bloch ansatz eta(x) = exp(i q.x) u(x), u 2pi-periodic, q in [0,1)^4.
  Fourier modes k = n + q, n in Z^4 (cube |n_i| <= Kb).
  L_q = -D_q H_q, D_q = diag(|n+q|^2),
  (H_q)_{n,n'} = [r + (8-|n+q|^2)^2] delta_{n,n'} + W_{n-n'},
  W_p = Fourier coeff of w(x) = -2 psi*(x) + 3 psi*(x)^2 (u=v=1).
  At q=0 the n=0 row/col is EXCLUDED (mean fixed); for q != 0, n=0 (k=q) is included.
  B_q = -D_q^{1/2} H_q D_q^{1/2} symmetric, similar to L_q (D_q > 0).
  Growth rate lambda = eigenvalue of B_q.
W is built by FFT on an N=28 grid from the relaxed coefficients (exact for the
quadratic product: relaxed support |k_i|<=4, W support |p_i|<=8 < 14).
Design (cost): the off-diagonal part of H_q is q-INDEPENDENT, so H is assembled
once per Kb (dense) and only the diagonal changes with q. Kb=2 dense full
spectrum for the map; Kb=3 dense full spectrum at selected q for convergence.
Checks: C1 Goldstone H*d_j psi* ~ 0 at q=0; C2 FD check of H action;
C3 Schur-complement slope for the conserved-mean channel; C4 Kb=2 vs Kb=3;
C5 K4-relaxed vs K6-relaxed W.
Pinned seed: default_rng(20261114) for the FD test vector only.
"""
import os
for k in ('OMP_NUM_THREADS', 'OPENBLAS_NUM_THREADS', 'MKL_NUM_THREADS'):
    os.environ[k] = '1'
import argparse, csv, itertools, json, time
from pathlib import Path
import numpy as np

BASE = Path('/home/hatch/workspace/research/irh/co-scientist-tasks-2026-11-10')
WORK = BASE / 'local-independent/task6-bloch-growth'
R, MEAN, Q2, U, V = -0.35, -0.18, 8.0, 1.0, 1.0

def load_relaxed(tag):
    z = np.load(WORK / f'data/relaxed_{tag}.npz')
    ks = [tuple(int(x) for x in k) for k in z['ks']]
    return dict(zip(ks, z['vals'])), float(z['energy']), float(z['rhs_rms'])

def build_W(a, ngrid=28, pmax=8):
    psi_hat = np.zeros((ngrid,) * 4, dtype=complex)
    psi_hat[(0,) * 4] = MEAN
    for k, v in a.items():
        psi_hat[tuple(x % ngrid for x in k)] = v
    psi_c = np.fft.ifftn(psi_hat, norm='forward')
    assert np.max(np.abs(psi_c.imag)) < 1e-12, float(np.max(np.abs(psi_c.imag)))
    w = -2 * U * psi_c.real + 3 * V * psi_c.real ** 2
    what = np.fft.fftn(w, norm='forward')
    W = {}
    for p in itertools.product(range(-pmax, pmax + 1), repeat=4):
        W[p] = complex(what[tuple(x % ngrid for x in p)])
    return W

def assemble_H_offdiag(Kb, W, thresh=1e-12):
    """Dense off-diagonal H (shifts p != 0) + W0. pts excludes n=0 (added back
    by caller when needed). Returns (pts, H_off, W0, nshifts_kept)."""
    pts = [k for k in itertools.product(range(-Kb, Kb + 1), repeat=4) if k != (0, 0, 0, 0)]
    n = len(pts)
    idx = {k: i for i, k in enumerate(pts)}
    K = np.array(pts, dtype=np.int32)
    lo = K.min(axis=0); hi = K.max(axis=0); width = hi - lo + 1
    stride = np.array([width[1] * width[2] * width[3], width[2] * width[3], width[3], 1], dtype=np.int64)
    ids = (K - lo) @ stride
    lut = np.full(int(np.prod(width)), -1, dtype=np.int32)
    lut[ids] = np.arange(n)
    H = np.zeros((n, n))
    kept = 0
    for p, wv in W.items():
        if p == (0, 0, 0, 0) or abs(wv) < thresh:
            continue
        kept += 1
        L = K - np.array(p)
        good = np.all((L >= lo) & (L <= hi), axis=1)
        ii = np.flatnonzero(good)
        jj = lut[(L[good] - lo) @ stride]
        valid = jj >= 0
        H[ii[valid], jj[valid]] += wv.real
    return pts, H, float(W[(0, 0, 0, 0)].real), kept

def spectra_for_q(q, pts, H_off, W0):
    """Full dense spectrum of B_q. Returns (lam_desc, Y, d, pts, H)."""
    q = np.array(q, dtype=float)
    K = np.array(pts, dtype=float)
    kk = K + q
    d = np.sum(kk * kk, axis=1)
    assert np.all(d > 0)
    diag = R + (Q2 - d) ** 2 + W0
    H = H_off + np.diag(diag)
    root = np.sqrt(d)
    B = -(root[:, None] * H * root[None, :])
    B = (B + B.T) / 2
    lam, Y = np.linalg.eigh(B)
    ix = np.argsort(lam)[::-1]
    return lam[ix], Y[:, ix], d, H

def mean_channel(lam, Y, d, pts):
    """Eigenvector (among all) with max |h_{n=0}|^2, h = sqrt(D) y normalised.
    Returns (lam_mean, p0, dom_n, dom_power)."""
    if (0, 0, 0, 0) not in pts:
        return None
    i0 = pts.index((0, 0, 0, 0))
    Hv = np.sqrt(d)[:, None] * Y
    Hv /= np.linalg.norm(Hv, axis=0)
    p0 = np.abs(Hv[i0, :]) ** 2
    j = int(np.argmax(p0))
    pw = np.abs(Hv[:, j]) ** 2
    return float(lam[j]), float(p0[j]), pts[int(np.argmax(pw))], float(pw.max())

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--coarse-only', action='store_true')
    args = ap.parse_args()
    t_start = time.perf_counter()
    a4, E4, rhs4 = load_relaxed('K4')
    try:
        a6, E6, rhs6 = load_relaxed('K6')
        have_k6 = True
    except FileNotFoundError:
        a6, E6, rhs6, have_k6 = None, None, None, False
    print(f'relaxed K4: E={E4:.15f} rhs={rhs4:.3e} ncoeff={len(a4)}', flush=True)
    if have_k6:
        print(f'relaxed K6: E={E6:.15f} rhs={rhs6:.3e} ncoeff={len(a6)}', flush=True)
    else:
        print('relaxed K6: NOT AVAILABLE YET (C5 will be NOT RUN)', flush=True)
    W4 = build_W(a4)
    W6 = build_W(a6) if have_k6 else None
    print(f'W4: W0={W4[(0,0,0,0)]:.10f} max|W|={max(abs(v) for v in W4.values()):.6f} '
          f'n|W|>1e-4={sum(1 for v in W4.values() if abs(v) > 1e-4)} '
          f'n|W|>1e-6={sum(1 for v in W4.values() if abs(v) > 1e-6)}', flush=True)
    checks = {}

    # ---- assemble Kb=3 H (also used for C1/C2/C3) ----
    t0 = time.perf_counter()
    pts3, Hoff3, W04, kept3 = assemble_H_offdiag(3, W4)
    print(f'Kb3 assembly: {time.perf_counter()-t0:.1f}s kept_shifts={kept3} n={len(pts3)}', flush=True)
    pts2, Hoff2, _, kept2 = assemble_H_offdiag(2, W4)
    print(f'Kb2 assembly: kept_shifts={kept2} n={len(pts2)}', flush=True)
    if have_k6:
        pts2b, Hoff2_6, W06, _ = assemble_H_offdiag(2, W6)
    else:
        pts2b = Hoff2_6 = None; W06 = float('nan')

    afull = dict(a4); afull[(0, 0, 0, 0)] = MEAN
    # ---- C1: Goldstone at q=0 ----
    lam0, Y0, d0, H0 = spectra_for_q((0, 0, 0, 0), pts3, Hoff3, W04)
    idx0 = {k: i for i, k in enumerate(pts3)}
    cvecs = [np.array([1j * k[j] * afull.get(k, 0.0) for k in pts3]) for j in range(4)]
    G = np.array([[float(np.vdot(cvecs[i], cvecs[j]).real) for j in range(4)] for i in range(4)])
    gold = []
    for j in range(4):
        for tag, vr in (('re', cvecs[j].real), ('im', cvecs[j].imag)):
            if np.linalg.norm(vr) < 1e-12:
                continue
            gold.append((j, tag, float(np.linalg.norm(H0 @ vr) / np.linalg.norm(vr))))
    checks['C1_goldstone_Hv_over_v'] = gold
    checks['C1_gram_eig_dpsi'] = np.linalg.eigvalsh(G).tolist()
    checks['C1_lam0_top6'] = lam0[:6].tolist()
    print('C1 Goldstone |H d_j psi*|/|d_j psi*|:', [(g[0], g[1], f'{g[2]:.3e}') for g in gold], flush=True)
    print('C1 Gram eig:', np.linalg.eigvalsh(G), ' lam0 top6:', lam0[:6], flush=True)

    # ---- C2: finite-difference check of H action ----
    rng = np.random.default_rng(20261114)
    eta = {}
    for k in pts3:
        eta[k] = rng.normal() + 1j * rng.normal()
    for k in list(eta):
        nk = tuple(-x for x in k)
        if nk in eta and k < nk:
            eta[nk] = eta[k].conjugate()
    def mu_of(a_dict):
        ngrid = 28
        ph = np.zeros((ngrid,) * 4, dtype=complex)
        for k, v in a_dict.items():
            ph[tuple(x % ngrid for x in k)] = v
        psi_r = np.fft.ifftn(ph, norm='forward').real
        mu = np.fft.fftn(-U * psi_r ** 2 + V * psi_r ** 3, norm='forward')
        return {k: (R + (Q2 - sum(x * x for x in k)) ** 2) * v
                + complex(mu[tuple(x % ngrid for x in k)]) for k, v in a_dict.items()}
    eps = 1e-6
    a_p = dict(afull); a_m = dict(afull)
    for k in pts3:
        a_p[k] = a_p.get(k, 0.0) + eps * eta[k]
        a_m[k] = a_m.get(k, 0.0) - eps * eta[k]
    mu_p, mu_m = mu_of(a_p), mu_of(a_m)
    fd = np.array([(mu_p[k] - mu_m[k]) / (2 * eps) for k in pts3])
    evec = np.array([eta[k] for k in pts3])
    Heta = H0 @ evec
    rel = float(np.linalg.norm(fd - Heta) / np.linalg.norm(Heta))
    checks['C2_fd_H_relative'] = rel; checks['C2_eps'] = eps
    print(f'C2 FD vs H: rel L2 err = {rel:.3e}', flush=True)

    # ---- C3: Schur complement for the mean channel (Kb=3, n=0 included) ----
    # pts_with_zero is defined below (vectorised); duplicate its logic inline here
    # via a local call to the same lut assembly used for the Bloch matrices.
    def _assemble_include_zero(Kb, W):
        pts = [k for k in itertools.product(range(-Kb, Kb + 1), repeat=4)]
        n = len(pts); idx = {k: i for i, k in enumerate(pts)}
        K = np.array(pts, dtype=np.int32)
        lo = K.min(axis=0); hi = K.max(axis=0); width = hi - lo + 1
        stride = np.array([width[1]*width[2]*width[3], width[2]*width[3], width[3], 1], dtype=np.int64)
        ids = (K - lo) @ stride
        lut = np.full(int(np.prod(width)), -1, dtype=np.int32); lut[ids] = np.arange(n)
        H = np.zeros((n, n))
        for p, wv in W.items():
            if p == (0, 0, 0, 0) or abs(wv) < 1e-12:
                continue
            L = K - np.array(p)
            good = np.all((L >= lo) & (L <= hi), axis=1)
            ii = np.flatnonzero(good); jj = lut[(L[good] - lo) @ stride]
            valid = jj >= 0
            H[ii[valid], jj[valid]] += wv.real
        return pts, H
    ptsf, Hoff_f = _assemble_include_zero(3, W4)
    Kf = np.array(ptsf, dtype=float)
    df = np.sum(Kf * Kf, axis=1)
    Hf = Hoff_f + np.diag(R + (Q2 - df) ** 2 + W04)
    Hf = (Hf + Hf.T) / 2
    i0 = ptsf.index((0, 0, 0, 0))
    rest = [i for i in range(len(ptsf)) if i != i0]
    H00 = Hf[i0, i0]; H0Q = Hf[i0, rest]; HQQ = Hf[np.ix_(rest, rest)]
    emin = float(np.linalg.eigvalsh(HQQ)[0])
    S = float(H00 - H0Q @ np.linalg.solve(HQQ, H0Q))
    checks['C3'] = dict(H00=float(H00), HQQ_min_eig=emin, Schur_S=S, pred_lambda_over_q2=-S)
    print(f'C3 Schur: H00={H00:.6f} HQQ_min_eig={emin:.6f} S={S:.6f} pred lam/|q|^2={-S:.6f}', flush=True)

    # ---- Coarse Bloch map: Kb=2 dense, full spectrum per q ----
    qpoints = []
    def add_q(q, label):
        qpoints.append((tuple(float(x) for x in q), label))
    for t in [0.0, 0.05, 0.1, 0.15, 0.2, 0.25, 0.3, 0.35, 0.4, 0.45, 0.5]:
        add_q((t, 0, 0, 0), 'axis_e1')
    for t in [0.05, 0.1, 0.15, 0.2, 0.25, 0.3, 0.35]:
        add_q((t, t, 0, 0), 'diag110')
    for t in [0.05, 0.1, 0.15, 0.2, 0.25, 0.3]:
        add_q((t, t, t, 0), 'diag1110')
        add_q((t, t, t, t), 'diag1111')
    for t in [0.1, 0.2, 0.3, 0.4, 0.5]:
        add_q((0.5, t, 0, 0), 'face_0.5_t')
        add_q((t, 0.5, 0.5, 0), 'corner_t55')
    for q, lab in [((0.5, 0.5, 0, 0), 'zone_M110'), ((0.5, 0.5, 0.5, 0), 'zone_M1110'),
                   ((0.5, 0.5, 0.5, 0.5), 'zone_R1111'), ((0.5, 0, 0, 0), 'zone_X100'),
                   ((0.3, 0.1, 0, 0), 'generic_a'), ((0.2, 0.35, 0.1, 0), 'generic_b'),
                   ((0.4, 0.2, 0.3, 0.1), 'generic_c'), ((0.15, 0.45, 0.2, 0.05), 'generic_d')]:
        add_q(q, lab)
    # Kb=2 pts exclude n=0, so for q=0 spectra use pts2 as-is; for q!=0 need n=0 included.
    # Handle by building a second Kb=2 assembly WITH n=0 for q!=0 points.
    def pts_with_zero(Kb, W):
        pts = [k for k in itertools.product(range(-Kb, Kb + 1), repeat=4)]
        n = len(pts); idx = {k: i for i, k in enumerate(pts)}
        K = np.array(pts, dtype=np.int32)
        lo = K.min(axis=0); hi = K.max(axis=0); width = hi - lo + 1
        stride = np.array([width[1]*width[2]*width[3], width[2]*width[3], width[3], 1], dtype=np.int64)
        ids = (K - lo) @ stride
        lut = np.full(int(np.prod(width)), -1, dtype=np.int32); lut[ids] = np.arange(n)
        H = np.zeros((n, n))
        for p, wv in W.items():
            if p == (0, 0, 0, 0) or abs(wv) < 1e-12:
                continue
            L = K - np.array(p)
            good = np.all((L >= lo) & (L <= hi), axis=1)
            ii = np.flatnonzero(good); jj = lut[(L[good] - lo) @ stride]
            valid = jj >= 0
            H[ii[valid], jj[valid]] += wv.real
        return pts, H
    pts2z, Hoff2z = pts_with_zero(2, W4)
    rows = []
    for q, label in qpoints:
        if q == (0.0, 0.0, 0.0, 0.0):
            lam, Y, d, _ = spectra_for_q(q, pts2, Hoff2, W04)
            pts_u, mc = pts2, None
        else:
            lam, Y, d, _ = spectra_for_q(q, pts2z, Hoff2z, W04)
            pts_u = pts2z
            mc = mean_channel(lam, Y, d, pts_u)
        rows.append(dict(q0=q[0], q1=q[1], q2=q[2], q3=q[3], qnorm=float(np.linalg.norm(q)),
                         label=label, Kb=2, lam_max=float(lam[0]), lam2=float(lam[1]),
                         lam3=float(lam[2]), lam4=float(lam[3]), lam5=float(lam[4]),
                         lam6=float(lam[5]),
                         lam_mean=(float(mc[0]) if mc else ''),
                         mean_power=(float(mc[1]) if mc else ''),
                         mean_dom_n=(str(mc[2]) if mc else '')))
        print(f'Kb2 q={q} {label}: lam_max={lam[0]:+.6f} lam2={lam[1]:+.6f} lam3={lam[2]:+.6f} '
              f'lam_mean={(mc[0] if mc else float("nan")):+.6f} (p0={(mc[1] if mc else 0):.3f})', flush=True)
    with open(WORK / 'data/bloch_coarse_Kb2.csv', 'w', newline='') as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0])); w.writeheader(); w.writerows(rows)

    results = dict(checks=checks, coarse_rows=len(rows))
    if args.coarse_only:
        (WORK / 'data/bloch_checks.json').write_text(json.dumps(results, indent=2, default=str))
        print('coarse-only done in', time.perf_counter() - t_start, 's', flush=True)
        return

    # ---- Kb=3 dense checks at selected q (convergence C4) ----
    # For q!=0 need pts including n=0 at Kb=3: build once.
    pts3z, Hoff3z = pts_with_zero(3, W4)
    pts3z6 = Hoff3z6 = None
    sel = [((0.0, 0, 0, 0), 'q0'), ((0.1, 0, 0, 0), 'axis0.10'), ((0.25, 0, 0, 0), 'axis0.25'),
           ((0.5, 0, 0, 0), 'zoneX'), ((0.25, 0.25, 0, 0), 'diag0.25'),
           ((0.5, 0.5, 0, 0), 'zoneM110'), ((0.5, 0.5, 0.5, 0.5), 'zoneR'),
           ((0.2, 0.35, 0.1, 0), 'generic_b')]
    c4 = []
    for q, label in sel:
        if q == (0.0, 0, 0, 0):
            lam2, Y2, d2, _ = spectra_for_q(q, pts2, Hoff2, W04)
            lam3, Y3, d3, _ = spectra_for_q(q, pts3, Hoff3, W04)
            mc2 = mc3 = None
        else:
            lam2, Y2, d2, _ = spectra_for_q(q, pts2z, Hoff2z, W04)
            lam3, Y3, d3, _ = spectra_for_q(q, pts3z, Hoff3z, W04)
            mc2 = mean_channel(lam2, Y2, d2, pts2z)
            mc3 = mean_channel(lam3, Y3, d3, pts3z)
        c4.append(dict(q=list(q), label=label,
                       Kb2_lam_max=float(lam2[0]), Kb3_lam_max=float(lam3[0]),
                       diff_lam_max=float(lam3[0] - lam2[0]),
                       Kb2_lam2=float(lam2[1]), Kb3_lam2=float(lam3[1]),
                       Kb2_lam_mean=(float(mc2[0]) if mc2 else ''),
                       Kb3_lam_mean=(float(mc3[0]) if mc3 else ''),
                       Kb2_mean_power=(float(mc2[1]) if mc2 else ''),
                       Kb3_mean_power=(float(mc3[1]) if mc3 else '')))
        print(f'C4 {label}: Kb2 lam_max={lam2[0]:+.8f} Kb3={lam3[0]:+.8f} diff={lam3[0]-lam2[0]:+.3e} '
              f'lam_mean Kb2={(mc2[0] if mc2 else float("nan")):+.6f} Kb3={(mc3[0] if mc3 else float("nan")):+.6f}', flush=True)
    checks['C4_Kb2_vs_Kb3'] = c4

    # ---- C5: K6-relaxed W at selected q (Kb=2 dense + Kb=3 at two q) ----
    c5 = []
    if not have_k6:
        checks['C5_K4_vs_K6'] = 'NOT RUN (relaxed_K6.npz not available yet)'
        results['checks'] = checks
        results['elapsed_s'] = time.perf_counter() - t_start
        (WORK / 'data/bloch_checks.json').write_text(json.dumps(results, indent=2, default=str))
        print('done (C5 NOT RUN) in', time.perf_counter() - t_start, 's', flush=True)
        return
    for q, label in [((0.0, 0, 0, 0), 'q0'), ((0.25, 0, 0, 0), 'axis0.25'),
                     ((0.5, 0, 0, 0), 'zoneX'), ((0.25, 0.25, 0, 0), 'diag0.25'),
                     ((0.5, 0.5, 0.5, 0.5), 'zoneR')]:
        if q == (0.0, 0, 0, 0):
            l4, _, _, _ = spectra_for_q(q, pts2, Hoff2, W04)
            l6, _, _, _ = spectra_for_q(q, pts2b, Hoff2_6, W06)
        else:
            pts2z6, Hoff2z6 = pts_with_zero(2, W6)
            l4, _, _, _ = spectra_for_q(q, pts2z, Hoff2z, W04)
            l6, _, _, _ = spectra_for_q(q, pts2z6, Hoff2z6, W06)
        c5.append(dict(q=list(q), label=label, lam_max_K4=float(l4[0]), lam_max_K6=float(l6[0]),
                       diff=float(l4[0] - l6[0]), lam2_K4=float(l4[1]), lam2_K6=float(l6[1])))
        print(f'C5 {label}: K4 lam_max={l4[0]:+.8f} K6={l6[0]:+.8f} diff={l4[0]-l6[0]:+.3e}', flush=True)
    checks['C5_K4_vs_K6'] = c5

    results['checks'] = checks
    results['elapsed_s'] = time.perf_counter() - t_start
    (WORK / 'data/bloch_checks.json').write_text(json.dumps(results, indent=2, default=str))
    print('done in', time.perf_counter() - t_start, 's', flush=True)

if __name__ == '__main__':
    main()
