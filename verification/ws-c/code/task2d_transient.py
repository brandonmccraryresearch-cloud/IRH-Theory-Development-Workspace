"""Task 2 part D — transient dt-convergence (attractor state is a fixed point,
so the seeded-at-A* ladder is degenerate: identical at every N and dt).
Seed at 1.2*A* (0.0931) and measure <A> at T=5 across dt; the relaxation
transient is where first-order time error shows. Richardson fit vs dt.
Writes results/task2_transient.csv.

Run-12 fix (EXP-1200 R-CODE, gap G-B2): the shipped version ran T=5 only and
overwrote the CSV with mode 'w', so the T=0.5/1.0 rows that make_figures.py
needs (fig 3a filters T == "0.5") could not be regenerated. The script now
loops over the horizons T in (5, 0.5, 1.0) -- the row order of the shipped
CSV -- with steps = round(T/dt), and writes all 12 rows. The *_at_T5 column
names are kept for compatibility; they hold the value at the row's horizon T.
err_vs_ref is taken per T against that T's dt=0.0025 row. amp_raw (full
precision amplitude) is appended so Richardson orders can be computed without
6-decimal rounding. err_vs_Astar follows the shipped mixed recipe: rounded amp
for the T=5 rows, raw amp for the T=0.5/1.0 rows (run-12 v-p0 VERDICT C1);
err_vs_ref for T=0.5/1.0 is taken against the raw reference amplitude.
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

# For each horizon T the dt=0.0025 run is the reference (smallest dt).
allrows = []
for T in (5, 0.5, 1.0):
    rows = []
    for dt in (0.02, 0.01, 0.005, 0.0025):
        steps = int(round(T / dt))
        t0 = time.time()
        ph, _, _, analyze = M.run_attractor(N=16, dt=dt, steps=steps,
                                            a_star=1.2 * A_STAR, hermitian=True)
        d = analyze(ph)
        row = dict(dt=dt, steps=steps, T=T, seed_amp=round(1.2 * A_STAR, 6),
                   amp_at_T5=round(d["amp"], 6), rms_at_T5=round(d["rms"], 6),
                   Fexc_at_T5=round(d["Fexc"], 6),
                   psibar_drift=round(abs(d["psibar"] + 0.18), 10),
                   seconds=round(time.time() - t0, 1))
        rows.append((row, repr(float(d["amp"]))))
        print(" | ".join(f"{k}={v}" for k, v in row.items()), flush=True)
    ref_amp = rows[-1][0]["amp_at_T5"]
    ref_raw = float(rows[-1][1])
    for r, raw in rows:
        r2 = dict(r)
        # err_vs_ref recipe as in the shipped CSV: T=5 rows round(rounded amp -
        # rounded ref); T=0.5/1.0 rows round(rounded amp - raw ref), which is
        # the only recipe that reproduces the shipped "-0.0" at T=0.5,
        # dt=0.0025 (run-12 w-p0fix amendment A1).
        if T == 5:
            r2["err_vs_ref"] = round(r["amp_at_T5"] - ref_amp, 6)
        else:
            r2["err_vs_ref"] = round(r["amp_at_T5"] - ref_raw, 6)
        # err_vs_Astar recipe as in the shipped CSV (v-p0 VERDICT C1):
        # T=5 rows were shipped as round(rounded amp - A*); the T=0.5/1.0
        # rows were shipped as round(raw amp - A*).
        if T == 5:
            r2["err_vs_Astar"] = round(r["amp_at_T5"] - A_STAR, 6)
        else:
            r2["err_vs_Astar"] = round(float(raw) - A_STAR, 6)
        r2["amp_raw"] = raw
        allrows.append(r2)

with open(CSV, 'w', newline='') as f:
    w = csv.DictWriter(f, fieldnames=FIELDS + ["err_vs_ref", "err_vs_Astar",
                                               "amp_raw"])
    w.writeheader()
    for r2 in allrows:
        w.writerow(r2)
print("TASK2-D DONE", flush=True)
