"""Task 1 — Formalize Substrate Selection Models: probe grid.

Shared conditions for every probe: N=16, L=pi, r=-0.35, u=v=1 (unless the
probe varies it), gamma=1.0 (wave runs). Dynamic model = tension-relaxation
damped wave (RK4 quench, sim6 test_quench) + conserved Model B attractor
(sim6 test_attractor, Hermitian-projected). Static model = imposed 24-mode
pattern (irh_models.static_pattern_field). Equilibrium model = one-mode
Landau functional F_mod (analytic, exact).

Probe grid (registered predictions P1-P3 in CLAIM_REGISTER.md):
  Q1 psibar= 0.00 q02=8.0 u=1 noise   (P1: sub-pattern, not 24/24)
  Q2 psibar=-0.18 q02=8.0 u=1 noise   (in-band wave quench; mean drift measured)
  Q3 psibar= 0.00 q02=8.0 u=0 noise   (P3: triad-off control, D4 < 0.35)
  Q4 psibar=-0.18 q02=7.5 u=1 noise   (P2: detuned, no ordered 24-mode state)
  Q5 psibar=-0.30 q02=8.0 u=1 noise   (band low edge)
  Q6 psibar=+0.10 q02=8.0 u=1 noise   (above band)
  Q7 psibar=-0.18 q02=8.0 u=1 noise seed=2 (seed sensitivity)
  A1..A4 psibar in {-0.30,-0.18,0.00,+0.10} q02=8.0, seeded 24-mode, Model B
  A5 psibar=-0.18 seeded 6-mode (modes = the 6 largest in Q1 final state)
  A6 psibar= 0.00 seeded 6-mode (same 6 modes)
  S1..S4 static imposed pattern at psibar in {-0.30,-0.18,0.00,+0.10}
  Landau: min over A of F_mod for 24-mode vs observed-6-mode vs disordered,
          psibar in [-0.40, 0.10].

Outputs: results/task1_probe_results.csv, results/task1_landau_curves.csv
"""
import csv
import json
import math
import os
import sys
import time

sys.path.insert(0, __file__.rsplit('/', 1)[0])
import numpy as np

import irh_models as M

OUT = os.path.join(os.path.dirname(__file__), '..', 'results')
os.makedirs(OUT, exist_ok=True)
VECS = M.d4_roots()
rows = []


def record(**kw):
    rows.append(kw)
    print(" | ".join(f"{k}={v}" for k, v in kw.items()), flush=True)


t00 = time.time()

# ---- quenches (RK4 damped wave, T=50) ----
quenches = [
    ("Q1", 0.00, 8.0, 1.0, 1),
    ("Q2", -0.18, 8.0, 1.0, 1),
    ("Q3", 0.00, 8.0, 0.0, 1),
    ("Q4", -0.18, 7.5, 1.0, 1),
    ("Q5", -0.30, 8.0, 1.0, 1),
    ("Q6", +0.10, 8.0, 1.0, 1),
    ("Q7", -0.18, 8.0, 1.0, 2),
]
q1_final_ph = None
for tag, pb0, q02, uu, seed in quenches:
    t0 = time.time()
    ph, d, grid = M.run_quench(psibar=pb0, q02=q02, u=uu, seed=seed,
                               dt=0.02, steps=2500)
    if tag == "Q1":
        q1_final_ph = ph
    record(model="dynamic-wave", tag=tag, psibar0=pb0, q02=q02, u=uu, seed=seed,
           psibar_final=round(d["psibar"], 5), amp=round(d["amp"], 5),
           d4=round(d["d4"], 4), modes=d["modes"], lock=round(d["lock"], 3),
           rms=round(d["rms"], 4), Fexc=round(d["Fexc"], 6),
           seconds=round(time.time() - t0, 1))

# Which 6 modes does Q1 occupy? (POST-HOC identification; see A3 in register.)
amps = np.array([q1_final_ph[M.Grid(16, math.pi).gidx(n)] / 16 ** 4 for n in VECS])
order = np.argsort(-np.abs(amps))
top6 = [VECS[i] for i in order[:6]]
print("Q1 top-6 modes:", top6, "amps:", [round(float(np.abs(amps[i])), 4) for i in order[:6]], flush=True)
top6_N, top6_T, top6_Q = M.shell_combinatorics(top6)
print(f"Q1 top-6 (N,T,Q) = ({top6_N},{top6_T},{top6_Q})", flush=True)
with open(os.path.join(OUT, 'task1_q1_top6.json'), 'w') as f:
    json.dump({"modes": [list(m) for m in top6],
               "amps": [float(np.abs(amps[i])) for i in order[:6]],
               "N": top6_N, "T": top6_T, "Q": top6_Q}, f, indent=1)

# ---- attractors (Model B, T=7.5) ----
for tag, pb, seed_vecs in [
        ("A1", -0.30, None), ("A2", -0.18, None),
        ("A3", 0.00, None), ("A4", +0.10, None),
        ("A5", -0.18, top6), ("A6", 0.00, top6)]:
    t0 = time.time()
    _, hist, _, _ = M.run_attractor(psibar=pb, dt=0.005, steps=1500,
                                    model='B', seed_vecs=seed_vecs)
    d = hist[-1]
    record(model="dynamic-ModelB", tag=tag, psibar0=pb, q02=8.0, u=1.0, seed="-",
           psibar_final=round(d["psibar"], 5), amp=round(d["amp"], 5),
           d4=round(d["d4"], 4), modes=d["modes"], lock=round(d["lock"], 3),
           rms=round(d["rms"], 4), Fexc=round(d["Fexc"], 6),
           seconds=round(time.time() - t0, 1))

# ---- static model (imposed pattern) ----
for tag, pb in [("S1", -0.30), ("S2", -0.18), ("S3", 0.00), ("S4", +0.10)]:
    a_star = M.stationary_amplitude(24, 192, 3384, -0.35, 1.0, 1.0, pb)
    a_use = a_star if a_star is not None else 0.0776
    ph, grid, analyze = M.static_pattern_field(psibar=pb, a_star=a_use)
    d = analyze(ph)
    record(model="static-imposed", tag=tag, psibar0=pb, q02=8.0, u=1.0, seed="-",
           psibar_final=round(d["psibar"], 5), amp=round(d["amp"], 5),
           d4=round(d["d4"], 4), modes=d["modes"], lock=round(d["lock"], 3),
           rms=round(d["rms"], 4), Fexc=round(d["Fexc"], 6),
           seconds=0.0)

with open(os.path.join(OUT, 'task1_probe_results.csv'), 'w', newline='') as f:
    w = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
    w.writeheader()
    w.writerows(rows)

# ---- Landau curves: min_A F_mod for 24-mode vs observed-6 vs disordered ----
curve = []
for pb in np.arange(-0.40, 0.101, 0.01):
    pb = round(float(pb), 2)
    f24 = None
    a24 = M.stationary_amplitude(24, 192, 3384, -0.35, 1.0, 1.0, pb)
    if a24 is not None:
        f24 = M.one_mode_free_energy(a24, 24, 192, 3384, -0.35, 1.0, 1.0, pb)
    f6 = None
    a6 = M.stationary_amplitude(top6_N, top6_T, top6_Q, -0.35, 1.0, 1.0, pb)
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

print(f"TOTAL elapsed {time.time() - t00:.0f}s")
