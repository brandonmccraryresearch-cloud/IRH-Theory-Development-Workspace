# LEG — IRH TEX SOURCE REBUILD WITHOUT FRONT-MATTER NOTE (2026-11-10)

## CLAIM
Same source rebuild as 2026-11-05, with the "Source rebuild --- read first"
front-matter note omitted, per Brandon 2026-11-10. Nothing else changed.

## STATUS: PASSED (compile)
- Build script: `build_no_note.py` — copy of the canonical 2026-11-05
  `../build_source_rebuild.py` (the top-level copy, with bold pinning and
  the U+2124 fix), with step 4 (front-matter insertion) skipped and an
  assertion that the note heading is absent from the output.
- Built tex: `IRH_v93_1_source_rebuilt_no_note.tex` (1,122 lines, 97,078
  bytes; Nov 5: 1,144 lines, 101,316 bytes).
- Output PDF: `IRH_v93_1_source_rebuilt_no_note.pdf` — XeTeX
  3.141592653-2.6-0.999998 (TeX Live 2026), pass 1 rc=0, pass 2 rc=0,
  0 errors, 0 undefined references, 0 missing characters, 0 FakeBold,
  33 pages (Nov 5: 34), A4, 1,836,490 bytes,
  SHA-256 d363bb3e2dc3d4a6ea7ad5d619fdb3c0243dbe2449ccd864b5412c183edf6f83.
- Note: the first compile run was interrupted by a runtime restart after
  pass 1 (rc=0); pass 2 was re-run alone and completed rc=0. No state was
  lost; the PDF is the two-pass output.

## VERIFICATION (all checked 2026-11-10)
- .tex diff vs Nov 5 `IRH_v93_1_source_rebuilt.tex`: exactly 22 deleted
  lines (the note block, lines 75–96), zero other differences.
- Extracted-text diff vs Nov 5 PDF: only the note block deleted, plus
  page-number lines shifting by one page (33 vs 34 pages). Zero new text.
- Note absent from the new PDF text (0 hits for "Source rebuild --- read
  first" and "read first"). Hyperref literal "hyperref[ref-40]" absent (0).
- 11.85% present (4x), 11.90% present (1x) — source values intact.
- 26 "Expansion (source rebuild)" passages present. Hyperref fixes present
  (2x hyperref[ref40], 0 dashed ref- labels). Bold pins present.
- Fonts embedded (pdffonts, all emb=yes): FiraSans-Bold, FiraSans-Regular,
  FiraSans-Italic, FiraMono-Regular, FiraMath-Regular. The three fonts in
  the Nov 5 PDF that are absent here (NotoSansMath-Regular, NotoSans-Regular,
  FiraMono-Bold) were used only by the removed note: the body never uses
  \setminus (only a preamble comment mentions it), never uses the literal
  subscript-a glyph, and never uses mono bold.

## CONSEQUENCE TO NOTE
The removed note was also where the 11.85% vs 11.90% band inconsistency
was flagged. This clean PDF no longer calls it out up front. The
inconsistency is still in the manuscript text (both values present); it is
just unflagged now. Which value is canonical remains Brandon's call.

## FILES (Nov 5 artifacts untouched)
- `build_no_note.py`, `IRH_v93_1_source_rebuilt_no_note.tex`,
  `IRH_v93_1_source_rebuilt_no_note.pdf`, `xelatex_pass1.log`,
  `xelatex_pass2.log`, this README. Symlinks: `IRH_v93_1_source/` and
  `figs/` point at `../IRH_v93_1_source/` (pristine source package).

## GRADE DISCIPLINE
No grade changes. No manuscript sentence altered. No repo commit made.
