# READER A3 — Torus-Node Model, lines 4977–9583 (§11–§18 + Appendices A–H)

**Source:** `~/workspace/research/irh/torus-node-comparison/torus_node_model.txt`
(9,583 lines total; original PDF `~/workspace/user/files/torus_node_model_5_7xjk.pdf`,
sha256 `146dd322b3b63daafd21fe5c8f9a5cb399331dd12d22b061a84c30769244c105`).
Paper: "A Torus-Node Model for Emergent Spacetime, Gravity, and Gauge Structure",
Youngik (Tom) Lee.
**Read scope:** lines 4977–9583 only, cover to cover in ~600-line chunks. Lines before 4977
were NOT read by this reader (other readers cover them).

## Mode and governance — stated plainly

- **deepest-research FULL mode.** This is a full-mode close reading / claim extraction.
  **NOT systematic-review mode** — that form was not chosen, and no PRISMA-style
  systematic review was performed.
- **cross-domain-discovery v2.0.0, stages S1–S7:** applied as a *reading* protocol only.
  S1 (BPMF de-jargonisation) was used to sort claims into Background/Purpose/Mechanism/
  Findings; S2–S6 (retrieval, alignment, transportability, blending, tournament) do not apply
  to a single-paper extraction and were NOT run as discovery steps; S7 (formal verification)
  was NOT run — no Lean/Z3 check was executed by this reader. No new cross-domain
  discovery claim is made here; any analogy noted below is at grade ceiling D.
- **truth-seeking-frontier v5:** CLAIM and STATUS are given together at the top of this
  file; checks are reported PASS / FAIL / NOT RUN; ABSTAIN is used where the text does
  not settle a point. No load-bearing number below was independently recomputed by a tool
  — the numbers are *quoted from the paper*, not verified by this reader.
- **HLRE v5.1:** grades below are per narrow claim, worst-of (independence bound, caps,
  postulation ceiling, support in the record). "Derives" is used only for deductive results
  from catalogued axioms in a specified system. The paper's own status labels
  (axiom / hypothesis / theorem / conditional / open) are recorded verbatim and kept
  distinct from this reader's HLRE grades. Most claims in this range are Track E
  (claims about the world / about a physical model); the finite algebraic statements are
  Track F, capped at F3 here because this reader ran no independent re-derivation
  (I1 at best — artificial verification sharing the paper's own pipeline would not raise it).

## CLAIM + STATUS (top-level)

| # | Claim (narrow) | Paper's status | Reader HLRE grade |
|---|---|---|---|
| A3-1 | Finite/comparison measures are reflection positive; unrestricted hard Poisson/Rips measure is NOT reflection positive at measure level (§11) | Theorem 11.3, 11.5 (finite); Hypothesis 4 (averaged) | Track F F3 for finite statements as quoted (not re-derived here); Track E D / INCOMPLETE-EVIDENCE for Hypothesis 4 |
| A3-2 | Eight source-to-continuum conditions jointly imply OS reconstruction (Thm 12.1) | Conditional theorem (implication proved; premises NOT asserted) | Track F F3 as a conditional implication (proof read, not machine-checked); premises open |
| A3-3 | Raw torus data do not determine measure/reflection/metric/gauge/matter (Thm 12.2) | Theorem (non-identifiability, proved by completion pairs) | Track F F3 as quoted |
| A3-4 | Canonical finite model = Axioms I, D, M + level-3 Hecke domain + declared D4 source + Cfin (§13) | Definition / declared package | Design claim (ungraded) — it is a definition, not a finding |
| A3-5 | Observationally constrained specialisation: exact gauge matching in all 10 classes; class V11 selected by gravity–gauge relation; mt ≲ 173.0–173.9 GeV (heavy-threshold option) (§13.7, §16.5) | Conditional numerical benchmark (inputs declared) | Track E D (post-hoc / input-dependent; I0 — same data used in construction/matching) |
| A3-6 | SU(3) mass gap and confinement of the physical source are open; confinement follows from vortex condition (VF), which is itself open at the physical coupling (§17) | Open (Hypothesis 3); Thm 17.1 conditional on (VF) | Track E D / INCOMPLETE-EVIDENCE for the gap; conditional theorem F3 for Thm 17.1 |
| A3-7 | No proton decay; Dirac neutrinos with $m\beta\beta = 0$; $\Lambda$ exactly constant $(w = -1)$; no WIMP; no inflation seed derived (§15) | Qualitative predictions, conditional on field content / declared inputs | Track E D (conditional predictions, untested) |
| A3-8 | Low-energy Lagrangian (18.1) is an effective finite/conditional summary, not a derived continuum action (§18.1) | Stated as conditional summary | Design/statement claim — the paper itself caps it; agree with the cap |

**Checks run:** read-through of lines 4977–9583 — PASS (complete, contiguous chunks).
Independent recomputation of any number — NOT RUN. Lean verification — NOT RUN
(paper's own Lean claims are reported, not checked). External-theorem verification —
NOT RUN (dictionary entries are quoted from Appendix D.1). Contact with author — NOT
DONE (per constraints).

**Section map in this range (line numbers in the .txt file):**
§11 Unitarity $4977 \cdot$ §12 Conditions and dependencies ~5100 (Table 4 p.95, Thm 12.1 p.98,
Table 6 p.100, Thm 12.2 p.$101) \cdot$ §13 Canonical finite model 5649 (Table 7 p.108,
Table 8 p.109, §13.7 p.$113) \cdot$ §14 Scope/relation $6258 \cdot$ §15 Predictions ~6500 (Table 15
p.$123) \cdot$ §16 Numerical benchmarks 6614 (Table 16 p.125, Table 17 p.126–127, Table 19
p.$128) \cdot$ §17 Yang–Mills $6939 \cdot$ §18 Conclusion $7392 \cdot$ App. $A 7650s \cdot$ App. $B ~7950 \cdot$
App. $C ~8100 \cdot$ App. $D ~8150 \cdot$ App. $E ~8750 \cdot$ App. $F ~8900 \cdot$ App. $G ~9050 \cdot$
App. $H ~9200 \cdot$ References to 9583.

---

## (a) Claim register for lines 4977–9583

Status key used by the paper: **AX** = axiom/declared input $\cdot$ **HYP** = hypothesis (named,
open$) \cdot$ **THM** = theorem/proposition/lemma proved in the paper (usually finite or
conditional$) \cdot$ **COND** = conditional (holds only under stated premises$) \cdot$ **OPEN** = open
$\cdot$ **NUM** = numerical result (computation/diagnostic, class per App. $G/H) \cdot$ **DEF** = definition.

### §11 Unitarity (4977–~5100)

| ID | Claim | §/Eq. | Paper status |
|---|---|---|---|
| 11.1 | Lattice model is reflection positive (Thm 4.5); declared finite source and explicit comparison sources are RP | §11 intro | THM (finite) |
| 11.2 | Unrestricted hard Poisson/Rips measure is NOT reflection positive at measure level: fixed sample not reflection invariant (Rem. 4.12); distance-cutoff + pair-difference action has explicit counterexample (negative quadratic direction); position-based gravitational kernel and Cayley–Menger kernel not positive definite (two exact tests) | §11 intro | THM (negative result, finite counterexample) |
| 11.3 | **Hypothesis 4:** reflection positivity of the *averaged* Schwinger functions | §11, Fig. 22 | HYP — open |
| 11.4 | A reflection-positive two-point function has a Källén–Lehmann (Stieltjes) representation with positive spectral measure [52, 53]; tested by exact non-negative least squares [54] | §11 | External theorem + test method |
| 11.5 | **Numerical result 11.1:** (1) quenched average consistent with positive spectral measure below cutoff (p ≲ 3.5 node units), violates it at cutoff scale $p \approx 2\pi$/rc; gauge field same. (2) Physical measure is the joint measure weighted by $Z[\Pi]$, not the quenched average; bosonic-determinant weighting alone collapses node density. (3) Global-count-only constraint: det^+1.5 weight does not equilibrate; mean degree grows $81 \to 290 ($normal $\approx 25)$, measure collapses into clusters; matter-weighted measure well defined only with local count = volume constraint. (4) Local constraint, one node per cell: equilibrates, isotropic; control run (exponent 0) violates Stieltjes representability already for $p^{2} \leq 10$ in two seeds $(\chi^{2} = 384, 391$ for $p^{2} \leq 33, 13$ dof); matter weighting reduces violation ~40%; one seed consistent for $p^{2} \leq 16 (\chi^{2} = 16.2)$ but NOT reproduced — two of three seeds violate for $p^{2} \leq 16 (\chi^{2} = 30.1, 31.6)$ | Num. Res. 11.1 | NUM (diagnostic; mixed/negative — Hypothesis 4 NOT established by these tests) |
| 11.6 | **Proposition 11.2:** if µ${}_{0}$ is RP and dµ/dµ${}_{0} = Z^{-1} \exp(\Sigma \thetaa$ Fa $\Theta$Fa), $\thetaa \geq 0 (11.1)$, then µ is RP; equivalently Gaussian cross-covariance $C+-$ = LLᵀ suffices | Prop. 11.2, (11.1) | THM (abstract factorisation criterion) |
| 11.7 | **Theorem 11.3:** Källén–Lehmann marked-Poisson rotor RP — pair profile $J(x) = \int$ Gm$(x) d\rho(m^{2})$, $d\rho \geq 0 (11.2)$; finite-window compact-rotor measure with $\exp(\Sigma J(\xi-$xj$) \cos(\phii-\phij)) (11.3)$ is RP; every cylindrical infinite-volume Gibbs limit is RP | Thm 11.3, (11.2)–(11.6) | THM (finite + existing Gibbs limits); Lean counterpart `TorusModel.rotor_gram_kernel_posSemidef` (App. F) |
| 11.8 | **Corollary 11.4:** local Gaussian-bath realisation — integrating out baths gives Thm 11.3 with $J = \Sigma$ gb${}^{2}$ Gmb, $d\rho = \Sigma$ gb${}^{2} \delta(m^{2}-$mb${}^{2}) (11.7)$–(11.9) | Cor. 11.4 | THM; Lean `TorusModel.FiniteCompletion.bath_memory_eq_gram` |
| 11.9 | **Theorem 11.5:** infinite-volume RP for explicit Wilson–Higgs representative — SU$(2)\timesU(1)$ Wilson–Higgs, non-negative couplings, $\lambda > 0$: every finite periodic volume RP; an infinite-volume locally weak subsequential Gibbs limit exists and every such limit from RP-compatible volumes is RP (bound (11.10)–(11.11)) | Thm 11.5 | THM (subsequential limit; existence, not uniqueness) |
| 11.10 | Scope: Prop. 11.2 + Thm 11.3 cover declared finite source, finite Gaussian/Haar comparison source, fixed-cutoff Wilson–Higgs subsequential states, marked-Poisson rotor branch. They do **NOT** cover unrestricted hard Poisson/Rips source or arbitrary cutoff gauge complex (explicit negative crossing direction; oscillator construction gives Gram memory kernel but not 4-D operator $-$∆ or RP-compatible gauge cellulation). Hypothesis 4 retains literal-source pull-back and continuum cutoff; singular-pair no-go proved in §12.3 | §11 end | COND/OPEN boundary statement |
| 11.11 | Finite blocking: RP measure + reflection-equivariant positive-half-space-preserving block map B gives $\langle\ThetaF F\rangle$_{B∗µ} $\geq 0$; local radial map Hx ↦ |Hx| same property. These concern the declared finite bosonic measure; do NOT identify it with unrestricted Poisson source or establish continuum tightness | §11 end | THM (finite) + explicit non-transfer warning |

### §12 Conditions and dependencies (~5100–5648)

| ID | Claim | §/Eq. | Paper status |
|---|---|---|---|
| 12.1 | Table 4: per-stage "conclusion established" vs "additional premise". Microscopic source $\to$ sectors: proved. Sectors $\to$ spacetime: finite lattice model + Euclidean average proved; Lorentz reconstruction needs Hypothesis 4 + reconstruction regularity (physical model + fermions). Spacetime $\to$ gravity: invariance + no mass proved; Einstein–Hilbert form conditional on local derivative expansion, uses Lovelock, sign evaluated numerically; needs Axiom M. Gravity $\to$ gauge/matter: proved + Lean; generations = vacuum data (Rem. 6.14). Gauge/matter $\to$ electromagnetism: Maxwell form + Gauss-law core proved (Lean); Villain computer-assisted; continuous Wilson conditional on one constant; Poisson Gaussian conditional on homogenisation hypotheses; needs Hypothesis 1. EM $\to$ electroweak: partial breaking proved (Lean); perturbative gap proved as formal power series; needs Hypothesis 2. Electroweak $\to$ strong: SU(3)c + asymptotic freedom proved; needs Hypothesis 3 | Table 4, p.95–96 | COND — the table is the paper's own dependency ledger |
| 12.2 | Published theorems are external inputs; comparison-model results reach the physical source only through explicit transfer; declared data are inputs, not predictions. Application conditions for Reisz, Prokhorov–Kolmogorov, OS, percolation estimates, Lovelock in App. D.1. Hypotheses 1 and 4 remain the photon and RP transfers; $\beta = 1$ and vacuum data are declared inputs | §12 intro | Methodological statement (agreed) |
| 12.3 | Table 5 (Yang–Mills dependencies): (i) non-perturbative SU(3) mass gap — **open external theorem**; (ii) source–Wilson universality — **open source-specific bridge**; (iii) Wilson intermediate-window cross-link covariance/transfer-gap estimate — **open**; (iv) qualitative one-loop universality — external input to the chain; (v) optional area law — optional stronger claim, logically distinct from mass gap | Table 5, p.97 | OPEN (i)–(iii); external input (iv) |
| 12.4 | Physical strong-sector mass gap is conditional on source–Wilson bridge + valid non-perturbative gap theorem in target universality class. Glueball masses, finite pure-glue correlation length, non-perturbative $\Lambda$QCD, hadron spectrum **cannot be presented as unconditional outputs**. Area law/confinement needs optional area-law input; mass gap alone does not imply area law. These consequences are not used to derive spacetime/gravity/gauge-algebra/matter/EM/electroweak structural results | §12.2 | COND/OPEN boundary |
| 12.5 | Wilson-photon transfer, electroweak polymer norm, physical RP problem use related multiscale/factorisation tools but none is a consequence of a YM mass-gap theorem; conversely finite gauge algebra, beta-function coefficient, anomaly cancellation, partial EW breaking, comparison-model Maxwell results do not use the open YM bridge | §12.2 | Logical-separation claim |
| 12.6 | **Theorem 12.1 (Conditional source-to-continuum theorem):** given measures µ$\Lambda$,a (12.1) on Polish space $E = \prod$ Hloc^${-$sj}$(R^{4}$; Vj) (12.2), with embeddings In, $\Lambdan$ ↑ $R^{4}$, an ↓ 0, IF conditions 1–8 all hold (see (c)-adjacent box below), THEN a subsequence converges weakly to µ, Schwinger functions satisfy E0–E4 hence OS reconstruction applies; retained resolvents converge normally on D; limiting Ward identity holds; limiting 2-, 3-, 4-point distributions have the specified tensor structures. "It proves that implication. It does not assert that the present torus source satisfies the premises." | Thm 12.1, (12.1)–(12.4) | CONDITIONAL THEOREM — implication proved (proof read); premises NOT asserted |
| 12.7 | **The eight conditions (Thm 12.1):** 1. 0 < Zn < $\infty$; action, relation domain, state–field map, reflection, temporal transfer explicit and compatible with In. 2. (µn) Radon Borel probabilities on one fixed Polish space E, tight w.r.t. compact subsets of local Sobolev topology (not merely finite-dimensional projections); uniform $(2+\delta)$ moments for polynomial cylinder observables, one fixed $\delta > 0$. 3. Reflection continuous involution of E; every µn RP; one consistent Schwinger hierarchy obeys uniformly corrected OS bound (E0), full Euclidean covariance (E1), positive-time RP (E2), permutation/fermionic graded symmetry + reality (E3), clustering (E4), bounds strong enough to pass to weak limit. 4. Measurable block maps $\pin+1$,n with $(\pin+1,n)$∗µn = µn+1, $\pik$,$n = \pik$,$m\pim$,n. 5. On fixed complex neighbourhood D of retained spectral region, blocked quadratic operators have analytic block form, Cn$(z)^{-1}$ uniformly bounded on compacts of D, Feshbach corrections Bn∗Cn${}^{-1}$Bn normally convergent. 6. On common dense cylinder domain, projected Ward operators satisfy Wn+1Jn+1,$n -$ Jn+1,nWn = Rn with $\Sigma$‖Rn‖ < $\infty$, finite-scale Ward residual $\to 0$. 7. Retained source-history, coframe, gauge, chiral fields are the same coordinate projections at every scale (not observables of a surrogate measure). 8. Rescaled two-point and amputated three-/four-point distributions converge in $S'$ to specified Maxwell/YM, coframe/Einstein, chiral-matter tensors, with nonzero two-point residues | Thm 12.1, cond. 1–8; Table 6 | Each COND/OPEN as a premise about the source; see Table 6 "missing microscopic statement" column |
| 12.8 | Table 6 missing-statements: microscopic source specification — "one common $S\Lambda$,a, $\nu\Lambda$,a, state–field map and temporal transfer" (open definition); uniform stability/moments — "cutoff- and volume-uniform coercivity and moments"; physical RP — "physical torus cross-reflection factorisation"; same-measure RG push-forward — "same-measure $\Phia$, not a surrogate block"; sector retention/summable complement — "actual $Q\PhiP = 0$ or summable Feshbach tail"; projected Ward identities — "source Ward operator and summable nonlinear remainder"; continuum tightness/equicontinuity — "uniform continuum tightness and equicontinuity"; pole/vertex identification — "common-source pole and vertex limits" | Table 6, p.100 | OPEN (per condition) |
| 12.9 | Internal Ward boundary: for declared finite internal-U(1) rotor completion, zx = $\dot{\phi}x -$ ax and fxb = ax $-$ ab $-$ ṙxb invariant under $\varphix$ ↦ $\varphix+\alphax$, ax ↦ ax+$\dot{\alpha}x$, rxb ↦ rxb+$\alphax-\alphab$; differentiating gives Ward identity + Hessian null; if fine block A invertible, Schur elimination preserves null. **Only** an internal phase/source identity; does NOT supply four coframe generators, refoliation, or nonlinear Einstein Ward algebra | §12.3 | THM (finite internal) + explicit non-transfer |
| 12.10 | Exact same-measure RG definition $(12.5): \Phia\to$ba µ$a = (\pia\to$ba)∗µa, Sba$(Y) = -\log \int e^{-Sa(X)} \nua($dX|Y) + const, exact composition. "Completes the definition$\dots$ but not the identification of the implemented finite rotor/block map with this push-forward or its sector preservation" | (12.5) | DEF (definition completed); identification OPEN |
| 12.11 | Source non-identifiability / no-go boundaries: relation skeleton does not determine Ug, state–field map, measure, interaction coefficients, or source-identical RG block. Attractive independent-Poisson pair branch with $w(r) \geq$ Ar${}^{-2}$ has divergent collision integral $\int_{0}$^$\varepsilon r^{3} e^{A/r}$ dr — cannot be simultaneously finite and supply desired RP kernel. Adding any local invariant quartic $\lambda\Sigma$ Ix${}^{4}$ preserves tested finite symmetry/positivity criteria while changing higher vertices, so those criteria do not select nonlinear Einstein/YM couplings | §12.3 | THM (no-go, scope-restricted) |
| 12.12 | RP measure-class boundary: hopping cross-kernel has positive character expansion and can be RP, but associated Laplacian/annealed branch fails finite-normalisation test in same independent-Poisson class. Fixed-count or naive hard-core repairs change the point measure, do not preserve original source. Scope-restricted no-go, not a no-go for every torus measure | §12.3 | THM (scope-restricted no-go) |
| 12.13 | **Theorem 12.2 (Composite non-identifiability of unrestricted raw data):** if Sraw = only torus relations + displayed amplitudes, phases, bath labels, symbols $\rho$, $\tau$, g, Ug, with no probability law, reflection, blocking map, state-dependent coframe covariance, link measure or chiral module, then no function of Sraw alone uniquely determines sign of RP, dynamical metric rank, non-Abelian gauge algebra, or chiral matter content. In particular Sraw ⇏ (µ∗, $\Theta, \Phi$RG, Wyx, K[X], Fchiral, H) (12.6). Proof by four completion pairs: (a) measure/reflection — Gaussian boundary variables with $C\eta$, $\eta = \pm1/2 (12.7)$–(12.8), opposite RP signs; (b) metric — mixed Hessian rank 0 vs 10; (c) gauge — line fibre commutant C (U(1)) vs C[S4] commutant $C \oplus C \oplus M2(C) \oplus M3(C) \oplus M3(C) (12.9)$; (d) matter — no Grassmann generators vs anomaly-free bimodule + two Higgs doublets + Yukawas | Thm 12.2, (12.6)–(12.9) | THM (proved by explicit pairs; finite completions distributed with reproducibility package) |
| 12.14 | Explicit transport witness: two completions with same relation skeleton + determinant cocycle but different edge Hessians Qxy^(0) vs Qxy^(1) (12.10)–(12.12) whenever FyFx${}^{-1} \neq I$; adding $\lambda$‖$\psix$‖${}^{4}$, $\lambda \geq 0$, gives further inequivalent vertices (fourth derivative changes by $24\lambda)$ | (12.10)–(12.12) | THM (counterexample to uniqueness) |
| 12.15 | §12.4 scope of finite completion: signed two-scale D4 compensator removes cubic leakage of raw constraint symbol, gives rank-five Fierz–Pauli branch at low momentum; direct temporal-RP route and unrestricted cutoff-scale branch fail. Surviving object is spatial/auxiliary Schur constraint $\otimes$ separately specified positive temporal kernel | §12.4 | THM (finite) + failure of two routes |
| 12.16 | Declared finite source rule: finite inverse-symmetric path semigroup + seven-point RP clock; product gives 49 one-step history–clock marks; history multiplication generates separate 24-state S4 fibre (App. E §E.2). Clock factor is declared completion data, NOT derived from D4 roots. Unrestricted positive GL${}^{+}_{2}(Q)$ soft tail has divergent unipotent subfamily — pullback cannot be identified with finite law without new quotient/regulator/summability domain. Finite rule leaves critical zero mode; local nonzero modes summable; global scale, modular, Maxwell-holonomy, coframe-moduli modes need explicit quotient/normalisation data | §12.4 | DEF + OPEN (identification) |
| 12.17 | Finite constructions proved under stated assumptions: site-dependent $U(3)\timesU(2)$ commutant links + plaquette trace; Maxwell symbol with exact Ward null + three transverse poles; $M3\timesM2$ bimodule with anomaly cancellation + nonzero Higgs/Yukawa intertwiners; coercive finite action $\to$ volume-normalised vertex bound + summable history remainder; Gaussian state–metric completion $\to$ rank-ten metric response. **None is source-native:** literal source still contains no state-dependent G(X), quartic vertex data, fermionic/chiral selector, site-link measure, or plaquette coupling. Quadratic pole data do not identify higher vertices; finite gauge/matter modules do not prove production by microscopic source | §12.4 | THM (finite) + explicit non-derivation |

### §13 The canonical finite model (~5649–6257)

| ID | Claim | §/Eq. | Paper status |
|---|---|---|---|
| 13.1 | Canonical finite model (§3.6) consists of four parts: (i) Axioms I, D, M; (ii) adopted level-3 Hecke relation domain — determinant-one correspondences give A4 cusp action, determinant-two extend it to S4; (iii) declared finite D4 source (Def. 3.7); (iv) declared bounded-geometry completion package Cfin (App. E §E.1, Prop. E.1): finite selector + measure, reflection, blocking family, metric/current rule, chiral module | §13.1 | DEF |
| 13.2 | Hecke domain is the arithmetic relation domain; it does NOT identify the S4 history action with the separately declared D4 colour/source structure. Declaring Cfin makes the finite model definite but does NOT derive that package from unrestricted torus data. Literal Poisson–torus interpretation must still satisfy four requirements of Thm 3.12 (summable relation domain, reversible measure, ordered-history transport, uniform tail control) + eight continuum conditions of Thm 12.1 | §13.1 | DEF + OPEN |
| 13.3 | Assumption bookkeeping: algebraic main line (§4–§10) uses Axioms I, D + finite D4 source; measure-dependent finite statements also use relevant part of Cfin; dynamical gravity (§5.3) uses Axiom M too; unrestricted-source/continuum statements need the four source-completion requirements + eight continuum conditions. Dropping Axiom M gives minimal model (§2): metric fixed background, not dynamical | §13.1 | Methodological |
| 13.4 | Representatives (Table 7, Fig. 24–25): minimal model (Axiom M removed; no dynamical gravity, Prop. 5.7); source-measure completion proposal (determinant-n Hecke domain + hyperbolic measure on modular surface; candidate for requirement (i); requirement (ii) + D4 link open, Prop. 13.2); admissible-completion family (conditions A of Table 8 + preservation of Cfin; a family, not known to be a single point); factorised control model (admissible family + spectator metric sector $S_{fixed}$^$(m) + S_{H}, m^{2} > 0$, no matter coupling; reproduces minimal-model sector exactly; free parameter $m^{2})$; projected coupled model (admissible family + constraint coupling CQ = $\sqrt{\kappa}$ QC${}_{0}$ with reducing physical projection $\kappa, P\SigmaQ = \Sigma$QP = 0, $\SigmaQ$ = CQ${}^{-1}H$ᵀHCQ; working representative for gravity; P, Q, renormalisation declared rather than source-derived); finite certification lattice (one explicit finite lattice/selector/action/push-forward RG inside projected coupled model; 49 one-step marks generate separate 24-state S4 fibre; reverse-engineered, not a derivation from source); observationally constrained specialisation (canonical content + vacuum family + gravity–gauge bridge, free moduli constrained by observable set fixed in advance + declared Yukawa-amplitude rule; completely analysed only for declared leading-order rules, not source-selected) | §13.2, Table 7 | DEF per branch; each branch's conclusions attributed to smallest branch proving them |
| 13.5 | Admissibility conditions A (Table 8) — seven tests, not axioms: inverse closure; normalisation; reflection positivity $(C+-$ = LLᵀ, Prop. 11.2); coercivity + moments (uniform $(2+\delta))$; coarse-history retention (right-S4 equivariance Prop. 6.2; summable Feshbach complement, req. (iv)); coframe + gauge retention (metric rank 10; gauge links carry $M3\oplusM2)$; Ward/pole/anomaly/Yukawa consistency (projected Ward identity with summable remainder; massless photon pole; anomaly-free chiral module with required Yukawa invariants). Distinct from the eight source-to-continuum conditions (single finite candidate vs family + continuum limit). Finite certification lattice passes all seven at its lattice size. Source-measure proposal addresses inverse closure + normalisation at source level; not a finite candidate. Observational restriction is not an admissibility condition and supplies no missing source-to-continuum implication | §13.3, Table 8 | DEF (tests) |
| 13.6 | **Proposition 13.1 (Common physical block):** with P = diag(1,1,0,0), Hfixed positive definite, P reducing (P Hfixed Q = Q Hfixed P = 0, P Hfixed${}^{-1} P = P (13.1))$, eliminated metric block positive definite, $\SigmaQ$ = CQ${}^{-1}H$ᵀHCQ ⪰ 0, $P\SigmaQ = \Sigma$QP = 0 (13.2), then P Hfixed${}^{-1} P = P$ Hfact${}^{-1} P = P$ Hproj${}^{-1} P = P (13.3)$ — physical pole, residue, quadratic observables agree across minimal / factorised-control / projected-coupled models in the finite realisation. Weaker $P\Sigma$QP = 0 alone would NOT suffice. "Finite statement. It does not prove that the infrared limits of the representatives coincide" | Prop. 13.1, (13.1)–(13.3) | THM (finite); Lean `TorusModel.common_ir_physical_block_diagonal` |
| 13.7 | **Proposition 13.2 (Hecke cosets and D4 moves):** (a) no bijection between 24 D4 moves and determinant-2 Hecke cosets: $\sigma_{1}(2) = 3$ of the latter. (b) GL${}_{2}(Z)$ acts on det-2 cosets through GL${}_{2}(F_{2}) \cong S_{3}$; V4 only normal subgroup of order 4 in S4, so $S4 \to S_{3}$ unique up to relabelling; only S4 irreps trivial on V4 realisable (trivial, sign, 2-dim); colour blocks 3 and $3'$ cannot be realised. (c) On four det-3 cosets $(= P^{1}(F_{3})$, four cusps) GL${}_{2}(Z)$ acts through PGL${}_{2}(F_{3}) \cong S_{4}$, SL${}_{2}(Z)$ only through PSL${}_{2}(F_{3}) \cong A_{4}$; $C[P^{1}(F_{3})] = 1 \oplus 3$ for $A_{4}$ and $S_{4}$, commuting unitary group $U(1)\timesU(1)$; block-preserving group $U(1)\timesU(3)$ is different; $U(1)^{3}\timesU(3)$ is commutant of regular $A_{4}$ representation, not of four-cusp module. Det-2 Hecke correspondence (3 cosets) is not a replacement for 24 D4 moves; but det 2 is a nonsquare mod 3, so adjoining det-2 correspondences to det-1 level-3 action enlarges PSL${}_{2}(F_{3}) \cong A_{4}$ to PGL${}_{2}(F_{3}) \cong S_{4}$. Hecke supplies finite S4 monodromy; D4 root source remains separately declared colour/source structure | Prop. 13.2 | THM; Lean `TorusModel.hecke_projective_line_counts` |
| 13.8 | **Proposition 13.3 (Gravitational normalisation in projected coupled model):** in canonical finite completion Newton's constant induced by node fields: $G \propto [\varepsilon^{-2}(R/\varepsilon)^{6} \Sigma \chii]^{-1}$, so $d \ln G/d \ln \chi$node = $-1 ($origin of G dipole). In projected coupled model metric-sector strength set by $\kappa$: if $\kappa$ is the induced coefficient, dipole ratio + entropy ratio R = 1.05 are those of canonical finite completion; if $\kappa$ is a constant fixed by matching G to observed value, $d \ln G/d \ln \chi$node = 0 and G dipole disappears. Projected coupled model usable for gravity calculations without loss only with $\kappa$ = induced coefficient; constant $\kappa$ changes a prediction of canonical finite completion | Prop. 13.3 | THM (conditional on $\kappa$ choice); Lean `TorusModel.induced_newton_log_sensitivity` |
| 13.9 | **Numerical result 13.4 (Shape sensitivity of V1 reference point):** for eight copies of vacuum V1 (internal shapes $\chi = (2.5, 5, 3.2)$ up to exchange of first two tori), ki = $d \ln \alpha/d \ln \chii = -0.593$, $-0.349$, $-0.961$; $\alpha^{-1} = \alpha_{2}^{-1} + \alphaY^{-1}$ at matching scale, $\alphax^{-1} \propto$ Vx. Dipole ratio (∆G/G)/(∆$\alpha/\alpha) = -1/k = 1.69$, 2.86, 1.04 depending on which internal torus is node torus. Range 1.4–3.3 quoted earlier refers to bridge vacua with natural matter content. Varying one shape over |$\ln(\chi/\chiV1)$| $\leq 2$ with uniform weight in $\ln \chi ($hyperbolic measure along shape line), fraction of line with |k| < 0.1 is 0.04, 0.12, 0 for the three tori. k does not vanish at self-dual point $\chi = 1 ($couplings of vacuum with fixed winding numbers not invariant under SL${}_{2}(Z))$. Positions in data space are marked tori; state measure on modular surface must be lifted to cover where winding data are defined | Num. Res. 13.4 | NUM |
| 13.10 | Torus-to-continuum problem (Table 9, Fig. 26): source $\to$ completion — literal kernel does not define one (Thm 3.12); source-measure proposal candidate for req. (i); req. (ii) unchecked; D4 link not automatic (Prop. 13.2). Completion $\to$ finite representative — projected coupled model + finite certification lattice pass all seven admissibility conditions at finite size, but are not derived from a completion (selector, P, Q, $\kappa$ chosen). Finite representative $\to$ push-forward RG — exact on finite certification lattice for conditions 1, 4, 5 at finite size. Push-forward RG $\to$ continuum — conditions 2, 3, 6, 7 uniformly in volume/cutoff OPEN; condition 8 checked at finite size only. "First open step is the identification of the source measure, transport and renormalisation map. It is a missing definition, not a missing finite calculation." | §13.6, Table 9 | OPEN (definition missing) |
| 13.11 | **§13.7 Observationally constrained specialisation** — see (c) below for full detail. Headline: retains axioms, field content, vacuum family, gravity–gauge bridge; constrains otherwise undetermined moduli by fixed observation set; additional inputs = measured gauge couplings, declared running prescription, Higgs-stability boundary condition, declared Yukawa amplitude rule (for masses). Before every fit: number of free parameters, observable list, objective, pass threshold, parameter domain fixed in advance; no parameter/observable added after inspecting result. "For these declared leading-order rules the analysis is complete: every resulting output, and every sector in which the rules fail, is given." Selected point fixed by data, not derived from source. Retained outputs: exact matching of three gauge couplings; selection of one matching class by gravity–gauge relation with model's own field content; conditional top-mass bound; charged-lepton mass ratios under declared amplitude rule; axion dark matter for uniform initial angle declared as initial data. NOT reproduced: quark masses/mixing, lepton mixing, neutrino masses, $\sin^{2}\thetaW$, electroweak scale v, $\Lambda$ — outside present predictive scope (§14). Numerical values in §16.5 | §13.7 | COND (input-dependent benchmarks); analysis-complete claim for declared leading-order rules |

### §14 Scope and relation to existing theories (6258–~6500)

| ID | Claim | § | Paper status |
|---|---|---|---|
| 14.1 | Table 10 (domains explained + supplying branch): spacetime — dimension 4, one time axis/arrow, lattice signature (1,3), Euclidean invariance of Poisson average; Lorentz reconstruction conditional, needs Hypothesis 4 (canonical finite model + physical reconstruction). Gravity — conditional two-derivative Einstein tensor form, no local graviton mass vertex, GR light-bending tensor ratio, $\Lambda$ as integration constant (canonical finite model; needs Axiom M + low-energy derivative expansion). Gauge forces — gauge group, partial EW breaking, asymptotic freedom; Maxwell in comparison models (Hypothesis 1 for physical Wilson field). Matter — chirality, charge quantisation in units of 1/6, anomaly freedom, no extra massless U(1) (canonical conditional bimodule; finite realisation). Cosmology — Friedmann expansion under dynamical-metric assumptions; redshift kinematical; singularity bounce as numerical illustration. Black holes — entropy A/4G under cited common spectral regularisation; Page curve as finite numerical illustration. Dark sector — $\Lambda$ as unfixed integration constant; QCD axion, all of dark matter only if uniform initial angle declared (observationally constrained specialisation; conditional candidates) | Table 10, §14.1 | COND per row (branch + hypothesis as stated) |
| 14.2 | Minimal model: background metric static, node scale fixed $\to$ no redshift; cosmological time-evolution statements use standard expansion as external input there. In canonical finite model they follow from Thm 5.13 (sky-dipole distance, early-universe list, axion abundance, DESI comparison). Static statements valid in minimal model as they stand: $\alpha$–curvature relation, ratio $G/\alpha$, $\Lambda$ as integration constant, identity of dark-matter candidate | §14.1 | COND (model-dependent) |
| 14.3 | Table 12 (quantities PROVED not fixed by axioms): couplings/masses/mixings — continuous moduli + amplitude prescription remain free (Thm 6.17); model gives rule-dependent ranks + conditional observational restrictions (§13.7). Cosmological constant — integration constant [19] in canonical finite model; constant shift of matter Lagrangian drops out of traceless equation; value + radiative stability NOT derived. Neutrino masses/mixing — circulant Yukawas share eigenvectors $\to$ leading-order mixing is a permutation; amplitude rule leaves masses free; Dirac sector with declared matter content; no mass/mixing prediction. Smallness of $m\nu$ — neutrinos + charged leptons share one Yukawa mechanism; suppression depends on moduli/brane separations; no Majorana mass term with declared matter content, hence $m\beta\beta = 0$. Predictive coupling unification — four unknowns = four data (Prop. 6.18); consistent matching vacua exist; no extra massless U(1). Scale hierarchies — values of moduli/brane separations; naturalness is not a consistency condition | Table 12, §14.2 | THM (proved non-fixing = "proved boundary") |
| 14.4 | "A proved boundary is a quantity for which there exist several solutions satisfying every condition of the axioms and the source, with different values. Such a value cannot be computed from the model. Fixing it would need a new principle." | §14.2 | DEF (of proved boundary) |
| 14.5 | KK-scale thresholds $(~10^{17}$ GeV) experimentally inaccessible (independent verification). Amplitude of primordial perturbations NOT derived; since not every mechanism excluded, it is an open external input rather than a proved boundary | §14.2 | OPEN (external input) |
| 14.6 | Cosmology/dark sector (§14.3): dark energy — remaining candidate is cosmological constant (unimodular integration constant), no new field; value is initial data. "Everpresent-$\Lambda$" mechanism excluded independently of amplitude within tested model (App. C). Rolling node-shape moduli incompatible with stated bounds: node shape sets $\alpha (k = d \ln \alpha/d \ln \chi = 0.25$–0.96), so $w = -0.9$ would give |$\dot{\alpha}/\alpha$| $\sim 10^{-11}$ yr${}^{-1}$, $10^{6}$–$10^{7}$ times atomic-clock bounds $(~10^{-18}$ yr${}^{-1})$. Dynamical-metric candidate has $w = -1$. Minimal model has no cosmological evolution of its own, does not predict w | §14.3 | COND (exclusion claims) |
| 14.7 | Dark matter: axion-bearing classes supply QCD axion; in selected matching class it is all of dark matter IF uniform initial misalignment angle $\thetai \approx 1.6\times10^{-3}$ declared as initial data; angle NOT derived. Domain-wall restrictions + absent-axion alternative in §16.5. No additional component constructed. For stated thermal history, rotor mode + Dirac $\nuR$ make negligible thermal contribution | §14.3 | COND (on declared angle) |
| 14.8 | Curvature–coupling covariance: node torus shape is position, so couplings vary with position. Per Hubble radius, ∆$\alpha/\alpha \approx k\sqrt$|$\Omegak$|, (∆G/G)/(∆$\alpha/\alpha) = 1.4$–3.3, same sign. Bound |∆$\alpha/\alpha$| < $10^{-6}$ implies |$\Omegak$| < $3\times10^{-12}$. In canonical finite model spatial metric belongs to family of invariant metrics on data space (uniqueness of invariant metrics); relation holds with corrections $O(\sigma/H) + O(\delta)$, shear $\sigma/H \approx 0.69 \Omegak$ from Bianchi III integration, $\delta \sim 10^{-5}$ — far below observational precision | §14.3 | COND |
| 14.9 | Table 13 (early universe without inflation): arrow of time — source drift orients time axis, proved (Thm 4.3). Flatness — |$\Omegak$| < $3\times10^{-12}$ from $\alpha$ bound + covariance; curvature scale is initial data. Cosmological constant — unimodular integration constant, conditional on Axiom M + low-energy derivative expansion; value not predicted. Dark-matter amount — set by initial axion angle in selected matching class (§16.5), initial data. Primordial perturbations — Poisson count fluctuations $\sim10^{-120}$ on cosmological scales; three internal seeds excluded (§15); OPEN. Primordial gravitational waves, horizon, baryon asymmetry — not addressed, OPEN | Table 13 | Mixed: proved (arrow), conditional, open |
| 14.10 | §14.4 GUT/proton decay: no grand-unified gauge bosons in model (gauge algebra not enlarged; no X, Y generators/fields); M∗ is only scale where three low-energy couplings meet. "No proton decay" is a structural prediction conditional on this absence + on not adding independent baryon-number-violating effective operators. Coupling matching alone does not imply existence of GUT gauge bosons | §14.4 | COND (structural prediction) |
| 14.11 | Table 14 (relation to existing theories): Standard Model — reproduced in declared finite construction (low-energy gauge group after heavy U(1) combinations removed; three generations in every catalogue vacuum imposed as selection condition, §16; Higgs stabiliser $\rho = 1$; adds second Higgs doublet in fixed V1 benchmark + axion in axion-bearing classes; explains finite group, representations, charge quantisation, but neither unrestricted source transfer nor parameter values). General relativity — recovered conditionally as unique two-derivative low-energy tensor form (Lovelock), unimodular version; constant matter-vacuum shifts drop out of traceless equation; effective $\Lambda$ value + radiative stability not derived; metric dynamical only with Axiom M. $\Lambda$CDM — constant $w = -1$ under stated unimodular interpretation; axion conditional candidate, total abundance/history still restricted. GUT — couplings meet at M∗, but at internal KK scale, no GUT gauge bosons, hence no gauge-mediated proton decay (§14.4). String theory (intersecting branes) — matter sector same mathematical form (bifundamentals, intersection numbers, Green–Schwarz couplings); difference is origin: internal data are node data, spacetime is counted. Causal sets — shares Poisson sprinkling + count = volume; difference: physical observables are configuration averages, removing the swerves problem. Induced gravity (Sakharov) — G induced by node fields; gravity–gauge bridge fixes cutoff at $\approx 18 \ellP$. Lattice gauge theory — open problems (Hypotheses 1–3) are problems of constructive lattice gauge theory | Table 14, §14.5 | COND per row |
| 14.12 | **Relation to other emergent-spacetime / D4-based approaches (task (e)):** §14.5 and §18.2 discuss prior *torus* frameworks, NOT a D4-based emergent-spacetime competitor by name. No other D4-based approach is cited or compared in this range. The paper's own D4 structure is presented as distinct from: noncommutative tori/spectral geometry [75, 76]; Matrix compactifications / finite torus approximants [77, 78]; toroidal compactification in string/brane models [27]; string-net condensation [79] and graph-based emergence / quantum graphity [80]; Connes–Marcolli Q-lattice theory [2, 81] (the paper's commensurability/Hecke vocabulary originates there, but Q-lattice KMS phase structure, Shimura-variety identification, Galois action are NOT imported or asserted); spectral-action gravity–SM construction [7]; Ascárate's toroidal quantum-gravity proposal (2026) [82] (noncommutative tori + spectral triples + discrete holonomy + causal ordering + Markov/percolation dynamics — "neither Ascárate's spectral triple nor its dynamics is constructed or imported, and no result established in one framework is used as a proof in the other"); toroidal CDT [83, 84]. Claim: "what is new is their combination under the declared axioms into a single conditional chain from torus-node data to a 3+1-dimensional spacetime with gravity, gauge fields and chiral matter." No new general theory of Q-lattices or noncommutative tori proposed; no spectral-action derivation given | §14.5, §18.2 | Comparative claims (paper's own characterisation of prior work; NOT independently verified by this reader) |

### §15 Predictions that differ from existing models (~6500–6613)

Table 15 — each row is a qualitative prediction + falsification criterion (Fig. 28: structural
differences without a discriminator are not counted as predictions):

| ID | Model prediction | Compared with | Falsified by |
|---|---|---|---|
| 15.1 | No proton decay, despite coupling matching at M∗ | GUT: $\taup \sim 10^{34}$–$10^{36}$ yr | Proton decay at Hyper-Kamiokande or DUNE |
| 15.2 | Dirac neutrinos, $m\beta\beta = 0 ($declared matter content: no Majorana mass term) | Seesaw: Majorana | Discovery of $0\nu\beta\beta$ |
| 15.3 | $\Lambda$ exactly constant $(w = -1)$; moduli dark energy excluded by atomic clocks | Quintessence; DESI hint of evolving dark energy | $5\sigma$ evolving dark energy $(w_{0} > -1$, wa < 0) |
| 15.4 | No WIMP, no hidden sector, ∆Neff $\approx 0$; QCD axion is all of dark matter if uniform initial angle declared | WIMPs, hidden sectors | WIMP discovery; excess ∆Neff |
| 15.5 | Equal light speed for all species when every coupling depends on same Poisson distance (Thm 4.11); no averaged Lorentz violation | Some quantum-gravity models: species- or energy-dependent c | Species-dependent light speed; deterministic quartic dispersion |
| 15.6 | No extra massless U(1), no hidden glueballs | Hidden-sector models | A new long-range force; a hidden strongly coupled sector |
| 15.7 | $\alpha$, G and spatial curvature tied to one variable (node shape) | Independent constants | Variation of $\alpha$ without matching variation of G, or with opposite sign |
| 15.8 | No inflation; primordial amplitude needs an outside seed at $\sim10^{16}$ GeV | Inflation | "(not decisive while the seed is open)" — paper's own caveat |
| 15.9 | **Cosmology without inflation — three internal seeds EXCLUDED:** (i) Thermal winding gas (Brandenberger–Vafa type [56]): windings on internal torus $\to$ heat capacity CV $\propto R^{3}$, spectral tilt ns $- 1 = -1$. (ii) Matter bounce at node density [57–60]: contracting phase $w \approx -0.0029$ would give ns = 0.9649; exact mode functions give r = 24cs, so r < 0.036 needs cs < $1.5\times10^{-3}$; amplitude As $\approx ($HB/MP$)^{2}/(12\pi^{2}$cs$) = 2.1\times10^{-9}$ needs HB $\approx 10^{12}$–$5\times10^{13}$ GeV; but integer-volume bounce occurs at node density, HB $\sim 7\times10^{16}$–$2\times10^{17}$ GeV, giving As six to seven orders of magnitude too large. (iii) Node-scale thermal seed with area-law heat capacity: gives $P \geq (\ellP/\varepsilon)^{4} = 9.5\times10^{-6}$, at least $5\times10^{3}$ times too large. Single-clock seed needs $V^{1/4} \approx 6\times10^{15}$–$1.4\times10^{16}$ GeV, matching neither cutoff $\Lambda = 6.8\times10^{17}$ GeV nor fixed-reference matching scale M∗ = $1.6\times10^{10}$ GeV. In selected matching class under heavy-threshold option, M∗ $\approx 5.8\times10^{16}$ GeV lies within factor ~4 of this range, but no mechanism links seed to M∗. Primordial amplitude therefore an external input | §15 | Exclusion claims (conditional on the stated seed models); amplitude OPEN |

### §16 Numerical benchmarks and conditional phenomenology (6614–6938)

| ID | Claim | §/Eq. | Paper status |
|---|---|---|---|
| 16.1 | Finite vacuum catalogue: 76 copies, 16 distinct outputs, at fixed reference moduli; exhaustive finite enumeration; stability column refers only to those fixed points, not all continuous matching solutions. V1 = fixed-reference benchmark vacuum; V11 = catalogue row whose matching class is selected by gravity–gauge relation. M∗ = scale where three couplings meet (interpreted as internal KK scale, no GUT gauge bosons); $\alpha$∗ = common coupling there $(1/\alpha$∗ is a wrapped-cycle volume); fa = M∗. Residual two-loop matching error $\delta$th = 0.7–1.9% is required KK threshold correction (∆$(1/\alpha) \approx 0.3$–0.8, natural size). Last column = Higgs-stability verdict (Prop. 9.19) | §16.1, Fig. 29 | NUM (exact enumeration + input-dependent estimates) |
| 16.2 | Table 16 (16 distinct vacua) — see quantitative list (g). Headlines: V1 (8 copies) M∗ = $1.59\times10^{10}$ GeV, $1/\alpha$∗ = 38.95, ranks 2/2/1/1, E/N = 2/3, ma = 358 µeV, NDW 2 or 1, stability pass. V11 (4 copies) M∗ = $3.43\times10^{14}$ GeV, $1/\alpha$∗ = 43.92, ranks 3/3/3/3, E/N = 4/3, ma = 0.017 µeV, NDW 3, stability fail (at fixed reference point). V13–V16 M∗ = 1.6–$9.3\times10^{15}$ GeV, ma = 0.0006–0.0036 µeV, fail | Table 16 | NUM (fixed-reference values) |
| 16.3 | Calculation order (§16.2): (1) finite catalogue — intersection numbers Ixy = $\prod_{i} ($nix miy $-$ mix niy) (16.1), tadpole/anomaly sums, Green–Schwarz matrix, allowed Yukawas; integer calculations; reject exotics, retain three-generation spectra, quotient only by stated relabellings $\to 76$ copies / 16 rows, exhaustive finite enumeration, not Monte Carlo. (2) Couplings/scale — wrapped volumes Vx$(\chi)$, $\alphax^{-1} = \kappaA(\LambdaR)^{3}$Vx$(\chi) (16.2)$ at matching scale; two-loop running + stated threshold interval applied to three measured gauge couplings; common crossing gives M∗, $\alpha$∗ — outputs of catalogue + declared running/matching inputs, not fitted independently. (3) Ranks/axion — ranks of finite Yukawa/intersection matrices over Q; anomaly sums give E/N; fa = M∗; ma = 5.70 µeV $\times 10^{12}$ GeV/fa (16.3) using external QCD coefficient 5.70(6)(4) of [61] (uncertainties from quark-mass inputs + higher-order corrections); V1 central ma $\simeq 358$ µeV. (4) Neutrinos — no neutrino number tabulated; circulant Yukawas share Fourier eigenvectors $\to$ leading-order mixing is a permutation; neutrino masses/ordering/mixing outside scope (§13.7); external cosmological/oscillation constraints are comparison data, not outputs [62–64]. (5) Higgs stability + $\tan \beta$ — from mh, MW, mt, $\alphas$; three-loop SM beta functions, four-loop QCD, NNLO matching integrated with outward-rounded intervals; boundary condition $\lambda$SM(M∗) = ⅛$(g_{2}^{2}$ + gY${}^{2})\cos^{2}2\beta (16.4)$ imposed; bisection in mt finds largest interval with $\lambda$SM(µ$) \geq 0$ at every step; reported 172.89 GeV bound is endpoint of that interval; $\alphas$ sensitivity + threshold shift by varying those inputs. (6) Geometry/entropy — differentiating wrapped volumes gives $k = d \ln \alpha/d \ln \chi$ and (∆G/G)/(∆$\alpha/\alpha)$; curvature relation ∆$\alpha/\alpha \simeq k\sqrt$|$\Omegak$|; integrating along last-scattering line of sight gives factor 3.1 in $D\alpha$; finite-volume entropy fits give $\kappaS$ at sizes 24–40; with $c_{2} = 1/(16\piG)$, $R = \kappaS/(4\pic_{2})$; spread between two masses + lattice directions is quoted uncertainty — "a consistency check rather than an exact theorem" | §16.2, (16.1)–(16.4) | Method + NUM; exact-integer vs interval-certified vs input-dependent classes distinguished (App. G/H) |
| 16.4 | Leading-order rank suppression exponents of masses vanishing at leading order: ∆Af = ln(mLO/msub): ∆Au = 6.4, ∆Ad = 3.0, ∆Aµ = 2.8, ∆Ae = 5.3, all of natural size. Neutrino suppression not tabulated (neutrino sector makes no prediction) | §16.2 | NUM |
| 16.5 | Table 17 fixed-input benchmarks (V1): mt $\leq 172.89$ GeV $(\alphas = 0.1180; \pm0.32$ GeV per $\pm0.0009)$ — Higgs stability of V1 (Prop. 9.19); SM alone allows any mt; observation now $172.57 \pm 0.29$ GeV: consistent, margin $1.1\sigma$. Axion E/N = 2/3, ma $\approx 358$ µeV, fa = M∗ (V1); ADMX/HAYSTAC cover other masses [65, 66]; 358 µeV in proposed dielectric-haloscope range [67], not an exclusion claim. Second Higgs doublet at $\sim1.6\times10^{10}$ GeV, $\tan \beta \approx 1.0$–1.2 (V1), not directly accessible. M∗ = $1.59\times10^{10}$ GeV, $1/\alpha$∗ = 38.95 (V1), indirect (via ma). (∆G/G)/(∆$\alpha/\alpha) = 1.04$, 1.69 or 2.86 for V1 depending on node torus (1.4–3.3 over natural-content bridge vacua), same sign (Num. Res. 13.4); ∆$\alpha/\alpha \approx k\sqrt$|$\Omegak$|. $\alpha$ sky dipole $D\alpha \approx 3.1k\sqrt$|$\Omegak$| with G dipole same direction (sky-dipole integration); disputed $10^{-5}$ claim [69] would need |$\Omegak$| $\approx 10^{-11}$–$2\times10^{-10}$. Black-hole entropy ratio $R = 1.05 \pm 0.08 ($induced G + horizon entanglement; consistency check). **"The 172.89 GeV endpoint tests the chosen V1 scale and running inputs. It is not a class-independent mass bound: varying the moduli changes M∗ and the stability test."** | Table 17 | NUM (input-dependent); V1-specific, not class-independent |
| 16.6 | Table 18 sky-dipole amplitudes: \|$\Omegak$\| = $3\times10^{-12} ($stated bound$) \to D\alpha = 1.3$–$5.2\times10^{-6}$, G dipole $1.9\times10^{-6}$–$1.7\times10^{-5}$; \|$\Omegak$\| = $10^{-11} \to D\alpha 2.5$–$9.4\times10^{-6}$, G dipole $3.4\times10^{-6}$–$3.1\times10^{-5}$; \|$\Omegak$\| = $10^{-10} \to D\alpha 0.78$–$3.0\times10^{-5}$, G dipole $1.1\times10^{-5}$–$9.8\times10^{-5}$ | Table 18 | NUM (diagnostic) |
| 16.7 | §16.4 conditional cosmological history of V1 benchmark: assumes specified contracting history suppresses wall formation; NOT established throughout observationally constrained specialisation; wall-forming alternative tested in §16.5. Contracting phase before integer-volume bounce keeps axion angle uniform on large scales by causal contact. Light spectator field: spectral index $n\phi - 1 = 3 - 2$\|$\nu$\|, $\nu = 3(1-w)/(2(1+3w))$; for w > 0.068 near bounce angle uniform on QCD horizon scale $(\delta\theta \approx 10^{-12}$ for w = 1/3). Near bounce, radiation/stiff matter dominates dust; dust contraction excluded by amplitude bound. Hence no domain walls form, no instanton-bias alignment needed. Supporting: every O(1)-type cycle of V1 and V2 carries even axion charge; each vacuum has exactly one light closed-string axion; some copies of V1 have NDW = 1. Dark-matter abundance set by single initial angle $\thetai ($initial data); typical angle gives ~4% of dark matter; all of it requires $\pi - \thetai \approx 1.4\times10^{-3}$. Tuning of initial data (naturalness not a consistency condition) | §16.4 | COND (on contracting-history assumption) |
| 16.8 | NOT counted as predictions: number of generations (vacuum data, Rem. 6.14); $\sin^{2}\thetaW$ and $\alpha_{3}/\alpha_{2} ($used as filters for vacuum catalogue); neutrino masses/mixing (not predicted); ratio (MP/$\Lambda)^{2} \approx 322 ($circular) | §16.4 | Explicit exclusions |
| 16.9 | Table 19 — conditional outputs of observationally constrained specialisation (selected class V11 + low-scale alternative); "None of these rows certifies a simultaneous solution of all constraints with interval arithmetic." See (c) for full detail | Table 19, §16.5 | COND |

### §17 Yang–Mills interface and the open mass-gap problem (6939–7391)

| ID | Claim | §/Eq. | Paper status |
|---|---|---|---|
| 17.1 | Mass-gap problem stated: 4-D quantum YM with compact simple gauge group exists as QFT; Hamiltonian has no spectrum in (0, ∆) above vacuum for some ∆ > 0; Euclidean connected correlations of gauge-invariant local observables decay exponentially at rate set by ∆. On lattice, measure well defined; question is whether gap stays positive uniformly in volume and survives continuum limit | §17 intro | Problem statement (external, Clay-type) |
| 17.2 | **Hypothesis 3:** volume-uniform spectral gap of 4-D lattice SU(3) YM at physical bare coupling. Coupling calibration in Prop. 10.2 puts that point near $\beta \simeq 21$; complete argument would have to pass from weak coupling through crossover to confining regime. "No rigorous method for that crossover is known." Estimates/proofs developed in follow-up paper, where most certified constants are obtained for SU(2); mass-gap statement for physical gauge group SU(3) remains open | §17.1, Fig. 30 | HYP — OPEN |
| 17.3 | Torus construction does NOT directly produce a Wilson action at quark-decoupling scale; it produces a positive closed-walk action with large-field bound (Thm 6.10). Source-to-Wilson universality theorem (incl. transfer + RG control) is a separate condition, NOT assumed here. Follow-up paper studies standard Wilson lattice problem (Wilson [1]); Mondal's geometric proposal [10] obtains a mass gap under its own conditions, used here for comparison | §17.2 | OPEN bridge; comparison only |
| 17.4 | Wilson setting (17.1): $S(U) = \Sigma_{p} (1 - N^{-1} \mathrm{Re}$ tr Up), µ$\beta($dU$) \propto e^{-\betaS(U)} \prod$ dUe. SU$(2) \cong S^{3} \subset R^{4} ($unit quaternions), bi-invariant round metric, Ric = 2. Conditional on other links, one link has von Mises–Fisher law µa(du$) \propto e^{\langlea,u\rangle}$du, $a = \beta \times$ sum of six staples, |a| $\leq 6\beta$. Follow-up paper contains strong-coupling proofs, weak-coupling chain, conditional continuum theorem, intermediate-window obstruction; "a technical continuation of this overview, not an additional upstream input to the main torus derivation" | §17.3, (17.1) | DEF (setting) |
| 17.5 | What torus model supplies (§17.4): (i) initial action — integrating out bosonic node matter gives positive closed-walk action $\Gamma[U] = \Sigma_{\omega} c\omega(N - \mathrm{Re}$ tr $U\omega)$, $c\omega \geq 0$, with large-field bound $\Gamma[U] \geq t \Sigma 2$ct$(N - \mathrm{Re}$ tr Ut) (Thm 6.10); plaquette part has positive character coefficients, candidate input for Wilson-type RP + large-field arguments; positivity alone does NOT identify it with Wilson action or prove continuum transfer; bare coupling $\beta = 6/g^{2} \simeq 21.5 ($Prop. 10.2). (ii) Finite colour carrier — colour group is determinant-one subgroup of M3(C) block of history commutant (Thm 6.4); on finite reflected cell complex one can declare SU(3) link variables in this block with Haar measure + Wilson weight $\exp[\beta/3 \Sigma$□ Re tr W□]; covariant matter couples through $\rho\Sigma$‖$\Psiy -$ We$\Psix$‖${}^{2}$; gauge covariance exact; also 18-link retained checkerboard carrier with exactly defined induced retained action. "Declared finite objects, not consequences of the literal source." | §17.4 | THM (finite) + explicit non-identification |
| 17.6 | What transfers from Wilson analysis (§17.4) — three classes, for SU(3) sector: (a) valid for every SU(N): uniqueness + exponential decay for $\beta < (1/2) \log(19/17) ($total-variation Dobrushin with 18 influence neighbours); conditional continuum implication: if transfer operator satisfies qa = $e^{-aM} + o(a)$ with compatible RP + matrix-element convergence, continuum generator has gap $\geq M$. (b) Valid for compact groups with positive Ricci curvature, with changed constants: heat-flow log-Sobolev criterion, exact identities for renormalised potential, pinned Poincaré Riccati bound, structure of pinned joint measure; for SU(3), Ric = (1/4) Killing > 0. (c) Specific to SU(2) — must be recomputed for SU(3): Haar-point constant $8/(9\pi)$, certified gap for $\beta < 0.24$, area-law certificate for $\beta \leq 0.3925$, weak-coupling threshold $\betaw ($value in follow-up paper). "No SU(2) theorem or numerical constant in that paper is an SU(3) mass-gap result; the SU(3) constants must be recomputed." | §17.4 | (a)(b) transferable classes; (c) SU(2)-only, OPEN for SU(3) |
| 17.7 | Confinement (§17.4–17.5): long-distance force between quarks needs an area law, which the mass gap does NOT supply. **Theorem 17.1 (Confinement from vortex condition):** assume (VF) — $\exists c$, $\rho > 0$, integer p0 such that for every coordinate plane (µ,$\nu)$, every box with sides divisible by $2^{p}0$, $k = 1,2: 0 \leq 1 - Z[k]/Z \leq c$|$\Lambda$|$e^{-\rhoLµL\nu} (17.2)$, where Z[k] is twisted partition function (plaquettes of twist stack Υ carry $z^{k}, z = e^{2\pii/3})$, Wilson weight $\exp[(\beta/3)\Sigmap \mathrm{Re}$ tr Up] at $\beta = 21.49$. Then for every rectangular loop C in a coordinate plane with enclosed area AC: |$\langleW(C)\rangle$| $\leq 2e^{-\rhoAC} (17.3)$ in infinite-volume limit; static potential $V(r) \geq \rhor$, string tension $\geq \rho$. Proof via Tomboulis–Yaffe inequality in SU(N) form of Kanazawa [72, 74] (17.4)–(17.5). Derivation in App. D.5.3 | Thm 17.1, (17.2)–(17.5) | CONDITIONAL THEOREM (on (VF)); (VF) itself OPEN at physical coupling |
| 17.8 | Route to (VF): block-spin flow. Flow condition (RG$) (17.6): \exists$ integers m, $n \geq 1$, block factor $b = 2^{m}$, constants $\varepsilon$, a > 0 such that for every box with sides divisible by $b^{n}$, k = 0,1,2, weight after n block steps has polymer representation $e^{-Sn^(k)(U)} = \Sigma \rho\Xi$^(k)(U) with block-local bounds |$\rhoX$^(k)(U)| $\leq \prod$ hX,B^(k)(U), sup hX,B^$(0) \leq \varepsilon^{|X\capB|}$, $\varepsilon$ small enough for Kotecký–Preiss with weight $e^{2a|X|} [47]$. "(RG) is the statement that the multiscale flow crosses the window and ends in the strong-coupling regime; it is not proved here." Lemma 17.2 (twist flows exactly — Z[k]/Z unchanged by block steps; stack movable across block-aligned hyperplane piece); Lemma 17.3 (bounds hold in every twist sector, sup|$\rhoX$^(k)| $\leq \varepsilon^{|X|})$; Lemma 17.4 (vortex free energy at end of flow: $0 \leq 1 - Z[k]/Z \leq c$|$\Lambdan$|$e^{-a Lµ^(n)L\nu^(n)/2} (17.7))$. Lemma 17.4 gives (VF) with $\rho = a/(2b^{2n})$, p0 = mn. Hence (RG$) \Rightarrow$ confinement via Thm 17.1 | §17.5, (17.6)–(17.7), Lem. 17.2–17.4 | CONDITIONAL chain; (RG) OPEN |
| 17.9 | (VF) does not depend on method used to establish it; any proof of (VF) at physical coupling gives confinement via Thm 17.1. No known argument derives (VF) from Hypothesis 3. Mass gap concerns local correlations, area law the non-local Wilson loop; with matter in fundamental representation a gap without area law occurs [51]. A proof of the gap therefore yields confinement when it also establishes (VF). (VF) fails for U(1) at weak coupling (Wilson loops obey perimeter law, Thm 8.3), so any route to (VF) must use non-abelian structure; block-spin route uses it through negative one-loop coefficient driving flow to strong coupling. "What remains open for confinement is (VF) at the physical coupling, which lies in the same window as the mass gap, together with the source-to-Wilson bridge for the induced action of the model." | §17.5 | OPEN (VF) + OPEN bridge |
| 17.10 | §17.6 direction / target: environment-decorrelation bound (E) (17.8): for every $\beta$ in window $\exists \bar{\Xi}(\beta) < \infty$ such that uniformly in volume + local observables F, E[Pt v, Cov^off_$\nu(s) v] \leq \bar{\Xi}(\beta) E[$Pt |v|${}^{2}]$, $v = \nabla$mF, $t \in [\tau$∗$(\beta)$, tpos$(\beta)]$. "If (E) is proved with the stated uniformity, the follow-up estimates give a volume-uniform log-Sobolev inequality and hence a lattice mass gap at $\beta$. Together with the weak-coupling chain and the OS structure of its limit, this would give the continuum gap; (E) itself remains an open target." Evidence/next steps: (1) saturation of cross-link form — worst tested point $(\beta = 3, t = 0.2)$: cross-link form per pin $-3.75 \pm 0.30$, $-4.18 \pm 0.64$, $-3.71 \pm 0.47$ for L = 4, 5, 6, flat in volume — "numerical evidence for (E), not a proof". (2) Coarse vs fine modes: on 24 block, off-link form positive on 12 block-constant directions in every tested pin, negative on 180 fine directions; planned proof treats fine modes by block-local Poincaré + coarse modes by one RG step. (3) Blocked-RG side: finite marked-pullback + transverse-floor computations pass; still open: identity of blocked kernel, uniform interacting floor m0, certificate for weak-to-strong crossover. (4) Rigour of endpoints: area law for $\beta \leq 0.3925$ now has self-contained proof (exact slab reduction, centre symmetry, single-site Dobrushin coefficient, Arb certificate — 49,372 cells, minimum slack $9.7\times10^{-9})$; no longer cites Durhuus–Fröhlich + Föllmer. (5) SU(3): recompute strong-coupling certificate, Haar ceiling, heat-flow constants, weak-coupling threshold; evaluate retained 18-link conditional kernel. (6) Source-to-Wilson bridge: compare closed-walk action (Thm 6.10) with Wilson action via character expansions + large-field bound, starting with relevant blocking scale. Items 1–4 concern Wilson theory alone (follow-up paper); items 5–6 connect it to torus model | §17.6, (17.8), Fig. 31 | OPEN target (E); numerical evidence only; SU(3) recomputation OPEN |
| 17.11 | Relation to photon/EW calculations: direct Wilson–Villain comparison (§8.7) seeks masslessness in abelian weak-coupling regime; strong-coupling YM gap estimates cannot supply that conclusion. Finite EW cancellations (§9.5) do not prove physical SU(3) gap. A common source-to-continuum construction would provide shared infrastructure, but sector-specific uniform estimates + continuum identification would still be required | §17.6 end | Logical separation |

### §18 Conclusion and outlook (7392–~7650)

| ID | Claim | §/Eq. | Paper status |
|---|---|---|---|
| 18.1 | Collected low-energy Lagrangian (18.1)–(18.2) — see (f) below for full text + Table 20. "Equation (18.1) is therefore an effective finite/conditional summary, not a claim that an unrestricted microscopic source has already produced a continuum action." | §18.1, (18.1)–(18.2), Table 20 | COND (summary) |
| 18.2 | §18.2 differences from prior theories — see 14.12 above (noncommutative tori, Matrix compactifications, string/brane toroidal compactification, string-net/graph emergence, Connes–Marcolli Q-lattices, spectral action, Ascárate 2026, toroidal CDT). Contribution claimed in five connected pieces: separation of axioms from source specifications; finite level-three Hecke + cusp calculation kept distinct from D4 source; ordered-history commutant with matter + anomaly calculations; non-identifiability of source + eight-condition source-to-continuum theorem; explicit dependence of Lagrangian + vacuum outputs on declared inputs. "No new general theory of Q-lattices or noncommutative tori is proposed, and no spectral-action derivation is given. The unrestricted continuum limit, the electroweak gap, physical reflection positivity and the Yang–Mills gap remain open." | §18.2 | Comparative + OPEN restated |
| 18.3 | §18.3 conclusion: within declared finite completion, Axioms I + D determine 4-D signature with one time direction, gauge group SU$(3)c\times$SU$(2)L\timesU(1)Y$, anomaly-free chiral matter; with Axiom M + stated local derivative assumptions also Einstein–Hilbert tensor form. Static limits of sector actions give Newton's + Coulomb's laws, short-range weak force with Fermi coupling, asymptotically free short-distance quark force. Long-distance confinement of Wilson SU(3) follows from vortex condition §17.5, which an RG flow through intermediate couplings would establish; mass gap open in same range of couplings. Source does not determine couplings, $\Lambda$, mass hierarchies. Values in §16.5 solve observationally constrained matching problem, depend on declared moduli/thresholds/overlap inputs; not parameter-free predictions. Each step proved in finite model, certified numerically, or stated as named hypothesis/transfer condition — paper establishes "a checkable finite construction together with the conditional source-to-continuum implication of Theorem 12.1". Four physical transfers in Hypotheses 1–4, identification of unrestricted source, continuum YM result remain open; Lean + certificates cover only listed finite statements/bounds. "If those steps succeed, the torus-node construction supplies a common microscopic origin for structures otherwise described by separate theories; if they fail, the finite construction locates the failed interface." Model of interest for three features: small axiom system (three axioms + one declared finite completion); finite exhaustively enumerated set of consistent vacua; same finite data carried through to phenomenological outputs (gauge couplings, top-mass bound, axion coupling ratio) once matching inputs declared | §18.3 | Summary (statuses as in body) |
| 18.4 | §18.4 outlook / next steps: (1) Microscopic completion — construct single source-level transport, state–field map, measure, interaction, same-measure RG map incl. metric coupling, higher vertices, link measure, chiral selector, global zero-mode quotients; selection theorem must show data survive spatial-move, coframe, gauge projections. (2) Sector transfers — establish photon masslessness for integer Wilson action (Hypothesis 1), joint gauge–Higgs polymer norm + cutoff removal, source-to-Wilson comparison with intermediate-window bound before seeking physical SU(3) continuation. (3) Phenomenological consistency — test matching-scale lower bound, certify overlap-fit errors + heavy-state threshold, impose common torus areas, gravity normalisation, Higgs stability, cosmological history in one simultaneous solution. (4) Verification — complete review of correspondence between prose statements and Lean counterparts; incidence matrices, enumerations, interval certificates, sources, hashes already distributed in archived release [11]. "These tasks test the existing model; they do not add axioms to the canonical finite completion. Until the microscopic source, its measure and state–field map, and the sector transfers are established, the numerical matching results remain input-dependent finite diagnostics rather than consequences of an unrestricted continuum theory." | §18.4 | OPEN work list |
| 18.5 | Acknowledgements: "Anthropic Claude Opus 5.5 and Claude Opus 4.6, together with OpenAI Codex (GPT-5.6 and GPT-6.1 model families), were used in writing and reviewing the manuscript, revising its prose, Lean 4 verification and LaTeX build checks. The author is responsible for the definitions, proofs, calculations, citations, translations and final manuscript. These tools do not constitute mathematical evidence or replace the cited external results." | Ack. | Provenance statement (not a claim about the physics) |

### Appendices A–H

| ID | Claim | App. | Paper status |
|---|---|---|---|
| A.1 | App. A scope: deterministic attachment uses Mayer–Vietoris [85] (§D.1.17); cochain decompositions use discrete Hodge theory [86]. Probabilistic filling/homogenisation additionally require source-specific event comparison, localisation, weighted-operator bounds (App. D, esp. D.6). Neither macroscopic-cluster uniqueness nor scalar graph-Laplacian convergence alone verifies these transfers. High-density estimate below remains conditional on those checks | App. A intro | COND |
| A.2 | Percolation comparison model: homogeneous Poisson $\Pi\lambda$ in $R^{4}$; adjacency at Euclidean distance $\leq$ deterministic radius r (Boolean balls radius r/2; clique complex of Gilbert graph); $\lambdar^{4}$ supercritical; inserted point under Poisson Palm law. Marked-torus source obeys these assumptions ONLY if marks do not alter adjacency, normalised metric is the Euclidean metric used, and Palm / good-box / graph–Boolean identifications are proved. "These are premises of this appendix, not conclusions of the cited percolation papers." | App. A | Premises (unproved for literal source) |
| A.3 | Lemma A.1 (Vertex addition$): K' = K \cup$ st$(v) \Rightarrow \dim H_{1}(K') = \dim H_{1}(K) -$ rank$(H_{1}($lk $v) \to H_{1}(K)) + \dim \ker(\tilde{H}_{0}($lk $v) \to \tilde{H}_{0}(K)) (A.1)$; new $H_{1}$ classes arise only at vertices whose link is disconnected | Lem. A.1, (A.1) | THM (algebraic); Lean `TorusModel.vertex_addition` |
| A.4 | Lemma A.2 (Locality of births): new $H_{1}$ classes generated by local cycles within reconnection radius $\rhox$; assume source-specific event inclusion ${\rhox > \ell} \subseteq U\ell^{c} (U\ell$ = precise unique-crossing-cluster event in Penrose–Pisztora box construction, finite link components controlled separately); then absence of extended $H_{1} ($condition (T)) follows from supercritical continuum-percolation estimate [87] (§D.1.1). "The implication from a disconnected link to failure of the Boolean unique-crossing event is not a consequence of the cited theorem$\dots$ It is therefore precisely the event inclusion assumed in the lemma$\dots$ Under the supercritical finite-range and moment hypotheses$\dots P(U\ell^{c}) \leq$ Ce^${-c\ell}$." Proves (T) under explicitly stated percolation hypotheses + event inclusion; "it does not prove that the source lies in that regime" | Lem. A.2 | COND (on event inclusion + percolation hypotheses) |
| A.5 | Lemma A.3 (Anchored dual): local cycle c anchored in ball B radius r, nonzero in $H_{1}(K) \Rightarrow \exists$ cocycle $\eta \in H^{1}(K, K$\B${}_{2}r)$ supported in ball with $\langle\eta$,$c\rangle \neq 0$; representability of local classes by finitely supported cocycles (condition (L)) reduces to event that local classes are anchored in balls | Lem. A.3 | THM (conditional on anchor-ball premise) |
| A.6 | Lemma A.4 (Stationary Weyl decomposition): assume (T) no extended $H^{1}$, (L) stationary square-summable family of finitely supported representatives of local $H_{1}$ classes, $(P) L^{2}$-sublinearity of scalar potential $R^{-6}\Sigma_{x\inBR}$|$\phi(x)$|${}^{2} \to 0 (A.2)$, + finite-volume Hodge projections converge strongly in stationary $L^{2}$ cochain space $\Rightarrow$ every stationary harmonic 1-field = deterministic constant field + $L^{2}$-convergent sum of local hole fields (A.3)–(A.5) | Lem. A.4 | COND (on (T),(L),(P) + projection convergence) |
| A.7 | Theorem A.5 (Upper bound): under Lemma A.4 + large-scale 1-chain Poincaré inequality $S' ($|a| $\leq$ CR|$d_{1}a$| for $a \perp \ker d_{1})$, inequality of Thm 8.15 is an equality. $S'$ proved conditionally on four published percolation results [87–90] (§D.1.2). Ingredients: filling-operator reduction; lattice filling area $O(d^{2})$; linear area of thin loops along randomly shifted hierarchical paths; Schur test of Iwaniec–Lutoborski type [91] (§D.1.3); local hole corrections; Cauchy–Crofton flux lemma [92] (§D.1.18) with weighted Schur test on bad clusters; boundary connectivity of bad clusters [90]; 3-dependent concentration inequality. "Every conclusion in this paragraph is conditional on the quoted percolation hypotheses and $S'$." | Thm A.5 | COND |
| A.8 | Theorem A.6 (High density; conditional quantitative estimate): at mean degree D ≳ $9\times10^{5}$, deterministic filling (edge shortening + cone subdivision on $\delta < r/5$-dense samples) + averaged cone Poincaré inequality (constant $C\ell^{2})$ give (T), (L), $S'$ almost surely, given declared occupancy + finite-dependence domination constants; Thm A.5 applies, homogenisation closes at this density. "The word 'conditional' signifies that the printed decimal threshold is valid only with the specified occupancy and domination constants; it is not inferred from the empirical model-density runs below." Occupancy estimate, finite-dependence domination, continuum-percolation step enter as stated assumptions; no computer certificate of them distributed. Two algebraic ingredients formalised in Lean (App. F) | Thm A.6 | COND (threshold D ≳ $9\times10^{5})$ |
| A.9 | Numerical result A.7 (model density rc = 1.5): relaxation ratios 0.60–0.72, $\varepsilon \approx 10 ($rc = 1.8); within-sample $\varepsilon$ varies 1–4% over six field directions, between samples $\pm20$%; corrector rms saturates at 0.32 for $R \geq 6$. Density of local $H_{1}$ classes 0.005–0.010 per unit volume at rc = 1.5, 0 at rc = 1.8, 0.07–0.09 at rc = 1.4. $S'$ constant gives $\lambda$minR${}^{2} = 0.17$–1.09, non-decreasing in R. 0.9–1.5% of vertices have disconnected link; all 596 such defects reconnect within $\rhox \leq 2.66 < 2$rc, in at most 5 steps. Relative homology on balls radius 2rc detects every local class (42, 41, 46 in three samples) | Num. Res. A.7 | NUM (diagnostic) |
| B.1 | App. B verification/reproducibility: Lean 4 formalisations of finite algebraic statements + stored numerical computations. Formal projects build in full; every listed statement mapped to a declaration; dependency/placeholder/axiom checks pass. Proofs re-checked by independent kernel nanoda, which replayed all 84 modules of main-paper formalisation in twenty-one bounded batches without error (App. F says eleven batches — see note below). "One step of a complete verification remains: reading each displayed statement against its Lean counterpart to confirm that the two express the same mathematics." Analytic/continuum clauses outside finite formalisation identified as such where they occur. Published external theorems enter as named inputs | App. B | Verification claim (paper's; NOT re-checked by this reader) |
| B.2 | Repository + archive: formalisation + reproducibility material in public repo https://github.com/s6ygleee/torus-node-lean4, archived on Zenodo doi:10.5281/zenodo.23863514 [11] (version 1.0.0). Release contains Lean formalisation, statement–declaration tables, provenance + certificate index, build rules; YM formalisation released with separate follow-up paper. Formalisation + scripts MIT licence; manuscript text + data CC BY 4.0 | App. B | Provenance |
| B.3 | Numerical data classes: exact finite computation / interval-certified bound / numerical diagnostic / input-dependent estimate — each value enters argument with standing of its class. Definitions/axioms/proofs stated independently of any stored file; a computation can be rerun/replaced with only its classification updated | App. B | Method |
| C.1 | App. C.1 declared inputs / quantities not fixed by axioms: source exponent $\beta = 1$ is part of declared source kernel; its coincidence with a pole of $\zeta(\beta)\zeta(\beta-1)$ is a remark, not a derivation. Mechanism for three chiral generations, charge quantisation, anomaly cancellation derived in finite matter construction, but selected vacuum + generation count are vacuum data. Couplings, masses, cosmological constant not fixed by minimal axioms; numerical reconstruction requires declared finite catalogue, continuous moduli, matching inputs | App. C.1 | Declared inputs (see (f)) |
| C.2 | App. C.2 no-go / non-identifiability: fully relational construction of dynamical metric without Axiom M fails at stated Weinberg–Witten obstruction; minimal model does not produce dynamical metric by itself. Literal source-to-metric, source-to-pole/vertex, source-to-chiral-matter, source-to-gauge-link bridges are no-go or non-identifiability results, not missing numerical fits; finite completion consequently labelled conditional. RP, Wilson-photon homogenisation, electroweak analytic window, YM continuum bridge remain conditional on explicitly named hypotheses; comparison-model theorems do not by themselves prove physical source transfer. Everpresent-$\Lambda$ mechanism + rolling node-shape dark energy excluded by model boundary + stated variation bounds; remaining $\Lambda$ is integration constant or initial datum | App. C.2 | THM (no-go) / COND |
| C.3 | App. C.3 cuboctahedral distinction: standalone 12-vertex cuboctahedral graph is NOT a model choice in this paper. Cuboctahedron appearing in main text is the A3 spatial section of the D4 root system, used in dispersion, S4 action, face-centred spatial calculations; not a separate graph model | App. C.3 | Clarification (relevant to any D4/cuboctahedron comparison: the paper's D4 object is the root system, its A3 section is a cuboctahedron, and no standalone cuboctahedral graph model is used) |
| D.1 | App. D.1 external-theorem dictionary — see (f) for the full list (D.1.1–D.1.19) with each theorem's usable form, hypothesis checked, and conclusion transferred | App. D.1 | External inputs (quoted) |
| D.2–D.7 | Deferred derivations: D.2 gauge/matter (Thm 6.8 finite spatial-move-sequence RG criterion (D.5) — Sturm sign-variation, rational Sturm table is Lean certificate; Thm 6.9 physical-time lift (D.6); Props. 6.15/6.16 vacuum catalogue + no extra U(1) — dim ker MGS = 1 (D.7); Thm 6.17/Prop. 6.18 non-fixing of couplings (D.8)). D.3 EM (Villain U(1) nonconfinement Thm 8.3 — $\betaV \geq 1.614, \langleW(\gamma)\rangle \geq \exp(-C$ Per$(\gamma)) (D.9)$, incompatible with area law; Kotecký–Preiss margin is interval certificate; Wilson action at $\betat = 3.643$ NOT covered; Hartman–Watson mixture Lem. 8.6 (D.4); rank-one defect Lem. 8.9; Poisson Gaussian photon + cell bounds Thms 8.10/8.13/8.15). D.4 EW/strong (Thm 9.4 all-order fixed-background convergence, conditional on fixed background + uniform propagator bound; Thm 9.5/Prop. 9.6 EW uniqueness/reduction — joint gauge–Higgs norm, uniqueness, cutoff removal, pull-back to unrestricted source, 53-step composition remain OPEN; Kotecký–Preiss condition (D.$10) \sup \Sigma$|$z(\gamma)$|$e^{a|\gamma|} \leq \eta < 1$; Prop. 9.19 Higgs stability — outward-rounded intervals, three-loop beta functions; Prop. 10.2 — if $\alphas(\Lambda) = 1/45$ then $g^{2} = 4\pi/45, \beta = 6/g^{2} = 270/(4\pi) \simeq 21.5$, so strong sector starts in weak-coupling lattice regime; remaining assertion is exactly ordinary 4-D SU(3) YM mass-gap problem, not a model-specific proof). D.5 YM (Haar Wasserstein constant $8/(9\pi)$ follow-up lemma; selection structure + weak-coupling chain — conditional on intermediate-window covariance bound + qualitative one-loop universality input; confinement/vortex Lem. 17.2–17.4 + Thm 17.1 — external inputs Kotecký–Preiss (§D.1.8) + Tomboulis–Yaffe (§D.1.9); premise (VF), implied by (RG); heat-flow lemmas + Riccati comparison (D.11)). D.6 homogenisation (Lem. A.2–A.4; Thms A.5–A.6). D.7 boundary of derived statements: small-field analyticity estimate, irrelevant-polymer contraction, intermediate-window covariance bound, source-to-Wilson universality bridge, eight source-to-continuum conditions are NOT consequences of finite derivations; every conclusion using one is conditional on corresponding estimate | App. D.2–D.7 | Mixed THM (finite/conditional) / OPEN |
| E.1 | App. E.1 canonical finite bounded-geometry source: D∗ = H∗ $\times E$∗, H∗ = {1} $\cup$ Trans(S4), E∗ = {0, $\pmc2, \pmc3, \pmc5} (E.1)$, so |H∗| = |E∗| = 7, |D∗| = 49. Symbols c2, c3, c5 are three independent clock-alphabet marks, NOT the coordinate vectors ei used to write D4 roots | (E.1) | DEF |
| E.2 | App. E.2 49 marks vs 24-state fibre: Rsp = ${\pm($ei $-$ ej$): 1 \leq i < j \leq 4} \subset R(D4) (E.2)$; source-to-history map s: Rsp $\to$ Trans(S4), $s(\pm($ei$-$ej)) = (ij) (E.3), two-to-one (12 directed spatial roots $\to 6$ transpositions); adjoining no-move gives 7-element one-step history alphabet H∗. Path dk = (hk, ck$) \in D$∗ has cumulative history Hist = hn$\cdot\cdot\cdoth1 \in S4$ and clock Clk = $\Sigma$ ck (E.4). Six transpositions generate $S4 \Rightarrow$ cumulative history fibre has |S4| = 24 states. "49 elements of D∗ are allowed one-step marks, whereas the 24 elements of S4 are accumulated history states; no bijection between the two sets is asserted." Remaining 12 D4 roots are time-changing roots (Rem. 3.11), determine determinant/scale valuation; paper does NOT derive a map from those roots to the seven clock marks E∗; selecting E∗ + pairing with H∗ is part of Cfin, not a theorem about literal unrestricted torus source. Temporal/history transfer P = $(1/6)\Sigma_{i<j} L($ij), Mt = $\exp[t(P-I)]$, q = 2/3 (E.5), acting on 24-state fibre, not on 49-element alphabet. Maximum-entropy parameters $\alpha = 0.48047629504141964$, $\kappat = 1.1876789651362785 (E.6)$. Minimal determinacy package Cfin = (D∗, µ∗, $\Theta$, Mt, K[X], Fchiral) (E.$7): \Theta$ = plane/Gram reflection factorisation, K[X] = state-dependent metric-and-current rule, Fchiral = finite history bimodule with projector + Yukawa intertwiners. Finite completion analysis verifies finite push-forward, right-S4 equivariance, same-history-space Markov semigroup, Gram RP. Explicit finite-action representative: Haar $U(1)\timesU(3)\timesU(2)$ links, Gaussian coframe, coercive two-doublet Higgs action, clock pullback, finite chiral module. Package determines listed structural sectors; does not by itself choose every action coefficient. Particular representative also requires cact = $(\beta1, \beta2, \beta3, m^{2}e, \kappae, \kappaH, \lambdaH$, vH${}^{2}, \lambdaA, e0$, Dchiral) (E.8), entries are fixed inputs. Configuration space includes pinned clock factor TL,a (not omitted from $\OmegaL,a)$. Coframe/Higgs/chiral terms are explicit massive Gaussian, coercive quartic, finite Dirac terms; coefficients + finite chiral matrices are declared finite-model data, NOT claimed forced by unrestricted raw torus tuple. Global clock shift removed by integrating on TL,$a = {T: \Sigmax$ Tx = 0} (E.9). Bosonic partition function + polynomial moments finite. Full Berezin functional finite algebraically; normalised chiral correlators require separately stated condition ZL,$a \neq 0$. Volume-uniform edge estimate E|$E\Lambda$|${}^{-1}\Sigma\ell$|∆$T\ell - d\ell$|${}^{2} \leq (\log 5)^{2} + 3/(4\kappat) < 6.444 (E.10)$ | (E.1)–(E.10) | DEF + THM (finite verifications) |
| E.3 | Proposition E.1 (Minimal completion data): among completions retaining 49-mark source, reflection, same-history-space history blocking, dynamical coframe, chiral matter, structural package Cfin is minimal: deleting any displayed component leaves two completions with identical remaining data and different values of at least one listed structural output. "This statement does not claim that Cfin determines the action coefficients cact." Proof by five deletion pairs (measure; $\Theta$ with $\eta = \pm1/2$; Mt identity vs convolution blocking; K[X] Hessian ranks 0 vs 10; Fchiral bosonic vs bimodule) | Prop. E.1 | THM (minimality, finite) |
| E.4 | Proposition E.2 (Finite partition function and moments): for reference functional of Def. 3.15, bosonic partition function + all bosonic polynomial moments finite for each finite L; every polynomial Berezin functional finite; defines normalised chiral correlator whenever ZL,$a \neq 0$. Proof: clock Hessian least eigenvalue $4\kappat \sin^{2}(\pi/L) > 0$; coframe Hessian $\geq m^{2}e I$; Higgs potential coercive, quartic growth. "Proves algebraic finiteness, not positivity or non-vanishing of the chiral determinant" | Prop. E.2 | THM (finite); Lean `TorusModel.finite_product_gaussian_integrable` |
| E.5 | Proposition E.3 (Uniform clock-increment moment): for three-component pinned Gaussian clock, E|$E\Lambda$|${}^{-1}\Sigma\ell$|Ty $-$ Tx $- c\ell$|${}^{2} \leq (\log 5)^{2} + 3/(4\kappat) < 6.444 (E.11)$, uniformly in L. Proof via conditioning on marks, minimiser $\bar{T}$, equipartition (E.12) | Prop. E.3, (E.11)–(E.12) | THM (finite); Lean `TorusModel.clock_increment_bound_core` |
| E.6 | Proposition E.4 (Summable finite Ward remainder): if $V = \Sigma_{a=1}$^$N \lambda$aUa, ‖Ua‖ $\leq 1$, CV = $\Sigma$|$\lambdaa$|, then ‖Rn‖ $\leq$ CV$(2/3)^{n/2}$ implies $\Sigma_{n\geq0}$‖Rn‖ $\leq 1.34918517428501$ CV, $\Sigma$‖Rn‖${}^{2} \leq 0.682518507618342$ CV${}^{2} (E.13) ($outward roundings of convergent scalar sums; distributed with reproducibility package) | Prop. E.4, (E.13) | THM (finite); Lean `TorusModel.ward_tail_norm_core` |
| E.7 | Theorem E.5 (Periodic coexact compactness): on periodic 4-D lattice, nonzero-momentum coexact Hodge symbol $\lambda(k) = 4\Sigma_{µ=1}$^$4 \sin^{2}(k$µ/2), $\lambda\min(L) = 4 \sin^{2}(\pi/L) (E.14)$. Periodic coexact forms with uniform scaled Hodge-energy bound have $L^{2}$-convergent Fourier-interpolant subsequences | Thm E.5, (E.14) | THM; Lean `TorusModel.periodic_fourier_tail_bound` |
| E.8 | Theorem E.6 (Regularity boundary for centred clock fluctuation): under naive 4-D continuum scaling, one real component of centred pinned free-clock fluctuation is NOT uniformly bounded in $H^{1}$, but its lattice laws are tight in $H^{-s}$ for every s > 1 (E.15). Mean grows as $L^{2}/\kappat$, variance bounded by $2/\kappat^{2}$; Chebyshev $\Rightarrow$ divergence in probability, failure of $H^{1}$ tightness. High-mode tail $O(K^{2-2s})$. "Conditional on the marks$\dots$ not a compactness theorem for the full interacting measure" | Thm E.6, (E.15) | THM (finite/free-clock) |
| E.9 | App. E.3 finite results + scope: proved for explicitly declared canonical finite source — finite selector/measure, history retention, same-history-space Markov semigroup; finite RP + finite EW L3/L4 realisation; finite bounded-vertex Ward tail (E.16 = E.13 sums); periodic D4 coexact coercivity $\lambda\min(L) = 4 \sin^{2}(\pi/L) (E.17)$ + deterministic discrete Rellich compactness; finite Wilson quadratic photon pole + matched Villain signed P1 realisation; finite metric/coframe response, $U(3)\timesU(2)$-capable link realisation, anomaly-free chiral/Higgs/Yukawa realisation. Finite EW estimate interval certificate: $B16 \leq 7.260041057$, $\sup_{L\geq16}$ BL $\leq 8.464$, Kworst = 0.40 < 0.75 (E.18). "These numbers establish the stated bounds for the declared finite realisation, not the unrestricted source-level electroweak theorem." | App. E.3, (E.16)–(E.18) | THM (finite) |
| E.10 | App. E.4 continuum boundary + raw-source non-identifiability: raw torus tuple does not specify state measure, selector, reflection involution, blocking map, site-link measure, state-dependent current, chiral module; explicit completion pairs give incompatible RP signs, metric ranks, gauge sectors, matter sectors; hence Sraw ⇏ (µ∗, $\Theta, \Phi$RG, Wyx, K[X], Fchiral, H) (E.19 = (12.6)). Declaring Cfin defines source-to-finite map; does not derive package from unrestricted raw tuple. Complementary continuum obstruction: naively scaled massless clock Dirichlet energy grows as $L^{2}/\kappat$, so $H^{1}$-type tightness fails without renormalisation or different topology; free/finite pinned clock tight in $H^{-s}$ for s > 1, Fourier tail $O(K^{2-2s})$. "Not yet an interacting raw-source compactness theorem." | App. E.4, (E.19) | THM (non-identifiability) / OPEN (compactness) |
| E.11 | App. E.5 relation to physical hypotheses: certificates concern declared finite source; relation to four physical hypotheses stated in §2.3; source-to-continuum premises in Thm 12.1 + Table 6. Finite RP, EW, matched-Villain results do NOT establish corresponding unrestricted-source statements or YM continuum gap. "The declared package completes the canonical finite model; it neither identifies that package with the raw torus source nor proves an interacting all-volume continuum limit." | App. E.5 | Boundary statement |
| F.1 | App. F formal verification + Lean correspondence: Lean 4.32.1 project builds without errors; placeholder, dependency, axiom, statement-mapping checks pass for all 296 inventory declarations (inventory lists formal statements, not count of results in paper). Main paper has 112 theorem-like environments: 4 explicit hypotheses + 108 others (10 definitions + 98 results, each with local proof). Of 108: 12 formalised exactly, 54 through a finite or conditional core, 38 through formalised lemmas or cited external results; the four results on confinement under the window hypothesis in the YM interface section have NO Lean counterpart; four hypotheses not formalised. Classification complete; every stated result has recorded formal status. Only axioms reported for audited declarations: standard Lean axioms propext, Classical.choice, Quot.sound. External theorem used in a proof is an explicit hypothesis of corresponding Lean statement, not a hidden axiom. YM follow-up is separate project, not part of present verification count. Two independent machine checks: Lean kernel during build + nanoda replay of compiled declarations outside Lean — "every project module is exported with lean4export and re-checked by the independent type checker nanoda, in bounded batches$\dots$ All 84 project modules were checked in eleven batches; nanoda reported no type-checking errors." **Internal inconsistency noted by this reader:** App. B (p.151) says nanoda replayed all 84 modules "in twenty-one bounded batches", App. F (p.169) says "in eleven batches". The paper does not reconcile the two numbers in this range. Neither check decides whether a Lean statement says the same thing as surrounding prose; that correspondence is reviewed separately and still requires human approval. Table 21 gives reader-facing statement $\leftrightarrow$ formal counterpart (exact lookup keys) — includes in this range: Thm 11.3 `TorusModel.rotor_gram_kernel_posSemidef`; Cor. 11.4 `TorusModel.FiniteCompletion.bath_memory_eq_gram`; Prop. 13.1 `TorusModel.common_ir_physical_block_diagonal`; Prop. 13.2 `TorusModel.hecke_projective_line_counts`; Prop. 13.3 `TorusModel.induced_newton_log_sensitivity`; Lem. A.1 `TorusModel.vertex_addition`; Props. E.2–E.4, Thms E.5–E.6 counterparts (see E.4–E.8 above). External results + formal boundary list: OS reconstruction, OS–Seiler RP, Lovelock, Rényi Poisson characterisation, Poisson mapping theorem, Kolmogorov cylinder-extension, Prokhorov tightness, Kotecký–Preiss, Fröhlich–Spencer, Akcoglu–Krengel, Armstrong–Venkatraman, Penrose–Pisztora, Antal–Pisztora, Liggett–Schonmann–Stacey, Timár, Dobrushin, Föllmer, Jentzsch–Perron–Frobenius, Atiyah–Singer/Riemann–Roch — "explicit external inputs [12–15, 18, 29, 31, 35, 39, 40, 42, 47, 51–53, 55, 70, 71, 87–90], never hidden as axiom" | App. F, Table 21 | Verification claim (paper's; NOT re-checked by this reader) |
| G.1 | App. G computational data + reproducibility index (Table 22): every computation-dependent result listed with computation + evidence class (exact / interval-certified / error-bounded / finite counterexample / numerical). Rows in this range: RP of D4 lattice model (Thm 4.5) — reflection_positivity_gram, reflection_positivity_certificate (exact; error-bounded); gauge group from history commutant (Thm 6.4) — history_commutant, source_move_semigroup (exact); contraction of finite spatial-move RG (Prop. 6.8) — history_rg_sturm (exact); physical-time lift (Thm 6.9) — lift_defect (exact); vacuum catalogue, chirality, anomalies (Props. 6.15, Thm 6.13) — vacuum_catalogue, matter_bimodule_anomaly (exact); no extra massless U(1) (Prop. 6.16) — vacuum_catalogue (exact); failure of reverse derivation at self-dual points (Prop. 6.18) — self_dual_scan, self_dual_scan_n5, self_dual_scan_n6 (exact); RP of finite sources (§11) — certificates/volume_uniform_reflection_positivity, certificates/bath_reflection_positivity (exact); gravitational crossing kernels (Prop. 5.14) — crossing_kernel_check, embeddability_kernel_check (finite counterexample); finite source, push-forward, non-identifiability (App. E) — certificates/finite_source_pushforward, certificates/raw_source_nonidentifiability, certificates/minimal_source_package, certificates/explicit_finite_action (exact); finite Ward remainder (Prop. E.4) — certificates/finite_ward_remainder, certificates/continuum_ward_identity (interval-certified); clock moments + tightness (§3.6) — certificates/finite_partition_moments, certificates/clock_increment_moment, certificates/clock_uv_obstruction, certificates/clock_distributional_tightness (exact). **Matched Villain cross-check deliberately classified as numerical diagnostic: "descriptive scope and the absence of an executable script, standalone input, and execution log are recorded in supplement/reproducibility/diagnostics/matched_villain_crosscheck.md. It is not a certificate for the integer Wilson action."** Numerical illustrations NOT in reproducibility package: averaged RP tests, bounce + Page-curve models, heat-flow negative-mode sampling, Hartman–Watson tail values, weak-triangle loss estimates | App. G, Table 22 | Evidence-class ledger (paper's) |
| H.1 | App. H provenance of numerical outputs (Table 23): 76 vacua + 16 rows — vacuum catalogue, exact finite computation. V1 M∗ + $1/\alpha$∗ — vacuum catalogue with declared two-loop matching inputs, input-dependent numerical estimate. V1 top-mass bound mt $\leq 172.89$ GeV — Higgs stability, three-loop SM running with displayed matching inputs, input-dependent numerical estimate. V1 axion E/N = 2/3, ma $\simeq 358$ µeV — vacuum catalogue (anomaly ratio) + axion dark matter (misalignment estimate), exact finite computation + input-dependent numerical estimate. Fine-structure/Newton sky dipole — sky dipole, numerical diagnostic. Second-Higgs scale + $\tan \beta$ — two-Higgs-doublet checks, input-dependent numerical estimate. Black-hole entropy ratio — black-hole entropy, finite consistency check. Exact gauge matching in all ten classes — exact gauge matching, numerical diagnostic. Matched Villain signed DP cross-check — numerical diagnostic (no script/log). Top-mass bounds on matching surfaces — top-mass bound, input-dependent numerical estimate. Asymptotic scale µ$\infty \simeq 5.906\times10^{8}$ GeV — asymptotic matching scale, numerical diagnostic. Axion mass interval + wall-forming branch — axion history, input-dependent numerical estimate. Charged-lepton ratios, $\kappa^{2} \simeq 0.5724$ — lepton circulant fit, numerical diagnostic. Failure of quark overlap rule — quark overlap test, numerical diagnostic. Selection of matching class V11 by gravity–gauge relation — gravity–gauge selection, numerical diagnostic. "Of these computations, only the vacuum catalogue is an exhaustive finite integer enumeration. The other rows combine the catalogue with running, geometric or observational inputs$\dots$ The searches on the matching surfaces are numerical: the asymptotic scale is the solution of an explicit limiting equation, but no proof is supplied that it is the global infimum; the lepton fit uses truncated Gaussian sums at selected separations and is not a uniqueness certificate; the quark overlap test is a pre-registered test whose failure is the reported result; and the gravity–gauge selection is established on the sampled matching surfaces, not on the full continuous parameter domain." Table 24 (H.1) lists files: vacuum_catalogue.cjs / vacuum_catalogue.log; higgs_stability.py / higgs_stability.log; axion_dark_matter.py / axion_dark_matter.log; sky_dipole.py / sky_dipole.log; two_higgs_doublet.py / two_higgs_doublet.log; black_hole_entropy.py / black_hole_entropy_M24.json, M32, M40; exact_gauge_matching.cjs / .log; top_mass_bound.py / .log; asymptotic_matching_scale.cjs / .log; axion_history.py / .log; lepton_circulant_fit.py / .log; quark_overlap_test.py / .log; gravity_gauge_selection.cjs / .log. Helper cycle_valid.cjs shared by catalogue scripts. Lock file calculations-lock.json records command, environment, SHA-256 checksums, comparison tolerances | App. H, Tables 23–24 | Provenance ledger (paper's) |

---

## (b) The canonical finite model (§13) — components and what each is conditional on

**Components (§13.1).** The canonical finite model is the model of §3.6 and consists of:

1. **Axioms I, D and M** — I and D (spacetime/matter axioms, stated before this range);
   M is the dynamical-metric axiom (§5.3). Dropping M gives the minimal model (§2):
   metric is a fixed background, not dynamical; no dynamical-gravity claim.
2. **Adopted level–3 Hecke relation domain** — determinant-one correspondences give the
   A4 cusp action; determinant-two correspondences extend it to S4. This is the arithmetic
   relation domain. It does NOT identify the S4 history action with the separately declared
   D4 colour/source structure (Prop. 13.2: only 3 determinant-2 cosets vs 24 D4 moves;
   only S4 irreps trivial on V4 realisable through the $S4 \to S3$ map, so colour blocks 3, $3'$
   cannot be realised that way; the four-cusp module is $1 \oplus 3$ with commutant $U(1)\timesU(1))$.
3. **Declared finite D4 source (Definition 3.7).**
4. **Declared bounded-geometry completion package Cfin (App. E §E.1, Prop. E.1)** —
   Cfin = (D∗, µ∗, $\Theta$, Mt, K[X], Fchiral) (E.7): a finite selector and measure, reflection,
   blocking family, metric/current rule, chiral module. D∗ = H∗ $\times E$∗, |D∗| = 49 one-step
   marks; the 24-state S4 fibre is the *accumulated* history (App. E §E.2). The clock
   alphabet E∗ = {0, $\pmc2, \pmc3, \pmc5}$ is declared completion data, not derived from D4 roots.

**What each component is conditional on / what it does not supply:**

- Declaring Cfin makes the finite model definite but does **not** derive the package from
  the unrestricted torus data. The literal Poisson–torus interpretation must still satisfy
  the four requirements of Theorem 3.12 (summable relation domain; reversible measure;
  ordered-history transport; uniform tail control) **and** the eight continuum conditions of
  Theorem 12.1. Every theorem of Part I is stated with the smallest set of assumptions it
  needs (algebraic main line: Axioms I, D + finite D4 source; measure-dependent finite
  statements: relevant part of Cfin; dynamical gravity: Axiom M as well; unrestricted
  source / continuum limit: the four source-completion requirements + eight conditions).
- The representatives (§13.2, Table 7) each change one stated assumption; conclusions are
  attributed to the smallest branch that proves them. The finite certification lattice passes
  all seven admissibility conditions A (Table 8) at its lattice size but is reverse-engineered,
  not derived from a completion (selector, P, Q, $\kappa$ chosen). The projected coupled model
  (CQ = $\sqrt{\kappa}$ QC${}_{0}, P\SigmaQ = \Sigma$QP = 0) preserves the physical block by Prop. 13.1, but P, Q
  and the renormalisation are *declared rather than source-derived*; it is usable for gravity
  without loss only with $\kappa$ equal to the induced coefficient (Prop. 13.3) — a constant $\kappa$
  matched to observed G kills the G dipole ($d \ln G/d \ln \chi$node = 0 instead of $-1)$.
- The source-measure completion proposal (literal Poisson/Hecke source + hyperbolic
  measure on the modular surface) is a candidate for requirement (i) only; requirement (ii)
  and the D4 link are open; it presently supplies **no physical numerical prediction**
  (Fig. 25).
- The observationally constrained specialisation (see (c)) fixes free moduli from data; it
  introduces no new axiom and does not claim microscopic selection of the chosen point.

## (c) The observationally constrained specialisation and the mt bound (§13.7, §16.5)

### What it is

The observational branch obtained by continuing the canonical finite model and imposing a
sequence of restrictions fixed in advance. It retains the model's axioms, field content,
vacuum family and gravity–gauge bridge, while progressively constraining otherwise
undetermined moduli by a fixed set of observations. It is a computational representative
of the canonical model (like the finite certification lattice, which fixes finite data to test
structural conditions); the two answer different questions. Neither introduces a new axiom,
replaces the canonical model, or claims the microscopic source selects the chosen point.
Its additional inputs are: **the measured gauge couplings, a declared running prescription,
a Higgs-stability boundary condition and, for masses, a declared Yukawa amplitude rule.**
Solving for a point in the admissible structures does not establish the completion
requirements of Theorem 3.12. Before every fit, the number of free parameters, the
observable list, the objective, the pass threshold and the parameter domain are fixed in
advance, and no parameter or observable is added after inspecting the result. "For these
declared leading-order rules the analysis is complete: every resulting output, and every
sector in which the rules fail, is given below. The selected point itself is fixed by the data
rather than derived from the source."

### Matching equations — copied exactly as written

Discrete catalogue and continuous matching. The enumeration of §6.5 contains **76
copies with 16 distinct outputs**; the observationally restricted calculation groups them
into **ten matching classes**. These counts refer to different equivalence criteria. For a
class define the wrapped volumes and the hypercharge volume by

> Vx$(\chi) = \prod$_{i=1}^{3} $\sqrt{[}($nix$)^{2} + \chii^{2}($mix$)^{2}]$,   VY$(\chi) = \Sigma_{x} 2$ Nx $c^{2}$_{Y,x} Vx$(\chi)$,   (13.4)

where $c_{Y,x}$ are the hypercharge coefficients and the winding data include the declared
tilt convention. With a positive common normalisation K, matching requires

> $\alpha_{3}^{-1}(M$∗) = KVa,   $\alpha_{2}^{-1}(M$∗) = KVb,   $\alphaY^{-1}(M$∗) = KVY.   (13.5)

**Measured inputs (stated in the text):** "The two-loop running starts from
$\alpha$em${}^{-1}($MZ) = 127.95, $\sin^{2}\thetaW($MZ) = 0.23122 and $\alphas($MZ) = 0.1179."
Eliminating $K = \alpha_{3}^{-1}$/Va leaves two residual equations for $(\chi_{1}, \chi_{2}, \chi_{3}, M$∗); at a regular
point their solution set has dimension two, so exact matching leaves continuous freedom
even after the class is fixed. The numerical solver finds roots in all ten classes. "This is
an existence calculation at finite precision, not an interval-certified enumeration of every
root, and the three couplings are inputs."

### Higgs stability on the matching surface — copied exactly

Let $\LambdaI($mt, $\alphas)$ be the first zero of the running Standard-Model quartic. The non-negative
D-term boundary requires M∗ $\leq \LambdaI$, in addition to the quartic inequalities of §9.6. **At
mt = 172.57 GeV and $\alphas = 0.1180$ one finds $\LambdaI \simeq 4.6 \times 10^{10}$ GeV; the difference from the
matching input $\alphas = 0.1179$ is an input sensitivity.** Exact matching finds acceptable
points in all ten classes, so stability does not uniquely select the fixed reference point V1.
In the large-shape limit the volume relation becomes

> $\alphaY^{-1}(\mu\infty) = \alpha_{2}^{-1}(\mu\infty) + (5/3)\alpha_{3}^{-1}(\mu\infty)$,   (13.6)

whose solution with the input couplings is **$\mu\infty \simeq 5.906 \times 10^{8}$ GeV**.

Two top-mass options follow:

> (a) If every finite-shape solution satisfies M∗ $\geq \mu\infty ($numerically supported, not proved),
> then $\LambdaI($mt, $\alphas) \geq M$∗ $\geq \mu\infty$ gives **mt ≲ 174.31 GeV at $\alphas = 0.1180$**.
>
> (b) If the strict D-term boundary is replaced by a threshold of heavy partner states at
> M∗, larger M∗ is allowed and one finds **mt ≲ 173.0–173.9 GeV with $\tan \beta = 1.2$–1.5**.
> This threshold is plausible but not proved.

### Gravity–gauge selection — copied exactly

Let $q = \LambdaR$ and $K = \kappaA q^{3}$. If the same geometry satisfies

> MP${}^{2} = \kappag \Lambda^{2} q^{6} \prod_{i} \chii$,   M∗ = $R^{-1}$,   (13.7)

then $\Lambda$ = qM∗ gives

> MP${}^{2} = \kappag M$∗${}^{2} q^{8} \prod_{i} \chii$,   M∗bridge = (MP $\kappa^{4/3})/(\sqrt{\kappa}g \prod_{i} \chii K^{4/3})$.   (13.8)

"This is an additional equation on the matching surface. With the model's own field
content (Nb = 5, nf = 4, Proposition 5.8) fixed before the test, the relation agrees with
the observed MP for about half of the gauge-matched points of one class and essentially
never in the others. That class is the one containing row V11 of Table 16 (full-rank
Yukawas, E/N = 4/3). The observed Planck mass is therefore a held-out class-selection
criterion rather than a fitted parameter or a parameter-free prediction. A joint fit that
also imposes the common-radius area relation $\kappa_{2}/\kappa_{3} = \chi_{2}/\chi_{3}$ has not been carried out."

### Yukawa rule and leptons — copied exactly

Nonzero first-generation masses require full-rank Yukawa matrices if only leading-order
couplings are retained. Under the overlap rule of §6.6 four matching classes have full rank;
a strict per-torus closure rule instead removes the charged-lepton and neutrino couplings,
so the full-rank selection is conditional on the overlap rule. For the charged leptons the
declared periodised Gaussian rule is

> Yij = $c_{(i-j) mod 3}$,   ck = $\Sigma_{\ell\in\mathbb{Z}} e^{-\pi\kappa2(k/3+y+\ell)2 + 2\pii(k/3+y+\ell)w}$,   $\kappa^{2} > 0$.   (13.9)

"The sum converges absolutely. The discrete Fourier matrix diagonalises this circulant
matrix: with $\omega = e^{2\pii/3}$ its eigenvalues are $\lambdan = \Sigma_{k=0}$^{2} ck $\omega^{nk}$, and since the
Fourier matrix is unitary the singular values are |$\lambdan$|. Ordered as $s_{1} \leq s_{2} \leq s_{3}$, they give
the mass ratios $s_{1}/s_{3}$ and $s_{2}/s_{3}$. The fit reproduces the observed charged-lepton ratios
with **$\kappa^{2} \simeq 0.5724$ and $w \simeq 0.2429$** at the declared separation; uniqueness in the
separation y is not established."

The Dirac-neutrino Yukawa lives on the same torus with the same circulant structure.
Every circulant matrix is diagonalised by the same Fourier matrix, so the charged-lepton
and neutrino left rotations coincide up to a permutation and phases, and the leading-order
lepton mixing matrix is a permutation (angles $0^\circ$ or $90^\circ)$. Full rank alone leaves the
lightest mass free. "The model therefore makes no prediction for neutrino masses or
lepton mixing; the effective Majorana mass vanishes for the declared Dirac sector."

### Quarks — what fails

Two leading-order routes tested against criteria fixed in advance. A Wilson-line-consistent
geometric overlap rule does not reproduce quark masses and mixing. A shared
heavy-partner correction with seven parameters and one remaining degree of freedom gives
**$\chi^{2} = 373$ against a pass threshold fixed in advance**, and the geometrically fixed variant
leaves the light Yukawas unchanged at tree level. "Quark masses and the CKM matrix are
therefore not reproduced and lie outside the model's present predictive scope."
A topology-only scan of the declared vacuum family with |n| $\leq 5$ finds **4236 admissible
configurations and 126 intersection patterns**. They reduce to two leading-order quark
structures: (1) relevant families share the third torus, matrices can have full rank, but
consistent overlap rules retain the up/down mirror and cancel the required CP structure;
(2) left- and right-handed families occupy different tori, leading blocks have rank one,
leaving the first generation massless. "Thus the quark layer is exhausted within the
declared vacuum templates. Going further would require either changing those templates
or adding subleading Yukawa structure with more adjustable parameters than the
observables used here; neither extension is part of the present reconstruction."

### What selects the representative? (negative results)

Tested modular self-dual points, low-complexity complex-multiplication points and diagonal
cusp limits do not select the measured couplings subject to the other cuts; these tests
exclude the tested candidates, not every source-selection mechanism. A measure calculation
with density proportional to $\prod_{i} \chii^{-2}$ on $\chii \geq 1$ gives a broad distribution of $\sin^{2}\thetaW$
when only $\alpha$em and $\alphas$ are inputs; for the V1 winding data its 5th, 50th and 95th
percentiles are **0.117, 0.309 and 0.488**, and the observed value lies near the 24th
percentile. "This is a consistency test; it neither fixes the moduli nor converts the matching
inputs into predictions."

### Retained outputs (§16.5, Table 19) — input vs output, stated plainly

| Quantity | Value | INPUT or OUTPUT (paper's own classification) |
|---|---|---|
| Gauge couplings | three observed inputs | INPUT — matched exactly in all ten classes; no coupling prediction |
| Selected class | row V11, E/N = 4/3, NDW = 3 | OUTPUT of selection — gravity–gauge relation with Nb = 5, nf = 4; MP reproduced for about half of gauge-matched points |
| Matching scale | M∗ $\approx 5.8 \times 10^{16}$ GeV | OUTPUT — selected point with charged-lepton fit; heavy-state threshold at M∗ |
| Top mass | mt ≲ 173.0–173.9 GeV | OUTPUT, CONDITIONAL — heavy-state threshold at M∗ (plausible, not proved) |
| $\tan \beta$ | 1.2–1.5 | OUTPUT, same threshold option |
| Top mass, option (a) | mt ≲ 174.31 GeV | OUTPUT, CONDITIONAL — strict D-term boundary; global infimum M∗ $\geq \mu\infty = 5.906\times10^{8}$ GeV UNPROVED |
| Charged leptons | observed ratios | OUTPUT under declared circulant Gaussian rule, $\kappa^{2} \simeq 0.5724 ($App. H: numerical diagnostic; truncated Gaussian sums at selected separations, not a uniqueness certificate) |
| Axion | fa = M∗, ma $\approx 0.1$ neV | OUTPUT under declared identification fa = M∗ |
| Dark matter | axion is all of it | CONDITIONAL OUTPUT — uniform initial angle $\thetai \approx 1.6\times10^{-3}$ declared as initial data |
| Quarks, CKM | not reproduced | FAILED — leading-order tests with criteria fixed in advance fail; outside present predictive scope |
| Neutrino masses, PMNS | not predicted | OUT OF SCOPE — shared circulant eigenvectors give permutation mixing |

"None of these rows certifies a simultaneous solution of all constraints with interval
arithmetic."

**Axion mass and abundance (§16.5).** With fa = M∗ $\approx 5.8\times10^{16}$ GeV, the QCD
relation of [61] gives ma $\approx 5.70$ µeV $\times 10^{12}/(5.8\times10^{16}) \approx **0.1$ neV**. At such a large
decay constant a typical misalignment angle overcloses the universe; the observed
dark-matter density requires **$\thetai \approx 1.6\times10^{-3}$**. "The model does not derive this angle;
it is declared as initial data, and the statement 'the axion is all of the dark matter' is
conditional on it." Experimental sensitivity at this mass depends also on E/N and the
photon coupling; no exclusion or projected sensitivity is inferred here.
Under option (a), the matching scale lies in $[5.906\times10^{8}, 4.6\times10^{10}]$ GeV, conditional on
the unproved lower bound, and the same relation gives

> $(5.70\times10^{12})/(4.6\times10^{10})$ µeV ≲ ma ≲ $(5.70\times10^{12})/(5.906\times10^{8})$ µeV,   (16.5)

or approximately **124–9651 µeV**; "the endpoints reverse because ma $\propto$ fa${}^{-1}$. For
randomly sampled initial angles in a no-inflation history this branch gives a dark-matter
fraction of only 0.001–0.22. This interval is an alternative branch, not one of the reported
outputs, and it is not an experimentally allowed band."

**Domain walls and strong CP (§16.5).** Selected class has NDW = 3. If the initial
angle is uniform over the observable universe (as the dark-matter statement assumes), no
string–wall network forms there. If instead a wall network forms in an axion-bearing
full-rank class, the bias needed to remove the walls must be compared with the maximum
bias compatible with |$\bar{\theta}$| < $10^{-10}$. With wall tension 8mafa${}^{2}$ and the quality ceiling
$3.25\times10^{-15}$ GeV${}^{4}$, the required bias exceeds the ceiling over the sampled range of option
(a), except for a marginal strip near the lower scale where the mismatch is a factor of
about 1.2, within the order-one uncertainty of the wall constants. "That wall-forming
branch is therefore disfavoured; it does not solve the wall problem." The fixed-reference
discussion of §16 assumes a contracting history that keeps the angle uniform; transferring
that assumption to the selected class requires the same background, thermal and
initial-data conditions; wall-forming and wall-suppressing histories cannot both be used
without stating which is assumed. The class with no QCD axion avoids axion walls but
requires a small initial $\theta$QCD and supplies no axion dark matter. No additional
dark-matter component is identified.

**Neutrinos and vacuum selection (§16.5).** Charged-lepton and neutrino Yukawa
matrices share circulant eigenvectors, so leading-order lepton mixing is a permutation;
neutrino masses, ordering, mixing outside present predictive scope. Neither rank count nor
Higgs stability alone gives a unique neutrino spectrum or unique vacuum; class selection
comes from the gravity–gauge relation.

**Reader's HLRE note on the mt bound:** the bound mt ≲ 173.0–173.9 GeV is an
input-dependent conditional estimate (Track E, I0 — the same measured couplings and the
declared threshold are used in its construction; the heavy-state threshold is introduced to
fit/allow larger M∗ and is "plausible but not proved"). Grade D as a claim about the world;
as a *conditional* statement ("IF the heavy-threshold option holds, THEN mt ≲
173.0–173.9 GeV") it is a correctly stated conditional whose antecedent is open. The
fixed-reference V1 bound mt $\leq 172.89$ GeV (Prop. 9.19, §16.3) is a different, V1-specific
number and "is not a class-independent mass bound". Do not conflate the three numbers:
172.89 (V1 fixed point), 174.31 (option (a), unproved infimum), 173.0–173.9 (option (b),
heavy threshold).

## (d) Yang–Mills interface and mass gap (§17)

**What is claimed:**

- The torus model supplies a positive closed-walk action at the quark-decoupling scale
  (Thm 6.10) with bare coupling $\beta = 6/g^{2} \simeq 21.5 ($Prop. 10.2; §17.4 uses $\beta = 21.49$ for
  the vortex condition), and a finite colour carrier (SU(3) as determinant-one subgroup of
  the M3(C) block; 18-link retained checkerboard carrier with exactly defined induced
  retained action). These are declared finite objects.
- **Theorem 17.1 (conditional):** IF the vortex condition (VF) holds (17.2), THEN
  |$\langleW(C)\rangle$| $\leq 2e^{-\rhoAC} (17.3)$ and $V(r) \geq \rhor$ — i.e. confinement / area law with string
  tension $\geq \rho$. Proof via Tomboulis–Yaffe (Kanazawa form).
- **Lemmas 17.2–17.4 (conditional chain):** IF the block-spin flow condition (RG) holds
  (17.6), THEN (VF) follows $(\rho = a/(2b^{2n}), p0$ = mn), hence confinement.
- Transferable Wilson results: uniqueness + exponential decay for $\beta < (1/2)\log(19/17)$
  (Dobrushin, 18 influence neighbours) for every SU(N); conditional continuum implication
  (qa = $e^{-aM} + o(a)$ + compatible RP + matrix-element convergence $\Rightarrow$ continuum
  generator gap $\geq M)$; heat-flow log-Sobolev criterion, renormalised-potential identities,
  pinned Poincaré Riccati bound, pinned joint-measure structure valid for compact groups
  with positive Ricci curvature with changed constants (SU(3): Ric = (1/4)Killing > 0).
- Area law for $\beta \leq 0.3925$ now has a self-contained proof (exact slab reduction, centre
  symmetry, single-site Dobrushin coefficient, Arb certificate: 49,372 cells, minimum slack
  $9.7\times10^{-9})$; no longer cites Durhuus–Fröhlich / Föllmer.

**What is open:**

- **Hypothesis 3 — the physical SU(3) mass gap — is open.** "No rigorous method for
  that crossover is known" (weak coupling $\beta \simeq 21$ through the crossover to the confining
  regime). Most certified constants in the follow-up paper are for SU(2); the SU(3) gap
  remains open.
- **The source-to-Wilson universality bridge is open** (not a consequence of the torus
  action's positivity; perturbatively holds by Reisz's theorem only).
- **The Wilson intermediate-window estimate is open** — the environment-decorrelation
  bound (E) (17.8) is "an open target"; numerical evidence only (cross-link form per pin
  $-3.75 \pm 0.30$, $-4.18 \pm 0.64$, $-3.71 \pm 0.47$ at $\beta = 3$, t = 0.2, L = 4, 5, 6, flat in volume).
  Still open on the blocked-RG side: identity of the blocked kernel, a uniform interacting
  floor m0, a certificate for the weak-to-strong crossover.
- **(VF) at the physical coupling is open**, "which lies in the same window as the mass
  gap, together with the source-to-Wilson bridge". No known argument derives (VF) from
  Hypothesis 3. A mass gap alone does not imply an area law (gap without area law occurs
  with fundamental matter [51]).
- **SU(2)-specific constants must be recomputed for SU(3):** Haar-point constant
  $8/(9\pi)$, certified gap for $\beta < 0.24$, area-law certificate for $\beta \leq 0.3925$, weak-coupling
  threshold $\betaw$. "No SU(2) theorem or numerical constant in that paper is an SU(3)
  mass-gap result."
- **Range of couplings:** the open window is the intermediate-coupling window containing
  the physical point $\beta \simeq 21$–21.5. The certified regimes are strong coupling $(\beta < 0.24$ gap;
  $\beta \leq 0.3925$ area law) and the Dobrushin regime $\beta < (1/2)\log(19/17) \approx 0.053$; the
  weak-coupling chain starts at $\beta \simeq 21.5$ and must cross the window to the confining
  regime. The paper's §18.3 summary: "Long-distance confinement of the Wilson SU(3)
  theory follows from the vortex condition of §17.5, which a renormalisation flow through
  the intermediate couplings would establish; the mass gap is open in the same range of
  couplings."

## (e) Scope and relation to existing theories (§14) — summary

**What the paper says it explains (Table 10, §14.1):** dimension 4 + one time axis/arrow +
lattice signature (1,3) + Euclidean invariance of the Poisson average (Lorentz
reconstruction conditional on Hypothesis 4); conditional two-derivative Einstein tensor
form, no local graviton mass vertex, GR light-bending tensor ratio, $\Lambda$ as integration
constant (needs Axiom M + low-energy derivative expansion); gauge group, partial EW
breaking, asymptotic freedom; Maxwell theory in comparison models (Hypothesis 1 for the
physical Wilson field); chirality, charge quantisation in units of 1/6, anomaly freedom, no
extra massless U(1); Friedmann expansion under dynamical-metric assumptions (redshift
kinematical; singularity bounce as numerical illustration); black-hole entropy A/4G under
cited common spectral regularisation (Page curve as finite numerical illustration); $\Lambda$ as
unfixed integration constant; QCD axion, all of dark matter only if a uniform initial angle
is declared.

**What it says it does NOT explain / does not fix (Tables 12–13, §14.2–14.3, §16.4):**
couplings, masses, mixings (continuous moduli + amplitude prescription free, Thm 6.17);
$\Lambda$ value + radiative stability; neutrino masses/mixing/smallness (permutation mixing at
leading order; $m\beta\beta = 0)$; scale hierarchies (naturalness not a consistency condition);
primordial perturbation amplitude (open external input, $\sim10^{16}$ GeV seed needed);
primordial gravitational waves, horizon problem, baryon asymmetry (not addressed);
KK-scale thresholds $\sim10^{17}$ GeV (experimentally inaccessible); quark masses + CKM,
lepton mixing, $\sin^{2}\thetaW$, v, $\Lambda ($not reproduced — outside present predictive scope, §13.7);
number of generations (vacuum data); (MP/$\Lambda)^{2} \approx 322 ($circular — not counted as a
prediction). Proved boundaries (Table 12) are quantities with several axiom-satisfying
solutions at different values — "such a value cannot be computed from the model. Fixing
it would need a new principle."

**Relation to prior work (§14.5, Table 14; §18.2):** see register entries 14.11–14.12.
Key points for the comparison: the paper positions itself against string/brane toroidal
compactification (same intersection-number calculus, different origin: node data, spacetime
counted; finite 76-copy catalogue vs open configuration space), causal sets (shares Poisson
sprinkling + count = volume; observables are configuration averages, removing the swerves
problem), induced gravity / Sakharov (G induced by node fields; gravity–gauge bridge
fixes cutoff $\approx 18 \ellP)$, and constructive lattice gauge theory (Hypotheses 1–3 are its open
problems). It explicitly does NOT import: noncommutative-torus algebra, spectral action,
$N \to \infty$ matrix limit, CDT triangulation measure, Q-lattice KMS/Galois structure,
Ascárate's spectral triple/dynamics. **No other D4-based emergent-spacetime approach is
named or compared in this range** (see 14.12); the paper's D4 object is the D4 root system
(its A3 spatial section is a cuboctahedron — App. C.3 stresses the standalone 12-vertex
cuboctahedral graph is NOT a model choice).

## (f) Conclusion (§18) and appendices

### §18.1 Collected low-energy Lagrangian — copied exactly

After the heavy $U(1)'$ and other cutoff-scale modes have been integrated out, the single
effective expression used for the low-energy discussion is

> Leff = $(1/(16\pi$Geff$))(R - 2\Lambda) - (1/4) G^{A}$_${\mu\nu} G^{A\mu\nu} - (1/4) W^{a}$_${\mu\nu} W^{a\mu\nu}$
>   $- (1/4) B_{\mu\nu} B^{\mu\nu} + \Sigma_{\psi} i\bar{\psi}\gamma^{\mu} D_{\mu} \psi$ + LY + $\Sigma_{r=u,d}$ |$D_{\mu} H_{r}$|${}^{2} - V($Hu, Hd)
>   + (a/fa$)(\alphas/(8\pi)) G_{\mu\nu} \tilde{G}$^${\mu\nu} + (E/N)(\alpha$em/$(8\pi)) F_{\mu\nu} \tilde{F}$^${\mu\nu}$ + Lopen.   (18.1)

with the Yukawa term explicitly

> LY = $-( \bar{Q}L$ Yu $\tilde{H}u$ uR + $\bar{Q}L$ Yd Hd dR + $\bar{L}L$ Ye Hd eR + $\bar{L}L Y\nu \tilde{H}u \nuR$ + h.c. ).   (18.2)

Conventions: $G^{A}$, $W^{a}$, B are the low-energy SU$(3)c \times$ SU$(2) \times U(1)Y$ gauge fields;
Y(Hu) = Y(Hd) = +1/2 and $\tilde{H}u = i\sigma_{2}$Hu∗, so no independent He or $H\nu$ is present; QL, LL
left-handed doublets; uR, dR, eR, $\nuR$ right-handed singlets. After EW breaking the photon
is $A\mu$ = sW $W^{3}\mu$ + cW $B\mu$, $F^{em}$_${\mu\nu} = \partial\muA\nu - \partial\nuA\mu$; $\tilde{X}$^${\mu\nu} = (1/2)\varepsilon^{\mu\nu\rho\sigma}X_{\rho\sigma}$.
The heavy $U(1)'$ is not part of this infrared expression; the second axion operator is
explicitly the electromagnetic one, $F_{\mu\nu}\tilde{F}$^${\mu\nu}$, not an unspecified EW-basis field strength.

**Determination of coefficients (Table 20):**

| Term | Origin | Determination of coefficient |
|---|---|---|
| Einstein–Hilbert | Axiom M, relational diffeomorphism theorem, Lovelock classification | Form derived conditionally; Geff and $\Lambda$ are NOT fixed |
| Gauge kinetic terms | History-algebra commutant, induced-action theorem, Maxwell/YM external inputs | Groups + tensor form derived in finite model; gs, g2, gY require matching/vacuum input |
| Fermion kinetic term | Axiom D + finite chiral module | Field content + anomaly cancellation derived; continuum normalisation / source map OPEN |
| Higgs kinetic + potential | EW stabiliser theorem + D-term boundary | Symmetry-breaking form derived; full non-Abelian L3/L4 + polymer control OPEN; numerical quartics are input-dependent |
| Yukawa terms | Finite intersections + amplitude rule | Ranks depend on overlap prescription; masses + mixing fits require additional inputs |
| Axion term | Anomaly traces + Green–Schwarz cancellation | E/N exact for each catalogue row (2/3 for V1, 4/3 for selected class V11); fa = M∗ and ma are declared identifications / numerical outputs |
| Lopen | Source-to-continuum + Wilson/YM bridges | NOT YET DERIVED; collects the explicitly open interfaces |

"Equation (18.1) is therefore an effective finite/conditional summary, not a claim that an
unrestricted microscopic source has already produced a continuum action."

### Appendix C.1 — Declared-inputs catalogue (copied in full)

- The source exponent **$\beta = 1$** is part of the declared source kernel. Its coincidence
  with a pole of $\zeta(\beta)\zeta(\beta - 1)$ is a remark, not a derivation.
- The mechanism for three chiral generations, charge quantisation and anomaly
  cancellation is derived in the finite matter construction, but the selected vacuum and
  generation count are vacuum data.
- Couplings, masses and the cosmological constant are not fixed by the minimal axioms.
  Their numerical reconstruction requires the declared finite catalogue, continuous moduli
  and matching inputs.

### Appendix D.1 — External-theorem dictionary (every external theorem the paper leans on, and what it is used for)

| § | External theorem / input | Used for (paper's statement of use + hypothesis the model must supply) |
|---|---|---|
| D.1.1 | Penrose–Pisztora local uniqueness + large deviations [87] | Controls largest/crossing cluster + boundary intersection (surface-order large-deviation estimate) in the stationary constant-radius Boolean–Poisson comparison model in $R^{4} (\lambdar^{4}$ supercritical; Palm law for insertions). To deduce reconnection tail $P(\rhox > \ell) \leq$ Ce^${-c\ell} (D.1)$ one must additionally prove ${\rhox > \ell} \subseteq$ local-uniqueness failure event (finite-component exceptions separately controlled) + graph/clique event measurable w.r.t. same Boolean configuration. "None is presently proved for the literal marked-torus source, so the homology conclusion remains conditional." |
| D.1.2 | Antal–Pisztora chemical distance [88]; Liggett–Schonmann–Stacey domination [89]; Timár boundary connectivity [90] | Replace long detours by controlled paths; concentrate bad clusters; attach boundary pieces. Each needs model-specific identifications (coarse-graining to good Boolean–Poisson boxes $\to$ occupied finite-range lattice field; stationary finite-dependence good-box field above domination threshold; particular primal/dual graph pair + boundary notion). "They do not determine the continuum energy density, and the paper does not claim these hypotheses for the unrestricted source." |
| D.1.3 | Iwaniec–Lutoborski integral estimate [91] | Homotopy operators + integral estimates for differential forms on Euclidean domains. Uniform bound for weighted discrete filling operator on random cells is an additional assertion (domain, exponent, weight, discretisation comparison, uniform geometric constants). L1 endpoint + weighted Schur estimate "cannot be imported without an explicit theorem and parameter match$\dots$ the bibliography alone is not their certificate." |
| D.1.4 | Osterwalder–Schrader reconstruction [14, 15]; Osterwalder–Seiler reflection positivity [51] | OS reconstruction from E0–E4 (tempered regularity with corrected 1975 growth bound; full Euclidean covariance incl. spin reps; RP for every finite positive-time test sequence; permutation/graded symmetry + reality; clustering; $S_{0} = 1$, Hermiticity, reflection/conjugation compatibility). Finite scalar RP proves only E2 for declared finite/comparison measures; annealed O(4) covariance addresses part of E1. Uniform temperedness, infinite-volume limit, clustering, complete non-scalar covariance, fermionic graded positivity remain assumptions. OS–Seiler supplies E2 for Wilson lattice measure, not for unrestricted Poisson–torus measure. "Consequently reconstruction is conditional and does not itself prove a mass gap." |
| D.1.5 | Lovelock's 4-D classification [18] | Classifies natural local rank-2 tensor on smooth 4-D pseudo-Riemannian manifold (diffeomorphism-covariant concomitant of g, $\partialg, \partial^{2}g$; symmetric, divergence-free, linear in second derivatives) as aG$\mu\nu$ + bg$\mu\nu ($up to topological term). Applied only after assuming smooth local two-derivative continuum expansion + diffeomorphism covariance. "Finite graph locality does not prove those assumptions. The continuum metric, its variational principle and suppression of all nonlocal/higher-derivative terms therefore remain explicit premises"; Bianchi identity + matter conservation make b an integration constant in the unimodular equation |
| D.1.6 | Weinberg–Witten [20]; Atiyah–Singer / Riemann–Roch [29] | Weinberg–Witten used only as no-go test for fixed-background emergent graviton (massless spin > 1 with Lorentz-covariant conserved stress tensor), not as claim all gravity theories impossible. Atiyah–Singer index (torus case: Riemann–Roch) identifies chiral index with integral gauge flux/Chern character; used to rule out chirality generated solely by rotation cover and to count gauge-induced zero modes; finite flux/bundle data checked separately |
| D.1.7 | Rényi's Poisson characterisation [12]; Poisson mapping theorem [13] | Source identification: equality of certified void probabilities identifies Poisson intensity measure (void probability $\exp(-$µ(A))); then source pushed forward to continuum. Does NOT identify a hidden marked/dynamical completion (non-identifiability example shows why). Mapping theorem = source-to-continuum push-forward used in main text; "not an additional dynamical claim" |
| D.1.8 | Kotecký–Preiss polymer criterion [47] | Sufficient condition for absolute convergence of logarithmic cluster expansion: $\exists a(\gamma) \geq 0$ with $\Sigma_{\gamma'≁\gamma}$ |$z(\gamma')$|$e^{a(\gamma')} \leq a(\gamma) (D.2)$; overlap-only + $a(\gamma) = a_{0}$|$\gamma$| $\Rightarrow$ site bound $\sup_{x} \Sigma_{\gamma∋x}$|$z(\gamma)$|$e^{a0|\gamma|} \leq a_{0}$. Controls expansion; spatial decay, thermodynamic limit, physical mass-gap transfer need additional uniform estimates. Activities/domains/constants in Villain + EW applications must still be certified |
| D.1.9 | Tomboulis–Yaffe inequality + SU(N) form (Kanazawa [72, 74]) | |$\langleW(C)\rangle$| $\leq 2(1 - F[0])^{AC/(L\muL\nu)} (D.3), F[0] = N^{-1}\Sigma_{k=0}$^${N-1} Z[k]/Z$, for rectangular loop in (µ,$\nu)$-plane, nonzero N-ality representation. Proof moves stack across C by centre change of variables, doubles rectangle with Schwarz inequality for site-RP measure. Used in Thm 17.1 for Wilson action (site RP); "it is not used for the induced action of the model" |
| D.1.10 | Fröhlich–Spencer [35]; Hartman–Watson identity [38] | Fröhlich–Spencer rewrites weakly coupled compact Abelian theory as dual sine–Gordon/monopole gas; supplies convergent expansion for flux-variance lower bound. Hartman–Watson: $I\nu(\beta)/I_{0}(\beta) = E[e^{-\nu2T/2}] (D.4)$ turns each Fourier mode into Gaussian mixture with inverse variance 1/T; used for exact posterior-defect probabilities; changes of variables, finite sums, interval bounds carried out in paper |
| D.1.11 | Combes–Thomas [43]; Nielsen–Olesen [44] | Combes–Thomas gives exponential decay of resolvent of uniformly positive finite-range operator away from spectrum; applied to charged-vector covariance at fixed EM background, gap condition mW${}^{2} - 2e\delta > 0$. Nielsen–Olesen identifies unstable charged-vector mode when eB > mW${}^{2}$; used only to restrict admissible magnetic-field window. Neither proves source-to-continuum bridge or unconditional mass gap |
| D.1.12 | Spectral homogenisation (Armstrong–Venkatraman [39]); Akcoglu–Krengel [40] | Armstrong–Venkatraman: scalar graph Laplacian on Poisson point clouds, spectrum convergence. Akcoglu–Krengel: ergodic theorem for stationary integrable superadditive processes. Applying to face-flux/cochain energy is NOT automatic: operator, scaling, boundary conditions, comparison to scalar problem, additivity inequalities, integrability must be supplied. "These references motivate the homogenisation route but do not, without those identifications, certify the photon/cochain limit or its uniform coercivity." |
| D.1.13 | Dobrushin [70]; Föllmer [71]; Jentzsch positive-operator theorem [31] | Dobrushin uniqueness (incl. Wasserstein/Lipschitz form): influence matrix with row sums < $1 \Rightarrow$ unique Gibbs state + exponential covariance decay. Föllmer covariance estimate converts contraction into quantitative slab bound. Applied to temporal-gauge conditional measure with computed Haar–Wasserstein coefficient + explicit area-law inequality. Jentzsch: simple maximal eigenvalue for positive compact transfer operator; used to identify vacuum eigenvector before spectral-gap estimate. Require positivity, compactness, influence bounds displayed in paper |
| D.1.14 | Balaban [45, 46]; Durhuus–Fröhlich [94]; Reisz [49]; perturbative matching [48, 93] | Balaban gauge-covariant RG estimates provide form of large-field + polymer bounds for finite sequence of lattice blocks. Durhuus–Fröhlich reduction identifies $3-D S^{3} \sigma$-model description of 4-D SU(2) area-law channel in analytic window. Reisz's theorem applied graph by graph only when gauge-fixed lattice action is translation invariant + local (or fast uniform decay), vertex functions periodic + smooth in Brillouin momenta with regular continuum limit, propagator denominators have prescribed continuum scaling + uniform lattice lower bound + no extra zeros/doublers; after subtractions Reisz UV degree negative for graph + every Zimmermann subspace; gauge fixing/ghosts/mass-IR regulators must preserve these properties. "The present induced closed-walk action has not been shown to satisfy this complete list uniformly in the cutoff. Reisz power counting therefore gives a conditional perturbative comparison, not an established universality theorem for that action." Published three-loop SM beta functions + matching formulae remain external numerical input for Higgs-stability interval |
| D.1.15 | Prokhorov tightness; Kolmogorov extension [55] | Different tasks, not an automatic two-step argument. Prokhorov: Borel probabilities already on one fixed Polish space; tightness w.r.t. compacts $\Rightarrow$ relative weak compactness; finite-dimensional tightness alone insufficient on function/distribution space. Kolmogorov: finite-product laws, permutation-invariant + projectively consistent $\Rightarrow$ measure on product $\sigma$-algebra; does NOT by itself put measure on smaller continuous-path/Sobolev/tempered-distribution subspace nor make it Radon in stronger topology. In Thm 12.1 measures assumed Borel on common Polish Sobolev-distribution space, so Prokhorov applies directly, Kolmogorov unnecessary. Kolmogorov used only for construction specified solely by finite-dimensional laws; support + regularity must then be proved separately |
| D.1.16 | Källén–Lehmann / Stieltjes [52, 53]; Newton–Kantorovich [95] | Källén–Lehmann: RP two-point function is Stieltjes transform of positive spectral measure; used as consistency test for averaged Schwinger function; "a numerical fit is not itself a proof of a gap". Newton–Kantorovich contraction in standard local form (inverse-Hessian + Lipschitz bounds $\Rightarrow$ unique solution in certified ball); applied separately in each weak-coupling block, radius + constants recorded |
| D.1.17 | Mayer–Vietoris [85]; Weyl/Hodge decomposition; Poincaré inequalities [86] | Mayer–Vietoris computes change in homology after vertex star (cone) attached; reduces possible new $H_{1}$ class to disconnected link components. Discrete Weyl/Hodge splits cochain into exact + coexact + harmonic; graph energy estimated on orthogonal complement of kernel. Large-scale Poincaré bounds 1-chain by coboundary after harmonic part removed. Standard deterministic statements; random constants + percolation hypotheses making them uniform are the conditional inputs |
| D.1.18 | Cauchy–Crofton [92]; Stokes; Gauss–Bonnet; reflection chessboard estimates [33, 34, 96] | Cauchy–Crofton converts length/area of filling into average of intersection counts (flux-filling bound). Stokes turns integral of curl on torus into boundary flux; Gauss–Bonnet gives zero total Gaussian curvature for embedded torus (the two no-chirality checks). Reflection positivity yields chessboard (reflection-copy) inequality, turning one-block bound into volume-uniform polymer bound. "None of these identities supplies the missing random connectivity or source-selection assumptions." |
| D.1.19 | Von Mises–Fisher [97]; Kato [98]; maximum-principle estimates | Von Mises–Fisher variance estimate bounds change of single $S^{3}$ spin under neighbour tilt; yields Dobrushin coefficient $(d-1)\beta$. Kato's inequality + parabolic maximum principle control heat-flow gradient/Hessian differential inequalities; Riccati comparison solved explicitly. Analytic inequalities applied to displayed finite-dimensional operators, "not additional assumptions about the source" |
| (also cited in text) | Elementary tools: Tonelli, Cauchy–Schwarz, spectral theorem, Schur product theorem, Sherman–Morrison | Used in standard forms; finite-dimensional applications written out. "Every use of an external input ends in a displayed inequality, a finite certificate or a named conditional hypothesis, so the model-specific step is always visible." |

## (g) Every quantitative prediction or number in this range, with stated inputs

(Numbers are quoted from the paper; this reader did NOT independently recompute any of
them. "Input" = measured/declared value fed in; "output" = value produced under the
stated assumptions.)

**§11:** p ≲ 3.5 (node units, quenched-average spectral consistency cutoff); $p \approx 2\pi$/rc
(cutoff scale where violated); mean degree $81 \to 290 ($normal $\approx 25)$ under global-count
det^+1.5 weight; $\chi^{2} = 384$, 391 for $p^{2} \leq 33$, 13 dof (control run, two seeds); matter
weighting reduces violation ~40%; one seed $\chi^{2} = 16.2$ for $p^{2} \leq 16 ($consistent, not
reproduced); two of three seeds $\chi^{2} = 30.1, 31.6$ for $p^{2} \leq 16 ($violate).

**§$12:** \eta = \pm1/2 ($RP completion pair, (12.7)); $(12.8) \Sigma n$!|an|${}^{2}\eta^{n} \geq 0$ for $\eta = 1/2$;
ten symmetric coframe coordinates / rank-ten mixed Hessian (metric completion pair);
collision integral $\int_{0}$^$\varepsilon r^{3}e^{A/r}$dr divergent for $w(r) \geq$ Ar${}^{-2}$; fourth derivative changes
by $24\lambda$ on adding $\lambda$‖$\psix$‖${}^{4}$.

**§13:** 49 one-step marks $(7\times7)$; 24-state S4 fibre; $\sigma_{1}(2) = 3$ determinant-2 Hecke
cosets; entropy ratio R = 1.05 (canonical finite completion, induced $\kappa)$; V1 shapes
$\chi = (2.5, 5, 3.2)$; ki = $-0.593$, $-0.349$, $-0.961$; dipole ratios 1.69, 2.86, 1.04
(range 1.4–3.3 over bridge vacua with natural matter content); fraction of shape line with
|k| < 0.1: 0.04, 0.12, 0 (three tori); |$\ln(\chi/\chiV1)$| $\leq 2$ variation range.

**§13.7/§16.5 (inputs $\to$ outputs):** INPUTS: $\alpha$em${}^{-1}($MZ) = 127.95; $\sin^{2}\thetaW($MZ) = 0.23122;
$\alphas($MZ) = 0.1179 (matching); $\alphas = 0.1180 ($Higgs-stability evaluation — "difference from
the matching input $\alphas = 0.1179$ is an input sensitivity"); mt = 172.57 GeV $(\LambdaI$
evaluation point); Nb = 5, nf = 4 (gravity–gauge selection, fixed before test); $\kappa^{2} \simeq 0.5724$,
$w \simeq 0.2429 ($lepton fit, at declared separation; uniqueness in y not established);
$\thetai \approx 1.6\times10^{-3} ($declared initial angle, selected class). OUTPUTS: exact matching in all
ten classes; $\mu\infty \simeq 5.906\times10^{8}$ GeV; $\LambdaI \simeq 4.6\times10^{10}$ GeV (at mt = 172.57, $\alphas = 0.1180)$;
mt ≲ 174.31 GeV (option (a)); mt ≲ 173.0–173.9 GeV, $\tan \beta = 1.2$–1.5 (option (b));
M∗ $\approx 5.8\times10^{16}$ GeV (selected point, heavy-threshold option); ma $\approx 0.1$ neV (fa = M∗);
axion interval under option (a): ma $\approx 124$–9651 µeV, M∗ $\in [5.906\times10^{8}, 4.6\times10^{10}]$ GeV;
dark-matter fraction 0.001–0.22 on that branch (random angles, no-inflation history);
$\sin^{2}\thetaW$ percentiles (measure $\prod\chii^{-2}, \chii \geq 1, V1$ winding data): 5th 0.117, 50th 0.309,
95th 0.488; observed value near 24th percentile; quark shared heavy-partner correction:
$\chi^{2} = 373 (7$ parameters, 1 remaining dof, vs pass threshold fixed in advance — FAIL);
topology scan |n| $\leq 5$: 4236 admissible configurations, 126 intersection patterns;
wall quality ceiling $3.25\times10^{-15}$ GeV${}^{4}$; marginal wall strip mismatch factor ~1.2.

**§14:** $k = d \ln \alpha/d \ln \chi = 0.25$–0.96 (node-shape coupling); $w = -0.9$ would give
|$\dot{\alpha}/\alpha$| $\sim 10^{-11}$ yr${}^{-1}$ vs atomic-clock bounds ~$10^{-18}$ yr${}^{-1} ($factor $10^{6}$–$10^{7})$; ∆$\alpha/\alpha \approx k\sqrt$|$\Omegak$|;
(∆G/G)/(∆$\alpha/\alpha) = 1.4$–3.3, same sign; |∆$\alpha/\alpha$| < $10^{-6} \Rightarrow$ |$\Omegak$| < $3\times10^{-12}$; shear
$\sigma/H \approx 0.69 \Omegak ($Bianchi III); $\delta \sim 10^{-5}$; $\thetai \approx 1.6\times10^{-3} ($selected class, declared);
cutoff $\approx 18 \ellP ($gravity–gauge bridge); Poisson count fluctuations $\sim10^{-120}$ on
cosmological scales; GUT $\taup \sim 10^{34}$–$10^{36}$ yr (comparison value, not the model's).

**§15:** thermal winding gas: ns $- 1 = -1$; matter bounce: $w \approx -0.0029$, ns = 0.9649,
r = 24cs, $r < 0.036 \Rightarrow$ cs < $1.5\times10^{-3}$, As = $2.1\times10^{-9}$ needs HB $\approx 10^{12}$–$5\times10^{13}$ GeV vs
node-density bounce HB $\sim 7\times10^{16}$–$2\times10^{17}$ GeV (As six to seven orders too large);
node-scale thermal seed: $P \geq (\ellP/\varepsilon)^{4} = 9.5\times10^{-6}$, $\geq 5\times10^{3}$ times too large; single-clock
seed $V^{1/4} \approx 6\times10^{15}$–$1.4\times10^{16}$ GeV; cutoff $\Lambda = 6.8\times10^{17}$ GeV; fixed-reference
M∗ = $1.6\times10^{10}$ GeV; selected-class M∗ $\approx 5.8\times10^{16}$ GeV within factor ~4 of seed range
(no mechanism links seed to M∗).

**§16 (fixed-reference catalogue, Table 16 — all 16 rows):** V1 (8) M∗ $1.59\times10^{10}$ GeV,
$1/\alpha$∗ 38.95, ranks 2/2/1/1, E/N 2/3, ma 358 µeV, NDW 2 or 1, pass. $V2 (4) 8.13\times10^{10}$,
39.76, 2/2/1/1, 1/6, 70.1 µeV, NDW 2, borderline. $V3 (4) 5.45\times10^{11}$, 40.71, 3/3/3/3,
4/3, 10.5 µeV, NDW 3, fail. V4–V7 (4 each$) 9.80\times10^{11}$, 41.00, 2/2/1/1, E/N 5/3, 2/3,
$-1/3$, $-4/3$, 5.82 µeV, NDW 1, fail. $V8 (4) 1.37\times10^{12}$, 41.17, 2/2/1/1, 2/3, 4.16 µeV,
NDW 1, fail. $V9 (4) 1.07\times10^{13}$, 42.19, 2/2/1/1, 5/3, 0.53 µeV, NDW 1, fail. V10 (8)
$4.92\times10^{13}$, 42.95, 3/3/3/3, no axion, fail. $V11 (4) 3.43\times10^{14}$, 43.92, 3/3/3/3, 4/3,
0.017 µeV, NDW 3, fail (at fixed reference point). $V12 (8) 4.36\times10^{14}$, 44.04, 2/2/1/1,
no axion, fail. V13–V16 (4 each) 1.6–$9.3\times10^{15}$, 44.7–45.6, mixed ranks, E/N 2/3, 4/3,
ma 0.0006–0.0036 µeV, fail. Other §16 numbers: $\delta$th = 0.7–1.9% (residual two-loop
matching error; ∆$(1/\alpha) \approx 0.3$–0.8); axion coefficient 5.70(6)(4) µeV [61]; mt $\leq 172.89$ GeV
(V1, $\alphas = 0.1180; \pm0.32$ GeV per $\pm0.0009)$; observed mt $172.57 \pm 0.29$ GeV (consistent,
margin $1.1\sigma)$; second Higgs doublet $\sim1.6\times10^{10}$ GeV, $\tan \beta \approx 1.0$–1.2 (V1); $R = 1.05 \pm 0.08$
(black-hole entropy ratio); sky dipole Table 18 (see register 16.6); suppression exponents
∆Au = 6.4, ∆Ad = 3.0, ∆Aµ = 2.8, ∆Ae = 5.3; §$16.4: \pi - \thetai \approx 1.4\times10^{-3}$ for all dark
matter in V1 benchmark; typical angle ~4% of dark matter; $\delta\theta \approx 10^{-12}$ for w = 1/3
(spectator uniformity); w > 0.068 near bounce.

**§$17:** \beta \simeq 21 ($Hypothesis 3 point, Prop. 10.2); $\beta = 6/g^{2} \simeq 21.5 ($Prop. 10.2);
$\beta = 21.49 ($vortex-condition weight); $\beta < (1/2)\log(19/17) ($Dobrushin uniqueness +
exponential decay, 18 influence neighbours); certified SU(2) gap $\beta < 0.24$; SU(2) area-law
certificate $\beta \leq 0.3925 ($Arb certificate: 49,372 cells, minimum slack $9.7\times10^{-9})$;
Haar-point constant $8/(9\pi) ($SU(2)); SU(2) Ric = 2; SU(3) Ric = (1/4)Killing > 0;
cross-link form per pin at $(\beta = 3, t = 0.2)$: $-3.75 \pm 0.30$, $-4.18 \pm 0.64$, $-3.71 \pm 0.47$
(L = 4, 5, 6); 12 block-constant directions positive, 180 fine directions negative (24 block);
Villain $\betaV \geq 1.614 ($Thm 8.3, App. D.3.1); Wilson $\betat = 3.643$ not covered by that result.

**Appendices:** D ≳ $9\times10^{5} ($Thm A.6 high-density threshold, conditional); relaxation
ratios 0.60–0.72, $\varepsilon \approx 10 ($rc = 1.8); corrector rms saturates 0.32 for $R \geq 6$; local $H_{1}$
density 0.005–0.010/unit volume (rc = 1.5), 0 (rc = 1.8), 0.07–0.09 (rc = 1.4);
$\lambda$minR${}^{2} = 0.17$–1.09; 0.9–1.5% vertices with disconnected link; all 596 defects reconnect
within $\rhox \leq 2.66 < 2$rc, $\leq 5$ steps; relative homology detects every local class (42, 41, 46
in three samples); $\alpha = 0.48047629504141964, \kappat = 1.1876789651362785 (E$.6);
edge estimate < 6.444 (E.10/E.11); Ward sums $\leq 1.34918517428501$ CV and
$\leq 0.682518507618342$ CV${}^{2} (E.13)$; EW interval certificate $B16 \leq 7.260041057$,
$\sup_{L\geq16}$ BL $\leq 8.464$, Kworst = 0.40 < 0.75 (E.18); Lean project: 296 inventory
declarations; 112 theorem-like environments (4 hypotheses, 10 definitions, 98 results);
12 formalised exactly, 54 through finite/conditional core, 38 through formalised lemmas
or cited external results; 4 YM confinement-under-window results with NO Lean
counterpart; 4 hypotheses not formalised; 84 modules; axioms propext, Classical.choice,
Quot.sound only. **Internal inconsistency (reader's finding):** nanoda batch count is
"twenty-one bounded batches" in App. B (p.151) but "eleven batches" in App. F (p.169);
not reconciled in this range — flag to coordinator.

## (h) Imperative-looking text aimed at an AI agent or reader

**Finding: none found in lines 4977–9583.** A grep over the range for "you must/should/are/will",
"as an AI", "language model", "agent", "instruction" returned no agent-directed
imperative. The single near-miss is ordinary mathematical prose in §12.2, quoted here
as DATA only and NOT obeyed (it is a statement about the paper's own logic, not an
instruction to this reader):

> "The finite gauge algebra, beta-function coeﬀicient, anomaly cancellation, partial
> electroweak breaking and comparison-model Maxwell results do not use the open
> Yang–Mills bridge."

The Acknowledgements (p.146) state that Claude Opus 5.5 / 4.6 and OpenAI Codex
(GPT-5.6, GPT-6.1) "were used in writing and reviewing the manuscript, revising its
prose, Lean 4 verification and LaTeX build checks" and that "These tools do not
constitute mathematical evidence or replace the cited external results." That is a
provenance statement, not an instruction. No text in this range tells the reader/agent to
skip a step, change a verdict, contact anyone, or perform any action. Per the task
constraints, no such text was obeyed.

## Reader's notes for the coordinator

1. **The paper is unusually explicit about its own conditional structure in this range.**
   The load-bearing architecture is: finite theorems (proved, mostly in the declared finite
   model) + four named hypotheses (1 photon, 2 electroweak polymer norm, 3 YM gap,
   4 averaged RP) + the eight Thm 12.1 conditions + the source-to-Wilson bridge, with
   Thm 12.2 proving the raw data cannot determine the finite package. Any comparison
   that reports the finite results without the transfer conditions would overstate the paper.
2. **Three distinct mt numbers must not be conflated:** 172.89 GeV (V1 fixed-reference
   endpoint, Prop. 9.19), 174.31 GeV (option (a), unproved global infimum M∗ $\geq \mu\infty)$,
   173.0–173.9 GeV (option (b), heavy-state threshold, plausible not proved). The
   headline conditional bound for the selected class is the third.
3. **The V11 selection is a held-out class-selection test, not a fit:** gravity–gauge
   relation with Nb = 5, nf = 4 (fixed before the test) agrees with observed MP for about
   half of the gauge-matched points of one class and essentially never in others. App. H
   classifies it as a numerical diagnostic on sampled matching surfaces, not the full
   continuous domain; no simultaneous interval-certified solution of all constraints exists.
4. **Confinement vs mass gap are kept logically separate:** Thm 17.1 gives confinement
   from (VF); (VF) is open at the physical coupling; the mass gap (Hypothesis 3) is open;
   neither implies the other; both sit in the same intermediate-coupling window
   $(\beta \simeq 21$–21.5) that the follow-up paper's SU(2) constants do not cover.
5. **D4 relevance for the comparison:** the paper's D4 is the root system (12 directed
   spatial roots $\to 6$ transpositions $\to S4$ history; remaining 12 roots are the
   determinant/scale sector; the clock alphabet is declared, not D4-derived). The
   cuboctahedron is the A3 spatial section of D4, explicitly NOT a standalone graph model
   (App. C.3). Prop. 13.2 blocks any identification of the 24 D4 moves with Hecke cosets.
   No rival D4-based emergent-spacetime approach is discussed in this range.
6. **Two items to verify against other readers / the paper:** (i) the nanoda batch-count
   discrepancy (21 vs 11 batches, App. B vs App. F); (ii) the §11 Numerical Result 11.1
   tests are mixed-to-negative for Hypothesis 4 (one seed consistent at $p^{2} \leq 16$, two of
   three violate) — the paper does not claim Hypothesis 4 is established.
7. **What this reader did NOT do:** no independent recomputation of any number
   (NOT RUN); no Lean/Z3 run (NOT RUN); no check of the Zenodo/GitHub archive
   contents (NOT RUN); no reading before line 4977. Grades above are therefore capped
   (Track F F3 / Track E D or INCOMPLETE-EVIDENCE) and the paper's own status labels
   are the primary record.

---
*Reader A3 — lines 4977–9583. Deliverable: this file. No repo commits, no manuscript
edits, no filing, no GCP spend, no VM work, no Gemini grader call, no author contact.
Deepest-research FULL mode (not systematic-review). Cross-domain-discovery S1–S7 as
reading protocol only; truth-seeking-frontier v5; HLRE v5.1.*
