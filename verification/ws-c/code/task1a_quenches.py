"""Task 1 part A — quenches Q1-Q3 (RK4 damped wave, T=50, N=16, L=pi).
Appends rows to results/task1_probe_results.csv (header created if missing).
Saves Q1 final state to results/task1_q1_final.npy for the top-6 extraction.
Usage: python task1a_quenches.py
"""
import csv
import os
import sys
import time

sys.path.insert(0, __file__.rsplit('/', 1)[0])
import numpy as np

import irh_models as M

OUT = os.path.join(os.path.dirname(__file__), '..', 'results')
os.makedirs(OUT, exist_ok=True)
CSV = os.path.join(OUT, 'task1_probe_results.csv')
FIELDS = ["model", "tag", "psibar0", "q02", "u", "seed", "psibar_final",
          "amp", "d4", "modes", "lock", "rms", "Fexc", "seconds"]


def append(row):
    new = not os.path.exists(CSV)
    with open(CSV, 'a', newline='') as f:
        w = csv.DictWriter(f, fieldnames=FIELDS)
        if new:
            w.writeheader()
        w.writerow(row)
    print(" | ".join(f"{k}={v}" for k, v in row.items()), flush=True)


for tag, pb0, q02, uu, seed in [("Q1", 0.00, 8.0, 1.0, 1),
                                ("Q2", -0.18, 8.0, 1.0, 1),
                                ("Q3", 0.00, 8.0, 0.0, 1)]:
    t0 = time.time()
    ph, d, grid = M.run_quench(psibar=pb0, q02=q02, u=uu, seed=seed,
                               dt=0.02, steps=2500)
    if tag == "Q1":
        np.save(os.path.join(OUT, 'task1_q1_final.npy'), ph)
    append(dict(model="dynamic-wave", tag=tag, psibar0=pb0, q02=q02, u=uu,
                seed=seed, psibar_final=round(d["psibar"], 5),
                amp=round(d["amp"], 5), d4=round(d["d4"], 4), modes=d["modes"],
                lock=round(d["lock"], 3), rms=round(d["rms"], 4),
                Fexc=round(d["Fexc"], 6), seconds=round(time.time() - t0, 1)))
print("PART A DONE", flush=True)
