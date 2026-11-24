# Record fixes — run 12 (EXP-1200 R-INV), companion to `IRH_GAP_INVENTORY_2026-11-12.md`

Author: w-p0inv (run 12, Dragon subagent), 2026-11-23. Independence I1 throughout. This file lists record fixes that came out of the run-10 part-7c and run-11 adjudication traces but were **not** applied to the inventory, because they target other files, other people's deliverables, or an entry that does not exist at the base commit. Nothing listed here was edited. Each item cites its source trace by path and sha256 (sha256sum).

Base commit: `64bd0657a2ea50b374d8af542d3a261e42338fb0` (origin/main). Branch: `run12/inventory-record-fixes`.

## 1. G-A31: status line held back (entry absent at 64bd065)

The entries G-A27–G-A31 (filed 2026-11-18) exist only in an uncommitted local edit of the inventory in the main clone. That edit is not part of this branch and was not touched. When the G-A27–G-A31 entries are committed, give G-A31 this status line (verbatim from the trace, §9 item 1):

> CLOSED-scoped (run 11, 2026-11-22): UV-regulated finite periodic 4D lattice, CK quantization; quadratic sector F2/I1 [D] (two engines); $v>0$ propagator F3/I1 via Simon II.27 (secondhand restatement); gap grade F3/I1; scope limits: continuum/renormalization, cubic-only truncation, $v>0$ vacuum.

- Source: `~/workspace/swarm/run11/adj/G-A31_trace.md`, sha256 `27955cb850339fc5f152e397e56ec33f360a8da2206a4a6b092f542646bcaddd`.
- Line-reference note: the trace cites the gap as "64bd065 l.465–470". The entry does not exist at 64bd065, so that line range belongs to the working tree (via the EXP-1104 quote), not to 64bd065.

## 2. G-C12: withdrawal notes owed in six other documents (not edited)

The inventory entry is withdrawn on this branch. The same false "eq. (7) wrong by a factor 2" statement appears at 64bd065 in these files. Each should carry a withdrawal note, not a silent patch (`G-C12_trace.md` §7.2):

| file (under `programme/`) | lines @64bd065 |
|---|---|
| `CONSOLIDATED_SUMMARY_2026-11-12.md` | 761, 765, 821, 1461 |
| `SUMMARY_AND_REPLICATION_GUIDE.md` | 769, 827, 1142, 1183, 1360 |
| `workstreams/ws-d-frameworks-rivals/task10_derivations_check.md` | 31, 191, 548 |
| `ws-d_summary.md` | 78, 168, 183 |
| `torus-node-comparison/TORUS_NODE_VS_IRH_COMPARISON.md` | 126, 301 |
| `torus-node-comparison/reader_b.md` | 35, 362 |

- WS-D downstream items T10-12, T10-14, T10-16 and T10-39 hold only as algebra on the misread form.
- Programme-record note (Dragon's memory, not the repo): the statement that v94 "corrected eq. (7)" is wrong. v94 restates the already-correct v93.1 equation unchanged (§7.3).
- Brandon is informed, not deciding (§7.4).
- Source: `~/workspace/swarm/run11/adj/G-C12_trace.md`, sha256 `815b84373568841808cad1034f3072d410247f9231c1e5861eb857f5f6768513`.

## 3. G-A12: author-file corrections (for the author or a later record)

From `G-A12_trace.md` §6 (sha256 `314f231fe248bbfaa6ea474447d3c609b5a43dbcea60469323e4be558028c057`), for the author's `G-A12.md` (sha `85241fca…`):
1. Replace "$D^*_{S2}=0.49858$. It occurs at the rational direction d110, not an irrational one" with "$D_{S2}$ over the stage-B set: 0.49858 at d110; refined minimum found ≤0.4800 at about 0.2° from d110 (v-ga12 s2opt.log); finite-window dependent".
2. Withdraw the "icosahedral-leaning" paragraph.
3. Replace "I conjecture these are related by $\mathrm{Aut}(D_4)$. This was not checked" with "verified by v-ga12 (W(F4) fold)".
4. Replace "a few per-direction D values" with "47 per-direction lines in 15 logs".
5. List the killed stageB_0…4 runs and controls_v2/v3/v5.
6. "Irrationality of the optimum: not established" now reads "no low-height algebraic relation found (v-ga12); irrationality unproved".
- `VERIFY_G-A12.md`: log the T2 plan deviations (item 4(d)) as an amendment. Its proposed F2 is superseded by F3.

From `G-A12-K2_trace.md` §7 (sha256 `a188b5e525505c60505237d2c350b9fa98fa227b75d2dc14362c5c29e6533468`), for the author's `G-A12-K2.md` (sha `430494fc…`):
1. STATUS "PROVED (computer-assisted …)" → "VERIFIED by two independent certified interval covers (F2/I1, rung 3, [D]); not kernel-verified".
2. The "F3 proposed, F2 NOT met" grade is superseded by F2.
3. D2 is superseded (full C recert).
- adj-E4 trace §4 C-1117e "min $LB_8\approx0.242$": annotate "sampled; true infimum ≈0.2342 (adj-E8, C)".

## 4. G-E9: verifier-file correction (fix (h))

`VERIFY_G-E9.md` claim b and `OUTPUTS.md` l.80 (v-ge9) say "10 satellite pairs". V's own data say 8. Correct to "1 dominant pair + 8 satellite pairs (9 of 12 occupied)". Source: `~/workspace/swarm/run11/adj/G-E9_trace.md`, sha256 `60b3e26a937c77db4cf7fa4cf896f784fd24c931dc900dde0241cb359d9bbb9e`, §5(h).

## 5. G-C21: manuscript recommendation (v94 l.958), not an erratum

v94 l.958 already scopes $[3/2,2]$ to CDT. Recommended addition after "no IRH grade changes" (`G-C21_trace.md` §8 fix 2):

> "IRH's own site-field operator (§III.1, l.458–468) has no UV dimensional reduction: its heat-kernel $d_s$ runs from the lattice fall-off through a maximum $\approx5.73$ to 4 (5 with time), so the $[3/2,2]$ interval is not an IRH prediction (EXP-1115, run 11, F2/I1). The Swift–Hohenberg $\psi$ operator was not tested."

- The author file `G-C21.md` is not edited (F-9).
- Source: `~/workspace/swarm/run11/adj/G-C21_trace.md`, sha256 `5259507ec3dbc63e46311298a2d9a51910f46b78347784f2d13884180420cf62`.

## 6. G-E10: map and v94 items (not applied)

- The corrected M6 wording (`G-E10_final_trace.md` §4) is for the comparison map's M6 row. It is an author decision (now under the 2026-11-22 delegation) and was not applied.
- v94 l.448: the grade B for "broad M6 overturned" is not supported by the run-11 record (C/I1). The narrowed sentence is CONTESTED pending the FoR full text (DOI 10.5281/zenodo.19151764 / 19170453).
- Candidate-table fixes (§7.1–7.7): row 30 DOI version (v9.3 19382492/19469301; v10.0 20552563 scores (1,0)); row 33 version and access FULL (figshare); row 35 access ABSTRACT; row 34 quote as two fragments; torus status "P (unconfirmed; search excerpt, source barred G-C16)"; R2's LITERAL count 6 superseded by 4; adj-B's fixes 1–5 stand.
- G-D10 was not edited (outside the R-INV list). Its text should be checked against the G-E10 closure.
- Sources: `~/workspace/swarm/run11/adj/G-E10_final_trace.md`, sha256 `d9f9ef7dd311e63b7afaed038608d8b44414ad8a70c4018be8604c27949050f4`; `~/workspace/swarm/run11/adj/G-E10_trace.md`, sha256 `0e4bbe9e4e9f9ea123e7872e3208126bbdfe42c7399ef8064eaa4e6b8c6f1ac7`.

## 7. G-C13 and G-A22: send-back fixes (not inventory edits)

- G-C13 (`G-C13r_trace.md` §8, sha256 `3fdd5e1fc24f31d9818c8dd6509d81e29f8359de9c9b2643e4ef8a1ed0e1aef0`):
  - R-1: R1's band-table row at 0.02 is float64-limited. The 40-digit values are $1.222772562520175\times10^{-10}$ and $1.472453884516146\times10^{-7}$.
  - R-2: V's "≥12 sig." / "≥10 sig." agreement statement is false at 0.02.
  - R-3: caption l.537 and the fig06 title should say "quadratic (small-$k$ envelope-limit) approximation". Amend before merge, then re-verify. This belongs to R-TEX.
  - R-4: "fails for θ≲π/6" should be "fails for θ < 0.4538 rad".
  - R-5: a READING sourcing note.
  - R-6: an optional heading change.
  - R-7: page-20.png is missing from SHA256SUMS.
  - v94-external must be regenerated after the merge.
- G-A22 (`G-A22_trace.md`, sha256 `5a7237f15c6a05e2f123e1bef771a271ad7136f74c533ebbf362775268e4f261`):
  - "21/25" → 22 lines / 29 hits.
  - The L1 bound "≤16" → ≤17.
  - l.408 "gapped" → "no sampled soft mode".
  - The EXP-1107 quote is an excerpt.
  - Record both the TL2022 and the TL2026 builds.
  - fig09 "⇒ THREE families" contradicts §V.2.
  - The fig01 title says "v93.1".

## 8. G-E8 and G-A15: provenance

- WS-D's shipped scripts (task10_scripts, task12_models) are not in the repo at 64bd065. They exist only in `~/workspace/research/irh/co-scientist-tasks-2026-11-10/ws-d-frameworks-rivals/`. The recommendation is to add them on a branch, with their shas (`G-E8_trace.md` §5.1, sha256 `fec787c48e73cd21aeadcb4fe9c54ba4c130bd342092b930e097282c075b2079`).
- The G-A15 task-13 code is outside the repo as well (`irh_models.py`, `task2a_attractor_ladder.py`; shas are in the inventory entry). Depositing it is a repo change for a branch (`G-A15_trace.md` §4.6(b), sha256 `8ee7bb48befd2f96f53d84bec23cb9ace760b950508cc74d5e69af09f2be095d`).
- Optional G-A16 note (unregistered, closes nothing): an unforced redundant spectral sector grows at the bare shell rate $k^2|\omega^2|=2.8$, the semi-implicit image of WS-C's 1.0142/step (`G-A15_trace.md` §4.7).

## 9. Merge record (m-p0, EXP-1200 Phase 0, 2026-11-23)

- Base: `origin/main` = `64bd0657a2ea50b374d8af542d3a261e42338fb0`.
- Merge 1, R-CODE `run12/artifact-fixes` @ `3c4e08c9e62901078d7264b6fe8c73b09deae2df`: merge commit `cdaa3b01450ec4d606489b1168183b13def15ed8`.
- Merge 2, R-TEX `run12/tex-record-fixes` @ `f7fcbf9df3e2b6a3fb4195ec4829345d406582ce`: merge commit `cda11ec8929b6c6990dfe64d845f17282e1dcfca`.
- Merge 3, R-INV `run12/inventory-record-fixes` @ `0fb18c58de303de32ff59c20cb22e7a12ca4db19`: merge commit `6b4efb27a1225aab06f8bcf73b7a6ce079d96fb8`.
- All merges `--no-ff`, no conflicts. Verifier verdicts v-p0 + v-p0b; adjudicator trace `adj/PHASE0_EXP-1200_trace.md` sha256 `3fb09a4712fdbdda0b9e8954b25062a557d688e06e0a2b75134b47227cbaa5f4`.
- C1 rounding recipe (amendment A1) reconstructed to match the shipped strings, not independently justified.

## 10. Run-12 erratum-candidate and record-item register (m-end, end-of-run record commit, 2026-11-23)

Every item below is **NOT APPLIED**. Manuscript items (E-, M-) wait behind the deepest-research validation gate and Brandon; record items (R-) are logged here and in the inventory only, and their target files were not edited in this commit. Trace paths are under `~/workspace/swarm/run12/adj/` unless stated; sha256 values were recomputed with `sha256sum` at merge time.

| item | class | target | what | source (trace §, sha256) |
|---|---|---|---|---|
| E-B8a | erratum candidate (manuscript) | `programme/v94/IRH_v94.tex` l.374, l.393, l.794, l.797 (also `v94-external` and summaries carrying 0.0034636) | uniform baseline printed as $-0.0034636$ omits the $k=0$ term of the l.149 operator; the literal l.149 value at $r=-0.35$, $\bar\psi=-0.18$, $u=v=1$, $q_0^2=8$ is $1.0333364$; the §II.8 conclusion survives a fortiori. Option A recommended; Option B (model change) PENDING-BRANDON | `G-B8_trace.md` §6, §11; `5f3bc559eb1e9d05251e37d3f7e1fe3a416b8811eacfb5f5fc4b3a5da40d2730` |
| E-A19a | erratum candidate (record/reproducibility class, not a refutation) | v94 l.349, l.364, l.367, l.368, l.1006 (same lines in `v94-external`) | 11.85% / 11.90% / 11.9% and the +0.03 union edge are not reproduced by any recorded definition; the l.368 cross-code reproduction is not in the record. Option A/A1: print a defined value ($11.55\%$ relaxed, W1 $81\times81$; with one-mode $11.60\%$ and coexistence-aware $11.42\%$). Option B (Brandon): supply the original scan definition. A window search aimed at 11.85% is excluded as post-hoc fitting | `G-A19_trace.md` §7; `c822c63b95bae387ddbd4d264d49bd6b47d54826d35d8632da1805bc6288129f` |
| E-A4a | erratum candidate (manuscript) | v94 l.406 (both texts) | "its survival there is metastability": the Model A end state is an index-9 saddle, not a local minimum. Option A (recommended): record now, text after the gate, with the corrected wording drafted in the trace; Option B: minimal deletion plus "a saddle of $F$ (index 9)" | `M-A4_trace.md` §5.1; `fd7c54a2d1189615855f393b2305dc2bad3c9fbb741a6d742d2970338b800ad0` |
| M-A4b | candidate tension (not an erratum) | v94 l.406 bold claim, l.867 (Model B "attractor") | rests on the same symmetric, noise-free seeded-survival inference shown uninformative about stability; Model B at $\bar\psi=-0.18$ untested by EXP-1216; next attack `M-A4_trace.md` §7 item 2 | `M-A4_trace.md` §5.1; sha as above |
| G-A4L prepared M-A4 wording | superseded | — | the G-A4L §9 manuscript wording and its "index 6" observation are superseded by `M-A4_trace.md` §4–§6 (index exactly 9, $F_{exc}=-0.025597066778294$) | `G-A4L_trace.md` §9; `3256cff8e3997cc50b0e49ba67c34a0d8679fc02629f5e4e5cd8865706da0aef` |
| R-A4c | code-record item | `verification/sim6_units.py` | shipped stepper instability (anti-Hermitian growth rate 0.351, NONFINITE at $t\approx220$ when extended); not relevant to the printed T=30 row; fix = per-step projection plus a non-finite guard. **Merger observation (m-end, unadjudicated):** at 0b7cb04 the file (sha256 `fd18f582f23cc65d58ad9112a04039729df53cc5e72f45589d3d8f195efe08c0`) already carries a per-step projection in `test_attractor` with `hermitian=True` as default (commit 773cc02, Phase 0 R-CODE) and uses full `fftn`, not `rfftn`; the unprojected path runs only via `hermitian=False`. The trace's "no Hermitian projection, rfft representation" description does not match this file as read; the adjudicator should say which stepper R-A4c refers to. Call-site grep (requested in the trace): the repo's only sim6 call sites are `sim6_units.py` l.135–141 (`test_attractor` 6000×0.005 = T 30, 1500×0.02 = T 30, unprojected 6000×0.005 = T 30; `test_quench` uses a separate damped-wave integrator); no call site with $T>100$ found; other hits are documentation | `M-A4_trace.md` §5.3; sha as above |
| R-1, R-2 | record fixes (coordinator text) | EXP-1216 question text; G-A4L §11 item 2 | quoted $F_{exc}=-0.025597065667943224$ / 6-fold are superseded by $-0.025597066778294$ / 9-fold | `M-A4_trace.md` §9; sha as above |
| G-C16 candidate | erratum candidate, DRAFT, unsent | `~/workspace/swarm/run12/w-gc16b/ERRATUM_CANDIDATE_G-C16.md` (sha256 `e10a50458c666f3fc23ab1bdc6067707a6e24bd5ec31deb4bc6edadfd8ad4aab`) | fit to reference only after a new version applies E4 (D1: "summed over the 12 link directions") and E5 (D3: $\mu^2$ wording); may not claim G-C16 closed or any $R$ value established; issuing it is Brandon's decision | `G-C16b_trace.md` §7; `58d7613f49a2b25db84f5a5e473c0685db2cbc99acfaaf2206cfc7d5df2698d1` |
| M-A21 | manuscript update candidate (not an erratum) | v94 l.90, l.319, l.918, l.1018 (same lines in `v94-external`; build map `build_external.py` l.103–104, 191) | "Trap robustness to a genuinely wider band is UNVERIFIED" is now superseded by EXP-1205 (G-A21 CLOSED-scoped) | `G-A21_trace.md` §10; `9113d713396ea021c005b382bb44abae2727b19eb5f7471c3aa94a870faa8dac` |
| R-A21a | record item | `programme/ADVANCES_since_v93.1_2026-11-14.md` l.72 (and rows l.26, §6 l.70–72) | cite "`run_native_cells.py` line 137" → l.138 (l.137 is the comment); dated addendum for the cap-144 rerun | `G-A21_trace.md` §10; sha as above |
| R-A21b | record item | `programme/local-independent/task4-native-cells/REPORT.md` l.320 (assumption A3) | dated note: sensitivity-checked at cap 144 (EXP-1205), outcomes unchanged, trap energy shift $-3.79\times10^{-9}$ | `G-A21_trace.md` §10; sha as above |
| R-E5a | record item | WS-B `wsb_s6charp.sing` l.5 comment; REPORT §8 l.101, U1 l.163 | the "dim 0, degree 35" expectation is wrong for $I_p$ (degree 5 at $p=101$; 35 = $7\cdot5$ is the $a_7=1$ slice count). Recorded in the G-E5 inventory entry; the script and REPORT are not edited | `G-E5_trace.md` §9; `00e2afd95f790d494992fb742c8c2a70830e06bc4ab18ca2a828cad7a7ff003f` |
| R-E5b | record item | WS-B REPORT l.124 falsifier; §8; C10/V10 l.185 | the char-$p$ falsifier is realised at $p=7$ (2-dimensional, degree 1816) and trivially at $p=3$ (empty); char-0 derivation untouched; dated notes owed | `G-E5_trace.md` §9; sha as above |
| R-E5c | record item | inventory G-E5 (old l.1195–1197) | "did not finish even p = 101 in 570 s": the fix was the engine (slimgb, 5 s), not the machine — covered by the new G-E5 wording in this commit | `G-E5_trace.md` §9; sha as above |
| G-C21 text call | manuscript addition candidate | v94 l.958 | optional addition: site-field operator has no UV reduction (EXP-1115); "the ψ operator likewise gives no plateau (EXP-1208)"; optionally "continuum $d_s$ monotonicity kernel-checked in Lean (EXP-1214)" | `G-C21-IRH-psi_trace.md` §7 (`6ca5a011da051399da6b37766590bd4d1007f4d0699d7a4ea356724b732d51a3`); `G-C21-lean_trace.md` §7 (`b87ebc2a2a41cd84488a6fce8d7690dbb7cb27550b5978fedde624aec3869463`) |

**Open follow-ups recorded with this register (not done here):**
- G-E10: the FoR full text (DOI 10.5281/zenodo.19151764 / 19170453) needs a live-browser fetch; zenodo returned 403 to subagents (`G-E10_trace.md`, `20c8e51efecd68b15269de74c8f653ed3502032605c85cbc6f8d5a37130eb2aa`).
- G-E5: copy the $p=5$/sp7 run logs locally before run 13 (`G-E5_trace.md` §8, §12).
- G-A31 is committed in the inventory from its run-11 trace (§1 above); G-A27–G-A30 remain in the main clone's uncommitted edit, which will conflict with the new G-A31 entry when it is committed.

## 11. Merge record (m-end, run-12 end-of-run record commit, 2026-11-23)

- Base: `origin/main` = `0b7cb0433ab572ac6fb3b8c4bb99e09f0b00bf8f`; branch `run12/record-end`. Commit hashes are in `~/workspace/swarm/run12/m-end/MERGE_REPORT.md`.
- Recount (`recount.py`, same rule as Phase 0): before 81 / 53 open / 19 closed / 5 closed-scoped / 4 non-gaps; after 82 / 45 / 23 / 10 / 4 (86 / 49 / 23 / 10 / 4 with G-A27–G-A30).
