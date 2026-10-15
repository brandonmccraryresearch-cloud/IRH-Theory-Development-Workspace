# Open Problems Register — IRH v93.1, Part IX

Verbatim classification from the paper. Each item links to its research brief in
`problems/`. Status values: OPEN (untouched), ACTIVE (work in flight), BLOCKED
(waiting on a decision or external result), CLOSED (resolved — by derivation,
exclusion, or promotion to the established core).

---

## IX.1 — Tractable Computation (§IX.1)

Specified; requires no new physics. All OPEN.

| # | Problem | Paper reference | Status |
|---|---------|-----------------|--------|
| 1.1 | Larger-volume simulation: single-crystal ordering and phase-locking convergence | §II.6, §VI.1 | OPEN |
| 1.2 | Nucleation barrier height and critical droplet size | §II.9, §IX.5 | OPEN |
| 1.3 | D₄ band under simultaneous detuning and higher-order terms | §II.7 | OPEN |
| 1.4 | Defect homotopy beyond elementary Burgers vectors | §V.1 | OPEN |
| 1.5 | Projection of D₄ to three dimensions along irrational directions | §II.10 | OPEN |

→ Brief: `problems/IX1-tractable-computation.md`

## IX.2 — Modeling Decisions (§IX.2)

| # | Problem | Status |
|---|---------|--------|
| 2.1 | **The dimensional assignment.** Three mutually exclusive readings — (A) base is Euclidean spacetime with dynamical signature; (B) four spatial dimensions with one compactified; (C) auxiliary base with spacetime from defect dynamics. **Must be decided; not resolvable by further calculation.** | OPEN — decision required |
| 2.2 | Generation count as acknowledged input wherever fermion content is discussed. | OPEN — standing rule |

→ Brief: `problems/IX2-modeling-decisions.md`

## IX.3 — Requires External Structure (§IX.3)

| # | Problem | What it needs | Status |
|---|---------|---------------|--------|
| 3.1 | Lorentzian signature | A dynamical-signature mechanism; published routes [17][18] need a 1-loop effective potential with more fermionic than bosonic DOF (Greensite [41], Carlini–Greensite [42]). No purely classical Euclidean substrate is known to work. | OPEN |
| 3.2 | Einstein field equations | Beyond analog gravity [16]: diffeomorphism invariance, Bianchi identity, universal coupling to conserved stress-energy, two transverse-traceless graviton polarizations. Analog models give effective curvature, not GR [19]. | OPEN |
| 3.3 | QM beyond single-particle envelopes | Entanglement / Bell-violating correlations from a classical substrate require nonlocality or superdeterminism [38]. **A boundary, not a gap.** | OPEN — boundary acknowledged |
| 3.4 | Monopole resolution (§V.3) | Inflationary dilution or a breaking pattern avoiding the relevant topology. | OPEN |

→ Brief: `problems/IX3-external-structure.md`

## IX.4 — Must Be Restarted (§IX.4)

| # | Problem | Status |
|---|---------|--------|
| 4.1 | E₆ breaking pattern and Higgs sector — not derived at all. | OPEN |
| 4.2 | Higgs VEV, A₃ resonance mass and widths, CKM mixing. **Nothing from the prior calculations is carried forward** (computed in an excluded framework, with independent arithmetic errors). | OPEN — clean restart |

→ Brief: `problems/IX4-restart.md`

## IX.5 — Genuinely Open Physical Questions (§IX.5)

The two sharpest; highest leverage in the program.

| # | Problem | Status |
|---|---------|--------|
| 5.1 | **What fixes $\bar\psi$?** Under conserved dynamics it is an initial datum, reclassifying the fine-tuning objection as a cosmological initial-condition question — but no mechanism sets its value. | OPEN |
| 5.2 | **What supplies the nucleation event?** First-order transition (§II.9); the D₄ phase must be nucleated across a barrier at $\bar\psi=-0.18$. | OPEN |

→ Brief: `problems/IX5-genuinely-open.md`

---

## Falsifiable predictions (Part VI) — test targets

Tracked separately in `predictions/VI-predictions.md`: triad phase locking (VI.1),
baseline-tension band (VI.2), non-relativistic validity boundary (VI.3), stability
bound (VI.4), fourth-order isotropy / absence prediction (VI.5), defect spectrum
(VI.6), monopoles predicted not excluded (VI.7).

## Guardrails

- `guardrails/EXCLUDED.md` — do not revive.
- `guardrails/INPUTS.md` — state as inputs wherever used.
- `established/CORE.md` — what new work may build on.
