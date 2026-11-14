# Task 5 — Spectral-power threshold for full $D_{4}$ formation (local-independent)

**CLAIM:** At fixed total modulation power (RMS $0.3800398$, total power $0.144430238451$), interpolating the initial spectrum of the $4$D field pilot from pure off-shell random ($s=0$) to pure on-shell random ($s=1$) gives a sharp, binary threshold: for the three specified random directions, recovery of the stationary full $24$-mode pattern is $0/3$ at $s \le 0.05$, $2/3$ at $s=0.075$, and $3/3$ at every $s \ge 0.10$ tested (up to $s=1$). The linearly interpolated $50\%$ point is $s_{50} \approx 0.069$; the first $s$ with $3/3$ recovery is $s=0.10$. No partial-pattern or other endpoint occurred in any of the $33$ runs.

**STATUS:** VERIFIED for the stated protocol only — $33$ runs, $11$ shell-concentration points $\times 3$ paired replicates, $t=200$, $N=18$, $K=4$, ETD2 Model B, one box, one parameter point, one total power. Independent re-derivation from the saved checkpoints confirms $33/33$ outcomes. Half-timestep re-runs confirm both outcomes straddling the transition. The population-level recovery probability at any $s$, and persistence of the threshold under any change of resolution, box, parameters, power, or horizon, are NOT established (see UNVERIFIED/ABSTAIN list).

![Threshold curve](threshold_curve.png)

## 1. Definitions (frozen before the Stage 1 runs)

### 1.1 The interpolation

Let $s$ be the initial $D_{4}$ shell power fraction,

$$s = \frac{\sum_{k \in S} |a_{k}|^{2}}{\sum_{k \ne 0} |\hat{\phi}_{k}|^{2}},$$

where $S$ is the $24$-vector $D_{4}$ star ($|k|^{2}=8$) and the denominator is total modulation power. For each replicate $rep \in \{0,1,2\}$, draw the same broadband Gaussian direction $u$ used by the $4$D field pilot: $rng$ from $\mathrm{SeedSequence}([931241112, rep])$, real iid Gaussian on the $18^{4}$ grid, $r$FFT, sharp tensor mask $|k_{i}| \le 4$, normalised to unit total modulation power. Decompose $u = u_{\mathrm{shell}} + u_{\mathrm{off}}$ in the weighted inner product, where $u_{\mathrm{shell}}$ is the projection onto the star and $u_{\mathrm{off}}$ is the orthogonal complement. Let $p = \|u_{\mathrm{shell}}\|^{2}$ be the pilot broadband shell fraction of that direction. For target shell fraction $s \in [0,1]$,

$$y(s) = \mathrm{TARGET} \cdot \left( \sqrt{s}\,\frac{u_{\mathrm{shell}}}{\|u_{\mathrm{shell}}\|} + \sqrt{1-s}\,\frac{u_{\mathrm{off}}}{\|u_{\mathrm{off}}\|} \right),$$

with $\mathrm{TARGET} = \sqrt{24}\,A_{*} = 0.38003978535286725$. Then total power is exactly $\mathrm{TARGET}^{2} = 0.144430238451$ (orthogonal unit components) and the shell fraction is exactly $s$ for every $s$. Endpoints are exact reproductions of pilot families: $y(p) = \mathrm{TARGET} \cdot u$ is the pilot broadband matched start (verified in code by assertion, max difference $< 10^{-12}$), and $y(1)$ is the pilot shell-random bridge start (same direction, renormalised to $\mathrm{TARGET}$). $s=0$ is a new pure off-shell random start (shell power exactly zero). The three directions are paired across all $s$: differences across $s$ are not confounded by direction.

Pilot shell fractions reproduced exactly by this construction: $p = 0.0017047296973272431$ (rep $0$), $p = 0.004572288765534954$ (rep $1$), $p = 0.00311746146135779$ (rep $2$) — identical to `field_outcomes.csv` of the pilot.

### 1.2 Dynamics, diagnostics, outcome rule (identical to the pilot)

Periodic box $[0,2\pi]^{4}$, $\phi = \psi - \bar{\psi}$, $\bar{\psi} = -0.18$, $r = -0.35$, $u = v = 1$, $q_{0}^{2} = 8$, $\alpha = 0.1072$, $\beta = 1.54$, mobility $1$. Excess energy density

$$f = \tfrac12 \sum_{k} [\alpha + (8-|k|^{2})^{2}] |\hat{\phi}_{k}|^{2} - \beta \langle \phi^{3} \rangle / 3 + \langle \phi^{4} \rangle / 4,$$

with Model B dynamics $\partial_{t} \hat{\phi}_{k} = -|k|^{2} [\alpha + (8-|k|^{2})^{2}] \hat{\phi}_{k} - \beta \widehat{P(\phi^{2})}_{k} + \widehat{P(\phi^{3})}_{k}$. Solver: second-order exponential Heun (ETD2), exact linear propagator, $N=18$, $K=4$, $dt=0.1$, $t_{\mathrm{final}} = 200$, startup caps $dt/1000$ until $t=0.02$ and $dt/20$ until $t=0.2$, energy-rejection tolerance $2 \times 10^{-13} + 2 \times 10^{-12} |F|$. Full endpoint (`stationary_full24`): occupancy $24$, amplitude CV $\le 0.05$, signed triad lock $\ge 0.95$ over the $32$ unordered star triads, projected RHS RMS $\le 10^{-7}$. Uniform: total modulation power $< 10^{-12}$. Anything else is `other` (none occurred).

### 1.3 Pre-registered estimators

Before any run: $s_{\mathrm{last\,zero}}$ = largest $s$ with recovery fraction $0$; $s_{\mathrm{first\,full}}$ = smallest $s$ with recovery fraction $1$; $s_{50}$ = linear interpolation in $s$ between the two adjacent grid points bracketing recovery fraction $0.5$ (first crossing only). Wilson $95\%$ intervals per point ($n=3$). These estimators are implemented in `merge_threshold.py` and were not changed after seeing results.

### 1.4 Design stages

- **Stage 1 (frozen grid):** $s \in \{0, 0.05, 0.15, 0.30, 0.50, 0.70, 0.90, 1.0\} \times 3$ replicates $= 24$ runs.
- **Stage 2 (adaptive densification, chosen after Stage 1 located the transition in $(0.05, 0.15)$):** $s \in \{0.075, 0.10, 0.125\} \times 3$ replicates $= 9$ runs. This refines the bracket; it is sequential design, disclosed here, and the Stage 1 bracket stands on its own.
- **Refinement:** half-timestep ($dt = 0.05$) re-runs of the two rep-$0$ runs straddling the transition, $s = 0.05$ and $s = 0.15$ ($2$ runs).

## 2. Results

### 2.1 Threshold curve

| $s$ | $n$ | full $24$ | uniform | other | recovery fraction | Wilson $95\%$ | mean initial energy |
|---:|---:|---:|---:|---:|---:|---:|---:|
| $0$ | $3$ | $0$ | $3$ | $0$ | $0$ | $[0, 0.5615]$ | $35.6885$ |
| $0.05$ | $3$ | $0$ | $3$ | $0$ | $0$ | $[0, 0.5615]$ | $33.9051$ |
| $0.075$ | $3$ | $2$ | $1$ | $0$ | $0.6667$ | $[0.2077, 0.9385]$ | $33.0135$ |
| $0.10$ | $3$ | $3$ | $0$ | $0$ | $1$ | $[0.4385, 1]$ | $32.1218$ |
| $0.125$ | $3$ | $3$ | $0$ | $0$ | $1$ | $[0.4385, 1]$ | $31.2302$ |
| $0.15$ | $3$ | $3$ | $0$ | $0$ | $1$ | $[0.4385, 1]$ | $30.3386$ |
| $0.30$ | $3$ | $3$ | $0$ | $0$ | $1$ | $[0.4385, 1]$ | $24.9891$ |
| $0.50$ | $3$ | $3$ | $0$ | $0$ | $1$ | $[0.4385, 1]$ | $17.8565$ |
| $0.70$ | $3$ | $3$ | $0$ | $0$ | $1$ | $[0.4385, 1]$ | $10.7240$ |
| $0.90$ | $3$ | $3$ | $0$ | $0$ | $1$ | $[0.4385, 1]$ | $3.5915$ |
| $1.0$ | $3$ | $3$ | $0$ | $0$ | $1$ | $[0.4385, 1]$ | $0.0253$ |

Totals: $33$ runs, $26$ stationary full $24$, $7$ uniform, $0$ other. Every full endpoint has final excess energy $-0.007726209285$ (field relaxed full branch; the $24$-mode value is $-0.007632267319$), occupancy $24$, amplitude CV $\le 2.0 \times 10^{-16}$, triad lock $1.0$, RHS RMS $\le 1.10 \times 10^{-15}$. Every uniform endpoint has final power $\le 3.5 \times 10^{-149}$ and final energy $\le 1.83 \times 10^{-150}$.

Threshold estimators (pre-registered): $s_{\mathrm{last\,zero}} = 0.05$, $s_{\mathrm{first\,full}} = 0.10$, bracket $(0.05, 0.10]$, $s_{50} = 0.06875 \approx 0.069$ by linear interpolation between $(0.05, 0)$ and $(0.075, 2/3)$.

### 2.2 The mixed point

At $s = 0.075$, rep $0$ and rep $2$ recover while rep $1$ goes uniform. Initial energies at $s = 0.075$ are $33.0771$ (rep $0$, recovers), $33.2585$ (rep $1$, uniform), $32.7048$ (rep $2$, recovers): the failing direction has the middle initial energy, so initial energy does not order the outcome at fixed $s$ — direction (which modes/phases carry the shell power) matters beyond total shell power and beyond energy. This is a $2/3$ point, not a clean step: the threshold is a transition region for these directions, with $s_{50}$ inside it.

### 2.3 Initial energy falls with $s$ — but does not explain the threshold

Mean initial excess energy falls monotonically from $35.6885$ at $s=0$ to $0.0253$ at $s=1$ (middle panel of the figure). That fall is expected: off-shell power carries the $(8-|k|^{2})^{2}$ linear penalty. But the threshold is not an energy threshold in disguise: at fixed $s$ the outcome varies while energy varies only by $\sim 1\%$ across replicates, and at $s=0.075$ the energy ordering contradicts the outcome ordering (§2.2). The controlling variable in this experiment is the shell fraction $s$ at fixed total power, not the initial energy, which is a consequence of $s$ plus direction.

### 2.4 Endpoint reproduction of the pilot

$s=1$ reproduces the pilot bridge family ($3/3$ stationary full $24$, same final energy to $10^{-15}$). The pilot broadband point $s \approx p \in [0.0017, 0.0046]$ lies between the $s=0$ and $s=0.05$ points, both $0/3$ uniform here, consistent with the pilot's $0/3$ broadband matched result. The interpolation therefore joins the two pilot endpoints with a single sharp transition, rather than a gradual ramp.

## 3. Checks run

Tool: conda env python `~/miniconda3/envs/jacobian-conjecture-2d/bin/python`, Python $3.11.16$, NumPy $2.4.6$, SciPy $1.17.1$, Matplotlib $3.11.2$. Every solver invocation below exited $0$.

| check | verdict | quoted result |
|---|---|---|
| Solver self-tests (dealiasing, gradient, dissipation, shell RHS vs exact $24$-mode truncation, linear decay; run at the start of every one of the $11$ solver invocations) | PASS | dealias energy $18$ vs $28$ same $K=4$: $0.0 < 10^{-10}$; projected nonlinearity max $1.69704 \times 10^{-18} < 10^{-12}$; energy–gradient FD error $1.18447 \times 10^{-10} < 10^{-7}$; dissipation identity error $2.91038 \times 10^{-10} < 10^{-8}$; shell RHS vs prior truncation max $6.96499 \times 10^{-17} < 10^{-12}$; shell energy vs prior truncation $6.93889 \times 10^{-18} < 10^{-12}$; linear decay relative error $5.13577 \times 10^{-7} < 10^{-5}$; $32$ unordered triads; $A_{*} = 0.07757529633928076$; matched RMS $0.38003978535286725$ |
| Interpolation exactness (asserted in code, all $3$ directions, $s \in \{0, 0.05, 0.5, 1.0\}$) | PASS | recomputed shell fraction $= s$ to $< 10^{-9}$; total power $= 0.1444302384510534$ to $< 10^{-12}$; pilot $p$ values reproduced exactly (§1.1) |
| Independent verification (`verify_outcomes.py`, fresh minimal implementation, no import of the solver; recomputes outcomes, shell fractions, powers and final energies from saved NPZ checkpoints) | PASS | $33/33$ PASS: reported outcome $=$ recomputed outcome, initial shell fraction $= s$ to $< 10^{-9}$, initial power $= 0.1444302384510534$ to $< 10^{-12}$, final energy agrees to $< 10^{-9}$ |
| Half-timestep refinement ($dt = 0.05$, rep $0$, $s = 0.05$ and $s = 0.15$) | PASS | $s = 0.05$ still uniform (final energy $2.28990 \times 10^{-151}$); $s = 0.15$ still stationary full $24$ (final energy $-0.007726209284874231$, RHS RMS $9.74697 \times 10^{-16}$); $2/2$ outcomes agree with $dt = 0.1$ |
| Step-energy safeguard over all $33$ runs | PASS | $0$ rejected steps; $73{,}920$ accepted steps; max step energy increase $\le 6.94 \times 10^{-18}$ |
| Stationarity of full endpoints | PASS | max final RHS RMS over $26$ full endpoints $= 1.09975 \times 10^{-15} \le 10^{-7}$ |
| Spatial refinement $K=6$/$N=28$ of threshold runs | NOT RUN | costed as pending (see §7) |
| Larger-box / other $q_{0}^{2}$ / other mean / other total power / longer-time repeats | NOT RUN | costed as pending (see §7) |
| External verification (Manus / Gemini 4 Argon / Academia Co-scientist) | NOT RUN | not run for this local-independent task; Co-scientist parallel output was not read, opened, or used, per the independence instruction |

Runtime: $33$ main runs, total solver time $4267.2$ s, mean $129.3$ s/run, range $78.3$–$186.7$ s (wall time under shared-VM throttling; CPU time per run $\sim 26$ s). Half-dt runs $309.3$ s and $183.1$ s. Peak resident memory $\le 196.8$ MiB per invocation (limit $4$ GiB). No GCP spend: $0$ USD.

## 4. Rival / failure mode

1. **Small direction sample.** Only $3$ random directions were tested. The Wilson intervals are wide: $3/3$ only bounds the population recovery probability above $0.4385$; $0/3$ only bounds it below $0.5615$. A fourth direction could fail at $s = 0.10$ or recover at $s = 0.05$. The bracket $(0.05, 0.10]$ is a statement about these three directions, not a population threshold.
2. **Paired directions are a strength and a limit.** Pairing removes direction as a confounder across $s$, but the three directions share the pilot master seed and the same Gaussian construction; a different direction family (e.g. shell power concentrated in a hex6 or fcc12 subset rather than spread randomly over all $24$ modes) could have a different threshold. This experiment spreads shell power randomly over the whole star; it does not test concentrated-subset starts.
3. **Resolution and box.** One cutoff ($K=4$, $N=18$) and one box ($2\pi$) were used. The pilot's $K=6$ check moved the full-branch energy by only $1.41 \times 10^{-6}$, but no $K=6$ run was done at the threshold itself; a finer cutoff could shift $s_{50}$ or change the mixed point.
4. **Horizon.** $t = 200$ only. A uniform endpoint at $s = 0.05$ is at power $\le 3.5 \times 10^{-149}$ — it cannot recover by growth from that residue — but a full endpoint is stationary, so horizon is not a live risk for these classifications; a much longer run could in principle matter only for a hypothetical slow escape from the full state, which no run shows.
5. **Energy confound.** Initial energy and $s$ are strongly correlated by construction (§2.3). The experiment varies $s$ at fixed total power, so energy is not held fixed; the §2.2 argument (energy ordering fails at fixed $s$) is the evidence against a pure-energy explanation, and it rests on one mixed point.
6. **Corrected basin map.** The prior ws-a Task 5 report called hex6/fcc12 stable attractors; the corrected basin map shows they are saddles at the operating point (negative Hessian directions), not stable attractors. This experiment found no partial-pattern endpoints at any $s$ — consistent with saddles, not traps — but it does not test hex6/fcc12-concentrated starts, so it neither confirms nor refutes the saddle claim directly.

## 5. Evidence that would change the answer

- A fresh direction (new master seed) recovering at $s \le 0.05$, or failing at $s \ge 0.10$, would widen or move the bracket and refute the sharp-step reading.
- A $K=6$/$N=28$ repeat of $s = 0.075$ changing the $2/3$ split, or of $s = 0.05$/$0.10$ changing either endpoint, would move $s_{50}$ or the bracket.
- A shell-power distribution concentrated in a sub-pattern (hex6/fcc12) recovering at lower $s$, or failing at higher $s$, would show the threshold depends on within-shell distribution, not only on $s$.
- If the $s=0.075$ rep-$1$ uniform outcome flipped under half-timestep or $K=6$ refinement, the mixed point — and hence $s_{50}$ — would move; the half-dt check was run only at $s = 0.05$ and $s = 0.15$, not at $s = 0.075$.
- Any sign that the $t=200$ uniform endpoints at $s \le 0.05$ retain a growing shell residue (they do not: final power is $\le 3.5 \times 10^{-149}$) would reopen those classifications.

## 6. HLRE grades (per narrow claim; worst-of shown)

Track E unless noted; independence $I1$ throughout (single artificial pipeline; the independent verifier shares the model, inputs and checkpoints, so it is a second route within one pipeline, not $I2$; no external verification run). No grade rises by itself; the $I1 \to C$ bound is repealed as amended $2026$-$11$-$12$, so grades follow the remaining rules.

| claim | grade | computation (bound / caps / ceiling / record) |
|---|---|---|
| For the three specified directions, recovery is $0/3$ at $s \le 0.05$ and $3/3$ at $s \ge 0.10$ (bracket $(0.05, 0.10]$) | B, Track E, I1 | bound none (I1 bound repealed); caps none (protocol frozen for Stage 1, densification disclosed); ceiling none (measurement, no mechanism postulated); record: $33$ direct runs, $33/33$ independently re-derived, half-dt confirms straddling points |
| Population recovery probability vs $s$ (any $s$), and $s_{50} \approx 0.069$ as a population parameter | C, Track E, I1 | record is the cap: $n=3$ directions, Wilson intervals wide ($[0, 0.5615]$ at $0/3$; $[0.4385, 1]$ at $3/3$); linear interpolation between grid points is an estimator choice, not a measurement |
| Logistic-fit $s_{50} = 0.0710$, profile range $[0.054, 0.086]$ | D (exploratory), Track E, I1 | fit hits the intercept grid boundary ($a = -12.00$) under near-separation; reported only as a consistency check on the linear-interpolation $s_{50}$ |
| All $26$ full endpoints are the pilot full state (same energy, occupancy, lock, RHS) | B, Track E, I1; F2, Track F | $26$ direct endpoints at $-0.007726209285$; independently recomputed from checkpoints (second machine route, F2) |
| Interpolation construction is exact (total power fixed, shell fraction $= s$, endpoints reproduce pilot families) | F2, Track F | asserted and verified in code ($< 10^{-9}$) and by the independent verifier ($33/33$ initial fractions/powers); premise ledger: pilot parameters and seeds re-derived from `parameters.json`/`field_outcomes.csv`, not assumed |
| Solver self-test claims (dealiasing, gradient, dissipation, shell RHS) | F2, Track F | two routes: solver self-tests in every invocation plus independent verifier recomputation; values quoted in §3 |
| Initial-energy table (mean initial energy vs $s$) | F3, Track F | single-route computation (solver diagnostics at $t=0$ only); the verifier recomputed power and shell fraction, not initial energy |
| No partial-pattern endpoint occurs in this interpolation | C, Track E, I1 | record: $0/33$ other outcomes, single protocol/box/power; hex6/fcc12-concentrated starts not tested |
| Threshold persists at other resolutions, boxes, parameters, powers, horizons, or in nature | ABSTAIN | not run; no evidence in this record either way |

## 7. Costed caps for heavy work still pending (no GCP spend)

All caps are local compute, $0$ USD GCP. No GCP spend is requested or authorised by this report.

| pending work | cap (named) | basis |
|---|---|---|
| Full ensemble grid: $s \in \{0.06, 0.07, 0.08, 0.09\}$ $\times n=10$ fresh directions (new master seed), plus the $11$ Stage 1/2 points topped up to $n=10$ ($77$ more runs) — $117$ runs total | $120$ runs, $\sim 4.5$ CPU-hours ($117 \times 129.3$ s $= 15{,}128$ s), $\sim 1.5$ h wall in $4$-way parallel batches, peak $\le 1$ GiB, $0$ USD | measured mean $129.3$ s/run (§3) |
| Spatial refinement: $K=6$/$N=28$ repeats of $s = 0.075$ rep $0$ (full), rep $1$ (uniform), and $s = 0.05$/$0.10$ rep $0$ — $4$ runs | $4$ runs, $20$ min wall, $0$ USD | pilot $K=6$ runs took $112.5$–$128.5$ s each on faster hardware; scaled $\times 4$ for current throttling |
| Longer horizon: $t = 400$ repeats at $s = 0.075$ ($3$ runs) | $3$ runs, $\sim 15$ min wall, $0$ USD | double the $t=200$ cost |
| Half-dt refinement at the mixed point $s = 0.075$ ($3$ runs, $dt = 0.05$) | $3$ runs, $\sim 15$ min wall, $0$ USD | measured half-dt runs $183$–$309$ s |

## 8. UNVERIFIED / ABSTAIN list

- Population recovery probability at any $s$; $s_{50}$ as a population parameter (Wilson intervals in §2.1 are the only population statement).
- Threshold location at $K=6$/$N=28$, in a larger box, at other $q_{0}^{2}$, mean, or $r$, at other total power/RMS, or at $t > 200$.
- Threshold for shell power concentrated in a sub-pattern (hex6, fcc12, six-mode) rather than spread randomly over the star.
- Any claim about $D_{4}$ selection in a physical or cosmological setting; this is one tuned, finite-box, deterministic pilot protocol.
- External verification of this task (Manus / Gemini 4 Argon / Co-scientist): NOT RUN; Co-scientist output for this task was not consulted, preserving independence.
- The hex6/fcc12 saddle claim itself: relied on from the corrected basin map, not re-tested here.

## 9. Assumption / parameter / choice ledger

**Parameters (all verified from the pilot, not assumed):** $r = -0.35$, $\bar{\psi} = -0.18$, $q_{0}^{2} = 8$, $u = v = 1$, $\alpha = 0.1072$, $\beta = 1.54$, $A_{*} = 0.07757529633928076$, matched RMS $= 0.38003978535286725$, total power $= 0.1444302384510534$, master seed $931241112$, per-replicate seeds $1471147641$ (rep $0$), $1605125163$ (rep $1$), $3243489666$ (rep $2$), $N = 18$, $K = 4$, $dt = 0.1$, $t_{\mathrm{final}} = 200$.

**Assumptions:** the pilot functional, box, and operating point are taken as given (not re-derived from the manuscript here); the $D_{4}$ star and $q_{0}$ tuning are imposed, not selected by this calculation; the outcome rule (occupancy/CV/lock/RHS thresholds) is the pilot's, adopted unchanged so endpoints are comparable.

**Choices (frozen before Stage 1 unless noted):** interpolation definition (§1.1); grid $s \in \{0, 0.05, 0.15, 0.30, 0.50, 0.70, 0.90, 1.0\}$; $n = 3$ paired replicates; $t_{\mathrm{final}} = 200$; Wilson intervals; linear-interpolation $s_{50}$. Adaptive (disclosed): Stage 2 points $\{0.075, 0.10, 0.125\}$ chosen after Stage 1. Logistic fit is exploratory only, computed after the fact from the $33$ binary outcomes.

**Withdrawal / demotion note:** (i) The resume logic in `run_threshold.py` compared the stored replicate as a string against an integer, so the $s=0.5$ completion invocation re-appended the rep-$0$ row instead of skipping it (runs $= 4$ recorded in that invocation's `parameters.json`). No run was re-integrated — the checkpoint was reused, values identical — and `merge_threshold.py` de-duplicates by $(s, \mathrm{replicate})$, so the merged $33$-run record is unaffected. The stale `runs_completed = 4` in the main `parameters.json` is corrected by the appended merged record (`runs_completed_merged = 33`). (ii) No other discrepancies: no silent corrections were made to any outcome.

## 10. Deliverables (in this work directory)

- `REPORT.md` — this report.
- `threshold_curve.png` — threshold curve, initial-energy and final-energy panels (regenerated after a legend/label fix; script hash in §10).
- `threshold_outcomes.csv` — one row per run ($33$ runs: $s$, replicate, seed, initial energy, outcome, occupancy, CV, lock, RHS RMS, final energy, elapsed time, steps).
- `threshold_summary.csv` — one row per $s$ point ($11$ rows: counts, recovery fraction, Wilson interval, mean initial energy).
- `threshold_estimate.json` — pre-registered bracket estimators ($s_{\mathrm{last\,zero}} = 0.05$, $s_{\mathrm{first\,full}} = 0.10$, $s_{50} = 0.06875$).
- `verify_outcomes.csv` — independent-verification verdicts ($33/33$ PASS).
- `numerical_tests.json` — solver self-test values (identical in all $11$ invocations).
- `parameters.json` — merged parameter record (see withdrawal note for the stale per-invocation count).
- `run_threshold.py` (sha256 `07b6fd49f765a9514a80533ca4e2c65430a6e6c186d7b1e5866867ac3ada523f`), `verify_outcomes.py` (sha256 `a30b3cb2ec8e2e1a9c2dd121ec7b411d160094557ce31ca2081ec4ec3b32731b`), `merge_threshold.py` (sha256 `d1a146e6d679d890e36260489cdf8e1e3d9f15be593eaaa1b2540da3e5e1bbc5`), `make_figures.py` (sha256 `7622b508f6aaa22a7ca7188a5129871bb29094f3cd98ff549233e9264be45510`).
- `basin_run_study.py` — unmodified copy of the basin-study source (sha256 `837b7ca2891491736d216c9f19a69523823da1d7cc732974de6147994ae409bf`, matching the hash recorded in the pilot `parameters.json`); used only for the shell-RHS self-test. Field solver source hash `a7b03651eb4eb66efa6d59cfc6adfe6021b00b8b73babaa2dfecf154f24ef422`.
- Per-run NPZ checkpoints ($33$ in the main directory; batch sub-directories `batch_low`, `batch_midlow`, `batch_midhigh`, `batch_high`, `dense_0075`, `dense_010`, `dense_0125`, `refine_halfdt` retain their own copies and per-batch tables).
- Nothing was filed, committed, or written into the manuscript or any repo; no git commands were run in the IRH or Jacobian repos; no browser or Academia use; no Co-scientist output was read.
