# IRH Theory-Development Workspace

**Source:** *Intrinsic Resonance Holography: Dynamical Selection of a $D_{4}$ Substrate from
Interference Dynamics*, v93.1 (Brandon D. McCrary, 2026-09-18, Zenodo DOI
10.5281/zenodo.22821689).
**Status of source:** five verification cycles complete; geometric core verified
(symbolic + numeric + Lean 4, eight modules, `lake build` exit 0); claim ledger closed
at Part VIII.

A 33-page source rebuild (rebuild 2, November 2026, used for the Gemini Sweep 5/6
follow-ups) is filed as `IRH_v93.1_source_rebuild_2.pdf`, replacing the 31-page
`IRH_v93_1.pdf` (removed 2026-11-14), with its LaTeX sources in
`source-2026-11-05/` and the rebuild verification in `rebuild-2026-11-04/`.

This workspace exists for one purpose: **continue development of the theory by
working the open problems stated in Part IX of v93.1.** Nothing here re-litigates
closed claims. The open problems are the research focus.

## Layout

- `OPEN_PROBLEMS.md` — the complete Part IX register, classified exactly as the
  paper classifies it, with workspace status for each item.
- `problems/` — one research brief per Part IX section (IX.1–IX.5). Each brief
  states the problem in the paper's words, why it matters, what is already known,
  concrete attack routes, and what "done" looks like.
- `predictions/VI-predictions.md` — the falsifiable predictions of Part VI,
  reformulated as test targets with pass/fail criteria.
- `guardrails/EXCLUDED.md` — claims the paper excludes by theorem or retracts.
  **These are not to be revived.** Any new work that appears to need one of them
  is wrong; find the error.
- `guardrails/INPUTS.md` — acknowledged inputs (Part VIII.3). They are assumptions,
  not results; any discussion of fermion content, tuning, or dynamics must state
  them as such.
- `established/CORE.md` — the verified geometric core (Part VIII.1), compressed to
  the facts new work may build on without re-derivation.
- `verification/` — the independent verification package (`irh93_pkg2`: Enigma's
  v93/v93.0 audit — `verify_claims.py` (51/51 checks), `sim6_units.py`,
  `sim7_fairtest.py`, `FINAL_AUDIT.md`, and the 8-module Lean 4 development).
  See `verification/README.md` for the contents map and the conventions it fixes.
  `verification/AUDIT_2026-10-15.md` records CAIC's independent re-verification
  of the external consolidated audit (confirmed/refined/downgraded per item),
  including manuscript errata flagged for a future revision ($\tau$-ratio, CFL table
  labels) and the executed 32-maximum proof.
- `programme/` — the November 2026 joint verification programme (Muse + Academia
  Co-scientist, with Gemini 4 sweeps): gap inventory, batch audits, sweep records
  and audits, workstream reports, and the independent local reproduction of the
  eight follow-on tasks. See "Programme status — November 2026" below and
  `programme/PROGRAMME_BRIEF.md`.
- `source-2026-11-05/` — LaTeX sources of the v93.1 manuscript (`.tex`,
  `paper_v931.md`, figures, build scripts) and the rebuild-2 tree.
- `rebuild-2026-11-04/` — verification of the manuscript rebuild (SymPy,
  second-tool, and Singular checks with logs).
- `torus-node-comparison/` — an independent torus-node model reaching the same
  $D_{4}$ mathematics by the opposite method, checked against IRH claim by claim
  (`TORUS_NODE_VS_IRH_COMPARISON.md`).

## Programme status — November 2026

Joint Muse + Academia Co-scientist programme, launched 2026-11-10, run under HLRE
v5.1 (as amended 2026-11-12), the truth-seeking computation gate, and
cross-domain-discovery. Nothing in `programme/` is incorporated into the
manuscript; these are verification records, and no grade moves except through the
evidence. Headline facts are unchanged: $D_{4}$ selected, $S = \tau^2/q_4 = 64/141 \approx 0.454$ (17.3% margin over $A_{4}^{*}$); gauge algebra $E_{6}$ via 2T/McKay;
$SO(8)$ excluded; three generations are an INPUT, not derived. Perelman's $\tau$
is not IRH's $\tau$; $S$ is never Perelman's $W$.

- Gap inventory (`programme/IRH_GAP_INVENTORY_2026-11-12.md`): 74 entries — 62
  open, 8 closed, 4 non-gaps (baseline 2026-11-12).
- Batch 1 audit (`programme/AUDIT_batch1_2026-11-12.md`): 36 claims — 34 VERIFIED,
  1 CORRECTED, 1 ABSTAIN.
- Batch 2 audit (`programme/AUDIT_batch2_2026-11-12.md`): 53 claims — 43 VERIFIED,
  9 UNVERIFIED, 1 REFUTED. G-A5 PARTIAL, stays open; G-A6 CLOSED as a mapping task
  (grade B / F2); G-A20 PARTIAL.
- Gemini 4 sweeps (specs in `programme/GEMINI-SWEEPS-SPECS-2026-11-12.md`; Task mode
  from Sweep 6, model pinned to Argon):
  - Sweep 1, G-D10: broad claim overturned (B); narrowed to spectral/Turing-only
    selection, open at C.
  - Sweep 2, G-C18: bound strengthened, scoped $C \to B$; universal ABSTAIN.
  - Sweep 3, G-C19: resolved, G8/F1 — Dirac varying-$G$ falsified.
  - Sweep 4, G-C20: resolved, grade B (Track E) / F2 (Track F).
  - Sweep 5, G-C21: core verdict confirmed; continuum UV value bounded to
    $[3/2, 2]$ at B; sharp value ABSTAIN; no grade change.
  - Sweep 6, G-D6: MISS — zero independent works citing or discussing IRH.
    The follow-up run was Gemini 4 Hydrogen, not Argon; cite it as Hydrogen.
    G-D6.2 independence $I2 \to I1$.
- Local independent reproduction (2026-11-14, \$0): all eight follow-on tasks
  re-run locally, blind to Co-scientist output — noise nucleation, grain locking,
  critical seed, native cells, spectral threshold, Bloch growth, peak ratios,
  phonon stiffness. Reports + code in `programme/local-independent/`; head-to-head
  comparison PENDING (scaffolds in each `COMPARISON_taskN.md`) until Co-scientist
  results land. No grades changed by this programme.
- Follow-on tasks in Academia: ten launched 2026-11-14 (the eight plus two Brandon
  launched himself); results pending.
- Heavy follow-ons: GCP caps approved 2026-11-14 (\~\$102 total: Task 4 \$25,
  Task 6 \$2.44, Task 8 \$25 + \$50); status in
  `programme/local-independent/CONSOLIDATED_SUMMARY_LOCAL_2026-11-14.md`.
- HLRE amendments 2026-11-12 (`programme/HLRE-*.md`): §6.5 human-gate repeal;
  external-verification authorization (Manus, Gemini 4 (Argon), Co-scientist);
  $I1 \to C$ bound repealed and replaced by external verification audited locally
  claim-by-claim.

## The two sharpest questions (§IX.5)

The paper singles out two questions as sharper than the rest — the highest-leverage
targets in this workspace:

1. **What fixes $\bar\psi$?** The baseline tension is an initial datum under conserved
   dynamics; no mechanism sets its value. Whether occupying the $D_{4}$ band is a
   prediction or a tuning is undetermined. $\to$ `problems/IX5-genuinely-open.md`
2. **What supplies the nucleation event?** The transition is first order (§II.9); the
   $D_{4}$ phase must be nucleated and does not emerge spontaneously at the relevant
   baseline tension. $\to$ `problems/IX5-genuinely-open.md`

## Working conventions (inherited from the paper)

- Every claim carries an epistemic label: DERIVATION / PREDICTION / CALIBRATION /
  INPUT / EXCLUDED / OPEN. Unlabeled claims are unsupported.
- Numerical claims ship with executed scripts; formal claims with Lean 4 where
  feasible. The v93.1 standard is: re-derived by executed computation, validated
  against a known limiting case, confirmed by simulation, excluded by theorem, or
  machine-checked.
- Corrections are recorded in the open (cf. Appendix A of v93.1), including
  corrections to our own prior output. Retractions name the error; they are never
  silent.

## What is not in this repo

- Run data (`.npz`, `.csv`, `.zip` bundles, figure PNGs from the programme tasks)
  stays local; the reports and scripts in `programme/` record exactly what was run
  and how to reproduce it.
- The downloaded `.tex` corpus of the literature screen (third-party sources) is
  not filed here.
- Jacobian-conjecture material lives in the separate
  `2D-Jacobian-Conjecture-Workspace` repo, including the Wise (WJAA) galley proof
  of the branch-(c) paper — it is not IRH material and is not filed here.
