# Basin screening of the full $D_{4}$ standing wave

**Scope: exact 24-wavevector Galerkin truncation of conserved Model B; not a full-field simulation.** Sources: McCrary, *Dynamical Selection of $a D_{4}$ Substrate from Interference Dynamics*, v93.1, §§I.2–I.3 and II.7–II.9, and the supplied gap memo, G1.

## Main finding

At the manuscript’s tuned full-pattern point, a finite-amplitude basin of the full phase-locked standing wave exists **within the retained $D_{4}$ star**. All 20 matched-power random starts and all 100 noisy patterned starts reached the same full state modulo retained-star symmetries and translations. All 20 weak random starts decayed to the uniform state. Exactly unperturbed six- and twelve-mode controls remained partial, but their truncated-energy Hessians have negative directions: these controls are saddles, not competing stable attractors in this truncation.

This supports conditional accessibility and local stability of the full pattern at this parameter point. It does **not** show that arbitrary initial conditions select $D_{4}$, that $D_{4}$ wins against other shells, or that these basin frequencies persist in full field dynamics.

## Outcome table

All runs use the same functional, mean, deterministic dynamics and stopping time. Patterned and matched-random starts have initial modulation RMS **0.3800398** (the exact value is $\sqrt{24} \times 0.0775752963393)$. “Six/twelve + noise” means a partial-pattern seed with a 1% relative-RMS, all-star perturbation before normalization. Percentages for full seeds have the same convention.

| Initial ensemble | Independent perturbed/random runs | Full 24-mode endpoint | Uniform | Full-success Wilson 95% interval |
|---|---:|---:|---:|---:|
| Shell-projected random, RMS 0.05 | 20 | 0 | 20 | 0–16.1% |
| Shell-projected random, matched RMS | 20 | 20 | 0 | 83.9–100% |
| Six-mode $A_{2}$ pattern + 1% noise | 20 | 20 | 0 | 83.9–100% |
| Twelve-mode $D_{3}$ pattern + 1% noise | 20 | 20 | 0 | 83.9–100% |
| Full pattern + 5% noise | 20 | 20 | 0 | 83.9–100% |
| Full pattern + 25% noise | 20 | 20 | 0 | 83.9–100% |
| Full pattern + 100% noise | 20 | 20 | 0 | 83.9–100% |

Three additional deterministic controls give **143 trajectories total**:

| Exact control | Final occupancy | Active unordered triads | Signed triad locking | Amplitude CV | Excess F/V | Local type |
|---|---:|---:|---:|---:|---:|---|
| Six-mode $A_{2}$ | 6 | 2 | 1 | 1.73205 | $-0.002253511969$ | Saddle |
| Twelve-mode $D_{3}$ | 12 | 8 | 1 | 1 | $-0.005362496463$ | Saddle |
| Full $D_{4}$ | 24 | 32 | 1 | 0 | $-0.007632267319$ | Minimum modulo translations |

No binomial interval is assigned to deterministic controls. There were no unresolved endpoints at the declared stationarity tolerance. The seven intervals describe the seven specified initial-condition distributions separately; they are neither simultaneous intervals nor a probability over unspecified initial conditions. The 100%-noise full-seed ensemble remains centered on the full template; the matched-random ensemble is the separate orientation-independent Gaussian-direction test.

## Functional and exact restriction

The implemented manuscript functional is

\[
F[\psi]=\int_{[0,2\pi]^4}\!d^4x\left[\tfrac12\psi\{r+(q_0^2+\nabla^2)^2\}\psi-\tfrac u3\psi^3+\tfrac v4\psi^4\right],
\qquad \partial_t\psi=\nabla^2\frac{\delta F}{\delta\psi}.
\]

The field is restricted to

\[
\psi(x)=\bar\psi+\sum_{k\in S}a_k e^{ik\cdot x},\quad
S=\{2(\pm e_i\pm e_j):i<j\},\quad a_{-k}=a_k^*.
\]

There are 24 signed wavevectors, hence 12 conjugate pairs and **24 real dynamical degrees of freedom**, plus a fixed zero mode. The box is four-dimensional and periodic; every retained nonzero mode has |k|${}^{2}=8$. No lattice-grid discretization is used.

After subtracting the uniform-state energy, the exact restricted excess density is

\[
f=\frac\alpha2\sum_k|a_k|^2-\frac\beta3\sum_{i+j+\ell=0}a_i a_j a_\ell
+\frac v4\sum_{i+j+\ell+m=0}a_i a_j a_\ell a_m,
\]

\[
\alpha=r+(q_0^2-8)^2-2u\bar\psi+3v\bar\psi^2=0.1072,
\qquad \beta=u-3v\bar\psi=1.54.
\]

Ordered resonant sums are evaluated exactly, with **192 ordered triads and 3384 ordered quartets**. The projected dynamics is

\[
\dot a_k=-8\left[\alpha a_k-\beta\sum_{i+j=k}a_i a_j
+v\sum_{i+j+\ell=k}a_i a_j a_\ell\right].
\]

All convolution indices lie in S. Nonresonant harmonics are discarded by Galerkin projection, not folded back by FFT aliasing. The zero mode does not evolve. Conservation is therefore exact **by construction**, not an independent test of a spatial field solver. At this single shell, Model B’s nonzero-mode mobility is the constant factor 8; this restricted system cannot test wavelength-dependent transport.

The full equal-real-amplitude stationary branch satisfies

\[
\alpha-8\beta A+141vA^2=0,
\quad A_*=0.0775752963393,
\quad f_*=-0.00763226731899.
\]

This reproduces the manuscript’s **one-shell ansatz** energy, not its harmonically relaxed full-field value $-0.0077276$. The missing harmonic lowering cannot occur here.

## Shared settings and initialization

| Setting | Value |
|---|---|
| r; u; v | $-0.35$; 1; 1 |
| Fixed mean | $-0.18$ |
| $q_{0}^{2}$; box side | 8; $2\pi$ |
| Mobility; evolution | 1; deterministic Model B, no annealing or time-dependent forcing |
| Final time | 400 dimensionless time units |
| Integrator | SciPy DOP853, adaptive explicit Runge–Kutta |
| Relative/absolute tolerances | $2\times10^{-9} / 2\times10^{-11}$ |
| Maximum timestep | 0.5 |
| Master seed | 931241110; independently spawned per-run generator seeds |
| Recorded times | t=0; 25 logarithmic points 0.01–2; then every 2 units through t=400 |

Random starts are circular Gaussian coefficient directions normalized to the specified modulation RMS, with exact conjugacy. They are **not** random fields containing arbitrary wavevectors. Both random ensembles use the same directional distribution; only their initial power differs. The 0.3800398 RMS ensemble is power-matched, not energy-matched: its initial excess energies range from +0.01187 to +0.04015, while the full seed has negative excess energy.

The six-mode template is $\pm{\alpha, \beta, \alpha+\beta}$, with unit roots $\alpha=(1,-1,0,0)$ and $\beta=(0,1,-1,0)$, subsequently scaled by 2. The twelve-mode template contains the $D_{4}$ roots with fourth coordinate zero. These are one $A_{2}$ and one $D_{3}$ embedding, randomized over star automorphisms; they do not exhaust all inequivalent six- or twelve-mode subsets.

For noisy patterns, a unit-norm random real-field coefficient direction is added to a unit-norm template at the stated ratio; the sum is then normalized to the common target RMS. The label is the **pre-normalization additive-noise ratio**, not the final angular displacement. Each run also receives a random star automorphism and continuous translation. Those symmetry copies are not counted as extra replicates. Exact controls receive no perturbation.

## Diagnostics and classifications

The code fixes the following rules before integration:

- **Occupancy:** count signed modes with |$a_{k}$| $\geq \max(10^{-6}, 0.10 \max_{j}$|$a_{j}$|). Endpoints with total modulation power below $10^{-12}$ are classified uniform and assigned occupancy zero.
- **Amplitude variation:** population SD of all 24 magnitudes divided by their mean, including unoccupied modes. This distinguishes equal-amplitude full patterns from partial patterns even when their triads lock perfectly.
- **Triad locking:** $\Sigma \mathrm{Re}(a_{i}a_{j}a\ell) / \Sigma$ |$a_{i}a_{j}a\ell$| over the 32 unordered zero-sum triads. The signed statistic equals one for favorable phase closure. It is not an absolute coherence statistic that would also accept unfavorable phases. Active-triad count and unweighted active-triad cosine mean are also saved.
- **Free energy:** excess density relative to the fixed uniform field, not absolute total F. The exact zero-mode baseline cancels.
- **Shell power:** $P=\Sigma$|$a_{k}$|${}^{2}$ is the modulation variance by Parseval. The shell fraction is 100% for every mathematically nonzero retained field **by construction**, including partial patterns. The final uniform-state fraction, CV and phase locking are left blank as physically undefined.
- **Stationarity:** RMS of the 24 complex coefficient derivatives $\leq10^{-7}$. It is not a stability test.
- **Full-pattern outcome:** stationary, occupancy 24, magnitude CV $\leq0.05$, and signed triad locking $\geq0.95$. The CSV `full_pattern` diagnostic omits stationarity; the `outcome` label includes it.

All 121 full endpoints, including the exact control, have locking 1 to stored precision, magnitude CV below $1.85\times10^{-13}$, and energy $-0.007632267319$. The final modulation power is 0.144430238451. The weak ensemble’s power decays below $4.5\times10^{-300}$; phase statistics at that numerical residue have no physical meaning. Changing the relative occupancy threshold to 1%, 5% or 20% leaves all nonuniform endpoint occupancies unchanged.

The figure shows replicate-level final occupancy, CV and locking, Wilson intervals for full success, and energy/absolute-shell-power trajectories. Temporal bands are the **full replicate range**, not confidence bands. The three deterministic controls are tabulated separately and excluded from the n=20 ensemble panels. Complete diagnostics are in the archive’s `diagnostic_traces.csv` and `trajectories.npz`.

## Symmetry-equivalent endpoints

The comparison enumerates **all 1152 automorphisms of the retained $D_{4}$ star**, including triality, and minimizes phase mismatch over four translation coordinates. Magnitudes first prune candidate permutations; multistart circular least-squares then fits translations. Relative coefficient $L^{2}$ distance below $10^{-5}$ defines a numerical match. Rotation-plus-translation checks on a nonuniform random test state pass at residual $1.12\times10^{-16}$.

| Class | Members | Interpretation |
|---|---:|---|
| S01 | 20 | Uniform state; tiny numerical residues identified |
| S02 | 121 | One full-pattern orbit |
| S03 | 1 | Exact six-mode saddle |
| S04 | 1 | Exact twelve-mode saddle |

The largest accepted endpoint-equivalence residual is below $8.9\times10^{-13}$. This clustering is numerical, not a certified global phase-optimization proof. Star automorphisms are symmetries of this restricted model; triality need not preserve the unrestricted integer spectrum of a cubic-box full-field solver. Arbitrary continuously rotated stars are outside this truncation.

## Local stability and numerical checks

A centered finite-difference Hessian (step $10^{-6})$ is computed in orthonormal real coefficient coordinates. Eigenvalues below $-10^{-7}$ count as negative, and magnitudes $\leq10^{-7}$ as zero. Because all retained |k|${}^{2}=8$, Model B’s linearized growth eigenvalues are $-8$ times the energy-Hessian eigenvalues.

| State | Negative / zero / positive eigenvalues | Minimum nonzero Hessian eigenvalue | Interpretation |
|---|---|---:|---|
| Uniform | 0 / 0 / 24 | +0.1072 | Linearly stable in the retained star |
| Full pattern | 0 / 4 / 20 | +0.341899 | Stable locally modulo four translations |
| Exact six-mode | 6 / 2 / 16 | $-0.1072$ | Unstable transverse directions; largest growth rate 0.8576 |
| Exact twelve-mode | 2 / 3 / 19 | $-0.0258672$ | Unstable transverse directions; largest growth rate 0.20694 |

Thus the exact partial patterns persist on invariant subspaces, while their 1% all-star perturbations can leave those subspaces. This explains the difference between exact controls and noisy partial seeds **in this model**; it does not explain all manuscript full-field partial-pattern outcomes.

Seventeen trajectories—two from each random/noisy ensemble plus the three controls—were reintegrated with tolerances 100 times tighter and maximum timestep four times smaller. All full-success classifications agree. Maximum final coefficient discrepancy is $6.82\times10^{-13}$; maximum excess-energy discrepancy is $1.39\times10^{-17}$. All finite-amplitude occupancy classifications agree.

Additional checks:

- Directional derivative of restricted energy versus analytic gradient: absolute error $3.77\times10^{-12}$.
- Energy against independent exact $5^{4}$-point quadrature of the degree-four polynomial in unit-root coordinates: zero discrepancy at displayed precision.
- Restricted dissipation identity df/dt=$-8\Sigma$|$\mu_{k}$|${}^{2}$: zero discrepancy at displayed precision in the test state.
- Largest energy increase between saved times: $1.95\times10^{-16}$, consistent with roundoff. Saved-time monotonicity alone is not an unconditional timestep-stability proof.
- Largest conjugacy defect over saved trajectories: $1.98\times10^{-13}$; maximum final derivative RMS: $8.54\times10^{-15}$.

## Reproduce and inspect

From the workspace root, with Python, NumPy, SciPy and Matplotlib available:

```bash
python3 co-scientist-outputs/d4-basin-study/run_study.py \
  --out co-scientist-outputs/d4-basin-study-reproduced
python3 co-scientist-outputs/d4-basin-study/validate_study.py \
  --out co-scientist-outputs/d4-basin-study-reproduced
```

Alternatively extract `reproducibility.zip` into a directory and run its two scripts with `--out` pointing to a new output directory. A smaller smoke test is `--replicates 2 --t-final 50`; it is not the reported experiment. `--seed`, `--rtol`, `--atol`, and `--max-step` are configurable. Use the defaults to reproduce the reported ensembles. NumPy/SciPy versions, actual solver evaluations, source-code SHA-256 and seed records are saved in `parameters.json` and `seed_manifest.json`. The companion source record hashes both supplied inputs.

The archive includes executable source, the parameter/seed records, all initial and saved coefficient states, diagnostic traces, endpoint representatives, validation results, tables and figures. `basin_outcomes.csv` has one row per trajectory; `basin_summary.csv` has one row per ensemble/control. NPZ trajectory coefficients have shape (saved time, run, signed wavevector); run ordering follows the seed manifest. The automorphism arrays are integer permutations of the wavevector order saved in the same archive.

## What G1 now supports—and what remains open

**Supported here:** a demonstrated finite-amplitude basin, perturbation recovery, phase-locked full occupancy, and local stability modulo translations in a precisely specified 24-mode conserved restriction. Weak starts fail at the same parameter point, consistent with positive effective quadratic coefficient and coexistence of a stable uniform state.

**Still open:** unrestricted initial spectra, off-shell instabilities and harmonic relaxation, spatially localized nuclei, defects and coarsening, box-size or resolution dependence, annealing protocols, detuning and mean scans, other inequivalent within-shell subsets, and competing lattices or orientations. The selected star and $q_{0}$ tuning are imposed; these results must not be presented as an independent demonstration of $D_{4}$ shell selection. There is no measured critical nucleus or nucleation rate, and no claim of convergence from arbitrary initial conditions.
