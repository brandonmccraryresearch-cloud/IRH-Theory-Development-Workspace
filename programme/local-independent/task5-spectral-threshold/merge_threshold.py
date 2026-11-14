#!/usr/bin/env python3
"""Merge per-batch threshold outcomes into the work-dir tables.

Reads threshold_outcomes.csv from the main directory and from each
batch sub-directory listed below, copies every per-run NPZ checkpoint
into the main directory, de-duplicates by (s_value, replicate), and
rewrites threshold_outcomes.csv and threshold_summary.csv (with Wilson
95% intervals) in the main directory. Also writes threshold_estimate.json
with the pre-registered bracket estimators:
  s_last_zero = largest s with recovery fraction 0
  s_first_full = smallest s with recovery fraction 1
  s50 = linear interpolation in s between the two adjacent grid points
        bracketing recovery fraction 0.5 (first crossing only)
No run is re-integrated here.
"""
import csv, json, shutil
from pathlib import Path
import numpy as np

OUT = Path(__file__).resolve().parent
BATCHES = ['batch_low', 'batch_midlow', 'batch_midhigh', 'batch_high',
           'dense_0075', 'dense_010', 'dense_0125']


def wilson(k, n, z=1.959964):
    if n == 0:
        return 0.0, 0.0
    ph = k / n
    den = 1 + z * z / n
    cen = ph + z * z / (2 * n)
    rad = z * np.sqrt(ph * (1 - ph) / n + z * z / (4 * n * n))
    return float((cen - rad) / den), float((cen + rad) / den)


def read_csv(path):
    with path.open() as f:
        return list(csv.DictReader(f))


def main():
    rows = {}
    for src in ['.'] + BATCHES:
        p = OUT / src / 'threshold_outcomes.csv'
        if not p.exists():
            print('MISSING', p)
            continue
        for r in read_csv(p):
            key = (float(r['s_value']), int(r['replicate']))
            if key in rows and rows[key]['run_id'] != r['run_id']:
                print('DUPLICATE KEY', key)
            rows[key] = r
    # Copy NPZ checkpoints into the main directory.
    for src in BATCHES:
        for npz in (OUT / src).glob('*.npz'):
            dest = OUT / npz.name
            if not dest.exists():
                shutil.copy2(npz, dest)
    outcomes = [rows[k] for k in sorted(rows)]
    fields = list(outcomes[0].keys())
    with (OUT / 'threshold_outcomes.csv').open('w', newline='') as f:
        w = csv.DictWriter(f, fieldnames=fields)
        w.writeheader()
        w.writerows(outcomes)
    summary = []
    for s in sorted({float(r['s_value']) for r in outcomes}):
        rr = [r for r in outcomes if float(r['s_value']) == s]
        k = sum(1 for r in rr if r['outcome'] == 'stationary_full24')
        lo, hi = wilson(k, len(rr))
        summary.append(dict(
            s_value=s, n=len(rr), full24=k,
            uniform=sum(1 for r in rr if r['outcome'] == 'uniform'),
            other=sum(1 for r in rr if r['outcome'] not in
                      ('stationary_full24', 'uniform')),
            recovery_fraction=k / len(rr),
            wilson_lo=lo, wilson_hi=hi,
            mean_initial_energy=float(np.mean([float(r['initial_energy']) for r in rr])),
            mean_elapsed_seconds=float(np.mean([float(r['elapsed_seconds']) for r in rr]))))
    with (OUT / 'threshold_summary.csv').open('w', newline='') as f:
        w = csv.DictWriter(f, fieldnames=list(summary[0]))
        w.writeheader()
        w.writerows(summary)
    # Pre-registered bracket estimators (first crossing only).
    fr = {r['s_value']: r['recovery_fraction'] for r in summary}
    zeros = [s for s, f in fr.items() if f == 0.0]
    fulls = [s for s, f in fr.items() if f == 1.0]
    s_last_zero = max(zeros) if zeros else None
    s_first_full = min(fulls) if fulls else None
    s50 = None
    pts = sorted(fr.items())
    for (s0, f0), (s1, f1) in zip(pts, pts[1:]):
        if f0 < 0.5 <= f1:
            s50 = float(s0 + (0.5 - f0) * (s1 - s0) / (f1 - f0)) if f1 != f0 else float(s1)
            break
    est = dict(n_runs=len(outcomes), n_points=len(summary),
               s_last_zero=s_last_zero, s_first_full=s_first_full,
               s50_linear_interpolation=s50,
               threshold_bracket=[s_last_zero, s_first_full],
               summary=summary)
    (OUT / 'threshold_estimate.json').write_text(json.dumps(est, indent=2) + '\n')
    print(json.dumps(est, indent=2))


if __name__ == '__main__':
    main()
