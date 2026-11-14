#!/usr/bin/env python3
"""Checker script 4: gauge matching / mt bounds / axions (Secs 13.7, 16),
lepton fit (13.9), RG cross-checks (1-loop mu_inf, 1+2-loop alpha_s running).
Tool: conda env python 3.11.16, SymPy 1.14.0, scipy 1.17.1, mpmath.
Exit 0 = ran to completion.
"""
import math
import numpy as np
import sympy as sp
from scipy.integrate import solve_ivp

def verdict(name, ok, detail=""):
    print(f"[{'PASS' if ok else 'FAIL'}] {name} :: {detail}")

print("== Table 16 axion masses: ma = 5.70 ueV * 1e12 / M* (eq. 16.3) ==")
Mstars = {"V1": 1.59e10, "V2": 8.13e10, "V3": 5.45e11, "V4-V7": 9.80e11,
          "V8": 1.37e12, "V9": 1.07e13, "V11": 3.43e14}
quoted = {"V1": 358, "V2": 70.1, "V3": 10.5, "V4-V7": 5.82, "V8": 4.16,
          "V9": 0.53, "V11": 0.017}
for k, M in Mstars.items():
    ma = 5.70e12/M
    # quoted values carry 2-3 significant figures; allow 3% relative tolerance
    verdict(f"ma({k}) = {quoted[k]} ueV", abs(ma-quoted[k])/quoted[k] < 0.03,
            f"5.70e12/{M:.2e} = {ma:.4g} ueV (0.01662 rounds to 0.017 for V11)")
# V13-V16 range 1.6-9.3e15 -> 0.0006-0.0036 ueV
lo, hi = 5.70e12/9.3e15, 5.70e12/1.6e15
verdict("ma(V13-V16) range 0.0006-0.0036 ueV",
        abs(lo-0.0006)/0.0006 < 0.05 and abs(hi-0.0036)/0.0036 < 0.05,
        f"range [{lo:.4g}, {hi:.4g}] ueV")
# selected class (16.5): fa = 5.8e16 -> ma ~ 0.1 neV
ma_sel = 5.70e12/5.8e16
verdict("selected-class ma ~ 0.1 neV", abs(ma_sel*1e3 - 0.098)/0.098 < 0.05,
        f"ma = {ma_sel:.4g} ueV = {ma_sel*1e3:.4f} neV")
# eq. (16.5): 5.70e12/4.6e10 .. 5.70e12/5.906e8
a = 5.70e12/4.6e10; b = 5.70e12/5.906e8
verdict("eq. (16.5) interval 124-9651 ueV", abs(a-124)/124 < 0.01 and
        abs(b-9651)/9651 < 0.01, f"[{a:.1f}, {b:.0f}] ueV")

print("== mt bounds (Prop 9.19, Sec 16.3): margin arithmetic ==")
verdict("mt=172.89 vs measured 172.57+-0.29 is a 1.1 sigma margin",
        abs((172.89-172.57)/0.29 - 1.1) < 0.05,
        f"(172.89-172.57)/0.29 = {(172.89-172.57)/0.29:.3f}")
print("  (info) The 172.89 / 172.41 / 174.31 / 173.0-173.9 GeV bounds themselves "
      "require the 3-loop SM RG + NNLO matching integration (Buttazzo et al.), "
      "whose beta functions and matching formulae are NOT stated in the text; "
      "they are UNVERIFIED from the text as written (see checker.md).")

print("== Eq. (13.6): 1-loop cross-check of mu_inf = 5.906e8 GeV ==")
# inputs (13.7): alpha_em^-1(MZ)=127.95, sin^2 theta_W=0.23122, alpha_s(MZ)=0.1179
aem_inv = 127.95; s2w = 0.23122; als_MZ = 0.1179; MZ = 91.1876
a2_inv = aem_inv*s2w
aY_inv = aem_inv - a2_inv
a1_inv = (3/5)*aY_inv
a3_inv = 1/als_MZ
print(f"  alpha2^-1(MZ)={a2_inv:.4f}, alphaY^-1(MZ)={aY_inv:.4f}, "
      f"alpha1^-1(MZ)={a1_inv:.4f}, alpha3^-1(MZ)={a3_inv:.4f}")
# 1-loop SM: d alpha_i^-1 / d ln mu = -b_i/(2 pi), b = (41/10, -19/6, -7)
def a_inv(mu, a0, b):
    return a0 - b/(2*math.pi)*math.log(mu/MZ)
# solve alphaY^-1(mu) = alpha2^-1(mu) + (5/3) alpha3^-1(mu)
# alphaY^-1 = (5/3) alpha1^-1
from scipy.optimize import brentq
def f_136(lnmu):
    mu = math.exp(lnmu)
    lhs = (5/3)*a_inv(mu, a1_inv, 41/10)
    rhs = a_inv(mu, a2_inv, -19/6) + (5/3)*a_inv(mu, a3_inv, -7)
    return lhs - rhs
lnmu_star = brentq(f_136, math.log(1e7), math.log(1e10))
mu_1loop = math.exp(lnmu_star)
print(f"  1-loop solution of (13.6): mu_inf = {mu_1loop:.3e} GeV "
      f"(paper, 2-loop: 5.906e8 GeV; ratio {mu_1loop/5.906e8:.3f})")
verdict("1-loop (13.6) solution is the same order as 5.906e8 GeV",
        0.5 < mu_1loop/5.906e8 < 2.0,
        "1-loop 6.9e8 vs 2-loop 5.906e8 (17% apart); exact 2-loop value "
        "UNVERIFIED (2-loop coefficients not stated in the text)")

print("== Eq. (13.7)/(13.8) algebra (symbolic) ==")
MP_, kg_, q_, chi_, Mstar_, kA_, K_ = sp.symbols('MP kg q chi Mstar kA K', positive=True)
# (13.7): MP^2 = kg Lambda^2 q^6 prod chi, M* = R^-1, Lambda = q M*
# -> MP^2 = kg M*^2 q^8 prod chi
Lam = q_*Mstar_
expr = kg_*Lam**2*q_**6*chi_
verdict("MP^2 = kg M*^2 q^8 prod chi follows from (13.7) with Lambda = q M*",
        sp.expand(expr - kg_*Mstar_**2*q_**8*chi_) == 0)
# K = kA q^3 (from alpha^-1 = kA q^3 Vx and K = alpha^-1/Vx) -> q = (K/kA)^(1/3)
# M* = MP / sqrt(kg prod chi) * (kA/K)^(4/3)
Mbridge = MP_/sp.sqrt(kg_*chi_) * (kA_/K_)**sp.Rational(4, 3)
check = sp.simplify(Mbridge**2 * kg_ * (K_/kA_)**sp.Rational(8, 3) * chi_ - MP_**2)
verdict("M*_bridge = MP (kA/K)^(4/3)/sqrt(kg prod chi) inverts (13.8)",
        check == 0, f"residual = {check}")
print("  (info) the printed (13.8) in the extracted text is garbled "
      "('M*bridge = p Q A^(4/3)/(kg prod chi K^(4/3))'); the algebra above "
      "is verified from (13.7), but the printed formula cannot be checked "
      "verbatim -- UNVERIFIED as printed.")

print("== alpha_s at the cutoff (Prop 10.2): alpha_s ~ 1/45 at 6.8e17 GeV ==")
# 1-loop with thresholds: nf=5 MZ->mt, nf=6 mt->Lambda; 2-loop via ODE.
mt = 172.57; Lam_cut = 6.8e17
def alpha_s_1loop(mu):
    # alpha^-1(mu) = alpha^-1(MZ) + sum (b0/(2 pi)) ln(mu2/mu1), b0 = 11-2nf/3
    ainv = 1/als_MZ
    lo = MZ
    for hi, nf in ((mt, 5), (mu, 6)):
        if mu <= lo: break
        hh = min(hi, mu)
        b0 = 11 - 2*nf/3
        ainv += b0/(2*math.pi)*math.log(hh/lo)
        lo = hh
    return 1/ainv
a1 = alpha_s_1loop(Lam_cut)
print(f"  1-loop alpha_s(6.8e17) = {a1:.6f} = 1/{1/a1:.2f}")
def rhs(t, y):
    mu = math.exp(t)
    nf = 5 if mu < mt else 6
    b0 = 11 - 2*nf/3; b1 = 102 - 38*nf/3
    a = y[0]
    return [-(b0/(2*math.pi))*a**2 - (b1/(8*math.pi**2))*a**3]
sol = solve_ivp(rhs, (math.log(MZ), math.log(Lam_cut)), [als_MZ],
                rtol=1e-12, atol=1e-14, dense_output=True)
a2 = float(sol.y[0, -1])
print(f"  2-loop alpha_s(6.8e17) = {a2:.6f} = 1/{1/a2:.2f}")
verdict("alpha_s(cutoff) ~ 1/45 from the paper's own alpha_s(MZ)=0.1179",
        abs(1/a1 - 45) < 2 or abs(1/a2 - 45) < 2,
        f"1-loop gives 1/{1/a1:.1f}, 2-loop gives 1/{1/a2:.1f}; "
        f"beta = 6/(4 pi alpha_s) would be {6/(4*math.pi*a2):.2f}, not 21.49")
print("  (info) beta=21.49 DOES follow exactly from alpha_s=1/45 "
      "(see check_anomaly.py); it is the alpha_s VALUE that fails.")

print("== Lepton fit (13.9): kappa2=0.5724, w=0.2429, y unstated ==")
# Y_ij = c_{(i-j) mod 3}; c_k = sum_l exp(-pi k2 (k/3+y+l)^2 + 2 pi i (k/3+y+l) w)
# eigenvalues lambda_n = sum_k c_k omega^{n k}; singular values |lambda_n|.
# observed ratios: m_e/m_tau, m_mu/m_tau (PDG 2024 central values, external inputs)
me, mmu, mtau = 0.51099895, 105.65837, 1776.86  # MeV
r1_obs, r2_obs = me/mtau, mmu/mtau
print(f"  observed s1/s3 = {r1_obs:.6e}, s2/s3 = {r2_obs:.6f}")
import mpmath as mp
mp.mp.dps = 25
k2v, wv = mp.mpf('0.5724'), mp.mpf('0.2429')
omega = mp.e**(2*mp.pi*mp.j/3)
def ratios(y):
    ck = []
    for k in range(3):
        s = mp.mpc(0)
        for l in range(-6, 7):
            x = mp.mpf(k)/3 + y + l
            s += mp.e**(-mp.pi*k2v*x**2 + 2*mp.pi*mp.j*x*wv)
        ck.append(s)
    lam = [sum(ck[k]*omega**(n*k) for k in range(3)) for n in range(3)]
    sv = sorted([abs(z) for z in lam])
    return sv[0]/sv[2], sv[1]/sv[2]
best = None
for iy in range(0, 2001):
    y = mp.mpf(iy)/2000
    r1, r2 = ratios(y)
    err = max(abs(math.log(float(r1)/r1_obs)), abs(math.log(float(r2)/r2_obs)))
    if best is None or err < best[0]:
        best = (err, float(y), float(r1), float(r2))
err, yb, r1b, r2b = best
print(f"  best y over [0,1): y={yb:.4f}, s1/s3={r1b:.6e} (obs {r1_obs:.6e}), "
      f"s2/s3={r2b:.6f} (obs {r2_obs:.6f}); worst log-error = {err:.4f}")
# explicit samples (second look at y-(in)dependence)
for ys in (0.0, 0.13, 0.37, 0.71, 0.99):
    r1s, r2s = ratios(mp.mpf(str(ys)))
    print(f"  y={ys:.2f}: s1/s3={float(r1s):.6e}, s2/s3={float(r2s):.6f}")
good1, good01 = [], []
for iy in range(0, 2001):
    y = mp.mpf(iy)/2000
    r1, r2 = ratios(y)
    e = max(abs(math.log(float(r1)/r1_obs)), abs(math.log(float(r2)/r2_obs)))
    if e < 0.01: good1.append(float(y))
    if e < 0.001: good01.append(float(y))
print(f"  (info) y-interval with worst log-error <1%: "
      f"[{min(good1):.3f}, {max(good1):.3f}] (width {max(good1)-min(good1):.3f})"
      if good1 else "  (info) no y gives <1% error")
print(f"  (info) y-interval with worst log-error <0.1%: "
      f"[{min(good01):.3f}, {max(good01):.3f}] (width {max(good01)-min(good01):.3f})"
      if good01 else "  (info) no y gives <0.1% error")
print("  (info) 2 ratios vs 3 parameters (kappa2, w, y): the fit is "
      "underdetermined even before the missing y is supplied.")
verdict("some y reproduces BOTH observed charged-lepton ratios (kappa2,w as stated)",
        err < 0.01, f"best worst log-error = {err:.4f} at y = {yb}")
print("  (info) the separation y is NOT given numerically anywhere in the text "
      "('at the declared separation'); the fit as stated is therefore UNVERIFIED "
      "as written -- the scan above only tests existence of a y.")

print("== Prop 9.19: cos^2 2beta = 0.031 -> tan beta; D-flat identity ==")
import math as m
cos2b = -m.sqrt(0.031)  # tan beta >= 1 requires cos 2beta < 0
tanb = m.sqrt((1-cos2b)/(1+cos2b))
verdict("cos^2 2beta=0.031 with tan beta>=1 gives tan beta ~ 1.19",
        abs(tanb-1.19) < 0.01, f"tan beta = {tanb:.4f}")
g2, gY = sp.symbols('g2 gY', positive=True)
l1 = (g2**2+gY**2)/4; l2 = l1; l3 = (g2**2-gY**2)/4; l4 = -g2**2/2
verdict("D-flat combination lam3+lam4+sqrt(lam1 lam2) = 0 at M*",
        sp.simplify(l3+l4+sp.sqrt(l1*l2)) == 0)
# 1/mW and Schwinger critical field (Sec 9.7, Sec 9.3)
hbarc_MeV_fm = 197.3269804  # MeV fm
mW_MeV = 80369.0
inv_mW_m = hbarc_MeV_fm/mW_MeV*1e-15
verdict("1/mW ~ 2.5e-18 m", abs(inv_mW_m-2.5e-18)/2.5e-18 < 0.05,
        f"hbar c / mW = {inv_mW_m:.3e} m")
# B_c^W = B_c^e (mW/me)^2; B_c^e = 4.41e9 T
Bc = 4.41e9*(80369.0/0.51099895)**2
verdict("mW^2/e critical field ~ 1e20 T", 0.5e20 < Bc < 2e20,
        f"B_c = {Bc:.3e} T")
# Lambda/mW blocks
ratio = 6.8e17/80.369
verdict("Lambda/mW lies between 2^52 and 2^53 (53 blocks)",
        2**52 < ratio < 2**53, f"ratio = {ratio:.4e}; 2^52={2**52:.3e}, 2^53={2**53:.3e}")
verdict("53 halvings reach <= mW; 52 do not",
        6.8e17/2**53 < 80.369 < 6.8e17/2**52,
        f"after 53: {6.8e17/2**53:.2f} GeV; after 52: {6.8e17/2**52:.2f} GeV")
print("DONE check_matching.py")
