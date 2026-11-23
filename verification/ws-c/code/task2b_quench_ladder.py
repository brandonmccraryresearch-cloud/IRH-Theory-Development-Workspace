"""Task 2 part B — quench ladder + seed sensitivity (RK4 damped wave, T=50, u=1).
N-ladder: N in {8,12,16} at dt=0.02. dt check: N=16 at dt=0.04.
Seeds {3,4,5} at N=16, dt=0.02 (seeds 1,2 already measured in Task 1: Q1, Q7).
Appends to results/task2_ladder.csv (quench rows) and
results/task2_input_sensitivity.csv (seed rows).
"""
import csv
import os
import sys
import time

sys.path.insert(0, __file__.rsplit('/', 1)[0])
import irh_models as M

OUT = os.path.join(os.path.dirname(__file__), '..', 'results')
CSV = os.path.join(OUT, 'task2_ladder.csv')
CSVS = os.path.join(OUT, 'task2_input_sensitivity.csv')
FIELDS = ["test", "N", "dt", "T", "u", "psibar_final", "psibar_drift", "amp",
          "amp_err", "amp_relerr", "d4", "modes", "lock", "rms", "Fexc",
          "Fexc_err_vs_relaxed", "seconds"]
SFIELDS = ["test", "seed", "psibar_final", "amp", "d4", "modes", "lock",
           "rms", "Fexc", "seconds"]


def append(path, fields, row):
    new = not os.path.exists(path)
    with open(path, 'a', newline='') as f:
        w = csv.DictWriter(f, fieldnames=fields)
        if new:
            w.writeheader()
        w.writerow(row)
    print(" | ".join(f"{k}={v}" for k, v in row.items()), flush=True)


for N, dt in [(8, 0.02), (12, 0.02), (16, 0.02), (16, 0.04)]:
    steps = int(50 / dt)
    t0 = time.time()
    _, d, _ = M.run_quench(N=N, dt=dt, steps=steps, seed=1, u=1.0)
    tag = "quench-N" if dt == 0.02 else "quench-dt"
    append(CSV, FIELDS, dict(test=tag, N=N, dt=dt, T=50, u=1.0,
                             psibar_final=round(d["psibar"], 5), psibar_drift="",
                             amp=round(d["amp"], 5), amp_err="", amp_relerr="",
                             d4=round(d["d4"], 4), modes=d["modes"],
                             lock=round(d["lock"], 3), rms=round(d["rms"], 4),
                             Fexc=round(d["Fexc"], 6), Fexc_err_vs_relaxed="",
                             seconds=round(time.time() - t0, 1)))

for seed in (3, 4, 5):
    t0 = time.time()
    _, d, _ = M.run_quench(seed=seed, dt=0.02, steps=2500, u=1.0)
    append(CSVS, SFIELDS, dict(test="quench-seed", seed=seed,
                               psibar_final=round(d["psibar"], 5),
                               amp=round(d["amp"], 5), d4=round(d["d4"], 4),
                               modes=d["modes"], lock=round(d["lock"], 3),
                               rms=round(d["rms"], 4), Fexc=round(d["Fexc"], 6),
                               seconds=round(time.time() - t0, 1)))
print("TASK2-B DONE", flush=True)
