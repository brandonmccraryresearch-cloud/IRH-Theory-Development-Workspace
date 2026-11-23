# IRH Gap Inventory — 2026-11-12

**Date:** 2026-11-12
**Baseline for:** the joint Muse + Academia Co-scientist programme to close all gaps in IRH
**Manuscript under audit:** IRH v93.1 (McCrary), source rebuild
`IRH_v93_1_source_rebuilt.txt` (34 pp., 1,638 lines)
**Companion document:** `CONSOLIDATED_SUMMARY_2026-11-12.md` (per-task
verdicts with HLRE v5.1 grades; cited here as "Summary §n")
**Sources:** the 15 task reports, `SUMMARY_AND_REPLICATION_GUIDE.md`
(§8 cross-cutting, §9 register, §12 open questions), `HARK_REPLICATION_AUDIT_REVIEW.md`,
`~/workspace/research/IRH-Theory-Development-Workspace/OPEN_PROBLEMS.md`
(repo open-problems register, Part IX), and the torus-node comparison
§7.3 (`~/workspace/research/irh/torus-node-comparison/TORUS_NODE_VS_IRH_COMPARISON.md`).
Nothing in this inventory is filed, committed, or written into the
manuscript. No simulations were run and no GCP spend was incurred to write it.

## 0. What "closed" means

A gap is **closed** when it has a **graded verdict** — verified /
corrected / refuted / ABSTAIN with the reason nailed down — **not** when
the manuscript is vindicated. Several gaps close by showing the manuscript
claim is wrong: the closure is the verdict, and the manuscript text that
needs changing is then a separate, Brandon-owned item (filing an erratum
or a correction is not the same as closing the gap). Conversely, a gap
stays **open** while its verdict is missing, even if the manuscript's
claim happens to be right — an unverified true claim is still an open gap.

**Owners.** Each entry names who owns the next step:

- **Co-scientist task** — a task for Academia Co-scientist (new, running,
  or candidate). New tasks need Brandon's launch decision where stated;
  running tasks need no action until they land, when they are audited
  locally.
- **Local Muse verification** — work Muse does locally (reading, small
  exact checks in the conda env, fetching a public file). No GCP spend
  without a named cap; no heavy simulation without costing first.
- **Brandon's call** — only Brandon can decide it (a manuscript wording,
  a canonical value, a decision between mutually exclusive readings, a
  script fix that changes delivered artifacts, an author-contact or
  launch decision). These are **not closable by the programme alone** and
  are never presented as if they were.
- **Literature / external** — the next step is a literature retrieval or
  an external result, not a computation.

**Grades.** Status/grade per entry is the grade of the *verdict about the
gap* (usually from the task that examined it), not a grade of the gap's
underlying physics. Caps: Track E **C** at I1; Track F **F2** two-route /
**F3** single-route. ABSTAIN and INCOMPLETE-EVIDENCE carry no grade.

**Counts.** 80 entries in total: **68 open gaps**, **8 closed-as-verdict**
(recorded inside their groups), **4 recorded non-gaps** (a boundary, a
standing rule, a gated non-item, a record guard). By group: A — 26 entries
(24 open, 2 closed); B — 9 (8 open, 1 closed); C — 22 (17 open, 3 closed,
2 recorded non-gaps); D — 12 (11 open, 1 recorded); E — 11 (8 open,
2 closed, 1 record guard). A further list of verdict-closures that are not gaps at
all (§6) is given separately and is not counted in the 80.

**Standing guard (not a gap).** WS-A task 5 ran **14 runs** (6000 steps
each), STATUS VERIFIED for the 14-run protocol. The "143 basin runs"
figure in Academia's 2026-11-12 email is **Academia's count, NOT ours**
— never cite 143 as our run count. (See also entry E11.)

---

## Group A — $D_{4}$ selection, band, basin, and truncation

Manuscript sections: §II.6–II.9 (band, nucleation), §VI.1–VI.2
(predictions), §IX.1 (tractable computation). Tasks: WS-A 1–5, WS-C 7+13,
WS-E 11 (band fraction). Cross-cutting: guide §8.1 (the band
discrepancy), §8.2 (Model B artifact).

### G-A1 — The 11.85% band fraction is not independently reproducible

- **Status/grade:** INCOMPLETE-EVIDENCE (WS-E task 11, C7; no grade).
- **What we know:** WS-A task 3 (W1 window) gives 11.60% (full family)
  and 12.94% (hex-only) at $(\delta = 0, w_{6} = 0)$; the manuscript's 11.85%
  lies between them — bracketed, not reproduced. WS-C task 7's measured
  slice at $r = -0.35$ is $\bar{\psi} \in (-0.235, -0.125)$, narrower than the quoted
  $(-0.33, +0.03)$. WS-E task 11: no scan code in repo `verification/`;
  scan definition absent.
- **What would close it:** the manuscript stating its scan window and
  scan definition, plus the sub-pattern free energies that set the band
  edges — then a recomputation against exactly that definition. (A
  canonical-value decision alone, G-A2, does not reproduce the scan.)
- **Owner:** Brandon's call (state the window/definition$) \to$ then
  Co-scientist task (recompute).

### G-A2 — 11.85% vs 11.90%: which band value is canonical?

- **Status/grade:** Genuine source inconsistency, unresolved; no grade.
- **What we know:** the band is stated as both **11.85%** (headline
  PREDICTION, §II.7) and **11.90%** $(w_{6} = 0$ value, §II.7 sixth-order
  paragraph; Appendix A item 8 calls 11.9% "the correct" value). Three
  workstreams bracket but do not reproduce 11.85%. The no-note IRH
  recompile (33 pp., 2026-11-10) no longer flags the inconsistency up
  front.
- **What would close it:** Brandon's decision on the canonical value
  (and whether the other figure is a rounding, a different window, or an
  error).
- **Owner:** **Brandon's call alone.** Not closable by the programme.

### G-A3 — Measured band slice vs the manuscript's quoted union; the +0.03 edge is UNVERIFIED

- **Status/grade:** Open discrepancy, not a refutation; +0.03 edge
  UNVERIFIED (WS-C task 7, grade C).
- **What we know:** measured 24-mode global-minimum band at $r = -0.35$ is
  $\bar{\psi} \in (-0.235, -0.125) (0.01$ grid). The manuscript'$s (-0.33, +0.03)$ is
  the union over quench depths in the full $(\bar{\psi}, r)$ phase diagram. The
  +0.03 edge is UNVERIFIED against the measured slice; the band's
  r-dependence is unmapped beyond the slice.
- **What would close it:** a full $(\bar{\psi}, r)$ phase-diagram recomputation —
  WS-A task 3's map is the tool for it (guide §12 Q7) — deciding whether
  the quoted union is the union of the measured slices or a different
  construction.
- **Owner:** Co-scientist task (new).

### G-A4 — The 24/24-from-noise rate: 0/5 seeds, unbounded

- **Status/grade:** CLOSED as a bounded rate (run 11, EXP-1114; F3 / Track E C, I1). 0/240 noise seeds are in the full 24-mode pattern at $T=50$ under the WS-C quench protocol ($N=16$, $L=\pi$, $r=-0.35$, $q_0^2=8$, $u=v=\gamma=1$, dt 0.02, noise $10^{-2}$, $\bar\psi_0=0$). CP 95% two-sided upper bound 1.53%, one-sided 1.24%. Outcomes: 6-mode 203, 2-mode 33, 8-mode 1, other 3. The verifier found 0/12 full24 on fresh seeds and agreed with R1 on 10/10 reruns. Scope: a $T=50$ snapshot; the class is not settled at $T=50$ for many seeds (219/240 differ from $T=30$, 68/240 from $T=40$). This is not a long-time-attractor rate. $\gamma=1.0$ follows the code; the WS-C task1 report l.363 says 1.2. (Was: Open; 0/5 is an upper bound, not a zero (WS-C task 7, grade C).)
- **What we know:** noise quenches never reach the full 24-mode pattern
  in the truncation (WS-C: 5 seeds $\to 6$-mode $\times3, 2$-mode, 8-mode; WS-A
  task 5: 0/6 noise seeds grow at all). Damped-wave quenches drift
  $\bar{\psi} \to +0.0025$, where hex6 is the lower state.
- **What would close it:** 20+ quench seeds to bound the rate (WS-C
  follow-up, costed, not run), plus longer quenches / annealing to test
  whether the 2-/8-mode outcomes are transient (see G-A13).
- **Owner:** Co-scientist task / local Muse verification (small local
  runs; larger seed counts costed first).

### G-A5 — The truncation gap: do the $D_{4}$ basin results survive outside the 24-mode truncation? [FIRST JOINT ITEM — PARTIAL, narrowed, stays OPEN — Batch 2 audit 2026-11-12]

- **Status/grade:** PARTIAL, narrowed, stays OPEN. Patterned recovery with harmonics VERIFIED in two cell constructions plus the 4D field test (Track E B / Track F **F1 (PROPOSED**, was F2 — two-leg evidence: full rerun + independent re-derivation)). General selection from noise NOT established anywhere (0/6 field; pooled 0/20 uniform per star, Wilson 95% upper bound $\approx 16\%$; AMS null expected at barrier/noise $\approx 34$). **LANDED and audited 2026-11-14:** noise-nucleation 4D field test (chat 02dfb5cb: 18 runs to $t=200$, meshes $18^{4}$/$28^{4}$; 9/9 patterned + 3/3 bridge recover, 6/6 random decay to uniform) and native-cells (Task 4) — see consolidated comparison.
- **What we know:** everything in WS-A/WS-C is inside the 24-mode
  truncation $(L = \pi$ box, $16^{4}$ grid, shell modes only). The "Compare $D_{4}$
  Selection Frameworks" gap memo (16th task, finished overnight
  Nov $9\to10$; email Nov 9, 5:31 PM CST) identified this as the sharpest
  open question — the gap between *selecting* the $D_{4}$ shell and
  *spontaneously reaching* its full 24-mode pattern — and the memo is
  now located and audited (see G-E1).
- **What would close it:** a graded verdict on whether the basin results
  persist once off-shell modes are permitted. **LANDED 2026-11-12:** "Run a
  four-dimensional field test of $D_{4}$ formation" (Academia chat
  `02dfb5cb-5423-47eb-9bbe-d8e3d25b6fdc`, COMPLETED) and locally audited
  (`AUDIT_batch2_2026-11-12.md`: 53 claims across the batch — 43 VERIFIED,
  9 UNVERIFIED, 1 REFUTED). The 4D run: 18 trajectories + 6 refinements to
  $t = 200$, meshes to $28^4$; all 9 patterned starts recovered phase-locked
  $D_4$; all 6 random starts decayed to uniform. Progress-update claims
  ($t = 100$ refinements / overlap > 0.999988; $B$ 0.0633–0.0768 ranges;
  rank-15/6/4 truncation on $24^4$) are UNVERIFIED — absent from
  `report.md`, `run.log`, and all data; superseded by the final $t = 200$
  record. What remains: general selection from noise — a real
  noise-selection test, not patterned starts.
- **Owner:** Co-scientist task (LANDED, audited). When it lands: local Muse
  audit claim-by-claim; nothing filed, committed, or written into the
  manuscript.

### G-A6 — Off-shell instabilities of the full $D_{4}$ wave [CLOSED as a mapping task — VERIFIED (Track E B / Track F F2) — Batch 2 audit 2026-11-12]

- **Status/grade:** CLOSED as a mapping task — VERIFIED (Track E B / Track F F2). The frozen-ansatz spectrum is fully verified (audit re-ran `run_offshell.py` at $K = 3, 6, 8$; headline $K = 8$ rate $+0.022877243496718158$ reproduces exactly; all other block rates to $\leq 8\times10^{-14}$). Stability of the harmonically relaxed state is ABSTAIN — a new follow-on gap, not G-A6.

**Follow-on landed 2026-11-14 (bloch-growth, Task 6):** sampled stability of the relaxed state is supported at grade **C (PROPOSED)** — three routes agree (52 $\Lambda$-sector fiber maxima, 259 $q$, 14,641 $q$ dense GCP map), no positive rate anywhere sampled; Goldstone zeros / mean channel F2 supported; frozen quartet $+0.0228772435$ confirmed as an artefact (F2 supported). Continuum Bloch stability for all $q$: **ABSTAIN** (no interval enclosure). Qualifier: the 52 rates are $\Lambda$-sector fiber maxima, not full-fiber maxima; one open numerical gap ($\Gamma$ first finite rate $-2.73844227$ vs $-2.73813733$, difference $3.05\times10^{-4}$).
- **What we know:** distinct from G-A5 (a field test of formation) and
  from WS-A task 3 (band under detuning within the truncation). The
  linear-stability analysis of the standing wave against off-shell
  perturbations now exists: four positive frozen-ansatz rates
  $\lambda \approx +0.02287724$, translation-like (99.996124% of Fourier
  power on the occupied star); all other sectors' leading rates negative.
  The ansatz is not a full-field equilibrium — the results do not establish
  instability of the relaxed state.
- **What would close it:** the candidate task "Map off-shell
  instabilities of the full $D_{4}$ wave" (Academia 2026-11-12 email) —
  linearize around the standing wave, leading unstable bands on a finite
  Fourier grid — then a local audit of its claims. **LANDED and audited
  2026-11-12** (chat `bf37d817-6646-4041-96f2-2d2e6648d9d0`, COMPLETED;
  `AUDIT_batch2_2026-11-12.md`: 12/12 claims VERIFIED, 0 corrected).
- **Owner:** Co-scientist task (LANDED, audited 2026-11-12). Follow-on:
  relaxed-state stability (ABSTAIN) needs a new scoped task.

### G-A7 — Stripe competitor omitted from the band's competitor set

- **Status/grade:** CLOSED (scoped). $L=\pi$, $N=16$: C-720-S F2/I1, rung 3 (7c + EXP-1102). $L=2\pi$, $N=16$: C-1101∪1111 F3/I1, rung 2, F2 at 6 Wolfram-checked band points (record-bound at $(-0.075,-0.03)$). Traces G-A7_trace (7c), G-A7p2_trace, G-A7_L2pi_trace (adj-D3) and G-A7_L2pi_union_trace (adj-E7).
- **What we know:** the WS-C band's competitor set {24-mode, 6-mode,
  disordered} omits stripes. A stripe-like state appeared at $\bar{\psi} = +0.10$
  in one Hark transverse run, re-run in run 11 (G-E9): the $-0.048943$ state is the decorated stripe (1+8 pairs); "metastable" for it is SCOPING only (adj-E3 kick probe, 4/4 return; not graded). The audit's claim that "the round-1 review had $\approx$
  $[-0.235, -0.14]$ with stripes/A2/A3 included" could NOT be verified
  (see G-E2).
  **Run 11 scope wording (adj-E7, G-A7_L2pi_union_trace §8):** On the v94 functional ($q_0^2=8$, $u=v=1$) on the $L=2\pi$ periodic 4D cell at $N=16$, a seeded relaxation search finds no stripe-family state below the $D_4$ family at any of the 55 $L=\pi$-band points checked. Those points are the whole $L=\pi$ band at step 0.01, with ±0.02 margins, at $r=-0.6,-0.425,-0.35,-0.25,-0.075,0.1$. The search used 14–18 seeds per point, including on- and off-shell stripes and the Hark transverse state, and a code-independent verifier agrees at 33 of the points. At 52 of the 55 points no stripe-family stationary state survives relaxation. At the 3 points where the exact one-mode coefficient $a_8<0$, the stripe is a stationary but unstable state, at least $4.69\times10^{-3}$ above $D_4$. A binary-independent Wolfram route agrees on winners and energies at 6 band points (F2 there). The band at those $r$ is unchanged by doubling the cell (F3/I1, rung 2). Cells beyond $2\pi$ and states outside the seeded basins are not tested.
  The Hark transverse test was re-run: 3 seeds per point in R1-ext, 2 in V-ext, none ending as a stripe in the band. The 1-run "stripe-like state at $\bar\psi=+0.10$" is off-band and is superseded by the positive controls: stripe1 wins at $\bar\psi\ge0.25$ in three codes. The G-E2 caveat above is unchanged.
- **What would close it:** a stripe-inclusive band recomputation
  (re-run the transverse runs, then recompute the band with stripes in
  the competitor family), or a demonstration that stripes never win
  anywhere in the band. Met as a scoped demonstration on $L=\pi$ and $L=2\pi$ cells (seeded; see carried K6).
- **Owner:** Local Muse verification, done in run 10 part 7c and run 11.
- **Carried:** K6 (seeded search, no $L\ge4\pi$), N1 (off-band 6pair_other gaps unchecked at $N=24$). Band-value caveat stays as recorded elsewhere: 11.85% vs part-7c 11.553% (Track E C; see G-A2).

### G-A8 — The $w_{6}$ term form is unstated; $w_{6}$ narrowing not re-derivable; joint (detuning $\times w_{6})$ map open (IX.1.3)

- **Status/grade:** INCOMPLETE-EVIDENCE (WS-E task 11, C8; no grade).
  Repo problem IX.1.3 is explicitly OPEN.
- **What we know:** WS-A task 3 confirms the narrowing trend
  (11.60% $\to 8.36$% in W1 vs manuscript 11.90% $\to 8.47$%) using its own
  $w_{6}$ term, but the manuscript's functional form of the $w_{6}$ term is not
  stated, so neither the 8.47% nor the joint map can be recomputed.
  $H = 911,040 (D_{4}$ shell sixth-order count) is stated, not re-derived.
- **What would close it:** the manuscript stating the $w_{6}$ term form —
  then a recomputation of the 8.47% and the joint map.
- **Owner:** Brandon's call (state the term form$) \to$ Co-scientist task
  (recompute).

### G-A9 — Larger-volume simulation: single-crystal ordering and phase-locking convergence (IX.1.1); larger-box droplet run costed, not run

- **Status/grade:** PARTIAL, narrowed, stays OPEN. Dissolution in the $4\pi$ box supports Track E **B (PROPOSED)**; size bound $L \gtrsim 61$ (35.11 GiB per real array at cutoff $6.5$) supports Track E **B (PROPOSED)**. Local growth in the $2\pi$ box is now read as finite-box/image-assisted filling, not an isolated-droplet threshold (local shell-fraction scaling predicts the $4\pi$ dissolution). The larger-box droplet run itself is still unrun; infinite-volume $R_{c}$ stays ABSTAIN.
- **What we know:** all package simulations are $L = \pi$, N = 16 (1.4
  wavelengths across); periodic images may stabilise sub-patterns that
  would be unstable in a larger box (WS-A task 5 §5). A larger-box
  droplet run $(L = 2\pi, N = 32)$ is costed, not run: $a 32^{4}$ grid is $16\times$ the
  points of $16^{4}$; at ~15 ms/step $(16^{4})$, a 6000-step run is ~25 min
  locally per seed, and the threshold search needs several seeds — a
  GCP-scale job.
- **What would close it:** the larger-box runs, testing whether the box
  threshold moves toward the ODE value $(R_{c} = 12.57)$ and whether
  sub-pattern traps survive without periodic-image stabilisation.
- **Owner:** Co-scientist task, **only with a named budget cap** (GCP
  spend needs Brandon's approval; no spend authorised for this yet).

### G-A10 — Nucleation barrier height and critical droplet size (IX.1.2): full-PDE droplet uncomputed

- **Status/grade:** OPEN (repo register). Partial verdicts: ODE
  $R_{c} = 12.57 / \Delta F* = 555$, grade B (exact within the amplitude
  equation); thin-wall $R_{c} = 7.38 / \Delta F* = 37.2$, grade C (approximation
  shown to fail — $\xi = 8.64 > R_{c})$. **2026-11-14:** saddle energy alone does not decide full-field fate — supported at Track E **C (PROPOSED)** (single-profile family; interface-tension: tensions $0.0189904$ / $0.0264060$ at coexistence, thin-wall transfers $36.95$ / $138.12$ vs saved saddle $550.93$; transferred tension is path-dependent by 40%). Deterministic saddle/threshold supports B / F2. Any rate stays ABSTAIN.
- **What we know:** the ODE and thin-wall routes use the one-mode
  $F_{mod}$ and the envelope gradient coefficient, ignoring higher harmonics
  and the relaxed free energy (1.2% lower at the operating point). The
  box threshold is a finite-box quantity, not the infinite-volume $R_{c}$
  (see Summary §2, task 4).
- **What would close it:** a full-PDE critical droplet (shooting the PDE,
  not the amplitude equation) — expected to refine $R_{c} / \Delta F$* by ~1–10%;
  the thick-wall character would survive. Plus the larger-box runs of
  G-A9.
- **Owner:** Co-scientist task (costed first; GCP-scale if on a big box).

### G-A11 — Defect homotopy beyond elementary Burgers vectors (IX.1.4)

- **Status/grade:** CLOSED-scoped. **Run 10 part 7c (topology, in-phase pattern; F2, I1, [D], rung 3; trace `run10p7c/adj/G-A11_trace.md`):** G-A11 CLOSED per EXP-719, scoped to the in-phase pattern ($\varphi_k=0$), topological classification only. $\Lambda=\pi D_4^*$; $\lvert P\rvert=1152$, $\lvert P^+\rvert=576$; $\Lambda_{P^+}=0$, so $\Gamma^{ab}=\mathbb Z_2$; 54 Γ-classes. $\pi_2(S^3)=0$, $\pi_3(S^3)=\mathbb Z$, $\pi_4(S^3)=\mathbb Z_2$ are cited standard theorems (not computed by any tool; accepted as textbook premises). Energetic stability is out of scope. **Run 11 (relaxed pattern; EXP-1103/1112):** G-A11 (D4 relaxed-pattern topology, $L=\pi$): CLOSED-scoped. At P1 $(-0.35,-0.18)$ and P2 $(-0.495,-0.24)$ the relaxed v94 field is a translate of the in-phase 24-mode $D_4$ pattern, with stabiliser point part $W(F_4)$ (1152). Three code-independent routes on two binaries agree: R1/V on Python and W on Wolfram (P1: $F_{exc}=-0.0077276236034134$, agreement $\le7.5\times10^{-16}$; P2: $-0.0099411477857516$, $\le1.8\times10^{-15}$). Grade: Track F F2, I1, [C]. P2 is at rung 3. P1 is at rung 2, F2 record PASS (adjudicator-observed Wolfram replay, adj-E5b); the run-11 coordinator adopted the passing rung-3 variant (`PROBE_E5b_rung3`, RUN11_REPORT §3). Not covered: the stripe seed at P1, $L=2\pi$ (EXP-1111), other in-band points, and the band membership of P1/P2, which rests on the 7c csv. Earlier status (2026-11-14): shortest-shell classification supported at Track E **B / Track F F2 (PROPOSED)**.
- **What we know (2026-11-14, phonon-stiffness, Task 8, 31/31 VERIFIED):** the translation (Burgers) lattice is $\pi D_{4}^{*}$, **not** $\pi D_{4}$ — the local side was wrong and Co-scientist is right (GCP confirms $(\pi/2)(1,1,1,1)$ is the shortest vector, $|b|=\pi$); one $W(F_{4})$ orbit per $D_{4}^{*}$ shell $\|b\|^{2}\le6$ verified (group order 1152 by exact-rational BFS). Stiffness $\lambda=\mu=4A^{2}q_{0}^{4}=1.54058921014457$ agrees exactly with the local value. Equilibrium edge/screw factor is $4/3$, **not** $2$ — the local edge coefficient was a non-equilibrium trial-field value, $3/2$ high; corrected elementary edge $K$ $0.490385\to0.326923$, $E/A(R=20)$ $0.899\to0.666$; screw unchanged. **Local edge leg demoted pending correction C5 (script rerun outstanding).** Defect realisation contradicted in the tested setup (Volterra defect heals under relaxation; GCP Job 3).
- **What would close it:** a computation / classification of the defect
  homotopy, or a stated reason it is out of scope.
- **Owner:** Co-scientist task (new).

### G-A12 — Projection of $D_{4}$ to three dimensions along irrational directions (IX.1.5): approximate icosahedral signature searched (finite window): ABSENT

- **Status/grade:** CLOSED-scoped (run 11, EXP-1117 / C-1117, adj-E4 2026-11-23). A nearest-icosahedral direction search was run in a finite window: $R=5$, $D_4$ root star S1 and diffraction star S2, angular power $l\le10$, metric $D$ = the non-icosahedrally-invariant fraction. The frozen rule ($\tau=0.05$) gives ABSENT. The best values found are $D^*_{S1}=0.5289539681$ at the irrational-looking family $(b,a,a,a)$, $b/a=4.30889\ldots$, and $D_{S2}\le0.4800$ about 0.2° from d110; at best about 47–52% of the anisotropic power is icosahedrally invariant. The $D_4$ star is not more icosahedral than random 4D 12-axis stars (43rd percentile). Track F F3 / Track E C, I1, rung 2; two code-independent routes on one binary. A sampled search, not a theorem.
  K2 (run 11, EXP-1118 / C-1118, adj-E8 2026-11-23): for the root-star signature S1 the ABSENT finding holds in **all** directions. For every unit $n\in S^3$, $D_{S1}(n)\ge LB_8(n)>0.05$ at $L=10$. Here $LB_8=(5T_2+9T_4+17T_8)/\sum_{l=2,4,\dots,10}(2l+1)T_l$; it is a rotation-free lower bound, valid because $I$ has no invariant harmonics at $l=2,4,8$. Method: a certified interval cover of a chart of the $W(F_4)$ chamber, with the d110 blow-up handled separately, done in two code- and binary-independent engines (CPython/numpy and C/gcc directed rounding), which agree; exact tiling check. Track F **F2**, I1, rung 3, [D]. Computer-assisted, not kernel-verified. Scope: S1 only, $L=10$, the EXP-1117 metric, $\tau=0.05$. S2 stays a sampled, window-dependent search (F3), so the overall G-A12 grade stays F3. Descriptive (C): $\inf_n LB_8\approx0.234$. That is not a bound on $D$. The sampled $D^*_{S1}=0.5290$.
  Earlier status (kept): the verified geometric-mapping part supports Track E **B / Track F F1 (PROPOSED)** (peak-ratios, Task 7: 41/41 VERIFIED across two bundles; $A_{1}$–$A_{4}$, $C_{1}$–$C_{4}$, $F_{1}$, $F_{2}$, $D_{1}$ agree to printed precision on both sides). The synthetic-discriminant reading supports B / F1, the measurable-discriminant reading stays C (post-hoc selection, I1, no detector/noise model, one normal).
- **What we know:** an *approximate* or finite-window icosahedral-like
  pattern is a separate, uncomputed question. Window counts (485/339/
  485/819 distinct positions; lattice fraction 249/1465 for irrational
  directions) are window-dependent (R = 5). Approximate/finite-window question now searched (above); exact icosahedral projection impossible ($5\nmid1152$, Task 1).
- **What would close it:** a nearest-icosahedral direction search in a
  finite window, or a stated reason it is not pursued.
- **Closed by:** EXP-1117 search (first option).
- **K2:** all-directions S1 bound certified (EXP-1118).
- **Owner:** Co-scientist task (new, small, local-cost).

### G-A13 — Are the 2-/8-mode quench outcomes transient?

- **Status/grade:** CLOSED (run 11, EXP-1114; F3 / Track E C, I1). The seed-4 2-mode state persists to $t=550$, deterministically and under annealing with $\Theta_0\in\{10^{-4},10^{-3},10^{-2}\}$, ramp 400, 3/3 replicas each. The seed-5 8-mode state is transient: it relaxes to a 2-mode state by $t=10$ (10/10 R1; verifier confirms) and never to the 6-mode. Both settle at $F_{exc}=-0.036540$, and the two end states are equivalent under a lattice symmetry plus a translation (adj-E6, residual $1.6\times10^{-15}$, ungraded). Energy ordering: 6-mode $-0.041772$ < 2-mode $-0.036540$ < 8-mode $-0.035767$, so the 2-mode is metastable at these noise levels. "2-mode" = half-max ndom 2 (a dominant pair plus 16 shell modes at 41.6%). The 6-mode sub-question: one 6-mode state (seed 3) is persistent under the same damped-wave continuation (R1 only). The first-pass (v1) continuations are void because of an anti-Hermitian roundoff defect. (Was: Open; no grade (untested).)
- **What we know:** quench seeds 4–5 (WS-C) reach 2-mode (Fexc
  $-0.036477)$ and 8-mode $(-0.035767)$ states; whether they anneal to the
  6-mode on longer runs is untested. Same question for the 6-mode
  quenches under the damped-wave dynamics (which drifts $\bar{\psi} \to +0.0025)$.
- **What would close it:** longer quenches / annealing runs from the
  2-/8-mode states.
- **Owner:** Co-scientist task / local Muse verification (small local
  runs).

### G-A14 — Barenblatt classification of the band edge: NOT ESTABLISHED

- **Status/grade:** ABSTAIN (WS-C task 7; no grade).
- **What we know:** the classification was attempted as part of the
  cross-domain synthesis (S5) and could not be established from the
  available material.
- **What would close it:** a Barenblatt-type analysis of the band edge,
  or a stated reason the classification does not apply.
- **Owner:** Co-scientist task / local Muse verification (analysis, no
  simulation needed).

### G-A15 — N = 24 grid point: run in run 11 (EXP-1116) — CLOSED (weak falsifier)

- **Status/grade:** CLOSED (run 11, EXP-1116 / C-1116). The falsification check passed, and it is a weak falsifier. Track F **F3**, I1, rung 2, [C], outcome confirmed. At $N=24$ the seeded in-phase $D_4$ attractor of the WS-C task-13 model gives $\langle A\rangle=0.0776817484$, $F_{exc}=-0.0077276236$ at dt $\in\{0.02,0.01,0.005,0.0025\}$. The model is sim6 Model B with $L=\pi$, $q_0^2=8$, $r=-0.35$, $u=v=1$, $\bar\psi=-0.18$, filter $K^2<200$, $T=30$. These values are within $10^{-6}$ of $0.077682/-0.007728$ in two code-independent routes on one binary (F3, I1), so the falsification check of G-A15 passed. Why it is a weak falsifier (SCOPING, not a theorem): $K^2=4|n|^2<200$ means $|n_i|\le7$; that ball lies wholly on every grid with $N\ge16$, so $N=16\to24$ changes only aliasing and roundoff, and the check tests the code and the fixed point, not continuum resolution-independence. Not shown: noise-started dynamics, other parameters, the transient order, or any manuscript claim. (Was: NOT RUN (WS-C task 13; choice ledger: cost/benefit; N = 20 already identical to N = 8).)
- **What we know:** the attractor fixed point is identical to 6 decimals over 8 ladder runs (7 distinct points): $N\in\{8,12,16,20\}$ at dt = 0.005 and dt $\in\{0.02,0.01,0.005,0.0025\}$ at $N=16$, + 4 runs at $N=24$ (all 4 dt): 12 runs, 11 distinct points, none beyond $10^{-6}$. (The earlier notation "$N \in \{8, 12, 16, 20\} \times$ dt $\in \{0.02, 0.01, 0.005, 0.0025\}$" was wrong: two 4-point ladders, not a product grid.)
- **What would close it:** running it (a falsification check only: a
  ladder point differing from $\langle A\rangle = 0.077682$ / Fexc = $-0.007728$ by more
  than 1e-6 would falsify resolution-independence; none found in 8
  points). Met in run 11 (none found in 12 runs).
- **Source location:** the task-13 code is NOT in the repo at 64bd065: `~/workspace/research/irh/co-scientist-tasks-2026-11-10/ws-c-substrate-convergence/code/irh_models.py` sha256 `f3755b6f710053c0938e717816dbdb256097ec88f37816900a3ce45a8c2fb0f3`, plus `task2a_attractor_ladder.py` sha256 `f412e9e9d88278b097c9b4da612bd476fca0b6dddbea1f849a803b50c3f5a7c9` (local Co-scientist package files, outside the repo).
- **Owner:** Local Muse verification; done in run 11 (VM run folder `/home/hatch/workspace/vertex-ai-run/session-2026-11-22/irh-run11`, bundle `bundles/G-A15_C-1116/`). Next check for F2 (not needed for closure): one $N=24$ point on a different binary or FFT library.

### G-A16 — Model B Hermitian artifact: fix verified, but the shipped sim6 file is unmodified and the manuscript's §I.2 equation still states the non-conserved form

- **Status/grade:** Diagnosis CLOSED (fix verified: stable to t = 30,
  $\langle A\rangle = 0.077682$, $D_{4} = 1.0000$, 24/24); the file/manuscript residue is
  OPEN.
- **What we know:** the shipped-style Model B update grows an
  anti-Hermitian roundoff component $\times1.0142$/step to NaN by ~6000 steps
  (found independently by WS-A and WS-C). Fix: per-step Hermitian
  symmetrisation/projection, an exact no-op in exact arithmetic. All
  package Model B results use the fixed stepper. The shipped sim6 file
  was NOT modified. The manuscript's §I.2 equation is the non-conserved
  form (see G-B7).
- **What would close it:** (a) the shipped sim6 file carrying the fix
  (a repo change — needs Brandon's approval, it changes delivered
  artifacts); (b) the manuscript's §I.2 equation corrected (G-B7).
- **Owner:** Brandon's call (file + manuscript text).

### G-A17 — "$\delta = 0.5$ kills the ordered branch" as a plane-wide claim — CLOSED (refuted as written, corrected)

- **Status/grade:** CLOSED. Corrected statement verified, grade C
  (WS-A task 3).
- **What we know:** TRUE at the operating point $(\bar{\psi}, r) = (-0.18, -0.35)$
  — discriminant < 0, matching the manuscript'$s q_{0}^{2} = 7.5$ result — but
  FALSE plane-wide: the band persists in-window at $\delta = 0.5 (8.18$% in
  W1), shifted to deeper r. The correct statement is the shift:
  detuning shifts the band by exactly $\delta^{2}$ in r (coexistence $-0.218 \to$
  $-0.468)$.
- **What closed it:** the exact root-finding + the in-window band
  measurement. Nothing further is needed except the manuscript (if ever
  revised) stating the shift rather than the plane-wide kill.
- **Owner:** None (closed). Manuscript wording, if revised, is
  Brandon's call.

### G-A18 — Thin-wall droplet estimate as the answer — CLOSED (shown to fail; ODE value stands)

- **Status/grade:** CLOSED. Thin-wall $R_{c} = 7.38 / \Delta F* = 37.2$, grade C
  (approximation shown to fail); ODE $R_{c} = 12.57 / \Delta F* = 555$, grade B
  (Summary §2, task 4).
- **What we know:** the correlation length $\xi = 8.64$ exceeds the
  thin-wall radius, so the thin-wall separation of volume gain and
  surface cost breaks down; the exact barrier is ~$15\times$ the thin-wall
  value. The thin-wall numbers are retained as the (failed)
  approximation, not the answer.
- **What closed it:** the $\xi > R_{c}$ comparison + the exact radial-ODE
  computation. The remaining open item is the full-PDE refinement
  (G-A10), not the thin-wall question itself.
- **Owner:** None (closed).

### G-A19 — Full (relaxed) free-energy band computation: band edges would shift ~1%

- **Status/grade:** Open; no grade (uncomputed refinement).
- **What we know:** the one-mode ansatz is 1.2% above the relaxed free
  energy at the operating point $(-0.0076323$ vs $-0.0077276)$; the band
  edges in WS-A task 3 and WS-C task 7 rest on the one-mode functional.
  The qualitative picture (detuning shift $\delta^{2}, w_{6}$ narrowing) would not
  change.
- **What would close it:** a band recomputation against relaxed
  (fully nonlinear) free energies.
- **Owner:** Co-scientist task (costed first; heavier than the one-mode
  map).

### G-A20 — No $A_{4}$* control simulated; no preregistered competitor set, no $\geq10$ seeds, no commensurate cells (Hark R4) [PARTIAL — exact-combinatorics + matched-pure-branch part VERIFIED (Track E B / Track F F1) — Batch 2 audit 2026-11-12]

- **Status/grade:** PARTIAL. The exact-combinatorics and matched-pure-branch part is VERIFIED (Track E B / Track F F1). The dynamical-competition, nucleation, and unbiased-emergence parts stay OPEN. No grade on the scope gap itself (a scope gap, not a failed claim).
- **What we know:** every simulation box is $L = \pi$ hypercubic; no $A_{4}$*
  (or 600-cell / 2O) control was simulated; no preregistered competitor
  set, no $\geq10$ seeds, no commensurate cells. $A_{4}$* is the manuscript's
  closest analytic rival (S = 12/31 vs $D_{4}$'s 64/141, margin $73/423 \approx$
  17.26%). The "Step 1.2 remains needed" citation is unlocated (see
  G-E3) — the need itself is real, the citation is not verifiable.
  **LANDED and audited 2026-11-12** (chat `e4600980-420b-41dc-8dda-67596411cec5`,
  COMPLETED; `AUDIT_batch2_2026-11-12.md`: 23 claims — 16 VERIFIED, 6
  UNVERIFIED, 1 REFUTED). The `methods.md` record is clean and fully
  verified (audit re-ran `reproduce.py`, exit 0; the 90,024-row scan table
  reproduces exactly, max abs diff 0.0). But the chat's final message
  overstates the record (D-A20-1–D-A20-7): six claims UNVERIFIED — onset
  range 0.0301–0.0434, "240 relevant wave states", fitted onset
  $0.0399 \pm 0.0003$, observed critical point $0.0329 \pm 0.0017$ / max
  0.0355, "only stable endpoint / every perturbation relaxed", "coplanar
  triplet branch to $r = -0.35$" — and one REFUTED as phrased: "the $A_4^*$
  branch does not exist on $24^4$/$28^4$ grids" (no such grids in the
  record; the branch exists in the scan, 7,765 rows). **Those final-message
  numbers must be struck from any summary of A20.** (Spot-check note:
  the onset digits do occur as raw data values in the scan/boundaries
  tables; the audit's "appear nowhere" means nowhere as stated results.)
  **2026-11-14 identity finding (material):** `matched-branches/` is **byte-identical to the Batch 2 `a20-onset/` record** — every data file matches (scan-table sha256 `da415b0c…`, same reproduction zip); `methods.md` differs only in LaTeX-delimiter style. This is a re-audit of the same record under a new task name, **not** a second independent delivery; it adds no new evidence beyond Batch 2. New in the 2026-11-14 audit: the rebuild-2 vs original-PDF check (unchanged — VERIFIED) and a fresh independent re-derivation + rerun (exit 0; 90,024-row scan max diff $0.0$). The chat-final-message numbers (onset $0.0301$–$0.0434$, $0.0399 \pm 0.0003$, $0.0329 \pm 0.0017$ / $0.0355$) remain UNVERIFIED and must be struck from any summary; the '$A_{4}^{*}$ branch does not exist on $24^{4}$/$28^{4}$ grids' phrasing remains REFUTED as phrased (branch exists in 7,765 scan rows).
- **What would close it (in part):** the candidate task "Calculate
  matched $D_{4}$ and $A_{4}$* onset branches" (Academia 2026-11-12 email) — both
  candidates on the same normalized amplitude / shell-penalty footing.
  **LANDED and audited 2026-11-12** (exact part VERIFIED; dynamical parts
  open). A full fair test (preregistered competitor set, $\geq10$ seeds,
  commensurate cells, $A_{4}$* control in a box that can hold it) is a larger
  programme item.
- **Owner:** Co-scientist task (LANDED, audited 2026-11-12) for the onset branches; the full fair test is a
  programme-scale item to be scoped and costed.

### G-A21 (proposed) — F-LOCAL-1: the local solver's physical cap is $|k|^{2} \leq 64$, so the GCP '$K=6$ full study' never widened the $A_{4}^{*}$ band

- **Status/grade:** Open; no grade (unverified, not a failed claim).
- **What we know:** the local solver's physical cap is hardcoded at $|k|^{2} \leq 64$, so the GCP '$K=6$' energies are identical to $K=4$ to 15 figures — trap robustness to a genuinely wider band is still UNVERIFIED.
- **What would close it:** a rerun with a genuinely wider band (cap raised), costed first.
- **Owner:** Local Muse verification (small local runs) / Co-scientist task.

### G-A22 (proposed 2026-11-17, filed) — McKay gauge-dynamics gap: v94 never derives a Yang–Mills kinetic term for $E_6$ from the tension–relaxation Lagrangian, nor Higgs representations for $E_6 \to SU(3)_C \times SU(2)_L \times U(1)_Y$ without light exotic relics

- **Status/grade:** Open; no grade (unverified, not a failed claim).
- **What we know:** v94 identifies $E_6$ as "the gauge algebra" by McKay identification (2T ↔ affine $E_6$) but never derives a Yang–Mills kinetic term $\frac14 F^a_{\mu\nu}F^{a\mu\nu}$ for $E_6$ from the Lagrangian. The deepest-research cross-domain synthesis (2026-11-17) finds the bridge does not exist anywhere in the literature either (scoped absence, C/I1): McKay gives a label; Kronheimer/quiver constructions give $\prod_i U(n_i)$; every $E_6$ dynamics route imports the kinetic term from elsewhere (DBI action, 11D supergravity, dilaton VEV). $E_6 \to$ SM breaking always costs Higgs representations plus light exotics or fine-tuning (B/I2).
- **What would close it:** (a) a construction of the kinetic term inside IRH's own Lagrangian, (b) an Ali-style root-sum postulate labelled as such (grade D, post-hoc), or (c) downgrading "the gauge algebra" to "the gauge-algebra label" in the manuscript.
- **Owner:** Brandon's call (construction vs scope decision); Local Muse verification (literature).

### G-A23 (proposed 2026-11-17, filed) — §III.4 $d = 4$ marginality wording + Model B label + Derrick wording

- **Status/grade:** Open; wording corrections, no grade moves follow from the fixes alone.
- **What we know:** the RG gloss ("exactly marginal," "RG-irrelevant") is contradicted by the isotropic-Lifshitz literature ($d_u = 8$, not 4; fluctuations relevant at $d = 4$, Brazovskii 1975); only tree-level scaling $\lambda^{4-d}$ survives (B/I1). The headline damped-wave equation is not Model B; "Kerr solitons" is nonstandard for Derrick.
- **What would close it:** reword §III.4 to tree-level Derrick scaling; restrict "Model B" to the conserved variant; correct the Derrick wording.
- **Owner:** Local Muse verification (manuscript edit).

### G-A24 (proposed 2026-11-17, filed) — §IX.3 Greensite misattribution + classical-substrate sentence + G-C20 overstatement

- **Status/grade:** Open; corrections + grade challenge. The §IX.3 sentence corrections are FILED in the v94 2026-11-17 patch (see G-C20); the G-C20 grade challenge is adjudicated there (B/F2 kept for the calculation recovery, D = 4 uniqueness qualified).
- **What we know:** the one-loop $n_F > n_B$ condition was attributed to [17][18] (classical clock-field papers) instead of [41][42]; "no purely classical Euclidean substrate is known…" was false as stated (Mukohyama–Uzan 2013); G-C20 "verified, $D = 4$ uniqueness" (B/F2) was overstated — at most C/I1 for the calculation as reported, with the $D = 6$ broken-SUSY qualifier (synthesis challenge; adjudication under G-C20).
- **What would close it:** the citation fix and sentence narrowing (done in the patch); the remaining wording (D = 6 qualifier) is filed in the patch.
- **Owner:** Local Muse verification (manuscript edit — done 2026-11-17).

### G-A25 (proposed 2026-11-17, filed) — §II.5 Elitzur gloss + missing citations

- **Status/grade:** Open; corrections, no grade moves follow from the fixes alone.
- **What we know:** the $(\pm1,\pm1,\pm1,\pm1)$ / $D_4$ gloss misstates Elitzur 2011 (needs the isoduality step $D_4^* \cong D_4$ and the correct vectors); Lifshitz–Petrich 1997 and Klein 2001 are uncited though directly relevant.
- **What would close it:** correct §II.5; add both citations with the Klein scope note.
- **Owner:** Local Muse verification (manuscript edit).

### G-A26 (proposed 2026-11-17, filed) — Bell disjunction incompleteness (v94:962)

- **Status/grade:** Open; wording, no grade moves follow from the fix alone.
- **What we know:** "nonlocality or superdeterminism" omits giving up realism/single outcomes (many-worlds, QBism) and retrocausality; superdeterminism is a programme proposal (Hossenfelder–Palmer 2020), not a constructed model.
- **What would close it:** complete the disjunction or justify the restriction.
- **Owner:** Local Muse verification (manuscript edit).

## Group B — Substrate models and dynamics convergence

Manuscript sections: §I.1–I.3 (substrate, dynamics, conserved Model B),
§II (selection). Tasks: WS-C 7+13. Cross-cutting: Hark F1/F2/F4, guide
§8.2, §8.3 (B1).

### G-B1 — The reference $\bar{\psi}$-drift value 8.3e-17 is not re-measured at full precision

- **Status/grade:** PARTIAL, grade C (WS-C task 13, C2.5 conservation
  leg).
- **What we know:** best measurement 1.1e-15 at t = 7.5 (projection on),
  one order coarser than the reference 8.3e-17; P5 (< 1e-12) PASS with
  drift 1.58e-15 at t = 30. The unprojected run's drift is 0.0 even at
  t = 27 (k = 0 mode exactly conserved; blow-up is in the anti-Hermitian
  sector). Projection costs ~1e-15 of conservation and buys stability
  to t = 30.
- **What would close it:** a full-precision re-measurement of the
  *unprojected* shipped sim6 run'$s \bar{\psi}$ drift at t = 7.5, to settle whether
  the reference 8.3e-17 is reproduced (guide §12 Q5).
- **Owner:** Local Muse verification (small local run).

### G-B2 — F4 provenance gap: task2d / make_figures (T = 0.5/1.0 rows not regenerable)

- **Status/grade:** PROVENANCE GAP (numbers stand). Hark F4 VERIFIED by
  the reviewer's own re-run.
- **What we know:** `task2d_transient.py` runs T = 5 only and overwrites
  the CSV with mode `'w'`; the shipped CSV's T = 0.5/1.0 rows carry
  `seconds=0` (not produced by this script); `make_figures.py` line 85
  filters `r["T"] == "0.5"` and line 88 indexes `err[-1]` — after a clean
  task2d re-run it crashes (`IndexError` at line 88). The numbers stand
  (shipped T = 0.5 rows match Hark's regenerated values exactly;
  $p \approx 0.95$ stands). This breaks guide §9 as written (the guide is
  corrected; the scripts are not).
- **What would close it:** ship the T = 0.5/1.0 rows or regenerate them
  in-script — a fix to the workstream artifacts.
- **Owner:** **Brandon's call** (offered in the Hark review; not done).
  Not closable by the programme alone.

### G-B3 — F2 lock-metric defect (ill-defined for partial patterns)

- **Status/grade:** DEFECT, minor (Hark F2 VERIFIED by code reading).
  Numbers stand; no load-bearing conclusion rests on the sub-pattern
  lock value.
- **What we know:** `d4model.analyze` averages cos S over all 32 triads
  including roundoff modes, so the metric is platform-dependent for
  partial patterns (hex6 0.304 / 0.455 vs shipped 1.000). The fix
  (restrict to triads with all three modes active; `active_lock` gives
  1.000 for hex6/fcc12/full) is correct.
- **What would close it:** applying the fix to `d4model.analyze` — a
  change to the workstream code.
- **Owner:** **Brandon's call** (offered; not done).

### G-B4 — WS-A task-1 JSON provenance gap (extra fields from another script revision)

- **Status/grade:** PROVENANCE GAP, minor (numbers stand). Hark §1
  VERIFIED by the reviewer's own re-run.
- **What we know:** the shipped JSON carries `n_distinct_positions` /
  `max_multiplicity`, which the shipped script does not write — it came
  from another script revision. Hark's "different lattice basis" did NOT
  reproduce in the reviewer's env (NumPy 2.4.6 vs 2.5.4) —
  environment-dependent, no number changes.
- **What would close it:** re-ship the JSON from the current script or
  record the revision.
- **Owner:** **Brandon's call** (offered; not done).

### G-B5 — Hoy [40] Lennard-Jones MD leg of C1.6: NOT RUN

- **Status/grade:** NOT RUN (abstention A5, WS-C task 7).
- **What we know:** C1.6 ("Landau + LJ corroborate the winner") rests on
  the manuscript-reported Hoy result for its LJ leg; the re-simulation
  was not attempted. The S4 split verdict (combinatorial PASS, scope
  FAIL) stands without it.
- **What would close it:** a re-simulation of the Hoy LJ-MD result, or
  a stated decision to take it as manuscript-reported.
- **Owner:** Co-scientist task / local Muse verification (costed first).

### G-B6 — Lean re-verification of the new WS-C claims: NOT RUN

- **Status/grade:** NOT RUN (abstention, WS-C task 7).
- **What we know:** no Lean work was done in this programme; the WS-C
  claims are simulation/exact-computation claims (Track E C / Track F
  F2–F3), not kernel claims.
- **What would close it:** a Lean formalization of the WS-C claims that
  admit one (e.g. the shell combinatorics, the $a_{0}$/CFL identities).
  Note: this is GGHV-programme-adjacent work, not IRH work; it competes
  for the same Lean capacity.
- **Owner:** Local Muse verification (Lean; scoped and costed first).

### G-B7 — Manuscript §I.2 is internally inconsistent (non-conserved RHS vs conserved requirement)

- **Status/grade:** SUBSTANTIATED on the manuscript text (Hark B1).
  No grade (a manuscript-text finding, not a computation).
- **What we know:** §I.2 (lines 185–191) states the dynamical equation
  as $\partial^{2}_{t}\psi + \gamma\partial_{t}\psi = **-\delta F/\delta\psi$** — a damped wave equation with a
  NON-conserved right-hand side — and §I.3 (lines 215–219) then derives
  that conserved dynamics is a requirement, citing Model B
  $\partial_{t}\psi = \nabla^{2}(\delta F/\delta\psi)$ preserving the mean to 8.3e-17. The manuscript's own
  §I.2 is therefore internally inconsistent: its stated equation is not
  the conserved dynamics its simulations use. The conserved-MPFC form
  $\partial^{2}_{t}\psi + \gamma\partial_{t}\psi = \nabla^{2}\delta F/\delta\psi$ appears in NEITHER the manuscript nor the
  package. Hark's citation "REVISION_PLAN 1.1" is unlocated (see G-E3)
  — the substance stands on the manuscript text; the citation does not.
- **What would close it:** a manuscript correction stating the
  conserved-MPFC form (or the Model B form actually simulated).
- **Owner:** **Brandon's call** (manuscript text). Not closable by the
  programme.

### G-B8 — The common-tangent diagram is still fixed-$\bar{\psi}$

- **Status/grade:** SUBSTANTIATED (Hark review §4).
- **What we know:** the package does fixed-$\bar{\psi}$ minimisation everywhere
  (WS-A task 3, WS-C task 7); no coexistence-aware common-tangent
  construction was done.
- **What would close it:** a common-tangent construction at coexistence
  $(r_{coex} = -0.217984$ at $\bar{\psi} = -0.18$ is known from two independent routes).
- **Owner:** Co-scientist task (new, analysis + small computation).

### G-B9 — Near-melting scope transfer (S4): combinatorial transfer PASSES, scope transfer FAILS — CLOSED as a split verdict

- **Status/grade:** CLOSED. Split verdict, grade C (WS-C task 7, C1.6).
- **What we know:** the S-criterion's combinatorial selection transfer
  $(3D\to4D)$ PASSES; the near-melting equilibrium scope transfer FAILS — a
  scope restriction, not a defect. The LJ$\to$field transportability audit
  likewise finds NOT transport (LJ carries an irreducible sC-component:
  particle identity, pair potential); independent corroboration only.
- **What closed it:** the split verdict itself, recorded with its scope.
  Nothing further is needed; the restriction must be cited whenever the
  transfer is invoked.
- **Owner:** None (closed).

---

## Group C — Frameworks, rivals, constants, and gravity

Manuscript sections: §V (3D validation, defects), §VII (retractions),
§VIII (selection principle), §IX.2–IX.4 (modelling decisions, external
structure, restarts). Tasks: WS-D 8, 9, 10, 12; WS-E 14 (map). Also the
torus-node comparison §7.3.

### G-C1 — No framework derives signature + Einstein + diffeomorphism invariance + SM gauge + a confirmed prediction together

- **Status/grade:** Survey COMPLETE as a draft (WS-D task 8, grade C);
  the physics gap itself is OPEN.
- **What we know:** each framework derives/postulates a different subset
  and fails, is silent, or is untested on at least one other. CDT has
  the strongest *derived* emergence result; causal sets have the only
  prediction-in-advance (Sorkin $1997 \Lambda \sim 10^{-120}$, pre-1998); LQG's
  sharpest derived result is kinematic; AdS/CFT is unproved; asymptotic
  safety's fixed point is truncation-only evidence; GFT's
  condensate-as-GR-geometry step is unestablished. IRH is narrowest and
  most checked at the geometric level (Grade A carried) while its gravity
  side is open or retracted by its own Part IX.
- **What would close it:** a derivation (by any framework, IRH included)
  of all four at once. The survey being complete does not close the
  physics gap — it only records exactly where every framework stands.
- **Owner:** Literature / external (a derivation, not a computation).
  The torus-node paper is a new candidate for the comparison (see G-C14).

### G-C2 — Lorentzian signature mechanism (IX.3.1)

- **Status/grade:** OPEN (repo register). Transfers FAIL (WS-D tasks 8,
  9, 12, Bartha S4).
- **What we know:** published routes [17][18] need a 1-loop effective
  potential with more fermionic than bosonic DOF (Greensite [41],
  Carlini–Greensite [42]). No purely classical Euclidean substrate is
  known to work. Greensite transfer into IRH FAILS (quantised phase
  field, one-loop potential, fermion dominance all in the Negative
  Analogy); Mukohyama–Uzan/Kehayias clock-field transfer FAILS (clock
  field, fine-tuned coupling, Galileon-not-GR gravity). "Dynamical
  signature $\Rightarrow$ IRH reading (A)" FAILS for v93.1 (fermion-dominant loop
  absent from a single real scalar).
- **What would close it:** a signature mechanism stated for IRH's single
  classical scalar substrate, or a stated replacement; deciding §IX.2
  (G-C8) is a prerequisite for any signature comparison (task 12, D7).
- **Owner:** Co-scientist task (new) / literature / external.

### G-C3 — Einstein field equations (IX.3.2)

- **Status/grade:** OPEN (repo register). Transfers FAIL (WS-D tasks 8,
  9, 12, Bartha S4).
- **What we know:** beyond analog gravity [16]: diffeomorphism
  invariance, Bianchi identity, universal coupling to conserved
  stress-energy, two transverse-traceless graviton polarizations. Analog
  models give effective curvature, not GR [19]. "Jacobson $\Rightarrow$ IRH
  transport" FAILS / NOT ESTABLISHED (thermodynamic premises $S \propto A$,
  $\delta Q = T$ dS, local equilibrium have no positive analogue in IRH).
  IRH v93.1's own Part VII retraction stands, confirmed against
  Barceló–Liberati–Visser 2011 and Sindoni 2012.
- **What would close it:** a derivation of the Einstein equations (with
  diffeomorphism invariance and the two TT polarizations) from the IRH
  substrate, or a stated replacement.
- **Owner:** Co-scientist task (new) / literature / external. This is
  also task 15's blocker B3 (see G-D4).

### G-C4 — QM beyond single-particle envelopes (IX.3.3): a boundary, not a gap — RECORDED

- **Status/grade:** OPEN in the register as an acknowledged boundary.
  Not counted as a closable gap.
- **What we know:** entanglement / Bell-violating correlations from a
  classical substrate require nonlocality or superdeterminism [38].
  The manuscript itself frames it as a boundary.
- **What would close it:** nothing within the programme — a boundary is
  recorded, not closed. Any future claim to cross it needs a stated
  mechanism (nonlocality or superdeterminism) and is a programme-scale
  decision.
- **Owner:** None (recorded boundary).

### G-C5 — Monopole resolution (IX.3.4 / §V.3)

- **Status/grade:** OPEN (repo register); ABSTAIN on any relic-density
  number (WS-E task 15, C5).
- **What we know:** §V.3 (lines 1086–1090) names the standard
  resolution — "inflationary dilution, or a breaking pattern avoiding
  the relevant topology" — but derives neither. VI.7 predicts monopoles,
  not their absence. No photon/baryon coupling is stated, so no
  relic-density number can be derived.
- **What would close it:** a stated dilution factor or breaking pattern
  turning the named resolution into a relic-density prediction (task 15
  requirements list, item 9).
- **Owner:** Brandon's call (manuscript: state the mechanism$) \to$
  Co-scientist task (forward-model it once stated).

### G-C6 — $E_{6}$ breaking pattern and Higgs sector (IX.4.1): not derived at all

- **Status/grade:** OPEN (repo register). No grade (unattempted).
- **What we know:** the $E_{6}$ identification via 2T/McKay is mathematics
  grade A (carried); the physical reading is grade D (Hark F6 — see
  Summary §0.1). "IRH'$s E_{6}$ identification derives coupling values / $\alpha$"
  FAILED (WS-D task 9, F4): no breaking pattern, no RG running (§IX.4).
- **What would close it:** a breaking pattern and Higgs sector derived
  (or a stated reason they are out of scope for v93.1).
- **Owner:** Co-scientist task (new, programme-scale) / literature.

### G-C7 — Higgs VEV, $A_{3}$ resonance mass and widths, CKM mixing (IX.4.2): clean restart

- **Status/grade:** OPEN (repo register). No grade (unattempted).
- **What we know:** "Nothing from the prior calculations is carried
  forward (computed in an excluded framework, with independent arithmetic
  errors)."
- **What would close it:** a clean-restart computation of the VEV, $A_{3}$
  mass/widths, and CKM mixing in the v93.1 framework.
- **Owner:** Co-scientist task (new, programme-scale).

### G-C8 — The dimensional assignment (IX.2.1): three mutually exclusive readings, undecided

- **Status/grade:** OPEN — decision required (repo register). "Must be
  decided; not resolvable by further calculation."
- **What we know:** (A) base is Euclidean spacetime with dynamical
  signature; (B) four spatial dimensions with one compactified; (C)
  auxiliary base with spacetime from defect dynamics. WS-D task 9 (C3,
  grade C) and task 12 (D7) both record it as undecided; it gates every
  signature comparison and task 15's blockers B2/B3.
- **What would close it:** Brandon's decision between (A), (B), (C).
- **Owner:** **Brandon's call alone.** Not closable by the programme.

### G-C9 — Generation count as acknowledged input wherever fermion content is discussed (IX.2.2): standing rule — RECORDED

- **Status/grade:** OPEN in the register as a standing rule. Not counted
  as a closable gap.
- **What we know:** three generations are INPUT, not derived (also in the
  torus comparison: three generations = vacuum data on BOTH sides).
  The rule is to state it as an input wherever fermion content is
  discussed.
- **What would close it:** nothing within the programme — a derivation of
  the generation count would be a programme-scale result, not a gap
  closure. The rule is recorded, not closed.
- **Owner:** None (standing rule).

### G-C10 — The $\alpha$ ansatz ($137 + 1/(28 - \pi/14))$: arithmetic exact, derivation absent

- **Status/grade:** Grade D (ansatz only; WS-D tasks 9, 10, 12).
  Arithmetic verified exactly; derivation absent.
- **What we know:** $\alpha^{-1}$ ansatz = 137.036002821941; CODATA $2022 \alpha^{-1}$ =
  137.035999177(21); difference +$3.64\times10^{-6} (\approx 27$ ppb; ~$174\sigma$; rel
  $2.660\times10^{-8}$; flint.arb $3.6449411\times10^{-6})$. Downgraded numerical ansatz in
  the Eddington class. "No surveyed rival derives $\alpha$" (task 9, C7) is C
  scoped / UNVERIFIED as a universal negative (see G-C18). Eddington's
  own derivation of $\alpha$ FAILED by measurement (historical control; $\alpha^{-1}$ is
  not an integer).
- **What would close it:** a derivation of $\alpha ($or of the ansatz's
  $1/(28 - \pi/14)$ term) from the IRH substrate, or a stated replacement /
  withdrawal of the ansatz.
- **Owner:** Co-scientist task (new) / Brandon's call (keep, replace, or
  withdraw the ansatz).

### G-C11 — R = 2589: ABSTAIN (no derivation inputs in the source)

- **Status/grade:** ABSTAIN (WS-D task 10, D18; no grade). The manuscript
  itself already downgrades it.
- **What we know:** no derivation inputs in the source; "the subtraction
  of 3 is not forced by any displayed symmetry"; arithmetic
  unverifiable-from-source, carried as downgraded, not re-derived
  (WS-D task 9).
- **What would close it:** the manuscript stating the derivation inputs,
  or dropping the number.
- **Owner:** Brandon's call (manuscript text).

### G-C12 — Printed dispersion relation (7): WITHDRAWN — the "wrong as printed" finding was a misreading; no erratum needed

- **Status/grade:** CLOSED (run 11, 2026-11-22) — no erratum needed. WS-D task 10 D5 REFUTED as a pdftotext misreading (superscript of $a_0^2$ read as a factor 2). Printed (7) equals the EOM-derived dispersion (Singular + Wolfram, F2/I1). v94 (7) is byte-identical to v93.1 (7). Source: run-11 adjudication `G-C12_trace.md` (and G-E8, T10-11 refuted). Downstream WS-D items T10-12, T10-14, T10-16, T10-39 hold only as algebra on the misread form. (Was: FAILED as printed (WS-D task 10, D5, grade C); the gap that remained was the erratum.)
- **What we know (WITHDRAWN as a finding; kept as history — this text rests on the misreading):** EOM-derived formula:
  $\sin^{2}(\omega\Delta t/2) = (\Delta t^{2}\cdot2J/(4M$\*$a_{0}^{2}))\cdot\Sigma_{\alpha}(1-\cos(a_{0}k\cdot\alpha))$ +
  $(\Delta t^{2}\mu^{2})/(4M$\*); printed (7) has $[2\Sigma_{\alpha}(1-\cos(a_{0}k\cdot\alpha)) + \mu^{2}]$ inside one
  bracket — factor of 2 too many in the $\Sigma$ term, $\mu^{2}$ misplaced. Three
  internal checks favour the derived formula (J = M\*$c^{2}/12$, the k = 0
  limit, the CFL table), and the manuscript's own §III.2 expansion uses
  the derived formula. The CFL bound computed from it is VERIFIED.
  Erratum: replace $[2\Sigma(1-\cos) + \mu^{2}]$ by $[\Sigma(1-\cos)]$ with the $\mu^{2}$ term
  outside the bracket at coefficient $\Delta t^{2}/(4M$\*).
- **What would close it:** filing the erratum. (Moot: no erratum is needed.) Withdrawal notes, not silent patches, are owed in the six documents that repeat the misread statement (listed in `programme/RECORD_FIXES_run12.md`).
- **Owner:** Brandon informed, not deciding (it reverses an item he was told was an erratum). Was: Brandon's call (guide §12 Q8).

### G-C13 — §III.3 envelope validity table does not reproduce: UNVERIFIED

- **Status/grade:** UNVERIFIED, not FAILED (WS-D task 10, D17).
- **What we know:** table $(4\times10^{-5}, 0.1$%, 1.0%, 11%, 133%) NOT
  REPRODUCIBLE; under the natural reading computed errors are $1.67\times10^{-5}$,
  $4.17\times10^{-4}$, $3.75\times10^{-3}$, 4.11%, 36.3% $(\Delta t\to0)$ — smaller by factors
  2.4–3.7; zone-edge 133% unreachable under that reading. The VI.3
  summary boundary (<1% for $a_{0}$|k| ≲ 0.3) survives the recomputation
  (0.042% at 0.10, 0.375% at 0.30). The table'$s \Delta t$, carrier $\theta ($or $\mu)$,
  direction, and error definition are unstated.
- **What would close it:** the author stating $\Delta t$, $\theta ($or $\mu)$, direction,
  and error definition for the table (guide §12 Q9).
- **Owner:** **Brandon's call** (he is the manuscript's author).

### G-C14 — The torus-node paper as a task-8 ledger entry

- **Status/grade:** Open; proposed entry grade $\leq C ($conditional chain,
  I1) if added (torus comparison §7.3 Q4).
- **What we know:** Youngik (Tom) Lee, "A Torus-Node Model for Emergent
  Spacetime, Gravity, and Gauge Structure", 190 pp., dated 2026-11-06.
  It is the first $D_{4}$-based emergent-spacetime rival not retrieved by
  task 14 (its 73 papers contain no torus-node mention; the paper never
  cites IRH, grep-verified). Headline: same $D_{4}$ mathematics (24 roots,
  24-cell 5-design, |$W(D_{4})$| = 192, |$W(F_{4})$| = 1152, $S_{4}$ fibre —
  checker-verified), opposite method: torus DECLARES $D_{4}$ + weights
  $(\beta = 1) + a 49$-mark completion package and derives a conditional
  downstream chain; IRH SELECTS $D_{4}$ dynamically (S = 64/141) and derives
  nothing downstream. No IRH grade changes. Checker (5 scripts, exit 0;
  123 PASS / 7 FAIL): F2 most consequential — eq. (5.5) gives
  $c_{2}^{b}(1) = 1.8446\times10^{-5}$, $54\times$ below stated ~$10^{-3}$, breaking the entropy
  ratio R = 1.05 (would be $\approx59.4)$; headline top-mass bound 173.0–173.9
  GeV UNVERIFIED (pipeline not reproducible from text). Three generations
  = vacuum data on BOTH sides; torus No-go 7.11 (triality gives no spinor
  law) corroborates IRH's Axiom-D independence.
- **What would close it:** recording the paper as a new candidate in the
  task-8 comparison ("no framework derives signature + Einstein +
  diffeomorphism invariance + SM gauge + a confirmed prediction
  together") — conditional, finite-model, couplings unfixed.
- **Owner:** **Brandon's call** (whether to add it).

### G-C15 — The $D_{4}$ bridge (torus §7.3 Q1): derive the torus weights from IRH triad interference, or IRH's S from a Poisson node source

- **Status/grade:** Open; the single most valuable follow-up in the
  torus comparison — **the only question whose answer could change a
  grade on either side**.
- **What we know:** torus declares $D_{4}$ + weights w(r) = 2^$(-t(r))$,
  $\beta = 1 ($Remark 3.8, declared inputs) and derives consequences (4D, one
  time axis, $S_{4})$; IRH derives $D_{4}$ selection from a criterion $(S = \tau^{2}/q_{4})$
  and declares only the $q_{0}$ tuning. Neither derives the other'$s D_{4}$.
  The torus paper is the first rival in this programme to use $D_{4}$ as a
  *declared* source rather than a *selected* outcome; it sharpens what
  IRH's selection claim actually buys.
- **What would close it:** a derivation either way — torus weights from
  IRH's triad-interference criterion, or IRH's S from a Poisson node
  source — graded on arrival.
- **Owner:** Co-scientist task / local Muse verification (research task;
  Brandon's call on whether to pursue it).

### G-C16 — Torus App. H files and the F2 fork (torus §7.3 Q2/Q3)

- **Status/grade:** Open; bounded next step, no author contact needed.
- **What we know:** the paper's reproducibility package lists
  `top_mass_bound.py`, `exact_gauge_matching.cjs`, `higgs_stability.py`
  and logs (App. H, Table 24). Checking those files against the text
  would resolve U1/U2 (the unverified top-mass bound and related items)
  without author contact. The F2 fork: is (5.5) misprinted, or is $c_{2}$ in
  Num. result 5.6 a different normalisation? The answer decides whether
  R = 1.05 stands. A one-equation clarification from the text's own terms
  (or the App. H `black_hole_entropy.py` log) would settle it. The files
  are in the paper's public repo/archive (github.com/s6ygleee/torus-node-lean4,
  Zenodo doi:10.5281/zenodo.23863514) — recorded, NOT fetched. Nanoda
  batch count (21 vs 11) is a minor provenance inconsistency, not
  load-bearing.
- **What would close it:** fetch and check the App. H files against the
  text.
- **Owner:** Local Muse verification (fetch public repo/archive; read
  only, no contact).

### G-C17 — WS-$D F3\to F2$ question: should the Hark two-route logic lift task-12 G1/G5/G8/G12 to F2? — CLOSED (regraded F2, 2026-11-12)

- **Status/grade:** CLOSED. G1/G5/G8/G12 are **F2** (was F3).
- **What we know:** the Hark regrade table covers only WS-A/WS-C/WS-E
  claims; task 12 is not in it (WS-D was not in the audited package).
  Task 12's own grading (§7) already notes the two-tool basis ("2
  independent tools $\to F2$; ceiling F3 cap applies (human gates not run$) \to$
  min(F2, F3) = F3"). The only thing holding them at F3 was the §6.5
  human-gate ceiling. Brandon repealed the §6.5 human-gate requirement
  on 2026-11-12 14:07 CST, in conversation, from his assessment and all
  future assessments (amendment note
  `HLRE-6-5-HUMAN-GATE-REPEAL-2026-11-12.md`). The repeal extends the
  Hark amendment's scope to WS-D, so the ceiling is gone and the
  two-tool basis carries them to F2. The amendment's provenance caveat
  (G-E4) is closed by the same act.
- **What would close it:** done — repeal + regrade, 2026-11-12.
- **Owner:** closed.

### G-C18 — "No rival derives $\alpha$" as a universal negative: C scoped / UNVERIFIED as universal

- **Status/grade:** C scoped / UNVERIFIED as a universal negative (WS-D
  task 9, C7).
- **What we know:** verified for surveyed sources only; a universal
  negative cannot be proved over all literature. No surveyed rival
  derives $\alpha$; neither does IRH (see G-C10).
- **What would close it:** it cannot be closed by a finite survey — only
  bounded. A retrieved counterexample (a framework deriving $\alpha)$ would
  overturn it; otherwise it stays scoped.
- **Owner:** Literature (retrieval watch).

### G-C19 — Ġ/G bound: ABSTAIN (no verified primary-source constraint)

- **Status/grade:** ABSTAIN (WS-D task 12, D3; no grade). No verdict on
  Dirac varying-G.
- **What we know:** no verified primary-source Ġ/G constraint was found
  in the run (lunar laser ranging not verified from a primary source).
  Dirac's arithmetic (Ġ/$G = -1/t; -7.25\times10^{-11}$/yr at $t_{0} = 13.8$ Gyr) is
  verified as arithmetic (G8, F3); |Dirac Ġ/G| is ~$3\times10^{6}\times$ the Rosenband
  $\alpha$ scale — different observables, not a falsification of Dirac.
- **What would close it:** a verified primary-source Ġ/G constraint
  (e.g. lunar laser ranging from the primary source).
- **Owner:** Literature (retrieval).

### G-C20 — Full Greensite one-loop mechanism — RESOLVED at B / F2 (decided; adjudicated 2026-11-17)

- **Status/grade:** RESOLVED at Track E B / Track F F2 (decided). Calculation recovery: the exact one-loop potential $V(\theta)$ recovered and re-derived locally (SymPy, exact; sweep-4 audit 2026-11-12); D = 4 uniqueness Cases I–V verified; §5 mass effects and the D = 6 broken-SUSY exception verified; heat-kernel regularization premise ledgered (argued, not proved).
- **Adjudication 2026-11-17 (Brandon: all decisions authorized):** the deepest-research cross-domain synthesis (2026-11-17) challenged B/F2 to at most C/I1, citing Greensite's own hedges and no independent replication. DECLINED for the calculation as reported: the sweep-4 audit's exact local re-derivation IS the second derivation. The challenge stands where it is right: "$D=4$ uniqueness" unqualified is withdrawn — it holds for massless non-SUSY fields only ($D=6$ also possible in broken SUSY, C&G §5) — and the §IX.3 sentences were grade D as written; they are corrected in the v94 2026-11-17 patch (one-loop requirement reattributed to [41][42]; classical-substrate sentence narrowed to the scoped reading: no classical mechanism known that selects signature for a single-scalar Swift–Hohenberg $D_4$ substrate without a tuned clock field).
- **What we know:** the Greensite calculation as stated is correctly reported; the mechanism's conclusion stays conditional on the heat-kernel regularization premise and the massless non-SUSY scope; neither the Greensite (quantum) nor the Mukohyama (classical clock-field) route is instantiated by IRH's substrate (no fermions, no loops, no clock field).
- **Owner:** Closed as a calculation-recovery verdict; the §IX.3 wording correction is filed in v94.

### G-C21-CDT — CDT small-scale endpoint (~2 vs ~3/2): literature tension unresolved [split from G-C21 in run 12; the IRH-side half is G-C21-IRH below]

- **Status/grade:** OPEN, owner Literature. This is the ~2 vs ~3/2 split within CDT itself. Part-7c's verdict stands (EXP-715 FAILED; Loll 2019 §7.1, Ambjørn–Loll 2026 "compatible with 2"). Run 11 (EXP-1115) hard-stopped literature work, so nothing there moves it. Continuum UV endpoint bounded to $[3/2, 2]$ at grade **B (PROPOSED)**; sharp value ABSTAIN. Core verdict confirmed (Gemini Sweep 5, audited 2026-11-12): the $\sim 2$ vs $\sim 3/2$ split is bare-coupling and extrapolation-regime dependence; the canonical point is $\approx 2$; the continuum UV value is bounded to $[3/2, 2]$ at B with the sharp value abstained; no grade change to any IRH claim.
- **What we know:** CDT $D_{s}(\sigma) = 4.02 - 119/(54+\sigma)$ evaluates 1.816 at
  $\sigma\to0 ($paper $1.80 \pm 0.25)$ and 4.02 at $\sigma\to\infty ($paper $4.02 \pm 0.10)$. IRH's v94 site-field operator (D4 Laplacian l.466; l.468 dispersion, $\mu=0$) has heat-kernel spectral dimension $d_s\to4$ for $\sigma\gg a_0^2$ (in units $2J/a_0^2=1$; $d_s-4\simeq1/(6\sigma)$), and 5 with the time direction (reading B / l.468 spacetime symbol). It shows no UV dimensional reduction. $d_s$ overshoots to $5.731$ at $\sigma\approx0.213$ and falls to 0 below the lattice scale (lattice artefact; 1 with continuum time). Hence IRH (site-field operator) does not reproduce CDT's UV reduction. The CDT-vs-IRH 'divergence at $\sigma\to0$' is not a like-for-like comparison: the σ units differ and the IRH UV is lattice-dominated. EXP-1115, F2/I1, rung 3. The small-scale endpoint is
  disputed in the literature (~2 vs ~3/2 — Coumbe & Jurkiewicz 2015).
- **What would close it:** resolution of the literature tension (a
  retrieved consensus or a new computation). Next test: post-2016 CDT literature on $D_S(0)$ along a constant-physics trajectory (not accessed in run 11, hard stop).
- **Owner:** Literature (retrieval).

### G-C21-IRH — IRH-side spectral dimension of the v94 site-field operator — CLOSED-scoped (run 11, negative result) [split from G-C21 in run 12]

- **Status/grade:** CLOSED-scoped (site-field operator). The v94 site-field operator (l.458–468, $\mu=0$, readings A and B) has no UV dimensional reduction. Its heat-kernel spectral dimension runs from the lattice fall-off ($\to0$; or $\to1$ for O2 with continuum time), through an overshoot (max $5.731226$ at $\sigma=0.213384$), to $4^+$ (O1) / $5^+$ (O2), with $z_{\rm eff}\to1$. The operator therefore produces no value in $[3/2,2]$. C-1115a ($d_s=1+d/z$): [D], rung 4D, F2, I1. C-1115b (O1/O2 endpoints + no plateau): [C], rung 3, F2, I1; F2 record passes (RUN11_REPORT §1). EXP-1115, trace `run11/adj/G-C21_trace.md`.
- **What we know:** v94 l.958 already scopes the $[3/2,2]$ interval to CDT ("the causal-dynamical-triangulation continuum UV endpoint … no IRH grade changes"); it does not claim that IRH produces the interval, so this is not an erratum. Recommended (manuscript, not applied here) addition after "no IRH grade changes": "IRH's own site-field operator (§III.1, l.458–468) has no UV dimensional reduction: its heat-kernel $d_s$ runs from the lattice fall-off through a maximum $\approx5.73$ to 4 (5 with time), so the $[3/2,2]$ interval is not an IRH prediction (EXP-1115, run 11, F2/I1). The Swift–Hohenberg $\psi$ operator was not tested."
- **Scope limit:** the non-retired Swift–Hohenberg $\psi$ operator (v94 l.149/151) is untested; until a frozen EXP computes $d_s(\sigma)$ for it, "IRH does not produce $[3/2,2]$" must not be stated beyond the site-field operator. Also carried: σ = 3000 Wolfram value; mass term $\mu\neq0$.
- **Owner:** Local Muse verification (carried: ψ-operator EXP).

### G-C22 — Triad relations "derive" c, $\hbar$, G: NOT A DERIVATION — CLOSED as a verdict (the physics gap stays open)

- **Status/grade:** CLOSED as a verdict. No grade — NOT A DERIVATION
  (WS-D tasks 9, 10, 12; definitional identities, F3 as identities).
- **What we know:** the triad relations are definitional re-expressions
  of measured Planck quantities (a change of variables); the triad
  closes iff $L_{P}^{2} = \hbar G/c^{3}$, the definition of $L_{P}$. The manuscript itself
  states the circle. Task 10 (D1, grade C) and task 12 (G3) agree.
- **What closed it:** the verdict itself — the claim *as a derivation*
  is refuted. The underlying physics gap (no derivation of the constants
  from the substrate) stays open and is carried by $G-C10 (\alpha)$ and G-C2/G-C3.
- **Owner:** None (closed as a verdict).

## Group D — Cosmology and the early universe

Manuscript sections: §VI (predictions VI.1–VI.7), §IX.5 (genuinely open
physical questions). Tasks: WS-E 11, 14, 15. The manuscript's own
assessment: "The joint early-universe narrative is missing in its
entirety" (programme brief).

### G-D1 — Cosmic expansion drives the parameters (r, $\bar{\psi}, q_{0})$: ABSTAIN — no coupling stated

- **Status/grade:** ABSTAIN (WS-E task 11, C9; no grade).
- **What we know:** "The manuscript states no coupling between cosmic
  expansion and any model parameter. There is no scale factor, no Hubble
  parameter, no Friedmann equation, no expansion-driven parameter law
  anywhere in the text (grep-verified over the full 1,638-line source
  rebuild)." This is task 15's blocker B1 as well.
- **What would close it:** a stated expansion$\to$parameter coupling (a
  scale factor a(t) or Hubble H(t), or what plays that role) in the
  manuscript.
- **Owner:** Brandon's call (manuscript: state the coupling$) \to$
  Co-scientist task (simulate the bifurcation cascade once stated).

### G-D2 — What fixes $\bar{\psi}? ($IX.5.1) — the sharpest open question

- **Status/grade:** ABSTAIN (WS-E task 11, C10; task 15, B6; no grade).
  Stated open in the manuscript.
- **What we know:** under conserved dynamics $\bar{\psi}$ is an initial datum,
  reclassifying the fine-tuning objection as a cosmological
  initial-condition question — but no mechanism sets its value. Whether
  occupying the $D_{4}$ band is a prediction or a tuning "remains
  undetermined" (task 15, B6). A mechanistic account of what fixes $\bar{\psi}$
  would change D4 from "conditional on basin IC" to "selected" (WS-C
  task 7).
- **What would close it:** a mechanism fixing $\bar{\psi}$, or a stated prior over
  $\bar{\psi} ($task 15 requirements list, item 6).
- **Owner:** Co-scientist task (new, theory) / Brandon's call (if the
  answer is a manuscript-level decision about priors).

### G-D3 — What supplies the nucleation event? (IX.5.2)

- **Status/grade:** ABSTAIN (WS-E task 11, C10; task 15, B4; no grade).
  Stated open in the manuscript.
- **What we know:** first-order transition (§II.9); the $D_{4}$ phase must be
  nucleated across a barrier at $\bar{\psi} = -0.18 ($barrier top $A_{small} = 0.0098$,
  F = +0.000039 at the operating point; homogeneous barrier
  $3.8585\times10^{-5}$ at $A_{max} = 0.00980059)$. No nucleation mechanism or rate is
  stated (§II.9 line 641: "Any cosmological account within this
  framework must supply a nucleation mechanism").
  **2026-11-14 (noise-nucleation chat 923db040, partial bundle):** negative result — no transition-gate crossings in 192 ordinary runs or the bounded adaptive-splitting search; per-configuration 95% upper bound on gate entry by model time 40 is $8.94\%$ (Clopper–Pearson $0/32$; pooled $0/192$ would be $1.55\%$). The null coheres with the local radial-envelope saddle ($550.930573$ at $dr=0.5$): at barrier/noise $\approx 34$ the Kramers factor $\exp(551/16) \approx 9.0\times10^{14}$ predicts $\sim 10^{-13}$ expected hits per run, so the null is expected, not evidence against nucleation. Open item: re-run the audit when the chat's 7 files land, checking the 192-vs-160 count discrepancy first (192 = code's 6-config default $\times 32$; bundle has 160 in `ensemble.log`, 128 tabulated).
- **What would close it:** a nucleation mechanism and rate — what
  nucleates the $D_{4}$ phase, at what temperature T\*, with what strength $\alpha$
  and duration $\beta/H ($task 15 requirements list, item 5). "These three
  numbers are the entire input to a first-order phase-transition GW
  spectrum."
- **Owner:** Co-scientist task (new, theory) / Brandon's call.

### G-D4 — Gravitational-wave forward model: ABSTAIN (no stated model)

- **Status/grade:** ABSTAIN (WS-E task 15; the ABSTAIN is the report's
  central result, not a failure of effort). All 11 observable rows
  UNSTATED.
- **What we know:** "gravitational wave" occurs 0 times in the manuscript
  text; "graviton" 1 (line 1383 only); "tensor" 1 (line 1376 only).
  VI.1–VI.7 contain no GW prediction. Blockers B1–B6 (task 15 §4) all
  stand: B1 no expansion history; B2 dimensional assignment undecided
  (§IX.2 A/B/C); B3 Einstein equations not recovered / tensor sector
  unrecovered (effective metric "obeys the substrate's own equation of
  motion, not $G\mu\nu = 8\pi T\mu\nu$"; "the two transverse-traceless graviton
  polarizations is a separate and substantially harder [problem]"); B4 no
  nucleation mechanism, no $\bar{\psi}$ mechanism (§IX.5); B5 no photon or baryon
  coupling; B6 no stated cosmological initial conditions. Any
  phase-transition GW estimate from the Task 11 barrier numbers FAILED
  as a derivation (the barrier is substrate energetics at fixed (r, $\bar{\psi})$,
  not (T\*, $\alpha, \beta/H))$.
- **What would close it:** the 9-item requirements list (task 15 §5), in
  order: (1) expansion history; (2) dimensional assignment (G-C8);
  (3) tensor sector — recover the two TT graviton polarizations and
  state the equation they obey ("Until then, every GW row stays
  ABSTAIN"); (4) Einstein recovery or a stated replacement; (5)
  nucleation mechanism and rate (T\*, $\alpha, \beta/H)$; (6) mechanism fixing $\bar{\psi}$
  or a stated prior; (7) photon and baryon couplings; (8) initial
  perturbations (scalar spectrum amplitude/tilt $n_{s}$, tensor spectrum
  amplitude/ratio r, or a derivation from substrate dynamics); (9) a
  monopole number (dilution factor or breaking pattern). "Items 3 and 5
  are the binding constraints for GW; items 7 and 8 for CMB. Items 1–2
  gate everything." One partial bridge (§6): the transition is first
  order and VI.6 states a defect spectrum, so "the *shape* of a future
  IRH GW prediction is visible: it would be a phase-transition spectrum,
  not an inflationary one" — but it does not reach the grid, because a
  phase-transition spectrum is fixed by (T\*, $\alpha, \beta/H, v_{w})$ and the
  manuscript supplies none of the four. A stated nucleation rate with
  T\*, $\alpha$, $\beta/H$ would make G4 computable with a standard template, and the
  LVK O1–O4a first-order-phase-transition constraints would then bite.
- **Owner:** Brandon's call (future manuscript work — guide §12 Q4:
  attempt the requirements list in a future IRH version?$) \to$ Co-scientist
  task (forward-model once the inputs exist). A newer manuscript version
  (v94+) would need a fresh extraction.

### G-D5 — CMB forward model: ABSTAIN (no stated model)

- **Status/grade:** ABSTAIN (WS-E task 15; same requirements list as
  G-D4). All CMB rows UNSTATED.
- **What we know:** "CMB" / "cosmic microwave" occur 0 times; "photon"
  0; "baryon" 0. Instrument responses are verified and on record for
  when a model exists (Planck \$2018 $n_{s} = 0.9649 \pm 0.0042$$; BK\$18 r_{0}.05$ <
  0.036, $\sigma(r) = 0.009$; newer combination r < 0.032; CMB-S4 design
  $\sigma(r) < 5\times10^{-4})$. Items 7 and 8 of the requirements list are the binding
  constraints for CMB.
- **What would close it:** the same 9-item requirements list as G-D4,
  with photon/baryon couplings and initial perturbations (items 7–8) as
  the binding constraints.
- **Owner:** As G-D4.

### G-D6 — No independent work citing or discussing IRH was found

- **Status/grade:** INCOMPLETE-EVIDENCE (unchanged). Gemini Sweep 6 (Task mode, 2026-11-13) audited 2026-11-13: **MISS** confirmed — zero independent works citing or discussing IRH; G-D6.1 (final) B CONFIRMED; G-D6.2 B (scoped bound) / ABSTAIN (universal negative) CONFIRMED, re-anchored on the Argon run. **Model-label correction:** the follow-up run was **Gemini 4 Hydrogen, not Argon** — cite it as Hydrogen; the two runs are one artificial pipeline ($\to$ I1), not two independent verifications. **Independence correction: G-D6.2 $I2 \to I1$** (the initial report's I2 is refuted as an overclaim; grade impact none — the $I1 \to C$ bound was repealed 2026-11-12). G-D6.3 F2 CONFIRMED and STRENGTHENED (Chaudhary 88-page full-text check closes the pp. 65–88 gap).
- **What we know:** no independent work citing/discussing IRH was found
  in the 63-query / 73-paper retrieval. "A different query set could
  find something."
- **What would close it:** a retrieved independent work engaging IRH
  (which would change M8), or a wider retrieval that still finds none
  (which strengthens the bound without proving the negative).
- **Owner:** Literature (retrieval watch).

### G-D7 — No findable Wise Journal revision record

- **Status/grade:** INCOMPLETE-EVIDENCE (WS-E task 14, M9;
  search-bounded absence).
- **What we know:** the IRH manuscript is under revision with the Wise
  Journal of Astrophysics and Astronomy (Gmail record), with a
  processing-charges invoice outstanding; no findable revision record
  was retrieved.
- **What would close it:** a located revision record, or Brandon's
  statement of the revision's status.
- **Owner:** Brandon's call (he holds the correspondence) / literature
  (retrieval watch).

### G-D8 — Klein (2001) caveat on the 3D validation

- **Status/grade:** Open question for Brandon (WS-E task 14, F1, grade C).
- **What we know:** Klein (arXiv:cond-mat/0104342, 2001) argues AM's BCC
  solutions are *unstable* — "the cubic term that selects BCC also
  destabilises it, and the stable 3D solution may be different." IRH
  v93.1 §V validates its selection principle in 3D by recovering BCC
  (the AM result). The finding "does **not** touch the structural
  affinity (Gate $2\dots)$, but it does bear on the *evidence* for IRH's
  mechanism: the manuscript's 3D check should be read as 'recovers the AM
  prediction', not 'recovers an established fact'." A stability analysis
  of the IRH \$4$D D_{4}$\$ solution is the direct analogue of the missing check.
- **What would close it:** acknowledging the caveat in a future revision
  (Brandon's call), and/or a stability proof for the IRH $D_{4}$ solution
  (which would retire F1's analogue) or a demonstration that AM's BCC is
  stable (which would retire F1).
- **Owner:** **Brandon's call** (acknowledge in the manuscript?$) \to$
  Co-scientist task (stability analysis of the \$4$D D_{4}$\$ solution).

### G-D9 — Selection-principle change SSRN $\to v93.1$: acknowledge it?

- **Status/grade:** Open question for Brandon (WS-E task 14, F2, grade C).
- **What we know:** the same-author SSRN predecessor selected by
  *maximal cymatic complexity* and obtained **dimension 8**; v93.1
  selects by **$S = \tau^{2}/q_{4}$** and obtains **$D_{4}$**. "The selection principle
  is therefore **version-dependent**." It currently is not acknowledged
  in the manuscript's history, as far as the retrieved record shows; the
  reason for abandoning maximal cymatic complexity is a question for the
  author.
- **What would close it:** acknowledging the change in the manuscript's
  history (Brandon's call), with the reason for the change stated.
- **Owner:** **Brandon's call alone.**

### G-D10 — IRH alone in the (2,2) corner: a structural fact, not evidence; no independent corroboration

- **Status/grade:** Open (narrowed); grade C — strengthened bound (WS-E task 14, M6, C/I1/F1). DECIDED 2026-11-12 ~19:11 CST by the assistant under Brandon's standing decision autonomy ("act as I would"); his widget tap for this option was withdrawn by his "disregard last message" instruction immediately after, so the call is the assistant's, on the audit's evidence. The broad claim stays overturned (audit grade B); the gap continues in narrowed form. **Audit landed 2026-11-12 (Gemini Sweep 1 audit):** the overturn stands under the stated three-criteria definition (IRH is not alone in the (2,2) corner; SSM (2,2,2)); the conditional sub-verdict is preserved at grade C — narrowed to spectral/Turing-only selection, no retrieved approach occupies the spectral-only (2,2) corner (SSM sits at (2,1,2), Lee at (2,1,1), Four Null at (2,1,1) under that reading). What would close the narrowed form: a retrieved approach with emergent spectral/Turing selection in the (2,2) corner, or a wider retrieval that still finds none.
- **What we know:** on the three structural criteria, no retrieved
  approach is close to IRH on all three at once; IRH is alone in the
  (substrate 2, selection 2) corner. GFT is closest on ontology
  (Gate 1 passes ontology, mechanism fails); AM/LP is closest on
  selection (Gate 2 passes mechanism, ontology fails — "the only gate in
  this report that passes at the mechanism level"); AS is furthest on
  ontology and strongest on stated quantitative predictions. Retrieval is
  bounded by 63 queries / 73 papers — "an approach not retrieved is not
  scored"; most likely miss is a small emergence programme at (2,2).
  Contestable scores (Verlinde substrate 1 vs 0; causal sets selection 1
  vs 0) do not change M3/M4/M6; GFT substrate ambiguity (quanta *of*
  geometry vs substrate *under* geometry) could drop GFT to 1 and make
  Volovik the ontology leader — reason M3 is grade C, not higher.
  Narrowed 2026-11-12: selection means emergent spectral/Turing
  bifurcation specifically, not free-energy/kinematic lattice
  crystallization — under that reading SSM sits at (2,1,2), Lee at
  (2,1,1), Four Null at (2,1,1), and no retrieved approach occupies the
  corner.
- **What would close it:** the broad claim ("IRH alone in the (2,2) corner") is already overturned — SSM (2,2,2), audit grade B; that overturn stands and is recorded, not re-litigated. In the narrowed form (spectral/Turing-only selection), what would close it: a retrieved approach with emergent spectral/Turing selection in the (2,2) corner; or a wider retrieval that still finds none (strengthening the bound at C).
- **Owner:** Literature (retrieval watch; the torus-node paper, G-C14,
  is the first candidate to check against the map).

### G-D11 — Full-field (beyond one-mode) bifurcation computation: blocked on missing inputs, not compute

- **Status/grade:** Open; costed, not run (WS-E task 11 §8).
- **What we know:** a full-field bifurcation computation would shift the
  curves by ~1%. It is blocked on missing inputs (the band-scan code with
  sub-pattern free energies; the $w_{6}$ term form — see G-A1, G-A8), not on
  compute. No GCP spend was proposed for it.
- **What would close it:** the missing inputs stated (G-A1, $G-A8) \to$
  then the computation.
- **Owner:** Brandon's call (state the inputs$) \to$ Co-scientist task
  (compute; costed first).

### G-D12 — Task 14 S5 blending / S6 tournament / S7 formal verification: NOT RUN by design — RECORDED

- **Status/grade:** NOT RUN by design (WS-E task 14). Not counted as a
  closable gap.
- **What we know:** S5 blending NOT RUN (gated affinities partial and
  mutually incompatible); S6 tournament NOT RUN (no candidates to
  evolve); S7 formal verification NOT RUN (claims comparative/historical,
  not formal).
- **What would close it:** nothing — these stages are gated on candidates
  that do not exist. If a (2,2) approach is ever retrieved (G-D10), S5/S6
  become runnable.
- **Owner:** None (recorded; gated).

---

## Group E — Programme-level, provenance, and audit-scope gaps

### G-E1 — The "Compare $D_{4}$ Selection Frameworks" gap memo — LOCATED and AUDITED (2026-11-12)

- **Status/grade:** LOCATED. Closed as a provenance gap by the pull + audit of 2026-11-12 (it was recorded NOT LOCATED in the first issue of this inventory; see the correction note below).
- **What we know:** the 16th task, finished overnight Nov $9\to10$ by Academia Co-scientist; source email "Co-scientist finished: Compare $D_{4}$ Selection Frameworks", sent Mon, 9 Nov 2026, 5:31 PM CST (Gmail message `1a1c2a6dead2cefa`, verified by direct lookup — NOT Nov 10 as first recorded). Excluded from the 15-task programme by the brief ("DONE already$\dots$ audit of its three files is a separate item (needs Academia login) and is NOT part of this programme"). Its three files were pulled from the task chat (https://www.academia.edu/co-scientist/chats/8bb74cc0-be71-462b-b925-7103744be2d3) on Brandon's "Do both" (2026-11-12 13:48 CST) and audited claim-by-claim the same day:
  - `compare-d4-frameworks/framework-matrix.md` — 15,059 B, md5 `1b4c5388db42f831ee24ccb2e5aea070`
  - `compare-d4-frameworks/gap-memo.md` — 11,495 B, md5 `6b5a91a08038a1f7af997847809c815a`
  - `compare-d4-frameworks/verification-audit.md` — 4,877 B, md5 `726a851d1887f8330e1499294ea80d75`
  - Audit: `compare-d4-frameworks/AUDIT_compare-d4-frameworks_2026-11-12.md` (591 lines) — 189 claims: 166 VERIFIED, 7 CORRECTED, 0 REFUTED, 16 ABSTAIN; no IRH grade moves. Its headline finding — the gap between *selecting* the $D_{4}$ shell and *spontaneously reaching* its full 24-mode pattern — is the gap the running 4D field test attacks (G-A5).
- **What would close it:** done — pulled and audited 2026-11-12. The memo's gaps (G1–G5) restate/sharpen gaps already in this inventory and close none of them.
- **Owner:** closed. **Correction note:** the first issue of this inventory dated the task/email "2026-11-10"; the email is Nov 9, 5:31 PM CST (verified by Gmail lookup). Nov 10 was the day the task was flagged to Brandon, not the email's date.

### G-E2 — Hark §3: "the round-1 review had $\approx [-0.235, -0.14]$ with stripes/A2/A3 included" — source NOT LOCATED

- **Status/grade:** UNVERIFIED — source not located in the workspace
  (Hark review §3).
- **What we know:** searched the 2026-10-30 deepest-research report, the
  v5 test report, the repo CORE.md, the task-14 report, and the
  manuscript text — no $[-0.235, -0.14]$ band and no "stripe" competitor
  set appears in any of them (the manuscript's band is "$-0.33$ ≲ $\bar{\psi}$ ≲ 0.03
  depending on quench depth", line 528; the manuscript contains no
  "stripe"). The $-0.235$ lower edge coincides with WS-C's measured edge,
  which makes the attribution suspicious. It may come from a review
  document Hark holds that is not in this workspace; from this side it
  cannot be cited.
- **What would close it:** locating Hark's source document, or dropping
  the attribution.
- **Owner:** Local Muse verification (search) / Hark (produce the source).

### G-E3 — REVISION_PLAN citations (B1/R4/R6/Step 1.2): no such document in the workspace

- **Status/grade:** UNVERIFIED — citations unlocated (Hark review §4).
- **What we know:** Hark cites "REVISION_PLAN 1.1" (for B1) and
  "Step 1.2" (for R4). Full-tree grep for REVISION_PLAN/UNDERDETERMINED
  found only the skill prompt files and a WS-D table entry using
  UNDERDETERMINED as a grade word. No REVISION_PLAN document exists
  anywhere in the workspace. The B1 substance stands on the manuscript
  text (G-B7); the R4 need is real (G-A20); the citations do not verify.
- **What would close it:** locating the document, or dropping the
  citations and citing the manuscript text / package directly.
- **Owner:** Local Muse verification (search) / Hark (produce the source).

### G-E4 — Hark §6.5 human-gate repeal: provenance — RESOLVED (2026-11-12)

- **Status/grade:** CLOSED. Provenance caveat resolved.
- **What we know:** the audited Hark document opens with an amendment
  dated 2026-11-10 22:33 CST stating Brandon repealed the HLRE §6.5
  human-gate requirement *for this assessment*. That repeal was recorded
  in Hark's document, **NOT in the reviewer's own conversation record
  with Brandon** — until 2026-11-12 14:07 CST, when Brandon stated the
  repeal himself, in conversation, in wider scope ("from your assesment
  and all future assesments"). The repeal is now in the conversation
  record. Amendment note: `HLRE-6-5-HUMAN-GATE-REPEAL-2026-11-12.md`.
  Nothing in the review depends on the repeal for its Track E conclusions
  (WS-A's A/B grades fall to C on the independence bound alone), but the
  Track F two-route $F3\to F2$ regrades DO rest on the amendment's terms —
  and their extension to WS-D is now decided (G-C17 closed, G1/G5/$G8/G12 \to F2)$.
- **What would close it:** done — Brandon's in-conversation repeal, 2026-11-12.
- **Owner:** closed.

### G-E5 — WS-B characteristic-p Gröbner dim/degree of the chart system: NOT RUN

- **Status/grade:** NOT RUN (WS-B task 6, U1; costed plan in the report
  §8). This is Jacobian-conjecture work, not IRH physics.
- **What we know:** the dim/degree of the 16 chart equations +
  $a_{7}^{3}b_{0}^{2} = 1$ over 𝔽${}_{101} ($control), 𝔽${}_{3}$, 𝔽${}_{5}$, 𝔽${}_{7}$ was attempted in Singular
  but did not finish even p = 101 in 570 s (263 s CPU; the log holds only
  `p = 101: #equations = 17`). Costed plan: a faster machine (e.g.
  lean-build-4's 24 cores once leg-9 ends — never while it runs), a
  longer wall-clock budget (estimate: several hours at the throttled
  local rate, unmeasured), or a smarter method (msolve, or the
  S-recursion/torus route used by the Lean proof). The char-0 derivation
  does not depend on this check.
- **What would close it:** the computation, run on a faster machine or
  by a smarter method, with a named cap.
- **Owner:** Local Muse verification / Co-scientist task (costed first;
  GCP/VM spend needs a named cap).

### G-E6 — WS-B second a816 certificate (`a816_lift_liftstd.txt`): not committed, not re-verified

- **Status/grade:** NOT RUN (WS-B task 6, U2).
- **What we know:** only the main certificate $(a_{8},{}_{16}^{2} = \Sigma H_{k} e_{k}$ over
  $K_{5}$; 76 cofactors, 3464 terms) was re-verified (VALID by python-flint
  rebuild + Singular over $\mathbb{Q}(w)$; all negative controls rejected). The
  second certificate file is not committed in the repo.
- **What would close it:** producing/committing the second certificate
  first, then re-verifying it.
- **Owner:** Brandon's call (produce/commit$) \to$ local Muse verification
  (re-verify).

### G-E7 — WS-B separate packaging: offered, unanswered

- **Status/grade:** Open; Brandon's call (offered 2026-11-10 19:54 CST).
- **What we know:** task 6 was excluded from the $D_{4}$ package zip
  (`d4-work-2026-11-10.zip`, 142 files, sha256 `e9acec99…`) because it is
  Jacobian-conjecture work, not $D_{4}$ physics. A separate package was
  offered and not answered.
- **What would close it:** Brandon's decision (package separately or
  leave it in the workstream directory).
- **Owner:** **Brandon's call.**

### G-E8 — WS-D was not audited by Hark (audit scope was WS-A/C/E)

- **Status/grade:** Open; audit-scope gap.
- **What we know:** the Hark audit is "an audit of the D4 work package
  (WS-A, WS-C, WS-E)". Its only WS-D content is a section-number note
  and a closing note: "WS-D's deliverables appear to be on disk (task8,
  task9, task10, task12 reports + ws-d_summary.md, written 2026-11-10
  17:05–17:20 CST). I have not verified or delivered them yet — that is
  the next item unless you say otherwise." WS-D was folded into the guide
  as §6 on 2026-11-11 and the parent re-ran its executable checks in a
  scratch copy (task 10: 45 + 33 PASS, 0 FAIL; task 12 driver: 55 PASS,
  0 FAIL; driver output identical to the shipped rerun log) and read the
  four reports — but no independent replication audit of WS-D exists.
  This is also why the $F3\to F2$ question (G-C17) was undecided in the first
  issue of this inventory; it is now decided by the 2026-11-12 repeal
  (G1/G5/$G8/G12 \to F2)$. The replication-audit question is separate.
- **What would close it:** an independent replication audit of WS-D on
  the Hark pattern (or a stated decision that the parent's re-runs
  suffice).
- **Owner:** Co-scientist task (audit) / Brandon's call (commission it).

### G-E9 — Hark'$s \bar{\psi} = 0$ and $\bar{\psi} = +0.10$ transverse runs, and the stripe side-result: REPORTED, NOT RE-RUN

- **Status/grade:** CLOSED (run 11, EXP-1113): a REPRODUCED; b MIXED (50–70% to a 2-mode decorated stripe, the rest to hex6 or a 12-mode state); c energies REPRODUCED, one-mode stripe metastability REFUTED. F3/I1, rung 2, two code-independent routes on one binary. (Was: REPORTED, NOT RE-RUN (Hark review, F1); the stripe side-result UNVERIFIED (single Hark run).)
- **What we know:** the reviewer's own transverse check covered $\bar{\psi}$ =
  $-0.18$ only (5/5 hex6 + 4/4 fcc$12 \to$ full24). Hark'$s \bar{\psi} = 0$ result
  (24-mode + 2% amplitude / 0.2 rad phase noise $\to 6$-mode) and $\bar{\psi} = +0.10$
  result $(\to 2$-mode stripe-like; '2-mode' means ndom = 2 under the 0.5·max rule of d4model.analyze. The state is one pair at 0.2891 plus 8 pairs at 0.0971, with 3 pairs empty. It is reached in 50–70% of noisy starts, so the claim is MIXED, not reproduced) are consistent with the WS-C numbers
  they quote (A6 6-mode Fexc $-0.041306$ at $\bar{\psi} = 0$ matches the task-1
  report exactly) but are recorded as reported, not independently
  confirmed. The stripe side-result (one run: one-mode stripes Fexc $\approx$
  $-0.0451$ vs hex$6 -0.0539$ at $\bar{\psi} = +0.10$; the one-mode stripe ($F_{exc}=-0.0450935$) is a transverse saddle. It is stationary only in its invariant subspace and left it in 0/40 kicked runs ($\varepsilon=0.002A^*$, 4 codes). The stripe-like state that persists is the decorated stripe at $-0.048943$, which is also above hex6 ($-0.053935$)) was a single run, now re-run in run 11 (EXP-1113). The WS-C
  one-mode competitor set {24-mode, 6-mode, disordered} omitting stripes
  is a real gap either way (see G-A7).
  **Run 11 caveats (G-E9_trace §5):** the 24-mode state at $\bar\psi=0$ is itself unstable. It goes to 6 noise-free (V FF cal24_0, one route), so the noise is not selective. Hark's noise protocol and run length are not in any located source; the run-11 protocols are R1 PLAN §4 (sha `de183c1d…`) and V PLAN (sha `4d37f63e…`). The model file d4model.py is not in the repo at 64bd065; cite `~/workspace/research/irh/co-scientist-tasks-2026-11-10/ws-a-core-computations/d4model.py` sha256 `0015851afe98a14c5ff0e6b18a42e0a5b22fc6ce1b41771ba15e3fdace0b99c1`.
- **What would close it:** re-running Hark'$s \bar{\psi} = 0 / +0.10$ transverse
  tests and the stripe run locally.
- **Owner:** Local Muse verification (small local runs).

### G-E10 — Task 14's most-likely-miss: a small emergence programme at (2,2) not retrieved

- **Status/grade:** CLOSED (run 11, EXP-1105). Outcome: **M6 refuted as worded** (broad "IRH alone at (2,2)" overturned). 4 non-IRH LITERAL (2,2) entries: SSM (Kulkarni, refereed, Quantum Rep. 8(4) 121, full text), quantum graphity (full text), Kelly–Trugenberger–Biancalana (arXiv:1901.09870), and Hunter's FoR substrate-field paper (abstract only; physics ABSTAIN). The robust ones are SSM and quantum graphity; either alone suffices. Track E **C**, I1, [D] (literature scoring, judgement-based). Scope: bounded by the queries run (R1 84 + R2 re-runs, logged); not a census. (Was: Open; bounded by retrieval (WS-E task 14).)
- **Reconciliation with v94 l.448 (open record items, not decided here):** (1) v94 records "the broad claim OVERTURNED at grade B"; the run-11 record supports only Track E C / I1 and does not endorse B. Unless v94's B rests on evidence not in the run-11 record, the record should read C. (2) The narrowed v94 sentence ("under the narrowed reading no retrieved approach occupies the corner") is **CONTESTED, pending the FoR full text** (DOI 10.5281/zenodo.19151764 / 19170453): defeated at abstract level for the run-11 retrieval, true of v94's own retrieval. (3) The corrected M6 wording (`G-E10_final_trace.md` §4) is for the map's M6 row and was not applied. Formerly Brandon items; now under the 2026-11-22 delegation.
- **What we know:** retrieval is bounded by 63 queries / 73 papers —
  "an approach not retrieved is not scored". The most likely miss is a
  small emergence programme scoring (2,2) — which would overturn M6
  ("no retrieved approach close on both ontology and mechanism jointly").
  The torus-node paper (G-C14) is the first such candidate found outside
  the retrieval.
- **What would close it:** a wider retrieval, or the torus paper (and
  any further candidates) scored against the map.
- **Owner:** Literature (retrieval watch) / local Muse verification
  (score the torus paper against the map if Brandon approves G-C14).

### G-E11 — Record guard: 143 vs 14 runs — NOT A GAP

- **Status/grade:** Record guard. Not counted as a gap.
- **What we know:** WS-A task 5 ran **14 runs** (6000 steps each),
  STATUS VERIFIED for the 14-run protocol. The "143 basin runs" figure
  in Academia's 2026-11-12 email is **Academia's count, NOT ours**.
- **What would close it:** nothing — it is a standing guard on citation.
  Never cite 143 as our run count.
- **Owner:** None (standing guard).

---

## 6. Closed in this baseline (graded verdicts that are not gaps)

These items are **closed** under the §0 definition — each has a graded
verdict — and are therefore not counted among the 64 open gaps. Several
close by showing the claim as written is wrong; the correction is the
result. (Items marked $\dagger$ are also cross-listed inside their groups with
CLOSED status.)

1. **hex6/fcc12 "stable attractors" (WS-A task 5; WS-C findings 6–7) —
   FAILED as written; corrected.** At $\bar{\psi} = -0.18$ the 24-mode attracts
   perturbed hex6 and fcc12 starts (5/5, 4/4); hex6/fcc12 are saddles.
   At $\bar{\psi} = 0$ hex6 is stable and the 24-mode is not (Hark's result, not
   re-run). Grade C. (Hark F1, VERIFIED by the reviewer's own run.)
2. **WS-C C1.2 (dynamic account predicts full 24-mode ONLY inside the
   band) — FAILED as written; basin-qualified version CONFIRMED** under
   C1.3 (divergence boundary D1–D4, grade C).
3. **WS-C C2.2 / P4 (discretization error decreases with N and dt) —
   FAILED as written; corrected version CONFIRMED** (transient error
   decreases, Richardson $p \approx 0.95$, first order as expected for
   semi-implicit Euler).
4. **"$\delta = 0.5$ kills the ordered branch" plane-wide — FAILED as written;
   corrected to the $\delta^{2}$ shift, VERIFIED** (grade C). $\dagger (G-A17)$
5. **Thin-wall droplet estimate as the answer — shown to fail; ODE value
   stands** $(R_{c} = 12.57 / \Delta F* = 555$, grade B). $\dagger (G-A18)$
6. **Printed dispersion relation (7) — CLOSED (run 11, 2026-11-22) — no erratum needed.** WS-D task 10 D5 REFUTED as a pdftotext misreading (superscript of $a_0^2$ read as a factor 2). Printed (7) equals the EOM-derived dispersion (Singular + Wolfram, F2/I1). v94 (7) is byte-identical to v93.1 (7). (The earlier "FAILED as printed; corrected formula VERIFIED; remaining item the erratum" is withdrawn.) $\dagger (G-C12)$
7. **Triad relations as derivations of c, $\hbar$, G — NOT A DERIVATION**
   (definitional identities). $\dagger (G-C22)$
8. **Near-melting scope transfer — split verdict recorded** (combinatorial
   PASS, scope FAIL). $\dagger (G-B9)$
9. **"No framework derives all four at once" — survey COMPLETE**
   (WS-D task 8, grade C). The physics gap stays open (G-C1); the survey
   question is closed.
10. **Task 15 forward model — ABSTAINED correctly** (no stated GW/CMB
    model; any number would be invented). The forward-model gap stays
    open (G-D4/G-D5); the verdict on v93.1 is closed.
11. **Cosmic-expansion coupling — ABSTAINED correctly** (no coupling
    stated anywhere in the 1,638-line source). The gap stays open (G-D1);
    the verdict is closed.
12. **"29 vs 31 checks" — RESOLVED** (29 check() call sites; the $r_{eff}$
    table loops over 3 rows $\to 31 [$PASS] lines; a counting-convention
    difference, not a package error).
13. **Hark "different lattice basis" — NOT REPRODUCED** in the reviewer's
    env (NumPy 2.4.6 vs 2.5.4); environment-dependent, no number changes.
    The JSON provenance gap itself remains open (G-B4).

## Appendix — Gap counts by group and by owner

| Group | Entries | Open | Closed-as-verdict | Recorded non-gaps |
|---|---|---|---|---|
| A — $D_{4}$ selection, band, basin, truncation | 21 | 19 | 2 (A17, A18) | 0 |
| B — Substrate models, dynamics convergence | 9 | 8 | 1 (B9) | 0 |
| C — Frameworks, rivals, constants, gravity | 22 | 18 | 2 (C17, C22) | 2 (C4 boundary, C9 standing rule) |
| D — Cosmology, early universe | 12 | 11 | 0 | 1 (D12 gated) |
| E — Programme, provenance, audit scope | 11 | 8 | 2 (E1, E4) | 1 (E11 record guard) |
| **Total** | **75** | **64** | **7** | **4** |

**By owner (open gaps only, 64 — counted by each entry's *next* step's owner;
entries gated on a Brandon decision or a stated input are counted under
Brandon until that step is taken, and under Co-scientist/local/literature
after it):**

| Owner (next step) | Count | Entries |
|---|---|---|
| Brandon's call (alone or first) | 23 | A1, A2, A8, A16, B2, B3, B4, B7, C5, C8, C11, C12, C13, C14, D1, D4, D5, D7, D8, D9, D11, E6, E7 |
| Co-scientist task (new / running / candidate) | 23 | A3, A4, A5 (running), A6 (running), A9, A10, A11, A12, A13, A14, A19, A20 (running), B5, B8, C2, C3, C6, C7, C10, C15, D2, D3, E8 |
| Local Muse verification | 10 | A7, A15, A21, B1, B6, C16, E2, E3, E5, E9 |
| Literature / external | 8 | C1, C18, C19, C20, C21, D6, D10, E10 |
| **Total** | **64** | |

23 + 23 + 10 + 8 = 64. Brandon's call and Co-scientist task are now tied as
the largest owner classes (23 each of 64) — over a third of the open gaps
still need a decision or a stated input from Brandon before any task can
close them. Of the 23 Co-scientist-owned gaps, 3 are running (A5, the 4D
field test; A6, off-shell instabilities; A20, matched $D_{4}/A_{4}$* onset).

*Correction note (2026-11-12): this appendix counted 66 open with C17, E1,
E4 listed as open Brandon's-call items in its first issue; those three
closed on 2026-11-12 (E1 LOCATED and audited, C17 regraded F2, E4
provenance resolved), and A6/A20 moved from candidate to running. Counts
above are current.*

**Manuscript-section index (where each gap lives in v93.1):** §I.1–I.3 —
B7, A16; §II.6–II.9 — A1–A5, A8–A10, D3; §II.10 — A12; §III.1–III.3 —
C12, C13; §IV — C10, C11, C22; §V — C5, D8; §VI.1–VI.7 — A1, A2, D4, D5;
§VII — C2, C3; §VIII — D9; §IX.1 — A9–A12, A8; §IX.2 — C8, C9, D4, D5;
§IX.3 — C2–C5; §IX.4 — C6, C7; §IX.5 — D2, D3. Cross-cutting (no single
section): A6, A7, A13–A15, A19, A20, B1–B6, B8, B9, C1, C14–C21, D1, D6,
D7, D10, D11, and all of Group E.

---
*Coordinator's note on method.* This inventory was assembled by reading
the source files listed in the companion summary's Appendix B and the five
workstream extractor records (WS-A, WS-B read directly by the coordinator;
WS-C, WS-D, WS-E from dedicated extractor subagents whose full records
were recovered and checked against the source reports), plus
`OPEN_PROBLEMS.md` and the torus-node comparison §7.3. The "Compare $D_{4}$
Selection Frameworks" gap memo was searched for (filename search and
full-tree grep, 2026-11-12) and **not located** at the time of writing;
it is recorded as such in G-E1 as first issued — but the three files
were pulled from Academia later the same day on Brandon's "Do both"
and audited claim-by-claim (`compare-d4-frameworks/`,
AUDIT_compare-d4-frameworks_2026-11-12.md); G-E1 is now LOCATED and
closed, and the inventory counts above reflect that. No new computation was run, no file was
modified, no repo or manuscript state was changed, no GCP spend was
incurred, nothing was launched in Academia, and nobody was contacted.
