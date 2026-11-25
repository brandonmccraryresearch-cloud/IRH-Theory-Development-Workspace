# IRH v95 draft — VALIDATION (deepest-research gate)

**Form chosen (stated per the standing delegation):** claim-level fact-check of every new or changed statement against the adjudicated run record (rulings, gap inventory, STATE), plus independent local recomputation of every number that can be recomputed cheaply, plus a web check of every new or changed citation. Not a systematic review. All checks are by the same pipeline as the record (I1); nothing here raises a grade.

## 1. Recomputation (`validation/recompute_v95.py`, Python 3.11.16, numpy 2.4.6, scipy 1.17.1, SymPy 1.14.0, mpmath 1.4.1)
Log `validation/recompute_v95.log`: 38 PASS, FAILS none, exit 0. Covers T=192, Q=3384, S=64/141, 12/31, 496/423, 16/45, r_c, 758/6561 = 11.5531%, 756/6561, r_eff = 0.1072, one-mode $C_{ijkl}$ (768/256/256, ρ=48), isotropic tensor, $c_L^2/c_T^2=3$, relaxed ratio 1.731985, $K/\mu+3/2$ and $K=-\mu/2$, overdamping thresholds 0.15/0.26, reflected-kernel closed form vs QUADPACK QAWF at 4 points (agreement ≈2e-11), $\hat G(\pi/\alpha)<0$, $dG/ds>0$, 4.627, 4.661, 7.35, 78.5%, n²=18 shell orbits 24/96/192, existence of a rotated $D_4$ in that shell, α = 137.0360028219 at 173.6σ, 1152/192 = 6, 8 partners at 120°, penalties 0.25.

## 2. Text-level claim check (`validation/check_tex_claims.py`)
Run on the final tex: `check_tex_claims.log` — PASS 26, FAIL 0, EXIT 0. It recomputes the load-bearing numbers as they appear in the text and asserts that record-forbidden statements are absent: $c_L/c_T=\sqrt2$, "abstain", 11.85% quoted as a value, generations derived, grade A on any physical claim, Washburn, $S$ called an entropy, the old GRS DOI and EKR arXiv id in the bibliography, (B) as working reading, a factor "46×".

## 3. Planted control — CAUGHT
Planted wrong claim: "$c_L/c_T=\sqrt2$" inserted next to the relaxed ratio in §8.2 (`/tmp/planted.tex`, made by `sed`). Checker on the planted file: PASS 25, FAIL 1 — "FORBIDDEN present: cL/cT = sqrt2 (false: sqrt3)", exit 1 (`validation/planted_control.log`). The final tex does not contain it.

Earlier in this build the checker also caught real defects, which were fixed before the final run: (i) the HLRE grade definitions in Appendix C did not match HLRE v5.1 (rewritten from the skill text: Track E A–D, Track F F1–F3, I0–I4); (ii) G-A28/G-A29 labels were swapped in §14.4 (fixed against inventory l.488/495/502); (iii) the stiffness 1.54058921 had been asserted to be the one-mode value — softened to a candidate reading per RF-2 (provenance untraced); (iv) relaxed/one-mode stiffness gap corrected 0.27% → 0.26%; (v) abstract pointed grade definitions to the wrong appendix.

## 4. Claim-by-claim against the record (new or changed claims)
| claim in v95 | record | verdict |
|---|---|---|
| G-A27 CLOSED-scoped, disordered B [MV]4K/4D F1/I1, crystal F2/I1 tested points; scope wording | a-ka_RULING rows 1.1–1.6, 3, 6; wording 2a | match |
| reflected kernel formula, $(\alpha+i\beta)^2=q_0^2-|k_\perp|^2+i\sqrt r$, bound $\pi r^{-3/4}$, −1.6684 at a=8 | a-ka 1.2–1.4 (−1.668411332072964) | match + recomputed |
| K-A trigger not fired; (A) not reinstated | a-ka row 4 | match |
| K-B1 fired, upheld (B/F2/I1 scoped) 16:30Z; (B) dropped, (C) working | a-kb1; STATE 16:30Z | match |
| 4 gapless branches, 0.342300 gap, $c_T^2=5.332526$, $c_L^2=15.996363$, 1.731985, agree ≤2e-8 | a-kb1 row 3a, inventory draft l.155 | match |
| KK table values and grades | a-kb1 row 5, l.166 | match |
| ξ6,L = −81.78±0.02, ξ6,T = 27.260±0.008 | a-kb1 l.158; STATE 16:40Z | match |
| μ_relaxed 1.54465 (F2/I1), λ_relaxed 1.54447 (F3/I1), ρ 0.2896648, q→0 ratio 2.99977 | STATE 16:40Z; a-kb1 RF-1 | match |
| MPFC 5 gapless, 3 speeds, verifier only F3/I1 | a-kb1 l.87, l.117 | match |
| G-A29 closed negative; G-A28 overtaken; G-A30 open, plate-type symbol unverified | a-kb1 §7 l.155–160; inventory l.488–506 | match (after fix ii) |
| G-D3 P1 29/30, P2 41/50, competitor +7.714e-4 strict local min F3/I1, P0 15/15, next box 5π, P2 label not established | a-gd3b; STATE 18:52Z | match |
| G-A10 119.06±0.03, R≈10.465, index 1, envelope not stationary (rel. grad 0.234), rate open | a-ga10 | match |
| EXP-1320 values and refutation scope ($L=2\pi$, these points) | a-1320_RULING | match |
| G-B6 C01–C23 and conditions on C11/C17/C21/C23 | a-gb6 l.56, 71–76, 133–137 | match |
| bracket max 32 proof and kernel status | a-gb6 l.97 (argument); N7 closed per a-n7b | match |
| HLRE definitions | hlre-v5-1 SKILL.md l.76, 111, 113 | match (after fix i) |
| ToE tiers: none met | IRH_TOE_BAR.md table + a-ka §B, a-kb1 T4.2 | match; T0.1 updated to reflect K-B1 |

## 5. Citations checked (browser_search, 2026-11-25)
GRS PLB 60 (1976) 177 doi …90417-2; Osterwalder–Schrader CMP 31 (1973) 83–112 doi 10.1007/BF01645738 and CMP 42 (1975) 281–305 doi 10.1007/BF01608978; Stefanovic–Haataja–Provatas PRL 96 225504; Williams–Turyshev–Boggs PRL 93 261101 (gives $(4\pm9)\times10^{-13}$/yr); Chaikin–Lubensky CUP 1995; arXiv:math/0607446 = Cohn–Kumar; Lean CADE-25 pp. 378–388 doi …_26; Mathlib CPP 2020 pp. 367–381. Biskupek et al. arXiv:2012.12032 was NOT verified and is not cited.

## 6. Build gate
XeTeX 3.141592653-2.6-0.999998 (TeX Live 2026) in env `jacobian-conjecture-2d`: three passes exit 0; 0 errors, 0 undefined references/citations, 0 "Missing character" with `\tracinglostchars=3` (hard error on any lost glyph); 1 overfull hbox of 0.54 pt. Fonts embedded: NotoSans Regular/Italic/Bold, NotoSansMono, NotoSansMath (v3.000, MATH table). 43 pages rendered with pdftoppm and inspected (contact sheets): no clipped tables, figures placed, equations render in Noto Sans Math. Final log `validation/xelatex_final_build.log`.

## 7. Not verified here (stated as such in the text or carried at record grade)
G-A12 S2 certification (still running on the VM, not adjudicated; S2 stays F3); G-E5 p=5 (Jacobian-side, pending ruling; not in the paper's physics); G-A30 plate-type argument; cubic L–T–T coupling value; n0=10 in infinite volume; the ruling's 41-subsystem count (only existence recomputed); RF-2 provenance of 1.54058921; dislocation edge-leg rerun (C5).

## 8. Figure pass (2026-11-25, evening CST)
- Build: three xelatex passes exit 0; 0 errors, 0 undefined references, 0 "Missing character", 0 overfull, 10 underfull (prose-pass count; none in captions); 51 pages. Log `validation/xelatex_figs_build.log`.
- Pages rendered with pdftoppm (80 dpi contact sheets) and inspected: printed pp. 5–7 (notation and Table 1), 8, 9, 10, 13–27 (fix ii on p. 19, fix i on p. 24), 29–35. Every figure placed near its first reference, labels legible, no clipping; Table 1 still directly follows §1.4.
- `recompute_v95.py` 38 PASS exit 0; `check_tex_claims.py` PASS 54 FAIL 0 exit 0; planted $c_L/c_T=\sqrt2$ caught (exit 1); planted old-wording restorations for both fixes caught (exit 1 each).
- Figure checks (figure source tree `paper-figures-2026-11-25/irh/`): `check_figs.py` on the shipped figures 67 PASS 0 FAIL exit 0; eight planted variants (dropped root, fibres of 8, rotated mode, extra band row, $\sqrt2$ ratio, dropped Gram pair, envelope barrier, negative odd eigenvalue) each rejected, exit 1. Printed size at `\textwidth`: smallest label 8.02–8.20 pt in all eight. Colour vision (colorspacious 1.1.2, Machado deuteranopia/protanopia/tritanopia at severity 100 and greyscale CAM02-UCS $J'$; threshold $\Delta E'=10$): 305 category pairs, 0 FAIL, 8 WARN, each WARN separated by a second channel (bar position and label in Figure 1(c) and Figure 4(d); six marker shapes in Figure 9). The first run had one FAIL (band map hex6/fcc12 in greyscale, $\Delta E'=3.4$), fixed by changing fcc12 to vermillion ($\Delta E'=11.8$).

## 9. Figure grades against the adjudicated record
| figure | grade in caption | source | result |
|---|---|---|---|
| 5 band | F3/I1 | draft (5.3) and run 12 G-A19 | match |
| 4 $L=3\pi$ shells | census, $312$: F2/I1 (recomputed); degeneracy F2/I1 at $N=32$; fraction $29/30$ F2/I1 | `swarm/run13/adj/a-gd3b_RULING.md` R1, R3, R5, R10 | match (CAPTIONS.md draft said "exact" and gave one $N=24$ offset; corrected) |
| 6 Hessian | F2/I1, three points, finite box | draft §6.2; run 13 EXP-1320 | match |
| 7 droplet | F2/I1; index certified at $12\pi$, $16\pi$ only | draft §7.2 (G-A10) | match |
| 8 field | phonon values F2/I1; rendering no claim | `run13/adj/a-kb1_RULING.md` items 1, 3c | match |
| 9 phonons | relaxed F2/I1; one-mode $\sqrt3$ B, [MV]4D/I1; overdamped below $0.15$/$0.26$ at $\gamma=1.2$ | a-kb1 items 3c, 4; ruling l.155 | match; scope $w_6=0$, zero damping stated |
| 1, 14 | exact, no grade | — | — |

Not verified here: the main text's statement in §4.6 that the rotated states are degenerate "to $3\times10^{-16}$" is, per a-gd3b R10, an $N=32$ statement ($N=24$ breaks it at up to $\sim10^{-9}$); the text does not say "at $N=32$". Left unchanged in this pass (not one of the two assigned fixes); Figure 4's caption carries the scope. Item 7's "41-subsystem count (only existence recomputed)" is now recomputed in integer arithmetic by the figure script (`fig06` facts: $1+24+16=41$).

## §4.6 scope fix (coordinator, 2026-11-25)
- xelatex three passes exit 0; 0 missing characters, 0 undefined, 0 overfull; 51 pages. recompute_v95.py exit 0; check_tex_claims.py PASS 54 FAIL 0 exit 0. PDF text confirms the new sentence.
