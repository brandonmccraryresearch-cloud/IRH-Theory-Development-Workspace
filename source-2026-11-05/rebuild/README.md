# LEG — IRH TEX SOURCE REBUILD (2026-11-05, from the author's supplied source package)

## CLAIM
Rebuilt from the author's REAL source (not from PDF extraction). The PDF-rebuilt
tex from the 2026-11-04 autonomous run is SUPERSEDED by this rebuild.

## STATUS: PASSED (compile) with two open-question verdicts + flags — see below
- Source package: ~/workspace/user/files/IRH_v93_1_source_package_2_ifrk.zip
  (3,202,228 bytes, 17 files), extracted to
  ~/workspace/research/irh/source-2026-11-05/IRH_v93_1_source/ (pristine).
- Authoring source is paper_v931.md; IRH_v93_1.tex is generated from it by the
  supplied md2tex.py, which regenerates the shipped .tex BYTE-IDENTICALLY
  (diff 0 lines, 84,988 bytes — verified 2026-11-05). Worked from the shipped
  .tex as the base.
- Rebuilt tex: IRH_v93_1_source_rebuilt.tex (1,144 lines, 101,316 bytes).
- Output PDF: IRH_v93_1_source_rebuilt.pdf — XeTeX 3.141592653-2.6-0.999998
  (TeX Live 2026), pass 1 rc=0, pass 2 rc=0, 0 errors, 0 undefined
  references, 0 missing characters, 34 pages, A4, 1,852,759 bytes
  (shipped PDF: 31 pp; PDF-rebuild: 32 pp; +3 pp here = rebuild front matter
  + 26 expansion passages + real figures).
- Fonts embedded (pdffonts): FiraSans-Bold, FiraSans-Regular, FiraSans-Italic,
  FiraMono-Regular, FiraMono-Bold, FiraMath-Regular, NotoSansMath-Regular
  (setminus fallback), NotoSans-Regular (subscript-a fallback). All embedded.
- NO FAKE BOLD (Brandon, 2026-11-05 00:17 CST: "No fake bold"): grep -c
  FakeBold on the final .tex = 0; both XeLaTeX logs contain 0 mentions of
  FakeBold / synthetic / font-shape-undefined. Bold faces are pinned by
  filename to the real weights (FiraSans-Bold.otf, FiraSans-BoldItalic.otf,
  FiraMono-Bold.otf) because fontspec's DEFAULT resolution for this family
  maps \textbf to ExtraBold (verified in a minimal test) — real weight, but
  not the intended Bold. After pinning, pdffonts shows FiraSans-Bold, no
  ExtraBold, no Medium. Fira Math ships Regular only (no Bold weight exists
  in this TeX Live tree), so no bold math version is declared; the 21
  \mathbf occurrences render in the regular math weight via unicode-math's
  fallback — NOT synthesized (no poor-man's-bold overprinting anywhere).
- SymPy 1.14.0: sympy_verify.log 59 PASS + 1 intentional FAIL-flag
  (11.85%/11.90% source inconsistency, see verdict (a)).
- Second tools: second_tool_verify.log 20 PASS, 0 FAIL (python-flint 0.8.0 +
  enumeration); singular_verify.log PASS (Singular 4.4.1, E6 det = 3,
  64/141 check).
- Figures: REAL fig01–fig10.png from the supplied package (symlinked figs/).
- Build deps installed into the conda TeX Live 2026 via tlmgr (2026-11-05):
  xltabular + ltablex + newunicodechar (the shipped .tex needs all three).
- No git commit made (per brief). No Lean build run in this leg; the Lean
  claim (§VI-A.2, lake build exit 0, 3101 jobs) is carried as stated.

## OPEN QUESTION (a) — 11.85% vs 11.90% band: VERDICT — genuine source inconsistency, NOT a garble
The source .tex genuinely contains BOTH values (paper_v931.md agrees;
the shipped PDF shows both too):
- L281 (PREDICTION): "occupying 11.85\% of the scanned plane"
- L296: "This qualification must accompany every citation of the 11.85\% figure."
- L298: "(11.90\% at $w_6=0$ to 8.47\% at $w_6=0.2$)... The $w_6=0$ value
  independently reproduces the 11.85\% obtained by different code."
- L842 (App. A item 8): "giving 63.8\% against the correct 11.9\%."
So the $w_6=0$ band value is stated as BOTH 11.90% (parenthetical) and
11.85% (next sentence), and Appendix A calls 11.9% "the correct" value.
The discrepancy is 0.05 percentage points. This rebuild KEEPS 11.85% as the
headline figure and FLAGS the inconsistency in the front matter; it does not
resolve it. Which value is canonical is a decision for Brandon.

## OPEN QUESTION (b) — $\tau_{D}4/\tau_{BCC}$: VERDICT — source says $\sqrt{2}$; correction CONFIRMED, no change needed
The source .tex states $\sqrt{2}$ everywhere:
- L45 (abstract): "$\tau_{D_4}/\tau_{\mathrm{BCC}}=\sqrt{2}$"
- L216 (§II.5): "and $\tau_{D_4}/\tau_{\rm BCC}=\sqrt2$ exactly"
- L218 (§II.5): "Closed forms: $\tau_{D_4}=4/\sqrt6$ and
  $\tau_{\rm BCC}=2/\sqrt3$, in ratio exactly $\sqrt2$"
- L674 (§VI-A.1): "an identity $\tau_{D_4}/\tau_{\rm BCC} = \sqrt{2}$"
The shipped PDF renders $\sqrt{2}$ as well (pdftotext -layout puts the radical on
its own layout line, which is what made it LOOK like "= 2" in extraction).
The PDF-rebuild's "correction" of a stated 2 addressed a pdftotext-layout
artifact, not a source error. The source was right all along. SymPy
confirms $(4/\sqrt{6})/(2/\sqrt{3}) = \sqrt{2}$ exactly.

## SOURCE DEFECTS FIXED IN THIS REBUILD (present in the shipped PDF too)
- Tex L45: `\\hyperref[ref-40]{[40]}` (double backslash, dashed label)
  renders literally as "hyperref[ref-40][40]" in the shipped PDF (verified in
  the shipped PDF's extracted text). Corrected to `\hyperref[ref40]{[40]}`.
  Same sentence's `[ref-1]/[ref-2]/[ref-3]` use dashed labels that do not
  exist (labels are ref1/ref2/ref3); corrected to undashed labels.
- Shipped .tex does NOT compile as-shipped in this environment: the preamble
  references a `fonts/` directory that is NOT in the supplied package;
  verified failure: `fontspec Error: The font "NotoSans-Regular" cannot be
  found` (xelatex exit 1). The Fira substitution repairs this.
- Two literal text-mode $\mathbb{Z} (U+2124)$ characters (§II.2 table, §II.5 table) are
  missing from Fira Sans; they now render via `\newunicodechar{ℤ}{$\mathbb{Z}$}`
  (Fira Math has U+2124; same glyph, math mode). 0 missing characters after.

## DIFF NOTE vs the PDF-REBUILD (2026-11-04)
What the source resolved:
- $\tau$ ratio: source correct $(\sqrt{2})$; the PDF-rebuild's "correction" was an
  artifact fix, not a source fix. No correction needed here.
- $r_{c}$: source has $r_{c} = (2/9)\cdotu^{2}\tau^{2}/(v\cdotq_{4})$ correct; the PDF-rebuild's
  "ledger garble $92\dots$" fix addressed the PDF-extracted text, not the source.
- Figures: real fig01–fig10.png now; PDF-rebuild had captioned placeholders.
- Structure: this rebuild KEEPS the author's structure (unnumbered
  \section*/\subsection*, $$...$$ display math, \hyperref[refN] links,
  xltabular tables). The PDF-rebuild had renumbered sections, equation
  environments, \cite references, and flagboxes.
- Provenance: .md is the authoring source (md2tex.py regenerates the .tex
  byte-identically); the PDF-rebuild had to assume PDF text was faithful.
What is unchanged between the two rebuilds:
- Manuscript content is the same throughout (the PDF-rebuild was faithful
  to the PDF text); the 26 "Expansion (source rebuild)" passages are the
  PDF-rebuild's 26 expansions, adapted only where the source already states
  the result $(\tau \sqrt{2}$ wording; "in the extracted text" $\to$ "in the source text").
- Verification results identical: SymPy 59 PASS + 1 FAIL-flag; second tool
  20 PASS; Singular PASS.
What remains flagged (same as PDF-rebuild, plus one new item):
- 11.85% vs 11.90% band inconsistency (genuine, see verdict (a)).
- All simulation/scan outcomes, several geometric enumerations (internal
  consistency only), the Lean build claim (carried as stated, no Lean run),
  the R = 2589 normalization, and the $\alpha^{-1}$ ansatz (arithmetic only, no
  physical derivation) — flagged unverifiable-from-source, no numbers invented.
- NEW: \mathbf renders in regular math weight (Fira Math has no Bold);
  no synthesis was used.
- NEW: bold pinning required (fontspec default maps \textbf to ExtraBold
  for this family); pins are in the preamble and verified in the PDF.

## GRADE DISCIPLINE
No grade changes. Math Grade A; physical/substrate reading $\leq C/D$; three
generations INPUT; Perelman $\tau \neq$ IRH $\tau$; S = 64/141 never identified with
Perelman's W.
