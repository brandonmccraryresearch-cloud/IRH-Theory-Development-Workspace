# Four-dimensional field test of $D_{4}$ formation

## Result and scope

**Completed: 18 dealiased 4D field trajectories at $18^{4}$ collocation points, plus six numerical refinements, including three $28^{4}$ trajectories.** Every integration reached the shared final time t=200. These are spatial Fourier–Galerkin **fields**, not a 24-mode restriction: the main field has 6,560 independent real nonzero Fourier degrees of freedom; the largest completed refinement has 28,560.

Both broadband random ensembles reached uniform in all three replicates, including starts with the prior basin study’s matched modulation RMS. All nine perturbed six-, twelve- and full-pattern starts reached stationary full-24, phase-locked states. The three shell-random matched-power bridge starts also reached the full state. Thus patterned recovery persists when off-shell modes are admitted, but the prior shell-only matched-random result does **not** transfer to broadband random fields with the same total RMS. This small, tuned, finite-box pilot is not evidence for $D_{4}$ formation from arbitrary random fields.

The main full-state excess energy is **-0.007726209285**. The K=6 spatial refinements give **-0.007727623601**, versus the exact one-shell value **$-0.007632267319$**. Harmonic relaxation lowers the energy by about **1.249%** relative to the truncated full branch. This is close to the manuscript’s reported relaxed $-0.0077276$, without treating that agreement as an independent basin or stability proof.

## Outcomes

| Initial family | n | Stationary full 24 | Uniform | Other/unresolved | Initial $D_{4}$ power fraction | Same-projection truncated full 24 |
|---|---:|---:|---:|---:|---:|---:|
| Broadband random, RMS 0.05 | 3 | 0 | 3 | 0 | 0.0017–0.0046 | 0 |
| Broadband random, RMS matched | 3 | 0 | 3 | 0 | 0.0017–0.0046 | 0 |
| Six-mode seed + 1% broadband noise | 3 | 3 | 0 | 0 | 0.9999–0.9999 | 3 |
| Twelve-mode seed + 1% broadband noise | 3 | 3 | 0 | 0 | 0.9999–0.9999 | 3 |
| Full seed + 25% broadband noise | 3 | 3 | 0 | 0 | 0.9413–0.9416 | 3 |
| Shell-random, matched RMS (bridge) | 3 | 3 | 0 | 0 | 1.0000–1.0000 | 3 |

Counts describe these specified starts only; n=3 is not a meaningful precision estimate of a general basin probability. The last column uses **each field’s actual initial $D_{4}$ projection without re-normalization**, evolved under the supplied exact truncated solver. It does not substitute the old shell-random ensemble for a broadband field.

![Field diagnostics](field_trajectories.png)

All lines are individual replicates, not uncertainty intervals. Phase locking and shell fraction are undefined and omitted after the uniform power threshold is crossed. Fractional shell concentration during overall decay does not indicate pattern formation. The off-shell panel uses absolute power for this reason.

## Functional, discretization and computational bound

The source is the supplied v93.1 PDF, §§I.2–I.3 and II.6–II.9, together with the prior basin report, source and parameter manifest. Source-file SHA-256 hashes are recorded in `parameters.json`. No manuscript simulation source was assumed.

On the periodic box $[0,2\pi]^{4}$, with $\phi=\psi-\bar{\psi}$ and $\bar{\psi}=-0.18$, the fixed-mean excess energy is

f = ½ $\Sigma_{k} [\alpha+(8-$|k|${}^{2})^{2}]$|$\hat{\phi}_{k}$|${}^{2} - \beta$〈$\phi^{3}$〉/3 + 〈$\phi^{4}$〉/4,

where $\alpha=r-2u\bar{\psi}+3v\bar{\psi}^{2}=0.1072$, $\beta=u-3v\bar{\psi}=1.54$, $r=-0.35$ and u=v=1. The zero mode of $\phi$ is fixed to zero. Dynamics is

$\partialt \hat{\phi}_{k} = -$|k|${}^{2} {[\alpha+(8-$|k|${}^{2})^{2}]\hat{\phi}_{k} - \beta P(\phi^{2})$̂${}_{k} + P(\phi^{3})$̂${}_{k}}$.

The mobility is one. Fourier coefficients use the normalized convention $\phi(x)=\Sigma\hat{\phi}_{k}\exp($ik$\cdotx)$. Energy is **excess density F/V**, not absolute F and not the uniform baseline.

| Setting | Main ensemble | Spatial check |
|---|---|---|
| Periodic collocation/evaluation mesh | $18^{4} = 104,976$ real points | $28^{4} = 614,656$ real points |
| Independent retained wavevectors | All integer k with |$k_{i}$|$\leq4$, excluding zero | All integer k with |$k_{i}$|$\leq6$, excluding zero |
| Real dynamical degrees of freedom | $9^{4}-1 = 6,560$ | $13^{4}-1 = 28,560$ |
| Nonlinear projection | Sharp tensor Fourier cutoff, no filtering inside it | Same rule |
| Cubic dealiasing | N=18 > 4K=16 | N=28 > 4K=24 |
| Grid spacing | $2\pi/18 = 0.349066$ | $2\pi/28 = 0.224399$ |
| Samples per axial $k_{i}=2$ period | 9 | 14 |
| Samples per shortest retained axial period | 4.5 for $k_{i}=4$ | 4.67 for $k_{i}=6$ |
| Time horizon | 200 | 200 |
| Maximum timestep | 0.1 | 0.1 |

For a cubic nonlinearity, **N>4K** ensures that a product frequency up to 3K cannot alias into a retained frequency $\leqK$. The same inequality makes the degree-four energy quadrature exact for the retained band. This is a stricter rule than a quadratic 2/3 cutoff. The zero mode is not overwritten by a nonlinear update: its Model B mobility is zero, and $\hat{\phi}_{0}$ is explicitly fixed.

The main domain admits the complete 24-wavevector shell |k|${}^{2}=8$, the 64-mode integer shell |k|${}^{2}=7$, and all other integer modes inside the tensor band. Neither the $D_{4}$ star nor any other shell is the only evolving support. Nevertheless the **box, $q_{0}^{2}=8$, orientation-compatible integer spectrum and finite cutoff are imposed**. The calculation does not select $q_{0}$ or compare arbitrary rotated/incommensurate crystals.

## Time integration and numerical checks

The solver uses second-order exponential Heun (ETD2). The entire stable linear generator $A_{k}=-$|k|${}^{2}[\alpha+(8-$|k|${}^{2})^{2}]$ is exponentiated exactly. With N(y) denoting the nonlinear RHS,

- Predictor: a = exp(hA$)y + h \phi_{1}($hA)N(y).
- Corrector: $y_{new} = a + h \phi_{2}($hA$)[N(a)-N(y)]$.

The nonlinear part is explicit: **there is no claim of unconditional nonlinear or energy stability**. Every proposed step evaluates the dealiased excess energy; nonfinite states or increases above $2\times10^{-13} + 2\times10^{-12}$|f| are rejected and retried at half-step. The maximum dt=0.1 is additionally capped at 0.0001 for t<0.02 and 0.005 for $0.02\leqt<0.2$, resolving initial stiff nonlinear transfer. The half-dt check halves **all** these caps. Steps land exactly on saved times and startup boundaries.

All main steps were accepted without backtracking: **0 rejected**; largest positive step energy change **5.2e-18**, at roundoff. Saved-time energy increases are at most **6.94e-18**. This is monitored dissipation for the completed trajectories, not a global theorem. The saved instantaneous dissipation is $-\Sigma$|k|${}^{2}$|$\hat{\mu}_{k}$|${}^{2}$, with $\mu$ projected onto the evolving band.

| Independent check | Absolute error or stated scalar |
|---|---:|
| dealias_energy_$18_{vs}$_$28_{same}$_K4 | 0 |
| dealias_projected_nonlinearity_max | 1.69704e-18 |
| energy_gradient_fd_absolute_error | 1.18447e-10 |
| dissipation_identity_absolute_error | 2.91038e-10 |
| shell_rhs_vs_exact_prior_truncation_max | 6.96499e-17 |
| shell_energy_vs_exact_prior_truncation | 6.93889e-18 |
| linear_decay_relative_error | 5.13577e-07 |
| unordered_triads | 32 |
| analytic_amplitude | 0.0775753 |
| matched_rms | 0.38004 |
| nonstationary_shell_rhs_vs_prior_max | 4.46037e-16 |

The linear-decay test uses an amplitude $10^{-7}$ times the full branch and therefore includes a small nonlinear remainder; its reported error is not a pure temporal convergence order estimate. The stronger nonstationary shell-RHS comparison uses a complex random star state, not just the equal-amplitude equilibrium. The dealiased nonlinear and energy tests compare the **same K=4 coefficients** on $18^{4}$ and $28^{4}$ evaluation meshes, separating aliasing from the K=6 physical refinement.

Across all main saved states, maximum reconstructed mean error is **4.6e-18** and $D_{4}$ conjugacy error is **5.65e-17**. Mean conservation is enforced spectrally; the real-space average checks reconstruction and normalization, not an independently unconstrained conservation law. Largest final RHS RMS among full endpoints is **1.21e-15**.

### Spatial and temporal refinements

Replicate 00 of broadband matched random, six-mode noisy, and full-mode noisy starts was repeated at half timestep and at K=6/N=28. Initial Fourier coefficients were copied exactly; new K=6 modes started at zero. This tests resolution of the **same initial condition**, not a newly drawn higher-resolution white-noise distribution. No axis permutation, translation or phase alignment was fitted when comparing endpoints.

| Start | Check | Final excess energy | Difference from main | Max shell-path error / initial full-field RMS | Outcome |
|---|---|---:|---:|---:|---|
| random_full_matched_00 | half_dt | 1.31716972214e-154 | -1.44e-158 | 5.91e-06 | uniform |
| random_full_matched_00 | spatial_K6 | 1.31731971717e-154 | 5.78e-160 | 9.4e-08 | uniform |
| six_1pct_full_noise_00 | half_dt | -0.00772620928487 | -1.73e-18 | 0.0141 | stationary_full24 |
| six_1pct_full_noise_00 | spatial_K6 | -0.00772762360144 | -1.41e-06 | 0.00234 | stationary_full24 |
| full_25pct_full_noise_00 | half_dt | -0.00772620928487 | 0 | 0.00013 | stationary_full24 |
| full_25pct_full_noise_00 | spatial_K6 | -0.00772762360144 | -1.41e-06 | 7.84e-05 | stationary_full24 |

The error column uses the $L^{2}$ difference of the 24 complex star coefficients over all recorded times, divided by the original full-field modulation RMS. Additional endpoint common-band errors, new-band power and maximum path energy differences are saved in `refinement_outcomes.csv`. For uniform endpoints, relative errors divided by an almost vanished final field are not useful; the initial-norm-scaled error and absolute energies should be used instead.

Three refined starts do not establish convergence of every basin boundary. In particular the spatially refined noisy twelve-mode and shell-random bridge ensembles were **not** run. Two cutoffs are a sensitivity check, not an asymptotic convergence proof. The largest half-dt shell-path difference is 1.41% of the initial full-field RMS (six-mode recovery), despite the same endpoint classification. Recovery timing should therefore be read as approximate rather than high-precision kinetics. Stationary endpoint agreement does not imply accuracy of the entire trajectory.

## Initialization and shared conditions

Each replicate uses one real iid Gaussian field, Fourier-projected onto all retained nonzero modes and normalized by Parseval. The same Gaussian direction supplies the weak and matched broadband starts and the noise used in patterned starts. Replicates use independent deterministic child seeds from master seed 931241112. There is no stochastic forcing after initialization, no annealing and no parameter ramp.

Six-mode seeds use the $A_{2}$ subset $\pm{(2,-2,0,0), (0,2,-2,0), (2,0,-2,0)}$. Twelve-mode seeds use the $k_{4}=0 D_{3}$ subset of the star. Full templates use all 24 equal-real coefficients. Patterned seeds receive ordinary cubic-box axis permutations, sign flips and continuous translations. Their unit-RMS templates are perturbed by 1%, 1% or 25% relative-RMS broadband noise **before** normalization to the common RMS. These noise levels are not all-star perturbations as in the earlier basin study. Triality transformations of the restricted star are not imposed on the full integer spectrum.

| Family | Initial modulation RMS | Initial excess-energy range |
|---|---:|---:|
| Broadband random, RMS 0.05 | 0.0500000 | 0.609811–0.619238 |
| Broadband random, RMS matched | 0.3800398 | 35.2447–35.7891 |
| Six-mode seed + 1% broadband noise | 0.3800398 | 0.00128742–0.00135775 |
| Twelve-mode seed + 1% broadband noise | 0.3800398 | -0.00171542–-0.00165779 |
| Full seed + 25% broadband noise | 0.3800398 | 2.05784–2.09574 |
| Shell-random, matched RMS (bridge) | 0.3800398 | 0.021504–0.0305839 |

Equal RMS is **not** equal energy: broadband starts carry a large off-shell linear penalty. The old matched-shell ensemble concentrated all variance on $D_{4}$; these broadband starts place only the tabulated small fraction there. Random-start failure therefore does not isolate an off-shell instability of an already formed $D_{4}$ state. It also reflects the changed initial distribution and rapid damping of off-shell power.

The bridge family takes the $D_{4}$ projection of each broadband random direction and **re-normalizes it to the old matched RMS** before field evolution. It recovers the shell-random intervention without claiming statistical equivalence to the earlier 20 draws. Its success distinguishes power placed on the resonant star from power spread across the retained spectrum.

## Diagnostics and the truncated comparison

- **Occupancy:** signed $D_{4}$ wavevectors with |$a_{k}$|$\geq\max(10^{-6},0.1 \max$|a|); override to zero when total field modulation power <$10^{-12}$. Counts at other thresholds can be recomputed from saved star trajectories.
- **Full endpoint:** occupancy 24, magnitude CV$\leq0.05$, weighted signed triad lock$\geq0.95$, and projected spatial RHS RMS$\leq10^{-7}$. This is stationarity and pattern agreement, not a stability theorem.
- **Locking:** $\Sigma\mathrm{Re}(a_{i}a_{j}a\ell)/\Sigma$|$a_{i}a_{j}a\ell$| over the 32 unordered star triads. A partial pattern can lock; occupancy and CV remain necessary. Locking does not test every off-shell phase relation.
- **Power:** $\Sigma$|$\hat{\phi}$|${}^{2}$ equals modulation variance. $D_{4}$ shell power sums exactly those 24 coefficients; shell fraction divides by **all retained nonzero power**. Off-shell power is the complement, not numerical alias power. On fully patterned endpoints these modes are harmonics; on random transients they are broadband components and should not all be called harmonics.
- **Spectral resolution:** power is also saved by integer |k|${}^{2}$ and at the cutoff boundary $\max_{i}$|$k_{i}$|=K. Final resolved harmonics are tabulated separately for main and refined states.

![Field versus exact truncation](field_vs_truncation.png)

The supplied `run_study.py` provides the exact 24-mode RHS, energy and diagnostics. It is integrated with DOP853 (rtol $2\times10^{-10}$, atol $2\times10^{-12}, \max$ step 0.5), from each corresponding **unscaled field projection**, to the same t=200. The self-test verifies that projecting the field RHS at a shell-only state reproduces that exact RHS to roundoff. After time zero the field grows off-shell coefficients and the two systems need not coincide. Their endpoint classifications agree here, while the field energy is lower. The old study’s 143-run frequencies remain results of a different, shell-restricted experiment.

![Resolved radial power](radial_spectra.png)

The radial plot shows replicate-mean power per integer shell, not spectral density per mode. Final uniform spectra below $10^{-24}$ are omitted. Numerical values, including much smaller uniform residues, remain in the NPZ and CSV outputs.

## Runtime, memory and what was actually completed

- **Main solves:** 18 trajectories, total measured integration time **510.2 s**, per-run range **16.6–188.9 s**.
- **Refinements:** 6 trajectories, total integration time **464.4 s**; largest $28^{4}$ runs took **112.5–128.5 s** each.
- **Wall time:** whole numerical invocation **1041.0 s**, including checks, truncation comparisons, serialization and checkpoint reuse if any. Per-run recorded solver times are the more reproducible work measure.
- **Measured peak resident memory:** **422.9 MiB** for the numerical invocation (Linux ru_maxrss, includes accumulated results and prior-model imports; not just a field array). Runs and refinements were sequential, one FFT worker. These are observed shared-sandbox wall times, not isolated CPU benchmarks; scheduling/suspension can inflate individual times.
- **Array sizes:** an $18^{4}$ float64 field is 0.80 MiB; its rFFT complex128 array is 0.89 MiB. At $28^{4}$ these are 4.69 and 5.02 MiB. Several fields, multipliers, FFT workspaces, diagnostics and accumulated records coexist, so these are not peak-memory estimates.

The budget was declared by mesh, six families $\times$ three replicates, fixed t=200, and six refinements. No unfinished run is counted. This completes a bounded 4D field test rather than substituting another 24-mode computation. It does **not** establish a large-box thermodynamic result, a general basin fraction, a critical nucleus, a nucleation rate, arbitrary-orientation selection, or absence of longer-time/off-band instabilities.

## Reproduce and inspect

From the workspace root:

```bash
python3 co-scientist-outputs/d4-field-test/run_field_study.py \
  --out co-scientist-outputs/d4-field-test-reproduced --validation
```

Defaults reproduce the declared parameters. The CLI accepts `--out`, `--replicates`, `--t-final`, `--dt` and `--validation`; the physical point is fixed to the requested experiment. Cutoff or seed changes require editing the named constants at the top of the solver; physical-parameter changes also require updating derived $\alpha$, $\beta$ and the matched-branch RMS consistently. `--validation` adds the six checks; without it only the main ensembles run. Use a **fresh output directory** for changed parameters. Existing compatible per-run checkpoints are reused; incompatible parameter directories are rejected. Source hashes record provenance, not a bitwise cross-platform guarantee.

A small test is `--replicates 1 --t-final 10 --out co-scientist-outputs/d4-field-smoke`; it is not this reported experiment. Python 3, NumPy, SciPy and Matplotlib are required; `summarize_results.py` additionally uses pandas. No package installation is performed. The archive preserves workspace-relative paths and includes the supplied inputs needed by the source-record and exact-truncation comparison; extract it into a fresh directory and run from that directory’s root.

### Output map

- `field_outcomes.csv`: one row per main field run, including initial conditions, final diagnostics, classification, truncated comparison and actual solver work.
- `field_summary.csv`: six ensemble count summaries; not probability estimates.
- `field_trajectories.csv`: 954 run-time rows with energy, instantaneous dissipation, mean, occupancy, CV, locking, full/shell/off-shell power and cutoff-boundary power.
- `truncated_trajectories.csv`: corresponding exact 24-mode projected-start traces; this table never labels itself as field output.
- `spectral_trajectories.npz`: run IDs, times, 24 complex star coefficients and power summed by integer |k|${}^{2}$ at every saved time.
- Per-run NPZ checkpoints: all compact initial and final **full-band** Fourier coefficients and star/shell-power histories. Full-band intermediate complex states are not stored; regenerate them with the solver if needed.
- `refinement_outcomes.csv`, `refinement_trajectories.csv` and `check_*.npz`: all six completed checks, with full-band initial/final states, trajectory diagnostics and comparison errors. Per-check CSVs in the archive hold the same traces separately.
- `final_harmonic_power.csv` and `refined_harmonic_power.csv`: non-negligible final power by integer shell; powers $\leq10^{-20}$ omitted only from these compact tables.
- `parameters.json`, `seed_manifest.json`, `numerical_tests.json` and `audit_summary.json`: configuration, source hashes, seeds, numerical validation and aggregate checks.
- `run_field_study.py`, `summarize_results.py`, three PNG figures and this report are included in `reproducibility.zip` with the completed data and original inputs.
