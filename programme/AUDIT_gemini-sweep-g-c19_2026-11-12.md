# Audit — Gemini Sweep 3 (G-C19): verified primary-source Ġ/G constraint

**CLAIM:** Gemini 4 (Argon)'s Sweep 3 verdict — G-C19 RESOLVED, upgraded
from ABSTAIN to G8/F1; Dirac varying-$G (G \propto t^{-1})$ FALSIFIED at >$7,500\sigma$
against modern Lunar Laser Ranging — is correct as stated, with two
minor citation corrections that change no number and no gate.
**STATUS:** VERIFIED (G-C19.1 VERIFIED, G-C19.2 VERIFIED, G-C19.3
VERIFIED; overall G-C19 RESOLVED at G8/F1, scoped as below).

**Audit:** local claim-by-claim audit of
`gemini-sweep-g-c19-2026-11-12.md` (Gemini 4 Argon, AI Studio,
autopoieticdragon@gmail.com, 2026-11-12 16:07–16:13 CST, 4,816 tokens,
\$0; Temporary-mode chat, so the saved file is the record). Nothing
taken from Gemini on trust: all three primary sources read firsthand
(full text, not abstracts alone, except Williams where the abstract
plus the PRL body text were both checked), Dirac 1938 read from the
primary-source scan, all arithmetic re-run locally (Python 3.11.16,
conda env `jacobian-conjecture-2d`, exit 0).
**Verdict counts:** claims 3 VERIFIED, 0 VERIFIED WITH CORRECTIONS,
0 REFUTED, 0 ABSTAIN. Source/arithmetic checks: 27 run — 25 PASS,
2 CORRECTED, 0 FAIL, 0 NOT RUN.

## 1. Primary-source checks (verbatim)

### 1A. Biskupek, Müller & Torre 2021 — PASS

- Source: L. Biskupek, J. Müller, J.-M. Torre, "Benefit of New
  High-Precision LLR Data for the Determination of Relativistic
  Parameters," Universe 7(2), 34 (2021); arXiv:2012.12032 (v1,
  22 Dec 2020). Read in full via arXiv PDF.
- Abstract value confirmed verbatim: "a possible temporal variation
  of the gravitational constant Ġ/$G_{0} = (-5.0 \pm 9.6) \times 10^{-15}$ yr${}^{-1}$",
  alongside $\Delta(m_{g}/m_{i})_{EM} = (-2.1 \pm 2.4) \times 10^{-14}$,
  $\beta-1 = (6.2 \pm 7.2) \times 10^{-5}$, $\gamma-1 = (1.7 \pm 1.6) \times 10^{-4}$ — all four
  match Gemini's quote exactly.
- §4.2 equations confirmed verbatim (separate-parameter fit):
  Ġ/$G_{0} = (-5.0 \pm 9.6) \times 10^{-15}$ yr${}^{-1}$,
  $\ddot{G}/G_{0} = (1.6 \pm 2.0) \times 10^{-16}$ yr${}^{-2}$. The current value is $0.52\sigma$
  from zero — consistent with Ġ = 0, as Gemini grades it (F0).
- §4.2 joint fit (linear + quadratic together), NOT quoted by
  Gemini, read as a robustness check: Ġ/$G_{0} = (0.2 \pm 1.3) \times 10^{-14}$
  yr${}^{-1}$. Also consistent with zero; the Dirac discrepancy against
  this joint fit is $5,574\sigma ($audit recomputation) — the falsification
  does not depend on which fit is used.
- Data span confirmed: 27,485 normal points, April 1970 to
  April 2020 (50 yr), 22,021 green + 5,464 IR; DE421 initial values,
  DE430 lunar-rotation model; LUNAR software (IfE Hannover).
- §4.2 also independently corroborates the MESSENGER bound:
  "From the analysis of MESSENGER data, [45] get an upper limit
  for Ġ/$G_{0} < 4 \times 10^{-14}$ yr${}^{-1}$."

### 1B. Hofmann & Müller 2018 value — PASS (value) / CORRECTED (table number)

- Value confirmed verbatim from Biskupek Table 1 (§4):
  Ġ/$G = (7.1 \pm 7.6) \times 10^{-14}$ yr${}^{-1}$ for Hofmann and Müller [13],
  against $(-5.0 \pm 9.6) \times 10^{-15}$ yr${}^{-1}$ for the current analysis;
  §4.2 restates it in equation form. Reference [13] is
  F. Hofmann & J. Müller, Class. Quantum Grav. 35, 035015 (2018).
- **CORRECTION 1 (minor, citation only):** Gemini's note says the
  value is in "Table 3 / Section 4". It is in **Table 1** in §4.
  The value itself is correct; no number or gate changes.
- "8-fold tightening": $\sigma 7.6 \times 10^{-14} \to 9.6 \times 10^{-15}$ is a factor
  7.92 — Gemini's "8-fold" is correct to the quoted precision.

### 1C. Williams, Turyshev & Boggs 2004 — PASS

- Source: J. G. Williams, S. G. Turyshev, D. H. Boggs, "Progress
  in Lunar Laser Ranging Tests of Relativistic Gravity," Phys. Rev.
  Lett. 93, 261101 (2004); arXiv:gr-qc/0411113v2.
- Abstract value confirmed verbatim: "The search for a time
  variation in the gravitational constant results in
  Ġ/$G = (4 \pm 9) \times 10^{-13}$ yr${}^{-1}$, consequently there is no evidence
  for local (~1 AU) scale expansion of the solar system." Also
  confirmed in the PRL body text (same value, same wording).
- Data: LLR March 1970 to April 2004, 15,553 normal points,
  McDonald/Haleakala/OCA; JPL simultaneous numerical integration
  ("the relativistic model used for JPL solutions"). Analysis
  group genuinely independent of IfE Hannover — the
  "independent pipelines" point stands.

### 1D. Genova et al. 2018 (MESSENGER) — PASS

- Source: A. Genova et al., "Solar system expansion and strong
  equivalence principle as seen by the NASA MESSENGER mission,"
  Nature Communications 9, 289 (2018); doi:10.1038/s41467-017-02558-1.
  Read in full via nature.com HTML and the MIT DSpace record
  (hdl.handle.net/1721.1/118777).
- Ġ$M\odot$/GM$\odot$ value confirmed verbatim (DSpace abstract, identical
  to the journal abstract): "we obtain an estimate of the time
  variation of the Sun gravitational parameter,
  Ġ$M\odot$/GM$\odot = (-6.13 \pm 1.47) \times 10^{-14}$, which is consistent with the
  expected solar mass loss due to the solar wind and interior
  processes."
- Bound confirmed verbatim (Nature body text, Introduction and
  Discussion): "constrain |Ġ|/G to be lower than $4.0 \times 10^{-14}$
  per year" / "The reconstructed Ġ/G is lower than $4.0 \times 10^{-14}$
  per year with an uncertainty that is mainly limited by the
  knowledge of the solar interior evolution $(2\sigma = 5.0 \times 10^{-14}$
  per year)."
- Solar-mass-loss interpretation confirmed: the retrieved negative
  rate is "close to the theoretical computations of the Sun's mass
  loss"; fusion ~$-0.679 \times 10^{-13}$ yr${}^{-1}$ plus solar wind $-(2$–\$3$) \times 10^{-14}$\$
  to $-(4.2$–\$6.9$) \times 10^{-14}$\$ yr${}^{-1}$, expected total $-(0.9$–\$1.1$) \times 10^{-13}$\$
  yr${}^{-1}$. The measured $-6.13 \times 10^{-14}$ yr${}^{-1}$ sits inside the expected
  solar-mass-loss range — i.e. the entire measured Ġ$M\odot$/GM$\odot$ signal
  is accounted for by known solar mass loss, leaving no room for
  a Ġ contribution at the $4 \times 10^{-14}$ yr${}^{-1}$ level. Gemini's reading
  is correct.
- Mission span confirmed: MESSENGER radio tracking January 2008
  to April 2015 (~7 yr), as Gemini states.

### 1E. Dirac 1938 — PASS (primary source)

- Source: P. A. M. Dirac, "A new basis for cosmology," Proc. R.
  Soc. Lond. A 165, 199–208 (1938). Read from the primary-source
  scan.
- $G \propto t^{-1}$ confirmed verbatim (pp. 205–206): "the gravitational
  force between them must be inversely proportional to the epoch.
  Thus the gravitational constant will be inversely proportional
  to the epoch." The statement is Dirac's own, in the atomic-units
  metric of the paper, and it is the premise from which
  Ġ/$G = -1/t$ follows. No secondary source needed.
- Note for the record: Dirac's paper is explicitly a first
  approximation ("the resulting theory will be valid only as a
  first approximation and may need amendment"), and Gamow's
  objection (that $G \propto 1/t$ does not necessarily follow) is noted
  in the literature — but the *statement* Gemini attributes to
  Dirac is verbatim, and the falsification targets the statement
  as stated, which is the correct target.

## 2. Arithmetic checks (all re-run locally, Python 3.11.16, exit 0)

| # | Check | Audit result | Gemini | Verdict |
|---|-------|--------------|--------|---------|
| 1 | Dirac Ġ/$G = -1/t_{0}$, $t_{0} = 13.8$ Gyr | $-7.246 \times 10^{-11}$ yr${}^{-1}$ | $-7.25 \times 10^{-11}$ | PASS |
| 2 | vs Biskupek \|$-7.25e-11 - (-5.0e-15)$\| / 9.6e-15 | $7,547.8\sigma$ | $\approx 7.55 \times 10^{3}\sigma$ | PASS |
| 3 | vs Williams \|$-7.25e-11 - 4e-13$\| / 9e-13 | $80.96\sigma$ | $80.9\sigma$ | PASS |
| 4 | vs Williams \|Dirac\| / $\sigma$ | 80.52 (80.56 with rounded $-7.25)$ | 80.6 | PASS (rounding) |
| 5 | vs MESSENGER \|Dirac\| / 4e-14 | $1,811.6\times$ | $1.81 \times 10^{3}\times$ | PASS |
| 6 | vs Hofmann 2018 \|Dirac $- 7.1e-14$\| / 7.6e-14 | $954.4\sigma$ | (not quoted) | PASS (extra) |
| 7 | vs Biskupek joint fit $(0.2 \pm 1.3)e-14$ | $5,574.3\sigma$ | (not quoted) | PASS (extra) |
| 8 | Tightening factor 7.6e-14 / 9.6e-15 | 7.92 | "8-fold" | PASS |
| 9 | $t_{0}$ sensitivity (13.797 vs 13.8 Gyr) | 0.022% | — | PASS (immaterial) |
| 10 | Biskupek central value \|$-5.0e-15$\| / 9.6e-15 | $0.52\sigma$ from 0 | consistent with Ġ = 0 | PASS |

- Headline ">$7.5 \times 10^{3}\sigma$" is exact: $7,547.8\sigma > 7,500\sigma$. The
  falsification does not hinge on the tightest bound: it is $81\sigma$
  against the 2004 bound, $954\sigma$ against the 2018 Hannover bound,
  and $1,812\times$ the MESSENGER upper bound. Every route falsifies
  Dirac'$s G \propto t^{-1}$ by orders of magnitude.
- Rosenband scope statement — PASS: the Rosenband $\dot{\alpha}/\alpha$ atomic-clock
  bound constrains a different observable and cannot directly
  falsify a pure varying-G model without a unified-coupling
  relation. Gemini's distinction is correct and honestly drawn.

## 3. Scope check — is anything tighter / missed?

- Targeted check for a more recent or tighter primary LLR bound
  (2023–2025): none found. The most recent literature citing a
  current LLR value quotes (Ġ/$G)_{0} = (2 \pm 7) \times 10^{-13}$ yr${}^{-1}$
  (Trivedi, arXiv:2512.16804, Dec 2025) — a conservative
  combination, LOOSER than Biskupek 2021 by a factor ~70 in $\sigma$.
  Biskupek et al. 2021 remains the tightest primary LLR bound
  found. Gemini missed nothing that changes the numbers.
- Biskupek §4.2 itself cites ephemeris bounds of $7 \times 10^{-14}$ and
  $2 \times 10^{-13}$ yr${}^{-1}$ — consistent with the search above.
- Alvey et al. 2020 (cited by Gemini §4 as not read) exists:
  arXiv:1910.10730, Eur. Phys. J. C (2020),
  $G_{BBN}/G_{0} = 0.99^{+0.06}$_${-0.05} (2\sigma)$; linear-time
  Ġ/$G_{0} = 0.7^{+3.8}$_${-4.3} \times 10^{-12}$ yr${}^{-1} (2\sigma)$. Its $2\sigma$ upper
  bound $(4.5 \times 10^{-12}$ yr${}^{-1})$ is $16\times$ Dirac's value — i.e. BBN/CMB
  alone would NOT falsify Dirac — which is exactly why Gemini's
  ABSTAIN on early-universe G(z) is honest and why the local
  falsification rests on LLR/MESSENGER, not on BBN. No conflict.

## 4. Grading check (HLRE v5.1 as amended 2026-11-12)

Gemini grades: G-C19.1 G8/F0; G-C19.2 G8/F0; G-C19.3 G8/F1;
gap G-C19 RESOLVED at G8/F1.

- **Vocabulary note (clarification, not a correction).** "G8" is
  the WS-D task-12 claim label carried from the prior state
  (Dirac's arithmetic was graded G8, F3 there); "F0/F1" are that
  task's falsification-status labels (F0 = consistent with the
  null, F1 = falsified), not HLRE Track F grades. The audit
  accepts them as the programme's local convention. In HLRE
  Track F terms, the falsification computation (G-C19.3) reads
  **F1**: independently re-derived with a closed premise ledger —
  Gemini's route plus this audit's independent recomputation,
  with every input verified verbatim from a primary source.
- **G-C19.1 — VERIFIED, G8/F0.** Two independent primary LLR
  analyses (JPL 2004; IfE Hannover/OCA 2021), values verified
  verbatim, both consistent with Ġ = 0. The bound is a direct
  primary-literature measurement, not a derivation. Grade stands.
- **G-C19.2 — VERIFIED, G8/F0.** Independent planetary-ephemeris
  route (MESSENGER Mercury ranging), value and bound verified
  verbatim, solar-mass-loss interpretation verified. Grade stands.
- **G-C19.3 — VERIFIED, G8/F1.** Dirac'$s G \propto t^{-1}$ verified
  verbatim from the 1938 primary source; the prediction
  $-7.25 \times 10^{-11}$ yr${}^{-1}$ recomputed; the discrepancy is $7,548\sigma$
  against the tightest bound and $\geq81\sigma$ against every bound
  checked. Falsified as a local secular variation. Grade stands.
- **CORRECTION 2 (minor, citation only):** G-C19.1's computation
  record says "direct primary literature verification across
  independent ephemeris pipelines DE421/430 & IfE Hannover".
  DE421/DE430 belong to Biskupek (DE421 initial values, DE430
  lunar-rotation model). Williams et al. 2004 predates both
  (DE421 released 2008, DE430 in 2013) and used JPL ephemerides
  of its era. The substance — two genuinely independent analysis
  pipelines, JPL vs IfE Hannover — is correct; the DE numbers
  attach to the wrong paper. No number or gate changes.

## 5. Scope honesty — does "RESOLVED" overclaim?

No, as stated, with the scope read as Gemini writes it in §4:

- RESOLVED covers the gap as defined: a verified primary-source
  Ġ/G constraint exists (it does, three of them), and the Dirac
  varying-G verdict is settled for **unscreened local secular
  variation** (it is, at >$7,500\sigma)$.
- Gemini's §4 honestly leaves ABSTAIN: (a) cosmological /
  early-universe G(z) step-function transitions (BBN/CMB bounds,
  e.g. Alvey et al. 2020, not read in full text); (b) screened /
  chameleon scalar-tensor models, where $G_{eff}$ varies only in
  low-density environments and is screened inside the Solar
  System — local LLR/MESSENGER bounds cannot rule those out.
- The audit confirms both ABSTAINs are genuine: the Alvey
  linear bound $(\pm4 \times 10^{-12}$ yr${}^{-1})$ is too loose to falsify Dirac,
  and screening is by construction invisible to Solar-System
  tests. The "RESOLVED" headline must not be read as "G is
  invariant everywhere" — Gemini's own guard statement says
  exactly that, and the audit endorses the guard as written.

## 6. Final verdict

**G-C19: RESOLVED, grade G8/F1** (was ABSTAIN, no grade).

- The gap asked for a verified primary-source Ġ/G constraint.
  It now has three, all verified verbatim from primary sources
  by this audit, plus the Dirac verdict settled at $7,548\sigma$.
- No IRH grade changes: this gap concerns an external
  (Dirac) hypothesis and the empirical Ġ/G bound, not any IRH
  claim. IRH's own stance on varying G is untouched by this
  sweep.
- Corrections recorded: (1) Hofmann & Müller value is in
  Biskupek Table 1, not Table 3; (2) DE421/DE430 attach to
  Biskupek, not to Williams 2004. Both citation-only.
- Open items carried forward (ABSTAIN, unchanged): screened /
  chameleon varying-G; early-universe G(z) (BBN/CMB).

## 7. Check log (26 checks)

| # | Check | Result |
|---|-------|--------|
| 1 | Biskupek abstract Ġ/$G_{0} = (-5.0 \pm 9.6)e-15$ | PASS (verbatim) |
| 2 | Biskupek §4.2 separate-fit equations | PASS (verbatim) |
| 3 | Biskupek §4.2 joint fit $(0.2 \pm 1.3)e-14$ | PASS (verbatim, extra) |
| 4 | Hofmann & Müller $2018 (7.1 \pm 7.6)e-14$ value | PASS (verbatim, Table 1) |
| 5 | Gemini "Table 3" citation | CORRECTED $\to$ Table 1 |
| 6 | 8-fold tightening $(7.92\times)$ | PASS |
| 7 | Biskupek data span 1970–2020, 27,485 NP | PASS |
| 8 | Williams abstract Ġ/$G = (4 \pm 9)e-13$ | PASS (verbatim) |
| 9 | Williams PRL body text, same value | PASS |
| 10 | Williams data span / JPL independence | PASS |
| 11 | Genova \|Ġ\|/G < 4e-14 bound | PASS (verbatim) |
| 12 | Genova Ġ$M\odot$/GM$\odot = (-6.13 \pm 1.47)e-14$ | PASS (verbatim, DSpace) |
| 13 | Genova solar-mass-loss interpretation | PASS (verbatim) |
| 14 | Genova MESSENGER span ~7 yr | PASS |
| 15 | Dirac $G \propto t^{-1}$, primary source 1938 | PASS (verbatim) |
| 16 | Dirac arithmetic $-1/13.8$ Gyr = $-7.25e-11$ | PASS $(-7.246e-11)$ |
| 17 | vs Biskupek \$7.55$e3\sigma$\$ | PASS $(7,547.8\sigma)$ |
| 18 | vs Williams $80.9\sigma$ | PASS $(80.96\sigma)$ |
| 19 | vs MESSENGER \$1.81$e3\times$\$ | PASS $(1,811.6\times)$ |
| 20 | vs Hofmann \$2018 ~$954\sigma$\$ | PASS (extra) |
| 21 | vs joint fit ~$5,574\sigma$ | PASS (extra) |
| 22 | No tighter recent LLR bound (2023–2025) | PASS (none found) |
| 23 | Alvey et al. 2020 exists (arXiv:1910.10730) | PASS |
| 24 | DE421/430 attribution to Williams 2004 | CORRECTED $\to$ Biskupek only |
| 25 | Rosenband scope statement | PASS |
| 26 | §4 ABSTAINs honest (screened, G(z)) | PASS |
| 27 | $t_{0}$ sensitivity 0.022% | PASS (immaterial) |

Tally: 27 checks run — 25 PASS, 2 CORRECTED, 0 FAIL, 0 NOT RUN.

## 8. Provenance and limits

- Sources read firsthand: arXiv:2012.12032 (abstract + full PDF),
  arXiv:gr-qc/0411113 (abstract + full PDF), Nature Communications
  9, 289 (full HTML) + MIT DSpace record hdl.handle.net/1721.1/118777,
  Dirac 1938 primary scan (knowen S3 mirror of the Royal Society
  paper), arXiv:1910.10730 (abstract, Alvey et al. 2020),
  arXiv:2512.16804 (abstract excerpt, Trivedi 2025, for the
  scope check).
- Arithmetic: Python 3.11.16 (conda env jacobian-conjecture-2d),
  two exec runs, both exit 0. No GCP spend. No manuscript edits,
  no commits, no author contact.
- This audit grades the sweep's claims about the literature and
  the arithmetic confrontation. It does not re-derive LLR or
  MESSENGER data reductions; those rest on the peer-reviewed
  primary analyses cited.
