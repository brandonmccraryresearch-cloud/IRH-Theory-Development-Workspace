# Gemini 4 (Argon) Sweep 2 — G-C18: does any rival derive $\alpha$?

**Date:** 2026-11-12 16:00–16:06 CST (harness-measured)
**Agent:** Gemini 4 (Argon) in Google AI Studio, account
autopoieticdragon@gmail.com (PRO), /u/1/, new chat "Sweep 2 Report —
G-C18: Does Any Rival Framework Derive $\alpha$?" (11,973 tokens), Grounding
with Google Search on. Cost \$0.
**Prompt:** as specified in `GEMINI-SWEEPS-SPECS-2026-11-12.md` Sweep 2
(pasted exactly), with SSM'$s \alpha$ claim named as a candidate to evaluate.
**Status:** Gemini's report, UNVERIFIED — local claim-by-claim audit to
follow (`AUDIT_gemini-sweep-g-c18_2026-11-12.md`). Do not cite the verdict
as established until the audit lands.
**RECORD NOTE:** this conversation ran in Temporary-chat mode ("Your
conversation won't be saved automatically") — the full response text
below, as captured in the browser handoff, IS the record of this sweep.

---

## FULL RESPONSE TEXT (verbatim from the Gemini 4 Argon response)

### Sweep 2 Report — G-C18: Does Any Rival Framework Derive $\alpha$?

Protocol: HLRE v5.1 as amended 2026-11-12 (human-gate repeal,
external-verification authorization, I1-bound repeal — grades follow the
evidence; no grade rises by itself).
Target Gap: G-C18 — "No rival derives $\alpha$" as a universal negative (Prior
state: C scoped / UNVERIFIED as universal; WS-D task 9, C7).
Research Question: Does any framework in the open literature derive the
fine-structure constant $\alpha$ from first principles (not fit it, not
postulate it, not numerologically approximate it — derive it)?

### 1. Executive Verdict

Verdict on G-C18: BOUND STRENGTHENED (for the scoped survey); UNVERIFIED
/ ABSTAIN as a universal negative.

Methodological Guard: A wider sweep that still finds nothing STRENGTHENS
a scoped bound — it does not prove a universal negative.

Summary of Findings: Seven candidate frameworks claiming a
"first-principles derivation" of $\alpha$ across the open literature (up to
November 2026) were retrieved and audited, including the explicitly
assigned candidate (Raghu Kulkarni's Selection–Stitch Model, 2026). None
of the retrieved candidates constitutes a genuine, assumption-free
first-principles derivation of $\alpha$. Every retrieved candidate fails via at
least one of three disqualifying mechanisms: (1) Unproved/postulated
microscopic priors or empirical scale-matching (Kulkarni 2026; Singh
2021/2022; Mueller/OPH 2026; Nagy 2025). (2) Explicit numerological
target-selection (building 137 or target integers directly into the
ansatz, as in Vinuesa Guerrero 2026 and Macedonia 2025). (3)
Scale-contingency (as established in the meta-theoretical analysis by
Sticker 2025/2026, showing $\alpha$ is a domain-specific structural ratio at
the intersection of independent theories rather than a pure mathematical
constant).

### 2. Explicit Evaluation of Assigned Candidate: Raghu Kulkarni's Selection–Stitch Model (SSM, 2026)

2.1 Retrieved Primary Sources
- Kulkarni, R. (Sept 2026, Preprint v1): "The fine-structure constant as
  a confinement-length ratio: $\alpha^{-1} = 2\pi\lambda_{e}/L_{c}$ in the FCC vacuum code",
  ResearchGate Preprint, DOI: 10.13140/RG.2.2.21524.05764.
- Kulkarni, R. (Sept/Oct 2026, Preprint v2): "The fine-structure constant
  from the FCC vacuum code: $\alpha^{-1} = \pi\sqrt{(m_{p}/m_{e})}$ from five axioms", Zenodo /
  SSMTheory Group Preprint, DOI: 10.5281/zenodo.22760383.
- Kulkarni, R. (Nov 8, 2026, Journal Article): "The Electromagnetic
  Sector of the Selection–Stitch Model: A Compact U(1) Field Beside a
  Stabilizer Code on the FCC Lattice", Symmetry 2026, 18(11), 1869,
  DOI: 10.3390/sym18111869.

2.2 Arithmetic Check of the SSM Formula
The prompt notes the SSM claim as $\alpha^{-1} = \pi m_{p}/m_{e} = 134.6 ($which reflects
how plain-text abstract scrapers on ResearchGate render the title/abstract
when stripping the radical sign $\sqrt{)}$. Checking both the literal un-rooted
expression and the actual formula from Kulkarni's Zenodo listing
(10.5281/zenodo.22760383):

Literal un-rooted check $(\pi m_{p}/m_{e})$: Using the empirical CODATA ratio
$m_{p}/m_{e} \approx 1836.15267343$: $\pi \times 1836.15267343 \approx 5768.4437 \neq 134.6$. Using
SSM's internal integer structural count $m_{p}/m_{e} = 1836$: $\pi \times 1836 \approx$
$5767.9641 \neq 134.6$. Thus, $\pi m_{p}/m_{e} = 134.6$ is arithmetically false by a
factor of $\approx 42.85$; it is a typographical artifact of stripped
square-root symbols in plain-text metadata.

Actual SSM formula check $(\alpha^{-1} = \pi\sqrt{(m_{p}/m_{e})})$: On the official SSM Theory
portal (10.5281/zenodo.22760383), the title is explicitly printed with
the square root: "The fine-structure constant from the FCC vacuum code.
$\alpha^{-1} = \pi\sqrt{(m_{p}/m_{e})}$ from five axioms". Using SSM's internal integer count
$(m_{p}/m_{e} = 1836)$: In SSM, the proton-to-electron mass ratio is an integer
count of lattice bonds/nodes: $(K+1)K^{2} - c_{skew} K = 13 \times 144 - 36 = 1836$.
Evaluating with \$1836: $\alpha$^{-1} = $\pi\sqrt{1836} = \pi \times 42.84857057$$... $$\approx 134.61276 \approx$\$
134.6. Using empirical $m_{p}/m_{e} = 1836.15267$: $\alpha^{-1} = \pi\sqrt{1836.15267} = \pi \times$
42.850352... $\approx 134.61836 \approx 134.6$.

How the radical arises in SSM: Step 1: From the Kogut–Susskind rotor
coupling $\alpha = U/(4\piJ)$ with charging energy $U = \varepsilon_{b} = m_{e} c^{2}$ and plaquette
stiffness $J = \hbarc/(4L_{c})$, SSM obtains: $\alpha^{-1} = 4\piJ/U = 4\pi\hbarc/(4L_{c} m_{e} c^{2})$ =
$\pi\hbar/(m_{e} c L_{c}) = 2\pi\bar{\lambda}$_$e/L_{c}$, where $\bar{\lambda}$_$e = \hbar/(2 m_{e} c)$. (Using reduced
Compton wavelength $\lambda_{e} = \hbar/(m_{e} c) = 386.159267$ fm and $2\pi/4 = \pi/2$ gives
$\alpha^{-1} = \pi\lambda_{e}/L_{c}$. Indeed, for $L_{c} = r_{p} = 0.8409$ fm, — specifically,
$2\pi(\hbar/2m_{e} c)/0.8409$ fm = $\pi \times 197.32698$ MeV⋅fm / 0.51099895 MeV / 840.9 fm
[Wait: $\lambda_{e} = \hbar/(m_{e} c) = 386.159$ fm; with $\alpha^{-1} = \pi\lambda_{e}/9L_{c}$ or
$2\pi(\lambda_{e}/2\pi)/L_{c}] 0.8409$ fm.) Let us check Kulkarni's exact identity in
the abstract: "$\alpha^{-1} = 2\pi\lambda_{e}/L_{c}$, $L_{c} = 4\pi^{2}\alpha^{2}\lambda_{e}$, at the scale where the
code structure that assigns charges and stiffnesses exists, the
confinement code... Read the other way, $L_{c} = r_{p}$ gives $\alpha^{-1}(\hbarc/r_{p})$ =
134.65 against the running value $135.5 \pm 0.3$."

Step 2: In v2 (10.5281/zenodo.22760383), Kulkarni eliminates $L_{c}$ by
equating two path counts ("1836 into the bulk at one bit each and 16
inside it at one quantum each"), fixing the ratio $\lambda_{e}/L_{c}$ in terms of
$\sqrt{(m_{p}/m_{e})} = \sqrt{1836} ($with $16 = 4^{2})$, yielding $\alpha^{-1} = \pi\sqrt{1836} = 134.61$
(quoted as 134.6) and $L_{c} = 0.8413$ fm.

2.3 Verbatim Quotes from SSM Sources
From Kulkarni (Sept 2026, v1, DOI: 10.13140/RG.2.2.21524.05764): "The
relation does not derive $\alpha$ from nothing. It turns two undetermined
quantities of the model, the coupling and the confinement length, into
one. 1 The question: No accepted theory derives the fine-structure
constant. Attempts to do so usually aim at $\alpha^{-1} = 137.036$, the value at
zero momentum. That is the wrong target for any theory with a cutoff: the
coupling runs, and a mechanism at a scale $\mu$ produces $\alpha(\mu)$, not $\alpha(0)$." —
"Read one way, $\alpha$ at $\hbarc/L_{c}$ gives $L_{c} = 0.83$ fm against the proton radius
0.8409 fm. Read the other way, $L_{c} = r_{p}$ gives $\alpha^{-1}(\hbarc/r_{p}) = 134.65$
against the running value $135.5 \pm 0.3$."

From Kulkarni (Sept 2026, v2, DOI: 10.5281/zenodo.22760383): "The
confinement length itself follows from one count applied twice: two-step
paths from the trapped-node defect, 1836 into the bulk at one bit each
and 16 inside it at one quantum each, equated by the model's stability
window. Within the SSM, then, $\alpha$ is not a free parameter: from the axioms
alone, $\alpha^{-1} = \pi\sqrt{(m_{p}/m_{e})} = 134.6$, with the proton radius an output
(0.8413 against 0.8409 fm), against the running value $135.5 \pm 0.3$ and
$r_{p} = 0.8409(4)$ fm. The axioms themselves, the rotor premise and the
two-code reading remain the framework's assumptions, and the paper marks
throughout which claims rest on them."

From Kulkarni (Nov 2026, Symmetry 18(11), 1869, DOI:
10.3390/sym18111869): "The Selection–Stitch Model (SSM) treats the
vacuum as a face-centered-cubic (FCC) lattice whose $\langle110\rangle$ bonds carry a
stabilizer code but no propagating electromagnetic field. We construct its
electromagnetic sector by asking where a compact U(1) gauge field can
live without sharing the code's variables, comparing the Gaussian
spectrum of the compact U(1) Hamiltonian on three candidate complexes."

2.4 Classification of SSM: Derivation, Fit, or Numerological Approximation?
Classification: Postulated-Prior / Combinatorial-Ansatz Approximation
(neither a first-principles derivation nor a continuous parameter fit, but
a discrete combinatorial approximation resting on unproved ad hoc axioms).
Reasons it does not count as a first-principles derivation: (a)
Inaccurate Numerical Value (0.65% error even at its chosen scale, and
1.77% off $\alpha^{-1}(0))$: The formula $\pi\sqrt{1836} = 134.61$ misses the zero-momentum
fine-structure constant $\alpha^{-1}(0) = 137.035999$ by 2.42 units. Even when
reinterpreted by the author as the running coupling $\alpha^{-1}(\mu)$ at the proton
confinement scale $\mu = \hbarc/r_{p} \approx 235$ MeV, the author admits the empirical
running value is $135.5 \pm 0.3$, which disagrees with 134.61 by $\sim3\sigma (0.65$%).
Wait — in standard QED, the running coupling $\alpha^{-1}(Q^{2})$ decreases as energy
Q increases (from 137.036 at Q = 0 to $\approx136.1$ at Q = 235 MeV via electron
vacuum polarization, and $\approx128$ at $M_{Z})$. Claiming $\alpha^{-1}(235$ MeV$) = 135.5 \pm$
0.3 and matching it to 134.6 does not reproduce $\alpha(0)$ without inputting
standard QED thresholds and lepton masses. (b) Ad Hoc Normalization
Postulates: To obtain $\alpha^{-1} = \pi\sqrt{1836}$, the model postulates five custom
rules ("the axioms themselves, the rotor premise and the two-code reading
remain the framework's assumptions"), specifically setting the
dimensionless charging coefficient u = 1 ("one standing bit per bond of
flux, $\varepsilon_{b} = m_{e} c^{2}$") and hopping stiffness 𝔧 = 1, and equating 1836 bulk
path bits to 16 internal quanta across two distinct lattice realizations
("two-code reading") whose relative spacing is not derived from a single
dynamics. (c) Peer-Review Status of the Coupling Formula: In the
subsequently peer-reviewed Symmetry article (published November 8, 2026),
Kulkarni publishes only the lattice complex construction for a compact
U(1) field on the $\langle100\rangle$ sub-lattice; the $\alpha^{-1} = 134.6$ calculation remains
an unrefereed Zenodo/ResearchGate preprint.

### 3. Wider Literature Sweep: Other Retrieved Candidates Claiming to Derive $\alpha$

Candidate 2: Observer Patch Holography (OPH) — Bernhard Mueller (2026).
Source: Mueller, B. et al. (2026), "The Fine-Structure Constant as an OPH
Pixel Fixed Point" / "First Derivation of the Fine-Structure Constant
from First Principles" (Pragma Research / OPH Paper Stack & GitHub
Repository FloatingPragma/observer-patch-holography, May–Sept 2026).
Claimed formula & value: Solves a "screen-grain" fixed-point closure
equation P⋆ = $\phi + \pi/A_{T}(P$⋆) (where $\phi$ is the golden ratio) to get
$\alpha_{source}^{-1} = (P$⋆ $- \phi)/\pi = 136.994835$..., and applies a "gauge-width fixed
point" shift to obtain $\alpha^{-1} = 137.0356601$... (missing the CODATA value
137.035999177 in the fourth decimal place, by $3.4\times10^{-4})$. Verbatim quote:
"The local equation P⋆ = $\phi + \pi/A_{T}(P$⋆) has a certified root for an
incomplete map... Through the declared branch that root lands close to
the measured fine-structure constant. A physical prediction needs a map
selected without using the measured constant, proof that its two sides
read one quantity, and same-scheme transport to the Thomson limit, so the
match carries diagnostic status; the exact construction and its
assumptions are stated in the technical papers." — "The screen-grain
proposal $(P = \phi + \pi/A_{T}(P))$ has an interval-certified fixed point; its
laboratory attachment awaits the same-scheme hadronic transport."
Evaluation: Not a derivation (Reverse-Engineered Map / Unbridged Ansatz).
In the technical documentation (AXIOM_REFERENCE.md and repository root),
the authors explicitly admit that the functional map $A_{T}(P)$ is "an
incomplete map," that a genuine physical prediction requires "a map
selected without using the measured constant" and "proof that its two
sides read one quantity," and that the match currently "carries
diagnostic status". Furthermore, the output 137.035660 disagrees with
experiment by >$16,000\sigma$.

Candidate 3: Octonionic Trace Dynamics / Exceptional Jordan Algebra —
Tejinder P. Singh (2021–2022). Source: Singh, T. P. (2021), "Quantum
theory without classical time: octonions, and a theoretical derivation of
the fine structure constant 1/137", Int. J. Mod. Phys. D 30, 2142010
(arXiv:2110.07548); and Singh, T. P. (2022), "Quantum gravity effects in
the infrared: a theoretical derivation of the fine-structure constant and
mass ratios of elementary particles", Eur. Phys. J. Plus 137, 664
(arXiv:2110.02062). Claimed formula & value: $\alpha = (9/1024) \exp[(1/3 - 3/8)$
$\times 2/3] = (9/1024) e$^$(-1/36) \approx 0.00729713 = 1/137.04006$. Verbatim quote:
"⋯ $\approx 0.00729713 = 1/137.04006$ ⋯ (11) which agrees with the measured value
to 2 parts in $10^{7}$, and agrees with it exactly if the Karolyhazy correction
is accounted for, and a specific energy scale for the electro-weak
symmetry breaking is assumed." — "The CODATA 2018 value of the fine
structure constant is 0.0072973525693(11) = 1/137.035999084(21) (58). Our
calculated value differs from the measured value in the seventh decimal
place." Evaluation: Not a derivation (Numerological Ansatz + Empirical
Scale Fitting). First, the base formula (9/1024) e^$(-1/36) = 1/137.04006$
is off by 30 ppm (0.004 in $\alpha^{-1})$, where $1024 = 2^{10}$ is selected by opening
brackets in an octonionic Lagrangian and choosing a specific
normalization factor 9/1024, and inserting Jordan eigenvalues into an
exponential $\exp[(\lambda_{1} - \lambda_{2})q]$ with no standard QFT justification for
exponentiating the eigenvalue difference. Second, to bridge the gap from
137.04006 to 137.035999, Singh explicitly states that "a specific energy
scale for the electro-weak symmetry breaking is assumed" via a Karolyhazy
length correction — making the exact match a post-hoc parameter fit.

Candidate 4: Vi Gravitatis (VG) Topological Vortex Model — Benito Vinuesa
Guerrero (Oct 2026). Source: Vinuesa Guerrero, B. (Oct 8, 2026),
"First-Principles Derivation of the Fine-Structure Constant from
Topological Maxwell–Chern–Simons World-Tube Dynamics", ResearchGate
Preprint. Claimed formula & value: $\alpha_{VG}^{-1} = N(1 + \pi^{2}/(2N^{2}))$ =
137.036020694 at leading order, where N = 137. Verbatim quote: "By
modeling the electron as a closed topological vortex filament with
winding integers (p, q) = (1, 137) on a toroidal-hyperbolic manifold, the
fundamental electromagnetic coupling is shown to emerge from topologically
massive gauge dynamics on the three-dimensional world-tube $\Sigma^{3}$ ... At
leading order, the Maxwell-Chern-Simons dispersion relation yields the
exact analytical prediction $\alpha_{VG}^{-1} = N(1 + \pi^{2}/(2N^{2})) = 137.036020694$ ..."
Evaluation: Not a derivation (Circular Postulation / Numerology). The
integer N = q = 137 is explicitly put in by hand as an assumed winding
number (p, q) = (1, 137), and subleading $O(N^{-3})$ terms are tuned to absorb
the residual $-2.153\times10^{-5}$.

Candidate 5: Kosmoplex Theory — Christian Macedonia (Aug 2025). Source:
Macedonia, C. (Aug 22, 2025), "A First-Principles Derivation of the
Fine-Structure Constant from the Axioms of Kosmoplex Theory",
Preprints.org, DOI: 10.20944/preprints202508.1294.v1. Claimed formula &
value: $\alpha^{-1} = 137 + 1/(8\pi) - \gamma/137 = 137.035577 ($where $\gamma \approx 0.57721566$ is
the Euler–Mascheroni constant). Verbatim quote: "Our derivation yields
$\alpha^{-1} = 137.035577$, agreeing with the measured value 137.035999177(21),
relative error $(3.1\times10^{-6}$, or 0.0003%), without empirical input. We
provide rigorous proofs for each component: (1) the combinatorial base
137 from octonionic structure, (2) the rotational correction $1/8\pi$ from
phase space requirements, and (3) the projection distortion $\gamma/137$ from
discrete-to-continuous mapping." Evaluation: Not a derivation
(Numerological Approximation). Combines ad hoc combinatorial integers
((8 choose 4) = 70, etc.) to construct 137, adds $1/(8\pi) \approx 0.0397887$, and
subtracts $\gamma/137 \approx 0.004213$, landing at 137.035577 — which misses the
experimental value by $4.2\times10^{-4} (\approx20,000\sigma)$.

Candidate 6: Holographic Bit–Mode Balance (HBMB) — Dávid Nagy (July–Nov
2025). Source: Nagy, D. (July 2025 / Nov 2025), "A First-Principles
Derivation of the Fine-Structure Constant from Holographic Bit-Mode
Balance" / "U(1)-Driven Local Holographic Horizons: Holographic Bit–Mode
Balance and the $\alpha$-Fixpoint", ResearchGate / Preprints.org. Claimed
formula & value: $\alpha^{-1} = S_{max}/g_{tot} = 137.035998(20)$. Verbatim quote:
"Four conceptually independent inputs enter: (i) the Bekenstein-Hawking
surface bit count, (ii) the degeneracy of the lowest Dirac modes under
MIT boundary conditions, (iii) a curvature-sensitive logarithmic
Seeley-DeWitt correction, and (iv) a uniform-WKB (zeta-regularised)
high-$\ell$ tail that captures large angular-momentum modes. Combining these
yields $\alpha^{-1} = 137.035998(20)$, in numerical agreement with the CODATA 2023
value to better than 0.001%." — "Crucially, B is not a fitting freedom; it
represents measurable or operationally specified properties of the local
electromagnetic environment." Evaluation: Not a derivation (Postulated
Micro-Horizon Boundary + Regularization Scheme Selection). Assumes an ad
hoc "micro-horizon" surrounding an electron with MIT bag boundary
conditions, a specific WKB zeta-regularization cutoff on angular momentum
modes, and an environment-dependent specification B.

Candidate 7: Dx Theory — Preprints.org (Oct 2026). Source: "Derivation
of the Fine-Structure Constant from Dx Theory", Preprints.org (Oct 22,
2026). Claimed formula & value: Combines $\pi, \pi^{2}$, and $4\pi^{3}$ phase-space
volumes: $4\pi^{3} + \pi^{2} + \pi = 124.0251 + 9.8696 + 3.14159 = 137.03630$. Verbatim
quote: "By evaluating the precise topological phase-space volumes required
to execute this 1D transition gate $(\pi)$, anchor the 3D stationary core
$(\pi^{2})$, and unitarily store the background kinetic flux in an orthogonal 4D
Hilbert space $(4\pi^{3})$, we derive the low-energy fine-structure constant
$(1/\alpha \approx 137.036)$ directly from pure geometry." Evaluation: Not a
derivation (Classic Numerology). The polynomial $4\pi^{3} + \pi^{2} + \pi \approx$
137.0363037 is a well-known mathematical coincidence (off by $3\times10^{-4}$ from
137.035999) dressed in ad hoc geometric terminology.

Meta-Theoretical Reference: Sticker (2025/2026) and Jentschura & Nándori
(2014). Source 1: Sticker, H. (Dec 2025 / 2026), "The Fine-Structure
Constant as a Scaled Quantity", Studies in History and Philosophy of
Science 119 (2026) 102199 (arXiv:2512.07027). "I argue instead that $\alpha$ is
a scaled quantity that arises only where the structural scales contributed
by classical electromagnetism (e), quantum mechanics $(\hbar)$, and special
relativity (c) intersect. None of these theories, taken individually,
supplies the independent scales required to define $\alpha$ ... The running of $\alpha$
in QED further demonstrates its status as a scale-dependent coupling
rather than a universal constant. I conclude that $\alpha$ is a domain-specific
structural ratio reflecting contingent relationships among independent
physical scales." Source 2: Jentschura, U. D. & Nándori, I. (2014),
"Attempts at a determination of the fine-structure constant from first
principles: A brief historical overview", Eur. Phys. J. H 39 (2014)
591–613 (arXiv:1411.4673). "It has been a notably elusive task to find a
remotely sensical ansatz for a calculation of Sommerfeld's electrodynamic
fine-structure constant $\alpha_{QED} \sim 1/137.036$ based on first principles."

### 4. Summary Table of Evaluated Candidates
- Selection–Stitch Model (SSM), R. Kulkarni (2026); Zenodo
  10.5281/zenodo.22760383; RG 10.13140/RG.2.2.21524.05764; Symmetry 18,
  1869; $\alpha^{-1}(\mu_{c}) = 2\pi\lambda_{e}/L_{c} = \pi\sqrt{(m_{p}/m_{e})} ($with $m_{p}/m_{e} = 1836)$;
  134.61 (at $\mu = \hbarc/r_{p}$, vs. $135.5 \pm 0.3$ quoted running or 137.036 at
  $q^{2} = 0)$; Postulated-Prior / Combinatorial Approximation: Uses 5 custom
  axioms (u = 1, 𝔧 = 1, two-code reading), misses running target by 0.65%
  and $\alpha^{-1}(0)$ by 1.77%. Plain-text $\pi m_{p}/m_{e}$ is a scraper typo for
  $\pi\sqrt{(m_{p}/m_{e})}$.
- Observer Patch Holography (OPH), B. Mueller et al. (2026); Pragma
  Research / GitHub observer-patch-holography; P⋆ = $\phi + \pi/A_{T}(P$⋆) plus
  gauge-width shift; 137.035660 (off by $3.4\times10^{-4})$; Reverse-Engineered /
  Diagnostic Map: Authors explicitly note in repo docs that $A_{T}(P)$ is an
  "incomplete map," lacks target-independent selection, and carries
  "diagnostic status".
- Octonionic Trace Dynamics, T. P. Singh (2021, 2022); IJMPD 30, 2142010
  (arXiv:2110.07548); EPJP 137, 664; [(9/1024) $\exp((1/3 - 3/8)(2/3))]^{-1}$;
  137.04006 (base); fitted to 137.036 via EWSB scale; Numerological Ansatz
  + Fit: Arbitrary octonionic prefactor 9/1024 and exponentiated Jordan
  roots give 137.04006; exact match requires assuming a specific EWSB
  scale for Karolyhazy corrections.
- Vi Gravitatis (VG) Condensate, B. Vinuesa Guerrero (2026); ResearchGate
  Preprint (Oct 2026); $N(1 + \pi^{2}/(2N^{2})) + O(N^{-3})$ with N = 137;
  137.036021 (leading); 137.03599916 (tuned); Circular Postulation /
  Numerology: Hardcodes winding number (p, q) = (1, 137) as an input
  assumption.
- Kosmoplex Theory, C. Macedonia (2025); Preprints.org
  10.20944/preprints202508.1294.v1; $137 + 1/(8\pi) - \gamma/137$; 137.035577
  (off by $4.2\times10^{-4})$; Numerological Approximation: Ad hoc assembly of 137,
  $1/8\pi$, and Euler's constant $\gamma$.
- Holographic Bit–Mode Balance, D. Nagy (2025); Preprints.org /
  ResearchGate (Jul–Nov 2025); $S_{max}(R$⋆$)/g_{tot}(R$⋆); 137.035998(20);
  Postulated Boundary / Cutoff Tuning: Postulates an electron
  micro-horizon, MIT bag boundary conditions, and zeta-regularized WKB
  tail.
- Dx Theory, Preprints.org (2026); Preprints.org (Oct 2026); $4\pi^{3} + \pi^{2}$ +
  $\pi$; 137.036304 (off by $3.0\times10^{-4})$; Classic Numerology: Standard polynomial
  coincidence in $\pi$.

### 5. HLRE v5.1 Grading of Load-Bearing Claims (under HLRE v5.1 as amended 2026-11-12 — human-gate repeal, external-verification authorization, I1-bound repeal — grades follow the evidence; no grade rises by itself):
Claim LB-1: Arithmetic and Source Evaluation of Kulkarni's SSM (2026).
Statement: In Raghu Kulkarni's Selection–Stitch Model (2026), the
plain-text expression $\alpha^{-1} = \pi m_{p}/m_{e} = 134.6$ is a metadata-scraper
rendering artifact of $\alpha^{-1} = \pi\sqrt{(m_{p}/m_{e})} = \pi\sqrt{1836} \approx 134.61 ($since $\pi \times$
$1836.15 \approx 5768.44 \neq 134.6)$. The formula is not a first-principles
derivation of $\alpha$: it rests on five model-specific postulates (including
setting dimensionless charging and hopping coefficients u = 1, 𝔧 = 1 and
a two-code lattice scale reading), does not derive $\alpha(0) = 137.036$, and
misses its own target running value $\alpha^{-1}(\hbarc/r_{p}) = 135.5 \pm 0.3$ by 0.65%.
Computation: Base Bound (Evidence Class): Direct primary-source
verification (10.5281/zenodo.22760383, 10.13140/RG.2.2.21524.05764,
10.3390/sym18111869) + exact arithmetic verification $\to$ Base = A. Caps
Applied: None (I1-bound and human-gate repealed per 2026-11-12
amendment; primary text and arithmetic are exact and unambiguous).
Ceiling: A. Record: [Claim: LB-1 | Bound: A | Caps: None | Ceiling: A |
Final Grade: A].
Claim LB-2: Evaluation of Other Retrieved Literature Candidates (OPH,
Singh, VG, Kosmoplex, HBMB, Dx). Statement: None of the other six
retrieved frameworks from the 2021–2026 literature (Mueller/OPH 2026;
Singh 2021/2022; Vinuesa Guerrero 2026; Macedonia 2025; Nagy 2025; Dx
Theory 2026) achieves a first-principles derivation of $\alpha$; each relies on
numerological integer/$\pi$ coincidences, unproved boundary/cutoff priors,
incomplete reverse-engineered maps, or empirical scale-fitting.
Computation: Base Bound (Evidence Class): Direct verification of formulas,
numerical outputs, and author caveats from primary preprints/articles and
technical repositories $\to$ Base = A for the specific failure mechanism of
each of the 6 surveyed works (or B where full internal algebraic
appendices of preprints are summarized via verbatim abstract/repo
disclosures). Caps Applied: Scoped to the 6 retrieved frameworks; minor
completeness cap (B) on internal preprint sub-lemmas where only
repository/abstract/excerpt level verification is required to falsify the
exactness or parameter-independence of the formula. Ceiling: B
(conservative across the ensemble; A on the arithmetic discrepancies
against CODATA 2022). Record: [Claim: LB-2 | Bound: A (arithmetic) / B
(text scope) | Caps: Preprint-excerpt scope cap (B) | Ceiling: B | Final
Grade: B].
Claim LB-3: Status of G-C18 ("No rival derives $\alpha$"). Statement: Across all
previously surveyed sources plus the expanded 2026 open-literature sweep
(arXiv, peer-reviewed journals including Symmetry, EPJP, IJMPD, SHPS, and
preprint servers ResearchGate, Zenodo, Preprints.org), no surveyed rival
framework derives $\alpha$ from first principles. However, because an
open-literature search cannot exhaustively inspect every unread or future
manuscript in existence, the universal negative remains UNVERIFIED / ABSTAIN
as an unrestricted universal claim, while the scoped negative bound is
strengthened. Computation: Base Bound (Evidence Class): Systematic
multi-database literature sweep verifying absence of valid derivations
across all retrieved candidates $\to$ Scoped Base = B (upgraded/strengthened
from prior C scoped). Universal Base = UNVERIFIED / ABSTAIN. Caps Applied:
Universal-negative epistemic cap — inductive sweeps over open literature
cannot prove a strict universal negative. A wider sweep that still finds
nothing STRENGTHENS a scoped bound — it does not prove a universal
negative. Ceiling: B (scoped to surveyed literature) / UNVERIFIED (ABSTAIN
as unrestricted universal negative). Record: [Claim: LB-3 (G-C18) | Bound:
C (prior scoped) -> B (strengthened scoped) / UNVERIFIED (universal) |
Caps: Inductive universal-negative cap | Ceiling: B (scoped) / ABSTAIN
(universal) | Final Grade: B (scoped to surveyed literature); UNVERIFIED /
ABSTAIN (as universal negative)].

### 6. Final Verdict for G-C18 Ledger
Verdict: BOUND STRENGTHENED (Scoped: $C \to B)$ / ABSTAIN (UNVERIFIED as
Universal Negative). Reason: Explicit evaluation of Raghu Kulkarni's
Selection–Stitch Model (2026) confirms that its claimed formula $(\alpha^{-1}$ =
$\pi\sqrt{(m_{p}/m_{e})} = \pi\sqrt{1836} = 134.61$, rendered in plain-text scrapers as $\pi$
$m_{p}/m_{e} = 134.6)$ is an unrefereed combinatorial ansatz resting on five ad
hoc model postulates that misses even its own chosen running coupling
scale by 0.65% and does not derive $\alpha(0) = 137.035999$. A broader sweep of
six additional 2021–2026 claimants (Mueller/OPH, Singh, Vinuesa Guerrero,
Macedonia, Nagy, Dx Theory) alongside peer-reviewed meta-analyses
(Jentschura 2014; Sticker 2026) confirms that every retrieved attempt
fails via numerology, circular input of 137, unbridged diagnostic maps, or
empirical scale fitting. A wider sweep that still finds nothing
STRENGTHENS a scoped bound — it does not prove a universal negative.
Accordingly, the scoped claim ("No surveyed rival derives $\alpha$") is
strengthened from C to B, while the unrestricted universal negative ("No
rival anywhere derives $\alpha$") is explicitly marked UNVERIFIED / ABSTAIN.

Sources cited in the response are numbered [1]–[35] (researchgate.net,
arxiv.org, preprints.org, mdpi.com, github.com, floatingpragma.io,
interdependentway.org, idrive.com, medium.com, hisour.com,
physicsforums.com, prereview.org, app.scholars.io). The page's Citations
list shows 6 URLs: https://www.preprints.org/frontend/manuscript/7b5351bbb31debb04dfb4261667baf8e/download_pub, https://www.preprints.org/frontend/manuscript/34a9d2a884fa556491e07cb246576d4c/download_pub, https://www.researchgate.net/publication/394848813_A_First-Principles_Derivation_of_the_Fine-Structure_Constant_from_Holographic_Bit-Mode_Balance, https://www.researchgate.net/profile/David-Nagy-26/publication/394848813_A_First-Principles_Derivation_of_the_Fine-Structure_Constant_from_Holographic_Bit-Mode_Balance/links/68a8b813d9261f6f51ae3b02/A-First-Principles-Derivation-of-the-Fine-Structure-Constant-from-Holographic-Bit-Mode-Balance.pdf, https://arxiv.org/pdf/2512.07027, https://app.scholars.io/research/550184/the-fine-structure-constant-as-a-scaled-quantity. Google Search Suggestions shown (required by Grounding with Google Search) include queries such as "Within the SSM, $\alpha$ is not a free parameter", "134.6" "Kulkarni" "Selection-Stitch", "derive fine structure constant first principles arXiv 2024 2025 2026", and site:arxiv.org "derivation of the fine-structure constant". This was sweep 2 only; no other sweep was started.
