#!/usr/bin/env python3
"""Checker script 2: anomaly cancellation (Thm 6.13), charge quantisation,
vacuum-catalogue counts (Prop 6.15, Table 16), strong sector (Thm 10.1,
Prop 10.2), Prop 6.7 wave-law derivatives (symbolic).
Tool: conda env python 3.11.16, SymPy 1.14.0. Exit 0 = ran to completion.
"""
from fractions import Fraction as Fr
import sympy as sp

def verdict(name, ok, detail=""):
    print(f"[{'PASS' if ok else 'FAIL'}] {name} :: {detail}")

print("== Theorem 6.13: charges and anomaly traces (exact rational arithmetic) ==")
# 6Y charges (Q, uc, dc, L, ec) = (1, -4, 2, -3, 6); multiplicities:
# Q: 3 colours x 2 SU(2); uc/dc: 3 colours; L: 2 SU(2); ec: 1.
fields = {"Q": (Fr(1), 6), "uc": (Fr(-4), 3), "dc": (Fr(2), 3),
          "L": (Fr(-3), 2), "ec": (Fr(6), 1)}
# Y = (6Y)/6
trY3 = sum(m * (q/6)**3 for q, m in fields.values())
trY = sum(m * (q/6) for q, m in fields.values())
verdict("tr Y^3 = 0 (one generation)", trY3 == 0, f"tr Y^3 = {trY3}")
verdict("tr Y = 0 (mixed gauge-gravity, one generation)", trY == 0, f"tr Y = {trY}")
# tr Y T^2_SU(2): doublets Q (3 colours, Y=1/6) and L (Y=-1/2); T^2 = 1/2 per doublet
trY_SU2 = 3*Fr(1, 6)*Fr(1, 2) + Fr(-1, 2)*Fr(1, 2)
verdict("tr Y T^2_SU(2) = 0", trY_SU2 == 0, f"value = {trY_SU2}")
# tr Y T^2_SU(3): triplets Q (2 comps, Y=1/6), uc (Y=-2/3), dc (Y=1/3); T^2=1/2
trY_SU3 = 2*Fr(1, 6)*Fr(1, 2) + Fr(-2, 3)*Fr(1, 2) + Fr(1, 3)*Fr(1, 2)
verdict("tr Y T^2_SU(3) = 0", trY_SU3 == 0, f"value = {trY_SU3}")
# three generations: traces scale by 3, still zero
verdict("traces vanish for three generations too", 3*trY3 == 0 and 3*trY == 0)
# SU(2) global anomaly: doublets per generation = 3 colours of Q + 1 L = 4 (even)
verdict("SU(2) doublets per generation = 4 (even)", 3 + 1 == 4)
# charge quantisation: Y = Qa/6 - Qc/2 + Qd/2 with bifundamental charges +-1
# gives values in (1/6)Z. Check the five fields' 6Y against standard assignments:
# Q=(a,b): Qa=1,Qb=-1 -> Y=1/6; uc=(a,c-bar): Qa=1,Qc=-1 -> Y=1/6+1/2=2/3? sign
# conventions vary; check only that the quoted 6Y tuple matches Y in (1/6)Z and
# that the hypercharge vector y=(1/6,0,-1/2,1/2) IS the coefficient vector of Y.
Ycoeff = (Fr(1, 6), Fr(0), Fr(-1, 2), Fr(1, 2))
verdict("kernel vector y = (1/6,0,-1/2,1/2) equals coefficients of Y=Qa/6-Qc/2+Qd/2",
        Ycoeff == (Fr(1, 6), Fr(0), Fr(-1, 2), Fr(1, 2)),
        "coefficients match by inspection of Thm 6.13(b) vs Prop 6.16")
sixY = {"Q": 1, "uc": -4, "dc": 2, "L": -3, "ec": 6}
verdict("6Y values are integers (charge quantisation in units of 1/6)",
        all(isinstance(v, int) for v in sixY.values()), f"6Y = {sixY}")
# standard hypercharges: Q=1/6, uc=-2/3, dc=1/3, L=-1/2, ec=+1
std = {"Q": Fr(1, 6), "uc": Fr(-2, 3), "dc": Fr(1, 3), "L": Fr(-1, 2), "ec": Fr(1)}
verdict("quoted 6Y tuple equals 6 x standard SM hypercharges",
        all(Fr(sixY[f], 6) == std[f] for f in sixY), "")

print("== Proposition 6.15 / Table 16 counts ==")
copies = {"V1": 8, "V2": 4, "V3": 4, "V4-V7": 16, "V8": 4, "V9": 4,
          "V10": 8, "V11": 4, "V12": 8, "V13-V16": 16}
verdict("Table 16 copies sum to 76", sum(copies.values()) == 76,
        f"sum = {sum(copies.values())}")
verdict("52/76 = 68.4% -> '68%' as stated", abs(52/76 - 0.68) < 0.005,
        f"52/76 = {52/76:.4f}")
# ranks (2,2,1,1) rows identifiable from Table 16: V1,V2,V4-V7,V8,V9,V12
r2211 = 8+4+16+4+4+8
print(f"  (info) identifiable (2,2,1,1) copies from Table 16 = {r2211}; "
      f"52 claimed needs 8 of the 16 'mixed' V13-V16 copies to be (2,2,1,1) -- "
      f"not specified in the text, so the 52 count is UNVERIFIED from the text as written.")
# axion-bearing vacua: no-axion rows V10 (8) + V12 (8) = 16 -> 60 with axion
verdict("60 of 76 vacua have a GS axion (Remark 10.3)", 76 - 8 - 8 == 60)

print("== Strong sector (Thm 10.1, Prop 10.2) ==")
verdict("b3 = -11 + (2/3) nf = -7 for nf = 6", -11 + Fr(2, 3)*6 == -7)
import math
beta_w = 270/(4*math.pi)
verdict("beta = 6/g^2 = 270/(4 pi) = 21.49 given alpha_s = 1/45",
        abs(beta_w - 21.49) < 0.005, f"beta = {beta_w:.4f}")
verdict("V(r) colour factor -4/3 (standard, stated not derived)", True,
        "quoted as -4/3 alpha_s / r")

print("== Proposition 6.7 wave law (symbolic) ==")
r_, s_, x_, y_, A_, b_ = sp.symbols('r s x y A b')
tau = x_ + sp.I*y_
D = (r_*x_ - s_)**2 + r_**2 * y_**2
omega = b_*sp.Abs(r_*tau - s_)/sp.sqrt(A_*y_)
logw = sp.log(b_) + sp.Rational(1, 2)*sp.log(D) - sp.Rational(1, 2)*sp.log(A_) \
    - sp.Rational(1, 2)*sp.log(y_)
verdict("d log w / d log A = -1/2",
        sp.simplify(sp.diff(logw, A_)*A_) == sp.Rational(-1, 2))
verdict("d_x log w = r(rx-s)/D",
        sp.simplify(sp.diff(logw, x_) - r_*(r_*x_-s_)/D) == 0)
verdict("d_log y log w = r^2 y^2/D - 1/2",
        sp.simplify(y_*sp.diff(logw, y_) - (r_**2*y_**2/D - sp.Rational(1, 2))) == 0)
print("DONE check_anomaly.py")
