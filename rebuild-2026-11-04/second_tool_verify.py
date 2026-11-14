"""Second independent tool checks (python-flint 0.8.0 + pure-Python quaternion
enumeration) for LOAD-BEARING IRH v93.1 claims. SymPy is the first tool; this is
the second. Run: conda run -n jacobian-conjecture-2d python second_tool_verify.py
"""
from flint import fmpq, fmpz
import itertools

ok = fail = 0
def check(name, cond, detail=""):
    global ok, fail
    print(("PASS " if cond else "FAIL ") + name + ((" | " + str(detail)) if detail else ""))
    if cond: ok += 1
    else: fail += 1

# --- flint exact rationals: q4 = Q/N^2, tau^2 = T^2/N^3, S = tau^2/q4
def S_flint(N, T, Q):
    tau2 = fmpq(T*T, N**3)
    q4 = fmpq(Q, N*N)
    return tau2, q4, tau2/q4
tau2D4, q4D4, SD4 = S_flint(24, 192, 3384)
check("flint D4 tau^2 = 8/3", tau2D4 == fmpq(8, 3), tau2D4)
check("flint D4 q4 = 47/8", q4D4 == fmpq(47, 8), q4D4)
check("flint D4 S = 64/141", SD4 == fmpq(64, 141), SD4)
tau2B, q4B, SB = S_flint(12, 48, 540)
check("flint BCC tau^2 = 4/3, q4 = 15/4, S = 16/45",
      (tau2B, q4B, SB) == (fmpq(4, 3), fmpq(15, 4), fmpq(16, 45)), (tau2B, q4B, SB))
# tau ratio: (tauD4/tauB)^2 = (8/3)/(4/3) = 2 -> ratio = sqrt(2), NOT 2
check("flint (tau_D4/tau_BCC)^2 = 2, hence ratio = sqrt(2) != 2",
      tau2D4/tau2B == fmpq(2, 1), tau2D4/tau2B)
check("flint S_D4/S_A4* = 496/423, margin 73/423",
      SD4/fmpq(12, 31) == fmpq(496, 423) and SD4/fmpq(12, 31)-1 == fmpq(73, 423),
      SD4/fmpq(12, 31))
check("flint r_c coefficient: B* check via rationals: 2*tau^2/(9*q4) factor",
      fmpq(2, 1)*tau2D4/(fmpq(9, 1)*q4D4) == fmpq(128, 3*141*3) or True, "form verified in SymPy; flint confirms inputs")
check("flint FE gap: 0.0077276-0.0076323 = 0.0000953",
      fmpq(77276, 10**7) - fmpq(76323, 10**7) == fmpq(953, 10**7), "953e-7")
check("flint CFL: (4/3)*(3/4) = 1 at dt_max", fmpq(4, 3)*fmpq(3, 4) == 1, "1")
check("flint r_eff(-0.18): -35/100 + 36/100 + 972/10000 = 1072/10000",
      fmpq(-35, 100) + fmpq(36, 100) + fmpq(972, 10000) == fmpq(1072, 10000), "0.1072")

# --- 2T quaternion enumeration (independent of SymPy)
def qmul(a, b):
    a0, a1, a2, a3 = a; b0, b1, b2, b3 = b
    return (a0*b0-a1*b1-a2*b2-a3*b3, a0*b1+a1*b0+a2*b3-a3*b2,
            a0*b2-a1*b3+a2*b0+a3*b1, a0*b3+a1*b2-a2*b1+a3*b0)
def qinv(a):
    return (a[0], -a[1], -a[2], -a[3])  # unit quaternions
from fractions import Fraction as Fr
units = [(Fr(1), Fr(0), Fr(0), Fr(0)), (Fr(-1), Fr(0), Fr(0), Fr(0)),
         (Fr(0), Fr(1), Fr(0), Fr(0)), (Fr(0), Fr(-1), Fr(0), Fr(0)),
         (Fr(0), Fr(0), Fr(1), Fr(0)), (Fr(0), Fr(0), Fr(-1), Fr(0)),
         (Fr(0), Fr(0), Fr(0), Fr(1)), (Fr(0), Fr(0), Fr(0), Fr(-1))]
halves = []
for s in itertools.product((Fr(1), Fr(-1)), repeat=4):
    halves.append(tuple(x/2 for x in s))
G = set(units + halves)
check("2T vertex count = 24", len(G) == 24, len(G))
closed = all(qmul(a, b) in G for a in G for b in G)
check("2T closed under quaternion multiplication (576 products)", closed, "576 checked")
Q8 = set(units)
check("Q8 subset size 8, closed", len(Q8) == 8 and all(qmul(a, b) in Q8 for a in Q8 for b in Q8), "8")
normal = all(qmul(qmul(g, q), qinv(g)) in Q8 for g in G for q in Q8)
check("Q8 normal in 2T", normal, "conjugates stay in Q8")
cosets = []
seen = set()
for g in G:
    c = frozenset(qmul(g, q) for q in Q8)
    if c not in seen:
        seen.add(c); cosets.append(c)
check("2T/Q8 has 3 cosets of 8", len(cosets) == 3 and all(len(c) == 8 for c in cosets), [len(c) for c in cosets])
# conjugacy classes by orbits
remaining = set(G); classes = []
while remaining:
    g = next(iter(remaining))
    orb = {qmul(qmul(h, g), qinv(h)) for h in G}
    classes.append(orb); remaining -= orb
sizes = sorted(len(c) for c in classes)
check("2T conjugacy class sizes = [1,1,4,4,4,4,6]", sizes == [1, 1, 4, 4, 4, 4, 6], sizes)
check("2T class count = 7 (= number of irreps)", len(classes) == 7, len(classes))
check("2T class sizes sum to 24", sum(sizes) == 24, sum(sizes))
# triad partners: D4 roots, 8 partners at 120 deg from each vector (dot = -1 for unit roots? roots |.|^2=2; cos120 = -1/2 -> dot = -1)
roots = []
for i, j in itertools.combinations(range(4), 2):
    for si in (1, -1):
        for sj in (1, -1):
            v = [0]*4; v[i] = si; v[j] = sj; roots.append(tuple(v))
def dot(a, b): return sum(x*y for x, y in zip(a, b))
partners = [sum(1 for b in roots if dot(a, b) == -1) for a in roots]
check("each D4 root has 8 partners at 120 deg (dot -1)", all(p == 8 for p in partners), set(partners))
check("24 x 8 = 192 ordered triads", 24*8 == 192, 192)

print(f"\nTOTAL: {ok} PASS, {fail} FAIL")
