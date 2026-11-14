# Deepest research (full mode): D4 geometry and interference dynamics, for IRH

**Mode:** deepest-research **full mode** (assistant's choice, per Brandon's standing
delegation). **Not** systematic-review mode: no PRISMA protocol, no meta-analysis;
Brandon did not explicitly choose that form.
**HLRE layer:** hlre-v5-1, as a protocol layer only. Grades attach to narrow claims.
HLRE's own error-catching benefit is graded **D** until its seeded-error benchmark
is run (per the skill itself). Language governance applied: "derives" is reserved
for deductive results; IRH readings are labelled as IRH's, not the literature's.
**Corpus and honesty note:** arXiv API search (24 queries, two passes) returned
**784 unique papers**; screened to **424 tier-A / 296 tier-B / 64 tier-C** by
title/abstract phrase rules, then to a **181-paper core** and a **63-paper tight
core** for .tex collection (rules in `RQ_BRIEF.md`, `screened.json`,
`core.json`, `tight_core.json`). This report is **not** a claim to have read all
784 papers in full: it is an abstract-level synthesis of the screened corpus plus
checked classic sources, with the .tex corpus collected for full reading. Any
claim below that turns on a paper's full text is marked as such and is not
upgraded by this report. Human gates (HLRE Step 6): not performed here —
all verification in this report is artificial (I1 at best); grades are capped
accordingly where noted.

## 1. Verdict first

The literature **supports the mathematics IRH reads off, and does not support
IRH's physical reading of that mathematics as a literature result**. That
distinction is the whole finding:

- **Established (Grade A, mathematics):** D4 root system / lattice, its 24
  roots as the 24-cell vertices, triality of SO(8)/Spin(8), the binary
  tetrahedral group 2T, and the McKay correspondence $2T \leftrightarrow$ affine E6.
- **Established (Grade A, pattern formation):** the Swift–Hohenberg equation
  (Swift & Hohenberg 1977) as a pattern-forming model, and the Landau
  three-wave / triad structure behind crystal selection arguments.
- **Contested in the literature (not a settled validation):** Alexander–
  McTague's original BCC-selection argument. Groh & Mulder (1999) show many
  structures are simultaneously accessible at a liquid–solid spinodal, with
  BCC special (lowest unstable-phase free energy) but not unique; a 2001
  arXiv analysis (cond-mat/0104342) finds Alexander–McTague solutions
  unstable. IRH's statement that its S criterion "recovers" BCC in 3D is
  therefore **IRH's computation under its own criterion**, not a literature
  consensus that Alexander–McTague is correct. It must be cited that way.
- **IRH's own (not literature) claims, graded at most C/D as presented
  here:** $S = \tau^{2}/q4$ as a dynamical selection criterion; D4 winning in 4D
  at S = 64/141; Model B (conserved) dynamics as a requirement; the gauge
  reading E6 as IRH's gauge algebra; any holographic interpretation of
  interference. None of these is found in the screened literature as a
  prior result, and none is upgraded by this report.
- **No literature bridge found:** no screened paper derives a physical
  substrate, a gauge algebra, or a holographic duality from D4 interference
  dynamics. Shared words — "holographic", "interference", "triality",
  "compactification" — are not bridges. See §6 for the debris audit.

## 2. D4 geometry: what is established

- **D4 root system (Grade A).** 24 roots in R4, the vertices of the regular
  24-cell; kissing number 24 in 4D; D4 is the densest lattice packing in
  4D in the classical Conway–Sloane sense, with 24 nearest neighbours at
  squared distance 2 and 24 more at squared distance 4 (Cohn–Kumar
  background, cited in the D4-optimality literature).
- **D4 is not universally optimal (Grade A, Cohn–Conway–Elkies–Kumar,
  Exp. Math. 16 (2007), 313–320; arXiv:math/0607447).** The 24-point D4
  configuration is not a universally optimal spherical code: another
  24-point code beats it for the potential f$(t) = (1-t)$^$(-1)$, and
  simulations converge to the competitor >90% of the time. IRH already
  records a related qualification (a competitor wins narrowly for
  Gaussian $\beta \in [2.6, 3.0])$. These are **different criteria** from
  IRH's S: universal optimality is about all absolutely monotonic
  potentials; S is about triad counts on a shell. Neither result
  refutes the other, and neither should be cited as the other.
  Consequence for IRH: "D4 wins" must always carry its criterion
  (S, with q0 tuned onto the shell, in the stated $\bar{\psi}$ band) — a
  criterion-free "D4 is selected" is contradicted by the
  universal-optimality result under its own criterion.
- **Triality (Grade A).** Spin(8) has three 8-dimensional representations
  (vector, spinor, conjugate spinor) permuted by outer automorphisms;
  this is special to D4 among simple Lie algebras. IRH's SO(8)
  exclusion argument (reps real/self-conjugate since $-1 \in W(D4))$
  is a representation-theoretic statement to be checked against
  the standard triality literature, not a fact this report
  re-derives; the triality papers in the corpus (including
  "Triality in so(4,4)", "Division Algebras, Triality, and
  Exceptional Magic", "The Standard Model, the Exceptional Jordan
  Algebra, and Triality") treat triality as mathematics and as
  speculative model-building, respectively — the two must not be
  conflated.
- **24-cell (Grade A geometry; Grade C/D physics uses).** The 24-cell,
  snub 24-cell from W(D4), and quaternionic pictures (Hurwitz units)
  are established geometry. Papers using the 24-cell for Standard
  Model flavour / spacetime imprints (e.g. arXiv:2511.10685,
  "Quantum Spacetime Imprints: The 24-Cell$\dots$") are **speculative
  physics uses**, not established results, and are graded D as
  physical claims here. They are not independent support for IRH:
  shared use of the 24-cell is shared geometry, not shared evidence
  (HLRE I1 warning: same mathematical object, different postulates).
- **McKay $2T \leftrightarrow E6 ($Grade A mathematics).** Finite subgroups of SU(2)
  give affine Dynkin diagrams via their McKay graphs; for 2T the
  graph is affine E6, with 7 irreps. This is McKay (1980) and standard
  ADE theory. **What it does not do:** it does not assign physical
  meaning to a vertex, a representation, or a gauge coupling. IRH's
  step "24-cell vertices form 2T, therefore gauge algebra is E6"
  adds two IRH postulates: (i) the pattern's vertex set is to be
  read as a finite subgroup of SU(2) acting in the gauge sector,
  and (ii) the McKay graph is to be read as a gauge algebra.
  Both belong in IRH's novelty budget, marked
  `introduced_to_fit` unless IRH independently motivates them.
  The same applies to the SO(8) exclusion: it is IRH's argument,
  graded by its own premises, not by McKay.

## 3. Interference dynamics: what is established, and where IRH departs

- **Swift–Hohenberg (Grade A).** Swift & Hohenberg, Phys. Rev. A 15,
  319–328 (1977), "Hydrodynamic fluctuations at the convective
  instability": $u_{t} = r u - (1+\nabla^{2})^{2} u + N(u)$; free energy with a
  $(\nabla^{2}+q0^{2})^{2}$ term selecting a shell |q| = q0. This is IRH's dynamical
  template, and it is genuine. What is **not** in Swift–Hohenberg:
  a 4D substrate, a D4 selection, Model B as a requirement, or any
  $\tau/q4$ combinatorics. IRH's damped-wave / Swift–Hohenberg dynamics
  on R4, with conserved (Model B) dynamics required because Model A
  drifts $\bar{\psi}$ out of the stable band, is IRH's construction. Model A/B
  in the Hohenberg–Halperin classification are dynamical
  universality classes for critical dynamics; IRH's use of "Model B
  required" must be justified as a modelling choice with its own
  stability argument, not cited to Hohenberg–Halperin as if they
  selected it.
- **Triads / three-wave interactions (Grade A mechanism, Grade D
  as IRH's shell combinatorics).** In pattern formation and in
  Landau theory, cubic terms from wavevectors summing to zero
  (k1+k2+k3 = 0 on the critical shell) favour lattices with many
  such triads. That mechanism is real and is the honest ancestor
  of IRH'$s \tau$. IRH's specific quantities — $\tau = T/N$^(3/2) counting
  ordered zero-sum triads on the reciprocal shell, q4, $S = \tau^{2}/q4$,
  $S_{D}4 = 64/141$, $S_{BCC} = 16/45$, $\tau_{D}4/\tau_{BCC} = 2$ exactly — are
  **IRH's definitions and computations**, not literature values.
  No screened paper was found computing $\tau$, q4, or S for D4/A4/Z4
  in IRH's sense. The 3D "validation" is therefore internal to
  IRH's framework (I0/I1), and its grade cannot exceed C without
  an independent re-derivation under a frozen protocol (I2) —
  which this report does not supply.
- **Alexander–McTague (Grade C at best, contested).** Original:
  Alexander & McTague, Phys. Rev. Lett. 41, 702 (1978), "Should
  all crystals be bcc?" — Landau theory suggesting BCC as the
  uniquely favoured 3D lattice near a weakly first-order transition.
  Counter-literature: Groh & Mulder, Phys. Rev. E 59, 5613–5620
  (1999), "Why all crystals need not be bcc" — many structures
  accessible at the spinodal, FCC among them, though BCC's unstable
  free energy is lowest; and cond-mat/0104342 (2001) — AM solutions
  are not stable, with nucleation implications. **IRH consequence:**
  do not cite Alexander–McTague as established support for a
  triad-selection principle in general. At most, IRH's S criterion
  is a new, sharper triad criterion whose 3D BCC outcome agrees
  with AM's conclusion while AM's own argument is disputed —
  that agreement is suggestive, not confirmatory, and the
  dispute must be disclosed in any IRH write-up (HLRE balance gate).
- **Competing 4D lattices (Grade B/C, by criterion).** A4, A4*,
  Z4, D4 are all classical 4D lattices; their packing/covering/
  quantizer properties are tabulated in Conway–Sloane and
  successors. IRH's claim that Z4 and A4 have zero triad content
  is a shell-combinatorics computation under IRH's definitions;
  it is checkable in principle (count zero-sum triples on the
  respective shells) and is a concrete, bounded verification task
  for a follow-up — but it is not found as a literature theorem
  in the screened corpus, so it stays IRH's claim, not a citation.
- **Interference in quantum/optical contexts (mostly vocabulary).**
  The corpus contains genuine interference dynamics (matter-wave
  interference of SU(N) fermions, arXiv:2206.02807; interferometry
  and complementarity/triality relations; holographic interference
  in optics and in AdS/CFT contexts) — none of which is a D4
  substrate dynamics. "Holographic interference" in the optics
  sense (recording an interference pattern) and in the AdS/CFT
  sense (bulk/boundary duality) are two different things, and
  neither is IRH's "intrinsic resonance holography" (a pattern
  that *is* the substrate). Conflating any of the three is a
  semantic-debris error; see §6.

## 4. What the literature does not contain (searched absence, with limits)

Within the declared queries (arXiv, 784 unique hits, abstract-level
screen), no paper was found that: (a) computes IRH's S for D4 vs
A4* vs Z4; (b) derives a 4D lattice from Swift–Hohenberg dynamics
with Model B as a requirement; (c) identifies a gauge algebra from
a nodal interference pattern via McKay; (d) proposes "intrinsic
resonance holography" or a D4 tension-field substrate. Searched
absence is not proof of absence in all literature (pre-arXiv
books, e.g. Conway–Sloane, and non-arXiv journals were covered
only via the classic-source checks in §2–§3), but the burden now
sits with any future claim that such a prior result exists: it
must name the paper.

## 5. HLRE claim record (narrow claims, grades)

| # | Narrow claim | Grade / status |
|---|---|---|
| C1 | D4 roots = 24-cell vertices; triality is special to D4 | A (mathematics) |
| C2 | McKay graph of 2T is affine E6 | A (mathematics) |
| C3 | Swift–Hohenberg (1977) selects a shell \|q\|=q0 and gives triad-mediated pattern selection | A (mechanism class) |
| C4 | Alexander–McTague BCC selection is established | **CONTRADICTED as stated** — contested; at most C for "BCC special near spinodal" (Groh–Mulder) |
| C5 | D4 is universally optimal | **CONTRADICTED** (Cohn et al. 2007) — do not claim; IRH's S-selection is a different criterion |
| C6 | IRH: $S_{D}4 = 64/141$ wins over A4* by 17.3%, Z4/A4 zero triad content | D as presented here (IRH computation, I0/I1; needs independent re-derivation for C, frozen I2 test for B) |
| C7 | IRH: Model B required; 24-mode wave is a global minimum in the stated $\bar{\psi}$ band with q0 on-shell | D (IRH's own, with qualifications that must travel with it) |
| C8 | IRH: gauge algebra is E6 via 2T/McKay; SO(8) excluded | D as a physical claim (mathematics A, physical reading IRH's postulate; novelty budget) |
| C9 | IRH: three generations derived | **NOT CLAIMED by IRH itself** (input, per profile) — do not upgrade |
| C10 | Literature contains a prior D4-interference substrate / IRH bridge | INCOMPLETE-EVIDENCE (searched absence, §4) — not a disproof |

Dependency ledger: C6–C8 depend on IRH v93.1's definitions $(\tau, q4$,
shell tuning, $\bar{\psi}$ band) and on its simulations, none re-derived here.
Any IRH write-up citing C1–C3 as support for C6–C8 without the
novelty-budget step commits a framing error (HLRE Gate 6/Step 6).

## 6. Semantic-debris audit (terms doing explanatory work in IRH)

- **"Substrate"** — operational target: the nodal pattern of $\psi$.
  Retain as a structural term only if $\psi$'s dynamics and the
  pattern-to-geometry map are specified; otherwise it is a
  load-bearing postulate (novelty budget).
- **"Holography"** — in IRH it does not mean AdS/CFT duality or
  optical recording. Ablation: replace with "pattern encodes
  geometry" and the explanatory payload is unchanged; the word
  "holography" adds no mechanism. Flag as **heuristic** until a
  bulk/boundary map is specified; do not cite optics/AdS
  holography literature as support.
- **"Resonance"** — operational core is shell tuning (q0 onto the
  D4 shell) and triad resonance (k1+k2+k3=0). Retain the
  operational part; the broader "resonance" narrative is
  heuristic.
- **"Selection"** — criterion-dependent (S vs universal optimality
  vs packing density give different winners). Never use
  unqualified; always name the criterion.
- **"Derives / derived"** — reserved. IRH's S-selection, gauge
  reading, and substrate claim are **postulated under stated
  premises**, not derived from the cited literature.

## 7. Licensed follow-ups (bounded, in order)

1. **Independent re-derivation of C6's shell combinatorics** $(\tau, q4$
   for D4, A4*, Z4, A4) by a verifier who did not see IRH's code,
   under a frozen counting rule — the single highest-value check;
   it moves C6 from D toward C if it passes, and falsifies it if
   it does not.
2. **AM-disclosure fix in IRH text:** cite Groh–Mulder (1999) and
   cond-mat/0104342 alongside Alexander–McTague (1978) wherever
   the 3D recovery is mentioned.
3. **Criterion labelling pass:** every "D4 wins / is selected"
   in IRH materials gets its criterion (S, $\bar{\psi}$ band, q0 on-shell)
   attached; remove any criterion-free selection claim.
4. **Full reads of the tight-core .tex set** (see §8) for the
   papers most likely to contain a prior S-like criterion —
   especially the 24-cell / triality / shell-design papers
   (e.g. harmonic strength of shells, arXiv:2308.14309) — before
   claiming searched absence beyond abstract level.
5. Nothing in this report licenses a new IRH mechanism, a gauge
   coupling calculation, or a claim about three generations.

## 8. Corpus and .tex inventory

- Search: `search_arxiv.py` (24 queries, two passes), metadata in
  `arxiv_search.json` (784 unique), screened tiers in
  `screened.json`, core in `core.json` (181), tight core in
  `tight_core.json` (63).
- .tex: collected under `tex/<arxiv-id>/` — **68 directories attempted
  (63 tight core + 5 from the first partial pass), 56 with .tex,
  110 .tex files, 5.8 MB**; 12 directories have no .tex (PDF-only
  sources, logged in `tex_download_log.txt`). Papers with no arXiv
  source (e.g. Alexander–McTague 1978, Swift–Hohenberg 1977,
  Cohn et al. 2007 journal version, Conway–Sloane book) have no
  .tex here — that is a source limitation, not a gap in the
  literature, and their citations above are to the published
  versions, not to .tex files. Two key old sources were recovered
  as single-file gzipped .tex: Cohn et al. D4-not-universally-optimal
  (`tex/0607447/d4.tex`) and the Alexander–McTague instability
  critique (`tex/0104342/alexmt.tex`).
- Key classic sources (checked via search, not .tex):
  Alexander & McTague, PRL 41, 702 (1978); Swift & Hohenberg,
  PRA 15, 319 (1977); McKay (1980) correspondence; Cohn–Conway–
  Elkies–Kumar, Exp. Math. 16, 313 (2007); Groh & Mulder,
  PRE 59, 5613 (1999); cond-mat/0104342 (2001).
- IRH anchor: v93.1 (2026-09-17) as summarised in
  `~/workspace/research/research-profile.md`, Strand 2. No IRH
  grade is changed by this report.
