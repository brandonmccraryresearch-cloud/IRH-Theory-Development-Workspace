#!/usr/bin/env python3
"""Figures for Task 3 from the run CSVs / NPZs already on disk.
1. seed_evolution.png -- modulation rms and excess energy vs time, alpha=1.
2. bracket.png -- outcome vs nominal seed radius (log x), with the three
   envelope predictions marked (thin-wall 7.38, ODE 12.57, droplet-repo
   seed threshold 16.20, saddle R_eq 13.53).
3. seed_profile.png -- radially averaged |phi| of the reconstructed initial
   field for R=1.2 (decays) and R=2.625 (grows), plus the tanh envelope.
"""
import csv
from collections import defaultdict
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

HERE = Path(__file__).parent
OUT = HERE
LAM = 2 * np.pi / np.sqrt(8.0)


def load_outcomes():
    return list(csv.DictReader(open(HERE / "seed_outcomes.csv")))


def load_traj():
    rows = list(csv.DictReader(open(HERE / "seed_trajectories.csv")))
    by = defaultdict(list)
    for r in rows:
        by[r["run_id"]].append(r)
    return by


# --- figure 1: evolution ---
oc = load_outcomes()
by = load_traj()
fig, axes = plt.subplots(1, 2, figsize=(12, 4.6), constrained_layout=True)
sel = [r for r in oc if r["tag"] in ("coarse_a1", "bisect_a1")]
for r in sel:
    tr = by[r["run_id"]]
    t = np.array([float(x["time"]) for x in tr])
    rms = np.array([float(x["modulation_rms"]) for x in tr])
    e = np.array([float(x["excess_energy"]) for x in tr])
    grow = r["outcome"] == "stationary_full24"
    c = "tab:green" if grow else "tab:red"
    ls = "-" if grow else "--"
    lab = f"R={float(r['radius_nominal']):g} {'grow' if grow else 'decay'}"
    axes[0].plot(t, rms, color=c, ls=ls, lw=1.1, label=lab)
    axes[1].plot(t, e, color=c, ls=ls, lw=1.1, label=lab)
axes[0].set_xscale("log")
axes[0].set_yscale("log")
axes[0].set_xlabel("Model B time $t$")
axes[0].set_ylabel("modulation rms")
axes[0].axhline(0.3805, color="k", ls=":", lw=1, label="full branch rms")
axes[0].set_title("Seed evolution: modulation rms ($\\alpha=1$)")
axes[0].grid(alpha=0.2)
axes[0].legend(fontsize=7, ncol=2)
axes[1].set_xscale("log")
axes[1].set_yscale("symlog", linthresh=1e-4)
axes[1].set_ylim(-0.02, 0.35)
axes[1].set_xlabel("Model B time $t$")
axes[1].set_ylabel("excess energy density")
axes[1].axhline(-0.0077262, color="k", ls=":", lw=1, label="relaxed full branch")
axes[1].set_title("Seed evolution: excess energy ($\\alpha=1$)")
axes[1].grid(alpha=0.2)
axes[1].legend(fontsize=7)
fig.suptitle("Localized $D_4$ seeds in the $L=2\\pi$ field: all $R\\leq2.5875$ decay by $t\\approx10$;\n"
             "$R=2.625$ and $2.7$ grow to the full branch.", fontsize=10)
fig.savefig(OUT / "seed_evolution.png", dpi=170)
plt.close(fig)

# --- figure 2: bracket vs envelope ---
fig, ax = plt.subplots(figsize=(10, 4.6), constrained_layout=True)
a1 = [r for r in oc if float(r["alpha"]) == 1.0 and r["tag"] != "smoke"]
a15 = [r for r in oc if float(r["alpha"]) == 1.5]
for r in a1:
    x = float(r["radius_nominal"])
    y = 1 if r["outcome"] == "stationary_full24" else 0
    ax.plot(x, y, "o", ms=9, color="tab:green" if y else "tab:red",
            markeredgecolor="k", markeredgewidth=0.6)
for r in a15:
    x = float(r["radius_nominal"])
    ax.plot(x, -0.18, "s", ms=8, color="tab:red", markeredgecolor="k",
            markeredgewidth=0.6)
ax.axvspan(2.5875, 2.625, color="tab:green", alpha=0.18, label="field bracket $(2.5875,\\,2.625]$")
for xv, lab in ((7.38, "thin-wall $R_c=7.38$ (fails)"),
                (12.57, "radial-ODE $R_c=12.57$"),
                (13.53, "saddle $R_{eq}=13.53$"),
                (16.20, "envelope seed threshold $16.20$")):
    ax.axvline(xv, color="k", ls="--", lw=1)
    ax.text(xv, 1.28, lab, rotation=90, va="top", ha="right", fontsize=8)
ax.axvline(np.pi, color="tab:blue", ls=":", lw=1.2)
ax.text(np.pi, 1.38, "box half-size $\\pi$", rotation=90, va="top", ha="right",
        fontsize=8, color="tab:blue")
ax.set_xscale("log")
ax.set_xlim(0.5, 20)
ax.set_ylim(-0.55, 1.45)
ax.set_yticks([0, 1])
ax.set_yticklabels(["dissolve\n(uniform)", "grow\n(full $D_4$)"])
ax.set_xlabel("nominal seed radius $R$ (model units; $\\lambda=2.22$)")
ax.set_ylabel("field outcome at $t=200$")
ax.plot([], [], "o", ms=9, color="tab:green", markeredgecolor="k", label="$\\alpha=1$ grow")
ax.plot([], [], "o", ms=9, color="tab:red", markeredgecolor="k", label="$\\alpha=1$ dissolve")
ax.plot([], [], "s", ms=8, color="tab:red", markeredgecolor="k", label="$\\alpha=1.5$ dissolve ($R\\leq1.5$)")
ax.set_title("Field threshold vs envelope predictions: different regimes, not one number")
ax.grid(alpha=0.2, which="both")
ax.legend(fontsize=8, loc="upper left")
fig.savefig(OUT / "bracket.png", dpi=170)
plt.close(fig)

# --- figure 3: radial seed profiles from stored initial coefficients ---
import importlib.util
spec = importlib.util.spec_from_file_location(
    "field_study",
    "/home/hatch/workspace/research/irh/co-scientist-tasks-2026-11-10/4d-field-test/run_field_study.py")
fmod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(fmod)
fig, ax = plt.subplots(figsize=(9, 4.6), constrained_layout=True)
for run_id, label in (("coarse_a1_a1_R1.2", "$R=1.2$ (dissolves)"),
                      ("bisect_a1_a1_R2.625", "$R=2.625$ (grows)")):
    z = np.load(HERE / f"{run_id}.npz")
    m = fmod.Field(18, 4)
    y0 = m.from_compact(z["wavevectors"], z["initial_coefficients"])
    phi = m.real(y0)
    n = 18
    xs = np.linspace(0, 2 * np.pi, n, endpoint=False)
    X = np.meshgrid(xs, xs, xs, xs, indexing="ij")
    rho = np.sqrt(sum((x - np.pi) ** 2 for x in X))
    bins = np.linspace(0, 3.2, 33)
    idx = np.digitize(rho.ravel(), bins)
    prof = [np.sqrt(np.mean(phi.ravel()[idx == j] ** 2)) if np.any(idx == j) else np.nan
            for j in range(1, len(bins))]
    ax.plot(0.5 * (bins[:-1] + bins[1:]), prof, ".-", lw=1.2, label=label)
r = np.linspace(0, 3.2, 200)
env = 0.5 * (1 - np.tanh(4.0 * (r - 2.625)))
ax.plot(r, 0.0775753 * np.sqrt(24) * env, ":", color="grey", lw=1,
        label="envelope $\\times A^*\\sqrt{24}$, $R=2.625$")
ax.set_xlabel("distance from box centre $\\rho$")
ax.set_ylabel("radial local rms of $\\phi$ (initial field)")
ax.set_title("Initial localized seeds: local rms matches the envelope for rho > 1.5; centre is a hot spot")
ax.grid(alpha=0.2)
ax.legend(fontsize=8)
fig.savefig(OUT / "seed_profile.png", dpi=170)
plt.close(fig)
print("FIGURES DONE")
