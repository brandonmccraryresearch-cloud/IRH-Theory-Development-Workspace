# Task 12 — Formalize rival accounts (DRAFT)

**Workstream D, task 12 — Co-scientist task programme, 2026-11-10.**
DRAFT for the parent agent to assemble into the final report. Not filed,
not committed, no manuscript edits (programme rules).

**Deepest-research mode: FULL.** Literature grounding for each rival account
was done in deepest-research FULL mode (primary sources verified by web
search/fetch, 2026-11-10; see §8 Citation record). Systematic-review mode
was NOT chosen and was not used. The literature-review form choice is the
assistant's per the standing delegation; systematic review would require
Brandon's explicit choice.

**Skills applied:** truth-seeking-frontier v5 (computation gate),
cross-domain-discovery v2.0.0 (protocol S1–S7), HLRE v5.1 (grading/records).
The skills themselves are DESIGN CLAIMS, ungraded — skill use is not
evidence of reliability. Grade caps from cross-domain-discovery apply:
Track $E \leq C$ / Track $F \leq F3$ until a human runs the source/balance gates.

## CLAIM and STATUS (together, at the top)

**CLAIM.** Five rival accounts of spacetime and of the origins of
dimensionless constants, formalised as executable SymPy/numerical models
and run under shared conditions against IRH v93.1 as reference, diverge
from IRH at six identified points (D1–D6 in `task12_divergence_table.md`),
and in two cases the divergence is IRH's *silence* (no prediction) rather
than a conflicting prediction: (i) the Greensite/Carlini–Greensite
dynamical-signature mechanism predicts Lorentzian signature iff
$n_{F} > n_{B}$, where IRH predicts nothing — and the mechanism cannot be
transferred into IRH, because its critical feature (a quantum-field
fermion/boson DOF balance) has no counterpart in IRH's single classical
scalar substrate (Bartha FAIL); (ii) the anthropic account accommodates
the observed $\Lambda$ under every prior tried, but its typicality number swings
~$80\times$ with the prior (0.0015 uniform vs 0.1204 log-uniform), so it
predicts no prior-independent number — prediction vs accommodation is
the divergence. The sharpest *quantitative* divergences that survive as
shared-condition comparisons are: a toy linear $\alpha$ drift of $1\times10^{-15}$/yr is
excluded by the Rosenband 2008 bound $(-1.6\pm2.3)\times10^{-17}$/yr by ~$25.6\times$, and
the CDT spectral dimension flows $1.82 \to 4.02$ while IRH holds D = 4 at all
scales (difference ~2.18 at $\sigma\to0)$. No rival formalised here derives $\alpha^{-1}$,
and neither does IRH (its $137 + 1/(28-\pi/14) = 137.0360028\dots$ is a numerical
ansatz only, differing from CODATA 2022 by +$3.6\times10^{-6}$ arithmetically).

**STATUS.** PARTIALLY VERIFIED (see branch lists, §9). All 55 executed
checks PASS (driver exit 0, 0 FAIL). The *formal* parts (selection
algebra, toy sign-flip, drift arithmetic, prior-dependence arithmetic,
CDT-fit evaluation) are verified as computations. The *physical* claims
the rivals make are graded C or D, or ABSTAINED where the primary source
could not be recovered (Greensite full one-loop mechanism; causal-set
$D_{s}$; any primary-source Ġ/G bound). Nothing in this draft upgrades any
IRH grade, and no EXCLUDED claim is revived.

## 1. Claim register (S1 — registered before analysis)

| ID | Target claim | Domain | What would count as evidence |
|---|---|---|---|
| R0 | IRH reference quantities (B*, $r_{c}, S$, triad relations as definitions, $\alpha$ ansatz arithmetic, d=4 marginality) reproduce v93.1 exactly | IRH geometric core | SymPy derivation + second-tool (flint) agreement, exit 0 |
| R1 | Greensite-type mechanism: Lorentzian signature favoured iff $n_{F} > n_{B}$ | Dynamical signature | One-loop $V(\theta)$ recovered from primary source, or toy sign-flip + explicit ABSTAIN on the rest |
| R2 | Dirac-type varying constants: Ġ/$G = -1/t$; a linear $\alpha$ drift is testable against Rosenband 2008 | Varying constants | Primary-source drift bound + computed exclusion factor |
| R3 | Anthropic selection: P(observed $\Lambda)$ under a stated prior | Multiverse / selection | Prior-dependence quantified under $\geq2$ named priors |
| R4 | CDT discrete spacetime: $D_{s}$ flows $4 \to 2$ at short scales | Discrete QG | Primary-source $D_{s}(\sigma)$ formula evaluated at matched $\sigma$; IRH D=4 contrast |
| R5 | Divergence points D1–D6 under shared conditions | Comparison | Table with IRH value, rival value, discriminating test per point; explicit "cannot be run" entries where sharing fails |

No claim was selected after inspecting a target outcome; the toy
parameters $(\alpha$ drift rate $1\times10^{-15}$/yr, prior ranges, $\Delta$ values) were fixed
as round illustrative values in the scripts before running, and are
labelled TOY/ILLUSTRATIVE wherever they appear.

## 2. BPMF facets (S1, per model)

| Model | Background | Purpose | Mechanism | Findings |
|---|---|---|---|---|
| A IRH ref. | $D_{4}$ substrate, $\psi$ on $\mathbb{R}^{4}$, Swift–Hohenberg | Reference values for shared comparison | Selection functional F(B); shell combinatorics $\tau$, $q_{4}$ | B*, $r_{c}$, S=64/141 verified; triad relations are definitions; $\alpha$ ansatz arithmetic only; d=4 marginal |
| B Signature | Euclidean base, Wick angle $\theta$ dynamical | Does a quantum mechanism select Lorentzian signature? | One-loop $V(\theta)$; sign set by $(n_{F}-n_{B})$ | Toy reproduces the sign-flip only; full mechanism ABSTAINED; transfer into IRH FAILS (Bartha) |
| C Varying consts. | Dirac LNH; $\alpha$ as a possibly-varying coupling | Test drift predictions against clocks | $G\propto1/t$; $\alpha(t)$ linear toy | Dirac Ġ/$G=-7.25\times10^{-11}$/yr; toy $\alpha$ drift excluded ~$25.6\times$ by Rosenband; no Ġ/G bound verified (ABSTAIN) |
| D Anthropic | Multiverse ensemble + observer window (galaxies) | Does selection predict or merely accommodate $\Lambda$? | Prior $\times$ window $\to P($observed) | P(near) 0.0015 vs \$0.1204 $(~80\times$\$ prior swing); accommodates under all priors |
| E Discrete | CDT triangulations; diffusion probes geometry | Does effective dimension flow at short scales? | $D_{s}(\sigma)=-2 d \log\langleP\rangle/d \log \sigma$ | Fit $1.82\to4.02$; IRH flat 4; endpoint disputed (~2 vs ~3/2); causal-set ABSTAINED |

## 3. Derivation (each step checkable)

### 3.1 Model A — IRH reference (`model_a_irh_reference.py`)
Solving F = 0 and $F' = 0$ simultaneously (SymPy, symbolic in B, r, u, v,
$\tau$, $q_{4})$ gives $B* = 2u\tau/(3$vq${}_{4})$ and $r_{c} = 2u^{2}\tau^{2}/(9$vq${}_{4}); r_{c} = (2u^{2}/9v)\cdotS$,
so ordering by $r_{c}$ is ordering by S, independent of u, v (v93.1 §II.3).
Exact rationals: $S_{D}_{4} = 64/141 \approx 0.453901$, $S_{A}_{4}* = 12/31 \approx 0.387097$,
ratio 496/423, margin $73/423 \approx 17.26$%; $\tau_{D}_{4}/\tau_{BCC} = \sqrt{2}$; $S_{BCC}(3D)$ =
16/45 — all cross-checked in python-flint (fmpq). Triad relations:
with $a_{0} = L_{P}/\sqrt{24}$ and $\Omega_{P} = \sqrt{24}\cdotc/L_{P}$, $c = a_{0}\Omega_{P}$ is an identity, and
$G = 24c^{2}a_{0}/M$* is consistent iff $L_{P}^{2} = \hbarG/c^{3}$ — i.e. the definitions
reproduce each other, which is *not* a derivation of c, $\hbar$ or G (§I.1).
$\alpha$ ansatz: $137 + 1/(28-\pi/14) = 137.0360028\dots$, vs CODATA 2022
137.035999177(21): difference +$3.6\times10^{-6}$ — arithmetic only (Part VII
downgrade). Scaling exponents at d = 4: gradient $-2$, potential $-4$,
Swift–Hohenberg 0 — marginal exactly and uniquely at d = 4 (§III.4).
$r_{eff} = +0.1072$ at $\bar{\psi} = -0.18 ($§II.9): nucleation required.
Dimensional assignment: UNDECIDED (§IX.2); this model is
reading-independent for the quantities checked and makes no signature
claim. **What IRH does NOT predict:** signature, Einstein equations,
the values of c, $\hbar$, G, $\alpha$.

### 3.2 Model B — Dynamical signature, toy (`model_b_signature.py`)
Toy potential $\mathrm{Re} V_{toy}(\theta) = \Delta\cdot\cos \theta$, $\Delta = n_{F} - n_{B} ($overall scale 1,
toy). Stationary points $\theta = 0 ($Euclidean) and $\theta = \pi ($Lorentzian);
$V''(\pi) = +\Delta$, $V''(0) = -\Delta$, so $\pi$ is the minimum iff $\Delta > 0$, 0 is the minimum
iff $\Delta < 0$, and $\Delta = 0$ leaves the potential flat (signature undetermined).
Verified symbolically (SymPy), by exact integer sign rule (flint), and
by numpy grid minimisation $(\Delta = -5, -1, 0, +1, +5)$. **Scope:** the exact
one-loop determinant of Greensite (1993) / Carlini–Greensite (1994) was
not recovered from available (abstract-level) text, so the D = 4
uniqueness of the stationary point and the fluctuation scale are NOT
reproduced and NOT claimed — ABSTAIN on the full mechanism. The toy
preserves the domain structure $(\theta$ an angle with period $2\pi, \Delta a$ DOF
difference, signature read off at $\theta = 0/\pi)$, satisfying the S7 DVP guard
as a toy. **Bartha audit (S4):** the source's Prior Association is a
quantum one-loop effective potential over propagating fermionic/bosonic
fields. IRH's substrate is a single classical real scalar $\psi$ with no
fermion/boson DOF count, so that critical feature sits in the Negative
Analogy: **the transfer of the Greensite mechanism into IRH FAILS.**
IRH reading (A) would need this mechanism supplied externally (§IX.3).

### 3.3 Model C — Varying constants, toy (`model_c_varying_constants.py`)
Dirac: $G(t) = G_{0}t_{0}/t$ gives Ġ/$G = -1/t$ exactly (SymPy); at $t_{0} = 13.8$ Gyr
(illustrative cosmic age, conventional input) Ġ/$G = -7.25\times10^{-11}$/yr
(flint cross-check $1/t_{0})$. G was $2\times$ present at $t_{0}/2$, will be ½ at \$2$t_{0}$\$.
Linear $\alpha$ toy: $\alpha(t) = \alpha_{0}(1 + r(t-t_{0}))$, $r = +1\times10^{-15}$/yr (round
ILLUSTRATIVE rate, not measured). Rosenband et al. 2008 (primary):
$\dot{\alpha}/\alpha = (-1.6\pm2.3)\times10^{-17}$/yr, $1\sigma$ interval $[-3.9, +0.7]\times10^{-17}$/yr,
containing 0. The toy exceeds the envelope edge $(3.9\times10^{-17}$/yr) by
~$25.6\times$ and accumulates one Rosenband $\sigma$ in ~0.023 yr (~8 days) — it is
EXCLUDED as a present-day linear drift. IRH predicts 0 for both drift
rates (no mechanism), consistent with Rosenband. **Scale comparison
only:** |Dirac Ġ/G| is ~$3\times10^{6}\times$ the Rosenband $\alpha$ scale — different
observables, not a falsification of Dirac. **ABSTAIN:** no
primary-source Ġ/G constraint number is stated (lunar laser ranging
not verified from a primary source in this run).

### 3.4 Model D — Anthropic selection (`model_d_anthropic.py`)
$y = \Lambda/\Lambda_{obs}$; observer window $0 < y \leq 100 ($Weinberg 1987: bound "quite
large", within 1–2 orders of magnitude of the upper bound; $100\times$ is the
2-order end, $10\times$ shown as sensitivity). $P(0.5 \leq y \leq 2)$: uniform on
[0,1000] $\to 0.0015$; log-uniform on [0.01,1000] $\to$ ln4/ln$10^{5} \approx 0.1204$;
uniform on the window [0,100] $\to 0.015$. Ratio log-uniform/uniform $\approx$
$80.3\times$. $P(y \leq 100)$: 0.10 uniform vs 0.80 log-uniform. Analytic (SymPy
log/rational) and numpy-integration cross-checks agree to <$2\times10^{-3}$.
Window-$10\times$ sensitivity: 0.010 vs 0.600 — still prior-dominated.
**Finding:** the account accommodates y ~ 1 under every prior but
predicts no prior-independent number; the prior-dependence IS the
divergence from a prediction. IRH has no entry for this observable.

### 3.5 Model E — Discrete spacetime, CDT fit (`model_e_discrete.py`)
$D_{s}(\sigma) = 4.02 - 119/(54+\sigma) ($Ambjørn et al. 2005, via Giasemidis et al.
2012 eq. 7). Limits: $\sigma\to0$ gives $1226/675 \approx 1.816 ($paper $1.80\pm0.25)$;
$\sigma\to\infty$ gives 4.02 (paper $4.02\pm0.10)$. Values: $\sigma=10 \to 2.16$, $\sigma=54 \to 2.92$,
$\sigma=100 \to 3.25$, $\sigma=500 \to 3.81$, $\sigma=1000 \to 3.91$, $\sigma=10000 \to 4.01$.
Reconstructed return-probability log-log slope recovers $D_{s}/2$ at
$\sigma=1000 (1.953$ vs 1.954). IRH: D = 4 at all scales — largest divergence
|$4 - 1.82$| $\approx 2.18$ at $\sigma\to0$, agreement only asymptotically. **Literature
tension (not resolved):** Coumbe & Jurkiewicz (JHEP 2015) find ~3/2 at
small scales, not ~2; the CDT endpoint is unsettled. **ABSTAIN:**
causal-set $D_{s}$ numbers (no formula verified from a primary source).

## 4. Checks run (PASS / FAIL / NOT RUN)

Tool versions: Python 3.11.16, SymPy 1.14.0, numpy 2.4.6,
python-flint 0.8.0, in `~/miniconda3/envs/jacobian-conjecture-2d/bin/python`.
Driver: `task12_models/compare_driver.py`, exit 0. **55 PASS / 0 FAIL.**

| Model | Checks | Result |
|---|---|---|
| A IRH reference | $15 (B*/r_{c}$ solve, S rationals + flint, $\tau$ ratio, BCC, triad identities, $\alpha$ arithmetic, marginality, $r_{eff})$ | 15 PASS |
| B Signature toy | 13 (stationary points, $V''$ sign rule, flint $\Delta\in{-5,-1,0,1,5}$, numpy grid) | 13 PASS |
| C Varying constants | 9 (Dirac $-1/t$, rate + flint, G doubling/halving, Rosenband interval, toy exclusion ~$25.6\times$, accumulation time, IRH 0) | 9 PASS |
| D Anthropic | 9 (three priors, P(near), P(window), ~$80\times$ ratio, numpy integration $\times2$, window sensitivity) | 9 PASS |
| E Discrete (CDT) | 9 (limits, exact rational 1226/675, monotonicity, values at $7 \sigma$, return-probability slope) | 9 PASS |

NOT RUN: Lean formalisation (not required for this task; no Lean builds
started, per task; a Lean process may already be running elsewhere).
NOT RUN: recovery of the exact Greensite one-loop determinant (ABSTAIN);
causal-set $D_{s}$ evaluation (ABSTAIN); primary-source Ġ/G bound
(ABSTAIN). No job exceeded ~10 min / ~4 GB; no GCP spend; lean-build-4
untouched; Gemini grader never called.

## 5. Rival / failure mode

- **Forcing a shared comparison where none exists** is the main failure
  mode of this task. It was avoided by explicit "no entry" cells and a
  "could not be run" section in the divergence table (Greensite$\to$IRH
  transfer, anthropic vs IRH $\Lambda$, causal set, Einstein equations,
  Dirac Ġ/G vs Rosenband $\dot{\alpha}/\alpha)$.
- **Toy mistaken for mechanism (B):** the sign-flip toy is not the
  one-loop potential; the report labels it TOY at every use and ABSTAINS
  on D=4 uniqueness. A reader who drops the label would overstate the
  result by two grades.
- **Illustrative rate mistaken for a measurement (C):** $r = 1\times10^{-15}$/yr is
  a round number chosen to be visible against the bound; the exclusion
  claim is "any linear drift above ~$4\times10^{-17}$/yr is excluded", not "the
  rival predicts $1\times10^{-15}$/yr".
- **Prior smuggled in as a prediction (D):** the uniform-on-window prior
  conditions on the answer; it is shown only to expose that circularity.
- **CDT endpoint (E):** the 2005 fit (~2) and the 2015 result (~3/2)
  disagree; using either as "the CDT prediction" without the tension
  would be a false precision.
- **IRH side:** the $\alpha$ ansatz's numerical closeness to CODATA $(+3.6\times10^{-6})$
  must not be read as evidence of a derivation; the manuscript downgrade
  stands.

## 6. Evidence that would change the answer

- (B) Recovery of the exact Greensite/Carlini–Greensite one-loop $V(\theta)$
  from the primary text, with the D=4 uniqueness and fluctuation scale
  reproduced, would lift the toy to a formalisation and remove the
  ABSTAIN (the Bartha FAIL for transfer into IRH would stand unless a
  DOF count for the IRH substrate were supplied).
- (C) A verified primary-source Ġ/G bound tighter than ~$7\times10^{-11}$/yr would
  decide Dirac'$s G\propto1/t$; a bound looser than it would leave Dirac alive
  on this observable. A measured non-zero $\dot{\alpha}/\alpha$ would falsify IRH's 0
  only if IRH claimed $\alpha$ constant as a prediction — it does not; it
  would instead falsify the *absence* of a mechanism, which is a weaker
  statement, and would require a mechanism to be supplied.
- (D) A multiverse measure fixed independently of the observed value
  (e.g. derived from a specified landscape prior) would convert the
  anthropic accommodation into a testable prediction; without it, the
  ~$80\times$ prior swing stands.
- (E) A settled CDT small-scale endpoint (2 vs 3/2) and a short-scale
  dimensional probe would sharpen D4; either way IRH's flat D=4 remains
  the contrasting prediction.
- (A) A derivation of $\alpha^{-1}$ or of $c/\hbar/G$ from substrate premises (not a
  change of variables) would change the IRH column of O5/O2b; none is
  offered here, and §I.1 explains why the triad relations are not one.
- Deciding the §IX.2 dimensional assignment would change which
  comparisons are even well-posed (D7).

## 7. HLRE grades (per narrow claim, worst-of shown)

Tier: Standard (mechanisms proposed, others may cite). Track E unless
noted Track F. Independence: all verification artificial, single
pipeline (this draft's scripts$) \to I1$ at best. Human source/balance
gates NOT performed $\to$ caps Track E C / Track F F3 (cross-domain-discovery
§6.5). Worst-of = min(independence bound, caps, postulation ceiling,
support in record).

| # | Narrow claim | Track | Worst-of computation | Grade |
|---|---|---|---|---|
| G1 | IRH selection algebra: B*, $r_{c}$, S=64/141, ratio 496/423 (as algebra from F(B)) | F | I-bound n/a (formal); 2 independent tools (SymPy+flint$) \to F2$; ceiling F3 cap applies (human gates not run$) \to \min(F2, F3)$ | **F3** |
| G2 | $D_{4}$ is selected in nature by S (physical reading of G1) | E | $I1 \to C$; postulation ceiling C (evidence-guided); record support C | **C** |
| G3 | Triad relations "derive" c, $\hbar$, G | E | No derivation exists (§I.1); change of variables only | **No grade — NOT A DERIVATION** (definitional identities: F3 as identities) |
| G4 | $\alpha^{-1} = 137+1/(28-\pi/14)$ as a derived value | E | Downgraded in manuscript; arithmetic F3, derivation absent | **D (ansatz only)** |
| G5 | Greensite toy: Lorentzian favoured iff $n_{F}>n_{B} ($toy sign-flip) | F | Single toy construction, artificial-only $\to F3$ | **F3** |
| G6 | Lorentzian signature is dynamically selected (full Greensite mechanism) | E | Mechanism not recovered $\to$ INCOMPLETE-EVIDENCE | **No grade (ABSTAIN)** |
| G7 | Greensite mechanism transfers into IRH | E | Bartha FAIL (critical feature in Negative Analogy) | **No grade — TRANSFER FAILS** |
| G8 | Dirac Ġ/$G = -1/t ($as arithmetic from $G\propto1/t)$ | F | 2 tools $\to F2$, capped | **F3** |
| G9 | Toy linear $\alpha$ drift $r=1\times10^{-15}$/yr is excluded by Rosenband 2008 | E | Comparison to primary measurement; frozen toy rate; I2 (held-out published observable$) \to B$; cap C (human gates not run$) \to \min(B, C)$ | **C** |
| G10 | Dirac varying-G as a physical claim | E | No verified Ġ/G constraint in this run $\to$ INCOMPLETE-EVIDENCE on this observable | **No grade (ABSTAIN on verdict)** |
| G11 | Anthropic P(observed $\Lambda)$ is prior-independent | E | Prior swing ~$80\times$ demonstrated $\to$ UNDERDETERMINED | **D (accommodation, not prediction)** |
| G12 | CDT $D_{s}$ flows $1.82\to4.02 (2005$ fit evaluation) | F | 2 tools (SymPy+numpy$) \to F2$, capped | **F3** |
| G13 | CDT spectral dimension flows in nature (physical) | E | $I1 \to C$; literature tension on endpoint (~2 vs ~$3/2) \to$ record support C | **C** |
| G14 | Divergence points D1–D6 as stated | E | $I1 \to C$; comparative, artificial-only | **C** |

No claim in this draft exceeds C (Track E) or F3 (Track F). No IRH grade
is changed by this draft.

## 8. Citation record (primary sources only for load-bearing numbers)

- IRH v93.1: `IRH_v93_1_source_rebuilt.txt` (34 pp.), §§I.1, I.2–I.3,
  II.3, II.5, II.9, III.4, VII, IX.2, IX.3; repo guardrails
  `established/CORE.md`, `guardrails/EXCLUDED.md`, `guardrails/INPUTS.md`,
  `predictions/VI-predictions.md`.
- Greensite 1993: Phys. Lett. B 300, 34–37, arXiv:gr-qc/9210008
  (ADS abstract verified 2026-11-10).
- Carlini & Greensite 1994: Phys. Rev. D 49, 866–878,
  arXiv:gr-qc/9308012 (verified via archive.org full text + IRH §IX.3).
- Elizalde, Odintsov & Romeo 1993: arXiv:hep-th/9312132v1 (summary of
  the $(n_{B}-n_{F})$ factor and $n_{F}>n_{B}$ condition).
- Dirac 1937: Nature 139, 323; Proc. Roy. Soc. A 165, 199 (1938) —
  Large Numbers Hypothesis, $G\propto1/t ($verified via Barrow
  arXiv:gr-qc/0209080v1 and MacTutor RAS obituary for the citation trail).
- Rosenband et al. 2008: Science 319, 1808–1812, DOI
  10.1126/science.1154622 — $\dot{\alpha}/\alpha = (-1.6\pm2.3)\times10^{-17}$/yr (NIST + PubMed
  abstracts agree).
- CODATA 2022: Tiesinga et al., Rev. Mod. Phys. 97, 025002 (2025);
  NIST SP 959 — $\alpha^{-1} = 137.035999177(21)$.
- Weinberg 1987: Phys. Rev. Lett. 59, 2607–2610, DOI
  10.1103/PhysRevLett.59.2607 (abstract verified).
- Ambjørn, Jurkiewicz & Loll 2005: Phys. Rev. Lett. 95, 171301,
  arXiv:hep-th/0505113 (CDT $D_{s}$ flow $4\to2)$.
- Giasemidis, Wheater & Zohren 2012: Phys. Rev. D 86, 081503,
  arXiv:1202.2710 eq. (7) — $D_{s}(\sigma) = 4.02 - 119/(54+\sigma) ($full text read).
- Coumbe & Jurkiewicz 2015: JHEP 03, 151 — small-scale $D_{s} ~3/2$
  (literature tension, via Springer abstract).
- Steinhaus & Johannes 2018: Phys. Rev. D 98, 026013 — cited only for
  the existence of causal-set spectral-dimension literature; no
  causal-set number is used (ABSTAIN).
- No citation is fabricated; every load-bearing number above carries its
  primary source and version. Quotations from copyrighted works: none
  exceed 50 words (no verbatim quotation is used beyond short phrases).

## Appendix A — Assumption, parameter and choice ledgers

**Assumption ledger.** (A1) IRH substrate is $\psi$ on $\mathbb{R}^{4}$ with Swift–Hohenberg
dynamics (§I.2) — IRH premise, not re-derived. (A2) Dimensional
assignment UNDECIDED (§IX.2); reading (A) assumed provisionally only
where a signature discussion needs a base. (A3) Greensite toy potential
$\mathrm{Re} V = \Delta\cdot\cos \theta$ with overall scale 1 — toy assumption, not the one-loop
result. (A4) Dirac $G\propto1/t$ with $t_{0} = 13.8$ Gyr illustrative cosmic age —
conventional input. (A5) Anthropic observer window $y \leq 100$ from
Weinberg's "1–2 orders of magnitude" — approximate reading of the
abstract. (A6) CDT 2005 fit taken as the stated fit; 2015 ~3/2 variant
flagged, not adjudicated. (A7) Priors in Model D are choices, not
measurements — that is the point of the model.

**Parameter ledger.** u, v (IRH couplings; cancel from S); $\tau$, $q_{4} ($shell
combinatorics, exact rationals); $\bar{\psi} = -0.18, r = -0.35 (v93.1$ §II.8–II.9
values, inputs to the $r_{eff}$ check); $\Delta = n_{F}-n_{B} ($toy integers $-5\dots+5)$;
$r = 1\times10^{-15}$/yr (toy $\alpha$ rate); $t_{0} = 13.8\times10^{9}$ yr; $\sigma ($CDT diffusion time);
prior ranges [0,1000] / [0.01,1000] / [0,100]. All fitted/illustrative
parameters are labelled as such; no parameter was tuned to match a
target after inspection (the $\alpha$ rate was chosen round before running).

**Choice ledger.** Toy functional forms $(\cos \theta$; linear $\alpha(t); \log$-uniform
prior); grid resolutions (numpy 20001-point $\theta$ grid; 2,000,001-point
y grid); $\sigma$ sample points {0,10,54,100,500,1000,10000}; $1\sigma ($not $2\sigma)$
Rosenband envelope for the exclusion factor; deepest-research FULL
mode (not systematic-review). None of these choices changes a headline
conclusion except the prior choice in Model D — which is the finding.

## Appendix B — Semantic reconstruction ledger (per model)

| Model term | Legacy classification | Operational target | Structural equivalent | Mathematical object |
|---|---|---|---|---|
| B (Model A) | Normalised amplitude | Order parameter of the standing wave | Shell-mode amplitude $\times \sqrt{N}$ | Real scalar $B \geq 0$ |
| $\tau$, $q_{4} (A)$ | Triad/quadruple densities | Closed-wavevector counts on the reciprocal shell | Ordered triples/quadruples summing to zero, normalised by $N^{3/2}/N^{2}$ | Exact rationals $(\tau^{2}=8/3$ for $D_{4})$ |
| $a_{0}$, $\Omega_{P} (A)$ | Lattice constant / Planck frequency | Substrate resonant scale $(a_{0}=2\pi/q_{0})$ vs Planck re-expression | Length / frequency | Positive reals; triad relations are definitional identities |
| $\theta (B)$ | Wick angle | Signature degree of freedom | Phase of the tangent-space metric component $e^{i\theta}$ | Angle, period $2\pi$; signature read at $0/\pi$ |
| $\Delta (B)$ | DOF balance | Fermion-minus-boson propagating DOF | Integer difference of DOF counts | Integer (toy values $-5\dots+5)$ |
| $\alpha(t)$, G(t) (C) | Couplings | Clock-measured fractional drift | Time-dependent coupling functions | Real functions of t; drift = logarithmic derivative |
| y (D) | Vacuum-energy ratio | $\Lambda$ relative to observed | Dimensionless ratio of two energy densities | Positive real; window $y\leq100$ = galaxy-formation condition |
| $D_{s}(\sigma) (E)$ | Spectral dimension | Diffusion return-probability scaling | $-2 d \log\langleP\rangle/d \log \sigma$ | Real function of diffusion time $\sigma$ |
| D (IRH, E) | Topological dimension | Dimension of the substrate base $\mathbb{R}^{4}$ | Fixed integer 4 | Constant 4 (no flow) |

No term in any model was collapsed into a trivial scalar: $\theta$ keeps its
angle structure, $\tau/q_{4}$ keep their combinatorial definitions, $D_{s}$ keeps
its diffusion definition distinct from the topological dimension 4,
and the triad relations are kept as labelled definitions, never
presented as derivations. (S7 DVP guard: PASS for all five models as
formalised; Model B passes as a toy, not as the full mechanism.)

## Appendix C — Cross-domain protocol (S1–S7) run log

- S1: claim register (§1) and BPMF facets (§2) written before analysis.
- S2: rival retrieval was by literature (primary sources in §8), not by
  graph/LBD mining — no AGATHA/KGE step was run; no S2 grade is claimed.
- S3: invariance alignment — the shared observables O1–O5 are the
  alignment; power-conjugacy / $\Pi$-group checks do not apply to these
  accounts and were not forced.
- S4: Bartha articulation — run for (B) (FAIL, §3.2), and for (D)/(E)
  the transfer question does not arise (standalone models); selection
  diagrams were not constructed because no causal graph is available —
  transportability is therefore NOT claimed for any transfer.
- S5: no conceptual blend was constructed; none is claimed.
- S6: no tournament/evolution was run; none is claimed.
- S7: DVP guard applied per model (Appendix B); no Lean formalisation
  was produced (not required); Z3 not used. Sheaf/AGM machinery not
  invoked — no contradiction between the models required revision; the
  divergences are recorded as divergences, not resolved.
- Self-evaluation rubric (8 checks): (1) independent test exists — PARTIAL
  (Rosenband/CDT-fit are independent of the toys, but the toys were built
  from the same sources); (2) falsification boundary stated — PASS (§6);
  (3) Bartha passes — FAIL for (B) transfer, recorded as a finding, not
  hidden; (4) transportability audited — PARTIAL (no causal graph, no
  claim); (5) second independent tool — PASS (SymPy + flint/numpy);
  (6) no invented numbers — PASS; (7) assumption ledger complete —
  PASS (Appendix A); (8) grade honest — PASS (§7). Rubric score 6/8
  with check 3 failed for the (B) transfer only: per the rubric, that
  transfer is rejected as a discovery and retained only as the recorded
  failure it is.

## Appendix D — Withdrawal / demotion note

None. No prior claim was corrected in this draft. Two pre-existing
manuscript positions are carried forward unchanged and are NOT
withdrawals by this draft: the $\alpha$ ansatz downgrade (Part VII) and the
retraction of the v92 signature/Einstein derivations (§IX.3).

## 9. Branch lists

**VERIFIED** (executed, exit 0, second tool where above CLAIMED):
G1 (selection algebra, F3); G5 (Greensite toy sign-flip, F3); G8 (Dirac
$-1/t$ arithmetic, F3); G9 (toy $\alpha$ drift excluded by Rosenband, C);
G12 (CDT fit evaluation, F3); $G2 (D_{4}$ selection, physical, C);
G13 (CDT flow, physical, C); G14 (divergence points, C).
**UNVERIFIED** (stated, not established by this run): G6 (full Greensite
mechanism — ABSTAIN); G10 (Dirac varying-G verdict — ABSTAIN pending a
verified Ġ/G bound); causal-set $D_{s} ($ABSTAIN); the CDT small-scale
endpoint (2 vs 3/2 — literature tension, unresolved); the §IX.2
dimensional assignment (UNDECIDED in the manuscript).
**FAILED** (transfer / claim rejected by a gate): G7 (Greensite$\to$IRH
transfer — Bartha FAIL); G3 (triad relations as derivations — not a
derivation); G11 as a *prediction* (prior-dependent — retained only as
an accommodation, grade D); the v92 signature and Einstein derivations
(already retracted in the manuscript; not revived here).
**NOT RUN:** Lean formalisation; exact Greensite determinant recovery.

*AI-contribution statement: this draft was produced by an AI research
subagent under the programme brief, with all computations executed in
the conda env and all literature claims checked against the primary
sources listed in §8. The human (Brandon D. McCrary) is the sole author
accountable for any use of it; incorporation into the repo or manuscript
requires deepest-research validation and his explicit approval.*
