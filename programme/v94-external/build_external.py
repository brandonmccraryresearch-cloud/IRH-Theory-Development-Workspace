#!/usr/bin/env python3
"""Build the clean external-submission edition of IRH v94 from the PATCHED
(decided-grades) audit edition.

UM-5.2 voice rule (audit remediation, 2026-11-14): the audit edition
(`programme/v94/IRH_v94.tex`, the full programme audit edition) keeps its
internal operational vocabulary in the front Version Note; the body of the
external edition strips it. Nothing scientific is stripped: every decided
grade, every caveat, every scope bound, every numerical value, and the
phonon correction with old values preserved are retained verbatim.

Input:
  IRH_v94_source/IRH_v94.tex  (patched audit edition, symlink to ../v94)
Output:
  IRH_v94_external.tex  (in this dir next to this script)

What is stripped, body only (the front Version Note is byte-identical):
  * "ledger row" pointers (v94 status-note headings, the VIII.4 table's
    third column and its intro sentence, Appendix A parentheticals).
  * Programme/audit vocabulary: "Batch 2", "chat final-message numbers",
    "Co-Scientist", "Academia", "GCP" (and "GCP Job"), "Gemini"/"Argon"/
    "Hydrogen" (the literature-sweep tool names), "UM-1 audit", "correction
    C5 (script rerun)", "ADVANCES_since_v93.1_2026-11-14.md", the
    "$9.13 of $102.44 cap" and "$0.03" cost figures, the internal run
    identifiers space_half / leading_FDT, the scan-table sha256, and
    "local Task 3" (an internal task label).
  * Each is replaced by neutral wording that keeps the scientific content:
    e.g. "GCP sweep" -> "an independent sweep", "52 sector fibers
    (Co-Scientist)" -> "52 sector fibers (external verification)",
    "the follow-up run was produced by Gemini 4 Hydrogen, not Argon" ->
    "the follow-up used the same pipeline family as the first run"
    (the independence reasoning is load-bearing and is preserved).
  * The VIII.4 table drops its "ledger row" column (3 columns -> 2);
    the "GCP Jobs 1--4" row becomes "Compute runs 1--4".

What is deliberately NOT stripped:
  * The front Version Note (lines up to the "How to Read" heading) is
    copied byte-identically, including all ledger rows, Batch 2,
    Co-Scientist, GCP, cost figures, and UM-1.
  * The standing manuscript vocabulary "complete claim ledger" (Part VIII
    section title and the How-to-Read sentence) is kept: it is the paper's
    own structure name, present since v93.1, not a programme pointer.
  * Gap IDs (G-A5, G-D6, ...), grades, ABSTAINs, numerical bounds, and the
    phonon correction with old values preserved are untouched.
  * The partially inaccurate sentence "The |b|^2=4 bound state and the R=20
    split verdicts survive" (V.1a) is carried over AS-IS from the patched
    audit edition: the C5 rerun flipped the |b|^2=10 edge verdict at R=20,
    and that sentence is Brandon's decision (amend before commit, or record
    as a follow-up), not something for this voice-cleaning build to fix
    unilaterally.

Assertions (the script exits non-zero if any fails):
  * Every replacement below applies exactly the expected number of times
    in the body.
  * The VIII.4 table loses exactly 21 trailing ledger-row cells
    (23 rows total; the phonon and compute-runs rows are rewritten first).
  * After cleaning, the body contains zero occurrences of the forbidden
    patterns listed in FORBIDDEN_BODY.
  * The front (Version Note) is byte-identical to the source front.

No manuscript sentence is altered otherwise. No commit is made.
"""
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
SRC = HERE / "IRH_v94_source" / "IRH_v94.tex"
OUT = HERE / "IRH_v94_external.tex"
NOTE_MARKER = r"\section*{VERSION NOTE --- WHAT CHANGED IN v94}"
FRONT_MARKER = r"\subsection*{How to Read This Document}"

# (old, new, expected count in body)
REPLACEMENTS = [
    (r"on the concurrence of the UM-1 audit delivered that evening",
     r"on the concurrence of an independent audit delivered that evening", 3),
    (r"\textbf{v94 status note (G-A20; ledger rows 4, 15).}",
     r"\textbf{v94 status note (G-A20).}", 1),
    (r"The matched-branches audit is a byte-identical re-audit of the Batch 2 "
     r"\texttt{a20-onset} record (scan-table sha256 \texttt{da415b0c\ldots}), "
     r"not a second delivery: it adds no new evidence beyond a fresh "
     r"re-derivation and rerun.",
     r"The matched-branches audit is a byte-identical re-audit of the earlier "
     r"\texttt{a20-onset} record, not a second delivery: it adds no new "
     r"evidence beyond a fresh re-derivation and rerun.", 1),
    (r"The chat final-message numbers are struck (six UNVERIFIED and one "
     r"REFUTED as phrased).",
     r"An earlier summary's counts are struck (six UNVERIFIED and one "
     r"REFUTED as phrased).", 1),
    (r"Decided: exact combinatorics and matched-pure-branch part, Track E B / "
     r"Track F F1, unchanged from Batch 2; the dynamical parts stay OPEN.",
     r"Decided: exact combinatorics and matched-pure-branch part, Track E B / "
     r"Track F F1, unchanged from the earlier record; the dynamical parts "
     r"stay OPEN.", 1),
    (r"Peak arithmetic (row 15) is at Track F F1 (decided)",
     r"Peak arithmetic is at Track F F1 (decided)", 1),
    (r"\textbf{v94 status note (G-A5; ledger rows 2, 6, 13).}",
     r"\textbf{v94 status note (G-A5).}", 1),
    (r"with the GCP sweep agreeing (32/48 $D_4$ full; every pattern family "
     r"8/8 full)",
     r"with an independent sweep agreeing (32/48 $D_4$ full; every pattern "
     r"family 8/8 full)", 1),
    (r"so the GCP ``$K=6$'' study never widened the $A_4^*$ band",
     r"so the ``$K=6$'' study never widened the $A_4^*$ band", 1),
    (r"\textbf{v94 status note (G-A6; ledger rows 3, 10, 14).}",
     r"\textbf{v94 status note (G-A6).}", 1),
    (r"52 sector fibers (Co-Scientist)",
     r"52 sector fibers (external verification)", 1),
    (r"and a dense GCP map of 14,641 $q$",
     r"and a dense independent map of 14,641 $q$", 1),
    (r"Relaxed dispersion (row 14) is at measured Track E B (decided): GCP "
     r"long-wave slopes agree with the frozen-stiffness expectation to "
     r"$\sim0.5\%$ at $|\mathbf{q}|=0.02$, with $L/T=3.016$ against $3$; "
     r"extraction of $\lambda_{\mathrm{relaxed}},\mu_{\mathrm{relaxed}}$ "
     r"is still open.",
     r"Relaxed dispersion is at measured Track E B (decided): independent "
     r"long-wave slopes agree with the frozen-stiffness expectation to "
     r"$\sim0.5\%$ at $|\mathbf{q}|=0.02$, with $L/T=3.016$ against $3$; "
     r"extraction of $\lambda_{\mathrm{relaxed}},\mu_{\mathrm{relaxed}}$ "
     r"is still open.", 1),
    (r"\textbf{v94 status note (nucleation; ledger rows 5, 7).}",
     r"\textbf{v94 status note (nucleation).}", 1),
    (r"The bundle is partial: 128/192 runs tabulated, 32 log-only "
     r"(\texttt{space\_half}), 32 never run (\texttt{leading\_FDT}).",
     r"The bundle is partial: 128/192 runs tabulated, 32 log-only, 32 "
     r"never run.", 1),
    (r"and the Co-Scientist dissolution at $L=4\pi$ occupy disjoint regimes",
     r"and the independent dissolution measurement at $L=4\pi$ occupy "
     r"disjoint regimes", 1),
    (r"Critical seed (row 7):",
     r"Critical seed:", 1),
    (r"\textbf{v94 status note (G-D10; ledger row 18).}",
     r"\textbf{v94 status note (G-D10).}", 1),
    (r"\subsection*{V.1a Phonon stiffness and dislocation coefficients "
     r"(corrected in v94; ledger rows 1, 12, 21)}",
     r"\subsection*{V.1a Phonon stiffness and dislocation coefficients "
     r"(corrected in v94)}", 1),
    (r"External verification (Academia Co-Scientist, corroborated by GCP) "
     r"corrected the local side on two points.",
     r"External verification, corroborated by independent computation, "
     r"corrected the local side on two points.", 1),
    (r"the local edge leg stays at INCOMPLETE-EVIDENCE pending correction "
     r"C5 (script rerun).",
     r"the local edge leg stays at INCOMPLETE-EVIDENCE pending a rerun of "
     r"the local dislocation calculation with the equilibrium edge field.",
     1),
    (r"a GCP Volterra-defect prototype ($\$0.03$) heals on relaxation",
     r"a Volterra-defect prototype run heals on relaxation", 1),
    (r"\subsection*{VI-A.5 External literature and blocked comparisons "
     r"(v94; ledger rows 9, 17)}",
     r"\subsection*{VI-A.5 External literature and blocked comparisons "
     r"(v94)}", 1),
    (r"Two Gemini sweeps (a 145-query Argon run and an 80-query follow-up) "
     r"found zero independent works citing or discussing IRH.",
     r"Two independent literature sweeps (145 queries and an 80-query "
     r"follow-up) found zero independent works citing or discussing IRH.",
     1),
    (r"the follow-up run was produced by Gemini 4 Hydrogen, not Argon, so "
     r"the two runs must not be counted as two independent verifications "
     r"(same session, same prompts, same pipeline family).",
     r"the follow-up used the same pipeline family as the first run, so "
     r"the two runs must not be counted as two independent verifications.",
     1),
    (r"G-D6.3 F2 (the Chaudhary pp.\ 65--88 gap is closed by the audit's "
     r"full-text check).",
     r"G-D6.3 F2 (the Chaudhary pp.\ 65--88 gap is closed by a full-text "
     r"check).", 1),
    (r"The grain-locking and spectral-threshold comparisons are BLOCKED: no "
     r"Co-Scientist files for either task are on disk (reproducibility "
     r"zips 215 MiB and 306 MiB; the chats' files have not arrived). "
     r"Nothing about those deliveries is stated here.",
     r"The grain-locking and spectral-threshold comparisons are BLOCKED: no "
     r"external files for either task are on disk (reproducibility "
     r"archives of 215 MiB and 306 MiB have not arrived). Nothing about "
     r"those comparisons is stated here.", 1),
    (r" Ledger rows are from \texttt{ADVANCES\_since\_v93.1\_2026-11-14.md}; "
     r"rows 22--26 (Jacobian programme) are not IRH advances and are "
     r"excluded from this table.",
     r"", 1),
    (r"\textbf{v94 note (ledger row 8).}",
     r"\textbf{v94 note.}", 1),
    (r"The $14.9\times$ barrier mismatch is the same $\sim15\times$ "
     r"mismatch local Task 3 already states",
     r"The $14.9\times$ barrier mismatch is the same $\sim15\times$ "
     r"mismatch the local calculation already states", 1),
    (r"\textbf{v94 status note (ledger rows 16, 19, 20).}",
     r"\textbf{v94 status note.}", 1),
    (r"\item \textbf{Dislocation lattice and edge coefficient (v94; ledger "
     r"row 1).}",
     r"\item \textbf{Dislocation lattice and edge coefficient (v94).}", 1),
    (r"\item \textbf{The ``$K=6$'' band-widening reading (v94; ledger row 6, "
     r"F-LOCAL-1).}",
     r"\item \textbf{The ``$K=6$'' band-widening reading (v94; F-LOCAL-1).}",
     1),
    (r"so the GCP $K=6$ study did not widen the $A_4^*$ band",
     r"so the $K=6$ study did not widen the $A_4^*$ band", 1),
    # VIII.4 table rows rewritten before the column drop:
    (r"Phonon coefficients & Corrected values B / F2 (decided); local edge "
     r"leg INCOMPLETE-EVIDENCE pending C5 & 1 \\",
     r"Phonon coefficients & Corrected values B / F2 (decided); local edge "
     r"leg INCOMPLETE-EVIDENCE pending a rerun with the equilibrium edge "
     r"field \\", 1),
    (r"GCP Jobs 1--4 & Measurements only, $\$9.13$ of $\$102.44$ cap; Job 3 "
     r"prototype only & 10--13 \\",
     r"Compute runs 1--4 & Measurements only; dislocation run was a "
     r"prototype only \\", 1),
]

# Patterns that must not survive in the body after cleaning.
FORBIDDEN_BODY = [
    "Co-Scientist", "Academia", "GCP", "Batch 2", "chat final",
    "ADVANCES", "Gemini", "Argon", "Hydrogen", "Manus",
    "ledger row", "Ledger row", "C5", "UM-1", "sha256",
    "$9.13", "$102.44", "$0.03", "space_half", "leading_FDT",
    "reproducibility zips", "chats' files", "script rerun",
    "Task 3", "Task 4",
]

TABLE_SPEC_OLD = (r"\begin{xltabular}{\linewidth}"
                  r"{l>{\raggedright\arraybackslash}Xl}")
TABLE_SPEC_NEW = (r"\begin{xltabular}{\linewidth}"
                  r"{l>{\raggedright\arraybackslash}X}")
TABLE_HEADER_OLD = r"gap & v94 position & ledger row \\"
TABLE_HEADER_NEW = r"gap & v94 position \\"
TABLE_ROW_RE = re.compile(r" & [0-9,\- ]+ \\\\$")


def main() -> int:
    text = SRC.read_text(encoding="utf-8")
    note_start = text.find(NOTE_MARKER)
    body_start = text.find(FRONT_MARKER)
    if note_start < 0 or body_start < 0 or note_start > body_start:
        print("FAIL: Version Note / body markers not found", file=sys.stderr)
        return 1
    # Three parts: the title block + abstract (cleanable), the Version Note
    # (byte-identical front record), and the body from "How to Read" on.
    pre, note, body = (text[:note_start], text[note_start:body_start],
                       text[body_start:])

    # The abstract is part of the paper proper, not the Version Note: its
    # one "UM-1 audit" mention is cleaned like the body.
    um1 = REPLACEMENTS[0]
    n = pre.count(um1[0])
    if n != 1:
        print(f"FAIL: UM-1 count in title/abstract {n} != 1", file=sys.stderr)
        return 1
    pre = pre.replace(um1[0], um1[1])

    # The front (Version Note) must stay byte-identical; clean the body only.
    for old, new, expected in REPLACEMENTS:
        n = body.count(old)
        if n != expected:
            print(f"FAIL: replacement count {n} != {expected} for: {old[:90]!r}",
                  file=sys.stderr)
            return 1
        body = body.replace(old, new)

    # VIII.4 table: drop the "ledger row" column.
    lines = body.split("\n")
    hdr = next(i for i, ln in enumerate(lines) if TABLE_HEADER_OLD in ln)
    # The table spec sits just above the header.
    if TABLE_SPEC_OLD not in lines[hdr - 2]:
        print("FAIL: VIII.4 table spec not where expected", file=sys.stderr)
        return 1
    lines[hdr - 2] = lines[hdr - 2].replace(TABLE_SPEC_OLD, TABLE_SPEC_NEW)
    lines[hdr] = lines[hdr].replace(TABLE_HEADER_OLD, TABLE_HEADER_NEW)
    end = next(i for i in range(hdr, len(lines))
               if r"\end{xltabular}" in lines[i])
    stripped = 0
    for i in range(hdr + 1, end):
        if TABLE_ROW_RE.search(lines[i]):
            lines[i] = TABLE_ROW_RE.sub(r" \\\\", lines[i])
            stripped += 1
    if stripped != 21:
        print(f"FAIL: stripped {stripped} table rows, expected 21",
              file=sys.stderr)
        return 1
    body = "\n".join(lines)

    # Post-assertions (title/abstract + body must be free of the
    # operational nouns; the Version Note is exempt by design).
    cleaned = pre + body
    for pat in FORBIDDEN_BODY:
        if pat in cleaned:
            bad = [ln for ln in cleaned.split("\n") if pat in ln]
            print(f"FAIL: forbidden pattern {pat!r} survives outside the "
                  f"Version Note:", file=sys.stderr)
            for ln in bad[:3]:
                print(f"  {ln[:160]}", file=sys.stderr)
            return 1
    # Guard: no line may end with a lone single backslash (a row
    # terminator is always two). The regex-sub replacement once
    # lost one to re.sub escape processing; this catches any
    # recurrence anywhere in the output, not just the VIII.4 table.
    _bs = chr(92)
    _bad = [ln for ln in (pre + note + body).split(chr(10))
            if ln.endswith(_bs) and not ln.endswith(_bs * 2)]
    if _bad:
        print("FAIL: line ends with a lone backslash:", file=sys.stderr)
        for ln in _bad[:3]:
            print(f"  {ln[:160]}", file=sys.stderr)
        return 1
    # The standing manuscript name "claim ledger" is intentionally kept.
    if body.count("claim ledger") != 1 or body.count("CLAIM LEDGER") != 1:
        print("FAIL: standing 'claim ledger' section name lost",
              file=sys.stderr)
        return 1
    # The front must still carry its vocabulary.
    if "UM-1" not in note or "ledger row" not in note:
        print("FAIL: front Version Note lost its vocabulary", file=sys.stderr)
        return 1
    if note != text[note_start:body_start]:
        print("FAIL: front Version Note was modified", file=sys.stderr)
        return 1

    OUT.write_text(pre + note + body, encoding="utf-8")
    print(f"OK: wrote {OUT}")
    print(f"  Version Note lines (unchanged): {note.count(chr(10))}")
    print(f"  body lines: {body.count(chr(10))}")
    print(f"  replacements applied: {len(REPLACEMENTS)}")
    print(f"  VIII.4 table rows stripped of ledger column: {stripped}")
    print(f"  'claim ledger' kept in body: "
          f"{body.count('claim ledger')}x lowercase, "
          f"{body.count('CLAIM LEDGER')}x title")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
