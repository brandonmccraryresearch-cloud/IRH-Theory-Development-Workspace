# Task 3 — Critical $D_{4}$ seed in the full field

## CLAIM

At the operating point $(\bar{\psi}, r) = (-0.18, -0.35)$, $u = v = 1$, $q_{0}^{2} = 8$,
in the periodic $L = 2\pi$ four-dimensional conserved Model B field (dealiased
Fourier–Galerkin, $|k_{i}| \leq 4$, $18^{4}$ collocation points), a localized,
phase-locked $D_{4}$ patch of per-mode amplitude $\alpha = 1$ ($A^{*} = 0.0775753$)
with a $\tanh$ envelope of sharpness $4.0$ dissolves for every tested nominal
radius $R \leq 2.5875$ and grows to the stationary full 24-mode ordered state for
$R \geq 2.625$. The direct field threshold is therefore bracketed as

$$R_{c,\mathrm{field}} \in (2.5875,\ 2.625]\quad (\alpha = 1,\ L = 2\pi),$$

i.e. $1.165$–$1.182$ resonant wavelengths ($\lambda = 2\pi/\sqrt{8} = 2.22144$),
with equivalent sharp-ball radii $R_{\mathrm{eq}} \in (2.483,\ 2.521]$.
This is a **finite-box** threshold. It is **not** the infinite-volume envelope
critical radius: the radial-envelope predictions are $R_{c} = 12.57$ (radial ODE,
Task 4), $R_{c} = 7.38$ (thin-wall, shown to fail), and a seed threshold of
$R \in (16.19,\ 16.21]$ with saddle $R_{\mathrm{eq}} = 13.53$
(critical-droplet envelope report) — $4.8\times$–$6.2\times$ larger than the
field bracket. The two numbers live in different regimes and must not be
conflated: the envelope assumes an infinite domain and a wall of width
$w = 6 \approx 2.7\lambda$, while the field bracket is set by a patch that
already fills most of a $2\pi$ box whose half-size is $\pi = 3.14$, and by
periodic-image overlap. Raising the seed amplitude to $\alpha = 1.5$ does not
rescue small seeds in this box: $R = 0.6$–$1.5$ all dissolve.

## STATUS

**VERIFIED (as a finite-box field bracket, Track E grade B for the bracket
itself; see §9).** All 11 $\alpha = 1$ main-grid runs completed at $t = 200$
with 0 rejected steps; both bracket endpoints are confirmed at half timestep;
the growing endpoint is confirmed at $K = 6$, $N = 28$ (final
$F_{\mathrm{exc}} = -0.007727623601$, the field test's $K = 6$ value);
an independent
semi-implicit solver reproduces both ends of the bracket in the same box and
reproduces Task 4 growth in the $L = \pi$ box. The envelope comparison is
stated, not conflated. **NOT established:** any infinite-volume critical
radius from this field (the box cannot contain one), a nucleation rate, a
stochastic waiting time, or a threshold for other envelope widths,
orientations, or unequal-mode seeds.

## 1. Derivation (each step checkable)

### 1.1 Operating point and field equations (from prior sources, verified here)

The prior 4D field test fixes $r = -0.35$, $\bar{\psi} = -0.18$, $q_{0}^{2} = 8$,
$u = v = 1$, mobility $1$, box $[0, 2\pi]^{4}$, $\phi = \psi - \bar{\psi}$
(`4d-field-test/parameters.json`, `report.md`). The excess energy density is

$$f = \tfrac{1}{2}\textstyle\sum_{k} [\alpha + (8 - |k|^{2})^{2}]\,|\hat{\phi}_{k}|^{2} - \beta \langle \phi^{3} \rangle / 3 + \langle \phi^{4} \rangle / 4,$$

with $\alpha = r - 2\bar{\psi} + 3\bar{\psi}^{2} = 0.1072$ and
$\beta = u - 3v\bar{\psi} = 1.54$, and Model B dynamics
$\partial_{t}\hat{\phi}_{k} = -|k|^{2}\{[\alpha + (8-|k|^{2})^{2}]\hat{\phi}_{k} - \beta \widehat{P(\phi^{2})}_{k} + \widehat{P(\phi^{3})}_{k}\}$.
These were re-verified arithmetically in `verify_envelope.py` (numpy roots and
`scipy.optimize.brentq` agree on $A^{*}$ to the printed precision;
$r_{\mathrm{eff}}(-0.18) = 0.1072$, $\beta = 1.54$ reproduced exactly).

### 1.2 One-mode amplitude $A^{*}$

The one-mode Landau density
$f_{\mathrm{mod}}(A) = 12\,r_{\mathrm{eff}} A^{2} - 64\,u_{\mathrm{eff}} A^{3} + 846\,A^{4}$ (with $N/2 = 12$, $T/3 = 64$, $Q/4 = 846$) has stationary
points from $d f_{\mathrm{mod}}/dA = 0$. Two independent routes give

$$A^{*} = 0.077575296339281, \qquad f_{\mathrm{mod}}(A^{*}) = -0.0076322673,$$

agreeing with the prior value $0.07757529633928076$ / $-0.007632267319$ and
with the field-test analytic amplitude. The relaxed full-branch energy in
the field is $-0.007726209285$ (field test) — the $1.25\%$ harmonic
relaxation quoted there.

### 1.3 Seed definition

For nominal radius $R$ and amplitude factor $\alpha$, on the $18^{4}$ grid,

$$\psi(x) = \bar{\psi} + \alpha A^{*}\,\mathrm{env}(\rho)\,
  \sum_{g \in \Phi_{D_{4}}} \cos(g \cdot x), \qquad
  \mathrm{env}(\rho) = \tfrac{1}{2}\bigl[1 - \tanh\bigl(4(\rho - R)\bigr)\bigr],$$

where $\rho$ is the Euclidean distance from the box centre
$(\pi,\pi,\pi,\pi)$, $\Phi_{D_{4}}$ is the 24-vector shell
$(\pm 2, \pm 2, 0, 0)$ and permutations, and the mean is then restored
exactly to $\bar{\psi}$. This is the Task 4 droplet envelope
(`task4_droplet_runs.py`: `sharp = 4.0`), transplanted from the $L = \pi$
box to the $L = 2\pi$ field-test box. The seed is projected onto the
retained band $|k_{i}| \leq 4$ before evolution, so harmonics, unequal
modes, and phase dynamics are free to evolve — the seed is not a star
restriction. The projected seed retains $90$–$99\%$ of the raw power
(`verify_seed.py`: $0.903$ at $R = 0.6$, $0.990$ at $R = 1.2$,
$0.988$ at $R = 2.4$, $0.978$ at $R = 2.7$), so projection loss is not
driving the outcomes.

Two radius conventions are reported for every run: the nominal $R$
(where $\mathrm{env} = 1/2$) and the sharp-ball equivalent
$R_{\mathrm{eq}} = (2 V_{\mathrm{env}}/\pi^{2})^{1/4}$ with
$V_{\mathrm{env}} = \int \mathrm{env}^{2}\, d^{4}x$. For the bracket
endpoints: $R = 2.5875 \to R_{\mathrm{eq}} = 2.483$;
$R = 2.625 \to R_{\mathrm{eq}} = 2.521$.

A structural fact about this seed family, visible in `seed_profile.png`:
at the centre all 24 carrier cosines align, so the local field peaks at
$24 A^{*} \approx 1.86$ there, exactly as in the full ordered branch
itself (whose rms is $\sqrt{24}\,A^{*} = 0.3805$ but whose pointwise
maximum is also $24 A^{*}$). The radially averaged local rms matches
$A^{*}\sqrt{24}\,\mathrm{env}(\rho)$ for $\rho \gtrsim 1.5$; near the
centre it is larger because the shell average has not yet averaged out
the carrier oscillations. The seed is therefore a patch of ordered phase
with the full branch's own peak structure, not a smooth low-amplitude bump.

### 1.4 Evolution and classification

Evolution reuses, by import, the field-test `Field` class and ETD2
integrator (`run_field_study.py`, sha256
`a7b03651eb4eb66efa6d59cfc6adfe6021b00b8b73babaa2dfecf154f24ef422`;
second-order exponential Heun, exact linear propagator, step-energy
rejection, startup caps $dt/1000$ until $t = 0.02$ and $dt/20$ until
$t = 0.2$; $dt = 0.1$, $t_{\mathrm{final}} = 200$). Classification uses
the field-test `outcome()` rule on the final saved state:

- **growth** = `stationary_full24`: occupancy $24$, amplitude CV
  $\leq 0.05$, triad lock $\geq 0.95$, projected RHS rms $\leq 10^{-7}$;
- **dissolve** = `uniform`: total modulation power $< 10^{-12}$.

No run ended in any other class. Decisions are fast: decaying seeds fall
below rms $10^{-3}$ by $t \approx 5$–$10$; growing seeds exceed rms $0.3$
by $t \approx 5$–$10$ (checked from `seed_trajectories.csv`). The
$t = 200$ horizon is therefore $\sim 20\times$ the decision time, not a
marginal cutoff. Occupancy alone is **not** a growth criterion: decaying
runs transiently reach occupancy $24$ (the surviving power is shell
power, because off-shell power damps first) while their rms collapses.

### 1.5 Envelope predictions to compare against (prior sources, quoted)

| Route | Value | Source |
|---|---|---|
| Thin-wall $R_{c}$ / $\Delta F^{*}$ | $7.38$ / $37.2$ (relaxed $\Delta f$: $7.29$ / $35.9$) | `ws-a-core-computations/task4_report.md` §2; arithmetic re-verified in `verify_envelope.py` from $\sigma = 0.018776$ |
| Radial-ODE $R_{c}$ ($A = A^{*}/2$) / $\Delta F^{*}$ | $12.57$ / $555$ | `ws-a-core-computations/task4_report.md` §3 (shooting; NOT recomputed here) |
| Envelope seed threshold, $\alpha = 1$, $w = 6$ | decay $16.191$, growth $16.211$ | `critical-droplet/threshold_table.csv` |
| Stationary saddle $R_{\mathrm{eq}}$ / $E$ | $13.529$ / $550.93$ | `critical-droplet/report.md` §5 |
| Correlation length $\xi = \sqrt{\kappa/(N r_{\mathrm{eff}})}$ | $8.64$ ($\kappa = 192$) | Task 4 §3; re-verified: $8.6387$ |

Thin-wall fails here because $\xi = 8.64 > R_{c} = 7.38$; the ODE value is
the exact-within-the-amplitude-equation answer. The envelope routes live
in an infinite domain ($L = 120$, $\Delta\rho = 0.5$) with a wide wall
($w = 6$); the field bracket lives in a $2\pi$ periodic box with a sharp
wall (width $0.25$). Section 6 states the comparison.

## 2. Results

### 2.1 Main bracket, $\alpha = 1$

| $R$ | $R_{\mathrm{eq}}$ | initial rms | initial $D_{4}$ fraction | initial $E_{\mathrm{exc}}$ | outcome at $t = 200$ |
|---:|---:|---:|---:|---:|:---|
| 0.6 | 0.559 | 0.02314 | 0.0141 | 0.03102 | dissolve |
| 0.9 | 0.834 | 0.04147 | 0.0200 | 0.03816 | dissolve |
| 1.2 | 1.120 | 0.05283 | 0.0231 | 0.03578 | dissolve |
| 1.5 | 1.411 | 0.05684 | 0.0267 | 0.03757 | dissolve |
| 1.8 | 1.705 | 0.06200 | 0.0381 | 0.04578 | dissolve |
| 2.1 | 2.001 | 0.07411 | 0.0607 | 0.07943 | dissolve |
| 2.4 | 2.298 | 0.09281 | 0.1069 | 0.15995 | dissolve |
| 2.55 | 2.446 | 0.10641 | 0.1473 | 0.22568 | dissolve |
| 2.5875 | 2.483 | 0.11038 | 0.1596 | 0.24297 | dissolve |
| **2.625** | **2.521** | **0.11457** | **0.1728** | **0.25982** | **grow** |
| 2.7 | 2.595 | 0.12364 | 0.2021 | 0.29120 | grow |

Full table with solver statistics: `threshold_table.csv` (main grid) and
`seed_outcomes.csv` (all runs including refinements). Growing endpoints
reach rms $0.380535$, $F_{\mathrm{exc}} = -0.007726209285$, occupancy $24$,
RHS rms $\sim 10^{-15}$ — the relaxed full branch, identical to the field
test's patterned endpoints. Dissolving endpoints reach rms $\sim 10^{-75}$
and $F_{\mathrm{exc}} \sim 10^{-151}$ — numerically uniform.

$$R_{c,\mathrm{field}} \in (2.5875,\ 2.625], \qquad
  R_{\mathrm{eq}} \in (2.483,\ 2.521], \qquad
  R_{c,\mathrm{field}}/\lambda \in (1.165,\ 1.182].$$

Bracket width $0.0375$ ($1.4\%$ of the midpoint $2.606$).

### 2.2 Amplitude sensitivity, $\alpha = 1.5$

$R = 0.6, 0.9, 1.2, 1.5$ at $\alpha = 1.5$ all dissolve (initial rms
$0.0347$–$0.0853$; final rms $\sim 10^{-77}$). In the $L = \pi$ Task 4 box
the same amplitude grew already at $R = 0.6$ — see §6 for why the boxes
differ. No $\alpha = 1.5$ bracket was attempted at larger $R$; the
$\alpha$-dependence of the field threshold above $R = 1.5$ is UNVERIFIED.

### 2.3 Why the $\pi$-box and the $2\pi$-box differ (measured, not assumed)

The same seed construction was evaluated in both boxes
(`verify_seed.py`, independent FFT shell-power computation, agreeing
with `d4model.analyze` exactly at $L = \pi$):

| Box | $R$ | shell fraction | rms |
|---|---:|---:|---:|
| $L = \pi$ | 0.6 | 0.2083 | 0.09621 |
| $L = \pi$ | 0.8 | 0.2907 | 0.14324 |
| $L = 2\pi$ | 0.6 | 0.0129 | 0.02424 |
| $L = 2\pi$ | 1.2 | 0.0229 | 0.05314 |
| $L = 2\pi$ | 2.4 | 0.1059 | 0.09352 |

For a fixed ball, the initial $D_{4}$ shell fraction scales as
$V_{\mathrm{ball}}/V_{\mathrm{box}}$: it is $16\times$ larger in the
$\pi$ box (box volume ratio $(2\pi)^{4}/\pi^{4} = 16$). A "droplet" of
$R = 0.8$ in the $\pi$ box is $29\%$ shell-concentrated and its periodic
images are only $\pi$ apart, so it behaves as a near-box-filling
perturbation; the same seed in the $2\pi$ box is $2\%$ shell-concentrated
and dissolves. The Task 4 box threshold (growth at $R \geq 0.8$,
$\alpha = 1$) is therefore a property of the $\pi$ box, and the present
bracket is a property of the $2\pi$ box. Neither is the infinite-volume
threshold.

## 3. Checks run

| Check | Result | Verdict |
|---|---|---|
| $A^{*}$ by numpy roots vs scipy brentq vs prior value | $0.077575296339281$ both routes; prior $0.07757529633928076$ | PASS |
| $r_{\mathrm{eff}}$, $\beta$, $f_{\mathrm{mod}}(A^{*})$, spinodal $-0.1439$, $r_{\mathrm{eff}}(-0.10) = -0.12$, $\xi = 8.6387$, $\lambda = 2.22144$, thin-wall $R_{c}/\Delta F^{*}$ from $\sigma$ | all reproduce prior numbers (see `verify_envelope.py` output) | PASS |
| Seed construction: this task's `build_seed` vs `d4model.seed_droplet` at $L = 2\pi$ (shell fraction, rms) | agree to 3 decimals at $R = 0.6, 1.2, 2.4$ | PASS |
| Seed construction at $L = \pi$ vs `d4model.analyze` | independent FFT shell fraction $0.208332$ = analyze $0.208332$; rms identical | PASS |
| Projection loss $|k_{i}| \leq 4$ | $90$–$99\%$ of raw power retained | PASS |
| Energy safeguard in every field run | 0 rejected steps in all 19 field runs; max step energy increase $\leq 8.7\times10^{-18}$ across all runs (0.0 on every dissolving run) | PASS |
| Half-timestep $dt = 0.05$, $R = 2.625$ (growth endpoint) | still growth; final $F_{\mathrm{exc}} = -0.007726209284874233$, identical to $dt = 0.1$ to 15 digits | PASS |
| Half-timestep $dt = 0.05$, $R = 2.5875$ (decay endpoint) | still dissolve; final rms $3.26\times10^{-75}$ | PASS |
| Spatial refinement $K = 6$, $N = 28$, $R = 2.625$ | still growth; final $F_{\mathrm{exc}} = -0.007727623601$, rms $0.380565$ (vs $K = 4$: $-0.007726209285$, $0.380535$); initial rms $0.11541$ vs $0.11457$ and initial $E_{\mathrm{exc}}$ $0.38688$ vs $0.25982$ (finer grid retains more wall power) | PASS |
| Independent integrator (ws-a semi-implicit Model B, $dt = 0.005$, 6000 steps, $t = 30$), $L = 2\pi$, $R = 1.2$ | decay; $d_{4,\mathrm{init}} = 0.0229$, final rms $4.8\times10^{-14}$ | PASS |
| Independent integrator, $L = 2\pi$, $R = 2.7$ | growth; final rms $0.380565$, $F_{\mathrm{exc}} = -0.007727623$ | PASS |
| Independent integrator, $L = \pi$, $R = 0.8$ (Task 4 geometry) | growth; $d_{4,\mathrm{init}} = 0.2907$ (= Task 4's $0.290695$), final rms $0.380565$, $F_{\mathrm{exc}} = -0.007727624$ | PASS |
| Field-test self-tests (dealiasing, energy gradient, dissipation identity, shell RHS vs exact truncation) | re-run by import: the imported module's published values stand; not re-executed as a separate run here | NOT RUN (prior) |

Tool verdicts: conda env python
`~/miniconda3/envs/jacobian-conjecture-2d/bin/python` (Python 3.11.16,
NumPy 2.4.6, SciPy 1.17.1, Matplotlib 3.11.2), exit 0 on every script
invocation reported here. Total field-integration time $2161$ s
($\approx 36$ min): $1647$ s across the 15 main-grid runs
($57$–$157$ s per run), $507$ s of refinements, $6$ s smoke test; plus
$366$ s ($\approx 6$ min) of cross-check runs. Every field run used
$2240$ accepted steps. Peak memory well under $4\,\mathrm{GB}$ (a $18^{4}$
float64 field is $0.80\,\mathrm{MiB}$; the $28^{4}$ field is
$4.69\,\mathrm{MiB}$). No GCP spend.

## 4. Rival / failure mode

1. **The bracket is a box artefact, not a nucleation threshold.** The
   growing seeds ($R \geq 2.625$) have diameter $5.25$ in a box of length
   $2\pi = 6.28$; the patch plus its periodic images nearly fills the box
   (the seed's own tail reaches the box faces). The "growth" may be
   image-assisted filling rather than expansion of an isolated droplet.
   This is the honest reading: the bracket measures when a patch stops
   being local in this box. It does not and cannot measure the
   infinite-volume $R_{c}$, which does not fit in any box simulated here.
2. **Envelope width.** The envelope threshold used $w = 6$; this task
   used sharpness $4.0$ (wall width $0.25$). The critical-droplet report's
   own sensitivity table moves its threshold by only $\sim 0.6$ when
   $w$ goes $4 \to 8$, so width alone cannot bridge a factor of $6$ —
   but a wide-wall field seed was not run, so a direct width-matched
   field bracket is UNVERIFIED.
3. **Single seed family.** One centre, one orientation (axis-aligned
   $D_{4}$ star), equal amplitudes, zero phases, no noise, no competing
   stars, no defects. A lower-symmetry or unequal-mode nucleus could in
   principle grow at smaller $R$; nothing here excludes it.
4. **Integrator dependence.** The ETD2 result is confirmed by the
   independent semi-implicit solver at the two sampled radii ($1.2$
   decay, $2.7$ growth) but the cross-check did not bisect the bracket,
   so a solver-dependent shift of the bracket edge smaller than the
   cross-check sampling is not excluded.
5. **Occupancy trap (avoided).** Decaying seeds transiently show
   occupancy $24$; any classification by occupancy alone would have
   called them growth. Classification here uses rms $+$ energy $+$
   stationarity, not occupancy.

## 5. Evidence that would change the answer

- A larger-box field run ($L = 4\pi$ or $6\pi$, $N = 36$–$56$) with the
  same seed family: if the bracket moves up toward the envelope values
  ($12$–$16$), the present bracket is confirmed as finite-box; if it
  stays near $2.6$, the envelope would need re-examination. Costed,
  not run: see §7.
- A wide-wall field seed (sharpness $\approx 1/6$ in $\rho$, matching
  $w = 6$): if its bracket lands far from $(2.5875, 2.625]$, the present
  bracket is width-dependent.
- A full-PDE critical-droplet computation (shooting the field equations,
  not the amplitude equation) refining the ODE $R_{c} = 12.57$.
- Any growing run at $R \leq 2.5875$ under a different seed family
  (unequal modes, rotated star, noisy seed) would demote the bracket to
  a statement about one seed family only.

## 6. Comparison with the envelope prediction (stated, not conflated)

| Quantity | Value | Regime |
|---|---|---|
| Field bracket, $\alpha = 1$ (this task) | $R \in (2.5875,\ 2.625]$; $R_{\mathrm{eq}} \in (2.483,\ 2.521]$ | $L = 2\pi$ periodic box, sharp wall, full field |
| Field bracket in wavelengths | $(1.165,\ 1.182]\,\lambda$ | same |
| Thin-wall $R_{c}$ | $7.38$ | infinite volume, $\xi \ll R_{c}$ assumed — fails |
| Radial-ODE $R_{c}$ / $\Delta F^{*}$ | $12.57$ / $555$ | infinite volume, amplitude equation |
| Envelope saddle $R_{\mathrm{eq}}$ / $E$ | $13.53$ / $550.93$ | infinite volume, radial envelope |
| Envelope seed threshold, $\alpha = 1$ | $(16.19,\ 16.21]$ | infinite volume, radial envelope, $w = 6$ |
| Task 4 box threshold, $\alpha = 1$ | growth at $R \geq 0.8$ | $L = \pi$ periodic box, sharp wall, semi-implicit solver |

Ratios to the field-bracket midpoint $2.606$: ODE $4.82\times$, saddle
$5.19\times$, envelope seed threshold $6.22\times$. The field bracket
is $0.83$ of the box half-size $\pi$; the ODE radius is $4.0\times$ the
box half-size and cannot be represented in this box at all. **For
nucleation in v93.1 (§II.9 / IX.5.2): no field threshold measured here
supports or refutes the envelope nucleation picture, because no simulated
box contains an envelope-scale droplet.** What the field does establish
is that in a $2\pi$ box, sub-wavelength-scale patches dissolve and only
near-box-filling patches grow — i.e. at this box size there is no
small localized nucleus in the full field. The nucleation event
(IX.5.2) remains open: neither the envelope barrier
($\Delta F^{*} \approx 555$) nor any field-measured barrier is a rate.

## 7. Costed follow-up (pending — no GCP spend authorised or used)

- **Larger-box field bracket, $L = 4\pi$, $N = 36$, $K = 8$** (so that
  $R_{c} \sim 12$ fits with images $12.57$ apart): a $36^{4}$ grid is
  $16\times$ the points of $18^{4}$; at the measured $\sim 2$ min per
  $t = 200$ run at $18^{4}$, a single seed run scales to roughly
  $30$–$60$ min locally with $\sim 16\times$ memory ($\sim 13\,\mathrm{MiB}$
  per field array, several arrays — still under $4\,\mathrm{GB}$), and a
  bracket needs $\sim 6$–$10$ seeds: **cap: $10$ local runs, $\sim 10$
  hours wall, $0$ GCP spend, pending Brandon's approval.** A $L = 6\pi$
  box containing the $16.2$ envelope seed threshold would need
  $N \approx 54$ ($54^{4} \approx 8.5\times10^{6}$ points, $\sim 81\times$
  the $18^{4}$ cost): **GCP-scale, cap to be named before any run:
  not costed beyond this scaling estimate; pending.**
- **Wide-wall field seed** (sharpness $\approx 0.17$): same cost as the
  present runs, $\sim 6$ seeds $\times \sim 2$ min: **cap $\sim 15$ min
  local, pending.**
- **$\alpha = 1.5$ bracket at larger $R$**: $\sim 4$ seeds $\times \sim 2$
  min: **cap $\sim 10$ min local, pending.**

## 8. Ledgers

### Assumption ledger
- Operating point $(\bar{\psi}, r) = (-0.18, -0.35)$, $u = v = 1$,
  $q_{0}^{2} = 8$, mobility $1$ — manuscript / prior field test, not
  re-derived here.
- Uniform state linearly stable at the operating point
  ($r_{\mathrm{eff}} = +0.1072 > 0$); growth must proceed by nucleation.
- Seed family: equal amplitudes, zero phases, axis-aligned star,
  centred, no noise — a choice, not a result.
- Classification thresholds are the field test's
  (occupancy $24$, CV $\leq 0.05$, lock $\geq 0.95$, RHS rms
  $\leq 10^{-7}$; uniform power $< 10^{-12}$).
- The envelope numbers are quoted from prior sources except where
  §3 says re-verified; the ODE shooting and the droplet-repo bracket
  were not re-run.

### Parameter ledger
| Parameter | Value | Provenance |
|---|---|---|
| $\bar{\psi}$, $r$, $u$, $v$, $q_{0}^{2}$ | $-0.18$, $-0.35$, $1$, $1$, $8$ | field test `parameters.json` |
| $A^{*}$ | $0.077575296339281$ | derived here, two routes (§1.2) |
| $\alpha$ (amplitude factor) | $1.0$ (main), $1.5$ (sensitivity) | chosen; Task 4 used $1.0$, $1.5$ |
| Box $L$, grid $N$, cutoff $K$ | $2\pi$, $18$, $4$ (main); $28$, $6$ (spatial check) | field test |
| Seed sharpness | $4.0$ | Task 4 droplet form |
| $dt$, $t_{\mathrm{final}}$ | $0.1$ ($0.05$ half-dt), $200$ | field test |
| Cross-check $dt$, steps | $0.005$, $6000$ ($t = 30$) | Task 4 droplet runs |

### Choice ledger
- Box $L = 2\pi$ (not $L = \pi$): the field-test box; the largest box
  with a published dealiased solver. Consequence: bracket is finite-box.
- Sharp wall (not envelope $w = 6$): matches Task 4, so the box
  comparison in §2.3 is apples-to-apples; consequence: width-matched
  comparison is UNVERIFIED.
- Bisection only at $\alpha = 1$: the $\alpha = 1.5$ scan stopped at
  $R = 1.5$ (all dissolve); consequence: $\alpha$-dependence above
  $R = 1.5$ UNVERIFIED.
- No replicates: seeds are deterministic (no RNG); replicates would be
  identical. Sensitivity is probed by $R$, $\alpha$, $dt$, $K$ instead.

### Dependency ledger
- Field bracket $\leftarrow$ field-test solver + Task 4 seed form +
  $A^{*}$ (§1.2) $+$ classification rule. The solver's own validation
  (dealiasing, gradient, dissipation, shell-RHS) is the field test's,
  re-imported, not re-executed as a separate run (NOT RUN in §3).
- Envelope comparison $\leftarrow$ Task 4 report (ODE, thin-wall,
  $\kappa$, $\sigma$) $+$ critical-droplet report/table (seed threshold,
  saddle). Thin-wall arithmetic re-verified; ODE shooting and droplet
  bracket quoted.
- Cross-check $\leftarrow$ `d4model.py` as-is (including its
  Hermitian-symmetry fix); diagnostics recomputed from scratch here.

### Withdrawal ledger
- One bug found and fixed during this task: `crosscheck_d4model.py`
  initially read the shell at FFT indices $(2,2,0,0)$ in the $L = \pi$
  box, where the shell sits at index $(1,1,0,0)$; the first $L = \pi$
  run was therefore reported "marginal" with $d_{4} \approx 0$ even
  though the field had grown (rms $0.3806$,
  $F_{\mathrm{exc}} = -0.0077276$). Fixed by making the shell labels
  box-dependent; the re-run gives growth with
  $d_{4,\mathrm{init}} = 0.2907$, exactly Task 4's value. The faulty
  run is discarded, not reported as a result.
- One bug found and fixed during this task: `run_critical_seed.py`
  initially referenced `m.KSTAR` (module-level in the field-test
  module, not a `Field` attribute); fixed before any production run.
- The `seed_profile.png` grey envelope line initially carried the
  wrong radius label ($R = 1.2$ for a curve drawn at $R = 2.625$);
  fixed and re-rendered.

## 9. HLRE grades (per narrow claim; worst-of shown)

Track E unless noted; independence I1 (all verification artificial, one
pipeline family for the main solver, second machine route for the
cross-check; external verification by an authorised agent is the
programme's route to lift grades, not claimed here). Postulation ceiling:
evidence-guided (seed family, box, and decision rule fixed before
inspection of outcomes — the bracket was bisected after the coarse scan,
which is a search, not a frozen prediction; hence no claim here is
graded above B).

| Claim | Grade | Worst-of computation |
|---|---|---|
| Field bracket $R_{c,\mathrm{field}} \in (2.5875,\ 2.625]$ at $\alpha = 1$, $L = 2\pi$ | **B** | I1 (bound repealed 2026-11-12; grade follows evidence) / evidence-guided ceiling B / two independent integrators agree at sampled radii $+$ half-dt both endpoints $+$ spatial check of growing endpoint / support in record: 11 main runs, 0 rejected steps |
| Growing endpoints reach the relaxed full branch ($F_{\mathrm{exc}} = -0.007726209285$, rms $0.380535$) | **B** | same as above; final RHS rms $\sim 10^{-15}$ |
| Dissolving endpoints reach uniform (rms $\sim 10^{-75}$) | **B** | same as above |
| $\alpha = 1.5$ does not rescue $R \leq 1.5$ seeds in the $2\pi$ box | **C** | coarse scan only (4 runs), no bisection, no refinement at $\alpha = 1.5$ |
| $\pi$-box vs $2\pi$-box shell-fraction scaling ($16\times$) explains the Task 4 / field threshold difference | **B** | measured in both boxes with two independent computations agreeing exactly |
| Thin-wall $R_{c} = 7.38$ fails ($\xi > R_{c}$) | **B** | prior result, arithmetic re-verified here |
| Envelope $R_{c} = 12.57$ / $\Delta F^{*} = 555$ (ODE) and seed threshold $(16.19, 16.21]$, saddle $13.53$ / $550.93$ | **B (quoted, not re-derived)** | prior-source values; this task verifies only the arithmetic around them, not the shooting / droplet integration |
| Field bracket measures the infinite-volume critical radius | **NOT A CLAIM — refuted as a reading** | bracket is $0.83\times$ box half-size; ODE radius exceeds the box |
| Any nucleation rate / waiting time from these runs | **ABSTAIN** | deterministic, no noise, no stochastic action |

## 10. UNVERIFIED / ABSTAIN list

- Infinite-volume critical radius from the field (no box simulated
  contains one).
- Nucleation rate, waiting time, cosmological timescale (no noise model).
- Field threshold for wide-wall ($w = 6$) seeds, rotated/unequal-mode
  seeds, off-centre seeds, or seeds with noise.
- $\alpha$-dependence of the field threshold above $R = 1.5$.
- Whether a lower-symmetry nucleus grows at smaller $R$.
- Spatial-refinement check of the decay endpoint (only the growing
  endpoint was refined in $K$; both endpoints were refined in $dt$).
- The field-test solver's own self-tests as a fresh re-execution
  (imported, not re-run).
- Any statement about v93.1 §II.9 nucleation beyond §6: the envelope
  barrier $\Delta F^{*} \approx 555$ is quoted, not measured here.

## 11. Deliverables

- `REPORT.md` (this file)
- `threshold_table.csv` — main-grid grow/dissolve bracket
  ($\alpha = 1$ coarse $+$ bisection; $\alpha = 1.5$ coarse)
- `refinement_table.csv` — half-timestep and spatial refinement rows
- `crosscheck_table.csv` — independent-integrator cross-check rows
- `seed_outcomes.csv` — one row per field run (all tags, with solver stats)
- `seed_trajectories.csv` — saved-time diagnostics per run
- `seed_evolution.png` — rms and energy vs time, $\alpha = 1$
- `bracket.png` — outcome vs $R$ with envelope predictions marked
- `seed_profile.png` — reconstructed initial radial profiles
- `run_critical_seed.py` — field-seed driver (imports the field-test solver)
- `crosscheck_d4model.py` — independent-integrator cross-check
- `verify_seed.py`, `verify_envelope.py` — construction and arithmetic checks
- `make_figures.py` — figure generation from the CSVs/NPZs
- Per-run NPZs (`<run_id>.npz`) — initial/final compact coefficients,
  shell coefficients, power by $|k|^{2}$
- `crosscheck_2pi.json`, `crosscheck_pi.json` — cross-check series

## 12. Reproduce

```bash
cd ~/workspace/research/irh/co-scientist-tasks-2026-11-10/local-independent/task3-critical-seed
~/miniconda3/envs/jacobian-conjecture-2d/bin/python run_critical_seed.py \
  --out . --alpha 1.0 --radii 2.5875 2.625 --t-final 200 --tag bisect_a1
~/miniconda3/envs/jacobian-conjecture-2d/bin/python verify_seed.py
~/miniconda3/envs/jacobian-conjecture-2d/bin/python verify_envelope.py
~/miniconda3/envs/jacobian-conjecture-2d/bin/python crosscheck_d4model.py \
  --box 2pi --radii 1.2 2.7 --out .
```

Nothing in this task was filed, committed, or written into any repo or
manuscript. No browser, no Academia, no Co-scientist output was used.
