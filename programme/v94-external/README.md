# LEG — IRH v94 CLEAN EXTERNAL SUBMISSION BUILD (2026-11-15)

## CLAIM
Same v94 manuscript as the patched audit edition
(`programme/v94/IRH_v94.tex`, decided grades, 2026-11-14 patch), with the
internal operational vocabulary stripped from the BODY paragraphs only, per
the UM-5.2 voice rule (audit remediation, 2026-11-14). Nothing scientific
is stripped: every decided grade, every caveat, every scope bound, every
numerical value, and the phonon correction with old values preserved are
retained verbatim. The front Version Note is byte-identical to the audit
edition and still carries the operational vocabulary (ledger rows, Batch 2,
Co-Scientist, GCP, cost figures, UM-1) — that is the front record, not the
submission body.

## STATUS: PASSED (compile)
- Build script: `build_external.py` — reads the patched audit-edition tex
  via the `IRH_v94_source/` symlink, splits it into title/abstract +
  Version Note + body, applies 36 anchored replacements to the body
  (each asserted to occur exactly its expected number of times), drops
  the VIII.4 table's "ledger row" column (spec 3 columns -> 2; 21 rows
  stripped, 2 rows rewritten first), and asserts the body is free of the
  21 forbidden operational patterns and free of lone-backslash line ends.
  The Version Note (26 lines) is asserted byte-identical.
- Built tex: `IRH_v94_external.tex` (1,214 lines; the audit edition is
  also 1,214 lines; SHA-256
  192e4ae4f21765b4991e24b6e636c0f6f0ecbb7fa7d45935e2462cca720cb6a2).
- Output PDF: `IRH_v94_external.pdf` — XeTeX (TeX Live 2026),
  latexmk -xelatex exit 0, 0 errors, 0 undefined references, 38 pages
  (the audit edition is also 38 pages), 1,864,367 bytes, md5
  a39b69a64a34e7886ce9659431ce4385, SHA-256
  18c76073bc3d90a101920aa80b468f71b9994c4a852db36b93dd43488d8524c0.
- Overfull boxes: 4 — the same 4 as the audit edition (Section VIII.3
  line + 3 bibliography DOI strings), all pre-existing. No new overfull
  box was introduced by the cleaning.

## VERIFICATION (all checked 2026-11-15)
- .tex diff vs the patched audit edition: exactly 104 changed lines
  (52 removed, 52 added), all inside the intended regions — abstract
  (UM-1 -> independent audit), How to Read, the five v94 status notes
  (G-A20, G-A5, G-A6, nucleation, G-D10), V.1a, VI-A.5 (G-D6 + BLOCKED),
  the VIII.4 intro + table, the IX.1 note, the IX.3 note, the Part X
  addendum, Appendix A items 19-20. Zero other differences; the
  Version Note does not appear in the diff at all.
- Body text scan (pdftotext, pages 3-38 after the "How to Read"
  heading): 0 hits for all 21 forbidden patterns (Co-Scientist,
  Academia, GCP, Batch 2, chat final, ADVANCES, Gemini, Argon, Hydrogen,
  Manus, "ledger row", "correction C5", UM-1, sha256, $9.13, $102.44,
  space_half, leading_FDT, "reproducibility zips", "script rerun",
  "chats"). The Version Note pages still carry the vocabulary
  (Co-Scientist, GCP, "ledger row", UM-1 present on pp. 1-2), as
  designed.
- Decided grades and qualifications present in the body text:
  "decided" 30x, OVERTURNED 3x, B / F2 5x, 8.94% 2x,
  INCOMPLETE-EVIDENCE 3x, ABSTAIN 14x, F-LOCAL-1 3x, G8/F1 2x,
  4/3 9x, 0.326923 1x, "Compute runs 1-4" 1x, and the neutral
  rewordings ("independent sweep", "independent literature sweeps",
  "independent dissolution measurement") each 1x.
- Tables visually verified: Section V.1 (p. 24, defect table + V.1a
  correction text) and Section VIII.4 (p. 31, the 2-column table with all
  23 rows) both fit within the margins; the VIII.1 table (pp. 29-30) is
  unchanged from the audit edition.
- The audit edition `IRH_v94.pdf` at the repo root was NOT overwritten:
  it is still the patched audit edition (md5
  291875a4bd0bbbbb50cee6cefe8b24f7, 38 pages). The external PDF lives
  only in this tree.

## BUILD DEFECT FOUND AND FIXED
The first build failed with 22 "Extra alignment tab" errors at the
VIII.4 table. Cause: the table-row regex substitution in
`build_external.py` emitted one backslash instead of two — in `re.sub`,
a 2-backslash replacement string yields one literal backslash, so each
row lost its `\\` terminator and the next row's `&` was read as a second
alignment tab. Fixed by writing the replacement literal with four
backslashes (which `re.sub` turns into two), plus a new guard assertion
in the script: no output line may end with a lone single backslash.
The two rows rewritten by plain `str.replace` (phonon coefficients,
compute runs) were unaffected — the prefix match left their second
backslash in place, verified by count. The rebuilt tex passes the guard
and builds clean. The two minimal-test rounds that first isolated the
defect are recorded in the task report, not in this tree.

## WHAT WAS STRIPPED, SECTION BY SECTION
- Abstract + How to Read + VIII.4 intro + Part X addendum: "the UM-1
  audit" -> "an independent audit" (4x in the body; the Version Note
  keeps "UM-1 audit").
- G-A20 note (Section II.5): "ledger rows 4, 15" dropped from the
  heading; "Batch 2 a20-onset record (scan-table sha256 da415b0c...)"
  -> "the earlier a20-onset record"; "The chat final-message numbers
  are struck" -> "An earlier summary's counts are struck"; "unchanged
  from Batch 2" -> "unchanged from the earlier record"; "(row 15)"
  dropped.
- G-A5 note (Section II.6): heading ledger rows dropped; "the GCP
  sweep agreeing" -> "an independent sweep agreeing"; "the GCP
  ``$K=6$'' study" -> "the ``$K=6$'' study".
- G-A6 note (Section II.8): heading ledger rows dropped; "52 sector
  fibers (Co-Scientist)" -> "52 sector fibers (external
  verification)"; "a dense GCP map of 14,641 $q$" -> "a dense
  independent map of 14,641 $q$"; "Relaxed dispersion (row 14) ... GCP
  long-wave slopes agree" -> "Relaxed dispersion ... independent
  long-wave slopes agree".
- Nucleation note (Section II.9): heading ledger rows dropped; the
  run identifiers `space_half` / `leading_FDT` dropped from the
  partial-bundle sentence (128/192, 32 log-only, 32 never run kept);
  "the Co-Scientist dissolution at $L=4\pi$" -> "the independent
  dissolution measurement at $L=4\pi$"; "(row 7)" dropped.
- G-D10 note (Section II.11): heading ledger row dropped.
- V.1a heading: ledger rows dropped. "External verification (Academia
  Co-Scientist, corroborated by GCP)" -> "External verification,
  corroborated by independent computation". "pending correction C5
  (script rerun)" -> "pending a rerun of the local dislocation
  calculation with the equilibrium edge field". "a GCP Volterra-defect
  prototype ($0.03$)" -> "a Volterra-defect prototype run".
- VI-A.5 heading: ledger rows dropped. "Two Gemini sweeps (a 145-query
  Argon run and an 80-query follow-up)" -> "Two independent literature
  sweeps (145 queries and an 80-query follow-up)". "the follow-up run
  was produced by Gemini 4 Hydrogen, not Argon, so the two runs must
  not be counted as two independent verifications (same session, same
  prompts, same pipeline family)" -> "the follow-up used the same
  pipeline family as the first run, so the two runs must not be counted
  as two independent verifications" (the independence reasoning is
  load-bearing and is preserved). "the audit's full-text check" -> "a
  full-text check". "no Co-Scientist files ... (reproducibility zips
  215 MiB and 306 MiB; the chats' files have not arrived). Nothing
  about those deliveries is stated here" -> "no external files ...
  (reproducibility archives of 215 MiB and 306 MiB have not arrived).
  Nothing about those comparisons is stated here".
- VIII.4 intro: the sentence citing
  `ADVANCES_since_v93.1_2026-11-14.md` and rows 22-26 (Jacobian
  programme) is removed. Table: "ledger row" column dropped (3 -> 2
  columns); "GCP Jobs 1-4 & Measurements only, $9.13 of $102.44 cap;
  Job 3 prototype only" -> "Compute runs 1-4 & Measurements only;
  dislocation run was a prototype only"; the phonon row's "pending C5"
  -> "pending a rerun with the equilibrium edge field".
- IX.1 note: "(ledger row 8)" dropped; "local Task 3 already states"
  -> "the local calculation already states".
- IX.3 note: heading ledger rows dropped.
- Appendix A items 19-20: "(ledger row 1)" / "(ledger row 6,
  F-LOCAL-1)" dropped (F-LOCAL-1 kept); "the GCP $K=6$ study" ->
  "the $K=6$ study".

## CONSEQUENCES TO NOTE
- The external edition carries the amended sentence "The $|b|^2=4$ bound state
  survives. The $R=20$ split verdicts are mixed: the $|b|^2=10$ edge split
  flips No to Yes…" (Section V.1a), exactly as the amended audit edition
  states it. The amendment was decided 2026-11-17 (Brandon: all decisions
  authorized) after an independent second-route C5 rerun confirmed the flip
  (agreement $<10^{-9}$, margin $+0.79\%$); the earlier "pending his call"
  note is superseded.
- The standing manuscript vocabulary "complete claim ledger" (Part VIII
  section title and the How-to-Read sentence) is deliberately KEPT: it
  is the paper's own structure name, present since v93.1, not a
  programme pointer. Only "ledger row" pointers were stripped.
- An external reader who reads the front Version Note will still see
  the operational vocabulary there (ledger rows, Batch 2, Co-Scientist,
  GCP, cost figures, UM-1). The cleaning is body-only, per the audit's
  remediation ("such vocabulary may remain confined to the front
  Version Note"). A submission that needs the front note cleaned too is
  a separate decision.

## FILES
- `build_external.py`, `IRH_v94_external.tex`,
  `IRH_v94_external.pdf`, `IRH_v94_external.log`, this README.
  Symlinks: `IRH_v94_source/` -> `../v94` (the patched audit-edition
  tree, read as input) and `figs/` -> `../v94/figs`. Build
  intermediates (.aux/.log/.fls/.fdb_latexmk/.out/.xdv) are gitignored.

## GRADE DISCIPLINE
No grade changes. No manuscript sentence altered except the voice
cleaning listed above. No qualification removed. No repo commit made.
