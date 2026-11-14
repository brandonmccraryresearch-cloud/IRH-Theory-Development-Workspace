# Comparison — Task 7: Discriminating three-dimensional $D_{4}$ peak ratios

**Status: COMPARISON PENDING — Academia side not landed.** Checked 2026-11-14 ~03:10 CST: no Co-scientist result files for this task exist in `~/workspace/research/irh/co-scientist-tasks-2026-11-10/` outside `local-independent/`. Do not treat this comparison as complete.

**Local side:** `REPORT.md` in this directory (worker completed 2026-11-14 ~02:39 CST).

## Local result (summary)

- $A_{1} = I(111)/I(200)$ and $A_{3} = I(100)/I(111)$ **survive** as discriminants: $A_{1}$ $26\times$–$182\times$ (from the smallest value $1/2.84 = 0.352$ to the largest $64$) and $A_{3}$ up to $941\times$ face-to-cover discrimination. $A_{2}$ and $A_{4}$ **fail**. Grades: arithmetic claims **F2**; "measurable discriminants" **C** (post-hoc ratio selection, no detector/noise model).
- Cut-and-project: $C_{2}$–$C_{4}$ survive as $h$-discriminants ($C_{2}$ = 1 vs 2.84 = 2.5×; $C_{3}$ = 1 vs 1.99); $C_{1}$ marginal for $L = 4$ and $6$ (1.00 vs 1.41 and 1.00 vs 1.42) and fails at $L = 2$.
- Cut-and-project scattering: $I_{\mathrm{CPS}}(111) \le 1.3\times10^{-4}$ (suppression $\ge 7{,}763\times$) — decisive; $I_{\mathrm{CPS}}(200)$ weaker ($19\times$–$1{,}106\times$, diverging from the analytic $16$). Ratios between two CPS leakages unstable by $>10\times$ — demoted to a **documented failure**.
- Ideal-window FFT is exact to $1.5\times10^{-8}$; a rectangular window spreads the $I_{100}$ peak by $184\times$ (F2). Resolution: strong-peak minimum separation $0.272440$ cycles/unit; Hann $L = 4$ closest pair (111)/(200) is marginal (only a 22% dip).
- $F_{1} = 4$, $F_{2} = 285.49$, $R^{*} = \sqrt{113}/5 = 2.1255879775711645$ (≥1 by $\sim 112$%).
- No heavy work pending ($\approx 83$ s total, \$0).
- Any claim about measured discriminants without a detector/window model: **ABSTAIN** beyond the stated C.
- The $A_{2}$ failure was the finding from the earlier CS task 7 (2026-11-12), not repeated here.

## Academia side

PENDING. Launched 2026-11-14 as "Extract discriminating three-dimensional $D_{4}$ peak ratios". No files landed yet.

## Per-number comparison checklist (complete when Academia lands)

| # | Quantity | Local value (grade) | Academia value | Agree? | Better supported | Settles |
|---|---|---|---|---|---|---|
| 1 | $A_{1} = I(111)/I(200)$ discrimination | Survives, $26\times$–$182\times$ per section (C) | | | | Survival must be checked per section and per window, not as a single number |
| 2 | $A_{3} = I(100)/I(111)$ discrimination | Survives, up to $941\times$ (C) | | | | |
| 3 | $A_{2}$, $A_{4}$ | Fail (F2) | | | | If Academia reports them surviving, check window/resolution definitions first |
| 4 | $C_{1}$–$C_{4}$ ($h$-discriminants) | $C_{2}$–$C_{4}$ survive; $C_{1}$ marginal/fails at $L = 2$ | | | | |
| 5 | CPS (111) suppression | $\le 1.3\times10^{-4}$, $\ge 7{,}763\times$ (F2) | | | | |
| 6 | CPS (200) suppression | $19\times$–$1{,}106\times$, diverges from analytic $16$ (F2) | | | | A single reported value without the energy-evolution note is incomplete |
| 7 | Inter-leakage ratios | Unstable $>10\times$ — demoted failure (B) | | | | Any Academia ratio of two leakages must show its stability |
| 8 | Resolution | Min separation $0.272440$ cycles/unit; Hann $L = 4$ marginal (22% dip) (F2) | | | | |

## S3 invariance alignment (cross-domain-discovery)

Do both derivations reduce to the same equations? Ratios reduce to sinc² kernels applied to atomic sums for the ideal window — that part is arithmetic, and should be identical on both sides. The alignment questions are the definitions: DC normalization, section vs projection, window (ideal vs rectangular vs Hann), and $L$. A rectangular window spreads $I_{100}$ by $184\times$, so a ratio computed without a stated window is not comparable to one with a stated window. The CPS leakage values are a separate regime (cut-and-project), and must not be compared against FFT section ratios.

## S4 Bartha articulation + transportability audit

- Transfer "synthetic-kernel ratio $\to$ measurable discriminant": **capped at C** — post-hoc ratio selection, no detector/noise model, no second perturbation direction.
- Transfer "FFT-measured ratio $\to$ true ratio": **FAILS for a rectangular window** (184× spread); holds for the ideal window ($1.5\times10^{-8}$).
- Selection-diagram note: no formal diagram built; the $S$-nodes (window, $L$, section/projection) are named in the report.

## 8-check rubric (local side, as far as assessable now)

1. Independent test exists — PASS in part: verified against closed-form `sinc` and analytic baseline; second tool (SymPy + exact rational arithmetic) on low-crash rows; Academia comparison pending.
2. Falsification boundary stated — PASS: inter-leakage instability was demoted on its own failure note; $A_{2}$/$A_{4}$ failures stated.
3. Bartha articulation passes — PASS for the stated transfers (measurement transfer capped, rectangular-window transfer fails).
4. Transportability audited — PARTIAL: window dependence quantified; no formal selection diagram.
5. Second independent tool — PASS: SymPy/exact rational arithmetic and a verified plot geometry.
6. No invented numbers — PASS: all numbers trace to run tables; the $A_{2}$ failure is attributed to the earlier CS task 7, not re-measured here.
7. Assumption ledger complete — PASS as reported; coordinator did not re-audit every ledger line.
8. Grade honest — PASS: "measurable discriminants" graded C, inter-leakage ratios demoted.

## Grade cap

This comparison report caps at **C (Track E) / F3 (Track F)** per the cross-domain-discovery skill's own grade cap until human source/balance gates are run. The comparison itself is a scaffold until the Academia side lands.

## What would settle the difference

Academia landing with its per-$L$, per-$h$, per-window ratio table; a detector/noise model on either side; a second perturbation direction (quoted but unspecified).
