#!/usr/bin/env python3
"""Authoritative reconciliation of the resonance-maximum count (IRH v93.1 audit item).

Setup (paper's §II.6 simulation grid):
  - periodic box L = 2*pi, 16 points per direction -> x_j = (pi/8) * j, j in {0..15}^4
  - D4 shell scaled to {(+-2,+-2,0,0) and perms}, |k|^2 = 8  ("two pattern periods per direction")
  - pattern P(x) = sum_{k in shell} cos(k . x)

Claim under test: P attains its global max 24 at exactly 32 grid points,
in two families: "corners" (m all even) and "body centres" (m all odd),
where x = (pi/2) * m.  (Manuscript §II.2 scope paragraph + §VI-A.3.)

Also re-checks the verifier's II.2 closed-cell scan (16 corners) for contrast.
"""
import itertools
import numpy as np

# ---- scaled D4 shell, |k|^2 = 8 ----
shell = []
for i, j in itertools.combinations(range(4), 2):
    for si in (1, -1):
        for sj in (1, -1):
            v = [0] * 4
            v[i] = 2 * si
            v[j] = 2 * sj
            shell.append(v)
K = np.array(shell, dtype=float)
assert len(K) == 24 and np.allclose((K ** 2).sum(1), 8)

# ---- 16^4 periodic grid, L = 2*pi ----
n = 16
h = 2 * np.pi / n
g1 = np.arange(n) * h
G = np.array(np.meshgrid(g1, g1, g1, g1, indexing="ij")).reshape(4, -1).T  # 65536 x 4

P = np.cos(G @ K.T).sum(1)
mx = P.max()
tol = 1e-9
am = np.argwhere(P > mx - tol)[:, 0]
print(f"global max P = {mx:.12f} (expect 24)")
print(f"# grid maxima   = {len(am)} (expect 32)")

# ---- classify: x = (pi/2) m  ->  j = 4 m, so m = j/4 must be integral ----
J = np.round(G[am] / h).astype(int)          # integer grid indices 0..15
m, rem = np.divmod(J, 4)
assert np.all(rem == 0), "maxima not on the (pi/2) subgrid!"
par = m % 2
all_even = np.all(par == 0, axis=1)
all_odd = np.all(par == 1, axis=1)
print(f"corner family (m all even): {all_even.sum()}, body-centre family (m all odd): {all_odd.sum()}")
assert bool(np.all(all_even | all_odd)) and all_even.sum() == 16 and all_odd.sum() == 16

# ---- analytic cross-check: maxima <=> m all same parity (proved in notes) ----
# k.x in 2*pi*Z for all shell k  <=>  x=(pi/2)m, all m_i same parity.
def is_max_analytic(j):
    return all(v % 4 == 0 for v in j) and (all((v // 4) % 2 == 0 for v in j)
                                           or all((v // 4) % 2 == 1 for v in j))
expected = {j for j in itertools.product(range(16), repeat=4) if is_max_analytic(j)}
found = {tuple(v) for v in J}
print(f"analytic prediction: {len(expected)}, enumerated: {len(found)}, match: {expected == found}")

# ---- periodicity: pattern translation lattice = (pi/2)*{m : all same parity} ----
# verify P(x + t) == P(x) for a generator, e.g. t = (pi/2)(1,1,1,1) (body-centre step)
t = np.array([np.pi / 2] * 4)
# shift grid indices by 4 mod 16  <=>  x -> x + t (mod L)
shift = np.roll(P.reshape((16,) * 4), shift=4, axis=(0, 1, 2, 3)).ravel()
print(f"max |P(x+t)-P(x)| for body-centre translation: {np.abs(shift - P).max():.2e} (expect ~0)")

# ---- contrast: verifier's II.2 closed-cell scan (unscaled dual shell, T in [0,1]^4) ----
A = np.array([[1, -1, 0, 0], [0, 1, -1, 0], [0, 0, 1, -1], [0, 0, 1, 1]], dtype=float)
dual = []
for i in range(4):
    for sgn in (1, -1):
        v = [0.0] * 4
        v[i] = sgn
        dual.append(v)
for s in itertools.product([1, -1], repeat=4):
    dual.append([0.5 * x for x in s])
Gd = 2 * np.pi * np.array(dual)
g = np.linspace(0, 1, 25)
T = np.array(np.meshgrid(g, g, g, g, indexing="ij")).reshape(4, -1).T
X = T @ A
Psi = np.cos(X @ Gd.T).sum(1)
am2 = np.argwhere(Psi > 24.0 - 1e-6)[:, 0]
t_am = T[am2]
corners = np.all((np.abs(t_am) < 1e-9) | (np.abs(t_am - 1) < 1e-9), axis=1)
print(f"II.2 closed-cell scan: max={Psi.max():.6f}, #argmax={len(am2)}, all corners: {bool(corners.all())}")

print("\nCONCLUSION: 32-count CONFIRMED on the physical 16^4 grid (L=2pi, scaled shell).")
print("The verifier's 16-count is a different grid (closed fundamental cell, unscaled shell);")
print("both are correct in their own setup. Manuscript's corner/body-centre explanation is right.")
