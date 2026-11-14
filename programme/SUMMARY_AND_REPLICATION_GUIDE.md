# D4 Work — Exhaustive Summary and Replication Guide

**Programme:** Academia Co-scientist task programme, launched 2026-11-10 ~17:00 CST
(Brandon's order: do all fifteen undone tasks, under
`/truth-seeking-frontier` `/cross-domain-discovery` `/hlre-v5-1`).
**Package date:** 2026-11-10 evening CST.
**Workstreams in this package:** WS-A (tasks 1–5, core computations),
WS-C (tasks 7 + 13, substrate models + convergence),
WS-D (tasks 8, 9, 10, 12, frameworks + rivals + derivations),
WS-E (tasks 11, 14, 15, cosmology + researcher map).
**Manuscript under test:** IRH v93.1 (Zenodo DOI 10.5281/zenodo.22821689,
18 Sep 2026); the 1,638-line extracted text is `00-programme/IRH_v93_1_source_rebuilt.txt`.

## 0. Scope — what is and is not in this package

**In scope.** Every file produced by the four completed D4 workstreams:
all reports, all computational scripts, all figures, all tables/CSVs/JSONs,
all run logs, the claim register and formalization notes (WS-C), the
literature slices (WS-E task 14), the comparison matrices and divergence
table (WS-D tasks 8, 9, 12), the executable rival models (WS-D task 12),
and the programme brief + manuscript text
(`00-programme/`). Each workstream is in its own directory, exactly as it
was produced; nothing was renamed, moved, or edited for packaging.

**Out of scope, deliberately.**
- **WS-B (task 6, branch (a,b) normal form)** is NOT in this package: it is
  a Jacobian-conjecture cross-check (GGHV (72,108) NewtonNF2), not D4 work.
  It is complete and verified (112 PASS, 0 FAIL) and lives at
  `~/workspace/research/irh/co-scientist-tasks-2026-11-10/ws-b-branch-normal-form/`.
  Say the word and it gets its own package.
- **WS-D (tasks 8, 9, 10, 12 — frameworks, rivals, derivations)** IS in
  this package (added 2026-11-11 ~01:30 CST, after it completed;
  see §6). Its parent-verified scripts were re-run by the parent
  (task 10: 45 + 33 PASS, 0 FAIL; task 12 driver: 55 PASS, 0 FAIL).
- **No repo commits, no manuscript edits, no filing** were made by any of
  these workstreams. Reports, figures, and tables only. The IRH repo and
  the manuscript are untouched by this programme.

## 1. How to read this guide

- Every task section opens with **CLAIM + STATUS** in the words of its own
  report, then the headline numbers, then the HLRE grade table (worst-of),
  then the files, then the exact replication commands.
- **VERIFIED** means: the stated computation was run, the stated tools
  returned exit 0, and the numbers in the report are the numbers the tools
  produced. It is NOT kernel verification (Lean) and it is NOT a grade
  above what the grade table says.
- **FAILED as written** means the claim exactly as registered is false;
  the report states the falsifier and usually the corrected version that
  DOES hold. The failed wording is never silently replaced.
- **INCOMPLETE-EVIDENCE** means the underlying data or definition needed
  to check the claim is absent from the manuscript/repo; no number was
  invented to fill the gap.
- **ABSTAIN** means the task presupposes something the manuscript does not
  state; there is nothing to compute, and no number was produced.
- Grades are HLRE v5.1 (A–D, independence I0–I4, Track E / Track F).
  Track E is the empirical/literature track; Track F is the formal track
  (F1 = kernel-verified in Lean, F2 = symbolic/computer-algebra check,
  F3 = deductive chain verified by exact computation but not kernel-checked).
  No NEW claim in this package is above C (Track E) or F3 (Track F):
  all new verification is artificial (I1 max), and the human
  source/balance gates were not run. The only A grades in this package
  are CARRIED from the repo record (the IRH geometric core — $D_{4}$
  selection, $E_{6}$, isotropy, CFL — cited, not re-earned; see §6). Nothing
  here is F1: F1 belongs to the Lean `main_theorem` /
  `branch_c_eliminated` alone.
- The skills themselves (`truth-seeking-frontier` v5,
  `cross-domain-discovery` v2.0.0, `hlre-v5-1`) are DESIGN CLAIMS,
  ungraded. Skill use is never presented as evidence of reliability.

## 2. Environment — measured, 2026-11-10

All computation ran locally (control-plane machine), no GCP spend,
lean-build-4 untouched, no Gemini grader calls. The interpreter is the
conda environment `jacobian-conjecture-2d`:

| component | version (measured 2026-11-10) |
|---|---|
| Python | 3.11.16 |
| SymPy | 1.14.0 |
| python-flint | 0.8.0 |
| scipy | 1.17.1 |
| NumPy | 2.4.6 |
| matplotlib | 3.11.2 |
| Z3 | 4.15.4 |
| Singular | 4.4.1 (conda-forge; **not needed** by any script in this package — all four workstreams are pure Python) |

Invoke the environment Python as:

```sh
PY=~/miniconda3/envs/jacobian-conjecture-2d/bin/python
```

Do NOT use the system `python3` (it lacks `bs4`, `flint`, `z3`, and the
pinned SymPy). Figures use the matplotlib Agg backend (headless-safe).
Singular, if you ever need it for adjacent work: always close stdin
(`Singular --version < /dev/null` — a bare `Singular --version` hangs
waiting on stdin), never use `continue` inside a Singular for-loop
(4.4.1 hangs; restructure with if/else), and parenthesise explicitly
because `a^b/c` parses as `a^(b/c)`.

## 3. Package layout

```text
d4-work-2026-11-10/
├── SUMMARY_AND_REPLICATION_GUIDE.md   (this file)
├── 00-programme/
│   ├── PROGRAMME_BRIEF.md            (programme rules: skills, grades, compute rules)
│   └── IRH_v93_1_source_rebuilt.txt  (1,638 lines; the manuscript text every check is run against)
├── ws-a-core-computations/           (tasks 1–5)
│   ├── README.md                     (workstream summary + bug list)
│   ├── d4model.py                    (shared 24-mode D4 model + Model B stepper, WITH the Hermitian fix)
│   ├── task1_projections.py  task1_report.md
│   ├── task2_anisotropy.py   task2_report.md
│   ├── task3_band.py         task3_report.md  task3_rerun.log  task3_rerun2.log
│   ├── task4_thinwall.py  task4_droplet_runs.py  task4_report.md  task4d.log
│   ├── task5_basin.py        task5_report.md  task5.log
│   ├── checks/check_model.py  checks/check_model.log
│   ├── figures/  (10 PNGs)
│   └── tables/   (12 files: CSV / JSON / .npy / .npz)
├── ws-c-substrate-convergence/       (tasks 7 + 13)
│   ├── CLAIM_REGISTER.md             (registered claims C1.1–C1.6, C2.1–C2.5, P1–P5)
│   ├── formalization_notes.md
│   ├── task1_substrate_selection_models.md
│   ├── task2_d4_dynamics_convergence.md
│   ├── code/   (16 scripts; shared module irh_models.py; exact_checks.py)
│   ├── figures/  (fig1–fig4 PNGs)
│   └── results/  (10 files: CSV / JSON / .npy)
└── ws-d-frameworks-rivals/             (tasks 8, 9, 10, 12)
    ├── ws-d_summary.md                 (workstream summary + consolidated grades)
    ├── task8_qg_frameworks.md  task8_qg_matrix.md  task8_qg_frameworks_DRAFT.md
    ├── task9_spacetime_frameworks.md  task9_spacetime_matrix.md  task9_spacetime_frameworks_DRAFT.md
    ├── task10_derivations_check.md
    ├── task10_scripts/  (task10_sympy_checks.py + log; task10_numeric_checks.py + log)
    ├── task12_rival_accounts.md  task12_divergence_table.md  task12_rival_accounts_DRAFT.md
    └── task12_models/  (5 executable models + compare_driver.py + driver_output.txt + rerun log)
└── ws-e-cosmology-map/               (tasks 11, 14, 15)
    ├── 11-bifurcations-report.md
    ├── 14-researcher-map-report.md
    ├── 15-cosmological-signatures-report.md
    ├── data/   (4 scripts, 2 JSONs, 3 literature slices)
    └── figures/  (fig1–fig6 PNGs)
```

Total package size ~5.0 MB (142 files). `__pycache__/` directories were excluded.
No credentials, tokens, or passwords anywhere in the package (scanned
before zipping).

---

## 4. Workstream A — core computations (tasks 1–5)

**Directory:** `ws-a-core-computations/`
**Shared model:** `d4model.py` — the 24-mode D4 standing wave, Landau
functional, conserved Model B dynamics; parameters exactly as in IRH
v93.1. All five task scripts import it. **Read `checks/check_model.py`
first:** it checks the shared model against the manuscript / repo
verification record, exits non-zero on any FAIL, and was re-run clean
(exit 0) after the stepper fix (see §4.6).

### 4.1 Task 1 — 3D projections of the D4 standing wave

**CLAIM.** The 3D projections of the D4 standing wave, for rational and
irrational viewing directions, with Fourier signatures, figures, and peak
tables.
**STATUS: VERIFIED** for the stated finite window (D4 points in the ball
of radius 5).

**Headline results.**
- |Aut(D4)| = **1152 exactly**, by Gram-matrix enumeration over
  simple-root automorphisms. Therefore 5 ∤ 1152: **no projection
  direction yields exact icosahedral symmetry** — the IX.1.5 question is
  answered in the negative.
- Projection $\neq$ cross-section: the e4 projection is **$Z^{3} ($simple
  cubic)**, not the FCC cross-section.
- Rational directions give periodic projections (lattice fraction 1.0,
  full-strength Bragg peaks); irrational directions give aperiodic ones
  (lattice fraction 249/1465, split intensities — the quasiperiodic
  signature, verified structural across 7 directions).

**Grades (worst-of, per narrow claim).**

| claim | grade | basis |
|---|---|---|
| \|Aut(D4)\| = 1152 | F3 | exact enumeration, one route (Gram enumeration); matches the known order of W(F4), not re-derived here — Hark audit §6 |
| No exact icosahedral projection (5 ∤ 1152) | F3 | deductive from the order on an F3 premise $\to$ worst-of F3 |
| P(D4) along e4 is $Z^{3}$ | C | parity argument (deductive) + window verification to \|x\| $\leq 4$; C is the Track E cap (I1) |
| Slice signatures (peak counts/multiplicities) | C | exact computation on the stated window; window-dependent; C is the Track E cap |
| Lattice fraction 249/1465 for irrational directions | C | measured regularity on 7 directions + mechanism; not a theorem |
| Bragg-peak splitting = quasiperiodic signature | C | direct computation; clustering width is a stated choice; C is the Track E cap |

**Files.** `task1_projections.py`, `task1_report.md`,
`figures/task1_projection_scatter.png`,
`figures/task1_structure_factor.png`, `figures/task1_wave_slice.png`,
`tables/task1_projections.json`, `tables/task1_slice_peaks.csv`,
`tables/task1_bragg.csv`.

**Replication.** From `ws-a-core-computations/`:

```sh
$PY task1_projections.py
```

Writes the three tables and three figures. The icosahedral verdict is
the Gram enumeration in the script (the earlier 384-generator attempt
was wrong and is replaced, not patched over — see the report §8).
Provenance note (Hark audit §1): the shipped
`tables/task1_projections.json` carries `n_distinct_positions` /
`max_multiplicity` fields the shipped script does not write, and its
lattice basis differs from the script's output in Hark's environment
(NumPy 2.5.4) — in the package environment (NumPy 2.4.6) a fresh run
reproduces the shipped basis exactly for all 7 directions. The shipped
JSON came from a different script revision; the numbers (lattice
fractions, shortest norms) are identical either way.

### 4.2 Task 2 — first directional anisotropy (sixth-moment polynomial)

**CLAIM.** The sixth-moment polynomial of the 24 roots, its angular
extrema, and a figure.
**STATUS: VERIFIED.** The moment polynomial is an exact symbolic
identity; all critical points are enumerated exactly.

**Headline results.**
- M6(k) = **60|k|${}^{2}\Sigmak_{i}^{4} - 48\Sigmak_{i}^{6}** ($sum over the 24 D4 roots).
- On the unit sphere: mean **15** exactly; **global $\min 12** (\langle100\rangle$,
  $\langle111\rangle)$; **global $\max 18** (\langle110\rangle)$ — $a **\pm20$% directional signature**,
  max/min = 3/2.
- All critical points enumerated exactly via Lagrange multipliers (the
  gradient condition forces the nonzero $k_{i}^{2}$ to take at most two distinct
  values) and confirmed by independent scipy optimisation.

**Grades (worst-of, per narrow claim).**

| claim | grade | basis |
|---|---|---|
| Exact isotropy through fourth order (M2, M4 direction-free) | C | symbolic + numerical cross-check (same basis); C is the Track E cap (I1) |
| Mean over $S^{3} = 15$ exactly | F2 | exact symbolic + independent numerical optimisation (two machine routes) — Hark audit §6 |
| Global min 12 at $\langle100\rangle$, $\langle111\rangle$ | F2 | Lagrange enumeration + AM-GM proof of the lower bound, confirmed by scipy 200-start optimisation |
| Global max 18 at $\langle110\rangle$ | F2 | Lagrange enumeration + 200-start numerical confirmation (max 18.000000000000014); no hand proof of the upper bound |
| Directional signature $\pm20$%, max/min 3/2 | C | follows from the min/max; C is the Track E cap |

**Files.** `task2_anisotropy.py`, `task2_report.md`,
`figures/task2_path.png`, `figures/task2_disk.png`,
`tables/task2_moment_values.csv`, `tables/task2_critical_points.csv`,
`tables/task2_summary.json`.

**Replication.** From `ws-a-core-computations/`:

```sh
$PY task2_anisotropy.py
```

### 4.3 Task 3 — D4 stability band under detuning

**CLAIM.** The stability band under detuning (mean, quench depth,
wavelength detuning, sixth-order coupling) with phase maps.
**STATUS: VERIFIED** for the stated windows and the one-mode Landau
functional. **This is the task that carries the band discrepancy — see
§8.1.**

**Headline results.**
- W1 band: **11.60%** of the scanned plane at $(\delta = 0, w6 = 0) \to$
  **8.36%** at $(\delta = 0, w6 = 0.2)$. Hex-only band: 12.94% $\to 9.68$%.
- The manuscript's **11.85% is bracketed (11.60% full family, 12.94%
  hex-only) but NOT reproduced** — the manuscript's window is unstated,
  so the comparison is at trend level only. The manuscript's w6
  narrowing (11.90% $\to 8.47$%) is likewise trend-matched (11.60% $\to$
  8.36%), not reproduced.
- **Detuning shifts the band by $\delta^{2}$ in r**: coexistence at $\bar{\psi} = -0.18$
  moves $-0.218 \to -0.468$.
- $\delta = 0.5$ kills the ordered branch **at the operating point only**, not
  plane-wide (band persists at 8.18%).
- **tri3 excluded** from the competitor family: Q = 0 exactly makes its
  one-mode functional unbounded below at w6 = 0 and unphysically deep
  $(A \approx 2.7)$ at w6 > 0.

**Grades (worst-of, per narrow claim).**

| claim | grade | basis |
|---|---|---|
| Band fractions in W1/W2 at $(\delta, w6)$ grid | C | exact minimisation on stated windows, validated vs scipy; window-dependent by construction; C is the Track E cap (I1 — the workstream graded these B; corrected per Hark audit §6) |
| w6 narrows the band 11.60% $\to 8.36$% (manuscript 11.90% $\to 8.47$%) | C | computation + manuscript comparison; the manuscript's window is unstated so the comparison is at trend level |
| Detuning shifts the band by $\delta^{2}$ in r (coexistence $-0.218 \to -0.468)$ | C | exact root-finding; the shift is a property of the one-mode functional |
| $\delta = 0.5$ kills the ordered branch at the operating point | C | discriminant computation + manuscript sim7 agreement |
| Band boundaries (coexistence + competition lines) | C | exact brentq on the large stationary root; cross-checked vs Task 4 |
| Manuscript 11.85% reproduced | C | bracketed (11.60% / 12.94%) but not reproduced exactly; window unstated |

**Files.** `task3_band.py`, `task3_report.md`, `task3_rerun.log`,
`task3_rerun2.log`, `figures/task3_phasemap.png`,
`figures/task3_band_heatmap.png`, `figures/task3_boundaries.png`,
`tables/task3_band.csv`, `tables/task3_band.json`,
`tables/task3_boundaries.csv`, `tables/task3_winner_W1.npy`,
`tables/task3_winF_W1.npy`.

**Replication.** From `ws-a-core-computations/`:

```sh
$PY task3_band.py
```

Grid: $(\bar{\psi}, r) \in [-0.6, 0.2] \times [-0.6, 0.1]$, $161\times161$. Minimisation is
vectorised: exact quadratic formula for w6 = 0; Newton from the w6 = 0
roots plus a coarse A-scan for w6 > 0. Note the brentq pitfall: brentq
on $F_{min}$ fails (flat above coexistence) — the script uses F at the
large stationary root (see §11, pitfall 8).

### 4.4 Task 4 — critical droplet + nucleation threshold

**CLAIM.** Critical droplet and nucleation threshold: droplets at several
sizes/amplitudes under conserved dynamics, critical-size estimate, growth
map.
**STATUS: VERIFIED** for the amplitude-equation routes $(\kappa$, thin-wall,
radial ODE) and the box runs.

**Headline results.**
- Gradient coefficient **$\kappa = 192$** verified against exact FFT energy
  (relative deviation 4.2e-05).
- Coexistence **$r_{coex} = -0.217984$**, **A\*_c = 0.058251**,
  **$\sigma = 0.018776** ($two independent quadratures agree exactly).
- **Radial-ODE (exact within the amplitude equation$): R_{c} = 12.57$,
  $\DeltaF$\* = 555** — ~$15\times$ the thin-wall estimate (7.38, 37.2), which FAILS
  here because $\xi = 8.64 > R_{c} ($thick-walled).
- §II.9 confirmed: exact spinodal **$\bar{\psi} = -0.1439$**; at $-0.10$,
  $r_{eff} = -0.12$, no barrier.
- **Box runs: 7/8 grew** to the full ordered state; only R = 0.6/A\*
  decayed.
- **$R_{c} ($ODE) and the box threshold are different quantities, not to be
  conflated:** the ODE value is infinite-volume (it cannot fit in the
  $\pi$-box: $R_{c} = 12.57$ vs box half-size 1.57); the box threshold is a
  finite-volume property.

**Grades (worst-of, per narrow claim).**

| claim | grade | basis |
|---|---|---|
| $\kappa = 192 ($gradient coefficient) | C | derived from the SH operator + exact-FFT verification to 4 decimals; derivation is mine, not the manuscript's; C is the Track E cap (I1 — the workstream graded these B; corrected per Hark audit §6) |
| Coexistence $r_{coex} = -0.217984$, A\*_c = 0.058251 | C | exact root-finding; cross-checked vs Task 3 |
| $\sigma = 0.018776$ | C | two independent quadratures agree exactly |
| Thin-wall $R_{c} = 7.38$, $\DeltaF$\* = 37.2 | C | the approximation is shown to fail here $(\xi > R_{c})$; reported as the failed approximation |
| ODE $R_{c} = 12.57$, $\DeltaF$\* = 555 | C | exact within the amplitude equation; two integration routes agree to 0.1%; truncation-limited |
| §II.9 barrier vanishes (spinodal $-0.1439)$ | C | exact $r_{eff}$ computation + stationary-point check |
| Box threshold: only R = 0.6/A\* decays, rest grow | C | direct Model B runs; finite-box result, stated as such |
| Infinite-volume $R_{c}$ vs box threshold distinguished | C | scale argument $(R_{c} = 12.57$ vs L/2 = 1.57, $\lambda = 2.22)$ |

**Files.** `task4_thinwall.py` (parts A–C, analytic routes),
`task4_droplet_runs.py` (part D, box runs), `task4_report.md`,
`task4d.log`, `figures/task4_droplet.png`,
`tables/task4_thinwall.json`, `tables/task4_ode_profile.npz`,
`tables/task4_droplet_runs.json`.

**Replication.** From `ws-a-core-computations/`:

```sh
$PY task4_thinwall.py
$PY task4_droplet_runs.py
```

Part D seeds: droplet radius $R \in {0.6, 0.8, 1.0, 1.2} ($box units,
$L = \pi) \times$ amplitude $A \in {A$\*, 1.5 A\*}, 6000 steps each, dt = 0.005,
$q0^{2} = 8.0$, $\bar{\psi} = -0.18$; metrics sampled every 250 steps. Classification
at the end: growth (D4 > 0.9 and rms > 0.3), decay (D4 < 0.2 and
rms < 0.1), else marginal.

### 4.5 Task 5 — basin map of the full 24-mode pattern

**CLAIM.** Basin map: random / partial-pattern / perturbed starts under
Model B.
**STATUS: PARTLY FAILED as written (Hark replication audit, 2026-11-10;
independently confirmed by the parent's own transverse run — see
HARK_REPLICATION_AUDIT_REVIEW.md §F1).** The 14-run protocol itself
reproduces (log ends `TASK5 EXIT:0`); the "stable attractor" reading of
the sub-pattern runs does not.

**Headline results.**
- Full pattern recovers from **phase noise up to 1.0 rad RMS** and
  **$\pm20$% amplitude** perturbations.
- **hex6 and fcc12 are NOT stable attractors — FAILED as written.**
  The unperturbed starts stay hex6/fcc12 (stationary to 6 decimals from
  step 3000), but that is an invariant-subspace artefact: the absent
  modes are seeded exactly zero. With a transverse perturbation as small
  as 0.2% of A\* in the absent modes, hex$6 \to$ full24 (5/5 runs) and
  fcc$12 \to$ full24 (4/4 runs) at $\bar{\psi} = -0.18$; the unperturbed control stays
  hex6. At $\bar{\psi} = -0.18$ the 24-mode is the only attractor seen from any
  perturbed start; hex6/fcc12 are saddles. The sentence "the Model B
  analogue of the manuscript's annealed 6-mode outcome" is withdrawn.
- sq4/sq8 decay (T = 0, predicted); **all 6 noise seeds decay**.

**Grades (worst-of, per narrow claim).**

| claim | grade | basis |
|---|---|---|
| Full pattern recovers from $\delta\phi \leq 1.0$ rad and $\pm20$% amplitude | C | 4 direct runs, fully converged; protocol-specific (Model B, $q0^{2} = 8.0)$; C is the independence-bound cap (I1 — the workstream graded these B; corrected per Hark audit §6) |
| hex6 is a stable attractor under Model B (stays hex6) | **FAILED as written** | unperturbed start stays hex6, but a 0.2% transverse perturbation grows it to full24 (5/5 runs) — invariant-subspace artefact, not stability |
| fcc12 is a stable attractor under Model B (stays fcc12) | **FAILED as written** | same falsifier as hex6 (4/4 transverse runs $\to$ full24) |
| sq4/sq8 decay to uniform | C | direct runs + one-mode prediction (T = 0) agree; C is the independence-bound cap |
| Noise seeds decay (6/6) | C | direct runs; small-sample (n = 6); C is the independence-bound cap |
| Basin map as stated (full / sub-pattern traps / uniform) | **FAILED as written (sub-pattern leg)** | the full-pattern and uniform legs stand; the "sub-pattern traps" leg is falsified by the transverse runs |

**Files.** `task5_basin.py`, `task5_report.md`, `task5.log`,
`figures/task5_basin.png`, `tables/task5_basin.json`.

**Replication.** From `ws-a-core-computations/`:

```sh
$PY task5_basin.py
```

14 runs, 6000 steps each, $L = \pi$, $q0^{2} = 8.0$, $\bar{\psi} = -0.18$: random noise
starts (seeds 1–6, amp 0.05); partial-pattern starts hex6, fcc12, sq4,
sq8 at A\*; perturbed full-pattern starts (phase RMS $\delta\phi \in {0.1, 0.5$,
1.0} rad; amplitude $\pm20$% pairwise so the field stays real). Phases are
assigned antisymmetrically $(\phi_{-n} = -\phi_{n})$ and amplitudes pairwise
(|$\phi[n]$| = |$\phi[-n]$|) so every seed is a real field. One run takes ~36 s
on the local CPU; the full set is ~10 minutes. The first launch was
killed by a runtime restart after 1 run; the script saves incrementally
and the relaunch completed all 14 runs — if your session is
interrupted, re-run the script; it resumes from the saved rows.

### 4.6 The load-bearing bug (WS-A §6, also found independently in WS-C)

The Model B stepper grows an **anti-Hermitian roundoff component
$\times1.0142$ per step** from roundoff, reaching NaN by ~6000 steps. It was
found via the droplet runs (WS-A) and independently via the attractor
runs (WS-C, where the shipped-style update blows up at t = 27.5).
The fix is a **per-step Hermitian symmetrisation** in
`d4model.ModelB.step` (WS-A) / per-step Hermitian projection (WS-C),
which is an exact no-op in exact arithmetic. After the fix,
`checks/check_model.py` re-ran clean (exit 0). **Any replication of
the Model B runs MUST use the fixed stepper as shipped in this
package; the unfixed update diverges and its outputs are meaningless.**

---

## 5. Workstream C — substrate models + D4 dynamics convergence (tasks 7 + 13)

**Directory:** `ws-c-substrate-convergence/`
**Shared module:** `code/irh_models.py` — generalises the repo
verification integrators (`sim6_units.py` Model B / Model A
semi-implicit attractor, RK4 damped-wave quench; `sim7_fairtest.py`
semi-implicit damped wave) over (N, L, $q0^{2}$, r, u, v, gamma, dt, steps,
$\bar{\psi}$, seed) WITHOUT changing the discretisation: same filters (K2<200
attractor, K2<64 quench), same schemes. **Read `CLAIM_REGISTER.md`
first:** it registers every claim (C1.1–C1.6, C2.1–C2.5, P1–P5) with its
falsifier before the results.
**Exact checks:** `code/exact_checks.py` — SymPy 1.14.0 + python-flint
0.8.0 + Z3 4.15.4, **29 check statements, 31 [PASS] lines (the $r_{eff}$
table loops over 3 rows), exit 0**. Baselines reproduced first:
sim6 attractor exact to all quoted digits; sim7 fair test 0.771 /
0.211 / 0.895 (annealed 0.895 exact vs the independent reproduction).
All computation local CPU, ~1 hour wall-clock.

### 5.1 Task 7 — formalize substrate selection models (static vs dynamic D4)

**CLAIM.** Formalize the static-D4 and dynamically-selected-D4 accounts
as models; state shared conditions and divergence points.
**STATUS: divergence boundary measured; one registered claim FAILED as
written (C1.2), the rest grade C / F3 as tabulated.**

**Headline results.**
- The noise quench **never reaches the full 24-mode pattern** (5 seeds:
  6-mode $\times3$, 2-mode, 8-mode). The 6-mode outcome is the manuscript's
  hexagonal sub-pattern, identified post-hoc: 3 coplanar cosine
  directions at $60^\circ$ in the $x_{4}=0$ subspace, (N,T,Q) = (6,12,90),
  $S_{6} = 0.2667$.
- The damped-wave quench **forgets the initial mean entirely**
  $(\bar{\psi}$_final $\approx +0.0025$ from any $\bar{\psi}_{0} \in {-0.30, -0.18, 0, +0.10})$.
- **Triads are load-bearing** $(u = 1 \to 6$-mode, $u = 0 \to 12$-mode).
- Detuning past the exact edge **|$q_{0}^{2}-8$| > 0.4024 kills the pattern**
  $(q_{0}^{2} = 7.5 \to$ noise only).
- The seeded 24-mode **decays at $\bar{\psi} = -0.30** ($no branch) but persists
  metastably at $\bar{\psi} = 0$, +0.10 (F above the 6-mode) **when unperturbed —
  FAILED as written as a "local minimum" claim (Hark audit F1): with a
  small perturbation the $\bar{\psi} = 0$ seeded 24-mode goes to 6-mode, and the
  $\bar{\psi} = +0.10$ one to a 2-mode stripe-like state. The persistence is an
  invariant-subspace artefact, as for hex6/fcc12.**
- Measured 24-mode global-minimum band at $r = -0.35$:
  **$\bar{\psi} \in (-0.235, -0.125)$** — narrower than the manuscript's quoted
  $(-0.33, +0.03)$, which is the union over quench depths; the **+0.03
  edge is UNVERIFIED** and is referred to WS-A task 3's band map.
- The static account's starkest failure: at $\bar{\psi} = -0.30$ it imposes the
  pattern at **Fexc = +0.011431, above the disordered state**.
- **C1.2 FAILED as written** — Q2 (noise quench at $\bar{\psi}_{0} = -0.18$, inside
  the quoted band) reaches 6/24, which is the register's own falsifier;
  the basin-qualified version is confirmed under C1.3.
- **Findings 6–7 ("both patterns are local minima at both $\bar{\psi}$") FAILED
  as written (Hark audit F1, confirmed by the parent's transverse
  run):** at $\bar{\psi} = -0.18$, hex6 + 0.2% transverse perturbation $\to$ full24
  (5/5); fcc$12 \to$ full24 (4/4). At $\bar{\psi} = 0$ hex6 is genuinely stable (Hark;
  not re-run by the parent). Corrected statement: the 24-mode is the
  only attractor seen from perturbed starts at $\bar{\psi} = -0.18$.
- P1, P2, P3 confirmed (P3 via the sim7 control, 0.211).
- **Real defect fixed:** the shipped-style Model B update blows up at
  t = 27.5 from anti-Hermitian roundoff growth (1.0142/step = 1/0.986
  at the shell); per-step Hermitian projection (exact no-op in exact
  arithmetic) extends stability to t = 30. The one-mode free-energy
  coefficient is **N/2, not $N^{2}** ($pdftotext rendering artifact) —
  corrected with evidence, not silently.

**Grades (worst-of, per narrow claim).**

| claim | grade | basis |
|---|---|---|
| C1.1 Static account predicts the full 24-mode pattern under ALL conditions | C | 24/24 imposed at every $\bar{\psi}$ incl. $\bar{\psi} = -0.30$ where Fexc > 0; falsifier (a manuscript statement giving the static account a selection dynamics) not found $\to C ($Track E cap) |
| C1.2 Dynamic account predicts the full 24-mode pattern ONLY inside the band with $q_{0}$ tuned and triads active | **FAILED as written** | Q2 is the register's own falsifier: noise quench at $\bar{\psi}_{0} = -0.18 ($inside the quoted band) reaches 6/24. The basin/evolved-$\bar{\psi}$ corrected version is CONFIRMED under C1.3. No grade above FAILED applies to the claim as written. |
| C1.3 Divergence boundary D1–D4 (branch edge, detuning 0.4024, triads off, basin IC) | C | all four legs confirmed at probe points; branch edge exact (two tools$) \to C ($Track E cap) |
| C1.4 Ontology change dissolves the circularity objection; $a_{0} = 2\pi/q_{0}$ is an output of the dispersion, not an input via $L_{P} ($Track F) | F2 | deductive chain verified $(a_{0} = 2.221441$, CFL dt_max = 1.9238, exact checks: SymPy + flint + Z3, 31 PASS — two-plus routes; F2 per Hark audit §6) |
| C1.5 Static account CANNOT explain (a) lattice selection, (b) finite band, (c) 6-mode outcome, (d) nucleation, (e) Model A vs B | C | (b), (c), (e) measured directly; (a), (d) established by absence of the relevant structure in the static formulation (manuscript §I.$1) \to C ($Track E cap) |
| C1.6 Landau + LJ corroborate the winner; S-transfer is deductive combinatorics; near-melting scope does NOT transfer | C | S4 split verdict (combinatorial PASS, scope FAIL); Hoy leg NOT RUN $(A5) \to C ($Track E cap) |

**Files.** `task1_substrate_selection_models.md`,
`code/task1_substrate_models.py` (single-driver version — see the
runtime note below), `code/task1a_quenches.py` (Q1–Q3),
`code/task1b_quenches.py` (Q4–Q7), `code/task1c_attractors.py`
(attractors, static model, Landau curves),
`code/instability_series.py`, `code/bisect_instability.py`,
`code/probe_t18.py`, `figures/fig1_landau_curves.png`,
`figures/fig2_divergence.png`, `figures/fig4_instability.png`,
`results/task1_landau_curves.csv`, `results/task1_probe_results.csv`,
`results/task1_q1_final.npy`, `results/task1_q1_top6.json`.

**Replication.** From `ws-c-substrate-convergence/`:

```sh
$PY code/exact_checks.py            # 29 statements, 31 PASS lines, exit 0 — run this first
$PY code/task1a_quenches.py         # Q1–Q3 (RK4 damped wave, T=50, N=16, L=π)
$PY code/task1b_quenches.py         # Q4–Q7
$PY code/task1c_attractors.py       # reads results/task1_q1_final.npy (from 1a); writes landau curves + top-6 JSON
$PY code/make_figures.py           # reads results/*.csv → figures/*.png
```

Order matters: 1c reads 1a's `.npy`. The drivers append rows to
`results/task1_probe_results.csv` incrementally (header created if
missing) — re-running a driver appends duplicate rows, so for a clean
replication delete the CSVs first (the shipped CSVs are the record of
the original runs; keep a copy). Do NOT use the single-driver
`code/task1_substrate_models.py` for replication: it died without
output in the original session, and the split drivers (1a/1b/1c) are
the reliable pattern. Diagnostics (not part of the main chain):
`code/bisect_instability.py DT TMAX` (bisects the late-onset Model B
instability), `code/probe_t18.py` (the t = 18 anomaly probe),
`code/instability_series.py` (unprojected vs projected $\langleA\rangle(t)$ series
for fig4).

### 5.2 Task 13 — check D4 dynamics convergence

**CLAIM.** Grid/time-step refinement: discretization, input, and
model-form errors vs analytic/published values.
**STATUS: attractor fixed point is resolution-independent, so two
registered claims FAIL as written — and the corrections are the result.**

**Headline results.**
- $\langleA\rangle = **0.077682$**, $D_{4} = **0.999981$**, Fexc = **$-0.007728$**, 24/24
  modes are **identical to 6 decimals at all 8 ladder points**
  $(N \in {8,12,16,20} \times$ dt $\in {0.0025$–0.02}); discretization error of
  the fixed-point state is **0 below 1e-6**.
- The genuine order lives in the transient: **first order, Richardson
  $p \approx 0.95$ at T = 0.5, over by T = 5 at every dt**.
- **C2.2 and P4 FAILED as written** (the $\langleA\rangle$-vs-A\* error, +0.000106,
  is dt-independent — a model-form harmonic gap, not discretization
  error). The corrected claim (transient error decreases, $p \approx 0.95)$ is
  confirmed.
- Error tabulation: attractor budget is model-form (ansatz-vs-relaxed
  **1.238%**, re-measured vs manuscript 1.25%) + input $(\bar{\psi} \pm0.01 \to$
  $\langleA\rangle \pm1.6$%, Fexc $\pm17$%; $q_{0}^{2} \pm0.1 \to \langleA\rangle -1.4$%, Fexc +9%, symmetric);
  quench budget is input-dominated (seed spread Fexc $-0.0358$ to
  $-0.0418$, 15%) with N = 8 failing (2-mode) and N = 12/16 agreeing;
  dt error negligible $(0.04 \equiv 0.02$ to 1e-6).
- **$\bar{\psi}$ drift 1.58e-15 at t = 30** — P5 (< 1e-12) confirmed by 3 orders;
  the reference 8.3e-17 is not re-measured at that precision (mine is
  1.1e-15 at t = 7.5, projection on).
- Model B vs wave on the seeded attractor: the difference is the mean
  only (wave $\to \bar{\psi} = +0.00087, \langleA\rangle = 0.08585)$; the pattern survives in
  both.

**Grades (worst-of, per narrow claim).**

| claim | grade | basis |
|---|---|---|
| C2.1 Reference model reproduces the analytic stationary state (A\* = 0.0775753, $F/V = -0.0076323, D_{4} = 1.0000, 24/24, \bar{\psi} ~1e-16)$ | C (Track E part); F2 (Track F part, A\*/F/V) | $\langleA\rangle$/Fexc differ from the ansatz values by the measured harmonic gaps (+0.137%, $-1.24$%) — model-form, not failure; $D_{4} = 0.999981 ($harmonic deficit 1.9e-5); 24/24 ✓; conservation measured 1.1e-15, not $1e-16 \to C$; analytic values verified exactly (two tools$) \to F2$ per Hark audit §6 |
| C2.2 Discretization error decreases with N and dt, measurable order | **FAILED as written** | fixed-point error is 0 at every ladder point (no decrease to measure); transient error DOES decrease, $p \approx 0.95$ — the corrected claim is confirmed, the registered claim is not |
| C2.3 Input error quantified separately, compared with discretization | C | seed spread (5 seeds), $\bar{\psi} \pm0.01$, $q_{0}^{2} \pm0.1$ all measured; input dominates discretization at reference resolution $\to C ($Track E cap) |
| C2.4 Model-form error quantified: (a) ansatz vs relaxed, (b) Model B vs wave, (c) sim6 vs sim7 | C | (a) 1.238% re-measured; (b) mean-only difference measured; (c) setup difference stated, not conflated with error $\to C ($Track E cap) |
| C2.5 CFL respected; $\bar{\psi}$ conservation at the 1e-16 level (Track F) | C (conservation leg); F2 (CFL leg) | CFL: exact arithmetic, all dt $\leq 0.04 << 1.9238 \to F2$ per Hark audit §6 (SymPy + flint + Z3 in exact_checks). Conservation: measured 1.1e-15 at t = 7.5, one order coarser than the reference $8.3e-17 \to C$ worst-of. P5 (< 1e-12) PASS. |

**Files.** `task2_d4_dynamics_convergence.md`,
`code/task2_convergence.py` (single-driver version — same caveat as
task 1: use the split drivers below), `code/task2a_attractor_ladder.py`
(N-ladder {8,12,16,20} at dt = 0.005; dt-ladder {0.02, 0.01, 0.005,
0.0025} at N = 16), `code/task2b_quench_ladder.py` (quench ladder +
seed sensitivity), `code/task2c_sensitivity_modelform.py` (input
sensitivity + model form), `code/task2d_transient.py` (transient
dt-convergence, Richardson fit),
`code/sim7_annealed_only.py` (baseline reproduction — see note below),
`figures/fig3_convergence.png`, `results/task2_ladder.csv`,
`results/task2_input_sensitivity.csv`, `results/task2_modelform.csv`,
`results/task2_transient.csv`, `results/task2_attractor_sensitivity.csv`.

**Replication.** From `ws-c-substrate-convergence/`:

```sh
$PY code/exact_checks.py                  # 29 statements, 31 PASS lines, exit 0 — run this first
$PY code/task2a_attractor_ladder.py       # reference A* = 0.0775753, F/V relaxed = -0.0077276
$PY code/task2b_quench_ladder.py          # seeds {3,4,5} at N=16, dt=0.02 (seeds 1,2 are Task 1's Q1, Q7)
$PY code/task2c_sensitivity_modelform.py  # ψ̄ ∈ {-0.19,-0.18,-0.17}, q0² ∈ {7.9,8.0,8.1}
$PY code/task2d_transient.py             # seed at 1.2*A* (0.0931); <A> at T=5 across dt
$PY code/make_figures.py                 # WARNING (Hark audit F4): task2d overwrites results/task2_transient.csv with T=5-only rows, and make_figures then CRASHES (IndexError, line 88) — the shipped CSV's T=0.5/1.0 rows came from an unshipped run. The p ≈ 0.95 claim stands (regenerated values match), but a clean re-run does NOT reproduce fig3 as written.
```

**Baseline note.** `code/sim7_annealed_only.py` re-runs ONLY the sim7
annealed leg (triad ON, anneal, seed = 2, noise 0.5) to close the
baseline (the full sim7 run's first two legs were already captured:
D4 = 0.771 triad ON, 0.211 triad OFF). It contains an absolute
`sys.path.insert` to
`/home/hatch/workspace/research/IRH-Theory-Development-Workspace/verification`
— the local IRH repo clone. If you replicate on another machine, point
that line at your own clone of
`brandonmccraryresearch-cloud/IRH-Theory-Development-Workspace`
(`verification/sim7_fairtest.py`); the logic is otherwise verbatim from
sim7.

---

## 6. Workstream D — frameworks + rivals + derivations (tasks 8, 9, 10, 12)

Method: deepest-research FULL mode throughout (stated plainly in each
report; systematic-review mode NOT chosen and NOT used). Tasks 8, 9, 12
were assembled by the parent agent from child drafts (assembly
corrections recorded in each report and in `ws-d_summary.md` §7);
task 10 was direct session work by the parent. All new claims: I1 max,
Track E cap C / Track F cap F3 (human source/balance gates not
performed). IRH geometric-core grades are carried from the repo record,
cited not re-earned. **Parent verification (2026-11-11 ~01:30 CST):**
task-10 scripts re-run in a scratch copy — 45 [PASS] / 0 [FAIL]
(SymPy) and 33 [PASS] / 0 [FAIL] (flint + numpy), both exit 0;
task-12 driver re-run in a scratch copy — 55 [PASS] / 0 [FAIL],
exit 0, and the shipped `driver_output.txt` is byte-identical to the
shipped rerun log. **Note on grades:** the Hark audit's §6.5 repeal and
$F3\toF2$ regrade applied to the audited package (WS-A/C/E) only. WS-D was
not in that audit; its F3 caps stand as the workstream stated them.
Whether the same two-route logic lifts any WS-D F3 to F2 is not
decided here.

### 6.1 Task 8 — compare quantum-gravity frameworks

**CLAIM.** Of the frameworks competing to explain quantum gravity / the
emergence of spacetime — LQG / spin foams, string theory (and AdS/CFT),
asymptotic safety, CDT, causal-set theory, GFT, emergent/analogue
gravity, and IRH v93.1 — **no framework has a laboratory-confirmed
Planck-scale prediction, and no framework has derived the Einstein
field equations together with Lorentzian signature, diffeomorphism
invariance, and the Standard Model gauge structure plus a confirmed
prediction.**
**STATUS: VERIFIED** as a comparative characterisation (deepest-research
FULL mode; primary sources confirmed in session). Comparative claims
C1–C12 grade C; the C9 interpretation ("gravity is emergent") is
exploratory, grade D.

**Headline results.**
- Strongest derived emergence result in the set: **CDT's numerical 4D
  de Sitter universe**, spectral dimension running $4.02 \pm 0.1 \to$
  $1.80 \pm 0.25 ($Ambjørn–Jurkiewicz–Loll 2004/2005; numbers verified in
  assembly via Giasemidis et al. 2012, eq. 7 — the task-8 ABSTAIN on
  these numbers was withdrawn).
- Only prediction-in-advance: **causal sets' heuristic $\Lambda \sim 10^{-120}$**
  (Sorkin 1997, pre-1998).
- LQG's sharpest derived result is kinematic (discrete area/volume,
  Rovelli–Smolin 1995); the EPRL classical limit is still open.
- AdS/CFT remains a conjecture (Maldacena 1997) formulated in AdS,
  not de Sitter. Asymptotic safety's Reuter fixed point is
  truncation-only evidence. GFT condensate cosmology yields a modified
  Friedmann equation, but the condensate-as-GR-geometry step is
  unestablished.
- **Bartha gate (S4) FAILS the transfer "substrate dynamics $\Rightarrow$
  Einstein equations" for IRH and analogue gravity generally** —
  confirming IRH v93.1's own retraction against
  Barceló–Liberati–Visser 2011 and Sindoni 2012. Jacobson $\Rightarrow$ IRH
  transport FAILS / NOT ESTABLISHED (thermodynamic premises have no
  positive analogue in IRH); dynamical signature $\Rightarrow$ IRH reading (A)
  FAILS for v93.1.
- IRH's position is the narrowest and most checked at the geometric
  level — $D_{4}$ selection $(S = 64/141 \approx 0.454)$ and $E_{6}$ via 2T/McKay are
  Grade A (carried) — while its gravity side is open or retracted by
  its own Part IX.

**Assembly corrections (parent).** arXiv:1703.07556 is Dowker & Zalel
2017, not a survey — citation corrected to Surya LRR 2019
(arXiv:1903.11544, full text read; the "only successful prediction"
phrase was not found there and was dropped). arXiv:2307.13743
confirmed (Das–Nasiri–Yazdi, everpresent-$\Lambda$ tests); arXiv:0712.2485
abstract confirms 17–28 Planck lengths.

**Files.**
`task8_qg_frameworks.md` (1,086 lines, FINAL),
`task8_qg_matrix.md` (159 lines, cross-referenced matrix),
`task8_qg_frameworks_DRAFT.md` (1,034 lines — the child's verbatim
draft, preserved; the FINAL differs by the assembly corrections).

**Replication.** Literature work: replication = the stated queries and
the primary-source checks in the report §2.1 / §7. No scripts.

### 6.2 Task 9 — compare spacetime frameworks

**CLAIM (narrow, frozen before analysis).** IRH v93.1's account of
spacetime and of dimensionless constants does **not** derive spacetime
signature, the Einstein equations, or the numerical values of
dimensionless constants. Its constants account is: (i) the §I.1 triad
relations are definitional re-expressions of measured Planck-scale
quantities, not derivations; (ii) the $\alpha^{-1}$ ansatz is a downgraded
numerical ansatz, not a derivation; (iii) the dimensional assignment
is undecided and not resolvable by further calculation; (iv) no
signature mechanism is supplied inside IRH; (v) Einstein equations
are not derived (analog-gravity route retracted as analogy).
**STATUS: VERIFIED as a negative characterisation of IRH's own text**
(the manuscript itself states each of (i)–(v)), **and UNVERIFIED as a
comparative ranking** — no rival framework in this comparison derives
the constants either, and none is shown here to be superior to IRH on
IRH's own selection problem $(D_{4}$ selection). The comparison is a
**coding and gap-flagging exercise, not a verdict that any framework
wins**. Every cross-framework transfer attempted is audited under
Bartha (S4) and **FAILS** as a derivation-transfer wherever a critical
feature of the source derivation sits in the Negative Analogy.

**Headline results.**
- IRH's constants account is the weakest part of IRH, **by IRH's own
  ledger**: geometric core Grade A mathematics; physical/substrate
  reading $\leq C/D$; constants account below that — definitional (triad),
  numerological $(\alpha$ ansatz), undecided (dimensional assignment).
- Only Greensite / Carlini–Greensite (quantum, one-loop,
  fermion-dominant) and Mukohyama–Uzan / Kehayias et al. (classical,
  clock field, Galileon-not-GR gravity) claim a signature derivation,
  and every derivation-transfer into IRH FAILS the Bartha S4 audit.
- Analog gravity gives an effective metric, never $G = 8\piT$. No surveyed
  account derives $\alpha$. The $\alpha^{-1}$ ansatz $(137.03600282\dots, +3.64\times10^{-6}$ vs
  CODATA 2022) is Eddington-class: arithmetic verified, derivation
  absent — and IRH *labels* it a downgraded ansatz, which is what saves
  it from Eddington's error.
- IRH's distinctive Grade A result $(D_{4}$ selection) is a question no
  rival attempts, so the matrices code rather than crown a winner.
  "IRH'$s E_{6}$ identification derives coupling values / $\alpha$" — **FAILED**
  (no breaking pattern, no RG running; §IX.4). "Anthropic reasoning
  explains $\alpha$ or IRH's tunings" — **FAILED / NOT SUPPORTED**.

**Grades.** Rival characterisations C1–C6, $C8 \to **C** (I1 \to C$; scoped
to surveyed sources). C7 (no rival derives $\alpha) \to **C$ scoped /
UNVERIFIED universal** (verified for surveyed sources only — a
universal negative cannot be proved over all literature).

**Files.**
`task9_spacetime_frameworks.md` (414 lines, FINAL),
`task9_spacetime_matrix.md` (103 lines),
`task9_spacetime_frameworks_DRAFT.md` (402 lines — child's verbatim
draft, preserved; the FINAL differs by one assembly correction, the
K2 clean re-check).

**Replication.** Literature work. Computation checks inside the report:
SymPy 1.14.0, `a₀·Ω_P = c` from the stated definitions — PASS,
exit 0 (algebraic consistency only, not a derivation); the $\alpha$-ansatz
arithmetic is cross-checked by task 10's clean flint.arb run
$(137.036002821941119\dots$, diff +$3.6449411\times10^{-6})$.

### 6.3 Task 10 — check your derivations (the new finding of this workstream)

**CLAIM.** The spacetime/constants derivations of IRH v93.1 were
transcribed into symbolic computation (SymPy) and checked a second time
with an independent tool (python-flint exact rationals + arb, numpy).
**78 checks pass (45 SymPy + 33 flint/numpy), 0 fail on re-run.**
**STATUS: COMPLETE.** The manuscript's arithmetic is, with two
exceptions, exactly as stated. **Exception 1: printed dispersion
relation (7) in §III.1 is WRONG — FAILED as printed.** **Exception 2:
the §III.3 envelope validity table is NOT REPRODUCIBLE from the text
as written — UNVERIFIED.** One claim ABSTAIN (R = 2589 — no derivation
inputs in the source).

**Headline finding 1 — printed (7) is wrong by a factor of 2 (FAILED
as printed).**
The EOM-derived formula is
$\sin^{2}(\omega\Deltat/2) = (\Deltat^{2}\cdot2J/(4M$\*$a_{0}^{2}))\cdot\Sigma(1-\cos) + (\Deltat^{2}\mu^{2})/(4M$\*),
while the printed (7) is
$\sin^{2}(\omega\Deltat/2) = (\Deltat^{2}\cdot2J/(4M$\*$a_{0}^{2}))\cdot[2\Sigma(1-\cos) + \mu^{2}]$.
Two separate errors in one printed equation: the $\Sigma$ term is doubled,
and $\mu^{2}$ is placed inside the bracket (multiplied by pref instead of by
$\Deltat^{2}/(4M$\*)). Three internal checks favour the derived formula: (1)
small-k J = M\*$c^{2}/12$ — the manuscript's own value — vs M\*$c^{2}/24$ from
the printed formula; (2) k = 0 gives $\sin^{2}(\theta/2) = \Deltat^{2}\mu^{2}/(4M$\*) as
§III.3 states; (3) the CFL table matches the derived formula. The
manuscript's own §III.2 expansion ("at the worst case the bracket
equals 32") uses the derived formula, contradicting the printed (7).
**The CFL bound itself is CORRECT** (worst-case sum 32 confirmed by a
$48^{4}$ Brillouin-zone scan; candidate values 4/3, $16\pi^{2}/3$, 1 reproduced).
This is a manuscript erratum to one printed equation, not a refutation
of the bound.

**Headline finding 2 — the §III.3 envelope table does not reproduce
(UNVERIFIED).**
Table: $4\times10^{-5}$, 0.1%, 1.0%, 11%, 133%. Under the natural reading (exact
lattice dispersion vs $\omega = c$|k|) the computed errors are $1.67\times10^{-5}$,
$4.17\times10^{-4}$, $3.75\times10^{-3}$, 4.11%, 36.3% $(\Deltat\to0)$ — smaller by factors 2.4–3.7;
the zone-edge 133% is unreachable under that reading. The table'$s \Deltat$,
carrier $\theta ($or $\mu)$, direction, and error definition are unstated. **The
VI.3 summary boundary (<1% for $a_{0}$|k| ≲ 0.3) still holds under the
recomputed values** (0.042% at 0.10, 0.375% at 0.30) — the boundary
survives; the table's exact entries do not reproduce.

**Also verified (both tools):** selection rationals $(D_{4} S = 64/141$,
$A_{4}$\* 12/31, BCC 16/45, margin 73/423, $\tau$ ratio $\sqrt{2})$; ordered branch
A\* = 0.0775753, $F = -0.0076323$, uniform baseline $-0.0034636$, detuned
no-branch discriminant < 0; resonance maximum 24 unique in the scanned
domain; 24-cell = 2T (576 products, $Q_{8}$ normal, 3 cosets); $E_{6}$ Cartan
det 3, Smith diag(1,1,1,1,1,3); Weyl orders 192/1920; Derrick scaling
and d = 4 marginality; isotropy moments; $\alpha$ ansatz $174\sigma$ from CODATA
2022 (confirms the manuscript's downgrade); $\xi_{2}$ retraction factor 2.
**Side finding:** at $\Deltat = a_{0}/c$ the discrete dispersion is exactly
linear $(\omega = c$|k|) along axis and body-diagonal directions.

**Run record (honest history).** First SymPy run: 3 FAILs, of which 2
were script bugs (E2 mis-stated identity; O2/O4 quaternion product
missing /2) and 1 was the F1 check restated as the exact difference
(the finding itself). In assembly, a further bug was found: the G3-f
check call was indented outside its `for` loop, so only the third dt
value was actually checked. Fixed and re-run; the counts were
corrected (the earlier text said 46 SymPy + 32 numeric; the true
counts are **45 SymPy + 33 numeric**).

| Claim | Grade | Basis |
|---|---|---|
| D1–D4, D6–D16, D19 (triad circle, $\alpha$ arithmetic, Derrick, dispersion identity, CFL, isotropy, selection rationals, ordered branch, $\xi_{2}$ factor, $E_{6}$ Cartan, 24-cell, Weyl orders, resonance, triads, shell counts, exact linearity) | C | two independent tools agree; $I1 \to C$ |
| D5 printed dispersion relation (7) | **C (FAILED as printed)** | EOM derivation + 3 internal checks + manuscript's own §III.2 expansion |
| D17 envelope validity table | **UNVERIFIED** | underdetermined from source; no natural reading reproduces it |
| D18 R = 2589 | **ABSTAIN** | no inputs in source |
| Geometric core (carried) | **A (carried)** | repo record; cited, not re-earned |

**Files.**
`task10_derivations_check.md` (626 lines),
`task10_scripts/task10_sympy_checks.py` + `task10_sympy_run_2026-11-10.log`
(45 PASS, 0 FAIL, exit 0),
`task10_scripts/task10_numeric_checks.py` + `task10_numeric_run_2026-11-10.log`
(33 PASS, 0 FAIL, exit 0). Both scripts print [PASS]/[FAIL] per check
and exit non-zero on any FAIL; they share no code.

**Replication (from `ws-d-frameworks-rivals/`).**

```sh
$PY task10_scripts/task10_sympy_checks.py     # 45 PASS, 0 FAIL, exit 0
$PY task10_scripts/task10_numeric_checks.py   # 33 PASS, 0 FAIL, exit 0
```

### 6.4 Task 12 — formalize rival accounts

**CLAIM.** Five rival accounts of spacetime and of the origins of
dimensionless constants, formalised as executable SymPy/numerical
models and run under shared conditions against IRH v93.1 as reference,
diverge from IRH at six identified points (D1–D6 in
`task12_divergence_table.md`), and in two cases the divergence is IRH's
*silence* (no prediction) rather than a conflicting prediction.
**STATUS: VERIFIED** — 55 checks, all PASS, driver exit 0 (re-run
verified by the parent; shipped `driver_output.txt` byte-identical to
the shipped rerun log).

**Sharpest divergences.**
- **D1 — signature.** The Greensite mechanism predicts Lorentzian
  signature iff $n_{F} > n_{B}$, where IRH predicts nothing — and the
  transfer into IRH FAILS Bartha (no DOF count in a single classical
  scalar substrate).
- **D2 — varying constants.** A toy linear $\alpha$ drift of $1\times10^{-15}$/yr is
  excluded ~$25.6\times$ by the Rosenband 2008 bound $\dot{\alpha}/\alpha$ =
  $(-1.6\pm2.3)\times10^{-17}$/yr, while Dirac $G\propto1/t$ gives Ġ/$G = -7.25\times10^{-11}$/yr.
- **D3 — Ġ/G.** No verified primary-source bound in this run —
  **ABSTAIN**, no verdict on Dirac.
- **D4 — spectral dimension.** CDT flows $1.82\to4.02$ while IRH holds
  D = 4 at all scales (gap ~2.18 at $\sigma\to0$; endpoint disputed, ~2 vs
  ~3/2).
- **D5 — anthropic typicality.** The anthropic account accommodates
  the observed $\Lambda$ under every prior, but its typicality number swings
  ~$80\times$ with the prior (0.0015 uniform vs 0.1204 log-uniform) —
  prediction vs accommodation is the divergence.
- **D6 — $\alpha$.** No rival here derives $\alpha^{-1}$, and neither does IRH.
- **D7 — prerequisite.** Deciding §IX.2 is a prerequisite for any
  signature comparison.

**Grades.** Formal claims G1, G5, G8, $G12 \to **F3** ($two tools; capped —
human gates not run). Physical claims G2, G9, G13, $G14 \to **C$**
$(I1 \to C)$. $G4 (\alpha$ ansatz$) \to **D ($ansatz only)**. G11 (anthropic
typicality$) \to **D ($accommodation, not prediction)**. G3 (triad
relations "derive" c, $\hbar$, $G) \to$ **NOT A DERIVATION** (definitional
identities only). G6/$G7/G10 \to$ ABSTAIN / TRANSFER FAILS (see the
report §7).

**Files.**
`task12_rival_accounts.md` (426 lines, FINAL),
`task12_divergence_table.md` (58 lines, shared-conditions table D1–D7),
`task12_rival_accounts_DRAFT.md` (408 lines — child's verbatim draft,
preserved; the FINAL differs by the assembly re-run verification),
`task12_models/` — 5 executable models (A IRH reference, B signature,
C varying constants, D anthropic, E discrete) + `compare_driver.py` +
`driver_output.txt` (55 [PASS]) + `driver_rerun_2026-11-10.log`
(byte-identical to `driver_output.txt`).

**Replication (from `ws-d-frameworks-rivals/`).**

```sh
$PY task12_models/compare_driver.py   # runs each model as a subprocess; 55 [PASS], 0 [FAIL], exit 0; prints to stdout only, writes no files
```

## 7. Workstream E — cosmology + researcher map (tasks 11, 14, 15)

**Directory:** `ws-e-cosmology-map/`
**Verification standard applied:** bifurcation part verified by two
independent tools (SymPy 1.14.0 exact + python-flint 0.8.0 rigorous
balls, both exit 0; the parent re-ran the FLINT check independently,
rc = 0, values confirmed). Literature parts use deepest-research full
mode. No GCP spend in WS-E (all local, seconds of compute).

### 7.1 Task 11 — simulate cosmological bifurcations

**CLAIM.** Simulate the cosmological bifurcations of the stated IRH
Landau functional, including any expansion-driven cascade.
**STATUS: bifurcation part VERIFIED (two tools); expansion-driven
cascade ABSTAIN; scan fraction and w6 narrowing INCOMPLETE-EVIDENCE.**
**CORRECTION (Hark audit F3, 2026-11-10):** the band-edge values (C4)
had only ONE tool behind them in the package — the flint script's
`fmpq_poly.roots()` returns `[]` for irrational edges. The values were
confirmed after the audit by Hark's arb computation and the parent's
independent SymPy solve (agreeing to <1e-12), so C4 stands at F2 on
SymPy + arb; the package's "two tools" basis for C4 was vacuous as run.

**Headline results (all verified by SymPy + FLINT, except the band
edges — see the C4 correction above).**
- S = 64/141, $\tau = 4/\sqrt{6}$, $q_{4} = 47/8$.
- A\* = 0.077575296339281, F(A\*$) = -0.007632267318990 ($matches the
  manuscript at its stated precision).
- $r_{eff} = 67/625 = 0.1072$, $u_{eff} = 77/50 = 1.54$.
- $r_{c}$,eff = 189728/793125 = 0.2392157604,
  $r_{spin}$,eff = 23716/88125 = 0.2691177305.
- Detuning thresholds refined: branch exists $q_{0}^{2} \in (7.5976, 8.4024)$
  (spinodal); global $\min q_{0}^{2} \in (7.6367, 8.3633) ($coexistence).
- **NEW: homogeneous barrier $F(A_{max}) = 3.858520750506e-05$ at
  $A_{max} = 0.0098005901855419$.**
- Coexistence band edges at $r = -0.35$ are **$[-0.23816, +0.90483]$**, NOT
  the manuscript band edges $(-0.33, +0.03)$ — those are
  sub-pattern-competition edges whose data are not in the text.
- **11.85% scan fraction NOT independently reproducible** (no scan code
  in repo `verification/`, scan definition absent$) \to$
  INCOMPLETE-EVIDENCE.
- **$w_{6}$ narrowing 11.90% $\to 8.47$% NOT re-derivable** $(w_{6}$ term form
  unstated$) \to$ INCOMPLETE-EVIDENCE.
- Barrier vanishes at $r_{eff} = 0$, **$\bar{\psi} \approx -0.1439** ($the repo IX1 brief's
  "$\approx -0.10$" is loose — a minor correction to a repo working document,
  not the manuscript).
- **Expansion-driven cascade ABSTAIN:** the manuscript states no
  cosmic-expansion mechanism (no scale factor / Hubble / Friedmann /
  parameter-driving law), so there is nothing to simulate. Fig. 4 is
  labelled HYPOTHETICAL throughout.

**Grades.**

| claim | grade | basis |
|---|---|---|
| C1–C3, C5–C6 (Landau values, thresholds, barrier, as computed) | C (Track E, I1, F2) | two-tool exact verification; independence is one agent + one pipeline |
| C4. Coexistence band edges at $r=-0.35$: $[-0.23816, +0.90483]$ | C (Track E, I1, F2) | SymPy + arb (Hark) — the package's flint leg printed `[]` (`fmpq_poly.roots()` finds rational roots only); the parent's independent SymPy solve confirms the values to <1e-12 |
| C7. 11.85% band fraction | INCOMPLETE-EVIDENCE (no grade) | scan absent from repo |
| C8. $w_{6}$ narrowing 11.90% $\to 8.47$% | INCOMPLETE-EVIDENCE (no grade) | term form unstated |
| C9. Cosmic expansion drives (r, $\bar{\psi}, q_{0})$ | ABSTAIN (no grade) | no such statement exists in the manuscript |
| C10. What fixes $\bar{\psi}$ / what supplies nucleation (IX.5) | ABSTAIN (no grade) | stated open in the manuscript |

**Files.** `11-bifurcations-report.md`,
`data/bifurcation_compute.py` (SymPy exact),
`data/bifurcation_flint_check.py` (python-flint second tool),
`data/bifurcation_table.json`, `data/bifurcation_values.json`,
`data/make_figures.py`, `figures/fig1_free_energy_curves.png`,
`figures/fig2_phase_diagram.png`, `figures/fig3_barrier_vs_psibar.png`,
`figures/fig4_hypothetical_scenarios.png`.

**Replication.** From `ws-e-cosmology-map/`:

```sh
$PY data/bifurcation_compute.py      # SymPy exact; writes data/bifurcation_values.json
$PY data/bifurcation_flint_check.py  # python-flint; expect exit 0, all values confirmed
$PY data/make_figures.py             # figs 1–4 (fig 4 is HYPOTHETICAL — see the report)
```

Stated functional: N = 24, T = 192, Q = 3384, u = v = 1; $r = -0.35$,
$\bar{\psi} = -0.18$. F(B) = $(r/2)B^{2} - (u\tau/3)B^{3} + (v q_{4}/4)B^{4}$ with $B = A\sqrt{N}$,
$\tau = T/N$^(3/2), $q_{4} = Q/N^{2}$.

### 7.2 Task 14 — map quantum-gravity researchers

**CLAIM.** Map the researchers and approaches closest to IRH on
substrate ontology, selection mechanism, and testable predictions.
**STATUS: MAP COMPLETE.** Synthesis of 73 retrieved papers (3 slices,
63 queries). Every affinity verdict passed or failed through the Bartha
critical-disanalogy gate. **Grade ceiling: Track E C / I1** for the
whole map (cross-domain-discovery skill cap, until a human runs the
source/balance gates). No claim in this report is graded above C.
Cross-domain S5/S6/S7 NOT RUN (reasons stated in the report).

**Headline results.**
- **Verdict: no retrieved approach is close to IRH on all three
  criteria at once.** Closest split by criterion: substrate ontology —
  GFT condensate cosmology (Oriti & Pang 2025; Calcinari et al. 2026;
  passes ontology, fails mechanism); selection mechanism —
  Alexander–McTague / Lifshitz–Petrich pattern-formation lineage (the
  only mechanism-level pass; no spacetime claim); testable predictions
  — Asymptotic Safety strongest (Higgs $\approx 126$ GeV pre-discovery;
  seesaw bound ~$10^{14}$ GeV) but furthest from IRH on ontology.
- OpenAlex volume proxy (broad text-search hits, NOT a field census):
  AS 1,758; LQG 28,665; CDT 22,759; GFT 35,600; Verlinde 1,918;
  analogue 27,786; causal sets 11,485; swampland 2,488.
- **Finding F1 (new, load-bearing caveat): Klein 2001
  (arXiv:cond-mat/0104342) argues Alexander–McTague's BCC solutions are
  unstable** — a caveat on IRH's 3D validation (the manuscript's 3D
  check should be read as "recovers the AM prediction", not "recovers
  an established fact").
- **Finding F2 (new): IRH's selection principle changed between the
  SSRN predecessor (maximal cymatic complexity $\to$ dimension 8) and
  $v93.1 (S = \tau^{2}/q_{4} \to D_{4})$.** The principle is version-dependent.
- **No independent work citing or discussing IRH found** (search-bounded
  absence, INCOMPLETE-EVIDENCE). **No findable Wise Journal revision
  record** (INCOMPLETE-EVIDENCE).
- 8-check rubric: **7/8 pass**; independence is the binding limit.
- Citation corrections applied (grep-verified, 0 remaining occurrences
  of the removed items): BEC Hawking paper = Muñoz de Nova et al. 2019,
  *Nature* 569, 688 (Steinhauer group), not "Steinhauer et al. 2019";
  Barceló et al. = *Living Rev. Relativ.* 29, 2 (2026;
  arXiv:gr-qc/0505065 v4 2024), not a "2011 review"; Edwards & Fauve =
  1993, PRE 47, R788, not "1994 JFM 278, 123"; removed: Weinfurtner
  2019 superradiance, Visser & Weinfurtner, a derived
  $a_{0} \approx 0.8\times10^{-10} m/s^{2}$ value, and unverified pattern-formation
  affiliations.

**Files.** `14-researcher-map-report.md`,
`data/lit-slice-A-asymptotic-safety.md`,
`data/lit-slice-B-emergent-discrete.md`,
`data/lit-slice-C-pattern-irh.md`, `data/make_map_figures.py`,
`figures/fig5_researcher_map.png`, `figures/fig6_openalex_counts.png`.

**Replication.** This task is literature work, not a computation.
Re-run it by re-running the stated queries (63 queries, 3 slices;
listed in the report §2 and the slice files) against the same sources
(OpenAlex + web), re-applying the Bartha gates (§4) and the scorecard
(Table 1, scores 0/1/2 with per-approach justification). The figures
are re-derivable from the scored table alone:

```sh
$PY data/make_map_figures.py   # numpy + matplotlib only; no data beyond the report's Table 1
```

### 7.3 Task 15 — model cosmological signatures

**CLAIM.** Forward-model the gravitational-wave signatures and CMB
power-spectrum modifications predicted by the IRH framework.
**STATUS: EXTRACTION COMPLETE; FORWARD MODEL ABSTAINED. The ABSTAIN
is the central result** — the presupposed stated model does not exist.
Any GW or CMB number produced here would be invented, not derived.

**Headline results.**
- Grep over the 1,638-line manuscript text (with working controls:
  "monopole" 12, "inflation" 1, "$D4/D_{4}$" 83): "gravitational wave" = 0,
  "CMB" / "cosmic microwave" = 0, "photon" = 0, "baryon" = 0,
  "Hubble" / "Friedmann" / "scale factor" = 0; predictions VI.1–VI.7
  contain no GW/CMB item.
- **Null observable grid (IRH = UNSTATED / ABSTAIN on all 11 rows)**
  against verified instrument responses: LVK O1–$O4a \Omega_{GW}(25$ Hz$) \leq$
  $2.8e-9 (\alpha = 0)$, $\leq 2.0e-9 (\alpha = 2/3)$, 95% CL (PRX 16, 041023, 2026);
  LISA $h^{2}\Omega ~1e-12$ at 1e-2 Hz, launch mid-2030s; NANOGrav 15-yr
  $A_{GWB} = 2.4^{+0}\cdot^{7}_{-0}\cdot_{6}e-15$; Planck $2018 n_{s} = 0.9649\pm0.0042$,
  r < 0.10 (Planck alone), < 0.056 (+BK15); BK18 r < 0.036, $\sigma(r)$ =
  0.009 (PRL 127, 151301, 2021); Planck PR4+BK18 r < 0.032; CMB-S4
  design $\sigma(r) < 5e-4$.
- Blockers B1–B6 (no expansion history; dimensional assignment IX.2
  undecided; Einstein equations / TT polarizations unrecovered; no
  nucleation or $\bar{\psi}$ mechanism; no photon/baryon coupling; no
  cosmological initial conditions).
- **No GW number was computed, and none can be, from the stated
  model.** A 9-item requirements list for a future forward model is in
  §5 of the report.
- Grade C (Track E), I1, F2.

**Files.** `15-cosmological-signatures-report.md` (no scripts; the
evidence is the grep counts and the verified instrument table).

**Replication.** Re-run the greps over
`00-programme/IRH_v93_1_source_rebuilt.txt` (the exact commands and
counts are in the report §2) and re-verify the instrument rows against
the cited sources. Reproducing the ABSTAIN means reproducing the zeros.

---

## 8. Cross-cutting results (read these before citing any single task)

### 8.1 The band discrepancy — three workstreams, one open question

The manuscript's 11.85% band fraction does not survive independent
recomputation in any of the three forms it takes:

| form | result |
|---|---|
| WS-A task 3, W1 band, stated windows | 11.60% $(\delta=0, w6=0) \to 8.36$% (w6=0.2); hex-only 12.94% $\to 9.68$%. 11.85% bracketed, not reproduced; window unstated. |
| WS-C task 7, 24-mode global-min band at $r = -0.35$ | $\bar{\psi} \in (-0.235, -0.125)$; manuscript $(-0.33, +0.03)$ is the union over quench depths; +0.03 edge UNVERIFIED. |
| WS-E task 11, scan fraction | 11.85% NOT independently reproducible: no scan code in repo `verification/`, scan definition absent. $w_{6}$ narrowing NOT re-derivable (term form unstated). |
| WS-E task 11, coexistence edges at $r = -0.35$ | $[-0.23816, +0.90483]$, NOT $(-0.33, +0.03)$ — those are sub-pattern-competition edges whose data are not in the text. |

WS-A task 3 and WS-C task 7 agree with each other (the measured slice
is narrower than the quoted union); WS-E task 11 adds that the scan
itself cannot be reproduced from the repo as it stands. **Which value
is canonical (11.85% vs 11.90%) remains Brandon's call** — nothing in
this package resolves it, and the no-note IRH recompile (33 pp.,
delivered 2026-11-10 separately) no longer flags the inconsistency
up front. **Competitor-set gap (Hark audit F1 side-result):** the
WS-C band's competitor set {24-mode, 6-mode, disordered} omits
stripes; a stripe-like state appeared at $\bar{\psi} = +0.10 ($one Hark run,
Fexc $-0.048943$, metastable not global-minimum — not re-run by the
parent). The audit's claim that "the round-1 review had $\approx [-0.235$,
$-0.14]$ with stripes/A2/A3 included" could NOT be verified — no such
band appears in the 2026-10-30 deepest-research report, the v5 test
report, the repo CORE.md, or the manuscript.

### 8.2 The Model B Hermitian artifact — found twice, independently

WS-A (droplet runs) and WS-C (attractor runs) independently found the
same defect: the shipped-style Model B update grows an anti-Hermitian
roundoff component $\times1.0142$/step and reaches NaN by ~6000 steps
(WS-C: blows up at t = 27.5). Fix: per-step Hermitian symmetrisation /
projection — an exact no-op in exact arithmetic. Both workstreams'
Model B results in this package use the fixed stepper. **Any future
Model B work must use the fixed stepper; the unfixed update diverges.**

### 8.3 Findings that touch the manuscript itself

- **Klein (2001) caveat (WS-E F1):** the manuscript's 3D validation
  recovers the Alexander–McTague BCC result, but Klein argues AM's BCC
  solutions are unstable. The 3D check should be read as "recovers the
  AM prediction", not "recovers an established fact". Open question for
  Brandon: acknowledge the caveat in the manuscript?
- **Selection-principle change (WS-E F2):** the SSRN predecessor
  selected by maximal cymatic complexity $(\to$ dimension 8); v93.1 selects
  by $S = \tau^{2}/q_{4} (\to D_{4})$. The principle is version-dependent. Open
  question for Brandon: acknowledge the change in the manuscript's
  history?
- **Minor correction to a repo working document (not the manuscript):**
  the repo IX1 brief's "$\approx -0.10$" for the barrier-vanishing $\bar{\psi}$ is loose;
  the exact value is $\bar{\psi} \approx -0.1439 ($WS-E task 11, WS-A task 4 §II.9).
- **Printed dispersion relation (7) is wrong — manuscript erratum
  (WS-D task 10, §6.3).** The printed formula doubles the $\Sigma$ term and
  misplaces $\mu^{2}$; the EOM-derived formula is correct on three internal
  checks plus the manuscript's own §III.2 expansion. The CFL bound
  computed from it is VERIFIED. One printed equation needs an erratum;
  nothing else changes. Open question for Brandon: file the erratum?
- **§III.3 envelope validity table does not reproduce (WS-D task 10,
  §6.3 — UNVERIFIED, not FAILED).** The table'$s \Deltat$, carrier $\theta ($or $\mu)$,
  direction, and error definition are unstated; no natural reading
  reproduces the five entries, and the 133% zone-edge entry is
  unreachable under the natural reading. The VI.3 summary boundary
  (<1% for $a_{0}$|k| ≲ 0.3) survives the recomputation. What would settle
  it: the author stating the conditions used for the table.

### 8.4 What this package does NOT change

No IRH grade moves beyond the failed-as-written claims listed in §9 —
which now include the WS-A task-5 / WS-C finding 6–7 "stable attractor"
claims (FAILED as written, Hark audit F1) and the WS-$A A/B \to C$
regrade (Hark audit §6).
The $D_{4}$ selection (S = 64/141), $E_{6}$ via 2T/McKay, SO(8) exclusion, and
the INPUT status of the three generations are untouched. The
11.85%/11.90% question, the Klein caveat, and the selection-principle
change are flagged for Brandon's call, not decided here. WS-D adds two
manuscript-facing items to the register (§9) — the printed (7) erratum
and the §III.3 envelope table (UNVERIFIED) — and confirms the
manuscript's own downgrades $(\alpha$ ansatz $174\sigma$ from CODATA; $\xi_{2}$ retraction
factor 2); no IRH grade moves.

---

## 9. FAILED / NOT RUN / INCOMPLETE-EVIDENCE register (everything that did not verify)

| item | verdict | falsifier / reason |
|---|---|---|
| WS-A task 5 hex6/fcc12 "stable attractors" | FAILED as written | unperturbed starts stay put, but a 0.2% transverse perturbation grows hex$6 \to$ full24 (5/5) and fcc$12 \to$ full24 (4/4) at $\bar{\psi}=-0.18$ — invariant-subspace artefact (Hark audit F1; confirmed by the parent's own transverse run). Corrected: at $\bar{\psi}=-0.18$ the 24-mode is the only attractor seen from perturbed starts; hex6/fcc12 are saddles. |
| WS-C findings 6–7 ("24-mode is a local minimum outside the band"; "both patterns are local minima at both $\bar{\psi}$") | FAILED as written | same falsifier as above; at $\bar{\psi}=0$ the seeded 24-mode goes to 6-mode under perturbation and at $\bar{\psi}=+0.10$ to a 2-mode stripe-like state (Hark; not re-run by the parent). At $\bar{\psi}=0$ hex6 is genuinely stable. |
| WS-E C4 "two tools" basis (band edges) | RECORD CORRECTED (values stand) | package flint leg printed `[]` (`fmpq_poly.roots()` finds rational roots only); values confirmed by Hark arb + parent SymPy solve to <1e-12. Grade F2 on SymPy + arb. |
| WS-C task2d/make_figures (T=0.5/1.0 rows) | PROVENANCE GAP (numbers stand) | task2d runs T=5 only and overwrites the CSV; make_figures then crashes (IndexError line 88). Shipped T=0.5/1.0 rows match Hark's regeneration exactly; $p \approx 0.95$ stands. |
| WS-A task-1 JSON extra fields | PROVENANCE GAP (numbers stand) | shipped JSON carries `n_distinct_positions`/`max_multiplicity` the shipped script does not write; came from another script revision. |
| Triad `lock` metric for partial patterns | DEFECT (minor) | `d4model.analyze` averages cos S over all 32 triads incl. roundoff modes; platform-dependent for partial patterns (hex6 0.304/0.455 vs shipped 1.000). Fix: active triads only. |
| WS-D task 10 D5 (printed dispersion relation (7), §III.1) | FAILED as printed | EOM-derived formula has $\Sigma ($not $2\Sigma)$ and $\mu^{2}$ outside the bracket; three internal checks + the manuscript's own §III.2 expansion agree with the derived formula. CFL bound VERIFIED. Erratum, not refutation. |
| WS-D task 10 D17 (§III.3 envelope validity table) | UNVERIFIED | table'$s \Deltat$, $\theta ($or $\mu)$, direction, error definition unstated; computed 1.67e-5 / 4.17e-4 / 3.75e-3 / 4.11% / 36.3% vs table 4e-5 / 0.1% / 1.0% / 11% / 133%; zone-edge 133% unreachable under the natural reading. VI.3 boundary (<1% for $a_{0}$\|k\| ≲ 0.3) survives. |
| WS-D task 10 D18 (R = 2589) | ABSTAIN | no derivation inputs in the source; manuscript itself downgrades it. |
| WS-D task 9 C7 (no rival derives $\alpha)$ | C scoped / UNVERIFIED universal | verified for surveyed sources only; a universal negative cannot be proved over all literature. |
| WS-D task 12 D3 (Ġ/G bound) | ABSTAIN | no verified primary-source Ġ/G constraint in this run; no verdict on Dirac varying-G. |
| WS-D task 12 G6/G7 (Greensite mechanism / transfer into IRH) | ABSTAIN / TRANSFER FAILS | full mechanism not recovered; transfer FAILS Bartha (no DOF count in a single classical scalar). |
| WS-D task 8/9 transfers ("substrate dynamics $\Rightarrow$ Einstein equations"; Jacobson $\Rightarrow$ IRH) | TRANSFER FAILS | Bartha S4: critical features in the Negative Analogy. Confirms IRH v93.1's own retraction. |
| WS-D task 9 F4 ("IRH'$s E_{6}$ identification derives coupling values / $\alpha$") | FAILED | no breaking pattern, no RG running in IRH (§IX.4). |
| WS-D task 9 F5 ("anthropic reasoning explains $\alpha$ or IRH's tunings") | FAILED / NOT SUPPORTED | ensemble unobserved; not in the manuscript. |
| WS-D task 10/12 triad relations "derive" c, $\hbar$, G | NOT A DERIVATION | definitional identities only (change of variables); manuscript itself states the circle. |
| WS-C C1.2 (dynamic account predicts full 24-mode ONLY inside the band) | FAILED as written | Q2 noise quench at $\bar{\psi}_{0} = -0.18 ($inside the quoted band) reaches 6/24 — the register's own falsifier. Basin-qualified version CONFIRMED under C1.3. |
| WS-C C2.2 (discretization error decreases with N and dt) | FAILED as written | Fixed-point error is 0 at every ladder point (no decrease to measure). Corrected claim (transient error decreases, $p \approx 0.95)$ confirmed. |
| WS-C P4 (same content as C2.2, premise form) | FAILED as written | Same falsifier as C2.2. |
| WS-E C7 (11.85% band fraction) | INCOMPLETE-EVIDENCE | No scan code in repo `verification/`; scan definition absent. |
| WS-$E C8 (w_{6}$ narrowing 11.90% $\to 8.47$%) | INCOMPLETE-EVIDENCE | $w_{6}$ term form unstated in the manuscript. |
| WS-E C9 (cosmic expansion drives parameters) | ABSTAIN | No expansion mechanism stated in the manuscript. |
| WS-E C10 (what fixes $\bar{\psi}$ / nucleation, IX.5) | ABSTAIN | Stated open in the manuscript. |
| WS-E task 15 (GW + CMB forward model) | ABSTAIN | No stated GW/CMB model; all 11 observable rows UNSTATED. |
| WS-C C1.6 Hoy [40] LJ-MD leg | NOT RUN | Hoy LJ-MD not re-simulated (abstention A5). |
| WS-C Lean re-verification | NOT RUN | Abstention; no Lean work in this programme. |
| WS-C Barenblatt classification of the band edge | NOT ESTABLISHED | Abstention. |
| WS-C band claims beyond the $r = -0.35$ slice | NOT CLAIMED | No claim beyond the measured slice. |
| WS-A task 3 manuscript 11.85% reproduced | C (not reproduced) | Bracketed (11.60% / 12.94%), window unstated. |
| WS-A task 4 thin-wall $R_{c} = 7.38$, $\DeltaF$\* = 37.2 | C (approximation shown to fail) | $\xi = 8.64 > R_{c}$; thick-walled. Reported as the failed approximation. |
| WS-E task 14 cross-domain S5/S6/S7 | NOT RUN | Reasons stated in the task-14 report. |
| WS-E task 14: independent work citing IRH; Wise Journal revision record | INCOMPLETE-EVIDENCE (search-bounded absence) | Not found in retrieval; absence is search-bounded, not proven. |

---

## 10. Full replication order (whole package, clean run)

```sh
# 0. Environment
PY=~/miniconda3/envs/jacobian-conjecture-2d/bin/python
unzip d4-work-2026-11-10.zip
cd d4-work-2026-11-10

# 1. WS-A — model check first, then tasks in order (all from ws-a-core-computations/)
cd ws-a-core-computations
$PY checks/check_model.py        # expect: ALL CHECKS PASSED, exit 0
$PY task1_projections.py
$PY task2_anisotropy.py
$PY task3_band.py
$PY task4_thinwall.py
$PY task4_droplet_runs.py
$PY task5_basin.py
cd ..

# 2. WS-C — exact checks first, then split drivers in order (all from ws-c-substrate-convergence/)
cd ws-c-substrate-convergence
$PY code/exact_checks.py          # 29 statements, 31 PASS lines, exit 0
$PY code/task1a_quenches.py       # then 1b, then 1c (1c reads 1a's .npy)
$PY code/task1b_quenches.py
$PY code/task1c_attractors.py
$PY code/task2a_attractor_ladder.py
$PY code/task2b_quench_ladder.py
$PY code/task2c_sensitivity_modelform.py
$PY code/task2d_transient.py     # WARNING (Hark audit F4): overwrites results/task2_transient.csv with T=5-only rows
$PY code/make_figures.py         # WARNING: CRASHES after the task2d re-run (IndexError line 88) — the shipped CSV's T=0.5/1.0 rows came from an unshipped run; see §5.2
cd ..

# 3. WS-D — derivations first, then the rival models (all from ws-d-frameworks-rivals/)
cd ws-d-frameworks-rivals
$PY task10_scripts/task10_sympy_checks.py    # 45 PASS, 0 FAIL, exit 0
$PY task10_scripts/task10_numeric_checks.py  # 33 PASS, 0 FAIL, exit 0
$PY task12_models/compare_driver.py          # 55 [PASS], 0 [FAIL], exit 0; prints to stdout, writes no files
cd ..   # tasks 8 + 9 are literature work: replication = the stated queries and primary-source checks in the reports

# 4. WS-E — bifurcation compute, FLINT cross-check, figures (all from ws-e-cosmology-map/)
cd ws-e-cosmology-map
$PY data/bifurcation_compute.py
$PY data/bifurcation_flint_check.py   # expect exit 0; NOTE: it prints `coexistence band edges (flint): []` — expected (fmpq_poly.roots() finds rational roots only); the edges are confirmed by SymPy + arb, not by this leg (Hark audit F3)
$PY data/make_figures.py
$PY data/make_map_figures.py
cd ..
```

**Expected wall-clock:** WS-C ~1 hour; WS-A tens of minutes (the
6000-step Model B runs are ~36 s each; task 5 is 14 runs, task 4 part D
is 8 runs); WS-D seconds (task 10 + task 12 driver); WS-E seconds. All
local CPU. **Do not delete the shipped CSVs/JSONs before comparing:** the clean-run outputs should match the
shipped tables to the quoted precision (WS-A task 5 log ends
`TASK5 EXIT:0`; WS-C exact checks print 31 PASS; WS-E FLINT check
prints all values confirmed, plus the expected `coexistence band edges
(flint): []` line — see §7.1). WS-C drivers append to CSVs — for a
clean replication, move the shipped `results/*.csv` aside first and
diff afterwards. WS-A and WS-E scripts overwrite their outputs in
place.

## 11. Pitfalls and runtime notes (learned the hard way, in-session)

1. **Use the conda env Python** (`~/miniconda3/envs/jacobian-conjecture-2d/bin/python`).
   System `python3` lacks the pinned packages.
2. **Working directories matter.** WS-A scripts use relative
   `tables/` and `figures/` paths — run from
   `ws-a-core-computations/`. WS-E scripts use relative `data/` paths —
   run from `ws-e-cosmology-map/`. WS-C scripts resolve paths from
   `__file__` and can run from anywhere, but the documented pattern is
   from `ws-c-substrate-convergence/`.
3. **The Model B stepper MUST be the fixed one** (§4.6 / §8.2). The
   unfixed update diverges to NaN by ~6000 steps.
4. **Runtime restarts happen.** Background exec sessions go "unknown"
   after completion and a run can be lost mid-run (WS-A task 5 lost its
   first launch after 1 run; WS-C lost a seed-5 run). Scripts that save
   incrementally survive this; single-shot scripts do not. If a run
   dies, re-run it — WS-A task 5 and the WS-C split drivers resume from
   saved rows; WS-C seed 5 was re-run standalone and its row is in the
   CSV.
5. **Harness "failures" with exit 0 are not failures.** Several runs
   in-session reported `output_drain_timeout` / `unknown` status while
   the process itself exited 0 and wrote its outputs. **Trust the log
   files and the output files, not the harness status line.**
6. **Do not use the single-driver scripts for replication.**
   `ws-c-substrate-convergence/code/task1_substrate_models.py` and
   `code/task2_convergence.py` died without output in-session; the
   split drivers (1a/1b/1c, 2a/2b/2c/2d) with incremental CSV appends
   are the reliable pattern.
7. **WS-C `sim7_annealed_only.py` has an absolute path** to the local
   IRH repo clone (see §5.2). Repoint it on another machine.
8. **WS-A task 3 brentq pitfall:** brentq on $F_{min}$ fails (flat above
   coexistence); use F at the large stationary root.
9. **WS-A task 4 shooting discriminator:** the sign of A at large r,
   not "trapped at $A_{small}$".
10. **Fourier indices must be unscaled root labels** (K2 = 8, not 32)
    and sub-pattern labels must come from `SUBPATTERN_LABELS`
    (WS-A task 5); both were real bugs in-session.
11. **Singular is not needed here**, but if you touch WS-B's scripts:
    close stdin, never `continue` in a for-loop, parenthesise `a^b/c`.
12. **Triad `lock` is ill-defined for partial patterns** (Hark audit
    F2): `d4model.analyze` averages cos S over all 32 triads, including
    modes at roundoff amplitude whose phases are noise. Shipped hex6
    lock 1.000 vs rerun 0.304 (WS-C A5: 1.000 vs 0.455) is a metric
    artefact, not a physics difference. Restrict to triads with all
    three modes active (`active_lock` gives 1.000 for hex6/fcc12/full).
    No load-bearing conclusion rests on the sub-pattern lock value
    except the task-5 §2 phrase "locked triads".
13. **WS-C `make_figures.py` crashes after a `task2d` re-run** (Hark
    audit F4): see §5.2 / §10. The shipped `task2_transient.csv` T=0.5
    and T=1.0 rows came from an unshipped run; the numbers are verified
    (regenerated values match exactly) but the clean-run order as
    written does not reproduce fig3.
14. **WS-D scripts run from the workstream root** (`ws-d-frameworks-rivals/`);
    the task-12 driver runs each model as a subprocess and prints to
    stdout — it writes no files, so there is nothing to diff except the
    55 [PASS] lines against `driver_output.txt`. The three `*_DRAFT.md`
    files are the children's verbatim drafts, preserved; the FINAL
    reports differ by the assembly corrections (task $8: 1,034 \to 1,086$
    lines; task $9: 402 \to 414$; task $12: 408 \to 426)$.
15. **WS-D task 10's counts were corrected in assembly** (46 SymPy +
    32 numeric $\to 45 + 33)$: the `def check` line had been counted as a
    check, and the G3-f call sat outside its `for` loop so only the
    third dt value was checked. Both are fixed in the shipped scripts;
    the re-run counts (45 / 33) are the true ones.

## 12. Open questions for Brandon (arising from this package)

1. **11.85% vs 11.90%** — which band value is canonical? (Still open;
   three workstreams now bracket but do not reproduce 11.85%.)
2. **Klein (2001) caveat** — acknowledge in the manuscript that the 3D
   validation recovers a contested AM result?
3. **Selection-principle change** — acknowledge the SSRN $\to v93.1$
   change (maximal cymatic complexity $\to S = \tau^{2}/q_{4})$ in the manuscript's
   history?
4. **Future forward model** — attempt the 9-item requirements list in
   WS-E task 15 §5 in a future IRH version? (New manuscript work, not
   a follow-up to this package.)
5. **WS-C follow-ups (costed, not run):** 20+ quench seeds to bound the
   24/24-from-noise rate (0/5 so far); longer quenches / annealing to
   test whether the 2-/8-mode outcomes are transient; full-precision
   re-measurement of the unprojected shipped sim$6 \bar{\psi}$ drift to settle
   the 8.3e-17 reference value.
6. **WS-A follow-up (costed, not run):** larger-box droplet run
   $(L = 2\pi, N = 32)$ to test whether the box threshold moves toward the
   ODE value — a GCP-scale job needing a named cap.
7. **WS-A task 3 vs WS-C task 7:** resolve the quoted-edge discrepancy
   (measured slice vs manuscript's quoted union-over-r band) with the
   full $(\bar{\psi}, r)$ recomputation — WS-A task 3's map is the tool for it.
8. **Printed dispersion relation (7) erratum (WS-D task 10):** file the
   erratum (replace $[2\Sigma(1-\cos) + \mu^{2}]$ by $[\Sigma(1-\cos)]$ with the $\mu^{2}$ term
   outside the bracket), or leave the printed equation as is?
9. **§III.3 envelope table (WS-D task 10):** the author would need to
   state $\Deltat$, $\theta ($or $\mu)$, direction, and error definition for the table to
   be re-checkable — is that worth pursuing with the manuscript's
   author (i.e. you)?
10. **WS-D F3 caps:** the Hark regrade $(F3\toF2$ on two routes) was not
    applied to WS-D, which was not in the audited package. Should the
    same two-route logic lift any WS-D F3 (task 12 G1/G5/G8/G12) to F2?

## 13. Provenance

- Programme brief: `00-programme/PROGRAMME_BRIEF.md` (6,245 bytes).
- Manuscript text: `00-programme/IRH_v93_1_source_rebuilt.txt`
  (1,638 lines), extracted from the Nov 5 source-rebuild PDF
  (34 pp., sha256 `cebc3b6f010ed9c059129b4b0ff2c9e3a8ea858e74adc68c3e7fd7d9f34affa8`).
- Reports were parent-verified on disk (file existence, line counts,
  grep spot checks) and, for WS-E task 11, by an independent re-run of
  the FLINT check (rc = 0); for WS-B (not in this package), by log
  tallies (112 PASS, 0 FAIL).
- Zip built 2026-11-10 evening CST by the parent agent from the
  workstream directories as produced; `__pycache__/` excluded; no
  files renamed, moved, or edited.
- **Amendment 2026-11-11 ~01:30 CST (WS-D added):** WS-D (tasks 8, 9,
  10, 12) completed after the first package build and was folded in:
  a new §6 in the guide; the `ws-d-frameworks-rivals/` directory added
  whole (including the three children's verbatim `*_DRAFT.md` files);
  the register (§9), replication order (§10), pitfalls (§11), open
  questions (§12), and §8.3 updated. The parent re-ran the WS-D
  executable checks in a scratch copy (task 10: 45 + 33 PASS, 0 FAIL;
  task 12 driver: 55 PASS, 0 FAIL; driver output identical to the
  shipped rerun log) and read the four reports. The zip was rebuilt
  from the corrected guide (142 files, integrity-tested). The
  workstream files themselves were NOT edited.
