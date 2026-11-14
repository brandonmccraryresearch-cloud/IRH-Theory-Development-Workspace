# Task 7 — Discriminating three-dimensional $D_{4}$ peak ratios

**CLAIM:** From the completed three-dimensional $D_{4}$ study, a small set of exactly defined peak ratios separates the FCC cross-section, the finite-source simple-cubic projection, and the irrational cut-and-project set, and separates the internal window $h$ within the cut-and-project family; most of those ratios survive finite resolution at $L=4$–$8$, with two named failures ($A_{2}$, $A_{4}$) and one marginal case (Hann window at $L=4$ on the closest peak pair).

**STATUS:** COMPUTED — local independent recomputation from the prior-programme spectra only. Arithmetic ratio values are reproduced by two independent routes (see §3). The interpretive claim that these ratios are *measurable discriminants* is graded C (Track E, I1, post-hoc ratio selection, no detector or noise model); no detector prediction is made and none is claimed. All "intensity" below means the stated mathematical squared Fourier amplitude or DC-normalised Bragg weight, never a measured scattering power.

## 1. Definitions (exact)

$q$ is in cycles per direct-coordinate unit; $k = 2\pi q$. Atomic intensities are DC-normalised, $I_{N}(q) = |N^{-1}\sum_{j} e^{-2\pi i q\cdot y_{j}}|^{2}$, $I_{N}(0) = 1$. Field-mode powers are coefficient-squared with unit parent-mode amplitude, not DC-normalised. Friedel pairs are counted once ("distinct pair") wherever a ratio is over pairs.

| ID | Definition | Peaks and normalisation |
|---|---|---|
| $A_{1}$ | $I(111)/I(200)$ | Atomic probes $q=(0.5,0.5,0.5)$ and $q=(1,0,0)$, DC-normalised |
| $A_{2}$ | $I(311)/I(111)$ | Atomic probes $q=(1.5,0.5,0.5)$ and $q=(0.5,0.5,0.5)$; negative control |
| $A_{3}$ | $I(100)/I(111)$ | Forbidden probe $q=(0.5,0,0)$ over allowed $(0.5,0.5,0.5)$ |
| $A_{4}$ | $I(110)/I(111)$ | Forbidden probe $q=(0.5,0.5,0)$ over allowed $(0.5,0.5,0.5)$ |
| $C_{1}$ | $I_{\mathrm{top}}/I_{\mathrm{2nd}}$ | Strongest / second-strongest distinct Friedel pair among the 288 non-DC CPS candidates, $I = \mathrm{sinc}^{2}(2ht^{*})$ ideal, finite-atom $I_{N}$ in parallel |
| $C_{2}$ | $I_{\mathrm{top}}/I_{\mathrm{rep}}$ | Strongest pair over the representative candidate $g=(0,1,-1,0)$, $\|q\| = 1.411$ |
| $C_{3}$ | $I_{\mathrm{top}}/\mathrm{median}(\mathrm{top}\ 10)$ | Strongest pair over the median of the 10 strongest distinct pairs |
| $C_{4}$ | Fraction of pairs with $I \geq 0.5$ (and $\geq 0.1$) | Count over the 144 distinct non-DC pairs |
| $C_{5}$ | $I_{\mathrm{CPS}}(q_{\mathrm{FCC\ probe}})$ absolute, and suppression $1/I_{\mathrm{CPS}}$ | CPS atoms evaluated at the FCC probe $q$'s; the discriminant is the absolute suppression against the section value $1$, not a ratio of two leakages (see §4) |
| $F_{1}$ | Max/min field-mode power | Rational field: half-diagonal modes (power $4$) over axis modes (power $1$); irrational section: all 24 modes power $1$ |
| $F_{2}$ | Max/min slab-mode power | Irrational slab-averaged field, $h = 0.7$: strongest mode power $0.998819$ over weakest $0.003499$ |
| $D_{1}$ | FFT detected max/min power | Grid-detected FFT peak powers within one field/window/volume case (from `fft_detected_peaks.csv`) |
| $S$ | Slice multiplicity ratio | Task 1 projected-root multiplicity, max/min over distinct projected positions |

Objects: FCC section = exact lattice section $D_{4}\cap\{x_{4}=0\}$; Z3 projection = finite-source orthogonal projection along $e_{4}$, source half-depth $H$; CPS = irrational cut-and-project set, normal $n_{i} = (1,\sqrt{2},\sqrt{3},\sqrt{5})/\sqrt{11}$, internal half-width $h$, physical half-side $L$. Field = the prescribed 24-wave ansatz $\Psi(x) = \sum_{g\in G} e^{2\pi i g\cdot x}$ with unit amplitudes, not the relaxed field.

## 2. Derivation (each step checkable)

1. Read `lattice_peak_intensities.csv` (3,531 rows), `field_mode_intensities.csv` (252 rows), `fft_detected_peaks.csv` (238 rows), `window_sensitivity.csv` (18 rows), `geometry_parameters_and_checks.json` from `3d-projections/`. Read `task1_report.md` and `d4model.py` from `ws-a-core-computations/` for $S$.
2. Atomic ratios $A_{1}$–$A_{4}$: divide the tabulated probe intensities per $(L, H)$. FCC section probes are exactly $1$ at allowed positions; the only $L$-dependence is the forbidden-probe leakage.
3. CPS ideal intensities: recompute $I_{\infty}/I_{\infty}(0) = \mathrm{sinc}^{2}(2ht^{*})$ from the tabulated $t^{*}$ and $h$ (two routes, §3); rank distinct Friedel pairs by $|\,q\,|$ key; form $C_{1}$–$C_{4}$.
4. CPS at FCC probes ($C_{5}$): regenerate the CPS atoms independently from the geometry JSON ($B$, $n_{i}$, parity rule, $|y_{j}|\leq L$, $|n\cdot x|\leq h$), verify the atom count $N$ against `window_sensitivity.csv` for five $(L,h)$ cases, then evaluate the direct Fourier sum $I_{N}(q)$ at the seven FCC probe $q$'s.
5. Field ratios: $F_{1} = 4/1 = 4$ (rational) from the tabulated coefficients; $F_{2} = 0.998819/0.003499 = 285.487$ (slab). Finite-window degradation: read $I_{\mathrm{finite\ window}}(q_{\mathrm{exact}})/I_{\mathrm{exact}}$ per mode from `field_mode_intensities.csv`; FFT-measured spread $D_{1}$ from `fft_detected_peaks.csv`.
6. Resolution: analytic kernels $K_{\mathrm{rect}}(\delta q) = \prod_{j}\mathrm{sinc}(2L\delta q_{j})$ and $K_{\mathrm{Hann}}$ as in the source §5; first zeros $1/(2L)$ (rect) and $1/L$ (Hann, verified numerically on the signed kernel); FWHM by root-finding on $|K|^{2} = 0.5$. Nearest-neighbour separations among strong CPS candidates and among the 24 field modes via `scipy.spatial.cKDTree`. Closest-pair line profile: exact separable $K_{3}$ sum of the two unit modes along the pair axis; valley/peak ratio between the centres.
7. Slice ratio $S$: recompute the 24 scaled roots projected along $e_{4}$ and $(1,1,1,1)/2$ from `d4model.SHELL`, group by rounded position, take max/min multiplicity.

## 3. Checks run

Tool verdicts (quoted): conda env python `~/miniconda3/envs/jacobian-conjecture-2d/bin/python`, Python 3.11.16, NumPy 2.4.6, SciPy 1.17.1, Matplotlib 3.11.2. `task7_compute.py` exit code 0 (run time $\sim$27 s); `task7_figures.py` exit code 0 ($\sim$56 s). The source study used Python 3.14.4 / NumPy 2.5.4 / SciPy 1.18.1, so this recomputation is also a cross-version check. No GCP spend, no browser, no network. Seed pinned: 20261114 (no RNG is used).

| Check | Verdict |
|---|---|
| $\mathrm{sinc}^{2}(2ht^{*})$ recomputed, pure-`math` route vs NumPy route, all 2,601 CPS rows | PASS, max difference $0.0$ |
| Recomputed ideal vs stored `I_infinite_DC_normalized`, all CPS rows | PASS, max difference $0.0$ |
| Probe values, pandas route vs pure-`csv`-module route | PASS, identical |
| CPS atom regeneration $N$ vs `window_sensitivity.csv`: $(L,h) = (3,0.7),(5,0.7),(7,0.35),(7,0.7),(7,1.4)$ giving $N = 155, 699, 967, 1923, 3855$ | PASS, exact in all five cases |
| Rational field $F_{1}$: half-diagonal/axis $= 4$, DC/axis $= 4$ | PASS |
| Task 1 slice recomputation: $e_{4}$ and $d_{1111}$ each 18 distinct projected roots, multiplicities 6$\times$2 and 12$\times$1 | PASS, matches `task1_report.md` §4 |
| Hann first zero on signed kernel $= 1/L$ ($0.25$ at $L=4$, $0.125$ at $L=8$) | PASS (see withdrawal note: first attempt used the squared kernel, invalid) |
| Closest irrational field-mode pair separation $0.272440$ cycles/unit | PASS, reproduced in both the field table and the CPS candidate set |

## 4. Results — discriminant table (reference case in bold; full table in `discriminant_table.csv`)

### 4.1 Atomic section vs projection

| Discriminant | FCC section $L=7$ | Z3 projection $H=6$ (and $H=2$) | Separation |
|---|---|---|---|
| $A_{1} = I(111)/I(200)$ | $1.000$ | $0.005480$ ($0.038888$) | $182\times$ ($26\times$) |
| $A_{2} = I(311)/I(111)$ | $1.000$ | $1.000$ ($1.000$) | none — negative control, FAILS |
| $A_{3} = I(100)/I(111)$ | $0.003874$ | $3.644628$ ($0.495816$) | $941\times$ ($33\times$) |
| $A_{4} = I(110)/I(111)$ | $0.003874$ | $0.016198$ ($0.001716$) | $4.2\times$ at $H=6$, but $0.11\times$ at $H=2$ — sign flips, FAILS |

$A_{3}$ for the section falls with $L$ ($0.015082$ at $L=3$, $0.006840$ at $L=5$, $0.003874$ at $L=7$): it is finite-window leakage, not a bulk FCC violation. For the projection, $A_{3}$ grows with $H$ because $I(111)$ decays ($0.038888$, $0.011714$, $0.005480$) while $I(100)$ stays $\approx 0.019$–$0.020$. $A_{4}$ is unusable: the projection value crosses the section value between $H=2$ and $H=6$, so no threshold separates the two objects across the stated window family.

### 4.2 Irrational CPS: internal-window ratios

| $h$ | $C_{1}$ ideal / finite ($L=7$) | $C_{2}$ ideal / finite | $C_{3}$ ideal / finite | $C_{4}$: pairs $I\geq0.5$ / $I\geq0.1$ (of 144) |
|---|---|---|---|---|
| $0.35$ | $1.004367$ / $1.004310$ | $1.014637$ / $1.014445$ | $1.016917$ / $1.016695$ | $36$ ($0.250$) / $58$ ($0.403$) |
| $0.70$ | $1.017609$ / $1.017541$ | $1.060129$ / $1.059887$ | $1.069756$ / $1.069473$ | $20$ ($0.139$) / $31$ ($0.215$) |
| $1.40$ | $1.072772$ / $1.073008$ | $1.268734$ / $1.269703$ | $1.316857$ / $1.318023$ | $10$ ($0.069$) / $16$ ($0.111$) |

Finite-vs-ideal agreement is better than $0.13\%$ for $C_{1}$, $0.5\%$ for $C_{2}$, at $L=7$ for every $h$; the mean absolute finite-minus-ideal difference over all 288 non-DC candidates at $h=0.7$ is $0.011016$ ($L=3$), $0.001981$ ($L=5$), $0.000871$ ($L=7$). $C_{1}$ is a weak discriminant (a $0.4\%$ effect at $h=0.35$); $C_{2}$–$C_{4}$ separate $h$ by $1.5\%$–$32\%$ and are the usable window discriminants. These ratios discriminate the window $h$, not the CPS against the section — that is $C_{5}$.

### 4.3 CPS against the FCC probes ($C_{5}$, regenerated atoms)

| $(L,h)$ | $N$ | $I_{\mathrm{CPS}}(111)$ | $I_{\mathrm{CPS}}(200)$ | Suppression $1/I(111)$ | Suppression $1/I(200)$ |
|---|---|---|---|---|---|
| $(3,0.7)$ | $155$ | $0.000129$ | $0.052104$ | $7{,}763$ | $19.2$ |
| $(5,0.7)$ | $699$ | $0.0000134$ | $0.017842$ | $74{,}402$ | $56.0$ |
| $(7,0.35)$ | $967$ | $0.0000112$ | $0.018955$ | $88{,}985$ | $52.8$ |
| $(7,0.7)$ | $1923$ | $0.00000158$ | $0.005166$ | $633{,}870$ | $193.6$ |
| $(7,1.4)$ | $3855$ | $0.000000492$ | $0.000904$ | $2{,}032{,}978$ | $1{,}105.7$ |

The section value at both probes is $1$. The $(111)$ probe is decisive at every window (suppression $\geq 7{,}763\times$); the $(200)$ probe is marginal at the smallest window ($19\times$) and strong at $L=7$ ($194\times$–$1{,}106\times$). Ratios *between* two CPS leakages (e.g. $I(100)/I(111) = 3.65, 0.17, 4.95, 0.96, 7.64$ across the five cases) are unstable by an order of magnitude and are NOT discriminants — the leakage level itself is the observable. This instability was found during the computation, not assumed: the $C_{5}$ rows in `discriminant_table.csv` therefore carry the absolute intensities, and the inter-leakage ratios are retained only in `cps_fcc_probe_intensities.csv` as a documented failure.

### 4.4 Field ratios

$F_{1}$: rational field $4.000$ (half-diagonal over axis, exact in every $L$/window case) vs irrational section $1.000$ (all 24 modes power $1$). $F_{2}$ (slab, $h=0.7$): $285.487$ exact. Finite-window power at the exact mode position, $I_{\mathrm{finite}}/I_{\mathrm{exact}}$: rational field exactly $1.000$ in all cases (commensurate modes); irrational section $0.9637$–$1.0334$ ($L=4$, rectangular), $0.9984$–$1.0141$ ($L=4$, Hann), $0.9975$–$1.0105$ ($L=8$, rectangular), $0.9999$–$1.0002$ ($L=8$, Hann) — no mode outside $\pm10\%$. Slab: the weakest mode is inflated by $+33.2\%$ ($L=4$, rectangular), $+17.7\%$ ($L=4$, Hann), $+11.6\%$ ($L=8$, rectangular), $+0.2\%$ ($L=8$, Hann); 4, 4, 2, 0 modes respectively lie outside $\pm10\%$. The effective measured $F_{2}$ is therefore still $\geq 214$ even at the worst window.

FFT-measured $D_{1}$ (detected max/min): rational field $4.000$, 15/15 modes detected, median offset $0$ in every case. Irrational section, Hann: $1.344$ ($L=4$, 18/24 detected, median offset $0.0579$) and $1.470$ ($L=8$, 24/24, median offset $0.0337$) — a spurious $34\%$–$47\%$ spread among truly equal modes, from off-grid leakage, which still leaves $F_{1} = 4$ vs $1.47$ separated by $2.7\times$. Irrational section, rectangular: $184.2$ ($L=4$, 26 detected) and $70.1$ ($L=8$) — sidelobe detections ($I$ down to $0.0042$) destroy the ratio; rectangular FFT detection FAILS as a measurement route for $F_{1}$. Slab Hann $D_{1}$ is $22.2$ ($L=4$) and $151.2$ ($L=8$), driven by weak-mode thresholding, not by the true $285.487$.

Task 1 slice ratio $S$: $e_{4}$ and $d_{1111}$ both give max/min multiplicity $2$ (6 positions of multiplicity 2, 12 of multiplicity 1, 18 distinct); $d_{1110}$ gives $24$ distinct positions all multiplicity $1$ ($S = 1$). $S$ discriminates direction within the Task 1 window ($R = 5$, 1,465 points).

## 5. Finite-resolution degradation (quantified, not asserted)

Kernel widths (cycles/unit): rectangular first zero $0.125$ ($L=4$), $0.0625$ ($L=8$); FWHM $0.110737$, $0.055368$. Hann first zero $0.25$, $0.125$; FWHM $0.180073$, $0.090036$. FFT bin spacing $1/(2L) = 0.125$, $0.0625$.

Strong-peak separations: the minimum nearest-neighbour separation among CPS candidates with $I \geq 0.1$ is $0.272440$ ($h=0.35$ and $0.70$; $0.898027$ at $h=1.4$); among candidates with $I \geq 0.5$ it is $0.272440$ ($h=0.35$), $0.844363$ ($h=0.70$), $0.953463$ ($h=1.4$). The closest pair among the 24 irrational field modes is also $0.272440$, between $q = (0.720967,-0.394613,-0.483300)$ and $q = (0.648684,-0.289729,-0.242472)$. The full 289-candidate set is dense and is NOT claimed resolved — only the strong ($I \geq 0.1$) subset is.

Closest-pair valley/peak (exact separable-kernel profile, Fig. 2 left): rectangular $L=4$: $0.00237$ (deep valley, resolved); Hann $L=4$: $0.78282$ (only a $22\%$ dip — marginally resolved, first-zero separation $0.272440 > 0.25$ is NOT a sufficient criterion); rectangular $L=8$: $0.0000085$; Hann $L=8$: $0.000192$ (both resolved). Survival summary:

| Discriminant | $L=4$ rect | $L=4$ Hann | $L=8$ rect | $L=8$ Hann | Verdict |
|---|---|---|---|---|---|
| $A_{1}$ section vs projection | survives | survives | survives | survives | SURVIVES |
| $A_{3}$ section vs projection | survives | survives | survives | survives | SURVIVES |
| $A_{2}$ | — | — | — | — | FAILS (identical) |
| $A_{4}$ | — | — | — | — | FAILS (sign flips with $H$) |
| $C_{1}$ ($h$-discriminant) | marginal | marginal | marginal | marginal | MARGINAL ($0.4\%$–$7.3\%$ effect) |
| $C_{2}$, $C_{3}$, $C_{4}$ ($h$) | survives | survives | survives | survives | SURVIVES |
| $C_{5}$ at $(111)$ | survives | survives | survives | survives | SURVIVES |
| $C_{5}$ at $(200)$ | marginal | marginal | survives | survives | MARGINAL at small window |
| $F_{1}$ analytic | survives | survives | survives | survives | SURVIVES |
| $F_{1}$ FFT-measured | FAILS | survives | FAILS | survives | window-dependent (see $D_{1}$) |
| $F_{2}$ slab | survives | survives | survives | survives | SURVIVES (weak-mode inflation $\leq 33\%$) |
| Closest strong pair resolved | yes | marginal | yes | yes | MARGINAL at $L=4$ Hann only |

## 6. Rival / failure mode

The main rival reading is that the ratios are artefacts of the chosen windows and of ratio selection after inspecting the spectra. Three pieces of evidence limit that reading: (i) $A_{1}$ and $A_{3}$ separate section from projection by $26\times$–$941\times$ across every stated window, in the same direction, with no tuning; (ii) $C_{1}$–$C_{4}$ finite values track their ideals to $<0.5\%$ at $L=7$, so the CPS ratios are not finite-size accidents; (iii) the failures are reported, not hidden — $A_{2}$, $A_{4}$, rectangular-FFT $F_{1}$, and the $L=4$ Hann closest pair all fail or go marginal, which is what a window artefact would look like, and they are the cases where the verdict changes. Remaining failure routes: a different irrational normal gives a different CPS pattern (only $n_{i}$ was computed); the full dense candidate set below $I = 0.1$ is unresolved at every window here; the slab weak-mode inflation grows if $h$ or the window shrink further; and the Task 1 slice ratios are window-dependent ($R = 5$). A detector coupled to $\Psi^{2}$ would produce sum/difference wavevectors absent from every table here, so no table ratio transfers to such a detector without a new computation.

## 7. Evidence that would change the answer

- A second irrational normal whose strong-peak ratios $C_{2}$–$C_{4}$ coincide with the $n_{i}$ values at a different $h$ would break the $h$-reading of those ratios (they would become orientation-dependent, not window-dependent).
- A larger physical window ($L \geq 12$) in which the CPS finite/ideal agreement or the $C_{5}$ $(200)$ suppression reverses would demote $C_{5}$ at $(200)$ from MARGINAL to FAILS at small windows (the $L=7$ value would stand).
- A Hann $L=4$ closest-pair measurement showing a single merged maximum (valley/peak $\to 1$) under a stated noise model would move that pair from MARGINAL to FAILS; the present $0.78282$ is a noiseless kernel value.
- Any detector/coupling model with a stated transfer function that maps these mathematical intensities to measured powers would supersede §5 for the measured ratios; until then the detector reading is ABSTAIN, not a survival claim.

## 8. HLRE grades (per narrow claim; worst-of shown)

Tier: Standard (search exceeds hand enumeration; others may cite). Track F for the arithmetic recomputations; Track E for the survival/measurability interpretation. Independence: **I1** throughout — new analysis of the same prior-programme data with shared selection choices; no external verification was performed in this local task (the parallel Co-scientist run was not read or used, per the task's independence rule). The 2026-11-12 I1-bound repeal does not raise any grade by itself; grades below follow the evidence and the remaining caps (post-hoc ratio selection caps the interpretive claim, not the arithmetic).

| Claim | Grade | Worst-of computation |
|---|---|---|
| $A_{1}$–$A_{4}$ values from the source probe tables | F2 | Two routes agree exactly (pandas vs pure-`csv`); premise ledger ends in the source CSVs, re-read here |
| $C_{1}$–$C_{4}$ ideal and finite values | F2 | `math` vs NumPy $\mathrm{sinc}^{2}$ agree to $0.0$; finite/ideal agreement $<0.5\%$ at $L=7$ |
| $C_{5}$ CPS intensities at FCC probes | F2 | Atom regeneration reproduces $N$ exactly in 5/5 cases; direct Fourier sum is independent of the source intensity table |
| $F_{1}$, $F_{2}$ exact field ratios | F2 | Coefficient arithmetic from the source table; rational case exact |
| Kernel widths, separations, closest-pair dips | F2 | Analytic kernels + numeric root-finding (Hann zero verified on the signed kernel); `cKDTree` separations |
| Task 1 slice ratio $S = 2$ ($e_{4}$, $d_{1111}$) | F2 | Recomputed from `d4model.SHELL`, agrees with `task1_report.md` |
| Strong CPS/field peaks stay resolved at $L=4$–$8$ (synthetic-kernel statement) | B (Track E) | Analytic kernel + finite-window table agree; post-hoc ratio selection noted; single normal, single orientation family |
| These ratios are measurable discriminants for the dimensional-reduction argument | C (Track E) | Post-hoc ratio selection; I1; no noise, detector, or coupling model; survives only under the stated windows |
| Any detector-measured value of these ratios | INCOMPLETE-EVIDENCE (ABSTAIN) | No transfer function, units, scale calibration, or noise model exists in the sources |

## 9. Assumption / parameter / choice ledger

- Sources: `3d-projections/` CSVs + JSON (one irrational normal $n_{i}$, $h \in \{0.35, 0.70, 1.40\}$, $L \in \{3,5,7\}$ atomic, $L \in \{4,8\}$ field, windows rectangular/Hann, FFT $96^{3}$, detection $3\times3\times3$ local max, $|q|\leq1.8$, $I \geq 0.5\%$ of global max); `ws-a-core-computations/task1_report.md`, `d4model.py` ($R=5$, 1,465 points). Nothing else was read for these tasks.
- Choices made in this task (all stated before the survival verdicts were computed): ratio definitions §1; distinct-Friedel-pair counting (144 pairs, not 288 singles); representative candidate $g=(0,1,-1,0)$ for $C_{2}$; top-10 median for $C_{3}$; strong-peak threshold $I \geq 0.1$ for the separation claim; survival criterion = valley/peak $< 0.5$ resolved, $0.5$–$0.9$ marginal, $>0.9$ merged, applied to the noiseless kernel profile; display Gaussian $\sigma = 0.07$ in Fig. 1 (display only).
- No parameters invented: every $L$, $H$, $h$, window, threshold, and peak position comes from the source tables or the geometry JSON. No benchmark figures are cited. No number is stated beyond its grade.

## 10. Withdrawal / demotion note

1. Hann first zero: the first computation applied `brentq` to $|K_{\mathrm{Hann}}|^{2}$ and returned $0.375$ ($L=4$) / $0.1875$ ($L=8$). That is invalid — a squared kernel cannot change sign, so `brentq` found a spurious crossing. Withdrawn; recomputed on the signed kernel, giving $1/L$ exactly ($0.25$ / $0.125$), asserted and passed. No report value depends on the withdrawn numbers (the FWHM values were computed on $|K|^{2} - 0.5$ and were correct).
2. CPS representative candidate: the first $C_{2}$ lookup asserted the representative row survived Friedel-pair deduplication; it did not (the partner was kept). Withdrawn as a lookup; $C_{2}$ now reads the representative intensity from the un-deduplicated table. Values unchanged in substance ($C_{2}$ ideal $1.060129$ at $h=0.7$ either way, within $10^{-6}$).
3. $C_{5}$ inter-leakage ratios: originally framed as discriminants; the computation showed them unstable by an order of magnitude across windows. Demoted to a documented failure (§4.3); the discriminant is the absolute suppression.

## 11. UNVERIFIED / ABSTAIN list

- Detector-measured values of any ratio in this report (no coupling, transfer function, noise model, units, or scale calibration in the sources).
- Whether $C_{2}$–$C_{4}$ separate $h$ for any irrational normal other than $n_{i}$ (one normal computed).
- Resolution of the full dense CPS candidate set below $I = 0.1$ at any window here (only the strong subset is claimed resolved).
- Whether the $L=4$ Hann closest pair is two maxima under any noise model (noiseless valley/peak $0.78282$ only).
- Any claim about the relaxed (harmonically corrected) field: all field ratios here use the equal-amplitude 24-wave ansatz.
- External verification of this report (local-independent task; the parallel Co-scientist run was not consulted).

## 12. Deliverables

- `REPORT.md` (this file)
- `discriminant_table.csv` — combined table (all ratios, per orientation/window)
- `discriminant_table_atomic.csv`, `discriminant_table_cps.csv`, `discriminant_table_field.csv`, `discriminant_table_fft.csv` — per-family tables
- `cps_fcc_probe_intensities.csv` — regenerated CPS intensities at FCC probes, with suppression factors and the (failed) inter-leakage ratios
- `peak_separations.csv`, `resolution_kernel_widths.csv`, `task1_slice_ratios.csv`
- `task7_fig1_reciprocal_maps.png` — paired synthetic reciprocal-space maps, plane $q_{3}=0.5$ (FCC section vs Z3 projection; CPS ideal vs finite)
- `task7_fig2_resolution.png` — closest-pair exact-kernel profiles and ratio drift with window
- `task7_compute.py`, `task7_figures.py` — reproducible scripts (pinned seed 20261114; no RNG used)
- `checks.json`, `line_profile_data.npz`, `line_profile_dips.json` — check record and profile data

## 13. Costed caps for heavy work still pending

None pending for this task: the whole computation ran locally in $\sim$27 s + $\sim$56 s, peak memory well under 4 GB, cost $\$0$, no GCP spend authorised or used. Costed proposals for follow-up (NOT started, require Brandon's approval with a named cap): (a) recompute $C_{1}$–$C_{5}$ for a second irrational normal at $L=7$, $h=0.7$ — local, $\sim$10 min, cap $\$0$; (b) extend CPS atom regeneration to $L=12$ — local, $\sim$30 min, cap $\$0$; (c) any detector-coupled prediction with a stated transfer function and noise model — new work, cost to be named before starting, cap $\$0$ until approved. Nothing is filed, committed, or written into the manuscript or any repo.
