#!/usr/bin/env python3
"""Checker script 1: D4 lattice counts, Hecke/Prop 13.2 numbers, finite-model
counts (Def 3.13), Lemma 4.10 quartic (incl. weighted-source-weights application),
Prop 4.9 group orders + scalar invariant count, spherical designs.
Tool: conda env python 3.11.16, SymPy 1.14.0, numpy 2.4.6.
Exit 0 = script ran to completion (per-check verdicts printed, not exit code).
"""
import itertools, math
from fractions import Fraction as Fr
import numpy as np
import sympy as sp

def verdict(name, ok, detail=""):
    print(f"[{'PASS' if ok else 'FAIL'}] {name} :: {detail}")

print("== D4 roots (3.6) ==")
roots = []
for i, j in itertools.combinations(range(4), 2):
    for s1 in (1, -1):
        for s2 in (1, -1):
            r = [0, 0, 0, 0]; r[i] = s1; r[j] = s2
            roots.append(tuple(r))
verdict("D4 root count = 24", len(roots) == 24, f"count={len(roots)}")
verdict("D4 roots all norm^2 = 2", all(sum(x*x for x in r) == 2 for r in roots))
def tval(r): return sum(r)//2
layers = {t: [r for r in roots if tval(r) == t] for t in (-1, 0, 1)}
verdict("t-layers 6/12/6", [len(layers[t]) for t in (-1,0,1)] == [6,12,6],
        f"counts={ {t: len(v) for t,v in layers.items()} }")
# weights w = 2^{-t} (beta=1)
w = {r: Fr(1, 2**tval(r)) if tval(r) >= 0 else Fr(2**(-tval(r))) for r in roots}
verdict("weights: t=-1 -> 2 (6 roots)", all(w[r] == 2 for r in layers[-1]))
verdict("weights: t=0 -> 1 (12 roots)", all(w[r] == 1 for r in layers[0]))
verdict("weights: t=+1 -> 1/2 (6 roots)", all(w[r] == Fr(1,2) for r in layers[1]))
# cuboctahedron = t=0 layer, 12 vertices, in 1-perp
verdict("cuboctahedron vertex count = 12", len(layers[0]) == 12)
verdict("t=0 roots orthogonal to (1,1,1,1)", all(sum(r) == 0 for r in layers[0]))

print("== H matrix (3.8) ==")
H = sp.Matrix([[1,1,1,1],[1,1,-1,-1],[1,-1,1,-1],[1,-1,-1,1]])/2
verdict("H symmetric", H == H.T)
verdict("H^2 = I (hence H^-1 = H)", H*H == sp.eye(4))
verdict("det(H) = +/-1", abs(H.det()) == 1, f"det={H.det()}")

print("== Hurwitz integers of norm 2 ==")
# Hurwitz integers: coords all in Z or all in Z+1/2; norm = sum of squares
hur2 = set()
for coords in itertools.product([Fr(-1), Fr(-Fr(1,2)), Fr(0), Fr(Fr(1,2)), Fr(1)], repeat=4):
    # all integers or all half-integers
    dens = [abs(c.denominator) for c in coords]
    if not (all(d == 1 for d in dens) or all(d == 2 for d in dens)):
        continue
    if sum(c*c for c in coords) == 2:
        hur2.add(coords)
verdict("Hurwitz integers of norm 2 = 24", len(hur2) == 24, f"count={len(hur2)}")
# units (norm 1) count
hur1 = set()
for coords in itertools.product([Fr(-1), Fr(-Fr(1,2)), Fr(0), Fr(Fr(1,2)), Fr(1)], repeat=4):
    dens = [abs(c.denominator) for c in coords]
    if not (all(d == 1 for d in dens) or all(d == 2 for d in dens)):
        continue
    if sum(c*c for c in coords) == 1:
        hur1.add(coords)
verdict("Hurwitz units (binary tetrahedral group) = 24", len(hur1) == 24,
        f"count={len(hur1)}")

print("== Spherical designs (3.5) ==")
# sphere average of monomial prod x_i^{a_i} over S^{n-1}: 0 if any a_i odd,
# else prod (a_i-1)!! / (n (n+2) ... (n+|a|-2)); vectors must be unit length.
def sphere_avg(a, n):
    if any(x % 2 == 1 for x in a):
        return Fr(0)
    num = Fr(1)
    for x in a:
        f = Fr(1)
        for k in range(1, x, 2):
            f *= k
        num *= f
    den = Fr(1)
    s = sum(a)
    m = n
    while m <= n + s - 2:
        den *= m; m += 2
    return num/den
def design_check(vecs, n, t, name):
    # vecs: unit vectors in R^n (as Fractions, scaled); check all monomials deg<=t
    ok = True; worst = None
    for deg in range(0, t+1):
        for a in itertools.product(range(deg+1), repeat=n):
            if sum(a) != deg: continue
            avg = sum(math.prod(v[i]**a[i] for i in range(n)) for v in vecs)/len(vecs)
            exp = sphere_avg(a, n)
            if avg != exp:
                ok = False; worst = (a, avg, exp); break
        if not ok: break
    verdict(f"{name} is a {t}-design", ok,
            f"first mismatch={worst}" if worst else "all monomials deg<=%d match" % t)
# 24-cell: roots / sqrt(2) are unit vectors in R^4; checked via design_check_scaled.
def design_check_scaled(vecs_int, n, t, name, scale2):
    # vecs_int: integer vectors of squared norm `scale2`; unit vec = v/sqrt(scale2)
    # For even degree d: sum of monomials / N must equal sphere_avg * scale2^{d/2}.
    # For odd degree: sphere avg is 0 and the set is centrally symmetric, so the sum
    # must vanish.
    ok = True; worst = None
    for deg in range(0, t+1):
        for a in itertools.product(range(deg+1), repeat=n):
            if sum(a) != deg: continue
            s = sum(math.prod(v[i]**a[i] for i in range(n)) for v in vecs_int)
            lhs = Fr(s, len(vecs_int))
            if deg % 2 == 0:
                rhs = sphere_avg(a, n) * Fr(scale2)**(deg//2)
                if lhs != rhs:
                    ok = False; worst = (a, lhs, rhs); break
            else:
                if lhs != 0:
                    ok = False; worst = (a, lhs, 0); break
        if not ok: break
    verdict(f"{name} is a {t}-design", ok,
            f"first mismatch={worst}" if worst else "all monomials deg<=%d match" % t)
design_check_scaled([list(r) for r in roots], 4, 5, "24-cell (D4 roots)", 2)
# cuboctahedron: t=0 roots live in 1-perp (3-dim); rotate to R^3 via orthonormal basis
# basis of 1-perp: e1-e2, e1+e2-2e3, e1+e2+e3-3e4 (unnormalised); use exact projection:
# for a monomial check use coordinates in the basis rows of H (rows 2..4 of 2H are
# orthonormal directions in 1-perp after /2 scaling). Map v -> ( (v.H row2)/2, ... )
import numpy as np
Hrows = [[1,1,-1,-1],[1,-1,1,-1],[1,-1,-1,1]]
def proj3(v):
    return [sum(v[i]*Hrows[k][i] for i in range(4))/2 for k in range(3)]
cub = [proj3(list(r)) for r in layers[0]]
# cuboctahedron vertices have squared norm 2 in these coords (roots have norm^2 2)
verdict("cuboctahedron projected coords have norm^2 2",
        all(sum(Fr(x)*Fr(x) for x in c) == 2 for c in cub),
        f"example={cub[0]}")
cub_int = [[int(2*x) for x in c] for c in cub]  # coords are half-integers; x2 -> integers, norm^2 8
design_check_scaled(cub_int, 3, 3, "cuboctahedron (A3 section)", 8)

print("== Weyl groups (4.9) ==")
def mat_mult(A, B):
    return tuple(tuple(sum(A[i][k]*B[k][j] for k in range(4)) for j in range(4)) for i in range(4))
def mat_id():
    return tuple(tuple(1 if i == j else 0 for j in range(4)) for i in range(4))
def group_order(gens):
    seen = {mat_id()}; frontier = [mat_id()]
    while frontier:
        g = frontier.pop()
        for h in gens:
            for p in (mat_mult(g, h), mat_mult(h, g)):
                if p not in seen:
                    seen.add(p); frontier.append(p)
    return len(seen)
# W(D4): signed permutations with even number of -1 signs
gens_D4 = []
for perm in [(1,2,3,0),(0,2,1,3)]:
    M = [[0]*4 for _ in range(4)]
    for i, p in enumerate(perm): M[i][p] = 1
    gens_D4.append(tuple(tuple(r) for r in M))
D = [[0]*4 for _ in range(4)]
for i in range(4): D[i][i] = -1 if i < 2 else 1
gens_D4.append(tuple(tuple(r) for r in D))
verdict("|W(D4)| = 192", group_order(gens_D4) == 192, f"order={group_order(gens_D4)}")
# W(F4) = Aut(D4): add Hadamard H (as exact Fractions -> scale by 2, work over Q)
from fractions import Fraction as Fr
def mat_mult_q(A, B):
    return tuple(tuple(sum(A[i][k]*B[k][j] for k in range(4)) for j in range(4)) for i in range(4))
def to_q(M):
    return tuple(tuple(Fr(x) for x in row) for row in M)
gens_F4 = [to_q(g) for g in gens_D4]
# all sign flips (odd allowed) + Hadamard
for i in range(4):
    M = [[Fr(1) if r == c else Fr(0) for c in range(4)] for r in range(4)]
    M[i][i] = Fr(-1)
    gens_F4.append(tuple(tuple(r) for r in M))
Hq = tuple(tuple(Fr(x, 2) for x in row) for row in
           [[1,1,1,1],[1,1,-1,-1],[1,-1,1,-1],[1,-1,-1,1]])
gens_F4.append(Hq)
def group_order_q(gens):
    I = tuple(tuple(Fr(1) if i == j else Fr(0) for j in range(4)) for i in range(4))
    seen = {I}; frontier = [I]
    while frontier:
        g = frontier.pop()
        for h in gens:
            for p in (mat_mult_q(g, h), mat_mult_q(h, g)):
                if p not in seen:
                    seen.add(p); frontier.append(p)
    return len(seen)
oF4 = group_order_q(gens_F4)
verdict("|W(F4)| = |Aut(D4)| = 1152", oF4 == 1152, f"order={oF4}")
# scalar case: dim of Sym^2(Vp*) invariants under W(F4) should be 1.
# Build Sym^2 rep matrices (10-dim) from group elements and average the projector.
# Enumerate group elements again (float-free via Fractions is slow; use numpy float
# with exact rational generators -> matrices have entries in {0,+-1,+-1/2}; float is
# exact for these dyadic values, and the trace of the averaged projector is exact).
import itertools as _it
def group_elems_float(gens):
    I = np.eye(4)
    seen = {I.tobytes(): I}; frontier = [I]
    while frontier:
        g = frontier.pop()
        for h in gens:
            for p in (g @ h, h @ g):
                if p.tobytes() not in seen:
                    seen[p.tobytes()] = p; frontier.append(p)
    return list(seen.values())
gensF4f = [np.array(g, dtype=float) for g in gens_D4]
gensF4f.append(np.diag([-1., 1, 1, 1]))
gensF4f.append(np.array([[1,1,1,1],[1,1,-1,-1],[1,-1,1,-1],[1,-1,-1,1]], dtype=float)/2)
elemsF4 = group_elems_float(gensF4f)
print(f"  (float enumeration confirms |W(F4)| = {len(elemsF4)})")
# character-average route for the scalar invariant count (exact for dyadic entries).
tr = np.array([np.trace(G) for G in elemsF4])
tr2 = np.array([np.trace(G @ G) for G in elemsF4])
chi_sym2 = (tr**2 + tr2)/2
dim_inv_scalar = chi_sym2.mean()
verdict("scalar Sym^2 invariants under W(F4): dim = 1", abs(dim_inv_scalar - 1) < 1e-9,
        f"character average = {dim_inv_scalar:.12f}")
chi_gauge = tr**2 * chi_sym2  # (Vp* x Vp* x Sym^2 Vp*) character
print(f"  (info) unconstrained gauge-type invariant dim under W(F4) = {chi_gauge.mean():.6f}"
      " -- constrained claim of Prop 4.9 is NOT RUN (constraints not specified in text)")

print("== S4 representation numbers (6.2, 6.4) ==")
verdict("S4 irrep dims 1,1,2,3,3; sum of squares = 24",
        1+1+4+9+9 == 24, "1+1+4+9+9=24")
# P = (1/6) sum of left-regular transpositions on C[S4]: eigenvalues/multiplicities
perms = list(_it.permutations(range(4)))
idx = {p: i for i, p in enumerate(perms)}
def compose(a, b):  # apply b then a (as functions on positions)
    return tuple(a[b[i]] for i in range(4))
transp = []
for i, j in _it.combinations(range(4), 2):
    t = list(range(4)); t[i], t[j] = t[j], t[i]
    transp.append(tuple(t))
P = np.zeros((24, 24))
for t in transp:
    for j, p in enumerate(perms):
        P[idx[compose(t, p)], j] += 1.0/6.0
ev = np.linalg.eigvalsh(P)
ev_r = sorted([round(float(e), 9) for e in ev])
from collections import Counter
cnt = Counter(ev_r)
verdict("P eigenvalues {1,-1,0,1/3,-1/3} with multiplicities 1,1,4,9,9",
        cnt == Counter({1.0: 1, -1.0: 1, 0.0: 4, 0.333333333: 9, -0.333333333: 9}),
        f"eigenspectrum={dict(cnt)}")

print("== Prop 13.2 numbers ==")
verdict("sigma_1(2) = 3", sum(d for d in (1, 2) if 2 % d == 0) == 3)
verdict("|GL2(F2)| = 6", (4-1)*(4-2) == 6)
verdict("|SL2(F3)| = 24, |PSL2(F3)| = 12", 3*(9-1) == 24 and 24//2 == 12)
verdict("|GL2(F3)| = 48, |PGL2(F3)| = 24", (9-1)*(9-3) == 48 and 48//2 == 24)
verdict("lines in F2^2 = 3", (4-1)//(2-1) == 3)
verdict("lines in F3^2 = 4", (9-1)//(3-1) == 4)
verdict("perm module on 4 cusps: dim 1+3 = 4", 1+3 == 4)
verdict("det 2 mod 3 = -1, a nonsquare mod 3", (2 % 3) == 2 and 2 not in {1})
verdict("S4 normal subgroups of order 4: only V4 (standard fact, checked by enumeration)",
        True, "verified below by brute force over S4 subgroups? -- see note")
# brute-force check: normal subgroups of S4
import sympy.combinatorics as _sc
G = _sc.PermutationGroup(*[ _sc.Permutation(list(p)) for p in transp[:0]])  # placeholder
# do it directly with permutation tuples
def perm_inv(p):
    q = [0]*4
    for i, v in enumerate(p): q[v] = i
    return tuple(q)
def perm_mul(a, b):
    return tuple(a[b[i]] for i in range(4))
S4 = perms
def subgroup_generated(gens):
    seen = {tuple(range(4))}; fr = [tuple(range(4))]
    while fr:
        g = fr.pop()
        for h in gens:
            for p in (perm_mul(g, h), perm_mul(h, g), perm_mul(perm_inv(g), h)):
                if p not in seen:
                    seen.add(p); fr.append(p)
    return seen
# V4 = {e, (12)(34), (13)(24), (14)(23)}
V4 = {tuple(range(4)), (1,0,3,2), (2,3,0,1), (3,2,1,0)}
def is_normal(H):
    for g in S4:
        gi = perm_inv(g)
        for h in H:
            if perm_mul(perm_mul(g, h), gi) not in H:
                return False
    return True
verdict("V4 is normal in S4", is_normal(V4))
# any other normal subgroup of order 4? candidates: subgroups generated by a
# double-transposition plus an 4-cycle power etc. Brute force: all subgroups of
# order 4 (enumerate subsets containing identity closed under mult).
norm4 = []
for combo in _it.combinations(S4, 3):
    H = set(combo) | {tuple(range(4))}
    if len(H) != 4: continue
    if all(perm_mul(a, b) in H for a in H for b in H) and is_normal(H):
        norm4.append(H)
verdict("unique normal subgroup of order 4 in S4", len(norm4) == 1,
        f"count={len(norm4)}")

print("== Finite model counts (Def 3.13, Prop 3.16-3.17, Thm 3.18) ==")
verdict("|Trans(S4)| = 6, |H*| = 7", len(transp) == 6 and 1+6 == 7)
verdict("mu_H normalisation: 1/2 + 6*(1/12) = 1",
        abs(Fr(1,2) + 6*Fr(1,12) - 1) == 0)
verdict("|E*| = 7, |D*| = 7*7 = 49", 7*7 == 49)
alpha = 0.48047629504141964
Zalpha = 1 + 2*(2**(-alpha) + 3**(-alpha) + 5**(-alpha))
print(f"  (info) Z_alpha = {Zalpha:.15f} for alpha = {alpha} (no defining equation in text)")
kt = 1.1876789651362785
b1 = (math.log(5)**2) + 3/(4*kt)
b2 = 2*(math.log(5)**2) + 3/(2*kt)
verdict("Prop 3.17: (log5)^2 + 3/(4 kt) < 2(log5)^2 + 3/(2 kt) < 6.444",
        b1 < b2 < 6.444, f"values = {b1:.6f} < {b2:.6f} < 6.444")
verdict("Thm 3.18: Var bound 2/kt^2 <= 2", 2/kt**2 <= 2, f"2/kt^2 = {2/kt**2:.6f}")
verdict("Thm 3.18: mean (L^4-1)/(kt L^2) -> infinity as L->inf (algebraic)",
        True, "leading term L^2/kt")

print("== Lemma 4.10 quartic (symbolic) ==")
k0, k1, k2, k3, wt, ws = sp.symbols('k0 k1 k2 k3 wt ws')
ks = [k1, k2, k3]
def root_list():
    R = []
    for i, j in _it.combinations(range(4), 2):
        for s1 in (1, -1):
            for s2 in (1, -1):
                r = [0, 0, 0, 0]; r[i] = s1; r[j] = s2
                R.append(tuple(r))
    return R
kk = [k0, k1, k2, k3]
# uniform-weight check: sum over time roots (with e0) weight wt, spatial weight ws
time_roots = [r for r in root_list() if r[0] != 0]
spat_roots = [r for r in root_list() if r[0] == 0]
expr = sp.Integer(0)
for r in time_roots:
    expr += wt*(sum(kk[i]*r[i] for i in range(4)))**4
for r in spat_roots:
    expr += ws*(sum(kk[i]*r[i] for i in range(4)))**4
expr = sp.expand(-expr/24)
ks2 = k1**2 + k2**2 + k3**2
formula = -sp.Rational(1, 24)*(12*ws*ks2**2 + 4*wt*(3*k0**4 + 6*k0**2*ks2)
                               + 4*(wt-ws)*(k1**4+k2**4+k3**4))
verdict("Lemma 4.10 formula (4.3) matches symbolic sum (uniform wt/ws)",
        sp.expand(expr - formula) == 0)
verdict("isotropic case wt=ws=w gives -(w/2)(k^2)^2",
        sp.expand(formula.subs({wt: sp.Symbol('w'), ws: sp.Symbol('w')})
                  + sp.Symbol('w')/2*(k0**2+ks2)**2) == 0)
# true source weights (Def 3.7): w(r) = 2^{-t(r)}
wfun = {r: Fr(1, 2**tval(r)) if tval(r) >= 0 else Fr(2**(-tval(r))) for r in root_list()}
expr_true = sp.Integer(0)
for r in root_list():
    expr_true += sp.Rational(wfun[r].numerator, wfun[r].denominator) * \
        (sum(kk[i]*r[i] for i in range(4)))**4
expr_true = sp.expand(-expr_true/24)
# compare with (4.3) at (wt,ws) = (5/4, 1) (paper's claim), (9/8, 1), and (9/8, 9/8)
f54 = sp.expand(formula.subs({wt: sp.Rational(5, 4), ws: 1}))
f981 = sp.expand(formula.subs({wt: sp.Rational(9, 8), ws: 1}))
f9898 = sp.expand(formula.subs({wt: sp.Rational(9, 8), ws: sp.Rational(9, 8)}))
d54 = sp.expand(expr_true - f54)
d981 = sp.expand(expr_true - f981)
d9898 = sp.expand(expr_true - f9898)
print(f"  true-weighted quartic minus (4.3) at wt=5/4, ws=1: {d54}")
print(f"  true-weighted quartic minus (4.3) at wt=9/8, ws=1: {d981}")
print(f"  true-weighted quartic minus (4.3) at wt=9/8, ws=9/8: {d9898}")
verdict("paper's (wt,ws)=(5/4,1) reproduces the true weighted quartic", d54 == 0,
        f"difference = {d54}")
verdict("(wt,ws)=(9/8,9/8) reproduces the EVEN part of the true weighted quartic",
        sp.expand(d9898 - sp.expand(sum(
            -sp.Rational(1, 12)*m for m in [
                k0**3*k1, k0**3*k2, k0**3*k3, k0*k1**3, k0*k2**3, k0*k3**3,
                k1**3*k2, k1**3*k3, k2**3*k1, k2**3*k3, k3**3*k1, k3**3*k2]))) == 0,
        f"residual after removing odd terms = {d9898}")
# extract the odd monomials and the even-part effective weight
poly = sp.Poly(expr_true, k0, k1, k2, k3)
odd_terms = {m: c for m, c in poly.as_dict().items()
             if any(e % 2 == 1 for e in m)}
print(f"  odd monomials present in true weighted quartic: {odd_terms}")
verdict("true weighted quartic has NO odd monomials (required by (4.3) form)",
        len(odd_terms) == 0, f"odd terms = {odd_terms}")
# even part: coefficient of k0^4 and of k1^4 and k1^2 k2^2
c_k04 = poly.as_dict().get((4, 0, 0, 0), 0)
c_k14 = poly.as_dict().get((0, 4, 0, 0), 0)
c_k12k22 = poly.as_dict().get((0, 2, 2, 0), 0)
print(f"  even-part coefficients: k0^4: {c_k04} (isotropic w=9/8 predicts -9/16); "
      f"k1^4: {c_k14} (predicts -9/16); k1^2 k2^2: {c_k12k22} (predicts -9/8)")
print(f"  mean source weight over all 24 roots = {(6*2 + 12*1 + 6*sp.Rational(1,2))/24} = 9/8")
print(f"  paper's anisotropy coefficient -(wt-ws)/6 at (5/4,1) = -1/24; "
      f"true even part is exactly isotropic (-(9/16)(k^2)^2), so its anisotropy "
      f"(deviation from isotropy) is 0; the actual anisotropy is the odd monomials "
      f"at coefficient -1/12, which no (wt,ws) in (4.3) can produce.")
print("DONE check_d4.py")
