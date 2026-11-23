"""Figures for WS-C reports. Reads results/*.csv, writes figures/*.png.
matplotlib 3.11.2, Agg backend.
"""
import csv
import os

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RES = os.path.join(BASE, "results")
FIG = os.path.join(BASE, "figures")
os.makedirs(FIG, exist_ok=True)

plt.rcParams.update({"font.size": 11, "axes.grid": True, "grid.alpha": 0.3,
                     "figure.dpi": 150})

# ---- Fig 1: Landau curves -----------------------------------------------
rows = list(csv.DictReader(open(os.path.join(RES, "task1_landau_curves.csv"))))
pb = np.array([float(r["psibar"]) for r in rows])
f24 = np.array([float(r["F24_min"]) if r["F24_min"] else np.nan for r in rows])
f6 = np.array([float(r["F6_min"]) if r["F6_min"] else np.nan for r in rows])
fig, ax = plt.subplots(figsize=(8, 5))
ax.axhline(0, color="k", lw=0.8)
ax.plot(pb, f24, "o-", ms=3, label="24-mode D4 (one-mode ansatz)")
ax.plot(pb, f6, "s-", ms=3, label="observed 6-mode hexagonal (one-mode ansatz)")
ax.axvspan(-0.235, -0.125, color="green", alpha=0.12,
           label="24-mode global minimum band (r=-0.35)")
# measured full-field points
pts = [(-0.18, -0.007728, "A2 24-mode"), (0.0, -0.025549, "A3 24-mode"),
       (-0.18, -0.00229, "A5 6-mode"), (0.0, -0.041306, "A6 6-mode")]
for x, y, lab in pts:
    ax.plot([x], [y], "D", ms=6, mfc="none", mec="red", mew=1.5)
    ax.annotate(lab, (x, y), textcoords="offset points", xytext=(6, 4), fontsize=9,
                color="red")
ax.set_xlabel(r"$\bar\psi$")
ax.set_ylabel(r"$F/V$ excess over disordered state")
ax.set_title("One-mode Landau free energies at r=-0.35, q0^2=8.0 (u=v=1)\n"
             "diamonds: measured full-field Model B values")
ax.legend(fontsize=9, loc="lower left")
fig.tight_layout()
fig.savefig(os.path.join(FIG, "fig1_landau_curves.png"))
plt.close(fig)

# ---- Fig 2: divergence diagram ------------------------------------------
probes = list(csv.DictReader(open(os.path.join(RES, "task1_probe_results.csv"))))
fig, ax = plt.subplots(figsize=(8, 5))
groups = {"dynamic-wave\n(noise quench)": [], "dynamic-ModelB\n(seeded)": [],
          "static-imposed": []}
for r in probes:
    if r["model"] == "dynamic-wave":
        groups["dynamic-wave\n(noise quench)"].append((float(r["psibar0"]), int(r["modes"])))
    elif r["model"] == "dynamic-ModelB":
        groups["dynamic-ModelB\n(seeded)"].append((float(r["psibar0"]), int(r["modes"])))
    else:
        groups["static-imposed"].append((float(r["psibar0"]), int(r["modes"])))
colors = {"dynamic-wave\n(noise quench)": "tab:blue",
          "dynamic-ModelB\n(seeded)": "tab:green", "static-imposed": "tab:red"}
for lab, vals in groups.items():
    xs = [v[0] for v in vals]
    ys = [v[1] for v in vals]
    ax.scatter(xs, ys, s=70, label=lab, color=colors[lab], zorder=3)
    for x, y in vals:
        ax.annotate(f"{y}/24", (x, y), textcoords="offset points", xytext=(5, 5),
                    fontsize=8)
ax.axhline(24, color="k", lw=0.8, ls="--")
ax.axvspan(-0.235, -0.125, color="green", alpha=0.12)
ax.set_xlabel(r"$\bar\psi_0$ (initial mean)")
ax.set_ylabel("occupied D4-shell modes (of 24)")
ax.set_ylim(0, 26)
ax.set_title("Divergence: modes occupied at final state vs initial mean\n"
             "(green band: 24-mode global minimum at r=-0.35; quenches never reach 24/24)")
ax.legend(fontsize=9, loc="lower left")
fig.tight_layout()
fig.savefig(os.path.join(FIG, "fig2_divergence.png"))
plt.close(fig)

# ---- Fig 3: convergence ---------------------------------------------------
lad = list(csv.DictReader(open(os.path.join(RES, "task2_ladder.csv"))))
tr = list(csv.DictReader(open(os.path.join(RES, "task2_transient.csv"))))
fig, (a1, a2) = plt.subplots(1, 2, figsize=(10, 4.5))
# (a) transient dt error at T=0.5
t05 = [r for r in tr if r["T"] == "0.5"]
dts = np.array([float(r["dt"]) for r in t05])
err = np.array([abs(float(r["err_vs_ref"])) for r in t05])
ref = err[-1] if err[-1] > 0 else 1e-9
a1.loglog(dts, err, "o-", label="|amp(dt) - amp(0.0025)| at T=0.5")
a1.loglog(dts, 0.000173 * (dts / 0.02), "k--", label="slope 1 (first order)")
a1.set_xlabel("dt")
a1.set_ylabel("amplitude error")
a1.set_title("(a) Transient time-step error\nRichardson p ~ 0.9-1.0")
a1.legend(fontsize=9)
# (b) quench Fexc vs N + seed spread at N=16
qn = [r for r in lad if r["test"] == "quench-N"]
ns = np.array([int(r["N"]) for r in qn])
fx = np.array([float(r["Fexc"]) for r in qn])
a2.plot(ns, fx, "o-", label="quench Fexc, seed 1")
seeds = list(csv.DictReader(open(os.path.join(RES, "task2_input_sensitivity.csv"))))
q1 = [r for r in probes if r["tag"] in ("Q1", "Q7")]
sf = [float(r["Fexc"]) for r in q1] + [float(r["Fexc"]) for r in seeds]
a2.errorbar([16], [np.mean(sf)], yerr=[[np.mean(sf) - min(sf)], [max(sf) - np.mean(sf)]],
            fmt="s", capsize=5, color="tab:red",
            label=f"N=16 seed spread (n=5): {min(sf):.4f}..{max(sf):.4f}")
a2.annotate("N=8: 2-mode\n(grid failure)", (8, fx[0]), textcoords="offset points",
            xytext=(8, 10), fontsize=9)
a2.set_xlabel("N (grid points per dimension)")
a2.set_ylabel("Fexc (quench final)")
a2.set_title("(b) Quench free energy vs grid N\n(seed spread >> N=12/16 difference)")
a2.legend(fontsize=9)
fig.tight_layout()
fig.savefig(os.path.join(FIG, "fig3_convergence.png"))
plt.close(fig)

# ---- Fig 4: instability ---------------------------------------------------
inst = list(csv.DictReader(open(os.path.join(RES, "instability_series.csv"))))
fig, ax = plt.subplots(figsize=(8, 5))
for h, lab, col in ((0, "no projection (shipped-style update)", "tab:red"),
                    (1, "Hermitian projection per step", "tab:green")):
    ts = np.array([float(r["t"]) for r in inst if int(r["hermitian"]) == h])
    am = np.array([float(r["amp"]) for r in inst if int(r["hermitian"]) == h])
    ok = np.isfinite(am)
    ax.semilogy(ts[ok], am[ok], "o-", ms=3, label=lab, color=col)
ax.axhline(0.077682, color="k", lw=0.8, ls="--", label="fixed point 0.077682")
ax.axvline(18, color="gray", lw=0.8, ls=":")
ax.annotate("manuscript stability\nclaim ends t=18", (18, 1e-1), fontsize=9,
            xytext=(10, 5), textcoords="offset points")
ax.annotate("blow-up t=27.5", (27.5, 1e2), fontsize=9, color="tab:red")
ax.set_xlabel("t")
ax.set_ylabel("<A> (mean shell amplitude, log scale)")
ax.set_title("Model B attractor: anti-Hermitian roundoff growth without projection\n"
             "growth 1.0142/step at the shell; projection extends stability to t=30")
ax.legend(fontsize=9, loc="upper left")
fig.tight_layout()
fig.savefig(os.path.join(FIG, "fig4_instability.png"))
plt.close(fig)
print("FIGURES DONE")
for f in sorted(os.listdir(FIG)):
    print(f, os.path.getsize(os.path.join(FIG, f)))
