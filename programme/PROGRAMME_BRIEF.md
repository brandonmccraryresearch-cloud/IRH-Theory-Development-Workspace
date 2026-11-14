# Co-scientist task programme — 2026-11-10

Brandon's order (2026-11-10 ~16:57 CST): do all of the Academia Co-scientist
suggested tasks that have not been done, under /truth-seeking-frontier
/cross-domain-discovery /hlre-v5-1. Where the skills conflict, use the one
that makes more sense in that instance.

DONE already (excluded from this programme): "Compare D4 Selection
Frameworks" — finished overnight by Academia Co-scientist; audit of its three
files is a separate item (needs Academia login) and is NOT part of this
programme.

## Skills (read all three SKILL.md files first; triggers in every brief)

- /truth-seeking-frontier — `~/workspace/custom-skills/truth-seeking-frontier/SKILL.md` (v5)
- /cross-domain-discovery — `~/workspace/custom-skills/cross-domain-discovery/SKILL.md` (v2.0.0)
- /hlre-v5-1 — `~/workspace/custom-skills/hlre-v5-1/SKILL.md`

Conflict rule (Brandon): where they conflict, use the skill that makes more
sense in that instance. Working resolution, unless a task shows otherwise:
HLRE v5.1 governs grading and records for every claim; the truth-seeking
computation gate governs every computed result (quoted tool verdict with
version + exit code; above CLAIMED needs a second independent tool);
cross-domain-discovery S1–S7 governs cross-domain synthesis method
(framework comparisons, rival accounts, analogies) with its grade caps
(Track E C / Track F F3 until a human runs the source/balance gates).
The skills themselves are DESIGN CLAIMS, ungraded — never present skill use
as evidence of reliability.

Standing rules that also apply:
- Deepest-research (full mode) for literature-heavy work and before any
  major revision is incorporated. Read
  `~/workspace/custom-skills/deepest-research/SKILL.md` when a task needs it.
- NOTHING is incorporated into the repo or manuscript from this programme:
  no commits, no pushes, no filing, no manuscript edits. Deliverables are
  reports + figures + tables in this programme directory. Incorporation
  needs deepest-research validation first and Brandon's explicit approval.
- Never state IRH results beyond their HLRE grades. A Co-scientist-style
  summary is NOT verification and moves NO grade.

## Sources (ground everything in these, not memory)

- Manuscript text: `IRH_v93_1_source_rebuilt.txt` in this directory
  (from `~/workspace/user/files/IRH_v93_1_source_rebuilt__1__3_0iaj.pdf`,
  34 pp., sha256 cebc3b6f010ed9c059129b4b0ff2c9e3a8ea858e74adc68c3e7fd7d9f34affa8).
- IRH repo clone: `~/workspace/research/IRH-Theory-Development-Workspace/`
  — README, OPEN_PROBLEMS.md, problems/IX1–IX5 briefs,
  predictions/VI-predictions.md, guardrails/EXCLUDED.md + INPUTS.md,
  established/CORE.md, verification/ (verify_claims.py 51/51, sim6_units.py,
  sim7_fairtest.py, reconcile_resonance_count.py, FINAL_AUDIT.md,
  AUDIT_2026-10-15.md, IX4_VEV_CONSISTENCY_2026-10-15.md, lean/ 8 modules).
- Triad amplitude dynamics (staged, not pushed; bears on VI.1):
  `~/workspace/irh-push-amplitude/analysis/`

## Established IRH facts (do not re-litigate; cite the qualification every time)

- D4 selected, $S = \tau^{2}/q4 = 64/141 \approx 0.454 (17.3$% margin over A4*).
- E6 via 2T/McKay. SO(8) EXCLUDED. Three generations INPUT, not derived.
- D4 band 11.85% of scanned plane CONDITIONAL on q0 tuned onto shell.
- First-order transition $(r_{eff} = +0.107$ at psi-bar = -0.18). Model B required
  (psi-bar conserved to 8.3e-17). CFL bound dt <= (sqrt(3)/2) a0/c.
- $\tau_{D}4/\tau_{BCC}$ = sqrt(2). Perelman tau != IRH tau; S is never Perelman's W.
- EXCLUDED, never revive: so(8) gauge algebra, SM in so(8), Pati–Salam
  from so(8), Kerr solitons, skyrmions/hopfions from one scalar, three
  generations derived, monopole absence, universal D4 optimality,
  $\xi_{2} = -1/384$, both v92 time steps, all v92 Higgs VEV/A3/CKM numbers.
- Sharpest open questions: IX.5.1 what fixes psi-bar? IX.5.2 what supplies
  the nucleation event? The joint early-universe narrative is missing
  in its entirety.
- Jacobian side (WS-B only): branches (a),(b) of the GGHV (72,108) case are
  eliminated in Lean, Grade A, kernel-verified. A symbolic re-derivation is
  a cross-check, not a re-proof.

## Compute rules (hard)

- Light symbolic/numerical checks run in the local conda env:
  `~/miniconda3/envs/jacobian-conjecture-2d/bin/python` (Python 3.11.16,
  SymPy 1.14.0, python-flint, numpy) and Singular 4.4.1 in the same env.
  Keep any single local job under ~10 min / ~4 GB. /tmp is a 512 MB tmpfs:
  keep all large work under ~/workspace, never /tmp.
- Sustained/heavy simulation: prototype small, COST the full run, and
  report the costed plan back — do NOT start GCP spend. GCP spend needs a
  named budget cap or per-action approval from Brandon.
- NEVER touch lean-build-4 (leg-9 run at full load, 23 workers), NEVER stop
  any VM, NEVER delete anything.
- NEVER call the Gemini grader
  (`~/workspace/research/truth-seeking-v5/gemini-grader/` — DO NOT CALL).
- `Singular --version` hangs on stdin: always `< /dev/null`.

## Output rules (every task)

- One report per task + figures (PNG) + tables, in your workstream
  directory. Report opens with CLAIM and STATUS together at the top, then
  derivation (each step checkable), checks run (PASS / FAIL / NOT RUN),
  rival/failure mode, evidence that would change the answer, citation
  record. End with VERIFIED / UNVERIFIED / FAILED branch lists.
- HLRE grade (A–D, Track E; F1–F3 Track F) per narrow claim with the
  worst-of computation shown; independence I0–I4 stated; assumption,
  parameter and choice ledgers included. No invented numbers, no uncited
  benchmark figures. ABSTAIN ("I cannot verify this with the available
  tools") is a complete answer where verification is impossible.
- No silent correction: discrepancies go in a withdrawal/demotion note.

## Workstreams

- ws-a-core-computations: tasks 1–5 (IRH core computations)
- ws-b-branch-normal-form: task 6 (Jacobian branch normal form)
- ws-c-substrate-convergence: tasks 7 + 13 (substrate models, D4 convergence)
- ws-d-frameworks-rivals: tasks 8, 9, 10, 12 (QG frameworks, spacetime
  frameworks, derivations check, rival accounts)
- ws-e-cosmology-map: tasks 11, 14, 15 (bifurcations, researchers map,
  cosmological signatures)
