"""Task 2 — Check D4 Dynamics Convergence: refinement ladder.

Reference model: sim6 Model B semi-implicit attractor (Hermitian-projected;
see irh_models docstring) + RK4 damped-wave quench (sim6 test_quench).
Reference values (analytic): A* = 0.0775753, F/V ansatz = -0.0076323,
F/V relaxed = -0.0077276, D4 = 1.0000, 24/24 modes, psibar conserved.

Ladder (physical time FIXED so refinement changes resolution, not duration):
  Attractor: T=30. N in {8,12,16,20} at dt=0.005; dt in {0.02,0.01,0.005,0.0025}
             at N=16. Observables at final time vs A*, Fexc, psibar drift.
  Quench:    T=50. N in {8,12,16} at dt=0.02; dt in {0.04,0.02,0.01} at N=16;
             u in {1,0}, seed=1. Observables: D4 shell fraction, modes, lock.
  Input error: attractor psibar in {-0.19,-0.18,-0.17}, q02 in {7.9,8.0,8.1}
             (N=16, dt=0.005, T=7.5); quench seeds {1..5} (N=16, dt=0.02, u=1).
  Model form: (a) ansatz vs relaxed F/V (from N=16 attractor Fexc);
             (b) Model B vs damped-wave RK4 on the same seeded attractor
                 (RK4 wave, seeded 24-mode at A*, psibar=-0.18, T=50);
             (c) sim6 vs sim7 setup numbers (quoted from the sim7 baseline run).

Outputs: results/task2_ladder.csv, results/task2_input_sensitivity.csv,
results/task2_modelform.csv
"""
import csv
import math
import os
import sys
import time

sys.path.insert(0, __file__.rsplit('/', 1)[0])
import numpy as np

import irh_models as M

OUT = os.path.join(os.path.dirname(__file__), '..', 'results')
os.makedirs(OUT, exist_ok=True)

A_STAR = 0.0775753
F_ANSATZ = -0.0076323
F_RELAXED = -0.0077276

ladder = []
sens = []
modelform = []


def rec(table, **kw):
    table.append(kw)
    print(" | ".join(f"{k}={v}" for k, v in kw.items()), flush=True)


# ---- attractor N-ladder (dt=0.005, T=30) ----
for N in (8, 12, 16, 20):
    t0 = time.time()
    _, hist, _, _ = M.run_attractor(N=N, dt=0.005, steps=6000, hermitian=True)
    d = hist[-1]
    rec(ladder, test="attractor-N", N=N, dt=0.005, T=30,
        psibar_final=round(d["psibar"], 8),
        psibar_drift=round(abs(d["psibar"] + 0.18), 10),
        amp=round(d["amp"], 6), amp_err=round(d["amp"] - A_STAR, 6),
        amp_relerr=round((d["amp"] - A_STAR) / A_STAR, 6),
        d4=round(d["d4"], 6), modes=d["modes"],
        Fexc=round(d["Fexc"], 6), Fexc_err_vs_relaxed=round(d["Fexc"] - F_RELAXED, 6),
        rms=round(d["rms"], 6), seconds=round(time.time() - t0, 1))

# ---- attractor dt-ladder (N=16, T=30) ----
for dt in (0.02, 0.01, 0.005, 0.0025):
    steps = int(30 / dt)
    t0 = time.time()
    _, hist, _, _ = M.run_attractor(N=16, dt=dt, steps=steps, hermitian=True)
    d = hist[-1]
    rec(ladder, test="attractor-dt", N=16, dt=dt, T=30,
        psibar_final=round(d["psibar"], 8),
        psibar_drift=round(abs(d["psibar"] + 0.18), 10),
        amp=round(d["amp"], 6), amp_err=round(d["amp"] - A_STAR, 6),
        amp_relerr=round((d["amp"] - A_STAR) / A_STAR, 6),
        d4=round(d["d4"], 6), modes=d["modes"],
        Fexc=round(d["Fexc"], 6), Fexc_err_vs_relaxed=round(d["Fexc"] - F_RELAXED, 6),
        rms=round(d["rms"], 6), seconds=round(time.time() - t0, 1))

# ---- quench N-ladder (dt=0.02, T=50) and dt-ladder (N=16, T=50) ----
for N, dt in [(8, 0.02), (12, 0.02), (16, 0.02), (16, 0.04), (16, 0.01)]:
    steps = int(50 / dt)
    for uu in (1.0, 0.0):
        t0 = time.time()
        _, d, _ = M.run_quench(N=N, dt=dt, steps=steps, seed=1, u=uu)
        tag = "quench-N" if dt == 0.02 else "quench-dt"
        rec(ladder, test=tag, N=N, dt=dt, T=50, u=uu,
            psibar_final=round(d["psibar"], 5),
            amp=round(d["amp"], 5), d4=round(d["d4"], 4), modes=d["modes"],
            lock=round(d["lock"], 3), rms=round(d["rms"], 4),
            Fexc=round(d["Fexc"], 6), seconds=round(time.time() - t0, 1))

# ---- input sensitivity: attractor psibar / q02 (N=16, dt=0.005, T=7.5) ----
for pb in (-0.19, -0.18, -0.17):
    _, hist, _, _ = M.run_attractor(psibar=pb, dt=0.005, steps=1500, hermitian=True)
    d = hist[-1]
    rec(sens, test="attractor-psibar", psibar0=pb, q02=8.0,
        psibar_final=round(d["psibar"], 6), amp=round(d["amp"], 6),
        d4=round(d["d4"], 4), modes=d["modes"], Fexc=round(d["Fexc"], 6))
for q02 in (7.9, 8.0, 8.1):
    _, hist, _, _ = M.run_attractor(q02=q02, dt=0.005, steps=1500, hermitian=True)
    d = hist[-1]
    rec(sens, test="attractor-q02", psibar0=-0.18, q02=q02,
        psibar_final=round(d["psibar"], 6), amp=round(d["amp"], 6),
        d4=round(d["d4"], 4), modes=d["modes"], Fexc=round(d["Fexc"], 6))

# ---- input sensitivity: quench seeds (N=16, dt=0.02, T=50, u=1) ----
for seed in (1, 2, 3, 4, 5):
    t0 = time.time()
    _, d, _ = M.run_quench(seed=seed, dt=0.02, steps=2500, u=1.0)
    rec(sens, test="quench-seed", seed=seed,
        psibar_final=round(d["psibar"], 5), amp=round(d["amp"], 5),
        d4=round(d["d4"], 4), modes=d["modes"], lock=round(d["lock"], 3),
        Fexc=round(d["Fexc"], 6), seconds=round(time.time() - t0, 1))

# ---- model form (b): damped-wave RK4 on the seeded attractor ----
# Seed the 24-mode state at A* and evolve with the wave equation (T=50).
# The wave dynamics does not conserve psibar: measure the drift and the
# pattern survival, against the Model B attractor at the same seed.
t0 = time.time()
grid = M.Grid(16, math.pi)
vecs = M.d4_roots()
ph0 = np.zeros((16,) * 4, complex)
ph0[0, 0, 0, 0] = -0.18 * 16 ** 4
for n in vecs:
    ph0[grid.gidx(n)] = 0.0776 * 16 ** 4
psi0 = np.fft.ifftn(ph0).real
# Reuse run_quench machinery by monkey-seeding: emulate via direct RK4 here.
K2 = grid.K2
omega2 = -0.35 + (8.0 - K2) ** 2
analyze, _ = M.make_analyzer(grid, 8.0, -0.35, 1.0, 1.0, vecs)
ph = np.fft.fftn(psi0)
vh = np.zeros_like(ph)
filt = (K2 < 64).astype(float)
ph *= filt
dt = 0.02
for step in range(1, 2501):
    def rhs(a, b):
        af, bf = a * filt, b * filt
        p = np.fft.ifftn(af).real
        nl = filt * (np.fft.fftn(p * p) - np.fft.fftn(p * p * p))
        return bf, -1.0 * bf - omega2 * af + nl
    k1p, k1v = rhs(ph, vh)
    k2p, k2v = rhs(ph + dt / 2 * k1p, vh + dt / 2 * k1v)
    k3p, k3v = rhs(ph + dt / 2 * k2p, vh + dt / 2 * k2v)
    k4p, k4v = rhs(ph + dt * k3p, vh + dt * k3v)
    ph += dt / 6 * (k1p + 2 * k2p + 2 * k3p + k4p)
    vh += dt / 6 * (k1v + 2 * k2v + 2 * k3v + k4v)
    ph *= filt
    vh *= filt
d = analyze(ph)
rec(modelform, test="wave-vs-ModelB-seeded-attractor",
    psibar_final=round(d["psibar"], 5), amp=round(d["amp"], 5),
    d4=round(d["d4"], 4), modes=d["modes"], lock=round(d["lock"], 3),
    rms=round(d["rms"], 4), Fexc=round(d["Fexc"], 6),
    seconds=round(time.time() - t0, 1))

# ---- model form (a): ansatz vs relaxed F/V (numbers from the N=16 run) ----
n16 = [r for r in ladder if r["test"] == "attractor-N" and r["N"] == 16][0]
rec(modelform, test="ansatz-vs-relaxed-F",
    F_ansatz=F_ANSATZ, F_relaxed_sim=n16["Fexc"], F_relaxed_paper=F_RELAXED,
    gap_vs_ansatz=round(n16["Fexc"] - F_ANSATZ, 6),
    gap_rel=round(abs(n16["Fexc"] - F_ANSATZ) / abs(F_RELAXED), 5))

for name, table in [("task2_ladder.csv", ladder),
                    ("task2_input_sensitivity.csv", sens),
                    ("task2_modelform.csv", modelform)]:
    with open(os.path.join(OUT, name), 'w', newline='') as f:
        w = csv.DictWriter(f, fieldnames=list(table[0].keys()))
        w.writeheader()
        w.writerows(table)
print("DONE task2")
