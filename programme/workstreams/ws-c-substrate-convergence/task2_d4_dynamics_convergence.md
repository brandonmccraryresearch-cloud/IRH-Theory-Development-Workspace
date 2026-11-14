# Task 2 — Check $D_{4}$ Dynamics Convergence

**Workstream C, Co-scientist task programme, 2026-11-10.**
**Skills:** truth-seeking-frontier $v5 \cdot$ cross-domain-discovery v2.0.$0 \cdot$ hlre-v5-1.
All three are DESIGN CLAIMS, ungraded — never evidence of reliability.
**Tier:** Standard. **Track:** E (cap C), except C2.1a/C2.5 (Track F, cap F3).
**Independence ceiling:** I1 (single tool family — my own simulations in the local
conda env; exact checks cross-verified with a second tool, SymPy + python-flint).
**Nothing in this report is incorporated into the repo or the manuscript.**

## CLAIM + STATUS

**CLAIM.** The reference tension–relaxation model (sim6 Model B semi-implicit
attractor, N = 16, $L = \pi$, $q_{0}^{2} = 8.0$, $r = -0.35$, u = v = 1, $\bar{\psi} = -0.18$,
dt = 0.005, T = 30) reproduces the analytic stationary state; its
discretization error decreases along the grid/time-step ladder with a
measurable convergence order; and discretization, input, and model-form errors
are separately tabulated and compared against the analytic values
$(S_{D}_{4} = 64/141$, etc.) and the published verification.

**STATUS: CONFIRMED in substance, with two claims FAILED as written and
corrected — the corrections are the result, not a defect.**
The attractor fixed point is **resolution-independent**: identical to 6
decimals at every ladder point $(N \in {8, 12, 16, 20} \times$ dt $\in {0.02, 0.01$,
0.005, 0.0025}), so there is no decreasing discretization error to fit for
the fixed-point state — C2.2 and P4 fail as written (their error is a
model-form gap, not a discretization error). The genuine convergence order
lives in the **transient**: first order (Richardson $p \approx 0.9$–1.0 at T = 0.5),
as expected for semi-implicit Euler. The error budget is dominated by input
(seed spread) for quenches and by model form (ansatz vs relaxed, 1.24%) for
the attractor — not by discretization.

## 1. Method

Reference model: sim6 Model B semi-implicit attractor and RK4 damped-wave
quench, generalized in `code/irh_models.py` (verbatim port of sim6 analyze();
Hermitian projection on by default — an exact no-op in exact arithmetic, see
Task 1 report §2 Step 5). Ladders (physical time fixed: T = 30 attractor,
T = 50 quench, so refinement changes resolution, not evolution time):

- Attractor N-ladder: $N \in {8, 12, 16, 20}$ at dt = 0.005.
- Attractor dt-ladder: dt $\in {0.02, 0.01, 0.005, 0.0025}$ at N = 16.
- Transient dt test: seeded at $1.2\cdotA$*, measured at T = 0.5, 1.0, 5.0.
- Quench N-ladder: $N \in {8, 12, 16}$ at dt = 0.02, u = 1, seed 1.
- Quench dt check: N = 16 at dt = 0.04 vs 0.02.
- Input sensitivity: attractor $\bar{\psi} \in {-0.19, -0.18, -0.17}$, $q_{0}^{2} \in {7.9, 8.0, 8.1}$;
  quench seeds 1–5 (seeds 1–2 in Task 1, seeds 3–5 here).
- Model form: (a) ansatz vs relaxed F/V; (b) Model B vs damped-wave RK4 on
  the same seeded attractor; (c) sim6 vs sim7 setup difference.

CFL bound: $a_{0} = 2\pi/q_{0} = 2\pi/\sqrt{8} = 2.221441$, dt_$\max = (\sqrt{3}/2)a_{0}/c = 1.923825$
(c = 1). Largest dt used anywhere: 0.04 (quench check) — $48\times$ below the bound;
reference dt 0.005 is $385\times$ below; attractor dt 0.02 is $96\times$ below.

## 2. Derivation (each step checkable)

**Step 1 — Analytic values (exact, two tools).** $S_{D}_{4} = 64/141 \approx 0.453901$;
$S_{A}_{4}* = 12/31$; $S_{BCC} = 16/45$; $\tau_{D}_{4}/\tau_{BCC} = \sqrt{2}$; A* = 0.0775753 (larger of
the two positive stationary roots of vQA${}^{2} -$ Tu_effA + Nr_eff = 0; the small
root is the unstable branch, F > 0); $F_{ansatz} = -0.0076323; r_{eff}(-0.18)$ =
+0.1072. All in `code/exact_checks.py` (29 checks, SymPy 1.14.0 +
python-flint 0.8.0 + Z3 4.15.4, exit 0).

**Step 2 — Attractor ladder (degenerate).** At every N and dt the fixed point
is $\langleA\rangle = 0.077682$, $D_{4} = 0.999981$, 24/24 modes, lock = 1.0, rms = 0.380565,
Fexc = $-0.007728$, $\bar{\psi} = -0.18$. The state is band-limited (shell + low
harmonics); the N = 8 grid already resolves it exactly, and the fixed point
of the semi-implicit update satisfies the same stationarity condition at every
dt. Hence the discretization error of the fixed-point state is **0 below
1e-6 at every ladder point** — there is nothing to fit a Richardson order to.

**Step 3 — Transient order (where the error lives).** Seeded at $1.2\cdotA$*:
at T = 0.5, $\langleA\rangle($dt) = 0.078030 (0.02), 0.078126 (0.01), 0.078177 (0.005),
0.078203 (0.0025). Successive differences 2.6e-5, 5.1e-5, 9.6e-5; ratios
1.94, $1.88 \to$ Richardson $p \approx 0.96$, 0.91 — **first order**, as expected for
semi-implicit Euler. At T = 1.0 the differences shrink to ~$1e-5 (p \approx 0.86$,
0.69 — degrading as the signal approaches the measurement floor); by T = 5
the transient is over at every dt $(\langleA\rangle = 0.077682$ at all four dt). The dt
error at the reference dt = 0.005 is $\approx2.6e-5$ in $\langleA\rangle$ at T = 0.5 (relative
3.3e-4) and 0 at $T \geq 5$.

**Step 4 — Conservation (full precision).** Projected run, $\bar{\psi}$ drift:
t = 2.5: 7.2e-16; t = 7.5: 1.14e-15; t = 18: 1.31e-15; t = 30: 1.58e-15.
The unprojected run's drift is 0.0 even at t = 27 (the k = 0 mode is exactly
conserved; the blow-up is in the anti-Hermitian sector). The projection costs
~1e-15 of conservation (two extra FFTs per step) and buys stability to
t = 30. P5 (drift < 1e-12) is confirmed by 3 orders of magnitude. The
reference run's reported 8.3e-17 is **not** re-measured by me at that
precision (my best is 1.1e-15 at t = 7.5, one order coarser, with the
projection on); it remains the reference's value, not mine.

## 3. Results

### 3.1 Attractor ladder (full table: `results/task2_ladder.csv`)

| test | N | dt | $\langleA\rangle$ | $D_{4}$ | modes | rms | Fexc | $\bar{\psi}$ drift |
|------|---|----|------|------|-------|------|------|---------|
| attractor-N | 8 | 0.005 | 0.077682 | 0.999981 | 24 | 0.380565 | $-0.007728$ | <5e-11* |
| attractor-N | 12 | 0.005 | 0.077682 | 0.999981 | 24 | 0.380565 | $-0.007728$ | <5e-11* |
| attractor-N | 16 | 0.005 | 0.077682 | 0.999981 | 24 | 0.380565 | $-0.007728$ | <5e-11* |
| attractor-N | 20 | 0.005 | 0.077682 | 0.999981 | 24 | 0.380565 | $-0.007728$ | <5e-11* |
| attractor-dt | 16 | 0.02 | 0.077682 | 0.999981 | 24 | 0.380565 | $-0.007728$ | <5e-11* |
| attractor-dt | 16 | 0.01 | 0.077682 | 0.999981 | 24 | 0.380565 | $-0.007728$ | <5e-11* |
| attractor-dt | 16 | 0.005 | 0.077682 | 0.999981 | 24 | 0.380565 | $-0.007728$ | <5e-11* |
| attractor-dt | 16 | 0.0025 | 0.077682 | 0.999981 | 24 | 0.380565 | $-0.007728$ | <5e-11* |

\* Ladder CSV rounds drift to 10 decimals $(0.0 \to <5e-11)$. Full-precision
measurement (§2 Step 4): 1.58e-15 at t = 30, the longest run; shorter runs
have proportionally less.

**Comparison with analytic values (C2.1).** $\langleA\rangle = 0.077682$ vs A* = 0.0775753:
+0.000106 (+0.137%) — a harmonic shift, not a discretization error (it is
identical at every N and dt). Fexc = $-0.007728$ vs $F_{ansatz} = -0.0076323$:
$-0.000096 (-1.24$% — the harmonic lowering, re-measured; manuscript 1.25%).
$D_{4} = 0.999981$ vs 1.0000: the 1.9e-5 deficit is the harmonic power outside
the shell. 24/24 modes ✓. $\bar{\psi}$ conserved ✓ (above).

### 3.2 Transient dt-convergence (`results/task2_transient.csv`)

| dt | $\langleA\rangle$ at T = 0.5 | $\langleA\rangle$ at T = 1.0 | $\langleA\rangle$ at T = 5 |
|----|---------------|---------------|--------------|
| 0.02 | 0.078030 | 0.077694 | 0.077682 |
| 0.01 | 0.078126 | 0.077700 | 0.077682 |
| 0.005 | 0.078177 | 0.077704 | 0.077682 |
| 0.0025 | 0.078203 | 0.077707 | 0.077682 |

Richardson order at $T = 0.5: p \approx 0.96$, 0.91 (first order). Figure:
`figures/fig3_convergence.png` (a).

### 3.3 Quench ladder and seed spread

| test | N | dt | seed | modes | $\langleA\rangle$ | rms | Fexc |
|------|---|----|------|-------|------|------|------|
| quench-N | 8 | 0.02 | 1 | **2** | 0.09038 | 0.5403 | $-0.036429$ |
| quench-N | 12 | 0.02 | 1 | 6 | 0.0685 | 0.5659 | $-0.041147$ |
| quench-N | 16 | 0.02 | 1 | 6 | 0.07371 | 0.5581 | $-0.040339$ |
| quench-dt | 16 | 0.04 | 1 | 6 | 0.07372 | 0.5581 | $-0.040338$ |
| quench-seed | 16 | 0.02 | 3 | 6 | 0.05891 | 0.5724 | $-0.041771$ |
| quench-seed | 16 | 0.02 | 4 | **2** | 0.09025 | 0.5409 | $-0.036477$ |
| quench-seed | 16 | 0.02 | 5 | **8** | 0.09071 | 0.5321 | $-0.035767$ |

(Seeds 1–2 in Task 1: seed $1 \to 6$-mode, Fexc $-0.040339$; seed $2 \to 6$-mode,
Fexc $-0.041236$.) **N = 8 fails** (2-mode — the grid is too coarse for the
noise-driven selection; the nonlinear triad/quartet interactions alias).
N = 12 and N = 16 agree on the 6-mode outcome; Fexc differs by 0.0008 (2%).
dt = 0.04 vs 0.02: identical to 1e-6 (RK4, 4th order, strongly damped).
**Seed spread dominates**: 5 seeds give 6-mode $\times3$, 2-mode, 8-mode;
Fexc range $-0.0358$ to $-0.0418 ($spread 0.0060, ~15% of |Fexc|). The quench
outcome is multi-stable among sub-patterns; no seed reaches 24/24.

### 3.4 Input sensitivity (attractor)

`results/task2_attractor_sensitivity.csv`.

| variation | $\langleA\rangle$ | Fexc | sensitivity |
|-----------|------|------|-------------|
| $\bar{\psi} = -0.19$ | 0.076338 | $-0.006399$ | $d\langleA\rangle/d\bar{\psi} \approx 0.126$/unit |
| $\bar{\psi} = -0.18 ($ref) | 0.077682 | $-0.007728$ | — |
| $\bar{\psi} = -0.17$ | 0.078856 | $-0.009041$ | dF/$d\bar{\psi} \approx -0.132$/unit |
| $q_{0}^{2} = 7.9$ | 0.076623 | $-0.007011$ | symmetric with 8.1 |
| $q_{0}^{2} = 8.0 ($ref) | 0.077682 | $-0.007728$ | — |
| $q_{0}^{2} = 8.1$ | 0.076627 | $-0.007015$ | $\Delta\langleA\rangle -0.0011 (1.4$%), $\DeltaF +0.0007 (9$%) |

$A \pm0.01$ error in $\bar{\psi}$ moves $\langleA\rangle$ by $\pm0.0013 (1.6$%) and Fexc by $\pm0.0013$
(17% of |Fexc| — the free energy is far more input-sensitive than the
amplitude). $A \pm0.1$ detuning in $q_{0}^{2}$ moves $\langleA\rangle$ by $-0.0011 (1.4$%) and Fexc by
+0.0007 (9%), symmetric in the detuning sign $(r_{shell}$ depends on
$(q_{0}^{2}-8)^{2})$. The one-mode predictions track the measurements at every point
$(\langleA\rangle$ within +0.00013, F within $-0.00010$ — the same harmonic shifts as at
the reference point).

### 3.5 Model form (`results/task2_modelform.csv`)

| comparison | result |
|------------|--------|
| (a) ansatz vs relaxed F/V | $F_{ansatz} = -0.0076323$, $F_{relaxed} = -0.007728 ($sim$) / -0.0077276 ($paper); gap $-9.6e-5$, relative **1.238%** (manuscript 1.25%) |
| (b) Model B vs damped-wave RK4, same seeded attractor | Wave: $\bar{\psi}$ drifts to +0.00087 (exactly the sim6 Model A value), $\langleA\rangle = 0.08585$, rms = 0.4206, Fexc = $-0.025597$, 24/24 modes survive. Model $B: \bar{\psi}$ held at $-0.18$, $\langleA\rangle = 0.07768$, Fexc = $-0.007728$. **The model-form difference is the mean, not the pattern**: both keep the seeded 24-mode; the wave version equilibrates to the $\bar{\psi} \approx 0$ stationary state, where the 24-mode is metastable. |
| (c) sim6 vs sim7 setup | sim$6 (q_{0}^{2} = 8.0, L = \pi)$: attractor $\langleA\rangle = 0.07768$, Fexc = $-0.007728$; quench $\to 6$-mode sub-pattern. sim$7 (q_{0}^{2} = 7.5, L = 2\pi$, competitor shell$): D_{4} = 0.771$ direct / 0.895 annealed / 0.211 control. Different observables (attractor vs quench; shell fraction vs mode occupation) — a setup difference, not an error. The two setups agree where they overlap: the sim7 reproduction matches the audit (0.895 annealed exact). |

## 4. Error tabulation (discretization / input / model-form, separately)

| error class | observable | magnitude at reference resolution | verdict |
|-------------|-----------|----------------------------------|---------|
| Discretization (attractor fixed point) | $\langleA\rangle$, $D_{4}$, Fexc, rms | **0 below 1e-6** (N 8–20, dt 0.0025–0.02 identical) | reference resolution already exact for the fixed point |
| Discretization (attractor transient) | $\langleA\rangle$ at T = 0.5 | 2.6e-5 at dt = 0.005 (3.3e-4 relative); first order, $p \approx 0.95$ | small; vanishes by T = 5 |
| Discretization (quench) | Fexc | N = 8 fails (2-mode); N = 12 vs 16 differ 0.0008 (2%); dt 0.04 vs 0.02 differ 1e-6 | $N \geq 12$ required; dt error negligible |
| Input (quench seed) | Fexc, mode count | spread 0.0060 across 5 seeds (15%); mode count 2/6/8 | **dominates** the quench error budget |
| Input (attractor $\bar{\psi} \pm0.01)$ | $\langleA\rangle$, Fexc | $\pm0.0013 (1.6$%), $\pm0.0013 (17$% of \|Fexc\|) | dominates the attractor error budget |
| Input (attractor $q_{0}^{2} \pm0.1)$ | $\langleA\rangle$, Fexc | $-0.0011 (1.4$%), +0.0007 (9%) | second-largest attractor error |
| Model form (ansatz vs relaxed) | Fexc | 1.238% (gap $-9.6e-5)$ | the $\langleA\rangle$-vs-A* gap (+0.137%) is this, not discretization |
| Model form (wave vs Model B) | $\bar{\psi}$_final, $\langleA\rangle$, Fexc | $\bar{\psi}$: $-0.18 \to +0.00087$; $\langleA\rangle$: $0.07768 \to 0.08585$; Fexc: $-0.00773 \to -0.02560$ | mean only; pattern survives in both |
| Model form (setup sim6 vs sim7) | selection observable | different observables; no common error scale | setup difference, not an error |

**Bottom line.** For the attractor, the error budget is model-form (1.24%)
and input $(\bar{\psi}, q_{0}^{2})$, with discretization at zero. For the quench, the error
budget is input (seed spread, 15%) and discretization at N = 8 (failure),
with dt error negligible. Nothing in the budget threatens the $D_{4}$ selection
result: the fixed point, the band, and the sub-pattern outcomes are all
stable across every refinement that does not itself fail (N = 8 quench).

## 5. Checks run

| check | result |
|-------|--------|
| exact_checks.py (29 checks, two tools + Z3) | **PASS** (exit 0) |
| sim6 attractor reproduction (shipped script, t = 2.5/7.5) | **PASS** (exact to all quoted digits) |
| sim7 fair-test reproduction (0.771 / 0.211 / 0.895) | **PASS** (annealed 0.895 exact vs independent reproduction) |
| P4 (attractor $\langleA\rangle$ error vs A* decreases with dt) | **FAILED as written** — error is constant 0.000106 at every dt (model-form gap); transient error DOES decrease with dt, $p \approx 0.95$ |
| $P5 (\bar{\psi}$ drift < 1e-12 at every ladder point) | **PASS** — full-precision drift 1.58e-15 at t = 30 (longest run); 1.14e-15 at t = 7.5 |
| C2.5 CFL leg (all dt << 1.9238) | **PASS** (largest dt 0.04, $48\times$ below) |
| C2.5 conservation leg (reference 8.3e-17) | **PARTIAL** — my best measurement is 1.1e-15 at t = 7.5 (projection on); the reference's 8.3e-17 is not re-measured at that precision |
| N = 24 grid point | **NOT RUN** (choice ledger: cost/benefit; N = 20 already identical to N = 8) |

## 6. Rival / failure mode

The strongest rival to "resolution-independent fixed point" is that the
ladder is degenerate *because* the seeded attractor starts at the fixed
point — a ladder that never leaves the fixed point cannot measure
convergence. Answer: that is exactly why the transient test (seeded at
$1.2\cdotA*)$ was run — it leaves the fixed point, and it shows first-order
dt-convergence $(p \approx 0.95)$ and full relaxation by T = 5 at every dt. A
second rival: the N = 8 quench failure could be a filter artifact (K2 < 64)
rather than a grid failure — but the attractor at N = 8 (filter K2 < 200) is
exact, and the quench filter is the same at every N, so the N = 8 quench
failure tracks the grid, not the filter. A third: the seed spread (2/6/8
modes) could be transient — longer quenches or annealing might collapse all
seeds to the 6-mode. That is untested here and is the first follow-up below.

## 7. Evidence that would change the answer

- A ladder point (N, dt) where the attractor fixed point differs from
  $0.077682/-0.007728$ by more than 1e-6 would falsify
  resolution-independence (none found in 8 points).
- A transient order significantly different from 1 (e.g. $p \approx 2)$ would
  indicate a different time-stepping error than semi-implicit Euler.
- A quench seed reaching 24/24 would change the Task 1 divergence finding
  (0/5 so far); 20+ seeds would bound the rate.
- Longer quenches (T = 200) or annealing showing the 2-/8-mode outcomes
  collapsing to the 6-mode would reduce the seed spread to a transient.
- A full-precision re-measurement of the *unprojected* shipped sim6 run's
  $\bar{\psi}$ drift at t = 7.5 would settle whether the reference 8.3e-17 is
  reproduced (mine is 1.1e-15 with the projection on).

## 8. HLRE grades per narrow claim (worst-of shown, against CLAIM_REGISTER.md)

| claim (register wording) | grade | worst-of computation |
|-------|-------|----------------------|
| C2.1 Reference model reproduces the analytic stationary state (A* = 0.0775753 (F), $F/V = -0.0076323 (F), D_{4} = 1.0000, 24/24, \bar{\psi} ~1e-16)$ | **C** (Track E part); **F3** (Track F part, A*/F/V) | $\langleA\rangle$/Fexc differ from the ansatz values by the measured harmonic gaps (+0.137%, $-1.24$%) — model-form, not failure; $D_{4} = 0.999981 ($harmonic deficit 1.9e-5); 24/24 ✓; conservation measured 1.1e-15, not $1e-16 \to C$; analytic values verified exactly (two tools$) \to F3 ($Track F cap) |
| C2.2 Discretization error decreases with N and dt, measurable order | **FAILED as written** | fixed-point error is 0 at every ladder point (no decrease to measure); transient error DOES decrease, $p \approx 0.95$ — the corrected claim is confirmed, the registered claim is not |
| C2.3 Input error quantified separately, compared with discretization | **C** | seed spread (5 seeds), $\bar{\psi} \pm0.01$, $q_{0}^{2} \pm0.1$ all measured; input dominates discretization at reference resolution $\to C ($Track E cap) |
| C2.4 Model-form error quantified: (a) ansatz vs relaxed, (b) Model B vs wave, (c) sim6 vs sim7 | **C** | (a) 1.238% re-measured; (b) mean-only difference measured; (c) setup difference stated, not conflated with error $\to C ($Track E cap) |
| C2.5 CFL respected; $\bar{\psi}$ conservation at the 1e-16 level (Track F) | **C** (conservation leg); **F3** (CFL leg) | CFL: exact arithmetic, all dt $\leq 0.04 << 1.9238 \to F3 ($Track F cap). Conservation: measured 1.1e-15 at t = 7.5, one order coarser than the reference $8.3e-17 \to C$ worst-of. P5 (< 1e-12) PASS. |

## 9. Ledgers

**Assumptions.** A1: sim6/sim7 are faithful implementations (reproductions
match the audit). A2: N = 16, $L = \pi, q_{0}^{2} = 8.0$ is the reference config. A3:
the 6-mode sub-pattern is identified by measured modes (post-hoc (N, T, Q),
grade D as a prediction). A4: static account as imposed pattern with ansatz
amplitude (charitable). A5: Hoy [40] taken as manuscript-reported, NOT RUN.

**Parameters.** Attractor: $N \in {8, 12, 16, 20}$, dt $\in {0.0025, 0.005, 0.01$,
0.02}, T = 30, seed_amp $\in {1.0$, 1.2}$\cdotA$*. Quench: $N \in {8$, 12, 16},
dt $\in {0.02, 0.04}$, T = 50, seeds 1–5, u = 1. Sensitivity: $\bar{\psi} \in {-0.19$,
$-0.18$, $-0.17}, q_{0}^{2} \in {7.9$, 8.0, 8.1}. Filters K2 < 200 (attractor),
K2 < 64 (quench), exactly as in sim6.

**Choices.** Physical time fixed across the ladder; N = 24 not run (N = 20
already identical to N = 8 — no information would be gained); quench dt
ladder truncated to {0.04, 0.02} (RK4 error already 1e-6; a 0.01 point would
cost ~260 s for no information); transient test added after the fixed-point
ladder proved degenerate (the order has to be measured where the error is).

## 10. VERIFIED / UNVERIFIED / FAILED

**VERIFIED.** All analytic values $(S_{D}_{4} = 64/141, A* = 0.0775753$,
$F_{ansatz} = -0.0076323$, CFL dt_max = 1.9238 — exact, two tools); attractor
fixed point $\langleA\rangle = 0.077682$, $D_{4} = 0.999981$, Fexc = $-0.007728$, 24/24 at all
8 ladder points; transient dt-order $p \approx 0.95 ($first order); $\bar{\psi}$ drift
1.58e-15 at t = 30 (P5 PASS); quench N = 8 failure, N = 12/16 agreement,
dt $0.04 \equiv 0.02$; seed spread 2/6/8-mode over 5 seeds; input sensitivities
$(\bar{\psi}, q_{0}^{2})$; ansatz-vs-relaxed gap 1.238%; wave-vs-ModelB mean-only difference;
sim6/sim7 reproductions match the audit.

**UNVERIFIED.** The reference run's 8.3e-17 conservation value at full
precision (mine: 1.1e-15 with projection); whether the 2-/8-mode quench
outcomes are transient (longer T / annealing untested); the 24/24-from-noise
rate beyond 0/5 seeds; N = 24 (not run, no information expected).

**FAILED.** C2.2 as written (no decreasing fixed-point discretization error
to measure — the ladder is degenerate); P4 as written $(\langleA\rangle$ error vs A* is
dt-independent — it is a model-form gap). Both corrected versions (transient
order $p \approx 0.95)$ are CONFIRMED.

## 11. Citation record

Manuscript IRH v93.1 (§I.2, §II.3, §II.6–II.8, §VI-A.2, §VI-A.4, App. A
item 13); repo `IRH-Theory-Development-Workspace/verification/`
(sim6_units.py, sim7_fairtest.py, FINAL_AUDIT.md, AUDIT_2026-10-15.md);
`CLAIM_REGISTER.md`; `code/irh_models.py`, `code/exact_checks.py`,
`code/task2a_attractor_ladder.py`, `code/task2b_quench_ladder.py`,
`code/task2c_sensitivity_modelform.py`, `code/task2d_transient.py`,
`code/instability_series.py`, `code/make_figures.py`;
`results/task2_ladder.csv`, `results/task2_transient.csv`,
`results/task2_input_sensitivity.csv`,
`results/task2_attractor_sensitivity.csv`, `results/task2_modelform.csv`,
`results/instability_series.csv`; `figures/fig3_convergence.png`,
`figures/fig4_instability.png`.

## 12. Abstentions

- No claim about N = 24 (not run).
- No claim that the reference 8.3e-17 conservation value is reproduced
  (measured 1.1e-15 with the projection on).
- No claim about the long-time fate of the 2-/8-mode quench outcomes.
- No GCP spend: all work is local CPU (total compute across both tasks
  $\approx 1$ hour wall-clock on the shared 1.5-CPU VM); no heavy-sim costed plan
  was needed, and none is filed. lean-build-4 was never touched.
