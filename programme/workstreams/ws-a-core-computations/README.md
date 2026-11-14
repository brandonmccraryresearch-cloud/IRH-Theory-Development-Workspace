# Workstream A — Core computations (Co-scientist tasks 1–5)

Shared model: `d4model.py` (24-mode D4 standing wave, Landau functional,
conserved Model B dynamics; parameters exactly as in IRH v93.1).
Model check: `checks/check_model.py` — **ALL CHECKS PASSED, exit 0**
(re-run after the stepper fix, 2026-11-10).

## Reports (CLAIM + STATUS at top; HLRE grades per narrow claim inside)

| task | report | headline result |
|---|---|---|
| 1. 3D projections | `task1_report.md` | No exact icosahedral projection (5 ∤ 1152); e4 projection is $Z^{3}$, not FCC; rational periodic vs irrational aperiodic (split Bragg peaks) |
| 2. Sixth-moment anisotropy | `task2_report.md` | M6 = 60\|k\|${}^{2}\Sigmak_{i}^{4} - 48\Sigmak_{i}^{6}$; $\min 12 (\langle100\rangle,\langle111\rangle)$, $\max 18 (\langle110\rangle)$, mean 15; $\pm20$% signature |
| 3. Stability band | `task3_report.md` | W1 band 11.60% $(\delta=0,w6=0) \to 8.36$% (w6=0.2); detuning shifts band by $\delta^{2}$; $\delta=0.5$ kills the branch at the operating point only |
| 4. Critical droplet | `task4_report.md` | ODE $R_{c} = 12.57$, $\DeltaF* = 555 ($thick-walled; thin-wall 7.38/37.2 fails); box threshold: only R=0.6/A* decays |
| 5. Basin of full24 | `task5_report.md` | Full pattern recovers from $\delta\phi \leq 1.0$ rad, $\pm20$% amp; hex6 and fcc12 are stable traps; sq4/sq8 and noise decay |

## Code

- `d4model.py` — shared module (includes the Hermitian-symmetry fix in
  `ModelB.step`; see task4_report.md §6 for the diagnosis).
- `task1_projections.py`, `task2_anisotropy.py`, `task3_band.py`,
  `task4_thinwall.py`, `task4_droplet_runs.py`, `task5_basin.py`
- `checks/check_model.py`, `checks/check_model.log`

## Figures (`figures/`) and tables (`tables/`)

- Task 1: `task1_projection_scatter.png`, `task1_structure_factor.png`,
  `task1_wave_slice.png`; `task1_projections.json`, `task1_slice_peaks.csv`,
  `task1_bragg.csv`
- Task 2: `task2_path.png`, `task2_disk.png`; `task2_moment_values.csv`,
  `task2_critical_points.csv`, `task2_summary.json`
- Task 3: `task3_phasemap.png`, `task3_band_heatmap.png`,
  `task3_boundaries.png`; `task3_band.csv`, `task3_band.json`,
  `task3_boundaries.csv`, `task3_winner_W1.npy`, `task3_winF_W1.npy`
- Task 4: `task4_droplet.png`; `task4_thinwall.json`,
  `task4_ode_profile.npz`, `task4_droplet_runs.json`
- Task 5: `task5_basin.png`; `task5_basin.json`

## Bugs found and fixed during checking (all in the reports)

1. Fourier indices must be the unscaled root labels (K2 = 8, not 32).
2. FFT-convolution index for H; triples route for H (negation-closed only).
3. Aut(D4) generator attempt (384) replaced by Gram enumeration (1152).
4. Task 3: tri3 (Q = 0) NaN minima (vectorised formula) and unphysical
   deep minimum at w6 > 0 — tri3 excluded from the competitor family.
5. Task 3/4: brentq on $F_{min}$ fails (flat above coexistence) — use
   F at the large stationary root.
6. Task 4: shooting discriminator is the sign of A at large r, not
   "trapped at $A_{small}$".
7. **Model B stepper: anti-Hermitian component grows $\times1.0142$/step from
   roundoff and reaches NaN by ~6000 steps** — fixed by enforcing
   Hermitian symmetry each step (in `d4model.ModelB.step`).
8. Task 5: scaled vs unscaled sub-pattern labels for Fourier seeding —
   use `SUBPATTERN_LABELS`.

## Rules observed

No repo commits, no manuscript edits, no filing. Local compute only;
no GCP spend. lean-build-4 untouched. No Gemini grader calls.
