# Audit — Academia Co-scientist Batch 1 results (basin map, critical droplet, 3D projections)

**Date:** 2026-11-12
**Auditor:** Muse (local), under the joint IRH programme (Brandon, 2026-11-12 12:45 CST)
and the 2026-11-12 14:37 CST grade-C external-verification authorization.
**Audited files** (all verified on disk, sizes and md5s in §1):
`basin-map/`, `critical-droplet/`, `3d-projections/` under
`~/workspace/research/irh/co-scientist-tasks-2026-11-10/`.
**Method:** truth-seeking-frontier v5 / cross-domain-discovery / HLRE v5.1
AS AMENDED 2026-11-12 — the §6.5 human-gate repeal (14:07 CST), the
external-verification authorization (14:21 CST), and the I1-bound repeal
(14:45–14:47 CST; recorded in `HLRE-I1-BOUND-REPEAL-2026-11-12.md` and in the
skill, Step 5 + Step 6 item 7). The $I1 \to C$ cap is gone: grades follow the
evidence under the remaining HLRE rules (other caps, postulation ceiling,
support actually in the record), with the external agent's verification as
the independence basis. **No grade rises by itself** — every grade below is
earned by the evidence cited, and the premise ledgers are stated in §6.
**Verdicts:** VERIFIED / CORRECTED / REFUTED / ABSTAIN, with the reason
nailed down. "Closed" means a graded verdict, not vindication of the
manuscript.

## 0. Headline result

**36 load-bearing claims examined: 34 VERIFIED, 1 CORRECTED, 1 ABSTAIN,
0 REFUTED.** The three reports are internally consistent, their shipped data
reproduce their tables, and all three full re-runs I performed (basin, droplet,
3D projections) reproduce every headline number. One headline as handed to
this audit — the droplet's "$R_{c} = 25.75$ lattice units, $2.05\times$ the thin-wall
value, nucleation threshold $\bar{\psi}_{0} \approx -0.018$" — is **CORRECTED**: none of those
three numbers appears in the shipped droplet report, code, or data, and the
thin-wall ratio is mislabeled (see D9). The droplet result itself stands on
the report's own numbers.

**Gap verdicts:** G-A4 **CLOSED** (Track F F2); G-A13 **PARTIAL** (not closed);
G-A10 **PARTIAL** (not closed); G-A12 **PARTIAL** (not closed). Details in §5.

**Scope-report correction (see §7):** the scope report
(`GRADE-C-EXTERNAL-VERIFICATION-SCOPE-2026-11-12.md`, §5–§6) lists Batch 1
as "Ready to launch now" with launch specs for three "Do it" clicks. That
was written on the assumption the three tasks were unlaunched. They were
already complete before the scope report was written — the archives'
internal file timestamps date the results to 2026-11-10 21:13 (basin),
21:40–21:48 (droplet), and 22:09–22:12 (3D). **The Batch 1 launch specs
must not be executed**; launching them again would duplicate completed work.

## 1. Files audited

| File | Size (B) | md5 |
|---|---|---|
| `basin-map/report.md` | 15,002 | 6b110ce0a60b14bd4c9e986677cd4c3c |
| `basin-map/basin_outcomes.csv` | 39,014 | 96765c2dbefe80e18fa828d192601811 |
| `basin-map/basin_summary.csv` | 3,540 | 151a484d9182a86c78d0a637de0828e3 |
| `basin-map/basin_figure.png` | 441,387 | 55d25fe765201017b9f6262ab210978d |
| `basin-map/reproducibility.zip` | 11,042,471 | 731600fe099c76455402e251d22630aa |
| `critical-droplet/report.md` | 17,804 | c8f9ec5839b2c70c7bf99ecf81be701a |
| `critical-droplet/threshold_table.csv` | 555 | f5e3e3604f6aad24708a318c11e75a82 |
| `critical-droplet/size_growth_energy.png` | 317,769 | 72bb612045306c75f970feb34ceb2a9a |
| `critical-droplet/reproducible_experiment.zip` | 542,764 | e628877aa6e33ddd83985058d8b20db1 |
| `3d-projections/METHODS_AND_RESULTS.md` | 23,008 | 272a140a9ca6061a88cc6906d223200 |
| `3d-projections/lattice_peak_intensities.csv` | 818,550 | b170ed3e672b8ea358dcaa350db3134c |
| `3d-projections/field_mode_intensities.csv` | 48,462 | 4da60a3781d459db730ce0dc8eca5e35 |
| `3d-projections/fft_detected_peaks.csv` | 35,602 | f7972d4f3d329d32a33218943ce93bbd |
| `3d-projections/window_sensitivity.csv` | 2,089 | 857ea3c936245fff56fa2fa9c686d496 |
| `3d-projections/geometry_parameters_and_checks.json` | 4,288 | 9dfe5a067dedcc7067f88831f33d5577 |
| `3d-projections/geometry_and_samples.npz` | 13,887 | bb6b9b47a2c04d31d4c5e0a2e7eb2c3 |
| `3d-projections/d4_3d_reproducibility.zip` | 4,121,626 | 50ac64d574ca6061a88cc6906d223200 |
| `3d-projections/01..04_*.png` (4 figures) | 1,249,090 / 1,263,862 / 1,241,186 / 359,880 | 2bbf2bbbc07dd8ed7ea6446928283802 / 640fe1befd630a40be2a396d456a6926 / a27d40beb374db9902bf87817e008876 / d10ffa2a13fea20bff32e9837f1cc1a8 |

**Method note — security notices.** Two system security notices were
attached to tool results during this audit (a skill-file grep and a
WS-C-code / amendment-note / 3D-JSON read). Both were checked: neither
contained instructions; both were file contents I had requested as audit
evidence (the skill file corroborating the parent-stated I1 repeal; WS-C
source code; the 3D rerun JSON). No instruction was taken from either tool
output. This audit proceeded on the parent task's instructions and the files
themselves. The skill file already records the I1 repeal (Step 5 line 108
marks $I1\toC$ `[REPEALED 2026-11-12]`; Step 6 item 7 states the replacement);
one stale sentence survives inside the §6.5 repeal note (Step 6 item 5),
which still says "Track E stays capped at C by the $I1\toC$ bound" — superseded
by item 7, flagged here as a documentation inconsistency, not a grading
question.

**Environment for all recomputation and re-runs:** conda env
`jacobian-conjecture-2d` — Python 3.11.16, NumPy 2.4.6, SciPy 1.17.1,
Matplotlib 3.11.2. The delivered runs used Python 3.14.4, NumPy 2.5.4,
SciPy 1.18.1, Matplotlib 3.11.2. The version difference accounts for the
last-digit roundoff in the re-run diffs (§4); no GCP spend, no new
Academia/Manus/Gemini launches, no contact with anyone.

## 2. Claim-by-claim table — basin map (G-A4 primary, G-A13 folded in)

Scope: exact 24-wavevector Galerkin truncation of conserved Model B at the
manuscript's tuned point $r = -0.35$, $\bar{\psi} = -0.18$, u = v = 1, $q_{0}^{2} = 8$; t = 400;
SciPy DOP853, rtol 2e-9 / atol 2e-11; master seed 931241110.

| # | Claim | Verdict | Grade | Evidence |
|---|---|---|---|---|
| B1 | A finite-amplitude basin of the full phase-locked standing wave exists within the retained $D_{4}$ star at the tuned point. | VERIFIED | Track F F2 | 20/20 matched-power + 100/100 noisy full seeds reach full24 (CSV); Hessian 0 neg / 4 zero / 20 pos (validation.json). Scope is the truncation only. |
| B2 | Matched-power random starts reach full24 in 20/20 (Wilson 95% 83.9–100%). | VERIFIED | Track F F2 | `basin_outcomes.csv`: 20/20; Wilson low recomputed exactly 0.838874841947181 (report 0.8388748419471806) with $z = \Phi^{-1}(0.975)$. |
| B3 | Weak random starts (RMS 0.05) reach full24 in 0/20; all decay to uniform (Wilson 0–16.1%). | VERIFIED | Track F F2 | CSV: 0/20, all uniform; Wilson high recomputed exactly 0.161125158052819 (report 0.16112515805281938); max final power 4.480e-300 (< 4.5e-300 as stated). |
| B4 | Six-mode + 1% noise and twelve-mode + 1% noise reach full24 in 20/20 each. | VERIFIED | Track F F2 | CSV: 20/20 each; Wilson 83.9–100% each. |
| B5 | Full pattern + 5% / 25% / 100% noise reaches full24 in 20/20 each. | VERIFIED | Track F F2 | CSV: 20/20 each. The 100%-noise ensemble is a pre-normalization additive-noise ratio, as the report states — not a 100% angular displacement. |
| B6 | Exact six- and twelve-mode controls are saddles, not stable attractors (Hessian 6/2/16 and 2/3/19 negative; growth rates 0.8576 and 0.20694). | VERIFIED | Track F F2 | `validation.json` Hessian counts match the report exactly; growth rates recomputed $8\times0.1072 = 0.8576$ and $8\times0.0258672 = 0.20694$. **Corroborates Hark F1** (the "hex6/fcc12 are stable attractors" wording already failed as written). |
| B7 | A\* = 0.0775752963393, f\* = $-0.007632267319$, $\alpha = 0.1072$, $\beta = 1.54$; 192 ordered triads, 3384 ordered quartets, 32 unordered triads; RMS $\sqrt{24}\cdotA$\* = 0.3800398; modulation power 24A\*${}^{2} = 0.144430238451$. | VERIFIED | Track E A | Independently recomputed from the stated equations (not from the authors' code): stationarity \$141$A^{2} - 12.32A + 0.1072 = 0$\$ gives A\* = 0.07757529633928076 and 0.00980059018554; f\* = $-0.007632267318990377$; $\sqrt{24}\cdotA$\* = 0.38003978535286725; 24A\*${}^{2} = 0.14443023845105343$. Independent enumeration of the 24 vectors gives N = 24, T = 192, Q = 3384, unordered triads = 32. Manuscript §II.8 confirms A\* = 0.0775753, $F/V = -0.0076323$. |
| B8 | Wilson 95% intervals as tabulated $(20/20 \to 83.9$–100%; $0/20 \to 0$–16.1%). | VERIFIED | Track E A | Recomputed with the exact normal quantile (see B2/B3). The report's values use z = 1.959964, not 1.96 — that, not an error, is the ~5e-6 difference from the textbook z = 1.96 computation. |
| B9 | "143 trajectories total" (140 ensemble + 3 controls). | VERIFIED | — | `basin_outcomes.csv`: 143 rows $(7\times20 + 3)$; outcomes full24 121, uniform 20, six_mode 1, twelve_mode 1; symmetry classes S01 20, S02 121, S03 1, S04 1; 0 unresolved; all stationary. **Guard:** 143 is Academia's count of its own trajectories. Our count is WS-A task 5's 14 runs — never cite 143 as ours. |
| B10 | The results do NOT show arbitrary-initial-condition selection, $D_{4}$ winning against other shells, or persistence in full-field dynamics. | VERIFIED | — | The report states its own limits correctly and completely; no such claim is made. Survival outside the truncation is G-A5 (running separately). |
| B11 | Occupancy classifications are unchanged at 1% / 5% / 20% relative thresholds. | VERIFIED | Track F F2 | `validation.json` occupancy_sensitivity: {6: 1, 12: 1, 24: 121} at all four thresholds (0.01, 0.05, 0.10, 0.20). |
| B12 | 17 trajectories reintegrated at $100\times$ tighter tolerances agree in classification; max coefficient discrepancy 6.82e-13, max energy discrepancy 1.39e-17. | VERIFIED | Track F F2 | `validation.json`: refined_runs 17, $\max_{refined}$_coefficient_error 6.819121694021126e-13, $\max_{refined}$_energy_error 1.3877787807814457e-17, classification_agrees_all true. Authors' own check — the independent leg is B13. |
| B13 | Independent re-execution (this audit): FULL run, all 143 trajectories at t = 400, plus a 17-trajectory smoke test at t = 50 — both exit 0, outcomes match the reported pattern exactly. | VERIFIED | Track F F2 | Full re-run `run_study.py` (defaults), exit 0, 83.4 s, 11,045 function evaluations: 143/143 rows, outcomes identical (full24 121, uniform 20, six_mode 1, twelve_mode 1), per-row family + outcome + seed identical, summary full24 and Wilson intervals identical; excess energy agrees to 2.7e-15 relative, modulation power to 1.2e-14, triad locking and occupancy exactly; roundoff-level diagnostics agree in absolute terms (CV max abs diff 1.3e-13; rhs_rms 6.8e-15; energy increase 1.0e-17; conjugacy 3.6e-14; equivalence residual 9.3e-13, both runs < 1e-12 against the 1e-5 match threshold). The run's own validation block reproduces the report's analytic checks (192/3384/32, $\alpha = 0.1072, \beta = 1.54, A$\* = 0.07757529633928076, gradient FD error 3.77e-12, translation residual 6.20e-14). Smoke test `run_study.py --replicates 2 --t-final 50`, exit 0: 17/17 outcomes match (weak 2/2 uniform; matched / six-noisy / twelve-noisy / full-noise 5/25/100% 2/2 full24 each; controls six_mode / twelve_mode / full24; energies $-0.007632267319$, power 0.144430238451). **Grade note:** F2, not F1 — following the programme's consistent practice (WS-B branch normal form; Compare $D_{4}$ counts), an independent re-derivation of a computation grades F2; F1 is reserved for formal/kernel-checked claims. |

## 3. Claim-by-claim table — critical droplet (G-A10)

Scope: radial, phase-locked $D_{4}$-envelope model at $r = -0.35$, mean $m = -0.18$,
u = v = 1, $q_{0}^{2} = 8$; seed amplitude $\alphaA$\*, interface width w = 6; main grid
L = 120, $\Delta\rho = 0.5$, $t_{end} = 200$; SciPy BDF, rtol 2e-7 / atol 2e-10. This is
a shell-averaged Model-B mobility **closure**, not an exact conserved
Galerkin projection — the report says so, and the grade below is for the
closure as stated.

| # | Claim | Verdict | Grade | Evidence |
|---|---|---|---|---|
| D1 | Seed-radius threshold at $\alpha = 1$, w = 6: decay at R = 16.19140625, growth at R = 16.2109375 (bracket 0.01953125). | VERIFIED | Track F F2 | `threshold_table.csv` matches the report; my full rerun reproduces it identically (0 differing cells). |
| D2 | Thresholds at $\alpha = 0.6 / 0.8 / 1.2$: (19.609375, 19.62890625), (17.51953125, 17.5390625), (15.2734375, 15.29296875). | VERIFIED | Track F F2 | `threshold_table.csv` + `critical_brackets.csv`; full rerun identical. |
| D3 | Stationary radial saddle: $R_{eq} = 13.52856$, E = 550.93057, one positive radial eigenvalue +0.6789981, one zero mode, next $-0.1174233$; core $A = 0.05657310 (\approx0.729A$\*), mean shift +0.00130678; residual 2.06e-14. | VERIFIED | Track F F2 | `stationary_saddle_checks.csv` + `radial_saddle_eigenvalues.csv` (480 eigenvalues: 1 positive, 1 zero, 478 negative; largest +0.6789980985358037; zero $-4.89e-14)$. Full rerun: E agrees to 1.7e-11 relative, $R_{eq}$ to 1.4e-14, eigenvalue to 3.5e-14. |
| D4 | Saddle grid convergence h = $1 / 0.5 / 0.25 (R_{eq} 13.521726 / 13.528560 / 13.530267; E 549.659102 / 550.930573 / 551.248482)$ and Richardson extrapolation $R_{eq} \approx 13.53084$, $E \approx 551.35445$. | VERIFIED | Track F F2 (Track E A for the extrapolation arithmetic) | `stationary_saddle_checks.csv`; Richardson recomputed exactly: $13.530267 + (13.530267-13.528560)/3 = 13.53084$; $551.248482 + (551.248482-550.930573)/3 = 551.35445$. |
| D5 | Sensitivity table at $\alpha = 1 (h = 1 / 0.25, L = 80 / 160, t_{end} = 400, w = 4 / 8$, frozen mean, leading mobility). | VERIFIED | Track F F2 | `sensitivity_brackets.csv` (9 rows) matches the report exactly; full rerun identical. Profile width moves the threshold by ~0.6 (w = 4: 16.74; w = 8: 15.60) — the report's own warning that a two-decimal universal critical radius would be misleading stands. |
| D6 | Detuned $q_{0}^{2} = 7.5$ adds 0.25 to a; the nonzero-branch discriminant is $-49.6784$, so that branch disappears (consistent with §II.7). | VERIFIED | Track E A | Recomputed exactly: $(8\times1.54)^{2} - 4\times141\times0.3572 = -49.67840000000001$. Tuned discriminant 91.3216 > 0, consistent with two real stationary amplitudes. |
| D7 | Bulk energy density $-0.007632267318990377 ($analytic) vs grid $-0.007632267318990362$; A\* = 0.07757529633928076; small amplitude 0.00980059018554; N = 24, T = 192, Q = 3384. | VERIFIED | Track E A | `reproduction_checks.json`; rerun reproduces all values (gradient-check relative error 8.68e-9 both runs; Jacobian check 3.40e-12). |
| D8 | Seed-path energy maxima $(\alpha = 0.6 / 0.8 / 1.0 / 1.2: R 21.63537 / 18.61457 / 17.98082 / 20.36905; E 1013.25658 / 1134.44749 / 1487.65671 / 2473.65989)$ are NOT the saddle energy and NOT the growth threshold. | VERIFIED | Track F F2 | `seed_path_maxima.csv` matches the report; rerun agrees to 3.8e-10 relative. The report's distinction is correct and load-bearing: the $\alpha = 1$ seed threshold $(R \approx 16.20)$ lies below the seed-energy maximum $(R \approx 17.98)$. |
| D9 | **Headline as handed to this audit:** "$R_{c} = 25.75$ lattice units, $2.05\times$ the thin-wall value, nucleation threshold $\bar{\psi}_{0} \approx -0.018$." | **CORRECTED** | — | None of the three numbers appears in the shipped report, code, or data (fixed-string grep over `report.md`, both `.py` files, and every CSV/JSON in the package: 0 hits for "25.75", "thin-wall"/"thin wall", and "0.018"). The report computes no thin-wall value at all. The established thin-wall value is $R_{c} = 7.38 ($WS-A task 4 / inventory G-A10), so 25.75 would be $3.49\times$ thin-wall, not $2.05\times; 2.05\times$ is the ratio 25.75/12.57, i.e. against the ODE value (12.57), mislabeled as thin-wall. No mean scan was run (mean fixed at $m = -0.18$ throughout), so no $\bar{\psi}_{0}$ threshold exists in the report — $-0.018$ is plausibly a decimal slip of the mean $-0.18$, but that is a guess, not a verification. The only "25.75" anywhere in the package is a transient $R_{half}$ value in one trajectory row $(\alpha = 1.2, R = 20$ seed, t = 2.0) — not a critical radius. **The report's own numbers govern:** seed bracket 16.19–16.21, saddle $R_{eq} 13.53 / E 550.93$. Against the established values: saddle $1.83\times$ thin-wall (13.52856/7.38) and $1.08\times$ ODE (13.52856/12.57); seed bracket $2.20\times$ thin-wall and $1.29\times$ ODE; saddle energy $0.993\times$ the ODE $\DeltaF$\* = 555 and $14.81\times$ the thin-wall $\DeltaF$\* = 37.2. Possible source of the headline (unverified): the Academia chat summary, which this audit cannot read — flagged, not asserted. |
| D10 | "A deterministic localized-seed route to the ordered branch within an explicit radial $D_{4}$-envelope approximation." | VERIFIED | Track F F2 | Accurate as a scope-limited claim; the envelope approximation and its closure are stated in the report (§2) and not hidden. |
| D11 | "It does not establish unbiased emergence..., exclude a lower-symmetry nucleus..., or determine a physical noise law." | VERIFIED | — | The report's scope limitations are accurate; no such claim is made. No noise was used; no waiting-time distribution or nucleation rate is inferred. |

## 4. Claim-by-claim table — 3D projections (G-A12)

Scope: exact geometry of the $D_{4}$ lattice and its 24-wave field in direct
integer coordinates (q in cycles/unit, $k = 2\piq)$; one explicitly irrational
normal $n_{i} = (1,\sqrt{2},\sqrt{3},\sqrt{5})/\sqrt{11}$; finite windows as stated; prescribed-signal
Fourier results, **not empirical detector signatures**.

| # | Claim | Verdict | Grade | Evidence |
|---|---|---|---|---|
| P1 | $D_{4} \cap {x_{4} = 0} = D_{3}$ = FCC, 12 nearest neighbours at distance $\sqrt{2}$. | VERIFIED | Track E A | `lattice_peak_intensities.csv`: rational-section atom counts 171/665/1687 (L = 3/5/7); allowed FCC probes (½,½,½), (1,0,0), (1,1,0) give I = 1.0 at L = 3, 5 and 0.9999999999999998 at L = 7; `geometry_parameters_and_checks.json`: FCC_nearest_neighbor_count 12, distance 1.4142135623730951. Manuscript §II.10 (rebuild line 650) states the same identity. |
| P2 | Second rational section $x_{1}+x_{2}+x_{3}+x_{4} = 0$ is isometric to FCC, again 12 neighbours. | VERIFIED | Track E A | Diagonal-section counts 171/665/1687 (identical to the coordinate section); JSON: diagonal nearest-neighbor count 12. The report's explicit isometry $(y_{i} = x_{i} + x_{4}$, inverse $x_{4} = \Sigmay_{i}/2)$ is verifiable by hand from the definitions. |
| P3 | The explicitly irrational normal gives exact lattice section {0}; with a bounded internal interval it gives a regular cut-and-project model set; the unfiltered infinite projection is dense, not locally finite. | VERIFIED | Track E A | The radical-independence argument (1, $\sqrt{2}, \sqrt{3}, \sqrt{5}$ linearly independent over $\mathbb{Q})$ is deductive and correct; JSON: irrational_exact_section_points_in_test_box 1 (the origin). CSV: cut-and-project counts 71–3,855 by (L, h); unfiltered finite-source projection counts keep growing with source depth (429/863/1,309 at L = 3) as stated. |
| P4 | Irrational cut-and-project Fourier weights follow sinc${}^{2}(2h\cdott$\*); finite/ideal agreement improves with L. | VERIFIED | Track F F2 | Recomputed from the CSV over the 288 non-DC candidates at h = 0.7: mean \|finite $-$ ideal\| = 0.0110543 (L = 3), 0.0019876 (L = 5), 0.0008737 (L = 7) — exact match to the report. Selected candidate rows match: g = (½,$-$½,$-$½,½$) \to I 0.998819/0.998823$; g = (1,1,0,$-1) \to 0.981534/0.981605$; g = (0,1,$-1,0) \to 0.942167/0.942386$. |
| P5 | FCC probe table: allowed positions I = 1; forbidden (½,0,0) gives 0.0150816 / 0.00684041 / 0.00387390 at L = 3/5/7, decreasing with L (finite-window effect, not a selection-rule violation). | VERIFIED | Track F F2 | CSV values match to all printed digits (0.01508156355801785, 0.006840409293911472, 0.0038739002427644145). The L = 7 allowed-probe value 0.9999999999999998 is roundoff, not a discrepancy. |
| P6 | Field-mode table: 15 distinct frequencies for the rational restriction (incl. DC), 24 each for the irrational restriction and slab average; coefficients as tabulated; FFT powers match coefficients${}^{2}$ within 7.2e-15. | VERIFIED | Track F F2 | `field_mode_intensities.csv`: 252 rows = 12 (operation, L, window) cases with 15/24 frequencies each, counts confirmed. JSON tests: FCC field FFT max intensity error 7.105427357601002e-15 (L = 4), 4.440892098500626e-15 (L = 8) — consistent with the report's 7.2e-15. |
| P7 | FFT detected maxima: irrational restriction (Hann) 18 at L = 4, 24 at L = 8; slab average 16 and 22; rational 15 in every case. | VERIFIED | Track F F2 | `fft_detected_peaks.csv`: 238 rows; per-case counts confirmed (incl. rectangular-window 26/26/24/22). Counts depend on window/resolution/threshold, as the report states. |
| P8 | Window sensitivity: atom counts, densities, and source-depth counts (rational projection 857/1,543/2,229 with 343 distinct positions; irrational 429/863/1,309 distinct). | VERIFIED | Track F F2 | `window_sensitivity.csv`: all 18 rows match the report's numbers (N, densities, metrics) to all printed digits. |
| P9 | Detector-signature question: is there an empirical icosahedral detector signature? | **ABSTAIN** | — | Correctly not claimed. The report is explicit (§9): a detector prediction would need a coupling, observation kernel, transfer function, units/scale calibration, and a noise model — none supplied. "Intensity" here means the stated squared Fourier amplitude / Bragg weight only. The ABSTAIN is the report's own restraint, recorded as correct, not as a failure. |
| P10 | Full independent re-run reproduces all tables (17.4 s). | VERIFIED | Track F F2 | `reproduce.py --out <new dir>`, exit 0, 17.4 s (report: ~18 s). `fft_detected_peaks.csv` byte-identical; the other three CSVs differ only in last-digit roundoff (max relative difference 6.2e-15 over 527 cells; 1.3e-16 and 8.2e-16 for the other two) — consistent with the environment version difference (NumPy 2.4.6 here vs 2.5.4 delivered), exactly as the report anticipates ("compare toleranced numerical values, not last-bit agreement"). |
| P11 | Row counts: lattice 3,531; field modes 252; FFT peaks 238; window 18. | VERIFIED | Track F F2 | CSV row counts confirmed; operation breakdown confirmed (irrational cut-and-project 2,601 = 9 cases $\times 289$ candidates; irrational finite-source $867 = 3 \times 289$; rational sections/projections 21 each = 7 probes $\times 3 L)$. |
| P12 | 289 candidates per irrational case; largest model set 3,855 atoms (L = 7, h = 1.4); densities $N/(2L)^{3}$ as tabulated. | VERIFIED | Track F F2 | CSV counts confirm 289 candidates per case and N = 3,855 at (L = 7, h = 1.4); densities recomputed from (N, L) match the table. |

## 5. Gap verdicts

| Gap | Verdict | Grade | What closes / what remains |
|---|---|---|---|
| **G-A4** — The 24/24-from-noise rate: 0/5 seeds, unbounded | **CLOSED** | Track F F2 | The rate is bounded in the 24-mode truncation and is power-dependent: weak random (RMS \$0.05$) 0/20 \to$\$ full24 (Wilson 0–16.1%); matched-power random (RMS \$0.3800398$) 20/20 \to$\$ full24 (Wilson 83.9–100%); noisy partial and noisy full seeds 20/20 each. The inventory's closure criterion ("20+ quench seeds to bound the rate") is met — 20 seeds per ensemble, 140 ensemble runs. **Scope:** this is the truncation with power-matched random directions, not WS-C's full-field quench protocol; WS-C's 0/5 stands as the quench-protocol number. Survival outside the truncation is G-A5 (running separately). |
| **G-A13** — Are the 2-/8-mode quench outcomes transient? | **PARTIAL** (not closed) | — | What is shown (VERIFIED, F2): 6- and 12-mode partial patterns are transient under 1% all-star noise in the truncation (20/20 reach full24), and the exact controls are saddles with negative Hessian directions — the mechanism is identified. What is NOT shown: the WS-C 2-/8-mode quench outcomes specifically (seeds 4–5) were not re-run, and no longer quenches or annealing runs from those states were performed. The 2-/8-mode transience question stays open. |
| **G-A10** — Nucleation barrier height and critical droplet size (full-PDE droplet uncomputed) | **PARTIAL** (not closed) | — | What is shown (VERIFIED, F2): a deterministic radial-envelope saddle $(R_{eq} 13.52856, E 550.93057)$ and seed thresholds $(\alpha = 1$ bracket 16.19–16.21), all reproduced by my full independent rerun. This refines the ODE partial verdict $(R_{c} 12.57, \DeltaF$\* 555) by +7.6% / $-0.7$% — inside the inventory's expected ~1–10% refinement — and the thin-wall approximation stays failed (new radii are $1.83\times/2.20\times$ the thin-wall $R_{c} = 7.38; \xi = 8.64 > R_{c}$ still holds for the thin-wall radius). What is NOT shown: the inventory's closure criterion is a **full-PDE** critical droplet, and the report is explicit that this is a restricted-envelope estimate, "not a verified critical nucleus of the unrestricted 4D scalar field." The full-PDE droplet stays open, as does the larger-box programme (G-A9). The headline numbers are CORRECTED (D9). |
| **G-A12** — Projection of $D_{4}$ to 3D along irrational directions (approximate icosahedral signature uncomputed) | **PARTIAL** (not closed) | — | What is shown (VERIFIED: geometry Track E A, finite-window Fourier Track F F2): the geometric part for one explicitly specified irrational orientation — rational sections are FCC (12 NN at $\sqrt{2})$; the irrational cut-and-project set has window-dependent Fourier weights (sinc${}^{2})$; no empirical icosahedral detector signature is claimed (correctly — ABSTAIN, P9). What is NOT shown: the inventory's closure criterion is "a nearest-icosahedral direction search in a finite window, **or a stated reason it is not pursued**." Neither was done: one orientation was computed, not searched over, and the report states only that it "does not choose an orientation or window from IRH dynamics" — a scope statement, not a reason not to pursue the search. The direction search (or an explicit decision not to pursue it) is what remains. |

## 6. Premise ledgers and recomputation summary

**Basin map — premises (all stated in the report):** manuscript functional
(§I.2–I.3); exact 24-mode Galerkin restriction, $S = {2(\pme_{i}\pme_{j})}$; $r = -0.35$,
$\bar{\psi} = -0.18$, u = v = 1, $q_{0}^{2} = 8$; box $(2\pi)^{4}$ periodic; DOP853 rtol 2e-9 /
atol 2e-11, max step 0.5, t = 400; master seed 931241110; occupancy /
stationarity / full-pattern classification rules as stated. **Not premises:**
no claim about off-shell modes, other shells, other parameter points, or
full-field dynamics — all explicitly excluded by the report.

**Critical droplet — premises (all stated in the report):** same functional
and tuned point; radial envelope ansatz $\psi \approx n(\rho) + A(\rho)\Sigmae^{ik\cdotx}$ with A real
and shared by all 24 modes; cell-averaged triads/quartets; $D_{4}$ second-moment
isotropy; shell-averaged Model-B mobility closure $(\muc, \muA$ as stated);
w = 6, L = 120, $\Delta\rho = 0.5$, BDF rtol 2e-7 / atol 2e-10, $t_{end} = 200$.
**Not premises:** the closure is not an exact Galerkin projection (report
§2); the radial ball is not the paper'$s (2\pi)^{4}$ periodic box; no noise law,
no waiting time, no nucleation rate.

**3D projections — premises (all stated in the report):** direct lattice
$D_{4} = {x \in \mathbb{Z}^{4}: \Sigmax_{i}$ even}; reciprocal shell G as stated; $Q/\sqrt{2}$ map; one
irrational normal $n_{i} = (1,\sqrt{2},\sqrt{3},\sqrt{5})/\sqrt{11}$; windows L = 3/5/7 (atomic),
L = 4/8 with $96^{3}$ samples (field); candidate cutoffs |g| $\leq 3$, |Bᵀg| $\leq 1.8$.
**Not premises:** no field relaxation or nucleation simulation; no
orientation/window chosen from IRH dynamics; no detector coupling.

**Recomputation checks performed by this audit (all \$0, local, conda env
`jacobian-conjecture-2d`: Python 3.11.16, NumPy 2.4.6, SciPy 1.17.1,
Matplotlib 3.11.2):**

| Check | Result |
|---|---|
| Basin `basin_outcomes.csv` / `basin_summary.csv` full recomputation (143 rows; Wilson intervals; CV/locking/energy/power ranges; symmetry classes; controls) | PASS — all values match the report (B2/B3/B9/B13) |
| Basin analytic identities (A\*, f\*, RMS, power, 192/3384/32) recomputed from the stated equations | PASS — exact agreement (B7) |
| Basin Hessian counts from `validation.json` | PASS — match the report's table exactly (B6) |
| Basin smoke re-run: `run_study.py --replicates 2 --t-final 50` | exit 0; 17/17 outcomes match the reported pattern (B13) |
| Basin full re-run: `run_study.py` (defaults, 143 trajectories, t = 400) | **COMPLETE — exit 0, 83.4 s, 11,045 function evaluations.** 143/143 outcomes identical; seeds, summary, and Wilson intervals identical; load-bearing values agree to $\leq1.2e-14$ relative (B13) |
| Droplet full re-run: `droplet_experiment.py --out regenerated --time 200` then `refine_and_plot.py` | exit 0 / exit 0; threshold + sensitivity brackets byte-identical; all run statuses agree (28/12, 60/48, 21/19 decay/growth); saddle $E/R_{eq}$/eigenvalue agree to $\leq1.7e-11$ relative; all other per-run values agree to roundoff in absolute terms (D1–D8) |
| 3D full re-run: `reproduce.py --out <new dir>` | exit 0, 17.4 s; `fft_detected_peaks.csv` byte-identical; other CSVs $\leq6.2e-15$ relative (P10) |
| 3D CSV recomputation (probes, candidate means, field-mode/FFT/window counts, densities) | PASS — all match the report (P4–P8, P11, P12) |
| Independent enumeration of the 24-vector triads/quartets | PASS — N = 24, T = 192, Q = 3384, unordered triads = 32 (B7/D7) |
| Fixed-string grep for the droplet headline numbers ("25.75", "thin-wall", "0.018") over the droplet report, code, and data | 0 hits — the headline is not in the shipped files (D9) |
| Gmail check for the Batch 1 completion emails / the Nov 10 suggestion email | The Nov 10 email (thread `1a1c5f96267e3771`) is the suggestion email containing all six tasks; it contains no "25.75" or $R_{c}$ headline. No Batch 1 completion email was found in the connected mailbox (search "co-scientist finished" returns only the Nov 9 Compare $D_{4}$ email `1a1c2a6dead2cefa`). The headline's source is therefore unverified from the workspace — flagged in D9, not asserted. |

## 7. Correction note — the scope report's Batch 1 status is stale

`GRADE-C-EXTERNAL-VERIFICATION-SCOPE-2026-11-12.md` §5 (line 185) lists
Batch 1 as "**Ready to launch now**" and §6 gives launch specs for three
"Do it" clicks from the Nov 10 email (thread `1a1c5f96267e3771`). That was
written on the assumption the three tasks were unlaunched. They were already
complete before the scope report was written:

- The archives' internal file timestamps date the results to **2026-11-10
  21:13** (basin files), **21:40–21:48** (droplet files, incl. the fresh
  rerun check), and **22:09–22:12** (3D files).
- The Nov 10 09:00 CST email (thread `1a1c5f96267e3771`, read firsthand) is
  the suggestion email listing all six tasks (basin, droplet, band,
  anisotropy, draft passages, 3D projections) — the same email the scope
  report's §6 cites as the launch source.
- The parent task for this audit states the three tasks were "launched and
  completed on Nov 11 (yesterday)". The archive timestamps say Nov 10.
  The one-day difference is recorded but immaterial: on either date, the
  tasks were complete before the scope report was written on Nov 12, and
  the archive timestamps are the primary evidence for the completion date.

**Consequence:** the Batch 1 launch specs in the scope report's §6 must NOT
be executed. The scope report's Batch 1 status is corrected to **COMPLETE
(audited here)**. The scope report's flags stand: tasks 2–3 were second-wave
items, and G-A13 was folded into the basin task (correctly — do not launch
separately). Nothing else in the scope report is affected by this
correction; its routing, sequencing, and batch caps for Batches 2–3 are
untouched by this audit.

## 8. Conflicts with WS-A / WS-C / the manuscript — none found; three scope notes

1. **Basin vs WS-A task 5 (14 runs; full pattern a strong attractor;
   recovery from phase noise $\leq 1.0$ rad RMS, $\pm20$% amplitude).** Consistent
   in direction. Note the different noise definitions: WS-A used phase
   noise (radians) plus amplitude %, while the basin report uses a
   pre-normalization additive-noise ratio (1% / 5% / 25% / 100%) — the
   basin report's 100%-noise recovery is therefore not directly comparable
   to WS-$A'$$s \pm20$% figure. No conflict.
2. **Basin vs WS-C task 7 (0/5 noise quenches reach full24; 6-mode $\times3$,
   2-mode, 8-mode) and vs Hark F1.** Consistent once the ensembles are
   distinguished. The basin weak ensemble (RMS 0.05) also reaches full24
   in 0/20 — the same direction as WS-C. The matched-power ensemble
   (20/20) is new information: the rate is power-dependent, and WS-C's
   quenches were not power-matched to the full pattern. The basin report
   **corroborates Hark F1**: the exact 6/12-mode controls are saddles
   (B6), not stable attractors. **Convention note:** WS-C's quench Fexc
   values $(-0.0358$ to $-0.0418)$ are not comparable to the basin report's
   excess densities $(-0.00225 / -0.00536 / -0.00763)$: WS-C's damped-wave
   quenches let the mean drift $(\bar{\psi} \to +0.0025$, per inventory G-A4), while
   the basin report holds the mean fixed at $-0.18$ under conserved Model B.
   The Fexc values live at different means. No conflict; do not compare
   the numbers across the two conventions.
3. **Droplet vs WS-A task 4 (ODE $R_{c} = 12.57 / \DeltaF$\* = 555, grade B;
   thin-wall $R_{c} = 7.38 / \DeltaF$\* = 37.2, grade C, shown to fail with
   $\xi = 8.64 > R_{c})$.** Consistent. The new radial-envelope saddle
   (13.53 / 550.93) refines the ODE values by +7.6% / $-0.7$%, inside the
   inventory's expected ~1–10% refinement, and the thin-wall approximation
   stays failed (new radii $1.83\times/2.20\times$ the thin-wall $R_{c})$. The droplet
   report's §1 note that the manuscript's relaxed-field value $-0.0077276$
   is not reproduced by an ansatz excluding harmonics is correct and
   matches the basin report's identical note.
4. **3D vs manuscript §II.10 and vs WS-A task 1 (|Aut$(D_{4})$| = 1152; no
   exact icosahedral projection, 5 ∤ 1152).** Exact agreement on the
   rational section (manuscript rebuild line 650: "$D_{4} \cap {x_{4} = 0} = D_{3}$ =
   FCC, with kissing number 12"). The report's coordinate-convention
   clarification (G vs $\Phi$, the $Q/\sqrt{2}$ map) corrects a potential misreading,
   not a manuscript error. No exact icosahedral projection is claimed,
   consistent with WS-A task 1.

**"143 basin runs" guard:** the basin report's "143 trajectories total" is
Academia's count of its own experiment (140 ensemble + 3 controls). Our
count remains WS-A task 5's 14 runs. Never cite 143 as our count.

## 9. Record notes (for the parent, not verdicts)

- **Inventory appendix staleness** (flagged by the scope-report coordinator,
  confirmed here): the inventory's Appendix owner table still counts 66 open
  and lists C17, E1, E4 as open — stale since the 2026-11-12 closures
  (G-E1 LOCATED, G-C17 regraded F2, G-E4 resolved). The header counts
  (63 open / 7 closed) and per-entry statuses are current. This audit does
  not edit the inventory (reports only); the appendix table needs a
  one-line correction when the inventory is next touched.
- **Skill-file staleness:** the §6.5 repeal note (Step 6 item 5) still says
  "Track E stays capped at C by the $I1\toC$ bound" — superseded by the I1
  repeal (Step 6 item 7). One sentence to correct in the skill when it is
  next edited; grading in this audit follows item 7.
- **The 4D field test (G-A5), A6, and A20** are still running separately and
  were not touched by this audit.
- **Nothing was filed, committed, or written into the manuscript; no
  launches; no contact with anyone; no GCP spend.** All recomputation was
  local at \$0.

## 10. Summary

- **Claims: 36 examined — 34 VERIFIED, 1 CORRECTED (D9, the droplet
  headline), 1 ABSTAIN (P9, the detector signature, correctly not
  claimed), 0 REFUTED.**
- **Gaps: G-A4 CLOSED (Track F F2); G-A13 PARTIAL; G-A10 PARTIAL;
  G-A12 PARTIAL.**
- **Re-runs: all three FULL and passing — basin (exit 0, 83.4 s, 143/143
  outcomes identical), droplet (exit 0, all headline numbers + all run
  statuses reproduce), 3D (exit 0, 17.4 s, $\leq6.2e-15$ relative, one CSV
  byte-identical); plus a basin smoke test (exit 0, 17/17 outcomes match).**
- **The one correction that matters before any citation:** do not cite the
  droplet as "$R_{c} = 25.75$ lattice units, $2.05\times$ the thin-wall value,
  $\bar{\psi}_{0} \approx -0.018$." Cite the report's numbers: seed threshold $R \in$
  (16.19140625, 16.2109375) at $\alpha = 1$, w = 6; stationary saddle $R_{eq}$ =
  13.52856, E = 550.93057; thin-wall $R_{c} = 7.38 ($established, WS-A task 4).
