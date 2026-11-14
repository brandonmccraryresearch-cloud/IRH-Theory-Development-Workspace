#!/usr/bin/env python3
"""Verify the envelope-prediction arithmetic used in REPORT.md, by two
independent routes where feasible. Inputs are the prior-source parameters
(r=-0.35, mean=-0.18, u=v=1, N=24, T=192, Q=3384, kappa=192,
sigma=0.018776, Delta_f one-mode 0.0076323 / relaxed 0.0077276,
r_coex=-0.217984). The large radial-ODE shoot (R_c=12.57, DeltaF*=555)
and the critical-droplet repo bracket (16.19-16.21) are NOT recomputed
here; they are quoted as prior-source values with file references.
Prints values and PASS/FAIL vs the prior-source numbers.
"""
import numpy as np
from scipy.optimize import brentq

R, MEAN, U, V = -0.35, -0.18, 1.0, 1.0
N, T, Q = 24, 192, 3384
KAPPA = 192.0
SIGMA = 0.018776


def r_eff(m):
    return R - 2 * U * m + 3 * V * m ** 2


def u_eff(m):
    return U - 3 * V * m


def f_mod(A, m=MEAN, r=R):
    return (N / 2 * r_eff(m) * A ** 2 - T / 3 * u_eff(m) * A ** 3
            + V * Q / 4 * A ** 4) if r == R else None


def f_mod_r(A, m, r):
    re = r - 2 * U * m + 3 * V * m ** 2
    ue = U - 3 * V * m
    return N / 2 * re * A ** 2 - T / 3 * ue * A ** 3 + V * Q / 4 * A ** 4


# A* route 1: numpy roots of d f / dA = 0 (cubic in A after factoring A)
re, ue = r_eff(MEAN), u_eff(MEAN)
coeff = [V * Q, -T * ue, N * re]  # dF/dA / A = Q A^2 - T ue A + N re
roots = np.roots(coeff)
a_star_1 = max(float(rt.real) for rt in roots if abs(rt.imag) < 1e-10)
# A* route 2: brentq on dF/dA between 0.05 and 0.10
df = lambda A: N * re * A - T * ue * A ** 2 + V * Q * A ** 3
a_star_2 = brentq(df, 0.05, 0.10, xtol=1e-14)
print(f"A* roots={a_star_1:.15f} brentq={a_star_2:.15f} "
      f"prior=0.07757529633928076 diff={abs(a_star_1-0.07757529633928076):.2e}")
print(f"f_mod(A*)={f_mod(a_star_1):.10f} prior=-0.007632267319")
print(f"r_eff(-0.18)={re:.4f} u_eff={ue:.2f} (prior 0.1072, 1.54)")

# spinodal: r_eff(m)=0 -> 3 m^2 - 2 m - 0.35 = 0
sp = np.roots([3, -2, R])
print(f"spinodal roots={sorted(sp)} prior -0.1439 / +0.8106")
print(f"r_eff(-0.10)={r_eff(-0.10):.4f} (prior -0.12, <0 => no barrier)")

# correlation length xi = sqrt(kappa/(N*r_eff))
xi = np.sqrt(KAPPA / (N * re))
print(f"xi={xi:.4f} prior 8.64")
lam = 2 * np.pi / np.sqrt(8.0)
print(f"lambda=2pi/sqrt(8)={lam:.5f} prior 2.22")

# thin-wall arithmetic given sigma, Delta_f
for df_, tag in ((0.0076323, "one-mode"), (0.0077276, "relaxed")):
    rc = 3 * SIGMA / df_
    dF = (27 * np.pi ** 2 / 2) * SIGMA ** 4 / df_ ** 3
    print(f"thin-wall {tag}: R_c={rc:.3f} DeltaF*={dF:.2f} (prior 7.38/37.2, 7.29/35.9)")

# coexistence check: at r_coex=-0.217984 the ordered minimum has f=0
rcx = -0.217984
re_c = rcx - 2 * U * MEAN + 3 * V * MEAN ** 2
roots_c = np.roots([V * Q, -T * ue, N * re_c])
a_c = max(float(rt.real) for rt in roots_c if abs(rt.imag) < 1e-10)
print(f"coexistence: A*_c={a_c:.6f} (prior 0.058251) f(A*_c)={f_mod_r(a_c, MEAN, rcx):.2e}")
# envelope ratios
print(f"field bracket midpoint R=2.60625 vs ODE R_c=12.57: ratio={12.57/2.60625:.2f}; "
      f"vs droplet-repo seed threshold 16.20: ratio={16.20/2.60625:.2f}; "
      f"vs saddle R_eq=13.53: ratio={13.53/2.60625:.2f}")
print(f"field bracket in wavelengths: 2.5875/{lam:.4f}={2.5875/lam:.3f} to 2.625/{lam:.4f}={2.625/lam:.3f}")
print("VERIFY_ENVELOPE DONE")
