# Comparison — Task 5: Spectral-power threshold for full $D_{4}$ formation

**Status: COMPARISON PENDING — Academia side not landed.** Checked 2026-11-14 ~03:10 CST: no Co-scientist result files for this task exist in `~/workspace/research/irh/co-scientist-tasks-2026-11-10/` outside `local-independent/`. Do not treat this comparison as complete.

**Local side:** `REPORT.md` in this directory (worker completed 2026-11-14 ~02:43 CST). Coordinator spot-check re-run 2026-11-14: `verify_outcomes.py`, conda python 3.11.16, exit 0 — **VERIFY 33/33** (all 33 run files reclassified independently from raw NPZs, endpoints re-derived, no partial endpoints).

## Local result (summary)

- Fixed total power, shell-fraction $s$ interpolated between shell-random and spread-spectrum spectra (ETD2, $\Delta t = 0.04$, $t = 200$): recovery $0/3$ at $s \le 0.05$, $2/3$ at $s = 0.075$, $3/3$ at every $s \ge 0.10$ ($n = 3$ per point, 11 points, 33 runs). Hull bracket on $s_{\mathrm{crit}}$: $(0.05,\ 0.10]$, with $s_{50} \approx 0.069$ (logistic estimate). Grade **B** (direction-specific bracket); **C** (population $s_{50}$); **D** (logistic fit, exploratory).
- Direction matters beyond $s$ and energy at the mixed point: the $s = 0.075$ $2/3$ outcome comes from direction 1 only, and post-hoc box-plot differences are not established.
- Interpolation reproducibility and solver checks: **F2** (refresh $0.9995$; all 33 endpoints re-derived by an independent script; 1.00 interpolation fraction with exact paired-off-shell recompute; half-dt straddling confirmations at $s = 0.05, 0.10$; dot-product and energy-gradient self-tests $10^{-11}$–$10^{-15}$).
- Inconclusive: population-cumulative exposure of the hidden $0.60$ shell fraction was not measured. The straddling point reflects the $0.20$ mixed-composition effect, not a reporting defect.
- Solver checks **F2**; general claims beyond the sampled directions: **ABSTAIN**.

## Academia side

PENDING. Launched 2026-11-14 as "Find the spectral-power threshold for full $D_{4}$ formation". No files landed yet.

## Per-number comparison checklist (complete when Academia lands)

| # | Quantity | Local value (grade) | Academia value | Agree? | Better supported | Settles |
|---|---|---|---|---|---|---|
| 1 | Bracket on $s_{\mathrm{crit}}$ | $(0.05,\ 0.10]$, direction-specific (B) | | | | Must be compared at the same interpolation and matched values ($0.30$ vs $0.20$ dependence is checked) |
| 2 | $s_{50}$ | $\approx 0.069$ (C) | | | | Population parameter of logistic regression; large-sample uncertainty interval |
| 3 | Recovery fractions per $s$ | $0/3$ ($\le 0.05$), $2/3$ ($0.075$), $3/3$ ($\ge 0.10$) | | | | Binomial sampling noise is the first explanation for a one-point disagreement |
| 4 | Endpoint energies (full pattern) | $E = -0.00772620928487$ (F2) | | | | Must match the relaxed full-24 value |
| 5 | Solver/check values | Refresh $0.9995$; half-dt straddling confirmations (F2) | | | | |
| 6 | Direction/mixed-point effect | Direction and mixed point are not identical effects (B) | | | | A comparison that only reports $s$ without direction is not the same measurement |

## S3 invariance alignment (cross-domain-discovery)

Do both derivations reduce to the same equations? Both sides should reduce to the same Model B dynamics with the same interpolation between shell-random and spread-spectrum initial spectra at fixed total power. The alignment questions: the interpolation definition (same mixing rule, same paired directions), the ensemble ($n = 3$ per point locally), and the outcome classification (full stationary pattern vs uniform vs partial — no partial endpoints occurred locally, so the classification is clean). If Academia used a different mixing rule or a different outcome threshold, its $s_{\mathrm{crit}}$ is a different quantity.

## S4 Bartha articulation + transportability audit

- Transfer "direction-specific bracket $\to$ population threshold": **capped at C** — $n = 3$ per point, 2 conflated points remembered; Wilson intervals used.
- Transfer "bracket $\to$ other boxes/params": **ABSTAIN** — the $K = 6$ / $N = 28$ refinement and $t = 400$ repeats are costed, not run.
- Selection-diagram note: no formal diagram built; the $S$-nodes (sample size, direction, mixed composition) are named in the report.

## 8-check rubric (local side, as far as assessable now)

1. Independent test exists — PASS: independent verifier 33/33 re-derived from raw NPZs, re-run by the coordinator to exit 0; Academia comparison pending.
2. Falsification boundary stated — PASS: half-dt confirmation of both straddling points; a $t = 400$ shift would count against the bracket.
3. Bartha articulation passes — PASS for the stated transfers (population transfer capped, cross-box transfer not claimed).
4. Transportability audited — PARTIAL: direction/mixed effects named; no formal selection diagram.
5. Second independent tool — PASS: `verify_outcomes.py` is an independent re-implementation re-run by the coordinator.
6. No invented numbers — PASS: all numbers trace to run tables.
7. Assumption ledger complete — PASS as reported; coordinator did not re-audit every ledger line.
8. Grade honest — PASS: logistic fit graded D, $s_{50}$ graded C, inconclusive items stated.

## Grade cap

This comparison report caps at **C (Track E) / F3 (Track F)** per the cross-domain-discovery skill's own grade cap until human source/balance gates are run. The comparison itself is a scaffold until the Academia side lands.

## What would settle the difference

Academia landing with per-$s$ recovery fractions and the interpolation definition; the full ensemble grid (120 runs, $\approx 4.5$ CPU-hours, local-only, no GCP); $K = 6$ / $N = 28$ refinement; $t = 400$ and half-dt repeats; a hidden $0.60$ shell-fraction exposure measurement.
