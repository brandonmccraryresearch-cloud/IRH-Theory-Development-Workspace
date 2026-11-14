# Task 1 formalization notes (cross-domain-discovery S1–S7, paper protocol)
# Written before the probe results are viewed (claim register frozen first).
# Catlab.jl NOT used (optional per skill; paper protocol suffices).
# S6 tournament NOT run as an LLM Elo tournament: the accounts are compared
# by measured simulation predictions under shared conditions instead.
# S7 Lean: NOT RUN (no new Lean work in WS-C; repo's 8 modules cited as-is).

## S1 — BPMF facets (Background / Purpose / Mechanism / Findings)

### A1 Static D4 (v92 ontology; manuscript Sec I.1, Part VII)
- Background: lattice field theory on a postulated lattice; Planck-scale constants.
- Purpose: define fields on D4 sites; derive constants from the lattice.
- Mechanism: NONE for selection. D4 postulated; site-field action; a0, $\Omega_{P}$
  primitive via $L_{P}$ = sqrt(hbar $G / c^{3})$.
- Findings: interference pattern Psi = 24.0 at lattice points (geometry, correct
  as geometry); constants as change of variables; two mutually inconsistent time
  steps (both violate the CFL bound); Model A drift 1.8e-1.

### A2 Dynamically selected D4 (v93.1; Sec I.2-II.9)
- Background: pattern formation; Swift-Hohenberg / Landau theory; Alexander-McTague.
- Purpose: explain WHY the substrate has D4 periodicity (selection, not postulation).
- Mechanism: tension-relaxation damped wave $\psi_{tt} + \gamma \psi_{t}$ = -dF/dpsi;
  Swift-Hohenberg operator penalizes |k| != q0; cubic triad term (T=192) breaks
  the linear degeneracy; conserved Model B dynamics holds psi-bar in the band.
- Findings: $S_{D}4 = 64/141$; D4 shell 77-84% direct quench, 89.5-100% annealed;
  full 24-mode attractor at psi-bar=-0.18; band 11.85% conditional on q0 tuning;
  first-order transition, nucleation required; a0 = 2 pi / q0 an output.

### A3 Equilibrium Landau selection (Alexander-McTague 1978; Elitzur-Karni-Rabinovici)
- Background: Landau theory of solidification; near-melting.
- Purpose: which lattice orders first on freezing.
- Mechanism: free-energy minimization over reciprocal shells; cubic term maximized
  by the shell with the most closed triads (cross-polytope in 4D).
- Findings: BCC in 3D; D4 (cross-polytope) in 4D at near-melting.

### A4 Particle crystallization (Hoy 4D Lennard-Jones MD, manuscript [40])
- Background: molecular dynamics, pairwise potentials.
- Purpose: what lattice does a supercooled 4D liquid freeze into?
- Mechanism: Newtonian particle dynamics under a Lennard-Jones potential.
- Findings: D4 at 0.59 < T < 0.63, N=648 (3x3x3x3 cells).

## S1 — Olog (text form; Spivak & Kent 2012 rules)
Boxes (indefinite singular noun phrases):
  "a tension field", "a reciprocal shell", "a closed triad", "a standing-wave
  pattern", "a lattice", "a baseline tension", "a free-energy functional",
  "a selection criterion S", "a quench depth".
Arrows (source label + arrow label + target label reads as a sentence):
  "a tension field" --has as resonant shell--> "a reciprocal shell"
  "a reciprocal shell" --contains--> "a closed triad"
  "a closed triad" --contributes to--> "a selection criterion S"
  "a selection criterion S" --orders--> "a standing-wave pattern"
  "a standing-wave pattern" --has as nodal set--> "a lattice"
  "a baseline tension" --tunes--> "a free-energy functional"
  "a free-energy functional" --determines--> "a selection criterion S"
  "a quench depth" --sets--> "a free-energy functional"
Path equivalence (commutative diagram, manuscript Sec II.5 "structural unification"):
  (field -> shell -> triads -> $S) \simeq ($field -> functional -> S).
  The interference picture and the energy picture are the same computation.
STATIC ACCOUNT'S OLOG: the box "a reciprocal shell" is a PRIMITIVE (no incoming
arrow from "a tension field"); there is no arrow "a tension field --has as
resonant shell--> ..." at all. That missing arrow IS the formal statement of
the missing selection mechanism (manuscript Sec I.1, objection 2).
Functor to 3D BCC: F maps D4-roots -> BCC reciprocal vectors, triads -> triads,
S -> S; preserves the diagrams (the same code computes both, Sec II.4). The
S-ordering is preserved: a meaningful functor with a natural isomorphism on
the ordering. Scope limit lives in S4, not here.

## S3 — Invariance alignment
Common structure across A1/A2/A3: the Landau functional F. A1 borrows it post hoc
(assumption A4 in the register: the most charitable static formalization); A2
derives selection from it; A3 minimizes it. The accounts do NOT reduce to the
same ODE: A1 has no dynamics; A2 has the damped wave + Model B; A3 has
equilibrium minimization. That non-reduction is the divergence, not a failure
of the alignment.
Dimensionless groups (exact arithmetic, SymPy/FLINT$): S = \tau^{2}/q4$ is pure
combinatorics; the detuning control is $(q0^{2}-8)^{2}$/|r|; the band edge is the
algebraic discriminant condition $(T u_{eff})^{2} = 4 v Q N r_{eff}$, NOT a dimensional
scaling law. Barenblatt First/Second Kind classification of the band edge:
NOT ESTABLISHED — ABSTAIN (the edge is an algebraic condition on the model,
not a measured scaling law; no RG-irrelevance test applies).
GENERIC check on A2: the damped wave is a damped Hamiltonian system (reversible
Hamiltonian part + damping); the Model B flow is a gradient flow of F under the
conserved $(L^{2}$ with nabla^2) metric. No GENERIC degeneracy violation is claimed
or needed: the two dynamics are used in their stated regimes (wave for
selection-from-noise, Model B for attractor stability), and their difference is
itself a measured model-form error (Task 2, item b).

## S4 — Bartha articulation: 3D BCC -> 4D D4 transfer via the S-criterion
Positive analogy: same Landau functional form; same triad-counting combinatorics;
same code computes both; both select the shell maximizing S; both corroborated
by an independent route (3D: experiment; 4D: LJ MD).
Negative analogy: 3D result is near-melting EQUILIBRIUM; 4D claim is DYNAMICAL
selection from noise; 3D has no psi-bar band / q0-tuning qualification; 4D has
no liquid phase in the model.
Neutral: whether 4D selection survives outside the near-melting regime
(Groh-Mulder caveat in 3D suggests regime-dependence).
Prior Association: Landau F$(B) + F = F' = 0$ -> ordering by S (deductive from
the functional + shell combinatorics; re-derived symbolically in exact_checks.py).
Critical features of the Prior Association: (i) shell combinatorics (N,T,Q)
enumerable; (ii) linear degeneracy broken ONLY by the cubic term; (iii) the
functional's cubic coefficient is the triad count.
GATE: none of (i)-(iii) sits in the Negative Analogy — (i) holds in 4D (exact
enumeration: 24,192,3384); (ii) holds (sim7 fair test: degenerate penalties
0.25/0.25); (iii) holds (same functional). TRANSFER PASSES for the combinatorial
selection claim.
SPLIT VERDICT: the near-melting EQUILIBRIUM scope is a critical feature of the
3D equilibrium claim with no 4D counterpart in the dynamic claim — scope
transfer FAILS, correctly: the manuscript does not claim near-melting equilibrium
in 4D; it claims dynamical selection. The gate splits, and the split is the
honest verdict.

## S4 — Transportability audit: LJ particle (A4) -> field substrate (A2)
Selection diagram: particle-system nodes (pairwise potential, Newtonian dynamics,
temperature, particle positions) vs field-system nodes (Swift-Hohenberg functional,
damped wave, quench depth, field power spectrum). S-nodes at: dynamics law,
control parameter, observable. The two systems share NO structural equations;
the D4 outcome cannot be transported as a causal effect (irreducible
sC-component: the mechanism nodes differ entirely). VERDICT: NOT transport —
independent corroboration (HLRE I2-style: independent re-derivation by a
different method, same winner). The manuscript's own framing agrees: "The two
determinations share no method" (Sec II.5).

## S5 — Blending (HDTP paper protocol; no maintained tooling)
Generic space: {reciprocal-shell interference + Landau functional}. Source
(static geometry) contributes the interference pattern; target (dynamics)
contributes tension-relaxation + Model B; the conflicting axiom (D4 postulated)
is dropped as lower-priority than the high-priority axiom (selection must be
derived). Blendoid retained: v93.1. This is a rational reconstruction, grade D
as a discovery claim — it explains the manuscript's architecture, it does not
add evidence for it.

## S7 — Z3 / Lean
Z3 (4.15.$4): r_{eff}(-0.18) > 0$, $r_{eff}(0) < 0$, $S_{D}4 > S_{A}4$* — all verified by
UNSAT of the negation (exact_checks.py, exit 0). Lean: NOT RUN — no new Lean
work in WS-C; the repo's 8 modules are cited to manuscript Sec VI-A.2 and
FINAL_AUDIT.md (lake build exit 0 as reported there). No Lean artifact is
produced here, so the DVP notational-collapse guard does not arise.
