# AUDIT — Gemini 4 (Argon) Sweep 2 (G-C18): Does Any Rival Framework Derive $\alpha$?

**Audit date:** 2026-11-12 (CST)
**Auditor:** local audit coordinator (Muse, subagent) — claim-by-claim audit of the Gemini sweep result
**Sweep under audit:** Gemini 4 (Argon), AI Studio, account `autopoieticdragon@gmail.com`,
new chat "Sweep 2 Report — G-C18: Does Any Rival Framework Derive $\alpha$?", 2026-11-12 16:00–16:06 CST,
11,973 tokens, \$0. Record: `gemini-sweep-g-c18-2026-11-12.md` (the chat ran in Temporary mode,
so that file IS the record).
**Gap item:** G-C18 (grade-C external-verification programme, scope report
`GRADE-C-EXTERNAL-VERIFICATION-SCOPE-2026-11-12.md`).
**Frameworks:** truth-seeking-frontier v5, cross-domain-discovery, HLRE v5.1 **as amended 2026-11-12**
(human gate repealed; I1 bound repealed and replaced by external verification by a capable
HLRE-constrained agent, audited locally claim-by-claim; grades follow the evidence under the
remaining rules; nothing beyond grades).

## CLAIM / STATUS

| Claim (Gemini) | Gemini grade | Audit status | Audit grade |
|---|---|---|---|
| **LB-1.** SSM'$s \alpha^{-1} = \pi\sqrt{(m_{p}/m_{e})} \approx 134.61$ is a metadata-scraper artifact of the $\pi\sqrt$ formula; it is not a first-principles derivation (five unproved postulates, rotor premise, two-code reading); it does not derive $\alpha(0) = 137.036$; it misses its own running target by 0.65%. | A | **VERIFIED WITH CORRECTIONS** | **B** |
| **LB-2.** None of the other six retrieved frameworks (OPH, Singh, VG, Kosmoplex, HBMB, Dx) derives $\alpha$; each fails via numerology, unproved priors, incomplete maps, or scale-fitting. | B | **VERIFIED WITH CORRECTIONS** | **B** |
| **LB-3.** No surveyed rival derives $\alpha$; the scoped bound is strengthened $C \to B$; the universal negative stays UNVERIFIED / ABSTAIN. | B scoped / ABSTAIN universal | **VERIFIED** | **B** (scoped); **ABSTAIN** (universal) |

## Final G-C18 verdict

**BOUND STRENGTHENED (scoped $C \to B)$; UNVERIFIED / ABSTAIN as universal negative. Scoped grade B.**

Gemini's verdict survives the audit with corrections. The corrections are material to the
record but do not reverse the verdict direction: the strongest correction (the running-coupling
target is ~0.24 low) *strengthens* the miss; the other corrections are to Gemini's
transcriptions and presentation, not to its conclusions.

## Method and scope

- This audit grades the sweep's **claims about the literature**, not the physics of any
  candidate framework. The physics of SSM, OPH, Singh, VG, Kosmoplex, HBMB, and Dx is
  **ABSTAIN** (capped D/C) — same boundary as the G-D10 audit. A candidate's formula
  reproducing a number is a textual/arithmetic fact; it is not a derivation, and this audit
  never calls it one.
- Every source below was fetched and read firsthand in this session; every number was
  recomputed locally. Nothing is taken on Gemini's trust. Where a source could not be
  reached, the claim is marked **NOT RUN / UNVERIFIED** with the reason — never guessed.
- Computation gate (truth-seeking-frontier v5): all load-bearing arithmetic was run in
  Python 3.11.16 (`~/miniconda3/envs/jacobian-conjecture-2d/bin/python`), mpmath 1.4.1,
  exit 0; outputs quoted in §6. The running-coupling integral was validated at $M_{Z}$ before
  use at 235 MeV (§3.2, R1).
- "Derives" is used only for deductive results. A closed-form assembly of named constants
  under unproved framework axioms is not a derivation, however close its value lands.

## Check counts

36 checks: **26 PASS, 5 CORRECTED, 2 FAIL, 2 NOT RUN, 1 GEMINI-GAP** (audit-closed, §2.4).

| Block | PASS | CORRECTED | FAIL | NOT RUN | GAP |
|---|---|---|---|---|---|
| S — source checks (S1–S16) | 11 | 2 | 0 | 2 | 1 |
| A — arithmetic checks (A1–A12) | 12 | 0 | 1 | 0 | 0 |
| R — running-coupling checks (R1–R6) | 3 | 2 | 1 | 0 | 0 |
| RA — rotor algebra (RA1) | 0 | 1 | 0 | 0 | 0 |
| **Total** | **26** | **5** | **2** | **2** | **1** |

---

## 1. LB-1 — SSM $\alpha$: scraper artifact, not a derivation

### 1.1 SSM sources firsthand

**S1 — The $\pi\sqrt$ formula. PASS.** The idrive PDF
(`https://www.idrive.com/ssmtheory/papers/fine-structure-constant-fcc-vacuum-code.pdf`,
same document as Zenodo doi:10.5281/zenodo.22760383) renders its title in the text layer as
"$\alpha^{-1} = \pi m_{p}/m_{e}$" — the radical is dropped by text extraction. The idrive SSM index page
renders the same paper's title with the radical intact: "$\alpha^{-1} = \pi\sqrt{(m_{p}/m_{e})}$ from five axioms".
The paper's own value settles it: $\pi\sqrt{1836} = 134.6127545 (A1)$, $\pi\sqrt{1836.15267} = 134.6183513 (A2)$,
while the linear form $\pi\times1836.15 = 5768.44375 (A3)$ — so the formula Gemini's scraper
reported ("$\alpha^{-1} = \pi m_{p}/m_{e} = 134.6$") is arithmetically false, and the $\pi\sqrt$ form is the
paper's. **The scraper-artifact explanation is confirmed firsthand, including by observing
the same dropped radical in the primary source's own text layer.**

**S2 — V1 quote "The relation does not derive $\alpha$ from nothing. It turns two undetermined
quantities of the model, the coupling and the confinement length, into one." NOT RUN.**
A `browser.find` for "does not derive" in the v2 PDF returned only other matches; the
sentence is **not in v2**. The ResearchGate v1 page (doi:10.13140/RG.2.2.21524.05764) was
not located in this session (DOI search returned the Singh EPJP page and other papers
instead). **Status: UNVERIFIED as a v1 quote.** Substance corroborated: v2 §10's ledger
states the same content in its own words (see S3), and §2.1 says "What the paper does not
derive is the postulates, the rotor premise of Section 7 under which the photon sector is
a U(1) rotor at all, and the two-code reading."

**S3 — Five axioms; u = 1, 𝔧 = 1. PASS, with a correction to Gemini's framing.** The
abstract states: "the first [Hamiltonian coefficient] is priced by the information
postulate as an energy, giving u = 1 from the electron calibration and gauge invariance,
the second by the kinematic postulate as a transmission, giving 𝔧 = 1 from the flux
current $I = -(J/\hbar)\sin B$, whose transfer per tick is exact because the phase is
conserved. The exact Floquet Hamiltonian of the tick shows no significant dressing of
their ratio." §2.1 (P1)–(P5) lists Geometry, Kinematics, Information, Pricing, Two
realizations. §10's ledger lists u = 1 and 𝔧 = 1 as **derived** from the postulates —
**not arbitrarily set**, as Gemini's "five model postulates, u = 1, 𝔧 = 1, two-code reading"
could be read to imply. **Correction:** the failure mode is the *unproved axioms* plus the
rotor premise (A3) plus the two-code reading (A1–A2) — the coefficients themselves are
derived *within* the framework. This sharpens, not weakens, LB-1: the derivation is
internally coherent and still rests on unproved foundations.

**S4 — The 1836 count. PASS.** §2: "$(K+1)K^{2} - c_{skew} K = 13 \times 144 - 36 = 1836$, the
proton-to-electron mass ratio." Abstract: "two-step paths from the trapped-node defect,
1836 into the bulk at one bit each and 16 inside it at one quantum each, equated by the
model's stability window." Arithmetic: $13\times144-36 = 1836$ ✓.

**S5 — $L_{c} = 0.8413$ fm vs $r_{p} = 0.8409$ fm. PASS.** Abstract: "the proton radius an output
(0.8413 against 0.8409 fm)"; "with $\alpha$ it gives $L_{c} = 0.83$ fm against $r_{p} = 0.8409$ fm."
§3.1: charge radius "0.8409 fm from muonic hydrogen (CODATA 2022: 0.84075(64) fm)."

**S6 — "Against the running value $135.5 \pm 0.3$." CORRECTED.** The quotation is accurate —
the abstract and §5 both state it — but the value is wrong as a standard-QED value.
See §1.3 (R4): the corrected one-loop value at $Q = \hbarc/r_{p}$ is $\alpha^{-1} \approx 135.70$–135.77
(central ~135.74), so SSM's stated target is ~0.24 low. Inside the paper'$s \pm0.3$ band
(not falsified), but the miss figures change (§1.3).

**S7 — Symmetry 2026, 18(11), 1869. PASS.** The Symmetry paper (doi:10.3390/sym18111869,
published 2026-11-08) publishes only the EM-sector construction of SSM; its abstract
contains no $\alpha$ formula. Gemini's claim that the $\alpha$ calculation "remains an unrefereed
Zenodo/ResearchGate preprint" stands. (Abstract confirmed verbatim via search.)

### 1.2 Rotor algebra §2.2 — worked independently (RA1: CORRECTED)

Gemini's §2.2 passage is garbled (a "[Wait: ...]" aside, confused $\lambda_{e}/\bar{\lambda}$_e factors, and a
nonstandard convention $\bar{\lambda}$_$e = \hbar/(2m_{e} c))$. Working from the paper's own definitions:

- The paper's impedance (abstract, text layer drops the radical — "$p U/J/4\pi$"):
  **$\alpha = \sqrt{(U/J)} / 4\pi$**, with U the charging energy of a unit link flux and J the stiffness
  of a plaquette.
- $U = \epsilon_{b} = m_{e} c^{2} ($one standing bit); $J = \hbarc/(4L_{c}) ($the bond quantum, 4 = K/d).
- Therefore **$\alpha^{-1} = 2\pi\sqrt{(\hbar/(m_{e} c L_{c}))} = 2\pi\sqrt{(\bar{\lambda}_}$_$e/L_{c})$** — the square root is
  load-bearing.
- With $L_{c} = r_{p} = 0.8409$ fm: $2\pi\sqrt{(\bar{\lambda}_}$_$e/r_{p}) = **134.6452** \approx$ the paper's 134.65 ✓.
- Since $r_{p} \approx 4\bar{\lambda}$_$p (r_{p}/(4\bar{\lambda}$_p) = 0.99960), this equals $\pi\sqrt{(m_{p}/m_{e})} = 134.6183513$ ✓ —
  the two forms coincide, which is why the paper states both.
- Gemini's linear rendering "$2\pi\bar{\lambda}$_$e/L_{c}$" gives **2885.37**; the linear form
  $\pi\hbar/(m_{e} c L_{c})$ gives **1442.69** — neither reproduces the paper's value. The linear
  form is off by a factor $21.43 = \sqrt{(\bar{\lambda}_}$_$e/r_{p})$.

**Verdict RA1:** Gemini's §2.2 formula as written is arithmetically inconsistent with the
paper's value; the paper's derivation, in its coherent (square-root) form, is internally
consistent given the rotor premise and the U, J assignments. Presentation correction, not
a substantive error in the paper — but it is a substantive error in Gemini's report, and
it is the same dropped-radical pattern as the title (S1) and as Singh (S9).

### 1.3 Arithmetic and running-coupling checks

**A1 — $\pi\sqrt{1836} = 134.6127545$. PASS.** (Gemini 134.61276 ✓.)
**A2 — $\pi\sqrt{1836.15267343} = 134.6183513$. PASS.** (Gemini 134.61836 ✓.)
**A3 — $\pi\times1836.15267343 = 5768.44375$. PASS.** Gemini's quoted "$\alpha^{-1} = \pi m_{p}/m_{e} = 134.6$"
is arithmetically false by a factor of 42.85.
**A4 — Miss vs $\alpha^{-1}(0) = 137.035999177$: 2.4232 units, 1.768%. PASS.** (Gemini 2.42, 1.77% ✓.)
**A5 — 134.61 vs 135.5: diff 0.88725, 0.6548%. PASS.** (Gemini 0.65% ✓ — against the
paper's own target; see R4 for the corrected target.)

**R1 — Method validation at $M_{Z}$. PASS.** One-loop leptonic vacuum polarization, spacelike:
$\Delta\alpha_{f}(Q^{2}) = (\alpha/3\pi)\cdotN_{c}\cdotQ_{f}^{2}\cdot\int_{0}^{1} 6x(1-x)\cdot\ln(1+Q^{2}x(1-x)/m^{2})$dx. At $M_{Z}$:
$\Delta\alpha_{lep} = 0.031423$ vs PDG 0.03150 (incl. two-loop); on-shell $\alpha^{-1}(M_{Z}^{2}) = 128.947$ vs
known 128.95. Method validated before use at 235 MeV.

**R2 — $\alpha^{-1}(Q = \hbarc/r_{p} = 234.66$ MeV), leptonic only = 135.840. PASS (computation).**
$\Delta\alpha_{lep} = 0.008728 ($electron 0.008204, muon 0.000525, tau 0.000003).

**R3 — With hadronic 0.0005–0.0010 (the paper's own range$): \alpha^{-1} \approx 135.70$–135.77,
central ~135.74. PASS (computation).**

**R4 — SSM's stated target $135.5 \pm 0.3$ is ~0.24 low vs the corrected value. CORRECTED.**
The target is inside its own $\pm0.3$ band, so it is not falsified — but the miss figures
change: SSM's 134.65 misses the corrected running value by **1.09 units (0.80%,
$3.6\sigma$ of the paper'$s \pm0.3)$**, vs $2.83\sigma$ against the paper's own target; SSM's 134.613
misses by 1.13 units $(3.8\sigma)$. **The correction strengthens LB-1's miss claim.**

**R5 — Gemini's "$\approx136.1$ at Q = 235 MeV via electron vacuum polarization." FAIL.**
Electron-only gives **135.91**, not 136.1. (Leptonic total 135.84; with hadronic ~135.74.)
Gemini's number is wrong in the opposite direction from SSM's target, and it is the
second wrong running value in the sweep report. It does not affect LB-1's conclusion
(it is a side number), but it is a factual error.

**R6 — SSM §5: "Exact one-loop leptonic polarization at spacelike $Q^{2} = 0.055$ GeV${}^{2}$ gives
$\Delta\alpha_{lep} = 0.0096$; the MS logarithms with e and $\mu$ active give 0.0107. $\dots$ So
$\alpha^{-1}(\hbarc/L_{c}) \simeq 135.5 \pm 0.3$." CORRECTED.** The 0.0096 does **not** reproduce from the
standard spacelike one-loop formula (mine 0.00873, ~10% high). The MS value 0.0107
**is** verified as the sum of logs without the $-5/3$ term. The paper explicitly says the
$\pm0.3$ spread "covers the scheme (spacelike versus MS) and the hadronic term" — so the
discrepancy is absorbed by the paper's own band, and the paper's central value 135.5
matches its MS computation (135.47). The paper's internal arithmetic is consistent
within its stated band; the band itself is centred ~0.24 low (§1.3, R4).

### 1.4 LB-1 verdict

**VERIFIED WITH CORRECTIONS, grade B** (Gemini claimed A). The core stands: the $\pi\sqrt$
formula is confirmed firsthand; the scraper artifact is confirmed firsthand (the primary
source's own text layer drops the radical); the paper's own ledger marks the postulates,
the rotor premise, and the two-code reading as not derived; the value misses its own
running target (and misses the corrected target by more, $3.6\sigma)$; it does not derive
$\alpha(0)$. Downgrade $A \to B$ because the audit found material corrections to Gemini's report:
the garbled §2.2 algebra (RA1), the wrong 136.1 side value (R5), the unconfirmed v1
quote (S2), the u/𝔧 framing nuance (S3), and the low running target (R4/S6). Grade B =
strong constrained support (HLRE v5.1: B is "strong constrained support"; A requires a
protocol-frozen, quantitatively successful, discriminating result with no material
corrections outstanding).

---

## 2. LB-2 — The six other candidates

### 2.1 OPH (Mueller et al. 2026) — S8: PASS

**Source.** GitHub `FloatingPragma/observer-patch-holography`, raw PDFs, read firsthand.
The repo's own admissions, verbatim: "The separate root $136.994835177413\dots$ is an
interval-certified output of an incomplete declared map; no derivation relates it to the
physical fine-structure endpoint." / "The certified roots do not constitute an independent
determination of the physical fine-structure constant." / "The fine-structure comparison
is diagnostic because the physical transport map is incomplete."

**A12 — Value and $\sigma$. PASS.** Gauge-width fixed point $\alpha^{-1} = 137.035660136946577$ confirmed.
Diff vs CODATA 2022 (137.035999177(21$)): 0.000339177 / 2.1\times10^{-8} = **16,151\sigma$**
(Gemini ">$16,000\sigma$" ✓). Gemini's classification (incomplete map, diagnostic status)
is the repo's own statement. **VERIFIED.**

### 2.2 Singh (T. P. Singh) — S9: CORRECTED

**Source.** arXiv:2110.07548 (IJMPD 30, 2142010); EPJP paper is arXiv:2205.06614.
Gemini cited arXiv:2110.02062, the earlier version — minor citation imprecision (C11).

**A6 — Gemini's transcription is arithmetically false. FAIL (transcription);
corrected formula PASS.** Gemini wrote (9/1024)e^$(-1/36) = 1/137.04006$. Recomputed:
(9/1024)e^$(-1/36) = 0.00854828 = **1/116.9826$**, NOT 1/137.04. The paper's Eq. (11),
confirmed verbatim from the Springer EPJP page:
"$\alpha^{2}(L_{P}/L)^{4} \equiv e^{2}/\hbarc = \exp[[1/3 - \sqrt{(3/8)}] \times 2/3] \times 9/1024 \approx 0.00729713 = 1/137.04006 (11)$."
Recomputed: $\exp[(1/3-\sqrt{(3/8)})\times2/3]\times9/1024 = 0.00729713629$, 1/v = **137.0400606** ✓.
Gemini dropped the $\sqrt$ on 3/8 — **the same error pattern as the SSM formula (S1, RA1)**.
Its value was right; its formula was wrong.

**Disqualifier. VERIFIED.** The EPJP text, verbatim: "The Karolyhazy correction to this
value gives an exact match with the measured value of the constant, after assuming a
specific value for the electro-weak symmetry breaking energy scale." ResearchGate/TIFR
text confirms: "The Karolyhazy correction to this value gives an exact match with the
measured value of the constant, after assuming a specific value for the electro-weak
symmetry breaking energy scale."

**A7 — 137.04006 vs CODATA 137.035999177: diff 0.0040608, 29.63 ppm. PASS.**
**VERIFIED WITH CORRECTION** (formula transcription only; value and disqualifier stand).

### 2.3 Vinuesa Guerrero (VG) — S10: NOT RUN

**Source not located.** Four targeted searches (general; quoted "Vi Gravitatis";
ResearchGate title search; author-name search "Vinuesa Guerrero" + vortex) returned no
paper by this author — only unrelated vortex/$\alpha$ papers (Super Golden TOE blog,
$\alpha-\pi$-Helix, Heegner–vorton, Lien spindle torus, Butto 2020). **Status: UNVERIFIED /
source not located.** The disqualifying fact (N = 137 hardcoded as winding number
(p,q) = (1,137)) is Gemini's report only.

**A11 — Formula value. PASS (arithmetic only).** $137\times(1+\pi^{2}/(2\times137^{2})) = 137.036020454$
(Gemini 137.036020694; diff $2.4\times10^{-7}$, negligible). The arithmetic checks; the paper's
content does not — this sub-claim cannot be counted as verified.

### 2.4 Kosmoplex (Macedonia et al.) — S11: PASS; S12: GEMINI-GAP (audit-closed)

**S11 — v1. PASS.** Preprints.org doi:10.20944/preprints202508.1294.$v1: \alpha^{-1} = 137.035577$;
formula $137 + 1/(8\pi) - \gamma/137.0397887357 = 137.0355768522$. Recomputed: paper's formula
137.035576706 (diff $1.5\times10^{-7}$, rounding); Gemini's formula $137 + 1/(8\pi) - \gamma/137$ =
137.035575483 — matches the paper to 6 decimal places. Gemini's v1 evaluation stands:
v1 misses CODATA by $4.2\times10^{-4} (~20,000\sigma)$ and rests on the unproved Kosmoplex framework
(7 axioms, 42 glyphs, octonionic substrate).

**S12 — v3 NOT evaluated by Gemini. GAP, audit-closed.** v3 (posted 2026-02-19 — nine
months before the sweep; same DOI, `.v3`) claims $\alpha^{-1} = 137.035999143 (1.62\sigma$ from CODATA
2022) with four correction terms, including a channel-memory term
x = ln$(n)/(2\times137) + \ln(\ln n)/(42\times7)$, $n \approx 8.07\times10^{60}$, $\ln n = 14\pi^{2} + \ln 8 + \varepsilon(\Phi)$,
where $\varepsilon(\Phi)$ is "a residual holonomy encoding the local measurement context" that the
paper treats as "a small real correction sufficient for evaluating $\alpha^{-1}$ at the precision
reported". Audit recomputation (A9): the reconstructed formula
$\alpha^{-1} = 137 + 1/(8\pi) - \gamma/(137 + 1/(8\pi) - x) + \zeta(3)/(137\times20)$ gives **137.035999101**
(paper 137.035999143; diff $4.2\times10^{-8}$, rounding in x); x = 0.5286522 (paper 0.528653);
implied $\varepsilon(\Phi) = -0.010309$, whose effect on $\alpha^{-1}$ is **$1.2\times10^{-9}$** — negligible, so $\varepsilon(\Phi)$
is not doing the fitting work. **But:** (a) the framework axioms are unproved and the
steps from axioms to formula are asserted mappings, not deductions from established
physics; (b) the formula is an assembly of named constants (137, $1/(8\pi), \gamma, \zeta(3)$, and
the n-term); (c) the revision history $v1 \to v3$ added correction terms to close $a 4.2\times10^{-4}$
gap — the hypothesis class expanded after target inspection, which is a post-hoc
adjustment of the formula even though no single free parameter is fitted (HLRE v5.1
postulation rule: a model set changed after inspection is at best post-hoc, ceiling D
for the derivation claim). The paper's own "No post-hoc adjustment is possible because
there are no free parameters" is therefore not accepted: adding terms between versions
*is* an adjustment. **The non-derivation classification stands for v3 as for v1, but the
Kosmoplex entry must be updated to v3** — Gemini graded a stale version. This is a
completeness error in the sweep, not a reversal of its verdict.

### 2.5 Nagy HBMB (micro-horizon) — S13: PASS

**Source.** OSF PDF, read firsthand. Abstract confirms the micro-horizon premise and the
four inputs (Bekenstein–Hawking bit count; Dirac modes under MIT boundary conditions;
Seeley–DeWitt correction; uniform-WKB zeta-regularised high-$\ell$ tail). $\alpha^{-1} = S_{max}/g_{tot}$
= 137.035998(20) confirmed. v2 (2026-02-27) adds boundary data B. The value lands
within $1.3\times10^{-8}$ of CODATA, but the derivation runs on the micro-horizon / MIT-bag
premise — an unproved framework assumption, not established first principles.
**VERIFIED** (value + disqualifying premise).

### 2.6 Dx Theory — S14: PASS

**Source.** Preprints.org 202610.2156, read firsthand. $1/\alpha = 4\pi^{3} + \pi^{2} + \pi = 137.0363038$
(Gemini 137.036304 ✓, A10). The paper postulates its structure (incl. P6); the formula
is $a \pi$-polynomial assembly with no derivation from established physics. Diff vs CODATA:
$3.05\times10^{-4} (~14,500\sigma)$. **VERIFIED** (value + numerological classification).

### 2.7 LB-2 verdict

**VERIFIED WITH CORRECTIONS, grade B** (as Gemini graded). Five of six candidates
verified firsthand (OPH, Singh with transcription correction, Kosmoplex v1 with the v3
gap audit-closed, Nagy, Dx); VG's source not located (UNVERIFIED sub-claim); the
Kosmoplex entry was stale (v1 vs v3). The conclusion — none of the six achieves a
first-principles derivation — survives on the verified five plus the audit's own v3
assessment; the VG classification remains Gemini's report, not audit-verified, and is
recorded as such. Grade B = strong constrained support; the two gaps (VG unlocated,
Kosmoplex stale) bar an A.

---

## 3. Meta-references

**S15 — Sticker. PASS.** arXiv:2512.07027, SHPS 119 (2026) 102199, exists and says what
Gemini claims: "I argue instead that $\alpha$ is a scaled quantity that arises only where the
structural scales contributed by classical electromagnetism (e), quantum mechanics $(\hbar)$,
and special relativity (c) intersect$\dots I$ conclude that $\alpha$ is a domain-specific structural
ratio reflecting contingent relationships among independent physical scales."

**S16 — Jentschura & Nándori. PASS.** arXiv:1411.4673, EPJH 39 (2014) 591–613, exists
and says what Gemini claims: "It has been a notably elusive task to find a remotely
sensical ansatz for a calculation of Sommerfeld's electrodynamic fine-structure constant
$\alpha_{QED} \sim 1/137.036$ based on first principles."

---

## 4. LB-3 — Scoped bound vs universal negative

**LB-3 verdict: VERIFIED.** The scoped bound is earned: the surveyed set (SSM + six
others) now stands audit-verified as containing no first-principles derivation of $\alpha$,
with the VG caveat recorded (its classification is Gemini's report, not audit-verified)
and the Kosmoplex entry corrected to v3. The bound moves **$C \to B$** on the strength of:
(a) the SSM core claim verified firsthand including the scraper-artifact mechanism;
(b) five of six further candidates verified firsthand with their disqualifying facts
confirmed from primary sources; (c) the running-coupling correction strengthening rather
than weakening the SSM miss. The universal negative stays **ABSTAIN by construction** —
a literature sweep, however careful, cannot establish that *no* framework derives $\alpha$,
and §5 lists unevaluated claimants that would have to be assessed before any universal
claim could be entertained. The audit grades the sweep's claims about the literature;
it does not grade, and does not vindicate or refute, the physics of any candidate.

## 5. Corrections register (to Gemini's Sweep 2 report)

| # | Correction | Check |
|---|---|---|
| C1 | SSM formula as Gemini's scraper reported it ("$\alpha^{-1} = \pi m_{p}/m_{e} = 134.6$") is arithmetically false (5768.44); correct is $\pi\sqrt{(m_{p}/m_{e})} = 134.618$. The primary source's own text layer drops the radical — confirmed firsthand. | S1, A3 |
| C2 | Gemini's §2.2 rotor passage is garbled ("[Wait: $\dots]$" aside, confused $\lambda_{e}/\bar{\lambda}$_e factors, nonstandard $\bar{\lambda}$_e). The paper's coherent form is $\alpha^{-1} = 2\pi\sqrt{(\bar{\lambda}_}$_$e/L_{c}) = 134.65$ at $L_{c} = r_{p}$; Gemini's linear form gives 2885.37. The $\sqrt$ is load-bearing. | RA1 |
| C3 | Gemini's "$\approx136.1$ at Q = 235 MeV via electron vacuum polarization" is WRONG: electron-only gives 135.91; leptonic total 135.84; with hadronic ~135.74. | R5 |
| C4 | SSM's stated running target $135.5 \pm 0.3$ is ~0.24 low vs the corrected standard-QED value (~135.74 central). Inside its $\pm0.3$ band (not falsified), but the miss grows to 1.09 units (0.80%, $3.6\sigma$ of $\pm0.3)$. | R4, S6 |
| C5 | SSM's "exact one-loop leptonic $\Delta\alpha_{lep} = 0.0096$" does not reproduce from the standard spacelike one-loop formula (0.00873); its MS value 0.0107 is verified as the sum of logs without $-5/3$; the paper'$s \pm0.3$ band absorbs the difference. | R6 |
| C6 | u = 1 and 𝔧 = 1 are DERIVED from the postulates per the paper's §10 ledger, not arbitrarily set. The failure mode is the unproved axioms + rotor premise + two-code reading. | S3 |
| C7 | Singh's formula as Gemini transcribed it is arithmetically false: (9/1024)e^$(-1/36) = 1/116.98$, not 1/137.04. Correct (paper Eq. 11): $\exp[(1/3-\sqrt{(3/8)})\times2/3]\times9/1024 = 1/137.04006$. Same $\sqrt$-dropping pattern as SSM. | S9, A6 |
| C8 | Kosmoplex: Gemini evaluated v1 only (137.035577). v3 (posted 2026-02-19, predates the sweep) claims 137.035999143 with four correction terms; audit recomputation gives 137.035999101. The non-derivation classification stands (unproved framework axioms; named-constant assembly; $v1\tov3$ term-adding is a post-hoc adjustment of the formula), but the entry must be updated to v3. | S12, A9 |
| C9 | VG (Vinuesa Guerrero): source NOT LOCATED after four targeted searches. The disqualifying fact (N = 137 as winding number (1,137)) is Gemini's report only. | S10 |
| C10 | SSM v1 quote "The relation does not derive $\alpha$ from nothing$\dots$" NOT confirmed in the v2 PDF; ResearchGate v1 page not located. UNVERIFIED as a v1 quote; substance corroborated by v2's §10 ledger. | S2 |
| C11 | Gemini cited Singh arXiv:2110.02062 (earlier version); the EPJP paper is arXiv:2205.06614. Minor citation imprecision. | S9 |

## 6. Scope notes — the sweep is scoped, not exhaustive

Searches in this audit surfaced further $\alpha$-derivation claimants Gemini did not evaluate.
None was assessed here; each would need its own evaluation before any universal claim.
Recorded for the inventory, consistent with LB-3's framing:

- **Pan V4**, **Murphy**, **Alves et al.** (Zenodo 21623367, $\alpha^{-1} = 137.035999171)$,
  **Nusbaumer** (Preprints.org 202608.0145/v1, 137.035999216, "matching LKB to $7.6\times10^{-11}$"),
  **Schwarz** (non-linear vacuum, 137.036002), **Peinador Sala** (Zenodo 18611630,
  137.035999206).
- **SSM's own April 2026 three-term paper** ("Holographic FCC Vacuum", Zenodo 19639340):
  $1/\alpha = 137.036025 (1.9\sigma$ from CODATA 2018) via a different three-term formula — a
  distinct SSM $\alpha$ claim Gemini did not evaluate. SSM'$s \alpha$ programme is not a single
  consistent derivation; the $v2 \pi\sqrt$ paper audited here is one of (at least) two.
- The G-D10 audit's boundary applies here too: a candidate's formula reproducing a
  number is a textual/arithmetic fact, not a derivation; the physics of every candidate
  is ABSTAIN.

## 7. Computation-gate record

All load-bearing numbers were computed locally in this session (Python 3.11.16,
`~/miniconda3/envs/jacobian-conjecture-2d/bin/python`, mpmath 1.4.1, exit 0):

- $\pi\sqrt{1836} = 134.6127545$; $\pi\sqrt{1836.15267343} = 134.6183513$; $\pi\times1836.15267343 = 5768.44375$.
- Miss vs $\alpha^{-1}(0) = 137.035999177$: 2.4232447 units, 1.7683%. 134.61 vs 135.5: 0.6548%.
- Singh as transcribed: (9/1024)e^$(-1/36) = 0.00854828 = 1/116.9826$. Corrected:
  $\exp[(1/3-\sqrt{(3/8)})\times2/3]\times9/1024 = 0.00729713629 = 1/137.0400606$; vs CODATA 29.63 ppm.
- Kosmoplex v1: paper formula 137.035576706 (paper 137.0355768522); Gemini formula
  137.035575483. Kosmoplex v3: 137.035999101 (paper 137.035999143); x = 0.5286522
  (paper 0.528653); implied $\varepsilon(\Phi) = -0.010309$, effect on $\alpha^{-1} 1.2\times10^{-9}$.
- Dx: $4\pi^{3}+\pi^{2}+\pi = 137.0363038$. VG: $137\times(1+\pi^{2}/(2\times137^{2})) = 137.036020454$.
- OPH: |$137.035999177 - 137.035660$| / $2.1\times10^{-8} = 16,151\sigma$.
- Rotor: $2\pi\sqrt{(\bar{\lambda}_}$_$e/r_{p}) = 134.6452 ($paper 134.65); $2\pi\sqrt{(\bar{\lambda}_}$_$e/4\bar{\lambda}$_p) = 134.6183514 =
  $\pi\sqrt{(m_{p}/m_{e})}$; linear forms $2\pi\bar{\lambda}$_$e/r_{p} = 2885.37$, $\pi\bar{\lambda}$_$e/r_{p} = 1442.69$.
- Running coupling (one-loop leptonic integral, spacelike; validated at $M_{Z}$:
  $\Delta\alpha_{lep} = 0.031423$ vs PDG 0.03150; $\alpha^{-1}(M_{Z}^{2}) = 128.947$ vs 128.95): at Q = 234.66 MeV,
  $\Delta\alpha_{lep} = 0.008728 (e 0.008204, \mu 0.000525, \tau 0.000003)$; $\alpha^{-1} = 135.840$
  leptonic-only; 135.70–135.77 with hadronic (central ~135.74); electron-only 135.91.

No GCP spend (local work only). Nothing filed, committed, or written into the manuscript.

## 8. Final G-C18 inventory verdict

**BOUND STRENGTHENED (scoped $C \to B)$; UNVERIFIED / ABSTAIN as universal negative.
Scoped grade B.**

- LB-1: VERIFIED WITH CORRECTIONS, grade B (Gemini claimed A).
- LB-2: VERIFIED WITH CORRECTIONS, grade B (as Gemini claimed).
- LB-3: VERIFIED — scoped bound $C \to B$ earned; universal ABSTAIN by construction.
- Checks: 36 total — 26 PASS, 5 CORRECTED, 2 FAIL, 2 NOT RUN, 1 GEMINI-GAP
  (audit-closed, §2.4).
- Open items carried forward: VG source still unlocated (S10); SSM v1 quote still
  unconfirmed (S2); Kosmoplex entry to be updated to v3 (C8); unevaluated claimants
  listed in §6 (no universal claim until assessed).
