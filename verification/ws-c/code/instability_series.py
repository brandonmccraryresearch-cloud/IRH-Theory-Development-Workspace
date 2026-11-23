"""Instability time series for the figure: <A>(t) for the shipped-style
Model B update WITHOUT Hermitian projection (blows up) vs WITH projection
(stable). N=16, dt=0.005, seeded at A*=0.0776, psibar=-0.18. Records every
100 steps. Unprojected run stops at first non-finite value.
Appends to results/instability_series.csv.
"""
import csv
import os
import sys
import time

sys.path.insert(0, __file__.rsplit('/', 1)[0])
import numpy as np

import irh_models as M

OUT = os.path.join(os.path.dirname(__file__), '..', 'results')
CSV = os.path.join(OUT, 'instability_series.csv')


def series(hermitian, steps=6000):
    grid = M.Grid(16, np.pi)
    K2 = grid.K2
    omega2 = -0.35 + (8.0 - K2) ** 2
    vecs = M.d4_roots()
    analyze, _ = M.make_analyzer(grid, 8.0, -0.35, 1.0, 1.0, vecs)
    ph = np.zeros((16,) * 4, complex)
    ph[0, 0, 0, 0] = -0.18 * 16 ** 4
    for n in vecs:
        ph[grid.gidx(n)] = 0.0776 * 16 ** 4
    dt = 0.005
    rows = []
    for step in range(0, steps + 1):
        if step % 100 == 0:
            d = analyze(ph)
            rows.append(dict(hermitian=int(hermitian), t=round(step * dt, 3),
                             amp=d["amp"], rms=d["rms"], d4=d["d4"],
                             psibar=d["psibar"]))
            if not np.isfinite(d["amp"]):
                print(f"hermitian={hermitian} nonfinite at t={step*dt}", flush=True)
                break
        if step == steps:
            break
        den = 1.0 + dt * K2 * omega2
        p = np.fft.ifftn(ph).real
        nl = K2 * np.fft.fftn(p * p - p * p * p)
        ph = (ph + dt * nl) / den
        if hermitian:
            ph = np.fft.fftn(np.fft.ifftn(ph).real)
    return rows


all_rows = []
for h in (False, True):
    t0 = time.time()
    rows = series(h)
    print(f"hermitian={h}: {len(rows)} points, last t={rows[-1]['t']}, "
          f"amp={rows[-1]['amp']:.6g}, {time.time()-t0:.0f}s", flush=True)
    all_rows.extend(rows)

with open(CSV, 'w', newline='') as f:
    w = csv.DictWriter(f, fieldnames=["hermitian", "t", "amp", "rms", "d4", "psibar"])
    w.writeheader()
    w.writerows(all_rows)
print("INSTABILITY SERIES DONE", flush=True)
