# Comparison — Task 2: $D_{4}$ grain locking in a larger four-dimensional box

**Status: COMPARISON PENDING — Academia side not landed.** Checked 2026-11-14 ~03:10 CST: no Co-scientist result files for this task exist in `~/workspace/research/irh/co-scientist-tasks-2026-11-10/` outside `local-independent/`. Do not treat this comparison as complete.

**Local side:** `REPORT.md` in this directory (worker completed 2026-11-14 ~03:04 CST).

## Local result (summary)

- In the $L = 4\pi$ box ($16\times$ pilot volume, shell $|m|^{2} = 32$, exactly the 24 vectors $(\pm 4, \pm 4, 0, 0)$ and permutations), independently shifted $D_{4}$ patches heal into a single coherent stationary pattern within a few time units. All five full-24 configs (A–E) end in the identical stationary full-24 state, energy $E = -0.00772620928487$, matching the pilot to all 15 digits. Grades **B** (run-specific claims C1–C5, C7).
- Antiphase patches heal to a pattern translated by $+\lambda/4$, exactly halfway between the patches. The ordered half invades the uniform half by $t = 2$.
- A genuine orientation grain (two hex6 sub-patterns in different planes) does **not** heal to full-24: the two hex grains fuse into the stationary 12-mode FCC cross-section pattern ($E = -0.00546783498566$ full tier).
- **Withdrawal:** configs C/D "rotations" were vacuous — the star sum is invariant under hyperoctahedral permutations — so they tested translation mismatches only. No grade is claimed for a full-24 orientation grain; none was run. General claim "local $D_{4}$ order joins into one coherent pattern in larger boxes": **C**.
- Slab RMS as a boundary diagnostic: **CONTRADICTED**.

## Academia side

PENDING. Launched 2026-11-14 as "Track $D_{4}$ grain locking in a larger four-dimensional box". No files landed yet.

## Per-number comparison checklist (complete when Academia lands)

| # | Quantity | Local value (grade) | Academia value | Agree? | Better supported | Settles |
|---|---|---|---|---|---|---|
| 1 | Final energy, healed full-24 | $-0.00772620928487$ (B) | | | | Must match the pilot relaxed value if the same state is reached |
| 2 | Healing time / energy at final value | $t = 2$–$5$, frozen to $t = 100$ | | | | Slower healing or non-stationary endpoints would disagree |
| 3 | Antiphase healed translation | $+\lambda/4$ | | | | A different translation, or phase disorder, would be a real disagreement |
| 4 | Orientation-grain outcome | Fuses to stationary fcc12, $E = -0.00546783498566$ (B, run-specific) | | | | If Academia's orientation grain heals to full-24, the grain definitions differ — check mode sets first |
| 5 | Grain-boundary signature | Slab RMS CONTRADICTED as a diagnostic | | | | Any boundary measure must beat the pattern's own $x_{1}$-ripple |
| 6 | Overlaps / shell power trajectories | $O = 0.722$ (antiphase), $0.586$–$0.802$ (shifts) | | | | |

## S3 invariance alignment (cross-domain-discovery)

Do both derivations reduce to the same equations? Both sides should reduce to conserved Model B with the same operator ($\alpha = 0.1072$, $\beta = 1.54$) on a periodic box. The alignment questions: box size ($L = 4\pi$ locally — what did Academia use?), shell identification (clean 24-vector shell at $|m|^{2} = 32$), patch construction (partition of unity, renormalisation), and spectral tier/band. If Academia used a different box (e.g. $L = 6\pi$, whose $|m|^{2} = 72$ shell has 312 vectors and is not a clean $D_{4}$ shell), the outcomes are not directly comparable. The local C/D withdrawal is an S3-relevant fact: "rotation" of the full star is a symmetry, so any Academia claim of a tested orientation mismatch must be checked against the same invariance.

## S4 Bartha articulation + transportability audit

- Transfer "translation healing in $4\pi$ box $\to$ general coherence in larger boxes": **capped at C** — single replicate per config, one box size, horizon $t = 100$, no thermal escape tested.
- Transfer "hex6-orientation fusion $\to$ fcc12 is the generic orientation-grain outcome": **not established** — config F is post-hoc relative to A–E; one pair of sub-patterns only.
- Selection-diagram note: no formal diagram built; transport across box sizes is the open question the pending $L = 8\pi$ run (costed, needs a memory-lean rewrite + GCP approval) would address.

## 8-check rubric (local side, as far as assessable now)

1. Independent test exists — PASS in part: second independently written tool re-derived all 11 runs to $10^{-9}$; half-dt check on B; Academia comparison pending.
2. Falsification boundary stated — PASS: frozen predictions P1–P3 written before running; P1 passed at the full tier, failed at the cheap tier (recorded, not silently corrected).
3. Bartha articulation passes — PASS for the stated transfers (general-coherence transfer capped, orientation transfer not claimed).
4. Transportability audited — PARTIAL: box-size transport explicitly open; no formal selection diagram.
5. Second independent tool — PASS: `check_energy_independent.py` (NumPy-only) on all runs.
6. No invented numbers — PASS: all numbers trace to run tables.
7. Assumption ledger complete — PASS as reported; coordinator did not re-audit every ledger line.
8. Grade honest — PASS: withdrawal ledgered, C6 capped at C, C8 CONTRADICTED stated plainly.

## Grade cap

This comparison report caps at **C (Track E) / F3 (Track F)** per the cross-domain-discovery skill's own grade cap until human source/balance gates are run. The comparison itself is a scaffold until the Academia side lands.

## What would settle the difference

Academia landing with per-config final energies, overlaps, and healing times at a stated box size; replicates ($n > 1$ per config) on either side; the $L = 8\pi$ run (costed, pending); an annealed/thermal escape test for the fcc12 fused state.
