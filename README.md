# IRH Theory-Development Workspace

**Source:** *Intrinsic Resonance Holography: Dynamical Selection of a D₄ Substrate from
Interference Dynamics*, v93.1 (Brandon D. McCrary, 2026-09-18, Zenodo DOI
10.5281/zenodo.22821689).
**Status of source:** five verification cycles complete; geometric core verified
(symbolic + numeric + Lean 4, eight modules, `lake build` exit 0); claim ledger closed
at Part VIII.

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

## The two sharpest questions (§IX.5)

The paper singles out two questions as sharper than the rest — the highest-leverage
targets in this workspace:

1. **What fixes $\bar\psi$?** The baseline tension is an initial datum under conserved
   dynamics; no mechanism sets its value. Whether occupying the D₄ band is a
   prediction or a tuning is undetermined. → `problems/IX5-genuinely-open.md`
2. **What supplies the nucleation event?** The transition is first order (§II.9); the
   D₄ phase must be nucleated and does not emerge spontaneously at the relevant
   baseline tension. → `problems/IX5-genuinely-open.md`

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

## Related work already in flight

- Triad amplitude dynamics (`~/workspace/irh-push-amplitude/analysis/`,
  `triad_amplitude_dynamics.py`) — staged, not yet pushed; bears directly on
  prediction VI.1 (triad phase locking) and the P1/P2/P3 triad-locking results.
- Lean 4 development (eight modules, `lake build` exit 0) — the machine-checked
  geometric core; extend it as new derivations close.
