# v-gb6 independent enumeration (verifier's own code; does not import or copy author code).
# Method: shells built two ways (norm filter over a box AND explicit sign/perm construction);
# counts by Counter-convolution of k-fold sum distributions (not nested loops).
import itertools, sys, math
from collections import Counter
from fractions import Fraction as F
import numpy as np

def boxshell(d, r, m, extra=None):
    out = [v for v in itertools.product(range(-r, r+1), repeat=d) if sum(x*x for x in v) == m]
    return sorted(v for v in out if extra is None or extra(v))

def signperm(base):
    s = set()
    for p in itertools.permutations(base):
        for sg in itertools.product((1, -1), repeat=len(base)):
            s.add(tuple(a*b for a, b in zip(p, sg)))
    return sorted(s)

def conv(A, B):
    C = Counter()
    for a, x in A.items():
        for b, y in B.items():
            C[tuple(i+j for i, j in zip(a, b))] += x*y
    return C

def counts(shell):
    d = len(shell[0]); z = (0,)*d
    D1 = Counter(shell); D2 = conv(D1, D1); D3 = conv(D2, D1)
    T = D3[z]
    Q = sum(c*D2[tuple(-x for x in k)] for k, c in D2.items())
    H = sum(c*D3[tuple(-x for x in k)] for k, c in D3.items())
    return len(set(shell)), len(shell), T, Q, H

shells = {}
shells['D4roots'] = boxshell(4, 2, 2); assert shells['D4roots'] == signperm((1,1,0,0))
shells['D4dual_x2'] = boxshell(4, 2, 4)   # 2*(min vectors of D4* = {±e_i} ∪ {(±1/2)^4})
assert shells['D4dual_x2'] == sorted(set(signperm((2,0,0,0)) + signperm((1,1,1,1))))
shells['D4s'] = boxshell(4, 3, 8); assert shells['D4s'] == signperm((2,2,0,0))
shells['Z4'] = boxshell(4, 2, 1)
shells['A4roots'] = boxshell(5, 2, 2, lambda v: sum(v) == 0)
a = [tuple(5*(1 if j == i else 0) - 1 for j in range(5)) for i in range(5)]
shells['A4star_min_x5'] = sorted(a + [tuple(-x for x in v) for v in a])
shells['BCCrow_fccvec'] = boxshell(3, 2, 2)
shells['FCCrow_bccvec'] = boxshell(3, 2, 3)
shells['SC'] = boxshell(3, 2, 1)
shells['comp7'] = boxshell(4, 4, 7); assert shells['comp7'] == signperm((2,1,1,1))
res = {}
for k, s in shells.items():
    nset, n, T, Q, H = counts(s); assert nset == n
    res[k] = (n, T, Q, H)
    print(f"{k}: N={n} T={T} Q={Q} H6={H}")
assert all(len(v) == 5 for v in shells['A4star_min_x5'])
print("A4star_min_x5 norms:", sorted(set(sum(x*x for x in v) for v in shells['A4star_min_x5'])), "sums:", set(sum(v) for v in shells['A4star_min_x5']))

def S(n, T, Q): return (F(T)**2/F(n)**3) / (F(Q)/F(n)**2)
for k in ['D4roots', 'A4roots', 'BCCrow_fccvec']:
    n, T, Q, _ = res[k]; print(f"{k}: tau2={F(T)**2/F(n)**3} q4={F(Q,n*n)} S={S(n,T,Q)}")
for k in ['FCCrow_bccvec', 'SC', 'Z4', 'A4star_min_x5']:
    n, T, Q, _ = res[k]; print(f"{k}: q4={F(Q,n*n)} T={T}")
r = S(*res['D4roots'][:3]) / S(*res['A4roots'][:3]); print("S_D4/S_A4*:", r, "margin:", r-1, "pct:", repr(float((r-1)*100)))
print("tau_D4/tau_BCC squared:", (F(res['D4roots'][1])**2/F(24)**3)/(F(res['BCCrow_fccvec'][1])**2/F(12)**3))

# partners and unordered triads
R = shells['D4roots']; dot = lambda u, v: sum(i*j for i, j in zip(u, v))
print("partners at dot -1:", Counter(sum(1 for b in R if dot(a, b) == -1) for a in R))
print("distinct-pair dot set roots:", sorted(set(dot(a, b) for a in R for b in R if a != b)))
P = shells['D4dual_x2']
print("distinct-pair dot set dual(x2, norm4):", sorted(set(dot(a, b) for a in P for b in P if a != b)))
un = sum(1 for t in itertools.combinations(R, 3) if all(sum(c) == 0 for c in zip(*t)))
print("unordered zero-sum 3-subsets:", un)

# 16^4 grid with D4s: exact congruence count, plus a float check of Psi
K = np.array(shells['D4s']); g = np.array(list(itertools.product(range(16), repeat=4)))
M = (g @ K.T) % 16; exact = int(np.sum(np.all(M == 0, axis=1)))
psi = np.cos(2*np.pi*(g @ K.T)/16).sum(axis=1)
print("grid16 points:", len(g), "exact coincidence count:", exact, "float Psi max:", repr(float(psi.max())),
      "count Psi>24-1e-9:", int(np.sum(psi > 24-1e-9)), "second-largest distinct Psi:", repr(float(np.unique(np.round(psi, 9))[-2])))
print("25^4 =", 25**4)
# C23 convention: Psi(x)=sum_g cos(2 pi g.x), g in D4* min shell = P/2
for name, x in [("lattice (1,1,0,0)", (1,1,0,0)), ("Z4\\D4 (1,0,0,0)", (1,0,0,0)), ("deep hole", (.5,.5,.5,.5))]:
    print("C23", name, repr(float(sum(math.cos(2*math.pi*dot(v, x)/2) for v in P))))
# bracket sum_alpha (1-cos(k.alpha)) max over k (relevant to N7), random + structured search
rng = np.random.default_rng(1304); Rn = np.array(R)
ks = np.vstack([rng.uniform(-np.pi, np.pi, size=(200000, 4)), np.array([[0, 0, np.pi, np.pi]])])
br = (1 - np.cos(ks @ Rn.T)).sum(axis=1); assert len(ks) > 0
print("bracket samples:", len(ks), "max:", repr(float(br.max())), "at (0,0,pi,pi):", repr(float(br[-1])))
# one-mode numbers (independent float recomputation)
N, T, Q = 24, 192, 3384; r, ps = -0.35, -0.18
reff = r - 2*ps + 3*ps*ps; ueff = 1 - 3*ps; D = (T*ueff)**2 - 4*Q*N*reff
A = (T*ueff + math.sqrt(D))/(2*Q); Fv = N/2*reff*A*A - T/3*ueff*A**3 + Q/4*A**4
rc = (T*ueff)**2/(4*Q*N)
print("reff", repr(reff), "ueff", repr(ueff), "A*", repr(A), "F(A*)", repr(Fv), "rc", repr(rc), "delta_edge", repr(math.sqrt(rc - 0.1072)))
r75 = r + (7.5-8)**2; reff75 = r75 - 2*ps + 3*ps*ps; print("q0^2=7.5: rshell", repr(r75), "reff", repr(reff75), "disc", repr((T*ueff)**2 - 4*Q*N*reff75))
a0 = 2*math.pi/math.sqrt(8); dt = math.sqrt(3)/2*a0
print("a0", repr(a0), "dtmax", repr(dt), "ratios", repr(dt/0.04), repr(dt/0.005), repr(dt/0.02))
print("16pi^2/3", repr(16*math.pi**2/3), "2/sqrt3", repr(2/math.sqrt(3)))
print("ENUM_DONE")
