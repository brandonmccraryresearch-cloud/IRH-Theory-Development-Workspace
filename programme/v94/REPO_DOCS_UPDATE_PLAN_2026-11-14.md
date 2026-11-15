# Repo-docs update plan for the IRH v94 update

**Date:** 2026-11-14
**Author:** Worker C (plan only — no file edited)
**Scope:** per-file update proposals for the six repo documents listed below, against
the 2026-11-14 advances (Co-scientist follow-on audits + local independent
reproduction + Gemini sweeps 5/6 audits + close-the-gaps / Puiseux programme
items). Edits come in a later wave, once the advances ledger lands.

## Conventions

- Each proposal gives: section/heading, current text (short verbatim quote),
  proposed new text, evidence citation (file path), and grade status.
- **PROPOSED GRADE** marks any proposal that involves a grade change or a new
  grade assignment. Per HLRE v5.1, grade changes are Brandon's call; everything
  marked PROPOSED is evidence only, never decided here. No grade was changed by
  any auditor in the 2026-11-14 programme.
- Evidence citations point at the audit files, not at this plan. Where a fact
  comes from the task context rather than a file on disk, the citation says so
  and the advances ledger is asked to confirm it.
- "No change" entries are stated explicitly so the later wave does not revisit
  them as open questions.
- All mathematics is in `$...$` or `$$...$$` delimiters.

## Evidence base (read for this plan)

- `~/workspace/research/irh/co-scientist-tasks-2026-11-10/CONSOLIDATED_COMPARISON_2026-11-14.md`
  (314 claims: 277 VERIFIED, 10 VERIFIED WITH CORRECTION, 4 REFUTED,
  20 UNVERIFIED, 1 ABSTAIN; 8 of 10 tasks audited; grain-locking and
  spectral-threshold BLOCKED, no files)
- `~/workspace/research/IRH-Theory-Development-Workspace/programme/AUDIT_gemini-sweep-g-c21_2026-11-12.md`
- `~/workspace/research/IRH-Theory-Development-Workspace/programme/AUDIT_gemini-sweep-g-d6_2026-11-13.md`
- `~/workspace/research/IRH-Theory-Development-Workspace/programme/AUDIT_gemini-sweep-g-d10_2026-11-12.md`
- `~/workspace/research/IRH-Theory-Development-Workspace/programme/AUDIT_batch2_2026-11-12.md`
  (cited via the gap inventory for Batch 2 verdicts)

## Advances that touch none of these six documents

- Close-the-gaps HYBRID settlement, Phase 1 landed, (P2) settled proved
  (grade B / I1), Puiseux Phase 0 complete (B0-LARGE separate): these are
  Jacobian-conjecture / GGHV-programme items, not IRH items. No proposal in
  any of the six files below arises from them. If a cross-reference from the
  IRH programme status to the GGHV programme is ever wanted, that is
  Brandon's call, not a v94 doc edit.
- The four GCP runs ($\$9.13$ total, lean-build-4 STOPPED) touch only the
  README's heavy-follow-on line (proposal R3 below); the spend figure itself
  comes from the task context and memory, and the advances ledger is asked
  to confirm the $\$9.13$ total before R3 is applied.

---

## 1. `README.md` — 4 proposals (1 PROPOSED grade)

### R1 — "Programme status — November 2026" / Local independent reproduction paragraph

- **Current text:** "Local independent reproduction (2026-11-14, \$0): all eight
  follow-on tasks re-run locally, blind to Co-scientist output — noise
  nucleation, grain locking, critical seed, native cells, spectral threshold,
  Bloch growth, peak ratios, phonon stiffness. Reports + code in
  `programme/local-independent/`; head-to-head comparison PENDING (scaffolds
  in each `COMPARISON_taskN.md`) until Co-scientist results land. No grades
  changed by this programme."
- **Proposed new text:** "Local independent reproduction (2026-11-14, \$0):
  all eight follow-on tasks re-run locally, blind to Co-scientist output.
  Head-to-head comparison COMPLETE 2026-11-14
  (`CONSOLIDATED_COMPARISON_2026-11-14.md` in
  `~/workspace/research/irh/co-scientist-tasks-2026-11-10/`): 314 claims
  audited — 277 VERIFIED, 10 VERIFIED WITH CORRECTION, 4 REFUTED,
  20 UNVERIFIED, 1 ABSTAIN. Six completed `COMPARISON_taskN.md` scaffolds;
  interface-tension and matched-branches comparisons are sections inside
  their audit files. No grades changed by this programme (grade implications
  are stated as evidence only; grade changes are Brandon's)."
- **Evidence:** `~/workspace/research/irh/co-scientist-tasks-2026-11-10/CONSOLIDATED_COMPARISON_2026-11-14.md`
  (claim totals table and deliverables list).
- **Grade change:** none. Note: the existing sentence "No grades changed by
  this programme" stays true as a statement about decided grades, but it
  will mislead once v94 proposals land; the added parenthetical guards it.

### R2 — "Programme status — November 2026" / Follow-on tasks in Academia

- **Current text:** "Follow-on tasks in Academia: ten launched 2026-11-14
  (the eight plus two Brandon launched himself); results pending."
- **Proposed new text:** "Follow-on tasks in Academia: ten launched
  2026-11-14 (the eight plus two Brandon launched himself); eight landed and
  audited 2026-11-14 (314 claims, see R1). Grain-locking and
  spectral-threshold still BLOCKED — no files on disk (reproducibility zips
  215 MiB and 306 MiB undownloaded); their `COMPARISON_task2.md` /
  `COMPARISON_task5.md` scaffolds remain pending."
- **Evidence:** `~/workspace/research/irh/co-scientist-tasks-2026-11-10/CONSOLIDATED_COMPARISON_2026-11-14.md`
  ("What is still BLOCKED or open" section).
- **Grade change:** none.

### R3 — "Programme status — November 2026" / Heavy follow-ons

- **Current text:** "Heavy follow-ons: GCP caps approved 2026-11-14 (~\$102
  total: Task 4 \$25, Task 6 \$2.44, Task 8 \$25 + \$50); status in
  `programme/local-independent/CONSOLIDATED_SUMMARY_LOCAL_2026-11-14.md`."
- **Proposed new text:** "Heavy follow-ons: GCP caps approved 2026-11-14
  (~\$102 total: Task 4 \$25, Task 6 \$2.44, Task 8 \$25 + \$50); all four runs
  DONE 2026-11-14, total spend **\$9.13** (\$0.19 / \$2.89 / \$0.03 / \$6.02);
  lean-build-4 STOPPED (asleep). Jobs 1, 2, 4 COMPLETE; Job 3 prototype only
  (Volterra defect heals under relaxation; $N=32$ production not run)."
- **Evidence:** task context 2026-11-14 (spend breakdown) — **to be confirmed
  by the advances ledger before applying**; `~/workspace/research/irh/co-scientist-tasks-2026-11-10/CONSOLIDATED_COMPARISON_2026-11-14.md`
  (phonon-stiffness §3: GCP Job 3 defect heals, measured $E/A$ ~$6{,}100\times$
  below the corrected prediction).
- **Grade change:** none.

### R4 — "Programme status — November 2026" / Batch 2 audit line, G-A6 follow-on

- **Current text:** "Batch 2 audit
  (`programme/AUDIT_batch2_2026-11-12.md`): 53 claims — 43 VERIFIED,
  9 UNVERIFIED, 1 REFUTED. G-A5 PARTIAL, stays open; G-A6 CLOSED as a mapping
  task (grade B / F2); G-A20 PARTIAL."
- **Proposed new text:** same, with this sentence appended: "G-A6 follow-on
  (2026-11-14): sampled stability of the relaxed state is supported at grade
  **C (PROPOSED)** — three routes agree (52 sector fibers, 259 $q$,
  14,641 $q$), no positive rate anywhere sampled; continuum Bloch stability
  for all $q$ stays ABSTAIN (no interval enclosure exists). The mapping-task
  closure (B / F2) is unchanged."
- **Evidence:** `~/workspace/research/irh/co-scientist-tasks-2026-11-10/CONSOLIDATED_COMPARISON_2026-11-14.md`
  (bloch-growth §2; grade-implications table, G-A6 row).
- **Grade change:** **PROPOSED GRADE** — new grade C assignment for the
  G-A6 follow-on (sampled stability). The closed mapping-task grade B / F2
  is not changed.

### README — no change needed

- Sweep 5 and Sweep 6 lines are already current (Sweep 5 continuum UV
  bounded to $[3/2, 2]$ at B, sharp ABSTAIN; Sweep 6 MISS, Hydrogen follow-up,
  G-D6.2 $I2 \to I1$). No proposal.
- Sweep 1 (G-D10 narrowed, open at C) is already current as written; the
  audit-landing record belongs in the gap inventory (proposal I10), not here.

---

## 2. `OPEN_PROBLEMS.md` — 3 proposals (0 PROPOSED grades)

### O1 — §IX.1 intro line

- **Current text:** "Specified; requires no new physics. All OPEN."
- **Proposed new text:** "Specified; requires no new physics. All OPEN.
  Programme note (2026-11-14): IX.1.1 and IX.1.2 have partial results —
  $4\pi$-box dissolution and the $L \gtrsim 61$ size bound (see gap inventory
  G-A9, G-A10) — but no item changes status; all five stay OPEN."
- **Evidence:** `~/workspace/research/irh/co-scientist-tasks-2026-11-10/CONSOLIDATED_COMPARISON_2026-11-14.md`
  (critical-seed §5; grade-implications table, G-A9 / G-A10 rows).
- **Grade change:** none.

### O2 — §IX.1 table row 1.4 (defect homotopy)

- **Current text:** "| 1.4 | Defect homotopy beyond elementary Burgers vectors
  | §V.1 | OPEN |"
- **Proposed new text:** same row, with this note appended below the table
  (or as a footnote to the row): "Programme note (2026-11-14): narrowed but
  stays OPEN. Phonon-stiffness corrects the local side — the translation
  (Burgers) lattice is $\pi D_{4}^{*}$, not $\pi D_{4}$, and the equilibrium
  edge/screw factor is $4/3$, not $2$; the shortest-shell classification is
  supported at B / F2 (PROPOSED, see gap inventory G-A11). The full homotopy
  classification is untouched, and defect realisation is contradicted in the
  tested setup (Volterra defect heals under relaxation)."
- **Evidence:** `~/workspace/research/irh/co-scientist-tasks-2026-11-10/CONSOLIDATED_COMPARISON_2026-11-14.md`
  (phonon-stiffness §3; grade-implications table, G-A11 row).
- **Grade change:** none in this file (this file carries no grades); the
  PROPOSED B / F2 lives in gap inventory proposal I5.

### O3 — §IX.5 table row 5.2 (nucleation event)

- **Current text:** "| 5.2 | **What supplies the nucleation event?** First-order
  transition (§II.9); the $D_{4}$ phase must be nucleated across a barrier at
  $\bar\psi=-0.18$. | OPEN |"
- **Proposed new text:** same row, with this note appended below the table
  (or as a footnote to the row): "Programme note (2026-11-14): stays OPEN.
  Noise-nucleation (chat 923db040, partial bundle) is a negative result: no
  transition-gate crossings in 192 ordinary runs or the bounded
  adaptive-splitting search; per-configuration 95% upper bound on gate entry
  by model time 40 is $8.94\%$ (Clopper–Pearson $0/32$). The null is expected
  at barrier/noise $\approx 34$ (Kramers factor $\sim 10^{15}$); it is a
  per-configuration gate-entry bound in the radial envelope, not a selection
  rate, and it neither confirms nor refutes a nucleation mechanism."
- **Evidence:** `~/workspace/research/irh/co-scientist-tasks-2026-11-10/CONSOLIDATED_COMPARISON_2026-11-14.md`
  (noise-nucleation-chat supplementary section; grade-implications table,
  G-D3 row: ABSTAIN unchanged).
- **Grade change:** none.

### OPEN_PROBLEMS.md — no change needed

- Rows 1.1, 1.2, 1.3, 1.5, 2.1, 2.2, 3.1–3.4, 4.1, 4.2, 5.1: statuses
  unchanged by the 2026-11-14 advances. G-A5 stays OPEN (patterned recovery
  verified, general selection from noise not established) — the register
  already says OPEN, so no edit; the detail belongs in the gap inventory
  (proposal I1).

---

## 3. `programme/IRH_GAP_INVENTORY_2026-11-12.md` — 12 proposals (7 PROPOSED grades)

### I1 — G-A5 (truncation gap), status line + "What we know"

- **Current text:** "**Status/grade:** PARTIAL, narrowed, stays OPEN.
  Patterned recovery with harmonics VERIFIED (Track E B / Track F F2).
  General selection from noise NOT established (0/6 random starts recover;
  Wilson 95% upper bound on the true rate $\approx 39\%$)."
- **Proposed new text:** "**Status/grade:** PARTIAL, narrowed, stays OPEN.
  Patterned recovery with harmonics VERIFIED in two cell constructions plus
  the 4D field test (Track E B / Track F **F1 (PROPOSED**, was F2 — two-leg
  evidence: full rerun + independent re-derivation)). General selection from
  noise NOT established anywhere (0/6 field; pooled 0/20 uniform per star,
  Wilson 95% upper bound $\approx 16\%$; AMS null expected at barrier/noise
  $\approx 34$). **LANDED and audited 2026-11-14:** noise-nucleation 4D field
  test (chat 02dfb5cb: 18 runs to $t=200$, meshes $18^{4}$/$28^{4}$; 9/9
  patterned + 3/3 bridge recover, 6/6 random decay to uniform) and
  native-cells (Task 4) — see consolidated comparison."
- **Evidence:** `~/workspace/research/irh/co-scientist-tasks-2026-11-10/CONSOLIDATED_COMPARISON_2026-11-14.md`
  (native-cells §1; noise-nucleation §8; grade-implications table, G-A5 row).
- **Grade change:** **PROPOSED GRADE** — patterned-recovery Track F F2
  $\to$ F1 (evidence only). Track E B unchanged; the open half unchanged.

### I2 — G-A6 (off-shell instabilities), add follow-on paragraph

- **Current text:** "**Status/grade:** CLOSED as a mapping task — VERIFIED
  (Track E B / Track F F2). ... Stability of the harmonically relaxed state
  is ABSTAIN — a new follow-on gap, not G-A6."
- **Proposed new text:** append a follow-on paragraph: "**Follow-on landed
  2026-11-14 (bloch-growth, Task 6):** sampled stability of the relaxed
  state is supported at grade **C (PROPOSED)** — three routes agree
  (52 $\Lambda$-sector fiber maxima, 259 $q$, 14,641 $q$ dense GCP map), no
  positive rate anywhere sampled; Goldstone zeros / mean channel F2
  supported; frozen quartet $+0.0228772435$ confirmed as an artefact (F2
  supported). Continuum Bloch stability for all $q$: **ABSTAIN** (no interval
  enclosure). Qualifier: the 52 rates are $\Lambda$-sector fiber maxima, not
  full-fiber maxima; one open numerical gap ($\Gamma$ first finite rate
  $-2.73844227$ vs $-2.73813733$, difference $3.05\times10^{-4}$)."
- **Evidence:** `~/workspace/research/irh/co-scientist-tasks-2026-11-10/CONSOLIDATED_COMPARISON_2026-11-14.md`
  (bloch-growth §2; grade-implications table, G-A6 row).
- **Grade change:** **PROPOSED GRADE** — new grade C for sampled stability
  (and F2 support for the Goldstone/artefact sub-claims). The CLOSED
  mapping-task verdict is not changed.

### I3 — G-A9 (larger-volume simulation), status line

- **Current text:** "**Status/grade:** OPEN (repo register); no grade."
- **Proposed new text:** "**Status/grade:** PARTIAL, narrowed, stays OPEN.
  Dissolution in the $4\pi$ box supports Track E **B (PROPOSED)**; size bound
  $L \gtrsim 61$ (35.11 GiB per real array at cutoff $6.5$) supports Track E
  **B (PROPOSED)**. Local growth in the $2\pi$ box is now read as
  finite-box/image-assisted filling, not an isolated-droplet threshold
  (local shell-fraction scaling predicts the $4\pi$ dissolution). The
  larger-box droplet run itself is still unrun; infinite-volume $R_{c}$
  stays ABSTAIN."
- **Evidence:** `~/workspace/research/irh/co-scientist-tasks-2026-11-10/CONSOLIDATED_COMPARISON_2026-11-14.md`
  (critical-seed §5; grade-implications table, G-A9 row).
- **Grade change:** **PROPOSED GRADE** — two new Track E B assignments
  (dissolution; size bound). Status stays OPEN.

### I4 — G-A10 (nucleation barrier / critical droplet), status line

- **Current text:** "**Status/grade:** OPEN (repo register). Partial verdicts:
  ODE $R_{c} = 12.57 / \Delta F* = 555$, grade B (exact within the amplitude
  equation); thin-wall $R_{c} = 7.38 / \Delta F* = 37.2$, grade C (approximation
  shown to fail — $\xi = 8.64 > R_{c})$."
- **Proposed new text:** append: "**2026-11-14:** saddle energy alone does
  not decide full-field fate — supported at Track E **C (PROPOSED)**
  (single-profile family; interface-tension: tensions $0.0189904$ /
  $0.0264060$ at coexistence, thin-wall transfers $36.95$ / $138.12$ vs saved
  saddle $550.93$; transferred tension is path-dependent by 40%).
  Deterministic saddle/threshold supports B / F2. Any rate stays ABSTAIN."
- **Evidence:** `~/workspace/research/irh/co-scientist-tasks-2026-11-10/CONSOLIDATED_COMPARISON_2026-11-14.md`
  (interface-tension §6; grade-implications table, G-A10 row).
- **Grade change:** **PROPOSED GRADE** — new Track E C for "saddle alone
  does not decide fate". Existing ODE B / thin-wall C unchanged.

### I5 — G-A11 (defect homotopy), status line + "What we know"

- **Current text:** "**Status/grade:** OPEN (repo register); untouched by all
  15 tasks." / "**What we know:** nothing in the programme bears on it.
  Manuscript §V.1 states the defect spectrum (dislocations yes; monopoles,
  skyrmions, hopfions no — line 924); the homotopy classification beyond
  elementary Burgers vectors is not computed anywhere."
- **Proposed new text:** "**Status/grade:** OPEN, narrowed. Shortest-shell
  classification supported at Track E **B / Track F F2 (PROPOSED)**; full
  homotopy untouched." / "**What we know (2026-11-14, phonon-stiffness,
  Task 8, 31/31 VERIFIED):** the translation (Burgers) lattice is
  $\pi D_{4}^{*}$, **not** $\pi D_{4}$ — the local side was wrong and
  Co-scientist is right (GCP confirms $(\pi/2)(1,1,1,1)$ is the shortest
  vector, $|b|=\pi$); one $W(F_{4})$ orbit per $D_{4}^{*}$ shell
  $\|b\|^{2}\le6$ verified (group order 1152 by exact-rational BFS).
  Stiffness $\lambda=\mu=4A^{2}q_{0}^{4}=1.54058921014457$ agrees exactly with
  the local value. Equilibrium edge/screw factor is $4/3$, **not** $2$ — the
  local edge coefficient was a non-equilibrium trial-field value, $3/2$
  high; corrected elementary edge $K$ $0.490385\to0.326923$, $E/A(R=20)$
  $0.899\to0.666$; screw unchanged. **Local edge leg demoted pending
  correction C5 (script rerun outstanding).** Defect realisation contradicted
  in the tested setup (Volterra defect heals under relaxation; GCP Job 3)."
- **Evidence:** `~/workspace/research/irh/co-scientist-tasks-2026-11-10/CONSOLIDATED_COMPARISON_2026-11-14.md`
  (phonon-stiffness §3, including the head-to-head corrections;
  grade-implications table, G-A11 row).
- **Grade change:** **PROPOSED GRADE** — new B / F2 for the shortest-shell
  classification. This is the first case in the programme where Co-scientist
  *corrects* the local side; the correction (C5 rerun) is outstanding and
  must be recorded as outstanding, not as done.

### I6 — G-A12 (3D projection / icosahedral signature), status line

- **Current text:** "**Status/grade:** Partly verified, partly open.
  |Aut$(D_{4})$| = 1152 (F3); no exact icosahedral projection (5 ∤ 1152) —
  verified (WS-A task 1)."
- **Proposed new text:** "**Status/grade:** Partly verified, partly open;
  stays OPEN. The verified geometric-mapping part supports Track E **B /
  Track F F1 (PROPOSED)** (peak-ratios, Task 7: 41/41 VERIFIED across two
  bundles; $A_{1}$–$A_{4}$, $C_{1}$–$C_{4}$, $F_{1}$, $F_{2}$, $D_{1}$ agree to
  printed precision on both sides). No nearest-icosahedral search was run;
  the synthetic-discriminant reading supports B / F1, the
  measurable-discriminant reading stays C (post-hoc selection, I1, no
  detector/noise model, one normal)."
- **Evidence:** `~/workspace/research/irh/co-scientist-tasks-2026-11-10/CONSOLIDATED_COMPARISON_2026-11-14.md`
  (peak-ratios §4; grade-implications table, G-A12 row).
- **Grade change:** **PROPOSED GRADE** — new B / F1 for the geometric-mapping
  part. The underlying open question (approximate icosahedral signature) is
  unchanged.

### I7 — G-A20 (no $A_{4}^{*}$ control), add identity finding

- **Current text:** "**Status/grade:** PARTIAL. The exact-combinatorics and
  matched-pure-branch part is VERIFIED (Track E B / Track F F1). The
  dynamical-competition, nucleation, and unbiased-emergence parts stay OPEN."
  / "**What would close it (in part):** ... **LANDED and audited
  2026-11-12** (exact part VERIFIED; dynamical parts open)."
- **Proposed new text:** append to "What we know": "**2026-11-14 identity
  finding (material):** `matched-branches/` is **byte-identical to the
  Batch 2 `a20-onset/` record** — every data file matches (scan-table sha256
  `da415b0c…`, same reproduction zip); `methods.md` differs only in
  LaTeX-delimiter style. This is a re-audit of the same record under a new
  task name, **not** a second independent delivery; it adds no new evidence
  beyond Batch 2. New in the 2026-11-14 audit: the rebuild-2 vs original-PDF
  check (unchanged — VERIFIED) and a fresh independent re-derivation + rerun
  (exit 0; 90,024-row scan max diff $0.0$). The chat-final-message numbers
  (onset $0.0301$–$0.0434$, $0.0399 \pm 0.0003$, $0.0329 \pm 0.0017$ /
  $0.0355$) remain UNVERIFIED and must be struck from any summary; the
  '$A_{4}^{*}$ branch does not exist on $24^{4}$/$28^{4}$ grids' phrasing
  remains REFUTED as phrased (branch exists in 7,765 scan rows)."
- **Evidence:** `~/workspace/research/irh/co-scientist-tasks-2026-11-10/CONSOLIDATED_COMPARISON_2026-11-14.md`
  (matched-branches §7; grade-implications table, G-A20 row).
- **Grade change:** none. The B / F1 for the exact part is unchanged; the
  proposal exists to stop the re-audit being counted as a second delivery.

### I8 — G-C21 (CDT small-scale endpoint), status line

- **Current text:** "**Status/grade:** Open; ABSTAIN on the endpoint (WS-D
  task 12)."
- **Proposed new text:** "**Status/grade:** Open; continuum UV endpoint
  bounded to $[3/2, 2]$ at grade **B (PROPOSED)**; sharp value ABSTAIN. Core
  verdict confirmed (Gemini Sweep 5, audited 2026-11-12): the $\sim 2$ vs
  $\sim 3/2$ split is bare-coupling and extrapolation-regime dependence; the
  canonical point is $\approx 2$; the continuum UV value is bounded to
  $[3/2, 2]$ at B with the sharp value abstained; no grade change to any IRH
  claim."
- **Evidence:** `~/workspace/research/IRH-Theory-Development-Workspace/programme/AUDIT_gemini-sweep-g-c21_2026-11-12.md`
  (audited grades: C-4 continuum UV endpoint B on $[3/2, 2]$, ABSTAIN sharp).
- **Grade change:** **PROPOSED GRADE** — ABSTAIN on the endpoint $\to$ B on
  the bounded interval $[3/2, 2]$, sharp value still ABSTAIN.

### I9 — G-D6 (no independent work citing IRH), status line + "What we know"

- **Current text:** "**Status/grade:** INCOMPLETE-EVIDENCE (WS-E task 14, M8;
  search-bounded absence, not a claim none exists)." / "**What we know:** no
  independent work citing/discussing IRH was found in the 63-query /
  73-paper retrieval. 'A different query set could find something.'"
- **Proposed new text:** "**Status/grade:** INCOMPLETE-EVIDENCE (unchanged).
  Gemini Sweep 6 (Task mode, 2026-11-13) audited 2026-11-13: **MISS**
  confirmed — zero independent works citing or discussing IRH; G-D6.1 (final)
  B CONFIRMED; G-D6.2 B (scoped bound) / ABSTAIN (universal negative)
  CONFIRMED, re-anchored on the Argon run. **Model-label correction:** the
  follow-up run was **Gemini 4 Hydrogen, not Argon** — cite it as Hydrogen;
  the two runs are one artificial pipeline ($\to$ I1), not two independent
  verifications. **Independence correction: G-D6.2 $I2 \to I1$** (the initial
  report's I2 is refuted as an overclaim; grade impact none — the
  $I1 \to C$ bound was repealed 2026-11-12). G-D6.3 F2 CONFIRMED and
  STRENGTHENED (Chaudhary 88-page full-text check closes the pp. 65–88 gap)."
- **Evidence:** `~/workspace/research/IRH-Theory-Development-Workspace/programme/AUDIT_gemini-sweep-g-d6_2026-11-13.md`
  (§§1, 4: model label, independence resolution, audited grades).
- **Grade change:** none (B scoped stands; ABSTAIN universal stands). The
  $I2 \to I1$ independence correction is flagged here because it is a
  material record correction even though no grade moves.

### I10 — G-D10 (IRH alone in the (2,2) corner), status line

- **Current text:** "**Status/grade:** Open (narrowed); grade C — strengthened
  bound (WS-E task 14, M6, C/I1/F1). DECIDED 2026-11-12 ~19:11 CST by the
  assistant under Brandon's standing decision autonomy ... The broad claim
  stays overturned (audit grade B); the gap continues in narrowed form."
- **Proposed new text:** append: "**Audit landed 2026-11-12 (Gemini Sweep 1
  audit):** the overturn stands under the stated three-criteria definition
  (IRH is not alone in the (2,2) corner; SSM (2,2,2)); the conditional
  sub-verdict is preserved at grade C — narrowed to spectral/Turing-only
  selection, no retrieved approach occupies the spectral-only (2,2) corner
  (SSM sits at (2,1,2), Lee at (2,1,1), Four Null at (2,1,1) under that
  reading). What would close the narrowed form: a retrieved approach with
  emergent spectral/Turing selection in the (2,2) corner, or a wider
  retrieval that still finds none."
- **Evidence:** `~/workspace/research/IRH-Theory-Development-Workspace/programme/AUDIT_gemini-sweep-g-d10_2026-11-12.md`
  (§C2, conditional sub-verdict preserved at C; "What the overturn does and
  does not do").
- **Grade change:** none (broad overturn B and narrowed bound C both stand
  as recorded; this proposal records the audit landing).

### I11 — G-D3 (nucleation event), add 2026-11-14 evidence note

- **Current text:** "**Status/grade:** ABSTAIN (WS-E task 11, C10; task 15,
  B4; no grade). Stated open in the manuscript."
- **Proposed new text:** append to "What we know": "**2026-11-14
  (noise-nucleation chat 923db040, partial bundle):** negative result — no
  transition-gate crossings in 192 ordinary runs or the bounded
  adaptive-splitting search; per-configuration 95% upper bound on gate entry
  by model time 40 is $8.94\%$ (Clopper–Pearson $0/32$; pooled $0/192$ would
  be $1.55\%$). The null coheres with the local radial-envelope saddle
  ($550.930573$ at $dr=0.5$): at barrier/noise $\approx 34$ the Kramers factor
  $\exp(551/16) \approx 9.0\times10^{14}$ predicts $\sim 10^{-13}$ expected
  hits per run, so the null is expected, not evidence against nucleation.
  Open item: re-run the audit when the chat's 7 files land, checking the
  192-vs-160 count discrepancy first (192 = code's 6-config default
  $\times 32$; bundle has 160 in `ensemble.log`, 128 tabulated)."
- **Evidence:** `~/workspace/research/irh/co-scientist-tasks-2026-11-10/CONSOLIDATED_COMPARISON_2026-11-14.md`
  (noise-nucleation-chat supplementary section; stochastic-nucleation §;
  grade-implications table, G-D3 row: ABSTAIN unchanged).
- **Grade change:** none (stays ABSTAIN).

### I12 — New entry G-A21 (proposed): F-LOCAL-1, the $|k|^{2}\le64$ cap

- **Current text:** none — new entry, to be added at the end of Group A
  (after G-A20).
- **Proposed new text:** "### G-A21 (proposed) — F-LOCAL-1: the local
  solver's physical cap is $|k|^{2} \leq 64$, so the GCP '$K=6$ full study'
  never widened the $A_{4}^{*}$ band — **Status/grade:** Open; no grade
  (unverified, not a failed claim). **What we know:** the local solver's
  physical cap is hardcoded at $|k|^{2} \leq 64$, so the GCP '$K=6$' energies
  are identical to $K=4$ to 15 figures — trap robustness to a genuinely wider
  band is still UNVERIFIED. **What would close it:** a rerun with a genuinely
  wider band (cap raised), costed first. **Owner:** Local Muse verification
  (small local runs) / Co-scientist task."
- **Evidence:** `~/workspace/research/irh/co-scientist-tasks-2026-11-10/CONSOLIDATED_COMPARISON_2026-11-14.md`
  (native-cells §1, "New finding F-LOCAL-1"; "Local corrections outstanding"
  list).
- **Grade change:** none (new open entry, no grade).
- **Counts consequence:** if accepted, the inventory becomes 75 entries;
  the §0 counts line and the appendix table must be updated in the same wave
  (open 63 $\to$ 64; Group A 20 $\to$ 21 entries, 18 $\to$ 19 open). The counts
  update is mechanical, not a separate proposal.

### Gap inventory — no change needed

- G-A18 (thin-wall, CLOSED): unchanged — interface-tension re-confirms the
  $\sim 15\times$ barrier mismatch the local Task 3 already states.
- G-C12 (printed dispersion relation (7)): unaffected by phonon-stiffness —
  the consolidated comparison says so explicitly.
- G-A1, G-A2, G-A3, G-A4, G-A7, G-A8, G-A13–A19, Group B, G-C1–C11, G-C13–C20,
  G-C22, G-D1, G-D2, G-D4, G-D5, G-D7, G-D8, G-D9, G-D11, G-D12, Group E:
  no 2026-11-14 advance touches them; no proposal.
- Counts in §0 and the appendix ("63 open, 7 closed, 4 non-gaps") need no
  change from the advances themselves — no gap closed and none opened,
  except proposed new entry I12 above (mechanical counts update only).

---

## 4. `verification/README.md` — 0 proposals (no change)

- **One line:** no change. The `irh93_pkg2` package is the verbatim Enigma
  v93/v93.0 audit record (51/51 checks, 8 Lean modules); none of the
  2026-11-14 advances touches it — phonon-stiffness corrects the
  *programme's local* Task 8 numbers, not the v93 verification package, and
  no new verification artifact is filed here.
- Flag for the later wave (not a proposal): if a v94 verification package is
  ever filed, this README will need a new section; that decision is
  Brandon's.

---

## 5. `programme/CONSOLIDATED_SUMMARY_2026-11-12.md` — 3 proposals (0 PROPOSED grades)

### S1 — §9, "RUNNING — Run a four-dimensional field test of $D_{4}$ formation"

- **Current text:** "**RUNNING — 'Run a four-dimensional field test of $D_{4}$
  formation' (Academia Co-scientist, launched 2026-11-12, chat
  `02dfb5cb-5423-47eb-9bbe-d8e3d25b6fdc`).** ... When it lands, it is audited
  claim-by-claim locally under truth-seeking-frontier /
  cross-domain-discovery / HLRE v5.1; nothing is filed, committed, or written
  into the manuscript."
- **Proposed new text:** "**LANDED and audited 2026-11-14 — 'Run a
  four-dimensional field test of $D_{4}$ formation' (Academia Co-scientist,
  chat `02dfb5cb-5423-47eb-9bbe-d8e3d25b6fdc`).** 18 trajectories + 6
  refinements to $t = 200$, meshes to $28^{4}$; all 9 patterned starts
  recovered phase-locked $D_{4}$; all 6 random starts decayed to uniform.
  Audited claim-by-claim locally (noise-nucleation audit, 21/27 VERIFIED,
  1 correction, 1 REFUTED as a nucleation measurement, 4 UNVERIFIED).
  G-A5 confirmed, not moved: patterned recovery VERIFIED; general selection
  from noise NOT established."
- **Evidence:** `~/workspace/research/irh/co-scientist-tasks-2026-11-10/CONSOLIDATED_COMPARISON_2026-11-14.md`
  (noise-nucleation §8).
- **Grade change:** none.

### S2 — §9, "CANDIDATE (not launched) — Map off-shell instabilities of the full $D_{4}$ wave"

- **Current text:** "**CANDIDATE (not launched) — 'Map off-shell instabilities
  of the full $D_{4}$ wave'.** Linearizes around the standing wave; leading
  unstable bands on a finite Fourier grid. **Gap attacked (inventory G-A6)**..."
- **Proposed new text:** "**LANDED and audited 2026-11-12 (Batch 2) and
  2026-11-14 (bloch-growth, Task 6) — 'Map off-shell instabilities of the
  full $D_{4}$ wave'.** Frozen-ansatz spectrum fully verified (headline
  $K=8$ rate $+0.022877243496718158$ reproduces exactly); follow-on sampled
  stability of the relaxed state supported at grade C (PROPOSED) — three
  routes agree, no positive rate anywhere sampled; continuum Bloch stability
  stays ABSTAIN. **Gap attacked (inventory G-A6)** — mapping task CLOSED;
  follow-on recorded in the gap inventory."
- **Evidence:** gap inventory G-A6 (Batch 2 verdict);
  `~/workspace/research/irh/co-scientist-tasks-2026-11-10/CONSOLIDATED_COMPARISON_2026-11-14.md`
  (bloch-growth §2).
- **Grade change:** none in this file; the PROPOSED C lives in inventory
  proposal I2 / README proposal R4.

### S3 — §9, "CANDIDATE (not launched) — Calculate matched $D_{4}$ and $A_{4}^{*}$ onset branches"

- **Current text:** "**CANDIDATE (not launched) — 'Calculate matched $D_{4}$
  and $A_{4}$* onset branches'.** Both candidates on the same normalized
  amplitude / shell-penalty footing. **Gap attacked (inventory G-A20)**..."
- **Proposed new text:** "**LANDED and audited 2026-11-12 (Batch 2) —
  'Calculate matched $D_{4}$ and $A_{4}$* onset branches'.** Exact-combinatorics
  and matched-pure-branch part VERIFIED (Track E B / Track F F1);
  dynamical-competition, nucleation, and unbiased-emergence parts stay OPEN.
  **2026-11-14 identity finding:** `matched-branches/` is byte-identical to
  the Batch 2 `a20-onset/` record — a re-audit, not a second independent
  delivery; no new evidence beyond Batch 2. **Gap attacked (inventory
  G-A20)**..."
- **Evidence:** gap inventory G-A20;
  `~/workspace/research/irh/co-scientist-tasks-2026-11-10/CONSOLIDATED_COMPARISON_2026-11-14.md`
  (matched-branches §7).
- **Grade change:** none.

### CONSOLIDATED_SUMMARY — no change needed

- §8.4 ("What this package does NOT change"): the headline facts it lists
  ($D_{4}$ selection $S = 64/141$, $E_{6}$ via 2T/McKay, SO(8) exclusion,
  three generations as INPUT) are untouched by the 2026-11-14 advances. No
  proposal. (The stale grade-cap language in §0.1, §7, and Appendix A is
  pre-existing staleness — see §7 below, not a v94 proposal.)

---

## 6. `established/CORE.md` — 1 proposal (0 PROPOSED grades)

### C1 — "Matter and defects" / Burgers vectors

- **Current text:** "Order-parameter space $M = T^4 \times S^3$: dislocation
  sheets (Burgers vectors in $D_{4})$, no line defects, integer-charged point
  solitons — §V.1."
- **Proposed new text:** "Order-parameter space $M = T^4 \times S^3$:
  dislocation sheets (Burgers vectors in the translation lattice
  $\pi D_{4}^{*}$ — corrected 2026-11-14; the $D_{4}$ form was wrong), no line
  defects, integer-charged point solitons — §V.1. Equilibrium edge/screw
  defect-cost factor is $4/3$, not $2$ (corrected 2026-11-14; elementary edge
  $K$ $0.490385\to0.326923$); screw costs unchanged."
- **Evidence:** `~/workspace/research/irh/co-scientist-tasks-2026-11-10/CONSOLIDATED_COMPARISON_2026-11-14.md`
  (phonon-stiffness §3: "Co is right, local is wrong — the translation
  lattice is $\pi D_{4}^{*}$, not $\pi D_{4}$"; edge/screw factor $4/3$).
- **Grade change:** none — CORE.md carries no grades; this is a wording
  correction to the established core. Note: this is the only CORE.md line
  the advances falsify as written. Because CORE.md is what new work may
  build on without re-derivation, this correction should be applied early
  in the edit wave, before any new work cites the old Burgers lattice.

### CORE.md — no change needed

- "Dynamical shell selection from noise; triad term causally responsible
  (77.1% vs 21.1% control; 89.5% annealed, independent reproduction) —
  §II.6": unchanged. The fair-test claim stands; the G-A5 narrowing concerns
  general selection from noise (a different claim), not the fair test.
- "Full 24-mode state is a genuine dynamical attractor ($F/V=-0.0077276$
  relaxed; one-mode ansatz accurate to 1.25%) — §II.8": unchanged (patterned
  recovery verified on both sides; the 1.249% / 1.231% harmonic-relaxation
  refinement is a correction inside the audit record, not a CORE.md change).
- "$D_{4}$ selected in 4D: $S = 64/141 \approx 0.454$, exact rationals, 17.3%
  margin over $A_{4}^{*}$": unchanged — re-verified on both sides
  ($S_{D_{4}}/S_{A_{4}^{*}} = 496/423$, margin $73/423$).
- "Conserved (Model B) dynamics required; $\bar\psi$ preserved to
  $8.3\times10^{-17}$": unchanged — no 2026-11-14 advance re-measures it.
- "Corrected envelope equation + quantified validity ($<1\%$ for
  $a_0|\mathbf{k}| \lesssim 0.3$) — §III.3": unchanged — G-C13 (the §III.3
  table UNVERIFIED) does not touch the VI.3 summary boundary, which survives
  recomputation.

---

## 7. Pre-existing staleness (NOT v94 proposals — do not fold into the edit wave)

These were already stale relative to v93.1 / the 2026-11-12 HLRE amendments
before today's advances. Listed separately, as instructed; fixing them is a
separate decision, not part of the v94 proposals above.

1. **README.md, gap-inventory counts line:** "Gap inventory
   (`programme/IRH_GAP_INVENTORY_2026-11-12.md`): 74 entries — 62 open,
   8 closed, 4 non-gaps (baseline 2026-11-12)." The inventory itself counts
   **63 open, 7 closed-as-verdict, 4 recorded non-gaps** (§0 and appendix
   table). The README's 62/8 matches neither the inventory's current counts
   nor its first-issue counts (66 open at first issue, per the appendix
   correction note).
2. **Gap inventory §0, caps line:** "Caps: Track E **C** at I1; Track F
   **F2** two-route / **F3** single-route." The $I1 \to C$ bound was repealed
   2026-11-12 (HLRE amendment, 14:45–14:47 CST) and replaced by external
   verification audited locally. The caps line still states the repealed
   bound as live.
3. **CONSOLIDATED_SUMMARY_2026-11-12.md, Appendix A grade key:** "At I1
   (artificial verification, single pipeline) every claim caps at **C**."
   Same repealed $I1 \to C$ bound, stated as live. The same stale cap
   language recurs in §0.1 (line 31), §0 (line 42), and the WS-D sections
   (§7, e.g. "capped at F3; human gates not run", "ceiling I1"), all
   predicated on the repealed §6.5 human-gate requirement as well.
4. **CONSOLIDATED_SUMMARY_2026-11-12.md, Appendix B source index:**
   "NOT LOCATED: the 'Compare $D_{4}$ Selection Frameworks' gap memo (three
   files behind Academia keypass links; no local copy found ... 2026-11-12)."
   The memo was located, pulled, and audited claim-by-claim later on
   2026-11-12 (gap inventory G-E1, now CLOSED as LOCATED). Appendix B was
   never updated.
5. **README.md vs
   `programme/local-independent/CONSOLIDATED_SUMMARY_LOCAL_2026-11-14.md`:**
   the README says heavy-follow-on caps were "approved 2026-11-14" with
   status in the local summary, but the local summary's §"Heavy work still
   undone" says the caps were "none approved, none started" and "all caps
   above await Brandon's approval". The local summary was never updated for
   the approval or for the completed runs (adjacent file, not one of the six
   in scope — flagged here because R3 cites it).
6. **`established/CORE.md`, broken LaTeX delimiters (pre-existing
   formatting):** "24-cell vertices = binary tetrahedral group \$2$$T
   \subset$\$ SU(2)\$ (exhaustive)", "\$2$$T/Q_{8} \cong \mathbb{Z}$$_3\$
   (8+8+8 coset decomposition)", and "McKay: \$2$$T \leftrightarrow$$\$ affine
   $E_{6}$" — the `$...$` delimiters are malformed in all three lines
   (unmatched/ doubled `$` signs). This predates the v94 work; it violates
   the standing $...$ delimiter rule and should be fixed in a formatting
   pass, not counted as a v94 content proposal.

## 8. Contradictions between the docs and the advances (flagged, not resolved here)

1. **Matched-branches is a re-audit, not a second delivery.** Any doc text
   that counts the Batch 2 onset record and the matched-branches record as
   two independent verifications would be wrong. Proposals I7 and S3
   correct the record in the two places that cite it; no other doc in scope
   does so.
2. **Phonon-stiffness corrects the local side.** The old local numbers
   (Burgers lattice $\pi D_{4}$, edge/screw factor 2, edge $K$ $0.490385$)
   survive only in CORE.md proposal C1 and gap inventory proposal I5 among
   the six files; the full corrected numbers live in the consolidated
   comparison and in `local-independent/task8-phonon-stiffness/`, where the
   outstanding local correction C5 (script rerun) is still open. Do not
   present the corrected numbers as if C5 had been run.
3. **README "No grades changed by this programme" vs the consolidated
   comparison's grade-implications table.** No contradiction if read
   strictly (no auditor changed any grade; the table is evidence-only
   proposals), but the sentence will mislead once v94 proposals are
   adopted. Proposal R1 adds the guarding parenthetical.
4. **Scaffold staleness (outside the six files):** the completed
   `COMPARISON_taskN.md` scaffolds for tasks 1, 3, 6, 7, 8 still carry a
   "Grade cap C/F3 until human gates run" section whose basis (HLRE §6.5)
   was repealed 2026-11-12; only the native-cells scaffold was corrected.
   Flagged for the owner of `programme/local-independent/`, not counted
   among these proposals.
5. **Noise-nucleation count discrepancy (unresolved in the evidence):**
   192 ordinary runs (chat) vs 160 in `ensemble.log` vs 128 tabulated in
   `raw_runs.csv`; `space_half` 0/32 log-line-only; `leading_FDT` never ran.
   Proposal I11 records it as an open item pending the chat's 7 files; no
   doc in scope should cite the $8.94\%$ bound as a pooled bound ($1.55\%$
   for $0/192$) or as a selection rate.

---

## Counts

| File | Proposals | Of which PROPOSED grade |
|---|---|---|
| `README.md` | 4 (R1–R4) | 1 (R4) |
| `OPEN_PROBLEMS.md` | 3 (O1–O3) | 0 |
| `programme/IRH_GAP_INVENTORY_2026-11-12.md` | 12 (I1–I12) | 7 (I1–I6, I8) |
| `verification/README.md` | 0 | 0 |
| `programme/CONSOLIDATED_SUMMARY_2026-11-12.md` | 3 (S1–S3) | 0 |
| `established/CORE.md` | 1 (C1) | 0 |
| **Total** | **23** | **8** |

Pre-existing staleness items (§7): 6, listed separately and not folded into
the 23 proposals. Blocked items with no doc proposal: grain-locking and
spectral-threshold (no files — nothing to record beyond the BLOCKED status
in R2); the noise-nucleation chat's 7 undownloaded files (re-audit pending,
recorded in I11).
