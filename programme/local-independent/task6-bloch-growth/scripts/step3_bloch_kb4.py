#!/usr/bin/env python3
"""Step 3 (Task 6): Bloch linearization at Kb=4 (the full relaxed band),
with parity-sector decomposition.
KEY FACT (found by diagnosis, see REPORT.md): the relaxed field has Fourier
support ONLY on vectors with all components even (star vectors are even, and
the Model B dynamics preserve even support). Hence W_p != 0 only for p even,
so H_q (and B_q) block-diagonalise by n mod 2: 16 parity sectors, largest
625 modes (all-even sector, |n_i| in {0,2,4}). Kb=2 and Kb=3 share the SAME
even sector (components -2,0,2 only), which is why they agreed to 1e-9 while
both missing the |n_i|=4 even modes and giving a spurious lam_max(0)=-0.00876.
At Kb=4 the even sector is complete (in-band), and q=0 must give 4 exact
Goldstone zeros. Sector sizes at Kb=4: even-component count 5 per axis,
odd-component count 4 per axis.
Per q: 16 dense eighs (n<=625). Full spectrum per sector is kept.
Checks in this script:
  C1b: H @ d_j psi* at Kb=4 (full band) ~ residual scale (analytic: = d_j mu = 0).
  C3b: Schur complement S at Kb=4 (even sector) vs fitted mean-channel slope.
  C4b: Kb=4 vs Kb=2 lam_max / lam_mean at matched q (quantifies Kb=2 bias).
  C5b: K6-relaxed W at Kb=4, selected q.
  C6:  duplicate q points with permuted/sign-flipped q give identical spectra
       (symmetry check, independent code path through different sector order).
Pinned seeds: default_rng(20261114) for random-BZ q sample.
"""
import os
for k in ('OMP_NUM_THREADS', 'OPENBLAS_NUM_THREADS', 'MKL_NUM_THREADS'):
    os.environ[k] = '1'
import csv, itertools, json, time
from pathlib import Path
import numpy as np

BASE = Path('/home/hatch/workspace/research/irh/co-scientist-tasks-2026-11-10')
WORK = BASE / 'local-independent/task6-bloch-growth'
R, MEAN, Q2, U, V = -0.35, -0.18, 8.0, 1.0, 1.0
KB = 4

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

def assemble_H(Kb, W, thresh=1e-12):
    """Dense H_off (p!=0 shifts) + W0 for the full cube |n_i|<=Kb (including n=0).
    Returns pts, H_off, W0. Vectorised per-shift assembly (A6-style lut)."""
    pts = [k for k in itertools.product(range(-Kb, Kb + 1), repeat=4)]
    n = len(pts)
    K = np.array(pts, dtype=np.int32)
    lo = K.min(axis=0); hi = K.max(axis=0); width = hi - lo + 1
    stride = np.array([width[1]*width[2]*width[3], width[2]*width[3], width[3], 1], dtype=np.int64)
    ids = (K - lo) @ stride
    lut = np.full(int(np.prod(width)), -1, dtype=np.int32); lut[ids] = np.arange(n)
    H = np.zeros((n, n))
    kept = 0
    max_im = 0.0
    for p, wv in W.items():
        if p == (0, 0, 0, 0) or abs(wv) < thresh:
            continue
        kept += 1
        max_im = max(max_im, abs(wv.imag))
        L = K - np.array(p)
        good = np.all((L >= lo) & (L <= hi), axis=1)
        ii = np.flatnonzero(good); jj = lut[(L[good] - lo) @ stride]
        valid = jj >= 0
        H[ii[valid], jj[valid]] += wv.real
    return pts, H, float(W[(0, 0, 0, 0)].real), kept, max_im

def sectors(pts):
    """Group indices by n mod 2."""
    sec = {}
    for i, k in enumerate(pts):
        sec.setdefault(tuple(x % 2 for x in k), []).append(i)
    return sec

def spectra_q(q, pts, Hoff, W0, sec):
    """Full spectrum: per parity sector, dense eigh of B. Returns
    (lam_desc, eigvecs as list of (sector_key, Y_sector, idx_sector), d)."""
    q = np.array(q, dtype=float)
    K = np.array(pts, dtype=float)
    d = np.sum((K + q) ** 2, axis=1)
    diag = R + (Q2 - d) ** 2 + W0
    H = Hoff + np.diag(diag)
    root = np.sqrt(d)
    out_lam = []
    out_vec = []
    for key, idx in sec.items():
        idx = np.array(idx)
        Hs = H[np.ix_(idx, idx)]
        rs = root[idx]
        Bs = -(rs[:, None] * Hs * rs[None, :])
        Bs = (Bs + Bs.T) / 2
        if np.all(q == 0) and key == (0, 0, 0, 0):
            # q=0, even sector: n=0 must be EXCLUDED (mean fixed)
            drop = list(idx).index(pts.index((0, 0, 0, 0))) if (0, 0, 0, 0) in pts else None
            keep = [j for j in range(len(idx)) if j != drop]
            Bs = Bs[np.ix_(keep, keep)]
            idx = idx[keep]
        lam, Y = np.linalg.eigh(Bs)
        out_lam.append(lam)
        out_vec.append((key, Y, idx))
    lam_all = np.concatenate(out_lam)
    ix = np.argsort(lam_all)[::-1]
    return lam_all[ix], out_vec, d, idx

def top_with_weights(lam_desc, vec_blocks, d, pts, n_top=8):
    """Reconstruct top eigenvectors' right-mode weights. Returns list of
    (lam, dom_n, dom_power, p0) for the top n_top eigenvalues, plus the
    mean-channel (max p0 over ALL eigenvectors, computed per sector)."""
    # Build per-sector full data for mean channel: need all eigenvectors.
    # Instead: mean channel from sector blocks directly (done in mean_channel()).
    return None

def mean_channel(vec_blocks, d, pts):
    """Eigenvector (over all sectors) with max |h_{n=0}|^2. h = sqrt(D) y."""
    if (0, 0, 0, 0) not in pts:
        return None
    i0 = pts.index((0, 0, 0, 0))
    best = None
    for key, Y, idx in vec_blocks:
        # eigenvalues for this sector are needed: recompute ordering via caller;
        # here we only return (p0, sector-local col) -- caller merges with lams.
        pass
    return None

def spectra_q_full(q, pts, Hoff, W0, sec):
    """Return (lam_desc, list of dicts {lam, sector, Ycol_global, idx}) with
    ALL eigenvalues and their (sector, local column)."""
    q = np.array(q, dtype=float)
    K = np.array(pts, dtype=float)
    d = np.sum((K + q) ** 2, axis=1)
    assert np.all(d > 0) or np.all(q == 0)
    diag = R + (Q2 - d) ** 2 + W0
    H = Hoff + np.diag(diag)
    root = np.sqrt(d)
    recs = []
    for key, idx in sec.items():
        idx = np.array(idx)
        include_zero = not (np.all(q == 0) and key == (0, 0, 0, 0))
        keep_idx = idx
        if not include_zero:
            zpos = list(idx).index(pts.index((0, 0, 0, 0)))
            keep_idx = np.array([j for j in range(len(idx)) if j != zpos])
            idx_use = idx[keep_idx]
        else:
            idx_use = idx
        Hs = H[np.ix_(idx_use, idx_use)]
        rs = root[idx_use]
        Bs = -(rs[:, None] * Hs * rs[None, :])
        Bs = (Bs + Bs.T) / 2
        lam, Y = np.linalg.eigh(Bs)
        for j in range(len(lam)):
            recs.append(dict(lam=float(lam[j]), sector=key, Ycol=Y[:, j], idx=idx_use))
    recs.sort(key=lambda r: -r['lam'])
    return recs, d

def analyse_rec(recs, d, pts, n_top=6):
    top = recs[:n_top]
    out = {}
    for i, r in enumerate(top):
        h = np.sqrt(d[r['idx']]) * r['Ycol']
        h = h / np.linalg.norm(h)
        pw = np.abs(h) ** 2
        out[f'lam{i+1}'] = r['lam']
        out[f'dom{i+1}'] = str(pts[int(r['idx'][int(np.argmax(pw))])])
        out[f'dompow{i+1}'] = float(pw.max())
    # mean channel: max p0 over all recs
    if (0, 0, 0, 0) in pts:
        i0 = pts.index((0, 0, 0, 0))
        best = None
        for r in recs:
            pos = list(r['idx']).index(i0) if i0 in r['idx'] else None
            if pos is None:
                continue
            h = np.sqrt(d[r['idx']]) * r['Ycol']
            h = h / np.linalg.norm(h)
            p0 = float(np.abs(h[pos]) ** 2)
            if best is None or p0 > best[1]:
                best = (r['lam'], p0, pts[int(r['idx'][int(np.argmax(np.abs(h) ** 2))])])
        if best is not None:
            out['lam_mean'], out['mean_power'], out['mean_dom_n'] = best
    return out

def main():
    t_start = time.perf_counter()
    a4, E4, rhs4 = load_relaxed('K4')
    a6, E6, rhs6 = load_relaxed('K6')
    print(f'K4 E={E4:.15f} rhs={rhs4:.3e}; K6 E={E6:.15f} rhs={rhs6:.3e}', flush=True)
    W4 = build_W(a4); W6 = build_W(a6)
    # symmetry audit of W: odd shifts must vanish (even support)
    odd_max = max(abs(v) for p, v in W4.items() if any(x % 2 for x in p))
    print(f'W4 odd-shift max |W| = {odd_max:.3e} (must be ~roundoff); '
          f'W0={W4[(0,0,0,0)]:.10f}; max|Im W|={max(abs(v.imag) for v in W4.values()):.3e}', flush=True)
    t0 = time.perf_counter()
    pts, Hoff, W0, kept, max_im = assemble_H(KB, W4)
    sec = sectors(pts)
    print(f'Kb4 assembly {time.perf_counter()-t0:.1f}s n={len(pts)} kept_shifts={kept} '
          f'max|Im W kept|={max_im:.3e} sectors={ {k: len(v) for k, v in sec.items()} }', flush=True)
    checks = {}

    # ---- C1b: Goldstone at Kb=4, full band ----
    afull = dict(a4); afull[(0, 0, 0, 0)] = MEAN
    recs0, d0 = spectra_q_full((0, 0, 0, 0), pts, Hoff, W0, sec)
    lam0 = [r['lam'] for r in recs0]
    print('q=0 top10 lam:', [f'{x:+.3e}' for x in lam0[:10]], flush=True)
    # H (not B) at q=0: H = Hoff + diag(R+(8-d)^2+W0)
    Karr = np.array(pts, dtype=float)
    darr = np.sum(Karr * Karr, axis=1)
    H0 = Hoff + np.diag(R + (Q2 - darr) ** 2 + W0)
    gold = []
    for j in range(4):
        v = np.array([1j * k[j] * afull.get(k, 0.0) for k in pts], dtype=complex)
        Hv = H0 @ v
        gold.append(float(np.linalg.norm(Hv) / np.linalg.norm(v)))
    checks['C1b_goldstone_Hv_over_v'] = gold
    checks['C1b_lam0_top10'] = lam0[:10]
    print('C1b |H d_j psi*|/|d_j psi*|:', [f'{g:.3e}' for g in gold], flush=True)

    # ---- C3b: Schur complement at Kb=4 (even sector only; H block-diagonal) ----
    ev_idx = np.array(sec[(0, 0, 0, 0)])
    Hev = H0[np.ix_(ev_idx, ev_idx)]
    zpos = list(ev_idx).index(pts.index((0, 0, 0, 0)))
    rest = [i for i in range(len(ev_idx)) if i != zpos]
    H00 = Hev[zpos, zpos]; H0Q = Hev[zpos, rest]; HQQ = Hev[np.ix_(rest, rest)]
    emin_qq = float(np.linalg.eigvalsh(HQQ)[0])
    emin_ev = float(np.linalg.eigvalsh(Hev)[0])
    S = float(H00 - H0Q @ np.linalg.solve(HQQ, H0Q))
    checks['C3b'] = dict(H00=float(H00), HQQ_min_eig=emin_qq, Hev_min_eig=emin_ev,
                         Schur_S=S, pred_lambda_over_q2=-S)
    print(f'C3b Schur Kb4: H00={H00:.6f} HQQ_min={emin_qq:.3e} Hev_min={emin_ev:.3e} '
          f'S={S:.6f} pred lam/|q|^2={-S:.6f}', flush=True)

    # ---- Bloch map at Kb=4 ----
    qpoints = []
    def add_q(q, label):
        qpoints.append((tuple(float(x) for x in q), label))
    for t in [0.0, 0.025, 0.05, 0.075, 0.1, 0.125, 0.15, 0.2, 0.25, 0.3, 0.35, 0.4, 0.45, 0.5]:
        add_q((t, 0, 0, 0), 'axis_e1')
    for t in [0.025, 0.05, 0.075, 0.1, 0.125, 0.15, 0.2, 0.25, 0.3, 0.35]:
        add_q((t, t, 0, 0), 'diag110')
        add_q((t, t, t, 0), 'diag1110')
        add_q((t, t, t, t), 'diag1111')
    for t in [0.05, 0.1, 0.15, 0.2, 0.25, 0.3, 0.35, 0.4, 0.45, 0.5]:
        add_q((0.5, t, 0, 0), 'face_0.5_t')
        add_q((t, 0.5, 0.5, 0), 'corner_t55')
    for q, lab in [((0.5, 0.5, 0, 0), 'zone_M110'), ((0.5, 0.5, 0.5, 0), 'zone_M1110'),
                   ((0.5, 0.5, 0.5, 0.5), 'zone_R1111'), ((0.5, 0, 0, 0), 'zone_X100'),
                   ((0.3, 0.1, 0, 0), 'generic_a'), ((0.2, 0.35, 0.1, 0), 'generic_b'),
                   ((0.4, 0.2, 0.3, 0.1), 'generic_c'), ((0.15, 0.45, 0.2, 0.05), 'generic_d'),
                   ((0.3, 0.3, 0.3, 0), 'diag1110_t0.3'), ((0.28, 0.28, 0.28, 0), 'diag1110_t0.28'),
                   ((0.32, 0.32, 0.32, 0), 'diag1110_t0.32')]:
        add_q(q, lab)
    rng = np.random.default_rng(20261114)
    for i in range(150):
        add_q(tuple(rng.uniform(0, 0.5, 4)), f'randomBZ_{i:03d}')
    rows = []
    for q, label in qpoints:
        recs, d = spectra_q_full(q, pts, Hoff, W0, sec)
        a = analyse_rec(recs, d, pts)
        rows.append(dict(q0=q[0], q1=q[1], q2=q[2], q3=q[3], qnorm=float(np.linalg.norm(q)),
                         label=label, Kb=4, lam_max=a['lam1'], lam2=a['lam2'], lam3=a['lam3'],
                         lam4=a['lam4'], lam5=a['lam5'], lam6=a['lam6'],
                         dom1=a['dom1'], dompow1=a['dompow1'],
                         lam_mean=a.get('lam_mean', ''), mean_power=a.get('mean_power', ''),
                         mean_dom_n=a.get('mean_dom_n', '')))
        if label.startswith(('axis', 'diag', 'zone', 'generic')) and q[0] in (0.0, 0.05, 0.1, 0.25, 0.5):
            print(f'Kb4 q={q} {label}: lam_max={a["lam1"]:+.6f} lam2={a["lam2"]:+.6f} '
                  f'lam4={a["lam4"]:+.6f} lam_mean={a.get("lam_mean", float("nan")):+.6f}', flush=True)
    with open(WORK / 'data/bloch_map_Kb4.csv', 'w', newline='') as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0])); w.writeheader(); w.writerows(rows)
    print(f'map rows={len(rows)} elapsed={time.perf_counter()-t_start:.1f}s', flush=True)

    # ---- C6: symmetry duplicates ----
    c6 = []
    for q, q2, lab in [((0.2, 0.1, 0, 0), (0.1, 0.2, 0, 0), 'perm12'),
                       ((0.2, 0.1, 0, 0), (-0.2, 0.1, 0, 0), 'signflip'),
                       ((0.3, 0.2, 0.1, 0.05), (0.05, 0.1, 0.2, 0.3), 'perm_rev')]:
        r1, _ = spectra_q_full(q, pts, Hoff, W0, sec)
        r2, _ = spectra_q_full(q2, pts, Hoff, W0, sec)
        l1 = np.array([r['lam'] for r in r1[:6]]); l2 = np.array([r['lam'] for r in r2[:6]])
        c6.append(dict(q=list(q), q2=list(q2), label=lab, max_top6_diff=float(np.max(np.abs(l1 - l2)))))
        print(f'C6 {lab}: max top6 diff = {c6[-1]["max_top6_diff"]:.3e}', flush=True)
    checks['C6_symmetry'] = c6

    # ---- C4b/C5b: Kb=4 vs Kb=2 and K6 at selected q (Kb=2 values from step2 CSV) ----
    import csv as _csv
    kb2 = {}
    for r in _csv.DictReader(open(WORK / 'data/bloch_coarse_Kb2.csv')):
        kb2[(float(r['q0']), float(r['q1']), float(r['q2']), float(r['q3']))] = r
    c4b = []
    sel = [(0.0, 0, 0, 0), (0.05, 0, 0, 0), (0.1, 0, 0, 0), (0.25, 0, 0, 0),
           (0.5, 0, 0, 0), (0.25, 0.25, 0, 0), (0.5, 0.5, 0.5, 0.5),
           (0.3, 0.3, 0.3, 0), (0.2, 0.35, 0.1, 0)]
    rowmap = {(round(r['q0'], 6), round(r['q1'], 6), round(r['q2'], 6), round(r['q3'], 6)): r for r in rows}
    for q in sel:
        r4 = rowmap.get(tuple(round(x, 6) for x in q))
        r2 = kb2.get(q)
        if r4 is None or r2 is None:
            continue
        c4b.append(dict(q=list(q), Kb4_lam_max=float(r4['lam_max']), Kb2_lam_max=float(r2['lam_max']),
                        diff=float(r4['lam_max']) - float(r2['lam_max']),
                        Kb4_lam_mean=r4['lam_mean'], Kb2_lam_mean=r2['lam_mean']))
        print(f'C4b q={q}: Kb4 lam_max={float(r4["lam_max"]):+.8f} Kb2={float(r2["lam_max"]):+.8f} '
              f'diff={float(r4["lam_max"])-float(r2["lam_max"]):+.3e}', flush=True)
    checks['C4b_Kb4_vs_Kb2'] = c4b
    # C5b: K6 W, Kb=4 assembly + selected q
    pts6, Hoff6, W06, kept6, _ = assemble_H(KB, W6)
    sec6 = sectors(pts6)
    c5b = []
    for q in [(0.0, 0, 0, 0), (0.1, 0, 0, 0), (0.25, 0, 0, 0), (0.5, 0, 0, 0),
              (0.25, 0.25, 0, 0), (0.5, 0.5, 0.5, 0.5), (0.3, 0.3, 0.3, 0)]:
        r6, _ = spectra_q_full(q, pts6, Hoff6, W06, sec6)
        l6 = [r['lam'] for r in r6[:3]]
        r4 = rowmap.get(tuple(round(x, 6) for x in q))
        c5b.append(dict(q=list(q), Kb4_K4_lam_max=float(r4['lam_max']) if r4 else None,
                        Kb4_K6_lam_max=float(l6[0]), diff=float(l6[0]) - float(r4['lam_max']) if r4 else None,
                        K6_lam2=float(l6[1])))
        print(f'C5b q={q}: K4 lam_max={float(r4["lam_max"]):+.8f} K6={l6[0]:+.8f} '
              f'diff={l6[0]-float(r4["lam_max"]):+.3e}', flush=True)
    checks['C5b_K4_vs_K6_Kb4'] = c5b

    # ---- Goldstone / mean slope fits from the Kb=4 axis cut ----
    axis_rows = [r for r in rows if r['label'] == 'axis_e1' and 0 < r['q0'] <= 0.15]
    axis_rows.sort(key=lambda r: r['q0'])
    # lam_max on axis = transverse branch (3-fold); lam4 = longitudinal+mean mix:
    # use lam_max (transverse) and lam_mean fits vs |q|^2 through origin.
    def fit_slope(rs, key):
        x = np.array([r['qnorm'] ** 2 for r in rs]); y = np.array([float(r[key]) for r in rs])
        return float(np.sum(x * y) / np.sum(x * x))
    checks['fits_axis'] = dict(
        transverse_slope_lam_max_vs_q2=fit_slope(axis_rows, 'lam_max'),
        mean_slope_lam_mean_vs_q2=fit_slope(axis_rows, 'lam_mean'),
        schur_pred=-checks['C3b']['Schur_S'],
        axis_points=[[r['q0'], float(r['lam_max']), float(r['lam_mean'])] for r in axis_rows])
    print('fits_axis:', checks['fits_axis'], flush=True)

    results = dict(checks=checks, map_rows=len(rows), elapsed_s=time.perf_counter() - t_start)
    (WORK / 'data/bloch_checks_Kb4.json').write_text(json.dumps(results, indent=2, default=str))
    print('done in', time.perf_counter() - t_start, 's', flush=True)

if __name__ == '__main__':
    main()
