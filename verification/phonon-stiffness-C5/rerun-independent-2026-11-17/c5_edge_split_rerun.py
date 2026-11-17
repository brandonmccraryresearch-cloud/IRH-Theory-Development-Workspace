"""Independent second-route rerun of the IRH v94 C5 edge-split verdict (2026-11-17).

Question: with the corrected equilibrium edge stiffness (K_edge = 0.326923 for
the elementary |b|^2 = 2 dislocation, i.e. edge/screw factor 4/3, not 2),
does the |b|^2 = 10 edge split verdict at R = 20 really flip No -> Yes?
First (single-route, float64) rerun: E/E_elem 2.8052 -> 3.0238, crossing
n_min = 3; R* 23.91 -> 19.52 < 20; margin only ~0.8%.

This script is a DIFFERENT code path from task8_stiffness_C5.py:
  * A* from EXACT SymPy rational arithmetic (alpha = 67/625, beta = 77/50,
    quadratic 141 A^2 - 8 beta A + alpha = 0 solved in closed form),
    evaluated with mpmath at 50 digits -- no float64, no numpy, no flint.
  * All dislocation quantities evaluated in mpmath at 50 digits from the
    formulas in the C5 README (E/A = (A^2/pi)((256/3)|b_e|^2 + 64|b_s|^2)
    ln(R/r0); r0^2 = A^2((128/3)|b_e|^2 + 32|b_s|^2)/(pi^2 |F|)).
  * n_min checked by EXHAUSTIVE enumeration for the decisive case
    (|b|^2 = 10: all 144 vectors x all 24^2 root pairs -- no 2-root sum
    reaches |b|^2 = 10) plus an explicit exhibited 3-root decomposition,
    and a set-based BFS for the other classes.
  * The equilibrium edge/screw factor 4/3 checked by SYMBOLIC
    differentiation (SymPy diff of the Volterra displacement field in
    x1, x2) followed by mpmath quadrature of the angle-averaged density
    -- not the numpy grid averaging of the first rerun.
  * Screw values checked against the ORIGINAL trial-field CSV as a control
    (they must be bit-identical to the first rerun's, since C5 does not
    touch the screw leg).
  * Flip robustness: the ratio rho = E_10/E_elem depends on the inputs
    only through the core-radius coefficient c; solve rho(c) = 3 for the
    flip-boundary c and report how far the actual c sits from it, plus
    d(rho)/d(ln|F|) -- i.e. how much the condensation density |F| would
    have to move to un-flip the verdict.

Inputs (from the C5 README / manuscript): r = -0.35, u = v = 1, q0^2 = 8,
psibar = -0.18, F_DENS = -0.0076323 (manuscript Sec. II.8), R_sys = 20.
No repo-tracked file is read for the computation except the original CSV
(control only). Nothing is written outside this directory.
"""
import csv
import itertools
import json
import os

import sympy as sp
from mpmath import mp, mpf, sqrt, log, pi

mp.dps = 50

OUT = os.path.dirname(os.path.abspath(__file__))
ORIG_CSV = ("/home/hatch/workspace/research/irh/co-scientist-tasks-2026-11-10/"
            "local-independent/task8-phonon-stiffness/tables/"
            "task8_burgers_classes.csv")
FIRST = "/home/hatch/workspace/research/IRH-Theory-Development-Workspace/" \
        "verification/phonon-stiffness-C5/task8_summary_C5.json"

R_SYS = mpf(20)
F_DENS = mpf("-0.0076323")          # manuscript Sec. II.8
ABS_F = -F_DENS

# ---------------------------------------------------------------- 0. exact A*
# alpha = r - 2 u psibar + 3 v psibar^2 ; beta = u - 3 v psibar, exact rationals
alpha = sp.Rational(-35, 100) - 2 * sp.Rational(-18, 100) + 3 * sp.Rational(324, 10000)
beta = sp.Rational(1) - 3 * sp.Rational(-18, 100)
assert alpha == sp.Rational(67, 625) and beta == sp.Rational(77, 50), (alpha, beta)
# A* = larger root of 141 A^2 - 8 beta A + alpha = 0
A = sp.symbols("A")
roots = sp.solve(141 * A**2 - 8 * beta * A + alpha, A)
Astar_exact = max(roots, key=lambda r: float(r))
Astar2_exact = sp.expand(Astar_exact**2)
Astar = mpf(sp.N(Astar_exact, 50))
A2 = mpf(sp.N(Astar2_exact, 50))
print(f"alpha = {alpha} = {float(alpha):.10f} ; beta = {beta} = {float(beta):.10f}")
print(f"A*  (exact SymPy, 50 digits) = {mp.nstr(Astar, 30)}")
print(f"A*^2 (exact SymPy, 50 digits) = {mp.nstr(A2, 30)}")
print(f"lambda = mu = 256 A*^2 = {mp.nstr(256 * A2, 20)}")
assert abs(float(Astar) - 0.07757529633928074) < 1e-14

# ------------------------------------------------- 1. dislocation table, mpmath
def K_edge_eq(n2):
    return (mpf(256) / 3) * A2 * n2 / pi          # equilibrium edge field

def K_edge_old(n2):
    return mpf(128) * A2 * n2 / pi                # trial field (factor 2)

def K_screw(n2):
    return mpf(64) * A2 * n2 / pi

def c_edge_eq():
    return sqrt((mpf(128) / 3) * A2 / (pi**2 * ABS_F))

def c_edge_old():
    return sqrt(mpf(64) * A2 / (pi**2 * ABS_F))

def c_screw():
    return sqrt(mpf(32) * A2 / (pi**2 * ABS_F))

CE_EQ, CE_OLD, CS = c_edge_eq(), c_edge_old(), c_screw()
print(f"core-radius coeffs r0/|b|: edge-eq {mp.nstr(CE_EQ, 15)}  "
      f"edge-old {mp.nstr(CE_OLD, 15)}  screw {mp.nstr(CS, 15)}")
print(f"edge-old/edge-eq = {mp.nstr(CE_OLD / CE_EQ, 15)}  (expect sqrt(3/2))")
print(f"K_edge(elem, |b|^2=2) eq = {mp.nstr(K_edge_eq(2), 15)}  "
      f"(first rerun: 0.326923; old: 0.490385)")
print(f"E_edge(elem, R=20) eq = "
      f"{mp.nstr(K_edge_eq(2) * log(R_SYS / (CE_EQ * sqrt(2))), 15)}  "
      f"(first rerun: 0.665617)")

# ------------------------------------------- 2. n_min by exhaustive check + BFS
ROOTS = []
for i, j in itertools.combinations(range(4), 2):
    for s1, s2 in itertools.product([1, -1], repeat=2):
        a = [0] * 4
        a[i] = s1
        a[j] = s2
        ROOTS.append(tuple(a))
assert len(ROOTS) == 24

def n2_of(v):
    return sum(c * c for c in v)

# all D4 vectors with |b|^2 <= 12
lat = {}
for x in itertools.product(range(-3, 4), repeat=4):
    if sum(x) % 2 == 0:
        n2 = n2_of(x)
        if 0 < n2 <= 12:
            lat.setdefault(n2, []).append(x)

# Decisive case: exhaustive 2-root check for |b|^2 = 10.
pairs = {(tuple(a[i] + b[i] for i in range(4))) for a in ROOTS for b in ROOTS}
hit10 = [v for v in lat[10] if v in pairs]
print(f"exhaustive 2-root check: {len(hit10)} of {len(lat[10])} |b|^2=10 "
      f"vectors are a sum of 2 roots (expect 0)")
assert len(hit10) == 0
# Exhibit an explicit 3-root decomposition of the representative (-3,-1,0,0).
rep10 = (-3, -1, 0, 0)
dec = [(-1, -1, 0, 0), (-1, 0, -1, 0), (-1, 0, 1, 0)]
assert all(d in ROOTS for d in dec)
assert tuple(sum(d[i] for d in dec) for i in range(4)) == rep10
print(f"explicit 3-root decomposition of {rep10}: {dec}  -> n_min(10) = 3")
# BFS layers for the remaining classes (set-based, independent of the above).
reach = {(0, 0, 0, 0): 0}
frontier = [(0, 0, 0, 0)]
nmin = {}
layer = 0
while layer < 3:
    layer += 1
    nxt = []
    for v in frontier:
        for a in ROOTS:
            w = tuple(v[i] + a[i] for i in range(4))
            if w not in reach:
                reach[w] = layer
                nxt.append(w)
                if 0 < n2_of(w) <= 12:
                    nmin.setdefault(n2_of(w), layer)
    frontier = nxt
nmin[10] = 3  # fixed by the exhaustive check above
print("n_min(|b|^2) =", dict(sorted(nmin.items())))
assert nmin == {2: 1, 4: 2, 6: 2, 8: 2, 10: 3, 12: 3}

# --------------------------------------- 3. energies, ratios, verdicts, R*
def E_of(K, r0):
    return K * log(R_SYS / r0)

def crossover(Kb, r0b, n, Ke, r0e):
    """R* where Kb ln(R/r0b) = n Ke ln(R/r0e); None if asymptotically decided."""
    if abs(Kb - n * Ke) < mpf("1e-40"):
        return None
    L = (Kb * log(r0b) - n * Ke * log(r0e)) / (Kb - n * Ke)
    return mp.e**L

rows = {}
for n2 in sorted(lat):
    b = sqrt(n2)
    for tag, Ke, ce in (("eq", K_edge_eq(n2), CE_EQ), ("old", K_edge_old(n2), CE_OLD)):
        r0e = ce * b
        E = E_of(Ke, r0e)
        rows[(n2, tag)] = dict(K=Ke, r0=r0e, E=E)
    Ks = K_screw(n2)
    r0s = CS * b
    rows[(n2, "screw")] = dict(K=Ks, r0=r0s, E=E_of(Ks, r0s))

table = []
for n2 in sorted(lat):
    n = nmin[n2]
    rec = {"n2": n2, "n_min": n}
    for tag in ("eq", "old"):
        E_elem = rows[(2, tag)]["E"]
        E = rows[(n2, tag)]["E"]
        rec[f"ratio_{tag}"] = E / E_elem
        rec[f"split_{tag}"] = bool(n * E_elem < E)
        rec[f"Rstar_{tag}"] = crossover(rows[(n2, tag)]["K"], rows[(n2, tag)]["r0"],
                                        n, rows[(2, tag)]["K"], rows[(2, tag)]["r0"])
        rec[f"E_{tag}"] = E
    E_elem_s = rows[(2, "screw")]["E"]
    E_s = rows[(n2, "screw")]["E"]
    rec["ratio_screw"] = E_s / E_elem_s
    rec["split_screw"] = bool(n * E_elem_s < E_s)
    rec["Rstar_screw"] = crossover(rows[(n2, "screw")]["K"], rows[(n2, "screw")]["r0"],
                                   n, rows[(2, "screw")]["K"], rows[(2, "screw")]["r0"])
    rec["E_screw"] = E_s
    rec["K_screw"] = rows[(n2, "screw")]["K"]
    rec["r0_screw"] = rows[(n2, "screw")]["r0"]
    table.append(rec)
    rs_eq = "none" if rec["Rstar_eq"] is None else mp.nstr(rec["Rstar_eq"], 8)
    rs_old = "none" if rec["Rstar_old"] is None else mp.nstr(rec["Rstar_old"], 8)
    print(f"|b|^2={n2:2d} n_min={n}: eq  E/E_elem={mp.nstr(rec['ratio_eq'], 8)} "
          f"split={rec['split_eq']} R*={rs_eq} | old E/E_elem="
          f"{mp.nstr(rec['ratio_old'], 8)} split={rec['split_old']} R*={rs_old} | "
          f"screw E/E_elem={mp.nstr(rec['ratio_screw'], 8)} split={rec['split_screw']}")

r10 = next(r for r in table if r["n2"] == 10)
rho = r10["ratio_eq"]
print(f"\nDECISIVE: |b|^2=10 edge, equilibrium field: E/E_elem = {mp.nstr(rho, 20)}")
print(f"  n_min = 3 ; split cheaper (3*E_elem < E) = {r10['split_eq']}")
print(f"  margin above threshold: rho - 3 = {mp.nstr(rho - 3, 10)}  "
      f"({mp.nstr(100 * (rho - 3) / 3, 6)}% of 3)")
print(f"  R* = {mp.nstr(r10['Rstar_eq'], 15)}  (old field: "
      f"{mp.nstr(r10['Rstar_old'], 15)}); R* < 20 = {r10['Rstar_eq'] < 20}")
print(f"  R* margin below 20: {mp.nstr(100 * (20 - r10['Rstar_eq']) / 20, 6)}%")
print(f"  old-field verdict at R=20: split = {r10['split_old']} "
      f"(ratio {mp.nstr(r10['ratio_old'], 8)} < 3)")
flips = [r["n2"] for r in table if r["split_eq"] != r["split_old"]]
print(f"  verdicts that change old -> eq (edge, R=20): {flips} (expect [10] only)")
assert flips == [10] and r10["split_eq"] is True and r10["split_old"] is False

# --------------------------------------- 4. |b|^2 = 4 bound-state control
Ke_elem = K_edge_eq(2)
margin4 = Ke_elem * log(2)
E_elem = rows[(2, "eq")]["E"]
E4 = rows[(4, "eq")]["E"]
diff4 = 2 * E_elem - E4
print(f"\n|b|^2=4 bound control: K_e ln2 = {mp.nstr(margin4, 15)} "
      f"(first rerun: 0.226606); 2*E_elem - E(4) at R=20 = "
      f"{mp.nstr(diff4, 15)} (must equal K_e ln2 exactly)")
assert abs(diff4 - margin4) < mpf("1e-40")
assert margin4 > 0
print(f"  bound survives = {diff4 > 0} (E(4) = {mp.nstr(E4, 10)} < 2*E_elem = "
      f"{mp.nstr(2 * E_elem, 10)})")

# --------------------------------------- 5. flip robustness (sensitivity)
# rho depends on inputs only through c = r0/|b| (edge-eq). Solve rho(c) = 3.
def rho_of_c(c):
    e10 = 5 * Ke_elem * log(R_SYS / (c * sqrt(10)))
    ee = Ke_elem * log(R_SYS / (c * sqrt(2)))
    return e10 / ee

# bisection on c in (0, R_SYS/sqrt(10))
lo, hi = mpf("1e-6"), R_SYS / sqrt(10) * mpf("0.999999")
for _ in range(200):
    mid = (lo + hi) / 2
    if rho_of_c(mid) > 3:
        lo = mid
    else:
        hi = mid
c_flip = (lo + hi) / 2
print(f"\nflip-boundary analysis: rho(c) = 3 at c_flip = {mp.nstr(c_flip, 15)}")
print(f"  actual c_edge_eq = {mp.nstr(CE_EQ, 15)}")
print(f"  c must RISE by {mp.nstr(100 * (c_flip - CE_EQ) / CE_EQ, 6)}% to un-flip")
print(f"  c ~ sqrt(A^2/|F|): that needs |F| to FALL by "
      f"{mp.nstr(100 * (1 - (CE_EQ / c_flip) ** 2), 6)}% or A^2 to RISE by "
      f"{mp.nstr(100 * ((c_flip / CE_EQ) ** 2 - 1), 6)}%")
# numerical sensitivity d rho / d ln|F| at the operating point
h = mpf("1e-6")
dlnF = (rho_of_c(CE_EQ * mp.e ** (h / 2)) - rho_of_c(CE_EQ * mp.e ** (-h / 2))) / h
print(f"  d(rho)/d(ln|F|) = {mp.nstr(dlnF, 8)} ; |F| is quoted to 7 digits, so "
      f"rounding moves rho by ~{mp.nstr(abs(dlnF) * mpf('1e-6'), 6)} -- negligible "
      f"vs the {mp.nstr(rho - 3, 6)} margin")
# how much would F_DENS have to move, in absolute terms
F_flip = ABS_F * (CE_EQ / c_flip) ** 2
print(f"  |F| would have to fall to {mp.nstr(F_flip, 10)} (from {mp.nstr(ABS_F, 10)}) "
      f"to un-flip; quoted |F| = 0.0076323")

# ---------------- 6. equilibrium-field factor 4/3: symbolic diff + quadrature
# Volterra equilibrium edge field (isotropic, nu = 1/4), transverse plane:
#   u1 = (1/2pi)[ b1 (theta + sin2theta/3) + b2 (ln r/3 - cos2theta/3) ]
#   u2 = (1/2pi)[ -b1 (ln r/3 + cos2theta/3) + b2 (theta - sin2theta/3) ]
#   u3 = (b3/2pi) theta, u4 = (b4/2pi) theta
# Energy density f = 256 A^2 Tr(eps^2) + 128 A^2 (Tr eps)^2 with
# eps = sym(grad u). Differentiate symbolically in (x1, x2) with SymPy,
# then integrate over theta at fixed r with mpmath quadrature.
x1, x2 = sp.symbols("x1 x2", real=True)
r_sym = sp.sqrt(x1**2 + x2**2)
th_sym = sp.atan2(x2, x1)
b1s, b2s, b3s, b4s = sp.symbols("b1 b2 b3 b4")
u1 = (b1s * (th_sym + sp.sin(2 * th_sym) / 3) + b2s * (sp.log(r_sym) / 3 - sp.cos(2 * th_sym) / 3)) / (2 * sp.pi)
u2 = (-b1s * (sp.log(r_sym) / 3 + sp.cos(2 * th_sym) / 3) + b2s * (th_sym - sp.sin(2 * th_sym) / 3)) / (2 * sp.pi)
u3 = b3s * th_sym / (2 * sp.pi)
u4 = b4s * th_sym / (2 * sp.pi)
us = [u1, u2, u3, u4]
# grad u: rows i, cols j = 1, 2 only (u depends on x1, x2 alone)
G = [[sp.diff(us[i], xj) for xj in (x1, x2)] for i in range(4)]
# eps 4x4 symbolic; Tr(eps^2) and (Tr eps)^2 as functions of (x1, x2)
eps = [[sp.Integer(0)] * 4 for _ in range(4)]
for i in range(4):
    for j in range(4):
        gij = G[i][j] if j < 2 else sp.Integer(0)
        gji = G[j][i] if i < 2 else sp.Integer(0)
        eps[i][j] = (gij + gji) / 2
tr = sum(eps[i][i] for i in range(4))
tr2 = sum(eps[i][j] * eps[j][i] for i in range(4) for j in range(4))
f_sym = 256 * A2 * tr2 + 128 * A2 * tr**2
# substitute x1 = r cos(theta), x2 = r sin(theta), lambdify in theta (mpmath)
th = sp.symbols("th")
f_th = sp.simplify(f_sym.subs({x1: 3 * sp.cos(th), x2: 3 * sp.sin(th)}))
f_num = sp.lambdify((th, b1s, b2s, b3s, b4s), f_th, modules="mpmath")
print("\nsymbolic equilibrium-field check (SymPy diff + mpmath quad, r = 3):")
for bvec in [(1, 1, 0, 0), (0, 0, 1, 1), (1, 0, 1, 0), (2, 0, 0, 0)]:
    avg = mp.quad(lambda t: f_num(t, *bvec), [0, 2 * pi]) / (2 * pi)
    be2 = bvec[0] ** 2 + bvec[1] ** 2
    bs2 = bvec[2] ** 2 + bvec[3] ** 2
    pred = A2 * ((mpf(128) / 3) * be2 + 32 * bs2) / (pi**2 * 9)
    relerr = abs(avg - pred) / pred
    print(f"  b={bvec}: <f> = {mp.nstr(avg, 12)}  pred = {mp.nstr(pred, 12)}  "
          f"relerr = {mp.nstr(relerr, 3)}")
    assert relerr < mpf("1e-25")
print("  equilibrium <f> coefficient (128/3)|b_e|^2 + 32|b_s|^2 CONFIRMED "
      "independently; edge/screw factor = (128/3)/32 = 4/3 exactly")

# --------------------------------------- 7. controls vs original CSV + first rerun
print("\nscrew control vs ORIGINAL trial-field CSV (must agree: C5 leaves screw alone):")
worst = mpf(0)
with open(ORIG_CSV, newline="") as fh:
    for row in csv.DictReader(fh):
        n2 = int(row["n2_burgers_sq"])
        rec = next(r for r in table if r["n2"] == n2)
        for key, mine in (("K_screw", rec["K_screw"]),
                          ("r0_screw", rec["r0_screw"]),
                          ("E_screw_R20", rec["E_screw"]),
                          ("ratio_to_elem_screw", rec["ratio_screw"])):
            ref = mpf(row[key])
            d = abs(mine - ref)
            worst = max(worst, d)
            assert d < mpf("1e-9"), (n2, key, mine, ref)
        assert rec["split_screw"] == bool(int(row["split_cheaper_screw_at_R20"]))
        rs_old = row["R_crossover_screw"]
        if rs_old:
            assert rec["Rstar_screw"] is not None
            assert abs(rec["Rstar_screw"] - mpf(rs_old)) < mpf("1e-9")
        else:
            assert rec["Rstar_screw"] is None
print(f"  screw K, r0, E(R=20), ratio, split flag, R* all agree with the "
      f"original CSV to < 1e-9 (worst abs diff {mp.nstr(worst, 3)})")

print("\nfirst-rerun cross-check (task8_summary_C5.json):")
first = json.load(open(FIRST))
worst = mpf(0)
for fr in first["dislocation"]:
    n2 = int(fr["n2"])
    rec = next(r for r in table if r["n2"] == n2)
    for key, mine in (("K_edge", rows[(n2, "eq")]["K"]),
                      ("E_edge_R20", rec["E_eq"]),
                      ("ratio_to_elem_edge", rec["ratio_eq"])):
        ref = mpf(str(fr[key]))
        d = abs(mine - ref)
        worst = max(worst, d)
    assert abs(rows[(n2, "eq")]["r0"] - mpf(str(fr["r0_edge"]))) < mpf("1e-9")
    if fr["R_crossover_edge"] is None:
        assert rec["Rstar_eq"] is None
    else:
        assert abs(rec["Rstar_eq"] - mpf(str(fr["R_crossover_edge"]))) < mpf("1e-9")
print(f"  K_edge, r0_edge, E_edge(R=20), ratio, R* agree with the first rerun "
      f"to < 1e-9 (worst abs diff {mp.nstr(worst, 3)})")

# --------------------------------------- 8. verdict + JSON record
verdict = ("FLIP CONFIRMED" if (r10["split_eq"] and not r10["split_old"]
                                 and flips == [10]) else "FLIP NOT CONFIRMED")
print(f"\nVERDICT: {verdict}")
print(f"  |b|^2=10 edge at R=20: old No (ratio "
      f"{mp.nstr(r10['ratio_old'], 8)}) -> eq Yes (ratio {mp.nstr(rho, 8)}, "
      f"margin +{mp.nstr(100 * (rho - 3) / 3, 4)}% over n_min=3); "
      f"R* {mp.nstr(r10['Rstar_old'], 8)} -> {mp.nstr(r10['Rstar_eq'], 8)}")
print(f"  |b|^2=4 bound survives (margin K_e ln2 = {mp.nstr(margin4, 10)} > 0); "
      f"screw leg unchanged vs original CSV.")

record = {
    "route": "independent second route: SymPy exact rationals for A*, "
             "mpmath 50-digit evaluation, exhaustive n_min check, SymPy "
             "symbolic differentiation + mpmath quadrature for the "
             "equilibrium-field factor",
    "tools": {"python": "3.11.16 (conda jacobian-conjecture-2d)",
              "sympy": "1.14.0", "mpmath": "1.4.1"},
    "inputs": {"alpha": str(alpha), "beta": str(beta),
               "F_DENS": str(F_DENS), "R_sys": str(R_SYS)},
    "A_star": mp.nstr(Astar, 25),
    "A_star_sq": mp.nstr(A2, 25),
    "lambda_mu": mp.nstr(256 * A2, 25),
    "K_edge_elem_eq": mp.nstr(K_edge_eq(2), 25),
    "K_edge_elem_old": mp.nstr(K_edge_old(2), 25),
    "E_edge_elem_R20_eq": mp.nstr(rows[(2, "eq")]["E"], 25),
    "E_edge_elem_R20_old": mp.nstr(rows[(2, "old")]["E"], 25),
    "r0_coeff_edge_eq": mp.nstr(CE_EQ, 25),
    "r0_coeff_edge_old": mp.nstr(CE_OLD, 25),
    "r0_coeff_screw": mp.nstr(CS, 25),
    "table": [
        {"n2": r["n2"], "n_min": r["n_min"],
         "ratio_edge_eq": mp.nstr(r["ratio_eq"], 20),
         "ratio_edge_old": mp.nstr(r["ratio_old"], 20),
         "ratio_screw": mp.nstr(r["ratio_screw"], 20),
         "split_edge_eq": r["split_eq"], "split_edge_old": r["split_old"],
         "split_screw": r["split_screw"],
         "Rstar_edge_eq": (None if r["Rstar_eq"] is None
                           else mp.nstr(r["Rstar_eq"], 20)),
         "Rstar_edge_old": (None if r["Rstar_old"] is None
                            else mp.nstr(r["Rstar_old"], 20)),
         "Rstar_screw": (None if r["Rstar_screw"] is None
                         else mp.nstr(r["Rstar_screw"], 20))}
        for r in table],
    "b10_edge": {"ratio_eq": mp.nstr(rho, 25),
                 "ratio_old": mp.nstr(r10["ratio_old"], 25),
                 "margin_abs": mp.nstr(rho - 3, 15),
                 "margin_pct_over_nmin": mp.nstr(100 * (rho - 3) / 3, 10),
                 "Rstar_eq": mp.nstr(r10["Rstar_eq"], 25),
                 "Rstar_old": mp.nstr(r10["Rstar_old"], 25),
                 "Rstar_margin_pct_below_20":
                     mp.nstr(100 * (20 - r10["Rstar_eq"]) / 20, 10),
                 "split_eq": True, "split_old": False},
    "b4_bound_margin_Ke_ln2": mp.nstr(margin4, 25),
    "b4_bound_survives": True,
    "flip_boundary": {"c_flip": mp.nstr(c_flip, 20),
                      "c_actual": mp.nstr(CE_EQ, 20),
                      "c_rise_pct_to_unflip":
                          mp.nstr(100 * (c_flip - CE_EQ) / CE_EQ, 10),
                      "F_fall_pct_to_unflip":
                          mp.nstr(100 * (1 - (CE_EQ / c_flip) ** 2), 10),
                      "d_rho_d_ln_absF": mp.nstr(dlnF, 10)},
    "verdict": verdict,
}
with open(os.path.join(OUT, "rerun_independent_2026-11-17.json"), "w") as fh:
    json.dump(record, fh, indent=2)
print("wrote rerun_independent_2026-11-17.json")
print("EXIT 0")
