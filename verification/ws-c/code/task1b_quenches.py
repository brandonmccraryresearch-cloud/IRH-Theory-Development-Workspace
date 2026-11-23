"""Task 1 part B — quenches Q4-Q7 (RK4 damped wave, T=50, N=16, L=pi).
Appends rows to results/task1_probe_results.csv.
Usage: python task1b_quenches.py
"""
import csv
import os
import sys
import time

sys.path.insert(0, __file__.rsplit('/', 1)[0])
import irh_models as M

OUT = os.path.join(os.path.dirname(__file__), '..', 'results')
CSV = os.path.join(OUT, 'task1_probe_results.csv')
FIELDS = ["model", "tag", "psibar0", "q02", "u", "seed", "psibar_final",
          "amp", "d4", "modes", "lock", "rms", "Fexc", "seconds"]


def append(row):
    with open(CSV, 'a', newline='') as f:
        w = csv.DictWriter(f, fieldnames=FIELDS)
        w.writerow(row)
    print(" | ".join(f"{k}={v}" for k, v in row.items()), flush=True)


for tag, pb0, q02, uu, seed in [("Q4", -0.18, 7.5, 1.0, 1),
                                ("Q5", -0.30, 8.0, 1.0, 1),
                                ("Q6", +0.10, 8.0, 1.0, 1),
                                ("Q7", -0.18, 8.0, 1.0, 2)]:
    t0 = time.time()
    ph, d, grid = M.run_quench(psibar=pb0, q02=q02, u=uu, seed=seed,
                               dt=0.02, steps=2500)
    append(dict(model="dynamic-wave", tag=tag, psibar0=pb0, q02=q02, u=uu,
                seed=seed, psibar_final=round(d["psibar"], 5),
                amp=round(d["amp"], 5), d4=round(d["d4"], 4), modes=d["modes"],
                lock=round(d["lock"], 3), rms=round(d["rms"], 4),
                Fexc=round(d["Fexc"], 6), seconds=round(time.time() - t0, 1)))
print("PART B DONE", flush=True)
