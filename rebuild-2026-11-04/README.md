# LEG 2 — IRH TEX REBUILD + RECOMPILE (2026-11-04, completed 2026-11-05 ~05:30 CST)

## CLAIM
Rebuilt-from-PDF (NOT the author's source). No .tex for IRH v93.1 exists in the
workspace or on Google Drive (both connected; Drive searches for IRH / .tex
returned only PDFs, verification zips, and an audit doc).

## STATUS: PASSED (compile) with corrections + flags — see report
- Source text: ~/workspace/user/files/IRH_v93_1_1_44kz.pdf (31 pp.)
  and ~/workspace/research/truth-seeking-v5/irh-test/irh_v93_1.txt (1472 lines).
- Rebuilt tex: IRH_v93_1_rebuilt.tex (930 lines).
- Output PDF: IRH_v93_1_rebuilt.pdf — XeLaTeX rc=0, 0 errors, 0 undefined
  references, 0 missing characters, 32 pages, A4, 191,831 bytes.
- Fonts embedded (pdffonts): Fira Sans, Fira Math, Fira Mono, Noto Sans Math
  (setminus fallback), Noto Sans (subscript-a fallback). No FakeBold (grep 0).
- SymPy 1.14.0: sympy_verify.log 59 PASS + 1 intentional FAIL-flag
  (11.85%/11.90% source inconsistency); sympy_supplement.log 7 PASS.
- Second tools: second_tool_verify.log 20 PASS (flint 0.8.0 + enumeration);
  singular_verify.log PASS (Singular 4.4.1, moment diffs 0, det E6 = 3).
- Corrections applied: $\tau_{D}4/\tau_{BCC}$ = sqrt(2) NOT 2 (throughout);
  $r_{c} = 2u^{2} \tau^{2}/(9 v q4) ($ledger garble fixed); 15->21 dimension wording
  clarified; 11.85/11.90 inconsistency flagged, not resolved.
- Figures: NOT recovered — captioned placeholders only.
- No git commit made (per brief; repo work is a later leg).
- No Lean build run in this leg; Lean claim carried as stated.
