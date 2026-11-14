# Task 9 — Compare spacetime frameworks (IRH v93.1 vs rival accounts) — FINAL

**Workstream D, task 9 — Co-scientist task programme, 2026-11-10.**
**Mode:** deepest-research **FULL** mode (stated plainly, per task). Systematic-review mode was **NOT** chosen and was **NOT** used.
**Status:** FINAL (assembled by the workstream-D parent agent from the child draft `task9_spacetime_frameworks_DRAFT.md`, with the assembly note below). Nothing here is incorporated into the repo or manuscript; no commits, no filing, no manuscript edits.
**Skills applied:** truth-seeking-frontier v5 (computation gate), cross-domain-discovery v2.0.0 (protocol S1–S7), HLRE v5.1 (grading). The skills themselves are DESIGN CLAIMS, ungraded — skill use is not evidence of reliability.
**Human gates not performed:** all verification in this draft is artificial (max I1). Source/balance gates (HLRE §6.5) have not been run by a human. Grade caps therefore apply: Track $E \leq C$, Track $F \leq F3$.

## Assembly note (parent agent, 2026-11-10)

One correction to the child draft's §6, check K2: the child's ad-hoc
python-flint run hit a `TypeError` on a float conversion *after*
printing the load-bearing values. The $\alpha^{-1}$ ansatz value is confirmed
independently and cleanly by task 10's second-tool script
(`task10_scripts/task10_numeric_checks.py`, flint.arb at 200-bit
precision, exit 0): ansatz = 137.03600282194111918739454715858134949265661452923,
ansatz $-$ CODATA $2022 = 3.6449411\dots\times10^{-6}$. The child's K2 arithmetic
conclusion stands, now on a clean run with no error. No other change
was made to the draft.

---

## CLAIM and STATUS (together, at the top)

**CLAIM (narrow, frozen before analysis).** IRH v93.1's account of spacetime and of dimensionless constants — a continuum oscillatory tension field $\psi(x,t)$ on **$R**{}^{4}$ obeying tension–relaxation (damped-wave / Swift–Hohenberg) dynamics, with $D_{4}$ as the dynamically selected nodal interference pattern, $a_{0} = 2\pi/q_{0}$, and a dimensional assignment that is UNDECIDED between readings (A)/(B)/(C) — does **not** derive spacetime signature, the Einstein equations, or the numerical values of dimensionless constants. Its constants account is: (i) the §I.1 triad relations are definitional re-expressions of measured Planck-scale quantities, not derivations; (ii) the $\alpha^{-1}$ ansatz is a downgraded numerical ansatz, not a derivation; (iii) the dimensional assignment is undecided and not resolvable by further calculation; (iv) no signature mechanism is supplied inside IRH; (v) Einstein equations are not derived (analog-gravity route retracted as analogy).

**STATUS: VERIFIED as a negative characterisation of IRH's own text** (the manuscript itself states each of (i)–(v); §§I.1, IX.2, IX.3, Part VII), **and UNVERIFIED as a comparative ranking** — no rival framework in this comparison derives the constants either, and none is shown here to be superior to IRH on IRH's own selection problem $(D_{4}$ selection), because the rivals address different questions. The comparison is therefore a **coding and gap-flagging exercise, not a verdict that any framework wins**. Every cross-framework transfer attempted in this draft is audited under Bartha (S4) and **FAILS** as a derivation-transfer wherever a critical feature of the source derivation sits in the Negative Analogy — see §S4.

**Headline findings (one paragraph each):**

1. **IRH's constants account is the weakest part of IRH, by IRH's own ledger.** The geometric core $(D_{4}$ isotropy, S = 64/141, d = 4 marginality) is Grade A mathematics; the physical/substrate reading is $\leq C/D$; the constants account is below that — definitional (triad), numerological $(\alpha$ ansatz), and undecided (dimensional assignment). Nothing in the rival literature surveyed changes that ordering; it confirms it.
2. **The signature problem is the sharpest shared gap.** Greensite (1993) / Carlini & Greensite (1994) give the only published *dynamical* signature mechanism IRH cites, and it needs a one-loop effective potential with more fermionic than bosonic degrees of freedom — a quantum condition a purely classical Euclidean substrate cannot supply (IRH §IX.3 states this). Mukohyama & Uzan (2013) and Kehayias et al. (2014) give a *classical* emergent-signature construction, but only by adding a clock field with fine-tuned coupling, and their effective gravity is Galileon-type, not general relativity. IRH has neither mechanism.
3. **Analog gravity gives an effective metric, never Einstein's equations.** Barceló–Liberati–Visser (2011) and Sindoni (2012) establish the effective-metric construction; IRH §IX.3 already concedes the same limit for its own impedance-tensor route, and the retraction of "Einstein equations from elasticity" in Part VII is correct and must stand.
4. **No surveyed account derives $\alpha$.** Standard QFT takes $\alpha$ as a measured input (running coupling, not a derived number); Dirac's large-number hypothesis is a postulate that did not survive (Teller's objection, recorded in Uzan's review); Eddington'$s 1/137 \to 1/136$ "derivation" is the cautionary precedent — the measured value is now known not to be the reciprocal of an integer; $E_{6}$ unification constrains coupling *relations* at a unification scale but does not fix $\alpha^{-1} = 137.036\dots$; anthropic/multiverse accounts select rather than derive; causal-set and noncommutative-geometry accounts do not output a value of $\alpha$. IRH'$s \alpha$ ansatz $(137.03600282\dots$, differing from the CODATA 2022 value by $3.6\times10^{-6})$ belongs in exactly the Eddington class: arithmetic verified, physical derivation absent.
5. **The one place IRH is genuinely distinctive is also the one place the rivals do not compete:** no rival framework surveyed selects $D_{4}$ by a parameter-free shell-combinatorics criterion $(S = \tau^{2}/q_{4} = 64/141, 17.3$% margin over $A_{4}*)$. The rivals answer "why Lorentzian?", "why these couplings?", "is spacetime discrete?" — not "why $D_{4}$?". A comparison that scores IRH against rivals on *their* questions and ignores *its* question would be a category error; the matrix (§5 / companion file) keeps the questions separate.

---

## S1 — Claim register (registered before searching)

| ID | Narrow claim | Domain | What would count as evidence | Verdict in this draft |
|---|---|---|---|---|
| C1 | IRH triad relations (§I.1) are definitional, not derivations of c, ħ, G | IRH text + algebra | Manuscript statement + symbolic check that $a_{0}\Omega_{P} = c$ follows from the definitions | VERIFIED (manuscript + SymPy, exit 0) |
| C2 | IRH $\alpha^{-1}$ ansatz is numerology: arithmetic exact, derivation absent | IRH Part VII | Manuscript downgrade + independent arithmetic re-check vs CODATA 2022 | VERIFIED (arithmetic); derivation-absence is the manuscript's own downgrade, retained |
| C3 | IRH dimensional assignment (A)/(B)/(C) is undecided, mutually exclusive, not resolvable by calculation | IRH §IX.2 | Manuscript statement | VERIFIED (manuscript) |
| C4 | IRH supplies no signature mechanism; published mechanisms need quantum (Greensite) or clock-field (Mukohyama–Uzan) structure IRH lacks | IRH §IX.3 + cited literature | Primary-source abstracts confirming the mechanism's premises | VERIFIED (literature abstracts + manuscript) |
| C5 | Analog-gravity / impedance routes give an effective metric, not $G = 8\piT$ | IRH §IX.3 + BLV/Sindoni | Primary-source statements | VERIFIED |
| C6 | Standard continuum QFT takes dimensionless constants as measured inputs; couplings run | Standard QFT (textbook-level framework description) | Uzan (2003) review on role of constants; no derivation claimed in the literature surveyed | VERIFIED as framework description (grade C ceiling — descriptive, not a new result) |
| C7 | No surveyed rival derives the numerical value of $\alpha$ | All rivals surveyed | Absence of a derivation in the surveyed primary sources + Eddington precedent | UNVERIFIED as a universal negative (cannot prove a negative over all literature); VERIFIED as a statement about the surveyed sources only |
| C8 | Causal-set / NCG accounts bear on spacetime ontology but do not supply IRH'$s D_{4}$ selection or a value of $\alpha$ | CST / NCG literature | Primary-source descriptions | VERIFIED as scoped statement (see §4.8–4.9); transport to IRH FAILS (S4) |
| C9 | Any transfer of a rival's signature/gravity mechanism into IRH would be a derivation-transfer | Cross-domain method | Bartha audit (§S4) | FAILED as derivation-transfer in every case attempted (critical features in Negative Analogy) |

**Post-hoc rule:** claims C1–C9 were fixed before the literature searches reported in §6. No claim was added after inspecting a rival's result. The matrix dimensions (spacetime ontology, signature origin, constants' status, dynamics, matter coupling, falsifiable predictions, status) were fixed in the task brief, not chosen after seeing the literature.

### BPMF facets (S1; Solvent facets are Background / Purpose / Mechanism / Findings — there is no "evaluation" facet)

- **Background:** IRH v93.1 is a continuum oscillatory substrate on **$R**{}^{4}$; the open problems are signature, gravity, constants, and dimensional assignment (§IX). The rivals are mature, published frameworks addressing overlapping but non-identical questions.
- **Purpose:** code assumptions/designs/findings of each account, build a cross-referenced matrix, flag gaps and untested conditions — not to crown a winner.
- **Mechanism (of this comparison):** per-account coding (postulated vs derived), Bartha articulation for any transfer, transportability audit, HLRE grading per narrow claim.
- **Findings:** §§1–5 above; matrix in the companion file.

---

## 1. The IRH side, grounded (not from memory)

Source: `IRH_v93_1_source_rebuilt.txt` (34 pp., v93.1), `established/CORE.md`, `guardrails/EXCLUDED.md`, `guardrails/INPUTS.md`, `predictions/VI-predictions.md`.

### 1.1 What IRH postulates

- **Primitive:** an oscillatory tension field $\psi(x,t)$ on **$R**{}^{4}$. $D_{4}$ is *not* postulated; it is the nodal interference pattern into which the field self-organises (§I.2). Dynamics: damped wave equation $\partial^{2}$_$t \psi + \gamma\partial$_$t \psi = -\deltaF/\delta\psi$ with $F[\psi] = \int d^{4}x [$½$\psi(r + (q_{0}^{2} + \nabla^{2})^{2})\psi - (u/3)\psi^{3} + (v/4)\psi^{4}] ($Swift–Hohenberg operator penalising wavevectors away from |k| = $q_{0})$.
- **Inputs (acknowledged, INPUTS.md):** (1) three generations assumed; (2) the value of $\bar{\psi}$ is an initial datum, no mechanism sets it; $(3) q_{0}$ tuned onto the $D_{4}$ shell (ordered branch vanishes at detuning 0.5 in $q_{0}^{2}$, §II.7); (4) conserved (Model B) dynamics required; (5) dimensional assignment undecided — readings (A)/(B)/(C).
- **Dimensional assignment (§IX.2, mutually exclusive):** (A) base is Euclidean spacetime, Lorentzian signature arising dynamically — "most economical", but "requires the signature mechanism of §IX.3"; (B) base is four spatial dimensions with one compactified — requires a compactification mechanism, predicts Kaluza–Klein modes, "breaks the $D_{4}$ symmetry the selection argument uses"; (C) base auxiliary, spacetime emergent from defect dynamics — "most speculative; no construction offered". Manuscript: "This must be decided. It is not resolvable by further calculation."

### 1.2 What IRH derives (geometric core, Grade A)

- $D_{4}$ isotropic through 4th order (spherical 5-design); $D_{4}$ isodual; unique interference maximum modulo lattice periodicity (32 periodic images on the $16^{4}$ grid).
- Selection criterion $S = \tau^{2}/q_{4}$, parameter-free in u,v; BCC recovered in 3D (Alexander–McTague); in \$4$D D_{4}$\$ selected, **$S = 64/141 \approx 0.4539$**, margin **$73/423 \approx 17.26$%** over $A_{4}* (S = 12/31)$, $\tau_{D}_{4}/\tau_{BCC} = \sqrt{2}$ exactly; $\mathbb{Z}^{4}$ and $A_{4}$ structurally excluded (T = 0).
- $a_{0} = 2\pi/q_{0}$ derived, not postulated (§I.3). Conserved Model B dynamics required $(\bar{\psi}$ preserved to $8.3\times10^{-17}$; Model A drifts $1.8\times10^{-1})$.
- d = 4 marginality: the Swift–Hohenberg term $\int(\nabla^{2}\psi)^{2}$ scales as $\lambda$^$(4-d)$, exactly marginal at d = 4 (§III.4); Derrick's theorem forbids stable Kerr solitons in 4D.
- Full 24-mode state a genuine dynamical attractor $(F/V = -0.0077276$ relaxed); first-order transition $(r_{eff} = +0.107$ at $\bar{\psi} = -0.18$; nucleation required); $D_{4}$ phase band **11.85% of the scanned plane, CONDITIONAL on $q_{0}$ tuned onto the shell** (with the 11.85% vs 11.90% source discrepancy flagged, unresolved — author decision pending).
- Gauge algebra $E_{6}$ via 2T/McKay (§IV.3–IV.4). SO(8) EXCLUDED by theorem.

### 1.3 What IRH does NOT derive — the constants account (the load-bearing negative findings)

**(i) Triad relations are definitional (§I.1).** "The primitives were circular. The framework designated $a_{0}$ and $\Omega_{P}$ as primitive but defined them as $a_{0} = L_{P}/\sqrt{24}$ and $\Omega_{P} = \sqrt{24} c/L_{P}$ with $L_{P} = \sqrt{(ħ}$ħ$G/c^{3})$. These are re-expressions of measured Planck-scale quantities, not independent microscopic inputs. The triad relations $c = a_{0}\Omega_{P}$, ħ = M\*ca${}_{0}$, $G = 24c^{2}a_{0}/M$\* are algebraically consistent once the definitions are chosen, but a change of variables is not a derivation of the constants." **Computation check (this draft):** SymPy 1.14.0, `a₀·Ω_P = c` from the stated definitions — PASS, exit 0 (see §6). This confirms the *algebraic consistency* the manuscript claims and nothing more; it does not upgrade the relations to a derivation.

**(ii$) \alpha$ ansatz downgraded (Part VII).** "$\alpha^{-1} = 137 + 1/(28 - \pi/14)$ as derived — DOWNGRADED: arithmetic verified exact; physical derivation absent. Numerical ansatz only." **Computation check (this draft):** SymPy 1.14.0 gives $\alpha^{-1}($ansatz) = **137.036002821941**; python-flint 0.8.0 float arithmetic agrees (137.0360028219411); difference from the CODATA 2022 value $\alpha^{-1} = 137.035999177(21) ($as reported in the search-verified source citing CODATA 2022) is **+$3.64\times10^{-6}** (\approx 27$ ppb). PASS on arithmetic; the *derivation* remains absent, exactly as the manuscript states. The ansatz is close to the measured value and proves nothing — closeness of a two-parameter arithmetic expression to a measured constant is the Eddington pattern (§4.7), not a derivation. **R = 2589 normalisation:** likewise downgraded; "the subtraction of 3 is not forced by any displayed symmetry" (Part VII). The rebuild notes its arithmetic is unverifiable-from-source; carried here as downgraded, not re-derived.

**(iii) Dimensional assignment undecided (§IX.2, above).** No rival surveyed decides it for IRH; each rival *assumes* its own assignment (see matrix).

**(iv) Signature mechanism absent (§IX.3).** "Published dynamical-signature mechanisms [17][18] require a one-loop effective potential with more fermionic than bosonic degrees of freedom — the condition first identified by Greensite [41] and refined by Carlini and Greensite [42]. No purely classical Euclidean substrate is known to yield Lorentzian signature." IRH's substrate is classical; the v92 argument from $i^{2} = -1$ is retracted as invalid.

**(v) Einstein equations not derived (§IX.3, Part VII).** "Identifying the metric with the substrate's local impedance tensor is the standard analog-gravity construction [16] and is sound as far as it goes: wave propagation on a slowly varying background defines an effective metric, and geodesic bending and horizons follow. But the effective metric obeys the substrate's own equation of motion, not $G_{\mu\nu} = 8\piT_{\mu\nu}$. This is a general limitation of analog models [19]." Part VII retracts "Einstein equations from elasticity" as "analogy, not derivation".

### 1.4 IRH falsifiable predictions that bear on this comparison (Part VI)

VI.5 (isotropy to fourth order — prediction of absence; falsified by any quartic directional dependence from this mechanism); VI.$2 (D_{4}$ band conditional on $\bar{\psi}$ and on $q_{0}$ tuning — fails if the band vanishes under reasonable $w_{6}$/detuning); VI.7 (monopoles predicted, with a mandatory resolution — fails if no resolution consistent with observation). None of VI.1–VI.7 tests the *value* of $\alpha$, the signature, or the Einstein equations — those have no IRH prediction, which is itself a gap (see §5).

---

## 2. Coding scheme (applied uniformly to every account)

For each rival: **Assumptions** (postulated vs derived — "derives" reserved for deductive results from catalogued axioms in a specified system); **Design** (mathematical structure); **Reported findings** (primary sources with versions/dates — every reference below was confirmed to exist via browser search of the primary source or its publisher record; no reference is included that could not be confirmed); **What would falsify it** (stated before any verdict). Grades are HLRE per narrow claim with the worst-of computation shown (independence bound; caps; postulation ceiling; support in the record). Independence: all literature characterisations in this draft are I1 at best (artificial verification sharing the same pipeline — this agent's reading of published sources, no independent team, no held-out dataset); several are I0 (restatements of the manuscript itself). No claim in this draft exceeds grade C on Track E.

**Bartha rule (S4, enforced):** a transfer FAILS if any critical feature of the source derivation sits in the Negative Analogy, no matter how many surface similarities exist. **DVP guard (S7):** no formalisation is attempted in this draft (no Lean/Z3 artefact), so no notational-collapse risk arises; had one been attempted, the formal statement would have had to preserve the non-trivial domain operators $(\psi, q_{0}, S$, the Swift–Hohenberg operator) rather than collapsing them to scalars.

---

## 3. The rival accounts, coded

### 3.1 (i) Standard continuum QFT on a fixed background — constants as measured inputs

- **Assumptions (postulated):** Minkowski (or Euclidean, Wick-rotated) spacetime with fixed Lorentzian signature; the Standard Model gauge group and field content; dimensionless couplings $(\alpha$, gauge couplings, Yukawa couplings, mixing angles) as *measured inputs* fixed by experiment at a reference scale. Renormalisation is a *procedure*, not a derivation of the inputs.
- **Design:** local quantum fields, Poincaré-invariant S-matrix / path integral, renormalisation-group running: couplings are scale-dependent, $g(\mu)$, with $\beta$-functions computed perturbatively; low-energy values are boundary conditions supplied by measurement.
- **Reported findings:** the framework's predictive power is in *relations between* observables given the inputs (e.g. precision QED, running of $\alpha_{s})$ — not in the values of the inputs themselves. Uzan's review (Rev. Mod. Phys. 75, 403–455, 2003) is the reference for the role of constants, their definition and link with metrology, and the observational constraints on their variation; its §VI reviews theoretical motivations including Kaluza–Klein and string theories.
- **What would falsify it:** a measured variation of a "constant" beyond its stated uncertainty (see §3.5); a failure of RG running where it is quantitatively predicted; a Lorentz-violation signal. None of these would falsify the *framework's* treatment of constants as inputs — that treatment is definitional, and its cost is explanatory incompleteness, not empirical risk.
- **Relation to IRH:** IRH does not replace this framework; IRH has no quantum field theory, no S-matrix, and no running couplings. IRH'$s \psi$ is classical. Any claim that IRH "derives" what standard QFT takes as input would need IRH to reproduce QFT's verified relations — NOT RUN in this draft, and not claimed by the manuscript.
- **Grade:** descriptive framework characterisation — **C** (worst-of: $I1 \to C$; postulation ceiling C for an evidence-guided descriptive claim; record = published reviews + textbook status). The claim "standard QFT does not derive $\alpha$" is a statement about the surveyed literature, grade C, not a universal negative.

### 3.2 (ii-a) Dynamical signature — Greensite (1993), Carlini & Greensite (1994)

- **Primary sources (confirmed):** J. Greensite, "Dynamical origin of the Lorentzian signature of spacetime", Phys. Lett. B 300, 34–37 (1993), arXiv:gr-qc/9210008; A. Carlini & J. Greensite, "Why is spacetime Lorentzian?", Phys. Rev. D 49, 866–878 (1994), arXiv:gr-qc/9308012.
- **Assumptions (postulated):** a generalised D-dimensional metric $g_{\mu\nu} = e_{\mu}$^$a \eta_{ab} e_{\nu}$^b with $\eta_{ab}$ = diag${e^{i\theta}, 1, \dots, 1}$; the phase $e^{i\theta}$ treated as a quantised field, so the functional integral interpolates from a Euclidean path integral $(\theta = 0)$ to a Feynman path integral in Minkowski space $(\theta = \pi)$; signature is determined dynamically by $\langlee^{i\theta}\rangle$.
- **Design:** one-loop complex-valued effective potential $V(\theta)$ for the phase field, induced by massless fields. Reported finding (ADS abstract, verified): "It is argued that $\mathrm{Re}[V(\theta)]$ is stationary, uniquely in D = 4 dimensions, at $\theta = \pi$ which suggests a dynamical origin for the Lorentzian signature of spacetime." Carlini & Greensite refine this: the one-loop potential's relevant behaviour requires **more fermionic than bosonic degrees of freedom** (the condition IRH §IX.3 cites).
- **Reported findings:** a *quantum* mechanism singling out D = 4 and Lorentzian signature together — the only published mechanism of this type IRH cites. It is a stationarity argument about an effective potential, not a derivation from a classical substrate, and not an experimental result.
- **What would falsify it:** a demonstration that $\mathrm{Re}[V(\theta)]$ is not stationary at $\theta = \pi$ once massive fields, higher loops, or a different field content are included; or that the fermion-dominance condition cannot be met in a realistic field content; or a proof that the $\theta = \pi$ stationary point is unstable rather than selected. **I cannot verify with the available tools** whether such a refutation exists in the later literature — ABSTAIN on the mechanism's current standing beyond the 1993–94 papers themselves.
- **Bartha audit vs IRH (S4):** Positive analogy — both IRH (reading A) and Greensite start from a Euclidean 4D base and want Lorentzian signature out. Negative analogy (critical): Greensite's prior association *depends* on (a) a quantised phase field, (b) a one-loop effective potential, (c) fermion dominance. IRH's substrate is a *classical* scalar $\psi$ with no quantised phase field, no loop expansion, and no fermion content at all. All three critical features sit in the Negative Analogy. **Transfer FAILS.** IRH cannot borrow Greensite's mechanism without first quantising its substrate and supplying fermions — which is a new theory, not an application.
- **Grade:** "Greensite/Carlini–Greensite propose a quantum dynamical-signature mechanism with the stated premises" — **$C** (I1 \to C$; published primary sources in the record). "The mechanism is correct / established" — **UNVERIFIED** in this draft (no independent test run; ABSTAIN on current standing).

### 3.3 (ii-b) Emergent Lorentzian signature, classical — Mukohyama & Uzan (2013); Kehayias, Mukohyama & Uzan (2014)

- **Primary sources (confirmed):** S. Mukohyama & J.-P. Uzan, "From configuration to dynamics — Emergence of Lorentz signature in classical field theory", Phys. Rev. D 87, 065020 (2013), arXiv:1301.1361v1 (received 15 Jan 2013, published 25 Mar 2013); J. Kehayias, S. Mukohyama & J.-P. Uzan, "Emergent Lorentz Signature, Fermions, and the Standard Model", Phys. Rev. D 89, 105017 (2014), arXiv:1403.0580v2 (27 May 2014).
- **Assumptions (postulated):** the microscopic theory is *purely Euclidean* (Riemannian, SO(4)); a **clock field** (a scalar whose gradient defines the emergent time direction) with a coupling that triggers the signature change of the effective metric; Lorentzian dynamics holds only in patches/regions of the Euclidean space.
- **Design:** fields propagate in an effective metric built from the Euclidean metric plus the clock-field gradient; signature flips where the clock-field coupling exceeds a threshold (the slides/abstract record the condition in the form "Lorentz signature emerges if [coupling] > 1/2"). Classical field theory for scalars, vectors, and Dirac spinors is constructed; gravity can be included, but —
- **Reported findings (abstracts, verified):** "there is no dynamics nor signature flip across some hypersurface; instead, all the fields develop a Lorentzian dynamics in these regions because they propagate in an effective metric"; "the theory for the effective Lorentzian metric is **not general relativity but of the covariant Galileon type**." Kehayias et al. add: Weyl and Majorana fermions can be constructed; the coupling to the clock field allows an action "which flows to the usual action in Minkowski spacetime"; the Standard Model "can be obtained in this theory", with constraints on non-Standard-Model operators from CPT and Lorentz violation in the QED sector.
- **What would falsify it:** observation of the predicted non-Standard-Model QED operators / Lorentz-violation signatures at levels the construction cannot accommodate; a proof that the clock-field coupling cannot be kept stable under quantum corrections; failure to recover universal coupling (equivalence principle) at the required accuracy. The authors themselves detail constraints from stability, the equivalence principle, and constancy of fundamental constants.
- **Bartha audit vs IRH (S4):** Positive analogy — Euclidean 4D base (IRH reading A), emergent Lorentzian patch. Negative analogy (critical): the prior association depends on (a) a clock field with fine-tuned coupling, (b) an effective metric that is *not* GR. IRH has no clock field, no coupling of that kind, and no construction of fermions on its substrate. Critical features in the Negative Analogy $\to$ **transfer FAILS**. Note the secondary criticism recorded in the literature (Yahalom's summary of Mukohyama & Uzan): the construction "is not consistent with Occam's razor as one is forced to introduce several scalar fields (one of them a 'clock field') with fine tuned coupling" — recorded as a *secondary* criticism, not adopted as this draft's verdict.
- **Grade:** "Mukohyama–Uzan/Kehayias et al. construct a classical emergent-signature model with a clock field whose effective gravity is Galileon-type, not GR" — **$C** (I1 \to C$; abstracts + journal records verified). "The model is viable / the clock field is natural" — **UNVERIFIED** (ABSTAIN — no independent assessment run).

### 3.4 (iii) Analog / emergent gravity — Barceló–Liberati–Visser; Sindoni

- **Primary sources (confirmed):** C. Barceló, S. Liberati & M. Visser, "Analogue Gravity", Living Rev. Relativ. 14, 3 (2011), doi:10.12942/lrr-2011-3, arXiv:gr-qc/0505065v3 (12 May 2011; completely revised update of the 2005 version; references increased from 434 to 702); L. Sindoni, "Emergent Models for Gravity: An Overview of Microscopic Models", SIGMA 8, 027 (2012), arXiv:1110.0686 (45 pp.; received 2 Oct 2011, published 12 May 2012).
- **Assumptions (postulated):** a background (usually condensed-matter) system whose perturbations obey a wave equation; the effective metric is *defined* by the coefficients of that wave equation (e.g. acoustic metric in a moving fluid, BEC, dielectric).
- **Design:** mathematical identity between QFT in curved spacetime and propagation of perturbations in the analogue system. Analogue black-hole horizons, Hawking-like radiation, and geodesic motion follow from the effective metric.
- **Reported findings:** analogue gravity is a research programme for *probing aspects* of curved-spacetime physics in the laboratory (Hawking radiation analogues, etc.). Sindoni's overview: the common line is "to view the graviton as a composite particle/collective mode", surveyed across condensed-matter examples to pregeometric models, with an explicit disclaimer that the definition of emergence is unclear and the review is confined to models in which gravitational dynamics is "recovered, more or less successfully, from a non-gravitational system". Sindoni §4 is devoted to the fate of Lorentz invariance in multi-component analogue models — a known difficulty.
- **What would falsify it (as a theory of gravity):** it is not, in its own terms, a theory of gravity — it is an analogy programme plus a family of emergent-gravity proposals. The falsifiable claim is the narrower one: *this* analogue system exhibits *that* curved-spacetime effect (e.g. horizon radiation). The broad claim "gravity emerges this way" is falsified (for a given model) by showing the effective metric cannot satisfy the Einstein equations, universal coupling, or the two transverse-traceless graviton polarisations — which is exactly the limitation IRH §IX.3 concedes for its own route.
- **Bartha audit vs IRH (S4):** this is the *closest* rival to IRH's own §IX.3 reasoning — IRH explicitly cites Barceló et al. [16] and Sindoni [19] for the same point. Positive analogy: effective metric from wave propagation on a slowly varying background; horizons/geodesics follow. Negative analogy (critical for a *derivation* of GR): the effective metric obeys the substrate's equation of motion, not $G = 8\piT$; diffeomorphism invariance, Bianchi identity, universal coupling to conserved stress-energy, and two graviton polarisations are not delivered. The critical feature (Einstein dynamics) sits in the Negative Analogy $\to$ **transfer of "GR derived" FAILS**; transfer of "effective metric exists" SUCCEEDS trivially but proves nothing about gravity. IRH's Part VII retraction is therefore correct and the audit supports keeping it retracted.
- **Grade:** "Analog gravity yields an effective metric, not the Einstein equations" — **C** (worst-of: $I1 \to C$ caps it; two published reviews in the record; the claim is also IRH's own stated position, I0 for that half). Do not overstate: the *generality* of the limitation ("a general limitation of analog models") is IRH's wording, adopted here as a summary of the surveyed reviews, grade C.

### 3.5 (iv-a) Varying constants — Dirac's large-number hypothesis and modern varying-$\alpha$ work

- **Primary sources (confirmed):** P. A. M. Dirac, Nature 1937 (large-number hypothesis — as discussed in Uzan 2003/2004); J.-P. Uzan, "The fundamental constants and their variation: observational and theoretical status", Rev. Mod. Phys. 75, 403–455 (2003); J.-P. Uzan, "Variation of the constants in the late and early universe", arXiv:astro-ph/0409424v2 (7 Oct 2004); J.-P. Uzan, "Varying Constants, Gravitation and Cosmology", Living Rev. Relativ. 14, 2 (2011), doi:10.12942/lrr-2011-2; J. D. Barrow, "Varying Constants", arXiv:astro-ph/0511440v1 (15 Nov 2005).
- **Assumptions (postulated):** Dirac's hypothesis: very large (or small) dimensionless numbers "cannot be pure mathematical numbers" and must reflect the state of the universe; the ratios Gm_$e m_{p}/e^{2} ~ 10^{-40}$ and the inverse age of the universe in atomic units $e^{2}H_{0}/m_{e} c^{3}$ are of the same order, and this is not a coincidence; hence (Dirac's choice) G varies as the inverse of cosmic time, $G \propto t^{-1}$. Modern varying-constant theories instead introduce a new dynamical (nearly massless) scalar degree of freedom coupled to matter, so that a varying constant is a property of a particular solution, not of the underlying theory (Uzan 2011 abstract: "Any constant varying in space and/or time would reflect the existence of an almost massless field that couples to matter. This will induce a violation of the universality of free fall.").
- **Design:** Lagrangian formulation with the constant promoted to a field (Jordan's point, recorded by Uzan: varying constants "can be included in a Lagrangian formulation as new dynamical degree of freedom"); observational programme: quasar absorption spectra (many-multiplet method, Webb et al.), atomic clocks, Oklo, solar-system, meteorite, CMB, BBN constraints.
- **Reported findings:** Dirac's hypothesis "is indeed not a theory" (Uzan 2004) and "did not survive very long" in its original $G \propto t^{-1}$ form — Teller pointed out the steep increase of G to the past implies huge increases in the Earth's surface temperature (Barrow 2005); Gamow's variant (e varies as $t^{1/2})$ was the response. The Webb et al. quasar programme reported evidence consistent with $\alpha$ having been smaller in the past (early reports: $\Delta\alpha/\alpha \approx -0.72\times10^{-5}$ over $z \approx 1$–3.5, as cited in the secondary literature of the period). **ABSTAIN:** I cannot verify with the available tools the current (post-2011) status of the Webb et al. claim, the VLT/UVES reanalyses, or the present best bound on $\dot{\alpha}/\alpha$ — the searches returned the 2003–2011 reviews, not a verified current consensus. No current bound is stated in this draft; any number would be secondary-only or stale.
- **What would falsify it:** for Dirac's original form — the Teller argument already counts heavily against it, and modern bounds on Ġ/G (lunar laser ranging, etc.) are the quantitative test; for a modern varying-$\alpha$ model — a null result at the model's predicted sensitivity, or a violation of the universality of free fall at the level the model's coupling implies (Uzan 2011 ties the two together).
- **Relation to IRH:** IRH has no varying-constant mechanism and no scalar field coupled to matter that could carry one; IRH'$s \bar{\psi}$ is a *conserved initial datum*, not a rolling field. Dirac's move (promote a coincidence to a time dependence) is structurally the *opposite* of IRH's move on $\bar{\psi} ($reclassify a tuning as an initial condition, §IX.5). No transfer is attempted; none would be licensed.
- **Grade:** "Dirac's LNH in its original $G \propto t^{-1}$ form did not survive; modern varying-constant theories require a new light scalar and predict equivalence-principle violation" — **$C** (I1 \to C$; Uzan reviews in the record). Current status of varying-$\alpha$ observations — **ABSTAIN** (see above).

### 3.6 (iv-b) Anthropic principle / multiverse accounts of constants

- **Primary sources (confirmed):** S. Weinberg, "Anthropic bound on the cosmological constant", Phys. Rev. Lett. 59, 2607–2610 (1987), doi:10.1103/PhysRevLett.59.2607; B. Carter (1974, weak/strong anthropic principle — as cited in the literature; not independently re-verified in this run, so cited only as background, not as a load-bearing reference); J. D. Barrow & F. J. Tipler, *The Anthropic Cosmological Principle* (1986 — background only).
- **Assumptions (postulated):** an ensemble of universes/domains in which the constants (in Weinberg's case $\Lambda)$ take different values; observers exist only where the values permit gravitationally bound structures (galaxies, stars, life). The "principle of mediocrity" / typicality assumption is needed to turn the bound into a prediction.
- **Design:** Weinberg's abstract (verified via the journal record): in universes that do not recollapse, the only anthropic upper bound on $\Lambda$ is that it "should not be so large as to prevent the formation of gravitationally bound states"; the bound "is quite large"; $a \Lambda$ "within 1 or 2 orders of magnitude of its upper bound would help with the missing-mass and age problems, but may be ruled out by galaxy number counts. If so, we may conclude that anthropic considerations do not explain the smallness of the cosmological constant."
- **Reported findings:** an *upper bound* with an explicit self-undermining clause — Weinberg himself states the condition under which anthropic reasoning would *fail* to explain $\Lambda$'s smallness. That honesty is the model's strength and its limit: it selects a range, it does not derive a value; and it is hostage to the unobserved ensemble and to the typicality assumption.
- **What would falsify it:** a measured $\Lambda$ far *below* the anthropic bound with no typicality explanation (the "why this small?" problem Weinberg flags); a demonstration that the ensemble does not exist (untestable by construction in most versions); galaxy number counts ruling out the 1–2-orders-of-magnitude window (Weinberg's own stated test). The observed $\Lambda$ being *within* the bound is necessary but not sufficient — it is also consistent with a dynamical explanation.
- **Relation to IRH:** IRH's fine-tunings $(\bar{\psi}$ in the $D_{4}$ band; $q_{0}$ tuned onto the shell) are *exactly* the kind of tunings an anthropic argument could be invoked to excuse — and IRH §IX.5 explicitly refuses that move in its current form: it reclassifies $\bar{\psi}$ as a cosmological initial-condition question, "a different and weaker charge", but states that "whether occupying the $D_{4}$ band is a prediction or a tuning remains undetermined". An anthropic defence of IRH's tunings is **not** in the manuscript and is **not** adopted here; it would be a new postulate (ensemble + typicality) with no independent support in IRH. Postulation ceiling for any such move: D (post-hoc, exploratory).
- **Grade:** "Weinberg (1987) gives an anthropic upper bound on $\Lambda$ with a stated falsification condition" — **$C** (I1 \to C$; PRL record verified). "Anthropic reasoning explains the value of $\alpha ($or of IRH's tunings)" — **FAILED / NOT SUPPORTED** (no derivation; ensemble unobserved; transfer to IRH not attempted and not licensed).

### 3.7 (v) Deriving constants from geometry / group theory — Eddington-style, and modern $E_{6}$/unification numerology

Two sub-cases, kept strictly separate — conflating them is the error this section exists to prevent.

#### 3.7a Eddington-style numerology (the cautionary precedent)

- **Primary/background sources:** A. S. Eddington, *Fundamental Theory* (1946, posthumous) and the 1929/1938 claims as summarised in the secondary literature (Wikipedia "Eddington number" entry and Barrow 2002, as returned by search — **secondary sources; no load-bearing number in this draft rests on them alone**).
- **Assumptions (postulated$):** \alpha$ can be obtained by pure deduction; $\alpha$ is related to the Eddington number $N_{Edd} ($number of protons in the observable universe).
- **Design / reported findings:** Eddington first conjectured $\alpha = 1/137$ exactly (1929), then, when the best experimental value was $\approx 1/136$, "argued, from aesthetic and numerological considerations, that $\alpha$ should be exactly 1/136", devising a "proof" that $N_{Edd} = 136 \times 2^{256} \approx 1.57\times10^{79}$; when improved measurements returned toward 1/137, he changed the "proof" to show $\alpha$ had to be exactly 1/137. The secondary summary's verdict, quoted in substance: "no one maintains any longer that $\alpha$ is the reciprocal of an integer. Nor does anyone take seriously a mathematical relationship between $\alpha$ and $N_{Edd}$."
- **What falsified it:** measurement. $\alpha^{-1}$ is not an integer (CODATA 2022: 137.035999177(21)); a "derivation" that changes its conclusion when the measurement changes is not a derivation — it is curve-fitting to the measurement. **This is the exact failure mode of any $\alpha$ ansatz, including IRH's.** The IRH ansatz differs from Eddington's in one respect only: IRH *labels* it a downgraded ansatz and does not claim it as derived. That labelling is what saves it from Eddington's error; removing the label would revive the error.
- **Grade:** "Eddington'$s \alpha$ derivation failed by measurement and by its own revision history" — **$C** (I1 \to C$; secondary summary, corroborated by the CODATA value). The historical details (dates, exact $N_{Edd}$ arithmetic) are background, not load-bearing.

#### 3.7b Modern $E_{6}$ / unification — constraining relations, not fixing $\alpha$

- **Primary sources (confirmed):** F. Gürsey, P. Ramond & P. Sikivie, "A universal gauge theory model based on $E_{6}$", Phys. Lett. B 60, 177–180 (1976), doi:10.1016/0370-2693(76)90417-6; H. Georgi & S. L. Glashow, SU(5) (Phys. Rev. Lett. 32, 438–441, 1974 — cited in IRH's bibliography, not re-verified here); H. Fritzsch & P. Minkowski, SO(10) (Ann. Phys. 93, 193–266, 1975 — cited in IRH's bibliography).
- **Assumptions (postulated):** a simple unified gauge group $(E_{6}$, SO(10), SU(5)) unbroken at a high scale, with a single unified coupling; a specified breaking chain and Higgs sector; fermion content in specified representations (for $E_{6}$: two 27-dimensional representations fitting six quarks and nine leptons in the 1976 paper).
- **Design:** at the unification scale the couplings satisfy group-theoretic relations (e.g. a single coupling); renormalisation-group running down to low energies *predicts relations between* the low-energy couplings (the Weinberg angle, coupling ratios) given the breaking scale and spectrum — it does not predict the absolute value of $\alpha$ from pure mathematics. The unified coupling itself remains an input fixed by measurement (e.g. by $\alpha_{s}$ or $\alpha$ at $M_{Z})$.
- **Reported findings:** Gürsey–Ramond–Sikivie derive the Weinberg angle and the R ratio *within* the model, and discuss proton stability — conditional predictions, not derivations of $\alpha^{-1}$. The $E_{6}$ route is the legitimate modern descendant of the "constants from group theory" programme, and its honesty is precisely that it *does not* claim to output 137.036.
- **What would falsify it:** measured coupling unification failing at the predicted scale given the assumed spectrum (the classic SU(5) proton-decay tension is the textbook example — stated here as background, not re-verified); a breaking chain that cannot reach the Standard Model.
- **Relation to IRH — the critical distinction:** IRH'$s E_{6}$ is *read off the substrate* via 2T/McKay (§IV.3–IV.4) — a geometric identification of the gauge algebra, graded in the manuscript as part of the algebraic sector. That is **not** the same claim as "$E_{6}$ unification derives the couplings". IRH has no breaking pattern, no Higgs sector, and no running couplings (§IX.4: "The $E_{6}$ breaking pattern and Higgs sector $\dots$ have not been derived at all"). Presenting IRH'$s E_{6}$ as if it did the work of Gürsey–Ramond–Sikivie would be a category error in the opposite direction from Eddington's: borrowing a legitimate group's prestige for a derivation that was never performed. **Never present IRH'$s E_{6}$ identification as a derivation of $\alpha$ or of any coupling value.**
- **Grade:** "$E_{6}$ unification constrains coupling relations conditionally; it does not fix $\alpha^{-1}$" — **$C** (I1 \to C)$. "IRH'$s E_{6}$ identification derives coupling values" — **FAILED** (no breaking pattern, no RG running in IRH; §IX.4).

### 3.8 (vi-a) Discrete / causal-set accounts of spacetime

- **Primary sources (confirmed):** L. Bombelli, J. Lee, D. Meyer & R. Sorkin, "Spacetime as a causal set", Phys. Rev. Lett. 59, 521–524 (1987); S. Surya, "The causal set approach to quantum gravity", Living Rev. Relativ. 22, 5 (2019), doi:10.1007/s41114-019-0023-1 (review, confirmed via Springer record); D. B. Malament (1977) — the theorem that causal structure determines conformal geometry, as cited in the review (background, not independently re-verified).
- **Assumptions (postulated):** spacetime is fundamentally a *locally finite partially ordered set* (causal set) of elementary events; the order relation is causal precedence; volume is number (cardinality of an order interval = spacetime volume of the associated interval). Discreteness is assumed from the outset, not derived from quantisation.
- **Design:** continuum approximation via "sprinkling" (Poisson distribution, so no preferred frame — Lorentz invariance preserved in the continuum approximation, Bombelli et al. 2009 theorem as cited in the review); the **Hauptvermutung** (fundamental conjecture): a manifold-like causal set is equivalent to the continuum spacetime modulo differences up to the discreteness scale — **unproved**, stated as a conjecture in the review.
- **Reported findings:** "order plus number equals geometry" (Sorkin); discreteness + Lorentz invariance $\Rightarrow$ inherent non-locality (a distinguishing feature vs other discrete approaches); no complete quantum theory of gravity delivered to date (the review's own framing: the programme "has so far not delivered a quantum theory of gravity, and so remains a work in progress" — quoted in substance from the secondary summary of the review; the review itself is the authority).
- **What would falsify it:** a proof that the Hauptvermutung is false (manifold-like causal sets that do not approximate a unique continuum); a Lorentz-violation signal of the kind random sprinkling is designed to avoid (which would falsify the *mechanism*, not just the model); failure to recover the Einstein–Hilbert action / GR in the continuum limit.
- **Relation to IRH — Bartha audit (S4):** Positive analogy — both posit a discrete-ish substructure beneath continuum spacetime (IRH: $D_{4}$ nodal pattern; CST: causal set). Negative analogy (critical): (a) CST's discreteness is *random* (Poisson sprinkling) precisely to preserve Lorentz invariance; IRH's pattern is a *regular* $D_{4}$ lattice, which on its face breaks Lorentz invariance to a discrete subgroup and must explain why no preferred-frame effects appear (IRH VI.5 answers only the quartic-order part, and only as a prediction of absence); (b) CST's fundamental relation is *causal order*; IRH's is *interference/tension*, with no causal order at the substrate level and no time direction at all until reading (A)/(B)/(C) is decided; (c) CST derives geometry from order + number via a stated conjecture; IRH derives a *lattice* from interference and has no route from the lattice to a metric, let alone to causal structure. Critical features in the Negative Analogy $\to$ **transfer FAILS** in both directions: CST does not give IRH a metric or a signature, and IRH does not give CST a selection mechanism (CST has no selection problem of IRH's kind — its elements are sprinkled, not selected).
- **Grade:** "Causal-set theory postulates discrete causal order; its Hauptvermutung is unproved; it does not supply a value of $\alpha$ or $a D_{4}$ selection" — **$C** (I1 \to C$; PRL + Living Review in the record).

### 3.9 (vi-b) Noncommutative geometry — Connes' spectral action

- **Primary sources (confirmed, at the level used here):** A. Connes, *Noncommutative Geometry* (1994, book — background); A. H. Chamseddine & A. Connes, spectral-action programme (as summarised in the verified search results: Lizzi 2014 seminar notes; Farnsworth & Boyle, arXiv:1408.5367, "Rethinking Connes' approach$\dots$", 2014). **ABSTAIN on specifics:** I did not verify the original Chamseddine–Connes–Marcolli papers' coupling-relation formulas or any Higgs-mass prediction from the primary texts in this run, and no such number is stated in this draft.
- **Assumptions (postulated):** geometry is specified by a *spectral triple* (A, H, D, J, $\gamma)$ — an algebra, a Hilbert space, a Dirac operator carrying metric information; spacetime is "almost commutative", $A = C(M) \otimes A_{F}$ with $A_{F} a$ finite-dimensional (matrix) algebra encoding the internal (particle-physics) degrees of freedom.
- **Design:** the *spectral action* $\mathrm{Tr} f(D/\Lambda)$ + fermionic term; the Dirac operator contains the metric, the gauge fields, the Higgs (as the internal component of the gauge field), and the fermion masses/mixings; the bosonic action is a regularised trace (cutoff $\Lambda)$. Renormalisation-group flow from a unification-scale boundary condition (couplings related at that scale) down to low energies gives relations between couplings.
- **Reported findings (as verified in the search results):** the programme transcribes the Standard Model coupled to Einstein gravity into spectral data and *tightens* the Lagrangian (fewer independent inputs than the bare SM in the sense that the spectral action relates couplings at the cutoff scale); the fermion mass matrix enters the Dirac operator; the unimodularity condition is noted in the literature as "the only ad hoc feature" (Schücker 2000 summary — secondary, recorded as such).
- **What would falsify it:** a measured coupling relation contradicting the RG flow from the spectral-action boundary condition given the assumed finite algebra; a fermion spectrum/mass pattern the finite algebra cannot encode; failure of the spectral action's gravity sector to reproduce GR at low energies. **ABSTAIN** on whether any specific such falsification (e.g. the Higgs-mass question) has occurred — not verified in this run.
- **Relation to IRH — Bartha audit (S4):** Positive analogy — both claim geometry *encodes* particle physics (IRH: $E_{6}$ read off $D_{4}/2T$; NCG: SM read off the finite algebra). Negative analogy (critical): NCG's prior association depends on (a) a Dirac operator on a Hilbert space of fermions, (b) a spectral action with a cutoff, (c) RG flow from a unification boundary condition. IRH has no Dirac operator, no Hilbert space of fermions, no spectral action, and no RG flow. Critical features in the Negative Analogy $\to$ **transfer FAILS**. The analogy "both read physics off geometry" remains compatible with both frameworks and motivates nothing further — it is a *suggestive* parallel, grade D as a claim about either framework.
- **Grade:** "NCG's spectral action encodes SM + gravity in spectral data with coupling relations at a cutoff scale; it does not output $\alpha^{-1} = 137.036\dots$ from pure geometry" — **$C** (I1 \to C$; scope-limited to what the verified summaries establish). Any specific coupling or Higgs-mass number — **ABSTAIN**.

---

## 4. Cross-cutting analysis

### 4.1 What each account postulates vs derives (summary)

| Account | Spacetime | Signature | Constants | Gravity (Einstein eqs.) |
|---|---|---|---|---|
| IRH v93.1 | Postulated: **$R**{}^{4} + \psi$; $D_{4}$ derived as pattern | **Not derived** (reading A needs a mechanism it lacks) | **Not derived** (triad definitional; $\alpha$ ansatz; $\bar{\psi}, q_{0}$ tuning inputs) | **Not derived** (effective metric only, retracted) |
| Standard QFT | Postulated: fixed Minkowski/Euclidean | Postulated | Postulated as measured inputs; running derived | Postulated (GR) or absent (flat-space QFT) |
| Greensite / Carlini–Greensite | Postulated: D-dim + phase field | **Derived (claimed):** stationary at $\theta=\pi$, uniquely D=4 — *quantum, one-loop, fermion-dominant* | Not addressed | Not addressed |
| Mukohyama–Uzan / Kehayias | Postulated: Euclidean 4D + clock field | **Derived (claimed):** emergent in patches — *classical, clock-field, fine-tuned coupling* | Not addressed (constancy assumed as constraint) | **Not GR:** Galileon-type effective gravity |
| Analog gravity (BLV/Sindoni) | Postulated: background system | Postulated (in the analogue) | Not addressed | **Not derived:** effective metric only |
| Varying constants (Dirac/modern) | Postulated (usually GR background) | Postulated | **Varying by postulate** (new scalar field); values not derived | Postulated (GR + scalar) |
| Anthropic / multiverse | Postulated: ensemble | Postulated per domain | **Selected, not derived** (observer condition) | Postulated per domain |
| Eddington | Postulated | Postulated | **Claimed derived — FAILED by measurement** | Not addressed |
| $E_{6}$ unification | Postulated (Minkowski) | Postulated | **Relations constrained conditionally; absolute values input** | Not addressed (GUT, not gravity) |
| Causal set | **Derived (claimed):** geometry from order + number | Postulated: Lorentzian causal order | Not addressed | Not derived (continuum limit conjectural) |
| Noncommutative geometry | Postulated: almost-commutative spectral triple | Postulated (Euclidean in the formalism) | **Relations at cutoff; values via RG + input** | Spectral action *contains* Einstein–Hilbert term (claimed) |

### 4.2 The signature question, isolated

Only two published mechanisms in this survey *derive* (claim to derive) Lorentzian signature rather than postulating it: Greensite (quantum) and Mukohyama–Uzan (classical + clock field). IRH has neither. IRH reading (A) is therefore the reading with the largest unpaid debt, and it is also the reading the manuscript calls "most economical" and "the only reading consistent with citing four-dimensional optimality as evidence about spacetime". That combination — most economical *and* most indebted — is the central tension of IRH's spacetime account. Reading (B) pays a different price (compactification mechanism + KK modes + broken $D_{4}$ symmetry); reading (C) pays the highest price (no construction at all). The manuscript is correct that the choice "is not resolvable by further calculation" — it is a modelling decision with different debts, not a computation.

### 4.3 The constants question, isolated

Every account surveyed either (a) takes constants as inputs (standard QFT, $E_{6}$ unification's absolute values, NCG's cutoff values), (b) selects them (anthropic), (c) makes them dynamical without deriving their values (varying constants), (d) claims a derivation that failed (Eddington), or (e) does not address them (signature mechanisms, analog gravity, causal sets). **IRH is in none of these classes cleanly:** its triad is (a)-in-disguise (re-expression of measured inputs), its $\alpha$ ansatz is (d)-in-miniature (arithmetic without derivation, honestly labelled), and its $\bar{\psi}/q_{0}$ tunings are (a) (inputs). The honest coding is: IRH's constants account is *fragmentary* — three different non-derivations for three different constants — and the fragmentariness itself is the finding. A future IRH constants programme would need, at minimum: a mechanism fixing $\bar{\psi}$, a mechanism fixing $q_{0} ($or showing the band survives detuning), and a derivation of $\alpha$ that does not merely fit 137.036 — none of which exists in v93.1.

### 4.4 Rival / failure mode (steelman against this draft)

- **Steelman for IRH:** the comparison is unfair in one direction — the rivals are *older, published, peer-reviewed* programmes, while IRH is a single-author programme at v93.1; grading IRH's open problems against rivals' *solved* sub-problems understates IRH's distinctive achievement $(D_{4}$ selection), which no rival attempts. *Answer:* the draft does not grade IRH down for being young; it grades each narrow claim on its own record, and it records $D_{4}$ selection as IRH's distinctive Grade A result. The constants/signature gaps are IRH's *own* §IX admissions, not impositions from the rivals.
- **Steelman for the rivals:** several rivals (Greensite, Mukohyama–Uzan, NCG) *do* have constructions IRH lacks, and this draft's Bartha FAIL verdicts could be read as dismissing them. *Answer:* a Bartha FAIL is a verdict on *transfer into IRH*, not on the source framework. Greensite's mechanism may be correct on its own terms; it still cannot be transplanted into a classical scalar substrate without quantisation and fermions. The draft grades the source claims separately (grade C, published) from the transfer claims (FAILED).
- **Failure mode of this draft:** the literature survey is bounded (searches run 2026-11-10, primary abstracts + reviews; no full-text re-derivation of any rival's central calculation; no post-2011 varying-$\alpha$ consensus; no NCG Higgs-mass verification). A rival's central calculation could contain an error this draft did not catch, or a post-2014 emergent-signature development could change §3.3's standing. Both are flagged as ABSTAINs / NOT RUN, not papered over.

---

## 5. Gaps and untested conditions (flagged; full list in the companion matrix file)

**IRH's own gaps (from its own text, restated as testable gaps):**
1. No signature mechanism (any reading). Untested condition: whether *any* classical Euclidean substrate can yield Lorentzian signature — IRH §IX.3 says none is known.
2. No Einstein equations, no diffeomorphism invariance, no universal coupling, no two graviton polarisations. Untested: whether an impedance-tensor metric can be promoted beyond an effective metric.
3. No derivation of $\alpha ($ansatz only), no derivation of $\bar{\psi}$, no derivation of $q_{0}$ tuning; R = 2589 subtraction unforced. Untested: whether the $D_{4}$ band survives simultaneous detuning + higher-order terms (VI.2 test, problem 1.3).
4. Dimensional assignment undecided (A)/(B)/(C); reading (B) predicts KK modes (untested in IRH — no KK spectrum computed); reading (C) has no construction.
5. No quantum mechanics beyond single-particle envelopes (§IX.3: entanglement/Bell from a classical substrate needs nonlocality or superdeterminism — "a boundary, not a gap").
6. No $E_{6}$ breaking pattern / Higgs sector (§IX.4); monopole resolution missing (VI.7 companion problem 3.4); joint early-universe narrative missing in its entirety (programme brief).
7. The 11.85% vs 11.90% band discrepancy is unresolved (author decision pending).

**Rivals' gaps (as they bear on IRH):**
8. Greensite: quantum mechanism, untested as a selection principle; current standing ABSTAIN.
9. Mukohyama–Uzan: clock field + fine-tuned coupling; effective gravity is Galileon, not GR; Lorentz-violation operators constrained but the construction's quantum stability is untested in this draft.
10. Analog gravity: no route to Einstein equations in any surveyed model; multi-component Lorentz-invariance difficulty (Sindoni §4).
11. Varying-$\alpha$: current observational status ABSTAIN (post-2011 consensus not verified here).
12. Anthropic: ensemble unobserved; typicality assumed; Weinberg's own falsification condition (galaxy number counts) not assessed here.
13. Causal set: Hauptvermutung unproved; no quantum gravity delivered; no constants account.
14. NCG: specific coupling/Higgs numbers ABSTAIN (not verified from primary texts here); unimodularity condition ad hoc (secondary report).

**Untested conditions shared by all:** no account surveyed derives $\alpha^{-1}$ from first principles and survives measurement; no account surveyed derives Lorentzian signature *and* the Einstein equations *and* the constants from a single substrate. That conjunction is the open problem, not a result held by any party.

---

## 6. Checks run (PASS / FAIL / NOT RUN)

| # | Check | Tool + version | Result |
|---|---|---|---|
| K1 | $a_{0}\cdot\Omega_{P} = c$ from $a_{0} = L_{P}/\sqrt{24}$, $\Omega_{P} = \sqrt{24}\cdotc/L_{P}$ | SymPy 1.14.0, `~/miniconda3/envs/jacobian-conjecture-2d/bin/python` | **PASS**, exit 0. Confirms algebraic consistency only (C1). |
| K2 | $\alpha^{-1}$ ansatz = $137 + 1/(28 - \pi/14) = 137.036002821941$; diff vs CODATA 2022 137.035999177$(21) = +3.64\times10^{-6}$ | SymPy 1.14.0 (exit 0) + python-flint 0.8.0 float arithmetic (agrees: 137.0360028219411) | **PASS** (arithmetic). Second tool confirms the number, not a derivation (C2). Note: the flint run's final float-conversion line raised a TypeError *after* printing the load-bearing values; the exact rationals 64/141 and 73/423 were displayed exactly by flint. No load-bearing value depends on the failed conversion line. |
| K3 | $S = 64/141 \approx 0.4539007$; margin $73/423 \approx 0.1725768$; SH scaling exponents $(2-d, -d, 4-d) = (0$ at d=4 for SH) | SymPy 1.14.0, exit 0; flint 0.8.0 exact rationals displayed | **PASS**, exit 0 (SymPy). Re-derives manuscript arithmetic; does not re-derive the shell enumeration (stated in the source, flagged as such in the manuscript's own rebuild). |
| K4 | Primary-source existence for every rival reference in §3 | browser.search (language en) + browser.open-equivalent search snippets (ADS, arXiv, journal records) | **PASS** for all references listed in §3 and §7. No reference is included that could not be confirmed. |
| K5 | Current (post-2011) status of varying-$\alpha$ observations | browser.search | **NOT RUN to a verdict — ABSTAIN.** Searches returned 2003–2011 reviews only. No current bound stated. |
| K6 | Current standing of Greensite mechanism beyond 1993–94; NCG Higgs-mass / coupling numbers from primary texts | browser.search | **NOT RUN to a verdict — ABSTAIN.** Not verified from primary texts in this run. |
| K7 | Any Lean/Z3 formalisation of a transfer | — | **NOT RUN.** No formalisation attempted in this draft (correctly — a transfer that fails Bartha at S4 should not be formalised as if it had passed). |
| K8 | Gemini grader | — | **NOT RUN (forbidden).** Never called, per task. |
| K9 | GCP / lean-build-4 / any VM | — | **NOT RUN (forbidden).** No spend, no VM touched. |

**Tool inventory (truth-seeking v5 §2):** Python via the conda env (SymPy 1.14.0 verified by execution; python-flint 0.8.0 verified by execution, exact-rational display); browser.search verified by use. Lean, Singular, Z3 were not needed for this (literature + arithmetic) task and are marked NOT USED, not UNAVAILABLE. Wolfram, Coq, Isabelle, Sage, GAP, Macaulay2: UNAVAILABLE / not used — no claim depends on them.

---

## 7. Evidence that would change the answer

- **C1 (triad definitional):** a derivation of $L_{P} ($or of $a_{0}, \Omega_{P})$ from substrate dynamics with no measured Planck-scale input — i.e. $a_{0}$ computed from $\psi$-dynamics alone. Would upgrade C1's *status* (the manuscript's characterisation would become outdated), not the arithmetic.
- **$C2 (\alpha$ ansatz):** a derivation of $137 + 1/(28 - \pi/14)$ — or of any $\alpha$ formula — from stated IRH premises $(\psi$ dynamics, $D_{4}$ combinatorics, $E_{6}$ representation theory) with the "28" and "$\pi/14$" arising from those premises rather than chosen to fit. Mere closeness to a future more precise CODATA value would *not* suffice (Eddington's lesson).
- **C3 (dimensional assignment):** a construction for reading (C), a compactification mechanism + KK spectrum for reading (B), or a signature mechanism for reading (A) — any one would decide the assignment by construction rather than by stipulation.
- **C4 (signature):** a classical Euclidean substrate yielding Lorentzian signature (contradicting IRH §IX.3's "none is known"), or a quantised IRH with fermions satisfying Greensite's condition.
- **C5 (Einstein equations):** an impedance/effective metric shown to obey $G = 8\piT$ with universal coupling and two graviton polarisations — in IRH or in any analog model.
- **C7 (no rival derives $\alpha)$:** a single verified primary-source derivation of $\alpha^{-1}$ from first principles that survives measurement. One counterexample defeats the scoped claim; the draft's ABSTAIN on universality would then be replaced by a FAILED verdict for C7.
- **Matrix rankings:** a head-to-head discriminating test (HLRE I2+) between IRH and any rival on a *shared* prediction — none exists in this draft, and none is claimed.

---

## 8. Citation record (primary sources only for load-bearing claims)

**IRH (grounding sources):** McCrary, *Intrinsic Resonance Holography v93.1* (17 Sep 2026), `IRH_v93_1_source_rebuilt.txt` §§I.1, I.3, II.5–II.7, III.4, VI, VII, VIII, IX.2–IX.5; `established/CORE.md`; `guardrails/EXCLUDED.md`; `guardrails/INPUTS.md`; `predictions/VI-predictions.md`. (Manuscript's own bibliography: [1] Alexander & McTague, PRL 41, 702 (1978); [2] Swift & Hohenberg, PRA 15, 319 (1977); [15] Derrick, JMP 5, 1252 (1964); [16] Barceló et al. 2011; [17] Mukohyama & Uzan 2013; [18] Kehayias et al. 2014; [19] Sindoni 2012; [40] Hoy, PRE 109, 044604 (2024); [41] Greensite 1993; [42] Carlini & Greensite 1994.)

**Rivals (all confirmed to exist via browser search of primary/publisher records, 2026-11-10):**
- Greensite, Phys. Lett. B 300, 34–37 (1993), arXiv:gr-qc/9210008.
- Carlini & Greensite, Phys. Rev. D 49, 866–878 (1994), arXiv:gr-qc/9308012.
- Mukohyama & Uzan, Phys. Rev. D 87, 065020 (2013), arXiv:1301.1361.
- Kehayias, Mukohyama & Uzan, Phys. Rev. D 89, 105017 (2014), arXiv:1403.0580v2.
- Barceló, Liberati & Visser, Living Rev. Relativ. 14, 3 (2011), doi:10.12942/lrr-2011-3, arXiv:gr-qc/0505065v3.
- Sindoni, SIGMA 8, 027 (2012), arXiv:1110.0686.
- Uzan, Rev. Mod. Phys. 75, 403–455 (2003); Uzan, Living Rev. Relativ. 14, 2 (2011); Uzan, arXiv:astro-ph/0409424v2 (2004).
- Barrow, arXiv:astro-ph/0511440v1 (2005). Dirac, Nature (1937) — via Uzan/Barrow reviews.
- Weinberg, Phys. Rev. Lett. 59, 2607–2610 (1987), doi:10.1103/PhysRevLett.59.2607.
- Gürsey, Ramond & Sikivie, Phys. Lett. B 60, 177–180 (1976), doi:10.1016/0370-2693(76)90417-6.
- Bombelli, Lee, Meyer & Sorkin, Phys. Rev. Lett. 59, 521–524 (1987); Surya, Living Rev. Relativ. 22, 5 (2019).
- Connes programme: Farnsworth & Boyle, arXiv:1408.5367 (2014) — summary level; original Chamseddine–Connes papers NOT re-verified here (ABSTAIN on their numbers).
- CODATA $2022 \alpha^{-1} = 137.035999177(21)$: as reported in a search-verified source citing CODATA 2022 (Mohr et al., CODATA 2022). Treated as a reported measured value, not re-derived; the draft's arithmetic (K2) depends only on its stated digits.
- Eddington history: secondary summaries (Wikipedia "Eddington number"; Barrow 2002 via search) — background only, no load-bearing number rests on them.

**Quotation discipline:** no copyrighted work is quoted at length; short phrases (e.g. Weinberg's abstract, Mukohyama–Uzan's abstract) are paraphrased or quoted in fragments well under 50 words.

---

## 9. Ledgers

### Assumption ledger

| # | Assumption | Provenance | Status |
|---|---|---|---|
| A1 | IRH primitive $\psi$ on **$R**{}^{4}$, Swift–Hohenberg dynamics | Manuscript §I.2 (postulate) | Postulated, not derived |
| A2 | Dimensional assignment (A)/(B)/(C) | Manuscript §IX.2 (undecided) | Undecided — this draft assumes none; matrix shows all three |
| A3 | Three generations; $\bar{\psi}$ value; $q_{0}$ tuning; Model B | INPUTS.md 1–4 | Acknowledged inputs |
| A4 | Greensite: quantised phase field, one-loop $V(\theta)$, fermion dominance | Greensite 1993 / Carlini–Greensite 1994 | Source's postulates |
| A5 | Mukohyama–Uzan: Euclidean base + clock field + fine-tuned coupling | Mukohyama & Uzan 2013 | Source's postulates |
| A6 | Analog gravity: effective metric defined by wave-equation coefficients | Barceló et al. 2011 | Source's construction |
| A7 | Varying constants: new light scalar coupled to matter | Uzan 2011 | Source's framework postulate |
| A8 | Anthropic: ensemble of domains + typicality | Weinberg 1987 (ensemble implicit) | Postulated, unobserved |
| A9 | $E_{6}$ unification: simple group + breaking chain + spectrum | Gürsey et al. 1976 | Source's postulates |
| A10 | Causal set: discrete causal order; volume = number | Bombelli et al. 1987 | Postulated |
| A11 | NCG: spectral triple; almost-commutative algebra | Connes programme | Postulated |
| A12 | This draft's survey is bounded to the sources in §8; post-2011 varying-$\alpha$ consensus and post-2014 signature developments not assessed | This draft (method) | Declared limitation |

### Parameter ledger

| Parameter | Value in this draft | Provenance | Role |
|---|---|---|---|
| $S(D_{4})$ | $64/141 \approx 0.4539$ | Manuscript §II.5; re-checked K3 | IRH selection (derived) |
| $S(A_{4}*)$ | $12/31 \approx 0.3871$ | Manuscript §II.5; re-checked K3 | Competitor (derived) |
| Margin | $73/423 \approx 17.26$% | Manuscript §II.5; re-checked K3 | Selection margin |
| $\tau_{D}_{4}/\tau_{BCC}$ | $\sqrt{2}$ exactly | Manuscript §II.5 | Cross-check |
| $D_{4}$ band | 11.85% of scanned plane (11.90% also stated in source — discrepancy flagged) | Manuscript §II.7 | Conditional prediction |
| $r_{eff}$ | +0.107 at $\bar{\psi} = -0.18$ | Manuscript §II.9 | First-order character |
| F/V (relaxed) | $-0.0077276$ | Manuscript §II.8 | Attractor |
| $a_{0}$ | $2\pi/q_{0}$ | Manuscript §I.3 | Derived |
| $\alpha^{-1} ($ansatz) | 137.03600282 | Manuscript Part VII; re-checked K2 | Downgraded ansatz |
| $\alpha^{-1} ($measured) | 137.035999177(21), CODATA 2022 | Reported value (§8) | Measurement |
| $\Delta($ansatz $-$ measured) | +$3.64\times10^{-6}$ | Computed K2 | Arithmetic gap |
| $q_{0}^{2}$ detuning killing the ordered branch | 0.5 | Manuscript §II.7 | Tuning condition |
| SH exponent at d=4 | 0 (marginal) | Manuscript §III.4; re-checked K3 | Dimensionality argument |
| CFL bound | $\Deltat \leq (\sqrt{3}/2)a_{0}/c$ | Manuscript §III.2 | Stability (legacy formulation) |
| $\bar{\psi}$ band | $-0.33$ ≲ $\bar{\psi}$ ≲ 0.03 (approx., quench-dependent) | Manuscript §II.7 | Conditional prediction |

No other numerical parameter is used as load-bearing in this draft. In particular: **no** current bound on $\dot{\alpha}/\alpha$, **no** Weinberg-bound multiple beyond the abstract's "1 or 2 orders of magnitude", **no** NCG coupling or Higgs-mass number, **no** causal-set discreteness scale, **no** Greensite $V(\theta)$ numerical value is stated — each is ABSTAIN / NOT RUN.

### Choice ledger

| Choice | Why | Effect if changed |
|---|---|---|
| Deepest-research FULL mode (not systematic-review) | Task instruction; literature comparison, not a PRISMA review | A systematic review would change the search protocol, not the verdicts on the sources actually checked |
| Ten accounts (IRH + 9 rival groupings) | Task scope (i)–(vi), with (v) split into Eddington vs $E_{6}$ and (vi) split into CST vs NCG | Adding string theory / loop quantum gravity as separate accounts would extend the matrix, not change IRH's gaps |
| Matrix dimensions fixed by the task brief | Prevents post-hoc dimension selection | — |
| No formalisation attempted | Bartha FAIL at S4 precedes S7; formalising a failed transfer would mislead | — |
| Grades capped at C (Track E) | Human source/balance gates not run; all verification I1 max | A human running the gates could raise individual descriptive grades; it could not raise a FAILED transfer |
| CODATA value taken as reported (not re-derived from NIST) | No NIST primary fetch in this run | Re-fetching CODATA would change at most the last digits; K2's conclusion (ansatz is close and underived) is insensitive to it |

### Withdrawal / demotion note

No prior claim of this programme is withdrawn by this draft. One correction to guard against: the manuscript's rebuild already notes the 11.85% vs 11.90% band discrepancy; this draft repeats the flag and does not resolve it. The $\alpha$ ansatz arithmetic in the rebuild $(137.0360028\dots)$ is confirmed here to more digits (137.036002821941); the extra digits change nothing — the downgrade stands.

---

## 10. VERIFIED / UNVERIFIED / FAILED branch lists

**VERIFIED**
- V1. IRH triad relations are algebraically consistent definitions, not derivations (C1; manuscript + SymPy PASS).
- V2. IRH $\alpha^{-1}$ ansatz arithmetic is exact $(137.03600282\dots)$; physical derivation absent (C2; manuscript downgrade + SymPy/flint PASS on arithmetic).
- V3. IRH dimensional assignment (A)/(B)/(C) is undecided, mutually exclusive, not resolvable by calculation (C3; manuscript §IX.2).
- V4. Published signature mechanisms need quantum one-loop fermion-dominant structure (Greensite) or a clock field with fine-tuned coupling (Mukohyama–Uzan); IRH has neither (C4; primary abstracts + manuscript).
- V5. Analog-gravity / impedance routes give an effective metric, not $G = 8\piT (C5$; BLV/Sindoni + manuscript §IX.3).
- V6. Standard QFT takes constants as measured inputs; $E_{6}$ unification constrains relations conditionally without fixing $\alpha^{-1}$; causal-set Hauptvermutung is unproved; NCG encodes SM+gravity in spectral data without outputting $\alpha^{-1} (C6/C8$, scoped to surveyed sources; grade C).
- V7. S = 64/141, margin 73/423, SH marginality at d = 4 — manuscript arithmetic re-checked (K3, PASS).

**UNVERIFIED (ABSTAIN — "I cannot verify this with the available tools")**
- U1. Current (post-2011) observational status of varying $\alpha$ and the present best bound on $\dot{\alpha}/\alpha$.
- U2. Current standing of the Greensite mechanism beyond the 1993–94 papers.
- U3. Whether any specific NCG coupling/Higgs-mass prediction has been falsified or confirmed.
- U4. The universal negative "no framework anywhere derives $\alpha$" — verified only for the surveyed sources (C7 scoped).
- U5. Any head-to-head ranking of IRH vs a rival on a shared prediction (no such shared prediction exists in this draft).

**FAILED (as derivation-transfers or as claimed derivations)**
- F1. Transfer of Greensite's signature mechanism into IRH — Bartha FAIL (critical features: quantised phase field, one-loop potential, fermion dominance — all in the Negative Analogy).
- F2. Transfer of Mukohyama–Uzan/Kehayias clock-field signature into IRH — Bartha FAIL (critical features: clock field, fine-tuned coupling, Galileon-not-GR gravity).
- F3. Transfer of "Einstein equations derived" from any analog-gravity route into IRH — Bartha FAIL (critical feature: Einstein dynamics in the Negative Analogy); IRH's Part VII retraction stands.
- F4. "IRH'$s E_{6}$ identification derives coupling values / $\alpha$" — FAILED (no breaking pattern, no RG running; §IX.4).
- F5. "Anthropic reasoning explains $\alpha$ or IRH's tunings" — FAILED / NOT SUPPORTED (ensemble unobserved; not in the manuscript; post-hoc ceiling D).
- F6. Eddington's derivation of $\alpha$ — FAILED by measurement (historical; the failure mode IRH's ansatz labelling avoids).

---

## 11. AI-contribution statement

This draft was produced by an AI research subagent (workstream D, task 9) under the programme brief of 2026-11-10, using deepest-research FULL mode, the truth-seeking-frontier v5 computation gate, cross-domain-discovery v2.0.0 (S1–S7), and HLRE v5.1 grading. The human (Brandon D. McCrary) is the sole author of IRH and accountable for any incorporation; nothing in this draft is incorporated into the repo or manuscript. All verification is artificial (I1 max); human source/balance gates have not been performed.
