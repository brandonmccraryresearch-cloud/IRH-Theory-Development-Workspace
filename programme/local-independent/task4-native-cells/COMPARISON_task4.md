# Comparison — Task 4: $D_{4}$ and $A_{4}$* formation on native cells

**Status: COMPARISON PENDING — Academia side not landed.** Checked 2026-11-14 ~03:10 CST: no Co-scientist result files for this task exist in `~/workspace/research/irh/co-scientist-tasks-2026-11-10/` outside `local-independent/`. Do not treat this comparison as complete.

**Local side:** `REPORT.md` in this directory (worker completed 2026-11-14 ~03:06 CST). Coordinator spot-checks re-run 2026-11-14 (conda python 3.11.16, exit 0): $D_{4}$ roots $24$, $A_{4}$* roots $20$; $S_{D_{4}} = 64/141$, $S_{A_{4}^{*}} = 12/31$, margin exactly $73/423$; $\det G_{D_{4}} = 4$, $\det G_{A_{4}} = 5$; covolume ratio $\sqrt{5}/2$ irrational.

## Local result (summary)

- Geometry re-verified exactly (F2 each): no common 4D torus (covolume ratio $\sqrt{5}/2$, irrational); $D_{4}$: $T = 192$, $Q = 3384$, $S = 64/141$; $A_{4}$*: $T = 120$, $Q = 1860$, $S = 12/31$; Gram dets $4$ vs $5$ (scaled $1024$ vs $1280$). $A_{4}$* native cell built from Helmert coordinates, $\det M = 16\sqrt{5}$, all 20 star vectors at integer lattice coords with $|k|^{2} = 8$.
- Paired formation (3 replicates/family, matched quench $r = -0.35$, $\bar{\psi} = -0.18$, $q_{0}^{2} = 8$, RMS $0.38004$, $t = 200$): random starts decay to uniform $6/6$ on both cells. Patterned seeds diverge: $D_{4}$ twelve-mode $\to$ full $3/3$, six-mode $\to$ full $3/3$; **$A_{4}$* twelve-mode $\to$ full $0/3$ — all trapped in a stationary 12-mode state** ($E = -0.00547044$, identified as the $A_{3}$ branch, 2.0% harmonic relaxation), six-mode $\to$ full $2/3$ (one trapped). Full/bridge seeds reach full $3/3$ on both cells. Relaxed full energies: $D_{4}$ $E = -0.00772621$, $A_{4}$* $E = -0.00587749$. Grades **B** (C4–C8); "$A_{4}$* forms less reliably from sub-pattern seeds": **C** ($n = 3$, one quench/band).
- Matching ledger: quench, RMS, seeds, integrator, physical spectral support ($|k|^{2} \le 64$) matched; initial energies and DOF counts **not** matched and quantified (random-matched $E_{0}$: $35$ vs $115$; retained DOF $6560$ vs $660$) — inherent to the different native cells.
- $D_{4}$ arm: prior 4D-field-test trajectories, replicated locally $10/10$ before the local $D_{4}$ run was stopped to spend remaining compute on the new $A_{4}$* arm (logged in report §6.4; completion costed below). General claims (basin fractions, nucleation, thermodynamic limit, other quenches/cells, physical selection): **UNVERIFIED / ABSTAIN**.

## Academia side

PENDING. Launched 2026-11-14 as "Test $D_{4}$ and $A_{4}$* formation on native cells". No files landed yet.

## Per-number comparison checklist (complete when Academia lands)

| # | Quantity | Local value (grade) | Academia value | Agree? | Better supported | Settles |
|---|---|---|---|---|---|---|
| 1 | No common torus / Gram dets | $4$ vs $5$; ratio $\sqrt{5}/2$ (F2) | | | | Exact arithmetic; any disagreement here is an error on one side |
| 2 | $A_{4}$* twelve-mode outcome | $0/3$ full, trapped at $E = -0.00547044$ (B) | | | | The trap is the headline: does Academia also see a stationary 12-mode trap, and at the same energy? |
| 3 | $D_{4}$ twelve-mode / six-mode outcome | $3/3$ full both (B) | | | | |
| 4 | $A_{4}$* six-mode outcome | $2/3$ full (C, $n = 3$) | | | | Small-$n$; a larger ensemble on either side settles this |
| 5 | Random-start outcome | $6/6$ uniform both cells (B) | | | | |
| 6 | Relaxed full energies | $-0.00772621$ ($D_{4}$) vs $-0.00587749$ ($A_{4}$*) (B) | | | | Must match if the same states are reached |
| 7 | Trap identification | $A_{3}$ branch, 2.0% harmonic relaxation (B) | | | | A different trap ID would be a real disagreement, not a rounding difference |
| 8 | Matching ledger | DOF $6560$ vs $660$; $E_{0}$ $35$ vs $115$ (B, ledgered) | | | | If Academia claims "matched" without these numbers, its matching is weaker |

## S3 invariance alignment (cross-domain-discovery)

Do both derivations reduce to the same equations? Both sides should reduce to the same conserved Model B dynamics on each star's native cell. The alignment questions: the $A_{4}$* cell construction (Helmert coordinates, $\det M = 16\sqrt{5}$), the physical band cap ($|k|^{2} \le 64$ — added locally after a failed self-test showed the uncapped $A_{4}$* tensor band reaches $|k|^{2} = 896$), and the matching protocol (RMS matched, DOF/energy not matched). The DOF mismatch is the critical S3 fact: the two cells differ in volume by $16\sqrt{5}$, so per-cell mode counts differ even though per-unit-volume densities are comparable. A comparison that ignores this would be comparing different effective resolutions.

## S4 Bartha articulation + transportability audit

- Transfer "onset advantage $\to$ dynamical selection": **not established** — the local side's C5b is C ($n = 3$, one quench/band); the trap is a dynamical difference in the same direction as the onset advantage, not a proof of selection in general.
- Transfer "trap at one quench $\to$ trap in general": **not established** — one quench point, one band; the second quench point ($\delta = 0.25$) is costed, not run.
- The local report's one traced failure: the first $A_{4}$* smoke run failed its dissipation-identity assertion (absolute error $4.6\times10^{-5}$); the identity was correct (relative error $4\times10^{-16}$) and the fault was the uncapped band — documented, no uncapped results used. The runtime-recorded failed exec calls for this worker are consistent with that diagnostic smoke run.

## 8-check rubric (local side, as far as assessable now)

1. Independent test exists — PASS in part: geometry 24/24 PASS; self-tests both stars; refinements 6/6 agree in outcome class; Academia comparison pending.
2. Falsification boundary stated — PASS: trap reproducing under half-dt and $K = 6$ refinement is the stated non-artefact test.
3. Bartha articulation passes — PASS for the stated transfers (selection transfer not claimed).
4. Transportability audited — PARTIAL: matching ledger complete; no formal selection diagram; other quenches/cells ABSTAIN.
5. Second independent tool — PASS: geometry verified by independently written basis matrices; coordinator spot-checks independently confirmed the exact-arithmetic geometry (exit 0).
6. No invented numbers — PASS: all numbers trace to run tables; the $D_{4}$-arm stop is logged, not hidden.
7. Assumption ledger complete — PASS as reported (band cap, DOF/energy mismatch ledgered); coordinator did not re-audit every ledger line.
8. Grade honest — PASS: C5b capped at C; C9 ABSTAIN.

## Grade cap

This comparison report caps at **C (Track E) / F3 (Track F)** per the cross-domain-discovery skill's own grade cap until human source/balance gates are run. The comparison itself is a scaffold until the Academia side lands.

## What would settle the difference

Academia landing with the outcome table per family/star and the trap energy; 10 replicates/family/star (costed, cap 2,200 solver-s); completing the local $D_{4}$ arm (cap 1,800 solver-s, ~65 min wall); a second quench point (cap 1,500 solver-s); the wider-band $K = 6$ study (cap 6,000 solver-s).
