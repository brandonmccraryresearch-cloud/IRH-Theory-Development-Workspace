"""Task 2 part A — attractor ladders (Model B, Hermitian-projected, T=30).
N-ladder: N in {8,12,16,20} at dt=0.005. dt-ladder: dt in {0.02,0.01,0.005,0.0025}
at N=16. Reference: A* = 0.0775753, F/V relaxed = -0.0077276.
Appends to results/task2_ladder.csv.
"""
import csv
import os
import sys
import time

sys.path.insert(0, __file__.rsplit('/', 1)[0])
import irh_models as M

OUT = os.path.join(os.path.dirname(__file__), '..', 'results')
os.makedirs(OUT, exist_ok=True)
CSV = os.path.join(OUT, 'task2_ladder.csv')
A_STAR = 0.0775753
F_RELAXED = -0.0077276
FIELDS = ["test", "N", "dt", "T", "u", "psibar_final", "psibar_drift", "amp",
          "amp_err", "amp_relerr", "d4", "modes", "lock", "rms", "Fexc",
          "Fexc_err_vs_relaxed", "seconds"]


def append(row):
    new = not os.path.exists(CSV)
    with open(CSV, 'a', newline='') as f:
        w = csv.DictWriter(f, fieldnames=FIELDS)
        if new:
            w.writeheader()
        w.writerow(row)
    print(" | ".join(f"{k}={v}" for k, v in row.items()), flush=True)


for N in (8, 12, 16, 20):
    t0 = time.time()
    _, hist, _, _ = M.run_attractor(N=N, dt=0.005, steps=6000, hermitian=True)
    d = hist[-1]
    append(dict(test="attractor-N", N=N, dt=0.005, T=30, u=1.0,
                psibar_final=round(d["psibar"], 8),
                psibar_drift=round(abs(d["psibar"] + 0.18), 10),
                amp=round(d["amp"], 6), amp_err=round(d["amp"] - A_STAR, 6),
                amp_relerr=round((d["amp"] - A_STAR) / A_STAR, 6),
                d4=round(d["d4"], 6), modes=d["modes"], lock=round(d["lock"], 3),
                rms=round(d["rms"], 6), Fexc=round(d["Fexc"], 6),
                Fexc_err_vs_relaxed=round(d["Fexc"] - F_RELAXED, 6),
                seconds=round(time.time() - t0, 1)))

for dt in (0.02, 0.01, 0.005, 0.0025):
    steps = int(30 / dt)
    t0 = time.time()
    _, hist, _, _ = M.run_attractor(N=16, dt=dt, steps=steps, hermitian=True)
    d = hist[-1]
    append(dict(test="attractor-dt", N=16, dt=dt, T=30, u=1.0,
                psibar_final=round(d["psibar"], 8),
                psibar_drift=round(abs(d["psibar"] + 0.18), 10),
                amp=round(d["amp"], 6), amp_err=round(d["amp"] - A_STAR, 6),
                amp_relerr=round((d["amp"] - A_STAR) / A_STAR, 6),
                d4=round(d["d4"], 6), modes=d["modes"], lock=round(d["lock"], 3),
                rms=round(d["rms"], 6), Fexc=round(d["Fexc"], 6),
                Fexc_err_vs_relaxed=round(d["Fexc"] - F_RELAXED, 6),
                seconds=round(time.time() - t0, 1)))
print("TASK2-A DONE", flush=True)
