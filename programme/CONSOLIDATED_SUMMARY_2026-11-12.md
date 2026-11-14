# Consolidated Summary — All 15 Co-scientist Tasks (IRH v93.1)

**Date:** 2026-11-12
**Baseline for:** the joint Muse + Academia Co-scientist programme to close all gaps in IRH
**Manuscript under audit:** IRH v93.1 (McCrary), source rebuild `IRH_v93_1_source_rebuilt.txt`
(34 pp., sha256 `cebc3b6f010ed9c059129b4b0ff2c9e3a8ea858e74adc68c3e7fd7d9f34affa8`, 1,638 lines)
**Programme brief:** `PROGRAMME_BRIEF.md` (Brandon's order 2026-11-10 ~16:57 CST)
**Guide:** `SUMMARY_AND_REPLICATION_GUIDE.md` (D4 package guide, 1,394 lines;
WS-D is §6, cross-cutting §8, FAILED/NOT RUN register §9, open questions §12)
**Hark review:** `HARK_REPLICATION_AUDIT_REVIEW.md` (audit of Hark's replication audit,
`D4_package_2026-11-10_replication_audit_4_yq6o.md`, uploaded 2026-11-10 22:36 CST)

## CLAIM + STATUS

**CLAIM.** This document summarises all 15 Academia Co-scientist tasks of the
2026-11-10 programme (workstreams A–E) with HLRE v5.1 grades, the Hark
replication-audit regrades applied, and per-task settled / failed / open lists.

**STATUS: COMPLETE as a summary of delivered work.** No new claims are made
beyond the delivered work; every claim below is cited to its source report
file. No grade moves above **C (Track E)** or **F2 (Track F, two-route)**
on the strength of this programme — all verification is artificial (I1 max);
human source/balance gates were not run. Nothing in this document is filed,
committed, or written into the manuscript. Nothing was run for this summary
beyond reading the source files (no simulations, no GCP spend, no Academia
launches, no contact with anyone).

## 0. How to read this summary

- **Grades.** HLRE v5.1, per narrow claim, worst-of computation shown.
  Track E (empirical/simulation/comparative): cap **C** at I1. Track F
  (formal/deductive): **F1** = kernel-verified in Lean (claimed by no task
  here — the Lean eliminations of branches (a),(b) are Grade A, carried,
  not re-earned); **F2** = machine-checked by exact computation with a
  second independent tool/route; **F3** = machine-checked with a single
  tool/route, or hand-checked. Independence **I1** throughout (single
  pipeline / artificial verification); I2/I3 only where a second
  independent tool or derivation is recorded.
- **Two grade columns.** Each task's report states its own grades; the
  Hark audit then regraded several claims. Both are shown: the report's
  grade first, the corrected grade after "$\to$". Where no regrade applies,
  the report's grade stands subject to the $I1 \to C$ cap on Track E.
- **"FAILED as written"** means the claim exactly as registered is false
  or unreproduced; a corrected version may be verified alongside it. The
  correction is the result, not a defect.
- **ABSTAIN** is a complete answer: it records that the input needed to
  verify a claim does not exist in the manuscript or the available
  sources, with the reason nailed down.
- **"Closed"** (used in the companion gap inventory
  `IRH_GAP_INVENTORY_2026-11-12.md`) means a gap has a graded verdict —
  verified / corrected / refuted / ABSTAIN with the reason nailed down —
  not that the manuscript is vindicated. Several gaps close by showing
  the manuscript claim is wrong.
- **Skills.** Work was done under truth-seeking-frontier v5,
  cross-domain-discovery v2.0.0, and HLRE v5.1. The skills themselves are
  DESIGN CLAIMS, ungraded — skill use is never presented as evidence of
  reliability.

## 0.1 Standing guards (do not violate when citing this programme)

- **Run counts.** WS-A task 5 ran **14 runs** (6000 steps each), STATUS
  VERIFIED for the 14-run protocol. The "143 basin runs" figure in
  Academia's 2026-11-12 email is **Academia's count, NOT ours** — never
  cite 143 as our run count.
- **The "Compare $D_{4}$ Selection Frameworks" gap memo (the 16th task,
  finished overnight Nov $9\to10$; email Nov 9, 5:31 PM CST) is LOCATED and
  AUDITED.** Its three files were pulled from Academia on Brandon's
  "Do both" (2026-11-12) and audited claim-by-claim the same day
  (`compare-d4-frameworks/`, audit `AUDIT_compare-d4-frameworks_2026-11-12.md`,
  591 lines): 189 claims — 166 VERIFIED, 7 CORRECTED, 0 REFUTED,
  16 ABSTAIN; no IRH grade moves. Its headline finding — the gap between
  *selecting* the $D_{4}$ shell and *spontaneously reaching* its full 24-mode
  pattern — is the gap the running 4D field test attacks. Recorded as
  G-E1 (LOCATED) in the gap inventory. (Correction: the first issue of
  this summary dated the task "2026-11-10"; the email is Nov 9, 5:31 PM CST.)
- **The 4D field test is the first joint item and is already running.**
  "Run a four-dimensional field test of $D_{4}$ formation" was launched in
  Academia on 2026-11-12 (browser task; chat
  `02dfb5cb-5423-47eb-9bbe-d8e3d25b6fdc`, RUNNING, free trial, no payment,
  no other task launched). It attacks the truncation gap (24-mode vs
  off-shell modes). Two further tasks from the same email are
  **candidates, NOT launched**: "Map off-shell instabilities of the full
  $D_{4}$ wave" and "Calculate matched $D_{4}$ and $A_{4}$* onset branches". The
  email's other two tasks are **DUPLICATES and must never be re-launched**:
  "Chart the $D_{4}$ stability band under detuning" (= WS-A task 3, delivered)
  and "Derive the first directional anisotropy of $D_{4}$ waves" (= WS-A task
  2, delivered).
- **Awaiting Brandon (not programme-closable):** the 11.85% vs 11.90%
  canonical-band call; the Klein (2001) caveat; the SSRN$\tov93.1$
  selection-principle change; the Hark script fixes (WS-C
  make_figures/task2d provenance, d4model lock metric, WS-A task-1 JSON
  provenance); WS-B separate packaging; the printed-(7) erratum; the
  §III.3 envelope-table conditions; the WS-$D F3\toF2$ question; the torus
  paper as a task-8 ledger entry; the $D_{4}$ bridge question's execution.
- **Grades unchanged.** No IRH grade moves beyond the failed-as-written
  claims listed in §9 of the guide and §4 below. The $D_{4}$ selection
  (S = 64/141), $E_{6}$ via 2T/McKay, SO(8) exclusion, and the INPUT status of
  the three generations are untouched. The brief's "Established IRH
  facts" framing overstates the round-1 review grades for two items
  (Hark F6, §4 below$): C6 (S_{D}_{4}$ wins by 17.3%) is **D as presented** and
  $C8 (E_{6}$ via 2T/McKay; SO(8) excluded) is **D as a physical claim**
  (mathematics A, physical reading IRH's postulate).

## 1. Scoreboard — all 15 tasks

| # | Task (workstream) | Verdict | Grade (corrected) |
|---|---|---|---|
| 1 | 3D projections of the $D_{4}$ standing wave (WS-A) | VERIFIED for the stated finite window | C (Track E); \|Aut$(D_{4})$\| = 1152 **F3** |
| 2 | First directional anisotropy of $D_{4}$ waves (WS-A) | VERIFIED | C (Track E); M6 mean 15 / min 12 / max 18 **F2** |
| 3 | $D_{4}$ stability band under detuning (WS-A) | VERIFIED for stated windows; manuscript 11.85% bracketed, not reproduced | C |
| 4 | Critical droplet + nucleation threshold (WS-A) | VERIFIED (amplitude-equation routes + box runs); thin-wall shown to fail | C |
| 5 | Basin of the full 24-mode $D_{4}$ pattern (WS-A) | VERIFIED for the 14-run protocol; hex6/fcc12 "stable attractors" **FAILED as written** (Hark F1) | C |
| 6 | Branch (a,b) normal form re-derivation (WS-B) | VERIFIED (symbolic cross-check); char-p Gröbner NOT RUN | **F2, I1** (worst-of) |
| 7 | Formalize substrate selection models (WS-C) | CONFIRMED as stated for the measured slice, EXCEPT C1.2 **FAILED as written** | C (Track E); C1.4 **F2** after Hark regrade |
| 8 | Compare quantum-gravity frameworks (WS-D) | Survey COMPLETE as a draft; no framework derives all four at once | C |
| 9 | Compare spacetime frameworks (WS-D) | VERIFIED as a negative characterisation of IRH's text; UNVERIFIED as a comparative ranking | C |
| 10 | Check your derivations (WS-D) | Transcription + two-tool verification COMPLETE; printed (7) **FAILED as printed** | C; D5 C (FAILED as printed); D17 UNVERIFIED; D18 ABSTAIN |
| 11 | Simulate cosmological bifurcations (WS-E) | SPLIT: bifurcation part VERIFIED; cosmic-expansion part ABSTAIN | C (Track E); C1–C4, C6 **F2** after Hark regrade; C7/C8 INCOMPLETE-EVIDENCE; C9/C10 ABSTAIN |
| 12 | Formalize rival accounts (WS-D) | PARTIALLY VERIFIED (55/55 checks pass; physical claims C/D/ABSTAIN) | C (Track E); G1/G5/G8/G12 **F3** (Hark $F3\toF2$ logic NOT applied — open) |
| 13 | Check $D_{4}$ dynamics convergence (WS-C) | CONFIRMED in substance, with C2.2 and P4 **FAILED as written** (corrected versions confirmed) | C (Track E); C2.1 analytic values, C2.5 CFL leg **F2** after Hark regrade |
| 14 | Map QG researchers, Asymptotic Safety, IRH (WS-E) | MAP COMPLETE (73 papers); no retrieved approach close on all three criteria | C (Track E), I1; M8/M9 INCOMPLETE-EVIDENCE |
| 15 | Cosmological signatures: GW + CMB forward model (WS-E) | EXTRACTION COMPLETE; forward model ABSTAINED (no input exists) | C (Track E); forward model ABSTAIN |

**Tallies.** Fully verified (as stated or for the stated scope): tasks 1,
2, 3, 4, 6, 8, 9 (negative characterisation), 10 (arithmetic), 12
(computations), 14 (map). Split / partially verified: 5, 7, 11, 13.
ABSTAIN as the central result: 15 (forward model), and in part 11
(C9/C10). Failed-as-written claims (corrected versions verified
alongside): task 5 hex6/fcc12, task 7 C1.2, task 10 D5 (printed (7)),
task 13 C2.2/P4, task 3 "$\delta = 0.5$ kills the branch" plane-wide, task 9
F1–F6 transfers, task 12 G7/G11-as-prediction. INCOMPLETE-EVIDENCE:
task 11 C7/C8, task 14 M8/M9. NOT RUN: task 6 char-p Gröbner, task 7 Hoy
LJ leg, task 13 N = 24 grid point, task 14 S5/S6/S7, task 15 forward
model.

## 2. Workstream A — core computations (tasks 1–5)

Source directory: `ws-a-core-computations/` (reports `task1_report.md` $\dots$
`task5_report.md`; shared model `d4model.py`). Shared model for all tasks:
damped-wave / Model B dynamics, $L = \pi$, N = 16, $q_{0}^{2} = 8.0$, $r = -0.35$,
u = v = 1, $\bar{\psi} = -0.18$ at the operating point, unless stated otherwise.
**Hark F5 applies to the whole workstream:** the reports grade claims A
and B; all verification is artificial (I1), so the independence bound caps
every Track E claim at **C**. The A/B grades below are the reports' own
grades, shown with the corrected grade after "$\to$".

### Task 1 — Three-dimensional projections of the $D_{4}$ standing wave

**Source:** `ws-a-core-computations/task1_report.md`
**Question:** What do 3D projections of the $D_{4}$ lattice and its 24-mode
standing wave look like, and does any viewing direction yield exact
icosahedral symmetry (manuscript §II.10 / problem IX.1.5)?
**VERDICT: VERIFIED** for the stated finite window $(D_{4}$ points in the ball
R = 5, 1465 points) and the seven directions computed.

- **|Aut$(D_{4})$| = 1152 exactly**, by Gram-matrix enumeration over
  simple-root images $(= 192 \times 6$ = |$W(F_{4})$|). An earlier single-Hadamard-
  triality-generator attempt giving 384 is withdrawn (that map is an
  order-2 diagram automorphism only). Grade B (report$) \to **F3** ($Hark
  regrade: one enumeration route; "matches the known order of $W(F_{4})$" is
  a cross-check, not a re-derivation).
- **No exact icosahedral projection: 5 ∤ 1152**, so no subgroup of
  Aut$(D_{4})$ is icosahedral and no projection direction yields exact
  icosahedral symmetry. Exact order argument, direction-independent.
  Grade $B \to **C$**.
- **$P(D_{4})$ along e4 is $Z^{3} ($simple cubic).** All 485 distinct projected
  positions integral; every $Z^{3}$ point with |x| $\leq 4$ occurs; max
  multiplicity 2. Mechanism exact (parity argument). Grade $B \to **C$**.
- **Slice signatures (exact, 24 projected roots):** e4: 18 distinct peaks;
  d110: 15; d1111: 18; d1110: 24; irrational phi1/phi4/sqrt: 24 each.
  Grade $B \to **C$**.
- **Lattice fraction:** 1.0 rational directions; **$249/1465 \approx 0.16997$**
  for all three irrational directions — flagged as a possible bug,
  RESOLVED as structural $(D_{4} \cap$ span$(\hat{n}) = {0}$ for irrational $\hat{n}$;
  verified on four additional random directions, 7/7). Grade C (measured
  regularity, not a theorem).
- **Bragg-peak splitting** (quasiperiodic signature) for irrational
  directions; rational peaks all full-strength (S = 1465). Grade $B \to **C$**.
- **Hark provenance gap (minor, numbers stand):** the shipped JSON
  carries `n_distinct_positions` / `max_multiplicity`, which the shipped
  script does not write — it came from another script revision. Hark's
  "different lattice basis" did NOT reproduce in the reviewer's env
  (NumPy 2.4.6 vs 2.5.4) — environment-dependent, no number changes.
**Settled:** the Aut$(D_{4})$ order, the icosahedral non-existence, the
projection-vs-cross-section distinction (manuscript §II.10 cross-section
is FCC; the projection is different).
**Failed:** none (one withdrawn attempt, replaced).
**Open:** an *approximate* icosahedral-like pattern in a finite window
(uncomputed); window-dependent counts change with R.

### Task 2 — First directional anisotropy of $D_{4}$ waves

**Source:** `ws-a-core-computations/task2_report.md`
**Question:** What is the first directionally dependent moment of the $D_{4}$
root system? (Manuscript: isotropic through fourth order.)
**VERDICT: VERIFIED.**

- **M6(k) = 60|k|${}^{2}\Sigma_{i}k_{i}^{4} - 48\Sigma_{i}k_{i}^{6}$** — exact SymPy identity, cross-checked
  against direct summation at 50 random directions (max error < 1e-9).
  M2 = 12|k|${}^{2}$ and M4 = 12|k|${}^{4}$ direction-independent (exact isotropy
  through fourth order). Grade $B \to **C** ($Track E).
- **Mean over $S^{3} = 15$ exactly** (spherical moments E[S4] = 1/2,
  E[S6] = 5/16). Grade $A \to **F2** ($Hark regrade: two routes in the
  package — exact symbolic + scipy numerical optimisation).
- **Global min 12** at $\langle100\rangle$ axes and $\langle111\rangle$ body diagonals (AM-GM proof
  of the lower bound); **global max 18** at $\langle110\rangle$ face diagonals
  (Lagrange enumeration + scipy 200 random starts: max
  18.000000000000014, min 11.99999999999999). Max/min = 3/2, i.e.
  **$\pm20$% about the mean**. Grades A (min$) / B (\max) \to **F2** ($Hark).
- **M6 is the root-system moment, NOT the sextic Landau count
  H = 911040** — the two must not be confused.
**Settled:** the sixth moment is the first directionally dependent
moment, with exact mean and extrema and the $\langle110\rangle-\max / \langle100\rangle$,$\langle111\rangle-\min$
directional signature.
**Failed:** none. **Open:** a hand proof of the upper bound $M6 \leq 18$|k|${}^{6}$
would raise that claim from numerically verified to proven; whether a
given sixth-order *observable* tracks M6 depends on its coupling.

### Task 3 — Chart the $D_{4}$ stability band under detuning

**Source:** `ws-a-core-computations/task3_report.md`
**Question:** Where in the $(\bar{\psi}, r)$ plane does the full 24-mode $D_{4}$ pattern
win, and how do detuning $(\delta = q_{0}^{2} - 8)$ and the sixth-order coupling $w_{6}$
move it?
**VERDICT: VERIFIED** for the stated windows and the one-mode Landau
functional with sub-pattern family {hex6, fcc12, sq4, sq8} (tri3 excluded
for cause: Q = 0 makes its functional unbounded below at $w_{6} = 0$ and
stabilised only at unphysical amplitude $A \approx 2.7$, $F \approx -33$, at $w_{6} > 0)$.

- **Band fractions (window W1, $\bar{\psi} \in [-0.6, 0.2] \times r \in [-0.6, 0.1]$,
  $161\times161): 11.60$% at $(\delta = 0$, $w_{6} = 0) \to 8.36$% at $(\delta = 0$, $w_{6} = 0.2)$**;
  hex-only 12.94% $\to 9.68$%. Manuscript 11.85% lies between the full-family
  and hex-only values — **bracketed, not reproduced** (manuscript window
  unstated). Grade $B \to **C$**; "manuscript 11.85% reproduced" is **C (not
  reproduced)**.
- **Detuning shifts the band by exactly $\delta^{2}$ in r:** coexistence line at
  $\bar{\psi} = -0.18$ moves from $r = -0.218 (\delta = 0)$ to $r = -0.468 (\delta = 0.5)$.
  Grade $B \to **C$**.
- **"$\delta = 0.5$ kills the ordered branch" — TRUE at the operating point**
  (discriminant < 0 at $(\bar{\psi}, r) = (-0.18, -0.35)$, matching the
  manuscript'$s q_{0}^{2} = 7.5$ result) but **FALSE plane-wide: the band
  persists in-window at $\delta = 0.5 (8.18$% in W1)**, shifted to deeper r.
  Corrected to the shift statement. Grade C (corrected).
- **Band boundaries:** coexistence line $F_{full} = 0$ and competition line
  $F_{full} = F_{hex}$ tabulated by exact brentq; coexistence at $\bar{\psi} = -0.18$,
  $r = -0.2180$, independently matching Task 4'$s -0.217984$. Grade $B \to **C$**.
- **Operating point:** A* = 0.0776, $F = -0.007632 ($manuscript $-0.0076323)$;
  full beats hex $(-0.002254)$ and fcc$12 (-0.005362)$. Minimiser validated
  against scipy bounded Brent at 12 random points (< 1e-6).
**Settled:** the band's extent is set by the coexistence and competition
lines; detuning shifts it by $\delta^{2}$; $w_{6}$ narrows it (11.60% $\to 8.36$% vs
manuscript 11.90% $\to 8.47$%).
**Failed (as written):** the plane-wide "$\delta = 0.5$ kills the branch" reading.
**Open:** the manuscript's exact window (needed to reproduce 11.85%);
the band against a larger competitor family; the full (relaxed)
free-energy band $(\approx1$% shift expected).

### Task 4 — Critical droplet and nucleation threshold

**Source:** `ws-a-core-computations/task4_report.md`
**Question:** How large is the critical droplet, and does the manuscript's
§II.9 barrier-vanishing statement hold?
**VERDICT: VERIFIED** for the amplitude-equation routes $(\kappa$, thin-wall,
radial ODE) and the finite-box droplet runs. The thin-wall numbers are
reported as the failed approximation, not the answer.

- **$\kappa = 192** ($gradient coefficient, in the $(\kappa/2)$|$\nablaA$|${}^{2}$ convention) —
  derived from the Swift–Hohenberg operator, verified by exact FFT energy
  of a modulated pattern (relative deviation 4.2e-05). Grade $B \to **C$**.
- **Coexistence $r_{coex} = -0.217984$**, A*_c = 0.058251; surface tension
  $\sigma = 0.018776 ($two independent quadratures agree exactly).
  Grade $B \to **C$**.
- **Thin-wall: $R_{c} = 7.38$, $\DeltaF* = 37.2$ — shown to FAIL here**, because the
  correlation length $\xi = \sqrt{(192/(24\cdot0.1072))} = **8.64$ exceeds** the
  thin-wall radius. Grade C (approximation shown to fail).
- **Radial-ODE critical droplet (exact within the amplitude equation):
  $R_{c} = 12.57$, $\DeltaF* = 555** ($trapezoid 555.2 vs Simpson 554.71, 0.1%
  agreement); core A(0) = 0.0566 never reaches bulk A* = 0.0776 —
  **thick-walled, not thin-walled**; exact barrier ~$15\times$ the thin-wall
  value. Grade $B \to **C$**.
- **Box droplet runs (8 seeds, 6000 steps each):** only the smallest,
  weakest seed (R = 0.6, A = A*) decays; all seven others grow to the
  full ordered state within 250–500 steps. Grade $B \to **C$**.
- **Scale mismatch (key interpretive point):** ODE $R_{c} = 12.57 \gg$ box
  half-size L/2 = 1.57, and $\lambda = 2\pi/\sqrt{8} = 2.22$ — the box runs map the
  finite-box nucleation threshold (periodic-image interactions), not the
  infinite-volume $R_{c}$. Neither invalidates the other.
- **§II.9 confirmed:** $r_{eff}$ vanishes at $\bar{\psi} = **-0.1439** ($exact
  spinodal); at $\bar{\psi} = -0.10, r_{eff} = -0.12 < 0$, no barrier. The
  manuscript's "$\approx -0.10$" is a rounded statement of the spinodal.
  Grade $B \to **C$**.
- **Load-bearing bug found here (and independently in WS-C):** the
  shipped-style Model B update grows an anti-Hermitian roundoff
  component $\times1.0142$/step to NaN by ~6000 steps. Fix: per-step Hermitian
  symmetrisation (exact no-op in exact arithmetic). All package Model B
  results use the fixed stepper.
**Settled:** the droplet is large and thick-walled; thin-wall fails;
§II.9's barrier-vanishing statement is confirmed with the exact spinodal.
**Failed:** the thin-wall approximation (as an answer here).
**Open:** a full-PDE critical droplet (beyond the amplitude equation,
~1–10% refinement); a larger-box droplet run $(L = 2\pi$, N = 32 — costed,
not run: ~25 min/seed locally, several seeds needed; a GCP-scale job
needing a named cap).

### Task 5 — Basin of the full 24-mode $D_{4}$ pattern

**Source:** `ws-a-core-computations/task5_report.md`
**Question:** Under conserved Model B dynamics, is the full 24-mode $D_{4}$
pattern a strong attractor, and what else attracts?
**VERDICT: VERIFIED for the 14-run protocol (6000 steps each)** — with the
sub-pattern trapping claims **FAILED as written** (Hark F1, below).
**14 runs, not 143** (see §0.1).

- **Full pattern recovers** from phase perturbations up to **1.0 rad RMS**
  and **$\pm20$% amplitude** perturbations (4 runs, all to $D_{4} = 1.000$,
  Fexc = $-0.007728)$. Grade $B \to **C$**. Untouched by F1 (those starts have
  all 24 modes present).
- **hex6 / fcc12 "stable attractors" — FAILED as written (Hark F1,
  VERIFIED by the reviewer's own run).** The package seeded sub-patterns
  with the other $D_{4}$ modes exactly zero, a start sitting in a subspace
  the dynamics preserves; persistence there says nothing about stability
  to the absent modes. Hark's transverse test: hex$6 + \varepsilon\cdotA$* in the 18
  absent modes $\to$ full24, **5/5** at $\bar{\psi} = -0.18$; fcc12 + same $\to$ full24,
  **4/4**; $\varepsilon = 0$ control stays hex6 (reproducing the package run exactly
  — the invariant-subspace artefact). **Corrected statement (I1,
  C-capped): at $\bar{\psi} = -0.18$ the 24-mode is the only attractor seen from
  perturbed starts; hex6/fcc12 are saddles.** At $\bar{\psi} = 0$ hex6 is stable
  and the 24-mode is not (Hark'$s \bar{\psi} = 0$ result, NOT re-run by the
  reviewer). The task-5 sentence "this is the mechanism behind the
  manuscript's annealed 6-mode outcome, now shown for Model B" is
  **withdrawn** — under Model B at $\bar{\psi} = -0.18$ hex6 is not a trap. (The
  damped-wave 6-mode quench outcomes in WS-C are unaffected: those start
  from noise in all modes, and that dynamics drifts $\bar{\psi} \to +0.0025$, where
  hex6 is the lower state.)
- **sq4/sq8 decay to uniform** (T = 0, no triads, no cubic term).
  Grade $B \to **C$**.
- **Noise seeds decay (6/6, amp 0.05)** — uniform state metastable
  $(r_{eff} = +0.107 > 0)$; nucleation needs a localised large-amplitude
  seed (Task 4). Grade $B \to **C$**.
- **Basin map as stated** (full / sub-pattern traps / uniform) — grade B
  $\to **C$**, with the sub-pattern-trap leg now FAILED as written (see
  above); the corrected basin map is: large-amplitude / full-pattern
  starts $\to$ full24; hex6/fcc12 starts $\to$ full24 under any transverse
  perturbation at $\bar{\psi} = -0.18$; small noise or triad-less starts $\to$ uniform.
- **Hark F2 (minor defect):** the triad `lock` metric averages cos S
  over all 32 triads including roundoff modes, so it is ill-defined /
  platform-dependent for partial patterns (hex6 0.304 / 0.455 vs shipped
  1.000). Fix (active triads only) is correct; no load-bearing conclusion
  rests on the sub-pattern lock value. Script fix offered, Brandon's call.
**Settled:** full-pattern robustness (1.0 rad / $\pm20$%); noise decay;
sq4/sq8 decay; the corrected basin map at $\bar{\psi} = -0.18$.
**Failed (as written):** hex6/fcc12 as stable attractors / local minima.
**Open:** the critical phase-noise amplitude between 1.0 rad and full
dephasing; a larger-box repeat (periodic images may stabilise
sub-patterns); the 24/24-from-noise rate beyond 0/6 seeds (WS-C: 0/5).

## 3. Workstream B — branch normal form (task 6)

**Source:** `ws-b-branch-normal-form/REPORT.md`
**Note:** this is Jacobian-conjecture work, not $D_{4}$/IRH physics — the
re-derivation of the branch (a,b) normal form (NewtonNF2) for the GGHV
(72,108) case. It was excluded from the $D_{4}$ package zip; separate
packaging was offered 2026-11-10 and is unanswered (Brandon's call).
**Question (Brandon's wording):** "Verify the branch normal form.
Re-derive the branch (a,b) normal form in your hypothetical (72,108)
counterexample using symbolic computation. Check each derivation step
numerically, including limiting cases, and flag any discrepancies."
**VERDICT: VERIFIED (symbolic cross-check). 112 SymPy checks pass (exit
0), all Singular checks pass, the a816 certificate re-verifies, and the
descent is rebuilt from scratch in an independent $K_{5}$ implementation.**

- **Overall: Track F, grade F2, independence I1** (worst-of across
  C1–C10; I1 driven by C2 and C10, single-tool). Nothing here is F1
  (kernel-verified) — that grade belongs to the Lean `main_theorem`
  alone and is not claimed. Scope: a CROSS-CHECK, not a re-proof; branches
  (a),(b) are already eliminated in Lean, Grade A, kernel-verified.
- **$C1 \phi$-morphism (F2, I2):** the $\phi$-exponent map (i,j) ↦ $(4j-i,j)$ sends
  pre-$\phi$ vertices exactly to post-$\phi$ vertices; $\det D\phi = -x^{2}$; chain rule
  checked exhaustively by Singular over all $25 \times 47 = **1175$ monomial
  pairs: 0 failures**. (Also confirms |N(P)| = 25, |N(Q)| = 47.)
- **C2 lattice/Pick/predicates (F2, I1):** |$N(P) \cap \mathbb{Z}^{2}$| = 25,
  |$N(Q) \cap \mathbb{Z}^{2}$| = 47; Pick areas 15 / 33 with boundary 18 / 26, interior
  7 / 21; half-plane predicates cut out exactly the polygon lattice sets.
- **C3 layer decomposition, 92 equations (F2, I2):** bracket-of-layers
  identity for all 11 (a,b) pairs; five-layer decomposition in 3 random
  specializations; 72 unknowns; counts 17/18/19/19/19. (E1's generic 19
  rests on SymPy trials; one Singular specialization gives 11 by
  accidental cancellation — the identity holds exactly.)
- **C4 E5 eliminants m = 1,3,5 (F2, I2):** m = 1 one-parameter family;
  m = 3 degree 3 (3 solutions, eliminant $3a_{2}^{3}-32)$; m = 5 degree 10
  (10 solutions, eliminant $9a_{4}^{10}+37200a_{4}^{5}+95051008)$; separable,
  irreducible, chart iff relations hold.
- **C5 m = 7 eliminant W, Belyi identity (F2, I1):** W degree 35, quintic
  in $a_{6}^{7}$, irreducible, separable, exactly one real root $\approx$
  3208.612478738048; $\phi'\cdot\alpha^{4} = \beta\cdotE5$lhs as a polynomial identity.
- **$C6 K_{5}$ point, Davenport bound (F2, I2):** the $K_{5}$ top-layer point
  satisfies E5 exactly; $\alpha$, $\beta$ separable and coprime; 2fg$'-3f'g = 2$;
  $\deg(g^{2}-(B^{2}/a_{7}^{3})f^{3}) = 8 ($extremal).
- **C7 chart system + witness (F2, I2):** the 16 Lean chart equations are
  exactly the E5 coefficient equations; the parsed witness satisfies all
  17 chart equations; $\kappa = B^{2}/a_{7}^{3}$ rescaling verified; inversion
  certificates hold.
- **C8 descent, 35 minors, $b_{12}$,${}_{24} = 0 (F2, I3)$:** E4 rank 17 / kernel dim
  2; E3 rank 18 / kernel dim 2, solvable for every t; E2 operator rank 12
  (injective) with 7 compatibility conditions; the 35 minors span
  $K_{5}[t_{1},t_{2}]_{5}$ and their row space equals the stored certificate's; the
  t = 0 collapse forces **$b_{12}$,${}_{24} = 0$**.
- **C9 a816 certificate (F2, I$2):** a_{8}$,${}_{16}^{2} = \Sigma H_{k} e_{k}$ over $K_{5}$ re-verified
  (76 cofactors, 3464 terms; python-flint rebuild VALID; Singular over
  $\mathbb{Q}(w)$ VALID; all negative controls rejected). Only the main certificate;
  the second certificate (`a816_lift_liftstd.txt`) is not committed and
  was not re-verified.
- **C10 limiting cases (F2, $I1):** \lambda = 0$ degenerate family (E5lhs $\equiv 0$,
  $g^{2} = f^{3}$, excluded by $\alpha(0) = 1); a_{7} = 0$ cascade $(E_{10}$ gives 21 = 0);
  characteristic-2 S-recursion break and characteristic-3 cascade break.
**Settled:** the normal form re-derives exactly as stated in the combined
paper and the Lean `BranchAb` material; no discrepancy against the Lean
elimination was found.
**Failed:** none (all failures encountered were the author's own script /
tooling errors, corrected with evidence and listed in the report §9).
**Open / NOT RUN:** **U1 — characteristic-p Gröbner dim/degree of the
chart system over 𝔽${}_{101}$, 𝔽${}_{3}$, 𝔽${}_{5}$, 𝔽${}_{7}** ($timed out at 570 s; costed plan:
faster machine — e.g. lean-build-4's 24 cores once leg-9 ends, never
while it runs — a longer budget, or a smarter method such as msolve or
the S-recursion/torus route). **U2** — second a816 certificate (needs
producing/committing first). **U3** — GGHV exhaustiveness and the
reduction chain (out of scope). **U4** — the m = 7 completeness argument
via Riemann's existence theorem (eliminant verified; the completeness
step not re-derived).
**Tooling note recorded for the programme:** Singular 4.4.1 (conda-forge)
**hangs on `continue` inside a for-loop** (verified by bisection) and
`a^b/c` parses as `a^(b/c)` — parenthesise explicitly. (Already in
`TOOLS.md`.)

## 4. Workstream C — substrate convergence (tasks 7 + 13)

Source directory: `ws-c-substrate-convergence/` (reports
`task1_substrate_selection_models.md`, `task2_d4_dynamics_convergence.md`;
register `CLAIM_REGISTER.md`). Standing: Tier Standard, Track E (cap C),
except C1.4 / C2.1a / C2.5 as Track F (cap F3 in the reports); independence
ceiling I1; exact checks cross-verified with a second tool (SymPy +
python-flint + Z3 in `code/exact_checks.py`, 29 check statements $\to 31$
[PASS] lines, exit 0 — both countings true).

### Task 7 — Formalize substrate selection models

**Source:** `ws-c-substrate-convergence/task1_substrate_selection_models.md`
**Question:** Can the static-$D_{4}$ account (postulated lattice, v92 ontology)
and the dynamically-selected-$D_{4}$ account (v93.1 tension–relaxation nodal
pattern) be formalized as rival substrate-selection models, simulated
under shared conditions, and do their interference-pattern predictions
diverge exactly outside a falsifiable boundary?
**VERDICT: CONFIRMED as stated for the measured slice $(r = -0.35$,
$q_{0}^{2} = 8.0$, N = 16, $L = \pi)$, with the band edges measured, not assumed —
EXCEPT C1.2, which is FALSIFIED as registered.**

- **C1.1 (static account predicts full 24-mode pattern under ALL
  conditions) — C, Track E.** 24/24 imposed at every $\bar{\psi}$, including
  $\bar{\psi} = -0.30$ where Fexc > 0; no manuscript statement giving the static
  account a selection dynamics was found.
- **C1.2 (dynamic account predicts full 24-mode ONLY inside the band) —
  FAILED as written.** The register's own falsifier Q2: noise quench at
  $\bar{\psi}_{0} = -0.18 ($inside the quoted band) reaches **6/24**. The
  basin/evolved-$\bar{\psi}$ corrected version is CONFIRMED under C1.3. Hark
  regrade: FAILED as written, unaffected by the regrade.
- **C1.3 (divergence boundary D1–D4) — C, Track E.** All four legs
  confirmed at probe points; branch edge exact (two tools). **$D1** \bar{\psi}$
  outside $(-0.235, -0.125)$; **D2** |$q_{0}^{2}-8$| > 0.4024; **D3** triad
  coupling off $(u = 0) \to 12$-mode, not 6-mode; **D4** noise initial
  condition (outside the full-pattern basin$) \to$ sub-pattern (6/2/8-mode
  by seed). Agreement only inside the band, with $q_{0}$ tuned, triads on,
  and a seeded/basin initial condition.
- **C1.4 (ontology change dissolves the circularity objection; $a_{0}$ =
  $2\pi/q_{0}$ is an output of the dispersion, not an input via $L_{P})$ — F3 in
  the report $\to F2 ($Hark regrade; exact_checks SymPy + flint + Z3,
  31 PASS, reviewer re-ran it).**
- **C1.5 (static account CANNOT explain lattice selection, finite band,
  6-mode outcome, nucleation, Model A vs Model B) — C, Track E.** (b),
  (c), (e) measured directly; (a), (d) established by absence of the
  relevant structure in the static formulation (manuscript §I.1).
- **C1.6 (Landau + LJ corroborate the winner; S-transfer deductive;
  near-melting scope does NOT transfer) — C, Track E.** S4 split verdict
  (combinatorial PASS, scope FAIL); Hoy [40] LJ-MD leg NOT RUN (A5).
- **Measured 24-mode global-minimum band at $r = -0.35$: $\bar{\psi} \in (-0.235$,
  $-0.125)** (0.01$ grid). The manuscript's quoted $(-0.33$, +0.03) is the
  union over quench depths in the full $(\bar{\psi}, r)$ phase diagram; the **+0.03
  edge is UNVERIFIED** against this slice. At $\bar{\psi} = -0.18$: A* = 0.0775753,
  $F/V = -0.0076323 ($ansatz); relaxed field $-0.0077276 (1.24$% harmonic
  lowering); branch exists iff $r_{eff} \leq 0.2691$, i.e. |$q_{0}^{2}-8$| $\leq 0.4024$.
- **Noise quench never reaches the full 24-mode pattern in this setup**
  (5 seeds: 6-mode $\times3, 2$-mode, 8-mode). **Mean forgetting (wave
  dynamics):** damped-wave quench equilibrates to $\bar{\psi}$_final $\approx +0.0025$
  from any $\bar{\psi}_{0} \in {-0.30, -0.18, 0, +0.10}$.
- **Model B instability diagnosed and fixed:** shipped sim6 Model B blows
  up at t = 27.5 (NaN) via the unphysical anti-Hermitian sector (growth
  1.0142/step); fix is per-step Hermitian projection (exact no-op in
  exact arithmetic, measured no-op error 3.8e-16); with projection the
  attractor is stable through $t = 30 (\langleA\rangle = 0.077682, \bar{\psi} = -0.180000$,
  $D_{4} = 1.0000$, 24/24, Fexc = $-0.007728)$. Shipped sim6 file NOT modified.
- **Task 1 findings 6–7 ("Both patterns are local minima at both $\bar{\psi}$";
  "24-mode is a local minimum outside the band") — FAILED as written,
  per Hark F1 (VERIFIED by the reviewer's own run; see Task 5 above).**
  Corrected: at $\bar{\psi} = -0.18$ the 24-mode attracts perturbed hex6 and fcc12
  starts; hex6/fcc12 are saddles; the "24-mode is metastable outside the
  band" reading is an invariant-subspace artefact.
- **Barenblatt classification of the band edge: NOT ESTABLISHED —
  ABSTAIN.** S5 blending: rational reconstruction, grade D by
  construction. S6 tournament as LLM Elo: NOT RUN (replaced by the
  simulation probe grid). Lean re-verification: NOT RUN.
**Settled:** the static vs dynamic accounts diverge exactly at D1–D4;
the v93.1 ontology change dissolves the circularity objection as a matter
of logic (C1.4, F2); the 24-mode is the global minimum and the attractor
inside the measured band, reached from seeded/basin initial conditions;
Model B instability diagnosed and fixed.
**Failed (as written):** C1.2; findings 6–7; P4's fixed-point form
$(\langleA\rangle$ error vs A* does not decrease with dt — a model-form gap, not a
discretization error; see Task 13).
**Open:** the manuscript's quoted band edges vs the measured slice (the
+0.03 edge unverified; band's r-dependence is WS-A task 3's map); the
24/24-from-noise rate beyond 0/5 seeds (run $n \geq 20)$; whether the 2-/8-mode
quench outcomes are transient; the Barenblatt classification; the Hoy LJ
leg; a mechanistic account of what fixes $\bar{\psi}$ and supplies nucleation
(manuscript IX.5) would change D4 from "conditional on basin IC" to
"selected".

### Task 13 — Check $D_{4}$ dynamics convergence

**Source:** `ws-c-substrate-convergence/task2_d4_dynamics_convergence.md`
**Question:** Does the reference tension–relaxation model (sim6 Model B
semi-implicit attractor, N = 16, $L = \pi$, $q_{0}^{2} = 8.0$, $r = -0.35$, u = v = 1,
$\bar{\psi} = -0.18$, dt = 0.005, T = 30) reproduce the analytic stationary state;
does its discretization error decrease along the grid/time-step ladder
with a measurable convergence order; and are discretization, input, and
model-form errors separately tabulated?
**VERDICT: CONFIRMED in substance, with two claims FAILED as written and
corrected — the corrections are the result, not a defect.** The attractor
fixed point is resolution-independent, so there is no decreasing
discretization error to fit for the fixed-point state. The genuine
convergence order lives in the transient: first order (Richardson
$p \approx 0.9$–1.0 at T = 0.5), as expected for semi-implicit Euler. The error
budget is dominated by input (seed spread) for quenches and by model form
(ansatz vs relaxed, 1.24%) for the attractor — not by discretization.

- **C2.1 (reference model reproduces the analytic stationary state) — C
  (Track E part); $F3 \to F2 ($Hark regrade, analytic A*/F/V; two tools:
  exact_checks + WS-E bifurcation checks).** $\langleA\rangle = 0.077682$ / Fexc =
  $-0.007728$ differ from ansatz values by the measured harmonic gaps
  (+0.137%, $-1.24$%); $D_{4} = 0.999981 ($harmonic deficit 1.9e-5); 24/24 ✓;
  $\bar{\psi}$ conservation measured 1.1e-15, not $1e-16 \to C$.
- **C2.2 (discretization error decreases with N and dt, measurable order)
  — FAILED as written.** Fixed-point error is 0 at every ladder point (no
  decrease to measure); transient error DOES decrease, $p \approx 0.95$ — the
  corrected claim is confirmed, the registered claim is not. Hark regrade:
  FAILED as written, unaffected.
- **C2.3 (input error quantified separately) — C, Track E.** Seed spread
  (5 seeds), $\bar{\psi} \pm0.01$, $q_{0}^{2} \pm0.1$ all measured; input dominates
  discretization at reference resolution.
- **C2.4 (model-form error quantified) — C, Track E.** (a) ansatz vs
  relaxed 1.238% re-measured; (b) Model B vs wave = mean-only difference;
  (c) sim6 vs sim7 = setup difference, stated, not conflated with error.
- **C2.5 (CFL respected; $\bar{\psi}$ conservation at the 1e-16 level) — C
  (conservation leg); $F3 \to F2 ($Hark regrade, CFL leg; exact_checks
  SymPy + flint + Z3, 31 PASS re-ran).** CFL: $a_{0} = 2\pi/q_{0} = 2.221441$,
  dt_$\max = (\sqrt{3}/2)a_{0}/c = 1.923825$; largest dt used anywhere 0.04 — $48\times$
  below the bound; reference dt 0.005 is $385\times$ below. Conservation: best
  measurement 1.1e-15 at t = 7.5, one order coarser than the reference
  $8.3e-17 \to C$ worst-of; P5 (< 1e-12) PASS (drift 1.58e-15 at t = 30).
- **P4 (attractor $\langleA\rangle$ error vs A* decreases with dt) — FAILED as
  written.** Error is constant 0.000106 at every dt (model-form gap);
  transient error DOES decrease with dt, $p \approx 0.95$.
- **$P5 (\bar{\psi}$ drift < 1e-12 at every ladder point) — PASS.**
- **Attractor ladder — resolution-independence:** at every N and dt the
  fixed point is $\langleA\rangle = 0.077682$, $D_{4} = 0.999981$, 24/24, lock = 1.0,
  rms = 0.380565, Fexc = $-0.007728$, $\bar{\psi} = -0.18$ — identical to 6 decimals
  at all 8 ladder points $(N \in {8, 12, 16, 20} \times$ dt $\in {0.02, 0.01, 0.005$,
  0.0025}). Discretization error of the fixed-point state is 0 below
  1e-6 at every ladder point.
- **Quench ladder:** N = 8 FAILS (grid too coarse; triad/quartet
  interactions alias); $N = 12 \to 6$-mode; $N = 16 \to 6$-mode; seeds 3–5:
  6-mode, 2-mode, 8-mode; Fexc spread $-0.0358$ to $-0.0418 (~15$% of
  |Fexc|); no seed reaches 24/24.
- **Input sensitivity (attractor$):** \bar{\psi} \pm0.01$ moves $\langleA\rangle$ by $\pm0.0013 (1.6$%)
  and Fexc by $\pm0.0013 (17$% of |Fexc|); $q_{0}^{2} \pm0.1$ moves $\langleA\rangle$ by $-0.0011$
  (1.4%), Fexc +0.0007 (9%).
- **Hark F4 — provenance gap, VERIFIED (not a numerical error):**
  `task2d_transient.py` runs T = 5 only and overwrites the CSV with mode
  `'w'`; the shipped CSV's T = 0.5/1.0 rows carry `seconds=0` (not
  produced by this script); `make_figures.py` line 85 filters
  `r["T"] == "0.5"` and line 88 indexes `err[-1]` — after a clean task2d
  re-run it crashes (`IndexError` at line 88). The numbers stand (shipped
  T = 0.5 rows match Hark's regenerated values exactly; $p \approx 0.95$
  stands); the provenance is broken. This breaks guide §9 as written.
  Script fix offered, Brandon's call.
**Settled:** attractor fixed point resolution-independent; genuine
convergence order is in the transient (first order, $p \approx 0.95)$; error
budget separated; CFL respected at every dt; P5 conservation PASS; $N \geq 12$
required; wave-vs-Model-B difference is the mean only.
**Failed (as written):** C2.2, P4. **Provenance gap:** F4 (numbers stand).
**Open:** the reference run's 8.3e-17 conservation value at full precision
(UNVERIFIED — best 1.1e-15 with projection; C2.5 conservation leg PARTIAL,
grade C); whether 2-/8-mode quench outcomes are transient; the
24/24-from-noise rate beyond 0/5 seeds; N = 24 (not run, no information
expected).

## 5. Workstream D — frameworks + rivals (tasks 8, 9, 10, 12)

Source directory: `ws-d-frameworks-rivals/` (reports `task8_qg_frameworks.md`,
`task9_spacetime_frameworks.md`, `task10_derivations_check.md`,
`task12_rival_accounts.md`; summary `ws-d_summary.md`). Standing:
deepest-research FULL mode; systematic-review mode NOT chosen/used. All
new verification artificial, I1 max; Track E cap C / Track F cap F3; human
source/balance gates not performed. **No IRH grade is changed by any task
in this workstream.** WS-D was NOT in the audited $D_{4}$ package, so the Hark
regrade was not applied to it (see the $F3\toF2$ question in §7 below and
guide §12 Q10).

### Task 8 — Compare quantum-gravity frameworks

**Source:** `ws-d-frameworks-rivals/task8_qg_frameworks.md`
**Question:** Of loop quantum gravity / spin foams, string theory (and
AdS/CFT), asymptotic safety, causal dynamical triangulations, causal set
theory, group field theory, emergent/analogue gravity, and IRH v93.1 —
which derives Lorentzian signature, the Einstein equations with
diffeomorphism invariance, the Standard Model gauge structure, and a
confirmed prediction, all at once?
**VERDICT: Comparative survey COMPLETE as a draft. No framework in the set
derives all four at once** — "no framework has a laboratory-confirmed
Planck-scale prediction, and no framework has derived the Einstein field
equations together with Lorentzian signature, diffeomorphism invariance,
and the Standard Model gauge structure from its own postulates without
additional input."
**Grades (Track E, I1):** C1 LQG discreteness, C2 EPRL dynamics, C3
String/AdS-CFT conjecture, C4 asymptotic safety, C5 CDT, C6 causal sets +
$\Lambda$ prediction, C7 GFT condensate cosmology, C8 analogue kinematics-not-
dynamics, C9 Jacobson conditional derivation, C11 IRH open problems, C12
no confirmed Planck-scale prediction — **all C**. C9-interpretation
("gravity is emergent") — **D** (exploratory; live alternatives). C10 IRH
geometric core — **A (carried from repo record, cited not re-earned)**;
IRH physical/substrate reading — **C/D (carried)**. Bartha gate — **FAIL**
(see below).

- **CDT** has the strongest *derived* emergence result (numerical 4D de
  Sitter universe; spectral dimension $4.02 \pm 0.1$ large scales $\to$
  $1.80 \pm 0.25$ short distances; $D_{s}(\sigma) = 4.02 - 119/(54+\sigma)$; simulated
  universe linear size 17–28 Planck lengths).
- **Causal sets** have the only prediction-in-advance (Sorkin 1997
  heuristic $\Lambda \sim 1/\sqrt{V} \sim 10^{-120}$, pre-1998 discovery); the "only successful
  prediction" superlative was DROPPED in assembly (phrase not found in
  Surya LRR 2019).
- **LQG's** sharpest derived result is kinematic (discrete area/volume,
  Rovelli–Smolin 1995); EPRL large-spin Regge asymptotics, continuum /
  classical limit still open. **AdS/CFT** is a conjecture (Maldacena
  1997), formulated in AdS not de Sitter, not proved. **Asymptotic
  safety:** Reuter fixed point is truncation-only evidence. **GFT:**
  condensate yields a modified Friedmann equation
  (Gielen–Oriti–Sindoni 2013); condensate-as-GR-geometry step
  unestablished.
- **IRH's position** is the narrowest and most checked at the geometric
  level $(D_{4}$ selection, $E_{6}$ via 2T/McKay, Grade A carried), while its
  gravity side is open or retracted by its own Part IX.
**Failed / refuted:** transfer "substrate dynamics $\Rightarrow$ Einstein equations"
— **Bartha FAIL** (§6.1), for IRH and analogue gravity generally;
confirms IRH v93.1's own retraction against Barceló–Liberati–Visser 2011
and Sindoni 2012. "Jacobson $\Rightarrow$ IRH transport" — **FAILS / NOT ESTABLISHED**
(thermodynamic premises $S \propto A, \deltaQ = T$ dS, local equilibrium have no
positive analogue in IRH). "Dynamical signature $\Rightarrow$ IRH reading (A)" —
**FAILS for v93.1** (fermion-dominant loop absent from a single real
scalar).
**Open (ABSTAIN):** Barbero–Immirzi numerical value / quantitative
LQG black-hole-entropy matching; string landscape vacuum counts;
SUSY/extra-dimension exclusion limits; Strominger–Vafa microstate
counting as a load-bearing claim; 2023 GFT "justified" gloss
(SECONDARY-ONLY). Classical/continuum limit unproved for LQG/spin foams,
CDT, GFT, causal sets; de Sitter vs AdS unresolved. S2/S5/S6/S7 NOT RUN.

### Task 9 — Compare spacetime frameworks (IRH vs rival accounts)

**Source:** `ws-d-frameworks-rivals/task9_spacetime_frameworks.md`
**Question:** Does IRH v93.1's account of spacetime and dimensionless
constants derive spacetime signature, the Einstein equations, or the
numerical values of dimensionless constants — and how do rival accounts
(standard QFT, Greensite/Carlini–Greensite dynamical signature,
Mukohyama–Uzan/Kehayias classical emergent signature, analog/emergent
gravity, varying constants/Dirac, anthropic/multiverse, Eddington-style
and $E_{6}$ unification, causal sets, noncommutative geometry) compare?
**VERDICT: VERIFIED as a negative characterisation of IRH's own text**
(the manuscript itself states each of (i)–(v) in the CLAIM);
**UNVERIFIED as a comparative ranking** — no rival derives the constants
either, and none is shown superior to IRH on IRH's own selection problem
$(D_{4}$ selection). The comparison is "a coding and gap-flagging exercise, not
a verdict that any framework wins." Every cross-framework transfer
attempted **FAILS** as a derivation-transfer under Bartha (S4).
**Grades (Track E, I1 max, cap C):** C1 triad relations definitional, C2
$\alpha^{-1}$ ansatz (arithmetic verified; derivation absent), C3 dimensional
assignment undecided, C4 no IRH signature mechanism, C5 analog gravity
gives effective metric not $G = 8\piT$, C6 standard QFT takes constants as
inputs, C8 causal-set/NCG scoped characterisations — **all C**. C7 "no
surveyed rival derives $\alpha$" — **C scoped / UNVERIFIED as a universal
negative** (verified for surveyed sources only). C9 any transfer of a
rival's signature/gravity mechanism into IRH — **FAILED as
derivation-transfer in every case attempted**.

- **$\alpha^{-1}$ ansatz = $137 + 1/(28 - \pi/14) = 137.036002821941$**; CODATA 2022
  $\alpha^{-1} = 137.035999177(21)$; difference **+$3.64\times10^{-6}** (\approx 27$ ppb).
  Arithmetic exact; derivation absent; downgraded numerical ansatz in
  the Eddington class. (Task 10's clean flint run supersedes task 9's
  ad-hoc run, which errored after printing the values.)
- **R = 2589 normalisation: downgraded**; "the subtraction of 3 is not
  forced by any displayed symmetry"; arithmetic unverifiable-from-source,
  carried as downgraded, not re-derived.
- **Triad check $K1:** a_{0}\Omega_{P} = c$ from the stated definitions — SymPy PASS
  (algebraic consistency only).
- **$S = 64/141 \approx 0.4539$**; margin $73/423 \approx 17.26$% over $A_{4}* (S = 12/31)$;
  $\tau_{D}_{4}/\tau_{BCC} = \sqrt{2}$ exactly; $D_{4}$ band 11.85% of scanned plane (11.90% also
  stated — discrepancy flagged, unresolved, author decision pending).
**Settled:** IRH's constants account is its weakest part by its own
ledger: triad relations are definitional re-expressions of measured Planck
quantities; $\alpha$ ansatz is arithmetic-exact but underived; dimensional
assignment (A)/(B)/(C) is undecided, mutually exclusive, "not resolvable
by further calculation." Only Greensite/Carlini–Greensite (quantum,
one-loop, fermion-dominant) and Mukohyama–Uzan/Kehayias et al. (classical,
clock field, Galileon-not-GR gravity) claim a signature derivation.
**Failed / refuted:** F1 Greensite signature transfer into IRH — Bartha
FAIL; F2 Mukohyama–Uzan/Kehayias clock-field signature transfer — Bartha
FAIL; F3 "Einstein equations derived" from any analog-gravity route —
Bartha FAIL; IRH's Part VII retraction stands. F4 "IRH'$s E_{6}$ identification
derives coupling values / $\alpha$" — FAILED (no breaking pattern, no RG
running; §IX.4). F5 "Anthropic reasoning explains $\alpha$ or IRH's tunings" —
FAILED / NOT SUPPORTED (ensemble unobserved; not in the manuscript). F6
Eddington's derivation of $\alpha$ — FAILED by measurement (historical control;
$\alpha^{-1}$ is not an integer).
**Open (ABSTAIN):** U1 current status of varying-$\alpha$ observations / present
best bound on $\dot{\alpha}/\alpha$; U2 current standing of the Greensite mechanism beyond
1993–94; U3 whether any specific NCG coupling/Higgs-mass prediction has
been falsified/confirmed; U4 universal negative "no framework anywhere
derives $\alpha$"; U5 any head-to-head IRH-vs-rival ranking (no shared prediction
exists).

### Task 10 — Check your derivations (IRH v93.1 spacetime & constants)

**Source:** `ws-d-frameworks-rivals/task10_derivations_check.md`
**Question:** Transcribe the spacetime/constants derivations of IRH v93.1
(§§I.1–I.3, II.1–II.9, III.1–III.4, IV.1–IV.3, Part VII) into symbolic
computation (SymPy) and check a second time with an independent tool
(python-flint + numpy) — do the manuscript's derivations reproduce?
**VERDICT: Transcription + two-tool verification COMPLETE. 78 checks pass
(45 SymPy + 33 flint/numpy), 0 fail on re-run** — with two exceptions
(below). Tools: SymPy 1.14.0, python-flint 0.8.0, numpy 2.4.6, Python
3.11.16, conda env `jacobian-conjecture-2d`, exit 0 on both final runs.
(First runs had 3 SymPy FAILs, all script bugs — E2 mis-stated identity;
O2/O4 quaternion product missing /2 — plus a G3-f loop-indentation
assembly fix; earlier "46 + 32" counts corrected to "45 + 33".)
**Grades (Track E, $I1 \to$ cap C; carried grades cited not re-earned):** D1
(Planck triad definitional circle), $D2 (\alpha$ ansatz arithmetic), D3 (Derrick
scaling; d = 4 marginality), D4 (dispersion identity), D6 (CFL bound), D7
(isotropy moments), D8 (selection rationals), D9 (ordered branch), D10
$(\xi_{2}$ retraction factor 2), $D11 (E_{6}$ Cartan det 3, Smith form), D12 (24-cell
= 2T closure), D13 (Weyl orders 192/1920), D14 (resonance maximum 24
unique), D15 (8 partners at $120^\circ$, 192 triads), D16 (shell counts 24/64),
D19 (exact linearity at $\Deltat = a_{0}/c)$ — **all C**. D5 printed dispersion
relation (7) — **C (FAILED as printed)**. D17 envelope validity table —
**UNVERIFIED**. D18 R = 2589 — **ABSTAIN**. Geometric core — **A
(carried)**.

- **D5 — printed dispersion relation (7) WRONG as printed (the new
  finding of this workstream).** EOM-derived formula:
  $\sin^{2}(\omega\Deltat/2) = (\Deltat^{2}\cdot2J/(4M$\*$a_{0}^{2}))\cdot\Sigma_{\alpha}(1-\cos(a_{0}k\cdot\alpha))$ +
  $(\Deltat^{2}\mu^{2})/(4M$\*); printed (7) has $[2\Sigma_{\alpha}(1-\cos(a_{0}k\cdot\alpha)) + \mu^{2}]$ inside one
  bracket — factor of 2 too many in the $\Sigma$ term, $\mu^{2}$ misplaced (multiplied
  by pref instead of $\Deltat^{2}/(4M$\*)). Three internal checks favour the
  derived formula: small-k J = M\*$c^{2}/12 ($the manuscript's own value) vs
  M\*$c^{2}/24$ from the printed formula; k = 0 gives $\sin^{2}(\theta/2)$ =
  $\Deltat^{2}\mu^{2}/(4M$\*) as §III.3 states; the CFL table matches the derived
  formula. The manuscript's own §III.2 expansion ("at the worst case the
  bracket equals 32") uses the derived formula, contradicting printed
  (7). **Erratum to one printed equation** (replace $[2\Sigma(1-\cos) + \mu^{2}]$ by
  $[\Sigma(1-\cos)]$ with the $\mu^{2}$ term outside the bracket at coefficient
  $\Deltat^{2}/(4M$\*)); not a refutation of the bound.
- **CFL bound — CORRECT (VERIFIED$):** \Deltat \leq (\sqrt{3}/2)a_{0}/c \approx 0.866a_{0}/c$;
  worst-case $\Sigma(1-\cos) = 32$ exactly, at (0,0,$\pi,\pi)$-type points, confirmed
  by $a 48^{4}$ Brillouin-zone scan (grid max 32.000000 at $a_{0}k = (0,\pi,\pi,0))$;
  $a_{0}/c$ exceeds $\Deltat_{max}$ by $2/\sqrt{3} = 1.1547 (~15$%).
- **D17 — envelope validity table UNVERIFIED:** table $(4\times10^{-5}, 0.1$%, 1.0%,
  11%, 133%) NOT REPRODUCIBLE; under the natural reading computed errors
  are $1.67\times10^{-5}$, $4.17\times10^{-4}$, $3.75\times10^{-3}$, 4.11%, 36.3% $(\Deltat\to0)$ — smaller by
  factors 2.4–3.7; zone-edge 133% unreachable under that reading (would
  require $\omega_{exact} \approx 2.33\cdotc$|k| / $\sin^{2} > 1)$. The VI.3 summary claim "<1%
  for $a_{0}$|k| ≲ 0.3" still holds under recomputed values (0.042% at 0.10,
  0.375% at 0.30) — the boundary survives; the table's exact entries do
  not reproduce.
- **D18 — R = 2589 ABSTAIN** (no derivation inputs in the source;
  manuscript itself already downgrades it).
- **$\alpha$ ansatz:** 137.03600282194111918739454715858134949265661452923;
  ansatz $-$ CODATA 2022 (137.035999177$(21)) = 3.645\times10^{-6} (~174\sigma$; rel
  $2.660\times10^{-8}$; flint.arb $3.6449411\times10^{-6})$.
- **$\xi_{2}$ retraction:** stated substitution yields $-1/768$, not $-1/384$ —
  factor 2 confirmed.
- **Selection rationals:** $D_{4} \tau^{2} = 8/3$, $q_{4} = 47/8$, S = 64/141; $A_{4}$*
  $\tau^{2} = 9/5$, $q_{4} = 93/20$, S = 12/31; ratio 496/423, margin $73/423 \approx$
  17.26%; BCC $\tau^{2} = 4/3$, $q_{4} = 15/4$, S = 16/45; $\tau_{D}_{4}/\tau_{BCC} = \sqrt{2}$; FCC
  $q_{4} = 27/8$, SC $q_{4} = 5/2$.
- **Ordered branch:** A\* = 0.0775753, $F = -0.0076323$, uniform baseline
  $-0.0034636$, $r_{eff} = +0.1072$ at $\bar{\psi} = -0.18$; detuned $(r_{shell} = -0.10)$
  discriminant < $0 (-28614.7584)$, no branch.
- **24-cell/2T:** 24 vertices, all 576 products in the set, $Q_{8}$ has 8
  elements and is normal, $2T/Q_{8}$ has 3 cosets of 8; $E_{6}$ Cartan det 3,
  Smith diag(1,1,1,1,1,3); |$W(D_{4})$| = 192, |$W(D_{5})$| = 1920.
- **Resonance:** $\Psi = 24.0 / -8.0 / -8.0$; maximum 24 unique (second-highest
  23.8110, 0.79% below); $16^{4}$ grid maxima = 32; every root has exactly 8
  partners at $120^\circ ($dot $-1)$; $24\times8 = 192$ ordered triads; shell counts 24
  $(D_{4}$ scaled) / 64 (competitor |k|${}^{2} = 7)$; penalties 0.25/0.25; ratio
  64/24 = 2.667.
- **Side finding (D19, VERIFIED, C):** at $\Deltat = a_{0}/c$ the discrete
  dispersion is exactly linear $(\omega = c$|k|) along axis and body-diagonal
  directions (S$(k) = 24\sin^{2}(a_{0}$|k|/2) exactly; numeric errors ~$10^{-13})$. Not
  a manuscript claim; does not rescue the §III.3 table.
**Settled:** the manuscript's arithmetic reproduces as stated for
D1–D4, D6–D16, D19 (two-tool agreement); the CFL bound is correct; the J
value M\*$c^{2}/12$ is correct; the §III.3 rest-mass absorption follows from
the EOM-derived formula.
**Failed (as printed):** D5 printed dispersion relation (7).
**Open:** D17 envelope table (UNVERIFIED — what would settle it: the
author stating $\Deltat$, carrier $\theta ($or $\mu)$, direction, error definition); D18
R = 2589 (ABSTAIN). No Lean formalization attempted (S7 NOT RUN).

### Task 12 — Formalize rival accounts

**Source:** `ws-d-frameworks-rivals/task12_rival_accounts.md`
**Question:** Formalise five rival accounts of spacetime and of the origins
of dimensionless constants as executable SymPy/numerical models and run
them under shared conditions against IRH v93.1 as reference — where do they
diverge from IRH (divergence points D1–D6)?
**VERDICT: PARTIALLY VERIFIED. All 55 executed checks PASS** (driver
`task12_models/compare_driver.py`, exit 0, 0 FAIL; independently re-run in
assembly, check lines identical to saved `driver_output.txt`). The *formal*
parts (selection algebra, toy sign-flip, drift arithmetic,
prior-dependence arithmetic, CDT-fit evaluation) are verified as
computations. The *physical* claims the rivals make are graded C or D, or
ABSTAINED where the primary source could not be recovered. Nothing upgrades
any IRH grade; no EXCLUDED claim is revived.
**Grades (per narrow claim, worst-of shown):** G1 IRH selection algebra
(B\*, $r_{c}, S = 64/141$, ratio 496/423) — **Track F, F3** (two tools $\to F2$,
capped at F3; human gates not run). G5 Greensite toy: Lorentzian favoured
iff $n_{F} > n_{B} ($toy sign-flip) — **Track F, F3**. G8 Dirac Ġ/$G = -1/t$
(arithmetic from $G \propto 1/t)$ — **Track F, F3**. G12 CDT $D_{s}$ flows $1.82 \to 4.02$
(2005 fit evaluation) — **Track F, F3**. $G2 D_{4}$ selected in nature
(physical reading of G1), G9 toy $\alpha$ drift excluded by Rosenband 2008, G13
CDT spectral dimension flows in nature (physical), G14 divergence points
D1–D6 — **Track E, C**. $G4 \alpha^{-1} = 137 + 1/(28 - \pi/14)$ as a derived value —
**Track E, D (ansatz only)**. G11 anthropic P(observed $\Lambda)$
prior-independent — **Track E, D (accommodation, not prediction)**. G3
triad relations "derive" c, $\hbar$, G — **No grade — NOT A DERIVATION**
(definitional identities: F3 as identities). G6 full Greensite mechanism,
G10 Dirac varying-G verdict — **No grade (ABSTAIN)**. G7 Greensite
mechanism transfers into IRH — **No grade — TRANSFER FAILS** (Bartha).

- **55 checks:** Model A IRH reference 15 PASS, Model B signature toy 13
  PASS, Model C varying constants 9 PASS, Model D anthropic 9 PASS, Model
  E discrete (CDT) 9 PASS. Tools: Python 3.11.16, SymPy 1.14.0, numpy
  2.4.6, python-flint 0.8.0.
- **Rosenband-2008 exclusion factor:** Rosenband et al. 2008, $\dot{\alpha}/\alpha$ =
  $(-1.6 \pm 2.3)\times10^{-17}$/yr, $1\sigma$ interval $[-3.9, +0.7]\times10^{-17}$/yr, containing
  0 (Science 319, 1808–1812). Toy linear $\alpha$ drift $r = +1\times10^{-15}$/yr
  (round ILLUSTRATIVE rate, not measured) exceeds the envelope edge
  $(3.9\times10^{-17}$/yr) by **~$25.6\times$** and accumulates one Rosenband $\sigma$ in
  ~0.023 yr (~8 days) — EXCLUDED as a present-day linear drift. IRH
  predicts 0 for both drift rates, consistent with Rosenband.
- **Dirac:** $G(t) = G_{0}t_{0}/t$ gives Ġ/$G = -1/t$ exactly; at $t_{0} = 13.8$ Gyr
  (illustrative) Ġ/$G = **-7.25\times10^{-11}$/yr**; G was $2\times$ present at $t_{0}/2$,
  will be ½ at $2t_{0}$. |Dirac Ġ/G| is ~$3\times10^{6}\times$ the Rosenband $\alpha$ scale —
  different observables, not a falsification of Dirac.
- **CDT:** $D_{s}(\sigma) = 4.02 - 119/(54+\sigma)$; $\sigma\to0$ gives $1226/675 \approx 1.816 ($paper
  $1.80 \pm 0.25); \sigma\to\infty$ gives 4.02 (paper $4.02 \pm 0.10)$; values $\sigma=10 \to 2.16$,
  $\sigma=54 \to 2.92$, $\sigma=100 \to 3.25$, $\sigma=500 \to 3.81$, $\sigma=1000 \to 3.91$, $\sigma=10000 \to$
  4.01. IRH holds D = 4 at all scales — largest divergence |$4 - 1.82$| $\approx$
  **2.18** at $\sigma\to0$, agreement only asymptotically.
- **Anthropic:** $P(0.5 \leq y \leq 2)$, $y = \Lambda/\Lambda_{obs}$, observer window $0 < y \leq 100$:
  uniform on [0,1000] $\to **0.0015$**; log-uniform on [0.01,1000] $\to$ ln4/ln$10^{5}$
  $\approx **0.1204$**; uniform on window [0,100] $\to 0.015$. Ratio
  log-uniform/uniform $\approx **80.3\times** (~80\times)$. Window-$10\times$ sensitivity: 0.010
  vs 0.600 — still prior-dominated.
- **Greensite toy (Model $B):** \mathrm{Re} V_{toy}(\theta) = \Delta\cdot\cos \theta$, $\Delta = n_{F} - n_{B}$;
  $\theta = \pi ($Lorentzian) is the minimum iff $\Delta > 0$, $\theta = 0 ($Euclidean) iff
  $\Delta < 0$, $\Delta = 0$ leaves the potential flat. Verified symbolically, by exact
  integer sign rule (flint), and numpy grid minimisation $(\Delta = -5, -1, 0$,
  +1, +5).
- **Divergences D1–D7:** D1 Greensite signature iff $n_{F} > n_{B}$, IRH
  predicts nothing, transfer FAILS Bartha; D2 toy $\alpha$ drift excluded
  ~$25.6\times$, Dirac Ġ/$G = -7.25\times10^{-11}$/yr; D3 Ġ/G no verified primary-source
  bound (ABSTAIN — no verdict on Dirac); D4 CDT flows $1.82\to4.02$ vs IRH
  flat 4 (gap ~2.18; endpoint disputed, ~2 vs ~3/2); D5 anthropic
  accommodates under every prior, typicality swings ~$80\times$; D6 no rival
  here derives $\alpha^{-1}$, neither does IRH; D7 deciding §IX.2 is a prerequisite
  for any signature comparison.
**Settled:** five rival accounts formalised as executable models; 55/55
checks pass under shared conditions; sharpest quantitative divergences
(toy $\alpha$ drift excluded ~$25.6\times$; CDT flow vs IRH flat D = 4, gap ~2.18);
two divergences are IRH's *silence* (no prediction) rather than a
conflicting prediction (Greensite signature D1, anthropic $\Lambda D5)$.
**Failed / refuted:** G7 Greensite$\to$IRH transfer — Bartha FAIL (critical
feature — quantum-field fermion/boson DOF balance — has no counterpart in
IRH's single classical scalar substrate). G3 triad relations as
derivations — not a derivation. G11 as a *prediction* — FAILED as
prediction; retained only as an accommodation, grade D. The v92 signature
and Einstein derivations — already retracted in the manuscript; not
revived.
**Open (ABSTAIN):** G6 full Greensite one-loop mechanism (exact $V(\theta)$,
D = 4 uniqueness — toy sign-flip only); causal-set spectral-dimension
numbers (no formula verified from a primary source); G10 Dirac verdict —
any primary-source Ġ/G constraint (lunar laser ranging not verified from a
primary source in this run); CDT small-scale endpoint (~2 vs ~3/2 —
Coumbe & Jurkiewicz 2015, literature tension, unresolved); §IX.2
dimensional assignment (UNDECIDED in the manuscript). NOT RUN: Lean
formalisation; recovery of the exact Greensite one-loop determinant.
**The $F3\toF2$ question (open):** the Hark two-route $F3\toF2$ logic was NOT
applied to task-12 G1/G5/G8/G12. The Hark regrade table covers only
WS-A/WS-C/WS-E claims; task 12 is not in it. Task 12's own grading (§7)
already notes the two-tool basis ("2 independent tools $\to F2$; ceiling F3
cap applies (human gates not run$) \to \min(F2, F3) = F3$"). Whether the same
repeal/two-route logic *would* lift them to F2 is **undecided in the files
read** — it would require a decision extending the Hark amendment's scope
to WS-D, which no file makes. **Do not report G1/G5/G8/G12 as F2.**

## 6. Workstream E — cosmology map (tasks 11, 14, 15)

Source directory: `ws-e-cosmology-map/` (reports
`11-bifurcations-report.md`, `14-researcher-map-report.md`,
`15-cosmological-signatures-report.md`). Standing: Tier Standard, Track E
unless noted; independence I1 throughout (re-derivation of stated values
with two independent tools; targets known, so not I2). Human gates (HLRE
§6.5): "not performed — all verification here is artificial (I1); grades
cap at C (Track E) / F3 (Track F) accordingly."

### Task 11 — Simulate cosmological bifurcations

**Source:** `ws-e-cosmology-map/11-bifurcations-report.md`
**Question:** "Simulate how cosmic expansion drives parameter changes and
bifurcation cascades, comparing scenarios and searching for conditions
that produce its predicted phase transitions." (Manuscript target: IRH
v93.1.)
**VERDICT: SPLIT. The bifurcation part is VERIFIED by two independent
tools; the cosmic-expansion part is ABSTAIN.** "FAILED: none — no computed
claim failed its check. The expansion-coupling extraction failed to find
any statement, which is recorded as ABSTAIN (C9), not as a failed
computation."

| Claim | Grade |
|---|---|
| C1 Fiducial A\*, F\* reproduce manuscript values | C (computation $F2 \to **F2$** after Hark regrade) |
| C2 Homogeneous barrier 3.8585e-05 at fiducial point | C (computation $F2 \to **F2**)$ |
| C3 Spinodal/coexistence curves; detuning thresholds 7.5976 / 7.6367 | C (computation $F2 \to **F2**)$ |
| C4 Coexistence edges at $r = -0.35$ are $[-0.238, +0.905]$ | C (computation F2 claimed $\to **F2$** after Hark regrade; see F3 below) |
| C5 Manuscript band edges are sub-pattern edges, not coexistence edges | C |
| C6 Barrier vanishes at $\bar{\psi} \approx -0.144 (r_{eff} = 0)$ | C (computation $F2 \to **F2**)$ |
| C7 11.85% band fraction | **INCOMPLETE-EVIDENCE (no grade)** |
| $C8 w_{6}$ narrowing 11.90% $\to 8.47$% | **INCOMPLETE-EVIDENCE (no grade)** |
| C9 Cosmic expansion drives (r, $\bar{\psi}, q_{0})$ | **ABSTAIN (no grade)** |
| C10 What fixes $\bar{\psi}$ / what supplies nucleation (IX.5) | **ABSTAIN (no grade)** |

- **Key numbers (exactly as reported):** N = 24, T = 192, Q = 3384,
  u = v = 1, fiducial $r = -0.35$, $\bar{\psi} = -0.18$. Selection constants:
  $\tau = 192/24^{3/2} = 4/\sqrt{6}$; $q_{4} = 3384/576 = 47/8$; **$S = \tau^{2}/q_{4} = 64/141$
  $\approx 0.4539$**. Fiducial point: A* = **0.07757530** (manuscript 0.0775753),
  F($A*) = **-0.00763227** ($manuscript $-0.0076323)$. Flint arb: A* =
  $[0.077575296339281 \pm 3.33e-16]$, F$(A*) = [-0.007632267318990 \pm$
  6.24e-16]. Homogeneous barrier (new derived number, not in manuscript):
  $A_{max} = **0.00980059$**, $F(A_{max}) = **3.8585\times10^{-5}** ($exact
  3.858520750506e-05). $r_{eff} = **+0.107$** at $\bar{\psi} = -0.18, **-0.120$** at
  $\bar{\psi} = -0.10$, **$-0.350$** at $\bar{\psi} = 0$. At $\bar{\psi} = -0.18$: $r_{c}$,eff = **0.239216**,
  $r_{spin}$,eff = **0.269118**; ordering $0 < r_{eff} < r_{c} < r_{spin}$ confirms
  first-order character. **Bifurcation interval / band edges:** at fixed
  $r = -0.35$, solving $r_{eff}(\bar{\psi}) = r_{c}$,eff$(\bar{\psi})$ gives $\bar{\psi} \in **[-0.23816$,
  +0.90483]**; solving $r_{eff} = r_{spin}$ gives **$[-0.25432$, +0.92099]**.
  **These are NOT the manuscript's band edges $(-0.33, +0.03)$** — scope
  distinction, not contradiction. Detuning thresholds (refining the
  manuscript table, which gives only $q_{0}^{2} = 7.5$ no branch and 8.0 branch
  exists): ordered branch exists for $q_{0}^{2} \in **(7.5976$, 8.4024)** and is
  the global minimum for $q_{0}^{2} \in **(7.6367, 8.3633)$** at (r, $\bar{\psi})$ =
  $(-0.35, -0.18)$. Barrier vanishes at $r_{eff} = 0$, i.e. $\bar{\psi} = (2 - \sqrt{8.2})/6$
  $\approx **-0.1439$**. §II.8 ansatz gap **1.25%** (0.0000953/0.0077276); SymPy
  exact **1.233%**. Tools: SymPy 1.14.0, python-flint 0.8.0, numpy 2.4.6
  + matplotlib 3.11.2, Python 3.11.16; scripts
  `data/bifurcation_compute.py`, `data/bifurcation_flint_check.py`,
  `data/make_figures.py`, all exit 0.
- **Hark F3 (VERIFIED by the reviewer by own run):**
  `bifurcation_flint_check.py` prints `coexistence band edges (flint):
  []` because `fmpq_poly.roots()` returns rational roots only and the
  edges are irrational. The Task 11 C4 row ("SymPy + flint arb, exit 0",
  "exact, two tools") therefore "had only one tool behind the band edges
  until this audit." **Values stand:** Hark re-did the edges with arb
  $([-0.238164846446380 \pm 3.4e-16], [0.90483151311305 \pm 4.1e-15])$;
  reviewer confirmed independently with a SymPy solve (coeffs ascending
  $c0=-11443/25380$, $c1=-590/423$, c2=295/141) giving
  $[-0.238164846446379897, 0.904831513113046563]$, agreeing with Hark's arb
  values to <1e-12. **Regrade: $C4 \to F2** ($SymPy + Hark arb; package flint
  leg was vacuous, F3). Also recorded: the script prints `$F(A_{max})$ =
  $[3.858520750506e-5 \pm 6.50e-18]$ contains 0.0000386: False` — a rounding
  artefact (0.0000386 = 3.86e-05 is outside the tight arb interval around
  the exact 3.858520750506e-05), not an error.
**Settled:** the stated Landau functional's bifurcation structure —
ordered branch, spinodal, coexistence, first-order character, detuning
thresholds, homogeneous barrier — recomputed exactly and agreeing with
every checkable manuscript number (C1–C6). The manuscript's band edges
are **sub-pattern-competition edges, not coexistence edges**: the
$D_{4}$-vs-disordered region is wider $([-0.238, +0.905]$ vs $[-0.33, +0.03])$;
the manuscript's band is set by sub-pattern competition (6-mode
hexagonal etc.), whose free energies are not stated in the text. Fig. 4
scenario trajectories are **HYPOTHETICAL** paths through the stated
parameter space, not manuscript predictions.
**Failed / refuted:** **Expansion-coupling extraction FAILED to find any
statement $\to$ ABSTAIN (C9):** "The manuscript states no coupling between
cosmic expansion and any model parameter. There is no scale factor, no
Hubble parameter, no Friedmann equation, no expansion-driven parameter
law anywhere in the text (grep-verified over the full 1,638-line source
rebuild)." No computed claim failed its check. The IX1 brief'$s \bar{\psi} \approx -0.10$
barrier-vanishing expectation was corrected to $\bar{\psi} \approx -0.144 (a$ minor
correction to a repo working document, not to the manuscript).
**Open:** **C7 — 11.85% band fraction: NOT RUN / INCOMPLETE-EVIDENCE**
("scan definition + sub-pattern data absent"; "no scan code in
`verification/`; the scan is referenced only in the text"). **C8 — $w_{6}$
narrowing 11.90% $\to 8.47$% at $w_{6} = 0.2$: NOT RUN / INCOMPLETE-EVIDENCE**
("the functional form of the $w_{6}$ term is not stated in the text"; neither
the 8.47% nor the joint (detuning $\times w_{6})$ map (repo problem IX.1.3,
explicitly open) can be recomputed; H = 911,040 stated, not re-derived).
**C9/C10 — ABSTAIN.** **Open question for Brandon — 11.85% vs 11.90%:**
"Known inconsistency (not mine to resolve): the band is stated as both
**11.85%** (headline PREDICTION, §II.7) and **11.90%** $(w_{6} = 0$ value,
§II.7 sixth-order paragraph; Appendix A item 8 calls 11.9% 'the correct'
value). The source rebuild notes flag this as genuine. **Brandon's call,
unresolved.**" Evidence that would change the answer: a stated
expansion$\to$parameter coupling; the band-scan code with sub-pattern free
energies; a stated $w_{6}$ term form; a full-field (beyond one-mode)
bifurcation computation (would shift curves by ~1%; costed in the report
§8, not run; blocked on missing inputs, not compute; no GCP spend
proposed).

### Task 14 — Map of quantum-gravity researchers, Asymptotic Safety, and IRH

**Source:** `ws-e-cosmology-map/14-researcher-map-report.md`
**Question:** Map quantum-gravity researchers, Asymptotic Safety, and IRH:
on three fixed structural criteria — (1) substrate ontology, (2) selection
mechanism, (3) testable predictions — which retrieved approaches are close
to IRH, and where does IRH sit in the field? Comparison target fixed: IRH
v93.1 (McCrary, Zenodo DOI 10.5281/zenodo.22821689, 18 Sep 2026).
**VERDICT: MAP COMPLETE. Synthesis of 73 retrieved papers (3 slices, 63
queries, §2). Every affinity verdict passed or failed through the Bartha
critical-disanalogy gate (§4).** Central claim: "On the three stated
structural criteria, **no retrieved approach is close to IRH on all three
at once**." IRH is alone in the (substrate 2, selection 2) corner of the
scorecard — "a structural fact about the retrieved literature, not
evidence for IRH."
**Grades: Overall C (Track E), I1, F2.** "Grade ceiling applies: **Track E
C / I1** for the whole map (cross-domain-discovery skill cap, until a human
runs the source/balance gates; independence is I1 — one retrieval
pipeline, shared by the three slices and this synthesis). No claim in this
report is graded above C." 8-check self-evaluation: **7/8 pass;
independence is the binding limit $\to$ grade C (Track E, I1).** No Hark
regrade of Task 14 claims is given. Per-claim grades (§9):

| ID | Claim | Grade |
|---|---|---|
| M1 | The 73 retrieved papers exist as stated | C / I1 / F2 |
| M2 | Scorecard scores (Table 1) | C / I1 / F1 |
| M3 | GFT condensate cosmology closest to IRH on substrate ontology | C / I1 / F1 |
| M4 | AM/LP lineage closest to IRH on selection mechanism | C / I1 / F1 |
| M5 | AS furthest from IRH on ontology and strongest on stated quantitative predictions | C / I1 / F1 |
| M6 | No retrieved approach close on both ontology and mechanism jointly | C / I1 / F1 |
| M7 | OpenAlex volume counts (§2) | C / I1 / F2 |
| M8 | No independent work citing/discussing IRH was found | **INCOMPLETE-EVIDENCE** / I1 / F1 |
| M9 | No findable Wise Journal revision record | **INCOMPLETE-EVIDENCE** / I1 / F1 |
| M10 | IRH's selection principle changed SSRN $\to v93.1$ | C / I1 / F1 |
| M11 | Klein (2001) argues AM's BCC solutions are unstable — caveat on IRH's 3D validation | C / I1 / F1 |
| M12 | Field-direction statements (§6) | C / I1 / F1 |

- **Paper count: 73 total** — Slice A (Asymptotic Safety): 22 (+4
  contested/counterpoint), 16 queries; Slice B (emergent/discrete/
  analogue): 25, 19 queries; Slice C (pattern formation + IRH): 26
  entries, 28 queries. **Total queries: 63.** Newest item retrieved June
  2026 (Eichhorn 2026 review, arXiv:2606.21522; Koch et al. 2026,
  arXiv:2606.22408).
- **OpenAlex volume proxy** (text-search hits, 2023-01-01 onward, HTTP
  200, exit 0): asymptotic safety quantum gravity **1,758**; loop quantum
  gravity **28,665**; causal dynamical triangulations **22,759**; group
  field theory quantum gravity **35,600**; emergent gravity Verlinde
  **1,918**; analogue gravity **27,786**; causal set theory quantum
  gravity **11,485**; string theory swampland **2,488**. **Caveat
  (load-bearing):** "these are **broad text-search matches, NOT a curated
  field census**$\dots$ Do not cite these numbers as field sizes."
- **Scorecard (Table 1, 0/1/2, judgements not measurements):** IRH v93.1
  **(2, 2, 1)** — alone at (2,2); GFT (2,1,1); Wolfram (2,1,0); Volovik
  (2,0,1); Verlinde (1,0,2); Analogue gravity (1\*,0,1); Causal sets
  (0,1,1); CDT (0,1,0); String/swampland (0,1,1); Asymptotic Safety
  **(0,1,2)**; LQG (0,0,0); Kibble–Zurek (0,0,1); AM/Lifshitz–Petrich
  **(0,2,2)**.
- **Closest per criterion:** substrate ontology — **GFT condensate
  cosmology** (Oriti & Pang 2025; Calcinari et al. 2026), runner-up
  Volovik; selection mechanism — **Alexander–McTague / Lifshitz–Petrich
  lineage** (Alexander & McTague 1978; Lifshitz & Petrich 1997;
  Faraday-wave experiments); testable predictions strongest —
  **Asymptotic Safety** (Higgs mass $\approx 126$ GeV pre-discovery,
  Shaposhnikov–Wetterich 2010; seesaw-scale bound ~$10^{14}$ GeV and
  Weinberg-operator exclusion, de Brito et al. 2025; proton-decay
  suppression, Eichhorn & Ray 2024), simultaneously furthest from IRH on
  substrate ontology.
- **Klein 2001 caveat (F1):** Klein (arXiv:cond-mat/0104342, 2001) argues
  AM's BCC solutions are *unstable* — "the cubic term that selects BCC
  also destabilises it, and the stable 3D solution may be different."
  IRH v93.1 §V validates its selection principle in 3D by recovering BCC
  (the AM result).
- **Selection-principle change (F2):** same-author SSRN predecessor
  selected by *maximal cymatic complexity* and obtained **dimension 8**;
  v93.1 selects by **$S = \tau^{2}/q_{4}$** and obtains **$D_{4}$**. "The selection
  principle is therefore **version-dependent**."
- IRH's own predictions as characterised: "weakest cosmologically (no
  GW/CMB prediction stated; VI.1–VI.7 predictions are quantitative but
  untested and partly conditional)"; three generations are INPUT, not
  derived; does NOT recover Einstein's field equations (effective metric
  only).
**Settled (grade C, I1):** M1–M7, M10–M12 — papers exist; scorecard as
judgements; GFT closest on ontology (Gate 1 passes ontology, mechanism
fails); AM/LP closest on selection (Gate 2 passes mechanism, ontology
fails — "the only gate in this report that passes at the mechanism
level"); AS furthest on ontology / strongest on predictions (Gate 3); no
retrieved approach close on both ontology and mechanism (M6); OpenAlex
counts as tool outputs with census caveat; selection-principle change
SSRN $\to v93.1 (M10)$; Klein caveat (M11); field directions (M12).
Protocol record: S1–S4 DONE; S5 blending NOT RUN by design (gated
affinities partial and mutually incompatible); S6 tournament NOT RUN (no
candidates to evolve); S7 formal verification NOT RUN (claims
comparative/historical, not formal).
**Failed affinity claims (Bartha gates):** AS $\leftrightarrow$ IRH selection affinity
beyond the abstract noun "dynamical selection" (Gate 3). CDT $\leftrightarrow$ IRH
mechanism and ontology (Gate 4). Volovik $\leftrightarrow$ IRH mechanism (Gate 5).
Wolfram $\leftrightarrow$ IRH mechanism (Gate 6); Verlinde $\leftrightarrow$ IRH any structural affinity
(Gate 7 — label only); Analogue gravity $\leftrightarrow$ IRH ontology as a claim about
our universe (Gate 8 — wrong referent); Causal sets $\leftrightarrow$ IRH substrate and
selection (Gate 9); LQG $\leftrightarrow$ IRH any structural affinity (Gate 10);
String/swampland $\leftrightarrow$ IRH any structural affinity (Gate 11 — exclusion $\neq$
selection); PFC/Swift–Hohenberg $\leftrightarrow$ IRH ontology (Gate 12 —
mechanism-family only); GFT $\leftrightarrow$ IRH mechanism (Gate 1 — ontology passes,
mechanism fails). "No approach passes on both ontology and mechanism —
IRH occupies the (2,2) corner alone."
**Open:** **M8, M9 — INCOMPLETE-EVIDENCE (search-bounded absence, not a
claim none exists):** no independent work citing/discussing IRH found; no
findable Wise Journal revision record. "A different query set could find
something." **Open questions for Brandon (findings F1/F2, §7 "Action for
the programme"):** **Klein caveat:** "the 3D validation claim should carry
the Klein caveat in any future revision; a stability analysis of the IRH
$4D D_{4}$ solution is the direct analogue of the missing check." F1 "does
**not** touch the structural affinity (Gate $2\dots)$, but it does bear on the
*evidence* for IRH's mechanism: the manuscript's 3D check should be read
as 'recovers the AM prediction', not 'recovers an established fact'."
Grade C. **Selection-principle change acknowledgement:** "the SSRN$\tov93.1$
change should be acknowledged in the manuscript's history (it currently is
not, as far as the retrieved record shows); the reason for abandoning
maximal cymatic complexity is a question for the author." Grade C.
Other open/bounded items: retrieval bounded by 63 queries / 73 papers —
"an approach not retrieved is not scored"; most likely miss is a small
emergence programme at (2,2); contestable scores (Verlinde substrate 1 vs
0; causal sets selection 1 vs 0) do not change M3/M4/M6; GFT substrate
ambiguity (quanta *of* geometry vs substrate *under* geometry) could drop
GFT to 1 and make Volovik the ontology leader — reason M3 is grade C, not
higher. Evidence that would change the answer: a retrieved (2,2) approach
other than IRH (overturns M6); a GFT paper stating a pattern-selection
mechanism; resolution of the Branchina–Held dispute against the fixed
point (weakens M5's predictions half); independent work engaging IRH
(changes M8); a stability proof for the IRH $D_{4}$ solution (retires F1's
analogue) or demonstration AM's BCC is stable (retires F1).
**Torus-node follow-up (comparison report §7.3, not in task 14's map):**
the torus-node paper (Lee, 2026-11-06, 190 pp.) is the first $D_{4}$-based
emergent-spacetime rival not retrieved by task 14; recording it as a
task-8 ledger entry is Brandon's call (grade $\leq C)$. See §7 below.

### Task 15 — Cosmological signatures: gravitational-wave and CMB forward model

**Source:** `ws-e-cosmology-map/15-cosmological-signatures-report.md`
**Question:** "Forward-model the gravitational-wave signatures and cosmic
microwave background power-spectrum modifications predicted by the IRH
framework" — presupposing a stated model.
**VERDICT: EXTRACTION COMPLETE; FORWARD MODEL ABSTAINED. "The ABSTAIN is
not a failure of effort: the forward model has no input. Any number
produced here for a GW spectrum or a CMB power spectrum would be invented,
not derived."** S1–S10: **VERIFIED**, grade **C**. UNVERIFIED: none.
FAILED: the task's presupposition (see below); any phase-transition GW
estimate from the Task 11 barrier numbers as a derivation.
**Grades: Overall C (Track E), I1, F2.** "The ABSTAIN is the report's
central result and is not a grade — it is the correct output for a task
whose input does not exist." Independence I1 throughout (one pipeline).
Computation F2 where a tool output is quoted (grep counts,
browser.search), F1 where the claim is a judgement on the manuscript. No
Hark regrade of Task 15 claims; the audit §3 accepts "WS-E ABSTAIN
correct" in its settled list.

| ID | Claim | Grade |
|---|---|---|
| S1 | Manuscript states zero GW predictions ("gravitational wave" = 0) | C / I1 / F2 |
| S2 | Manuscript states zero CMB predictions ("CMB"/"cosmic microwave" = 0) | C / I1 / F2 |
| S3 | No photon or baryon coupling stated ("photon" = 0, "baryon" = 0) | C / I1 / F2 |
| S4 | No expansion history stated ("Hubble"/"Friedmann"/"scale factor" = 0) | C / I1 / F2 |
| S5 | VI.1–VI.7 contain no GW/CMB prediction | C / I1 / F2 |
| S6 | Every observable in the grid is UNSTATED / ABSTAIN for IRH | C / I1 / F1 |
| S7 | Instrument sensitivities as quoted (§3) | C / I1 / F2 |
| S8 | Blockers B1–B6, each gated to a manuscript passage | C / I1 / F1 |
| S9 | Requirements list (§5) for a future forward model | C / I1 / F1 |
| S10 | No GW number can be derived from the stated model (phase-transition parameters T\*, $\alpha, \beta/H, v_{w}$ all unstated) | C / I1 / F1 |

- **Extraction greps** (`grep -c` on `IRH_v93_1_source_rebuilt.txt`,
  1,638 lines, exit 0): "gravitational wave" **0**; "CMB" / "cosmic
  microwave" **0**; "photon" **0**; "baryon" **0**; "graviton" **1** (line
  1383 only); "tensor" **1** (line 1376 only); "Hubble" / "Friedmann" /
  "scale factor" **0**. Controls: "monopole" **12**; "inflation" **1**
  (§V.3 only); "D4" / "$D_{4}$" **83** — "the zeros are real, not a grep
  failure." Second independent check: predictions file VI.1–VI.7 headings
  re-grepped; none is GW/CMB.
- **Null observable grid — every IRH prediction column reads UNSTATED /
  ABSTAIN** (G1–G4, C1–C5). Instrument responses (verified; LVK and BK18
  re-verified by fresh searches in the session): G1 LVK O1–$O4a: \Omega_{GW}(25$
  Hz$) \leq **2.8\times10^{-9}** (\alpha = 0), \leq **2.0\times10^{-9}** (\alpha = 2/3), 95$% CL (PRX 16,
  041023, 2026, DOI 10.1103/dlfv-z6m2). O1–O4c1 improves $\times1.3$–1.5. G2
  LISA: $h^{2}\Omega_{sens} ~**10^{-12}$** at $10^{-2}$ Hz, ~**$10^{-13}$** at $10^{-8}$ Hz; launch
  mid-2030s; $\Omega_{gw}$ as low as **$6\times10^{-13}$** detectable in one month. G3
  NANOGrav 15-yr: $A_{GWB} = **2.4^{+0}\cdot^{7}_{-0}\cdot_{6}\times10^{-15}$** at f = 1/yr,
  Hellings–Downs correlation, Bayes factor **>$10^{14}** ($ApJL 2023,
  arXiv:2306.16213). A background is *detected* in this band
  (astrophysical origin favoured). C1 Planck $2018: n_{s} = **0.9649 \pm$
  0.0042** (A&A 641, A10, 2020). C2 r: Planck alone $r_{0}$.002 < **0.10**;
  +BK15 < **0.056**; BICEP/Keck BK$18 r_{0}$.05 < **0.036**, $\sigma(r) = 0.009$,
  95% CL (PRL 127, 151301, 2021); newer combination (Planck PR4 + BK18):
  r < **0.032**. C3 CMB-S4 design $\sigma(r) < **5\times10^{-4}$**. C5 monopole relic
  density: UNSTATED (named, not derived) — ABSTAIN; Preskill 1979,
  Turner 1984, Guth 1981 cited as the standard background.
- What the manuscript DOES predict (VI.1–VI.7, laboratory/pattern scales,
  none cosmological): VI.1 triad phase locking; VI.2 baseline-tension
  band (**11.85%** scan fraction — "see task 11, INCOMPLETE-EVIDENCE on
  reproducibility"); VI.3 non-relativistic validity boundary; VI.4
  stability bound; VI.5 isotropy to fourth order (prediction of absence);
  VI.6 defect spectrum (dislocations yes; monopoles, skyrmions, hopfions
  no — line 924); VI.7 monopoles — predicted, not excluded.
- Only cosmology-adjacent statements (all named, none derived): §V.3
  lines 1086–1090 (monopole problem "requires the standard resolution:
  inflationary dilution, or a breaking pattern avoiding the relevant
  topology"); §II.9 line 641 ("Any cosmological account within this
  framework must supply a nucleation mechanism"); §IX.5 lines 1406–1410
  (no mechanism sets $\bar{\psi}$; no nucleation event supplied).
**Settled (grade C, I1):** S1–S10 — zero GW predictions; zero CMB
predictions; no photon/baryon coupling; no expansion history; VI.1–VI.7
contain no GW/CMB prediction; every grid observable UNSTATED/ABSTAIN;
instrument sensitivities as quoted; blockers B1–B6 gated to manuscript
passages; requirements list (§5); no GW number derivable from the stated
model.
**Blockers B1–B6** (all must be resolved before a GW or CMB number can be
derived): B1 no expansion history; B2 dimensional assignment undecided
(§IX.2 options A/B/C); B3 Einstein equations not recovered / tensor
sector unrecovered — effective metric "obeys the substrate's own equation
of motion, not $G\mu\nu = 8\piT\mu\nu$" (§IX.3, lines 1376–1380), "the two
transverse-traceless graviton polarizations is a separate and
substantially harder [problem]" (line 1383); B4 no nucleation mechanism,
no $\bar{\psi}$ mechanism (§IX.5); B5 no photon or baryon coupling; B6 no stated
cosmological initial conditions $(\bar{\psi}$ "an initial datum"; whether occupying
the $D_{4}$ band is a prediction or a tuning "remains undetermined"). "The gap
is specific and total: **the manuscript predicts patterns, not
cosmologies.**"
**Failed / refuted:** **The task's presupposition FAILED on extraction:**
"The task's presupposition that IRH states GW signatures and CMB
power-spectrum modifications to forward-model — **FAILED on extraction**:
the terms occur 0 times and VI.1–VI.7 contain no such prediction. The
forward model is therefore ABSTAINED, not merely unattempted."
**Any phase-transition GW estimate from the Task 11 barrier numbers
FAILED as a derivation:** "the barrier is substrate energetics at fixed
(r, $\bar{\psi})$, not (T\*, $\alpha, \beta/H)$; the conversion needs the missing cosmology
(B1, B4)." Task 11 numbers cited: barrier $3.8585\times10^{-5}$ at $A_{max}$ =
0.00980059, homogeneous; coexistence edges — "they are not $\alpha$, $\beta$, or T\*."
**Open — forward model: ABSTAINED, not run.** "Forward model (GW spectrum
/ CMB power spectrum): **NOT RUN — ABSTAIN.** No stated prediction exists
to forward-model; computing one would require inventing a cosmology."
**Future forward model — requirements list (§5), in order** (the open work
for Brandon / a future version): 1. An expansion history — scale factor
a(t) or Hubble H(t), or what plays that role (B1). 2. A dimensional
assignment — resolve §IX.2 A/B/C (B2). 3. A tensor sector — recover the two
TT graviton polarizations and state the equation they obey (B3). "Until
then, every GW row stays ABSTAIN." 4. Einstein recovery or a stated
replacement (B3). 5. A nucleation mechanism and rate — what nucleates the
$D_{4}$ phase, at what temperature T\*, with what strength $\alpha$ and duration $\beta/H$
(B4). "These three numbers are the entire input to a first-order
phase-transition GW spectrum." 6. A mechanism fixing $\bar{\psi}$ — or a stated
prior over $\bar{\psi} (B6)$. 7. Photon and baryon couplings (B5). 8. Initial
perturbations — scalar spectrum (amplitude, tilt $n_{s})$ and tensor spectrum
(amplitude, ratio r), or a derivation from substrate dynamics (B6). 9. A
monopole number — dilution factor or breaking pattern, turning §V.3's
named resolution into a relic-density prediction (C5). "Items 3 and 5 are
the binding constraints for GW; items 7 and 8 for CMB. Items 1–2 gate
everything." One partial bridge (§6) that does not reach the grid: the
transition is first order (§II.9) and VI.6 states a defect spectrum, so
"the *shape* of a future IRH GW prediction is visible: it would be a
phase-transition spectrum, not an inflationary one." It does not reach the
grid because a phase-transition spectrum is fixed by (T\*, $\alpha, \beta/H, v_{w})$
and the manuscript supplies none of the four. Evidence that would change
the answer: a manuscript passage stating a GW spectrum, tensor-to-scalar
ratio, scalar tilt, or CMB modification; resolution of any single blocker
B1–B6 in a stated, derived form (not a named intention); a stated
nucleation rate with T\*, $\alpha$, $\beta/H (G4$ becomes computable with a standard
template, and the LVK O1–O4a first-order-phase-transition constraints
would then bite). A newer manuscript version (v94+) would need a fresh
extraction; this report is about v93.1.

## 7. The Hark replication audit and its review

**Audited document:** `D4_package_2026-11-10_replication_audit_4_yq6o.md`
(auditor "Hark (IRH project)", uploaded by Brandon 2026-11-10 22:36 CST).
**Review:** `HARK_REPLICATION_AUDIT_REVIEW.md` — claim-by-claim check of
Hark's audit against (a) the manuscript text, (b) the repo record, (c) the
package itself (`d4-work-2026-11-10.zip` as delivered, plus the workstream
directories). Standard: HLRE v5.1; truth-seeking computation gate.
Reviewer independence: I1 (re-ran the package's own code, wrote own checks
on the package's stepper; did NOT re-run Hark's `hark_checks/`, which are
not in the workspace, and did NOT re-run Hark's full replication table).
**No grade moves above C (Track E) / F2 (Track F, two-route) on the
strength of this review.**

**Amendment / provenance caveat (load-bearing).** The audited document
opens with an amendment dated 2026-11-10 22:33 CST stating Brandon
repealed the HLRE §6.5 human-gate requirement *for this assessment*.
That repeal is recorded in Hark's document, **NOT in the reviewer's own
conversation record with Brandon**; the review assesses the audit on its
terms (Track E unchanged, $I1 \to C$; Track F two-route claims $F3 \to F2)$ and
flags the provenance rather than silently adopting it. Nothing in the
review depends on the repeal for its Track E conclusions: WS-A's A/B
grades fall to C on the independence bound alone.

**Resolution (2026-11-12 14:07 CST).** Brandon stated the repeal himself,
in conversation, in wider scope — "amend the human gate requirement
repealing it from your assesment and all future assesments." The provenance
caveat above is closed. The repeal now applies to this assessment and all
future assessments (amendment note
`HLRE-6-5-HUMAN-GATE-REPEAL-2026-11-12.md`; the v5 document and the
hlre-v5-1 skill are not edited in place). Consequences: WS-D task-12
G1/G5/$G8/G12 \to F2 ($inventory G-C17 closed); the Compare $D_{4}$ exact counts
$\to F2$, I1 (audit amendment note). Track E is unchanged $(I1 \to C)$.

| Hark claim | Review verdict |
|---|---|
| §1 replication table (all rows) | PARTLY VERIFIED — every row re-run or checked reproduces; rows not re-run are NOT independently confirmed |
| F1 hex6/fcc12 "stable attractors" FAILED as written | **VERIFIED — by the reviewer's own run** (5/5 hex6 + 4/4 fcc12 transverse perturbations $\to$ full24 at $\bar{\psi} = -0.18$; control stays hex6) |
| $F1 \bar{\psi} = 0 (24$-mode+noise $\to 6$-mode) and $\bar{\psi} = +0.10 (\to 2$-mode stripe) | REPORTED, NOT RE-RUN (consistent with WS-C numbers; check covered $\bar{\psi} = -0.18$ only) |
| F1 stripe side-result (one run, not graded) | UNVERIFIED (single Hark run; not re-run; plausible, not established) |
| F2 lock metric ill-defined for partial patterns | **VERIFIED** (code reading) |
| F3 flint band-edge leg vacuous | **VERIFIED — by own run** (prints `coexistence band edges (flint): []`; values confirmed by Hark arb + reviewer's SymPy solve) |
| F4 task2d/make_figures provenance gap | **VERIFIED — by own re-run** (task2d T=5 only overwrites CSV; make_figures crashes `IndexError` line 88; shipped T=0.5/1.0 rows match Hark's regeneration) |
| §1 task1 JSON provenance gap (extra fields) | **VERIFIED — by own re-run** (fresh output lacks `n_distinct_positions`/`max_multiplicity`; shipped JSON came from another script revision) |
| §1 task1 "different lattice basis" | NOT REPRODUCED in reviewer's env (basis identical to shipped for all 7 directions, NumPy 2.4.6 vs Hark's 2.5.4 — environment-dependent, no number changes) |
| §1 "29 vs 31 checks" | RESOLVED, not a discrepancy (29 check() call sites; the $r_{eff}$ table loops over 3 rows $\to 31 [$PASS] lines; guide must state both) |
| F5 WS-A grade inflation $(A/B \to C)$ | **VERIFIED** (independence bound $I1 \to C$ caps Track E; WS-A's A/B grades fall regardless of the human-gate amendment) |
| F6 brief "established facts" vs round-1 review | **SUBSTANTIATED, with nuance** (review grades C6/C8 D — see §0.1; brief's "do not re-litigate" label overstates them, but the brief itself demands the qualification travel with the claim) |
| §3 "round-1 review had $\approx [-0.235, -0.14]$ with stripes/A2/A3" | **UNVERIFIED — source not located** (no such band in the 2026-10-30 report, the v5 test report, CORE.md, or the manuscript; may come from a review document Hark holds that is not in this workspace) |
| §4 B1 (§I.2 inconsistent; Model B vs MPFC) | SUBSTANTIATED on manuscript text (§I.2 lines 185–191 state $\partial^{2}_{t}\psi + \gamma\partial_{t}\psi = -\deltaF/\delta\psi, a$ NON-conserved RHS, while §I.3 lines 215–219 derives conserved dynamics as a requirement; the conserved-MPFC form appears in neither manuscript nor package). Citation "REVISION_PLAN 1.1" is **unlocated**: no REVISION_PLAN document exists anywhere in the workspace |
| §$4 R4 (L=\pi$ box cannot hold A4\*; no fair test) | SUBSTANTIATED as a statement about the package (every simulation box is $L=\pi$ hypercubic; no A4\* control simulated; no preregistered competitor set, no $\geq10$ seeds, no commensurate cells). "Step 1.2" citation unlocated (same missing document) |
| §4 common-tangent diagram still fixed-$\bar{\psi}$ | SUBSTANTIATED (package does fixed-$\bar{\psi}$ minimisation everywhere) |
| §4 B2/B3 untouched by design | TRUE (programme scope; no claim made) |
| §6 regrade table | ACCEPTED (with the amendment) — see below |

**The §6 regrade table (accepted entry by entry):**

| Claim | Old | New | Check |
|---|---|---|---|
| All Track E empirical/simulation claims | C | **C** | $I1 \to C$; unchanged |
| WS-A M6 mean 15, min 12, max 18 | $A/B \to F3$ | **F2** | Two routes in the package itself, verified by reading task2_report.md: exact symbolic (Lagrange + AM-GM) + independent numerical optimisation (scipy, 200 random starts) |
| WS-A \|Aut$(D_{4})$\| = $1152 \to$ no icosahedral projection | $B \to F3$ | **F3** | One enumeration route (Gram enumeration); "matches the known order of $W(F_{4})$" is a cross-check, not a re-derivation — F3 stands |
| WS-E Landau values, thresholds, barrier (C1–C3, C6) | C / F2 | **F2** | SymPy exact + python-flint, both run (reviewer re-ran the flint check, rc = 0) |
| WS-E band edges at $r = -0.35 (C4)$ | C / F2 claimed | **F2** | SymPy + Hark arb (package flint leg was vacuous, F3); reviewer's SymPy solve confirms the values to <1e-12 |
| WS-$C C1.4 (a_{0}$, CFL), C2.5 CFL leg | F3 | **F2** | exact_checks uses SymPy + flint + Z3, 31 PASS (reviewer re-ran it) |
| WS-C C2.1 analytic A\*, F/V | F3 | **F2** | Two tools (exact_checks + WS-E bifurcation checks) |
| WS-C C1.2, C2.2, P4; F1 hex6/fcc12 "stable attractor" | FAILED as written | **FAILED as written** | Unaffected by the regrade; F1 adds the WS-A task-5 / WS-C finding 6–7 failures |

Still required by HLRE §7 for any deposit: a disclosure that all
verification is artificial (I1), with the independence level of every
pipeline stated. That disclosure was already in the guide §1; it stands.

**What the review did NOT verify (stated plainly):** Hark's full §1
replication table rows not re-run (WS-A tasks 1–4, WS-C 1a–2d, WS-E
compute/figs, task-5 lock values); Hark'$s \bar{\psi} = 0$ and $\bar{\psi} = +0.10$ transverse
runs; the stripe side-result (one run); Hark's arb band-edge computation
(values confirmed by an independent SymPy solve, not by re-running arb);
the "$[-0.235, -0.14]$ band" and the REVISION_PLAN / B1/R4/R6/Step 1.2
citations (sources not located in the workspace); Klein 2001 and WS-E's
citation corrections (not opened by Hark or by the reviewer).

**Corrections applied to the guide** (per the review; zip rebuilt and
re-verified): (1) "29 checks" $\to$ "29 check statements, 31 [PASS] lines";
(2) WS-A task 5 hex6/fcc$12 \to$ FAILED as written (F1), corrected statement,
grades $B \to C$; (3) WS-C findings 6–$7 \to$ FAILED as written (F1), corrected
statement, grades unchanged (C); (4) WS-E C4 "two tools" basis $\to$ one tool
until the audit, values confirmed, grade F2; (5) WS-C replication:
task$2d \to$ make_figures crashes (F4), T=0.5/1.0 rows depend on an unshipped
run, guide §9 order corrected; (6) lock metric defect noted, fix noted;
(7) WS-A task-1 JSON provenance gap noted; (8) §8 register: F1 FAILED
items, F3 record correction, F4 provenance gap added; (9) §1 grades:
WS-$A A/B \to C$, §6 regrade table applied.

**Offered, not done (Brandon's call):** fix the workstream scripts
themselves — (a) WS-C `make_figures.py` / `task2d_transient.py` (ship the
T=0.5/1.0 rows or regenerate them in-script); (b) `d4model.analyze` lock
over active triads only; (c) WS-A task-1 JSON provenance (re-ship from the
current script or record the revision). Fixing them changes the
workstreams' artifacts, so they were not touched. **Separately (not part
of this audit):** WS-D's deliverables were on disk but not verified or
delivered by the audit — that is recorded here as an open audit-scope gap
(see the gap inventory, G-E9).

## 8. Cross-cutting results (read before citing any single task)

### 8.1 The band discrepancy — three workstreams, one open question

The manuscript's 11.85% band fraction does not survive independent
recomputation in any of the three forms it takes:

| Form | Result |
|---|---|
| WS-A task 3, W1 band, stated windows | 11.60% $(\delta = 0, w_{6} = 0) \to 8.36$% $(w_{6} = 0.2)$; hex-only 12.94% $\to 9.68$%. 11.85% bracketed, not reproduced; window unstated. |
| WS-C task 7, 24-mode global-min band at $r = -0.35$ | $\bar{\psi} \in (-0.235, -0.125)$; manuscript $(-0.33, +0.03)$ is the union over quench depths; +0.03 edge UNVERIFIED. |
| WS-E task 11, scan fraction | 11.85% NOT independently reproducible: no scan code in repo `verification/`, scan definition absent. $w_{6}$ narrowing NOT re-derivable (term form unstated). |
| WS-E task 11, coexistence edges at $r = -0.35$ | $[-0.23816, +0.90483]$, NOT $(-0.33, +0.03)$ — those are sub-pattern-competition edges whose data are not in the text. |

WS-A task 3 and WS-C task 7 agree with each other (the measured slice is
narrower than the quoted union); WS-E task 11 adds that the scan itself
cannot be reproduced from the repo as it stands. **Which value is canonical
(11.85% vs 11.90%) remains Brandon's call** — nothing in this package
resolves it, and the no-note IRH recompile (33 pp., delivered 2026-11-10
separately) no longer flags the inconsistency up front. **Competitor-set
gap (Hark audit F1 side-result):** the WS-C band's competitor set
{24-mode, 6-mode, disordered} omits stripes; a stripe-like state appeared
at $\bar{\psi} = +0.10 ($one Hark run, Fexc $-0.048943$, metastable not global-minimum
— not re-run by the reviewer). The audit's claim that "the round-1 review
had $\approx [-0.235, -0.14]$ with stripes/A2/A3 included" could NOT be verified
— no such band appears in the 2026-10-30 deepest-research report, the v5
test report, the repo CORE.md, or the manuscript.

### 8.2 The Model B Hermitian artifact — found twice, independently

WS-A (droplet runs) and WS-C (attractor runs) independently found the same
defect: the shipped-style Model B update grows an anti-Hermitian roundoff
component $\times1.0142$/step and reaches NaN by ~6000 steps (WS-C: blows up at
t = 27.5). Fix: per-step Hermitian symmetrisation / projection — an exact
no-op in exact arithmetic. Both workstreams' Model B results in this
package use the fixed stepper. **Any future Model B work must use the fixed
stepper; the unfixed update diverges.**

### 8.3 Findings that touch the manuscript itself

- **Klein (2001) caveat (WS-E F1):** the manuscript's 3D validation
  recovers the Alexander–McTague BCC result, but Klein argues AM's BCC
  solutions are unstable. The 3D check should be read as "recovers the AM
  prediction", not "recovers an established fact". Open question for
  Brandon: acknowledge the caveat in the manuscript?
- **Selection-principle change (WS-E F2):** the SSRN predecessor selected
  by maximal cymatic complexity $(\to$ dimension 8); v93.1 selects by
  $S = \tau^{2}/q_{4} (\to D_{4})$. The principle is version-dependent. Open question for
  Brandon: acknowledge the change in the manuscript's history?
- **Minor correction to a repo working document (not the manuscript):**
  the repo IX1 brief's "$\approx -0.10$" for the barrier-vanishing $\bar{\psi}$ is loose;
  the exact value is $\bar{\psi} \approx -0.1439 ($WS-E task 11, WS-A task 4 §II.9).
- **Printed dispersion relation (7) is wrong — manuscript erratum
  (WS-D task 10).** The printed formula doubles the $\Sigma$ term and misplaces
  $\mu^{2}$; the EOM-derived formula is correct on three internal checks plus the
  manuscript's own §III.2 expansion. The CFL bound computed from it is
  VERIFIED. One printed equation needs an erratum; nothing else changes.
  Open question for Brandon: file the erratum?
- **§III.3 envelope validity table does not reproduce (WS-D task 10 —
  UNVERIFIED, not FAILED).** The table'$s \Deltat$, carrier $\theta ($or $\mu)$, direction,
  and error definition are unstated; no natural reading reproduces the
  five entries, and the 133% zone-edge entry is unreachable under the
  natural reading. The VI.3 summary boundary (<1% for $a_{0}$|k| ≲ 0.3)
  survives the recomputation. What would settle it: the author stating the
  conditions used for the table.
- **Manuscript §I.2 is internally inconsistent (Hark B1, substantiated on
  the manuscript text).** §I.2 states $\partial^{2}_{t}\psi + \gamma\partial_{t}\psi = -\deltaF/\delta\psi$ — a damped
  wave equation with a NON-conserved right-hand side — and §I.3 then
  derives that conserved dynamics is a requirement, citing Model B
  $\partial_{t}\psi = \nabla^{2}(\deltaF/\delta\psi)$ preserving the mean to 8.3e-17. The manuscript's own
  §I.2 is therefore internally inconsistent: its stated equation is not
  the conserved dynamics its simulations use. The conserved-MPFC form
  $\partial^{2}_{t}\psi + \gamma\partial_{t}\psi = \nabla^{2}\deltaF/\delta\psi$ appears in NEITHER the manuscript nor the
  package.

### 8.4 What this package does NOT change

No IRH grade moves beyond the failed-as-written claims listed in §9 of the
guide and §7 above — which now include the WS-A task-5 / WS-C finding 6–7
"stable attractor" claims (FAILED as written, Hark audit F1) and the WS-A
$A/B \to C$ regrade (Hark audit §6). The $D_{4}$ selection (S = 64/141), $E_{6}$ via
2T/McKay, SO(8) exclusion, and the INPUT status of the three generations
are untouched. The 11.85%/11.90% question, the Klein caveat, and the
selection-principle change are flagged for Brandon's call, not decided
here. WS-D adds two manuscript-facing items to the register — the printed
(7) erratum and the §III.3 envelope table (UNVERIFIED) — and confirms the
manuscript's own downgrades $(\alpha$ ansatz $174\sigma$ from CODATA; $\xi_{2}$ retraction
factor 2); no IRH grade moves.

## 9. Joint programme — first items and their mapping onto gaps

(The full gap inventory, with owners and what-would-close-each-gap, is
`IRH_GAP_INVENTORY_2026-11-12.md`. This section maps only the live and
candidate Academia items.)

- **RUNNING — "Run a four-dimensional field test of $D_{4}$ formation"
  (Academia Co-scientist, launched 2026-11-12, chat
  `02dfb5cb-5423-47eb-9bbe-d8e3d25b6fdc`).** A small 4D periodic field
  calculation that also permits off-shell modes, from random fields and
  patterned seeds, returning mode-occupancy, harmonic-power and energy
  trajectories. **Gap attacked (inventory G-A5): the truncation gap** —
  whether the $D_{4}$ basin results survive outside the 24-mode truncation.
  It is the headline gap from the (not-locatable) "Compare $D_{4}$ Selection
  Frameworks" gap memo: the gap between *selecting* the $D_{4}$ shell and
  *spontaneously reaching* its full 24-mode pattern. Locally, the
  sharpest form of the gap is: noise quench reaches 24/24 in 0/5 seeds
  (WS-C) and 0/6 noise seeds grow at all (WS-A task 5); the 24-mode is
  the attractor from seeded/basin starts but is never reached from noise
  inside the truncation. The 4D test is the first attempt to see whether
  that changes once off-shell modes are permitted. When it lands, it is
  audited claim-by-claim locally under truth-seeking-frontier /
  cross-domain-discovery / HLRE v5.1; nothing is filed, committed, or
  written into the manuscript.
- **CANDIDATE (not launched) — "Map off-shell instabilities of the full
  $D_{4}$ wave".** Linearizes around the standing wave; leading unstable bands
  on a finite Fourier grid. **Gap attacked (inventory G-A6):** the
  stability of the full $D_{4}$ wave against off-shell perturbations — a
  different method from WS-A task 3 (which maps the band under detuning
  within the truncation). Genuinely new, not a duplicate.
- **CANDIDATE (not launched) — "Calculate matched $D_{4}$ and $A_{4}$* onset
  branches".** Both candidates on the same normalized amplitude /
  shell-penalty footing. **Gap attacked (inventory G-A20):** no $A_{4}$*
  control was ever simulated (Hark R4 — every simulation box is $L=\pi$
  hypercubic; no preregistered competitor set). No $A_{4}$* onset-branch
  computation was found in the local WS-D summary. $A_{4}$* is the
  manuscript's closest analytic rival (S = 12/31 vs $D_{4}$'s 64/141). This
  task would supply the first matched, same-footing comparison.
- **DUPLICATES — never re-launch:** "Chart the $D_{4}$ stability band under
  detuning" (= WS-A task 3, delivered 2026-11-10) and "Derive the first
  directional anisotropy of $D_{4}$ waves" (= WS-A task 2, delivered
  2026-11-10).
- **DRAFTING — "Draft replacement $D_{4}$ selection and evidence passages for
  v93.1".** New as a deliverable type, but the programme rule is
  reports/figures/tables only, no manuscript edits; any draft would be a
  report for Brandon's decision, not a filing.

## Appendix A — Grade key (HLRE v5.1, as used here)

- **Track E (empirical / simulation / comparative / historical):** A–D.
  At I1 (artificial verification, single pipeline) every claim caps at
  **C**. D = the claim as presented rests on the manuscript's own
  premises / a single un-re-derived computation / an accommodation rather
  than a prediction.
- **Track F (formal / deductive):** **F1** = kernel-verified in Lean
  (not claimed by any task here); **F2** = machine-checked by exact
  computation with a second independent tool or route; **F3** =
  machine-checked with a single tool/route, or hand-checked.
- **Independence:** I0 = the claim's own computation, no independence;
  I1 = single tool/pipeline, artificial verification; I2 = second
  independent tool; I3 = second independent tool + independent
  derivation; I4 = independent human replication (not reached here).
- **Verdict words:** VERIFIED (the claim as stated checks out);
  FAILED as written (the claim exactly as registered is false or
  unreproduced — a corrected version may be verified alongside);
  INCOMPLETE-EVIDENCE (the check could not be run for lack of stated
  inputs); NOT RUN (the check was not attempted, reason stated);
  ABSTAIN (verification is impossible with the available tools/inputs,
  reason stated); UNVERIFIED (neither verified nor refuted — e.g. a
  table whose defining conditions are unstated).

## Appendix B — Source file index (every claim above traces to one of these)

- Programme brief: `PROGRAMME_BRIEF.md`
- Guide: `SUMMARY_AND_REPLICATION_GUIDE.md` (§4 WS-A, §5 WS-C, §6 WS-D,
  §7 WS-E, §8 cross-cutting, §9 register, §12 open questions)
- Hark review: `HARK_REPLICATION_AUDIT_REVIEW.md`
- WS-A: `ws-a-core-computations/task1_report.md`,
  `task2_report.md`, `task3_report.md`, `task4_report.md`,
  `task5_report.md`
- WS-B: `ws-b-branch-normal-form/REPORT.md`
- WS-C: `ws-c-substrate-convergence/task1_substrate_selection_models.md`,
  `task2_d4_dynamics_convergence.md`, `CLAIM_REGISTER.md`
- WS-D: `ws-d-frameworks-rivals/task8_qg_frameworks.md`,
  `task9_spacetime_frameworks.md`, `task10_derivations_check.md`,
  `task12_rival_accounts.md`, `ws-d_summary.md`
- WS-E: `ws-e-cosmology-map/11-bifurcations-report.md`,
  `14-researcher-map-report.md`, `15-cosmological-signatures-report.md`
- Manuscript text (as needed for wording): `IRH_v93_1_source_rebuilt.txt`
- Repo record: `~/workspace/research/IRH-Theory-Development-Workspace/OPEN_PROBLEMS.md`
  (all OPEN items; EXCLUDED and DOWNGRADED lists; INPUTS)
- Torus-node comparison §7.3:
  `~/workspace/research/irh/torus-node-comparison/TORUS_NODE_VS_IRH_COMPARISON.md`
- NOT LOCATED: the "Compare $D_{4}$ Selection Frameworks" gap memo (three
  files behind Academia keypass links; no local copy found by filename
  search and full-tree grep, 2026-11-12). Recorded as not located, not
  reconstructed.

---
*Coordinator's note on method.* This summary was assembled by reading the
source files listed in Appendix B and the five workstream extractor
records (WS-A, WS-B read directly by the coordinator; WS-C, WS-D, WS-E
from dedicated extractor subagents whose full records were recovered and
checked against the source reports). No new computation was run, no file
was modified, no repo or manuscript state was changed, no GCP spend was
incurred, nothing was launched in Academia, and nobody was contacted.
