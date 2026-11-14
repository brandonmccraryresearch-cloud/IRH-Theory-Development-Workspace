# Comparison — Task 6: Bloch growth around the relaxed $D_{4}$ wave

**Status: COMPARISON PENDING — Academia side not landed.** Checked 2026-11-14 ~03:10 CST: no Co-scientist result files for this task exist in `~/workspace/research/irh/co-scientist-tasks-2026-11-10/` outside `local-independent/`. Do not treat this comparison as complete.

**Local side:** `REPORT.md` in this directory (worker completed 2026-11-14 ~02:38 CST).

## Local result (summary)

- Relaxed field reproduced locally to $1.3\times10^{-13}$ in energy by an independent implementation of the stated checkerboard rule; growth map computed for 259 distinct Bloch wavevectors (one eighth-octant of the Brillouin zone).
- Growth map result: **no positive growth rate at any sampled $q$** (least-damped rates $-1.332276$ at $q = (0.32, 0.32, 0.32, 0)$). Grade **C** (sampled-map stability only).
- The frozen-ansatz $\mathbf{A}^{6}$ quartet (positive rate $+0.0228772435$ at $q = (0.23, 0.23, 0.23, 0)$) does **not** survive relaxation — a nonstationarity artefact: the frozen-ansatz residual is $2.5\times10^{-3}$ (larger than the perturbation amplitudes) and the quartet sits $21\%$ outside the band that is legitimate for the linear operation acting on the stationary state.
- Analytic channels: Goldstone zeros ($6\times10^{-11}$ signed max; predicts $\lambda = 0$); conserved-mean slope matches Schur-complement prediction ($-64.26$ vs $-64.255220$, $-64.25523$ at zero wavevector, $0.01\%$). Long-wave: $\lambda_{T}/|q|^{2} \to -42.4$, $\lambda_{L}/|q|^{2} \to -128.0$.
- Grades: reproduction/zeros/slopes **F2**; sampled-map stability **C**; continuum stability for all $q$ and the full dynamics: **ABSTAIN**.

## Academia side

PENDING. Launched 2026-11-14 as "Map Bloch growth around the relaxed $D_{4}$ wave". No files landed yet. (This is the same gap named in the 2026-11-13 proactivity item — the relaxed-state stability ABSTAIN left open by G-A6.)

## Per-number comparison checklist (complete when Academia lands)

| # | Quantity | Local value (grade) | Academia value | Agree? | Better supported | Settles |
|---|---|---|---|---|---|---|
| 1 | Largest growth rate over sampled map | $\le 0$ everywhere; least-damped $-1.332276$ at $q = (0.32, 0.32, 0.32, 0)$ (C) | | | | A positive rate on Academia's side must first be checked against the relaxation question (row 3) |
| 2 | Frozen-ansatz $\mathbf{A}^{6}$ quartet | $+0.0228772435$, does NOT survive relaxation (F2) | | | | If Academia's rates are about a frozen ansatz, they are not stability of the relaxed state |
| 3 | Residual of the reference state | Frozen ansatz $2.5\times10^{-3}$ vs relaxed state $1.1\times10^{-5}$ | | | | The state a Bloch analysis is about must be stated; rates about a nonstationary state are artefacts |
| 4 | Goldstone zeros | $6\times10^{-11}$ signed max (F2) | | | | A failure here indicates a wrong reference state or operator |
| 5 | Conserved-mean slope | $-64.26$ vs $-64.255220$ (0.01%) (F2) | | | | |
| 6 | Long-wave branch slopes | $\lambda_{T}/|q|^{2} \to -42.4$, $\lambda_{L}/|q|^{2} \to -128.0$ (F2) | | | | |
| 7 | Relaxed-field reproduction | Energy to $1.3\times10^{-13}$ (F2) | | | | If the relaxed states differ, the maps are not comparable |

## S3 invariance alignment (cross-domain-discovery)

Do both derivations reduce to the same equations? The Bloch map reduces to the linearisation of the same Model B operator about a reference state — but the reference state is the whole question. The local side computed about the *relaxed* field; the earlier $\mathbf{A}^{6}$ quartet was about a *frozen ansatz*. If Academia linearises about the frozen ansatz, its positive rates and the local map disagree for a stated reason (nonstationarity artefact), and the comparison must say so rather than vote. Alignment questions: reference state (relaxed vs frozen), Bloch operator (Schur complement, mean projection), band (legitimate for the operator), and $q$ sampling (259-point octant locally, 0.01-step cuts pending).

## S4 Bartha articulation + transportability audit

- Transfer "sampled-map stability $\to$ continuum stability for all $q$": **FAILS as proof** (ABSTAIN) — 259 sampled points do not cover the zone; the dense 4D map is costed, not run.
- Transfer "frozen-ansatz rates $\to$ relaxed-state stability": **FAILS** — shown by the residual and out-of-band arguments.
- Selection-diagram note: no formal diagram built; the $S$-node that matters is the reference-state stationarity.

## 8-check rubric (local side, as far as assessable now)

1. Independent test exists — PASS in part: reproduction to $10^{-13}$ by an independent implementation; Academia comparison pending.
2. Falsification boundary stated — PASS: a positive rate about the relaxed state at any sampled $q$ would falsify the no-growth result; one is absent.
3. Bartha articulation passes — PASS for the stated transfers (both named transfers fail, and the failures are the result).
4. Transportability audited — PARTIAL: dense-map coverage stated as the open step; no formal selection diagram.
5. Second independent tool — PASS: cross-checks by mpmath (Schur complements) and exact fractions.
6. No invented numbers — PASS: all numbers trace to run tables.
7. Assumption ledger complete — PASS as reported; coordinator did not re-audit every ledger line.
8. Grade honest — PASS: continuum stability graded ABSTAIN, not inferred from the sampled map.

## Grade cap

This comparison report caps at **C (Track E) / F3 (Track F)** per the cross-domain-discovery skill's own grade cap until human source/balance gates are run. The comparison itself is a scaffold until the Academia side lands.

## What would settle the difference

Academia landing with its reference state, residual, and per-$q$ rates; the dense 4D map ($\approx 2$ h on 4 workers local, or $\approx \$2.44$ GCP — needs approval); dense 0.01-step cuts ($\approx 10$ min, local); an interval-certified enclosure (cost TBD).
