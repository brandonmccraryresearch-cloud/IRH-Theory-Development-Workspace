# SWEEP 5 (G-C21) AUDIT PREP — CDT endpoint

**Prepared:** 2026-11-12 evening CST (research stage; not the audit itself)
**Status:** Gemini's Sweep 5 report LANDED 2026-11-12 17:27 CST, UNAUDITED.
Chat: https://gemini.google.com/u/1/app/2660d093d0b7ee78
**Local record:** no Sweep 5 report file exists locally yet — the Gemini chat is the
only source of the report text. The audit must pull the report from that chat first.
**Governing rules:** truth-seeking-frontier v5; HLRE v5.1 as amended 2026-11-12.
All LaTeX math below is in `$...$` / `$$...$$` delimiters.

## Gemini's verdict (UNAUDITED — claims, not findings)

- The $\sim 2$ vs $\sim 3/2$ tension is bare-coupling and extrapolation-regime
  dependence across Phase C, not a contradiction at one point.
- Canonical point $(\kappa_0, \Delta) = (2.2, 0.6)$: $D_s(\sigma \to 0) \approx 2$,
  grade B (Track E).
- Multi-point finer-lattice shift toward $\approx 3/2$: grade B (Track F).
- Continuum UV limit bounded to $D_s(\sigma \to 0) \in [3/2, 2]$, grade B on the
  interval, ABSTAIN on a sharp value.
- IRH fixed $D = 4$ diverges from CDT in the UV by 2.184 (2005 fit) and 2.50
  (fine-lattice endpoint); agrees only in the IR ($D_s(\infty) = 4.02 \pm 0.10$).

## Pre-verified before the audit (checked 2026-11-12 evening, independent of Gemini)

### 1. The 2005-fit arithmetic CHECKS OUT

Ambjørn, Jurkiewicz & Loll 2005 (PRL 95, 171301) fit, as quoted in
Benedetti & Henson and in Hořava 2009:

$$D_s(\sigma) = 4.02 - \frac{119}{54 + \sigma}$$

- $D_s(0) = 4.02 - 119/54 = 4.02 - 2.2037 = 1.816$ (recomputed locally).
- IRH divergence vs 2005 fit: $4 - 1.816 = 2.184$ — matches Gemini's 2.184 exactly.
- Fine-lattice endpoint $3/2$: $4 - 3/2 = 2.50$ — matches Gemini's 2.50 exactly.
- IR value $D_s(\infty) = 4.02 \pm 0.10$ confirmed in Hořava 2009
  (arXiv:0902.3657), citing Ambjørn et al. [11] firsthand.

### 2. The $\approx 3/2$ endpoint is anchored in Coumbe & Jurkiewicz 2015

Coumbe & Jurkiewicz, JHEP 03 (2015) 151, abstract (retrieved firsthand):
"the dimension of spacetime smoothly decreases from $\sim 4$ on large distance
scales to $\sim 3/2$ on small distance scales." This is the finer-lattice /
relative-lattice-spacing result Gemini's Track F claim rests on. The audit
still needs to check Gemini's "multi-point" claim against the paper's actual
data points — the abstract alone supports the endpoint, not the multi-point
characterisation.

### 3. PRD citation: 93 is CORRECT, 87 is the error

Phys. Rev. D **93**, 104032 (2016) is real and CDT: Ambjørn, Coumbe,
Gizbert-Studnicki & Jurkiewicz, "Searching for a continuum limit of causal
dynamical triangulation quantum gravity." Confirmed verbatim in the reference
list of Cooperman & Dorghabekov, arXiv:1812.09331. Gemini's single "87, 104032"
citation is the wrong volume; "93, 104032" is right. Correction, verdict-neutral.

### 4. The "Ambjørn (2026) abstract duplicates Coumbe & Jurkiewicz 2015" defect looks FALSE

Checked against both arXiv abstract pages firsthand:

- arXiv:2604.05641 (Ambjørn & Loll, submitted 7 Apr 2026, 20 pp., invited
  Scholarpedia contribution): "Causal Dynamical Triangulations (CDT) is a
  methodology to define and compute the gravitational path integral, whose aim
  is a fully fledged nonperturbative quantum field theory of gravity and
  spacetime. Analogous to lattice formulations of nongravitational quantum
  fields, CDT provides a blueprint for lattice quantum gravity..."
- Coumbe & Jurkiewicz 2015 (JHEP 03 (2015) 151): "We calculate the spectral
  dimension for a nonperturbative lattice approach to quantum gravity, known as
  causal dynamical triangulations (CDT), showing that the dimension of
  spacetime smoothly decreases from $\sim 4$ on large distance scales to
  $\sim 3/2$ on small distance scales..."

These are plainly different texts — different sentences, different structure,
different claims. A verbatim duplication is refuted on the face of the two
abstracts. **This is the sharpest audit finding to confirm:** if Gemini's
report really asserts verbatim duplication, that is a Gemini fabrication (or a
confusion with some other text), and the defect evaporates. The audit must
quote Gemini's exact sentence and compare it against both abstracts in full
before grading it.

### 5. Canonical point $(\kappa_0, \Delta) = (2.2, 0.6)$ — plausible, not yet confirmed

$(\kappa_0, \Delta) = (2.2, 0.6)$ appears as a standard simulation point in the
CDT spectral-gap literature (e.g. the Lattice 2019 spectral-methods work shows
histograms at $k_0 = 2.2$ and $\Delta = 0.6$ in phase $C_{dS}$). Consistent
with Gemini's "canonical point" framing; the audit should still confirm the
point and its $D_s(\sigma \to 0) \approx 2$ value against Gemini's cited source,
not against this plausibility check.

## Still open for the audit (needs the Gemini report text)

- **C-6 ledger row:** renders with no computation or grade in Gemini's report.
  Cannot be checked without the report; the audit must read the row as rendered
  in the chat and grade it (or mark it NOT RUN if it is genuinely empty).
- **Gemini's cited sources for the canonical point and the multi-point shift:**
  verify each citation resolves to the claimed paper, table, or figure.
- **The interval grade:** $D_s(\sigma \to 0) \in [3/2, 2]$ as a grade-B interval
  vs ABSTAIN on a sharp value — check whether the interval follows from the
  cited endpoints or is Gemini's own interpolation.
- **IRH consequence:** IRH's fixed $D = 4$ vs CDT's UV $D_s \in [3/2, 2]$ —
  confirm the audit states the consequence at its true grade (no IRH grade
  change is implied by Gemini's verdict as summarised, but the audit decides).

## Also resolved in this pass (G-C20 audit, separate item)

The $D = 6$ sign flag from the G-C20 audit is now RESOLVED — see the dated
correction note appended to `AUDIT_gemini-sweep-g-c20_2026-11-12.md`. The arXiv
text (gr-qc/9308012, §5, near eq. (82)) reads: "Assuming two inequalities,
namely $\Delta(x)_{BF} < 0$ and $\Delta(x^3)_{BF} > 0$..." — so the audit
file's second inequality was a mistranscription ($x^3$ read as $x_3$, sign
flipped). Verdict-neutral; the $D = 6$ case stays conditional on the spectrum.

## Next after the audit

- Sweep 6 (G-D6) still to launch on gemini.google.com as Deep Research, Argon
  account, full HLRE amendment + IRH v93.1 PDF attached — launch after the
  Sweep 5 audit lands, not before.
- Nothing in this prep file is filed, committed, or written into the manuscript.
