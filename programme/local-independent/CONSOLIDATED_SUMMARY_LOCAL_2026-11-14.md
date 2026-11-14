# Consolidated summary — local independent reproduction of 8 IRH $D_{4}$ tasks

**Date:** 2026-11-14 (all 8 local runs complete by 09:06 UTC / 03:06 CST). **Cost so far: \$0.** Nothing filed, committed, or written into any manuscript or repo; reports, figures, and tables only.

**Independence:** all local runs were done without reading any Co-scientist output for these 8 tasks. **Comparison status: PENDING for all 8** — checked 2026-11-14 ~03:10 CST, no Co-scientist result files for any of the 8 exist in the programme directory outside `local-independent/`. The Academia launch (parent browser task) is still in flight as far as this directory shows. Do **not** claim any comparison complete. One unresolved count discrepancy: the parent note says ten follow-on tasks running in Academia since 2026-11-14, while 8 were launched here — await the browser-task handoff to settle it.

**Work tree:** `~/workspace/research/irh/co-scientist-tasks-2026-11-10/local-independent/`, one directory per task (`task1-noise-nucleation` … `task8-phonon-stiffness`), each with `REPORT.md` plus, where applicable, `scripts/`, `figures/`, `tables/`. Comparison scaffolds: `COMPARISON_task1.md` … `COMPARISON_task8.md` in each task directory (local result, Academia status PENDING, per-number checklist, S3 invariance alignment, S4 Bartha/transportability audit, 8-check rubric, grade cap C/F3).

## Per-task headlines (HLRE grades as workers graded them; all I1 unless stated)

| Task | Headline | Grade |
|---|---|---|
| 1 Noise nucleation | Box transition is a homogeneous shell-amplitude crossing, barrier $\approx 0.0038$ — five orders below the droplet $\Delta F^{*} = 555$; box waiting times do **not** measure the droplet barrier. Route B Arrhenius slope $567$, 95% $[456, 670]$ vs $555.20$; Route A crossover $0/5, 0/5, 2/5, 3/5, 5/5, 5/5$ at $D = 0.1$–$3.0$. Physical nucleation rate: ABSTAIN. | B (slope, crossover); C (prefactor) |
| 2 Grain locking ($L = 4\pi$) | Independently shifted patches heal to the identical stationary full-24 state, $E = -0.00772620928487$, in a few time units; antiphase heals translated $+\lambda/4$; orientation grain fuses to stationary fcc12, not full-24. C/D "rotations" were vacuous — withdrawn. General coherence claim: C. Slab RMS diagnostic CONTRADICTED. | B (run-specific); C (general) |
| 3 Critical seed | Field bracket $R_{c,\mathrm{field}} \in (2.5875,\ 2.625]$ at $L = 2\pi$, $\alpha = 1$; envelope $12.57$ / $16.19$–$16.21$ are a different regime ($4.8\times$–$6.2\times$ larger), stated not conflated. $\alpha = 1.5$ does not rescue small seeds. Infinite-volume radius and rates: ABSTAIN. | B (bracket); C ($\alpha$) |
| 4 Native cells | Geometry exact (F2): $D_{4}$ $T = 192$, $Q = 3384$, $S = 64/141$; $A_{4}$* $T = 120$, $Q = 1860$, $S = 12/31$; no common torus. $D_{4}$ seeds $\to$ full $3/3$; $A_{4}$* twelve-mode $\to$ full $0/3$, trapped in stationary 12-mode $A_{3}$ state ($E = -0.00547044$). Relaxed energies $-0.00772621$ vs $-0.00587749$. | F2 (geometry); B (outcomes); C ($A_{4}$* reliability) |
| 5 Spectral threshold | Recovery $0/3$ at $s \le 0.05$, $2/3$ at $s = 0.075$, $3/3$ at $s \ge 0.10$ (33 runs); bracket $(0.05,\ 0.10]$, $s_{50} \approx 0.069$. Direction matters beyond $s$ and energy. | B (bracket); C ($s_{50}$); D (logistic fit); F2 (checks) |
| 6 Bloch growth | **No positive growth rate at any of 259 sampled $q$**; least-damped $-1.332276$. Frozen-ansatz $\mathbf{A}^{6}$ quartet $+0.0228772435$ does not survive relaxation — a nonstationarity artefact. Goldstone zeros F2; conserved-mean slope matches to $0.01\%$. | F2 (reproduction/zeros/slopes); C (sampled map); ABSTAIN (continuum) |
| 7 Peak ratios | $A_{1}$ and $A_{3}$ survive as discriminants ($26\times$–$182\times$, up to $941\times$); $A_{2}$, $A_{4}$ fail. $C_{2}$–$C_{4}$ survive; $C_{1}$ marginal. CPS (111) suppression $\ge 7{,}763\times$ decisive. Inter-leakage ratios demoted (unstable $>10\times$). | F2 (arithmetic); C (measurable discriminants) |
| 8 Phonon stiffness | $\lambda = \mu = 256 A_{*}^{2} = 1.5405892101$, bulk $B = 384 A_{*}^{2}$ (B; F2 as variational upper bound). Quadratic isotropy exact; first anisotropy cubic (2.6%). One $W(F_{4})$ orbit per $\|b\|^{2}$ shell $\le 12$ (F2); edge/screw cost factor exactly 2 (B). Relaxed dispersion ABSTAIN. | B (stiffness, costs); F2 (orbits, as bound); C (cores) |

## Coordinator verification (second tool, run 2026-11-14 by the coordinator)

- `coordinator_spotchecks.py` (conda python 3.11.16, **exit 0**): $D_{4}$ roots $24$; $A_{4}$* roots $20$; $S_{D_{4}} = 64/141$, $S_{A_{4}^{*}} = 12/31$, margin exactly $73/423$; $|W(F_{4})| = 1152$ by independent exact-rational BFS closure (confirms Task 8's F2 group-order claim); $\det G_{D_{4}} = 4$, $\det G_{A_{4}} = 5$; covolume ratio $\sqrt{5}/2$ irrational.
- Task 1 `scripts/verify_params.py` re-run: **exit 0** — $r_{\mathrm{eff}} = 0.1072$, $u_{\mathrm{eff}} = 1.54$, $A^{*} = 0.07757529633928076$, spinodal $-0.143927$, ODE $\Delta F^{*} = 555.199$ (trap) / $554.664$ (Simpson), $R_{c} = 12.570884$.
- Task 5 `verify_outcomes.py` re-run: **exit 0 — VERIFY 33/33**.
- CLAIM+STATUS heads of all 8 `REPORT.md` files spot-read by the coordinator and confirmed to match the workers' handoff summaries.

## Failed-exec flags — reconciliation

Runtime recorded failed exec calls in three workers' sessions (Task 8: 2; Task 4: 3 with exit codes 1/1/2 plus a SIGTERM kill; Task 2: 2), even though those workers' reports state all production scripts exit 0. Reconciliation:

- **Task 4 — RESOLVED, ledgered:** the report documents that the first $A_{4}$* smoke run failed its dissipation-identity assertion (absolute error $4.6\times10^{-5}$ on a dissipation of $\sim10^{11}$; the identity itself was correct at relative error $4\times10^{-16}$). The fault was the uncapped tensor band reaching $|k|^{2} = 896$; the fix was the physical cap $|k|^{2} \le 64$. No uncapped results are used anywhere. The recorded failures are consistent with this diagnostic smoke run.
- **Task 1 — RESOLVED, self-kills:** the recorded kills were the worker's own SIGTERM self-kills of its long background runs (housekeeping), not failures.
- **Task 2 and Task 8 — UNTRACED, flagged for audit:** 2 failed exec calls each are not individually identified in the handoff summaries or in the reports' own failure tables (Task 8's report records "failed executions: 0" in its self-test table). The workers' production claims (all scripts exit 0; second independent tools re-deriving the runs) stand on their own verification artefacts, which the coordinator re-ran for Task 1 and Task 5 only. These 4 calls are flagged here rather than silently passed; they are most plausibly failed commands during exploration (mistyped commands or pre-fix script runs), but that is an inference, not a verified fact. Recommend the audit phase re-check the two workers' logs before the comparison is finalised.

## Heavy work still undone — costed caps (none approved, none started)

| Task | Pending heavy work | Cap |
|---|---|---|
| 1 | Full radial-PDE stochastic scan | GCP-scale, cap to be named first |
| 1 | Longer-window runs, larger-box Route A | Local, costed by worker (see report) |
| 2 | $L = 8\pi$ box ($\approx 80$ min CPU/run, 4–6 GB) | Needs memory-lean rewrite + GCP pricing + approval |
| 3 | $L = 4\pi$ bracket ($\approx 10$ h wall) | \$0 |
| 3 | $L = 6\pi$ box | GCP-scale, cap to be named first |
| 3 | Wide-wall seed, $\alpha$ bracket | $\approx 25$ min, local |
| 4 | Complete $D_{4}$ arm | Cap 1,800 solver-s ($\approx 65$ min wall) |
| 4 | $A_{4}$* refinements (10 replicates/family/star, wider-band $K = 6$, second quench) | Caps 2,200 / 6,000 / 1,500 solver-s; GCP \$25 proposed |
| 5 | Full ensemble grid (120 runs) | $\approx 4.5$ CPU-hours, local; $K = 6$ / $N = 28$ refinement; $t = 400$, half-dt repeats |
| 6 | Dense 4D map | $\approx 2$ h on 4 workers local, or $\approx \$2.44$ GCP (needs approval); dense 0.01-step cuts $\approx 10$ min local; interval enclosure cost TBD |
| 7 | None | $\approx 83$ s total, \$0 |
| 8 | Relaxed-field Bloch phonon spectrum | GCP \$25 (needs approval) |
| 8 | Direct full-field dislocation simulation | GCP \$50 (needs approval) |

## Comparison method (per the parent task)

Each `COMPARISON_taskN.md` was written using both skills: `academic-research-skills` deep-research module in fact-check mode (verify each side's claims against sources, record denominators, never invent citations/data) and `cross-domain-discovery` S1–S7 (S3 invariance alignment — do both derivations reduce to the same equations?; S4 Bartha articulation + transportability audit for any transferred claim; S7 Z3/Lean checks where formalizable — the coordinator's exact-arithmetic spot-checks above; the 8-check rubric on the final comparison). The comparison reports respect the cross-domain-discovery skill's own grade cap (**C/F3 until human source/balance gates**). Since the Academia side has not landed, each file is a scaffold with a per-number comparison checklist to complete when it lands.

## What remains

1. **Academia side landing:** when Co-scientist result files appear in the programme directory, run the real per-number comparison per task against the checklists in `COMPARISON_taskN.md`, and upgrade each file from scaffold to completed comparison.
2. **Browser-task handoff:** confirm which tasks launched (8 vs the ten noted in the parent memory) with chat URLs.
3. **Heavy-work approvals:** all caps above await Brandon's approval; nothing to start on GCP without one.
4. **Audit flags:** re-check the Task 2 / Task 8 failed-exec calls in the audit phase; the Task 4 smoke-run explanation is ledgered.
5. **No grades changed** by this programme: all verdicts are local reproductions at the grades stated; the comparison, once complete, may move grades only through the evidence.
