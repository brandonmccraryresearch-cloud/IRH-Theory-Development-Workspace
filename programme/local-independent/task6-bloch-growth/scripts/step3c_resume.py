#!/usr/bin/env python3
"""Step 3c (Task 6): resume the Kb=4 map (randomBZ_096..149) and finish the
post-map steps of step3b (Goldstone overlaps, C6, C4b, C5b, fits) using the
already-written data/bloch_map_Kb4.csv (208 rows). Same spectra_fast routine
as step3b, so numbers are directly comparable."""
import os
for k in ('OMP_NUM_THREADS', 'OPENBLAS_NUM_THREADS', 'MKL_NUM_THREADS'):
    os.environ[k] = '1'
import csv, importlib.util, json, time
from pathlib import Path
import numpy as np

BASE = Path('/home/hatch/workspace/research/irh/co-scientist-tasks-2026-11-10')
WORK = BASE / 'local-independent/task6-bloch-growth'
R, MEAN, Q2 = -0.35, -0.18, 8.0
KB = 4

def load_mod(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
    return m

s3 = load_mod('s3', WORK / 'scripts/step3_bloch_kb4.py')
s3b = load_mod('s3b', WORK / 'scripts/step3b_bloch_kb4_fast.py')

def main():
    t_start = time.perf_counter()
    a4, E4, rhs4 = s3.load_relaxed('K4')
    a6, E6, rhs6 = s3.load_relaxed('K6')
    W4 = s3.build_W(a4); W6 = s3.build_W(a6)
    pts, Hoff, W0, kept, _ = s3.assemble_H(KB, W4)
    sec = s3.sectors(pts)
    blocks = s3b.sector_blocks(pts, Hoff, sec)
    print(f'assembly done {time.perf_counter()-t_start:.1f}s', flush=True)

    # --- resume random sample ---
    existing = list(csv.DictReader(open(WORK / 'data/bloch_map_Kb4.csv')))
    done_labels = {r['label'] for r in existing}
    rng = np.random.default_rng(20261114)
    missing = []
    for i in range(150):
        q = tuple(float(x) for x in rng.uniform(0, 0.5, 4))
        lab = f'randomBZ_{i:03d}'
        if lab not in done_labels:
            missing.append((q, lab))
    print(f'existing rows={len(existing)} missing random={len(missing)}', flush=True)
    fields = ['q0', 'q1', 'q2', 'q3', 'qnorm', 'label', 'Kb', 'lam_max', 'lam2', 'lam3',
              'lam4', 'lam5', 'lam6', 'dom1', 'dompow1', 'lam_mean', 'mean_power', 'mean_dom_n']
    rows = list(existing)
    with open(WORK / 'data/bloch_map_Kb4.csv', 'a', newline='') as f:
        w = csv.DictWriter(f, fieldnames=fields)
        for q, label in missing:
            recs, d = s3b.spectra_fast(q, pts, W0, blocks)
            a = s3b.analyse(recs, d, pts)
            row = dict(q0=q[0], q1=q[1], q2=q[2], q3=q[3], qnorm=float(np.linalg.norm(q)),
                       label=label, Kb=4, lam_max=a['lam1'], lam2=a['lam2'], lam3=a['lam3'],
                       lam4=a['lam4'], lam5=a['lam5'], lam6=a['lam6'],
                       dom1=a['dom1'], dompow1=a['dompow1'],
                       lam_mean=a.get('lam_mean', ''), mean_power=a.get('mean_power', ''),
                       mean_dom_n=a.get('mean_dom_n', ''))
            w.writerow(row); f.flush()
            rows.append(row)
    print(f'map complete rows={len(rows)} elapsed={time.perf_counter()-t_start:.1f}s', flush=True)

    # --- C1b / C3b (recompute, cheap-ish: one spectra_fast + eigvalsh) ---
    afull = dict(a4); afull[(0, 0, 0, 0)] = MEAN
    recs0, d0 = s3b.spectra_fast((0, 0, 0, 0), pts, W0, blocks)
    lam0 = [r['lam'] for r in recs0]
    Karr = np.array(pts, dtype=float); darr = np.sum(Karr * Karr, axis=1)
    H0 = Hoff + np.diag(R + (Q2 - darr) ** 2 + W0)
    gold = []
    for j in range(4):
        v = np.array([1j * k[j] * afull.get(k, 0.0) for k in pts], dtype=complex)
        gold.append(float(np.linalg.norm(H0 @ v) / np.linalg.norm(v)))
    ev_idx = np.array(sec[(0, 0, 0, 0)])
    Hev = H0[np.ix_(ev_idx, ev_idx)]
    zpos = list(ev_idx).index(pts.index((0, 0, 0, 0)))
    rest = [i for i in range(len(ev_idx)) if i != zpos]
    H00 = Hev[zpos, zpos]; H0Q = Hev[zpos, rest]; HQQ = Hev[np.ix_(rest, rest)]
    S = float(H00 - H0Q @ np.linalg.solve(HQQ, H0Q))
    checks = {}
    checks['C1b_goldstone_Hv_over_v'] = gold
    checks['C1b_lam0_top10'] = lam0[:10]
    checks['C3b'] = dict(H00=float(H00), HQQ_min_eig=float(np.linalg.eigvalsh(HQQ)[0]),
                         Hev_min_eig=float(np.linalg.eigvalsh(Hev)[0]), Schur_S=S,
                         pred_lambda_over_q2=-S)
    print('C1b:', gold, 'C3b S:', S, flush=True)

    # --- Goldstone overlaps ---
    vecs = []
    for j in range(4):
        v = np.array([1j * k[j] * afull.get(k, 0.0) for k in pts], dtype=complex)
        vecs.append(v / np.linalg.norm(v))
    orows = []
    for q, label in [((0.05, 0, 0, 0), 'axis0.05'), ((0.1, 0, 0, 0), 'axis0.10'),
                     ((0.15, 0, 0, 0), 'axis0.15'), ((0.05, 0.05, 0, 0), 'diag110_0.05'),
                     ((0.1, 0.1, 0, 0), 'diag110_0.10'), ((0.05, 0.05, 0.05, 0.05), 'diag1111_0.05')]:
        recs, d = s3b.spectra_fast(q, pts, W0, blocks)
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
    print('overlaps written', len(orows), flush=True)

    # --- C6 ---
    c6 = []
    for q, q2, lab in [((0.2, 0.1, 0, 0), (0.1, 0.2, 0, 0), 'perm12'),
                       ((0.2, 0.1, 0, 0), (-0.2, 0.1, 0, 0), 'signflip'),
                       ((0.3, 0.2, 0.1, 0.05), (0.05, 0.1, 0.2, 0.3), 'perm_rev')]:
        r1, _ = s3b.spectra_fast(q, pts, W0, blocks)
        r2, _ = s3b.spectra_fast(q2, pts, W0, blocks)
        l1 = np.array([r['lam'] for r in r1[:6]]); l2 = np.array([r['lam'] for r in r2[:6]])
        c6.append(dict(q=list(q), q2=list(q2), label=lab, max_top6_diff=float(np.max(np.abs(l1 - l2)))))
    checks['C6_symmetry'] = c6
    print('C6:', c6, flush=True)

    # --- C4b ---
    kb2 = {}
    for r in csv.DictReader(open(WORK / 'data/bloch_coarse_Kb2.csv')):
        kb2[(float(r['q0']), float(r['q1']), float(r['q2']), float(r['q3']))] = r
    rowmap = {(round(float(r['q0']), 6), round(float(r['q1']), 6), round(float(r['q2']), 6), round(float(r['q3']), 6)): r for r in rows}
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

    # --- C5b ---
    pts6, Hoff6, W06, kept6, _ = s3.assemble_H(KB, W6)
    blocks6 = s3b.sector_blocks(pts6, Hoff6, s3.sectors(pts6))
    c5b = []
    for q in [(0.0, 0, 0, 0), (0.1, 0, 0, 0), (0.25, 0, 0, 0), (0.5, 0, 0, 0),
              (0.25, 0.25, 0, 0), (0.5, 0.5, 0.5, 0.5), (0.3, 0.3, 0.3, 0)]:
        r6, _ = s3b.spectra_fast(q, pts6, W06, blocks6)
        l6 = [r['lam'] for r in r6[:3]]
        r4 = rowmap.get(tuple(round(x, 6) for x in q))
        c5b.append(dict(q=list(q), Kb4_K4_lam_max=float(r4['lam_max']) if r4 else None,
                        Kb4_K6_lam_max=float(l6[0]),
                        diff=float(l6[0]) - float(r4['lam_max']) if r4 else None,
                        K6_lam2=float(l6[1])))
    checks['C5b_K4_vs_K6_Kb4'] = c5b
    print('C5b:', c5b, flush=True)

    # --- fits ---
    axis_rows = [r for r in rows if r['label'] == 'axis_e1' and 0 < float(r['q0']) <= 0.15]
    axis_rows.sort(key=lambda r: float(r['q0']))
    def fit_slope(rs, key):
        x = np.array([float(r['qnorm']) ** 2 for r in rs]); y = np.array([float(r[key]) for r in rs])
        return float(np.sum(x * y) / np.sum(x * x))
    checks['fits_axis'] = dict(
        transverse_slope_lam_max_vs_q2=fit_slope(axis_rows, 'lam_max'),
        mean_slope_lam_mean_vs_q2=fit_slope(axis_rows, 'lam_mean'),
        schur_pred=-checks['C3b']['Schur_S'],
        axis_points=[[float(r['q0']), float(r['lam_max']), float(r['lam_mean'])] for r in axis_rows])
    print('fits_axis:', checks['fits_axis'], flush=True)

    results = dict(checks=checks, map_rows=len(rows), elapsed_s=time.perf_counter() - t_start)
    (WORK / 'data/bloch_checks_Kb4.json').write_text(json.dumps(results, indent=2, default=str))
    print('done in', time.perf_counter() - t_start, 's', flush=True)

if __name__ == '__main__':
    main()
