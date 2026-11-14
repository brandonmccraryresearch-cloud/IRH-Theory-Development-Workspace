# Task 8 — Compare quantum gravity frameworks (including IRH) — FINAL

**Workstream D, task 8 — Co-scientist task programme, 2026-11-10.**
**Mode: deepest-research FULL mode** (stated plainly per the standing delegation).
Systematic-review mode is NOT chosen and was NOT used. No PRISMA protocol, no
meta-analysis, no screening of a pre-registered corpus: this is a comparative
literature survey with per-claim primary-source verification, not a systematic
review.

**Status of this document:** FINAL (assembled by the workstream-D parent
agent from the child draft `task8_qg_frameworks_DRAFT.md`, with the
corrections listed in the Assembly notes below). Nothing in it is
incorporated into any repo or manuscript. No commits, no filing, no
manuscript edits were made. The Gemini grader was NOT called. No GCP
spend. No VM was touched.

## Assembly notes (parent agent, 2026-11-10)

Spot-checks performed in assembly; corrections applied to the child draft:

1. **Wrong arXiv ID corrected (K8, §5.5, §12).** The draft cited
   "arXiv:1703.07556" as a causal-set survey. That ID is Dowker &
   Zalel, "Evolution of Universes in Causal Set Cosmology" (2017) —
   not a survey. The prediction-in-advance assessment is now cited to
   Surya, "The causal set approach to quantum gravity", Living Rev.
   Relativity 22, 5 (2019), arXiv:1903.11544 — verified by direct
   read of the ar5iv full text in assembly ("the most striking is the
   1987 prediction of Sorkin for the value of the cosmological constant
   $\Lambda ($Sorkin 1991; Sorkin 1997)").
2. **"Only successful prediction" superlative DROPPED.** The draft
   attributed that superlative to a review via the wrong ID; the exact
   phrase was not found in Surya's Living Review (searched in
   assembly). The report now states only what is verified: Sorkin's
   1997 prediction predates the 1998 discovery, and Surya's review
   calls it "the most striking" causal-set phenomenology. The grade
   (C) and the historical fact are unchanged.
3. **CDT spectral-dimension numbers VERIFIED in assembly; ABSTAIN
   withdrawn.** The draft abstained on $4.02 \pm 0.1 / 1.80 \pm 0.25$ as
   secondary-only. Direct read of Giasemidis–Wheater–Zohren,
   Phys. Rev. D 86, 081503 (2012), eq. (7) in assembly gives
   $D_{s}(\sigma) = 4.02 - 119/(54+\sigma)$ with $1.80 \pm 0.25$ at $\sigma\to0$ and $4.02 \pm 0.1$
   at $\sigma\to\infty$, citing Ambjørn et al. 2005. The numbers are now stated
   as verified primary-source values (see §5.4, §9, §13, matrix).
   This is consistent with task 12's independent evaluation of the
   same fit (1.82 at $\sigma\to0$, within $1.80 \pm 0.25)$.
4. **Aharony et al. year corrected:** "Phys. Rep. 1999" $\to$
   "Phys. Rep. 323 (2000) 183–386".
5. **§3 "Dynamics, Grade A/B (carried)" tightened** to the
   manuscript's own grading (Swift–Hohenberg mathematics Grade A;
   physical/substrate reading $\leq C/D)$.
6. **CDT 17–28 Planck lengths verified in assembly:** arXiv:0712.2485
   abstract ("the linear size of the quantum universes under study is
   in between 17 and 28 Planck lengths") — the draft's figure is
   correct as cited.

---

## CLAIM and STATUS (together, at the top)

**CLAIM.** Of the frameworks competing to explain quantum gravity / the
emergence of spacetime — loop quantum gravity / spin foams, string theory
(and AdS/CFT), asymptotic safety, causal dynamical triangulations, causal
set theory, group field theory, emergent/analogue gravity, and Intrinsic
Resonance Holography (IRH v93.1) — **no framework has a laboratory-confirmed
Planck-scale prediction, and no framework has derived the Einstein field
equations together with Lorentzian signature, diffeomorphism invariance, and
the Standard Model gauge structure from its own postulates without
additional input.** Each framework derives or postulates a different subset
of the target; each fails, is silent, or is untested on at least one of the
others. IRH is the only framework in the set whose *geometric core*
$(D_{4}$ selection, 2T–McKay–$E_{6})$ is machine-checked, and also the only one whose
own manuscript explicitly retracts its earlier Einstein-equation and
signature claims; its physical/substrate reading is graded $\leq C/D$ and it
cannot answer the signature, field-equation, or multi-particle-quantum
questions without external structure (Part IX).

**STATUS.** Comparative survey COMPLETE as a draft. Literature claims are
graded per narrow claim below (Track E; all verification in this draft is
artificial, I1, so grades cap at **C** for new comparative claims — HLRE
§6.5 fallback, human source/balance gates not performed). IRH-side grades
are *carried* from the repo record (`established/CORE.md`,
`verification/`), not re-derived here; they are cited, not re-verified.
Three quantitative items are **ABSTAIN** (see §9). The cross-domain
protocol (S1–S7) was run; the Bartha gate (S4) **FAILS** the transfer
"analogue/elastic substrate $\Rightarrow$ Einstein equations" — for IRH and for
analogue gravity generally — which is exactly the retraction IRH v93.1
already records.

**Headline findings (one paragraph each in §8; full detail in §5–§7):**

1. **Only one prediction-in-advance in the whole set belongs to a rival:**
   causal-set theory's fluctuating $\Lambda \sim 1/\sqrt{V} \sim 10^{-120} ($Sorkin 1997, before
   the 1998 acceleration discovery). It is heuristic, order-of-magnitude
   only, and its dynamics (a full quantum theory) still does not exist.
2. **The strongest *derived* emergence result is CDT's:** a macroscopic
   4D de Sitter-like universe and a spectral dimension running from 4 at
   large scales to ~2 at short distances, from Monte Carlo simulation
   (Ambjørn–Jurkiewicz–Loll 2004, 2005). It is numerical evidence in one
   phase of a lattice model, not a derivation of GR.
3. **LQG's sharpest derived result is kinematic, not dynamical:** discrete
   area/volume spectra (Rovelli–Smolin 1995). Its dynamics (EPRL spin
   foam, 2008) has the right large-spin (Regge) asymptotics; the continuum
   / classical limit remains the field's own open problem.
4. **String theory / AdS-CFT is the only framework with a precise
   non-perturbative duality conjecture** (Maldacena 1997), but the duality
   is conjectured, not proved; it is formulated in AdS (negative $\Lambda)$, not
   in the observed de Sitter-like universe; and it postulates strings,
   supersymmetry, and extra dimensions rather than deriving them.
5. **Asymptotic safety is the most conservative programme** (metric QFT +
   a non-Gaussian UV fixed point, Weinberg 1979; Reuter 1998) — and the
   one whose central object, the Reuter fixed point, is supported only by
   truncation evidence, with truncation artefacts the acknowledged risk.
6. **IRH's honest position is the narrowest and the most checked at the
   geometric level:** $D_{4}$ selection and $E_{6}$ are Grade A (machine-checked);
   the substrate reading, the signature, the field equations, the $E_{6}$
   breaking pattern, and the nucleation event are open or retracted
   (Part IX). IRH does not compete with the others on deriving GR — it
   currently *cannot*, by its own record.

---

## 1. Claim register (S1 — registered before analysis)

Registered before any literature search or comparison. Anything selected
after inspecting a target would be POST-HOC and grade D; none of the
claims below was revised after inspection (no revision cycle was triggered).

| ID | Claim (narrow) | Domain | What would count as evidence |
|----|----------------|--------|------------------------------|
| C1 | LQG derives discrete spectra for area and volume operators | LQG kinematics | Primary paper stating discreteness from the spin-network Hilbert space |
| C2 | The EPRL spin-foam vertex gives LQG dynamics with Regge asymptotics at large spin | LQG dynamics | Primary EPRL papers + asymptotics theorem |
| C3 | String theory postulates strings / SUSY / extra dimensions; AdS/CFT is a conjectured duality, not a proved equivalence | String / AdS-CFT | Maldacena 1997 text (conjecture language) + review |
| C4 | Asymptotic safety rests on a non-Gaussian UV fixed point, evidenced only within truncations | Asymptotic safety | Weinberg 1979 proposal + Reuter 1998 FRG construction + truncation caveat in the literature |
| C5 | CDT simulations produce an emergent macroscopic 4D de Sitter-like universe; spectral dimension runs $4 \to ~2$ | CDT | Ambjørn et al. 2004 PRL + 2005 spectral-dimension paper |
| C6 | Causal sets: order + number = geometry; Sorkin predicted $\Lambda \sim 1/\sqrt{V} \sim 10^{-120}$ in advance (1997) | Causal sets | Bombelli et al. 1987 + Sorkin 1997 + later everpresent-$\Lambda$ tests |
| C7 | GFT condensate states yield a modified Friedmann equation; whether the condensate phase is continuum GR geometry is NOT established | GFT cosmology | Gielen–Oriti–Sindoni 2013 + 2023 mean-field result + stated open question |
| C8 | Analogue gravity reproduces gravitational *kinematics* (effective metric, horizons, Hawking analogue) but NOT Einstein *dynamics* | Analogue / emergent | Barceló–Liberati–Visser 2011 + Sindoni 2012 |
| C9 | Jacobson derives the Einstein equation from horizon thermodynamics *given* $S \propto A$, $\deltaQ = T$ dS, local equilibrium | Thermodynamic gravity | Jacobson 1995 PRL, abstract + assumptions |
| C10 | IRH geometric core $(D_{4}$ selection S = 64/141; $E_{6}$ via 2T/McKay) is Grade A; IRH physical/substrate reading is $\leq C/D$ | IRH | Repo record CORE.md + verification/ (carried, not re-derived) |
| C11 | IRH cannot answer Lorentzian signature, Einstein equations, or QM beyond single-particle envelopes without external structure | IRH open problems | Manuscript Part IX (§IX.2–IX.3) |
| C12 | No framework in the set has a laboratory-confirmed Planck-scale prediction | Whole set | Absence across the surveyed primary literature (negative claim, grade C max) |

**BPMF facets (S1, cross-domain-discovery v2.0.0).** For each framework the
matrix document (`task8_qg_matrix.md`) records Background / Purpose /
Mechanism / Findings. Facets are background, purpose, mechanism, findings —
there is no "evaluation" facet and the "PME" acronym is not used.

**Scope boundary.** Frameworks compared are those named in the task plus
IRH. Excluded from scope: semi-classical gravity as a standalone programme,
non-commutative geometry, twistor theory, and quantum graphity (mentioned
only where Sindoni 2012 surveys them). The comparison dimensions are fixed:
ontology, dynamics, background independence, Lorentz-signature origin,
matter/gauge emergence, falsifiable predictions, status.

---

## 2. Method (deepest-research FULL mode)

1. **Ground the IRH side first** in the manuscript
   (`IRH_v93_1_source_rebuilt.txt`, 34 pp.), `established/CORE.md`,
   `guardrails/EXCLUDED.md`, `guardrails/INPUTS.md`,
   `predictions/VI-predictions.md`, and `OPEN_PROBLEMS.md` (Part IX).
   No IRH claim is stated from memory.
2. **Literature verification** by `browser.search` (with language code)
   and `browser.open` against primary sources: arXiv abstract pages and
   journal records. A reference enters the citation record only if its
   existence was confirmed in this session. Quotation is kept under 50
   words per copyrighted work.
3. **Computation gate (truth-seeking-frontier v5).** The only load-bearing
   numbers recomputed locally are IRH's own selection arithmetic (see
   §3, checks). Rival-framework numbers are *reported* numbers with their
   primary source named, never recomputed or invented. Where a number
   could only be sourced secondarily, it is labelled SECONDARY-ONLY or
   ABSTAIN, never silently promoted.
4. **Cross-domain protocol (S1–S7).** S1 register above; S2 retrieval is
   the framework set named in the task (not a network-mined set — no
   AGATHA/KGE run was performed; that stage is NOT RUN for this task and
   the grade cap reflects it); S3 alignment is the shared comparison
   dimensions in the matrix; S4 Bartha + transportability audit in §6;
   S5 blending is NOT attempted (no hybrid model is proposed); S6 no
   tournament (single author, no multi-agent Elo); S7 no Lean/Z3
   formalization was attempted in this task — the DVP notational-collapse
   guard therefore has nothing to check here, and no formal claim is made.
   **Grade caps applied:** Track E C / Track F F3 until a human runs the
   source/balance gates (HLRE §6.5 fallback; cross-domain-discovery
   v2.0.0 provenance note).
5. **HLRE v5.1 grading.** Per narrow claim, worst-of computation shown
   (independence bound; caps; postulation ceiling; support in the record).
   Independence: all new comparative claims are **I1** (artificial
   verification sharing this pipeline's sources) — hence the C cap. IRH
   carried grades keep their repo independence (stated per claim).

---

## 3. IRH ground (what is being compared against)

Grounded in the files listed in §2.1. Grades are carried from the repo
record; this draft does not re-run `verification/`.

- **Geometric core, Grade A.** $D_{4}$ selected with $S = \tau^{2}/q_{4} = 64/141 \approx 0.454$,
  17.3% margin over $A_{4}$*; $D_{4}$ isotropic through 4th order (exact, spherical
  5-design); 24-cell vertices = binary tetrahedral group $2T \subset$ SU(2);
  $2T/Q_{8} \cong \mathbb{Z}_{3}$; McKay $2T \leftrightarrow$ affine $E_{6}$; gauge algebra $E_{6} ($§IV.4). Lean 4
  formalization, 8 modules, `lake build` exit 0; `verify_claims.py`
  51/51 (per CORE.md).
- **Arithmetic check run in this task (computation gate):**
  `~/miniconda3/envs/jacobian-conjecture-2d/bin/python` (Python 3.11.16,
  SymPy 1.14.0), exit 0: $64/141 = 0.4539007092\dots \approx 0.454$ ✓; implied $A_{4}$*
  value from the stated 17.3% margin is $0.4539/1.173 \approx 0.387 ($consistency
  arithmetic only — the 17.3% figure itself is carried from CORE.md, not
  independently recomputed). Second independent tool: `fractions.Fraction`
  exact check $64/141 \times 141 = 64$ ✓ (same interpreter, stdlib — a weak
  second route; recorded honestly as such).
- **Dynamics mathematics, Grade A (carried per the manuscript's grading:
  the $D_{4}$/triality/2T–McKay–$E_{6}$/Swift–Hohenberg mathematics is Grade A; the
  physical/substrate reading is $\leq C/D).** a_{0} = 2\pi/q_{0}$ derived; Model B conserved
  dynamics required $(\bar{\psi}$ preserved to $8.3\times10^{-17})$; CFL bound
  $\Deltat \leq (\sqrt{3}/2)a_{0}/c$; corrected envelope equation, <1% for $a_{0}$|k| ≲ 0.3;
  d = 4 marginality of the Swift–Hohenberg term.
- **Inputs (must be stated wherever used):** three generations (input, not
  derived); the value of $\bar{\psi} ($initial datum, no mechanism); tuning of $q_{0}$
  onto the $D_{4}$ shell (the 11.85% band figure is conditional on it — cite
  the qualification every time); conserved substrate dynamics; the
  dimensional assignment (A)/(B)/(C) undecided.
- **Open / retracted (Part IX, verbatim classification):**
  - IX.2: dimensional assignment (A) Euclidean base + dynamical signature /
    (B) four spatial dimensions + compactification / (C) auxiliary base —
    mutually exclusive, undecided, "not resolvable by further calculation".
  - IX.3: Lorentzian signature requires external structure (published
    mechanisms need a one-loop potential with more fermionic than bosonic
    DOF; "No purely classical Euclidean substrate is known to yield
    Lorentzian signature"); Einstein equations NOT derived (effective
    metric obeys the substrate's own EOM, not $G\mu\nu = 8\piT\mu\nu$ — "a general
    limitation of analog models [19]"); QM beyond single-particle
    envelopes is "a boundary, not a gap" (entanglement/Bell needs
    nonlocality or superdeterminism); monopole resolution open.
  - IX.$4: E_{6}$ breaking pattern and Higgs sector not derived at all; Higgs
    VEV, $A_{3}$, CKM — clean restart, nothing carried forward.
  - IX.5: what fixes $\bar{\psi}$? what supplies the nucleation event? (sharpest
    open questions; joint early-universe narrative missing in its entirety).
- **Falsifiable predictions (Part VI, carried):** VI.1 triad phase
  locking (measured 0.26 of max 1 — "real but incomplete locking");
  VI.$2 \bar{\psi}$-band (conditional on $q_{0}$ tuning); VI.3 envelope validity
  boundary; VI.4 CFL stability bound; VI.5 absence of quartic anisotropy;
  VI.6 defect spectrum (no line defects); VI.7 monopoles predicted.
- **EXCLUDED — never revived in this draft:** so(8) gauge algebra, SM in
  so(8), Pati–Salam from so(8), Kerr solitons, skyrmions/hopfions from
  one scalar, three generations derived, monopole absence, universal $D_{4}$
  optimality, $\xi_{2} = -1/384$, v92 time steps, v92 Higgs VEV/$A_{3}$/CKM numbers.
  None appears below as a live claim.

---

## 4. Checks run (PASS / FAIL / NOT RUN)

| # | Check | Tool / source | Verdict |
|---|-------|---------------|---------|
| K1 | IRH $S = 64/141 \approx 0.454$ arithmetic | conda python 3.11.16, SymPy 1.14.0, exit 0; Fraction cross-check | PASS |
| K2 | Rovelli–Smolin 1995 discreteness paper exists, Nucl. Phys. B 442 (1995) 593–622, erratum ibid. 456 (1995) 753 | browser.search, arXiv/lit. record | PASS |
| K3 | Maldacena 1997, hep-th/9711200 v1–v3, Adv. Theor. Math. Phys. 2 (1998) 231–252; conjecture language in abstract | browser.search + arXiv record | PASS |
| K4 | Weinberg 1979 asymptotic-safety proposal; Reuter 1998 FRG construction | Scholarpedia/Lauscher–Reuter hep-th/0110021 record | PASS |
| K5 | Ambjørn–Jurkiewicz–Loll 2004 PRL 93, 131301 (emergent 4D world) | browser.search, PRL record | PASS |
| K6 | Ambjørn et al. 2005 spectral dimension, hep-th/0505113 v2; abstract: 4D large scales, ~2D short distances | browser.open arXiv abs page, crawled 2026-11-10; precise values verified in assembly via Giasemidis–Wheater–Zohren 2012, eq. (7) | PASS (qualitative + quantitative: $4.02 \pm 0.1$ large scales, $1.80 \pm 0.25$ short distances) |
| K7 | Bombelli–Lee–Meyer–Sorkin 1987, PRL 59, 521–524 | browser.search, PRL/OSTI record | PASS |
| K8 | Sorkin $1997 \Lambda \sim 1/\sqrt{V} \sim \pm10^{-120}$ prediction-in-advance | Surya, Living Rev. Relativity 22, 5 (2019), arXiv:1903.11544 (full text read in assembly) + Das–Nasiri–Yazdi, arXiv:2307.13743 (everpresent-$\Lambda$ tests) | PASS (as reported in the field's own reviews) |
| K9 | Gielen–Oriti–Sindoni 2013, PRL 111, 031301 (GFT condensate cosmology, modified Friedmann) | browser.search, PRL record | PASS |
| K10 | Marchetti–Oriti–Pithis–Thürigen 2023, PRL 130, 141501 (mean-field condensate transition justified) | browser.search (secondary summary; PRL record via that summary) | PASS with SECONDARY-ONLY caveat on the "justified" gloss — the PRL existence is confirmed; the interpretive gloss is the summarizer's |
| K11 | Barceló–Liberati–Visser 2011, Living Rev. Relativity 14, 3; doi:10.12942/lrr-2011-3 | browser.search, journal record; updated version Living Rev. Rel. 29, 2 (2026) noted | PASS |
| K12 | Sindoni 2012, SIGMA 8, 027, arXiv:1110.0686 | browser.search, SIGMA/ar5iv record | PASS |
| K13 | Jacobson 1995, PRL 75, 1260–1263, arXiv:gr-qc/9504004v2 | browser.search, arXiv record | PASS |
| K14 | EPRL vertex, Engle–Livine–Pereira–Rovelli 2008, Nucl. Phys. B 799, 136–149, arXiv:0711.0146 | browser.search | PASS |
| K15 | IRH refs [17][18][41][42] (Mukohyama–Uzan 2013; Kehayias et al. 2014; Greensite 1993; Carlini–Greensite 1994) exist as cited | Manuscript bibliography (carried; not independently re-opened) | PASS (carried) |
| K16 | S2 network/KGE retrieval, S5 blending, S6 tournament, S7 Lean/Z3 formalization | — | NOT RUN (no hybrid model proposed; no formalization attempted) |
| K17 | Precise Immirzi value; precise CDT spectral-dimension numbers; string vacuum count | — | ABSTAIN (see §9) |
| K18 | Gemini grader | — | NOT RUN (forbidden by programme rules) |

---

## 5. Framework-by-framework comparison

### 5.1 Loop quantum gravity / spin foams (LQG)

**Assumptions — postulated vs derived.** Postulated: canonical quantization
of GR in Ashtekar (connection) variables; SU(2) spin-network kinematics;
the Barbero–Immirzi parameter $\gamma$ as a free parameter of the quantization.
Derived (within the framework): the spin-network Hilbert space and the
discrete spectra of area and volume operators (C1). The Hamiltonian
constraint / dynamics is not uniquely derived — it is imposed via the
spin-foam ansatz, and different vertex models (Barrett–Crane $\to$ EPRL) are
successive proposals, not deductions.

**Design.** Background-independent canonical quantization; states are
spin networks (graphs labelled by SU(2) representations); dynamics as a
sum over spin foams (2-complexes labelled by representations), the
covariant path integral. EPRL (Engle–Livine–Pereira–Rovelli, Nucl. Phys.
B 799 (2008) 136–149, arXiv:0711.0146) embeds SU(2) data into SL(2,$\mathbb{C})$
via the $Y_{\gamma}$ map and imposes simplicity weakly; its large-spin asymptotics
recover the Regge action (Barrett et al. asymptotics results).

**Reported findings.** (i) Discreteness of area and volume (Rovelli–
Smolin, Nucl. Phys. B 442 (1995) 593–622; erratum ibid. 456 (1995) 753).
(ii) EPRL vertex with finite Immirzi parameter (2008). (iii) Loop quantum
cosmology: a quantum bounce replacing the big-bang singularity in the
symmetry-reduced model (Ashtekar–Pawlowski–Singh 2006, as reported in the
literature — the bounce is a *model* result, not a full-theory result).
(iv) Black-hole entropy counting that matches Bekenstein–Hawking only
after fixing $\gamma$ — the fixing is a calibration, not a prediction (see §9
ABSTAIN on the numerical value).

**What would falsify it.** A demonstrated failure of the classical limit
(smooth GR not recovered from spin foams in the continuum limit) would
remove its claim to be quantum GR; observed Lorentz violation at a level
the framework's discreteness implies would count against it; a proof that
no EPRL-type amplitude has a good continuum limit would be fatal. The
classical-limit question is the field's own stated open problem, not an
external objection.

**Grade (C1, C2).** C1: **C** — worst-of: independence $I1 \to C$; postulation
ceiling: evidence-guided (kinematics derived from stated quantization
premises$) \to C$; record: primary paper confirmed $\to C. C2: **C$** — same
computation; the Regge asymptotics is a theorem about the model, the
model itself is a proposal (postulation ceiling C).

### 5.2 String theory and AdS/CFT

**Assumptions — postulated vs derived.** Postulated: fundamental objects
are 1D strings (not points); supersymmetry; extra spatial dimensions
(10D superstrings / 11D M-theory); a background spacetime in which strings
propagate (perturbative string theory is background-*dependent*; AdS/CFT
is the background-independent claim). Derived (conditionally): the
graviton as a massless spin-2 string mode; gauge interactions from open
strings / branes; the AdS/CFT duality *conjecture* from the D-brane
decoupling argument.

**Design.** Perturbative expansion in the string coupling and $\alpha'$; the
low-energy limit is supergravity; non-perturbative definition is claimed
via dualities, above all AdS/CFT: Type IIB string theory on AdS${}_{5}\timesS^{5}$ is
conjectured dual to N = 4 SU(N) super-Yang–Mills in 4D (Maldacena,
hep-th/9711200 v1 27 Nov 1997; journal version Adv. Theor. Math. Phys.
2 (1998) 231–252). The paper's own language is conjecture: "We conjecture
that compactifications of M/string theory on various AdS spacetimes is
dual to various conformal field theories."

**Reported findings.** (i) The duality conjecture itself and its large-N,
large-$\lambda$ supergravity limit, where classical gravity computations reproduce
strong-coupling field-theory results (Aharony–Gubser–Maldacena–Ooguri–Oz,
Phys. Rep. 323 (2000) 183–386, hep-th/9905111 — review, existence confirmed in this
session's search). (ii) Black-hole microstate counting in specific
supersymmetric cases (Strominger–Vafa 1996 — cited here as a reported
result of the field; NOT independently verified in this session, so it
carries no load in this draft's grades). (iii) No experimental prediction
of string theory has been confirmed; supersymmetry and extra dimensions
remain unobserved at collider and astrophysical scales probed to date.

**What would falsify it.** A proof that no consistent de Sitter vacuum
exists in string theory would falsify its claim to describe our universe
(the de Sitter / swampland debate is live and unresolved — stated here
as an open controversy, not a verdict); a theorem that AdS/CFT cannot
extend beyond AdS asymptotics would confine it to a toy setting; direct
observation of Lorentz violation or of a hard Planck-scale cutoff
incompatible with string spectra would count against it. Note the
asymmetry: because the framework is vast and flexible (landscape), it is
the hardest in the set to falsify — that flexibility is itself a
methodological cost, recorded here, not a finding.

**Grade (C3).** **C** — worst-of: $I1 \to C$; postulation ceiling: the duality
is a conjecture (evidence-guided at best$) \to C$; record: primary paper
confirmed, conjecture language verified $\to C$. The claim "AdS/CFT is
proved" would be CONTRADICTED; it is not made here.

### 5.3 Asymptotic safety

**Assumptions — postulated vs derived.** Postulated: quantum gravity is a
local quantum field theory of the metric; the Wilsonian RG applies to
gravity; a non-Gaussian UV fixed point (the Reuter fixed point) exists
with finitely many relevant directions. Derived (conditionally): within a
truncation, the fixed point exists and predicts relations among couplings
(e.g. the bare couplings become predictions rather than inputs, per the
programme's own statement).

**Design.** Functional renormalization group (Wetterich equation) for the
effective average action; Einstein–Hilbert truncation as the simplest
approximation, extended to higher-derivative and matter-coupled
truncations. Background independence is implemented via the background-field
method — the extent to which this is genuine background independence is a
live internal debate, recorded here.

**Reported findings.** Weinberg's proposal (in *General Relativity: An
Einstein Centenary Survey*, 1979, p. 790); Reuter's FRG construction for
gravity (1998); Lauscher–Reuter (hep-th/0110021) report "considerable
evidence" for a non-Gaussian fixed point *in the truncated flow* and state
explicitly the open question "whether the fixed point predicted by the
Einstein–Hilbert truncation actually approximates a fixed point in the
exact theory, or whether it is an artifact of the truncation." That caveat
is part of the finding, not an afterthought.

**What would falsify it.** Demonstration that the fixed point is a
truncation artefact (e.g. it disappears systematically as truncations are
enlarged in a controlled way); a proof that gravity requires infinitely
many relevant directions (loss of predictivity); or a conflict between its
(cosmological / black-hole) predictions and observation once those
predictions are made sharply — most are currently too qualitative to test.

**Grade (C4).** **C** — worst-of: $I1 \to C$; postulation ceiling: the fixed
point is postulated, evidence is truncation-internal $\to C ($evidence-guided);
record: primary sources confirmed, caveat quoted from the source $\to C$.

### 5.4 Causal dynamical triangulations (CDT)

**Assumptions — postulated vs derived.** Postulated: the gravitational
path integral is a sum over causal triangulations — piecewise-flat
4-geometries built from 4-simplices with a fixed global time foliation
(causality imposed by hand); a Wick rotation only after causal structure
is fixed; the Regge action as the discretized Einstein–Hilbert action.
Derived (numerically): the phase structure, including a de Sitter phase in
which an extended 4D universe emerges.

**Design.** Lattice quantum gravity with Lorentzian building blocks;
Monte Carlo simulation of the sum over geometries; observables are
geometric (volume profiles, spectral dimension, curvature correlators).

**Reported findings.** (i) "Emergence of a 4D World from Causal Quantum
Gravity" (Ambjørn–Jurkiewicz–Loll, Phys. Rev. Lett. 93 (2004) 131301):
evidence that a macroscopic four-dimensional world emerges dynamically.
(ii) Spectral dimension: "While four-dimensional on large scales, the
quantum universe appears two-dimensional at short distances" (Ambjørn et
al., hep-th/0505113 v2, abstract, verified by direct arXiv read
2026-11-10) — "dynamical dimensional reduction", offered as a possible
self-renormalization mechanism at the Planck scale. (iii) The quantum
fluctuations around the emergent de Sitter universe are, in the simulated
regime (linear size 17–28 Planck lengths, per arXiv:0712.2485), "to good
approximation still describable semiclassically".

**What would falsify it.** If the de Sitter phase were shown to be a
lattice artefact vanishing in the continuum limit; if the spectral
dimension ran to a value incompatible with any continuum interpretation;
if matter coupling destroyed the de Sitter phase. The programme's own
limitation: matter and gauge fields are not yet part of the emergent
picture, and the continuum limit is not proved.

**Grade (C5).** **C** — worst-of: $I1 \to C$; postulation ceiling: numerical
evidence in a lattice model (evidence-guided$) \to C$; record: primary
papers confirmed, abstract read directly $\to C$. The precise spectral-
dimension numbers $(4.02 \pm 0.1 / 1.80 \pm 0.25)$ are verified in the
primary literature (Giasemidis et al. 2012, eq. 7 — see §9, item 2 as
amended in assembly); no grade above C is claimed for them in any case.

### 5.5 Causal set theory

**Assumptions — postulated vs derived.** Postulated: spacetime is
fundamentally a locally finite partially ordered set (causal set); volume
= number of elements (one element per Planck 4-volume, Poisson
sprinkling); the causal order is the fundamental structure. Derived
(from classical Lorentzian geometry, Malament 1977, building on
Hawking–King–McCarthy): causal structure determines the metric up to a
conformal factor — the theorem that motivates the programme ("order +
number = geometry"). The quantum dynamics is NOT derived: it is the
programme's central open problem (classical sequential growth models are
a classical stochastic stand-in).

**Design.** Discrete causal order as ontology; continuum manifold as
approximation; dynamics sought as a quantum sum over causal sets (no
agreed action); cosmology via stochastic growth models (Rideout–Sorkin
classical sequential growth).

**Reported findings.** (i) The founding proposal (Bombelli–Lee–Meyer–
Sorkin, Phys. Rev. Lett. 59 (1987) 521–524). (ii) The $\Lambda$ prediction:
Sorkin (Int. J. Theor. Phys. 36 (1997) 2759–2781, arXiv:gr-qc/9706002)
argued from the number/volume uncertainty relation that $\Lambda$ fluctuates
with magnitude $\Lambda \sim \Delta\Lambda \sim 1/\sqrt{V} \sim \pm10^{-120}$ in natural units — published
before the 1998 supernova discovery of acceleration, and described in
Surya's Living Review (arXiv:1903.11544) as "the most striking" of the
causal-set phenomenology ("the 1987 prediction of Sorkin for the value
of the cosmological constant $\Lambda$"). The everpresent-$\Lambda$ model (Ahmed–Dodelson–Greene–Sorkin,
astro-ph/0209274) develops it into a stochastic dark-energy model
confronted with SN Ia and CMB data (Zwane–Afshordi–Sorkin 2018;
2307.13743 review). Note the honest qualification: the prediction is
order-of-magnitude and heuristic, and it assumes an unknown dynamics
drives mean $\Lambda$ to zero.

**What would falsify it.** A measurement showing $\Lambda$ is exactly constant
with no fluctuation structure at the predicted level would count against
everpresent $\Lambda ($current data do not resolve this); a proof that no causal-
set dynamics can recover GR in the continuum limit would be fatal; the
absence of any quantum dynamics after four decades is the standing
methodological charge.

**Grade (C6).** **C** — worst-of: $I1 \to C$; postulation ceiling: the $\Lambda$
argument is heuristic (evidence-guided$) \to C$; record: founding paper and
1997 prediction confirmed in primary/secondary literature $\to C$. The
"prediction-in-advance" status is a historical fact about publication
order (1997 vs 1998), grade C as a historical claim.

### 5.6 Group field theory (GFT / TGFT)

**Assumptions — postulated vs derived.** Postulated: the fundamental
entities are quanta of geometry (polyhedra / spin-network vertices)
described by a field theory on a group manifold (not on spacetime);
spacetime is a many-body / condensate phase of these quanta. Derived
(conditionally): spin-foam amplitudes as Feynman amplitudes of the GFT;
effective cosmological dynamics as hydrodynamics of a condensate.

**Design.** Quantum field theory on (products of) a Lie group, with
combinatorially non-local interactions; states are polyhedral complexes;
a condensate state (analogous to Bose–Einstein condensation) is the
candidate geometric phase; geometrogenesis is the proposed phase
transition from a non-geometric to a geometric phase.

**Reported findings.** (i) Gielen–Oriti–Sindoni (Phys. Rev. Lett. 111
(2013) 031301): a class of condensate states interpretable as macroscopic
homogeneous geometries, yielding in the semiclassical isotropic case a
modified Friedmann equation — "the first concrete, general procedure for
extracting an effective cosmological dynamics directly from a fundamental
theory of quantum geometry" (authors' words). (ii) Marchetti–Oriti–
Pithis–Thürigen (Phys. Rev. Lett. 130 (2023) 141501): mean-field theory
of the condensate transition is justified in realistic TGFT models — the
condensate assumption is no longer pure hypothesis. (iii) OPEN, stated in
the field's own 2026 landscape summary: whether the condensate phase *is*
continuum GR geometry remains unresolved.

**What would falsify it.** Demonstration that the condensate phase does
not exist in the full (non-mean-field) theory; that its effective dynamics
cannot reproduce GR even approximately; or that geometrogenesis requires
an extra temporal dimension (a criticism raised in the philosophy-of-
physics literature — Oriti's proposal analysed in *Philosophy of Physics*,
2023; the extra-time worry is a live objection, not a settled refutation).

**Grade (C7).** **C** — worst-of: $I1 \to C$; postulation ceiling: condensate
= geometric phase is a postulate under active test $\to C$; record: 2013 PRL
confirmed; 2023 PRL existence confirmed with SECONDARY-ONLY gloss on
"justified" $\to C$.

### 5.7 Emergent / analogue gravity (incl. thermodynamic gravity)

**Assumptions — postulated vs derived.** This is a family, not one theory.
Common move: the metric is a collective / effective variable of some
non-gravitational substrate (fluid, BEC, spin system, pregeometric
fields). Postulated: the substrate and its dynamics. Derived
(conditionally): an effective Lorentzian metric for perturbations; in
Jacobson's case, the Einstein equation from thermodynamic premises.

**Design.** (a) Analogue models: sound in a moving fluid obeys a wave
equation in an effective acoustic metric; supersonic flow creates an
acoustic horizon ("dumb hole") with phononic Hawking radiation
(Barceló–Liberati–Visser, Living Rev. Relativity 14 (2011) 3,
doi:10.12942/lrr-2011-3; major update Living Rev. Relativity 29 (2026) 2).
(b) Induced/emergent gravity: the graviton as a composite / Goldstone
mode; Einstein–Hilbert term induced by matter loops (Sakharov's idea, as
surveyed in Sindoni 2012). (c) Thermodynamic gravity: Jacobson (Phys.
Rev. Lett. 75 (1995) 1260–1263, arXiv:gr-qc/9504004v2) derives the
Einstein equation from $S \propto A$ plus $\deltaQ = T$ dS applied to all local Rindler
horizons — "the Einstein equation is an equation of state". (d)
Pregeometric models: metric as a composite (meson-like) operator of
microscopic fields (Sindoni 2012, §8; Sindoni 2013, J. Phys.: Conf. Ser.
410, 012140).

**Reported findings.** (i) Analogue Hawking radiation is a *theoretical*
necessity in the models and has been *experimentally observed in analogue
form* (fluid/BEC horizons — reported in the 2026 BLV update; the
observation is of the analogue, not of astrophysical Hawking radiation).
(ii) Jacobson's derivation is valid given its premises; its interpretation
is disputed (it may show that gravity is thermodynamic, or only that the
Einstein equation is consistent with horizon thermodynamics — the
alternative reading is live in the recent literature, e.g. arXiv:1401.5262
line of work). (iii) Sindoni's critical conclusion (SIGMA 8 (2012) 027):
gravity-like features are recovered "more or less successfully" across
the models, with Lorentz invariance and the equivalence principle as the
recurrent failure points (multi-component systems generically give
multi-metric / Finsler geometries, not one metric).

**What would falsify it.** For analogue models: the Bartha gate (§6) —
they do not claim to be theories of gravity, so "falsification" is the
wrong frame; they are falsified as *analogies* where the mapping breaks
(the negative analogy). For Jacobson-style claims: a demonstration that
local equilibrium fails at the relevant horizons, or that the entropy–area
relation is not fundamental, removes the derivation's premises. For
pregeometric models: recovery of a single universal metric with the
equivalence principle is the test — Sindoni's survey says it is not yet
passed.

**Grade (C8, C9).** C8: **C** — worst-of: $I1 \to C$; the kinematics/dynamics
split is stated in the primary review itself $\to C$. C9: **C** — worst-of:
$I1 \to C$; Jacobson's result is a conditional derivation (premises stated in
the abstract$) \to C$ as a conditional claim; the *interpretation* ("gravity
is emergent") is a separate claim, grade **D** (exploratory, live
alternatives, no discriminating test).

### 5.8 IRH in the comparison

**Assumptions — postulated vs derived.** Postulated: a real scalar field
$\psi$ on a 4D base with Swift–Hohenberg-type dynamics (conserved, Model B);
the substrate itself (its physical identity is unspecified); three
generations; $\bar{\psi}$; $q_{0}$ tuning; the dimensional assignment (undecided).
Derived (Grade A, carried$): D_{4}$ selection (S = 64/141), isotropy through
4th order, 2T/McKay/$E_{6}$, CFL bound, envelope equation and its validity
domain, d = 4 marginality. NOT derived (Part IX): Lorentzian signature,
Einstein equations, $E_{6}$ breaking, Higgs sector, nucleation event,
$\bar{\psi}$'s value.

**Design.** Interference dynamics of a pattern-forming field: triad
resonances select $D_{4}$; the 24-cell / 2T structure reads off $E_{6}$; defects
(dislocations, point solitons) are the matter-like content; spacetime and
gravity are *not yet* constructed — reading (A)/(B)/(C) undecided.

**Reported findings.** See §3. The distinctive IRH results are the
*selection mechanism* (a dynamical explanation of why $D_{4}$, not a
postulate of it) and the *gauge identification* $(E_{6}$ read off the
substrate, with so(8) excluded by theorem). No other framework in the set
derives its gauge algebra from a selection mechanism; no other framework
in the set has its geometric core machine-checked in Lean. Conversely,
IRH is the *least* developed on the gravitational side: it has no
candidate Einstein equation, no signature mechanism, and no cosmology.

**What would falsify it.** VI.1: phase locking saturating well below 1 in
the large-volume limit. VI.2: the $D_{4}$ band vanishing under reasonable $w_{6}$
and detuning. VI.5: quartic directional dependence from this mechanism.
VI.6: a stable line defect in $T^{4}\timesS^{3}$. VI.4: a stable run above the CFL
bound. Programme-level: a proof that no dynamical-signature mechanism can
work on a classical Euclidean substrate (Greensite's condition) would
close reading (A) and force (B) or (C).

**Grade (C10, C11).** C10: geometric core **A** (carried from the repo
record: kernel-verified, I2+ independent re-derivation — the grade is the
repo's, cited here, not re-earned by this draft); physical/substrate
reading **C/D** (manuscript Part X: "supported rather than asserted" for
the emergence claim; the substrate's physical identity is a postulate).
C11: **C** as a negative/absence claim (Part IX text verified by direct
read of the manuscript in this session; $I1 \to C$ cap applies to this
draft's statement of it).

---

## 6. Bartha articulation & transportability audit (S4)

### 6.1 The load-bearing transfer: substrate dynamics $\Rightarrow$ Einstein equations

| | Source: analogue gravity (fluid/BEC) | Target: IRH substrate |
|---|---|---|
| **Positive analogy** | Wave propagation on a slowly varying background defines an effective metric; horizons and geodesic bending follow | Wave (envelope) propagation on the $\psi$ substrate would define an effective metric |
| **Prior association (source)** | Acoustic metric derived from fluid equations; phononic Hawking radiation derived from the horizon | (No derivation in IRH: the effective metric is *identified* with a local impedance tensor, not derived from substrate dynamics) |
| **Negative analogy** | Effective metric obeys the *fluid's* equations, not Einstein's; no diffeomorphism invariance; no Bianchi identity; no universal coupling; no two TT polarizations | Same, by IRH's own record (§IX.3): "the effective metric obeys the substrate's own equation of motion, not $G\mu\nu = 8\piT\mu\nu$. This is a general limitation of analog models [19]" |
| **Critical feature in Negative Analogy?** | YES — the Einstein equations themselves, diffeomorphism invariance, and the graviton polarizations are exactly the features that fail to transfer | — |

**Verdict: transfer FAILS (Bartha gate).** A critical feature of the
source derivation — that the dynamics are the substrate's, not Einstein's
— sits in the Negative Analogy. No number of surface similarities (horizons,
bending, effective metric) repairs this. This is not a new finding of this
draft: IRH v93.1 already records it (§IX.3) and retracted the v92
Einstein-from-elasticity claim. This draft *confirms* the retraction
against the primary analogue-gravity literature (BLV 2011; Sindoni 2012)
and records the gate as FAILED for any future attempt to revive it.

### 6.2 Jacobson $\Rightarrow$ IRH

Jacobson's derivation assumes $(i) S \propto A$ for local Rindler horizons,
(ii$) \deltaQ = T$ dS, (iii) local equilibrium at every spacetime point. IRH's
substrate is a classical scalar field with no established horizon
thermodynamics, no entropy–area relation, and no local-equilibrium
structure. Critical features (i)–(iii) have **no established positive
analogue** in IRH. Transportability audit: the selection diagram would
carry S-nodes at every thermodynamic premise with no bridging
mechanism — **transport FAILS / NOT ESTABLISHED**. A Jacobson-style
derivation inside IRH would first need a substrate thermodynamics, which
does not exist in v93.1.

### 6.3 Dynamical signature $\Rightarrow$ IRH reading (A)

Greensite (1993) / Carlini–Greensite (1994) / Mukohyama–Uzan (2013)
mechanisms require a one-loop effective potential with more fermionic
than bosonic DOF. IRH's substrate is a single real (bosonic) scalar.
The critical feature (fermion dominance in the loop) sits in the
Negative Analogy for the current substrate. Transfer FAILS for v93.1 as
it stands; it could in principle be repaired by adding fermionic
substrate degrees of freedom — which would be a new postulate, not a
derivation, and would need its own ledger entry.

### 6.4 CDT / GFT / LQG $\Rightarrow$ IRH (structural comparison, not transfer)

No transfer is attempted between these frameworks and IRH. Structural
observations only: CDT and IRH both *derive* a 4D structure dynamically
(CDT: de Sitter phase from simulation; IRH: $D_{4}$ from interference), but
CDT's emergence is of the spacetime metric itself while IRH's is of a
spatial lattice symmetry with spacetime undecided (IX.2). GFT's
condensate and IRH's pattern formation are both many-body emergence
stories, but GFT's quanta are geometric by construction while IRH's
field is not. These are compatible-with observations (grade D as
cross-framework claims), not transfers.

**Self-evaluation rubric (cross-domain-discovery §"Self-Evaluation
Rubric", 8 checks):** (1) independent test exists — PARTIAL: each
framework's own tests are named, but this draft runs none; (2)
falsification boundary stated — PASS (per framework, §5); (3) Bartha
articulation passes — FAIL for the Einstein-equation transfer (correctly
failed: the failure is the finding); (4) transportability audited — PASS
(§6.2–6.3); (5) second independent tool — PASS for the one recomputed
number (K1), NOT RUN for literature numbers (they are reported, not
computed); (6) no invented numbers — PASS (ABSTAINs recorded); (7)
assumption ledger complete — PASS (§10); (8) grade honest — PASS
(worst-of shown). Overall: a hypothesis-grade comparative survey, not a
discovery — which is what the task asked for.

---

## 7. Gaps and untested conditions (flagged)

### 7.1 Gaps in the field as a whole

1. **No framework derives all four at once:** (a) Lorentzian signature,
   (b) Einstein equations with diffeomorphism invariance, (c) the
   Standard Model gauge structure and matter, (d) a confirmed
   prediction. String theory has (c)-adjacent structure (gauge groups
   from branes) but not (a)/(d); LQG has background independence but not
   (c)/(d); asymptotic safety has (b)-adjacent structure (GR as the
   classical limit is assumed, not derived) but not (c)/(d); CDT has an
   emergent (a)-like spacetime but no (c); causal sets have a (d)-adjacent
   prediction but no dynamics; GFT has a (b)-adjacent effective dynamics
   but no established (c); IRH has a derived (c)-adjacent gauge algebra
   $(E_{6})$ but no (a)/(b).
2. **The classical/continuum limit is unproved everywhere it matters:**
   LQG/spin foams, CDT, GFT, causal sets all carry it as an open problem.
   Asymptotic safety assumes the metric description throughout. String
   theory's limit is supergravity by construction (postulated, not
   emergent).
3. **Matter is an add-on everywhere except string theory and IRH'$s E_{6}$
   reading:** LQG, CDT, causal sets, GFT, asymptotic safety all couple
   matter by hand. IRH reads $E_{6}$ off the substrate but has not derived
   the breaking pattern, the Higgs sector, or three generations (input).
4. **de Sitter vs AdS:** the observed universe has positive $\Lambda$; AdS/CFT
   is formulated in AdS. No framework in the set has a controlled,
   agreed de Sitter quantum gravity. CDT's emergent universe *is* de
   Sitter-like — but only as a Euclidean simulation result in one phase.
5. **Lorentz invariance:** emergent frameworks (including IRH at 6th
   order / next-nearest-neighbour) must explain why Lorentz violation is
   absent to the precision observed. IRH's VI.5 absence prediction
   (no quartic anisotropy) is a genuine test — but the 6th-order size is
   uncomputed, so the test has no quantitative target yet.

### 7.2 Gaps specific to IRH (from Part IX — where IRH cannot answer)

- **IX.2:** dimensional assignment (A)/(B)/(C) undecided; the framework
  cannot say what its 4D base *is* relative to observed 3+1 spacetime.
  Reading (B) breaks the $D_{4}$ symmetry the selection argument uses;
  reading (C) has no construction offered.
- **IX.3:** Lorentzian signature (no classical Euclidean substrate is
  known to work); Einstein equations (Bartha FAIL, §6.1); QM beyond
  single-particle envelopes (boundary, not gap — entanglement/Bell needs
  nonlocality or superdeterminism); monopole resolution open.
- **IX.$4:** E_{6}$ breaking and Higgs sector not derived at all; VEV/$A_{3}$/CKM
  are a clean restart.
- **IX.$5:** \bar{\psi}$ unfixed; nucleation event unsupplied; joint early-universe
  narrative missing in its entirety.
- **IX.1 (tractable but undone):** larger-volume phase locking (VI.1
  measured 0.26 of 1 — incomplete), nucleation barrier, $D_{4}$ band under
  detuning + higher-order terms, defect homotopy beyond elementary
  Burgers vectors, irrational $D_{4}\to3D$ projections.
- **Consequence for the comparison:** IRH cannot currently be scored
  against the others on "derives GR" — it is not in that race yet. Its
  comparative advantage is narrow and real (derived selection + derived
  gauge algebra + machine-checked core); its comparative deficit is
  broad (no spacetime, no gravity dynamics, no cosmology).

### 7.3 Untested conditions (per framework)

| Framework | Sharpest untested condition |
|---|---|
| LQG / spin foams | Continuum/classical limit of EPRL amplitudes; recovery of the Einstein equations from the spin-foam sum |
| String / AdS-CFT | Any de Sitter construction; any experimental signature of strings/SUSY/extra dimensions; proof of the duality beyond the supergravity limit |
| Asymptotic safety | Existence of the Reuter fixed point beyond truncations; finiteness of relevant directions |
| CDT | Continuum limit of the de Sitter phase; coupling of matter/gauge fields; Lorentzian (not Euclidean-simulated) observables |
| Causal sets | Any quantum dynamics recovering GR; everpresent-$\Lambda$ fluctuation structure vs constant $\Lambda ($currently unresolvable) |
| GFT | Condensate phase = continuum GR geometry; geometrogenesis without extra time; full-theory (non-mean-field) condensate existence |
| Analogue / emergent | Single universal metric + equivalence principle from a multi-component substrate (Sindoni's failure point); Jacobson premises in a concrete substrate |
| IRH | VI.1 large-volume locking $\to 1$; VI.2 band survival under detuning + $w_{6}$; VI.5 sixth-order anisotropy size; IX.2 decision; IX.3 external structure; IX.5 nucleation |

---

## 8. Rival / failure mode (steelman and defeat)

**Strongest rival to the CLAIM.** The CLAIM says no framework derives
signature + field equations + gauge structure + a confirmed prediction.
The strongest objection: causal-set theory *did* predict $\Lambda$'s order of
magnitude in advance, and CDT *did* derive a de Sitter universe from
simulation — so "no framework has anything" would be false. **Answer:**
the CLAIM does not say that; it says no framework has *all four* and
none has a *laboratory-confirmed Planck-scale* prediction. The $\Lambda$
prediction is order-of-magnitude and heuristic, and CDT's de Sitter
universe is a numerical result in a lattice model without matter. Both
are real achievements and both are recorded at full strength in §5; neither
defeats the CLAIM.

**Strongest rival to IRH's standing.** IRH's geometric core is Grade A,
but its physical claims are the weakest in the set on gravity. A critic
could say IRH is not a quantum-gravity framework at all, but a
pattern-formation model with a gauge-algebra observation. **Answer:**
that is close to IRH's own Part X assessment ("a well-posed research
programme with a verified geometric core$\dots$ not a completed unified
theory, and the distance to one is large — measured precisely by
Part IX"). The draft does not resist this; it records it. What would
change the assessment: a derivation of the signature mechanism, a
substrate thermodynamics supporting a Jacobson-type argument, or a
decision procedure for IX.2 — none of which exists in v93.1.

**Failure mode of this draft.** A comparative survey can smuggle in a
ranking the evidence does not support. Guard: no overall ranking is
given; the matrix (§9 of the companion file) is dimension-by-dimension,
and every "strongest" statement names the dimension it is strongest on.
If a reader wants a single winner, this draft abstains — the evidence
does not support one.

---

## 9. ABSTAINs

1. **The numerical value of the Barbero–Immirzi parameter** (and hence
   any quantitative statement about LQG black-hole entropy matching).
   "I cannot verify this with the available tools" — the value was seen
   only in a secondary blog summary in this session, not in a primary
   source. The qualitative claim (entropy matching fixes $\gamma)$ is stated
   without a number.
2. **Precise CDT spectral-dimension values — VERIFIED IN ASSEMBLY;
   the draft's ABSTAIN is withdrawn.** The numbers $4.02 \pm 0.1$ at large
   scales and $1.80 \pm 0.25$ at short distances are in the primary
   literature: Giasemidis–Wheater–Zohren, "Dynamical dimensional
   reduction in toy models of 4D causal quantum gravity", Phys. Rev. D
   86, 081503 (2012), eq. $(7): D_{s}(\sigma) = 4.02 - 119/(54+\sigma)$, with
   $1.80 \pm 0.25$ at $\sigma\to0$ and $4.02 \pm 0.1$ at $\sigma\to\infty$, citing Ambjørn et al.
   2005. Full text read directly by the parent agent in assembly.
   (Task 12 independently evaluates the same fit: 1.82 at $\sigma\to0$,
   within $1.80 \pm 0.25$.)
3. **Any quantitative string-theory landscape count** (e.g. numbers of
   vacua) and any quantitative supersymmetry/extra-dimension exclusion
   limit. "I cannot verify this with the available tools" — no primary
   source for such a number was opened in this session, and none is
   needed for the comparison.
4. **Strominger–Vafa black-hole microstate counting** as a load-bearing
   claim: not independently verified in this session; mentioned only as
   a reported result of the field and excluded from all grades.
5. **The 2023 GFT mean-field result's interpretive gloss** ("the
   condensate assumption is justified"): the PRL's existence is confirmed;
   the gloss is SECONDARY-ONLY (from a landscape summary) and is labelled
   as such wherever used.

---

## 10. Ledgers

### 10.1 Assumption ledger

| # | Assumption | Where it enters | Status |
|---|------------|-----------------|--------|
| A1 | IRH: real scalar $\psi$, Swift–Hohenberg-type Model B dynamics on a 4D base | All IRH claims | Postulate (manuscript §I) |
| A2 | IRH: three generations; $\bar{\psi}$ value; $q_{0}$ tuning; dimensional assignment | IRH matter / band claims | Acknowledged inputs (INPUTS.md) |
| A3 | LQG: Ashtekar variables; SU(2) spin networks; Immirzi parameter | C1, C2 | Postulate of the programme |
| A4 | String: strings, SUSY, extra dimensions, background for perturbation theory | C3 | Postulate of the programme |
| A5 | Asymptotic safety: metric QFT + Wilsonian RG + Reuter fixed point exists | C4 | Postulate (fixed point) |
| A6 | CDT: causal triangulations + foliation + Regge action | C5 | Postulate (regularization) |
| A7 | Causal sets: discrete partial order; volume = number | C6 | Postulate (founding hypothesis) |
| A8 | GFT: field theory on group manifold; condensate = geometric phase | C7 | Postulate (condensate identification) |
| A9 | Analogue: substrate dynamics given; effective metric defined by perturbations | C8 | Postulate (substrate) |
| A10 | Jacobson: $S \propto A$; $\deltaQ = T$ dS; local equilibrium at all local Rindler horizons | C9 | Premises (stated in the paper) |
| A11 | This draft: literature survey, not systematic review; I1 verification only | All comparative grades | Method choice (stated §2) |

### 10.2 Parameter ledger

| Parameter | Value / range | Provenance | Role |
|---|---|---|---|
| IRH $S = \tau^{2}/q_{4}$ | $64/141 \approx 0.454 ($exact rationals) | CORE.md; arithmetic re-checked K1 | Derived selection criterion |
| IRH $D_{4}$ margin over $A_{4}$* | 17.3% | CORE.md (carried) | Derived (carried) |
| IRH $D_{4}$ band | 11.85% of scanned plane | CORE.md (conditional on $q_{0}$ tuning) | Derived, conditional |
| IRH $r_{eff}$ | +0.107 at $\bar{\psi} = -0.18$ | CORE.md (carried) | First-order transition marker |
| IRH $\bar{\psi}$ conservation | to $8.3\times10^{-17}$ | CORE.md (carried) | Model B requirement |
| IRH envelope validity | <1% for $a_{0}$\|k\| ≲ 0.3 | CORE.md (carried) | Validity boundary VI.3 |
| IRH triad locking | 0.26 of max 1 (measured) | VI-predictions.md (carried) | VI.1 status |
| CDT simulated universe size | 17–28 Planck lengths | arXiv:0712.2485 abstract | Regime of the de Sitter result |
| Causal-set $\Lambda$ | $\sim \pm10^{-120} ($natural units) | Sorkin 1997, as reported | Heuristic prediction |
| LQG $\gamma ($Immirzi) | — | ABSTAIN (§9.1) | Free parameter |
| String vacuum count | — | ABSTAIN (§9.3) | Not stated |

### 10.3 Choice ledger

| Choice | Why | Effect if changed |
|---|---|---|
| deepest-research FULL mode; systematic-review NOT chosen | Task + standing delegation; comparison, not exhaustive coverage | A systematic review would change the corpus, not the per-claim grades |
| Framework set = task list + IRH | Task scope | Adding frameworks (e.g. twistor, non-commutative geometry) would widen the matrix, not change the CLAIM |
| Comparison dimensions = the 7 named in the task | Task scope | Different dimensions could flatter different frameworks |
| Grades capped at C for new comparative claims (I1, human gates not run) | HLRE §6.5 fallback | A human source/balance gate could raise individual descriptive grades, not the physical claims |
| S2/S5/S6/S7 NOT RUN | No network mining, no blending, no tournament, no formalization in this task | Running them could add hypotheses, not change the Bartha FAIL |
| Precise CDT spectral numbers | Verified in assembly via Giasemidis et al. 2012, eq. (7) | The draft's ABSTAIN is withdrawn; the numbers are now stated as verified |

---

## 11. Evidence that would change the answer

- **For the CLAIM:** any framework deriving signature + Einstein equations
  + gauge structure from its own postulates with a confirmed prediction
  would falsify the CLAIM outright. Short of that: a proved continuum
  limit for EPRL/CDT/GFT, a proved AdS/CFT duality, or a demonstrated
  Reuter fixed point beyond truncations would each force a rewrite of
  §5 and §7 for that framework.
- **For the Bartha FAIL (§6.1):** a substrate model in which the
  effective metric's dynamics *are* the Einstein equations (with
  diffeomorphism invariance and two TT polarizations derived, not
  imposed) would reverse the gate. No such model is in the surveyed
  literature.
- **For IRH's standing:** a signature mechanism working on a classical
  Euclidean substrate; a substrate thermodynamics; an IX.2 decision with
  a construction; large-volume VI.1 locking $\to 1$.
- **For causal sets:** a quantum dynamics recovering GR would promote
  C6 from heuristic prediction to a theory with dynamics; a measurement
  of $\Lambda$ fluctuation structure would test everpresent $\Lambda$ directly.

---

## 12. Citation record

Primary sources confirmed in this session (existence + key content
verified via arXiv/journal pages or the manuscript itself). No reference
below is fabricated; items not confirmed are absent or ABSTAINed in §9.

**IRH (grounding files, read directly):**
- McCrary, B. D., IRH v93.1, `IRH_v93_1_source_rebuilt.txt` (34 pp.),
  esp. Part IX (§IX.2–IX.5) and Appendix A; refs [16]–[19], [41], [42].
- `established/CORE.md`, `guardrails/EXCLUDED.md`,
  `guardrails/INPUTS.md`, `predictions/VI-predictions.md`,
  `OPEN_PROBLEMS.md` (IRH-Theory-Development-Workspace).

**Loop quantum gravity / spin foams:**
- Rovelli, C. & Smolin, L., "Discreteness of area and volume in quantum
  gravity", Nucl. Phys. B 442 (1995) 593–622; erratum ibid. 456 (1995) 753.
- Rovelli, C. & Smolin, L., "Spin networks and quantum gravity",
  Phys. Rev. D 52 (1995) 5743–5759, arXiv:gr-qc/9505006.
- Engle, J., Livine, E., Pereira, R. & Rovelli, C., "LQG vertex with
  finite Immirzi parameter", Nucl. Phys. B 799 (2008) 136–149,
  arXiv:0711.0146.
- Engle, J., Pereira, R. & Rovelli, C., "Flipped spinfoam vertex and loop
  gravity", Nucl. Phys. B 798 (2008) 251–290, arXiv:0708.1236.

**String theory / AdS-CFT:**
- Maldacena, J. M., "The Large N limit of superconformal field theories
  and supergravity", Adv. Theor. Math. Phys. 2 (1998) 231–252,
  arXiv:hep-th/9711200 (v1 27 Nov 1997; v3 22 Jan 1998).
- Aharony, O., Gubser, S. S., Maldacena, J. M., Ooguri, H. & Oz, Y.,
  "Large N field theories, string theory and gravity",
  Phys. Rep. 323 (2000) 183–386, arXiv:hep-th/9905111 (review; existence
  confirmed in session).

**Asymptotic safety:**
- Weinberg, S., "Ultraviolet divergences in quantum theories of
  gravitation", in *General Relativity: An Einstein Centenary Survey*
  (eds. Hawking & Israel), Cambridge Univ. Press (1979), p. 790.
- Reuter, M., "Nonperturbative evolution equation for quantum gravity",
  Phys. Rev. D 57 (1998) 971–985.
- Lauscher, O. & Reuter, M., "Is Quantum Einstein Gravity
  Nonperturbatively Renormalizable?", arXiv:hep-th/0110021.
- Niedermaier, M. & Reuter, M., "The Asymptotic Safety Scenario in
  Quantum Gravity", Living Rev. Relativity 9 (2006) 5.

**Causal dynamical triangulations:**
- Ambjørn, J., Jurkiewicz, J. & Loll, R., "Emergence of a 4D World from
  Causal Quantum Gravity", Phys. Rev. Lett. 93 (2004) 131301,
  arXiv:hep-th/0404156.
- Ambjørn, J., Jurkiewicz, J. & Loll, R., "Spectral Dimension of the
  Universe", Phys. Rev. Lett. 95 (2005) 171301, arXiv:hep-th/0505113 v2
  (abstract read directly 2026-11-10).
- Ambjørn, J., Görlich, A., Jurkiewicz, J. & Loll, R., "Planckian Birth
  of the Quantum de Sitter Universe", arXiv:0712.2485.
- Loll, R., "Quantum Gravity from Causal Dynamical Triangulations: A
  Review", Class. Quantum Grav. 37 (2019) 013002.

**Causal sets:**
- Bombelli, L., Lee, J., Meyer, D. & Sorkin, R. D., "Space-time as a
  causal set", Phys. Rev. Lett. 59 (1987) 521–524.
- Sorkin, R. D., "Forks in the road, on the way to quantum gravity",
  Int. J. Theor. Phys. 36 (1997) 2759–2781, arXiv:gr-qc/9706002.
- Ahmed, M., Dodelson, S., Greene, P. B. & Sorkin, R. D., "Everpresent
  $\Lambda$", Phys. Rev. D 69 (2004) 103523, arXiv:astro-ph/0209274.
- Surya, S., "Directions in Causal Set Quantum Gravity",
  arXiv:1103.6272 (review).
- Surya, S., "The causal set approach to quantum gravity", Living Rev.
  Relativity 22, 5 (2019), arXiv:1903.11544 (review; cited for the
  prediction-in-advance assessment — full text read in assembly:
  "the most striking is the 1987 prediction of Sorkin for the value
  of the cosmological constant $\Lambda$").

**Group field theory:**
- Gielen, S., Oriti, D. & Sindoni, L., "Cosmology from Group Field
  Theory Formalism for Quantum Gravity", Phys. Rev. Lett. 111 (2013)
  031301.
- Marchetti, L., Oriti, D., Pithis, A. G. A. & Thürigen, J.,
  "Mean-field phase transitions in TGFT quantum gravity",
  Phys. Rev. Lett. 130 (2023) 141501, arXiv:2211.12768.
- Oriti, D., "Group field theory as the second quantization of loop
  quantum gravity", Class. Quantum Grav. 33 (2016) 085005 (background;
  existence confirmed via the field's literature as surveyed in session).

**Emergent / analogue / thermodynamic gravity:**
- Barceló, C., Liberati, S. & Visser, M., "Analogue Gravity",
  Living Rev. Relativity 14 (2011) 3, doi:10.12942/lrr-2011-3,
  arXiv:gr-qc/0505065v3; major update Living Rev. Relativity 29 (2026) 2.
- Sindoni, L., "Emergent Models for Gravity: An Overview of Microscopic
  Models", SIGMA 8 (2012) 027, arXiv:1110.0686.
- Jacobson, T., "Thermodynamics of Spacetime: The Einstein Equation of
  State", Phys. Rev. Lett. 75 (1995) 1260–1263, arXiv:gr-qc/9504004v2.
- Greensite, J., "Dynamical origin of the Lorentzian signature of
  spacetime", Phys. Lett. B 300 (1993) 34, arXiv:gr-qc/9210008
  (as cited in IRH refs [41]; carried).
- Carlini, A. & Greensite, J., "Why is spacetime Lorentzian?",
  Phys. Rev. D 49 (1994) 866–878 (as cited in IRH refs [42]; carried).
- Mukohyama, S. & Uzan, J.-P., "From Configuration to Dynamics —
  Emergence of Lorentz Signature in Classical Field Theory",
  Phys. Rev. D 87 (2013) 065020, arXiv:1301.1361 (as cited in IRH
  refs [17]; carried).

**Skills / protocol (design claims, ungraded — not evidence):**
- truth-seeking-frontier v5, cross-domain-discovery v2.0.0, HLRE v5.1,
  deepest-research v2.12.1 (FULL mode). Skill use is method, not
  reliability evidence.

---

## 13. Grade summary (worst-of computations)

| Claim | Independence bound | Caps | Postulation ceiling | Record | Final |
|---|---|---|---|---|---|
| C1 LQG discreteness | $I1 \to C$ | none | evidence-guided $\to C$ | primary confirmed | **C** |
| C2 EPRL dynamics | $I1 \to C$ | none | evidence-guided $\to C$ | primary confirmed | **C** |
| C3 String / AdS-CFT conjecture | $I1 \to C$ | none | conjecture $\to C$ | primary confirmed | **C** |
| C4 Asymptotic safety fixed point | $I1 \to C$ | none | postulated $\to C$ | primary + caveat | **C** |
| C5 CDT emergent 4D + spectral run | $I1 \to C$ | none | evidence-guided $\to C$ | primary confirmed | **C** |
| C6 Causal sets + $\Lambda$ prediction | $I1 \to C$ | none | heuristic $\to C$ | primary confirmed | **C** |
| C7 GFT condensate cosmology | $I1 \to C$ | SECONDARY-ONLY gloss on 2023 item | postulate under test $\to C$ | primary confirmed | **C** |
| C8 Analogue kinematics, not dynamics | $I1 \to C$ | none | review-stated split $\to C$ | primary confirmed | **C** |
| C9 Jacobson conditional derivation | $I1 \to C$ | none | conditional $\to C$ | primary confirmed | **C** |
| C9-interpretation ("gravity is emergent") | $I1 \to C$ | live alternatives | exploratory $\to D$ | disputed in literature | **D** |
| C10 IRH geometric core | (repo record) | — | — | kernel-verified, carried | **A (carried)** |
| C10 IRH substrate reading | (manuscript Part X) | — | — | supported, not asserted | **C/D (carried)** |
| C11 IRH open problems (IX) | $I1 \to C$ | none | absence claim $\to C$ | manuscript read directly | **C** |
| C12 No confirmed Planck-scale prediction | $I1 \to C$ | negative claim | exploratory $\to C$ | survey of primaries | **C** |
| Bartha FAIL (Einstein from substrate) | — | — | — | BLV + Sindoni + IX.3 | **FAIL (gate)** |

---

## VERIFIED / UNVERIFIED / FAILED branch lists

**VERIFIED (in this draft's sense: primary source confirmed in session,
claim stated at its graded level):**
- C1, C2, C3, C4, C5 (qualitative spectral-dimension statement), C6, C7
  (2013 result; 2023 result with gloss caveat), C8, C9 (conditional),
  C10 (carried grades), C11, C12.
- IRH arithmetic $K1 (64/141 \approx 0.454$, exit 0).
- The retraction of Einstein-from-elasticity / signature-from-$i^{2}$ in IRH
  v93.1, confirmed against BLV 2011 and Sindoni 2012.

**UNVERIFIED (stated with the gap named, or not stated):**
- Precise CDT spectral-dimension numbers — VERIFIED in assembly
  (Giasemidis et al. 2012, eq. 7); the draft's ABSTAIN is withdrawn.
- Immirzi parameter value / quantitative BH-entropy matching — ABSTAIN (§9.1).
- String landscape counts; SUSY/extra-dimension exclusion limits — ABSTAIN (§9.3).
- Strominger–Vafa microstate counting — mentioned as reported, not
  verified, excluded from grades.
- The 2023 GFT "justified" gloss — SECONDARY-ONLY.
- IRH carried grades (A core, C/D substrate) — cited from the repo
  record, not re-verified in this draft.
- Greensite / Carlini–Greensite / Mukohyama–Uzan papers — carried from
  the IRH bibliography, not independently re-opened.

**FAILED:**
- **Bartha transfer "substrate dynamics $\Rightarrow$ Einstein equations" — FAILS**
  (§6.1). Critical features (Einstein dynamics, diffeomorphism
  invariance, TT polarizations) sit in the Negative Analogy. This failure
  is IRH v93.1's own recorded retraction, confirmed here.
- **Jacobson $\Rightarrow$ IRH transport — FAILS / NOT ESTABLISHED** (§6.2).
  Thermodynamic premises have no positive analogue in the IRH substrate.
- **Dynamical signature $\Rightarrow$ IRH reading (A) — FAILS for v93.1 as it
  stands** (§6.3). Fermion-dominant loop is absent from a single real
  scalar substrate.
- No other transfer was attempted; S5/S6/S7 NOT RUN (§4, K16).

---

*Draft prepared 2026-11-10 (subagent, workstream D task 8). AI contribution:
literature search, verification against primary sources, and drafting under
HLRE v5.1 / truth-seeking-frontier v5 / cross-domain-discovery v2.0.0.
Human author and accountable party: Brandon D. McCrary. All verification
artificial (I1); human source/balance gates not performed; grades for new
comparative claims cap at C.*
