# Record fixes — run 13 (EXP-1300), companion to `IRH_GAP_INVENTORY_2026-11-12.md`

Author: w-rec13 (run 13, Dragon subagent, symbolic-computer role), 2026-11-24. Independence I1 throughout (same model). These are coordinator decisions D1–D6, made by the Dragon run-13 coordinator under Brandon's 2026-11-22 full delegation and frozen in EXP-1300 (sha256 `f3e6de8d4501761b666c33892e8d54701935520fe1fc3d7d6f5613784e844667`). They are applied as record and not re-litigated here. Run folder on lean-build-4: `/home/hatch/workspace/vertex-ai-run/session-2026-11-24/irh-run13/record/rec13/` (logs under `logs/`, every computation through `runlog.sh` with `EXIT=0`).

Base: `origin/main` = `782a5551b9a6f1461c8951845d08a614c357413b`.
- Branch `run13/record-fixes` holds the inventory and this file only. Commits: `d1b5c2264a8d20301a7a81b5e83c66d0e95fb9db` (D6 fold-in), `091cd56d7466c5db2fb58936ef8727a92c02521b` (D1–D4), then the counts commit with this file.
- Branch `run13/tex-errata` holds the v94 and v94-external `.tex` and the rebuilt PDFs. Tex commit `e513771055dccdc545495deee5ac69b1197135f2`, then a PDF rebuild commit. It stays **UNMERGED** until the deepest-research gate (EXP-1310).

## 1. D1 — G-A1 / E-A19a: Option A

- **Canonical band value:** $11.5531\%$ = 758/6561 (exact: `baseline.log`, 758/6561 × 100 = 11.553116902911142).
- **Definition** (G-A19 status, `~/workspace/swarm/run12/adj/G-A19_trace.md` l.134): relaxed full field (v94 l.149), $N=16$, $L=\pi$, $q_0^2=8$, $u=v=1$, $\delta=0$, $w_6=0$, fixed $\bar\psi$, W1 rows 81×81, the frozen competitor set.
- $11.85\%$ and $11.90\%$ stay recorded as NOT REPRODUCIBLE under any recorded definition.
- **Inventory changes:**
  - G-A1 moves from PENDING-BRANDON to CLOSED as a record decision.
  - G-A2 stays closed, with its canonical value revised from $11.85\%$ to $11.5531\%$. The 2026-11-17 text is kept, labelled superseded.
  - The G-A19 pointer now names the tex branch.
- **Tex (both texts, same lines):**
  - l.349: prints $11.55\%$ (758/6561) with the definition, the window, and the union $-0.33\lesssim\bar\psi\lesssim0.05$.
  - l.364 and l.367: "the 11.85\% figure" becomes "the band fraction".
  - l.368: G-A19 trace §7 Option A wording. The unsupported reproduction sentence is deleted, and the one-mode $11.60\%$→$8.36\%$ replaces $11.90\%$→$8.47\%$.
  - l.1006: Option A wording ($\approx11.6\%$).
  - After the edit, neither text contains 11.85 or 11.9 anywhere.
- Wording choices made by the author (drafts were the G-A19 trace §7 Option A):
  - At l.349 the D1 definition is printed in full. "$\delta=0$" is glossed "shell detuning", the meaning of $\delta$ in G-A17.
  - The competitor set is described as "the frozen seeded competitor set of shell sub-patterns, stripes, a decorated stripe and 20-mode proxies", paraphrasing the G-A19 status.
  - "[WS-A task 3]" at l.368 is kept verbatim from the draft. It is an internal label in the paper body, and the gate should replace it with a reference.

## 2. D2 — E-B8a: Option A (record fix)

- **Value:** the literal l.149 uniform baseline at $r=-0.35$, $\bar\psi=-0.18$, $u=v=1$, $q_0^2=8$ is $\tfrac12(r+q_0^4)\bar\psi^2-\tfrac u3\bar\psi^3+\tfrac v4\bar\psi^4 = 25833411/25000000 = 1.03333644$.
- **Checks** (`baseline.log`, exact Fractions):
  - Without the $q_0^4$ term the value is $-86589/25000000=-0.00346356$, which is the printed $-0.0034636$.
  - Baseline/gap is $10842.98$ (was 36.34).
  - Changed-input control at $r=-0.30$ (`baseline_control.log`): $1.03414644$.
- **Tex (both texts), wording from `G-B8_trace.md` §6 Option A:**
  - l.374: the baseline formula and value $1.0333364$, "$\approx1.03$" for "$\sim3.5\times10^{-3}$", plus the drafted sentence on the $k=0$ term.
  - l.393: "$1.0333364\approx1.03$" and "about $1.1\times10^4$ times larger".
  - l.794: "≈1.03".
  - l.797: "baseline $1.0333364$".
- The drafted sentence carries "(G-B8, …on W1)" verbatim. These are internal labels, flagged for the gate.
- Programme summaries that carry 0.0034636 were not edited. They are outside this branch's scope (".tex only" and "inventory and records only").
- G-B8 pointer updated.

## 3. D3 — E-A4a: Option A (scoped wording)

- v94 l.406 (both texts): the sentence "Under non-conserved dynamics the pattern also survives but the baseline tension drifts out of the stable band; its survival there is metastability." is replaced verbatim by the corrected wording of `run12/adj/M-A4_trace.md` §5.1.
- That wording ends "[Index: F2/I1; instability: F3/I1; run 12, EXP-1216.]". It is internal vocabulary, flagged for the gate.
- The l.406 bold claim (M-A4b, candidate tension) and R-A4c were not touched.
- G-A4 pointer updated.

## 4. D4 — G-B7

**Record fact: run 12 left NO adjudicator-recommended option set for G-B7.**

Local swarm folder:
```
$ cd ~/workspace/swarm/run12; grep -rl "G-B7" . | wc -l
23
$ grep -rn "G-B7" . | grep -i -E "option|recommend"
./STATE.md:19:G-B7 (manuscript §I.2 — prepare options), G-B5 Hoy LJ-MD, ... (Run-13 queue candidates (not yet frozen))
./w-lit/SEARCH_G-E2_E3.md:35:- **C-1212e (G-E3): NOT LOCATED → recommend citations DROPPED.** ... Cite the manuscript text instead for B1 (G-B7), ...
$ ls adj | grep -i b7
(no output)
```

VM run-12 folder (`logs/grep_gb7.log`, EXIT=0):
```
count_files=10
/home/hatch/workspace/vertex-ai-run/session-2026-11-23/irh-run12/RUN12_REPORT.md:147:7. G-B7: the prepared options.
```

- `RUN12_REPORT.md` l.147 lists "the prepared options" among Brandon's decision items, but no option set was written anywhere in run 12.
- Other run-12 hits are recount logs, inventory copies, `EXP-1200.md:51` ("Do NOT edit manuscript §I.2 (G-B7 is a manuscript-text item for run 13)"), and the G-E3 citation trace.

**Equations the package actually integrates** (`logs/grep_dyn.log`, `git grep` at 782a555, EXIT=0):

| form | equation | file:line |
|---|---|---|
| Model B (conserved), semi-implicit | $\partial_t\psi=\nabla^2(\delta F/\delta\psi)$ | `verification/sim6_units.py:88` (`den = 1.0 + dt_use*K2*omega2`), `:97` (`ph = (ph + dt_use*K2*nl)/den`); also `verification/ws-a/d4model.py:233,241`, `verification/ws-c/code/irh_models.py:204,221` |
| Model A (non-conserved), semi-implicit | $\partial_t\psi=-\delta F/\delta\psi$ | `verification/sim6_units.py:89` (`denA = 1.0 + dt_use*omega2`), `:99` (`ph = (ph + dt_use*nl)/denA`) |
| (both above) | §II.8 seeded attractor tests | `sim6_units.py:73` `def test_attractor`, called `:135`, `:136`, `:138` |
| damped wave (non-conserved) | $\partial_t^2\psi+\gamma\partial_t\psi=-\delta F/\delta\psi$ | `verification/sim6_units.py:120` (`return bf, -gamma*bf - omega2*af + nl`, RK4 `test_quench` `:107`, called `:140–141`); `verification/sim7_fairtest.py:69–70` (semi-implicit, §II.6 $q_0^2=7.5$ fair test) |
| conserved MPFC | $\partial_t^2\psi+\gamma\partial_t\psi=\nabla^2(\delta F/\delta\psi)$ | none: `count_mpfc_hits=0` |

Here `nl` is the Fourier transform of $u\psi^2-v\psi^3$ and `omega2` is $r+(q_0^2-K^2)^2$, so `omega2*ph - nl` is $\widehat{\delta F/\delta\psi}$ and `K2` is $-\nabla^2$ (author sign check).

- **Decision:** take the inventory's own "Model B form actually simulated" branch.
- **Drafted on the tex branch (both texts):**
  - l.145 now states the three simulated forms: the damped wave for the §II.6 quenches, and Model A / Model B for §II.8 and the §I.3 conservation test.
  - l.151 adds the conserved MPFC only as the inertial generalisation, labelled **not simulated**.
- **Note:** the package does integrate §I.2's non-conserved damped wave, for the §II.6 quenches. So the correction states all three forms, not Model B alone.
- G-B7 status is now "correction DRAFTED on `run13/tex-errata` (decision D4); CLOSED on merge after the deepest-research gate". It stays OPEN in the recount.
- Owner moves to Local Muse verification (gate and merge).
- Line note: the inventory's "lines 185–191 / 215–219" do not match v94 at 782a555, where §I.2 is l.141–151 and the conserved requirement is l.163. This is recorded in the entry.

## 5. D5 — G-C13

Verified, not touched.
- The inventory entry heading reads "CLOSED as CORRECTED (run 11)".
- Its status cites "(Brandon 2026-11-22 15:19 CST)" and "question dropped by Brandon, 15:19 CST".
- Recount class: CLOSED.
- Stale clause, left as is: "being merged via run-12 R-TEX". The merge happened in run 12 Phase 0 (`RECORD_FIXES_run12.md` §9). Correcting it is not in D5's scope.

## 6. D6 — G-A27–G-A30 fold-in

- **Source:** branch `local/g-a27-a31-filing-2026-11-17` at `6043c9c3323df377e4ebf1116d9aae3c0cf70311`, `programme/IRH_GAP_INVENTORY_2026-11-12.md` l.437–464 (28 lines: the four entries with their blank separators).
- **Byte identity:** sha256 of that block is `04570960c176420324585d0fa89e3f658d5c5f521f860c1e6d2be4aa9008b229` (`inv_stageA.log`). The same block on the branch (l.480–507 after the fold-in) hashes to the same value (sha256sum).
- **Inserted** between G-A26 and main's G-A31.
- **Removed as stale:**
  - §0 bullet "**Not counted here:** G-A27–G-A30 … 86 / 49 open …" (782a555 l.51).
  - G-A31 "**Provenance note (run 12, m-end):** …" (782a555 l.487).
  - The Appendix note "G-A27–G-A30 are not; see §0" was rewritten in the counts commit.
- **G-A31: main's entry kept.** Diff, 6043c9c (older, `<`) vs main (`>`):
```
< - **Status/grade:** Open; no grade (unverified, not a failed claim).
< - **What we know:** … decay exponentially (Araújo 2019). Source: Consensus IRH thread audit 2026-11-18.
< - **What would close it:** … (e.g. a non-dissipative quantization route).
> - **Status/grade:** CLOSED-scoped (run 11, 2026-11-22): UV-regulated finite periodic 4D lattice, CK quantization; … (Was: Open; no grade.)
> - **What we know:** … decay exponentially (Araújo 2019).
> - **What would close it:** … (e.g. a non-dissipative quantization route). (Met in scope by run 11; the named scope limits stay open.)
```
  - Main's entry drops the source line "Source: Consensus IRH thread audit 2026-11-18." that the older text carried. It was not re-added, because D6 says to keep main's entry. The source is the same as G-A27–G-A30.

## 7. Recount (run-12 `recount.py`, sha256 `17ff88cd68497ce597325ec7943b2dc05cdf57714424ca92a0921dc1987cd6d7`, same rule)

| point | file | entries / open / closed / closed-scoped / non-gaps | log |
|---|---|---|---|
| 1 | 782a555 | 82 / 45 / 23 / 10 / 4 | `recount1_782a555.log` |
| 2 | after fold-in (d1b5c22) | 86 / 49 / 23 / 10 / 4 | `recount2_foldin.log` |
| 3 | after D1–D4 (091cd56) | 86 / 48 / 24 / 10 / 4 | `recount3_D1D4.log` |

- Point 2 reproduces the run-12 prediction ("86 / 49 / 23 / 10 / 4 with G-A27–G-A30").
- Point 3: G-A1 moves open → closed. G-B7 stays open.
- The counts commit updates §0 and the Appendix to point 3.
- Owner table:
  - Brandon's call 19: A1 removed as closed; B7 moved to local.
  - Co-scientist 13.
  - Local 9: A27, B7 added.
  - Literature 7: A28, A29, A30 added.
  - A27–A30 are assigned by the first owner named on their Owner lines.

## 8. PDF builds (tex branch)

- TeX Live 2026 `xelatex` (`/home/hatch/texlive/2026/bin/x86_64-linux/xelatex`, sha256 `5e3229c24f3bd06c47b6f118e765973902a2c4cfc2ec9a84d7e9138cd61aecba`).
- 3 passes per text, every pass `EXIT=0`, with `SOURCE_DATE_EPOCH=1763856000`. This is the run-12 R-TEX practice.
- `IRH_v94.pdf` (programme/v94 and the byte-identical repo-root copy): 40 pages, sha256 `d2609b66e6e32dbfa76ac51089a7eaf5a2d339a1667c7e0f53329c7c6bdda837`.
- `IRH_v94_external.pdf`: 40 pages, sha256 `6c0957e1e3721d110e63377f1c5aff04bf8d618922fc1234e3059a7a8118cef3`.
- The PDFs committed at 782a555 have 39 pages each (`pdfinfo`). The added text (l.145, l.151, l.349, l.374, l.406) adds one page.
- 4 overfull boxes per text (paragraphs at l.841, 1179–1180, 1187–1188, 1207–1208). These are the same 4 pre-existing ones; none of them sits at an edited line. 0 undefined references, 0 missing characters.
- `v94-external` was regenerated by the unchanged `build_external.py` (sha256 `1d92bfb2aaa31ecc89c953f756fc9ba2765236ec4712bc93cc51328e5ba6f843`, `EXIT=0`, 36 replacements, 21 table rows). The result is byte-identical (`cmp`) to the same spec applied by hand to the 782a555 external text.
- Practice followed: main tracks the PDFs, and run 12 committed rebuilt PDFs, including the repo-root copy, in a separate commit (f7fcbf9). Run 13 does the same on the tex branch.

## 9. Run-13 end-of-run record commit (w-rec13e, 2026-11-26)

Branch `run13/record-end`, cut from main `1ea6c14ac4bd793a62daec6f3b2c946d5c1744c6`; not merged. Author w-rec13e (Dragon subagent, I1, same model). Applies only adjudicated run-13 rulings in `swarm/run13/adj/`; each item names its ruling and the ruling file's sha256. Frozen deliverables (`G-D3b.md`, `K-A.md`, `M-A4b.md`, `G-E5p5.md`, …) are **not edited** (F-9); their corrections live here. No `.tex` or PDF is changed. Manuscript-facing candidates are collected in `programme/RUN13_MANUSCRIPT_NOTES.md`. Logs: `swarm/run13/w-rec13e/logs/`.

### 9.1 Lean files committed
- `verification/lean-gb6/` gains the N7 files (EXP-1313; `a-n7_RULING.md` sha256 `858c24211984…`, `a-gb6_RULING.md` sha256 `ecb6b4db2333…`): N7Bracket, N7CtrlFail31, N7CtrlFailRoots, verifier VN7Indep and VN7Ctrl, four cross-check scripts; MANIFEST 29 → 38 lines, `sha256sum -c` EXIT=0.
- New `verification/lean-ka/` (EXP-1314; `a-ka_RULING.md` sha256 `986b7de9c377…`): KA.lean, KACtrl.lean, verifier VKA/VKACtrl1–3, five cross-check scripts, README stating that the Fourier identity and the $\epsilon,\delta$ assembly are not formalised (4D); MANIFEST 12 lines, `sha256sum -c` EXIT=0.

### 9.2 Corrections to frozen deliverables (record wording only)
- **6-mode cluster list (a-b1 §4, `a-b1_RULING.md` sha256 `00f02ffaa5ef…`).** Correction (run 13, a-b1, on v-ma4b's verification): the 6-mode control spectrum listed in `w-ma4b/M-A4b.md` §(a) and `w-ma4b/OUTPUTS.md` ("0.354616 ×4, 0.598209, 0.598834, 0.697240, 0.712527, 0.758273 ×10, 1.17409, 1.38791") is REFUTED. The list is incomplete (20 nonzero plus 2 zero, against 24 eigenvalues below the Weyl floor $15.32$), and it contains values excluded by the verifier's bracketed Wolfram Galerkin and Kahan-certified numpy spectra. The verified lowest Hessian eigenvalues of the 6-mode state ($F_{exc}=-0.04177200107014797$) are $0.354616\times6$, $0.598834\times2$, $0.758273\times12$, $1.172415$ (unconstrained; $1.174160$ constrained) and $1.387976$, plus 2 translation zero modes. The inertia $(0,2,22)$ and the M-A4b verdict are unaffected. No repo text carried the list (`git grep` 0 hits at b8a496a).
- **R-A4c (a-b1 §2).** SPLIT: withdrawn as worded (the shipped `verification/sim6_units.py`, sha256 `fd18f582…`, projects by default); the missing non-finite guard is carried under R-A4c. Full text in inventory G-A4. (`a-b1_RULING.md` sha256 `00f02ffaa5ef…`)
- **K-A.md l.95 (a-ka row 2a, `a-ka_RULING.md` sha256 `986b7de9c377…`).** The sentence ending "the SH fluctuation measure about either phase is not an OS-positive Euclidean field theory in these directions" drops "lattice-regularised" for the crystal. Record wording: "… about the disordered phase on $\mathbb R^4$, and about the crystal for the lattice-regularised $F_h$, in the tested directions".
- **G-D3b (a-gd3b Q4, `a-gd3b_RULING.md` sha256 `c42524f43311…`):**
  1. `G-D3b.md:90`: read "$\lvert dF_{exc}\rvert_{50}=8.6\times10^{-13}$ (total-$F$ $\lvert dF\rvert_{50}=4.74\times10^{-12}$)" for "$\lvert dF_{exc}\rvert_{50}=4.74\times10^{-12}$".
  2. `G-D3b.md:114`: "against the analytic 0.2248" should read "against the discrete-map rate 0.2248 (continuum 0.22)".
  3. `G-D3b.md:6` / board #159: the P2 "selects" label is cited only with the a-gd3b qualifier: not reproduced; pooled $0.82$ $[0.692,0.902]$.
  4. Board #126: "330x6+411x6+3221x6" should read "3221x12" (a board note, not an edit).
  5. Tooling: the repo analyzer (`verification/sim6_units.py:30–35, 55–61`; leg files `gd3b_common.py:38–43`, `gd3b_run.py:127–129`) scores only the hard-coded $(\pm a,\pm a,0,0)$ star, so any shell with more than one $D_4$ subsystem ($L=3\pi,5\pi,6\pi,\dots$) is mislabelled `other`. Fix on a branch only (merger's decision): a rotation-invariant label (occupied set $\ge0.1\cdot\max$, Gram rank 4, inner products $\{\pm n^2,\pm n^2/2,0\}$, symmetric and reflection-closed). Any prior result that relied on the repo label at $L>\pi$ with multi-$D_4$ shells must be re-read. **Not applied here** (code change; no code is edited on this branch).
- **G-E5p5 (a-ge5p5 §7, `a-ge5p5_RULING.md` sha256 `b0901f4d8f70…`):**
  - RF-1 (G-E5p5.md l.23, A4.1, A4.2): given purity, $I_5$ is a CI and so CM, and affine section length is $\le$ the scheme degree; the scatter is due to sections meeting $\bar V$ at infinity, which only lowers the count.
  - RF-2 (l.18–20): the "4-section guard empty on both engines" is draw-dependent; dimension rests on Krull plus purity, not on the guard.
  - RF-3 (l.97): the Hilbert polynomial at $k=1$ must be computed in the 17-variable embedding; the 10-variable A2 presentation does not preserve degree.
  - RF-4: "degree" throughout means scheme degree in $\mathbb A^{17}$ (closure in $\mathbb P^{17}$).
  - RF-5 (cosmetic): in §6, L13-ge5-11 is listed before L13-ge5-10.
  - RF-6: the block-B sha citation should name its extraction rule (regex group `ideal I = (.*?);`).
- **G-A9 "35.11 GiB" (a-abst §5 E-1, `a-abst_RULING.md` sha256 `6db0a198e48a…`).** Inventory parenthetical replaced (see G-A9). The run-11 session file `session-2026-11-20/irh/gap-closure/G-A9.md:30` ("a $256^4$ grid requires $35.11$ GiB") is read-only history and is not edited; its error is recorded here: $256^4\cdot8$ B $=32.00$ GiB.

### 9.3 Barrier wording (a-ga10 §6 R1–R5, `a-ga10_RULING.md` sha256 `96c3db44c144…`)
- R1, R2 (G-A10 Status and the ~1–10% expectation) and R3 (G-A18 "~$15\times$" qualified as the amplitude-equation barrier; full field ≈$3.2\times$) applied in the inventory. R4 applied as a dated addendum in `programme/tasks/critical-droplet/report.md` (after l.7); R5 appended in `OPEN_PROBLEMS.md` (l.76–78 paragraph).
- Secondary "~15×" / "555 as the barrier" occurrences got a dated addendum pointer at the end of each file, no rewrite: `programme/CONSOLIDATED_SUMMARY_2026-11-12.md` (l.279), `programme/SUMMARY_AND_REPLICATION_GUIDE.md` (l.321), `programme/workstreams/ws-a-core-computations/task4_report.md` (l.72, 175), `programme/AUDIT_batch1_2026-11-12.md` (l.262–265).
- E1–E4 (v94 l.436, 319, 938, 89/920) are manuscript candidates in `RUN13_MANUSCRIPT_NOTES.md` §1.

### 9.4 Artifact tooling (v-art, `swarm/run13/v-art/V_REPORT.md` sha256 `47ec60cee714…`)
Recorded as notes on G-B2, G-B3 and G-B4; their Status lines are unchanged because no adjudicated ruling closes them. Open items: `sim6_units.analyze` l.62–63 still averages the lock over all triads with no empty/zero-state guard; the absolute floor `max(0.5·max, 1e-3·A*)` needs coordinator countersign before any run; the shipped ws-c csv `lock` columns use the old metric; the T-B4 JSON is byte-identical only on the numpy 2.x VM env (physics fields agree).

### 9.5 Other record items
- **G-C13:** stale "being merged" text replaced by "merged on main via run-12 R-TEX (899efb8 → cda11ec)" (basis: Brandon's closure 2026-11-22 15:19 CST and run-12 R-TEX; no run-13 ruling).
- **G-C8:** reading (B) decided 2026-11-25 ~05:45 CST under Brandon's delegation and reversed the same day when the memo's K-B1 trigger fired (EXP-1315, `a-kb1_RULING.md` sha256 `f8df06b8dfdd…`); (C) is the working reading with no construction; (A) not reinstated. Memo copied verbatim as `programme/G-C8_DECISION_2026-11-25.md` (sha256 `6073322da2cc27b883b064005e029754ba4bc5b7385ef0ba7da6ac1e7c45f7d3`). v94 §IX.2 unchanged.
- **G-E10 Q5:** v1 DOI 10.5281/zenodo.19151765 is a deleted record (HTTP 410), so Q5 is CLOSED (`G-E10_Q5_NOTE.md` sha256 `90ceff7e073c…`); M6 dated correction note added under the M6 row of `programme/workstreams/ws-e-cosmology-map/14-researcher-map-report.md` (row kept).
- **G-C19:** the ABSTAIN record was stale; resolved at G8/F1 on 2026-11-12 (a-abst §4) (`a-abst_RULING.md` sha256 `6db0a198e48a…`).

### 9.6 Recount (frozen `recount.py`, sha256 `17ff88cd68497ce597325ec7943b2dc05cdf57714424ca92a0921dc1987cd6d7`)

| point | commit | entries / open / closed / closed-scoped / non-gaps | log |
|---|---|---|---|
| before | 1ea6c14 | 86 / 48 / 24 / 10 / 4 | `recount_before_1ea6c14.log` |
| after rulings | f0a0571 | 87 / 42 / 27 / 14 / 4 | `recount_after_f0a0571.log` |

Moves: open → closed G-A16, G-B7, G-C19; open → closed-scoped G-A27, G-A28, G-A29, G-B6; new open G-A32. §0 and the Appendix were updated to the after-count in b78867f.
