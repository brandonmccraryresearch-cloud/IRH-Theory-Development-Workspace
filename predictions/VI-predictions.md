# Falsifiable Predictions — Part VI: Test Targets

Each prediction from Part VI of v93.1, reformulated as a test with pass/fail
criteria. These are the empirical handles of the framework — the places where
it can be proven wrong.

## VI.1 Triad phase locking

**Prediction.** For a real field with $u>0$, the cubic term is minimized when
$\phi_1+\phi_2+\phi_3 = 0 \pmod{2\pi}$ on every closed triad — a hard signature
distinguishing a genuine D₄ standing wave from a coincidental superposition of
modes on the right shell.

**Measured.** Order parameter 0.26 against a maximum of 1 — "real but incomplete
locking, consistent with a defected state in a small box."

**Test.** Larger volume should drive this toward unity (→ problem 1.1).
**Fail criterion:** locking saturates well below 1 in the large-volume limit.

## VI.2 The baseline-tension band

**Prediction.** The full 24-mode pattern is the global minimum only for
$\bar\psi$ in a definite band along the order/disorder boundary ($\approx
-0.33 \lesssim \bar\psi \lesssim 0.03$, 11.85% of the scanned plane), **and
only for $q_0$ tuned onto the D₄ shell**. Outside either condition,
lower-symmetry patterns or no pattern result.

**Test.** Map the band under simultaneous detuning and higher-order terms
(→ problem 1.3).
**Fail criterion:** the band vanishes under physically reasonable $w_6$ and
detuning — the tuning requirement becomes effectively measure-zero.

## VI.3 Validity boundary of the non-relativistic limit

**Prediction.** The envelope-limit Schrödinger equation (§III.3) holds to under
1% frequency error for $a_0|\mathbf{k}| \lesssim 0.3$, degrading as tabulated
(1% at 0.3, 11% at 1.0, 133% at zone edge).

**Test.** Direct comparison of exact transcendental dispersion vs. quadratic
approximation — already done; the table *is* the test.
**Fail criterion:** any use of the envelope equation outside its quantified
validity regime without stating the error.

## VI.4 Stability bound

**Prediction.** $\Delta t \le \sqrt{3/2}\,a_0/c$ for any discrete
implementation.

**Test.** Violate it in simulation and watch the instability develop; the bound
is sharp (worst-case mode at $a_0\mathbf{k}=(0,0,\pi,\pi)$-type points, spatial
sum exactly 32).
**Fail criterion:** a stable run above the bound (would indicate an error in
the derivation).

## VI.5 Isotropy to fourth order — a prediction of absence

**Prediction.** No anisotropic quartic Lorentz-violating term arises from
nearest-neighbour D₄ coupling. Anisotropy enters at sixth order or via
next-nearest-neighbour couplings. **This is falsified by any observation of
quartic-order directional dependence attributable to this mechanism.**

**Test.** Observational: Lorentz-violation phenomenology (e.g., SME
coefficients). Theoretical: compute the sixth-order anisotropy explicitly and
the next-nearest-neighbour contributions — the paper states where anisotropy
*first* appears but does not compute its size.
**Fail criterion:** quartic directional dependence from this mechanism.

## VI.6 Defect spectrum

**Prediction.** Dislocation sheets with Burgers vectors in D₄, integer-charged
point solitons, **no line defects**.

**Test.** Classify defect composites (→ problem 1.4); the absence of line
defects is the sharpest sub-prediction.
**Fail criterion:** a stable line defect in the $T^4 \times S^3$
order-parameter space.

## VI.7 Monopoles — predicted, not excluded

**Prediction.** Stable magnetic monopoles exist ($\pi_2(G/H)=\mathbb{Z}$ for
E₆ → ⋯ → SM breaking).

**Test.** This is a prediction *of* the framework, but an undiluted monopole
abundance contradicts observation — so the mandatory companion is the
resolution (→ problem 3.4).
**Fail criterion:** no monopole resolution consistent with observation.
