# IRH v95 draft — CHANGELOG (against v94 at origin/main 1ea6c14)

Base: `programme/v94/IRH_v94.tex` (1214 lines, sha256 e69c9565…0975993), unchanged.
New file: `programme/v95/IRH_v95_draft.tex`, built to `IRH_v95_draft.pdf` (43 pp., XeTeX / TeX Live 2026).

## Errata applied (each was an error or record defect in v94)

| # | v94 location | v94 text | v95 | source |
|---|---|---|---|---|
| E1 | ref [26] | GRS DOI `10.1016/0370-2693(76)90417-6` | `…90417-2` | INSPIRE / ScienceDirect pii 0370269376904172 (checked 2026-11-25) |
| E2 | ref [45] | EKR entry carries `arXiv:math/0607446` | removed (that id is Cohn–Kumar, ref [43]); keeps arXiv:1101.1631, doi:10.1142/S0217984911026358 | arXiv listing (checked 2026-11-25) |
| E3 | ref [34] | Lean system description pp. 26–48, doi …21401-6_2 | pp. 378–388, doi 10.1007/978-3-319-21401-6_26 | Lean devs' citation (Zulip), multiple bibliographies (checked 2026-11-25) |
| E4 | ref [35] | Mathlib CPP 2020 pp. 30–46 | pp. 367–381 | ACM bibtex (checked 2026-11-25) |
| E5 | §II.7 / Appx A item 8 | band "≈11.6%" and record values 11.85% / 11.90% | canonical 758/6561 = 11.5531% with full R1 definition; one-mode 756/6561 = 11.5226%; hex6-only 12.9706%; 161² one-mode 11.60%; coexistence 11.42%; 11.85% and 11.90% stated as not reproducible | run-12 G-A19 ruling; inventory; recompute_v95.log |
| E6 | l.374 | uniform density 1.0333364 stated without the $k=0$ term | formula now includes $\tfrac12 q_0^4\bar\psi^2$ (E-B8a) | record fix E-B8a; recompute_v95.log |
| E7 | §II.9 | 550.93057 / 555 presented as the barrier | identified as saddles of the radially restricted envelope (E1, E2, E4 qualifiers); full-field ΔF*∞ = 119.06±0.03 (F2/I1); barrier/noise ≈34 (envelope) vs ≈7.3 (full field); thin-wall factors 3.2× / 0.86× (E3) | run13/adj/a-ga10_RULING.md |
| E8 | l.950 | "This must be decided. It is not resolvable by further calculation." | overtaken; §14 gives the tested outcome (RF-4) | run13/adj/a-kb1_RULING.md RF-4 |
| E9 | l.946 | costs of (B) omit two light cones | §14 states the decisive cost (RF-3) | a-kb1 RF-3 |
| E10 | l.408 | "L/T = 3.016 against 3" | identified as $c_L^2/c_T^2$ at $|q|=0.02$ incl. $q^2$ term; $q\to0$ limit 2.99977 (RF-1) | a-kb1 RF-1 |
| E11 | l.85 / l.720 | stiffness 1.54058921 presented without provenance | equals one-mode $256A^2$ at A=0.0775753 — stated as a candidate reading, script not traced; relaxed μ=1.54465 (F2/I1), λ=1.54447 (F3/I1) (RF-2) | a-kb1 RF-2 |
| E12 | VI.5 (l.764) | quartic isotropy presented as the leading LV statement | leading LV is the isotropic cone mismatch $c_L\ne c_T$ (RF-5) | a-kb1 RF-5 |
| E13 | §III.3 | θ chosen silently in rebuild | chosen θ=π/2 presented beside the original "<1% for $a_0|k|\lesssim0.3$", range table kept; explicitly not a correction (G-C13) | G-C13 closure (Brandon 2026-11-22) |
| E14 | (record) | claim that eq.(7) prefactor is wrong by 2 | no erratum: pdftotext misread of $a_0^2$; stated in Appx A (G-C12) | G-C12 closure |
| E15 | §III.2 | "maximum exactly 32" stated, not re-derived | short proof via $\sum\cos=2[(\sum c_i)^2-\sum c_i^2]\ge-8$; kernel theorem (N7) | a-gb6 N7, a-n7b |

## Results added (with grade as adjudicated; none raised)

| result | grade | source |
|---|---|---|
| G-D3 at $L=3\pi$: P1 29/30 $D_4$ [0.833,0.994]; P2 41/50 [0.692,0.902]; P2 label not established; 42-mode competitor +7.714e-4, strict local min; P0 control 15/15 uniform; next box $5\pi$ | F2/I1 (competitor F3/I1) | run13/adj/a-gd3b_RULING.md; STATE 18:52Z |
| n²=18 shell: 312 modes = 24+96+192 (recomputed); 41 $D_4$ subsystems = 1 star + 24 of type 411×8+3221×16 + 16 of type 330×6+411×6+3221×12 (ruling); our search reproduces one system of the last type | exact (orbits); ruling count | validation/recompute_v95.py; a-gd3b_RULING.md |
| G-A4 bounded rate: 0/240 at T=50 (≤1.53%), 0/60, 0/30 at T=500 | C, F3/I1 | inventory G-A4 |
| G-A10 full-field critical droplet 119.06±0.03, $R_{eq}\approx10.465$, index 1; rate OPEN (UV divergence, ε*, n0=10 claimed only) | F2/I1 / F3/I1 parts | a-ga10_RULING.md |
| EXP-1320 odd-sector Hessian (L=2π): no negatives at 3 points; gaps 0.3423000506 / 0.4305432217 / 0.2718504312; outside-model "3 subharmonic negatives" refuted | F2/I1 | run13/adj/a-1320_RULING.md |
| Run-12 Model A drifted state is a saddle (9-fold λ≈−0.0646) | index F2/I1, instability F3/I1 | run-12 record |
| New §8 phonons: closed-form $C_{ijkl}=256A^2(\delta\delta+\delta\delta+\delta\delta)$, ρ=48A², $c_L^2/c_T^2=3$ (Cauchy relation from the 4-design); relaxed 1.731985; $K/\mu+3/2$ theorem; overdamping at γ=1.2; KK table; ξ6; MPFC 5 branches | B [MV]4D/I1; F2/I1; F3/I1 as marked | a-kb1_RULING.md; derivation re-checked in recompute_v95.py |
| New §13 reflection positivity: no Källén–Lehmann form; reflected kernel closed form and sign; $\pi r^{-3/4}$ bound; crystal lattice $F_h$ not RP in tested directions; G-A27 CLOSED-scoped | B [MV]4K/4D F1/I1; crystal F2/I1 | a-ka_RULING.md; closed form re-checked vs QUADPACK |
| §14 dimensional assignment: decision (B) + reversal rule; K-B1 fired, upheld 16:30Z; (B) dropped; (C) working, no construction; (A) not reinstated; G-A29 closed negative, G-A28 overtaken, G-A30 open | B/F2/I1 scoped | a-kb1_RULING.md; G-C8_DECISION.md |
| G-B6: C01–C23 Lean kernel theorems with C11/C17/C21/C23 conditions | B [MV]4K F1/I1 | a-gb6_RULING.md; repo verification/lean-gb6/ |
| §18 status by ToE-bar tier, T0–T7, none met | — | your_files/irh-toe-bar/IRH_TOE_BAR.md, updated per a-ka §B and a-kb1 |
| α ansatz numbers: 137.0360028219, 173.6σ from CODATA 2022 | D | recompute_v95.log |
| Lunar laser ranging $\dot G/G=(4\pm9)\times10^{-13}$/yr (G-C19 context) | literature | Williams–Turyshev–Boggs PRL 93 261101 (checked) |

New references: [46] Stefanovic–Haataja–Provatas 2006, [47] Chaikin–Lubensky 1995, [48]/[49] Osterwalder–Schrader 1973/1975, [50] Williams–Turyshev–Boggs 2004 (all checked 2026-11-25). Ref [9] (Landau 1937) dropped: it was never cited in the v94 text.

## Restructuring

- Parts I–X with Roman sub-numbering → 19 numbered sections + 3 appendices; equations numbered by section; all cross-references are `\ref`/`\eqref`.
- Version note (14-item itemize), "How to read" itemize and §IX.2 itemize → prose (§1.3, §14.1).
- All 26 `\expansion{}` boxes folded into the main derivations as step-by-step algebra.
- Claim ledger VIII.1–VIII.4 tables dropped; each status now sits with its result, and §18 gives the tier-by-tier status.
- Appendix A enumerate (20 items) → two prose paragraphs (v94 items; v95 additions).
- Epistemic labels: ALL-CAPS bold → small capitals; grades in brackets.
- Title-page Drive link box removed; repo pointer kept.
- Fonts: Noto Sans text/mono, Noto Sans Math v3.000 (OTF with MATH table, bundled in `fonts/`); Fira Math fallback configured as unneeded (no missing glyphs; `\tracinglostchars=3` makes any missing glyph a hard error).
- Sole author Brandon D. McCrary (ORCID 0009-0008-2804-7165); AI only in the closing "note on assistance".
