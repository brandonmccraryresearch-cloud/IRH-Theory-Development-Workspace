# Diff summary: IRH v93.1 → v94 (draft, 2026-11-14)

Worker D, Phase 1. Draft only — nothing compiled, committed, or pushed.

**Baseline:** `source-2026-11-05/rebuild-no-note/IRH_v93_1_source_rebuilt_no_note.tex`,
1,122 lines, md5 `999b9fc8aae6295763da6090b17ce1b9` (verified unchanged after this work).

**Draft:** `programme/v94/IRH_v94.tex`, 1,214 lines (+92), md5
`25adc894503e31fafb01cb6ba1aa8376`.

**Evidence base:** `programme/ADVANCES_since_v93.1_2026-11-14.md` (26-row ledger).
Every edit below cites its ledger row. Ledger rows 22–26 (Jacobian/GGHV
programme) are **not** IRH advances and appear nowhere in the draft.

**Grading contract (HLRE v5.1 as amended 2026-11-12):** every grade change in
v94 is marked **PROPOSED**. No auditor changed a grade. All grade changes are
Brandon's call. All other claims keep exactly the standing v93.1 states.

**Method:** the canonical tex was copied, never edited in place; 19
exact-anchor replacements were applied to the copy only (script
`/tmp/v94_edits.py`, all anchors asserted unique before writing). No compile
was attempted (build phase comes later).

## Summary table

| # | Location (v94 lines) | Change | Ledger row | PROPOSED grade? |
|---|---|---|---|---|
| 1 | Title, line 50; date, line 58 | Version 93.1 → 94; September 17, 2026 → November 14, 2026 | — (mechanical) | No |
| 2 | Abstract, line 73 | One sentence flagging v94 + PROPOSED discipline | — (mechanical) | No |
| 3 | New § VERSION NOTE, lines 78–103 | Changelog + HLRE gap-ID definitions | 1–21 | Yes (see rows) |
| 4 | How to Read, line 106 | Pointer to version note + §VIII.4 | — (mechanical) | No |
| 5 | §II.5, line 280 | Matched-branches re-audit note; peak arithmetic | 4, 15 | Yes |
| 6 | §II.6, line 319 | G-A5 narrowed statement; F-LOCAL-1 caveat | 2, 6, 13 | Yes |
| 7 | §II.8, line 408 | G-A6 sampled stability; relaxed dispersion | 3, 10, 14 | Yes |
| 8 | §II.9, line 436 | Noise-nucleation bound; critical seed | 5, 7 | Yes |
| 9 | §II.11, line 448 | G-D10 narrowing | 18 | Yes |
| 10 | §V.1 table, line 709 | Burgers-vector row corrected in place (flagged) | 1 | Yes (via §V.1a) |
| 11 | New §V.1a, lines 720–725 | Corrected phonon/dislocation values + GCP Job 3 | 1, 12, 21 | Yes |
| 12 | §VI.6, line 766 | Burgers vectors corrected in place (flagged) | 1 | Yes (via §V.1a) |
| 13 | New §VI-A.5, lines 806–812 | G-D6 MISS; grain-locking/spectral-threshold BLOCKED | 9, 17 | Yes |
| 14 | §IX.1, line 938 | Interface-tension note | 8 | Yes |
| 15 | §IX.3, line 958 | G-C21 (new); G-C19, G-C20, G-C18 | 16, 19, 20 | Yes |
| 16 | New §VIII.4, lines 893–931 | v94 status table (23 rows) | 1–21 | Yes |
| 17 | Appendix A, items 19–20, lines 1017–1018 | Correction record: dislocation lattice; $K=6$ reading | 1, 6 | No (record) |
| 18 | Part X, line 990 | v94 addendum paragraph | 1–21 | No (summary) |

## Section-by-section detail

### 1–2. Title, date, abstract (lines 50, 58, 73)

Title block now reads "Version 94"; date "November 14, 2026". The abstract's
final sentence now adds: "Version 94 (November 14, 2026) adds a front version
note recording external-verification results since v93.1; every grade change
in it is marked PROPOSED and awaits the author's decision." No other abstract
wording touched.

### 3. New VERSION NOTE section (lines 78–103) — placement choice

Placed at the **front**, immediately before "How to Read This Document",
rather than before Part VII: the note is the reader's first encounter with the
new HLRE gap-ID language, so it belongs up front, and Part VII keeps its
v92-only retraction scope. Contents: one paragraph stating the evidence base
(Co-Scientist programme, four GCP runs, Gemini sweeps 5–6; HLRE v5.1 as
amended 2026-11-12; "nothing else in the paper changes"); a gap-ID definition
paragraph (G-A5 §II.6; G-A6 §II.8; G-A11 §V.1; G-D6 §VI-A.5; G-C21 §IX.3, new
topic; G-D10 §II.11, new topic); a 13-bullet changelog, one bullet per ledger
item/group (rows 1–21); and a closing line excluding ledger rows 22–26. Every
grade in the section is marked PROPOSED.

### 4. How to Read pointer (line 106)

One sentence appended to the Part VII / Parts VIII–IX sentence: "A version
note at the front records what changed in v94, and §VIII.4 records the v94
status of each audited gap; grades marked PROPOSED in either place are
proposals, not decisions."

### 5. §II.5 matched-branches note (line 280; rows 4, 15)

New "v94 status note (G-A20)" paragraph after the closed-forms paragraph.
Byte-identical re-audit of Batch 2 `a20-onset` (scan-table sha256
`da415b0c…`); NOT a second delivery; $S_{D_4}/S_{A_4^*}=496/423$, margin
$73/423\approx17.26\%$; crossing at $r=-0.591438362$ VERIFIED WITH CORRECTION
(preempted by $A_3$/$A_2$); chat final-message numbers struck (six UNVERIFIED,
one REFUTED as phrased). **PROPOSED:** exact combinatorics + matched-pure-branch
part Track E B / Track F F1, unchanged from Batch 2; dynamical parts OPEN.
Peak arithmetic (row 15): **PROPOSED** Track F F1; synthetic-discriminant
reading B / F1; measurable-discriminant reading C; G-A12 and G-C8 stay OPEN.

### 6. §II.6 G-A5 note + F-LOCAL-1 caveat (line 319; rows 2, 6, 13)

New "v94 status note (G-A5)" paragraph after the independent-reproduction
paragraph. Patterned recovery verified: $12/12$ (native cells) + $12/12$ (4D
field) + GCP $32/48$ $D_4$ full (every pattern family $8/8$ full). General
selection from noise NOT established: $0/6$ broadband random starts (Wilson
$95\%$ upper bound $\approx39\%$), $20/20$ uniform per star pooled (Wilson
$95\%$ upper bound $\approx16\%$), nucleation null expected at barrier/noise
$\approx34$. **PROPOSED:** patterned-recovery half Track E B / Track F F1
(native-cell route; F2 on the 4D-field route); general-selection half no grade,
stays OPEN. F-LOCAL-1: local cap $|\mathbf{k}|^2\leq64$ means the GCP "$K=6$"
study never widened the $A_4^*$ band ($A_4^*$ energies identical to $K=4$ to 15
figures; newly admitted band power 0; $D_4$ genuinely widens,
$\Delta E=-1.41\times10^{-6}$); trap robustness to a genuinely wider band
UNVERIFIED.

### 7. §II.8 G-A6 note (line 408; rows 3, 10, 14)

New "v94 status note (G-A6)" paragraph after the attractor paragraph. Three
routes agree, no positive rate anywhere sampled: 52 sector fibers, 259 $q$
(local), 14,641 $q$ GCP (exactly one $q$ with $\lambda_{\max}>0$, the $q=0$
Goldstone roundoff $8.67\times10^{-12}$); least-damped nonzero rate
$-2.13324\times10^{-5}$. Cautions recorded: the 52 rates are sector-fiber
maxima, not full-fiber maxima; the $\Gamma$ first-finite-rate gap of
$3.05\times10^{-4}$ is attributed to sector coverage but UNPROVEN.
**PROPOSED:** sampled stability grade C; continuum Bloch stability ABSTAIN.
Relaxed dispersion (row 14): **PROPOSED** measured Track E B (slopes agree to
$\sim0.5\%$ at $|\mathbf{q}|=0.02$; $L/T=3.016$ against $3$;
$\lambda_{\mathrm{relaxed}},\mu_{\mathrm{relaxed}}$ extraction still open).

### 8. §II.9 nucleation note (line 436; rows 5, 7)

New "v94 status note (nucleation)" paragraph after the Consequence paragraph.
Negative result: saddle $550.93057$ at $h=0.5$; thresholds $16.19140625$ /
$16.2109375$; AMS $0/160$, max score $0.49474158627843945$; per-configuration
$95\%$ gate-entry bound $8.94\%$ (Clopper–Pearson upper bound for $0/32$,
$8.9368\%$); partial bundle ($128/192$ runs tabulated, 32 log-only
`space_half`, 32 never run `leading_FDT`); null expected at barrier/noise
$\approx34$. Stated explicitly: NOT a selection rate. **PROPOSED:**
deterministic saddle/threshold B / F2; AMS + ensemble null C (scoped null);
any physical rate ABSTAIN. Critical seed (row 7): local bracket
$R_{c,\mathrm{field}}\in(2.5875,\ 2.625]$ at $\alpha=1$, $L=2\pi$ vs
Co-Scientist dissolution at $L=4\pi$ are disjoint regimes (no genuine
disagreement; finite-box-filling rival reading strengthened). **PROPOSED:**
$4\pi$ dissolution Track E B; G-A9 PARTIAL, stays OPEN; G-A10 stays OPEN.

### 9. §II.11 G-D10 note (line 448; row 18)

New "v94 status note (G-D10)" paragraph after the defensible-statement
paragraph. Broad "(2,2) corner" claim OVERTURNED: Kulkarni SSM scores
$(2, 2, 2)$, Lee torus model $(2, 1, 1)$. **PROPOSED:** broad claim OVERTURNED
at grade B; narrowed to spectral/Turing-only selection, OPEN at grade C
(PROPOSED); rival models' physics NOT validated (ABSTAIN).

### 10–12. §V.1 / §V.1a / §VI.6 — phonon and dislocation correction (rows 1, 12, 21)

- §V.1 table row (line 709): "Burgers vectors in D₄" changed in place to
  "Burgers vectors in $\pi D_4^*$ (corrected in v94; see §V.1a)". This is one of
  only two in-place alterations of v93.1 sentences, and it is flagged on the
  spot (see "Wording compromises").
- New §V.1a (lines 720–725): correction notice stating plainly that external
  verification (Co-Scientist + GCP) corrected the local side; Burgers lattice
  $\pi D_4^*$ not $\pi D_4$ (shortest vector $(\pi/2)(1,1,1,1)$,
  $|\mathbf{b}|=\pi$; one $W(F_4)$ orbit per $D_4^*$ shell with
  $\lVert\mathbf{b}\rVert^2\le6$); edge/screw factor $4/3$ not $2$ (local edge
  coefficient $3/2$ high); stiffness $\lambda=\mu=1.54058921014457$ agrees
  exactly. Corrected values with v93.1 values in parentheses: elementary edge
  $K$, $0.490385\to0.326923$; $E/A(R=20)$, $0.899\to0.666$; edge $R^*$ rescaled
  by $\sqrt{2/3}$ ($16.62\to13.57$, $12.79\to10.44$, $23.91\to19.52$,
  $19.19\to15.67$); screw unchanged; $|\mathbf{b}|^2=4$ bound state and $R=20$
  split verdicts survive. **PROPOSED:** corrected coefficients Track E B /
  Track F F2; local edge leg demoted pending correction C5 (script rerun).
  G-A11 narrows but stays OPEN. GCP Job 3 (row 12): Volterra defect heals
  ($E/A=0.0013609$, $\sim9{,}000\times$ below the elastic prediction of
  $\approx12.5$, $\sim6{,}100\times$ with the corrected edge coefficient);
  no $1/r^2$ field; $r_0=10.05/7.10$ against $R_{\max}=\pi\approx3.14$; $N=32$
  production NOT run; re-attempt needs a pinned defect and
  $R_{\max}\gg r_0\approx10$. Old values are never deleted silently: they are
  recorded here, in the changelog, and in Appendix A item 19.
- §VI.6 (line 766): "Burgers vectors in D₄" changed in place to
  "$\pi D_4^*$ (corrected in v94, §V.1a)". The second flagged in-place change.

### 13. New §VI-A.5 (lines 806–812; rows 9, 17)

Placed in Part VI-A (Independent Verification) after §VI-A.4. **G-D6 MISS:**
145-query Argon run + 80-query follow-up found zero independent works citing
or discussing IRH; both ResearchGate IRH records show Citations (0); full-text
checks (Chaudhary 88 pp., Kulkarni, Schmidt et al., Swann, Ali) find zero
"McCrary". Correction recorded: the follow-up run was Gemini 4 Hydrogen, not
Argon, so the two runs must not count as two independent verifications; G-D6.2
independence corrected $I2\to I1$. **PROPOSED:** G-D6.1 B (scoped); G-D6.2 B
(scoped) / ABSTAIN (universal); G-D6.3 F2. G-D6.1 as a positive claim stays
INCOMPLETE-EVIDENCE; universal negative ABSTAIN. **BLOCKED, not evidence:**
grain-locking and spectral-threshold comparisons BLOCKED (no files on disk;
reproducibility zips 215 MiB and 306 MiB); nothing about those deliveries is
stated.

### 14. §IX.1 interface-tension note (line 938; row 8)

One paragraph appended to §IX.1: tensions $0.0189904$ / $0.0264060$ at
coexistence; thin-wall transfers $36.95$ / $138.12$ against the saved saddle
$550.93$; the $14.9\times$ barrier mismatch is the same $\sim15\times$
mismatch local Task 3 already states; second transfer shows path dependence
($40\%$), so the disagreement is a regime difference. **PROPOSED:**
coexistence tensions Track E B / Track F F1; G-A18 stays CLOSED, strengthened;
G-D3 stays ABSTAIN.

### 15. §IX.3 sweep notes (line 958; rows 16, 19, 20)

One paragraph appended after the Lorentzian-signature paragraph. **G-C21**
(new topic — v93.1 contains no CDT content): $\sim2$ vs $\sim3/2$ tension is
bare-coupling / extrapolation-regime dependence; canonical point $(2.2, 0.6)$
gives $D_S(0)=1.97\pm0.27$. **PROPOSED:** continuum UV endpoint bounded to
the scoped interval $[3/2, 2]$ at grade B; sharp value ABSTAIN; no IRH grade
changes. Three sweep claims REFUTED as stated (Phase A $4/3$; branched-polymer
$4/3$; Carlip aside). **G-C19 PROPOSED RESOLVED at G8/F1** (Dirac varying-$G$
falsified on a verified primary-source $\dot{G}/G$ constraint). **G-C20
PROPOSED RESOLVED at B / F2** (Greensite one-loop mechanism, $D=4$
uniqueness). **G-C18 PROPOSED strengthened from scoped C to B** (no surveyed
rival derives $\alpha$; SSM
$\alpha^{-1}=\pi\sqrt{m_p/m_e}\approx134.61$ is a metadata-scraper artifact);
universal negative ABSTAIN.

### 16. New §VIII.4 v94 status table (lines 893–931; rows 1–21)

Placed after §VIII.3 (Inputs), before Part IX — the ledger area, keeping the
paper's own DERIVATION/PREDICTION/INPUT/EXCLUDED/OPEN vocabulary in §VIII.1–3
untouched. Intro paragraph states the PROPOSED discipline, excludes ledger
rows 22–26, and records that the §VIII.1 "Dynamical shell selection from
noise" PREDICTION row is narrowed by the G-A5 entry (label retained for the
patterned-recovery part only, PROPOSED). The table has 23 rows: G-A5, G-A6,
G-A11, G-A9, G-A10, G-A12, G-A18, G-A20, G-C8, G-C18, G-C19, G-C20, G-C21,
G-D3, G-D6, G-D10, F-LOCAL-1, phonon coefficients, noise nucleation, relaxed
dispersion, peak arithmetic, grain-locking / spectral-threshold, GCP Jobs 1–4
— each with its v94 position and ledger row(s).

### 17. Appendix A items 19–20 (lines 1017–1018; rows 1, 6)

Item 19: dislocation lattice and edge coefficient (local $\pi D_4$ and factor
$2$ were wrong; lattice is $\pi D_4^*$, factor $4/3$, edge coefficient $3/2$
high; stiffness already correct). Item 20: the "$K=6$" band-widening reading
(local $|\mathbf{k}|^2\leq64$ cap; GCP $K=6$ did not widen the $A_4^*$ band;
trap robustness to a genuinely wider band UNVERIFIED). Record entries, not
grade changes.

### 18. Part X addendum (line 990; rows 1–21)

One paragraph appended to Part X: external verification since v93.1 narrowed
rather than widened established ground (G-A5 OPEN; G-A6 continuum ABSTAIN;
G-A11 OPEN with corrected coefficients; G-D6 MISS; G-D10 overturned in broad
form and narrowed). Restates that every grade change is PROPOSED and awaits
the author's decision; nothing else in the assessment changes.

## What was NOT changed

- Every other claim keeps its v93.1 wording and standing, including the
  abstract's "What is now established / excluded / remains open" paragraphs,
  the §VIII.1–3 ledger vocabulary, Part VII retractions, and all figure/table
  content except the two flagged §V.1 / §VI.6 Burgers-vector phrases.
- Ledger rows 22–26 (Jacobian close-the-gaps / Puiseux) are excluded from the
  draft entirely, per brief.
- Ledger row 26 (record hygiene: stale "Grade cap C/F3 until human gates run"
  sections in five `COMPARISON_taskN.md` scaffolds; peak-ratios summary wording
  slips; critical-seed `SHA256SUMS.txt` path remap; stochastic-bundle gaps;
  outstanding C5 rerun and Bloch $\Gamma$ sector check) was not written into
  the manuscript — it is programme bookkeeping, not manuscript content — except
  that correction C5 is named as pending in §V.1a and the changelog.
- Grain-locking and spectral-threshold: no results exist to report; recorded
  only as BLOCKED (§VI-A.5, changelog, §VIII.4).
- The $11.85\%$ vs $11.90\%$ band inconsistency flagged in the tex map (§3) was
  **not** adjudicated and no edit touches it — which value is canonical remains
  Brandon's call.

## Wording compromises / judgment calls

1. **Two in-place sentence changes, both flagged.** The §V.1 table row and
   §VI.6 are the only places a v93.1 sentence was altered rather than
   supplemented, because leaving "Burgers vectors in D₄" standing would have
   left a false statement in the body. Both carry an explicit "(corrected in
   v94)" flag pointing at §V.1a, and the old values are preserved in §V.1a,
   the changelog, and Appendix A item 19. No other old value was overwritten.
2. **G-A5 grade phrasing.** The ledger gives the patterned-recovery half as
   Track E B / Track F F1 (native cells) with the 4D-field route at F2 in its
   per-row notes; the draft writes "Track E B / Track F F1 (native-cell route;
   F2 on the 4D-field route)" rather than picking one F-level.
3. **G-C19 "G8/F1" reproduced verbatim.** The ledger states G-C19 as
   RESOLVED at "G8/F1"; the draft carries that label exactly as written
   rather than interpreting it into the A–D / F1–F3 scheme. The G-C19/G-C20
   audits were read headline-only in the ledger; the draft marks both
   PROPOSED as stated.
4. **Homes for topics with no v93.1 prose.** G-C21 (no CDT content anywhere in
   v93.1) is placed in §IX.3 after the Lorentzian-signature paragraph, and
   G-D10 (no matching prose) in §II.11 after the defensible-statement
   paragraph — new-topic paragraphs, not edits to existing claims. F-LOCAL-1
   has no $K=6$ sentence to correct (none exists in v93.1), so it is attached
   as a caveat to the §II.6 G-A5 note, the changelog, Appendix A item 20, and
   §VIII.4.
5. **§VIII.1 row left standing.** The "Dynamical shell selection from noise"
   PREDICTION row was not edited (to keep the paper's own ledger vocabulary
   intact); its narrowing is recorded in §VIII.4, which states the label is
   retained for the patterned-recovery part only (PROPOSED).
6. **"Version 93.1" still appears** in the draft only as a historical
   reference (changelog, §V.1a parenthetical, §VI-A.2 build status, §VIII.4
   intro, §IX.3 note, Part X addendum). The title and date are Version 94 /
   November 14, 2026.

## Verification checks performed (no compile)

- Canonical v93.1 tex md5 unchanged: `999b9fc8aae6295763da6090b17ce1b9`.
- Draft: 1,214 lines (+92), md5 `25adc894503e31fafb01cb6ba1aa8376`.
- New math delimiters balance: unescaped dollar-sign count 1,404 (even); +294 vs
  baseline 1,110 (even). The 5 `\$` literals are the three dollar amounts
  ($\$9.13$, $\$102.44$, $\$0.03$) in two places.
- Brace balance: open/close diff is 7 in both baseline and draft — a
  pre-existing quirk, unchanged by these edits (66 opens / 66 closes added).
- No unescaped `%` outside pre-existing preamble comments.
- "PROPOSED" appears 36 times in the draft; every grade change carries it.
- No Jacobian/GGHV content added; no commit, push, or remote contact.

## Layout fix 2026-11-14 ~20:52 (Brandon: tables spill over the page)
- §V.1 defect table: `tabular}{lll}` → `tabularx}{\linewidth}{ll>{\raggedright\arraybackslash}X}` (result column now wraps; was 100.0 pt overfull).
- §VIII.4 status table: `xltabular}{llX}` → `{l>{\raggedright\arraybackslash}Xl}` (the long v94-position text was in a non-wrapping `l` column; was 269.1 pt overfull). Content of both tables unchanged.
- Rebuilt: latexmk -xelatex exit 0; overfull \hbox count 12 → 4 (remaining 4 are small paragraph overfulls: 3 bibliography DOI strings, 1 line at §VIII.3; pre-existing v93.1 formatting, not v94 content). PDF now 39 pages (was 38), md5 `3c4a89ee3efd25bb37de5ca469dbdbde`. Both tables visually verified on pages 24 and 31.
