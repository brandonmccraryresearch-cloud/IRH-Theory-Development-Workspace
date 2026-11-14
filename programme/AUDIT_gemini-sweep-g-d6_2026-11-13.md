# Local audit of Gemini Sweep 6 (G-D6): Independent Work Citing or Discussing IRH

**Sweep audited:** G-D6, Task mode on gemini.google.com, Argon account (autopoieticdragon@gmail.com), task https://gemini.google.com/u/1/app/87cd6e25f4c0dccd. Browser task 2ee86a34, ran 2026-11-13 04:37–08:23 CST (3h 45m).
**Record audited:** `gemini-sweep-g-d6-2026-11-13.md` (verbatim record of both reports).
**Audit date:** 2026-11-13. **Auditor:** local audit (Dragon), under truth-seeking-frontier v5 and HLRE v5.1 as amended 2026-11-12.
**Method:** claim-by-claim check of both reports against their cited sources, with independent re-checks where cheap (ResearchGate pages, Zenodo record + full PDF text, IJSREM DOI page, MDPI full text, Preprints.org PDF, Swann PDF, Springer full text, arXiv/PubMed, Google's Gemini model documentation). No contact with anyone, no GCP spend, no Lean builds. All mathematics in this file is in `$...$` / `$$...$$` delimiters.

## Overall verdict

**The headline verdict stands: MISS (Strengthened Scoped Absence) — zero independent works citing or discussing IRH were found.** Both runs agree, and this audit independently re-verified the absence in every full text it could fetch: the two ResearchGate IRH records show zero resolved citations, and the full texts of Chaudhary (88 pp.), Kulkarni (Symmetry 18(11), 1813), Schmidt et al., Swann, and Ali contain zero mentions of McCrary.

**But the final report is not an Argon sweep.** Its follow-up run was produced by **Gemini 4 Hydrogen** — a different, speed-tier Gemini 4 model launched Nov 12, 2026 — not Argon. The sweep was commissioned as Gemini 4 (Argon); the initial run was Argon and reached the same verdict on a larger corpus (145 queries vs 80 distinct / 88 executed), so the sweep as a whole still satisfies the authorization through the initial run. The final report must be cited as a Hydrogen run, and the two runs must not be counted as two independent verifications (same session, same prompts, same pipeline family $\to$ I1).

**Audited grades:** G-D6.1 (final) B — CONFIRMED. G-D6.2 B (scoped bound) / ABSTAIN (universal negative) — CONFIRMED, re-anchored on the Argon run; the initial report's I2 is CORRECTED to I1. G-D6.3 F2 — CONFIRMED and STRENGTHENED: this audit closes Gemini's Chaudhary pp. 65–88 gap by a full-text check of the 88-page v2.4. G-D6.4 B — VERIFIED WITH CORRECTION (Hoy leg verified; Elitzur and de Laat legs UNVERIFIED in this session, not refuted). G-D6.1 (initial) INCOMPLETE-EVIDENCE — CONFIRMED. G-D6.3 (initial, universal negative) ABSTAIN / INCOMPLETE-EVIDENCE — CONFIRMED.

## 1. Model label: Argon vs Hydrogen (MATERIAL)

**Finding: the follow-up run was produced by Gemini 4 Hydrogen, not Argon.**

- The handoff notes the follow-up run "shows the model picker as 'Hydrogen'". This audit confirms from Google's own documentation (support.google.com/gemini/answer/18648722) that **Gemini 4 Hydrogen** is a real, distinct model: "A high-speed, capable model that balances performance and responsiveness across standard chat and task modes." It launched Nov 12, 2026 (Google DeepMind announcement; 9to5Google, Digital Trends, same date). The Gemini app picker assigns "Everyday help" to Hydrogen, "Code & analysis" to Argon, "Most complex work" to Carbon. Hydrogen is the speed/efficiency tier; Argon is the frontier reasoning tier.
- The HLRE amendment (2026-11-12) authorizes "Gemini 4 (Argon)" as the external verifier. The final report therefore does **not** satisfy the letter of the authorization: it is a Gemini 4-family verification by the wrong model. The initial run **was** Argon, ran the same question with a larger query set (145 vs 80 distinct), and reached the same verdict — so the sweep's verdict is still externally verified by the authorized model. The final report's grades are adopted only as corroboration, re-anchored on the initial run's corpus.
- The two runs are **not** two independent verifications of each other: same task conversation, same sweep question, same query set family, same single pipeline. Under HLRE Step 3 (I1 is not I3), they count as one artificial pipeline $\to$ I1. No grade rises from having two runs.
- **Correction required in the record:** the final report must be labelled "Gemini 4 Hydrogen run" wherever the sweep is cited. **Recommendation:** future Task-mode sweeps must pin the model picker to Argon before submitting and record the model label in the report; after a usage-limit reset, re-check the picker before sending a follow-up (the reset at 08:09 CST is the likely point at which the picker moved to Hydrogen).

## 2. Query counts: 145 (initial) vs 80 listed / 88 executed (final)

**Resolved: both counts are internally consistent; they describe different runs.**

- Initial log: this audit counted **145 numbered queries** (1–145) in the verbatim record. Arithmetic checks out: $145/63 = 2.30$ ("$2.30\times$" the 63-query baseline ✓).
- Final §5: this audit counted **80 listed query lines** in the verbatim record, and the trailing parenthetical names **8 additional queries** ("3101 jobs" / "Lean 4" / "$d4_{fourth}$_moment"; "0.380565" / "1.689598" / "Model B"; "source rebuild" / "Intrinsic Resonance Holography"; "source_rebuild_2" / "IRH"; "$S = \tau^2/q_4$" OR "$S = \tau^2/q_4$" / "$D_4$"; "$u_{eff} = u - 3v$" / "$D_4$"; "2T/Q8" / "affine E6" / "$D_4$"; "Brandon D. McCrary" / "ORCID"). $80 + 8 = 88$ executed ✓. Arithmetic checks out: $80/63 = 1.27$ ("+27%" ✓).
- Each verdict rests on its own run's corpus: the initial MISS rests on 145 queries / 88 inspected records; the final MISS rests on 80 distinct / 88 executed queries. The final report's "80-query wider retrieval (exceeding the 63-query baseline)" is accurate for its own run. "24 academic indexes" (initial) vs "22+ domains/databases" (final) are different runs' counts, not a contradiction.
- **Not verifiable from the record:** the initial report's "88 unique records" (no record-level list is given to check against) — UNVERIFIED, not refuted. The query logs themselves are the checkable evidence, and they check out.

## 3. Chaudhary: IJSREM 66 pp. vs Zenodo v2.4 88 pp. — RESOLVED

**The two reports read different versions of the same paper. The final report's pp. 65–88 gap is closed by this audit.**

- **Zenodo v2.4 (final report): VERIFIED.** Record https://zenodo.org/records/24124830 exists: published November 11, 2026, Version v7, file `Unified_Geometry_Clocks_Scales_Lepton_Angle_v2_4.pdf` (3.2 MB), with the note "Revised to v2.2, 5 October 2026; to v2.3, 12 October 2026; to v2.4, 10 November 2026 (Appendix D)". The PDF itself states "Page 1 of 88" — **88 pages confirmed**. This audit fetched the full PDF text (4,645 lines) and searched it: **zero matches for "McCrary" and zero matches for "Intrinsic Resonance"** across all 88 pages. Gemini's "pp. 65–88 UNVERIFIED" is therefore superseded: the whole v2.4 text is verified clean by this audit.
- **IJSREM version (initial report): PARTLY VERIFIED.** DOI 10.55041/IJSREM67145 resolves to the IJSREM page for the same paper (published 2026-09-07). The abstract matches, and the reference list shown on the page contains no McCrary (checked by this audit; the page itself notes "The remaining references of the two source papers are retained in their sections", so the shown list is not the complete reference list). The "66 pages" count and the full 66-page body were **not** re-read locally — UNVERIFIED, not refuted. The initial report's §30 (Attribution, pp. 61–62) could not be checked against the IJSREM body from the fetch.
- **Cross-version note:** the initial report's Chaudhary quotes ("2T is the largest finite subgroup of SU(2) all of whose elements have crystallographic order — order 24 against 12 for \$2$$D_{3}$$$. Scaled by $$$\sqrt{2}$$\$ its 24 elements are the $D_4$ root system, the 24-cell...") are **verbatim in the v2.4 text** (found at the PDF's line 427 by this audit). The quotes are genuine Chaudhary text; only the version attribution differs.
- **Minor correction:** the final report places "Relation to prior work" on p. 3; in the v2.4 PDF it begins on **p. 2**. The quoted sentence from it ("In this paper 2T is not a family symmetry: it is the unit group of the integral quaternions, its McKay graph is the gauge algebra, and the generation $Z_3$ is a separate object (§28).") is verbatim in the v2.4 text.

## 4. G-D6.2 independence: I2 (initial) vs I1 (final) — RESOLVED: I1

**The initial report's I2 is REFUTED as an independence overclaim. The final report's I1 is correct.**

- HLRE Step 3: I2 is "held-out observable under a frozen protocol, or independent re-derivation by a verifier who did not see the original". Executing 145 queries inside a single Gemini pipeline — one model, one session, one prompt set — is a single artificial pipeline. Per Step 3, "AI pipelines sharing inputs/prompts/sources" count as I1 ("new analysis of closely related data with shared selection choices"). There is no held-out observable and no second verifier who did not see the original. **I2 does not apply.**
- The final report correctly records I1 for G-D6.2. **Grade impact: none.** Under the 2026-11-12 amendment the $I1 \to C$ bound is repealed; the grade follows the evidence under the remaining rules: postulation ceiling constraint-led $\to$ B, caps none (scoped claim, no universal-negative overreach), support in record strong for the scoped claim (145-query Argon corpus + 80-query Hydrogen corpus, both zero). **B (scoped bound) stands.**
- The same reasoning applies to the final report's G-D6.1 (I1, B) and G-D6.4 (I1, B): I1 correctly stated, grades follow the evidence.

## 5. Scoped-absence grades (B) vs universal-negative ABSTAIN — CONFIRMED

**The grading follows HLRE Step 5 correctly in both reports.**

- Step 5: statuses (`INCOMPLETE-EVIDENCE`, `CONTRADICTED`) override letter grades where evidence is absent. The positive reception claim (G-D6.1 initial: "at least one independent work cites IRH") has zero supporting instances, so INCOMPLETE-EVIDENCE is the correct status, not a grade. Both reports apply this correctly.
- The scoped claims ("zero indexed independent works in the sampled corpus") are directly supported by the query logs and the full-text reads, so a letter grade is available; B follows from min(bound, caps, ceiling, record) with the I1 bound repealed. The universal negative ("no work anywhere cites IRH") is unobservable by open-web search, so ABSTAIN / INCOMPLETE-EVIDENCE is correct in both reports. The sentence "a wider sweep that still finds nothing STRENGTHENS a scoped bound — it does not prove a universal negative" is the correct HLRE rule, correctly applied.
- P2 (publication lag, "57 days"): arithmetic verified (\$17\$ Sep $\to$ \$13\$ Nov $= 57$ days ✓). The Drive-hosting fact and the "No file available" ResearchGate state are verified; the causal gloss ("this structural availability bottleneck explains why external citations have not yet accrued") is an interpretation, not a graded claim — flagged as such.

## Claim-by-claim table

Verdicts: VERIFIED / VERIFIED WITH CORRECTION / REFUTED / UNVERIFIED / ABSTAIN.

| # | Claim | Report | Verdict | Evidence |
|---|---|---|---|---|
| 1 | Verdict MISS (Strengthened Scoped Absence), zero independent works citing/discussing IRH | Both | VERIFIED | Both runs agree; this audit independently re-verified zero "McCrary" in Chaudhary v2.4 (full 88 pp.), Kulkarni (full text), Schmidt et al. (full text), Swann (full text), Ali (full text), and zero resolved citations on both RG records. |
| 2 | RG 401899717 (ssrn.6136926) shows Citations (0) | Both | VERIFIED | RG page fetched 2026-11-13: "ResearchGate has not been able to resolve any citations for this publication." Abstract matches Gemini's quote verbatim. |
| 3 | RG 405829591 (ssrn.6812879) shows Citations (0) | Both | VERIFIED | RG page fetched 2026-11-13: same "has not been able to resolve any citations" wording; abstract matches Gemini's quote verbatim. |
| 4 | G-D6.1 (final) grade B | Final | VERIFIED | Direct observation, I1, no caps; B follows the evidence under the repealed I1 bound. |
| 5 | G-D6.1 (initial) INCOMPLETE-EVIDENCE | Initial | VERIFIED | Zero instances found; Step 5 status override correctly applied. |
| 6 | G-D6.2 grade B (scoped) / ABSTAIN (universal) | Both | VERIFIED | Scoped claim supported by both corpora; universal negative unobservable. See §4 for the $I2 \to I1$ correction. |
| 7 | G-D6.2 independence I2 | Initial | REFUTED | Single pipeline is I1 per Step 3; no held-out observable, no second verifier. Corrected to I1 in the final report. |
| 8 | G-D6.2 independence I1 | Final | VERIFIED | Correctly stated. |
| 9 | G-D6.3 grade F2 (3 full texts + Chaudhary pp. 1–64) / UNVERIFIED (pp. 65–88) | Final | VERIFIED WITH CORRECTION | F2 stands (one machine route). The pp. 65–88 gap is **closed by this audit**: full 88-page v2.4 text searched, zero "McCrary" / zero "Intrinsic Resonance". IJSREM 66-page body remains locally unverified. |
| 10 | G-D6.3 universal negative ABSTAIN / INCOMPLETE-EVIDENCE | Initial | VERIFIED | Correct Step 5 application. |
| 11 | G-D6.4 grade B (80-query sweep widens 63-query baseline, +27%) | Final | VERIFIED | $80/63 = 1.27$ ✓; 80 listed lines counted ✓. |
| 12 | G-D6.4 grade B (prior-art corroboration, I3) | Initial | VERIFIED WITH CORRECTION | Hoy leg verified (arXiv:2311.03465; abstract quote verbatim). Elitzur (arXiv:1101.1631) and de Laat (arXiv:2404.18794v2) legs **UNVERIFIED in this session** (existence not re-confirmed; quotes not re-checked) — not refuted. Narrow surviving claim (Hoy + four contemporary works) supports B. |
| 13 | 145 distinct queries, 88 records, 10 full-text sources | Initial | VERIFIED WITH CORRECTION | 145 numbered queries counted in the record ✓; $145/63 = 2.30$ ✓. "88 unique records" UNVERIFIED (no record list). "10 full-text sources" does not reconcile: the listed sources number **11** (3 self + 5 contemporary incl. Kulkarni a+b + 3 prior-art). |
| 14 | "Full-text verification of all 6 independent papers" | Initial | VERIFIED WITH CORRECTION | The reads themselves are verified for the named works (see #16–20), but "6" matches no natural grouping (5 contemporary with Kulkarni as one; 8 total with prior-art). Which six is UNVERIFIED. |
| 15 | 80 distinct queries, 88 executed | Final | VERIFIED | 80 lines counted; 8 additional queries named in the parenthetical; $80 + 8 = 88$ ✓. |
| 16 | Chaudhary v2.4: 88 pages, pp. 1–64 read, pp. 65–88 UNVERIFIED | Final | VERIFIED WITH CORRECTION | 88 pages confirmed ("Page 1 of 88"; record 24124830, v2.4 dated 10 Nov 2026). The pp. 65–88 gap is closed by this audit's full-text search (see §3). "Relation to prior work (p. 3)" should read p. 2. |
| 17 | Chaudhary IJSREM: full 66-page text read, §30 Attribution pp. 61–62, zero citations | Initial | VERIFIED WITH CORRECTION | DOI 10.55041/IJSREM67145 resolves; abstract matches; shown reference list contains no McCrary. The 66-page count and full body were not re-read locally — UNVERIFIED. Quotes verified verbatim in the v2.4 text. |
| 18 | Kulkarni 2026b (Symmetry 18(11), 1813): 20 pp., 19 refs, zero IRH citations | Both | VERIFIED | MDPI page fetched: article exists; abstract and §1 quotes verified verbatim; full-text search (3,748 lines) zero "McCrary". Reference count (19) not counted locally — UNVERIFIED detail. |
| 19 | Schmidt et al. (Preprints.org 202605.2108 v2): read in full, 25 refs, zero IRH citations | Both | VERIFIED | PDF fetched (3,723 lines, 29 pp.; posted 22 June 2026, DOI 10.20944/preprints202605.2108.v2); full-text search zero "McCrary". Reference count (25) not counted locally — UNVERIFIED detail. |
| 20 | Swann (2026 RSTM PDF): read in full, 57 pp., 54 refs, zero IRH citations | Both | VERIFIED | PDF fetched from officialpaulswann.github.io/microscopic-rstm.pdf (4,205 lines; ORCID 0009-0006-4758-2169 matches; Zenodo DOI 10.5281/zenodo.22643415 v1.0); full-text search zero "McCrary"; "Relation to contemporary substrate-first approaches" subsection quote verified verbatim. Page/reference counts not counted locally — UNVERIFIED details. |
| 21 | Ali (2025, EPJC 85(11), 1282): 18 pp., 43 refs, zero IRH citations; 1 forward citation (McCulloch-James, May 2026) | Initial | VERIFIED WITH CORRECTION | Article verified (DOI 10.1140/epjc/s10052-025-15016-w; "Page 2 of 18"); full-text search (1,070 lines) zero "McCrary". Reference count (43) and the forward-citation claim UNVERIFIED locally. |
| 22 | Kulkarni 2026a (Quantum Reports 8(4), 109); 35 preprints in SSM corpus; RG Record 404913677 | Initial | UNVERIFIED | Not checked in this session. Not load-bearing for the absence verdict. |
| 23 | Final run produced by Gemini 4 (Argon) | Final (implied) | REFUTED | The follow-up run shows model label "Hydrogen". Gemini 4 Hydrogen is a distinct speed-tier model (launched Nov 12, 2026). See §1. |
| 24 | "A wider sweep that still finds nothing STRENGTHENS a scoped bound — it does not prove a universal negative" | Both | VERIFIED | Correct HLRE rule, correctly applied to both corpora. |
| 25 | Premise P1 (search coverage): Google search + direct browsing accurately reflect publicly indexed records as of 2026-11-13 | Initial | VERIFIED WITH CORRECTION | Verified for the public pages this audit re-fetched. UNVERIFIED for unindexed/private repositories — correctly ABSTAINed in both reports. |
| 26 | Premise P2 (publication lag): v93.1 dated Sept 17, 2026, 57 days before the audit; Drive-hosted, not DOI-minted | Initial | VERIFIED | \$57\$ days arithmetic ✓; Drive link and RG "No file available" state confirmed. Causal gloss is interpretation, not a graded claim. |

## Independent-check log (this audit, 2026-11-13)

- ResearchGate https://www.researchgate.net/publication/401899717 — fetched; title, abstract, "request a copy directly from the author", "ResearchGate has not been able to resolve any citations for this publication."
- ResearchGate https://www.researchgate.net/publication/405829591 — fetched; same three facts confirmed.
- Zenodo https://zenodo.org/records/24124830 — fetched; published Nov 11, 2026, Version v7, v2.4 dated 10 Nov 2026.
- Zenodo v2.4 PDF (3.2 MB, 4,645 fetched lines) — "Page 1 of 88"; find "McCrary" $\to$ 0 matches; find "Intrinsic Resonance" $\to$ 0 matches; find "largest finite subgroup of SU(2)" $\to$ verbatim match at L427.
- IJSREM DOI https://doi.org/10.55041/IJSREM67145 — resolves; published 2026-09-07; abstract matches; shown reference list searched, zero "McCrary".
- MDPI https://www.mdpi.com/2073-8994/18/11/1813 — fetched (3,748 lines); abstract/§1 quotes verbatim; find "McCrary" $\to$ 0 matches.
- Schmidt PDF https://quantumgravityresearch.org/wp-content/uploads/2026/06/preprints202605.2108.v2.pdf — fetched (3,723 lines, 29 pp.); find "McCrary" $\to$ 0 matches.
- Swann PDF https://officialpaulswann.github.io/microscopic-rstm.pdf — fetched (4,205 lines); find "McCrary" $\to$ 0 matches; "Relation to contemporary substrate-first approaches" quote verified verbatim at L412.
- Springer https://link.springer.com/article/10.1140/epjc/s10052-025-15016-w — fetched (1,070 lines); find "McCrary" $\to$ 0 matches.
- arXiv:2311.03465 (Hoy) — confirmed via arXiv/PubMed; abstract quote ("Supercooled four-dimensional (4D) Lennard-Jones (LJ) liquids maintained at zero pressure and constant temperatures $0.59 < T < 0.63$ crystallized within $\sim 2\times10^4 \tau$") verbatim.
- Google Gemini model documentation (support.google.com/gemini/answer/18648722) — "Gemini 4 Hydrogen: A high-speed, capable model"; Pro Tasks list Hydrogen and Argon as separate models. Launch Nov 12, 2026 (9to5Google, Digital Trends, Google DeepMind announcement).
- Record-file counts: initial log 145 numbered queries; final §5 80 listed lines + 8 named = 88 executed.

## Audit limitations

- No contact with any author, repository, or Gemini; no GCP spend; no Lean builds. All checks are open-web re-fetches by this audit's own tools.
- Elitzur (arXiv:1101.1631) and de Laat (arXiv:2404.18794v2) were not re-fetched in this session; their existence and quotes rest on Gemini's reads.
- Reference counts (Kulkarni 19, Schmidt 25, Swann 54, Ali 43) and Swann's 57-page count were not counted locally; they are not load-bearing for the absence verdict.
- The IJSREM 66-page full body was not re-read; only its DOI page (abstract + shown references) was checked.
- The "88 unique records" count and the "6 independent papers" count cannot be reconciled from the record as given.
- The browser task conversation "remains open in the retained tab for verification" per the handoff; this audit did not access the tab.

## Final grades (audited)

| Claim | Audited grade |
|---|---|
| G-D6.1 — independent reception of IRH (positive claim) | INCOMPLETE-EVIDENCE (no instances found) |
| G-D6.1 — RG preprints show Citations (0) | B |
| G-D6.2 — scoped absence of indexed independent citations | B (anchored on the Argon 145-query run; Hydrogen 80-query run corroborates) |
| G-D6.2 — universal negative | ABSTAIN / INCOMPLETE-EVIDENCE |
| G-D6.3 — the four inspected 2026 works do not cite/discuss IRH | F2 (premise ledger now closed for Chaudhary v2.4 by this audit's full-text check; IJSREM body still open) |
| G-D6.4 — 80-query sweep widens the baseline | B |
| G-D6.4 — prior-art corroboration of $D_4$ sub-claims | B, narrow surviving claim (Hoy + contemporary four verified; Elitzur/de Laat legs UNVERIFIED) |
| Sweep 6 overall | MISS (Strengthened Scoped Absence) — CONFIRMED |

---
*Report only. Nothing filed, committed, or written into the manuscript. No payment made; no contact with Gemini, Google, or any author. No GCP spend.*
