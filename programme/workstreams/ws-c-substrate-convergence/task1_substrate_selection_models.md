# Task 1 — Formalize Substrate Selection Models

**Workstream C, Co-scientist task programme, 2026-11-10.**
**Skills:** truth-seeking-frontier $v5 \cdot$ cross-domain-discovery v2.0.$0 \cdot$ hlre-v5-1.
All three are DESIGN CLAIMS, ungraded — never evidence of reliability.
**Tier:** Standard. **Track:** E (cap C), except C1.4 (Track F, cap F3).
**Independence ceiling:** I1 (single tool family — my own simulations in the local
conda env; exact checks cross-verified with a second tool, SymPy + python-flint).
**Nothing in this report is incorporated into the repo or the manuscript.**

## CLAIM + STATUS

**CLAIM.** The static-$D_{4}$ account (postulated lattice, v92 ontology) and the
dynamically-selected-$D_{4}$ account (v93.1 tension–relaxation nodal pattern) can be
formalized as rival substrate-selection models, simulated under shared conditions,
and their interference-pattern predictions diverge exactly outside a falsifiable
boundary: the static account predicts the full 24-mode $D_{4}$ pattern for every mean
field $\bar{\psi}$ and every tuning, while the dynamic account predicts it only inside the
band where the 24-mode pattern is the global free-energy minimum, with the shell
tuned and triad coupling on and the initial condition inside the full-pattern
basin. Outside that boundary the dynamic account predicts sub-patterns (6-, 2-,
8-mode) or disorder, and the static account is wrong.

**STATUS: CONFIRMED as stated for the measured slice $(r = -0.35, q_{0}^{2} = 8.0$,
N = 16, $L = \pi)$, with the band edges measured, not assumed — EXCEPT C1.2,
which is FALSIFIED as registered (see below).**
Three qualifications carry the full weight of the result and must not be dropped
when the claim is quoted:

1. **C1.2 is falsified as written.** The register's C1.2 says the dynamic
   account predicts the full 24-mode pattern inside the band with $q_{0}$ tuned and
   triads active; its falsifier is "a noise quench inside the band failing to
   [reach 24/24]". Q2 is exactly that: a noise quench at $\bar{\psi}_{0} = -0.18 ($inside
   the quoted band), $q_{0}^{2} = 8.0$, triads on, reaching 6/24, not 24/24. The
   physics behind the falsification: the damped-wave quench does not conserve
   the mean — it drifts to $\bar{\psi} \approx +0.0025$, *outside* the measured band, where
   the 6-mode is the global minimum. The basin-qualified version (the 24-mode
   is the global minimum and the attractor inside the band, reached from
   seeded/basin initial conditions) is CONFIRMED by A2 + the Landau curves
   and is carried by C1.3, which already contains the basin qualifier. C1.2
   as registered conflates "the pattern is the attractor" with "the pattern
   is reached from noise"; the two are different claims, and only the first
   holds.
2. The noise quench **never reaches the full 24-mode pattern in this setup**
   (5 seeds: 6-mode $\times3, 2$-mode, 8-mode). The v93.1 ontology change dissolves
   the old circularity objection $(D_{4}$ is no longer postulated), but dynamical
   selection of the *full* pattern from noise is **not** demonstrated in the
   $L = \pi$ setup — it needs a seeded or basin initial condition. The manuscript's
   fair-test setup (sim7, competitor shell at equal linear penalty) is a
   different competition (between shells) and does show 77–84% direct-quench
   $D_{4}$ selection; the two results are consistent, not contradictory.
3. The measured 24-mode global-minimum band at $r = -0.35$ is
   **$\bar{\psi} \in (-0.235, -0.125)$**, narrower than the manuscript's quoted
   $(-0.33, +0.03)$, which is the union over quench depths in the full
   $(\bar{\psi}, r)$ phase diagram. My slice is consistent with the manuscript's
   explicit statement that the 6-mode hexagonal sub-pattern beats the
   24-mode at $\bar{\psi} = 0$ at every quench depth tested; the quoted +0.03 edge
   is **UNVERIFIED** against my slice and is referred to ws-a's
   stability-band task (full phase-diagram recomputation). This is an open
   discrepancy, not a refutation.

## 1. Formalization (cross-domain-discovery S1–S7)

Full protocol notes: `formalization_notes.md`. Summary:

- **S1 (BPMF facets).** Four accounts faceted: A1 static $D_{4} ($imposed lattice);
  A2 dynamic $D_{4} ($tension–relaxation nodal pattern); A3 equilibrium Landau
  (one-mode free-energy minimization over candidate shells); A4 particle LJ
  (Hoy [40] molecular dynamics, manuscript-reported). Shared invariant: the
  Landau functional $F[\psi]$ and the shell combinatorics (N, T, $Q) \to S = \tau^{2}/q_{4}$.
- **S2 (olog).** Text olog with boxes (field $\psi$, functional F, shell, triads,
  S-value, pattern) and arrows; path equivalence
  (field$\to$shell$\to$triads$\toS) \simeq ($field$\to$functional$\toS)$ holds for A2/A3. In the
  static account A1, "a reciprocal shell" is a PRIMITIVE with no incoming
  arrow — the missing mechanism, formalized as a dangling box. That is what
  the static account cannot explain.
- **S3 (invariance alignment).** The accounts share the Landau functional F
  but do **not** reduce to the same dynamics — that non-reduction IS the
  divergence. Functor to 3D BCC preserves the diagrams.
- **S4 (Bartha articulation, $3D\to4D S$-criterion transfer): SPLIT verdict.**
  Combinatorial selection transfer PASSES (no critical feature in the Negative
  Analogy: the S-criterion depends only on (N, T, Q), which are computed
  identically in 3D and 4D). Near-melting equilibrium scope transfer FAILS —
  correctly, because the manuscript claims *dynamical* selection, not
  near-melting equilibrium. The failure is a scope restriction, not a defect.
- **S4 (transportability audit, LJ$\to$field): NOT transport.** The LJ particle
  system carries an irreducible sC-component (particle identity, pair
  potential); it is independent corroboration only, not a transport of the
  field mechanism.
- **S5 (blending):** rational reconstruction, grade D by construction.
- **S6 (tournament):** NOT RUN as LLM Elo; replaced by the simulation probe
  grid below (a measurement, not a vote).
- **S7 (verification):** Z3 checks in `code/exact_checks.py` (PASS); Lean
  re-verification NOT RUN (no new Lean work; repo's 8 modules cited to
  manuscript §VI-A.2 / FINAL_AUDIT lake-build exit 0 as reported).

## 2. Derivation (each step checkable)

**Step 1 — Shell combinatorics (exact).** $D_{4}$ shell: 24 roots $\pme_{i}\pme_{j}$.
Exhaustive enumeration: N = 24, T = 192 ordered zero-sum triples,
Q = 3384 ordered zero-sum quadruples. $\tau = T/N^{3/2} = 192/24^{3/2} = 4/\sqrt{6}$,
$q_{4} = Q/N^{2} = 3384/576 = 47/8$, $S = \tau^{2}/q_{4} = (8/3)/(47/8) = 64/141 \approx 0.453901$.
Competitors: $A_{4}* (20, 120, 1860)$, $S = 12/31 \approx 0.387097$; BCC (12, 48, 540),
$S = 16/45 \approx 0.355556$. Margin $S_{D}_{4}/S_{A}_{4}* = 496/423$, i.e. $73/423 \approx 17.26$%.
All verified by SymPy 1.14.0 + python-flint 0.8.0 + Z3 4.15.4
(`code/exact_checks.py`, 29 checks, exit 0).

**Step 2 — One-mode free energy (corrected coefficient).** With the manuscript
§II.7–II.8 form, the quadratic coefficient is **N/2, not $N^{2}$** — the pdftotext
rendering "N2" is the fraction N/2 (confirmed by §II.3's F(B) form and by the
stationary values reproducing only with N/2; the $N^{2}$ form gives a negative
discriminant and no stationary point). Corrected form:
$F_{mod} = (N/2)(r_{shell} - 2u\bar{\psi} + 3v\bar{\psi}^{2})A^{2} - (T/3)(u - 3v\bar{\psi})A^{3} + ($vQ/$4)A^{4}$,
$r_{shell} = r + (q_{0}^{2}-8)^{2}$, $r_{eff} = r - 2u\bar{\psi} + 3v\bar{\psi}^{2}$, $u_{eff} = u - 3v\bar{\psi}$.
Stationarity: vQA${}^{2} -$ Tu_effA + Nr_eff = 0. Ordered branch exists iff
(Tu_eff$)^{2} \geq 4$vQNr_eff. At $r = -0.35$, $\bar{\psi} = -0.18$, $q_{0}^{2} = 8.0$:
A* = 0.0775753, $F/V = -0.0076323 ($ansatz). Relaxed field: $-0.0077276$
(1.24% harmonic lowering). At $\bar{\psi} = -0.18$ the branch exists iff
$r_{eff} \leq 0.2691$, i.e. |$q_{0}^{2}-8$| $\leq 0.4024$. At $q_{0}^{2} = 7.5 ($detuning 0.5, past
the edge$): r_{shell} = -0.10, r_{eff} = 0.3572$, **no ordered branch**.

**Step 3 — Static account (most charitable formalization, A4).**
$\Psi(x) = \bar{\psi} + A*\Sigma_{g} \cos(g\cdotx)$ over the $24 D_{4}$ roots, amplitude from the
one-mode ansatz (v92 had no amplitude equation; the ansatz value is the
charitable choice). Predictions: 24/24 modes, lock = 1.0, Fexc from the
ansatz, for **every** $\bar{\psi}$ and every $q_{0}^{2}$. No mechanism, no band, no
initial-condition dependence.

**Step 4 — Dynamic account.** Two dynamics under shared conditions
(N = 16, $L = \pi, r = -0.35, u = v = 1, q_{0}^{2} = 8.0$ unless noted):
(a) damped-wave RK4 quench from noise (sim6 test_quench, generalized),
T = 50, dt = 0.02; (b) Model B semi-implicit attractor from a seeded
24-mode pattern (sim6 test_attractor, generalized), T = 7.5, dt = 0.005,
with Hermitian projection (see §5). Shared analyzer (verbatim port of
sim6 analyze()).

**Step 5 — Model B instability diagnosis and fix (extends the manuscript).**
The shipped sim6 Model B run blows up at t = 27.5 (NaN). Diagnosis: the
physical field is stationary through t = 18 (rms = 0.380565,
max|$\psi$| = 1.689597 constant — exactly the manuscript §VI-A.4 claim); the
blow-up is the **unphysical anti-Hermitian sector**: exact dynamics preserves
Hermiticity, but the semi-implicit update amplifies anti-Hermitian roundoff
by 1/den > 1 at the shell (den = 1 + dt$\cdotK2\cdot\omega^{2} = 0.986)$, growth factor
1.0142/step — measured $\langleA\rangle$ growth ratios 4.09–4.10 per 100 steps =
$1.0142^{100}$ exactly. The real-part dynamics is decoupled (the nonlinearity
sees only Re(ifftn(ph))); only the |ph|-based diagnostic $\langleA\rangle$ is
contaminated. **Fix** (in `code/irh_models.py`, hermitian=True default):
per-step projection ph $\leftarrow$ fftn(ifftn(ph).real) — an exact no-op in exact
arithmetic (fftn of a real field is Hermitian by construction; measured
no-op error 3.8e-16). With projection the attractor is stable through
$t = 30 (\langleA\rangle = 0.077682, \bar{\psi} = -0.180000, D_{4} = 1.0000, 24/24$,
rms = 0.380565, Fexc = $-0.007728)$. The shipped sim6 file was NOT modified.
Figure: `figures/fig4_instability.png`. Data: `results/instability_series.csv`.

## 3. Results

### 3.1 Shared-condition probe grid (N = 16, $L = \pi, r = -0.35, u = v = 1)$

Full table: `results/task1_probe_results.csv`. Quenches are RK4 damped-wave,
T = 50, dt = 0.02; attractors are Model B, T = 7.5, dt = 0.005.

| tag | model | $\bar{\psi}_{0}$ | $q_{0}^{2}$ | u | $\bar{\psi}$_final | $\langleA\rangle$ | modes | rms | Fexc |
|-----|-------|------|-----|---|----------|------|-------|------|------|
| Q1 | wave quench | 0.00 | 8.0 | 1 | +0.00253 | 0.07371 | 6/24 | 0.5581 | $-0.040339$ |
| Q2 | wave quench | $-0.18$ | 8.0 | 1 | +0.00253 | 0.07412 | 6/24 | 0.5574 | $-0.040265$ |
| Q3 | wave quench | 0.00 | 8.0 | 0 | +0.00012 | 0.07369 | 12/24 | 0.4282 | $-0.01618$ |
| Q4 | wave quench | $-0.18$ | 7.5 | 1 | +0.00001 | 0.00349 | 14* | 0.0184 | $-0.000017$ |
| Q5 | wave quench | $-0.30$ | 8.0 | 1 | +0.00251 | 0.0748 | 6/24 | 0.5563 | $-0.040138$ |
| Q6 | wave quench | +0.10 | 8.0 | 1 | +0.00253 | 0.0738 | 6/24 | 0.5579 | $-0.040323$ |
| Q7 | wave quench | $-0.18$ | 8.0 | 1, seed 2 | +0.00263 | 0.06777 | 6/24 | 0.5667 | $-0.041236$ |
| A1 | Model B seeded 24 | $-0.30$ | 8.0 | 1 | $-0.30$ | 0.0 | — | 0.0 | $-0.0$ |
| A2 | Model B seeded 24 | $-0.18$ | 8.0 | 1 | $-0.18$ | 0.07768 | 24/24 | 0.3806 | $-0.007728$ |
| A3 | Model B seeded 24 | 0.00 | 8.0 | 1 | 0.00 | 0.08585 | 24/24 | 0.4206 | $-0.025549$ |
| A4 | Model B seeded 24 | +0.10 | 8.0 | 1 | +0.10 | 0.08402 | 24/24 | 0.4116 | $-0.028565$ |
| A5 | Model B seeded 6 | $-0.18$ | 8.0 | 1 | $-0.18$ | $0.04033\dagger$ | 6/24 | 0.3952 | $-0.00229$ |
| A6 | Model B seeded 6 | 0.00 | 8.0 | 1 | 0.00 | $0.05834\dagger$ | 6/24 | 0.5716 | $-0.041306$ |
| S1 | static imposed 24 | $-0.30$ | 8.0 | 1 | $-0.30$ | 0.0776 | 24/24 | 0.3802 | **+0.011431** |
| S2 | static imposed 24 | $-0.18$ | 8.0 | 1 | $-0.18$ | 0.07758 | 24/24 | 0.3800 | $-0.007632$ |
| S3 | static imposed 24 | 0.00 | 8.0 | 1 | 0.00 | 0.0857 | 24/24 | 0.4199 | $-0.025495$ |
| S4 | static imposed 24 | +0.10 | 8.0 | 1 | +0.10 | 0.08375 | 24/24 | 0.4103 | $-0.028464$ |

\* Q4 "14 modes" is a diagnostic artifact: at noise amplitude $(\langleA\rangle = 0.00349)$
the half-max criterion counts noise; use $\langleA\rangle$/rms/Fexc — essentially no pattern.
$\dagger A5/A6 \langleA\rangle$ is the mean over all 24 shell modes; the 6 occupied modes have
$\approx0.161 (A5)$ and $\approx0.233 (A6)$, matching the one-mode prediction exactly (§4).

**d4 note (read before citing any d4 value).** In this $L = \pi$ setup d4 = 1.0 in
*every* quench because d4 measures shell-power fraction and only the $D_{4}$ shell
is linearly unstable here. It does NOT contradict sim7's 0.771 (different
setup: sim7 has a competitor shell at equal linear penalty). The discriminating
observable in my setup is **mode occupation** (6 vs 12 vs 24), not shell
fraction. Task 2's seed survey adds: seed $4 \to 2$-mode (Fexc $-0.036477)$,
seed $5 \to 8$-mode (Fexc $-0.035767)$ — see Task 2 report §3.4.

### 3.2 The observed 6-mode sub-pattern (post-hoc identification, A3)

Q1's top-6 modes: $(-1,-1,0,0)$, (1,1,0,0), (0,$-1,-1,0)$, (0,1,1,0),
(1,0,$-1,0)$, $(-1,0,1,0)$; amps 0.223–0.227. All have $x_{4} = 0$: the pattern
lives entirely in the 3D subspace $x_{4} = 0 ($the $D_{4} \cap {x_{4} = 0}$ cross-section).
The three cosine directions (1,1,0,0), (0,1,1,0), (1,0,$-1,0)$ are coplanar
(determinant 0) at $60^\circ/60^\circ/120^\circ$ — the manuscript's "hexagonal" sub-pattern.
(N, T, Q) = (6, 12, 90); $S_{6} = (2/3)/2.5 = 0.2667 ($vs $S_{D}_{4} = 0.4539)$.
Saved: `results/task1_q1_top6.json`, `results/task1_q1_final.npy`.
**Any (N, T, Q) for the observed subset is POST-HOC, grade D as a prediction**
(the subset was identified from the data, not predicted before it).

### 3.3 Landau band map at $r = -0.35 ($one-mode ansatz)

`results/task1_landau_curves.csv`; figure `figures/fig1_landau_curves.png`.

| $\bar{\psi}$ range | global minimum | evidence |
|---------|---------------|----------|
| $\bar{\psi} \leq -0.26$ | disordered (no ordered branch) | F24/F6 do not exist; A1 decays to uniform |
| $-0.25$, $-0.24$ | disordered (branch exists, F24 > 0) | F24 = +0.001345, +0.00022 |
| **$-0.23 \dots -0.13$** | **24-mode $D_{4}$** | F24 < F6 < 0; A2 persists |
| $-0.12 \dots +0.10$ | 6-mode hexagonal | F6 < F24 < 0; A6 Fexc $-0.0413 < A3 -0.0255$ |
| $\bar{\psi} = -0.18 ($centre) | 24-mode by 0.0054 | $F24 -0.007632$ vs $F6 -0.002254$ |

Band edges (0.01 grid): 24-mode global minimum for $\bar{\psi} \in (-0.235, -0.125)$.
The manuscript's "approximately $-0.33$ ≲ $\bar{\psi}$ ≲ 0.03 depending on quench depth"
is the union over the $(\bar{\psi}, r)$ plane; the +0.03 edge is UNVERIFIED against
this slice (see CLAIM §2).

### 3.4 Findings (each tied to a row above)

1. **Mean forgetting (wave dynamics).** The damped-wave quench equilibrates
   to $\bar{\psi}$_final $\approx +0.0025$ from *any* $\bar{\psi}_{0} \in {-0.30, -0.18, 0, +0.10} (Q1, Q2$,
   Q5, Q6 identical to 4 decimals). The wave equation does not conserve the
   mean; the initial mean is not a control parameter of the quench outcome.
   The static account has no such effect (it takes $\bar{\psi}$ as given).
2. **Noise quench selects sub-patterns, never 24/24.** Q1/Q2/Q5/Q6/Q7: 6-mode;
   Q3 (triads off, u = 0): 12-mode — matching FINAL_AUDIT ("6-mode (u=1) and
   12-mode (u=0)"). Task 2 seeds add 2-mode and 8-mode. The 6-mode is the
   most common (3/5 seeds) and the lowest-F quench outcome.
3. **Triads change the outcome.** $u = 1 \to 6$-mode (Fexc $-0.040)$; $u = 0 \to$
   12-mode (Fexc $-0.016)$. The triad coupling is load-bearing for selection.
4. **Detuning kills the pattern.** $Q4 (q_{0}^{2} = 7.5$, past the 0.4024 edge):
   $\langleA\rangle = 0.00349$, rms = 0.0184 — residual noise only. P2 CONFIRMED.
5. **Seeded 24-mode decays outside the branch.** $A1 (\bar{\psi} = -0.30)$: decays to
   uniform (amp = 0, Fexc = 0) — exactly as the discriminant predicts
   (no ordered branch at $\bar{\psi} = -0.30, r = -0.35)$. The static account's S1
   imposes the same pattern with Fexc = **+0.011431, above the disordered
   state** — the starkest divergence in the grid.
6. **Metastability, not band membership.** $A3 (\bar{\psi} = 0)$ and $A4 (\bar{\psi} = +0.10)$:
   the seeded 24-mode PERSISTS under Model $B (\langleA\rangle = 0.08585, 0.08402)$ but
   with Fexc $(-0.0255, -0.0286)$ ABOVE the 6-mode $(-0.0413$ at $\bar{\psi} = 0)$. The
   24-mode is a local minimum outside the band; the 6-mode is the global
   minimum there. $(\langleA\rangle = 0.08585$ at $\bar{\psi} = 0$ is also the sim6 Model A final
   amplitude — Model A drifts $\bar{\psi} \to 0$, then equilibrates to the $\bar{\psi} = 0$
   stationary value. Consistent.)
7. **Both patterns are local minima at both $\bar{\psi}$.** A5 (seeded 6-mode,
   $\bar{\psi} = -0.18)$: persists, Fexc $-0.00229 ($above the 24-mode'$s -0.00773)$;
   $A6 (\bar{\psi} = 0)$: persists, Fexc $-0.04131 ($below the 24-mode'$s -0.02555)$.
   Which is global flips at $\bar{\psi} \approx -0.125$.
8. **One-mode ansatz is accurate.** It predicts the 6-mode amplitude to
   0.1% (A6: predicted 0.2333 per occupied mode, measured 0.2334) and its
   F to $5\times10^{-5} ($predicted $-0.041287$, measured $-0.041306)$; it predicts A*
   to 0.14% (harmonic shift, not error — see Task 2 §3.1).

## 4. The divergence boundary (falsifiable)

The accounts' predictions diverge when **any** of the following holds
$(r = -0.35, u = v = 1)$:

- **D1.** $\bar{\psi}$ outside the 24-mode global-minimum band $(-0.235, -0.125)$:
  static predicts 24/24; dynamic predicts 6-mode $(\bar{\psi}$ ≳ $-0.12)$, disorder
  $(\bar{\psi}$ ≲ $-0.235)$, or a metastable 24-mode only if seeded.
- **D2.** |$q_{0}^{2} - 8$| > 0.4024 (ordered branch absent): static predicts 24/24;
  dynamic predicts no pattern (Q4).
- **D3.** Triad coupling off (u = 0): static is silent (no triad concept);
  dynamic predicts 12-mode, not 6-mode (Q3).
- **D4.** Noise initial condition (outside the full-pattern basin): static
  predicts 24/24; dynamic predicts a sub-pattern (6/2/8-mode by seed).

They agree only inside the band, with $q_{0}$ tuned, triads on, and a seeded or
basin initial condition (A2/S2: both give 24/24, $\langleA\rangle = 0.0776$–0.0777,
Fexc = $-0.0076/-0.0077$ — agreeing to the 1.24% harmonic gap).

**What the static account can and cannot explain.** It CAN explain: the
pattern's geometry (24 roots, S = 64/141), the stationary amplitude to
0.14%, and the free energy to 1.24% — *where the pattern exists*. It CANNOT
explain: why $D_{4}$ rather than another shell (no mechanism — the shell is a
primitive in its olog); the band edges; the $\bar{\psi} = 0$ sub-pattern; the detuning
cutoff; the seed dependence; or why the pattern decays at $\bar{\psi} = -0.30$. The
v93.1 ontology change dissolves the circularity objection as a matter of
logic (the theory no longer postulates what it claims to derive), but the
*dynamical* selection claim is conditional on D1–D4 — and in the $L = \pi$
setup the full pattern is not selected from noise at all.

## 5. Checks run

| check | result |
|-------|--------|
| exact_checks.py (SymPy 1.14.0 + python-flint 0.8.0 + Z3 4.15.4): 29 checks — (24,192,3384), $S_{D}_{4} = 64/141$, $\tau^{2} = 8/3$, $q_{4} = 47/8$, $S_{A}_{4}* = 12/31$, $S_{BCC} = 16/45$, ratio 496/423, margin 73/423, $\tau$ ratio $\sqrt{2}$, A* = 0.0775753, $F/V = -0.0076323$, $r_{eff}$ table, detuning edge 0.4024, CFL dt_max = 1.9238 | **PASS** (exit 0) |
| sim6 attractor reproduction (shipped script): Model B t = 2.5, 7.5 match paper exactly; Model A completes $(\bar{\psi} = +0.00087, \langleA\rangle = 0.08585)$ | **PASS** |
| sim7 fair-test reproduction: 0.771 / 0.211 / 0.895 (author 0.84 / 0.44–0.56 / 1.00; independent reproduction 0.895 exact) | **PASS** |
| $P1 (\bar{\psi} = 0$ noise quench $\to$ sub-pattern, not 24/24) | **PASS** (6-mode) |
| $P2 (\bar{\psi} = -0.18, q_{0}^{2} = 7.5 \to$ no ordered 24-mode state) | **PASS** (noise only) |
| P3 (triads off $\to D_{4}$ shell fraction < 0.35) | **PASS** — by the sim7 fair-test reproduction (triad-off control $D_{4} = 0.211 < 0.35$, matching the independent reproduction's 21.1% exactly). The $L = \pi$ quenches are a different setup where d4 is undefined as a discriminator (d4 = 1.0 always); the prediction as written is about the sim7 control value, which was measured. |
| P4, P5 | Task 2 report |
| P1/P2 confirmed, P3 confirmed (sim7 control 0.211), P4/P5 | Task 2 report |
| Hoy [40] LJ-MD re-simulation | **NOT RUN** (taken as manuscript-reported, A5) |
| Lean re-verification of new claims | **NOT RUN** (no new Lean work) |
| Barenblatt classification of the band edge | **NOT ESTABLISHED — ABSTAIN** |
| S6 tournament as LLM Elo | **NOT RUN** (replaced by simulation grid) |

## 6. Rival / failure mode

The strongest rival to the divergence claim is that the $L = \pi$ setup is too
favourable to sub-patterns: with only the $D_{4}$ shell unstable, the quench has
no competitor shell to lose to, so it settles into a sub-pattern of the one
available shell. The sim7 setup (competitor shell at equal linear penalty)
*does* show $D_{4}$ selection from noise (77–84%). The honest reading: the
dynamic account selects $D_{4}$ *between shells* robustly, but selects the *full
24-mode pattern within the shell* only conditionally (basin/seeded IC). A
second failure mode: the 6-mode outcome could be an artifact of the RK4
damped-wave quench $(\gamma = 1.2)$ rather than the free-energy landscape — but the
Model B seeded runs (A5/A6) and the Landau curves agree with the quench
outcomes independently, and the 6-mode's F is the global minimum at $\bar{\psi} = 0$
by both the ansatz and the full-field measurement, so the outcome tracks the
landscape, not the integrator. A third: the one-mode ansatz could mis-rank
patterns — but the full-field measurements (A3 vs A6, A2 vs A5) confirm the
ansatz ranking at every point checked, to $5\times10^{-5}$ in F.

## 7. Evidence that would change the answer

- A noise quench in the $L = \pi$ setup reaching 24/24 at any seed would falsify
  the "never from noise" finding (D4) — run more seeds $(n \geq 20)$ to bound the
  rate.
- A full-field phase-diagram recomputation (ws-a task 3) showing the 24-mode
  band extending to $\bar{\psi} = +0.03$ at some r would resolve the quoted-edge
  discrepancy in the manuscript's favour; showing it does not would confirm
  the slice.
- A demonstration that the 2-/8-mode quench outcomes are transient (longer
  T, or annealing to the 6-mode) would collapse the seed-dependence to a
  single sub-pattern.
- A mechanistic account of what fixes $\bar{\psi}$ and supplies the nucleation event
  (IX.5.1, IX.5.2 — the manuscript's own sharpest open questions) would
  change the status of D4 from "conditional on basin IC" to "selected".

## 8. HLRE grades per narrow claim (worst-of shown, against CLAIM_REGISTER.md)

| claim (register wording) | grade | worst-of computation |
|-------|-------|----------------------|
| C1.1 Static account predicts the full 24-mode pattern under ALL conditions (pattern postulated, not produced) | **C** | S1–S4: 24/24 imposed at every $\bar{\psi}$ incl. $\bar{\psi} = -0.30$ where Fexc > 0; falsifier (a manuscript statement giving the static account a selection dynamics) not found $\to C ($Track E cap) |
| C1.2 Dynamic account predicts the full 24-mode pattern ONLY inside the band with $q_{0}$ tuned and triads active | **FAILED as written** | Q2 is the register's own falsifier: noise quench at $\bar{\psi}_{0} = -0.18 ($inside the quoted band) reaches 6/24. The basin/evolved-$\bar{\psi}$ corrected version is CONFIRMED under C1.3. No grade above FAILED applies to the claim as written. |
| C1.3 Divergence boundary D1–D4 (branch edge, detuning 0.4024, triads off, basin IC) | **C** | all four legs confirmed at probe points; branch edge exact (two tools$) \to C ($Track E cap) |
| C1.4 Ontology change dissolves the circularity objection; $a_{0} = 2\pi/q_{0}$ is an output of the dispersion, not an input via $L_{P} ($Track F) | **F3** | deductive chain verified $(a_{0} = 2.221441$, CFL dt_max = 1.9238, exact checks); F3 is the Track F cap until a human runs the source/balance gates |
| C1.5 Static account CANNOT explain (a) lattice selection, (b) finite band, (c) 6-mode outcome, (d) nucleation, (e) Model A vs B | **C** | (b), (c), (e) measured directly; (a), (d) established by absence of the relevant structure in the static formulation (manuscript §I.$1) \to C ($Track E cap) |
| C1.6 Landau + LJ corroborate the winner; S-transfer is deductive combinatorics; near-melting scope does NOT transfer | **C** | S4 split verdict (combinatorial PASS, scope FAIL); Hoy leg NOT RUN $(A5) \to C ($Track E cap) |

## 9. Ledgers

**Assumptions.** A1: sim6/sim7 are faithful implementations of the manuscript
dynamics (reproductions match the audit to all quoted digits). A2: N = 16,
$L = \pi$, $q_{0}^{2} = 8.0$ is the reference config. A3: the 6-mode sub-pattern is
identified by measured occupied modes, NOT assumed to be the manuscript's
"hexagonal" pattern — its (N, T, Q) is POST-HOC, grade D as a prediction.
A4: static account formalized as imposed $\Psi(x) = \bar{\psi} + A*\Sigma\cos(g\cdotx)$ with the
ansatz amplitude (most charitable reading; v92 had no amplitude equation).
A5: Hoy [40] LJ-MD taken as manuscript-reported, NOT re-simulated.

**Parameters.** $r = -0.35$, u = v = 1, $\gamma = 1.2 ($wave), dt = 0.02 (quench),
dt = 0.005 (attractor), T = 50 (quench), T = 7.5 (attractor), seeds 1–5,
$q_{0}^{2} \in {7.5, 8.0}$, $\bar{\psi}_{0} \in {-0.30, -0.18, 0, +0.10}$.

**Choices.** $L = \pi$ setup (only $D_{4}$ shell unstable) rather than sim7'$s L = 2\pi$
competitor-shell setup — chosen because it isolates *within-shell* selection,
which is what the static-vs-dynamic divergence turns on. Hermitian projection
on by default in the shared module (exact no-op in exact arithmetic).

## 10. VERIFIED / UNVERIFIED / FAILED

**VERIFIED.** $S_{D}_{4} = 64/141$ and all shell combinatorics (exact, two tools);
A* = 0.0775753, $F_{ansatz} = -0.0076323 ($exact); detuning edge 0.4024 (exact);
wave quench forgets $\bar{\psi}_{0} (\to +0.0025, 4 \bar{\psi}_{0}$ values); noise quench $\to 6$-mode
(3/5 seeds), 12-mode triads-off, 2-mode and 8-mode (1 seed each); detuned
quench $\to$ no pattern; seeded 24-mode decays at $\bar{\psi} = -0.30$ and persists
metastably at $\bar{\psi} = 0$, +0.10; 6-mode is the global minimum at $\bar{\psi} = 0$
(ansatz + full-field agree to $5\times10^{-5})$; static pattern at $\bar{\psi} = -0.30$ has
Fexc = +0.011431 > 0; one-mode ansatz predicts the 6-mode amplitude to
0.1%; Model B instability diagnosed (1.0142/step) and fixed by Hermitian
projection, stable to t = 30 (extends the manuscript's t = 18 claim).

**UNVERIFIED.** The manuscript's quoted band edges $(-0.33, +0.03)$ against the
measured $r = -0.35$ slice $(-0.235, -0.125)$; the band's r-dependence (ws-a
task 3); the rate of 24/24 selection from noise (0/5 seeds — an upper bound,
not a zero); Barenblatt classification of the band edge; the Hoy [40] LJ leg
of C1.6 (NOT RUN).

**FAILED.** C1.2 as registered (dynamic account predicts the full 24-mode
pattern inside the band from a noise quench) — falsified by Q2 under the
register's own falsifier. The basin-qualified correction is CONFIRMED under
C1.3. P4's fixed-point form is REFUTED as written (see Task 2 report §4) —
the $\langleA\rangle$ error vs A* does not decrease with dt, because it is a model-form gap
(harmonic shift), not a discretization error.

## 11. Citation record

Manuscript IRH v93.1 (§I.2 dynamics, §II.3 F(B), §II.6 fair test, §II.7–II.8
one-mode analysis and band, §VI-A.2 verification, §VI-A.4 reviewer
instability, App. A item 13, App. B phase-diagram method); repo
`IRH-Theory-Development-Workspace/verification/` (sim6_units.py,
sim7_fairtest.py, FINAL_AUDIT.md, AUDIT_2026-10-15.md); `CLAIM_REGISTER.md`
(frozen predictions P1–P5, assumptions A1–A5); `formalization_notes.md`
(S1–S7); `code/irh_models.py`, `code/exact_checks.py`,
`code/task1a_quenches.py`, `code/task1b_quenches.py`,
`code/task1c_attractors.py`, `code/bisect_instability.py`,
`code/probe_t18.py`, `code/instability_series.py`, `code/make_figures.py`;
`results/task1_probe_results.csv`, `results/task1_landau_curves.csv`,
`results/task1_q1_top6.json`, `results/task1_q1_final.npy`,
`results/instability_series.csv`; `figures/fig1_landau_curves.png`,
`figures/fig2_divergence.png`, `figures/fig4_instability.png`.

## 12. Abstentions

- Hoy [40] LJ-MD: NOT re-simulated (A5); the transportability audit is a
  structural argument, not a measurement.
- Barenblatt classification of the band edge: NOT ESTABLISHED.
- Lean re-verification of the new claims: NOT RUN.
- No claim is made about the full $(\bar{\psi}, r)$ phase diagram beyond the $r = -0.35$
  slice measured here.
