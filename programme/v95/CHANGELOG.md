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

## Prose second pass (2026-11-25, checklist `paper-figures-2026-11-25/PROSE_CHECKLIST.md`)

Style pass only. No number, grade, status, citation or claim was changed; no figure added; every existing `\label`/`\ref` kept (15 equation labels plus `sec:notation`, `tab:notation` added). Build 44 pp. (was 43; the notation table adds a page), 0 errors, 0 undefined references, 0 missing glyphs, 0 overfull boxes.

- Notation: new §1.4 with Table 1 (symbols used across sections, where each is defined; caption lists the local second meanings of $N$, $\phi$, $\mu^2$, $J$, $\theta$, $\lambda$). Gap labels (G-…) and run numbers explained at first use in §1.3. $M^*$ defined at first use (§1.1); $\tau=T/N^{3/2}$, $q_4=Q/N^2$ defined in the abstract; $W(F_4)$ identified at its first use (§6.2).
- Symbol clashes removed without changing values: simulation time written $t$ (not $T$, the triad count) at $t=50$, $t=500$, $t\ge500$; Lennard-Jones temperature written $T^*$; the principal-symbol variable in §14.4 written $\omega$ (was $\tau$, the triad density).
- Sentence starting with a symbol (§3.5) rewritten; "trivially" (§3.3) replaced by the reason.
- Strategy sentences added before the first-order-point elimination (§4.2), the baseline-tension expansion (§5.1), the speed-ratio argument (§8.3), the stability bound (§9.2), the $2T$ representation count (§11.4) and the residue evaluation (§13.2).
- Steps shown: why the shell quadratic term reduces to $\tfrac r2\langle\psi^2\rangle$ (§4.1); the coefficients of $\langle\varphi^2\rangle,\langle\varphi^3\rangle,\langle\varphi^4\rangle$ before collecting (§5.1); $u_{\rm eff}=u-3v\bar\psi$ before its value (§6.1); why the Källén–Lehmann form is non-increasing (§13.2); $I_{\rm grad},I_{\rm pot},I_{\rm curv}$ defined (§10).
- Key displays numbered (were unnumbered): $\Psi$, shell free energy, excess free energy in $\varphi$, $r_{\rm eff}$ at the operating point, $f_{\rm el}$, phonon equation of motion, site action, bracket maximum $32$, worst-mode value, envelope equation, Derrick scaling, OS condition, $G(s)$, $\hat G$ integral. Equation references now carry a noun phrase ("the stability bound (9.6)", "the free energy (2.1)").
- Number multiset (digit sequences of old vs new tex, labels/refs excluded): nothing removed except one literal "$<0$" restated in words ("makes the left side of (13.1) negative"); additions are only exponents/subscripts in the new definitions and shown steps, two gap-label examples, and the notation table's symbols and column widths.
- Validation rerun: `recompute_v95_prose2.log` 38 PASS exit 0; `check_tex_claims_prose2.log` PASS 26 FAIL 0 exit 0; planted control (`c_L/c_T=\sqrt2`) caught, PASS 25 FAIL 1 exit 1 (`planted_control_prose2.log`). Build log `validation/xelatex_prose2_build.log`. (The `*.log` files are git-ignored, as for the first pass; they sit in the local worktree and in the coordinator's copy.) Heuristic script `validation/ai_tell_heuristics.py`.

## Record-computed figures and two content fixes (2026-11-25, evening CST)

Build 51 pp. (was 44), 0 errors, 0 undefined references, 0 missing glyphs, 0 overfull boxes (10 underfull, the same count as the prose pass; none in a figure caption). Notation (§1.4, p. 6) and Table 1 (p. 7) stay where they were; no figure floats ahead of them.

Figures (final numbers and printed pages). New figures are vector PDFs drawn at `\textwidth`, smallest printed label 8.02–8.20 pt:

| no. | label | file | page | status |
|---|---|---|---|---|
| 1 | `fig:d4cell` | `figs/fig01_d4_24cell.pdf` | 9 | added (§3.1) |
| 2 | `fig:moment` | `figs/fig02.png` | 10 | kept |
| 3 | `fig:causal` | `figs/fig03.png` | 14 | kept; text reference added |
| 4 | `fig:rotd4` | `figs/fig06_L3pi_shells.pdf` | 16 | added (§4.6) |
| 5 | `fig:band` | `figs/fig04_phase_band.pdf` | 18 | replaces old `fig:phase` (`figs/fig04.png`) |
| 6 | `fig:hessian` | `figs/fig08_hessian_ladder.pdf` | 21 | added (§6.2) |
| 7 | `fig:droplet` | `figs/fig07_nucleation_saddle.pdf` | 23 | added (§7.2) |
| 8 | `fig:d4field` | `figs/fig03_d4_field_slices.pdf` | 26 | added (§8.2) |
| 9 | `fig:phonons` | `figs/fig05_phonons.pdf` | 27 | added (§8.2) |
| 10 | `fig:cfl` | `figs/fig05.png` | 30 | kept |
| 11 | `fig:nr` | `figs/fig06.png` | 31 | kept; text reference added |
| 12 | `fig:scaling` | `figs/fig07.png` | 32 | kept |
| 13 | `fig:branch` | `figs/fig08.png` | 33 | kept |
| 14 | `fig:2thopf` | `figs/fig02_2T_hopf.pdf` | 35 | added (§11.3) |
| 15 | `fig:chain` | `figs/fig09.png` | 35 | kept; text reference added |

- Replaced: the old phase diagram `figs/fig04.png` (v94 legacy, arrived with commit 90b692e; no plotting script in the repo). It showed competitors D4 / hexagonal (6) / subset (12) / lamellar (2) / disordered on $\bar\psi\in[-0.4,0.4]$, including a lamellar region at $\bar\psi\gtrsim0.12$ that the run-12 record (G-A19, $\bar\psi\in[-0.38,0.08]$ computed) never computed, and it cannot be traced to the $758/6561$ data. The new Figure 5 is drawn cell by cell from that record, marks the uncomputed strips, and shows the record's competitor set (hex6, fcc12). The old file stays in `figs/` unreferenced (as do `fig01.png` and `fig10.png`, unreferenced since v95's first build).
- Every figure is now referred to from the text with a sentence saying what to look at; `fig:causal`, `fig:nr` and `fig:chain` had no `\ref` before this pass.
- Captions: human prose, no bold, math in `$...$`, scope and grade stated, grades copied from the record and not raised (sources in VALIDATION.md §9). Caption changes against the figure builder's `CAPTIONS.md`: Figure 4 no longer calls the census and $312$ count "exact" as a grade (they are F2/I1 in the record, a-gd3b R1/R3, recomputed here in integer arithmetic); it gives both $N=24$ offsets ($-5.6\times10^{-13}$ and $+6.7\times10^{-11}$, aliasing at $N=24$) and scopes the degeneracy grade to $N=32$ (a-gd3b R10); the selection fraction is pointed to §4.6 since it is not plotted. Figures 5, 8 and 9 state $w_6=0$; Figure 9 states zero damping as its scope; Figure 1 states the triad count $24\cdot8=192$ from the $120^\circ$ partners explicitly (the grey lines are the $60^\circ$ pairs).
- Figure fixes before insertion (in the figure source tree): all eight redrawn at width 6.3 in with an 8-pt printed-size floor; fig04 fcc12 colour changed to vermillion #D55E00 after the colour-vision check found hex6/fcc12 indistinguishable in greyscale ($\Delta E'=3.4$, now $11.8$); panel titles and legends shortened in figs 3, 6, 7, 8 to meet the floor.
- Edit script: `validation/insert_figures_2026-11-25.py` (exact-match anchors; reapplied to the HEAD 3ab787d text it reproduces this tex except for the three added references to existing figures).

Content fixes (record-checked before editing):

1. §7.2 thin-wall factors. Old: "Against the envelope saddle these differ by a factor of about $15$; …" and "The amplitude-equation barrier is about $15$ times the thin-wall value; the full-field barrier is within a factor of about $3.2$." New: "Against the envelope saddle they differ by factors of $550.93/36.95\approx14.9$ and $550.93/138.12\approx4.0$; …" and "The amplitude-equation barrier is about $15$ times the first thin-wall estimate and about $4.0$ times the second; the full-field barrier is about $3.2$ times the first and $0.86$ times the second." Record: v94 `IRH_v94.tex` l.938 (thin-wall transfers $36.95$ / $138.12$ against the saddle $550.93$; v94 states only the $14.9\times$ mismatch, which is the first route). Arithmetic: $550.93057/36.95=14.910$, $550.93057/138.12=3.989$.
2. §5.3 sextic narrowing. Old: "reduces the one-mode band from $11.60\%$ at $w_6=0$ to $8.36\%$ at $w_6=0.2$." New: "reduces the one-mode band, computed on a $161\times161$ grid of the same window with the competitors hex6, fcc12, sq4 and sq8, from $11.60\%$ at $w_6=0$ to $8.36\%$ at $w_6=0.2$. The value $11.60\%$ is that one-mode $161\times161$ number of Section 5; it is not the canonical full-field value $11.5531\%$ of (5.3) on the $81\times81$ grid, nor the one-mode value $11.5226\%$ on that grid." Record: WS-A `programme/workstreams/ws-a-core-computations/task3_report.md` l.7–9 and table l.43 (W1, $161\times161$, family {hex6, fcc12, sq4, sq8}: $11.60\%\to8.36\%$); run 12 `w-ga19/G-A19.md` l.26, 68, 70 and `v-ga19/OUTPUTS.md` l.24, 29 ($11.5531\%$ full field $81\times81$; one-mode $81\times81$ $11.5226\%$; one-mode W1 $161\times161$ recomputed $11.5968\%$); v94 l.368.

Bibliography keys versus printed numbers. This CHANGELOG (and the earlier sections above) name references by printed number where written as [n], but the source uses keys `ref1`…`ref50` with `ref9` (Landau 1937) dropped, so printed numbers run one below the key from `ref10` on: `ref1`–`ref8` print as [1]–[8]; `ref10`→[9], `ref11`→[10], …, `refN`→[N−1], …, `ref50`→[49] (from `IRH_v95_draft.aux`, 49 `\bibcite` entries). The "New references" line of the first pass names keys: Stefanovic–Haataja–Provatas is `ref46`, printed [45]; Chaikin–Lubensky `ref47`, [46]; Osterwalder–Schrader `ref48`/`ref49`, [47]/[48]; Williams–Turyshev–Boggs `ref50`, [49].

Validation rerun: `recompute_v95_figs.log` 38 PASS, exit 0; `check_tex_claims_figs.log` PASS 54 FAIL 0, exit 0 (28 new assertions: both fixes, every figure referenced, figure grades); planted control `c_L/c_T=\sqrt2` caught (PASS 53 FAIL 1, exit 1, `planted_control_figs.log`); two new plants restoring each old wording caught (exit 1 each, `planted_factor15_figs.log`, `planted_1160_figs.log`); the HEAD 3ab787d text fails 14 of the new assertions, as it should. `ai_tell_figs.log`: same counts as the prose pass (only item 9, four tricolon paragraphs, all previously read and kept). Build log `validation/xelatex_figs_build.log`.
