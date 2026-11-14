# Reader B — the IRH side (v93.1) for the torus-node comparison

**Mode:** deepest-research **FULL mode** (stated plainly, per the task order).
**Not systematic-review mode:** no PRISMA protocol, no meta-analysis; that form was
not chosen. **Skills:** `/deepest-research` (full) / `/cross-domain-discovery`
v2.0.0 / `/truth-seeking-frontier` v5 / `/hlre-v5-1`.
**Cross-domain stages:** S1–S4 run (claim registration, retrieval, invariance
alignment, Bartha/transportability audit — as already run in the cited WS-D/WS-E
reports, whose gates are reported here, not re-run). S5 (blending), S6
(tournament) and S7 (formal verification) **NOT RUN**: this is an extraction of
IRH's recorded claims for a comparison, not a model-building or formalisation
exercise — the same reason task 14 gives for not running S5–S7.
**Truth-seeking-frontier v5:** CLAIM + STATUS at the top of this file and of
each topic; checks PASS / FAIL / NOT RUN; ABSTAIN used as a complete answer
where the source supplies nothing to check.
**HLRE v5.1:** grades are reproduced **exactly as recorded** in the sources
below. Nothing is upgraded or re-graded here. "Derives" is used only for
deductive results from catalogued axioms in a specified system; everything else
is "postulated", "read off", "fitted", "suggested", or "remaining compatible
with". The skills themselves are DESIGN CLAIMS, ungraded — skill use is not
evidence of reliability.

## CLAIM + STATUS (together, at the top)

**CLAIM.** IRH v93.1 (McCrary, Zenodo DOI 10.5281/zenodo.22821689, 18 Sep 2026)
is a single-author programme whose **geometric core is carried at grade A**
$(D_{4}$ selection, isotropy, 2T/McKay/$E_{6}$, CFL — repo record, cited not re-earned),
whose **physical/substrate reading is $\leq C/D$**, and whose **constants account is
below that** (definitional triad relations, a downgraded $\alpha$ ansatz, an undecided
dimensional assignment). It does **not** derive Lorentzian signature, the
Einstein equations, $\alpha$, coupling values, or three generations; those are
open, retracted, or acknowledged inputs in its own Part IX / Part VII.
**STATUS: EXTRACTION COMPLETE.** Every claim below is tied to its source
location. Two manuscript-facing defects found by the co-scientist programme
are carried here as recorded: printed dispersion relation (7) FAILED as
printed (erratum, CFL bound unaffected); §III.3 envelope table UNVERIFIED.
The 11.85% / 11.90% band inconsistency is genuine and UNRESOLVED (Brandon's
call). No IRH grade is changed by this extraction.

## Sources read (all of them)

- Manuscript text: `co-scientist-tasks-2026-11-10/IRH_v93_1_source_rebuilt.txt`
  (1,638 lines; rebuilt from the Nov 5 source-rebuild PDF, 34 pp.).
- Repo record: `IRH-Theory-Development-Workspace/established/CORE.md`
  (compressed from Part VIII.1; `verification/` record cited therein).
- Programme guide: `co-scientist-tasks-2026-11-10/SUMMARY_AND_REPLICATION_GUIDE.md`
  (§4–§8 especially). **The guide's grades are used throughout, not the
  workstream reports' original grades** — the guide incorporates the
  2026-11-10 Hark replication audit corrections (see §12).
- WS-D: `ws-d-frameworks-rivals/task8_qg_frameworks.md`,
  `task9_spacetime_frameworks.md`, `task10_derivations_check.md`,
  `task12_rival_accounts.md` (plus `ws-d_summary.md`).
- WS-E task 14: `ws-e-cosmology-map/14-researcher-map-report.md`
  (and task 11, `11-bifurcations-report.md`, for the band figures).
- 2026-10-30 deepest-research report: `irh/D4-interference-deepest-research.md`
  (full mode; 784 arXiv hits screened, 181-paper core, 63-paper tight core).

**Grade vocabulary.** Track E = empirical/literature track; Track F = formal
track (F1 = kernel-verified in Lean, F2 = two independent machine routes,
F3 = single-route / deductive chain by exact computation). Independence
I0–I4; all new co-scientist verification is I1 max (artificial, one pipeline),
so new Track E claims cap at C and new Track F claims at F3 (F2 where the
Hark audit's two-route regrade applies — see §12). Carried grades (A core)
are the repo record's, cited not re-earned.

---

## 1. $D_{4}$ selection: $S = \tau^{2}/q_{4} = 64/141 \approx 0.454$, 17.3% margin over $A_{4}$*

| Narrow claim | Grade | Source |
|---|---|---|
| $D_{4}$ selected in 4D: $S = 64/141 \approx 0.453901$, exact rationals; margin $73/423 \approx 17.26$% over $A_{4}$\* (S = 12/31); $\mathbb{Z}^{4}$ and $A_{4}$ structurally excluded (T = 0) | **A (carried, geometric core)** | Manuscript §II.5; CORE.md "Geometry and selection"; guide §6 (task 8 C10) and §1 ("the only A grades in this package are CARRIED from the repo record") |
| $S = \tau^{2}/q_{4}$ is parameter-free in u, v; BCC recovered in 3D (Alexander–McTague) | **A (carried)** as the criterion's internal arithmetic; see caveat below | Manuscript §II.3–II.4; CORE.md |
| $\tau_{D}_{4} = 4/\sqrt{6}$, $\tau_{BCC} = 2/\sqrt{3}$, ratio exactly $\sqrt{2}$; $S_{BCC} = 16/45$ | **C** (two independent tools agree; $I1 \to C)$ as re-checked arithmetic | WS-D task 10 D8 (SymPy + flint.fmpq); guide §6.3 |
| Dynamical shell selection from noise; triad term causally responsible (77.1% vs 21.1% control; 89.5% annealed, independent reproduction) | **A (carried)** in the repo record; the *dynamic-account* formulation as registered in WS-C is narrower — see §1 note | Manuscript §II.6; CORE.md; `verification/sim7_fairtest.py` |

**Qualification that must travel with the claim (always cite it):**
conditional on **$q_{0}$ tuned onto the shell** — CORE.md: "$D_{4}$ phase band: 11.85%
of scanned plane **(conditional on $q_{0}$ tuned onto shell — always cite the
qualification)** — §II.7"; manuscript §VIII.3 lists "tuning of $q_{0}$ onto the $D_{4}$
shell" as an acknowledged INPUT, alongside the generation count, the value of
$\bar{\psi}$, conserved substrate dynamics, and the dimensional assignment.

**Two gradings of the same numbers, and why they differ (no re-grading):**
the **A** above is the repo record's carried grade (internal verification:
`verification/verify_claims.py` 51/51 checks passed; `sim6_units.py`,
`sim7_fairtest.py`; Lean 4 formalisation, 8 modules, `lake build` exit 0 —
CORE.md "Verification"). The 2026-10-30 deepest-research report grades the
same selection claim **D as presented there** (its C6: "IRH computation,
I0/I1; needs independent re-derivation for C, frozen I2 test for B") —
because *from the external literature alone* no screened paper computes $\tau$,
$q_{4}$ or S for $D_{4}/A_{4}$\*/$\mathbb{Z}^{4}$ in IRH's sense, and the 3D "validation" is internal
to IRH's framework. The report's headline: "The literature supports the
mathematics IRH reads off, and does not support IRH's physical reading of
that mathematics as a literature result." Both gradings are recorded here
as recorded; neither is changed by this extraction.

**Further qualifications recorded in the sources:**
- "$D_{4}$ wins" must always carry its criterion (S, with $q_{0}$ tuned onto the
  shell, in the stated $\bar{\psi}$ band). A criterion-free "$D_{4}$ is selected" is
  contradicted by the universal-optimality result under its own criterion
  (Cohn–Conway–Elkies–Kumar \$2007: $D_{4}$\$ is **not** universally optimal;
  2026-10-30 report §2, C5 CONTRADICTED as a universal claim).
- 3D BCC recovery caveat: Alexander–McTague is contested — Groh & Mulder
  (1999) show many structures simultaneously accessible at a spinodal;
  Klein (2001, arXiv:cond-mat/0104342) argues AM's BCC solutions are
  unstable (WS-E task 14 finding F1, grade C; 2026-10-30 report C4
  "CONTRADICTED as stated", at most C for "BCC special near spinodal").
  IRH's 3D check should be read as "recovers the AM prediction", not
  "recovers an established fact" (guide §8.1/§8.3).
- WS-C C1.2 (dynamic account predicts the full 24-mode pattern ONLY inside
  the band) **FAILED as written**: noise quench at $\bar{\psi}_{0} = -0.18 ($inside the
  quoted band) reaches 6/24 — the claim register's own falsifier. The
  basin/evolved-$\bar{\psi}$ corrected version is CONFIRMED under C1.3 (grade C).
  Guide §5.1.
- WS-C measured 24-mode global-minimum band at $r = -0.35$: $\bar{\psi} \in (-0.235$,
  $-0.125)$ — narrower than the manuscript's quoted $(-0.33$, +0.03), which
  is the union over quench depths; the +0.03 edge is UNVERIFIED (guide
  §5.1, §8.1).
- Independent corroboration as recorded: 4D Lennard-Jones crystallisation
  to $D_{4} ($Hoy [40]); 4D hard spheres, densest Voronoi cluster consistent
  with $D_{4} ($manuscript §II.5). WS-C C1.6: Landau + LJ corroborate the
  winner; S-transfer is deductive combinatorics; near-melting scope does
  NOT transfer (grade C); the Hoy LJ-MD leg was NOT RUN (abstention A5).

## 2. $E_{6}$ via 2T / McKay

| Narrow claim | Grade | Source |
|---|---|---|
| 24-cell vertices = binary tetrahedral group \$2$T \subset$\$ SU(2) (exhaustive); \$2$T/Q_{8} \cong \mathbb{Z}$_{3} (8+8+8\$ cosets); McKay: \$2$T \leftrightarrow$\$ affine $E_{6} ($unique; irreps {1,1,1,2,2,2,3}); $E_{6}$ chiral $(w_{0} \neq -1)$, complex **27**, $E_{6} \supset$ SO$(10) \supset$ SU$(5) \supset$ SM chain non-increasing in rank | **A (mathematics)** | Manuscript §IV.3; CORE.md "Algebra"; 2026-10-30 report §1–§2, C1–C2 (A, mathematics) |
| **Gauge algebra of IRH is $E_{6}$**, read off the substrate (via $S^{3} \cong$ SU(2), 2T, McKay) | **A as mathematics; D as a physical claim** | Manuscript §IV.4; CORE.md; 2026-10-30 report C8: "D as a physical claim (mathematics A, physical reading IRH's postulate; novelty budget)" |
| SO(8) excluded as gauge algebra (non-chiral: $-1 \in W(D_{4})$; Borel–de Siebenthal maximal-rank subalgebras contain no su$(3)\oplus$su(2)) | **A (carried)** — EXCLUDED by theorem | Manuscript §IV.1, §VIII.2; CORE.md |
| $E_{6}$ Cartan det 3, Smith diag(1,1,1,1,1,3); Weyl orders \|$W(D_{4})$\| = 192, \|$W(D_{5})$\| = 1920 | **C** (two independent tools) as re-checked arithmetic | WS-D task 10 D11, D13 (SymPy; guide §6.3) |
| 24-cell = 2T closure (576 products, $Q_{8}$ normal, 3 cosets) | **C** (two independent tools) | WS-D task 10 D12 |

**Why the two grades differ.** McKay \$2$T \leftrightarrow$\$ affine $E_{6}$ is standard ADE theory
(McKay 1980) and is grade A *as mathematics*. The physical step adds two
IRH postulates, both belonging in IRH's novelty budget (marked
`introduced_to_fit` unless independently motivated): (i) the pattern's
vertex set is to be read as a finite subgroup of SU(2) acting in the gauge
sector; (ii) the McKay graph is to be read as a gauge algebra
(2026-10-30 report §2). The manuscript's own ledger agrees in effect:
Part X grades the physical/substrate reading $\leq C/D$, and task 8 carries the
substrate reading at C/D (guide §6.1, C10). The same split applies to the
SO(8) exclusion: the exclusion is IRH's argument, graded by its own
premises, not by McKay.

## 3. Lorentz signature / spacetime emergence: what IRH does and does NOT derive

**What IRH does:**
- Postulates a real scalar field $\psi$ on a 4D base with Swift–Hohenberg-type
  dynamics; the primitive is "an oscillatory tension field $\psi(x,t)$ on $\mathbb{R}^{4}$"
  (manuscript §I.2). $D_{4}$ is the nodal interference pattern into which the
  field self-organises — not postulated as a lattice.
- **Conserved (Model B) dynamics required**, not a modelling choice:
  under Model A the mean drifts $1.8\times10^{-1}$ out of the stable band; under
  Model $B \bar{\psi}$ is preserved to $8.3\times10^{-17} ($manuscript §I.3; CORE.md).
  WS-C re-measured conservation at $1.1\times10^{-15}$ at t = 7.5 (P5, < 1e-12,
  PASS); the reference $8.3\times10^{-17}$ was not re-measured at that precision
  (guide §5.2, C2.5: conservation leg C, CFL leg F2).
- d = 4 marginality of the Swift–Hohenberg term: a new structural argument
  for four-dimensionality (manuscript §III.4; WS-D task 10 D3, grade C).
- $a_{0} = 2\pi/q_{0}$ derived, not postulated; site-field action retired
  (manuscript §I.3; WS-C C1.4, F2 per Hark regrade — see §12).
- An envelope-limit Schrödinger equation is established (§III.3); the
  exact dispersion, Hamiltonian positivity and CFL bound
  $\Deltat \leq (\sqrt{3}/2)\cdota_{0}/c ($worst-case spatial sum exactly 32) are carried at
  grade A (manuscript §III.1–2; CORE.md; WS-D task 10 D6, grade C as
  re-checked — CFL bound VERIFIED, see §10).

**What IRH does NOT derive (its own text):**
- **Signature derivation absent.** Manuscript §IX.3: "No purely classical
  Euclidean substrate is known to yield Lorentzian signature." Published
  dynamical-signature mechanisms (Greensite; Carlini–Greensite) require a
  one-loop effective potential with more fermionic than bosonic degrees of
  freedom — structure IRH (a single classical scalar) lacks. The v92
  argument from $i^{2} = -1$ is RETRACTED (Part VII): canonical $i\hbar$ is present
  in Euclidean field theory also; it does not select signature.
- **Dimensional assignment (A)/(B)/(C) undecided — Part IX.2.**
  (A) base is Euclidean spacetime, Lorentzian signature arising
  dynamically — most economical; the only reading consistent with citing
  4D optimality as evidence about spacetime; cost: requires the signature
  mechanism of §IX.3. (B) base is four spatial dimensions with one
  compactified — self-consistent via §II.$10 (D_{4} \cap {x_{4}=0}$ = FCC); cost:
  requires a compactification mechanism, predicts Kaluza–Klein modes,
  breaks the $D_{4}$ symmetry the selection argument uses. (C) base is
  auxiliary, spacetime emergent from defect dynamics — most speculative;
  no construction offered. Manuscript: "This must be decided. It is not
  resolvable by further calculation." (Task 9 C3, VERIFIED as a manuscript
  statement; task 12 D7: deciding §IX.2 is a prerequisite for any
  signature comparison.)
- **No Einstein-equation derivation** — see §8.
- **No joint early-universe narrative** — see §9 (IX.5) and §11 (WS-E
  task 15: no expansion mechanism, no GW/CMB model; ABSTAIN).

## 4. Gauge structure: $E_{6}$ read off the substrate; what is missing

| Narrow claim | Grade / status | Source |
|---|---|---|
| Gauge algebra is $E_{6}$, read off the substrate (§IV.4) | A (mathematics) / D (physical claim) — see §2 | Manuscript §IV.4; CORE.md; 2026-10-30 report C8 |
| $E_{6}$ breaking pattern | **NOT derived at all** — Part IX.4 "Must Be Restarted" | Manuscript §IX.4 |
| Higgs sector | **NOT derived at all** — §IX.4 | Manuscript §IX.4 |
| Higgs VEV $v_{0}$, $A_{3}$ resonance mass and widths, CKM mixing | **RETRACTED** (v92 numbers computed in an excluded framework, with independent arithmetic errors); "Nothing from those calculations should be carried forward" (§IX.4) | Manuscript Part VII, §IX.4 |
| Running couplings / derivation of $\alpha$ or coupling values | **FAILED** — "IRH'$s E_{6}$ identification derives coupling values / $\alpha$" (task 9 F4; no breaking pattern, no RG running; §IX.4) | Guide §6.2, §9; task 9 §3.7b |
| Monopole absence | **EXCLUDED** — inconsistent with $E_{6}$ breaking topology; IRH inherits the standard monopole problem (§V.3) | Manuscript §V.3, §VIII.2, Part VII |

Standard continuum QFT, for contrast, takes dimensionless constants as
measured inputs and couplings run (task 9 C6, grade C as a framework
description); $E_{6}$ unification constrains coupling relations conditionally
without fixing $\alpha^{-1} ($task 9 §3.7b, grade C).

## 5. Three generations: INPUT, not derived

**CLAIM: three generations is an INPUT, not an output.**
**STATUS: VERIFIED as IRH's own stated position** (manuscript §V.2 verdict,
§VIII.3 inputs, Part VII retraction table, abstract-grade discipline note).

- Manuscript §V.2: five candidate mechanisms tested and closed —
  (1) coset $\mathbb{Z}_{3}$ as diagram automorphism (permutes nodes; does not generate
  multiplicity); (2) centre $\mathbb{Z}_{3}$ grades representations (27: class 1,
  27̄: class 2, 78: class 0) but does not count copies; (3) anomaly
  cancellation imposes nothing $(E_{6}$ has no third-order Casimir — no
  exponent 2); (4) index route closed twice over (Lichnerowicz vanishing
  on $S^{3}/2T$; index density on a closed odd-dimensional manifold);
  (5) triality conflation. Verdict: "Three distinct objects were being
  conflated: a symmetry permuting cosets, a symmetry grading
  representations, and a multiplicity in the field content. The first two
  are real and structurally elegant. Neither is the third$\dots$ The framework
  does not predict three generations and has not done so since so(8) was
  excluded."
- 2026-10-30 report C9: "NOT CLAIMED by IRH itself (input, per profile)
  — do not upgrade."
- One generation of Standard Model fermions embeds in a single **27**
  (manuscript §IV.3) — that is the embedding statement, not a generation
  count. The 24-cell decomposing into three octets and $E_{6}$ generations
  coming in threes is, in the manuscript's words, "a coincidence$\dots$
  The match is not a mechanism."

## 6. Dimensional assignment undecided; constants account

**Dimensional assignment:** undecided, (A)/(B)/(C) mutually exclusive, not
resolvable by calculation — see §3 (manuscript §IX.2; task 9 C3).

**Constants account (task 9's headline: "IRH's constants account is the
weakest part of IRH, by IRH's own ledger" — geometric core grade A
mathematics; physical/substrate reading $\leq C/D$; constants account below
that):**

| Narrow claim | Grade / status | Source |
|---|---|---|
| §I.1 triad relations $(c = a_{0}\Omega_{P}, \hbar = M$\*ca${}_{0}, G = 24c^{2}a_{0}/M$\*) "derive" c, $\hbar$, G | **NOT A DERIVATION** — definitional re-expressions of measured Planck-scale quantities $(a_{0} = L_{P}/\sqrt{24}, \Omega_{P} = \sqrt{24}\cdotc/L_{P}, L_{P} = \sqrt{(\hbarG/c^{3})})$; a change of variables, not a derivation. Manuscript itself states the circle. | Manuscript §I.1; task 9 C1 (VERIFIED, manuscript + SymPy PASS that $a_{0}\Omega_{P} = c$ follows from the definitions); task 10 D1 (grade C); task 12 G3 (NOT A DERIVATION; definitional identities only, F3 as identities) |
| $\alpha^{-1}$ ansatz: $137 + 1/(28 - \pi/14) = 137.036002821941$ | **Arithmetic exact; derivation absent (downgraded).** Diff vs CODATA 2022 $(137.035999177) = +3.6449411\times10^{-6}$; $174\sigma$ from CODATA. Eddington-class: arithmetic verified, derivation absent — IRH *labels* it a downgraded ansatz, which is what saves it from Eddington's error. | Manuscript Part VII (downgraded, "Numerical ansatz only"); task 9 C2 (VERIFIED as arithmetic); task 10 D2 (grade C; 50-digit SymPy + flint.arb; NIST SP 959); task 12 G4 (**D, ansatz only**) |
| R = 2589 normalisation | **ABSTAIN** — no inputs in source; manuscript itself downgrades it ("arithmetic exact; the subtraction of 3 is not forced by any displayed symmetry") | Manuscript Part VII; task 10 D18 (ABSTAIN); guide §6.3, §9 |
| No rival surveyed derives $\alpha$ either | **C scoped / UNVERIFIED universal** (task 9 C7) — verified for surveyed sources only; a universal negative cannot be proved over all literature | Guide §6.2, §9 |
| "Anthropic reasoning explains $\alpha$ or IRH's tunings" | **FAILED / NOT SUPPORTED** (task 9 F5; ensemble unobserved; not in the manuscript) | Guide §6.2, §9 |

## 7. Band 11.85% vs 11.90%: genuine source inconsistency, UNRESOLVED

**STATUS: UNRESOLVED — Brandon's call. Nothing in the co-scientist package
resolves it (guide §8.1, §12 Q1).**

- The band is stated as **both 11.85%** (headline PREDICTION, §II.7) and
  **11.90%** $(w_{6} = 0$ value, §II.7 sixth-order paragraph) in the manuscript
  (WS-E task 11, §7.1 of the guide).
- **11.85% scan fraction NOT independently reproducible** — no scan code in
  repo `verification/`, scan definition absent $\to$ **INCOMPLETE-EVIDENCE**
  (WS-E task 11 C7; guide §7.1, §9).
- **$w_{6}$ narrowing 11.90% $\to 8.47$% NOT re-derivable** — $w_{6}$ term form unstated
  $\to$ **INCOMPLETE-EVIDENCE** (WS-E task 11 C8; guide §7.1, §9).
- WS-A task 3 (stated windows, W1 band): **11.60%** at $(\delta=0, w_{6}=0) \to$
  **8.36%** at $(\delta=0, w_{6}=0.2)$; hex-only 12.94% $\to 9.68$%. The manuscript's
  11.85% is **bracketed (11.60% full family, 12.94% hex-only) but NOT
  reproduced** — the manuscript's window is unstated, so the comparison
  is at trend level only (grade C; guide §4.3).
- WS-C task 7: measured 24-mode global-min band at $r = -0.35$ is
  $\bar{\psi} \in (-0.235, -0.125)$; manuscript $(-0.33, +0.03)$ is the union over
  quench depths; +0.03 edge UNVERIFIED (guide §5.1).
- WS-E task 11: coexistence band edges at $r = -0.35$ are
  **$[-0.23816, +0.90483]$**, NOT the manuscript band edges $(-0.33, +0.03)$
  — those are sub-pattern-competition edges whose data are not in the
  text (grade C, F2 on SymPy + arb — see §12; guide §7.1).
- WS-A task 3 and WS-C task 7 agree with each other (the measured slice
  is narrower than the quoted union); WS-E task 11 adds that the scan
  itself cannot be reproduced from the repo as it stands (guide §8.1).
- The no-note IRH recompile (33 pp., delivered 2026-11-10 separately) no
  longer flags the inconsistency up front (guide §8.1).

## 8. Gravity / Einstein equations: analog-gravity route RETRACTED as analogy

| Narrow claim | Grade / status | Source |
|---|---|---|
| Einstein equations from elasticity / substrate impedance | **RETRACTED** — "analogy, not derivation" (Part VII); §IX.3: the effective metric obeys the substrate's own equation of motion, not $G_{\mu\nu} = 8\piT_{\mu\nu}$. "This is a general limitation of analog models." Recovering the field equations, diffeomorphism invariance, the Bianchi identity, universal coupling to conserved stress-energy, and the two transverse-traceless graviton polarizations is "a separate and substantially harder programme." | Manuscript Part VII, §IX.3 |
| Transfer "substrate dynamics $\Rightarrow$ Einstein equations" (Bartha S4) | **FAILS** — critical features (Einstein dynamics, diffeomorphism invariance, TT polarisations) sit in the Negative Analogy. Confirms IRH v93.1's own retraction against Barceló–Liberati–Visser 2011 and Sindoni 2012. | WS-D task 8 §6.1; task 9 F3; guide §6.1, §9 |
| Jacobson (thermodynamic gravity$) \Rightarrow$ IRH transport | **FAILS / NOT ESTABLISHED** — thermodynamic premises have no positive analogue in IRH | WS-D task 8 §6.2; guide §6.1, §9 |
| Dynamical signature $\Rightarrow$ IRH reading (A) | **FAILS for v93.1** — fermion-dominant loop absent from a single real scalar | WS-D task 8 §6.3; task 9 F1; task 12 G7 (TRANSFER FAILS); guide §9 |
| Analog gravity gives an effective metric, never $G = 8\piT$ | **$C** (I1 \to C$; two published reviews in the record; also IRH's own stated position, I0 for that half) | Task 9 §3.4 (C5 VERIFIED); guide §6.2 |
| No framework in the task-8 set derives Einstein equations + Lorentzian signature + diffeomorphism invariance + SM gauge structure + a confirmed prediction all at once; no framework has a laboratory-confirmed Planck-scale prediction | **C** (task 8 C1–C12; C9-interpretation "gravity is emergent" grade **D**, exploratory) | Guide §6.1; task 8 §13 |

Task 8's comparative headline (for context, not an IRH claim): strongest
derived emergence result in the set is CDT's numerical 4D de Sitter
universe (spectral dimension $4.02 \pm 0.1 \to 1.80 \pm 0.25)$; only
prediction-in-advance is causal sets' heuristic $\Lambda \sim 10^{-120} ($Sorkin 1997).

## 9. Part IX open problems (IX.1–IX.5)

Manuscript Part IX is IRH's own open-problem register; Part X measures
"the distance to [a completed unified theory]" precisely by Part IX.

- **IX.1 Tractable Computation** (specified, requiring no new physics):
  larger-volume simulation for single-crystal ordering and phase-locking
  convergence; nucleation barrier height and critical droplet size;
  behaviour of the $D_{4}$ band under simultaneous detuning and higher-order
  terms; defect homotopy beyond elementary Burgers vectors; projection
  of $D_{4}$ to three dimensions along irrational directions. (WS-A task 1
  answers one IX.1.5 sub-question in the negative: |Aut$(D_{4})$| = 1152, so
  5 ∤ 1152 — **no projection direction yields exact icosahedral
  symmetry**, grade F3; guide §4.1.)
- **IX.2 Modeling Decisions:** the dimensional assignment (A)/(B)/(C) —
  see §3. Plus: the generation count, now an input, "whose assumed value
  must be stated as such wherever fermion content is discussed."
- **IX.3 Requires External Structure:** Lorentzian signature; Einstein
  field equations (see §8); quantum mechanics beyond single-particle
  envelopes (envelope-limit Schrödinger equation established §III.3;
  reproducing entanglement/Bell-violating correlations from a classical
  substrate requires nonlocality or superdeterminism — "a boundary, not
  a gap"); the monopole resolution (§V.3).
- **IX.4 Must Be Restarted:** the $E_{6}$ breaking pattern and Higgs sector —
  see §4.
- **IX.5 The Genuinely Open Physical Questions** — "Two questions are
  sharper than the rest and would most advance the programme":
  (1) **What fixes $\bar{\psi}$?** Under conserved dynamics it is an initial datum
  rather than a tuned coupling, which reclassifies the fine-tuning
  objection as a cosmological initial-condition question — "a different
  and weaker charge. But no mechanism sets its value, so whether
  occupying the $D_{4}$ band is a prediction or a tuning remains
  undetermined." (2) **What supplies the nucleation event?** The
  transition is first order (§II.9), so the $D_{4}$ phase must be nucleated.
  "Spontaneous emergence from a featureless substrate does not occur at
  the relevant baseline tension." Both are **ABSTAIN** in WS-E task 11
  (C10: stated open in the manuscript; guide §7.1, §9).
- **Missing joint early-universe narrative:** there is no stated
  expansion mechanism in v93.1 — no scale factor, Hubble, Friedmann, or
  parameter-driving law — so there is nothing to simulate (WS-E task 11
  C9, ABSTAIN; task 15: grep over the 1,638-line manuscript text finds
  "gravitational wave" = 0, "CMB"/"cosmic microwave" = 0, "photon" = 0,
  "baryon" = 0, "Hubble"/"Friedmann"/"scale factor" = 0; predictions
  VI.1–VI.7 contain no GW/CMB item; all 11 observable rows UNSTATED /
  ABSTAIN — guide §7.3). A 9-item requirements list for a future forward
  model is in task 15 §5; it is not a model.

## 10. What WS-D task 10 found about IRH's own text

Task 10 transcribed IRH v93.1's spacetime/constants derivations into
SymPy and checked them a second time with an independent tool
(python-flint exact rationals + arb, numpy). **78 checks pass (45 SymPy +
33 flint/numpy), 0 fail on re-run** (parent-verified 2026-11-11 ~01:30 CST;
guide §6.3). All D1–D19 grade **C** unless noted; geometric core carried
at **A**.

| Item | Verdict | Detail |
|---|---|---|
| D5 — printed dispersion relation (7), §III.1 | **FAILED as printed** (grade C) | Printed: $\sin^{2}(\omega\Deltat/2) = (\Deltat^{2}\cdot2J/(4M$\*$a_{0}^{2}))\cdot[2\Sigma(1-\cos) + \mu^{2}]$. EOM-derived: $\sin^{2}(\omega\Deltat/2) = (\Deltat^{2}\cdot2J/(4M$\*$a_{0}^{2}))\cdot\Sigma(1-\cos) + (\Deltat^{2}\mu^{2})/(4M$\*). Two errors in one equation: the $\Sigma$ term is doubled, and $\mu^{2}$ is placed inside the bracket (multiplied by the prefactor instead of by $\Deltat^{2}/(4M$\*)). Three internal checks favour the derived formula: (1) small-k J = M\*$c^{2}/12$ — the manuscript's own value — vs M\*$c^{2}/24$ from the printed formula; (2) k = 0 gives $\sin^{2}(\theta/2) = \Deltat^{2}\mu^{2}/(4M$\*) as §III.3 states; (3) the CFL table matches the derived formula. The manuscript's own §III.2 expansion ("at the worst case the bracket equals 32") uses the derived formula, contradicting the printed (7). **Manuscript erratum, not a refutation of the bound.** |
| CFL bound itself | **VERIFIED** | Worst-case sum 32 confirmed by $a 48^{4}$ Brillouin-zone scan; candidate values 4/3, $16\pi^{2}/3$, 1 reproduced (D6, grade C). |
| D17 — §III.3 envelope validity table $(4\times10^{-5}, 0.1$%, 1.0%, 11%, 133%) | **UNVERIFIED** | Under the natural reading (exact lattice dispersion vs $\omega = c$\|k\|) the computed errors are $1.67\times10^{-5}$, $4.17\times10^{-4}$, $3.75\times10^{-3}$, 4.11%, 36.3% $(\Deltat\to0)$ — smaller by factors 2.4–3.7; the zone-edge 133% is unreachable under that reading. The table'$s \Deltat$, carrier $\theta ($or $\mu)$, direction, and error definition are unstated. The VI.3 summary boundary (<1% for $a_{0}$\|k\| ≲ 0.3) **still holds** under the recomputed values (0.042% at 0.10, 0.375% at 0.30) — the boundary survives; the table's exact entries do not reproduce. |
| D18 — R = 2589 | **ABSTAIN** | No derivation inputs in the source (see §6). |
| D19 — side finding: exact linearity at $\Deltat = a_{0}/c$ | **C** | At $\Deltat = a_{0}/c$ the discrete dispersion is exactly linear $(\omega = c$\|k\|) along axis and body-diagonal directions (hand identity + numpy, ~$10^{-13})$. |
| D1–D4, D6–D16 (triad circle, $\alpha$ arithmetic, Derrick/d=4, dispersion identity, isotropy, selection rationals, ordered branch A\* = $0.0775753 / F = -0.0076323, \xi_{2}$ retraction factor 2, $E_{6}$ Cartan, 24-cell = 2T, Weyl orders, resonance maximum, triads, shell counts) | **C** (two independent tools agree) | Guide §6.3; task 10 §8. Also verified: $\alpha$ ansatz $174\sigma$ from CODATA; $\xi_{2}$ retraction factor 2. |

Run-record honesty note (guide §6.3): first SymPy run had 3 FAILs, of
which 2 were script bugs (E2 mis-stated identity; O2/O4 quaternion
product missing /2) and 1 was the F1 check restated as the exact
difference (the finding itself). A further assembly bug (G3-f check call
indented outside its `for` loop) was fixed; counts corrected from
46+32 to the true **45+33**.

## 11. What WS-D tasks 8/9/12 and WS-E task 14 already compared IRH against

**So the coordinator can tell what is NEW vs already covered. Nothing in
this section is a new comparison — it is a record of the comparisons
already run.**

### Task 8 — quantum-gravity frameworks (deepest-research FULL mode)
Frameworks: LQG / spin foams; string theory and AdS/CFT; asymptotic
safety; CDT; causal-set theory; GFT; emergent/analogue gravity
(incl. thermodynamic/Jacobson gravity); IRH v93.1. Comparative claims
C1–C12 grade **C**; C9-interpretation ("gravity is emergent") grade **D**.
Headline verdicts: no framework derives signature + Einstein equations +
diffeomorphism invariance + SM gauge structure + a confirmed prediction
together; no framework has a laboratory-confirmed Planck-scale
prediction; CDT's numerical 4D de Sitter universe is the strongest
derived emergence result; causal sets' $\Lambda \sim 10^{-120}$ is the only
prediction-in-advance; LQG's sharpest derived result is kinematic
(discrete area/volume); AdS/CFT remains a conjecture in AdS, not de
Sitter; asymptotic safety's Reuter fixed point is truncation-only
evidence; GFT condensate cosmology yields a modified Friedmann equation
but the condensate-as-GR-geometry step is unestablished.

### Task 9 — spacetime frameworks (deepest-research FULL mode)
Rivals coded: standard continuum QFT (constants as measured inputs);
Greensite / Carlini–Greensite dynamical signature (quantum, one-loop,
fermion-dominant); Mukohyama–Uzan / Kehayias et al. emergent signature
(classical, clock field, Galileon-not-GR gravity); analog/emergent gravity
(Barceló–Liberati–Visser; Sindoni); Dirac large-number hypothesis and
modern varying-$\alpha$ work; anthropic/multiverse accounts (Weinberg 1987);
Eddington-style numerology (control case — FAILED by measurement) and
modern $E_{6}$/unification numerology; causal-set theory (Hauptvermutung
unproved); Connes' noncommutative geometry / spectral action. Rival
characterisations C1–C6, C8 grade **C** (scoped to surveyed sources);
C7 (no rival derives $\alpha) **C$ scoped / UNVERIFIED universal**. Every
cross-framework derivation-transfer attempted FAILS the Bartha S4 audit
wherever a critical feature of the source derivation sits in the Negative
Analogy. Task 9's verdict: the comparison is "a coding and gap-flagging
exercise, not a verdict that any framework wins" — IRH's distinctive
grade-A result $(D_{4}$ selection) is a question no rival attempts.

### Task 12 — rival accounts formalised as executable models
Five models run under shared conditions against IRH as reference
(Model A: IRH reference; B: dynamical signature toy; C: varying
constants toy; D: anthropic selection; E: discrete spacetime / CDT fit);
driver: **55 checks, all PASS, exit 0** (parent re-run verified,
byte-identical output). Divergences D1–D7 (see `task12_divergence_table.md`):
D1 signature (Greensite predicts Lorentzian iff $n_{F} > n_{B}$; IRH predicts
nothing; transfer FAILS Bartha); D2 varying constants (toy linear $\alpha$ drift
$1\times10^{-15}$/yr excluded ~$25.6\times$ by Rosenband 2008, $\dot{\alpha}/\alpha = (-1.6\pm2.3)\times10^{-17}$/yr;
Dirac $G\propto1/t$ gives Ġ/$G = -7.25\times10^{-11}$/yr); D3 Ġ/G — **ABSTAIN** (no verified
primary-source bound in this run; no verdict on Dirac); D4 spectral
dimension (CDT flows $1.82\to4.02$ while IRH holds D = 4 at all scales; gap
~2.18 at $\sigma\to0$; endpoint disputed, ~2 vs ~3/2); D5 anthropic typicality
(accommodates observed $\Lambda$ under every prior, but typicality swings ~$80\times$
with the prior: 0.0015 uniform vs 0.1204 log-uniform — accommodation, not
prediction, grade D); $D6 \alpha ($no rival here derives $\alpha^{-1}$, and neither does
IRH); D7 prerequisite (deciding §IX.2 is a prerequisite for any signature
comparison). Grades: formal claims G1, G5, G8, $G12 \to **F3** ($two tools;
capped — human gates not run); physical claims G2, G9, G13, $G14 \to **C$**;
$G4 (\alpha$ ansatz$) \to **D$**; G11 (anthropic typicality$) \to **D$**; G3 (triad
"derivation"$) \to$ NOT A DERIVATION; G6/$G7/G10 \to$ ABSTAIN / TRANSFER FAILS.

### Task 14 — researcher map (deepest-research FULL mode; 73 papers, 3 slices, 63 queries)
Criteria (structural only, never surface vocabulary): (1) substrate
ontology, (2) selection mechanism, (3) testable predictions. Scorecard
(Table 1, 0/1/2 per criterion; whole map grade ceiling **C / I1**):
IRH (2,2,1) — alone in the (2,2) corner. Closest split by criterion:
substrate ontology — **GFT condensate cosmology** (Oriti & Pang 2025;
Calcinari et al. 2026; Bartha Gate 1 passes on ontology, fails on
mechanism); selection mechanism — **Alexander–McTague / Lifshitz–Petrich
pattern-formation lineage** (the only mechanism-level pass, Gate 2; no
spacetime claim); testable predictions — **Asymptotic Safety** strongest
(Higgs $\approx 126$ GeV pre-discovery; seesaw bound ~$10^{14}$ GeV) but furthest
from IRH on ontology. Other entries scored: Wolfram model (2,1,0);
Volovik helium droplet (2,0,1; Gate 5 ontology pass); Verlinde (1,0,2);
analogue gravity (1\*,0,1); causal sets (0,1,1); CDT (0,1,0); string /
swampland (0,1,1); LQG / spin foams (0,0,0); Kibble–Zurek (0,0,1);
AM/LP (0,2,2). **Verdict: no retrieved approach is close to IRH on all
three criteria at once.** S5/S6/S7 NOT RUN (reasons stated in the report).
Two new findings: **F1** Klein (2001) caveat on AM BCC (grade C);
**F2** SSRN $\to v93.1$ selection-principle change — maximal cymatic
complexity $(\to$ dimension 8) replaced by $S = \tau^{2}/q_{4} (\to D_{4})$; the principle
is version-dependent (grade C). **No independent work citing or
discussing IRH found** (search-bounded absence, INCOMPLETE-EVIDENCE);
**no findable Wise Journal revision record** (INCOMPLETE-EVIDENCE).
8-check rubric: 7/8 pass; independence is the binding limit.

## 12. The Hark audit corrections as recorded in the guide

The 2026-11-10 Hark replication audit (review:
`HARK_REPLICATION_AUDIT_REVIEW.md`) corrected the WS-A/C/E package; the
guide incorporates the corrections. **Use the guide's grades, not the
workstream reports' original grades.**

| Item | Correction (guide §4–§5, §8–§9) |
|---|---|
| WS-A task 5 hex6/fcc12 "stable attractors" | **FAILED as written** (F1; independently confirmed by the parent's own transverse run). Unperturbed starts stay hex6/fcc12 (invariant-subspace artefact: absent modes seeded exactly zero), but a transverse perturbation as small as 0.2% of A\* in the absent modes grows hex$6 \to$ full24 (5/5 runs) and fcc$12 \to$ full24 (4/4 runs) at $\bar{\psi} = -0.18$; the unperturbed control stays hex6. Corrected: at $\bar{\psi} = -0.18$ the 24-mode is the only attractor seen from perturbed starts; hex6/fcc12 are saddles. The sentence "the Model B analogue of the manuscript's annealed 6-mode outcome" is withdrawn. Full-pattern recovery from $\delta\phi \leq 1.0$ rad and $\pm20$% amplitude stands (grade C). |
| WS-C findings 6–7 ("both patterns are local minima at both $\bar{\psi}$"; "24-mode is a local minimum outside the band") | **FAILED as written** (F1). At $\bar{\psi} = 0$ the seeded 24-mode goes to 6-mode under perturbation; at $\bar{\psi} = +0.10$ to a 2-mode stripe-like state (Hark; not re-run by the parent). At $\bar{\psi} = 0$ hex6 is genuinely stable (Hark; not re-run by the parent). |
| WS-A A/B grades $\to C$ | **F5.** Independence bound $I1 \to C$ caps Track E; WS-A's original A/B grades (task 2 M6, task 3/4/5 band/droplet/basin claims) fall to **C** regardless of the human-gate amendment. |
| M6 (sixth-moment polynomial: mean 15, min 12, max 18, $\pm20$% signature) | **F2** (was A/B). Two routes in the package, verified: exact symbolic (Lagrange + AM-GM) + independent numerical optimisation (scipy, 200 starts: max 18.000000000000014, min 11.99999999999999). The $\pm20$% directional signature itself is grade C (Track E cap). |
| \|Aut$(D_{4})$\| = $1152 (\to$ no exact icosahedral projection) | **F3** (stays F3). One enumeration route (Gram enumeration); "matches the known order of $W(F_{4})$" is a cross-check, not a re-derivation. |
| WS-E C4 (coexistence band edges $[-0.23816, +0.90483]$ at $r = -0.35)$ — flint leg vacuous | **F3, record corrected; values stand at F2.** The package's flint script `fmpq_poly.roots()` returns `[]` for irrational edges (it finds rational roots only) — the "two tools" basis was vacuous as run. Values confirmed after the audit by Hark's arb computation and the parent's independent SymPy solve (agreeing to <1e-12), so C4 stands at **F2** on SymPy + arb. |
| WS-C make_figures / task2d (T = 0.5/1.0 rows) | **F4, provenance gap (numbers stand).** task2d overwrites `results/task2_transient.csv` with T = 5-only rows, and make_figures then CRASHES (IndexError, line 88). The shipped T = 0.5/1.0 rows came from an unshipped run; $p \approx 0.95$ stands (regenerated values match). |
| WS-A task-1 JSON extra fields | Provenance gap (numbers stand): shipped JSON carries `n_distinct_positions` / `max_multiplicity` the shipped script does not write; lattice fractions and shortest norms identical either way. |
| Triad `lock` metric for partial patterns | **F2, defect (minor).** `d4model.analyze` averages cos S over all 32 triads including roundoff modes; platform-dependent for partial patterns (hex6 0.304/0.455 vs shipped 1.000). Fix: active triads only. No load-bearing conclusion rests on the sub-pattern lock value except the task-5 §2 phrase "locked triads". |
| WS-$C C1.4 (a_{0}$, CFL), C2.1 (analytic A\*/F/V), C2.5 (CFL leg) | **F2** (Hark §6 regrade: two-plus routes — SymPy + flint + Z3, 31 PASS in `exact_checks.py`). |
| WS-E C1–C3, C6 (Landau values, thresholds, barrier) | **F2** (SymPy exact + python-flint, both run). |
| WS-C C1.2, C2.2, P4 | **FAILED as written** (unaffected by the regrade — see §1 and guide §5.2: C2.2/P4, fixed-point error is 0 at every ladder point so no decrease to measure; corrected claim — transient error decreases, $p \approx 0.95$ — is confirmed). |
| WS-D F3 caps | **Stand as stated.** The Hark audit's §6.5 repeal and $F3\toF2$ regrade applied to the audited package (WS-A/C/E) only. WS-D was not in that audit; its F3 caps stand. Whether the same two-route logic lifts any WS-D F3 (task 12 G1/G5/G8/G12) to F2 is not decided (guide §6, §12 Q10). |

Also recorded in the guide (§8.2): the Model B Hermitian artifact — the
shipped-style Model B update grows an anti-Hermitian roundoff component
$\times1.0142$/step and reaches NaN by ~6000 steps (WS-C: blows up at t = 27.5);
fix is per-step Hermitian symmetrisation/projection (exact no-op in exact
arithmetic). Any future Model B work must use the fixed stepper.

---

## What IRH does NOT claim

Load-bearing for the comparison — each item is IRH's own text or a
recorded verdict, not a rival's imposition:

1. **No signature derivation.** No mechanism in v93.1 yields Lorentzian
   signature from a classical Euclidean substrate (§IX.3); the $v92 i^{2}$
   argument is retracted. Dimensional assignment (A)/(B)/(C) is
   undecided and not resolvable by calculation (§IX.2).
2. **No Einstein equations.** The analog-gravity / impedance route is
   RETRACTED as analogy; the effective metric obeys the substrate's own
   equation of motion, not $G = 8\piT ($§IX.3, Part VII). Bartha S4 FAILS
   the transfer "substrate dynamics $\Rightarrow$ Einstein equations".
3. **No $\alpha$ derivation.** The $\alpha^{-1}$ ansatz is arithmetic-exact and
   derivation-absent (downgraded, Eddington-class); the §I.1 triad
   relations are definitional re-expressions, not derivations of c, $\hbar$, G.
4. **No generations derivation.** Three generations is an INPUT (§V.2
   verdict, §VIII.3); five mechanisms closed.
5. **No gravity emergence as a derived result.** No candidate Einstein
   equation, no signature mechanism, no cosmology, no GW/CMB prediction
   (task 15 ABSTAIN on all 11 observable rows); no expansion mechanism,
   so no joint early-universe narrative.
6. **No $E_{6}$ breaking pattern, Higgs sector, running couplings, or
   coupling values** (§IX.4; task 9 F4 FAILED). No monopole absence
   (EXCLUDED — inconsistent with $E_{6})$.
7. **No claim that $D_{4}$ selection is criterion-free.** Selection is S =
   $\tau^{2}/q_{4} = 64/141$ **conditional on $q_{0}$ tuned onto the shell**, in the
   stated $\bar{\psi}$ band; $D_{4}$ is not universally optimal (Cohn et al. 2007);
   the 3D BCC validation recovers a contested AM result (Klein 2001).
8. **No claim that the 11.85% band figure is reproduced.** It is
   bracketed but not reproduced; 11.85% vs 11.90% is a genuine source
   inconsistency, UNRESOLVED (Brandon's call).
9. **No claim that hex6/fcc12 are stable attractors under Model B, or
   that the 24-mode is a local minimum outside the band** — both FAILED
   as written (Hark F1); at $\bar{\psi} = -0.18$ the 24-mode is the only attractor
   seen from perturbed starts.
10. **No claim that the printed dispersion relation (7) is correct as
    printed, or that the §III.3 envelope table reproduces** — (7) FAILED
    as printed (erratum; CFL bound VERIFIED); the table is UNVERIFIED.
    R = 2589: ABSTAIN.

**What IRH DOES claim, in one line:** a verified geometric core $(D_{4}$
selection by triad interference, isotropy, 2T/McKay/$E_{6}$, CFL, d = 4
marginality — grade A carried), a defensible gauge identification, a
quantified stability domain, and a specific list of open problems
(Part IX) — "a well-posed research programme$\dots$ not a completed unified
theory, and the distance to one is large — measured precisely by Part IX"
(Part X).

---

## Checks run (PASS / FAIL / NOT RUN)

| Check | Result |
|---|---|
| Read manuscript text (1,638 lines), CORE.md, guide (§4–§8), WS-D tasks 8/9/10/12, WS-E task 14 (+ task 11), 2026-10-30 deepest-research report | PASS — all sources read; locations cited per claim above |
| Deepest-research FULL mode stated; systematic-review mode not used | PASS |
| Cross-domain S1–S4 (as run in cited reports); S5/S6/S7 | NOT RUN (reason stated at top — extraction, not model-building/formalisation) |
| Any new computation, GCP spend, VM work, Gemini grader call | NOT RUN — none performed; no repo commits, no manuscript edits, no filing, no contact with anyone |
| Re-grading of any IRH claim | NOT RUN — grades reproduced exactly as recorded; the two gradings of $D_{4}$ selection / $E_{6} ($repo-carried A vs 2026-10-30 literature-view D) are both reported with the reason they differ |

## VERIFIED / UNVERIFIED / FAILED / ABSTAIN branch lists (this extraction)

- **VERIFIED (as recorded claims, at their recorded grades$):** D_{4}$ selection
  arithmetic and margin (A carried); 2T/McKay/$E_{6}$ mathematics (A);
  SO(8) exclusion; Model B requirement; CFL bound; d = 4 marginality;
  the Part IX / Part VII negative statements (signature, Einstein,
  breaking, generations-as-input); the $\alpha$-ansatz arithmetic and its
  downgrade; the task-10 D1–D4/D6–D16/D19 checks (grade C).
- **UNVERIFIED:** §III.3 envelope validity table (D17); 11.85% scan
  fraction and $w_{6}$ narrowing (INCOMPLETE-EVIDENCE); +0.03 band edge;
  task 9 C7 as a universal negative; no independent work citing IRH
  (search-bounded absence).
- **FAILED (as written / as printed):** printed dispersion relation (7);
  "$E_{6}$ identification derives coupling values / $\alpha$"; "anthropic reasoning
  explains $\alpha$ or IRH's tunings"; Bartha transfers (Einstein equations,
  Jacobson, dynamical signature into IRH); hex6/fcc12 "stable attractors"
  and WS-C findings 6–7; WS-C C1.2, C2.2, P4 as registered.
- **ABSTAIN:** R = 2589; Ġ/G bound (task 12 D3); cosmic-expansion driving
  of (r, $\bar{\psi}, q_{0})$; what fixes $\bar{\psi}$ / what supplies nucleation (IX.5);
  GW/CMB forward model (task 15); full Greensite mechanism (task 12 G6).

## Evidence that would change the answers

- A derivation of $\alpha^{-1} ($or of $c/\hbar/G)$ from substrate premises — not a
  change of variables, not closeness to a future CODATA value (tasks 9,
  10, 12).
- A classical Euclidean substrate yielding Lorentzian signature; a
  substrate thermodynamics supporting a Jacobson-type argument; an IX.2
  decision with a construction (tasks 8, 9, 12).
- A derivation of (7)'s printed form from the stated action, with a
  correction of the §III.2 expansion; or the author stating $\Deltat$, $\theta ($or $\mu)$,
  direction, and error definition for the §III.3 table (task 10).
- Derivation inputs for R = 2589 in the source (task 10).
- Brandon's call on 11.85% vs 11.90%, and on the Klein caveat /
  selection-principle-change acknowledgements (guide §12).
- A human running the HLRE source/balance gates, which could raise
  individual descriptive grades (it could not raise a FAILED transfer).

## AI-contribution statement

Extraction and synthesis by an AI agent (Reader B) under deepest-research
FULL mode, cross-domain-discovery v2.0.0 (S1–S4 as run in the cited
reports; S5–S7 not run), truth-seeking-frontier v5, and HLRE v5.1. No new
computation was run; all grades and verdicts are quoted from the cited
sources. Human author and accountable party for IRH: Brandon D. McCrary.
All co-scientist verification cited here is artificial (I1 max); human
source/balance gates not performed.
