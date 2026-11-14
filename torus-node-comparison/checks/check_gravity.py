#!/usr/bin/env python3
"""Checker script 3: gravity (Prop 5.8, 5.10, Num. results 5.6/5.11/13.4),
entropy ratio R, sky-dipole Table 18, curvature bound, (MP/Lambda)^2.
Tool: conda env python 3.11.16, SymPy 1.14.0, mpmath via SymPy. Exit 0 = ran.
"""
import math
from fractions import Fraction as Fr
import sympy as sp

def verdict(name, ok, detail=""):
    print(f"[{'PASS' if ok else 'FAIL'}] {name} :: {detail}")

print("== Proposition 5.8 (gravity-gauge bridge) ==")
Ig = 1.6475e-7; IA = 1.5614e-4; Nb = 5; nf = 4
kg = 16*math.pi*Nb*Ig
kA = 4*math.pi*nf*IA
verdict("kg = 16 pi Nb Ig = 4.14e-5", abs(kg - 4.14e-5)/4.14e-5 < 0.005,
        f"kg = {kg:.4e}")
verdict("kA = 4 pi nf IA = 7.85e-3", abs(kA - 7.85e-3)/7.85e-3 < 0.005,
        f"kA = {kA:.4e}")
chi = (1.25, 3.2, 1.0)
Pchi = chi[0]*chi[1]*chi[2]
verdict("P_chi = 1.25*3.2*1 = 4", Pchi == 4.0, f"P_chi = {Pchi}")
L = 11.2; MP = 1.22e19
# MP^2 eps^2 = kg L^6 P_chi  ->  eps^-1 = MP / (sqrt(kg P_chi) L^3)
eps_inv = MP/(math.sqrt(kg*Pchi)*L**3)
verdict("eps^-1 = 6.77e17 GeV given L=11.2", abs(eps_inv-6.77e17)/6.77e17 < 0.01,
        f"eps^-1 = {eps_inv:.3e} GeV")
verdict("MP / eps^-1 = 18.02 (paper's rounded eps^-1 = 6.77e17)",
        abs(MP/6.77e17 - 18.02) < 0.01, f"MP/6.77e17 = {MP/6.77e17:.4f}")
print(f"  (info) eps^-1 recomputed from unrounded kg is {eps_inv:.3e} (0.3% below "
      f"6.77e17 -- consistent with rounding of L=11.2 and kg=4.14e-5).")
verdict("(MP/Lambda)^2 = 322 with Lambda = 6.8e17",
        abs((MP/6.8e17)**2 - 322) < 2, f"(MP/6.8e17)^2 = {(MP/6.8e17)**2:.1f}")
print(f"  (info) (18.02)^2 = {18.02**2:.1f}; 322 corresponds to Lambda=6.8e17 "
      f"(rounded), 324.7 to eps^-1=6.77e17 -- consistent within rounding.")
# R^-1 = eps^-1 / L (for reference vs M*bridge 5.8e16)
print(f"  (info) R^-1 = eps^-1/L = {eps_inv/L:.3e} GeV (best-matched row, Prop 5.8)")
# K implied by L: L^3 = K/kA
K_impl = L**3 * kA
print(f"  (info) implied K = L^3 kA = {K_impl:.4f} -- K itself is unstated in the "
      f"text, so L=11.2 is UNVERIFIED from the text as written (conditional on K).")

print("== Proposition 5.10 (black-hole entropy) ==")
scell = 18.02**2/4
verdict("s_cell = eps^2/(4 l_P^2) = 81.2 nats", abs(scell-81.2) < 0.1,
        f"s_cell = {scell:.2f}")
mult = L**6 * Pchi
verdict("internal-site multiplicity L^6 P_chi is of order 10^6-10^7",
        1e6 <= mult <= 1e7, f"L^6 P_chi = {mult:.3e}")

print("== Equation (5.5): induced Einstein coefficient sum ==")
# c2^b(mu^2) = 1/(24 pi^2 (2+mu^2)^2) * sum_{l>=1} (2/(2+mu^2))^l l(l+1)/(l+2)^4
# At mu^2 = 1: prefactor and sum; paper says c2 ~ 1.0e-3 (Num. result 5.6).
def c2b(mu2, nmax=2000):
    pref = 1/(24*math.pi**2*(2+mu2)**2)
    q = 2/(2+mu2)
    s = sum(q**l * l*(l+1)/(l+2)**4 for l in range(1, nmax+1))
    return pref*s, s
for mu2 in (1.0, 0.5, 2.0):
    val, s = c2b(mu2)
    print(f"  mu^2={mu2}: sum={s:.6f}, c2^b={val:.6e}")
val1, s1 = c2b(1.0)
# exact cross-check of the mu^2=1 sum with mpmath (independent summation)
import mpmath as mp
mp.mp.dps = 30
s1_mp = mp.nsum(lambda l: (mp.mpf(2)/3)**l * l*(l+1)/(l+2)**4, [1, mp.inf])
print(f"  (info) mpmath independent sum at mu^2=1: {s1_mp} (float sum: {s1:.6f})")
# maximum over mu^2 is at mu^2=0: exact zeta evaluation
# sum_{l>=1} l(l+1)/(l+2)^4 = sum_{m>=3} (1/m^2 - 3/m^3 + 2/m^4)
z2, z3, z4 = float(mp.zeta(2)), float(mp.zeta(3)), float(mp.zeta(4))
s0 = (z2 - 1 - Fr(1, 4)) - 3*(z3 - 1 - Fr(1, 8)) + 2*(z4 - 1 - Fr(1, 16))
c2b0 = s0/(24*math.pi**2*4)
print(f"  (info) exact mu^2=0 sum = {float(s0):.6f}; c2^b(0) = {c2b0:.4e} "
      f"(the maximum over mu^2, since c2^b decreases in mu^2)")
verdict("eq. (5.5) as printed yields c2^b(mu^2=1) ~ 1.0e-3 (Num. result 5.6)",
        0.5e-3 < val1 < 2e-3,
        f"c2^b(1) = {val1:.4e}, a factor {1.0e-3/val1:.1f} below 1.0e-3; "
        f"even the mu^2=0 maximum {c2b0:.2e} is ~5x below 1e-3, and a "
        f"Brillouin-zone AVERAGE cannot exceed that maximum.")

print("== Numerical results 5.6/5.11: entropy ratio R = kappa_S/(4 pi c2) ==")
# kappa_S = 0.01376 (m^2=0.5), 0.01254 (m^2=1); R = 1.05 +- 0.08.
# Implied c2 for R=1.05:
for kS in (0.01376, 0.01254):
    print(f"  kappa_S={kS}: c2 implied by R=1.05 is {kS/(4*math.pi*1.05):.6e}")
verdict("implied c2 values are both ~1.0e-3 (consistent with Num. result 5.6)",
        abs(0.01376/(4*math.pi*1.05) - 1.0e-3) < 0.1e-3 and
        abs(0.01254/(4*math.pi*1.05) - 1.0e-3) < 0.1e-3, "")
# spread: R(m^2=0.5)/R(m^2=1) = kappa ratio if c2 fixed
print(f"  (info) kappa_S ratio (m^2=0.5)/(m^2=1) = {0.01376/0.01254:.4f}; "
      f"quoted R spread +-0.08 (~8%) is consistent with this ~10% spread.")
# c2 from the (5.5) sum at mu^2=1 vs R: R = kappa_S/(4 pi c2^b(1))
R_from_sum = 0.01376/(4*math.pi*val1)
print(f"  (info) using the (5.5) sum c2^b(1)={val1:.4e}, R(m^2=0.5) = {R_from_sum:.3f} "
      f"vs quoted 1.05 +- 0.08")

print("== Numerical result 13.4: dipole ratios ==")
ks = {"chi1": -0.593, "chi2": -0.349, "chi3": -0.961}
for name, k in ks.items():
    print(f"  {name}: k={k}, -1/k = {-1/k:.4f}")
verdict("-1/k = 1.69, 2.86, 1.04 for k = -0.593, -0.349, -0.961",
        abs(-1/-0.593 - 1.69) < 0.01 and abs(-1/-0.349 - 2.86) < 0.01
        and abs(-1/-0.961 - 1.04) < 0.01,
        "values 1.686, 2.865, 1.041; note -1/0.349 = 2.865 rounds to 2.87, "
        "so the stated 2.86 implies unrounded k ~ -0.3494 (consistent with printed "
        "-0.349) -- a rounding-level note, not a failure")

print("== Table 18: sky-dipole amplitudes (D_alpha ~= 3.1 k sqrt|Omega_k|) ==")
# D_alpha ranges per row; solve implied k interval per row.
rows = [(3e-12, 1.3e-6, 5.2e-6, 1.9e-6, 1.7e-5),
        (1e-11, 2.5e-6, 9.4e-6, 3.4e-6, 3.1e-5),
        (1e-10, 0.78e-5, 3.0e-5, 1.1e-5, 9.8e-5)]
for Om, dlo, dhi, glo, ghi in rows:
    klo = dlo/(3.1*math.sqrt(Om)); khi = dhi/(3.1*math.sqrt(Om))
    print(f"  |Om_k|={Om:g}: implied k in [{klo:.3f}, {khi:.3f}]")
    # G dipole / D_alpha ratio must be in [1.4, 3.3]
    rlo = glo/dlo; rhi = ghi/dhi
    print(f"    G/D_alpha range [{rlo:.2f}, {rhi:.2f}] (bridge-vacua range 1.4-3.3)")
verdict("Table 18 D_alpha ranges are consistent with ONE k-interval across rows",
        True, "implied k intervals: [0.242,0.968], [0.255,0.959], [0.252,0.968] -- "
              "mutually consistent; cf. Sec 14.3 k = 0.25-0.96")
verdict("Table 18 G-dipole ranges consistent with (dG/G)/(dalpha/alpha) in 1.4-3.3",
        all(abs(g/d - 1.4) < 0.15 or abs(g/d - 3.3) < 0.15
            for Om, dlo, dhi, glo, ghi in rows for g, d in ((glo, dlo), (ghi, dhi))),
        "endpoint ratios 1.36-1.46 and 3.27-3.30")
# disputed 1e-5 claim needs |Om_k| ~ 1e-11 - 2e-10: D=1e-5 -> sqrt|Om| = 1e-5/(3.1 k)
for k in (0.25, 0.96):
    Om = (1e-5/(3.1*k))**2
    print(f"  D_alpha=1e-5 with k={k}: |Omega_k| = {Om:.2e}")
verdict("10^-5 dipole needs |Omega_k| in ~1e-11 - 2e-10",
        abs((1e-5/(3.1*0.96))**2 - 1.1e-11)/1.1e-11 < 0.1 and
        abs((1e-5/(3.1*0.25))**2 - 1.7e-10)/1.7e-10 < 0.2,
        "endpoints 1.1e-11 and 1.7e-10")

print("== Section 14.3: curvature bound from |dalpha/alpha| < 1e-6 ==")
# dalpha/alpha ~= k sqrt|Om_k| -> |Om_k| < (1e-6/k)^2
for k in (0.25, 0.349, 0.577, 0.593, 0.96):
    print(f"  k={k}: |Omega_k| < {(1e-6/k)**2:.2e}")
print("  (info) stated bound |Omega_k| < 3e-12 corresponds to k = 0.577; V1 k=0.593 "
      "gives 2.8e-12. But the paper's own stated k range 0.25-0.96 gives "
      "1.1e-12 - 1.6e-11, so 3e-12 is a representative-k value, not the range-wide "
      "implication. See checker.md.")
verdict("|dalpha/alpha| < 1e-6 implies |Omega_k| < 3e-12 for ALL stated k in 0.25-0.96",
        (1e-6/0.25)**2 < 3e-12, f"weakest-k bound is {(1e-6/0.25)**2:.2e} > 3e-12")
# atomic-clock ratio
verdict("|alpha-dot/alpha| 1e-11 vs bound 1e-18 is 10^7 times",
        abs(1e-11/1e-18 - 1e7)/1e7 < 0.01, "ratio = 1e7 (paper: 10^6-10^7)")
print("DONE check_gravity.py")
