# Task 4 — Critical droplet and nucleation threshold

**CLAIM:** At the operating point $(\bar{\psi}, r) = (-0.18, -0.35)$ the ordered
branch sits beside a linearly stable uniform state, so reaching it needs
nucleation — but the critical droplet is LARGE and thick-walled: the exact
amplitude-equation (radial-ODE) critical radius is $R_{c} = 12.57$ with
barrier $\DeltaF* = 555$, while the thin-wall estimate $(R_{c} = 7.38, \DeltaF* = 37.2)$
fails because the correlation length $\xi = 8.64$ exceeds the thin-wall
radius. In the finite periodic $\pi$-box used for the 4D Model B runs, the
infinite-volume critical radius does not fit, and the observed threshold
is instead in amplitude/size within the box: only the smallest, weakest
seed (R = 0.6, A = A*) decays; all seven other seeds grow to the full
ordered state within 250–500 steps. The manuscript's §II.9 statement
that the barrier vanishes near $\bar{\psi} \approx -0.10$ is confirmed (exact spinodal
$\bar{\psi} = -0.1439$; $r_{eff} = -0.12 < 0$ at $\bar{\psi} = -0.10)$.

**STATUS:** VERIFIED for the amplitude-equation routes $(\kappa$, thin-wall,
radial ODE) and for the finite-box droplet runs. The thin-wall numbers
are reported as what they are — an approximation that fails here — not as
the answer. The infinite-volume $R_{c}$ and the box threshold are different
quantities and are not to be confused.

## 1. Gradient coefficient (route A, verified)

For a slowly varying amplitude A(x) on the D4 pattern, the quadratic
energy density from the Swift–Hohenberg operator is

$12\cdotr\cdot\langleA^{2}\rangle + 96\cdot\langle$|$\nablaA$|${}^{2}\rangle + 12\cdot\langleA\nabla^{4}A\rangle + \dots$,

i.e. $\kappa = 192$ in the $(\kappa/2)$|$\nablaA$|${}^{2}$ convention (the factor $96 = 2\cdot\Sigma_{g}(g\cdot\hat{n})^{2}$
with $\Sigma_{g}(g\cdot\hat{n})^{2} = 48$|$\nablaA$|${}^{2}$ over the 24 roots). Verified by exact FFT
energy of a modulated pattern $(32^{4}$ grid, $L = 2\pi$, modulation k = 1,
$\varepsilon = 0.1)$: exact excess $F/V = -0.00411359$ vs amplitude-equation prediction
$-0.00411376 ($local $-0.007363$, gradient +0.002889, $\nabla^{4} +0.000361)$,
**relative deviation 4.2e-05**. This is my derivation, not the
manuscript's — and it is now checked against the exact 4D FFT energy.

## 2. Thin-wall estimate (route B)

Coexistence at $\bar{\psi} = -0.18$: $r_{coex} = **-0.217984** ($found by brentq on
F at the large stationary root; $F_{min}$ is flat above coexistence so
brentq on $F_{min}$ fails — see §6), with A*_c = 0.058251. Surface tension
$\sigma = \int_{0}$^{A*_c} $\sqrt{(2\kappaV(A))}$ dA = **0.018776** (scipy quad; Simpson on a
20,001-point grid gives the identical 0.018776). Then $R_{c} = 3\sigma/\Deltaf$,
$\DeltaF* = (27\pi^{2}/2)\sigma^{4}/\Deltaf^{3} (4D$: volume $(\pi^{2}/2)R^{4}$, area $2\pi^{2}R^{3})$:

| $\Deltaf$ | $R_{c}$ | $\DeltaF$* |
|---|---|---|
| 0.0076323 (one-mode) | 7.38 | 37.2 |
| 0.0077276 (relaxed) | 7.29 | 35.9 |

## 3. Radial-ODE critical droplet (route C, exact within the amplitude equation)

Shooting $\kappa(A'' + 3A'/r) = V'(A)$, $A'(0) = 0$, $A(\infty) = 0$, with $V = F_{mod}$ at
the operating point. The separatrix is bracketed by bisection on A(0):
undershoot (A stays $\geq 0$, turning back up) vs overshoot (A crosses zero
and dives); the critical value is $A(0)_{c} = **0.056605** ($bracket width
< 1e-10). Profile: A(30) = 4.37e-3, decaying Bessel-like tail
(A(40) = 9.45e-4, A(50) = 1.95e-4, matching the $K_{1}(0.116r)/r$ prediction
to ~5%). Results:

- $R_{c} (A = A*/2) = **12.57$**
- $\DeltaF* = **555.2** ($trapezoid on solver steps; 554.71 by Simpson on the
  dense-output interpolant to r = 55 — agreement 0.1%)
- The droplet core (A(0) = 0.0566) never reaches the bulk amplitude
  (A* = 0.0776): thick-walled, not thin-walled.

**Why thin-wall fails here:** the correlation length
$\xi = \sqrt{(\kappa/(n\cdotr_{eff}))} = \sqrt{(192/(24\cdot0.1072))} = **8.64$** exceeds the
thin-wall $R_{c} = 7.38$. The wall is as wide as the droplet, so the
thin-wall separation of volume gain and surface cost breaks down; the
exact barrier is ~$15\times$ the thin-wall value. The thin-wall numbers are
retained in the table above as the (failed) approximation, not the answer.

## 4. Full 4D Model B droplet runs (route D)

Seeds $R \in {0.6, 0.8, 1.0, 1.2} \times A \in {A*, 1.5A*}$, 6000 steps each,
$L = \pi$, $q0^{2} = 8.0$, $\bar{\psi} = -0.18$. Growth = final D4 > 0.9 and rms > 0.3;
decay = D4 < 0.2 and rms < 0.1.

| R | A = A* | A = 1.5A* |
|---|---|---|
| 0.6 | **decay** (rms $\to 0$, Fexc $\to 0$; rms < 0.01 by step 1000) | **growth** (D4 > 0.9 by step 500) |
| 0.8 | **growth** (D4 > 0.9 by step 500) | **growth** (by step 250) |
| 1.0 | **growth** (by step 250) | **growth** (by step 250) |
| 1.2 | **growth** (by step 250) | **growth** (by step 250) |

Every growing run reaches the full ordered state (D4 = 1.000,
rms = 0.381, Fexc = $-0.007728)$. Growth is fast once nucleated
(250–500 steps to D4 > 0.9). Full time series:
`tables/task4_droplet_runs.json`.

**Scale mismatch (the key interpretive point):** the ODE critical
radius $R_{c} = 12.57$ is far larger than the box half-size (L/2 = 1.57),
and the pattern wavelength is $\lambda = 2\pi/\sqrt{8} = 2.22$ — a droplet of
$R \leq 1.2$ contains less than one wavelength and is really a localised
amplitude bump, not a droplet of ordered phase with a sharp wall. The
box runs therefore do NOT measure the infinite-volume $R_{c}$; they map the
finite-box nucleation threshold, which is set by periodic-image
interactions (a droplet's images are only $L = \pi$ apart). The observed
threshold (between R = 0.6 and 0.8 at A*, below R = 0.6 at 1.5A*) is a
property of the $\pi$-box, and the ODE value is the infinite-volume answer.
Neither invalidates the other; conflating them would.

## 5. Manuscript §II.9 check (barrier vanishes near $\bar{\psi} \approx -0.10)$

$r_{eff}(\bar{\psi}) = -0.35 - 2\bar{\psi} + 3\bar{\psi}^{2}$ vanishes at $\bar{\psi} = **-0.1439** ($exact) and
+0.8106. At $\bar{\psi} = -0.10$, $r_{eff} = **-0.12 < 0$**: the uniform state is
linearly unstable, the barrier-top stationary point has moved to
negative amplitude $(A_{small} = -0.0101$, unphysical), and there is no
barrier — confirmed. The manuscript's "$\approx -0.10$" is a rounded statement
of the spinodal at $-0.1439$; at the operating point $\bar{\psi} = -0.18$ the
barrier is small but nonzero (barrier top $A_{small} = 0.0098$,
F = +0.000039).

## 6. Checks

| check | verdict |
|---|---|
| $\kappa = 192$: exact FFT energy vs amplitude-equation prediction, rel dev 0.0000 | PASS |
| Coexistence $r_{coex} = -0.217984$ matches Task 3's boundary value $-0.2180 ($independent route) | PASS |
| $\sigma$ by scipy quad = Simpson on 20,001-point grid (0.018776 both) | PASS |
| ODE $\DeltaF$* by trapezoid (555.2) = Simpson on dense output (554.71) | PASS |
| ODE profile tail matches $K_{1}(0.116r)/r$ to ~5% | PASS |
| §II.9: spinodal $\bar{\psi} = -0.1439$; $r_{eff}(-0.10) = -0.12 < 0$, no barrier | PASS |
| Droplet runs: 7/8 grow to the full ordered state; 1 decays to uniform; all finite (no NaN) with the fixed stepper | PASS |
| Seeded full pattern re-verified with the fixed stepper (6000 steps: D4 = 1.0000, rms = 0.3806, Fexc = $-0.007728)$ | PASS |
| check_model.py re-run after the stepper fix: ALL CHECKS PASSED, exit 0 | PASS |

**Withdrawal / demotion note (bugs found during checking, all fixed in
the delivered code):**
(i) The first thin-wall run returned $r_{coex} = 0.1$, $\sigma = 0$, $R_{c} = 0$:
brentq on $F_{min}$ returns the bracket endpoint because $F_{min}$ is flat
(= 0) above coexistence. Fixed by brentq on F at the large stationary
root (smooth through coexistence); the same fix was applied to Task 3's
boundaries. (ii) The first shooting bracket misclassified the
subcritical side as "trapped at the barrier-top amplitude $A_{small}$":
subcritical profiles in fact decay toward 0 and turn back up (the
growing Bessel mode). The discriminator is now the sign of A at large r
(crosses zero = overshoot, stays $\geq 0$ = undershoot). (iii) **Model B
stepper, Hermitian-symmetry artifact (found via the droplet runs):**
the first droplet run (R = 0.6, A*) reached NaN by step 6000. Root
cause, diagnosed exactly: the semi-implicit update evaluates the
nonlinearity on the real part only, so the anti-Hermitian (non-real)
component of ph receives no nonlinear stabilisation and grows at the
bare shell rate $\times1.0142$/step from a roundoff seed (the droplet seed
itself carries herm_err 2.4e-13; by step 2500 the anti-Hermitian shell
modes reach ~128 while the real field decays cleanly, then overflow).
Fix, now in `d4model.ModelB.step`: enforce Hermitian symmetry every
step (reverse-conjugate average, exact index map). After the fix the
droplet decays cleanly to uniform (rms 4e-12 at step 6000, herm_err
exactly 0) and the seeded pattern re-verifies identically. The original
NaN run is discarded, not reported as a result. (iv) The first Task 5
launch crashed on a scaled-vs-unscaled label confusion (see Task 5
report); no Task 4 run was affected.

## 7. Rival / failure mode

The main rival is the amplitude-equation truncation itself: the ODE and
thin-wall routes use the one-mode $F_{mod}$ and the envelope gradient
coefficient, ignoring higher harmonics and the relaxed (fully nonlinear)
free energy (which is 1.2% lower at the operating point). A full 4D
critical-droplet computation (shooting the PDE, not the amplitude
equation) would shift $R_{c}$ and $\DeltaF$* by an amount of that order — it would
not change the thick-wall conclusion $(\xi > R_{c})$ or the scale mismatch
with the box. A second failure mode: the box runs' threshold depends on
L (periodic images); a larger box would move the observed threshold
toward the ODE value, but a box containing $R_{c} = 12.57 (L$ ≳ 30) is
beyond the local $16^{4}$ grid and was not attempted (costed, not run — see
§8).

## 8. Evidence that would change the answer / costed follow-up

- A full-PDE critical droplet (beyond the amplitude equation) would
  refine $R_{c} = 12.57 / \DeltaF* = 555$ by ~1–10%; the thick-wall character
  would survive.
- A larger-box droplet run (e.g. $L = 2\pi$, N = 32) would test whether the
  box threshold moves toward the ODE value. Costed, not run: $a 32^{4}$ grid
  is $16\times$ the points of $16^{4}$; at the measured ~15 ms/step $(16^{4})$, a 6000-step
  run is ~25 min locally per seed on this machine, and the threshold
  search needs several seeds — this is a GCP-scale job, not a local one,
  and no GCP spend was authorised for it.
- If a droplet run in a bigger box grew at R well below 12.57, the ODE
  $R_{c} ($or the amplitude equation itself) would need re-examination.

## 9. HLRE grades (per narrow claim; worst-of shown)

| claim | grade | basis |
|---|---|---|
| $\kappa = 192 ($gradient coefficient) | B | derived from the SH operator + exact-FFT verification to 4 decimals; derivation is mine, not the manuscript's |
| Coexistence $r_{coex} = -0.217984$, A*_c = 0.058251 | B | exact root-finding; cross-checked vs Task 3 |
| $\sigma = 0.018776$ | B | two independent quadratures agree exactly |
| Thin-wall $R_{c} = 7.38$, $\DeltaF* = 37.2$ | C | the approximation is shown to fail here $(\xi > R_{c})$; reported as the failed approximation |
| ODE $R_{c} = 12.57$, $\DeltaF* = 555$ | B | exact within the amplitude equation; two integration routes agree to 0.1%; truncation-limited |
| §II.9 barrier vanishes (spinodal $-0.1439)$ | B | exact $r_{eff}$ computation + stationary-point check |
| Box threshold: only R = 0.6/A* decays, rest grow | B | direct Model B runs; finite-box result, stated as such |
| Infinite-volume $R_{c}$ vs box threshold distinguished | B | scale argument $(R_{c} = 12.57$ vs L/2 = 1.57, $\lambda = 2.22)$ |

## 10. Deliverables

- Figure: `figures/task4_droplet.png` (ODE profile + Landau potential)
- Tables: `tables/task4_thinwall.json`,
  `tables/task4_ode_profile.npz`, `tables/task4_droplet_runs.json`
- Code: `task4_thinwall.py`, `task4_droplet_runs.py` (uses shared
  `d4model.py`, including the Hermitian-symmetry fix in `ModelB.step`)

## 11. Assumption / parameter / choice ledger

- Operating point $\bar{\psi} = -0.18$, $r = -0.35$, u = v = 1, $q0^{2} = 8.0$, A* = 0.0776
  — from the manuscript / repo verification code.
- $\kappa = 192$ derived (not a manuscript parameter) and verified (§1).
- $\Deltaf$: one-mode 0.0076323 and relaxed 0.0077276 (sim6 value), both shown.
- Droplet seeds: tanh envelope, sharpness 4.0 (width 0.25); radii in box
  units $(L = \pi)$; 6000 steps, dt = 0.005.
- The ODE route assumes the amplitude equation (envelope) holds; the
  thin-wall route additionally assumes $\xi \ll R_{c} ($shown false here).
