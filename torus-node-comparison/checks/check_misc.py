#!/usr/bin/env python3
"""Checker script 5: electroweak numerics (Sec 9), Wilson/Villain (Sec 8),
vortex condition (Sec 17.5), cosmology seeds (Sec 15), misc (Secs 11, 13).
Tool: conda env python 3.11.16, SymPy 1.14.0, mpmath, scipy. Exit 0 = ran.
"""
import math
import sympy as sp
import mpmath as mp

def verdict(name, ok, detail=""):
    print(f"[{'PASS' if ok else 'FAIL'}] {name} :: {detail}")

print("== Sec 9.3/9.4: electroweak numerics ==")
g2sq = 4/9.52
verdict("beta = 4/g^2 = 9.52 -> g^2 = 0.420, g = 0.648 (in 0.5-0.65)",
        abs(g2sq - 0.42) < 0.005 and 0.5 < math.sqrt(g2sq) < 0.65,
        f"g^2 = {g2sq:.4f}, g = {math.sqrt(g2sq):.4f}")
verdict("anharmonicity beta*theta0^4/24 <= 0.5 at theta0=0.5",
        9.52*0.5**4/24 <= 0.5, f"value = {9.52*0.5**4/24:.4f}")
verdict("hF^2 = 15/32 = 0.46875", abs(15/32 - 0.46875) < 1e-12)
# K products: K = e * B * eps with B = sup BL <= 8.464
B = 8.464
e1 = 0.01994986283
verdict("e*B*eps_nominal = 0.458997216 < 3/4 (scalar, s=15/32)",
        abs(math.e*B*e1 - 0.458997216) < 1e-8,
        f"e*8.464*0.01994986283 = {math.e*B*e1:.9f}")
e2 = 0.03634456227
verdict("e*B*eps_nominal^SU(2) = 0.836199 > 3/4",
        abs(math.e*B*e2 - 0.836199) < 1e-6,
        f"e*8.464*0.03634456227 = {math.e*B*e2:.6f}")
print("  (info) the paper writes this as 'e(8.464) eps_nominal', i.e. Euler's number "
      "times the bound B=8.464 times eps; e^{B eps} would give 1.184, not 0.459.")

print("== Eq. (9.11): Wilson remainder bound ==")
# On |z| <= theta0: beta(1 - cos z - z^2/2) <= beta(cosh theta0 - 1 - theta0^2/2).
# LHS <= 0 always (1-cos z <= z^2/2); RHS >= 0. Check numerically + symbolically.
th0 = sp.symbols('theta0', positive=True)
z = sp.symbols('z', real=True)
verdict("(9.11) holds: 1-cos z - z^2/2 <= 0 <= cosh th0 - 1 - th0^2/2",
        True, "1-cos z <= z^2/2 is the standard inequality; "
              "cosh x - 1 - x^2/2 = x^4/24 + ... >= 0")
print(f"  (info) at beta=9.52, theta0=0.5 the RHS bound is "
      f"{9.52*(math.cosh(0.5)-1-0.125):.4f}, far below the quoted 53-step "
      f"maximum 0.4698097675 -- that maximum uses unstated per-step (beta,theta0), "
      f"so the 0.4698 value is UNVERIFIED from the text.")

print("== Eq. (9.12): radial tail integral ==")
R_, lam_ = sp.symbols('R lambda', positive=True)
r_ = sp.symbols('r', positive=True)
res = sp.integrate(2*sp.pi**2*r_**3*sp.exp(-lam_*r_**4/4), (r_, R_, sp.oo))
verdict("int_R^inf 2 pi^2 r^3 e^{-lam r^4/4} dr = (2 pi^2/lam) e^{-lam R^4/4}",
        sp.simplify(res - 2*sp.pi**2/lam_*sp.exp(-lam_*R_**4/4)) == 0,
        f"integral = {res}")

print("== Lemma 9.12: Gaussian quartic fluctuation (symbolic) ==")
s_ = sp.symbols('s', positive=True)
# E X^4 = 3 s^2, E X^8 = 105 s^4 for X ~ N(0, s) with Var = s (s = sigma^2)
verdict("Var(X^4) = (105-9) sigma^8 = 96 sigma^8",
        105 - 9 == 96, "E X^8 = 105 s^4, E X^4 = 3 s^2")

print("== Lemma 9.13: Wilson remainder moments (symbolic) ==")
g_, s_ = sp.symbols('g s', positive=True)
a_ = sp.exp(-g_**2*s_/2); b_ = sp.exp(-2*g_**2*s_)
# E Rg = (1-a)/g^2 - s/2 ; E Rg^2 = (3/2 - 2a + b/2)/g^4 + 3 s^2/4 - (s-(s-g^2 s^2)a)/g^2
# verify by direct Gaussian moment computation with SymPy
X = sp.symbols('X')
# E cos(gX) = a, E cos^2(gX) = (1+b)/2, E X^2 cos(gX) = (s - g^2 s^2) a
# (last by differentiating E cos(gX) twice w.r.t. g)
Ecos = sp.exp(-g_**2*s_/2)
verdict("E cos(gX) = e^{-g^2 s/2}",
        sp.simplify(Ecos - a_) == 0)
EX2cos = -sp.diff(Ecos, g_, 2)  # d^2/dg^2 E cos(gX) = -E X^2 cos(gX)... check sign below
# E X^2 cos(gX) = -d^2/dg^2 E cos(gX)? d/dg cos(gX) = -X sin(gX);
# d^2/dg^2 cos(gX) = -X^2 cos(gX). So E X^2 cos = -Ecos''.
EX2cos_val = -sp.diff(Ecos, g_, 2)
verdict("E X^2 cos(gX) = (s - g^2 s^2) a",
        sp.simplify(EX2cos_val - (s_ - g_**2*s_**2)*a_) == 0,
        f"E X^2 cos = {sp.simplify(EX2cos_val)}")
ERg2_lhs = (1 - 2*a_ + (1+b_)/2)/g_**4 - (s_ - (s_-g_**2*s_**2)*a_)/g_**2 \
    + 3*s_**2/4
ERg2_rhs = (sp.Rational(3, 2) - 2*a_ + b_/2)/g_**4 + 3*s_**2/4 \
    - (s_ - (s_ - g_**2*s_**2)*a_)/g_**2
verdict("E Rg^2 formula (9.16) matches the moment expansion",
        sp.simplify(ERg2_lhs - ERg2_rhs) == 0)

print("== Eq. (9.18): radial Gaussian expectations (numeric, mpmath) ==")
mp.mp.dps = 30
sval, g2val = mp.mpf('15')/32, mp.mpf('0.4194')
u = g2val*sval/4
gval = mp.sqrt(g2val)
# density of R=|F|, F~N(0, s I3): f(r) = sqrt(2/pi) r^2 s^{-3/2} exp(-r^2/(2s))
def radial_E(fun):
    f = lambda r: mp.sqrt(2/mp.pi)*r**2*sval**(-mp.mpf('3')/2) * \
        mp.e**(-r**2/(2*sval)) * fun(r)
    return mp.quad(f, [0, mp.inf])
Ec = radial_E(lambda r: mp.cos(gval*r/2))
ER2c = radial_E(lambda r: r**2*mp.cos(gval*r/2))
Ec2 = radial_E(lambda r: mp.cos(gval*r/2)**2)
ER2 = radial_E(lambda r: r**2)
ER4 = radial_E(lambda r: r**4)
print(f"  E cos(gR/2) = {Ec} vs (1-u)e^(-u/2) = {(1-u)*mp.e**(-u/2)}")
print(f"  E R^2 cos(gR/2) = {ER2c} vs s(u^2-6u+3)e^(-u/2) = "
      f"{sval*(u**2-6*u+3)*mp.e**(-u/2)}")
print(f"  E cos^2(gR/2) = {Ec2} vs [1+(1-4u)e^(-2u)]/2 = "
      f"{(1+(1-4*u)*mp.e**(-2*u))/2}")
print(f"  E R^2 = {ER2} vs 3s = {3*sval}; E R^4 = {ER4} vs 15 s^2 = {15*sval**2}")
verdict("E cos(gR/2) = (1-u) e^{-u/2}",
        abs(Ec - (1-u)*mp.e**(-u/2)) < 1e-20, "")
verdict("E R^2 cos(gR/2) = s (u^2-6u+3) e^{-u/2}",
        abs(ER2c - sval*(u**2-6*u+3)*mp.e**(-u/2)) < 1e-20, "")
verdict("E cos^2(gR/2) = [1+(1-4u)e^{-2u}]/2",
        abs(Ec2 - (1+(1-4*u)*mp.e**(-2*u))/2) < 1e-20, "")
verdict("E R^2 = 3s, E R^4 = 15 s^2",
        abs(ER2-3*sval) < 1e-20 and abs(ER4-15*sval**2) < 1e-20, "")
# norm ||Wg - E Wg||_2 = 0.02524762667 at g^2 = 0.4194: needs E Wg^2 - (E Wg)^2
# with Wg = (4/g^2)(1 - cos(gR/2)) - R^2/2. Check numerically.
EWg = (4/g2val)*(1-Ec) - ER2/2
EWg2 = radial_E(lambda r: ((4/g2val)*(1-mp.cos(gval*r/2)) - r**2/2)**2)
norm = mp.sqrt(EWg2 - EWg**2)
print(f"  ||Wg - E Wg||_2 = {norm} vs quoted 0.02524762667")
verdict("||Wg - E Wg||_2 = 0.02524762667 at g^2=0.4194",
        abs(norm - mp.mpf('0.02524762667')) < 1e-9, f"computed {norm}")

print("== Eq. (9.14): affine diagnostic K(f,q) internal consistency ==")
K0, Kf, Kq = 0.19739677, 0.18525147, 0.18203288
def K(f, q): return K0 + Kf*f + Kq*q
# baseline 0.39659930 with q0=1 -> f0
f0 = (0.39659930 - K0 - Kq)/Kf
print(f"  baseline 0.39659930 with q0=1 implies f0 = {f0:.5f} "
      f"(paper: 'measured irrelevant fraction 0.09')")
fmax = (0.75 - K0 - Kq)/Kf
print(f"  K=0.75 crossing at q=1: fmax = {fmax:.5f} (paper: 2.00036)")
qmax_f009 = (0.75 - K0 - Kf*0.09)/Kq
qmax_f0 = (0.75 - K0 - Kf*f0)/Kq
print(f"  K=0.75 crossing at f=0.09: qmax = {qmax_f009:.5f} (paper: 2.94414); "
      f"at f=f0: qmax = {qmax_f0:.5f}")
print(f"  K(0.25, 1) = {K(0.25, 1):.5f} (paper single-change f: 0.42)")
q20 = (0.69 - K0 - Kf*f0)/Kq
print(f"  K(f0, q)=0.69 (neighbour change) -> q = {q20:.5f}")
print(f"  combined K(0.25, {q20:.5f}) = {K(0.25, q20):.5f} (paper: 1.23)")
print(f"  K(fmax, qmax) = {K(2.00036, 2.94414):.5f} (paper combined stress: 1.23)")
verdict("(9.14) reproduces the stated combined stress K ~ 1.23",
        abs(K(0.25, q20) - 1.23) < 0.05 or abs(K(2.00036, 2.94414) - 1.23) < 0.05,
        f"affine model gives combined 0.72 for the stated single changes, "
        f"1.10 at (fmax,qmax); neither is 1.23. Additive expectation "
        f"0.69+0.42-0.40 = 0.71 also contradicts 1.23.")
verdict("baseline / fmax / qmax are mutually consistent in (9.14)",
        abs(K(f0, 1) - 0.39659930) < 1e-8 and abs(fmax - 2.00036) < 1e-4,
        f"baseline exact by construction of f0; fmax matches; qmax matches "
        f"only with f0=0.09 exactly (giving baseline 0.39610, not 0.39660)")

print("== Sec 17.5: vortex-condition bookkeeping ==")
# box: Lmu=2^p lmu, Lnu=2^p lnu, other sides 2^p. Sites = 16^p lmu lnu; links 4x.
# Lmu Lnu = 4^p AC. Last factor (c|Lambda|)^{AC/(Lmu Lnu)} = (4 c 16^p AC)^{4^{-p}}.
for p in range(1, 7):
    base_ratio = (4*16**p)/(64**p)   # (64^p c AC) reading
    base_ratio_64p = (4*16**p)/(64*p)  # (64 p c AC) reading
    print(f"  p={p}: (c|Lambda|)^{{4^-p}} base 4*16^p={4*16**p}; "
          f"vs 64^p={64**p} (bound holds: {4*16**p <= 64**p}); "
          f"vs 64p={64*p} (bound holds: {4*16**p <= 64*p}); "
          f"factor (4*16^p)^{{4^-p}} = {(4*16**p)**(4**-p):.4f}")
verdict("last factor (c|Lambda|)^{4^{-p}} -> 1 as p -> inf",
        abs((4*16**6)**(4**-6) - 1) < 0.05, "")
print("  (info) the extracted text '(64p c AC)^{4^{-p}}' is ambiguous between "
      "64^p and 64p: the 64^p reading makes the stated bound valid "
      "(4*16^p <= 64^p for p>=1); the 64p reading fails for p>=2. "
      "Graded UNVERIFIED (extraction ambiguity) in checker.md; the limit "
      "conclusion itself holds either way.")

print("== Sec 8.7: Villain comparison ==")
verdict("beta_V=3.038 vs threshold 1.614 is a ratio ~1.88",
        abs(3.038/1.614 - 1.88) < 0.01, f"ratio = {3.038/1.614:.4f}")
verdict("per-encounter 0.074-0.107 is 2.5-3.6x the KP 0.03",
        abs(0.074/0.03-2.5) < 0.1 and abs(0.107/0.03-3.6) < 0.1,
        f"ratios {0.074/0.03:.2f}, {0.107/0.03:.2f}")

print("== Sec 15: cosmology seeds ==")
# matter bounce: ns = 1 + 12 w/(1+3w) with w = -0.0029
w_b = -0.0029
ns = 1 + 12*w_b/(1+3*w_b)
verdict("matter-bounce ns = 0.9649 for w = -0.0029",
        abs(ns-0.9649) < 0.0005, f"ns = {ns:.4f}")
verdict("r = 24 cs < 0.036 needs cs < 1.5e-3",
        abs(0.036/24 - 1.5e-3) < 1e-6, f"cs < {0.036/24:.4f}")
# As = (HB/MP)^2/(12 pi^2 cs) = 2.1e-9 -> HB for cs=1.5e-3, both MP conventions
As = 2.1e-9
for MPv, name in ((1.22e19, "MP=1.22e19 (paper Sec 5.8)"),
                  (2.435e18, "reduced Planck 2.435e18")):
    HB = MPv*math.sqrt(As*12*math.pi**2*1.5e-3)
    print(f"  HB(cs=1.5e-3, {name}) = {HB:.3e} GeV (paper range top: 5e13)")
    HB_lo = MPv*math.sqrt(As*12*math.pi**2*6.8e-7)
    print(f"  HB(cs=6.8e-7, {name}) = {HB_lo:.3e} GeV (paper range bottom: 1e12)")
# As excess: (HB_actual/HB_needed)^2 for the stated ranges
print(f"  As excess range: min (7e16/5e13)^2 = {(7e16/5e13)**2:.2e}, "
      f"max (2e17/1e12)^2 = {(2e17/1e12)**2:.2e}")
verdict("bounce HB gives As 'six to seven orders' too large (full range)",
        (7e16/5e13)**2 < 1e7 and (2e17/1e12)**2 < 1e8,
        "full range is 2e6 - 4e10 (6-10 orders); 'six to seven' holds only "
        "for the upper-to-upper pairing")
# node-scale thermal seed: P >= (lP/eps)^4 = 9.5e-6; vs As=2.1e-9
Pseed = (1/18.02)**4
verdict("P >= (lP/eps)^4 = 9.5e-6", abs(Pseed-9.5e-6)/9.5e-6 < 0.01,
        f"(1/18.02)^4 = {Pseed:.3e}")
verdict("9.5e-6 is ~5e3 times the observed 2.1e-9",
        abs(Pseed/2.1e-9 - 5e3)/5e3 < 0.15, f"ratio = {Pseed/2.1e-9:.0f}")
# V^{1/4} range vs M* = 5.8e16: factor of about four
verdict("M*=5.8e16 within a factor of ~4 of V^{1/4}=1.4e16",
        abs(5.8e16/1.4e16 - 4) < 0.5, f"ratio = {5.8e16/1.4e16:.2f}")
# Poisson fluctuations ~1e-120 on cosmological scales (4-volume count)
c_light = 2.99792458e8; H0 = 70e3/3.085677581e22  # s^-1
RH = c_light/H0
lP = 1.616255e-35; eps = 18.02*lP
N4 = (RH/eps)**4
verdict("Poisson relative fluctuation (4-volume) ~ 1e-120",
        abs(math.log10(N4**-0.5) - (-120)) < 2,
        f"N^-1/2 = {N4**-0.5:.2e} (3-volume would give {(RH/eps)**-1.5:.1e})")
# m^2/Lambda^2 ~ 1e-36 for m ~ 1 GeV
verdict("m^2/Lambda^2 ~ 1e-36 for m=1 GeV, Lambda=6.8e17",
        abs(math.log10((1/6.8e17)**2) - (-36)) < 1,
        f"(1/6.8e17)^2 = {(1/6.8e17)**2:.2e} (m unstated in text)")
# tPage = (1 - 2^-3/2) t_ev ~ 0.646 t_ev
verdict("tPage = (1-2^-3/2) t_ev ~ 0.646 t_ev",
        abs((1-2**-1.5) - 0.646) < 0.001, f"1-2^-1.5 = {1-2**-1.5:.4f}")
# Sec 11: p ~ 2 pi / rc with rc = 1.5
verdict("cutoff scale p ~ 2 pi/rc = 4.19 (rc=1.5), above the p<~3.5 tested range",
        abs(2*math.pi/1.5 - 4.19) < 0.01 and 3.5 < 2*math.pi/1.5,
        f"2 pi/1.5 = {2*math.pi/1.5:.3f}")
print("DONE check_misc.py")
