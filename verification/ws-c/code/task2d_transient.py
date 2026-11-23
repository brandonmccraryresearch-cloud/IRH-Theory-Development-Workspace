"""Task 2 part D — transient dt-convergence (attractor state is a fixed point,
so the seeded-at-A* ladder is degenerate: identical at every N and dt).
Seed at 1.2*A* (0.0931) and measure <A> at T=5 across dt; the relaxation
transient is where first-order time error shows. Richardson fit vs dt.
Appends to results/task2_transient.csv.
"""
import csv
import os
import sys
import time

sys.path.insert(0, __file__.rsplit('/', 1)[0])
import numpy as np

import irh_models as M

OUT = os.path.join(os.path.dirname(__file__), '..', 'results')
CSV = os.path.join(OUT, 'task2_transient.csv')
A_STAR = 0.0775753
FIELDS = ["dt", "steps", "T", "seed_amp", "amp_at_T5", "rms_at_T5", "Fexc_at_T5",
          "psibar_drift", "seconds"]

# The dt=0.0025 run at T=5 is the reference (smallest dt).
ref = None
rows = []
for dt in (0.02, 0.01, 0.005, 0.0025):
    steps = int(5 / dt)
    t0 = time.time()
    ph, _, _, analyze = M.run_attractor(N=16, dt=dt, steps=steps,
                                        a_star=1.2 * A_STAR, hermitian=True)
    d = analyze(ph)
    row = dict(dt=dt, steps=steps, T=5, seed_amp=round(1.2 * A_STAR, 6),
               amp_at_T5=round(d["amp"], 6), rms_at_T5=round(d["rms"], 6),
               Fexc_at_T5=round(d["Fexc"], 6),
               psibar_drift=round(abs(d["psibar"] + 0.18), 10),
               seconds=round(time.time() - t0, 1))
    rows.append(row)
    print(" | ".join(f"{k}={v}" for k, v in row.items()), flush=True)

ref_amp = rows[-1]["amp_at_T5"]
new = not os.path.exists(CSV)
with open(CSV, 'w', newline='') as f:
    w = csv.DictWriter(f, fieldnames=FIELDS + ["err_vs_ref", "err_vs_Astar"])
    w.writeheader()
    for r in rows:
        r2 = dict(r)
        r2["err_vs_ref"] = round(r["amp_at_T5"] - ref_amp, 6)
        r2["err_vs_Astar"] = round(r["amp_at_T5"] - A_STAR, 6)
        w.writerow(r2)
print("TASK2-D DONE", flush=True)
