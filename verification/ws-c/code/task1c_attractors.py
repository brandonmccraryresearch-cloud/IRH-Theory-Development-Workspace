"""Task 1 part C — attractors (Model B, T=7.5), static model, Landau curves.
Reads results/task1_q1_final.npy for the POST-HOC top-6 identification.
Appends rows to results/task1_probe_results.csv; writes
results/task1_landau_curves.csv and results/task1_q1_top6.json.
Usage: python task1c_attractors.py
"""
import csv
import json
import os
import sys
import time

sys.path.insert(0, __file__.rsplit('/', 1)[0])
import numpy as np

import irh_models as M

OUT = os.path.join(os.path.dirname(__file__), '..', 'results')
CSV = os.path.join(OUT, 'task1_probe_results.csv')
FIELDS = ["model", "tag", "psibar0", "q02", "u", "seed", "psibar_final",
          "amp", "d4", "modes", "lock", "rms", "Fexc", "seconds"]
VECS = M.d4_roots()


def append(row):
    with open(CSV, 'a', newline='') as f:
        w = csv.DictWriter(f, fieldnames=FIELDS)
        w.writerow(row)
    print(" | ".join(f"{k}={v}" for k, v in row.items()), flush=True)


# Q1 top-6 (POST-HOC; see CLAIM_REGISTER.md A3)
ph1 = np.load(os.path.join(OUT, 'task1_q1_final.npy'))
grid16 = M.Grid(16, __import__('math').pi)
amps = np.array([ph1[grid16.gidx(n)] / 16 ** 4 for n in VECS])
order = np.argsort(-np.abs(amps))
top6 = [VECS[i] for i in order[:6]]
top6_N, top6_T, top6_Q = M.shell_combinatorics(top6)
print("Q1 top-6 modes:", top6, "amps:",
      [round(float(np.abs(amps[i])), 4) for i in order[:6]], flush=True)
print(f"Q1 top-6 (N,T,Q) = ({top6_N},{top6_T},{top6_Q})", flush=True)
with open(os.path.join(OUT, 'task1_q1_top6.json'), 'w') as f:
    json.dump({"modes": [list(m) for m in top6],
               "amps": [float(np.abs(amps[i])) for i in order[:6]],
               "N": top6_N, "T": top6_T, "Q": top6_Q}, f, indent=1)

for tag, pb, seed_vecs in [("A1", -0.30, None), ("A2", -0.18, None),
                           ("A3", 0.00, None), ("A4", +0.10, None),
                           ("A5", -0.18, top6), ("A6", 0.00, top6)]:
    t0 = time.time()
    _, hist, _, _ = M.run_attractor(psibar=pb, dt=0.005, steps=1500,
                                    model='B', seed_vecs=seed_vecs)
    d = hist[-1]
    append(dict(model="dynamic-ModelB", tag=tag, psibar0=pb, q02=8.0, u=1.0,
                seed="-", psibar_final=round(d["psibar"], 5),
                amp=round(d["amp"], 5), d4=round(d["d4"], 4), modes=d["modes"],
                lock=round(d["lock"], 3), rms=round(d["rms"], 4),
                Fexc=round(d["Fexc"], 6), seconds=round(time.time() - t0, 1)))

for tag, pb in [("S1", -0.30), ("S2", -0.18), ("S3", 0.00), ("S4", +0.10)]:
    a_star = M.stationary_amplitude(24, 192, 3384, -0.35, 1.0, 1.0, pb)
    a_use = a_star if a_star is not None else 0.0776
    ph, grid, analyze = M.static_pattern_field(psibar=pb, a_star=a_use)
    d = analyze(ph)
    append(dict(model="static-imposed", tag=tag, psibar0=pb, q02=8.0, u=1.0,
                seed="-", psibar_final=round(d["psibar"], 5),
                amp=round(d["amp"], 5), d4=round(d["d4"], 4), modes=d["modes"],
                lock=round(d["lock"], 3), rms=round(d["rms"], 4),
                Fexc=round(d["Fexc"], 6), seconds=0.0))

curve = []
for pb in np.arange(-0.40, 0.101, 0.01):
    pb = round(float(pb), 2)
    f24, a24 = None, M.stationary_amplitude(24, 192, 3384, -0.35, 1.0, 1.0, pb)
    if a24 is not None:
        f24 = M.one_mode_free_energy(a24, 24, 192, 3384, -0.35, 1.0, 1.0, pb)
    f6, a6 = None, M.stationary_amplitude(top6_N, top6_T, top6_Q, -0.35, 1.0, 1.0, pb)
    if a6 is not None:
        f6 = M.one_mode_free_energy(a6, top6_N, top6_T, top6_Q, -0.35, 1.0, 1.0, pb)
    curve.append(dict(psibar=pb,
                      F24_min=(round(f24, 6) if f24 is not None else None),
                      A24=(round(a24, 5) if a24 is not None else None),
                      F6_min=(round(f6, 6) if f6 is not None else None),
                      A6=(round(a6, 5) if a6 is not None else None),
                      F_disordered=0.0))
with open(os.path.join(OUT, 'task1_landau_curves.csv'), 'w', newline='') as f:
    w = csv.DictWriter(f, fieldnames=list(curve[0].keys()))
    w.writeheader()
    w.writerows(curve)
print("PART C DONE", flush=True)
