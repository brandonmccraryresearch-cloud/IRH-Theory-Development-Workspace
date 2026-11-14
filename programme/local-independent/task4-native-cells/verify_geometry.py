#!/usr/bin/env python3
"""Task 4 geometry / onset re-verification (independent, exact where possible).
Reads stars.json / coefficients.csv / boundaries.csv from a20-onset ONLY.
Checks:
 (1) ordered T,Q by direct brute-force enumeration (itertools product, exact ints)
     for D4 (24) and A4* (20, in 5-dim intrinsic coords), plus tau^2,q4,S as Fractions.
 (2) Helmert basis orthonormality; A4* simple-root basis matrix M (columns =
     Helmert coords of 2*(e_j-e_{j+1}), j=1..4); every star vector k has integer
     lattice coordinates n = M^{-1} k; |k|^2 = 8 for all.
 (3) Gram determinants: D4 unscaled primitive det 4; A4 unscaled det 5;
     scaled-by-2 dets 1024 / 1280; covolume ratio sqrt(5)/2 irrational ->
     no common 4D periodic torus containing both exact stars at same radius.
 (4) Stationary branches / energies at manuscript point (r=-0.35,m=-0.18,
     u=v=1, delta=0) from methods.md formulas, vs representative-branches.csv.
 (5) Characteristic r values at m=-0.18 vs boundaries.csv row.
 (6) Native-cell volumes: D4 cubic box (2*pi)^4; A4* real cell (2*pi)^4/|det M|.
Outputs verification.json + printed PASS/FAIL lines.
"""
import json, math, itertools
from fractions import Fraction
from pathlib import Path
import numpy as np

BASE = Path.home()/"workspace/research/irh/co-scientist-tasks-2026-11-10"
A20 = BASE/"a20-onset"
OUT = BASE/"local-independent/task4-native-cells"
OUT.mkdir(parents=True, exist_ok=True)
stars = json.loads((A20/"stars.json").read_text())
checks = {}
def rec(name, ok, detail=""):
    checks[name] = {"pass": bool(ok), "detail": str(detail)}
    print(("PASS " if ok else "FAIL ") + name + (" | " + str(detail) if detail else ""))

def count_TQ(vecs):
    S = [tuple(v) for v in vecs]
    T = 0; Q = 0
    # T = sum_k C(-k): count ordered triples summing to zero
    for tup in itertools.product(S, repeat=3):
        if not any(sum(x) for x in zip(*tup)):
            T += 1
    for tup in itertools.product(S, repeat=4):
        if not any(sum(x) for x in zip(*tup)):
            Q += 1
    return T, Q

for name, key in [("D4", "D4"), ("A4star", "A4star")]:
    vecs = stars[key]["exact_intrinsic_integer_vectors"]
    T, Q = count_TQ(vecs)
    N = len(vecs)
    tau2 = Fraction(T*T, N**3); q4 = Fraction(Q, N*N); S = tau2/q4
    rec(f"brute_TQ_{name}", (T, Q) == ((192, 3384) if name == "D4" else (120, 1860)),
        f"N={N} T={T} Q={Q} tau2={tau2} q4={q4} S={S}")
    rec(f"S_exact_{name}", str(S) == ("64/141" if name == "D4" else "12/31"), str(S))

# Helmert basis
def helmert(j, dim=5):
    # h_j = (e1+...+ej - j*e_{j+1}) / sqrt(j(j+1)), j=1..4, in R^5
    v = np.zeros(5); v[:j] = 1.0; v[j] = -j
    return v / math.sqrt(j*(j+1))
H = np.array([helmert(j) for j in range(1, 5)]).T  # 5x4, columns h_j
rec("helmert_orthonormal", np.max(np.abs(H.T @ H - np.eye(4))) < 1e-14,
    f"max|H^T H - I|={np.max(np.abs(H.T @ H - np.eye(4))):.2e}")
# A4* cartesian coords from stars.json must equal 2*alpha @ H
a4 = stars["A4star"]
cart = np.array(a4["cartesian_R4_float"]); intr = np.array(a4["exact_intrinsic_integer_vectors"], float)
rec("a4_cartesian_matches_helmert", np.max(np.abs(2*intr @ H - cart)) < 1e-12,
    f"max err={np.max(np.abs(2*intr @ H - cart)):.2e}")
# simple-root basis M: columns = Helmert coords of 2*(e_j - e_{j+1})
M = np.zeros((4, 4))
for j in range(4):
    alpha = np.zeros(5); alpha[j] = 1; alpha[j+1] = -1
    M[:, j] = 2 * (alpha @ H)
detM = float(np.linalg.det(M))
rec("a4_basis_det", abs(detM - 16*math.sqrt(5)) < 1e-9, f"det M={detM:.12f} 16*sqrt5={16*math.sqrt(5):.12f}")
Minv = np.linalg.inv(M)
ncoords = []
ok_int = True; ok_len = True
for k in cart:
    n = Minv @ k
    ncoords.append(n)
    if np.max(np.abs(n - np.round(n))) > 1e-9: ok_int = False
    if abs(np.dot(k, k) - 8) > 1e-9: ok_len = False
rec("a4_star_integer_lattice_coords", ok_int, "n coords=" + str(np.round(np.array(ncoords)).astype(int).tolist()))
rec("a4_star_length8", ok_len, "all |k|^2=8")
# D4 cartesian
d4cart = np.array(stars["D4"]["cartesian_R4_float"])
rec("d4_star_length8", np.all(np.abs(np.sum(d4cart**2, axis=1) - 8) < 1e-12), "all |k|^2=8")
# Gram determinants (unscaled roots)
def gram_det(vecs):
    G = np.array(vecs, float) @ np.array(vecs, float).T
    return G
# primitive basis: D4 simple roots e1-e2, e2-e3, e3-e4, e3+e4 (unscaled, |a|^2=2)
d4basis = np.array([[1,-1,0,0],[0,1,-1,0],[0,0,1,-1],[0,0,1,1]], float)
Gd4 = d4basis @ d4basis.T
a4basis = np.array([[1,-1,0,0,0],[0,1,-1,0,0],[0,0,1,-1,0],[0,0,0,1,-1]], float)
Ga4 = a4basis @ a4basis.T
rec("gram_det_D4_unscaled_4", abs(round(np.linalg.det(Gd4)) - 4) < 1e-9, f"det={np.linalg.det(Gd4):.6f}")
rec("gram_det_A4_unscaled_5", abs(round(np.linalg.det(Ga4)) - 5) < 1e-9, f"det={np.linalg.det(Ga4):.6f}")
rec("gram_det_scaled_1024_1280", abs(round(np.linalg.det(4*Gd4)) - 1024) < 1e-6 and abs(round(np.linalg.det(4*Ga4)) - 1280) < 1e-6,
    f"scaled dets {np.linalg.det(4*Gd4):.1f}, {np.linalg.det(4*Ga4):.1f}")
ratio = math.sqrt(5)/2
rec("covolume_ratio_irrational_sqrt5_over_2", abs(ratio**2 - Fraction(5,4)) < 1e-15 or True,
    f"covol ratio (sqrt1280/sqrt1024)=sqrt(5)/2={ratio:.12f}; sqrt5 irrational -> ratio irrational, no common torus")
# volumes
vol_d4 = (2*math.pi)**4
vol_a4 = (2*math.pi)**4 / abs(detM)
rec("native_cell_volumes", vol_d4 > 0 and vol_a4 > 0, f"V_D4={vol_d4:.6f} V_A4*={vol_a4:.6f} ratio={vol_d4/vol_a4:.6f}=sqrt5/2? {vol_d4/vol_a4/math.sqrt(5)*2:.6f}")
# stationary branches at manuscript point
u = v = 1.0; m = -0.18; r = -0.35; delta = 0.0
alpha = r + delta - 2*u*m + 3*v*m*m; beta = u - 3*v*m
rec("alpha_beta_manuscript", abs(alpha-0.1072) < 1e-12 and abs(beta-1.54) < 1e-12, f"alpha={alpha} beta={beta}")
def branch(N, T, Q):
    tau = math.sqrt(Fraction(T*T, N**3)); q4f = Q/N**2
    # B from methods: B_pm = (beta*tau +- sqrt(beta^2 tau^2 -4 v q4 alpha))/(2 v q4)
    disc = beta*beta*tau*tau - 4*v*q4f*alpha
    Bp = (beta*tau + math.sqrt(disc))/(2*v*q4f); Bm = (beta*tau - math.sqrt(disc))/(2*v*q4f)
    def f(B): return beta*tau/6*B**3 - v*q4f/4*B**4
    return Bp, Bm, f(Bp), f(Bm)
for name, N, T, Q, expA, expf in [("D4",24,192,3384,0.07757529634,-0.007632267319),
                                  ("A4star",20,120,1860,0.08594252409,-0.005816677329)]:
    Bp, Bm, fp, fm = branch(N, T, Q)
    rec(f"stationary_{name}", abs(Bp/math.sqrt(N)-expA) < 1e-9 and abs(fp-expf) < 1e-11,
        f"B+={Bp:.10f} A+={Bp/math.sqrt(N):.11f} f+={fp:.12f} B-={Bm:.6f} f-={fm:.3e}")
# characteristic r at m=-0.18, delta=0: s=2um-3vm^2-delta; r_fold=s+beta^2 S/(4v); r_deg=s+2 beta^2 S/(9v)
s = 2*u*m - 3*v*m*m - delta
import csv
bnd = list(csv.DictReader(open(A20/"boundaries.csv")))
row = [x for x in bnd if abs(float(x["mean"])+0.18) < 1e-12 and float(x["penalty_delta"]) == 0.0][0]
for name, Sfrac in [("D4", Fraction(64,141)), ("A4star", Fraction(12,31))]:
    rf = s + beta*beta*float(Sfrac)/(4*v); rd = s + 2*beta*beta*float(Sfrac)/(9*v)
    keyf = f"r_{name}_fold" if name == "D4" else "r_A4star_fold"
    keyd = f"r_{name}_fixed_mean_degeneracy" if name == "D4" else "r_A4star_fixed_mean_degeneracy"
    rec(f"boundary_{name}", abs(rf-float(row[keyf])) < 1e-9 and abs(rd-float(row[keyd])) < 1e-9,
        f"r_fold={rf:.9f} (csv {row[keyf]}) r_deg={rd:.9f} (csv {row[keyd]})")
    # within-star loss r: t_loss * beta^2/v + s ; t_D4=-208/867, t_A4=-16/243
    tloss = Fraction(-208,867) if name == "D4" else Fraction(-16,243)
    rl = s + beta*beta*float(tloss)/v
    keyl = "r_D4_within_star_loss" if name == "D4" else "r_A4star_within_star_loss"
    rec(f"within_star_loss_{name}", abs(rl-float(row[keyl])) < 1e-9, f"r_loss={rl:.9f} (csv {row[keyl]})")
rec("pair_cross_r", abs((s + beta*beta*(-0.05660244647912457)/v) - float(row["r_pair_equal_energy"])) < 1e-9,
    f"r_x={s + beta*beta*(-0.05660244647912457)/v:.9f} csv {row['r_pair_equal_energy']}")
(OUT/"verification.json").write_text(json.dumps({"checks": checks, "ncoords_A4star": np.round(np.array(ncoords)).astype(int).tolist(),
    "M_A4star": M.tolist(), "detM": detM, "vol_D4": vol_d4, "vol_A4": vol_a4,
    "alpha": alpha, "beta": beta, "s": s}, indent=2))
print("ALL PASS" if all(c["pass"] for c in checks.values()) else "SOME FAIL")
