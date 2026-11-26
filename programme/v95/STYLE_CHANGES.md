# STYLE_CHANGES — journal-style restyle, 2026-11-26

Requested by Brandon (2026-11-26 07:00 CST): bring the papers to a top-tier-journal look, with citation links and colour, using the preamble of the corrected topology report (`main_corrected.tex`, 2026-11-25) as the model.

**This is a styling pass only.** No sentence, number, claim, grade, label or reference target was changed. The body diff against the previous edition is limited to the items listed under "Body edits" below, each of which is markup.

## Common style (all three documents)

- Engine: LuaLaTeX (TeX Live 2026, `jacobian-conjecture-2d` env), 3 passes.
- Fonts (Brandon's rule): Noto Sans text (real Regular/Bold/Italic/BoldItalic) with a per-glyph Fira Sans fallback chain (luaotfload); Noto Sans Mono for code; Noto Sans Math v3.000 (bundled in `fonts/`, has the OpenType MATH table; sha256 `9dda7e17…97ca28`) with a Fira Math range fallback. `\tracinglostchars` on; 0 missing characters.
- Palette: the exact light-mode palette of the topology report (`trueaccent` #1A73E8, `truetext` #174EA6, `opentext` #B05B00, `falsetext` #A50E0E, neutral greys). Blue / orange / red are the report's proved / open / refuted colours; the blue–orange pair is colour-blind-safe, red is only used together with a text label.
- Headings: section numbers in accent blue, hairline rule under section titles (titlesec); part pages with accent rule (combined paper).
- Running header/footer (fancyhdr): short title left, author right, edition line and page number in the footer, hairline rules.
- Captions: small, bold blue label, grey text, ragged right.
- Title block: accent double rule, centred title, date in grey; abstract in a light panel with a blue left rule.
- Theorem-like environments: heading in dark blue bold; remarks in grey italic heading.
- Tables: booktabs rules in light grey, light grey header row shading, slightly opened row spacing.
- Links (hyperref `colorlinks`): cross-references and URLs in accent blue, citations in a second blue. Every bibliography entry that already stated an arXiv identifier, a DOI or a zbMATH/JFM review number now carries a working `\href`. No identifier was invented. Link texts use `\nolinkurl` so long identifiers break at punctuation without a false hyphen.
- Status highlighting, used sparingly and only where the text already states the status: small tinted tags (`\stproved`, `\stopen`, `\strefuted`, `\stneutral`).

## Figures: why the earlier editions looked black and white

The figure files were already in colour (measured: every figure has saturated pixels; the Jacobian status map ~43 % coloured, the IRH phase-band ~11 %). Nothing in the figures was greyscale, and no figure needed regenerating. The monochrome look came from the typography around them: black headings, black captions, links set to `hidelinks` in the IRH draft (no visible link colour at all) and to a dark navy `blue!60!black` in the combined paper, and no colour anywhere in tables or labels. That is what this pass changes.

## IRH v95 draft (`programme/v95/IRH_v95_draft.tex`)

- Pages: 50 (was 51; text metrics under LuaLaTeX). 3 passes: 0 errors, 0 undefined, 0 missing characters (`\tracinglostchars=3`, hard error), 0 overfull boxes.
- Links in the PDF: 339 internal, 52 external annotations (42 distinct). Before: 339 internal, 1 external (the ORCID), because the draft used `hidelinks` and its bibliography had no `\href`.
- Header: "Intrinsic Resonance Holography, v95" / "B. D. McCrary"; footer "Draft of November 25, 2026".
- Body edits (markup only): title page restyled (accent rules, coloured subtitle, the edition note in a light panel instead of a minipage); epistemic labels (`\lbl`) keep their small capitals and are now coloured by kind — Derivation and Prediction blue, Exclusion red, Open orange, Input and Calibration slate; Table "Claims withdrawn from version 92": status cells tagged (retracted red, corrected / downgraded neutral); bibliography: 41 identifiers linked.
- Bibliography entries left unlinked (books and older papers whose entries state no DOI or arXiv id; none invented): ref3, ref6, ref10, ref21, ref24, ref25, ref30, ref31, ref32, ref47.
- Checks: `validation/check_tex_claims.py` on the restyled source PASS 54 FAIL 0 (log `validation/check_tex_claims_style.log`); AI-tell heuristics unchanged in every count (`validation/ai_tell_style.log`); every DOI confirmed registered via the doi.org handle API.
- The older PNG figures (fig02, fig03, fig05–fig09) are unchanged and already in colour; redrawing them as vector figures is still open, as before.
