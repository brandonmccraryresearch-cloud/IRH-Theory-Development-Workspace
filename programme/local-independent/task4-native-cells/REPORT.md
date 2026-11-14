# Task 4 — $D_{4}$ and $A_{4}$* formation on native cells

## CLAIM and STATUS

**CLAIM.** At the matched quench $r=-0.35$, $\bar{\psi}=-0.18$, $q_{0}^{2}=8$, $u=v=1$,
with matched initial modulation RMS $0.38004$, conserved Model B field dynamics
run separately on each star's native four-dimensional cell gives paired
formation trajectories in which $D_{4}$ forms reliably from every patterned
seed while $A_{4}$* is trapped by its own $A_{3}$ sub-pattern: $A_{4}$*
twelve-mode seeds reach the full 20-mode state in $0/3$ runs (all trapped in a
stationary 12-mode state at $E=-0.00547044$), against $3/3$ for $D_{4}$
twelve-mode seeds; $A_{4}$* six-mode seeds reach full in $2/3$ runs (one
trapped); broadband random starts decay to uniform in $6/6$ runs on both
cells. The relaxed full-star energies are $E=-0.00772621$ ($D_{4}$) and
$E=-0.00587749$ ($A_{4}$*), each about $1\%$ below its pure equal-amplitude
branch. This is a dynamical difference in the same direction as the onset
advantage, not a proof of dynamical selection in general.

**STATUS: COMPLETE for the declared design** — $18$ new $A_{4}$* field runs to
$t=200$ plus $6$ refinements, all exit $0$; $D_{4}$ arm supplied by the prior
4d-field-test trajectories on the identical cell, replicated locally $10/10$
(including one twelve-mode run) before the local $D_{4}$ run was stopped to
spend the remaining compute on the new $A_{4}$* arm. All headline numbers
below are from the completed runs. Nothing is filed, committed, or written
into the manuscript or any repo.

Work directory:
`~/workspace/research/irh/co-scientist-tasks-2026-11-10/local-independent/task4-native-cells/`

Prior sources used (only): `a20-onset/` (`methods.md`, `reproduce.py`,
`stars.json`, `boundaries.csv`, `coefficients.csv`, `validation.json`,
`onset-competition.png`), `4d-field-test/` (`run_field_study.py`,
`parameters.json`, `report.md`, trajectories and outcomes), and
`ws-a-core-computations/d4model.py`. No Co-scientist output was read, opened,
or used for this task; no browser; no Academia; local compute only.

## 1. Derivation

### 1.1 Why no shared cell, re-verified

Both stars span rank-four reciprocal lattices. The unscaled primitive Gram
determinants are $\det G_{D_{4}}=4$ and $\det G_{A_{4}}=5$; scaling both stars
by $2$ gives $1024$ and $1280$, with reciprocal covolumes $32$ and
$16\sqrt{5}$. If both exact stars at the same radius belonged to one discrete
rank-four reciprocal lattice, their covolume ratio would be a ratio of finite
integer indices. It is $\sqrt{5}/2$, irrational, so **no common
four-dimensional periodic torus, rectangular or oblique, contains both exact
stars at the same radius**. Rotation cannot change this. This was re-derived
here from independently written basis matrices (see §3, `verify_geometry.py`):
$\det G_{D_{4}}=4.000000$, $\det G_{A_{4}}=5.000000$, scaled determinants
$1024.0$ and $1280.0$, all exact to the printed precision.

### 1.2 Native cells

Write the field in lattice coordinates $y\in[0,1)^{4}$, $x=Ay$ with
$A=2\pi M^{-T}$, so a plane wave $\exp(2\pi i\, n\cdot y)$ has physical
wavevector $k=Mn$, $n\in\mathbb{Z}^{4}$. The functional, the operator
$(q_{0}^{2}+\nabla^{2})^{2}$, and the cubic/quartic terms are then exactly the
field-test ones, with $|k|^{2}$ computed from $Mn$. Energies are
volume-normalised excess densities, so the two cells are comparable as
densities.

- **$D_{4}$ cell:** $M=I$, cubic box $[0,2\pi]^{4}$, reciprocal lattice
  $\mathbb{Z}^{4}$, cell volume $V_{D_{4}}=(2\pi)^{4}=1558.545457$. This is
  exactly the 4d-field-test cell, so the $D_{4}$ arm is that study.
- **$A_{4}$* cell:** $M$ has columns equal to the Helmert coordinates of
  $2(e_{j}-e_{j+1})$, $j=1,\dots,4$ (the $A_{4}$ simple roots scaled by $2$).
  Verified: $\det M = 16\sqrt{5} = 35.777087640$; every one of the $20$ star
  vectors has integer lattice coordinates $n$ with entries $0,\pm1$;
  $|k|^{2}=8$ for all $20$; Helmert basis orthonormal to $2.22\times10^{-16}$.
  Real-cell volume $V_{A_{4}^{*}}=(2\pi)^{4}/|\det M| = 43.562670$. The volume
  ratio is $V_{D_{4}}/V_{A_{4}^{*}} = 16\sqrt{5} \approx 35.777$ (the
  reciprocal-covolume ratio is $\sqrt{5}/2$; the two ratios are different
  quantities and are not to be confused).

### 1.3 Exact onset quantities, re-verified by brute force

Direct ordered enumeration (no FFT, no tolerance) over the integer vectors in
`stars.json` reproduces:

| Star | $N$ | $T$ | $Q$ | $\tau^{2}=T^{2}/N^{3}$ | $q_{4}=Q/N^{2}$ | $S=\tau^{2}/q_{4}$ |
|---|---:|---:|---:|---:|---:|---:|
| $D_{4}$ | $24$ | $192$ | $3384$ | $8/3$ | $47/8$ | $64/141$ |
| $A_{4}$* | $20$ | $120$ | $1860$ | $9/5$ | $93/20$ | $12/31$ |

At the manuscript point $u=v=1$, $m=-0.18$, $r=-0.35$, $\delta=0$:
$\alpha = r+\delta-2um+3vm^{2} = 0.1072$, $\beta = u-3vm = 1.54$.
Stationary large branches (methods.md §3–§4 formulas): $D_{4}$ per-mode
$A=0.07757529634$, RMS $B=0.3800397854$, $f=-0.007632267319$; $A_{4}$*
$A=0.08594252409$, $B=0.3843466521$, $f=-0.005816677329$. Characteristic
$r$ values at $m=-0.18$ (fold, fixed-mean degeneracy, within-star loss, pair
equal-energy $r_{\times}=-0.591438362$) all reproduce `boundaries.csv` to
better than $10^{-9}$. The $A_{3}$ sub-pattern pure branch is
$B_{+}=0.40331836$, $A_{+}=0.11642798$, $f=-0.005362496463$ (same formulas,
$N=12$, $T=48$, $Q=540$).

### 1.4 Dynamics and matched conditions

Conserved Model B, mobility $M=1$, in Fourier–Galerkin form on each native
cell:

$$\partial_{t}\hat{\phi}_{k} = -|k|^{2}\left\{\left[\alpha+(8-|k|^{2})^{2}\right]\hat{\phi}_{k} - \beta\,\widehat{P(\phi^{2})}_{k} + \widehat{P(\phi^{3})}_{k}\right\},$$

integrated with the field test's second-order exponential Heun (ETD2) scheme,
exact dissipative linear propagator, explicit nonlinearity, step-energy
rejection (reject if $F_{\rm new} > F_{\rm old} + 2\times10^{-13} +
2\times10^{-12}|F_{\rm old}|$), startup caps $dt/1000$ until $t=0.02$ and
$dt/20$ until $t=0.2$, $dt=0.1$, $t_{\rm final}=200$. Retained band: tensor
$|n_{i}|\le 4$ in lattice coordinates **and** physical $|k|^{2}\le 64$,
$N=18$ grid points per cell dimension ($N>4K$ dealiasing in $n$-space).
The physical cap is redundant for $D_{4}$ (its tensor band already implies
$|k|^{2}\le 64$) and essential for $A_{4}$*: without it the $A_{4}$* tensor
band reaches $|k|^{2}=896$ and its broadband starts are dominated by
ultra-high-$|k|$ linear penalty (dissipation $\sim 10^{11}$, found during
debugging and removed by the cap — see §6).

Matched: $r$, $m$, $q_{0}^{2}$, $u$, $v$, $M$, $\alpha$, $\beta$, $dt$,
$t_{\rm final}$, save times, master seed $931241112$, replicate seeds, total
modulation RMS $0.3800397854$ for every matched start (the $D_{4}$
stationary RMS; per-mode $A$ then differs, $0.07758$ vs $0.08497$, as the
onset comparison requires). Initial families mirror the field test exactly:
broadband random weak (RMS $0.05$) and matched; six-mode seed $+1\%$
broadband noise; twelve-mode seed $+1\%$; full-star seed $+25\%$; shell-random
bridge (star projection of the broadband direction, renormalised to matched
RMS). Sub-patterns: $D_{4}$ six $=$ $A_{2}$ subset, twelve $=$ $k_{4}=0$
$D_{3}$ slice; $A_{4}$* six $=$ $A_{2}$ roots $e_{i}-e_{j}$, $i,j\in\{1,2,3\}$,
twelve $=$ $A_{3}$ roots $i,j\in\{1,2,3,4\}$. Patterned-seed orientations:
$D_{4}$ cubic axis permutations/sign flips $+$ translation (as field test);
$A_{4}$* a random $S_{5}$ permutation of the five underlying indices $+$
$y$-translation (the star's own symmetry group — analogous, not identical;
see matching ledger §5).

Stationarity/pattern criteria (same as field test): full endpoint $=$
occupancy $N$, amplitude CV $\le 0.05$, weighted signed triad lock $\ge 0.95$,
projected RHS RMS $\le 10^{-7}$. "Stationary other" $=$ stationary
(RHS $\le 10^{-7}$) but not the full star. All times below are first saved
times at which the stated property holds thereafter (save grid: geometric
$0.01$–$2$, then every $5$); they are upper bounds on the true times, not
high-precision kinetics.

### 1.5 Second independent route: shell-only truncated dynamics

Every field run is paired with the exact shell-only (truncated) dynamics
$\dot a_{k} = -8[\alpha a_{k} - \beta\sum_{p+q=k}a_{p}a_{q} +
v\sum_{p+q+s=k}a_{p}a_{q}a_{s}]$ from the same initial shell projection
(unscaled), integrated with DOP853 (rtol $2\times10^{-10}$,
atol $2\times10^{-12}$, max step $0.5$). Two independent implementations
were cross-checked: explicit pair/triple enumeration vs FFT convolution on
the $y$-grid, agreeing to $1.9\times10^{-20}$ ($A_{4}$*) and
$2.7\times10^{-20}$ ($D_{4}$) at a random real-field star state. Endpoint
class (uniform / full / other) agrees field-vs-truncation in $18/18$
$A_{4}$* runs and $18/18$ $D_{4}$ prior runs; exact outcome-string agreement
is $14/18$ for $A_{4}$* (the four differences are all
stationary-vs-finite-time timing in the trapped/other class, never a
different endpoint class).

## 2. Results

### 2.1 Paired outcome counts (3 replicates per family)

| Family | $D_{4}$ uniform | $D_{4}$ full | $D_{4}$ other | $A_{4}$* uniform | $A_{4}$* full | $A_{4}$* other |
|---|---:|---:|---:|---:|---:|---:|
| Random weak (RMS $0.05$) | $3$ | $0$ | $0$ | $3$ | $0$ | $0$ |
| Random matched (RMS $0.38004$) | $3$ | $0$ | $0$ | $3$ | $0$ | $0$ |
| Six-mode $+1\%$ noise | $0$ | $3$ | $0$ | $0$ | $2$ | $1$ |
| Twelve-mode $+1\%$ noise | $0$ | $3$ | $0$ | $0$ | $0$ | $3$ |
| Full $+25\%$ noise | $0$ | $3$ | $0$ | $0$ | $3$ | $0$ |
| Shell bridge (matched RMS) | $0$ | $3$ | $0$ | $0$ | $3$ | $0$ |

Full table: `paired_summary.csv`. $D_{4}$ counts are the prior field-test
outcomes; $A_{4}$* counts are the new runs here.

### 2.2 The $A_{4}$* trap

All four $A_{4}$* "other" endpoints are the **same stationary 12-mode
state**: $12$ modes at equal amplitude $|a|=0.1168$, $8$ modes at zero
(final amplitudes read from `a4star/spectral_trajectories.npz`), triad lock
$1.0$, RHS RMS $2.4\times10^{-11}$ to $9.7\times10^{-14}$,
$E=-0.00547043620975$ in all four runs (identical to $10$ significant
figures). Its amplitude matches the equal-amplitude $A_{3}$ branch
($A_{+}=0.11642798$) to $0.3\%$ and its energy is $2.01\%$ below the pure
$A_{3}$ branch value $-0.005362496463$ (harmonic relaxation; the field's
shell amplitudes are $0.3\%$ above the branch value and off-shell power is
$3.07\times10^{-6}$). The $A_{3}$ state is therefore a genuine stationary
attractor of the $A_{4}$* field dynamics at this quench, not a transient:
twelve-mode seeds settle into it in $3/3$ runs (stationary by first saved
time $t=50$–$55$), and one six-mode seed falls into it (stationary by
$t=115$, after the $A_{3}$ amplitudes are established by $t=10$). The other
two six-mode seeds escape it and reach full (stationary by $t=25$–$30$).
For $D_{4}$, twelve-mode seeds pass through a $D_{3}$ 12-mode intermediate
and reach full (stationary by $t=45$–$50$); no $D_{4}$ run is trapped.

### 2.3 Relaxed full-star energies

| Star | Pure branch $f$ | Field endpoint $E$ | Relaxation |
|---|---:|---:|---:|
| $D_{4}$ | $-0.007632267319$ | $-0.007726209285$ | $1.23\%$ below branch |
| $A_{4}$* | $-0.005816677329$ | $-0.005877487079$ | $1.05\%$ below branch |

$A_{4}$* full endpoints agree across all $6$ full/bridge runs to
$2\times10^{-15}$ in $E$; final amplitude CV $\le 3.8\times10^{-16}$,
triad lock $1.0$, RHS RMS $\le 9.1\times10^{-16}$. The $D_{4}$ value is the
prior field-test value, replicated locally to $1.73\times10^{-18}$ (§2.5).

### 2.4 Formation times (first saved time, §1.4)

| Family | $D_{4}$ stationary by | $A_{4}$* stationary by |
|---|---:|---:|
| Random weak / matched (uniform) | $t=15$ | $t=15$–$20$ |
| Full $+25\%$ noise | $t=5$ | $t=15$ |
| Shell bridge | $t=10$ | $t=15$–$20$ |
| Six-mode | $t=20$ (full) | $t=25$–$30$ (full, $2/3$); $t=115$ (trap, $1/3$) |
| Twelve-mode | $t=45$–$50$ (full) | $t=50$–$55$ (trap, $3/3$) |

Full per-run times: `formation_times.json`. These are save-grid
quantisations; the ordering (patterned $D_{4}$ faster or equal at every
family) is the finding, not the exact times.

### 2.5 $D_{4}$ replication (local)

The generalised solver was run locally on the $D_{4}$ cell for $10$ runs
before being stopped (see §6): random weak $3/3$ uniform, random matched
$3/3$ uniform, six-mode $3/3$ stationary full, plus a twelve-mode checkpoint
at stationary full. Outcome classes match the prior field test $10/10$;
final energies agree to $1.73\times10^{-18}$ absolute on patterned runs
(uniform runs agree to $\sim 10^{-165}$ absolute on $\sim 10^{-154}$
energies). Self-test values reproduce the field test's numbers exactly:
dealias energy $0$, projected-nonlinearity max $1.69704\times10^{-18}$,
energy-gradient FD error $1.18447\times10^{-10}$, dissipation identity
$2.91038\times10^{-10}$, linear-decay relative error $5.13577\times10^{-7}$.
On that basis the $D_{4}$ arm of the paired figure uses the prior
field-test trajectories (all $18$ runs), labelled as such; the local runs
are the replication evidence, in `d4/`.

## 3. Checks run

Tool verdicts are quoted with tool name $+$ version $+$ exit code, per the
computation gate. All numbers below were produced in this task by
`~/miniconda3/envs/jacobian-conjecture-2d/bin/python` (Python $3.11.16$,
NumPy $2.4.6$, SciPy $1.17.1$, Matplotlib $3.11.2$).

| Check | Result | Verdict |
|---|---|---|
| `verify_geometry.py`: exact $T,Q$ brute force, $S$, Gram dets, Helmert orthonormality, $A_{4}$* integer $n$ coords, $\|k\|^{2}=8$, stationary branches, boundaries vs `boundaries.csv` | $24/24$ PASS, `ALL PASS` | PASS — Python $3.11.16$, exit $0$ |
| $A_{4}$* self-tests (`run_native_cells.py --star A4star`): dealias energy $18$ vs $28$ same $K4$ $=0$; projected-nonlinearity max $3.01\times10^{-18}$; energy-gradient FD error $1.09\times10^{-9}$; dissipation identity absolute error $1.86\times10^{-9}$ (also asserted relatively, $<10^{-9}$ of the dissipation magnitude); shell RHS vs exact truncation $5.83\times10^{-16}$; FFT-vs-enumeration truncated RHS $1.92\times10^{-20}$; shell energy vs truncation $0$; linear-decay rel. error $4.27\times10^{-7}$; triads $20$; analytic amplitude $0.08594252409$ | all thresholds passed | PASS — Python $3.11.16$, exit $0$ |
| $D_{4}$ self-tests: values listed in §2.5, identical to field test | all thresholds passed | PASS — Python $3.11.16$, exit $0$ |
| $A_{4}$* main runs: $18/18$ completed to $t=200$, $0$ rejected steps, max mean error $2.17\times10^{-17}$, max step energy increase $1.21\times10^{-17}$ | completed | PASS — exit $0$ |
| $A_{4}$* refinements ($6$): half-$dt$ and spatial $K=6$ ($28^{4}$) for random-matched $00$, six $00$, full $00$ | $6/6$ same outcome class; $\|\Delta E\|\le 3.5\times10^{-18}$; max trajectory shell error / initial norm $\le 1.48\times10^{-3}$ (half-$dt$); newly admitted band power $0$ in all $K=6$ checks | PASS — exit $0$ |
| $D_{4}$ local runs: $10$ runs, $0$ rejected steps | $10/10$ outcome classes match prior; energies to $1.73\times10^{-18}$ | PASS — stopped deliberately, see §6 |
| Seed-energy decomposition (§6, point 2): off-shell linear penalty of the $1\%$ noise computed exactly from saved seed coefficients | $+0.00357$ ($D_{4}$) vs $+0.01225$ ($A_{4}$*); sums reproduce field $E_{0}$ exactly | PASS (diagnostic, not a run outcome) |
| Trapped-state identification: final star amplitudes from `spectral_trajectories.npz` | $12$ modes at $0.1168$, $8$ at $0$ in all $4$ trapped runs | PASS |

NOT RUN: $D_{4}$ half-$dt$ / $K=6$ refinements locally — the prior field test
already ran them for $D_{4}$ (half-$dt$ and $K=6$ for random-matched,
six-mode and full starts; endpoints agree, largest half-$dt$ shell-path
difference $1.41\%$ of initial RMS) and the local $D_{4}$ replication above
covers this solver. No GCP runs were made.

## 4. Rival / failure mode

The main rival reading is that the $A_{4}$* trap is an artefact of the
$A_{4}$* cell construction rather than $A_{4}$* dynamics: the $A_{4}$* cell
is $35.777\times$ smaller in volume, holds $660$ retained real degrees of
freedom against $D_{4}$'s $6560$ at the same physical spectral support, and
its broadband starts carry far more initial energy at matched RMS
(random-matched $E_{0}$: $114.6$–$124.7$ vs $35.2$–$35.8$). Three replies,
all in the record: (i) the trap reproduces under halved timestep and under
$K=6$ spatial refinement with $\Delta E = -1.73\times10^{-18}$ — it is not
a timestep or resolution artefact; (ii) it is reached from two different
seed families (six- and twelve-mode) and in $4$ independent replicates,
with identical endpoint energy to $10$ figures, and its amplitudes match an
independently computed exact branch ($A_{3}$, §1.3) — a numerical artefact
would not land on an exact branch; (iii) the patterned families most
affected by the volume/DOF difference (full and bridge) show no trapping
and identical endpoints in both cells, so the difference is specific to
sub-pattern seeds, not a global cell defect. The rival is therefore
disfavoured but not eliminated: the trap's existence is established at this
one quench point, in this one band, in these cells; its robustness to band,
cell size, and quench depth is UNVERIFIED (§7).

Other failure modes: (a) $n=3$ per family is a pilot count, not a basin
probability — no frequency is claimed beyond the counts in §2.1; (b) the
trapped state is stationary in the retained band only — off-band and
longer-time instabilities are not tested; (c) $t_{\rm final}=200$ is finite;
the trap could in principle decay on longer times (its RHS is
$\le 2.4\times10^{-11}$ and dissipation $\sim 10^{-22}$, so no decay is
visible, but that is not a proof); (d) the uniform state is linearly stable
on shell at this point ($\alpha>0$), so all formation here is
seed-dependent by construction — nothing here shows spontaneous formation
from noise.

## 5. Ledgers

### Parameter ledger

| Parameter | Value | Source |
|---|---|---|
| $r$ (bare quench) | $-0.35$ | `a20-onset/methods.md` §4; `4d-field-test/parameters.json` |
| $\bar{\psi}=m$ | $-0.18$ | same |
| $q_{0}^{2}$ | $8$ ($\delta=0$) | same |
| $u$, $v$ | $1$, $1$ | same |
| Mobility $M$ | $1$ | same |
| $\alpha$, $\beta$ | $0.1072$, $1.54$ | derived in §1.3, re-verified |
| Matched RMS $B$ | $0.3800397854$ | $D_{4}$ stationary RMS, methods.md §4 |
| Weak RMS | $0.05$ | field test |
| $dt$, $t_{\rm final}$ | $0.1$, $200$ | field test |
| Grid $N$, cutoff $K$ | $18$, $4$ | field test ($N>4K$) |
| Physical cap | $\|k\|^{2}\le 64$ | new in this task (§1.4, §6) |
| Master seed | $931241112$ | field test |
| $D_{4}$: $N,T,Q$ | $24$, $192$, $3384$ | brute force §1.3 |
| $A_{4}$*: $N,T,Q$ | $20$, $120$, $1860$ | brute force §1.3 |
| $A_{3}$: $N,T,Q$ | $12$, $48$, $540$ | brute force (A20 coefficients) |

### Assumption ledger

| # | Assumption | Status |
|---|---|---|
| A1 | Excess energy is volume-normalised density in each cell (the only way to compare cells of different volume) | Declared convention; absolute energies would differ by the $16\sqrt{5}$ volume ratio and are not compared |
| A2 | The field-test functional, $\alpha,\beta$ conventions, and excess-over-uniform baseline carry over unchanged to the oblique cell | Verified: shell RHS vs exact truncation to $5.8\times10^{-16}$ on the $A_{4}$* cell |
| A3 | Retained band $=$ tensor $\|n_{i}\|\le4$ plus $\|k\|^{2}\le64$ is an adequate representation of formation at this quench | Sensitivity-checked only by the $K=6$ refinements (§3); a wider band is UNVERIFIED |
| A4 | Stationarity (RHS RMS $\le10^{-7}$) plus occupancy/CV/lock identifies the endpoint pattern | Stated criterion, not a stability theorem; explicit in every outcome label |
| A5 | $D_{4}$ arm $=$ prior field-test trajectories, on the strength of the $10/10$ local replication | Stated in §2.5; the local $D_{4}$ runs are in `d4/` |

### Choice ledger

| Choice | Why it was made | What would change if changed |
|---|---|---|
| Physical cap $\|k\|^{2}\le64$ | Without it $A_{4}$* broadband starts are dominated by $\|k\|^{2}$ up to $896$ modes (found in debugging, §6) | Uncapped $A_{4}$* random starts would be incomparable and numerically stiff |
| RMS (not per-mode $A$, not energy) as the matched modulation | Onset comparison matches $B=\sqrt{N}A$ (methods.md §3); equal per-mode $A$ would not match total modulation power across different $N$ | Matching energy instead would change initial amplitudes (random $E_{0}$ already differs — see below) |
| $S_{5}$ permutation $+$ $y$-translation for $A_{4}$* patterned seeds | The star's own symmetry group; cubic permutations do not act on the oblique cell | A different symmetry sampling could change which replicates trap (the trap itself is seen in $4$ replicates across $2$ families) |
| $D_{4}$ local run stopped after $10$ runs | $10/10$ replication established; remaining wall time was better spent on the new $A_{4}$* arm (§6) | Completing all $18$ local $D_{4}$ runs would add nothing except a fuller replication table (costed in §8) |
| Refinements only for $3$ $A_{4}$* starts (random-matched, six, full) | Mirrors the field test's refinement design; twelve-mode refinement not run | A twelve-mode refinement would test the trap's resolution dependence directly — pending, costed in §8 |

### Matching ledger — what was matched, what was not

| Quantity | Matched? | Evidence |
|---|---|---|
| Quench ($r,m,q_{0}^{2},u,v,M,\alpha,\beta$) | Yes, exactly | Same constants in both solvers |
| Total modulation RMS at $t=0$ | Yes, $0.38004$ (matched) / $0.05$ (weak) | Verified per run in outcomes CSVs |
| Random-direction seeds (same master/replicate seeds) | Yes, in lattice coordinates | Same `SeedSequence` construction |
| Integrator, $dt$, $t_{\rm final}$, save times, energy-rejection rule | Yes | Same code path |
| Spectral support (physical $\|k\|^{2}\le64$) | Yes | Cap in §1.4 |
| Retained degrees of freedom | **No** — $6560$ ($D_{4}$) vs $660$ ($A_{4}$*) | Inherent: cells differ in volume by $16\sqrt{5}$; per-unit-volume mode density is comparable, per-cell it is not |
| Initial excess energy of broadband starts | **No** — random matched $E_{0}$: $35.2$–$35.8$ ($D_{4}$) vs $114.6$–$124.7$ ($A_{4}$*) | Same RMS spread over different mode distributions; mean linear penalty differs (see §6) |
| Initial excess energy of patterned seeds | **No, in detail** — six-mode $E_{0}$: $0.00129$–$0.00136$ ($D_{4}$) vs $0.00921$–$0.01026$ ($A_{4}$*); twelve-mode: $-0.00172$–$-0.00166$ vs $0.00622$–$0.00724$; full: $2.06$–$2.10$ vs $6.54$–$7.28$ | The $1\%$/$25\%$ noise carries off-shell linear penalty $+0.00357$ ($D_{4}$) vs $+0.01225$ ($A_{4}$*) for the six-mode seed (exact decomposition, §3); the shell-pattern part of $E_{0}$ is matched |
| Seed symmetry sampling | Analogous, not identical | $D_{4}$ cubic permutations vs $A_{4}$* $S_{5}$ permutations (§1.4) |
| Cell volume | **No** — $(2\pi)^{4}$ vs $(2\pi)^{4}/(16\sqrt{5})$ | Inherent to native cells; energies compared as densities only |

## 6. Derivation notes, discrepancies, and withdrawal note

1. **Physical cap found by a failed self-test.** The first $A_{4}$* smoke
   run failed its dissipation-identity assertion: absolute error
   $4.6\times10^{-5}$ on a dissipation of $\sim10^{11}$. The identity itself
   was correct (relative error $4\times10^{-16}$); the fault was the
   uncapped tensor band reaching $|k|^{2}=896$, which also made broadband
   initial energies incomparable. The fix was the physical cap
   $|k|^{2}\le64$ (§1.4) and a relative dissipation tolerance. No result
   from the uncapped runs is used anywhere. The cap changes the $A_{4}$*
   band from $6560$ to $660$ retained real degrees of freedom; that count
   difference is reported, not hidden.
2. **Six-mode seed energies.** The six-mode seeds report $E_{0}>0$
   ($+0.00135$ $D_{4}$, $+0.01001$ $A_{4}$*) although the equal-amplitude
   $A_{2}$ pattern alone gives $f=-0.00223$. This is not an error: the cubic
   term matches the analytic value exactly ($-0.02300$), and the exact
   decomposition gives off-shell linear penalty $+0.00357$ ($D_{4}$,
   off-shell mean $|k|^{2}=26.9$) vs $+0.01225$ ($A_{4}$*, mean
   $|k|^{2}=47.1$) for the same $\sim1.44\times10^{-5}$ noise power; the
   sums reproduce the field $E_{0}$ exactly. The noise is matched in RMS
   and unmatched in energy, as ledgered in §5.
3. **Volume-ratio wording corrected during this task.** An early check line
   in `verify_geometry.py` printed the cell-volume ratio next to
   $\sqrt{5}/2$ in a confusing way. The correct statements are:
   $V_{D_{4}}/V_{A_{4}^{*}} = 16\sqrt{5}$ (cell volumes) and reciprocal
   covolume ratio $\sqrt{1280/1024}=\sqrt{5}/2$ (the no-common-torus
   argument). The report uses only the correct forms; no number in any
   table depended on the confusing line.
4. **$D_{4}$ run stopped early (deliberate, logged).** The local $D_{4}$
   invocation was killed after $10$ runs (SIGTERM, `d4_full.log`) once the
   replication sample was complete ($10/10$, §2.5); the twelfth-mode
   checkpoint's final row was recovered from its `.npz` and agrees with
   the prior study. The $D_{4}$ arm therefore rests on the prior
   field-test trajectories plus the local replication, stated in §2.5 and
   A5 — not on a completed local $D_{4}$ run. Completing it is costed in
   §8.
5. No other discrepancies. No silent corrections were made: every change
   above is recorded here.

## 7. Evidence that would change the answer

- A **wider retained band** ($K=6$ full study, not just $3$ refinement
  runs) in which the $A_{4}$* twelve-mode seeds reach full, or the trap
  moves/disappears — would demote the trap from a dynamical finding to a
  band artefact.
- A **different quench point** (deeper $r$, different $m$, $\delta=0.25$)
  in which $A_{4}$* twelve-mode seeds reach full while $D_{4}$ seeds trap —
  would reverse the reliability comparison (C5b).
- **More replicates** ($n\ge10$ per family) in which the six-mode trap
  frequency moves far from $1/3$, or a twelve-mode $A_{4}$* run reaches
  full — would change the counts, though not the existence of the trap
  (already seen $4$ times).
- **Longer time** ($t\gg200$) in which a trapped run leaves the $A_{3}$
  state — would change "stationary attractor" to "long-lived transient".
- A **common-torus approximant** study (rational approximants to the
  $A_{4}$* star) in which both stars compete in one box — a different
  experiment that could in principle give a different ordering; it would
  not invalidate these native-cell results, which are explicitly
  single-star-cell results.
- Discovery that the $A_{4}$* cell matrix $M$ used here does not generate
  the $A_{4}$ root lattice (e.g. a Helmert-basis error) — would invalidate
  the $A_{4}$* arm entirely. The integer-coordinate and length checks in
  §1.2 are the guard against this; an independent re-derivation of $M$
  from the $A_{4}$ Cartan matrix would be the check to run.

## 8. Per-claim HLRE grades (v5.1 as amended 2026-11-12)

Tier: Standard (search exceeds hand enumeration; others may cite).
Track: F for exact/enumerative claims, E for dynamical-computation claims.
Independence: I1 throughout (all verification artificial, single local
pipeline; the parallel Co-scientist run is the designated external route
and has not been read or audited here — no I2 claimed). The I1→C bound is
repealed (2026-11-12 amendment); grades below follow the remaining rules
(remaining caps, postulation ceiling, support in the record).

| Claim | Track | Grade | Computation (worst of: bound, caps, ceiling, record) |
|---|---|---|---|
| C1. No common 4D periodic torus contains both exact stars at the same radius | F | **F2** | Exact Gram/covolume argument, re-derived here; premise ledger ends in `stars.json` transcription plus independently written root bases; F1 would need a second independent derivation route |
| C2. $A_{4}$* native-cell construction ($M$, integer $n$, $\|k\|^{2}=8$, $V=(2\pi)^{4}/(16\sqrt{5})$) | F | **F2** | Verified numerically to $10^{-12}$–$10^{-16}$ in this task; single machine route |
| C3. Onset quantities re-verified ($T,Q,S$, stationary branches/energies, boundaries) | F | **F2** | Exact brute-force enumeration plus formula checks vs A20 tables to $10^{-9}$; single machine route |
| C4. $D_{4}$ arm replication ($10/10$ local runs match prior field test) | E | **B** | I1 bound lifted by repeal; strong constrained support (energies to $1.73\times10^{-18}$); capped at B by $n=10$ partial replication, not the full $18$ |
| C5a. $A_{4}$* outcome table (§2.1, $18$ specified runs) | E | **B** | Direct report of completed, refinement-checked integrations; capped at B (single cell, single quench, $n=3$ per family) |
| C5b. $A_{4}$* forms less reliably than $D_{4}$ from sub-pattern seeds (twelve $0/3$ vs $3/3$; six $2/3$ vs $3/3$) | E | **C** | Plausible constrained hypothesis: counts are small, one quench point, one band; the direction is supported by the trap mechanism (C6) but a basin-frequency claim would need $n\ge10$ |
| C6. The $A_{4}$* trap is the equal-amplitude $A_{3}$ branch ($12$ modes at $\|a\|=0.1168$, $E=-0.00547044$) | E | **B** | Amplitudes/energy read directly from saved coefficients; branch value recomputed exactly; $4$ independent replicates; capped at B by single-band/single-quench scope |
| C7. Relaxed full-star energies ($D_{4}$ $-0.00772621$, $A_{4}$* $-0.00587749$) | E | **B** | Six $A_{4}$* full/bridge runs agree to $2\times10^{-15}$; $D_{4}$ value replicated to $1.73\times10^{-18}$; capped at B by refinement coverage ($3$ starts) |
| C8. Matching statement (§5: RMS/quench matched; initial energies and DOF counts unmatched as quantified) | E | **B** | Design facts with exact decompositions in the record |
| C9. Any general claim: basin fractions, nucleation rates, thermodynamic limit, other quench points/cells/orientations, physical $D_{4}$ selection | — | **UNVERIFIED / ABSTAIN** | Not tested here; I cannot verify these with the available tools and runs |

## 9. UNVERIFIED / ABSTAIN list

- General $D_{4}$ vs $A_{4}$* basin fractions (the $3$-replicate counts are
  not probability estimates).
- Nucleation events, critical nuclei, nucleation rates, and the
  early-universe narrative (IX.5.1/IX.5.2 remain open; nothing here supplies
  a nucleation event).
- Behaviour at any quench point other than $(r,m,\delta)=(-0.35,-0.18,0)$,
  including $\delta=0.25$ ($q_{0}^{2}=7.5$) and deeper $r$ below the
  $A_{4}$* within-star loss at $r=-0.61335$.
- Behaviour in a wider band ($K=6$ full study), a larger cell, or a
  common-torus approximant; off-band and $t>200$ stability of the trapped
  $A_{3}$ state.
- Whether the $A_{3}$ trap persists under the $A_{4}$* symmetry sampling
  used here vs other orientation samplings.
- Any statement that $D_{4}$ is selected in nature, or that IRH's $D_{4}$
  selection is dynamically established — the onset figure plus these
  trajectories are evidence at grades B/C for the specified design only.
- The parallel Co-scientist Task 4 result (not read; external verification
  pending its audit).

## 10. Costed caps for heavy work still pending (all USD 0 GCP; local VM only)

No GCP was spent on this task and none is authorised by this report.
Local costs actually incurred: $A_{4}$* main solver $660.4$ s for $18$ runs
(total invocation wall $1439.2$ s at the shared-VM CPU share, peak RSS
$393.1$ MiB); $A_{4}$* validation invocation wall $1085.1$ s (including
$6$ refinements); $D_{4}$ local replication $717.3$ solver-s for $9$
completed runs (peak RSS from the prior field test $422.9$ MiB). All
single jobs were kept under $\sim4$ GB; the $10$-minute single-job guide
was exceeded in wall time only because of the shared-VM CPU share
($\sim17\%$), not by job size — each star's main solver CPU is
$\sim11$ min.

| Pending work | Named cap (must be approved before starting) |
|---|---|
| Complete the local $D_{4}$ arm: remaining $8$ runs $+$ $6$ refinements, same design | Cap: 1,800 solver-s, USD 0 GCP, wall $\sim65$ min at current CPU share; reuses the $10$ existing checkpoints |
| $A_{4}$* twelve-mode refinements (half-$dt$ $+$ $K=6$, rep $00$) — the one refinement family not run | Cap: 300 solver-s, USD 0 GCP |
| More replicates: $10$ replicates per family per star ($60$ new runs) for basin-frequency estimates | Cap: 2,200 solver-s, USD 0 GCP, wall $\sim2$ h at current CPU share |
| Wider-band $K=6$ full study (both stars, $18$ runs each, $28^{4}$ grid) | Cap: 6,000 solver-s, USD 0 GCP — cost first by running $2$ pilot runs and re-costing before the full set |
| Second quench point ($\delta=0.25$, $r=-0.35$) on both cells, $18$ runs each | Cap: 1,500 solver-s, USD 0 GCP |
| Any GCP run (e.g. a many-replicate sweep on lean-build-4) | **NOT costed here and NOT started.** Requires a named dollar cap from Brandon first; a USD 25 GCP cap ($\sim20$ h at $\sim$USD 1.22/h on lean-build-4) is proposed for approval, not assumed |

## 11. Reproduce

```bash
cd ~/workspace/research/irh/co-scientist-tasks-2026-11-10/local-independent/task4-native-cells
~/miniconda3/envs/jacobian-conjecture-2d/bin/python verify_geometry.py
~/miniconda3/envs/jacobian-conjecture-2d/bin/python run_native_cells.py --star A4star --replicates 3 --t-final 200 --validation
~/miniconda3/envs/jacobian-conjecture-2d/bin/python run_native_cells.py --star D4 --replicates 3 --t-final 200
~/miniconda3/envs/jacobian-conjecture-2d/bin/python make_figures.py
```

$A_{4}$* script SHA-256 recorded in `a4star/parameters.json`:
`544352f265828fd617b6ab72ee7e0b57c9422b4da3272a08755a785dcc35787d`.
Checkpoints in `a4star/*.npz` and `d4/*.npz` are reused on re-invocation
with identical parameters; a different parameter set requires a fresh
output directory. Dependencies: Python $3.11.16$, NumPy $2.4.6$,
SciPy $1.17.1$, Matplotlib $3.11.2$ in the `jacobian-conjecture-2d` conda
environment (system `python3` lacks `bs4` and was not used).

## 12. File map

| File | Contents |
|---|---|
| `REPORT.md` | This report |
| `verify_geometry.py` | Exact re-verification of stars, cells, onset quantities (§1.1–§1.3) |
| `verification.json` | Machine-readable geometry/onset check record ($24$ checks, all PASS) |
| `run_native_cells.py` | Generalised native-cell Model B solver $+$ shell-only truncated comparison $+$ self-tests $+$ refinements |
| `a4star/parameters.json`, `numerical_tests.json`, `seed_manifest.json` | $A_{4}$* configuration, self-test values, seeds |
| `a4star/field_outcomes.csv`, `field_summary.csv` | $A_{4}$* per-run outcomes and per-family counts ($18$ runs) |
| `a4star/field_trajectories.csv`, `truncated_trajectories.csv` | $A_{4}$* field and shell-only trajectories ($954$ run-time rows each) |
| `a4star/spectral_trajectories.npz`, `a4star/*.npz` | $A_{4}$* star coefficients, spectra, per-run checkpoints |
| `a4star/refinement_outcomes.csv`, `check_*_trajectory.csv` | $A_{4}$* half-$dt$ / $K=6$ refinements ($6$ checks) |
| `a4star_full.log`, `a4star_validation.log` | Full $A_{4}$* run logs (exit $0$) |
| `d4/parameters.json`, `numerical_tests.json`, `field_outcomes.csv`, `field_trajectories.csv`, `*.npz` | Local $D_{4}$ replication ($10$ runs; partial invocation, see §6 point 4) |
| `d4_full.log` | Local $D_{4}$ run log (stopped after $10$ runs, §6 point 4) |
| `paired_summary.csv` | Paired outcome counts, both arms (§2.1) |
| `formation_times.json` | Per-run formation-time metrics, both arms (§2.4) |
| `paired_trajectories.png` | Paired $D_{4}$ vs $A_{4}$* trajectories (occupancy, energy, shell fraction) |
| `formation_vs_onset.png` | A20 onset figure set against paired formation-energy trajectories |
| `make_figures.py` | Figure script |

## 13. Citation record

- Manuscript / onset source: IRH v93.1, §§II.3–II.9, via
  `a20-onset/methods.md` and `stars.json` / `boundaries.csv` /
  `coefficients.csv` / `validation.json` (A20 onset task, prior programme).
- Field-test design, solver, diagnostics and $D_{4}$ arm:
  `4d-field-test/run_field_study.py`, `parameters.json`, `report.md`
  (prior programme; $D_{4}$ trajectories reused as the replicated arm,
  §2.5).
- Model module: `ws-a-core-computations/d4model.py` (parameters and
  sub-pattern definitions cross-checked; $H$ sextic not used here).
- HLRE v5.1 as amended 2026-11-12
  (`~/workspace/custom-skills/hlre-v5-1/SKILL.md`): grades A–D Track E,
  F1–F3 Track F, independence I0–I4; human-gate requirement repealed;
  I1→C bound repealed and replaced by external verification through the
  authorised agents (Co-scientist parallel run not read or audited here).
- AI contribution: the solver, analysis and this report were produced by
  the local agent (Dragon/Muse) under Brandon D. McCrary's direction;
  Brandon is the sole accountable author of any use of these results.
