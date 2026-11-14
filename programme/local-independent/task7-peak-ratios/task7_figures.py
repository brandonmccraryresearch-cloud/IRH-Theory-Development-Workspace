#!/usr/bin/env python
"""Task 7 figures: paired synthetic reciprocal-space maps + resolution profiles.
Synthetic = kernel-broadened display of the tabulated peak lists only; no new
data. Exact separable finite-window kernels are used for the line profiles.
"""
import json, math, os
import numpy as np
import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

HERE = os.path.dirname(os.path.abspath(__file__))
PROG = "/home/hatch/workspace/research/irh/co-scientist-tasks-2026-11-10"
SRC3 = os.path.join(PROG, "3d-projections")

lat = pd.read_csv(os.path.join(SRC3, "lattice_peak_intensities.csv"))
fld = pd.read_csv(os.path.join(SRC3, "field_mode_intensities.csv"))
with open(os.path.join(HERE, "line_profile_data.npz")) as _:
    pass
prof = np.load(os.path.join(HERE, "line_profile_data.npz"))
qa, qb = prof["qa"], prof["qb"]
sep = float(prof["sep_pair"])

# ---------------- Figure 1: paired synthetic maps, plane q3 = 0.5 ----------------
SIGMA = 0.07  # display Gaussian width (cycles/unit), stated on the figure
grid = np.linspace(-1.8, 1.8, 241)
Q1, Q2 = np.meshgrid(grid, grid)
Q3 = 0.5

def synth_map(peaks_q, peaks_I):
    # peaks_q: (n,3), peaks_I: (n,) ; Gaussian display kernel in 3D distance
    img = np.zeros_like(Q1)
    for q, I in zip(peaks_q, peaks_I):
        d2 = (Q1 - q[0]) ** 2 + (Q2 - q[1]) ** 2 + (Q3 - q[2]) ** 2
        img += I * np.exp(-d2 / (2 * SIGMA ** 2))
    return img

def probes(op, L, h):
    s = lat[(lat.operation == op) & (lat.L == L) & (lat.h == h)]
    s = s[s.label != "DC"]
    return s[["q1", "q2", "q3"]].values, s["I_finite_DC_normalized"].values

panels = []
q, I = probes("rational_exact_lattice_section", 7, 0.0)
panels.append(("FCC section (atomic), $L=7$\n7 probes, $I(111)=I(200)=1$", q, I))
q, I = probes("rational_finite_source_projection", 3, 6.0)
panels.append(("Simple-cubic projection, $L=3$, $H=6$\n$I(111)=0.00548$, $I(200)=1$", q, I))
c = lat[(lat.operation == "irrational_cut_and_project") & (lat.L == 7) & (lat.h == 0.7)]
c = c[(c.I_infinite_DC_normalized >= 0.01) & (c.q_norm > 1e-9)]
panels.append(("Irrational CPS, ideal, $h=0.7$\n156 candidates $I\\geq0.01$ (of 288 non-DC)", 
               c[["q1", "q2", "q3"]].values, c["I_infinite_DC_normalized"].values))
panels.append(("Irrational CPS, finite, $h=0.7$, $L=7$, $N=1923$\nsame 156 candidates, finite $I$",
               c[["q1", "q2", "q3"]].values, c["I_finite_DC_normalized"].values))

fig, axes = plt.subplots(2, 2, figsize=(10, 9))
for ax, (title, pq, pI) in zip(axes.flat, panels):
    img = synth_map(pq, pI)
    im = ax.imshow(np.log10(np.maximum(img, 1e-4)), origin="lower",
                   extent=[-1.8, 1.8, -1.8, 1.8], cmap="inferno",
                   vmin=-4, vmax=0.3, aspect="equal")
    ax.set_title(title, fontsize=10)
    ax.set_xlabel("$q_1$ (cycles/unit)")
    ax.set_ylabel("$q_2$ (cycles/unit)")
    ax.set_xticks([-1.5, -0.75, 0, 0.75, 1.5])
    ax.set_yticks([-1.5, -0.75, 0, 0.75, 1.5])
fig.suptitle("Synthetic reciprocal-space maps, plane $q_3=0.5$  |  "
             "Gaussian display kernel $\\sigma=0.07$ cycles/unit; "
             "$\\log_{10}$ intensity, DC-normalised",
             fontsize=11)
cax = fig.add_axes([0.92, 0.18, 0.02, 0.68])
cbar = fig.colorbar(im, cax=cax)
cbar.set_label("$\\log_{10} I / I(0)$ (synthetic display)")
fig.text(0.5, 0.01, "SYNTHETIC DISPLAY ONLY: kernel-broadened rendering of the tabulated peak lists "
         "(3d-projections CSVs). Not a measured diffraction pattern; no detector, noise or coupling model.\n"
         "In the $q_3=0.5$ plane only the $q_3=0.5$ probes are in-plane (FCC: (111) and (311)); "
         "the other FCC/projection probes lie out of this plane.",
         ha="center", fontsize=8, style="italic")
fig.tight_layout(rect=[0, 0.05, 0.90, 0.95])
fig.savefig(os.path.join(HERE, "task7_fig1_reciprocal_maps.png"), dpi=200)
plt.close(fig)

# ---------------- Figure 2: resolution ----------------
def K_rect(d, L):
    return np.sinc(2 * L * d)
def K_hann(d, L):
    z = 2 * L * d
    return np.sinc(z) + 0.5 * (np.sinc(z - 1) + np.sinc(z + 1))
def K3(q, qm, L, kind):
    d = q - qm
    k = K_rect if kind == "rectangular" else K_hann
    return k(d[0], L) * k(d[1], L) * k(d[2], L)

mid = (qa + qb) / 2
direc = (qb - qa) / sep
s = np.linspace(-0.6, 0.6, 601)
sa = float(np.dot(qa - mid, direc)); sb = float(np.dot(qb - mid, direc))
dips = {}
fig, axes = plt.subplots(1, 2, figsize=(11, 4.6))
ax = axes[0]
for L, kind, ls in [(4, "rectangular", "-"), (4, "hann", "--"),
                    (8, "rectangular", "-"), (8, "hann", "--")]:
    amp = np.zeros_like(s)
    for qm in (qa, qb):
        amp += np.array([K3(mid + sv * direc, qm, L, kind) for sv in s])
    power = amp ** 2
    label = f"$L={L}$, {kind}"
    ax.plot(s, power, ls, label=label)
    # dip between the two centres
    m = (s > sa) & (s < sb)
    valley = float(power[m].min()) if m.any() else float("nan")
    peak = float(max(power[np.argmin(np.abs(s - sa))], power[np.argmin(np.abs(s - sb))]))
    dips[f"L{L}_{kind}"] = dict(valley_over_peak=valley / peak if peak else None,
                                valley=valley, peak=peak)
ax.axvline(sa, color="grey", lw=0.8); ax.axvline(sb, color="grey", lw=0.8)
ax.set_xlabel("distance along pair axis $s$ (cycles/unit)")
ax.set_ylabel("finite-window power $|\\sum_m K_3|^2$ (unit modes)")
ax.set_title(f"Closest irrational field-mode pair\n$\\Delta q={sep:.4f}$ cycles/unit")
ax.legend(fontsize=8); ax.set_ylim(0, 1.3); ax.grid(alpha=0.3)

ax = axes[1]
# ratio vs window: A3 (FCC, L=3,5,7), A3 (projection, H=2,4,6), A1 (projection)
ax.plot([3, 5, 7], [0.015082, 0.006840, 0.003874], "o-", label="$A_3$ FCC section, $L$")
ax.plot([2, 4, 6], [0.495816, 1.688443, 3.644628], "s-", label="$A_3$ projection, $H$")
ax.plot([2, 4, 6], [0.038888, 0.011714, 0.005480], "^-", label="$A_1$ projection, $H$")
ax.axhline(1.0, color="grey", lw=0.8, ls=":")
ax.set_yscale("log")
ax.set_xlabel("window parameter ($L$ for section, $H$ for projection)")
ax.set_ylabel("ratio (log scale)")
ax.set_title("Forbidden/allowed and 111/200 ratios\nvs finite window / source depth")
ax.legend(fontsize=8); ax.grid(alpha=0.3, which="both")
fig.suptitle("Finite-resolution behaviour: closest-pair profiles and ratio drift with window",
             fontsize=11)
fig.tight_layout(rect=[0, 0, 1, 0.93])
fig.savefig(os.path.join(HERE, "task7_fig2_resolution.png"), dpi=200)
plt.close(fig)

with open(os.path.join(HERE, "line_profile_dips.json"), "w") as f:
    json.dump({"closest_pair_sep": sep, "qa": qa.tolist(), "qb": qb.tolist(),
               "centre_s": [sa, sb], "dips": dips}, f, indent=2)
print("dips:", json.dumps(dips, indent=2))
print("closest pair qa,qb:", qa, qb, "sep", sep)
print("figures written")
