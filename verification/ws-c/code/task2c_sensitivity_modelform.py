"""Task 2 part C — input sensitivity (attractor psibar/q02) + model form.
Attractor sensitivity: psibar in {-0.19,-0.18,-0.17}, q02 in {7.9,8.0,8.1}
(N=16, dt=0.005, T=7.5). Model form (b): damped-wave RK4 on the seeded
24-mode attractor (T=50) vs the Model B attractor at the same seed.
Appends to results/task2_input_sensitivity.csv and results/task2_modelform.csv.
"""
import csv
import os
import sys
import time

sys.path.insert(0, __file__.rsplit('/', 1)[0])
import numpy as np

import irh_models as M

OUT = os.path.join(os.path.dirname(__file__), '..', 'results')
CSVS = os.path.join(OUT, 'task2_attractor_sensitivity.csv')
CSVM = os.path.join(OUT, 'task2_modelform.csv')
SFIELDS = ["test", "seed", "psibar_final", "amp", "d4", "modes", "lock",
           "rms", "Fexc", "seconds"]
AFIELDS = ["test", "psibar0", "q02", "psibar_final", "amp", "d4", "modes",
           "Fexc", "seconds"]
MFIELDS = ["test", "psibar_final", "amp", "d4", "modes", "lock", "rms",
           "Fexc", "seconds"]


def append(path, fields, row):
    new = not os.path.exists(path)
    with open(path, 'a', newline='') as f:
        w = csv.DictWriter(f, fieldnames=fields)
        if new:
            w.writeheader()
        w.writerow(row)
    print(" | ".join(f"{k}={v}" for k, v in row.items()), flush=True)


for pb in (-0.19, -0.18, -0.17):
    t0 = time.time()
    _, hist, _, _ = M.run_attractor(psibar=pb, dt=0.005, steps=1500, hermitian=True)
    d = hist[-1]
    append(CSVS, AFIELDS, dict(test="attractor-psibar", psibar0=pb, q02=8.0,
                               psibar_final=round(d["psibar"], 6),
                               amp=round(d["amp"], 6), d4=round(d["d4"], 4),
                               modes=d["modes"], Fexc=round(d["Fexc"], 6),
                               seconds=round(time.time() - t0, 1)))
for q02 in (7.9, 8.0, 8.1):
    t0 = time.time()
    _, hist, _, _ = M.run_attractor(q02=q02, dt=0.005, steps=1500, hermitian=True)
    d = hist[-1]
    append(CSVS, AFIELDS, dict(test="attractor-q02", psibar0=-0.18, q02=q02,
                               psibar_final=round(d["psibar"], 6),
                               amp=round(d["amp"], 6), d4=round(d["d4"], 4),
                               modes=d["modes"], Fexc=round(d["Fexc"], 6),
                               seconds=round(time.time() - t0, 1)))

# Model form (b): RK4 damped wave on the seeded 24-mode attractor.
t0 = time.time()
grid = M.Grid(16, __import__('math').pi)
vecs = M.d4_roots()
ph0 = np.zeros((16,) * 4, complex)
ph0[0, 0, 0, 0] = -0.18 * 16 ** 4
for n in vecs:
    ph0[grid.gidx(n)] = 0.0776 * 16 ** 4
K2 = grid.K2
omega2 = -0.35 + (8.0 - K2) ** 2
analyze, _ = M.make_analyzer(grid, 8.0, -0.35, 1.0, 1.0, vecs)
ph = np.fft.fftn(np.fft.ifftn(ph0).real)
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
append(CSVM, MFIELDS, dict(test="wave-vs-ModelB-seeded-attractor",
                           psibar_final=round(d["psibar"], 5),
                           amp=round(d["amp"], 5), d4=round(d["d4"], 4),
                           modes=d["modes"], lock=round(d["lock"], 3),
                           rms=round(d["rms"], 4), Fexc=round(d["Fexc"], 6),
                           seconds=round(time.time() - t0, 1)))

# Model form (a): ansatz vs relaxed F/V (N=16 attractor value from part A).
import csv as _csv
lad = list(_csv.DictReader(open(os.path.join(OUT, 'task2_ladder.csv'))))
n16 = [r for r in lad if r["test"] == "attractor-N" and r["N"] == "16"][0]
append(CSVM, ["test", "F_ansatz", "F_relaxed_sim", "F_relaxed_paper",
              "gap_vs_ansatz", "gap_rel"],
       dict(test="ansatz-vs-relaxed-F", F_ansatz=-0.0076323,
            F_relaxed_sim=n16["Fexc"], F_relaxed_paper=-0.0077276,
            gap_vs_ansatz=round(float(n16["Fexc"]) + 0.0076323, 6),
            gap_rel=round(abs(float(n16["Fexc"]) + 0.0076323) / 0.0077276, 5)))
print("TASK2-C DONE", flush=True)
