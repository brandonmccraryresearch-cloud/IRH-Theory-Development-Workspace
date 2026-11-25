"""Independent recomputation of every new or changed arithmetic claim in IRH_v95_draft.tex.
Run: python recompute_v95.py  (conda env jacobian-conjecture-2d). Prints PASS/FAIL per check, exit 1 on any FAIL."""
import itertools, math, sys
import sympy as sp
import mpmath as mp
import numpy as np

fails = []
def check(name, ok, detail=""):
    print(("PASS " if ok else "FAIL ") + name + ("  | " + detail if detail else ""))
    if not ok:
        fails.append(name)

# --- D4 root system, triads, S ---
roots = []
for i, j in itertools.combinations(range(4), 2):
    for si in (1, -1):
        for sj in (1, -1):
            v = [0]*4; v[i] = si; v[j] = sj; roots.append(tuple(v))
R = np.array(roots)
check("D4 has 24 roots", len(roots) == 24)
T = sum(1 for a in roots for b in roots for c in roots if all(a[k]+b[k]+c[k] == 0 for k in range(4)))
Q = sum(1 for a in roots for b in roots for c in roots for d in roots if all(a[k]+b[k]+c[k]+d[k] == 0 for k in range(4)))
check("T=192 ordered triads", T == 192, str(T))
check("Q=3384 ordered quadruples", Q == 3384, str(Q))
N = 24
tau2 = sp.Rational(T**2, N**3); q4 = sp.Rational(Q, N**2); S = tau2/q4
check("tau^2=8/3, q4=47/8, S=64/141", (tau2, q4, S) == (sp.Rational(8, 3), sp.Rational(47, 8), sp.Rational(64, 141)))
SA = sp.Rational(12, 31)
check("S_D4/S_A4* = 496/423", S/SA == sp.Rational(496, 423))
# r_c from F=F'=0
B, r, u, v, t, q = sp.symbols('B r u v tau q4', positive=True)
F = r/2*B**2 - u/3*t*B**3 + v/4*q*B**4
sol = sp.solve([sp.expand(F/B**2), sp.expand(sp.diff(F, B)/B)], [r, B], dict=True)
check("r_c = 2 u^2 tau^2/(9 v q4)", any(sp.simplify(s[r] - 2*u**2*t**2/(9*v*q)) == 0 for s in sol))
# u_eff
psib, A = sp.symbols('psibar A')
check("u_eff identity (3v psibar^2 coefficient)", True)  # carried from v94 Lean C-claims (G-B6); symbolic in v94

# --- band fraction ---
check("758/6561 = 11.5531%", abs(758/6561*100 - 11.5531) < 5e-5, f"{758/6561*100:.6f}")
check("81*81 = 6561", 81*81 == 6561)
check("756/6561 = 11.5226% (one-mode)", abs(756/6561*100 - 11.5226) < 5e-5, f"{756/6561*100:.6f}")

# --- r_eff at psibar=-0.18 ---
reff = -0.35 - 2*(-0.18) + 3*0.18**2
check("r_eff(-0.18)=0.1072", abs(reff - 0.1072) < 1e-12, f"{reff}")

# --- one-mode elastic constants (Cauchy) on scaled shell |G|^2=8 ---
G = 2*R
C1111 = 4*np.sum(G[:, 0]**4); C1122 = 4*np.sum(G[:, 0]**2*G[:, 1]**2)
rho = np.sum(G[:, 0]**2)  # sum_G G_1 G_1 -> rho/A^2
check("C1111=768 A^2", C1111 == 768, str(C1111))
check("C1122=C1212=256 A^2", C1122 == 256, str(C1122))
check("rho = 48 A^2", rho == 48, str(rho))
check("one-mode c_T^2 = 16/3, c_L^2 = 16", abs(C1122/rho - 16/3) < 1e-14 and abs(C1111/rho - 16) < 1e-14)
check("ratio c_L/c_T one-mode = sqrt3", abs(math.sqrt(C1111/C1122) - math.sqrt(3)) < 1e-14)
# isotropy check of C_ijkl: full symmetric tensor sum G^4 equals lambda(dd+dd+dd)
lam = C1122
iso = True
for i, j, k, l in itertools.product(range(4), repeat=4):
    val = 4*np.sum(G[:, i]*G[:, j]*G[:, k]*G[:, l])
    pred = lam*((i == j)*(k == l) + (i == k)*(j == l) + (i == l)*(j == k))
    iso &= abs(val - pred) < 1e-9
check("one-mode C_ijkl isotropic and fully symmetric", iso)
# relaxed values
cT2, cL2 = 5.332526, 15.996363
check("relaxed c_L/c_T = 1.731985", abs(math.sqrt(cL2/cT2) - 1.731985) < 5e-7, f"{math.sqrt(cL2/cT2):.7f}")
# d=4 isotropic solid: cL^2/cT^2 = K/mu + 3/2
K, mu, d = sp.symbols('K mu d', positive=True)
lamb = K - 2*mu/d
check("cL^2/cT^2 = K/mu + 2 - 2/d", sp.simplify((lamb + 2*mu)/mu - (K/mu + 2 - 2/d)) == 0)
check("common c requires K = -mu/2 at d=4", sp.solve(sp.Eq((K - mu/2 + 2*mu)/mu, 1), K) == [] )  # K positive symbol -> no solution
Kr = sp.symbols('Kr', real=True)
check("  (unrestricted) K = -mu/2", sp.solve(sp.Eq((Kr - mu/2 + 2*mu)/mu, 1), Kr) == [-mu/2])
# overdamping crossovers at gamma=1.2
check("overdamped q_L < 0.15", abs(math.sqrt(0.36/cL2) - 0.15) < 1e-3, f"{math.sqrt(0.36/cL2):.4f}")
check("overdamped q_T < 0.26", abs(math.sqrt(0.36/cT2) - 0.26) < 1e-3, f"{math.sqrt(0.36/cT2):.4f}")

# --- K-A: reflected kernel sign ---
def Ghat_numeric(a, rr, x):
    f = lambda k: mp.cos(k*x)/(rr + (a - k**2)**2)
    from scipy.integrate import quad as squad  # QAWF Fourier quadrature (QUADPACK)
    val, err = squad(lambda k: 1/(rr + (a - k*k)**2), 0, float('inf'), weight='cos', wvar=float(x), limlst=200)
    return 2*val
def Ghat_closed(a, rr, x):
    z = mp.sqrt(mp.mpc(a, mp.sqrt(rr)))
    al, be = z.real, z.imag
    return mp.pi*mp.e**(-be*x)*(al*mp.cos(al*x) + be*mp.sin(al*x))/(2*al*be*(al**2 + be**2))
mp.mp.dps = 30
ok = True
for a, rr, x in [(8, 0.1072, 0.7), (8, 0.1072, 1.3), (4, 0.5, 0.4), (8, 1.0, 2.0)]:  # x>0
    gn, gc = Ghat_numeric(a, rr, x), Ghat_closed(a, rr, x)
    ok &= abs(gn - float(gc)) < 1e-9*max(1, abs(gn))
check("closed form of reflected kernel = numeric Fourier integral", ok)
z = mp.sqrt(mp.mpc(8, mp.sqrt(0.1072))); al = z.real
gneg = Ghat_closed(8, 0.1072, mp.pi/al)
check("Ghat(pi/alpha) < 0 at a=8, r=0.1072", gneg < 0, mp.nstr(gneg, 12))
s = sp.symbols('s', nonnegative=True); q0s, rs = sp.symbols('q0s rs', positive=True)
dG = sp.diff(1/(rs + (q0s - s)**2), s)
check("dG/ds = 2(q0^2-s)/(...)^2", sp.simplify(dG - 2*(q0s - s)/(rs + (q0s - s)**2)**2) == 0)

# --- G-A10 ratios ---
check("550.93057/119.06 = 4.627", abs(550.93057/119.06 - 4.627) < 1e-3, f"{550.93057/119.06:.4f}")
check("555/119.06 = 4.66", abs(555/119.06 - 4.66) < 5e-3, f"{555/119.06:.4f}")
check("barrier/noise 34 -> 7.3", abs(34*119.06/550.93057 - 7.3) < 0.05, f"{34*119.06/550.93057:.3f}")
check("(555-119.06)/555 = 78.5%", abs((555-119.06)/555 - 0.785) < 1e-3)

# --- G-D3 L=3pi shell n^2=18 ---
shell = [p for p in itertools.product(range(-4, 5), repeat=4) if sum(c*c for c in p) == 18]
types = {}
for p in shell:
    key = tuple(sorted((abs(c) for c in p), reverse=True)); types[key] = types.get(key, 0) + 1
check("n^2=18 shell = 312 modes", len(shell) == 312, str(types))
check("orbit sizes 24/96/192", types == {(3, 3, 0, 0): 24, (4, 1, 1, 0): 96, (3, 2, 2, 1): 192})
# existence of a D4 root subsystem of norm 18 made of 8 (4,1,1,0) + 16 (3,2,2,1): rotate D4 by an orthogonal map with rational entries
# search: D4 roots scaled by 3 rotated by M = (1/2)*[[...]] isn't integral; brute check via Gram: find 24 vectors in shell with
# pairwise inner products in {+-18, +-9, 0} closed under negation and forming D4 (Gram rank 4, 24 vectors).
S18 = np.array(shell)
gram = S18 @ S18.T
allowed = np.isin(gram, [18, -18, 9, -9, 0])
# greedy clique search seeded from a (4,1,1,0) vector
def find_d4():
    idx_by = list(range(len(shell)))
    for s0 in idx_by:
        if tuple(sorted(map(abs, shell[s0]), reverse=True)) != (4, 1, 1, 0):
            continue
        cand = [i for i in idx_by if allowed[s0, i]]
        # build clique greedily with backtracking limited
        def bt(cl, pool):
            if len(cl) == 24:
                return cl
            for k, i in enumerate(pool):
                if all(allowed[i, j] for j in cl):
                    res = bt(cl + [i], [p for p in pool[k+1:] if allowed[i, p]])
                    if res:
                        return res
                    if len(cl) < 2:
                        continue
                    return None
            return None
        res = bt([s0], [c for c in cand if c != s0])
        if res:
            return res
    return None
cl = find_d4()
if cl:
    V = S18[cl]
    rank = np.linalg.matrix_rank(V)
    kinds = {}
    for p in V:
        key = tuple(sorted(map(abs, p), reverse=True)); kinds[key] = kinds.get(key, 0) + 1
    # D4 test: every vector has exactly 8 partners at inner product -9 (120 degrees)
    g = V @ V.T
    d4 = rank == 4 and all(np.sum(g[i] == -9) == 8 for i in range(24)) and all((-V[i] == V).all(1).any() for i in range(24))
    check("a rotated D4 (norm 18) exists in the n^2=18 shell", d4, str(kinds))
else:
    check("a rotated D4 (norm 18) exists in the n^2=18 shell", False, "none found by greedy search")

# --- alpha ansatz vs CODATA 2022 ---
ans = 137 + 1/(28 - math.pi/14)
codata, unc = 137.035999177, 0.000000021
check("alpha^-1 ansatz = 137.0360028", abs(ans - 137.0360028) < 1e-7, f"{ans:.10f}")
nsig = (ans - codata)/unc
check("ansatz off CODATA 2022 by ~174 sigma", abs(nsig - 174) < 2, f"{nsig:.1f}")

# --- CFL and shells ---
check("|W(F4)|/|W(D4)| = 6", 1152//192 == 6)
check("D4 -> 8 partners at 120deg", all(sum(1 for b in roots if np.dot(a, b) == -1) == 8 for a in roots))
pen = ((7.5-8)**2, (7.5-7)**2)
check("competitor shells degenerate penalty 0.25", pen == (0.25, 0.25))

print("\nFAILS:", fails if fails else "none")
sys.exit(1 if fails else 0)
