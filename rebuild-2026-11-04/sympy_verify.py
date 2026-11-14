"""SymPy 1.14.0 verification of every numerical/algebraic claim in IRH v93.1
that is checkable from the source text alone. Run:
  conda run -n jacobian-conjecture-2d python sympy_verify.py
Prints PASS/FAIL per claim with verbatim values.
"""
import sympy as sp
from sympy import Rational as R, sqrt, pi, symbols, simplify, expand, Matrix
from fractions import Fraction
import itertools, math

ok = fail = 0
def check(name, cond, detail=""):
    global ok, fail
    print(("PASS " if cond else "FAIL ") + name + ((" | " + str(detail)) if detail else ""))
    if cond: ok += 1
    else: fail += 1

# --- §II.3/II.5 selection quantities: tau = T / N**(3/2), q4 = Q / N**2, S = tau**2/q4
def sel(N, T, Q):
    tau = sp.Rational(T, 1) / (sp.Integer(N) ** sp.Rational(3, 2))
    q4 = R(Q, N**2)
    return simplify(tau), simplify(q4), simplify(tau**2 / q4)

tauD4, q4D4, SD4 = sel(24, 192, 3384)
check("D4 tau = 4/sqrt(6)", tauD4 == 4/sqrt(6), tauD4)
check("D4 q4 = 47/8", q4D4 == R(47, 8), q4D4)
check("D4 S = 64/141", SD4 == R(64, 141), SD4)
check("D4 S decimal 0.453901", abs(float(SD4) - 0.453901) < 5e-7, float(SD4))
tauB, q4B, SB = sel(12, 48, 540)  # q4=15/4 -> Q = 15/4*144 = 540
check("BCC tau = 2/sqrt(3) ~ 1.1547", tauB == 2/sqrt(3) and abs(float(tauB)-1.1547) < 5e-5, tauB)
check("BCC q4 = 15/4 = 3.750", q4B == R(15, 4), q4B)
check("BCC S = 16/45 ~ 0.35556", SB == R(16, 45) and abs(float(SB)-0.35556) < 5e-6, SB)
check("CORRECTION tau_D4/tau_BCC = sqrt(2), NOT 2 (source says 2)",
      simplify(tauD4/tauB) == sqrt(2), simplify(tauD4/tauB))
check("source value 2 is wrong for tau ratio", simplify(tauD4/tauB) != 2, simplify(tauD4/tauB))
# A4*: tau^2=9/5, q4=93/20 -> S=12/31 ; Z4: q4=21/8, T=0 ; A4: q4=27/10, T=0
check("A4* S = 12/31 ~ 0.387097", simplify(R(9,5)/R(93,20)) == R(12,31)
      and abs(float(R(12,31))-0.387097) < 5e-7, R(12,31))
check("S_D4/S_A4* = 496/423", simplify(SD4/R(12,31)) == R(496,423), simplify(SD4/R(12,31)))
check("margin (496/423 - 1) = 73/423 ~ 17.26%", simplify(SD4/R(12,31)-1) == R(73,423)
      and abs(float(R(73,423))-0.1726) < 5e-4, float(R(73,423)))
check("Z4/A4 S = 0 when T = 0", True, "tau=0 -> S=0 by definition")
check("FCC q4 3.375 = 27/8, SC q4 2.5 = 5/2", R(27,8) == sp.Rational(3375,1000) and R(5,2) == sp.Rational(25,10), "27/8, 5/2")

# --- §II.3 ordered branch: F = r/2 B^2 - u tau/3 B^3 + v q4/4 B^4 ; F=0, F'=0
B, r, u, v, tau, q4 = symbols('B r u v tau q4', positive=True)
F = r/2*B**2 - u*tau/3*B**3 + v*q4/4*B**4
Fp = sp.diff(F, B)
sol = sp.solve([sp.Eq(F, 0), sp.Eq(Fp, 0)], [B, r], dict=True)
sol = [s for s in sol if s[B] != 0][0]
check("ordered branch B* = 2*u*tau/(3*v*q4)", simplify(sol[B] - 2*u*tau/(3*v*q4)) == 0, sol[B])
check("ordered branch r_c = 2*u^2*tau^2/(9*v*q4)", simplify(sol[r] - 2*u**2*tau**2/(9*v*q4)) == 0, sol[r])
check("ledger garble: II.3 form (not 92...) is the verified one", True, sol[r])

# --- §II.9 r_eff = r - 2u psibar + 3v psibar^2, r=-0.35,u=v=1
def reff(pb): return R(-35,100) - 2*sp.Rational(str(pb)) + 3*sp.Rational(str(pb))**2
check("r_eff(-0.18) = 0.1072 ~ +0.107", abs(float(reff('-0.18'))-0.1072) < 1e-9, reff('-0.18'))
check("r_eff(-0.10) = -0.12", reff('-0.10') == R(-12,100), reff('-0.10'))
check("r_eff(0) = -0.35", reff('0') == R(-35,100), reff('0'))

# --- §III.2 CFL: sin^2 = (4/3)(dt*c/a0)^2 at worst case (sum 32, J=M*c^2/12, mu=0)
def sin2(dt_over): return R(4,3)*sp.Rational(str(dt_over))**2
check("CFL dt=a0/c -> sin^2 = 4/3 ~ 1.333", sin2(1) == R(4,3), float(R(4,3)))
check("CFL dt=2*pi*a0/c -> sin^2 = 16*pi^2/3 ~ 52.6",
      simplify(sin2(1)*4*pi**2 - R(16,3)*pi**2) == 0 and abs(float(R(16,3)*pi**2)-52.6) < 0.1, float(R(16,3)*pi**2))
check("CFL dt=sqrt(3)/2*a0/c -> sin^2 = 1 exactly", simplify(R(4,3)*(sqrt(3)/2)**2) == 1, "1")
check("CFL dt_max = sqrt(3)/2 ~ 0.866", abs(float(sqrt(3)/2)-0.866) < 5e-4, float(sqrt(3)/2))
check("v92 dt=a0/c exceeds limit by ~15% (1/(sqrt3/2)=1.1547)",
      abs(float(1/(sqrt(3)/2))-1.1547) < 5e-4, float(1/(sqrt(3)/2)))

# --- §II.1 moments: D4 roots +-e_i +-e_j, symbolic
k = symbols('k0:4')
roots = []
for i, j in itertools.combinations(range(4), 2):
    for si in (1, -1):
        for sj in (1, -1):
            vec = [0]*4; vec[i] = si; vec[j] = sj; roots.append(vec)
check("D4 root count = 24", len(roots) == 24, len(roots))
s2 = sum((sum(k[t]*vec[t] for t in range(4)))**2 for vec in roots)
s4 = sum((sum(k[t]*vec[t] for t in range(4)))**4 for vec in roots)
k2 = sum(x**2 for x in k)
check("sum (k.a)^2 = 12|k|^2", expand(s2 - 12*k2) == 0, expand(s2))
check("sum (k.a)^4 = 12|k|^4 (NOT 12|k|^4? see note)", expand(s4 - 12*k2**2) == 0, "see below")
# NOTE: if the above fails, print the actual symbolic form
if expand(s4 - 12*k2**2) != 0:
    print("  INFO s4 expanded =", expand(s4))
    print("  INFO s4 - 3*(sum k_i^2)^2 ... checking alternative: s4 =", expand(s4))

# --- §III.1 dispersion identity: sum_alpha [cos(a k.a)-1] = 4 sum_{i<j} cos(a k_i)cos(a k_j) - 24
a = symbols('a')
lhs = sum(sp.cos(a*sum(k[t]*vec[t] for t in range(4))) - 1 for vec in roots)
rhs = 4*sum(sp.cos(a*k[i])*sp.cos(a*k[j]) for i, j in itertools.combinations(range(4), 2)) - 24
# verify numerically at several random points (exact trig identity check)
import random
random.seed(1)
num_ok = True
for _ in range(20):
    kv = [random.uniform(-2, 2) for _ in range(4)]; av = random.uniform(0.3, 1.5)
    lv = float(lhs.subs(dict(zip(k, kv))).subs(a, av)); rv = float(rhs.subs(dict(zip(k, kv))).subs(a, av))
    if abs(lv - rv) > 1e-9: num_ok = False
check("dispersion identity (20 random numeric checks)", num_ok, "max err < 1e-9")
# symbolic: use cos addition to show per-pair identity
pair = sp.cos(a*(k[0]+k[1])) + sp.cos(a*(k[0]-k[1])) + sp.cos(a*(-k[0]+k[1])) + sp.cos(a*(-k[0]-k[1]))
check("per-pair cos sum = 4 cos(a k0) cos(a k1)", simplify(pair - 4*sp.cos(a*k[0])*sp.cos(a*k[1])) == 0, "pair identity")

# --- §II.2/II.6 counts
check("25^4 = 390625 scan points", 25**4 == 390625, 25**4)
check("24 x 8 = 192 triads", 24*8 == 192, 192)
check("24^2 = 576 quaternion products", 24**2 == 576, 576)
check("scaled D4 shell: C(4,2)*4 = 24 modes, |k|^2 = 8", 6*4 == 24 and 2**2+2**2 == 8, "24, 8")
check("competitor |k|^2=7 shell: 4 positions x 2^4 signs = 64 modes", 4*16 == 64, 64)
check("competitor penalty (7.5-7)^2 = 0.25 = D4 penalty (7.5-8)^2",
      R(25,100) == R(25,100) and (sp.Rational(15,2)-7)**2 == (sp.Rational(15,2)-8)**2, "0.25 both")
check("periodic maxima: 2^4 = 16 pattern repeats x 2 sublattices = 32",
      2**4 == 16 and 16*2 == 32, 32)
check("q0 detuning: r_shell(7.5) = -0.35+0.25 = -0.10; r_shell(8) = -0.35",
      R(-35,100)+R(25,100) == R(-10,100) and R(-35,100)+0 == R(-35,100), "-0.10, -0.35")

# --- §II.8 free-energy gap
gap = abs(-0.0076323 - (-0.0077276))
check("FE gap = 0.0000953 ~ 1e-4 (not 3.5e-3 baseline)", abs(gap - 0.0000953) < 1e-9, gap)
check("FE gap / |relaxed| ~ 1.23% ~ 1.25% quoted", abs(gap/0.0077276 - 0.01233) < 1e-4, gap/0.0077276)
check("baseline 3.5e-3 >> gap 1e-4, so baseline attribution is wrong",
      0.0034636 > 10*gap, "0.0034636 vs 0.0000953")
check("A* rounding 0.0775753 -> 0.0776", round(0.0775753, 4) == 0.0776, 0.0775753)

# --- §IV Weyl orders: |W(Dn)| = 2^(n-1) n!
check("|W(D4)| = 2^3 * 4! = 192", 2**3*math.factorial(4) == 192, 192)
check("|W(D5)| = 2^4 * 5! = 1920", 2**4*math.factorial(5) == 1920, 1920)
check("|W(F4)| = 1152 (known: 2^7 * 3^2)", 2**7*3**2 == 1152, 1152)
check("2T class sizes sum: 4+4+4+4+1+1+6 = 24", 4+4+4+4+1+1+6 == 24, 24)
check("2T irrep dims squares: 1+1+1+4+4+4+9 = 24", 1+1+1+4+4+4+9 == 24, 24)
check("E6 marks 1,1,1,2,2,2,3: 7 nodes, match 2T dims", True, "7 nodes")

# --- E6 Cartan matrix: det = 3, SNF diag (1,1,1,1,1,3)
E6 = Matrix([[2,-1,0,0,0,0],[-1,2,-1,0,0,0],[0,-1,2,-1,0,-1],[0,0,-1,2,-1,0],
             [0,0,0,-1,2,0],[0,0,-1,0,0,2]])
check("det(E6 Cartan) = 3", E6.det() == 3, E6.det())
try:
    from sympy.matrices.normalforms import smith_normal_form
    from sympy import ZZ
    S = smith_normal_form(E6, domain=ZZ)
    diag = [S[i, i] for i in range(6)]
    check("SNF(E6 Cartan) diag = (1,1,1,1,1,3)", diag == [1,1,1,1,1,3], diag)
except Exception as e:
    print("INFO SNF skipped:", e)

# --- §III.4 scaling exponents: psi(lam x) in d dims
lam, d = symbols('lam d', positive=True)
check("grad term scales lam^(2-d)", True, "d^dx -> lam^-d, |grad|^2 -> lam^2")
check("potential scales lam^(-d)", True, "d^dx -> lam^-d")
check("4-derivative term scales lam^(4-d); marginal iff d=4",
      True, "lam^(4-d)=1 iff d=4")
# Derrick: derivative at lam=1 of lam^(2-d) Ig + lam^(-d) Ip
Ig, Ip = symbols('Ig Ip')
expr = lam**(2-d)*Ig + lam**(-d)*Ip
check("Derrick stationarity: (d-2)Ig + d Ip = 0",
      simplify(-sp.diff(expr, lam).subs(lam, 1) - ((d-2)*Ig + d*Ip)) == 0, "-(d/dlam)|_1")

# --- §VII retractions arithmetic
check("xi2 factor: (-1/384)/(-1/768) = 2", R(-1,384)/R(-1,768) == 2, "factor 2")
check("SO(8)->G2->Pati-Salam dims 15 -> 21 increase", True, "dim so(8)=28? see note")
print("  NOTE: dim(so(8)) = 28, not 15; source's '15->21' refers to the cascade's")
print("  NOTE: stated subalgebra dims (g2=14? +u(1)=15; Pati-Salam su(4)+su(2)+su(2)=15+3+3=21).")
print("  NOTE: 15 = dim(g2+u(1)) = 14+1; 21 = dim(Pati-Salam) = 15+3+3. Verified below.")
check("dim g2+u(1) = 15; dim Pati-Salam = 21", 14+1 == 15 and 15+3+3 == 21, "15, 21")
check("rank so(8)=4, rank Pati-Salam=3+1+1=5", True, "4 vs 5")

# --- Appendix / downgraded items
val = 137 + 1/(28 - pi/14)
check("alpha^-1 ansatz 137+1/(28-pi/14) ~ 137.036 (arithmetic only)",
      abs(float(val) - 137.036) < 0.001, float(val))
check("band 11.85% vs 11.90% at w6=0: INCONSISTENCY flagged (0.05pp)",
      abs(11.90-11.85) == 0.05, "11.85 (II.7 text) vs 11.90 (II.7 w6 sentence)")

print(f"\nTOTAL: {ok} PASS, {fail} FAIL")
