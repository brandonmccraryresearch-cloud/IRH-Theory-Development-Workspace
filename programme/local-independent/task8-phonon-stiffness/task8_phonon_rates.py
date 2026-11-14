"""Task 8 — phonon (phase-mode) relaxation rates, Model B.

Independent real-space check of the stiffness derivation:
  * Build psi0 (24-mode standing wave, A* from task8_stiffness.py) and a
    phase perturbation eta for a long-wave displacement
    u(x) = U cos(q x1) e_hat, U = 0.01, on a box L = 4 pi, N = 32 per axis.
  * Apply the exact linearised operator H (A6 construction):
        H eta = (r + (q0^2 + nabla^2)^2) eta - 2 psi0 eta + 3 psi0^2 eta
    pseudospectrally (spectral differential part, pointwise products).
  * Energy curvature  dF/V = (1/2) <eta, H eta>  vs the analytic elastic
    prediction  <f_el>  from lambda = mu = 256 A^2  (two routes).
  * Instantaneous energy decay rate of the trial mode (exact identity for
    Model B, dF/dt = -int |grad mu|^2, dF/dt = 2 Gamma dF):
        Gamma = -<|grad mu|^2> / (2 dF/V).
  * Finite-difference check of the H application (A6 §6 style).
Deterministic; no random numbers.
"""
import itertools
import json
import math

import numpy as np

WD = "/home/hatch/workspace/research/irh/co-scientist-tasks-2026-11-10/local-independent/task8-phonon-stiffness"
R = -0.35
U_ = 1.0
V_ = 1.0
Q0SQ = 8.0
PSIBAR = -0.18
ASTAR = 0.07757529633928076
A2 = ASTAR ** 2
LAM = MU = 256 * A2

L = 4 * math.pi
N = 32
UAMP = 0.01

# D4 scaled shell (24 vectors) and 12 +/- pairs
ROOTS = []
for i, j in itertools.combinations(range(4), 2):
    for s1, s2 in itertools.product([1, -1], repeat=2):
        a = [0] * 4
        a[i] = s1
        a[j] = s2
        ROOTS.append(tuple(2 * x for x in a))
PAIRS = [g for g in ROOTS if (g[0] > 0 or (g[0] == 0 and g[1] > 0)
                               or (g[0] == 0 and g[1] == 0 and g[2] > 0)) ]
assert len(ROOTS) == 24 and len(PAIRS) == 12

xs = np.linspace(0, L, N, endpoint=False)
X = np.meshgrid(xs, xs, xs, xs, indexing='ij')
freq = np.fft.fftfreq(N, d=L / N) * 2 * math.pi
KX, KY, KZ, KW = np.meshgrid(freq, freq, freq, freq, indexing='ij')
K2 = KX ** 2 + KY ** 2 + KZ ** 2 + KW ** 2
OMEGA2 = R + (Q0SQ - K2) ** 2   # (r + (q0^2 + nabla^2)^2) in Fourier space

# psi0(x) = psibar + 2 A sum_pairs cos(g.x)
psi0 = np.full((N,) * 4, PSIBAR)
for g in PAIRS:
    psi0 = psi0 + 2 * ASTAR * np.cos(g[0] * X[0] + g[1] * X[1] + g[2] * X[2] + g[3] * X[3])
psi0_hat = np.fft.fftn(psi0)


def mu_of(psi):
    """Chemical potential mu[psi] = (r+(q0^2+nabla^2)^2) psi - psi^2 + psi^3."""
    ph = np.fft.fftn(psi)
    lin = np.fft.ifftn(OMEGA2 * ph).real
    return lin - U_ * psi ** 2 + V_ * psi ** 3


def apply_H(eta):
    eh = np.fft.fftn(eta)
    lin = np.fft.ifftn(OMEGA2 * eh).real
    return lin - 2 * U_ * psi0 * eta + 3 * V_ * psi0 ** 2 * eta


# --- finite-difference validation of apply_H (one case, q=1 longitudinal)
def phase_eta(q, ehat):
    # eta(x) = -2 A sum_pairs (g.u(x)) sin(g.x),  u = UAMP cos(q x1) ehat
    u = [UAMP * np.cos(q * X[0]) * ehat[i] for i in range(4)]
    eta = np.zeros((N,) * 4)
    for g in PAIRS:
        gu = sum(g[i] * u[i] for i in range(4))
        eta = eta - 2 * ASTAR * gu * np.sin(g[0] * X[0] + g[1] * X[1] + g[2] * X[2] + g[3] * X[3])
    return eta


eta_fd = phase_eta(1.0, (1, 0, 0, 0))
Heta = apply_H(eta_fd)
# delta = 1e-3: truncation error is O(delta^2 * eta^3) ~ 1e-13, while roundoff
# scales as eps*||mu[psi0]||/delta (||mu[psi0]|| ~ 11.6, dominated by the
# k=0 mode (r + q0^4) * psibar); verified by a delta sweep in the log:
# relerr 4.2e-9 at 1e-3, 4.5e-8 at 1e-4, 4.4e-6 at 1e-6  (pure 1/delta).
delta = 1e-3
mu_fd = (mu_of(psi0 + delta * eta_fd) - mu_of(psi0 - delta * eta_fd)) / (2 * delta)
# subtract the residual mu[psi0] contribution: mu_of is affine + nonlinear;
# centred difference removes the constant term exactly, leaving H eta.
relerr = np.linalg.norm(mu_fd - Heta) / np.linalg.norm(Heta)
print(f"H finite-difference check (delta=1e-3): rel L2 error = {relerr:.3e}")
assert relerr < 1e-7

def apply_H_grad(eta):
    eh = np.fft.fftn(eta)
    return np.fft.ifftn(OMEGA2 * eh).real


mu0 = mu_of(psi0)

rows = []
for q in (0.5, 1.0, 1.5, 2.0):
    for pol, ehat in (("L", (1, 0, 0, 0)), ("T", (0, 1, 0, 0))):
        eta = phase_eta(q, ehat)
        mu = apply_H(eta)
        dF = 0.5 * float(np.mean(eta * mu))
        dF_grad = 0.5 * float(np.mean(eta * apply_H_grad(eta)))
        dF_nl = dF - dF_grad
        lin = float(np.mean(mu0 * eta))  # first-variation (residual) term
        # analytic elastic prediction for u = UAMP cos(q x1) ehat:
        # L: <f> = 384 A^2 (UAMP q)^2 / 2 ;  T: <f> = 64 A^2 (UAMP q)^2
        if pol == "L":
            dF_an = 192 * A2 * (UAMP * q) ** 2
            dF_grad_an = A2 * UAMP ** 2 * (12 * R + 192 * q ** 2 + 12 * q ** 4)
        else:
            dF_an = 64 * A2 * (UAMP * q) ** 2
            dF_grad_an = A2 * UAMP ** 2 * (12 * R + 64 * q ** 2 + 12 * q ** 4)
        # |grad mu|^2 volume average, spectrally
        muh = np.fft.fftn(mu)
        grad2 = 0.0
        for K in (KX, KY, KZ, KW):
            gcomp = np.fft.ifftn(1j * K * muh).real
            grad2 += float(np.mean(gcomp ** 2))
        gamma = -grad2 / (2 * dF)
        rows.append(dict(q=q, pol=pol, dF=dF, dF_analytic=dF_an,
                         relerr_dF=abs(dF - dF_an) / dF_an,
                         dF_grad=dF_grad, dF_grad_analytic=dF_grad_an,
                         relerr_grad=abs(dF_grad - dF_grad_an) / abs(dF_grad_an),
                         dF_nl=dF_nl, lin=lin,
                         grad_mu_sq=grad2, Gamma=gamma))
        print(f"q={q:.1f} {pol}: dF/V={dF:.6e} analytic={dF_an:.6e} "
              f"relerr={abs(dF-dF_an)/dF_an:.3e} | dF_grad={dF_grad:.6e} "
              f"grad-an={dF_grad_an:.6e} relerr={abs(dF_grad-dF_grad_an)/abs(dF_grad_an):.3e} "
              f"| dF_nl/(A^2U^2)={dF_nl/(A2*UAMP**2):+.4f} lin={lin:.3e} "
              f"| Gamma(trial)={gamma:.6e}")

# q -> 0 extrapolation of the full curvature: fit
#   dF / (A^2 U^2 q^2) = C0 + C2 q^2  on the q <= 1.5 points; C0 is the
#   long-wave elastic coefficient (192 L, 64 T).  Also fit dF_grad alone.
for pol, c0 in (("L", 192.0), ("T", 64.0)):
    sub = [r for r in rows if r["pol"] == pol and r["q"] <= 1.5]
    x = np.array([r["q"] ** 2 for r in sub])
    y = np.array([r["dF"] / (A2 * UAMP ** 2 * r["q"] ** 2) for r in sub])
    slope, inter = np.polyfit(x, y, 1)
    yg = np.array([r["dF_grad"] / (A2 * UAMP ** 2) for r in sub])
    # dF_grad/(A^2U^2) = 12R + C0 q^2 + 12 q^4: fit vs q^2 with q^4 known
    yg2 = yg - 12 * x ** 2
    slope_g, inter_g = np.polyfit(x, yg2, 1)
    print(f"pol {pol}: full-curvature fit C0={inter:.4f} (expect {c0}), "
          f"slope={slope:.4f}; grad-part fit C0={slope_g:.4f}, "
          f"intercept={inter_g:.4f} (expect 12R={12*R:.2f})")
with open(f"{WD}/tables/task8_phonon_rates.csv", "w") as fh:
    fh.write("q,pol,dF_per_vol,dF_analytic,relerr_dF,dF_grad,dF_grad_analytic,"
             "relerr_grad,dF_nl,lin_term,grad_mu_sq,Gamma_trial\n")
    for r in rows:
        fh.write(f"{r['q']},{r['pol']},{r['dF']:.12e},{r['dF_analytic']:.12e},"
                 f"{r['relerr_dF']:.6e},{r['dF_grad']:.12e},{r['dF_grad_analytic']:.12e},"
                 f"{r['relerr_grad']:.6e},{r['dF_nl']:.12e},{r['lin']:.6e},"
                 f"{r['grad_mu_sq']:.12e},{r['Gamma']:.12e}\n")
print("wrote tables/task8_phonon_rates.csv")
print("EXIT 0")
