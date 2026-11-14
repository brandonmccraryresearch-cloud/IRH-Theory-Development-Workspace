# $D_{4}$ droplets: deterministic radial-envelope thresholds

## Result and scope

At the manuscript’s tuned point **$r = -0.35$, mean $m = -0.18$, u = v = 1, $q_{0}^{2} = 8$**, a radial, phase-locked $D_{4}$-envelope model has a finite-amplitude access threshold. For a nominal per-mode seed amplitude A* = 0.07757529634 and interface-width parameter w = 6, the **initial seed-radius parameter is bracketed by decay at R = 16.19140625 and growth at R = 16.2109375** on the main grid. The bracket is numerical, not a statistical confidence interval; grid and profile choices cause larger shifts.

A separate nonuniform stationary saddle has **$L^{2}$-equivalent radius 13.52856 and total excess energy 550.93057** on that grid. It has one positive radial dynamical eigenvalue. Contracting or expanding its profile by 2% produces decay or growth, respectively. On the finest tested grid its radius is 13.53027 and energy 551.24848. These are **restricted-envelope estimates**, not a verified critical nucleus of the unrestricted 4D scalar field.

**No noise was used. No waiting-time distribution, temperature, stochastic action, physical nucleation rate or cosmological timescale is inferred.** A deterministic separatrix is not a stochastic waiting time. The saddle energy is not automatically the activation exponent of an unspecified noise process.

![Growth thresholds, near-critical trajectories, initial-seed excess energies and the stationary radial profile.](size_growth_energy.png)

## 1. Inputs and source checks

Sources inspected: `uploads/Dynamical_Selection_of_a_D_4_Substrate_f.pdf`, v93.1, §§I.2–3 and II.6–9, especially PDF pages 9–11; and G4 of `co-scientist-outputs/d4-framework-comparison/gap-memo.md`. The tables on PDF pages 10–11 were checked in their printed-page views. Source hashes and package versions are in the reproduction bundle’s `environment.json`.

The starting functional and mobility are

\[
F[\psi]=\int_{\mathbb R^4}\left[\tfrac12\psi\{r+(q_0^2+\nabla^2)^2\}\psi-\tfrac13\psi^3+\tfrac14\psi^4\right]d^4x,
\qquad \partial_t\psi=\nabla^2\frac{\delta F}{\delta\psi}.
\]

The shell consists of the 24 vectors obtained by permuting $(\pm2,\pm2,0,0)$, with |k|${}^{2} = 8$. Explicit enumeration in the supplied code recovers **N = 24, T = 192, Q = 3384**. We set $w_{6} = 0$ and mobility to one; there is no inertial term or damping parameter $\gamma$ in this Model-B experiment.

At fixed mean, define $a = r - 2m + 3m^{2} = **0.1072$** and $b = 1 - 3m = **1.54$**. The homogeneous shell energy density is

\[
f_A(A)=\frac{N a}{2}A^2-\frac{T b}{3}A^3+\frac Q4 A^4.
\]

Its larger stationary amplitude is A* = **0.0775752963393**, its smaller positive stationary amplitude is 0.009800590186, and $f_{A}(A*) = **-0.007632267319$**. The latter reproduces §II.8’$s -0.0076323$. The small homogeneous stationary amplitude is **not** a droplet threshold. The manuscript’s relaxed-field value $-0.0077276$ is not reproduced by an ansatz that excludes harmonics.

A control at the manuscript’s detuned value $q_{0}^{2} = 7.5$ adds 0.25 to a on this fixed shell. The homogeneous nonzero-branch discriminant is **$-49.6784$**, so that branch disappears, consistent with §II.7. All reported droplet runs are at $q_{0}^{2} = 8$; this is not a detuning scan.

### Baseline convention

All plotted and tabulated energies are **total excess over the uniform field at the same conserved mean**, not energy density and not absolute F. With the functional written above, its full absolute uniform density is 1.03333644. The manuscript’$s -0.00346356$ omits the constant $q_{0}^{4}m^{2}/2 = 1.0368$. At fixed total mean this constant convention does not affect excess energies. Here the full functional is retained for local mean variations, and its uniform value and tangent are subtracted analytically to avoid cancellation errors.

## 2. Radial ansatz and approximation

Let $\rho$ = |x| and use

\[
\psi(x)\approx n(\rho)+A(\rho)\sum_{k\in\Phi_{D_4}}e^{ik\cdot x},\qquad n=m+c.
\]

A is real and shared by all 24 signed modes. Thus the carrier is a **deliberately seeded, equally populated, phase-locked $D_{4}$ pattern**. Phases, unequal amplitudes, competing stars and defects cannot evolve independently in this calculation. The signed-mode convention already makes the sum real; there is no additional factor of two in A.

Cell averaging drops nonresonant carrier products and keeps closed triads and quartets. $D_{4}$’s second-moment isotropy gives $\Sigma(k\cdot\nablaA)^{2}$ = Nq${}_{0}^{2}$|$\nablaA$|${}^{2}/4$. Therefore the shell-gradient contribution is $N[(\DeltaA)^{2} + q_{0}^{2}$|$\nablaA$|${}^{2}]/2$. This is a spatial scale-separation approximation: it is not an exact integration of an envelope times carriers over a finite 4D box.

Using $\Delta = \partial\rho^{2} + 3\partial\rho/\rho$, the excess radial energy is

\[
\begin{aligned}
E=2\pi^2\int_0^{L}\rho^3\,d\rho\,\{&\tfrac12(q_0^4+a)c^2+(m-\tfrac13)c^3+\tfrac14c^4
+q_0^2 c\Delta c+\tfrac12(\Delta c)^2\\
&+\tfrac N2[(\Delta A)^2-q_0^2 A\Delta A+a(n)A^2]
-\tfrac T3 b(n)A^3+\tfrac Q4 A^4\},
\end{aligned}
\]

where $a(n) = r - 2n + 3n^{2}$ and $b(n) = 1 - 3n$. Gradient terms are integrated by parts with no-flux conditions. The omitted linear mean term integrates to zero because $\int\rho^{3}c d\rho = 0$.

The implementation evolves the coarse mean and common amplitude using the **shell-averaged Model-B mobility closure**

\[
\dot c=\Delta\mu_c,\qquad \dot A=(\Delta-q_0^2)\mu_A,
\]

\[
\begin{aligned}
\mu_c={}&[(\Delta+q_0^2)^2+a]c+(-1+3m)c^2+c^3
+N[-1+3(m+c)]A^2+TA^3,\\
\mu_A={}&\Delta^2 A-q_0^2\Delta A+a(m+c)A
-\tfrac TN b(m+c)A^2+\tfrac QN A^3.
\end{aligned}
\]

Here $\muc = \deltaE/\deltac$ and $\muA = (1/N)\deltaE/\deltaA$, with radial volume measure understood. Angularly odd carrier-gradient contributions to mobility and phase dynamics are discarded. Averaging mobility and averaging energy separately is a **closure**, not an exact conserved Galerkin projection of the full field. A leading-envelope alternative, $\dot{A} = -q_{0}^{2}\muA$, is included as a sensitivity test.

This system conserves the **coarse mean** and dissipates its stated energy:

\[
\dot E=-\int |\nabla\mu_c|^2d^4x-N\int (|\nabla\mu_A|^2+q_0^2\mu_A^2)d^4x\le0.
\]

The amplitude is not conserved: its nonzero-wave-number carrier can relax under conserved scalar-field dynamics. Conservation of the reconstructed finite-domain oscillatory field is only represented through cell averaging; it has not been checked against an actual 4D field realization.

## 3. Seeds, radii and outcome definitions

The initial coarse mean is uniform, $c(\rho,0) = 0$. The seeded envelope is

\[
A(\rho,0)=\alpha A_*\,\frac{1-\tanh[(\rho^2-R^2)/(2Rw)]}{2}.
\]

This form is even at the origin and has zero radial derivative there. **R is the radius where A equals half the nominal amplitude $\alphaA$***; w is its local interfacial-width scale. The central amplitude is $\alphaA*[1$ + tanh(R/(2w))]/2, not exactly $\alphaA$*, particularly for small droplets. No droplet mean offset or independent carrier phase is imposed.

A radius available for arbitrary evolving profiles is

\[
R_{\rm eq}=\left[4\int_0^L\rho^3(A/A_*)^2d\rho\right]^{1/4}.
\]

It equals the geometric radius of a sharp 4-ball of amplitude A*. It is **not** a density contour or a literal solid-volume measurement, and changing amplitude changes it even without interface motion. $R_{half}$ in raw data is the outermost cell center with $A \geq A*/2$; that is a fixed absolute-amplitude contour, not the seed R for $\alpha \neq 1$. The stationary saddle’s quoted radius is $R_{eq}$; it must not be substituted for the initial-profile R in the threshold table.

Each trajectory is sampled at 101 times through t = 200. Decay means the final maximum amplitude is below 0.05A*, or $R_{eq}$ falls by more than one unit with continued late contraction. Growth means $R_{eq}$ increases by more than one unit with continued late growth, or fills the domain after documented growth **before** $R_{half}$ reaches 0.7L. Runs reaching 0.85L are flagged as boundary-affected. Filled-domain energies are not used as infinite-system final-state estimates. Unclassified runs would be retained as unresolved, not assigned to either side; none occurred in these brackets.

## 4. Threshold table

Main grid: L = 120, $\Delta\rho = 0.5$, w = 6, $t_{end} = 200$. A 40-run coarse scan used $\alpha = 0.6$, 0.8, 1.0, 1.2 and R = 2, 4, 6, 8, 10, 12, 15, 20, 30, 40. Another 40 runs bisected the four transitions. Monotonic threshold behavior is supported by these sampled families; it is not a theorem for arbitrary seeds.

| Nominal amplitude $\alphaA$* | $\alpha$ | Largest tested decaying R | Smallest tested growing R |
|---:|---:|---:|---:|
| 0.04654518 | 0.6 | 19.609375 | 19.62890625 |
| 0.06206024 | 0.8 | 17.51953125 | 17.53906250 |
| 0.07757530 | 1.0 | 16.19140625 | 16.21093750 |
| 0.09309036 | 1.2 | 15.27343750 | 15.29296875 |

The accompanying `threshold_table.csv` includes each endpoint’s initial excess energy. Lengths are in the manuscript’$s k = (\pm2,\pm2,0,0)$ coordinates. The resonant wavelength $2\pi/q_{0} \approx 2.22144$ makes the $\alpha = 1$ threshold about 7.3 wavelengths; this is a model-unit conversion, not a microscopic length prediction.

## 5. Stationary critical profile and size-dependent energy

A sparse Newton solve enforces $\muA = 0$, spatially constant $\muc$, and zero integrated c. Starting from R = 15 converges to a nonuniform stationary solution rather than the uniform state. On the main grid:

- **Radius and energy** — $R_{eq} = 13.52855989$; E = 550.93057345.
- **Core** — A in the innermost cell is 0.05657310, about 0.729A*; local mean shift is +0.00130678.
- **Stationarity** — maximum equation residual is $2.06 \times 10^{-14}$.
- **Radial instability** — the $480 \times 480$ dynamical Jacobian has one positive eigenvalue, +0.6789981, one mass-conservation zero mode $(-4.9 \times 10^{-14}$ numerically), and the next eigenvalue $-0.1174233$. This counts only perturbations admitted by this radial equal-amplitude model.
- **Directional check** — a 2% radial contraction reaches negligible amplitude; a 2% dilation expands and eventually fills the finite domain. Both start with energies below the saddle, as expected along an unstable direction. Their initial equivalent radii are 13.25858 and 13.79966.

This is evidence for an index-one **radial** transition saddle. It does not prove a globally minimum barrier, a unique nucleus, or stability against nonradial, phase or unequal-mode perturbations. No continuation search over other saddles was performed.

The figure maps initial total excess energy over 173 radii per amplitude. Its constrained seed-path maxima are:

| $\alpha$ | R at seed-path maximum | Maximum initial E |
|---:|---:|---:|
| 0.6 | 21.63537 | 1013.25658 |
| 0.8 | 18.61457 | 1134.44749 |
| 1.0 | 17.98082 | 1487.65671 |
| 1.2 | 20.36905 | 2473.65989 |

**These maxima are not the stationary saddle energy and are not the growth threshold.** The fixed seed family does not follow a minimum-energy path. For example, the $\alpha = 1$ seed threshold near R = 16.20 lies below the seed-energy maximum near R = 17.98. A positive-energy initial seed can grow while descending E; the sign of initial excess energy is not a growth criterion. No sharp-interface capillary formula or fitted surface tension was needed.

## 6. Discretization and reproduction checks

### Space and time

Cell centers are $\rhoj = (j + 1/2)h$. Radial cell weights are wj = $(\rhoj+1/2^{4} - \rhoj-1/2^{4})/4$, and the face conductance is $g = \rho$face${}^{3}/h$. The conservative finite-volume Laplacian is

\[
(Dz)_j=\{g_{j+1/2}(z_{j+1}-z_j)-g_{j-1/2}(z_j-z_{j-1})\}/w_j.
\]

It is negative semidefinite in the weighted inner product, has D1 = 0, and has exact weighted flux cancellation. Zero face flux is imposed at $\rho = 0$ and L. Repeated applications of the same D define $\Delta^{2}$ and the higher-order dynamics; this supplies the compatible no-flux closure for the auxiliary Laplacians and chemical potentials. At the origin it avoids evaluating $3/\rho$ explicitly. This is a radial ball, **not the paper’$s (2\pi)^{4}$ periodic box**, which cannot contain these large localized seeds.

Discrete E uses this same weighted operator, so its derivative is exactly the chemical potential implemented in the ODE. SciPy’s adaptive implicit BDF solver uses an analytic sparse Jacobian, relative tolerance $2 \times 10^{-7}$ and absolute tolerance $2 \times 10^{-10}$. No fixed timestep is assumed. There is no Fourier transform, aliasing or dealiasing in this radial discretization. The stiff linear operator alone is not taken as a proof of nonlinear timestep stability; numerical dissipation is checked directly.

### Sensitivity at $\alpha = 1$

Each row below has its own bisection endpoints; compare intervals, not rounded midpoint digits.

| Test | Decay R | Growth R |
|---|---:|---:|
| h = 1 | 16.18164 | 16.19629 |
| h = 0.25 | 16.21094 | 16.22559 |
| L = 80 | 16.19629 | 16.21094 |
| L = 160 | 16.19629 | 16.21094 |
| $t_{end} = 400$ | 16.19629 | 16.21094 |
| w = 4 | 16.73828 | 16.75293 |
| w = 8 | 15.59570 | 15.61035 |
| Freeze local mean c = 0 | 16.25488 | 16.26953 |
| Leading amplitude mobility $-q_{0}^{2}$ | 16.19629 | 16.21094 |

The h = 0.25 threshold is about 0.015–0.02 above the main-grid midpoint. Profile width changes R by about 0.6, so reporting a universal critical seed radius to two decimal places would be misleading. Finite-domain and doubled-duration checks agree within the bisection resolution. These are numerical checks, **not an error bar on the underlying envelope approximation**.

Stationary saddle convergence is cleaner:

| h | $R_{eq}$ | Total saddle excess E |
|---:|---:|---:|
| 1 | 13.521726 | 549.659102 |
| 0.5 | 13.528560 | 550.930573 |
| 0.25 | 13.530267 | 551.248482 |

The changes are approximately second order. A two-finest-grid extrapolation gives $R_{eq} \approx 13.53084$ and $E \approx 551.35445$; treat these as convergence indications, not extra physical precision. At h = 0.5, changing L from 80 to 160 changes saddle E from 550.95861 to 550.92532.

Other checks recorded in `reproduction_checks.json`:

- **Bulk energy** — discrete uniform-envelope energy density $-0.007632267318990362$ agrees with the analytic $-0.007632267318990377$.
- **Uniform solution** — the zero perturbation has exactly zero numerical RHS.
- **Energy derivative** — a fixed-seed random directional derivative agrees with the implemented chemical potentials to relative error $8.68 \times 10^{-9}$.
- **Jacobian** — a finite-difference directional check agrees with the sparse analytic Jacobian to relative error $3.40 \times 10^{-12}$.
- **Conservation** — the largest absolute coarse-mean error across the refinement and sensitivity runs is $2.52 \times 10^{-15}$.
- **Dissipation** — the largest positive sampled energy increment is $3.11 \times 10^{-7}$, against saturated |E| $\approx 7.81 \times 10^{6}$; this is a small numerical violation, not exact stepwise monotonicity. Early and near-saddle trajectories descend energy.

The 40 coarse, 40 refinement and 108 sensitivity trajectories are preserved with energies, radius metrics, classifications, boundary flags and solver counts. The full coarse-scan time histories, saddle perturbations, seed-energy map and final saddle profile are also included.

## 7. Reproduce and inspect

The ZIP is a self-contained code-and-data package; it does not require either source document to run. Extract it in a writable folder. With Python, NumPy, SciPy and Matplotlib available, run these commands from the extracted package root:

```bash
python3 droplet_experiment.py --out regenerated --time 200
python3 refine_and_plot.py --out regenerated
```

A single controlled experiment can be run independently:

```bash
python3 droplet_experiment.py --single --radius 16.2 --alpha 1 \
  --width 6 --dr 0.25 --domain 120 --time 400 --out single_run
```

Optional flags `--frozen` and `--leading-mobility` reproduce the two closure tests. The scan’$s \alpha$ values and coarse radii are explicitly listed in `droplet_experiment.py`; the bisection, stationary equations, sensitivity configurations and figure are in `refine_and_plot.py`. `requirements.txt` records the exact package versions used, rather than silently installing anything. Python was 3.14.4. A fresh complete rerun into a separate directory reproduced the threshold table, sensitivity brackets, saddle grid checks and numerical diagnostics exactly in this environment. In another environment, compare toleranced numerical values, not execution times or last-bit agreement.

The package’s `reference_results/` folder contains every numerical table and JSON diagnostic used here, including the main threshold table, per-run outcomes, 40 coarse trajectories, eigenvalue spectrum, three saddle-grid checks, two saddle-domain checks, perturbation checks and 692 initial-seed energy samples. `SHA256SUMS.txt` checks the packaged files. The report and both PNG/SVG figure formats are included.

## 8. What this resolves—and what it does not

This supplies a deterministic localized-seed route to the ordered branch **within an explicit radial $D_{4}$-envelope approximation** and quantifies how its size threshold depends on amplitude and interface width. It goes beyond persistence of a box-filling seeded pattern, as requested by G4.

It does **not** establish unbiased emergence of all 24 modes, exclude a lower-symmetry nucleus, reproduce the unrestricted harmonic relaxation, or determine a physical noise law. The interface scale w = 6 is only about 2.7 resonant wavelengths, so omitted carrier-scale and phase effects may be material. The next validation would be a sufficiently large, resolved 4D conserved-field calculation initialized from these near-critical profiles, including local mass compensation and perturbations outside the imposed symmetry. A stochastic interpretation would separately require a specified noise covariance, its conservation properties and any fluctuation–dissipation relation; none is supplied or assumed here.
