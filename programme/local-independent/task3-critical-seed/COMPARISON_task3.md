# Comparison — Task 3: Critical $D_{4}$ seed in the full field

**Status: COMPARISON PENDING — Academia side not landed.** Checked 2026-11-14 ~03:10 CST: no Co-scientist result files for this task exist in `~/workspace/research/irh/co-scientist-tasks-2026-11-10/` outside `local-independent/`. Do not treat this comparison as complete.

**Local side:** `REPORT.md` in this directory (worker completed 2026-11-14 ~02:29 CST).

## Local result (summary)

- Field threshold (direct, full 4D field, $L = 2\pi$ box, $\alpha = 1$): $R_{c,\mathrm{field}} \in (2.5875,\ 2.625]$, bracket width $0.0375$; $R_{\mathrm{eq}} \in (2.483,\ 2.521]$. Dissolve at $R \le 2.5875$, grow to the stationary full 24-mode state at $R \ge 2.625$. Grade **B**.
- Growing endpoints reach rms $0.380535$, $F_{\mathrm{exc}} = -0.007726209285$; dissolving endpoints reach rms $\sim 10^{-75}$. Decisions fast (rms crosses thresholds by $t \approx 5$–$10$, horizon $t = 200$). $\alpha = 1.5$ does not rescue small seeds ($R = 0.6$–$1.5$ all dissolve): **C**.
- Envelope comparison, stated not conflated: radial-ODE $R_{c} = 12.57$, envelope seed threshold $(16.19, 16.21]$, saddle $R_{\mathrm{eq}} = 13.53$ — $4.8\times$–$6.2\times$ the field bracket. Different regimes: envelope is infinite-domain with a $w = 6$ wall; the field bracket is a finite-box threshold with an image-assisted patch nearly filling the box. No field result here supports or refutes the envelope nucleation picture.
- Shell-fraction scaling explains why the $L = \pi$ box grew at $R \ge 0.8$ while the $2\pi$ box dissolves to $R = 2.5875$ ($0.29$ vs $0.023$ at $R = 1.2$): **B**.
- Infinite-volume critical radius from the field, any nucleation rate/waiting time: **ABSTAIN**.

## Academia side

PENDING. Launched 2026-11-14 as "Measure the critical $D_{4}$ seed in the full field". No files landed yet.

## Per-number comparison checklist (complete when Academia lands)

| # | Quantity | Local value (grade) | Academia value | Agree? | Better supported | Settles |
|---|---|---|---|---|---|---|
| 1 | Field bracket $R_{c,\mathrm{field}}$ | $(2.5875,\ 2.625]$ at $\alpha = 1$, $L = 2\pi$ (B) | | | | Must be compared at the same box, amplitude, and envelope width — a different box is a different measurement |
| 2 | Equivalent sharp-ball radii | $R_{\mathrm{eq}} \in (2.483,\ 2.521]$ | | | | |
| 3 | $\alpha$-dependence | $\alpha = 1.5$ no rescue at $R \le 1.5$ (C, coarse) | | | | A rescue at small $R$ would disagree; a bracket at larger $R$ would refine |
| 4 | Envelope numbers (quoted) | ODE $12.57$, seed $(16.19, 16.21]$, saddle $13.53$ (B, quoted not re-derived) | | | | Agreement here only checks the shared prior work, not the new bracket |
| 5 | Box-size scaling | Shell fraction $0.29$ ($\pi$ box) vs $0.023$ ($2\pi$ box) at $R = 1.2$ (B) | | | | This scaling is the first thing to check if Academia's bracket differs |
| 6 | Growing-endpoint energy | $F_{\mathrm{exc}} = -0.007726209285$ | | | | Must match the relaxed full-24 value if the same state is reached |

## S3 invariance alignment (cross-domain-discovery)

Do both derivations reduce to the same equations? The field bracket reduces to conserved Model B in a finite periodic box with a localised seed; the envelope prediction reduces to a radial ODE on an infinite domain. They do **not** reduce to the same equations — that is the local side's central point, and the comparison must not force agreement between them. The alignment question for Academia is which regime its number lives in: box size, envelope width $w$, amplitude $\alpha$, and whether periodic images assist. If Academia reports a single "critical radius" without stating the box, the number is uninterpretable as a comparison.

## S4 Bartha articulation + transportability audit

- Transfer "field bracket $\to$ infinite-volume $R_{c}$": **FAILS** — the box cannot contain an envelope-scale droplet; stated by the local side.
- Transfer "seed threshold $\to$ nucleation rate": **FAILS** — deterministic runs, no noise; waiting times ABSTAIN.
- Selection-diagram note: no formal diagram built; the $S$-nodes that differ between regimes (box size, wall width, amplitude) are named in the report's ledgers.

## 8-check rubric (local side, as far as assessable now)

1. Independent test exists — PASS in part: independent semi-implicit solver reproduces both bracket ends; half-dt both endpoints; $K = 6$ check on the growing endpoint; Academia comparison pending.
2. Falsification boundary stated — PASS: a bracket endpoint flipping under half-dt or $K = 6$ would have counted against it.
3. Bartha articulation passes — PASS for the stated transfers (both named transfers fail, and the failures are the result).
4. Transportability audited — PARTIAL: regime difference stated and quantified; no formal selection diagram.
5. Second independent tool — PASS: two integrators + two quadratures for surrounding arithmetic.
6. No invented numbers — PASS: all numbers trace to run tables.
7. Assumption ledger complete — PASS as reported; coordinator did not re-audit every ledger line.
8. Grade honest — PASS: ABSTAIN stated for the infinite-volume radius and rates.

## Grade cap

This comparison report caps at **C (Track E) / F3 (Track F)** per the cross-domain-discovery skill's own grade cap until human source/balance gates are run. The comparison itself is a scaffold until the Academia side lands.

## What would settle the difference

Academia landing with a bracket at a stated box/amplitude/width; the larger-box $L = 4\pi$ bracket (costed, $\sim 10$ runs, $\sim 10$ h wall, \$0); the $L = 6\pi$ box to contain the $16.2$ envelope threshold (GCP-scale, cap to be named); a wide-wall ($w = 6$) field seed.
