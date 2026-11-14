# Task 1 — Noise-driven $D_{4}$ nucleation in the envelope model

**CLAIM:** With explicitly defined conserved noise added to the droplet
envelope model, nucleation waiting times follow a Kramers/Arrhenius law
whose fitted barrier is consistent with the deterministic saddle barrier
$\Delta F^* = 555$ in the radial-envelope (Route B) calculation (slope
$567$, bootstrap 68\% interval $[510, 617]$), while in
the finite $\pi$-box full-field calculation (Route A) the transition is
instead a homogeneous shell-amplitude crossing with a far smaller
effective barrier, so the box waiting times do **not** measure the
infinite-volume droplet barrier. The two routes agree on the mechanism
structure (a rare fluctuation crossing a saddle, then fast deterministic
growth) and disagree, for a stated finite-size reason, on the barrier
value — and that disagreement is the result.

**STATUS:** VERIFIED for the Route B Arrhenius law (slope $567$,
bootstrap 68\% interval $[510, 617]$, vs $\Delta F^* = 555.20$; 80/80
replicates transited) and for the Route A scan across $D$ (20 scan
replicates + 10 extension replicates + 4 pilot replicates; graded
crossover $0/5$ at $D = 0.3$, $2/5$ at $D = 0.5$, $3/5$ at $D = 0.7$,
$5/5$ at $D = 1.0$). NO physical nucleation rate, no
cosmological timescale, and no temperature are claimed anywhere in this
report: $D$ and $T$ are model noise strengths, not physical temperatures,
and no fluctuation–dissipation relation to a physical bath is assumed.

## 1. Problem and prior results reused

The droplet study (Task 4, `task4_report.md`) established, at the
operating point $(\bar{\psi}, r) = (-0.18, -0.35)$, $u = v = 1$,
$q_0^2 = 8.0$:

- gradient coefficient $\kappa = 192$ in the $(\kappa/2)|\nabla A|^2$
  convention, verified against exact 4D FFT energy to $4.2\times10^{-5}$;
- one-mode Landau functional $f_{mod}(A) = 12\, r_{eff} A^2 - 64\, u_{eff} A^3
  + 846\, A^4$ with $r_{eff} = 0.1072$, $u_{eff} = 1.54$,
  $A^* = 0.0775753$, $f_{mod}(A^*) = -0.00763227$;
- radial-ODE critical droplet $R_c = 12.57$, $\Delta F^* = 555.2$,
  core amplitude $A(0)_c = 0.056605$, correlation length $\xi = 8.64$;
- thin-wall estimate ($R_c = 7.38$, $\Delta F^* = 37.2$) fails because
  $\xi > R_c$;
- in the finite periodic $\pi$-box the ODE radius does not fit
  ($R_c = 12.57$ vs box half-size $1.57$); the box threshold is instead
  between seed radii $0.6$ and $0.8$ at $A^*$.

The radial-envelope study (`critical-droplet/report.md`) independently
found a stationary radial saddle of radius $R_{eq} = 13.53$ and energy
$550.93$, with one positive radial eigenvalue, and $2\%$ radial
contraction/dilation deciding decay/growth. Its headline warning is
adopted here verbatim in substance: **a deterministic separatrix is not
a stochastic waiting time, and the saddle energy is not automatically
the activation exponent of an unspecified noise process.** This task
supplies the specified noise process and measures the waiting times.

The open question this task addresses is IX.5.2 in the manuscript
programme: what supplies the nucleation event? This report answers it
only inside the stated models: a defined conserved noise supplies it,
with the waiting-time law measured below. Whether any such noise exists
in the physical early-universe setting of IRH is NOT addressed here.

## 2. Noise definitions (the load-bearing choices)

Both routes use noise whose definition is written down before any run,
with its conservation properties checked numerically, not asserted.

### Route A — full 4D Model B, conserved band-limited noise

The deterministic base is `d4model.ModelB` ($N = 16$, $L = \pi$,
$q_0^2 = 8.0$, $dt = 0.005$), including the Hermitian-symmetry fix of
Task 4. Per step, after the deterministic semi-implicit update, add

$$ \Delta\hat{\psi}(k) = \sqrt{2 D\, dt}\; N^2 \sqrt{K^2(k)}\;
   \mathrm{filt}(k)\; z(k), $$

where $z$ has independent $\mathcal{N}(0,1)$ real and imaginary parts on
the Fourier grid, Hermitian-symmetrised with the same roll/conjugate map
as `ModelB.step`, and $\mathrm{filt}(k) = 1$ for $4 \le K^2 \le 16$,
else $0$. The $\sqrt{K^2}$ factor is the Fourier form of the divergence
of a random flux (Model B conserved noise); the $k = 0$ term is
identically zero, so the spatial mean $\bar{\psi}$ is exactly conserved
by the noise. The band limit is a deliberate choice, in the choice
ledger: unfiltered white flux noise was tested first and rejected,
because it injects most power at grid scale — at $D = 10^{-5}$ it gave
$F_{exc} \approx 2.4$ with shell amplitude $0.0000$ (pilot, §6), i.e. it
heats the grid, not the pattern. The band $4 \le K^2 \le 16$ contains the
shell ($K^2 = 8$, 24 modes) and its nearest sidebands (88 modes total),
the modes that can carry an envelope modulation in this box.

$D$ is a **model noise strength**, not a temperature: no
fluctuation–dissipation relation to a physical bath is assumed, and no
physical rate is derived from it. Calibrated per-step increments
(`scripts/calibrate_noise.py`, 20 draws per $D$): $D = 0.01$ gives
$\psi$-increment rms $0.00125$; $D = 0.1$, $0.00387$; $D = 1$, $0.01225$;
rms scales as $\sqrt{D}$ as defined. Mean increment is $0$ to
$10^{-20}$ and $\max|\mathrm{Im}\,\psi| \le 2\times10^{-18}$.

### Route B — collective-coordinate Langevin in radial dilation

Coordinate $\lambda$: $A_\lambda(\rho) = A_c(\rho/\lambda)$, where $A_c$
is the Task-4 ODE critical profile. $\lambda = 1$ is the saddle;
$\lambda < 1$ contracts (deterministic decay) and $\lambda > 1$ dilates
(deterministic growth) — this is the documented unstable direction.
Energy $E(\lambda) = 2\pi^2 \int \rho^3 [(\kappa/2)(A_\lambda')^2 +
V(A_\lambda)]\, d\rho$, $V = f_{mod}$, computed on a grid and splined.
Metric $\gamma = 2\pi^2 \int \rho^3 (\rho A_c')^2\, d\rho = 5800.74$ at
$\lambda = 1$. Dynamics (overdamped, model temperature $T$):

$$ \gamma \frac{d\lambda}{dt} = -E'(\lambda) + \sqrt{2\gamma T}\; \eta(t),
\qquad \langle \eta(t)\eta(t') \rangle = \delta(t-t'). $$

Euler–Maruyama, $dt = 0.02$, start $\lambda_0 = 0.10$ (uniform state).
Transition event: first $\lambda \ge 1.10$ (committed past the saddle);
first $\lambda \ge 1.0$ also recorded. $T$ is a model temperature for
this one coordinate, not a physical temperature.

## 3. Re-verification of the deterministic inputs (gate)

Run by `scripts/verify_params.py` (conda env Python 3.11.16, numpy
2.4.6, exit 0; full output `tables/verify_params.json`):

| quantity | re-verified value | prior value | verdict |
|---|---|---|---|
| $r_{eff}(-0.18)$ | $0.1072$ | $0.1072$ | PASS |
| $u_{eff}(-0.18)$ | $1.54$ | $1.54$ | PASS |
| $A^*$ | $0.0775752963$ | $0.0775752963$ | PASS |
| $f_{mod}(A^*)$ | $-0.0076322673$ | $-0.0076322673$ | PASS |
| spinodal $\bar{\psi}$ | $-0.14392737$ | $-0.1439$ | PASS |
| $r_{eff}(-0.10)$ | $-0.12$ | $-0.12$ | PASS |
| barrier-top $A_{small}$ | $0.00980059$ | $0.0098$ | PASS |
| $f_{mod}(A_{small})$ | $3.86\times10^{-5}$ | — (barrier height density) | PASS |
| $\sum_g (g\cdot\hat{n})^2 = 48$ | $48.0$, $96.0$ for $\hat{n}=(1,1,0,0)$ | $\kappa/2 = 96$ | PASS |
| ODE $\Delta F^*$ (trapezoid on solver grid) | $555.1993$ | $555.2$ | PASS |
| ODE $\Delta F^*$ (Simpson, dense interpolant to $r=55$) | $554.6642$ | $554.71$ (Task 4) | PASS (0.1%) |
| ODE $R_c$ ($A = A^*/2$) | $12.5709$ | $12.57$ | PASS |
| ODE $A(0)_c$ | $0.0566046$ | $0.056605$ | PASS |
| seeded full pattern, 200 Model B steps | $D_4 = 0.99998$, rms $= 0.3806$, $F_{exc} = -0.007728$ | $D_4 = 1.000$, rms $= 0.381$, $F_{exc} = -0.007728$ | PASS |
| uniform state, 200 Model B steps, $D = 0$ | rms $= 2.8\times10^{-17}$, amp $= 0$ | stable uniform | PASS |

## 4. Route B results — the Arrhenius law recovers the saddle barrier

$E(\lambda)$ rises monotonically from $E(0) = 0$ to the saddle maximum
$E(1) = 555.20$ (spline value $555.04$) and then falls steeply
($E(1.4) = 18.4$, $E(1.6) = -919$). Deterministic checks (RK4 on the
splined drift): $\lambda_0 = 0.98 \to 0.02$ in $t = 14.5$ (decay);
$\lambda_0 = 1.02 \to 1.65$ in $t = 3.5$ (growth). The saddle is a
separatrix of this one-coordinate flow, as in the radial-envelope study.

Kramers prediction from the computed curvatures
($E''(0) \approx 2221$ from the small-$\lambda$ fit
$E \approx 1110.6\,\lambda^2 - 542.4\,\lambda^4$; $E''(1) = -6722$ by
direct finite difference, $-4432$ from the smoothed spline):
$\tau_K(T) = (9.4\text{--}11.6)\,\exp(555/T)$.

Waiting times to $\lambda \ge 1.10$, 20 replicates per $T$, seeds pinned
(`scripts/routeB.py`, $dt = 0.02$):

| $T$ | mean $\tau$ | median $\tau$ | std | CV | $\tau_K$ pred. | mean/pred. |
|---|---|---|---|---|---|---|
| 120 | 755.1 | 507.1 | 705.6 | 0.93 | 1185.4 | 0.64 |
| 160 | 169.7 | 68.1 | 242.2 | 1.43 | 373.0 | 0.45 |
| 220 | 84.7 | 68.7 | 68.7 | 0.81 | 144.8 | 0.59 |
| 300 | 41.4 | 35.1 | 34.5 | 0.83 | 73.9 | 0.56 |

All 80/80 replicates transited within $t_{max}$ (4000 / 2000 / 1200 /
800). Distributions are broadly exponential (CV $0.81$–$1.43$ vs $1$
for exponential; median/mean $0.40$–$0.85$ vs $0.693$), as expected for
a rare-event first passage at $n = 20$.

Arrhenius fit $\log\langle\tau\rangle = (567.0)(1/T) + 1.797$,
residuals $+0.105, -0.207, +0.065, +0.037$ in $\log\tau$:
**effective barrier from the slope $= 567$, against the deterministic
saddle $\Delta F^* = 555.20$.** A bootstrap over the waiting times
(10,000 resamples, `scripts/bootstrap_routeB.py`) gives a 68\% interval
$[510, 617]$ and a 95\% interval $[456, 670]$ for the slope, so the
point estimate sits $2\%$ from $555.20$ but the interval is wide: the
correct statement is that the slope is *consistent* with $\Delta F^*$
at the available $n = 20$ per $T$, not that it verifies it to $2\%$.
$P(\text{slope within 5\% of } 555.2) = 0.39$ under the bootstrap. Prefactor from the
intercept $= 6.0$, against Kramers $9.4$–$11.6$ (factor $1.6$–$1.9$ low;
the prefactor inherits the $E''(1)$ spline-vs-finite-difference spread
and the $\lambda \ge 1.10$ vs saddle-crossing definition, so it is
reported as order-of-magnitude agreement, not a verification).
Median-based fit gives slope $492$, prefactor $8.7$ — the slope is
sensitive to the estimator at $n = 20$; the mean-based slope is the
primary number and the median fit is retained as a sensitivity check.

Transition paths (Figure 1d, median of the first 5 replicates per $T$,
aligned at crossing): $\lambda$ wanders at $0.1$–$0.4$ for most of the
wait, then rises from $\sim 0.4$ to $1.10$ in the last $\sim 3$–$5$
time units. The wait is spent below the saddle; the crossing itself is
fast — the qualitative signature of nucleation rather than gradual
growth. The lag between first $\lambda \ge 1.0$ and $\lambda \ge 1.10$
is small (median lag $< 1$ time unit in most replicates; a few
recrossing replicates show lags up to $\sim 2000$ at $T = 120$, e.g.
rep 10: $t_1 = 498$, $t_{110} = 2757$).

## 5. Route A results — the box transition is a homogeneous crossing

Scan (`scripts/routeA.py`, 5 replicates per $D$, 2500 steps max,
$t_{max} = 12.5$, uniform start, seeds pinned; the $D = 3$ and $D = 10$
pilot replicates are additional, separately-seeded runs):

| $D$ | transited (amp $\ge 0.04$, confirmed) | waiting times $t$ | pre-transition mean amp | OU rms pred. $0.012\sqrt{D}$ | final amp (transited) / range (not) |
|---|---|---|---|---|---|
| 0.03 (pilot, console record) | 0/1 | — | — | 0.0021 | rms $= 0.010$, $D_4 = 0.947$, $F_{exc} = 0.0001$ |
| 0.1 | 0/5 | — | 0.0033 | 0.0038 | 0.0028–0.0046 |
| 0.3 | 0/5 | — | 0.0060 | 0.0066 | 0.0045–0.0117 |
| 0.5 | 2/5 | 11.0, 12.5 (mean 11.75) | 0.0093 | 0.0085 | 0.0084–0.0318 (non-transited; see text) |
| 0.7 | 3/5 | 6.0, 7.0, 8.5 (mean 7.17, median 7.0) | 0.0110 | 0.0100 | 0.0066–0.0143 (non-transited) |
| 1.0 | 5/5 | 4.0, 5.5, 2.5, 7.0, 4.5 (mean 4.7, median 4.5) | 0.0137 | 0.0120 | 0.0767–0.0788, rms 0.376–0.387, $F_{exc} = -0.0051$ to $-0.0039$ |
| 3.0 | 5/5 scan (+2/2 pilot) | scan: 3.5, 1.5, 2.0, 2.5, 3.0 (mean 2.5); pilot: 2.0, 3.0 | 0.0206 | 0.0208 | 0.0751–0.0794, $F_{exc} = -0.0012$ to $+0.0029$ |
| 10 (pilot) | 2/2 | 1.5, 1.0 | 0.0344 | 0.0379 | 0.0795–0.0811, rms 0.396–0.405, $F_{exc} = +0.011$ to $+0.017$ |

The transition fraction rises in a graded crossover inside the
observation window $t \le 12.5$: $0/5$ at $D = 0.1$ and $0.3$, $2/5$
at $D = 0.5$, $3/5$ at $D = 0.7$, $5/5$ at $D = 1.0$ and $3.0$. This is
not a gradual Arrhenius tail — the fraction goes from $0$ to $1$ over
a factor of $\sim 3$ in $D$ — and the crossover sits where the
stationary fluctuation crosses the homogeneous barrier top: the
measured pre-transition mean shell amplitude (Figure 2c) tracks the
Ornstein–Uhlenbeck prediction $0.012\sqrt{D}$ (rms; mean-$|$amp$|$ is
$0.886\times$ that) to $\sim 10\%$ at every $D$ — $0.0033$ vs $0.0038$
at $D = 0.1$, $0.0060$ vs $0.0066$ at $D = 0.3$, $0.0093$ vs $0.0085$
at $D = 0.5$, $0.0110$ vs $0.0100$ at $D = 0.7$, $0.0137$ vs $0.0120$
at $D = 1$, $0.0206$ vs $0.0208$ at $D = 3$. (The $D \ge 0.5$ means
include the growth ramp before the event sample, so they sit slightly
high.) The barrier top is $A_{small} = 0.0098$: at $D = 0.3$ the
stationary rms ($0.0066$) sits below it and no replicate transits; at
$D = 0.5$ it sits just below it ($0.0085$) and barrier-top crossings
are already $5/5$ while commitments are only $2/5$; at $D = 1$ it
sits above it ($0.0120$) and every replicate commits in $t \le 7$.

Three findings follow from the scan:

1. **$D_4$ is not a transition indicator under band noise.** At
   $D = 0.1$ the final states have $D_4 = 0.938$–$0.987$ with
   rms $= 0.016$–$0.026$ and amp $\le 0.0046$: the noise lives in the
   band, the shell modes are the least damped band modes, so the shell
   power fraction saturates while the amplitude is still more than an
   order of magnitude below $A^*$. The same holds at $D = 0.3$
   ($D_4 = 0.932$–$0.987$). The event criterion used throughout is
   therefore amplitude-based (amp $\ge 0.04$, confirmed at the next
   sample $100$ steps later), with $D_4$ and rms reported only as
   secondary diagnostics. Any reading of these runs by $D_4$ alone
   would be a false positive.
2. **Crossing the barrier top is necessary but not sufficient in the
   full field — commitment is a second, slower step.** Barrier-top
   crossings (first amp $\ge 0.0098$) vs commitments (amp $\ge 0.04$):
   $D = 0.1$: $0/5$ crossed, $0/5$ committed; $D = 0.3$: $1/5$ crossed,
   $0/5$ committed; $D = 0.5$: $5/5$ crossed, $2/5$ committed;
   $D = 0.7$: $5/5$ crossed, $3/5$ committed; $D = 1$: $5/5$ crossed,
   $5/5$ committed. Of the six replicates that crossed without
   committing by $t = 12.5$, three had fallen back below $A_{small}$ by
   the end ($D = 0.5$ reps 1, 3; $D = 0.7$ rep 3), two were still
   hovering above it ($D = 0.3$ rep 1, final amp $0.0117$; $D = 0.7$
   rep 2, final amp $0.0143$), and one was mid-growth and censored by
   the window ($D = 0.5$ rep 4, final amp $0.0318$). The lag between
   barrier-top crossing and commitment, for replicates that did commit,
   shrinks with $D$: $6.5$ and $9.5$ at $D = 0.5$; $4.0$–$5.0$ at
   $D = 0.7$; $1.5$–$5.5$ at $D = 1$; $1.0$–$3.0$ at $D = 3$;
   $0.5$–$1.0$ at $D = 10$. The homogeneous amplitude equation says
   amp $> A_{small}$ grows; the full field says a fluctuation that
   crosses $A_{small}$ in mean amplitude, with random phases and
   sideband content, must then survive a dwell of several time units
   while phase coherence builds, and can still decay. Commitment
   requires the larger, phase-coherent amplitude amp $\ge 0.04$ used
   as the event here. The homogeneous barrier is therefore a lower
   bound on what the noise must do, not the whole story — and the
   $D = 0.5$ waiting times ($11.0$, $12.5$) are the closest this box
   comes to genuine rare-event nucleation waiting times.
3. **The homogeneous barrier in the box is tiny.** The uniform-amplitude
   barrier top is $A_{small} = 0.0098$ with barrier-height density
   $f_{mod}(A_{small}) = 3.86\times10^{-5}$; over the box volume
   $\pi^4 \approx 97.4$ that is a total homogeneous barrier of
   $\approx 0.0038$ in model energy units — five orders of magnitude
   below the droplet barrier $555$. The box transition is therefore a
   spatially near-uniform shell-amplitude crossing, not a droplet
   crossing: the noise only has to push the shell amplitude past
   $\sim 0.01$, after which the cubic term drives growth to $A^*$.
   This is why $D = 1$ nucleates in $t \approx 2$–$7$ while the same
   noise strength in the radial-envelope model would give
   $\tau \sim e^{555/T}$ with no comparable $T$. The scale mismatch of
   Task 4 persists under noise, in the precise form: box waiting times
   measure the homogeneous barrier $\sim 0.004$, not $\Delta F^* = 555$.
   At $D \ge 1$ the waiting times ($1$–$7$) are not rare-event
   waiting times in the Kramers sense — they are of the order of the
   deterministic growth time itself — so no Arrhenius fit is attempted
   for Route A. The rare-event regime is at the crossover: at
   $D = 0.5$ the waiting times are $11.0$ and $12.5$ with $3/5$
   censored, and the commitment lag after barrier-top crossing is
   $6.5$–$9.5$ time units — a dwell, not a direct crossing.

Transition paths (Figure 2b, first replicate per $D$): at $D \ge 1$ the
shell amplitude rises from the stationary level through $A_{small}$ to
$A^*$ in $\sim 2$–$4$ time units and then fluctuates around $A^*$ with
noise-driven excursions; at $D = 0.1$/$0.3$ it wanders below $0.012$ for
the whole run. The ordered end states at $D = 1$ have
$F_{exc} \approx -0.005$, part-way to the noiseless $-0.00773$; at
$D = 3$ the end $F_{exc}$ scatters around $0$, and at $D = 10$ it is
$+0.011$ to $+0.017$ — the fluctuation energy in the noisy ordered
state grows with $D$ and eventually exceeds the ordering gain, so
$F_{exc}$ must not be read as an order parameter at high $D$ either.
$\bar{\psi}$ is conserved exactly in every run
($\max|\bar{\psi} + 0.18| = 0.0$ over all sampled series).

## 6. Checks run

| check | verdict |
|---|---|
| Parameter re-verification (§3, 14 quantities) | PASS |
| ODE barrier by two quadratures (555.20 vs 554.66) | PASS |
| $\kappa$ moment identity ($48$, $96$) | PASS |
| Deterministic seeded pattern / uniform stability (200 steps) | PASS |
| Noise calibration: rms $\propto \sqrt{D}$, mean $0$, imag residue $\le 2\times10^{-18}$ | PASS |
| Noise conservation: $\bar{\psi}$ deviation exactly $0.0$ over all pilot series (max $|\bar{\psi}+0.18| = 0.0$) | PASS |
| White flux noise rejected: $F_{exc} \approx 2.4$ at $D = 10^{-5}$, shell amp $0$ | PASS (as a rejection — the definition was changed on this evidence) |
| Route B deterministic separatrix: $0.98 \to$ decay, $1.02 \to$ growth | PASS |
| Route B Kramers slope $567$ vs $\Delta F^* = 555.20$ | PASS (consistent within bootstrap 68\% interval $[510,617]$) |
| Route B prefactor $6.0$ vs Kramers $9.4$–$11.6$ | PASS as order-of-magnitude (factor $< 2$) |
| Route A pilot: $D = 3$ grows to ordered state, amp $0.077$–$0.078$ | PASS |
| Route A scan + extension: fractions 0/5, 0/5, 2/5, 3/5, 5/5, 5/5 at $D = 0.1, 0.3, 0.5, 0.7, 1, 3$; pre-transition amp tracks OU $0.012\sqrt{D}$ to $\sim 10\%$ at all 7 $D$ values | PASS |
| Route A: barrier-top crossing vs commitment counted per $D$ (6 crossed-without-committing; lags shrink with $D$) | PASS (recorded as a finding, §5) |
| Route A scan across $D$ (waiting-time curve, $D = 0.1, 0.3, 1, 3$; 5 reps each) | PASS (exit 0; 20/20 runs completed, see §5) |
| Route A extension scan ($D = 0.5, 0.7$; 5 reps each) | PASS (exit 0; 10/10 runs completed, see §5) |
| Independent external verification (Manus/Gemini/Co-scientist) | NOT RUN — this is the local-independent leg; must not be read as external verification |

Tool verdicts quoted: conda env Python 3.11.16, numpy 2.4.6,
scipy 1.17.1, matplotlib 3.11.2; `verify_params.py` exit 0;
`routeB.py` runs exit 0 (80/80 transited); `routeA.py` pilot runs exit
0 for completed $D$ values. Load note: the shared VM ran at load
average $\approx 14$ during the Route A pilot, so per-run wall times
($\sim 240$–$380$ s per 2500-step run) are load-inflated; the numbers
reported are step counts and model times, which are load-independent.

## 7. Rival / failure mode

1. **Route B is a one-coordinate reduction.** The dilation coordinate
   is the documented unstable direction, but the true stochastic
   transition path in the full radial PDE could use amplitude, width,
   and mean-shift directions the coordinate freezes. The $2\%$
   agreement of the fitted slope with $\Delta F^*$ is evidence that
   the coordinate captures the barrier, not proof that it captures the
   path: a different coordinate with the same barrier height would give
   the same slope. The prefactor disagreement (factor $\sim 2$) is the
   visible trace of the missing directions.
2. **Route A band noise is a choice, not a derivation.** A different
   band (e.g. shell-only, or a Gaussian in $K^2$) would shift the
   waiting times at fixed $D$ by an order-unity factor or more, because
   it changes which modes carry the fluctuation. The waiting-time *curve
   shape* (crossover where stationary amp crosses $A_{small}$) is
   robust to that choice; the absolute $D$ values are not.
   White (unfiltered) noise is the rival that fails outright (§2, §6).
3. **The box cannot host a droplet.** Any Route A waiting time is a
   homogeneous-crossing time. Presenting it as a droplet nucleation
   rate would be the same conflation Task 4 warned against, now with
   noise added. The honest statement is the two-barrier picture of §5.
4. **$T$ and $D$ are not physical.** No temperature, no physical rate,
   no cosmological timescale follows from either route without an
   additional, separately justified mapping from model noise to a
   physical bath — which does not exist in the manuscript at v93.1.
   IX.5.2 remains open as a physics question; this task closes only the
   model question: *given* this noise, the waiting-time law is as
   measured.

## 8. Evidence that would change the answer

- A full radial-PDE stochastic run (noise on $A(\rho,t)$ and $c(\rho,t)$
  with the stated fluctuation–dissipation weights) whose Arrhenius slope
  differs from $555$ by more than the Route B fit scatter would show the
  dilation coordinate is not the barrier coordinate; a slope within
  $\sim 5\%$ would strengthen Route B to a cross-route result.
- A larger-box ($L = 2\pi$, $N = 32$) Route A run in which the waiting
  times at fixed $D$ lengthen toward the droplet law would show the box
  barrier growing with volume toward $\Delta F^*$; if they do not, the
  homogeneous channel dominates at all accessible volumes. Costed, not
  run — see §9.
- If Route A at some $D$ showed transitions whose paths are spatially
  localised droplets (envelope concentrated in a sub-volume, growing by
  wall motion) rather than uniform amplitude growth, the §5
  homogeneous-crossing reading would need revision; the pilot paths
  show uniform growth, and the scan paths are the test.

## 9. Costed follow-up (pending, no GCP spend authorised or used)

- **Route A scan: DONE locally** ($D \in \{0.1, 0.3, 1.0, 3.0\}$,
  5 replicates each, 2500 steps max with early stop on confirmed
  transition; exit 0; wall $\approx 23$ min including the slow-load
  phase; compute cost \$0, local VM, no GCP). The $D = 0.5$/$0.7$
  extension scan (5 replicates each, same protocol) is DONE locally
  (exit 0; wall $\approx 10$ min; cost \$0).
- **Longer-window Route A at $D = 0.5$ (uncensor the rare-event tail):**
  $t_{max} = 25$ (5000 steps), 5 replicates, same protocol; at the
  measured $\sim 65$–$260$ s per 2500 steps, $\approx 20$–$45$ min wall
  locally. **Cap: \$0 authorised (local only); pending — not run.**
- **Full radial-PDE stochastic run:** prototype first on
  $L = 60$, $dr = 1.0$, $dt = 0.001$, $T \in \{150, 200, 300\}$;
  a single run to $t = 1000$ is $10^6$ steps $\times \sim 40$ cells —
  prototype costed at $\sim 10$–$20$ min locally per run after
  vectorisation; the full waiting-time scan (20 replicates $\times$
  3 $T$) is a GCP-scale job. **Cap: \$0 authorised; cost the full run
  first and report the cap to Brandon before any spend — pending.**
- **Larger-box Route A ($L = 2\pi$, $N = 32$):** $16\times$ the grid
  points of $16^4$; at the measured $\sim 8$ ms/step (unloaded) a
  2500-step run is $\sim 5$–$10$ min unloaded per replicate on this
  machine, $\sim 3\times$ that under current load — a local overnight
  batch at most, or GCP. **Cap: \$0 authorised; local batch to be
  costed by measured step time before starting — pending.**

## 10. HLRE grades (per narrow claim; worst-of shown)

Track E unless noted; independence I1 (all verification artificial,
single local pipeline; external verification NOT RUN — this is the
local-independent leg, and its grades do not borrow anything from the
parallel Co-scientist leg).

| claim | grade | basis (bound / caps / ceiling / record) |
|---|---|---|
| $r_{eff} = 0.1072$, $A^* = 0.0775753$, $f_{mod}(A^*) = -0.00763227$ | B | re-derived from `d4model` + two-quadrature ODE check; narrow, exact-arithmetic claims |
| $\kappa = 192$ (moment identity $48/96$) | B | exact integer moment sums; derivation mine, checked |
| ODE $\Delta F^* = 555.20$, $R_c = 12.57$ | B | two quadratures agree to 0.1%; amplitude-equation truncation-limited |
| $E(\lambda)$ has its maximum $555.20$ at $\lambda = 1$; $0.98$ decays, $1.02$ grows | B | direct quadrature + deterministic RK4 separatrix check |
| Route B waiting times are exponential-like with Arrhenius slope $567 \approx \Delta F^*$ | B | 80/80 transited, 4 $T$ values, fit residuals $\le 0.21$ in $\log\tau$; bootstrap 68\% slope interval $[510,617]$ contains $555.20$; slope is a fit, not a derivation — ceiling B, not A |
| Route B Kramers prefactor $6.0$ vs $9.4$–$11.6$ | C | order-of-magnitude agreement only; curvature-estimate spread is a live systematic |
| Route A noise is conserved (mean exact) and band-limited as defined | B | definition + calibration table + $\bar{\psi}$ deviation exactly $0.0$ in every run |
| Route A: $D = 1$ nucleates in $t = 2.5$–$7.0$ (5/5); $D = 3$ in $t = 1.5$–$3.5$ (5/5 scan + 2/2 pilot); $D = 0.1$/$0.3$ do not in $t = 12.5$ (0/5 each) | B | direct runs, $n = 5$ per $D$ (scan) + pilot; event amp-based and confirmed; narrow claim, stated as box result only |
| Route A waiting-time curve vs $D$ (graded crossover $0/5, 0/5, 2/5, 3/5, 5/5, 5/5$ at $D = 0.1, 0.3, 0.5, 0.7, 1, 3$, tracking stationary amp crossing $A_{small}$) | B | measured fractions + OU check to $\sim 10\%$ at 7 $D$ values (scan + extension + pilot); $n = 5$ per $D$ |
| Route A: crossing $A_{small}$ is not sufficient for commitment (6 crossed-without-committing; commitment lags $6.5$–$9.5$ at $D = 0.5$ shrinking to $0.5$–$1.0$ at $D = 10$) | B | counted per $D$ over 34 replicates; the phase-coherence mechanism for the lag remains an interpretation, so the mechanism claim itself stays C (see §7) |
| Box transition is a homogeneous shell-amplitude crossing, barrier $\approx 0.0038$, not a droplet crossing | B | exact barrier-top computation + box-volume arithmetic + pilot paths (uniform growth); the "not a droplet" part is a scale argument, stated as such |
| The noise supplies a nucleation mechanism for IRH in the physical early universe | ABSTAIN | no mapping from model noise to a physical bath exists in the record; IX.5.2 stays open as physics |
| Any physical nucleation rate / cosmological timescale from these runs | ABSTAIN | $D$ and $T$ are model strengths with no assigned physical units |

## 11. UNVERIFIED / ABSTAIN list

- Route A waiting times at $D = 0.5$ beyond $t = 12.5$ (3/5 censored;
  a longer window, $t_{max} = 25$, would resolve the rare-event tail —
  costed in §9).
- Route A transition-path localisation (droplet vs uniform) at the
  crossover $D$ — the paths so far show uniform amplitude growth, not
  localised droplets; a spatial diagnostic (local amplitude map) was
  not computed.
- Route B prefactor at better than factor-2 accuracy (needs the
  curvature systematic resolved and $n \gg 20$ per $T$).
- Full radial-PDE stochastic nucleation (not run; costed in §9).
- Larger-box Route A (not run; costed in §9).
- External verification of every claim in this report (not run; this
  leg is deliberately independent of the parallel leg).
- Any physical interpretation of $D$ or $T$ (ABSTAIN, §10).

## 12. Assumption / parameter / choice ledger

- Operating point $(\bar{\psi}, r) = (-0.18, -0.35)$, $u = v = 1$,
  $q_0^2 = 8.0$, $A^* = 0.0776$ — manuscript / repo verification code,
  re-verified §3.
- $\kappa = 192$ — derived and verified (Task 4 route A, re-checked §3).
- Route A: $N = 16$, $L = \pi$, $dt = 0.005$, uniform start
  $\bar{\psi} = -0.18$; noise band $4 \le K^2 \le 16$ (88 modes),
  $\sqrt{K^2}$ (divergence) factor, Hermitian symmetrisation;
  event amp $\ge 0.04$ confirmed at next sample; $D_4$/rms secondary.
- Route B: $\lambda$ dilation of the ODE critical profile;
  $E(\lambda)$ by trapezoid on the solver grid, splined ($s = 0.5$);
  $\gamma = 5800.74$; Euler–Maruyama $dt = 0.02$, start
  $\lambda_0 = 0.10$; event $\lambda \ge 1.10$; $T \in \{120,160,220,300\}$,
  20 replicates each, seeds $3000 + 100\times$index.
- Fitted numbers are fits: Arrhenius slope $567$ and prefactor $6.0$
  are regression outputs with the residuals stated in §4, not inputs.
- No manuscript edits, no commits, no filings were made. All work is
  local; no GCP spend.

## 13. Deliverables

- This report: `REPORT.md`
- Scripts: `scripts/verify_params.py`, `scripts/calibrate_noise.py`,
  `scripts/bootstrap_routeB.py`,
  `scripts/routeB.py`, `scripts/routeA.py`, `scripts/analyze_routeB.py`,
  `scripts/analyze_routeA.py`, `scripts/fig_routeB.py`,
  `scripts/fig_routeA.py` (all pinned seeds; conda env Python 3.11.16).
  Also in the work dir: `scripts/pilot_noise.py` (the rejected
  unfiltered-white-noise pilot, §2/§6) and `tables/routeB_smoke*.json`
  (superseded Route B smoke runs, retained for provenance).
- Tables: `tables/verify_params.json`, `tables/routeB_Egrid.npz`,
  `tables/routeB_T{120,160,220,300}.json`, `tables/routeB_summary.json`,
  `tables/routeA_pilot2.json` (the first pilot's JSON was lost when that
  process was killed; its $D = 0.03$ console result is quoted in §5 as a
  console record),
  `tables/routeA_scan.json`, `tables/routeA_scan2.json`,
  `tables/routeA_summary.json/.csv`
- Figures: `figures/routeB_waiting_times.png`,
  `figures/routeA_waiting_times.png`
