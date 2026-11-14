#!/usr/bin/env python3
"""Step 3b (Task 6): Kb=4 Bloch map, fast version.
Sector blocks of Hoff are precomputed once; per q only the diagonal changes.
Rows are written to CSV incrementally (flush every row) so a timeout cannot
lose the map. Reuses load_relaxed/build_W/assemble_H/sectors from step3.
Also: Goldstone-overlap table at selected small q, C3b, C4b, C5b, fits.
Pinned seed: default_rng(20261114) for the random-BZ sample.
"""
import os
for k in ('OMP_NUM_THREADS', 'OPENBLAS_NUM_THREADS', 'MKL_NUM_THREADS'):
    os.environ[k] = '1'
import csv, importlib.util, itertools, json, time
from pathlib import Path
import numpy as np

BASE = Path('/home/hatch/workspace/research/irh/co-scientist-tasks-2026-11-10')
WORK = BASE / 'local-independent/task6-bloch-growth'
R, MEAN, Q2 = -0.35, -0.18, 8.0
KB = 4

spec = importlib.util.spec_from_file_location('s3', WORK / 'scripts/step3_bloch_kb4.py')
s3 = importlib.util.module_from_spec(spec); spec.loader.exec_module(s3)

def sector_blocks(pts, Hoff, sec):
    blocks = {}
    for key, idx in sec.items():
        idx = np.array(idx)
        blocks[key] = (idx, Hoff[np.ix_(idx, idx)])
    return blocks

def spectra_fast(q, pts, W0, blocks):
    """Return recs (sorted desc) using precomputed Hoff sector blocks.
    Each rec: dict(lam, Ycol, idx). q=0: n=0 excluded from the even sector."""
    q = np.array(q, dtype=float)
    K = np.array(pts, dtype=float)
    d = np.sum((K + q) ** 2, axis=1)
    recs = []
    for key, (idx, Hsec) in blocks.items():
        idx_use = idx
        if np.all(q == 0) and key == (0, 0, 0, 0):
            zpos = int(np.where(idx == pts.index((0, 0, 0, 0)))[0][0])
            keep = [j for j in range(len(idx)) if j != zpos]
            idx_use = idx[keep]
            Hsec = Hsec[np.ix_(keep, keep)]
        dd = d[idx_use]
        rs = np.sqrt(dd)
        Bs = -(rs[:, None] * Hsec * rs[None, :])
        dg = R + (Q2 - dd) ** 2 + W0
        Bs[np.diag_indices_from(Bs)] -= dd * dg
        Bs = (Bs + Bs.T) / 2
        lam, Y = np.linalg.eigh(Bs)
        for j in range(len(lam)):
            recs.append(dict(lam=float(lam[j]), Ycol=Y[:, j], idx=idx_use))
    recs.sort(key=lambda r: -r['lam'])
    return recs, d

def analyse(recs, d, pts, n_top=6):
    out = {}
    for i, r in enumerate(recs[:n_top]):
        h = np.sqrt(d[r['idx']]) * r['Ycol']
        h = h / np.linalg.norm(h)
        pw = np.abs(h) ** 2
        out[f'lam{i+1}'] = r['lam']
        out[f'dom{i+1}'] = str(pts[int(r['idx'][int(np.argmax(pw))])])
        out[f'dompow{i+1}'] = float(pw.max())
    if (0, 0, 0, 0) in pts:
        i0 = pts.index((0, 0, 0, 0))
        best = None
        for r in recs:
            if i0 not in r['idx']:
                continue
            pos = int(np.where(r['idx'] == i0)[0][0])
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
    a4, E4, rhs4 = s3.load_relaxed('K4')
    a6, E6, rhs6 = s3.load_relaxed('K6')
    W4 = s3.build_W(a4); W6 = s3.build_W(a6)
    t0 = time.perf_counter()
    pts, Hoff, W0, kept, max_im = s3.assemble_H(KB, W4)
    sec = s3.sectors(pts)
    blocks = sector_blocks(pts, Hoff, sec)
    print(f'assembly {time.perf_counter()-t0:.1f}s n={len(pts)} kept={kept}', flush=True)
    checks = {}

    # C1b + C3b (as in step3, using full H0)
    afull = dict(a4); afull[(0, 0, 0, 0)] = MEAN
    recs0, d0 = spectra_fast((0, 0, 0, 0), pts, W0, blocks)
    lam0 = [r['lam'] for r in recs0]
    Karr = np.array(pts, dtype=float); darr = np.sum(Karr * Karr, axis=1)
    H0 = Hoff + np.diag(R + (Q2 - darr) ** 2 + W0)
    gold = []
    for j in range(4):
        v = np.array([1j * k[j] * afull.get(k, 0.0) for k in pts], dtype=complex)
        gold.append(float(np.linalg.norm(H0 @ v) / np.linalg.norm(v)))
    checks['C1b_goldstone_Hv_over_v'] = gold
    checks['C1b_lam0_top10'] = lam0[:10]
    print('C1b:', [f'{g:.2e}' for g in gold], 'lam0 top6:', [f'{x:+.2e}' for x in lam0[:6]], flush=True)
    ev_idx = np.array(sec[(0, 0, 0, 0)])
    Hev = H0[np.ix_(ev_idx, ev_idx)]
    zpos = list(ev_idx).index(pts.index((0, 0, 0, 0)))
    rest = [i for i in range(len(ev_idx)) if i != zpos]
    H00 = Hev[zpos, zpos]; H0Q = Hev[zpos, rest]; HQQ = Hev[np.ix_(rest, rest)]
    emin_qq = float(np.linalg.eigvalsh(HQQ)[0]); emin_ev = float(np.linalg.eigvalsh(Hev)[0])
    S = float(H00 - H0Q @ np.linalg.solve(HQQ, H0Q))
    checks['C3b'] = dict(H00=float(H00), HQQ_min_eig=emin_qq, Hev_min_eig=emin_ev,
                         Schur_S=S, pred_lambda_over_q2=-S)
    print(f'C3b S={S:.6f} HQQ_min={emin_qq:.2e} Hev_min={emin_ev:.2e}', flush=True)

    # q grid
    qpoints = []
    def add_q(q, label):
        qpoints.append((tuple(float(x) for x in q), label))
    for t in [0.0, 0.025, 0.05, 0.075, 0.1, 0.125, 0.15, 0.2, 0.25, 0.3, 0.35, 0.4, 0.45, 0.5]:
        add_q((t, 0, 0, 0), 'axis_e1')
    for t in [0.025, 0.05, 0.075, 0.1, 0.125, 0.15, 0.2, 0.25, 0.3, 0.35]:
        add_q((t, t, 0, 0), 'diag110'); add_q((t, t, t, 0), 'diag1110'); add_q((t, t, t, t), 'diag1111')
    for t in [0.02, 0.04, 0.06, 0.08, 0.12, 0.14, 0.16, 0.18, 0.22, 0.24, 0.26, 0.28, 0.32, 0.34, 0.36, 0.38, 0.42, 0.44, 0.46, 0.48]:
        add_q((t, 0, 0, 0), 'axis_fine')
        add_q((t, t, t, 0), 'diag1110_fine')
    for t in [0.05, 0.1, 0.15, 0.2, 0.25, 0.3, 0.35, 0.4, 0.45, 0.5]:
        add_q((0.5, t, 0, 0), 'face_0.5_t'); add_q((t, 0.5, 0.5, 0), 'corner_t55')
    for q, lab in [((0.5, 0.5, 0, 0), 'zone_M110'), ((0.5, 0.5, 0.5, 0), 'zone_M1110'),
                   ((0.5, 0.5, 0.5, 0.5), 'zone_R1111'), ((0.5, 0, 0, 0), 'zone_X100'),
                   ((0.3, 0.1, 0, 0), 'generic_a'), ((0.2, 0.35, 0.1, 0), 'generic_b'),
                   ((0.4, 0.2, 0.3, 0.1), 'generic_c'), ((0.15, 0.45, 0.2, 0.05), 'generic_d')]:
        add_q(q, lab)
    rng = np.random.default_rng(20261114)
    for i in range(150):
        add_q(tuple(rng.uniform(0, 0.5, 4)), f'randomBZ_{i:03d}')

    fields = ['q0', 'q1', 'q2', 'q3', 'qnorm', 'label', 'Kb', 'lam_max', 'lam2', 'lam3',
              'lam4', 'lam5', 'lam6', 'dom1', 'dompow1', 'lam_mean', 'mean_power', 'mean_dom_n']
    fmap = open(WORK / 'data/bloch_map_Kb4.csv', 'w', newline='')
    w = csv.DictWriter(fmap, fieldnames=fields); w.writeheader()
    rows = []
    for q, label in qpoints:
        recs, d = spectra_fast(q, pts, W0, blocks)
        a = analyse(recs, d, pts)
        row = dict(q0=q[0], q1=q[1], q2=q[2], q3=q[3], qnorm=float(np.linalg.norm(q)),
                   label=label, Kb=4, lam_max=a['lam1'], lam2=a['lam2'], lam3=a['lam3'],
                   lam4=a['lam4'], lam5=a['lam5'], lam6=a['lam6'],
                   dom1=a['dom1'], dompow1=a['dompow1'],
                   lam_mean=a.get('lam_mean', ''), mean_power=a.get('mean_power', ''),
                   mean_dom_n=a.get('mean_dom_n', ''))
        w.writerow(row); fmap.flush()
        rows.append(row)
    fmap.close()
    print(f'map rows={len(rows)} elapsed={time.perf_counter()-t_start:.1f}s', flush=True)

    # Goldstone overlaps at small q (top-6 eigenvectors vs d_j psi*)
    vecs = []
    for j in range(4):
        v = np.array([1j * k[j] * afull.get(k, 0.0) for k in pts], dtype=complex)
        vecs.append(v / np.linalg.norm(v))
    orows = []
    for q, label in [((0.05, 0, 0, 0), 'axis0.05'), ((0.1, 0, 0, 0), 'axis0.10'),
                     ((0.15, 0, 0, 0), 'axis0.15'), ((0.05, 0.05, 0, 0), 'diag110_0.05'),
                     ((0.1, 0.1, 0, 0), 'diag110_0.10'), ((0.05, 0.05, 0.05, 0.05), 'diag1111_0.05')]:
        recs, d = spectra_fast(q, pts, W0, blocks)
        for rank, r in enumerate(recs[:6], start=1):
            h = np.zeros(len(pts))
            h[r['idx']] = np.sqrt(d[r['idx']]) * r['Ycol']
            h = h / np.linalg.norm(h)
            ov = [float(abs(np.vdot(vecs[j], h)) ** 2) for j in range(4)]
            orows.append(dict(q0=q[0], q1=q[1], q2=q[2], q3=q[3], label=label, rank=rank,
                              lam=r['lam'], ov_d1=ov[0], ov_d2=ov[1], ov_d3=ov[2], ov_d4=ov[3],
                              ov_sum=sum(ov)))
    with open(WORK / 'data/goldstone_overlaps.csv', 'w', newline='') as f:
        ww = csv.DictWriter(f, fieldnames=list(orows[0])); ww.writeheader(); ww.writerows(orows)
    print('goldstone overlaps written', len(orows), flush=True)

    # C6 symmetry
    c6 = []
    for q, q2, lab in [((0.2, 0.1, 0, 0), (0.1, 0.2, 0, 0), 'perm12'),
                       ((0.2, 0.1, 0, 0), (-0.2, 0.1, 0, 0), 'signflip'),
                       ((0.3, 0.2, 0.1, 0.05), (0.05, 0.1, 0.2, 0.3), 'perm_rev')]:
        r1, _ = spectra_fast(q, pts, W0, blocks)
        r2, _ = spectra_fast(q2, pts, W0, blocks)
        l1 = np.array([r['lam'] for r in r1[:6]]); l2 = np.array([r['lam'] for r in r2[:6]])
        c6.append(dict(q=list(q), q2=list(q2), label=lab, max_top6_diff=float(np.max(np.abs(l1 - l2)))))
    checks['C6_symmetry'] = c6
    print('C6:', c6, flush=True)

    # C4b: Kb=4 vs Kb=2
    kb2 = {}
    for r in csv.DictReader(open(WORK / 'data/bloch_coarse_Kb2.csv')):
        kb2[(float(r['q0']), float(r['q1']), float(r['q2']), float(r['q3']))] = r
    rowmap = {(round(r['q0'], 6), round(r['q1'], 6), round(r['q2'], 6), round(r['q3'], 6)): r for r in rows}
    c4b = []
    for q in [(0.0, 0, 0, 0), (0.05, 0, 0, 0), (0.1, 0, 0, 0), (0.25, 0, 0, 0),
              (0.5, 0, 0, 0), (0.25, 0.25, 0, 0), (0.5, 0.5, 0.5, 0.5),
              (0.3, 0.3, 0.3, 0), (0.2, 0.35, 0.1, 0)]:
        r4 = rowmap.get(tuple(round(x, 6) for x in q)); r2 = kb2.get(q)
        if r4 is None or r2 is None:
            continue
        c4b.append(dict(q=list(q), Kb4_lam_max=float(r4['lam_max']), Kb2_lam_max=float(r2['lam_max']),
                        diff=float(r4['lam_max']) - float(r2['lam_max']),
                        Kb4_lam_mean=r4['lam_mean'], Kb2_lam_mean=r2['lam_mean']))
    checks['C4b_Kb4_vs_Kb2'] = c4b
    print('C4b:', c4b, flush=True)

    # C5b: K6-relaxed W at Kb=4
    pts6, Hoff6, W06, kept6, _ = s3.assemble_H(KB, W6)
    blocks6 = sector_blocks(pts6, Hoff6, s3.sectors(pts6))
    c5b = []
    for q in [(0.0, 0, 0, 0), (0.1, 0, 0, 0), (0.25, 0, 0, 0), (0.5, 0, 0, 0),
              (0.25, 0.25, 0, 0), (0.5, 0.5, 0.5, 0.5), (0.3, 0.3, 0.3, 0)]:
        r6, _ = spectra_fast(q, pts6, W06, blocks6)
        l6 = [r['lam'] for r in r6[:3]]
        r4 = rowmap.get(tuple(round(x, 6) for x in q))
        c5b.append(dict(q=list(q), Kb4_K4_lam_max=float(r4['lam_max']) if r4 else None,
                        Kb4_K6_lam_max=float(l6[0]),
                        diff=float(l6[0]) - float(r4['lam_max']) if r4 else None,
                        K6_lam2=float(l6[1])))
    checks['C5b_K4_vs_K6_Kb4'] = c5b
    print('C5b:', c5b, flush=True)

    # Fits
    axis_rows = [r for r in rows if r['label'] == 'axis_e1' and 0 < r['q0'] <= 0.15]
    axis_rows.sort(key=lambda r: r['q0'])
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
