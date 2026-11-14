# LOCAL AUDIT — Gemini Sweep 5 (Gap G-C21): CDT Small-Scale Spectral Dimension Endpoint

**Audited:** Gemini Deep Research report "Sweep 5 Audit Report — Gap G-C21"
(Runs 1 and 2), retrieved from https://gemini.google.com/u/1/app/2660d093d0b7ee78
**Record:** `gemini-sweep-g-c21-2026-11-12.md` in this directory (verbatim, verify-clean)
**Audit date:** 2026-11-13, firsthand checks 12:41–12:46 CST
**Auditor:** Dragon (local claim-by-claim audit; no contact with Gemini, no GCP spend, no Lean builds)
**Governing rules:** truth-seeking-frontier v5; HLRE v5.1 as amended 2026-11-12
(I1 bound repealed and replaced by external verification; human-gate requirement
repealed; grades follow the evidence under the remaining rules).
**Prep brief:** `SWEEP5_AUDIT_PREP_2026-11-12.md` (117 lines) — its pre-checks were
re-verified each; two of its items are superseded below (§B.3, §B.10).
**Verdict in one line:** Gemini's core verdict is CONFIRMED — the $\sim 2$ vs
$\sim 3/2$ tension is bare-coupling / extrapolation-regime dependence across
Phase C, the canonical point is $\approx 2$, the continuum UV endpoint is
bounded to the scoped interval $[3/2, 2]$ at grade B with ABSTAIN on a sharp
value. The audit corrects Gemini's independence labels throughout, refutes
three supporting claims (Phase A value, branched-polymer value, Carlip aside),
corrects six citations, and records that the two prep-flagged defects (abstract
duplication; PRD "87") are absent from the retrieved report. No IRH grade change
is implied.

**Claim tally:** 65 numbered claims — 41 VERIFIED, 16 VERIFIED WITH CORRECTION,
3 REFUTED, 4 UNVERIFIED, 1 stated audit decision. The prep brief's
"abstract duplication" defect is additionally REFUTED as stated (no such claim
exists in the retrieved report; §B.1).

## §A. Record and provenance

- **Retrieval.** Browser task d3791f83, 2026-11-13 11:32–12:38 CST, after Brandon
  signed in himself in the browser (the saved Argon password had been rejected
  by Google at 11:33 CST). The task returned the FULL verbatim text of both runs.
- **Run 1** (31-page `IRH_v93_1.pdf`, Canvas, 2026-11-12 17:27 CST) is transcribed
  in full in the record file: verdict summary, §§1–8, including the Run 1-only
  "Audit Note on Primary Text Inspection" in §3.
- **Run 2** (33-page `IRH_v93.1_source_rebuild_2.pdf`, chat reply) is transcribed
  in full for its verdict summary and §1, then the retrieval's enumerated
  substitution list (a)–(g), the C-6 ledger row as it renders, the exact
  sentences, and the limitations note. **Run 2 §§2–8 were NOT independently
  re-transcribed; they rest on the retrieval's diff report.** The record file
  states this provenance honestly in its header; this audit grades Run 2 §§2–8
  only as diff-reported, not as independently re-transcribed.
- **Scope of this audit.** Every claim in the record was checked against its
  cited source where the source was fetchable. Firsthand checks: arXiv abstract
  pages (2604.05641, 1411.7712), hep-th/0505113 and hep-th/0505154 full text,
  arXiv:1411.7712 HTML (682 lines), arXiv:1603.02076, arXiv:1509.08788v2,
  arXiv:2401.09399, arXiv:1905.08669 (Loll 2019), arXiv:1705.05417 (Carlip 2017),
  both local IRH v93.1 builds (grep + rendered p. 17 of rebuild-2), and an
  independent SymPy recomputation in the conda env `jacobian-conjecture-2d`.
  The Loll repository PDF returned HTTP 403 on `browser.open` 2026-11-13 12:43
  CST; the published-version pagination is therefore UNVERIFIED and the URL was
  not retried.

## §B. Claim-by-claim audit

### B.1 The "abstract duplication" defect — EVAPORATES as stated

Gemini's exact sentences in the record (§3.2): the Ambjørn (2026) abstract is
quoted as "At the same time, large quantum fluctuations lead to unexpected
properties on short scales, most prominently, a spectral dimension near 2,
replacing the classical value of 4." The Coumbe & Jurkiewicz 2015 abstract is
quoted as "We calculate the spectral dimension for a nonperturbative lattice
approach to quantum gravity, known as causal dynamical triangulations (CDT),
showing that the dimension of spacetime smoothly decreases from approximately 4
on large distance scales to approximately 3/2 on small distance scales..."

1. **The retrieved report text contains NO claim that the Ambjørn (2026)
   abstract duplicates the Coumbe & Jurkiewicz 2015 abstract.** — VERIFIED.
   The word "duplicat" does not occur anywhere in the retrieved text; neither
   does any sentence asserting the two abstracts are the same text. The prep
   brief's defect ("if Gemini's report really asserts verbatim duplication")
   is therefore REFUTED as stated: there is no such assertion to refute.
2. **Gemini's Ambjørn 2026 abstract sentence is verbatim.** — VERIFIED
   firsthand against arXiv:2604.05641 (Ambjørn & Loll, submitted 7 Apr 2026,
   invited Scholarpedia contribution): the sentence appears exactly as quoted.
3. **Gemini's Coumbe & Jurkiewicz 2015 abstract sentence is verbatim.** —
   VERIFIED firsthand against arXiv:1411.7712 (JHEP 03 (2015) 151).
4. **The two abstracts are plainly different texts.** — VERIFIED. Different
   sentences, different structure, different claims: the 2026 abstract is a
   review framing ("Causal Dynamical Triangulations (CDT) is a methodology to
   define and compute the gravitational path integral..."); the 2015 abstract
   reports a calculation ("We calculate the spectral dimension... showing that
   the dimension of spacetime smoothly decreases from approximately 4... to
   approximately 3/2...").
5. **Caveat (scope).** The retrieval excluded the chat's prompts and research
   plan; a duplication claim could only live in a part of the chat that was not
   retrieved. — UNVERIFIED (unretrieved scope, not a gap in the report).

### B.2 C-6 — reproduced exactly as rendered; NO grade

6. **C-6 renders with NO Computation cell in either run.** — VERIFIED. The
   C-6 row in §6.1 has a claim cell and a Track cell ("Track E / Track F
   (Comparative audit)") and nothing else in the Bound / Caps / Ceiling /
   Record columns.
7. **C-6 renders with NO Final Grade cell in either run.** — VERIFIED. No
   grade string follows the C-6 row in either run.
8. **The two stray cells reading "4 - 4.02" and "= $0.02 \pm 0.10))$." are the
   tail of the C-6 claim text split across cells.** — VERIFIED as a rendering
   description. The claim text ends "...and agrees only asymptotically as
   $\sigma\to\infty$ (($|4 - 4.02| = 0.02 \pm 0.10$))" and the parenthesised
   tail split off into two extra cells. This is a report-formatting artifact,
   not a content claim.
9. **Audit decision (stated, not a claim): no grade is invented for C-6.**
   The underlying divergences (2.184, $2.20 \pm 0.25$, $2.03 \pm 0.27$,
   $\approx 2.50$, $0.02 \pm 0.10$) are independently verified in §B.5; a grade
   for C-6 itself would require a Computation the report never rendered.

### B.3 PRD citation 87 vs 93 — the "87" error is ABSENT from the retrieved text

10. **"87, 104032" does NOT appear anywhere in the retrieved text.** —
    VERIFIED. The string "87" occurs in the retrieved text only inside
    "1411.7712" (twice). Count of "87, 104032": 0.
11. **"93, 104032" appears 3 times in the retrieved text.** — VERIFIED (§3
    introduction of the 1603 paper; §3.2 quotation; §8 item 5).
12. **Phys. Rev. D 93, 104032 (2016) is the correct citation.** — VERIFIED:
    Ambjørn, Coumbe, Gizbert-Studnicki & Jurkiewicz, "Searching for a
    continuum limit in causal dynamical triangulation quantum gravity",
    arXiv:1603.02076.
13. **The prep brief's "87 once vs 93 elsewhere" does not match the retrieved
    text.** — VERIFIED WITH CORRECTION. The prep described a report that cites
    87 once; the report as retrieved cites 93 three times and 87 never as a
    volume. The correction is verdict-neutral either way (93 is right), but the
    prep item is superseded: there is no "87" error in the retrieved report to
    correct.

### B.4 Canonical point, endpoint values, and the multi-point shift

14. **The canonical point is $(\kappa_0, \Delta) = (2.2, 0.6)$.** — VERIFIED.
    hep-th/0505113 p. 5 and hep-th/0505154 Fig. 10 both state the simulations at
    $\kappa_0 = 2.2$, $\Delta = 0.6$, $t = 80$, $N_4 = 181k$.
15. **$D_S(\sigma=0) = 1.80 \pm 0.25$ at the canonical point (2005).** —
    VERIFIED against hep-th/0505113 eq. (15), fitted over $\sigma \in [40, 400]$
    with the $\sigma \ge 40$ cut for odd-even artifacts.
16. **$D_S(\sigma\to 0) = 1.97 \pm 0.27$ at the canonical point (2015).** —
    VERIFIED against arXiv:1411.7712 Table 2: $(2.2, 0.6)$, 160k,
    $D_S(0) = 1.970 \pm 0.266$, 0.1 s.d. from 2, $a_{rel} = 1.00$; Table 1
    volume for that point 367k.
17. **The asymptotic value $D_S(\sigma=\infty) = 4.02 \pm 0.10$.** — VERIFIED WITH CORRECTION. $4.02 \pm 0.10$ is the 2005 fit value (hep-th/0505113
    eq. (14)); the 2015 canonical-point fitted value is $4.05 \pm 0.17$ (C&J
    Table 2). The two agree within errors; Gemini's C-2 attributes the 2005
    value without saying so.
18. **The multi-point shift is real: across $(2.2, 0.6)$, $(3.6, 0.6)$,
    $(4.4, 0.6)$ the extrapolated $D_S(0)$ falls to $\approx 1.53$–\$1.58\$ and
    $a_{rel}$ falls to 0.57 then 0.11.** — VERIFIED against C&J 2015 Table 2:
    $(3.6, 0.6)$: $1.576 \pm 0.093$, 4.5 s.d. from 2, $a_{rel} = 0.57$;
    $(4.4, 0.6)$: $1.534 \pm 0.058$, 8.0 s.d., $a_{rel} = 0.11$;
    $(4.4, 2.0)$ 300k: $1.540 \pm 0.060$, 7.7 s.d., $a_{rel} = 0.10$.
19. **Gemini's "down to $a_{rel} = 0.118$" understates the minimum.** —
    VERIFIED WITH CORRECTION. arXiv:1603.02076 Table 2 gives $a_{rel} = 0.116   \pm 0.001$ at P4 $(4.67, 0.6)$; 0.118 is the P6 value ($0.118 \pm 0.003$).
    Full P1–P8: P1 $(2.20, 0.6)$ $a_{rel} = 1$; P2 $(3.60, 0.6)$ $0.791 \pm   0.008$; P3 $(4.40, 0.6)$ $0.336 \pm 0.006$; P4 $(4.67, 0.6)$ $0.116 \pm   0.001$; P5 $(4.64, 0.5)$ $0.134 \pm 0.001$; P6 $(4.62, 0.4)$ $0.118 \pm   0.003$; P7 $(4.57, 0.3)$ $0.122 \pm 0.001$; P8 $(4.53, 0.2)$ $0.122 \pm   0.001$.
20. **Gemini's Phase A value $D_S \approx 1.5$ is REFUTED; the correct value
    is $4/3$.** — REFUTED. C&J 2015 §3.2.1: the Phase A spectral dimension is
    "consistent with the constant 4/3 over the $\sigma$ range studied
    $\sigma\in[60,492]$", Fig. 7 at $(\kappa_0, \Delta) = (8.0, 0.6)$. Loll
    2019 pp. 42–43 agrees: Phase A at $(8.0, 0.6)$ shows "strong indications
    of 'branched-polymer' behaviour $D_S\approx4/3$, independent of $\sigma$
    in the range $\sigma\in[60,500]$".
21. **Gemini's "branched-polymer value (1.5–1.6)" is REFUTED.** — REFUTED.
    The branched-polymer value is $4/3$ (claim 20). The 1.5–1.6 range is the
    level of the near-transition Phase C curves, not the branched-polymer value.
22. **Gemini's §4 table generalization "$\sigma<40$ is spoiled" is the 2005
    cut, not C&J's.** — VERIFIED WITH CORRECTION. C&J 2015 fit cuts are
    $\sigma\in[50,494]$ (canonical) and $[60,492]$ (others); the $\sigma \ge 40$
    cut belongs to the 2005 fit (hep-th/0505113, $\sigma \in [40, 400]$).
23. **The 1603 p. 8 quotation is verbatim.** — VERIFIED: "Typically, we find
    a small scale spectral dimension that is more consistent with the lower
    bound $D_S(\sigma\to0)\sim3/2$... than with $D_S(\sigma\to0)\simeq2$,
    thereby supporting the findings of Ref. [16]. Furthermore, except for the
    points close to the C-A transition we find a large scale spectral
    dimension that is consistent with $D_S(\sigma\to\infty)\sim4$". Pagination
    note: it sits on arXiv v3 p. 9; PRD p. 8 is plausible. Ref [16] = Coumbe &
    Jurkiewicz 2015 (JHEP 1503:151); ref [18] = Ambjørn, Jurkiewicz & Loll
    2005 (PRL 95, 171301). Eq. (14) $D_S(\sigma)=a-b/(c+\sigma)$ and eq. (15)
    rescaling $D_S(\sigma)=a-b/(c+\sigma/a_{rel}^2)$ check out.
24. **Gemini's §3.2 MG14 quotation says "summarised in Table 1" where the
    arXiv version says "summarised in Table 2".** — VERIFIED WITH CORRECTION
    (minor quote discrepancy; the ResearchGate rendering may differ). The
    "majority of the sampled points" language is verified in both the
    proceedings (arXiv:1509.08788v2) and C&J 2015.
25. **Gemini's Ambjørn (2026) citation is wrong on authors and title.** —
    VERIFIED WITH CORRECTION (§2, §8 item 8). The paper is Ambjørn & Loll
    (TWO authors), "Causal Dynamical Triangulations: New Lattice Theory of
    Quantum Gravity", arXiv:2604.05641, submitted 7 Apr 2026 — not single-author
    Ambjørn, and not "Causal Dynamical Triangulations: A Review".
26. **Gemini's 2024 citation is wrong on authors and title.** — VERIFIED WITH CORRECTION (§2, §8 item 7). arXiv:2401.09399 is Ambjørn & Loll only
    (no Jurkiewicz), "Causal Dynamical Triangulations: Gateway to
    Nonperturbative Quantum Gravity" — not "Causal Dynamical Triangulations and
    the Search for a Theory of Quantum Gravity". Its Fig. 5 replotted the 2005
    fit at $N_4 = 360,000$; it is not a new 2024 measurement. Fig. 5 caption
    and the "$D_s(\sigma\to0) = 1.80 \pm 0.25$, a phenomenon dubbed dynamical
    dimensional reduction" sentence are verbatim.
27. **Gemini's Loll journal year "(2019)" is wrong.** — VERIFIED WITH CORRECTION (§8 item 6). Loll, "Quantum Gravity from Causal Dynamical
    Triangulations: A Review", CQG 37, 013002, is 2020 (arXiv May 2019).
28. **Gemini's §4 Carlip aside is REFUTED as stated, on two counts.** —
    REFUTED. (a) arXiv:1612.03894 is Mielczarek & Trześniewski, "Spectral
    dimension with deformed spacetime signature" (LQG, $d_S\to1$ in the UV),
    not Carlip — Carlip 2017 is arXiv:1705.05417. (b) Carlip §3.2 says 3D CDT
    drops from $d_S = 3$ at large scales to $d_S \approx 2$ at small scales,
    and "may be consistent with $d_S = 1.5$" is an uncertainty caveat on the
    4D value; the $\approx 1.5$ value in Carlip §3.2 is Euclidean DT with
    fine-tuned measure, not 3D CDT. Verdict-neutral for the interval (it rests
    on the 4D Phase C endpoints), but the supporting aside is wrong.
29. **Loll's corroboration quotation is verbatim.** — VERIFIED: "Ref. [91]
    corroborates the original result $D_S \approx 2$... finding
    $D_S(\sigma\to0) = 1.97 \pm 0.27$ in simulations at roughly twice the
    previous volume, $N_4 = 367k$, with time extension $t_{tot} = 80$" —
    arXiv v1 ref [91], p. 42. Gemini cited the published [97] / p. 34; the
    published-version pagination is UNVERIFIED (repository PDF HTTP 403).
30. **Loll pp. 42–43 strongly support Gemini's §4 / interval reasoning.** —
    VERIFIED, verbatim: the curves "flatten considerably in the $\sigma$-range
    considered ($\sigma\le500$)"; "$D_S(0)\approx1.5$ at these points... seems
    at odds with the assumed universal character"; "The curves become extremely
    flat, with $D_S$ barely exceeding 1.6 at the upper end $\sigma=500$...
    One has to set $a\approx4$ by hand in eq. (32)"; "make it difficult to
    judge whether the qualitative increase in the lattice spacing... is a
    genuine physical effect"; "Comparing measurements at different points in
    phase space is of course not meaningful a priori unless they lie on the
    same renormalization group trajectory of constant physics".
31. **The "We expect" fragment in Gemini's Fig. 10 quotation was not located
    in the caption.** — UNVERIFIED as quoted (likely adjacent body text in
    hep-th/0505154; verdict-neutral). The rest of the caption is verbatim:
    "measured for $\kappa_0 = 2.2$, $\Delta = 0.6$ and $t = 80$, and a
    spacetime volume $N_4 = 181k$... superimposed best fit
    $D_S(\sigma) = 4.02-119/(54+\sigma)$. The two outer curves represent
    error bars."
32. **The $a_{abs}$ 0.33–0.43 numbers are verified, but the tabulated values
    are rescaled to unity at P1, not absolute Planck units.** — VERIFIED WITH CORRECTION (framing). 1603 Table 2 $a_{abs}$ columns (rescaled to 1 at P1)
    range 0.33–0.43 across P6–P8; Gemini's §4 table presents them without the
    rescaling note.

### B.5 The 2005-fit arithmetic — independently recomputed

All recomputations below were run 2026-11-13 ~12:46 CST in the conda env
`jacobian-conjecture-2d` (SymPy), independently of Gemini's arithmetic.

33. **$D_s(0) = 4.02 - 119/54 = 1.816296\ldots$** — VERIFIED. $119/54 =   2.2037037\ldots$; $4.02 - 2.2037037 = 1.8162963 \approx 1.816$.
34. **The divergences: $4 - 1.816296 = 2.1837 \approx 2.184$ (central fit);
    $4 - 1.80 = 2.20 \pm 0.25$ (2005 ensemble); $4 - 1.97 = 2.03 \pm 0.27$
    (2015 canonical point); $4 - 3/2 = 2.50$ (fine-lattice endpoint);
    $|4 - 4.02| = 0.02 \pm 0.10$ (IR agreement).** — VERIFIED.
35. **The sigma-figures: $2.20/0.25 = 8.8\sigma$; $2.03/0.27 = 7.5185 \to   7.5\sigma$; $0.02/0.10 = 0.2\sigma$.** — VERIFIED.
36. **The $+0.32$ in §5: $2.50 - 2.1837 = 0.3163 \approx 0.32$.** — VERIFIED.
37. **Canonical-point agreement: $1.97 - 1.80 = 0.17$ against combined
    $\sigma = \sqrt{0.25^2 + 0.27^2} = 0.368$, i.e. $0.46\sigma$ apart.** —
    VERIFIED. The 2005 and 2015 canonical-point values agree well within
    errors.
38. **"Roughly twice" the volume: \$367{,}000/181{,}$000 = 2.03\times$\$.** —
    VERIFIED.
39. **The scaling exponents and the Derrick identity re-derive exactly.** —
    VERIFIED. Under $\psi(x) \to \psi(\lambda x)$ in $d$ dimensions: gradient
    $\lambda^{2-d}$, potential $\lambda^{-d}$, 4-derivative $\lambda^{4-d}$;
    $4 - d = 0 \iff d = 4$ uniquely; Derrick identity
    $\frac{d}{d\lambda}[\lambda^{2-d} I_{grad} + \lambda^{-d} I_{pot}]_{\lambda=1}   = (2-d) I_{grad} - d I_{pot} = 0$ confirmed.

### B.6 Run 1's Audit Note — the access block was transient

40. **arXiv:1411.7712 HTML loads fine now (682 lines).** — VERIFIED firsthand,
    2026-11-13 12:41 CST. Table 2, §3.2.1, and §4 were all read from it for
    claims 16, 18, 20, 22.
41. **The one-pass access block affects no graded claim.** — VERIFIED. The
    Audit Note's own conclusion stands ("the arXiv PDF is the authoritative
    text"), the PDF values were read, and the HTML is accessible on re-check.
    The block was transient.

### B.7 Run 2's SymPy verification claim — checked against the local rebuild-2 PDF

42. **The Expansion block exists on rebuild-2 p. 17 and says "Verified
    symbolically in SymPy".** — VERIFIED. Rebuild-2 p. 17 was rendered to
    `/tmp/rebuild2_p17-17.png` and read firsthand.
43. **Run 2's page citations check out against the actual PDF.** — VERIFIED:
    §III.4 heading p. 16, expansion block p. 17; §VIII.3 p. 27; §IX.2 p. 27,
    §IX.3 p. 28.
44. **Gemini's Run 2 §1 quotation misquotes one line.** — VERIFIED WITH CORRECTION (minor). Gemini writes "$\psi \to \psi$ so
    $|\nabla\psi|^2 \to \lambda^2|\nabla\psi|^2$"; the manuscript reads
    "$\nabla \to \lambda\nabla$ so $|\nabla\psi|^2 \to   \lambda^2|\nabla\psi|^2$".
45. **Zero CDT mentions in BOTH builds.** — VERIFIED by grep (count 0) over
    the full term list (CDT, Causal Dynamical Triangulations, spectral
    dimension, Ambjørn, Jurkiewicz, Loll, Coumbe; also no $D_S$ / $D_s$ in
    rebuild-2) in `/tmp/rebuild2.txt` (pdftotext of
    `IRH_v93.1_source_rebuild_2.pdf`) and `IRH_v93_1_source_rebuilt.txt`.
46. **Run 1's page citations (§III.4 pp. 14–15; Part VII p. 22; §IX.2–IX.3
    p. 25) are UNVERIFIED.** — UNVERIFIED (caveat, not refutation). No local
    31-page PDF exists; the `.txt` is a different rendering whose form-feed
    pagination differs (its §III.4 falls pp. 17–18, Part VII p. 25, §IX.2
    p. 28).
47. **"This must be decided. It is not resolvable by further calculation."
    is on rebuild-2 p. 28.** — VERIFIED.

### B.8 Independence — Gemini's I-assignments corrected under HLRE Step 3

48. **Deep Research is a single artificial pipeline, so the sweep's
    independence is I1.** — VERIFIED. One chat, one question, one pipeline
    family, shared prompts and sources.
49. **The two runs are not two verifications.** — VERIFIED. Same chat, same
    question, same pipeline family; Run 2 re-audits a different manuscript
    build, it does not independently verify Run 1.
50. **C-1: Gemini's "I4" label is wrong; the A / F1 verdict stands on the
    audit's independent re-derivation.** — VERIFIED WITH CORRECTION. C-1 is
    exact arithmetic on a published formula (claim 33, recomputed here from
    hep-th/0505113 eq. (11)); the "I4" label is a category error, but the
    A/F1 verdict is independently established by this audit.
51. **C-2: I3 $\to$ I2.** — VERIFIED WITH CORRECTION. The two studies share
    authors (Ambjørn & Jurkiewicz co-author both the 2005 and the 2015 work),
    so they are not independent teams; grade unchanged (I2 $\to$ B).
52. **C-3: I2/I3 $\to$ I1.** — VERIFIED WITH CORRECTION. The 2015/2016
    multi-point scan is one collaboration's work (Ambjørn, Coumbe,
    Gizbert-Studnicki, Jurkiewicz — the same CDT group); grade unchanged
    (B on Track E).
53. **C-4: I4 $\to$ I1; and "I4 $\to$ B" is incoherent.** — VERIFIED WITH CORRECTION. Under the rules I4 $\to$ A; the B on the interval comes from
    the caps / ceiling / record (extrapolation cap, unresolved RG flow), not
    from I4. Grade unchanged (B on the interval, ABSTAIN sharp).
54. **C-5: the "I4" label is wrong; F2 stands on the audit's independent
    manuscript check and SymPy re-derivation.** — VERIFIED WITH CORRECTION.
    The manuscript's own "Verified symbolically in SymPy" is a self-assertion,
    not an independent route; the independent route is this audit's claims 39,
    42–43.
55. **Gemini's §7 disclosure is honest.** — VERIFIED. It states I1, and states
    the amendments (human-gate repeal, I1-bound repeal) correctly.
56. **"The wider sweep strengthens a scoped bound" is the correct HLRE rule,
    correctly applied.** — VERIFIED. A wider retrieval that finds no
    counterexample strengthens a scoped bound; it does not convert it into a
    universal claim.

### B.9 The zero-CDT-mentions finding, scoped

57. **The zero-mentions finding is scoped to the two builds inspected.** —
    VERIFIED (claim 45; the scope is the two v93.1 builds, not the IRH
    literature generally).
58. **The "scoped bound" language is correct HLRE usage.** — VERIFIED. The
    interval $[3/2, 2]$ is a bound on a scoped domain (Phase C, stated
    couplings), not a universal endpoint claim.

### B.10 Reconciliation with the prep brief

59. **Prep brief's "C-3 grade B (Track F)" is wrong; the retrieved text says
    Track E, and the retrieved text governs.** — VERIFIED WITH CORRECTION.
    C-3 is a literature-synthesis / lattice-simulation claim (Track E), and
    Gemini grades it B on Track E in both runs.
60. **Both Drive archive links are UNVERIFIED.** — UNVERIFIED (flagged). The
    Run 1 link ID begins `1Sxkginzo...` and the Run 2 link ID begins
    `15xkginzo...` — they differ by one character (`S` vs `5`). Neither link
    was opened in this session; flag as a possible transcription artifact,
    not as a verified difference.

### B.11 Premises P-1–P-4

61. **P-1 — VERIFIED.** The $\sigma \ge 40$ cut is documented
    (hep-th/0505113: odd-even artifacts below $\sigma = 40$); the return
    probability $D_S(\sigma) = -2\, d\log \langle P(\sigma) \rangle / d\log   \sigma$ is the standard CDT dimension estimator.
62. **P-2 — VERIFIED.** The ansatz $D_S(\sigma) = a - b/(c+\sigma)$ plus
    sensitivity is documented; C&J 2015 Tables 3–4 give alternative fits.
63. **P-3 — VERIFIED as contested.** Whether the finer-lattice shift is a
    genuine physical effect is genuinely contested in the literature: Loll
    2019, "make it difficult to judge whether the qualitative increase in the
    lattice spacing... is a genuine physical effect" (claim 30).
64. **P-4 — VERIFIED.** The $R^4$ Swift-Hohenberg substrate is INPUT in
    §I.2 and its physical-spacetime mapping is OPEN in §IX.2–IX.3 (local
    rebuild-2 text, pp. 3, 27–28).

### B.12 IRH consequence

65. **No IRH grade change is implied by Gemini's verdict.** — VERIFIED.
    Gemini's verdict is about CDT's endpoint, not about IRH: IRH fixes $D = 4$
    and diverges from CDT in the UV by 2.184–2.50 while agreeing only in the
    IR. That is a comparison, not a revision of any IRH claim.

## §C. Audited grades

| Claim | Gemini's grade | Audited grade | Basis |
|---|---|---|---|
| C-1 CDT central fit evaluation | A (Track F: F1), "I4" | **A (Track F: F1)** — VERIFIED WITH CORRECTION | Exact arithmetic, independently re-derived (§B.5, claim 33). "I4" label wrong (claim 50). |
| C-2 CDT canonical-point endpoint | B (Track E), "I3" | **B (Track E)** — VERIFIED WITH CORRECTION | §B.4 claims 14–17. I3 $\to$ I2 (claim 51). |
| C-3 Multi-point finer-lattice shift | B (Track E), "I2/I3" | **B (Track E)** — VERIFIED WITH CORRECTION | §B.4 claims 18–19. I2/I3 $\to$ I1 (claim 52). Prep's "Track F" wrong (claim 59). |
| C-4 Continuum UV endpoint | B on interval $[3/2, 2]$; ABSTAIN sharp, "I4" | **B on interval $[3/2, 2]$; ABSTAIN sharp** — VERIFIED WITH CORRECTION | §B.4 claims 20, 22, 30. I4 $\to$ I1 (claim 53). |
| C-5 Swift-Hohenberg marginality | F2 (Track F) on $d = 4$ scaling; C / OPEN (Track E) on physical spacetime, "I4" | **F2 (Track F) on $d = 4$ scaling; C / OPEN (Track E) on physical spacetime** — VERIFIED WITH CORRECTION | §B.5 claim 39; §B.7 claims 42–44. "I4" label wrong (claim 54). |
| C-6 UV vs IR divergence | No grade rendered | **NO GRADE** (not rendered) | §B.2. Underlying divergences verified (§B.5). No grade invented. |
| P-1–P-4 | As stated in §6.2 | **P-1 VERIFIED; P-2 VERIFIED; P-3 VERIFIED as contested; P-4 VERIFIED** | §B.11. |

**Gemini's overall verdict — CONFIRMED.** The $\sim 2$ vs $\sim 3/2$ tension is
bare-coupling / extrapolation-regime dependence across Phase C; the canonical
point is $\approx 2$; the continuum UV endpoint is bounded to the scoped
interval $[3/2, 2]$ at grade B with ABSTAIN on a sharp value; IRH's fixed
$D = 4$ diverges from CDT in the UV and agrees only in the IR.

## §D. Errata ledger

### D.1 Errors in Gemini's report (mechanical demotion: none — no claim that depends on these errors changes grade)

1. **Phase A value $D_S \approx 1.5$** (§4) — REFUTED; correct is $4/3$
   (claim 20). Affects §4 reasoning only; the interval verdict rests on the
   Phase C endpoints and is unchanged.
2. **"Branched-polymer value (1.5–1.6)"** (§4) — REFUTED; the
   branched-polymer value is $4/3$ (claim 21).
3. **Carlip §4 aside** (3D CDT $\approx 1.5$, link arXiv:1612.03894) — REFUTED
   as stated (claim 28). Wrong link (Mielczarek & Trześniewski, not Carlip)
   and wrong attribution ($\approx 1.5$ is Euclidean DT, not 3D CDT).
4. **Ambjørn (2026) citation** (§2, §8 item 8) — single author and title
   wrong (claim 25). Correct: Ambjørn & Loll, "Causal Dynamical
   Triangulations: New Lattice Theory of Quantum Gravity", arXiv:2604.05641.
5. **2024 citation** (§2, §8 item 7) — authors and title wrong (claim 26).
   Correct: Ambjørn & Loll only, "Causal Dynamical Triangulations: Gateway
   to Nonperturbative Quantum Gravity", arXiv:2401.09399.
6. **Loll year (2019)** (§8 item 6) — wrong; CQG 37 is 2020 (claim 27).
7. **"$a_{rel}$ down to 0.118"** (§3.2) — understates the minimum; P4 is
   $0.116 \pm 0.001$ (claim 19).
8. **"$\sigma<40$ is spoiled" generalization** (§4 table) — the C&J cut is
   50/60, not 40 (claim 22).
9. **"summarised in Table 1"** (§3.2 MG14 quote) — arXiv version says
   Table 2 (claim 24).
10. **Independence labels throughout** (C-1 I4; C-2 I3; C-3 I2/I3; C-4 I4;
    C-5 I4) — all corrected downward (§B.8). No grade changes.
11. **Run 2 §1 misquotation** ("$\psi \to \psi$" for "$\nabla \to   \lambda\nabla$") — minor (claim 44).
12. **$a_{abs}$ framing** (§4 table) — values rescaled to unity at P1, not
    absolute Planck units (claim 32).
13. **C-2 asymptotic attribution** — $4.02 \pm 0.10$ is the 2005 value; the
    2015 canonical-point value is $4.05 \pm 0.17$ (claim 17).

### D.2 Corrections to the prep brief (superseded by the retrieved text)

1. **"Abstract duplication" defect** — REFUTED as stated. No duplication claim
   exists in the retrieved report (§B.1).
2. **"PRD 87 cited once"** — superseded. "87, 104032" occurs 0 times;
   "93, 104032" occurs 3 times (§B.3).
3. **"C-3 grade B (Track F)"** — wrong; retrieved text says Track E (§B.10).

### D.3 Withdrawal ledger

No Gemini claim is withdrawn. The three REFUTED items (claims 20, 21, 28) are
supporting asides; the claims that cite them do not change grade, so no
mechanical demotion is triggered. The prep brief's three superseded items are
recorded in §D.2, not withdrawn from the prep file (the prep file is a
research-stage note, not a deposited record).

## §E. Limitations and open items

- **Run 2 §§2–8 rest on the retrieval's diff report**, not on independent
  re-transcription (§A). Any claim graded here about Run 2 §§2–8 carries that
  provenance.
- **Run 1 page citations are unverified** (claim 46): no local 31-page PDF
  exists. The 33-page rebuild-2 citations are verified; the 31-page ones are
  a caveat, not a refutation.
- **Loll published-version pagination unverified** (claim 29): the repository
  PDF returned HTTP 403; the arXiv v1 pagination was used instead.
- **Drive archive links unverified** (claim 60): the two reported links differ
  by one character (`S` vs `5`); neither was opened.
- **"We expect" fragment** (claim 31): not located in the Fig. 10 caption;
  likely adjacent body text; verdict-neutral.
- **Per-point volumes for P4–P8 at 300k** are consistent with the §2 policy in
  1603.02076 but are not tabulated per-point; caveat, not refutation.
- **No IRH grade change** is implied by this sweep (§B.12).

## §F. Evidence index (firsthand checks, 2026-11-13)

- arXiv:2604.05641 abstract (Ambjørn & Loll; two authors; submitted 7 Apr
  2026; invited Scholarpedia contribution) — 12:41 CST.
- arXiv:1411.7712 abstract + HTML (682 lines): Table 1, Table 2, §3.2.1,
  §4 — 12:41 CST.
- hep-th/0505113 full text: eqs. (10), (11), (14), (15); $\sigma \in [40, 400]$;
  $N_4 = 181{,}000$, $t = 80$, $\sigma_{\max} = 400$ — 12:41 CST.
- hep-th/0505154 Fig. 10 caption — 12:41 CST.
- arXiv:1603.02076: Table 2 (P1–P8), p. 8/9 quotation, §2 finite-size passage,
  eqs. (14), (15), refs [16], [18] — 12:41–12:42 CST.
- arXiv:1509.08788v2 (MG14 proceedings) — 12:42 CST.
- arXiv:2401.09399: Fig. 5 caption, "$D_s(\sigma\to0) = 1.80 \pm 0.25$" sentence
  — 12:42 CST.
- arXiv:1905.08669 (Loll 2019): corroboration quotation (v1 ref [91], p. 42),
  pp. 42–43 interval reasoning — 12:42 CST. Repository PDF HTTP 403, 12:43 CST.
- arXiv:1705.05417 (Carlip 2017) §3.2 — 12:42 CST. arXiv:1612.03894 identified
  as Mielczarek & Trześniewski — 12:42 CST.
- Local builds: grep count 0 for CDT terms in both builds — 12:42 CST.
  Rebuild-2 p. 17 rendered (`/tmp/rebuild2_p17-17.png`) and read; §III.4 p. 16,
  §VIII.3 p. 27, §IX.2 p. 27, §IX.3 p. 28, "This must be decided..." p. 28 —
  12:42 CST.
- Independent SymPy recomputation (conda env `jacobian-conjecture-2d`):
  $D_s(0)$, divergences, sigma-figures, scaling exponents, Derrick identity —
  12:46 CST.
