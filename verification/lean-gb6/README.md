# G-B6 — Lean kernel sources for the WS-C / v94 shell combinatorics (IRH run 13, EXP-1304)

This folder records the run-13 Lean 4 kernel verification of the 23 Lean-able finite-combinatorics and $a_0$/CFL claims (C01–C23) behind inventory entry G-B6. Adjudicator ruling: `a-gb6` (sha256 `ecb6b4db2333edf1ef87f9d76c6791d822e1959bf2f1e2641a7c331a074fec4e`), verdict **G-B6: CLOSED-scoped to C01–C23**.

This is a copy-and-document commit. Every source file is copied byte-for-byte from the author (w-gb6) or verifier (v-gb6) working directories, and each was matched against that agent's recorded SHA256SUMS before copying. Nothing here was rebuilt for this commit. No `.olean` files, build products or logs are committed.

**All verification was done by AI agents of one model family.** The author, verifier and adjudicator are the same family and the kernel route used the same Lean binary, so independence is **I1** throughout. No authorized external agent took part.

## Toolchain

- Lean: version 4.34.0, commit `293d5d0c0c3f3dded4688b3ccd6a33939ac5102b` (Release). `lean` binary sha256 `e8baaa71855a616dc351028f3ad2200051b0671f423a1696a100e809302d5550`; `leanchecker` sha256 `ccef1bfe9bfeecea65137d94a69033c1a89f360711f50fa3178e7ba3e696fcbe`.
- Mathlib rev `5ed2965256430c3649e86755f9576b54eca72435`, prebuilt oleans (from the `theorem-r-campaign/o5` tree), used **read-only via `LEAN_PATH`**. No lakefile is provided here, and no `lake` was run in the Mathlib tree.

## How it was built (on the run-13 VM)

- Each module was compiled with plain `lean` (one process at a time, `LEAN_NUM_THREADS=4`, 16 GB RSS watchdog). `LEAN_PATH` = the Mathlib package lib dirs plus the folder holding the earlier GB6 oleans.
- Finite facts use `decide +kernel` only. There is no `native_decide`, no `sorry`, no `ofReduceBool` and no `trustCompiler`. `set_option maxHeartbeats 4000000` appears in the literal-table files; it affects only the elaborator, not the kernel check.
- Every `#print axioms` output is $\subseteq$ {`propext`, `Classical.choice`, `Quot.sound`}. That is 143 axiom lines over the 14 production modules plus 51 in the verifier audit file, with 0 outside the set.
- The verifier (v-gb6) independently rebuilt all 14 production modules fresh (14/14 EXIT=0) and replayed 15/15 modules (the 14 plus `GB6V_audit`) with `leanchecker` (all EXIT=0, peaks tracking the build peaks). `leanchecker` ran without `--fresh`, so imported Mathlib declarations are trusted as loaded.

Build order (each file only imports files above it, plus Mathlib):

1. `GB6Core`
2. `GB6Counts`, `GB6CountsA4Q`, `GB6CountsD4Q`, `GB6Grid`, `GB6HILit`, `GB6HJLit`
3. `GB6Real` (imports Counts, CountsD4Q, CountsA4Q)
4. `GB6Analytic` (imports Counts, Grid)
5. `GB6H` → `GB6HI` → `GB6HI2` (imports HILit) → `GB6HJ` (imports HJLit) → `GB6HJ6`
6. Controls: `GB6CtrlFailCounts`, `GB6CtrlFailHeavy1–3` (Core), `GB6CtrlFailReal` (Real), `GB6CtrlNeg` (Real, Grid), `GB6CtrlFailH` (HJ)
7. Verifier: `verifier/GB6V_audit`, `verifier/GB6V_ctrl_fail`, `verifier/GB6V_ctrl_neg` (import production modules up to `GB6HJ6`)

Peak RSS reached about 12.8 GB (`GB6CountsD4Q`), so budget at least 16 GB.

## Layout

| path | what | provenance |
|---|---|---|
| `GB6Core.lean` … `GB6HJ6.lean` (14 files) | production sources | w-gb6 (author) |
| `GB6CtrlFail*.lean` (6), `GB6CtrlNeg.lean` | must-fail perturbed controls and must-compile negations | w-gb6 |
| `verifier/GB6V_audit.lean` | verifier audit, including the C11 dual-shell supplement `GB6V.V11_dual_*`, the plant check `RG_Q`, `V_dual_T` and `V18_nonvacuous` | **v-gb6 (verifier)**, copied verbatim |
| `verifier/GB6V_ctrl_fail.lean`, `verifier/GB6V_ctrl_neg.lean` | the verifier's own 10 must-fail controls (including the plant) and 7 must-compile negations | **v-gb6**, copied verbatim |
| `generators/genI.py`, `generators/genJ.py` | generators for the literal tables in `GB6HILit` / `GB6HJLit` | w-gb6 |
| `crosscheck/xcheck_counts.py` | author's Python enumeration (nested loops, exact `Fraction`) | w-gb6 |
| `crosscheck/v_enum.py` | verifier's independent enumeration (Counter convolution; does not import author code) | v-gb6 |
| `MANIFEST.sha256` | sha256 of every other file in this folder | — |

> **Generators: untrusted, output kernel-checked.** `genI.py` and `genJ.py` only emit certificate tables. They are not part of the trusted base: every emitted table is checked by kernel evaluation (`C17I_D2`, `C17J_B*`, `C17J_P*`). `genJ.py` `exec`s `genI.py` from the working directory, so run it from `generators/`.

## Claim-to-theorem map (C01–C23)

The verbatim v94 / WS-C quotes with file:line (repo 782a555) are in the frozen claim ADDENDUM (sha256 `41d3453cdf933318a8b66003f8904d682d87f2ed0de1ce355cc013f8d607311e`), countersigned before any Lean ran. T and Q below are ordered counts.

| Claim | Statement as formalized | Lean theorem(s) (file) |
|---|---|---|
| C01 | $D_4$ = all of $\mathbb Z^4$ with $\lvert v\rvert^2=2$; $N=24$, $T=192$, $Q=3384$ | `C01_D4_N`, `C01_D4_T`, `C01_D4_form` (GB6Counts); `C01_D4_Q` (GB6CountsD4Q); `C01_D4_complete` (GB6Analytic) |
| C02 | $\tau^2=8/3$, $q_4=47/8$, $S=64/141$, $\tau=T/N^{3/2}=4/\sqrt6$ | `C02_D4_tau2`, `C02_D4_q4`, `C02_D4_S`, `C02_D4_tau` (GB6Real) |
| C03 | $A_4$ roots $(20,120,1860)$; $\tau^2=9/5$, $q_4=93/20$, $S=12/31$ | `C03_A4r_N/T/form` (GB6Counts), `C03_A4r_Q` (GB6CountsA4Q), `C03_tau2/q4/S` (GB6Real), `C03_A4r_complete` |
| C04 | BCC row $(12,48,540)$; $4/3$, $15/4$, $16/45$; $\tau=2/\sqrt3$ | `C04_BCC_N/T/Q` (GB6Counts), `C04_tau2/q4/S/tau` (GB6Real), `C04_BCC_complete` |
| C05 | FCC $(8,0,216)$, $q_4=27/8$; SC $(6,0,90)$, $q_4=5/2$ | `C05_FCC_N/T/Q`, `C05_SC_N/T/Q`, `C05_FCC_q4/S`, `C05_SC_q4/S`, `C05_*_complete` |
| C06 | $\mathbb Z^4$ $(8,0,168)$, $q_4=21/8$; $A_4$ row $(10,0,270)$, $q_4=27/10$ | `C06_Z4_N/T/Q`, `C06_A4sm_N/T/Q`, `C06_A4sm_shell`, `C06_Z4_q4/S`, `C06_A4_q4/S`, `C06_Z4_complete` |
| C07 | $S_{D_4}/S_{A_4^*}=496/423$, margin $73/423$, $S_{D_4}>S_{A_4^*},S_{BCC}$ | `C07_ratio`, `C07_margin`, `C07_D4_wins` |
| C08 | $\tau_{D_4}/\tau_{BCC}=\sqrt2$ | `C08_tau_ratio` |
| C09 | printed decimals ($\lvert 64/141-0.453901\rvert<5\cdot10^{-7}$, …, $73/423=17.26\%$, $2/\sqrt3\approx1.1547$), each to half a unit in the last printed digit | `C09_decimals` |
| C10 | each root has exactly 8 partners at dot $-1$; triads = partner pairs; $24\cdot8=192$ | `C10_norm2`, `C10_partners`, `C10_triad_iff`, `C10_T_eq_partner_pairs` |
| C11 | root shell: distinct-root dots in $\{-2,-1,0,1\}$, all attained; dual shell: norm 4, distinct dots in $\{-4,-2,0,2\}$, all attained (same cosine set $\{-1,-\tfrac12,0,\tfrac12\}$) | `C11_fingerprint_range`, `C11_fingerprint_attained` (author); **`GB6V.V11_dual_norm`, `V11_dual_range`, `V11_dual_attained`, `V11_dual_nodup`** (verifier/GB6V_audit) |
| C12 | $\sum_\alpha(k\cdot\alpha)^2=12\lvert k\rvert^2$, $\sum_\alpha(k\cdot\alpha)^4=12\lvert k\rvert^4$ for all $k\in\mathbb R^4$ | `C12_iso2`, `C12_iso4` (via `D4_eq_lit`) |
| C13 | scaled shell $(\pm2,\pm2,0,0)$: 24 modes, $\lvert k\rvert^2=8$, $T=192$ | `C13_D4s_N`, `C13_D4s_form`, `C13_D4s_T`, `C13_D4s_complete` |
| C14 | full integer shell $\lvert k\rvert^2=7$: 64 modes (completeness proved), $T=0$; penalties $0.25=0.25$; $64/24=8/3\approx2.7$ | `C14_C7_N/T/form`, `C14_C7_complete`, `C14_penalties` |
| C15 | 32 unordered zero-sum triads, $192=6\cdot32$ | `C15_unordered`, `C15_ordered_vs_unordered` |
| C16 | $\#\{n\in(\mathbb Z/16)^4: k\cdot n\equiv0\ (16)\ \forall k\in D_{4s}\}=32$; $\Psi(2\pi n/16)=24$ iff $n$ is such a point; $\Psi\le24$ everywhere | `C16_grid_count`, `C16_grid_size` (GB6Grid); `C16_Psi_max_iff`, `C16_Psi_max_count` (GB6Analytic) |
| C17 | $H=911040$, the number of ordered zero-sum 6-tuples of $D_4$ roots | `C17_H` (GB6HJ6), via `cntH_eq`, `cntH_table` (GB6H), `key`, `cntH_link`, `cntH_tableI` (GB6HI), `C17I_D2` (GB6HI2), `WI_split`, `C17J_B0..B10`, `C17J_D3` (GB6HJ), `C17J_P0..P10` (GB6HJ6) |
| C18 | $F=0$, $F'=0$, $B\ne0$ give $B^*=2u\tau/(3vq_4)$ and $r_c=\tfrac29u^2\tau^2/(vq_4)$; converse; $r_c\propto S$ (hypotheses $v,q_4\ne0$) | `C18_Bstar_rc`, `C18_converse`, `C18_rc_prop_S`; non-vacuity witness `GB6V.V18_nonvacuous` |
| C19 | one-mode values: $r_{eff}=0.1072$, $u_{eff}=1.54$, $A^*$, $F(A^*)$, edge $r_c\approx0.2691$, $\lvert\delta\rvert\le0.4024$, detuned case at $q_0^2=7.5$ | `C19_reff`, `C19_reff_psi0`, `C19_disc`, `C19_Astar`, `C19_Fexc`, `C19_edge`, `C19_detuned` |
| C20 | $a_0=2\pi/\sqrt8\approx2.221441$; $dt_{max}=(\sqrt3/2)a_0\approx1.923825$ ($c=1$); ratios $48\times$, $385\times$, $96\times$ | `C20_a0_dt` |
| C21 | l.505 algebra with bracket $=32$ as a hypothesis: $\sin^2=\tfrac43(\Delta t\,c/a_0)^2$; values $4/3$, $16\pi^2/3\approx52.6$, $1$, $2/\sqrt3$ | `C21_prefactor`, `C21_sin2`, `C21_values` |
| C22 | $25^4=390625$ | `C22_grid25` |
| C23 | $\Psi$ test points $24$ / $-8$ / $-8$ | `C23_P4_shell`, `C23_P4_complete`, `C23_lattice_point`, `C23_Z4_point`, `C23_deep_hole`, `C23_points` (GB6Analytic) |

## Condition labels (from the a-gb6 ruling)

- **C11** — closed via the verifier's supplement `GB6V.V11_dual_*` (verifier-authored). The author file alone covers only the root half and is PARTIAL. The identification of `P4 := shellOf 4 2 4` with $2\cdot\min(D_4^*)$ is checked by hand and in Python, not proved in Lean. "$D_4$ is isodual" is cited, not formalized.
- **C17** — holds under the **D-H reading**: $H$ is the number of ordered zero-sum 6-tuples of roots. The definition of $H$ is not printed in the source. The printed $911040$ is reproduced exactly, which supports the reading but does not prove it is the source's definition.
- **C21** — **CONDITIONAL** on (i) the bracket maximum $=32$ (hypothesis `hbr`, carried, see N7) and (ii) the l.505 reading of the eq. (7) prefactor $\Delta t^2\,2J/(4Ma_0^2)$, which is carried and not re-derived.
- **C23** — under an **unprinted convention**: $D_4=\{y\in\mathbb Z^4:\sum y\ \text{even}\}$, the shell is $\min(D_4^*)$, $\Psi=\sum\cos(2\pi g\cdot x)$, encoded as $h=2g$ (24 vectors, $\lvert h\rvert^2=4$, list proved complete) with $x=y/2$. "Global maximum, unique" and the 0.1 % clause are not covered (N1).
- **C19** — two minor non-load-bearing items are unformalized: the edge equivalence is proved as two facts rather than one theorem, and the task2 "small root unstable, $F>0$" remark is not formalized.

## Not covered: N1–N9

| ID | Claim | Status |
|---|---|---|
| N1 | "no other point within 0.1 % of the max" | not Lean-able (float scan); the exact maximum set is proved in C16 |
| N2 | 400-direction spread $3\cdot10^{-16}$ | not Lean-able (float measurement) |
| N3 | band 11.85 % / 11.90 % / 8.47 % | not Lean-able (simulation) |
| N4 | power shares | not Lean-able (simulation) |
| N5 | relaxed $F/V$, 1.24 % lowering | not Lean-able (PDE relaxation) |
| N6 | WS-C C1.1–C1.3, C1.5, C1.6, C2.1–C2.4, P1–P5 | not Lean-able (simulation) |
| N7 | "maximum exactly 32" (l.505 bracket) | **Lean-able, not attempted, OPEN.** Next attack: a Lean theorem $\forall k\in\mathbb R^4,\ \sum_\alpha(1-\cos(k\cdot\alpha))\le32$ plus attainment at $k=(0,0,\pi,\pi)$; it would remove condition (i) of C21. The paper argument $\sum_\alpha\cos(k\cdot\alpha)=2[(\sum c_i)^2-\sum c_i^2]\ge-8$ is UNVERIFIED. |
| N8 | Weyl / $W(F_4)$ orders | **out of scope** for EXP-1304 (Lean-able in principle) |
| N9 | C1.4 "ontology dissolves circularity" | not Lean-able (interpretive) |

## Grade

Every claim C01–C23: **B [MV]4K F1/I1** (HLRE v5.1 with the 2026-11-12 amendments, UM-1 v3.1), with the condition labels above. This commit does not change any grade.

- Evidence: a kernel theorem per claim; a fresh rebuild and `leanchecker` replay by a separate agent; a statement audit against the printed text; and, for counts, two code-independent Python enumerations that agree.
- Controls: the author's 40/40 perturbed statements fail and 29/29 negations compile; the verifier's 10/10 must-fail controls (including a planted false value, $Q=3348$, which was caught) fail and 7/7 negations compile. Recorded shortfall: there is no dedicated perturbed control for the C16 analytic part, C23, or the C11 dual supplement. This is a follow-up and does not lower the grade.
- **Independence I1:** all verification was artificial, by AI agents of the same model family, using the same Lean binary. Nothing reaches I2.

No printed value was found false, and there is no erratum.

## Superseded attempts (not committed; listed by hash only)

| source | source sha256 | log(s) | log sha256 | outcome |
|---|---|---|---|---|
| `GB6H6.lean` | `d80145a3f88a8cd52d23ccdb8b14b004185ccacae9c938948289da87ed33d4ac` | `GB6H6_h2.log` | `bdbdc8da7caf2e322f3fda645d4e72f0157f62ad86423e153b245ea2f6978e33` | EXIT=143 (16 GB watchdog) |
| `GB6HI3.lean` | `1078b18f11b52201dcc9f267825b581b6a4c48947106a412fd9f1c783fc29534` | `GB6HI3_h4.log` | `9873348a94dafce8205cf1c2f1e3e813a28eeecd83236f903f5f1f86e5cb8348` | EXIT=1 (kernel deep recursion) |
| | | `GB6HI3_h5.log` | `ed0b901ef023b0104ff2891492583bd98e6ad0d02d3063946f3834669a92f922` | EXIT=143 (watchdog) |
| `GB6HI6.lean` | `eb6c2223f895ee5554846d717de5ddd94058c378356f59561488e7ffd9298f17` | none in the record | — | imports GB6HI3; never built |
| `GB6HLit.lean` | `0f06459555264cc8be62de26d1448f30c7b88b56c26c5b6f2525d625a8852fb7` | `GB6HLit_h1.log` | `044bf9d447912df672636acbc2e8d333337204ea4d485f061476fe343097f98f` | EXIT=1 (heartbeat timeout) |
| | | `GB6HLit_h2.log` | `b6ff2cc38ed56e9832e96e09358f56bf201cd54865f6104d1c8acd588d7d689b` | EXIT=0, but its only consumer GB6H6 failed; route superseded |
| `T0_perf.lean` | `0227f4a068d4b64f9080448c8d80465e4b56c4f87733f4e4205e5f0ea4282bdc` | `T0_perf.log` | `e21e1850e59b52d2756e8ede47088d3d16a3174fc74c457b0e338acb522d7483` | performance probe |
| | | `T0_perf_a3.log` | `2c649bb3774150ea058080e9b2d34c8bfc9fbbf78e10995dbafec774179a9ac1` | performance probe |
| `gen_htables.py` (generator for GB6HLit) | `33c70de16c9974703c323810df24194565d2e45b56137f75876e5ca8fd386da0` | — | — | superseded by genI/genJ |

Failed earlier attempts of committed modules (also superseded): `GB6HI_h3.log` `e8629d24d2902d306d21b5593506577f30b57e64c06ee71f3f432d51cf65ffe8` (EXIT=1, heartbeat timeout), `GB6Analytic_a1.log` `48e14188e45b0d5a084f130ed9af4b0fa4772d9803815e3c0416b2be4f7c5431` (EXIT=1, linarith), `GB6CtrlNeg_k1.log` `05bb885bd982a44008983ef0168031592c74e6757cb4a8a8adbb95d5323a9a6d` (EXIT=1, "No goals"). The first `GB6HJ` attempt's logs were overwritten under the same tag (deviation D1); the surviving `_j1` logs are the successful run, and the verifier rebuilt those modules independently.

Successful production build logs (not committed): `GB6Core_c3` `172b599d5b518ba9eedca933f92e973205c7979afb752f3d8fc231b1918a37ea`, `GB6Counts_c3` `e73642443577607447e6a10a615442b848f7abd7990e7dd8d356e2ec5ac185d2`, `GB6CountsA4Q_c3` `957bc59c4c20d0b3670d148679dcdcca0995328be4c400ccf0d993f18f196db7`, `GB6CountsD4Q_c3` `a78f1fc5a05f8d0daf8606fe8eb09ca8eb4cf03192cfd60b609f3114f73d694d`, `GB6Grid_c3` `7a7b66006cd71bd20b72a5cee9ed91fa6058cbe2b6fdc6097bdbccb651228b4d`, `GB6Real_r1` `bc590131d70695fd075dcbec616a2aed3206a58c795197a2cabc41fccbbfa210`, `GB6Analytic_a2` `3c4d338a1541fbecd088b41c787ba6f2f6764c1e722ecbbf3dcb31b17b2ffa0c`, `GB6H_h1` `db58b532b30525771909ee6f5ab5e2153367352c0e04621236bf2cc3db0e5735`, `GB6HI_h4` `5d3c2e4fa67f6bd21a20a47018854bd8dd5bf20b089099611b3358274a728f6f`, `GB6HILit_h4` `35e0f2759aa8ebf564679ea8130a3b82523a40c706abeb1ca64a18cef01deb62`, `GB6HI2_h4` `a083cf31923fffd443f414f2f8e71b30a494556bf7a83b0653422450fe71873a`, `GB6HJLit_j1` `1752142846dcd596aa7ad75c4b1e4efc36fd31261f2752efb458277fa2553ee4`, `GB6HJ_j1` `ddc57fff55b29c58a9d97c4d9a0a5b1f1320469b3c4eba2e18b9bb9e38520f0d`, `GB6HJ6_j1` `1c56c9e1168f72be768017e2948dd3e63a0ea563977ac036365972aacf34886b`.

## Verify this folder

```bash
cd verification/lean-gb6 && sha256sum -c MANIFEST.sha256
```
