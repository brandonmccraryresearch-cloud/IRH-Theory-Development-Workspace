"""Task 8 — figures: defect-energy map and stiffness / phonon-curvature plots.
Reads the CSV tables produced by task8_stiffness.py and task8_phonon_rates.py.
Also computes the cubic-coefficient spread over random unit-norm strains
(for the anisotropy statement in REPORT.md).
"""
import json
import math

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

WD = "/home/hatch/workspace/research/irh/co-scientist-tasks-2026-11-10/local-independent/task8-phonon-stiffness"
RNG = np.random.default_rng(20261114)

summ = json.load(open(f"{WD}/tables/task8_summary.json"))
A2 = summ["A_star_sq"]
F_DENS = abs(summ["F_density"])

# --- cubic-coefficient spread over random unit-Frobenius-norm strains ------
def f3_of(eps):
    eps2 = eps @ eps
    SHELL = []
    import itertools
    for i, j in itertools.combinations(range(4), 2):
        for s1, s2 in itertools.product([1, -1], repeat=2):
            a = [0] * 4
            a[i] = s1
            a[j] = s2
            SHELL.append(tuple(2 * x for x in a))
    s3 = 0.0
    for g in SHELL:
        gv = np.array(g, dtype=float)
        s3 += (gv @ eps @ gv) * (gv @ eps2 @ gv)
    return 2 * A2 * s3

f3s = []
for _ in range(300):
    M = RNG.standard_normal((4, 4))
    E = (M + M.T) / 2
    E /= np.linalg.norm(E)
    f3s.append(f3_of(E))
f3s = np.array(f3s)
print(f"f3 over 300 random unit-norm strains: min={f3s.min():.6f} "
      f"max={f3s.max():.6f} mean={f3s.mean():.6f} std={f3s.std():.6f}")
print(f"uniaxial |f3| = {384*A2:.6f} for comparison")

# --- Figure 1: defect-energy map ------------------------------------------
dis = summ["dislocation"]
n2s = [d["n2"] for d in dis]
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(11, 4.6))
R = np.logspace(math.log10(4.0), math.log10(60.0), 200)
for d in dis:
    # E/A is defined only for R > r0 (log of a number < 1 is unphysical here);
    # mask the R <= r0 part of each curve.
    m_e = R > d["r0_edge"]
    m_s = R > d["r0_screw"]
    ax1.plot(R[m_e], d["K_edge"] * np.log(R[m_e] / d["r0_edge"]), label=f"$|b|^2={d['n2']}$")
    ax2.plot(R[m_s], d["K_screw"] * np.log(R[m_s] / d["r0_screw"]), label=f"$|b|^2={d['n2']}$")
for ax in (ax1, ax2):
    ax.axvline(20.0, color="k", ls=":", lw=1)
    ax.set_xscale("log")
    ax.set_xlabel("system radius $R$ (dimensionless length)")
    ax.set_xlim(4, 60)
ax1.set_ylabel("energy per unit sheet area $E/A$")
ax1.set_title("(a) edge character ($b \\perp$ sheet)")
ax2.set_title("(b) screw character ($b \\parallel$ sheet)")
ax1.legend(fontsize=8, loc="upper left")
ax2.legend(fontsize=8, loc="upper left")
ax1.text(21, 0.15, "$R=20$ ref.", fontsize=8)
fig.tight_layout()
fig.savefig(f"{WD}/figures/task8_defect_energy_map.png", dpi=150)
plt.close(fig)

# --- Figure 2: stiffness anisotropy + phonon curvature ---------------------
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(11, 4.6))
bi = np.loadtxt(f"{WD}/tables/task8_biaxial_f3.csv", delimiter=",", skiprows=1)
ax1.plot(bi[:, 0] * 180 / math.pi, bi[:, 1], "C0-")
ax1.axhline(384 * A2, color="k", ls="--", lw=1, label="uniaxial $+384A^2$")
ax1.axhline(-384 * A2, color="k", ls="--", lw=1, label="uniaxial $-384A^2$")
ax1.set_xlabel("biaxial angle $t$ (deg), $\\epsilon=\\mathrm{diag}(\\cos t,\\sin t,0,0)$")
ax1.set_ylabel("cubic coefficient $f_3$  ($f = f_2 e^2 + f_3 e^3$)")
ax1.set_title("(a) cubic (anharmonic) stiffness: first anisotropy")
ax1.legend(fontsize=8)
ax1.set_xlim(0, 360)
pr = np.loadtxt(f"{WD}/tables/task8_phonon_rates.csv", delimiter=",", skiprows=1,
                dtype=str)
# columns: q, pol, dF, dF_an, relerr, dF_grad, dF_grad_an, relerr_grad, dF_nl,
#          lin, grad_mu_sq, Gamma
q = np.array([float(r[0]) for r in pr])
pol = np.array([r[1] for r in pr])
dF = np.array([float(r[2]) for r in pr])
y = dF / (A2 * 0.01 ** 2 * q ** 2)
qq = np.linspace(0, 4.3, 50)
for p, c0, mk in (("L", 192.0, "o"), ("T", 64.0, "s")):
    m = (pol == p) & (q < 2.0)
    mx = (pol == p) & (q >= 2.0)
    ax2.plot(q[m] ** 2, y[m], mk, label=f"{p} measured ($q<2$)")
    ax2.plot(q[mx] ** 2, y[mx], "x", ms=9, mew=2,
             label=f"{p} $q=2$ excluded" if p == "L" else "")
    ax2.plot(qq, c0 + 12 * qq, "-", label=f"{p}: ${c0} + 12q^2$ exact")
ax2.set_xlabel("$q^2$")
ax2.set_ylabel("$\\Delta F / (A^2 U^2 q^2)$")
ax2.set_title("(b) phase-mode curvature vs $q^2$")
ax2.legend(fontsize=8)
ax2.set_xlim(0, 4.3)
fig.tight_layout()
fig.savefig(f"{WD}/figures/task8_stiffness.png", dpi=150)
plt.close(fig)
print("wrote figures/task8_defect_energy_map.png, figures/task8_stiffness.png")
print("EXIT 0")
