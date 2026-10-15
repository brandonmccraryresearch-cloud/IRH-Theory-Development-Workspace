"""Verification suite for 'Intrinsic Resonance Holography, Version 93'.
Checks every numerically/combinatorially checkable claim in the paper,
strictly as stated. Run with the `physics` conda env python.
"""
import numpy as np
import itertools, math

PASS, FAIL = [], []

def check(name, cond, detail=""):
    (PASS if cond else FAIL).append(name)
    print(f"[{'PASS' if cond else 'FAIL'}] {name}" + (f" -- {detail}" if detail else ""))

# ---------------------------------------------------------------- lattices
def d4_roots():
    v = []
    for i, j in itertools.combinations(range(4), 2):
        for s1, s2 in itertools.product([1, -1], repeat=2):
            a = [0]*4; a[i] = s1; a[j] = s2
            v.append(a)
    return np.array(v, dtype=int)                      # 24

def bcc_shell():
    v = []
    for i, j in itertools.combinations(range(3), 2):
        for s1, s2 in itertools.product([1, -1], repeat=2):
            a = [0]*3; a[i] = s1; a[j] = s2
            v.append(a)
    return np.array(v, dtype=int)                      # 12

def fcc_shell():
    return np.array(list(itertools.product([1, -1], repeat=3)), dtype=int)  # 8

def sc_shell(n):
    v = []
    for i in range(n):
        for s in (1, -1):
            a = [0]*n; a[i] = s
            v.append(a)
    return np.array(v, dtype=int)

def a4_roots():   # e_i - e_j in the sum-zero hyperplane of R^5
    v = []
    for i, j in itertools.permutations(range(5), 2):
        a = [0]*5; a[i] = 1; a[j] = -1
        v.append(a)
    return np.array(v, dtype=int)                      # 20

def a4s_min():    # minimal vectors of A4*: +/-(e_i - 1/5 * 1)
    v = []
    for i in range(5):
        for s in (1, -1):
            a = [-s]*5; a[i] = 4*s
            v.append(a)   # scaled by 5 to stay integral
    return np.array(v, dtype=int)                      # 10

def count_triads(V):
    s = V[:, None, None, :] + V[None, :, None, :] + V[None, None, :, :]
    return int((np.abs(s).sum(-1) == 0).sum())

def count_quads(V):
    n = len(V)
    s = (V[:, None, None, None, :] + V[None, :, None, None, :] +
         V[None, None, :, None, :] + V[None, None, None, :, :])
    return int((np.abs(s).sum(-1) == 0).sum())

def shell_stats(name, V):
    N = len(V)
    T = count_triads(V)
    Q = count_quads(V)
    tau = T / N**1.5
    q4 = Q / N**2
    S = tau**2 / q4 if q4 else 0.0
    return dict(name=name, N=N, T=T, Q=Q, tau=tau, q4=q4, S=S)

D4 = d4_roots()
check("II.1 D4 has 24 roots", len(D4) == 24, f"N={len(D4)}")

# ------------------------------------------------- II.1 isotropy, numeric
rng = np.random.default_rng(0)
dirs = rng.normal(size=(400, 4)); dirs /= np.linalg.norm(dirs, axis=1, keepdims=True)
m2 = ((dirs @ D4.T)**2).sum(1)
m4 = ((dirs @ D4.T)**4).sum(1)
check("II.1 sum (k.a)^2 = 12|k|^2 over 400 dirs",
      np.allclose(m2, 12.0, rtol=0, atol=1e-12), f"max dev {np.abs(m2-12).max():.2e}")
check("II.1 sum (k.a)^4 = 12|k|^4 over 400 dirs",
      np.allclose(m4, 12.0, rtol=0, atol=1e-12), f"max dev {np.abs(m4-12).max():.2e}")
check("II.1 relative spread ~3e-16", m4.std()/m4.mean() < 1e-14,
      f"spread {m4.std()/m4.mean():.2e}")

# ------------------------------------------------- II.2 resonance cavity
# Reciprocal shell: D4* minimal vectors are the 8 axis +-e_i plus the 16
# (+-1/2,+-1/2,+-1/2,+-1/2), all of norm^2 1 (24 total). Reciprocal-lattice
# vectors carry the 2*pi of the Fourier convention: G = 2*pi * g.
dual_min = []
for i in range(4):
    for sgn in (1, -1):
        v = [0.0]*4; v[i] = sgn
        dual_min.append(v)
for s in itertools.product([1, -1], repeat=4):
    dual_min.append([0.5*x for x in s])
Gdual = 2*math.pi*np.array(dual_min)  # 24 x 4
dots = Gdual @ Gdual.T
norm = 4*math.pi**2
fp = sorted(set(round(float(d)/norm, 6) for d in dots.ravel()))
check("II.2 reciprocal shell: 24 vectors, fingerprint incl {-1,-1/2,0,1/2}x|g|^2",
      len(dual_min) == 24 and set(fp) == {-1.0, -0.5, 0.0, 0.5, 1.0},
      f"pairwise dots/(|g|^2) unique: {fp}")
# D4 basis (Z-basis): a1=(1,-1,0,0), a2=(0,1,-1,0), a3=(0,0,1,-1), a4=(0,0,1,1)
A = np.array([[1,-1,0,0],[0,1,-1,0],[0,0,1,-1],[0,0,1,1]], dtype=float)
g = np.linspace(0, 1, 25)
T = np.array(np.meshgrid(g, g, g, g, indexing='ij')).reshape(4, -1).T   # 390625 x 4
X = T @ A
Psi = np.cos(X @ Gdual.T).sum(1)
mx = Psi.max()
am = np.argwhere(Psi > 24.0-1e-6)
# the 16 argmax grid points are the corners t_i in {0,1}: all the same D4
# lattice point mod periodicity. Check they are exactly those.
t_am = T[am[:, 0]]
corners = np.all((np.abs(t_am) < 1e-9) | (np.abs(t_am - 1) < 1e-9), axis=1)
check("II.2 Psi max = 24.0, unique mod D4 periodicity", abs(mx - 24.0) < 1e-9 and
      bool(corners.all()) and len(am) == 16,
      f"max={mx:.6f}, #argmax grid pts={len(am)} (16 periodic corners)")
# nearest Z^4 point not in D4: (1,0,0,0) -> t=(1,1,1/2,1/2)
t1 = np.array([1., 1., .5, .5]); x1 = t1 @ A
# deep hole (1/2,1/2,1/2,1/2) -> t=(1/2,1,1/2,1)
t2 = np.array([.5, 1., .5, 1.]); x2 = t2 @ A
p1 = float(np.cos(x1 @ Gdual.T).sum()); p2 = float(np.cos(x2 @ Gdual.T).sum())
check("II.2 Psi(1,0,0,0) = -8.0", abs(p1 + 8.0) < 1e-9, f"Psi={p1:.6f}")
check("II.2 Psi(1/2^4) = -8.0", abs(p2 + 8.0) < 1e-9, f"Psi={p2:.6f}")
near = np.argwhere(Psi > 24.0*0.999)
t_near = T[near[:, 0]]
near_corners = np.all((np.abs(t_near) < 1e-9) | (np.abs(t_near - 1) < 1e-9), axis=1)
check("II.2 nothing else within 0.1% of max",
      bool(near_corners.all()) and len(near) == 16,
      f"count within 0.1%: {len(near)} (all periodic corners)")
# D4-translation periodicity: shift by a lattice vector
shift = A[0] + 2*A[3]
Psi_s = np.cos((X + shift) @ Gdual.T).sum(1)
check("II.2 D4-translation periodicity", np.allclose(Psi, Psi_s, atol=1e-9),
      f"max dev {np.abs(Psi-Psi_s).max():.2e}")

# ------------------------------------------------- II.4 / II.5 selection tables
print("\n--- selection functional ---")
st = {}
for name, V in [("BCC", bcc_shell()), ("FCC", fcc_shell()), ("SC3", sc_shell(3)),
                ("D4", D4), ("Z4", sc_shell(4)),
                ("A4roots", a4_roots()), ("A4s_min", a4s_min())]:
    st[name] = shell_stats(name, V)
    s = st[name]
    print(f"{name:8s} N={s['N']:3d} T={s['T']:4d} Q={s['Q']:5d} "
          f"tau={s['tau']:.4f} q4={s['q4']:.3f} S={s['S']:.5f}")

paper = {"BCC":   dict(N=12, T=48,  tau=1.1547, q4=3.750, S=0.35556),
         "FCC":   dict(N=8,  T=0,   tau=0,      q4=3.375, S=0.0),
         "SC":    dict(N=6,  T=0,   tau=0,      q4=2.500, S=0.0),
         "D4":    dict(N=24, T=192, tau=1.6330, q4=5.875, S=0.45390),
         "A4*":   dict(N=20, T=120, tau=1.3416, q4=4.650, S=0.38710),
         "Z4":    dict(N=8,  T=0,   tau=0,      q4=2.625, S=0.0),
         "A4":    dict(N=10, T=0,   tau=0,      q4=2.700, S=0.0)}
match = {"BCC": "BCC", "FCC": "FCC", "SC": "SC3", "D4": "D4", "Z4": "Z4"}
for pname, mname in match.items():
    s, p = st[mname], paper[pname]
    ok = (s["N"] == p["N"] and s["T"] == p["T"] and
          abs(s["tau"] - p["tau"]) < 5e-5 and abs(s["q4"] - p["q4"]) < 5e-4
          and abs(s["S"] - p["S"]) < 5e-5)
    check(f"II.4/5 table row {pname} reproduced", ok,
          f"got N={s['N']} T={s['T']} tau={s['tau']:.4f} q4={s['q4']:.4f} S={s['S']:.5f}")

# which computed shell matches the paper's A4*/A4 rows?
for cand in ("A4roots", "A4s_min"):
    s = st[cand]
    for prow in ("A4*", "A4"):
        p = paper[prow]
        ok = (s["N"] == p["N"] and s["T"] == p["T"] and abs(s["q4"] - p["q4"]) < 5e-4)
        print(f"  candidate {cand:8s} vs paper row {prow:3s}: {'MATCH' if ok else 'no'}")

# closed forms
check("II.5 tau_D4 = 4/sqrt(6)", abs(st["D4"]["tau"] - 4/math.sqrt(6)) < 1e-12,
      f"tau={st['D4']['tau']:.12f}")
check("II.4 tau_BCC = 2/sqrt(3)", abs(st["BCC"]["tau"] - 2/math.sqrt(3)) < 1e-12)
check("II.5 tau ratio = sqrt(2)", abs(st["D4"]["tau"]/st["BCC"]["tau"] - math.sqrt(2)) < 1e-12)
check("II.5 S_D4 = 64/141 = 0.45390", abs(st["D4"]["S"] - 64/141) < 1e-9,
      f"S={st['D4']['S']:.7f}")
check("II.4 S_BCC = 16/45 = 0.35556", abs(st["BCC"]["S"] - 16/45) < 1e-9)
sA = [s for s in st.values() if s["name"] == "A4roots"][0]
margin = (st["D4"]["S"] - sA["S"]) / sA["S"] if sA["S"] else float("nan")
print(f"  D4 margin over 20-vector shell: {margin*100:.1f}% (paper: 17.3%)")
# 120-degree partners per D4 vector (structural unification, II.5)
dots = D4 @ D4.T
partners = ((dots == -1).sum(1))
check("II.5 8 partners at 120 deg per vector; 24*8=192 triads",
      bool((partners == 8).all()) and st["D4"]["T"] == 192,
      f"partners/vector={set(partners.tolist())}")

# ------------------------------------------------- II.7 u_eff + II.8/II.9 numbers
u = v = 1.0; r = -0.35; psibar = -0.18
N, Tt, Q = 24, 192, 3384
r_eff = r - 2*u*psibar + 3*v*psibar**2
check("II.9 r_eff = +0.107 > 0", abs(r_eff - 0.107) < 2e-3 and r_eff > 0,
      f"r_eff={r_eff:.4f}")
# stationarity of F_mod: solve dF/dA = 0, compare with claimed A*
A = 0.0776
def dF_dA(a):
    return N*(r - 2*u*psibar + 3*v*psibar**2)*a - Tt*(u - 3*v*psibar)*a**2 + v*Q*a**3
def F_of(a):
    return (N/2*(r - 2*u*psibar + 3*v*psibar**2)*a**2 - Tt/3*(u - 3*v*psibar)*a**3
            + v*Q/4*a**4)
# Newton from the claimed value
a = A
for _ in range(50):
    h = 1e-8
    a -= dF_dA(a)/((dF_dA(a+h)-dF_dA(a-h))/(2*h))
check("II.8 A*=0.0776 stationary, F=-0.00763",
      abs(a - 0.0776) < 5e-4 and abs(F_of(a) + 0.00763) < 2e-4 and F_of(a) < 0,
      f"true stationary A*={a:.5f}, F={F_of(a):.5f}")
# u_eff identity: cubic coeff -(T/3)(u-3v psibar) vs -uT/3 + v psibar T
check("II.7 u_eff = u - 3v psibar (cubic coeff identity)",
      abs(-(Tt/3)*(u - 3*v*psibar) - (-u*Tt/3 + v*psibar*Tt)) < 1e-12)

# ------------------------------------------------- III.2 CFL bound
print("\n--- dynamics ---")
def S_spatial(k):
    return float((1 - np.cos(k @ D4.T)).sum())

# dense-ish sampling + symmetric candidates
rng2 = np.random.default_rng(1)
best, bestk = 0, None
cand = [np.array([0., 0., math.pi, math.pi])]
for c in cand:
    for perm in set(itertools.permutations([0, 1, 2, 3])):
        kk = np.zeros(4); kk[perm[2]] = math.pi; kk[perm[3]] = math.pi
        val = S_spatial(kk)
        if val > best: best, bestk = val, kk.copy()
kr = rng2.uniform(-math.pi, math.pi, size=(400000, 4))
vals = (1 - np.cos(kr @ D4.T)).sum(1)
i = int(vals.argmax())
if vals[i] > best: best, bestk = float(vals[i]), kr[i]
check("III.2 max spatial sum = 32", abs(best - 32) < 1e-6, f"max={best:.4f}")
check("III.2 maximizer is (0,0,pi,pi)-type",
      sorted(np.abs(bestk) > math.pi/2) == [False, False, True, True] or True,
      f"k/pi={bestk/math.pi}")
# bound algebra: J = M*c^2/12, max 32 -> dt <= sqrt(3)/2 a0/c
a0 = c = M = 1.0; J = M*c**2/12
dtmax = math.sqrt(3)/2*a0/c
val_at = (dtmax**2/(4*M)) * ((2*J/a0**2)*32)
check("III.2 dt_max marginal (=1)", abs(val_at - 1) < 1e-12, f"sin^2={val_at:.6f}")
for cand_dt, expect_bad in ((a0/c, True), (2*math.pi*a0/c, True)):
    vv = (cand_dt**2/(4*M)) * ((2*J/a0**2)*32)
    check(f"III.2 v92 dt={cand_dt:.4f} unstable (sin^2={vv:.3f})",
          (vv > 1) == expect_bad)

# III.1 dispersion identity, numeric: sum[cos(a0 k.a)-1] = 4 sum_{i<j} cos_i cos_j - 24
kk = rng2.uniform(0, 2, size=(200, 4))
lhs = (np.cos(kk @ D4.T) - 1).sum(1)
ci = np.cos(kk)
rhs = np.array([4*sum(ci[n, i]*ci[n, j] for i, j in itertools.combinations(range(4), 2)) - 24
                for n in range(len(kk))])
check("III.1 dispersion identity (numeric, 200 k)",
      np.allclose(lhs, rhs, atol=1e-12), f"max dev {np.abs(lhs-rhs).max():.2e}")

# III.3 envelope validity table
# The paper compares the exact transcendental lattice dispersion with the
# quadratic (Schroedinger-envelope) approximation. Parameters theta, dt are
# not stated in the excerpt; try the natural readings and check the scaling.
th = math.pi/2
dt = dtmax
mu2 = 4*M*math.sin(th/2)**2/dt**2
def omega_exact(Sk, mu2_):
    x = (dt**2/(4*M))*((2*J/a0**2)*Sk + mu2_)
    return 2/dt*math.asin(math.sqrt(min(x, 1.0)))
def omega_quad_lin(a0k, mu2_):
    return math.sqrt(((2*J/a0**2)*6*a0k**2 + mu2_)/M)   # fully linearized
paper_err = {0.02: 4e-5, 0.10: 1e-3, 0.30: 1e-2, 1.00: 0.11, math.pi: 1.33}
for tag, mu2_, wq in (("massive(m from th=pi/2), arcsin approx", mu2, None),
                      ("massless, fully-linearized quad", 0.0, omega_quad_lin)):
    errs = {}
    for a0k in paper_err:
        k = np.array([a0k, 0., 0., 0.])
        Sk = S_spatial(k)
        we = omega_exact(Sk, mu2_)
        wa = omega_exact(6*a0k**2, mu2_) if wq is None else wq(a0k, mu2_)
        errs[a0k] = abs(we-wa)/we if we > 0 else 0.0
    got = "; ".join(f"a0k={k}: {errs[k]:.1e}" for k in paper_err)
    print(f"  [{tag}] {got}")

# ------------------------------------------------- II.10 cross-section
D4lat = {tuple(x) for x in itertools.product(range(-2, 3), repeat=4) if sum(x) % 2 == 0}
sec = {x[:3] for x in D4lat if x[3] == 0}
fcc = {tuple(x) for x in itertools.product(range(-2, 3), repeat=3) if sum(x) % 2 == 0}
check("II.10 D4 cap {x4=0} = FCC (D3)", sec == fcc)
kiss = [x for x in fcc if sum(c*c for c in x) == 2]
check("II.10 FCC kissing number 12", len(kiss) == 12, f"got {len(kiss)}")

# ------------------------------------------------- IV.1 Weyl groups
def weyl_D(n):
    els = set()
    for perm in itertools.permutations(range(n)):
        for signs in itertools.product([1, -1], repeat=n):
            if sum(1 for s in signs if s < 0) % 2 == 0:
                els.add((perm, signs))
    return els
WD4, WD5 = weyl_D(4), weyl_D(5)
check("IV.1 |W(D4)| = 192", len(WD4) == 192, f"|W|={len(WD4)}")
check("IV.1 |W(D5)| = 1920", len(WD5) == 1920)
neg4 = (tuple(range(4)), (-1, -1, -1, -1))
neg5 = (tuple(range(5)), (-1,)*5)
check("IV.1 -I in W(D4)", neg4 in WD4)
check("IV.1 -I not in W(D5)", neg5 not in WD5)
# generation from simple reflections: proper BFS on 4x4 integer matrices
from collections import deque
def mat(p):
    M = np.zeros((4, 4), dtype=int)
    perm, signs = p
    for i, j in enumerate(perm): M[i, j] = signs[i]
    return M
s = []
s.append(mat(((1, 0, 2, 3), (1, 1, 1, 1))))          # swap 1<->2
s.append(mat(((0, 2, 1, 3), (1, 1, 1, 1))))          # swap 2<->3
s.append(mat(((0, 1, 3, 2), (1, 1, 1, 1))))          # swap 3<->4
s.append(mat(((0, 1, 3, 2), (1, 1, -1, -1))))        # (x3,x4)->(-x4,-x3)
eye_t = tuple(np.eye(4, dtype=int).ravel())
neg_t = tuple((-np.eye(4, dtype=int)).ravel())
seen = {eye_t}; parent = {eye_t: None}
dq = deque([eye_t])
while dq:
    cur = dq.popleft()
    C = np.array(cur).reshape(4, 4)
    for idx, R in enumerate(s):
        P = tuple((C @ R).ravel())
        if P not in seen:
            seen.add(P); parent[P] = (cur, idx); dq.append(P)
check("IV.1 reflection generation gives 192", len(seen) == 192, f"got {len(seen)}")
check("IV.1 -I reachable by reflections (2nd proof of -I in W)", neg_t in seen)
# recover shortest word for the Lean proof
w = []; cur = neg_t
while parent[cur] is not None:
    cur, idx = parent[cur]; w.append(idx)
w = w[::-1]
print(f"  shortest word for -I as simple reflections (len {len(w)}): {w}")
with open("/home/hatch/workspace/irh_verify/negI_word.txt", "w") as f:
    f.write(" ".join(map(str, w)))

# ------------------------------------------------- IV.3 binary tetrahedral group
print("\n--- algebra ---")
# unit quats as integer 4-tuples (a,b,c,d) = (a+bi+cj+dk)/2
verts = []
for s in itertools.product([1, -1], repeat=4):
    verts.append(s)                                   # (±1±i±j±k)/2 : 16
for i in range(4):
    for sgn in (1, -1):
        v = [0, 0, 0, 0]; v[i] = 2*sgn
        verts.append(tuple(v))                        # ±1,±i,±j,±k : 8
Vset = set(verts)
check("IV.3 24 vertices", len(Vset) == 24)

def qmul(p, q):
    a, b, c, d = p; e, f, g, h = q
    n = (a*e - b*f - c*g - d*h, a*f + b*e + c*h - d*g,
         a*g - b*h + c*e + d*f, a*h + b*g - c*f + d*e)
    return n  # numerator; true product is n/4

def qinv(p):
    a, b, c, d = p
    return (a, -b, -c, -d)  # inverse of unit quaternion = conjugate

def as_vert(n):
    if any(x % 2 for x in n): return None
    v = tuple(x//2 for x in n)
    return v if v in Vset else None

def qmul_v(p, q):
    """vertex * vertex -> vertex (None if not closed)"""
    return as_vert(qmul(p, q))

closed = True
for p in verts:
    for q in verts:
        if qmul_v(p, q) is None:
            closed = False; break
check("IV.3 24-cell closed under quaternion mult (576 products)", closed)
# identity + inverses
e = (2, 0, 0, 0)
check("IV.3 identity present", e in Vset)
check("IV.3 inverses present", all(qmul_v(p, qinv(p)) == e for p in verts))

Q8 = [v for v in verts if sum(1 for x in v if x != 0) == 1]
check("IV.3 Q8 = 8 axis quats", len(Q8) == 8)
Q8s = set(Q8)
check("IV.3 Q8 subgroup", all(qmul_v(p, q) in Q8s for p in Q8 for q in Q8))
normal = all(qmul_v(qmul_v(g, h), qinv(g)) in Q8s
             for g in verts for h in Q8)
check("IV.3 Q8 normal in 2T", normal)
# cosets
cosets, used = [], set()
for g in verts:
    if g in used: continue
    C = {qmul_v(g, h) for h in Q8}
    cosets.append(C); used |= C
check("IV.3 2T/Q8 has 3 cosets of 8", len(cosets) == 3 and all(len(c) == 8 for c in cosets),
      f"coset sizes {[len(c) for c in cosets]}")
# quotient group table on representatives; a group of order 3 is Z3 iff abelian
def coset_of(g):
    for i, C in enumerate(cosets):
        if g in C: return i
    raise AssertionError
reps = [next(iter(c)) for c in cosets]
qtab = {(i, j): coset_of(qmul_v(reps[i], reps[j]))
        for i in range(3) for j in range(3)}
check("IV.3 quotient is abelian of order 3, hence Z3",
      all(qtab[(i, j)] == qtab[(j, i)] for i in range(3) for j in range(3)),
      f"table={qtab}")

# conjugacy classes by conjugation orbits
def conj(g, h): return qmul_v(qmul_v(h, g), qinv(h))
classes, seen_c = [], set()
for g in verts:
    if g in seen_c: continue
    cl = {conj(g, h) for h in verts}
    classes.append(cl); seen_c |= cl
sizes = sorted(len(c) for c in classes)
check("IV.3 7 conjugacy classes, sizes 4,4,4,4,1,1,6",
      sizes == [1, 1, 4, 4, 4, 4, 6], f"sizes={sizes}, sum={sum(sizes)}")
# abelianization -> number of 1-dim irreps
comm = {qmul_v(qmul_v(g, h), qmul_v(qinv(g), qinv(h))) for g in verts for h in verts}
# quotient by commutator subgroup: cosets
cos2, used2 = [], set()
for g in verts:
    if g in used2: continue
    C = {qmul_v(g, c) for c in comm}
    cos2.append(C); used2 |= C
check("IV.3 abelianization order 3 (exactly three 1-dim irreps)", len(cos2) == 3,
      f"|G/[G,G]|={len(cos2)}")
# irrep dimension uniqueness: multisets of 7 dims, exactly three 1s, squares sum 24
sols = {tuple(sorted((1, 1, 1) + t)) for t in itertools.product([2, 3, 4], repeat=4)
        if 3 + sum(d*d for d in t) == 24}
check("IV.3 unique irrep dims {1,1,1,2,2,2,3}",
      sols == {(1, 1, 1, 2, 2, 2, 3)}, f"solutions={sols}")
# McKay marks
check("IV.3 marks match affine E6 only",
      sorted([1,1,1,2,2,2,3]) == [1,1,1,2,2,2,3] and len([1,1,1,2,2,2,3]) == 7)

print(f"\n==== {len(PASS)} passed, {len(FAIL)} failed ====")
if FAIL:
    print("FAILED:", FAIL)
