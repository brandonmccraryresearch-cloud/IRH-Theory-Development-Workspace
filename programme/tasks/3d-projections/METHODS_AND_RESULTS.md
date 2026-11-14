# Three-dimensional reductions of the $D_{4}$ lattice and its 24-wave field

## Findings

The manuscript’s coordinate section is reproduced: **$D_{4} \cap {x_{4}=0} = D_{3}$ = FCC**, with 12 nearest neighbours at distance $\sqrt{2}$ in the stated integer-coordinate units. A second rational section, $x_{1}+x_{2}+x_{3}+x_{4}=0$, is also isometric to FCC. Orthogonal projection along $e_{4}$ is a different operation: its distinct positions are $\mathbb{Z}^{3}$, with overlapping contributions from different layers. The explicitly irrational normal used here gives a trivial exact lattice section, but a nontrivial cut-and-project set when a bounded internal interval is selected.

The delivered computations include finite atomic point measures, restricted and slab-averaged standing fields, their three-dimensional Fourier transforms, and independent physical-window/internal-window/source-depth tests. These are **geometric and prescribed-signal results, not empirical detector signatures**.

## 1. Source and scope

Source: `uploads/Dynamical_Selection_of_a_D_4_Substrate_f.pdf`, version 93.1, September 17, 2026. Relevant passages read:

- §II.1, pp. 4–5: the 24 roots $\pme_{i}\pme_{j}$ and isoduality.
- §II.2, pp. 5–6: the reciprocal-shell cosine construction; field values 24 at a lattice point and $-8$ at the stated non-lattice/deep-hole points.
- §II.6, p. 8: the simulation convention $k=2\alpha$, |k|${}^{2}=8$, versus unscaled roots |$\alpha$|${}^{2}=2$.
- §§II.7–8, pp. 9–11: the equal-amplitude approximation and additional harmonics of a relaxed field.
- §II.10, p. 11: the coordinate-section FCC statement.
- §§IX.1–2, p. 25: irrational projections as a tractable computation, and the unresolved dimensional assignment.

No new field-relaxation or nucleation simulation is claimed. The sampled field has equal complex-mode amplitude 1, zero imposed baseline and zero phase offsets. It is the specified 24-wave ansatz, not the manuscript’s harmonically relaxed solution.

## 2. Direct versus reciprocal coordinates

Use the direct lattice

\[
\Lambda=D_4=\{x\in\mathbb Z^4:\sum_i x_i\in2\mathbb Z\},\qquad \operatorname{covol}(\Lambda)=2.
\]

Fourier frequencies q are in **cycles per direct-coordinate unit**; angular wavevectors are $k=2\piq$. In this convention

\[
\Lambda^*=\mathbb Z^4\cup(\mathbb Z+\tfrac12)^4.
\]

The shortest reciprocal shell has 24 unit vectors:

\[
G=\{\pm e_i\}_{i=1}^4\cup\{\tfrac12(s_1,s_2,s_3,s_4):s_i=\pm1\}.
\]

This is congruent, after rotation and scale, to the manuscript’s root set $\Phi={\pme_{i}\pme_{j}}$, whose vectors have length $\sqrt{2}$. Specifically,

\[
Q=\frac1{\sqrt2}\begin{pmatrix}1&1&0&0\\1&-1&0&0\\0&0&1&1\\0&0&1&-1\end{pmatrix},\qquad G=Q\Phi/\sqrt2.
\]

Isoduality does **not** mean that $\Phi$ and the minimal reciprocal shell occupy identical coordinates. Using $\Phi$ unchanged as Fourier frequencies would put the maxima on a scaled $D_{4}$* in those coordinates. A plane called $x_{4}=0$ must also be transformed when changing conventions. This study uses the reciprocal shell G in the direct integer coordinates of §II.10, rather than conflating the two coordinate descriptions.

The actual field computed is

\[
\Psi(x)=\sum_{g\in G}e^{2\pi i g\cdot x}=\sum_{g\in G}\cos(2\pi g\cdot x)
=2\sum_{i=1}^4\cos(2\pi x_i)+16\prod_{i=1}^4\cos(\pi x_i).
\]

Both signs of every mode are included; the cosine sum has 24 terms, equivalently 12 cosine pairs of amplitude 2. Its maximum 24 occurs exactly at $\Lambda$: achieving it requires every summand to be 1, first forcing integer coordinates and then even coordinate sum. The code independently checks the explicit sum against the polynomial form, including values (24,$-8,24,-8)$ at (0,0,0,0), (1,0,0,0), (1,1,0,0), and (½,½,½,½).

For the unscaled root-wave variable u, $\Psi(x)=\Sigma\alpha \cos(\alpha\cdotu)$ with $u=(2\pi/\sqrt{2})Q$ᵀx. For the manuscript’$s k=2\alpha$ variable z, u=2z. This makes the rotation and length convention reproducible. Here |k|=$2\pi$ on G; the root-coordinate resonant magnitude differs by the stated change of variables. No absolute physical length is inferred.

## 3. Orthogonal geometry and distinct reductions

For unit normal n choose $a 4\times3$ matrix B with Bᵀ$B=I_{3}$ and Bᵀn=0. Every x decomposes as

\[
y=B^Tx,\quad t=n\cdot x,\quad x=By+tn.
\]

The code fixes B reproducibly using the Householder map $H=I-2$vvᵀ/(vᵀv), $v=e_{4}-n$, then B=(He${}_{1}$,He${}_{2}$,He${}_{3})$, the first three columns. For $n=e_{4}$ it uses $B=(e_{1},e_{2},e_{3})$. Numerical matrices are saved in `geometry_parameters_and_checks.json`.

| Operation | Definition | What is, and is not, retained |
|---|---|---|
| Exact lattice section | $\Lambda\cap{n\cdotx=0}$, expressed as y | Only lattice points lying exactly in the plane; nothing nearby is accepted. |
| Orthogonal finite-source projection | Push forward a finite atomic source by x↦Bᵀx | Every source atom remains; coincident positions carry summed weights. |
| Cut-and-project | {Bᵀ$x : x\in\Lambda$, |$n\cdotx$|$\leqh}$ | A fixed bounded internal acceptance interval is applied **before** projection. |
| Field restriction | $f(y)=\Psi($By) | A continuous field is evaluated on a plane; this is not a set of lattice sites. |
| Field slab average | $f_{h}(y)=(2h)^{-1}\int_{-h}^{h}\Psi($By+tn)dt | Continuous depth integration, not selection of lattice atoms. |

An atomic slab selection followed by projection is precisely the cut-and-project operation used here. It is not an independent kind of infinite object. Likewise, the finite-source cylinder and a finite cut-and-project crop are identical if H=h and L agree; what differs is whether internal width is held fixed or source depth is increased without bound. The code and tables retain this distinction rather than assigning different mathematics to identical finite sets.

### Rational normals

1. **$n_{r}=e_{4}$:** $y=(x_{1},x_{2},x_{3})$, $t=x_{4}$. At t=0 the remaining integer coordinates have even sum, exactly $D_{3}$. The 12 nearest vectors are permutations of $(\pm1,\pm1,0)$, with all sign choices and distance $\sqrt{2}$.
2. **$n_{d}=(1,1,1,1)/2$:** the exact section is ${x\in\mathbb{Z}^{4}:\Sigmax_{i}=0}=A_{3}$. With the stated B, $y_{i}=x_{i}+x_{4}$. Thus y is integral, $\Sigmay_{i}=2x_{4}$ is even, and the inverse is $x_{4}=\Sigmay_{i}/2$, $x_{i}=y_{i}-x_{4}$. This is an explicit isometry to $D_{3}$, not just a visual resemblance. The numerical neighbour count is again 12.

For $n_{r}$ the **full projection**, unlike the section, includes every $y\in\mathbb{Z}^{3}$: choose $x_{4}$ with the parity needed to make $\Sigmax_{i}$ even. Its finite atomic multiplicities must not be silently discarded.

### Explicitly irrational normal

\[
n_i=(1,\sqrt2,\sqrt3,\sqrt5)/\sqrt{11}.
\]

The four numerator entries are linearly independent over $\mathbb{Q} ($they are distinct basis monomials in $\mathbb{Q}(\sqrt{2},\sqrt{3},\sqrt{5}))$. Consequently $n_{i}\cdotx=0$ for integer x only if x=0. The exact lattice section is therefore **{0}**, not a 3D quasicrystal. No nonzero lattice vector is parallel to $n_{i}$ either, so the physical projection is injective. The internal projection is dense, and a fixed compact interval gives a regular cut-and-project model set. The unfiltered infinite projection is dense in $\mathbb{R}^{3}$ and is not a locally finite unit-weight atomic measure. Only its explicitly truncated finite versions are transformed here.

## 4. Finite windows and complete enumeration

The physical crop is $C_{L}={y$: |$y_{j}$|$\leqL}$; boundaries are included. The internal acceptance interval is $W_{h}=[-h,h]$, centred at zero. Values used:

- Atomic physical half-sides L=3,5,7; cut-and-project half-widths h=0.35,0.70,1.40.
- Finite-source projection: physical L=3, source half-depth H=2,4,6; no infinite-projection diffraction measure is asserted.
- Field physical half-sides L=4,8; rectangular and separable Hann windows; $96^{3}$ samples per field/window combination.

Enumeration is complete, not a crop of an insufficient source box. Any accepted point satisfies |x|${}^{2}$=|y|${}^{2}+t^{2}\leq3L^{2}+h^{2}$, so enumerating integer coordinates in $[-M,M]^{4}$ with M=ceil$\sqrt{(3L^{2}+h^{2})}$ contains every accepted point. Parity is imposed exactly. $A 10^{-11}$ geometric boundary tolerance covers floating-point B multiplication; the exact-section identities are also checked with integer coordinate equations.

Densities $N/(2L)^{3}$ use continuous cube volume. Rational integer-endpoint crops have visible surface-count corrections; those are not a change of bulk density. The largest model set contains 3,855 atoms (L=7,h=1.4).

## 5. Fourier definitions, peak positions and normalization

### Atomic point measures

For the N selected atoms, retaining projection multiplicities,

\[
A_N(q)=N^{-1}\sum_{j=1}^N e^{-2\pi i q\cdot y_j},\qquad I_N(q)=|A_N(q)|^2,\quad I_N(0)=1.
\]

The calculation is a direct ungridded 3D Fourier sum, without a voxel form factor. For the irrational model set, each $g\in\Lambda$* supplies a reciprocal candidate

\[
q_g=B^Tg,\quad t_g^*=n\cdot g,\quad
I_\infty(q_g)/I_\infty(0)=\operatorname{sinc}^2(2h t_g^*),
\qquad \operatorname{sinc}(z)=\sin(\pi z)/(\pi z).
\]

This follows by Fourier-transforming the internal interval: the unnormalized Fourier–Bohr amplitude is dens$(\Lambda)\int_{-h}^{h}\exp(2\pi$it_g*t)dt=h sinc(2ht_g*), and mean point density is h. The infinite intensity is the corresponding normalized Bragg weight, not the pointwise Fourier transform of a finite object.

The table enumerates **289 candidates** with |g|$\leq3$ and |Bᵀg|$\leq1.8$, including DC, for every irrational atomic case. This bounded 4D enumeration is not an exhaustive list of peaks in the 3D ball: the irrational reciprocal module is dense. Finite intensities are evaluated **at those analytic candidate positions**; they are not numerically optimized local maxima. Physical-window broadening and contributions from unresolved nearby frequencies can displace a finite local maximum. The separate field FFT table contains actual grid-detected maxima.

For rational FCC, $q\inD_{3}*=\mathbb{Z}^{3}\cup(\mathbb{Z}$+½$)^{3}$ are allowed. In conventional FCC indices q=(h,k,l)/2, all h,k,l must be even or all odd. The conventional cubic cell side is 2, direct density is ½, and the shortest reciprocal star has eight points $(\pm$½,$\pm$½,$\pm$½), |q|=$\sqrt{3}/2$. This **eight-vector reciprocal star** is distinct from the **12 direct neighbours**.

### Standing-field spectra

Each restricted field has analytic frequencies $q_{g}=B$ᵀg and coefficient 1 per parent g. If frequencies coincide, their **amplitudes are added before squaring**. Slab averaging multiplies each parent coefficient by sinc$(2h n\cdotg)$. There are 15 distinct frequencies for the rational coordinate restriction, including DC, and 24 each for the irrational restriction and irrational slab average.

Field table intensities are coefficient squared, with unit parent-mode amplitude. They are **not DC-normalized point-measure intensities**. The rational field has DC coefficient 2; the irrational sections have no exact DC term. If $\Psi$ is multiplied by A, non-DC powers scale as $A^{2}$; an added baseline changes DC separately.

For a finite physical window w, use the normalized transform $\int$wf $\exp(-2\pi$iq$\cdoty)/\intw$. Its exact continuous value is $\Sigma_{g} c_{g} K_{w}(q-q_{g})$. For the cube, $K_{rect}(\deltaq)=\prod_{j}$sinc$(2L\deltaq_{j})$. With the Hann window $w(y)=\prod_{j}[1+\cos(\piy_{j}/L)]/2$ inside $C_{L}$,

\[
K_{\rm Hann}(\delta q)=\prod_j\{\operatorname{sinc}(z_j)+\tfrac12[\operatorname{sinc}(z_j-1)+\operatorname{sinc}(z_j+1)]\},\quad z_j=2L\delta q_j.
\]

Both exact coefficients and continuous finite-window powers at their exact positions are in the field-mode table. These evaluations should not be mistaken for deconvolved measurements.

### Sampled 3D FFT

Each field is sampled on $[-L,L)^{3}$, 96 points per axis, without endpoint duplication. The transform is FFT(wf$)/\Sigmaw$; frequencies are cycles/unit. Bin spacing is 0.125 for L=4 and 0.0625 for L=8; Nyquist frequencies are 6 and 3, respectively, above every prescribed field-mode frequency. Off-grid irrational frequencies leak across bins; no artificial commensurate approximation is used.

Local maxima are selected using $a 3\times3\times3$ neighbourhood, |q|$\leq1.8$, power $\geq0.5$% of the full-array maximum, at most 40 per case. Both Friedel partners are retained. The FFT table reports the nearest exact mode and offset, but a nearby sidelobe is **not automatically a new underlying mode**. The finite nonperiodic cube is what is transformed; FFT binning does not establish periodicity of the irrational field.

## 6. Numerical comparison with §II.10

### Rational section: exact analytic agreement

Both rational sections contain N=171,665,1,687 atoms for L=3,5,7 in their stated B coordinates. Allowed FCC reciprocal positions have $I_{N}=1$ to roundoff, since every atomic phase equals 1 there.

| Probe q [cycles/unit] | FCC status | Ideal I/I(0) | Finite I at L=3 | L=5 | L=7 |
|---|---|---:|---:|---:|---:|
| (½,½,½) | 111, allowed | 1 | 1 | 1 | 1 |
| (1,0,0) | 200, allowed | 1 | 1 | 1 | 1 |
| (1,1,0) | 220, allowed | 1 | 1 | 1 | 1 |
| (½,0,0) | 100, forbidden in bulk | 0 | 0.0150816 | 0.00684041 | 0.00387390 |

Forbidden probes need not vanish for a finite sharp crop. Their decrease demonstrates a finite-window contribution rather than a violation of FCC selection rules.

The rational field restriction is

\[
\Psi(y,0)=2+2\sum_{i=1}^3\cos(2\pi y_i)+16\prod_{i=1}^3\cos(\pi y_i).
\]

Its frequencies and coherent amplitudes are:

| Frequency family | Count | Coefficient per frequency | Coefficient squared |
|---|---:|---:|---:|
| q=0 | 1 | 2 | 4 |
| $q=\pme_{i}$ | 6 | 1 | 1 |
| $q=(\pm$½,$\pm$½,$\pm$½) | 8 | 2 | 4 |

Thus the field’s nonzero support is FCC-compatible, but its powers are **not** the equal-weight reciprocal comb of the FCC atomic measure. All 15 commensurate field FFT powers match these coefficients squared within $7.2\times10^{-15}$.

### Rational projection: different result

At physical L=3, finite projection source depths H=2,4,6 give 857,1,543,2,229 atomic contributions, respectively, but only 343 distinct projected positions in every case. These positions are the full $7^{3}$ integer cube, not just its 171 FCC sites. At q=(½,½,½), the finite projected atomic powers are 0.0388877, 0.0117139, 0.00547959, respectively, versus exactly 1 for the FCC section. Integer q peaks remain 1. In the joint bulk/depth limit the normalized layer weights give the simple-cubic reciprocal pattern; an infinite raw count along the fibre would diverge.

### Irrational cut-and-project: nontrivial interval-selected pattern

For h=0.7:

| Physical L | N | $N/(2L)^{3}$; ideal density 0.7 | Mean absolute finite/ideal intensity difference over 288 non-DC candidates |
|---:|---:|---:|---:|
| 3 | 155 | 0.717593 | 0.0110543 |
| 5 | 699 | 0.699000 | 0.00198760 |
| 7 | 1,923 | 0.700802 | 0.000873727 |

Selected analytic candidates at h=0.7, L=7 (the negative partners also occur):

| Parent g | $q_{1}$ | $q_{2}$ | $q_{3}$ | Ideal I/I(0) | Finite $I_{N}$ |
|---|---:|---:|---:|---:|---:|
| (½,$-$½,$-$½,½) | 0.950195 | 0.136672 | 0.279761 | 0.998819 | 0.998823 |
| (1,1,0,$-1)$ | 0.024843 | $-0.379081$ | $-1.689022$ | 0.981534 | 0.981605 |
| (0,1,$-1,0)$ | 0.088687 | 1.125423 | $-0.846389$ | 0.942167 | 0.942386 |

The mean discrepancy is a descriptive convergence diagnostic for this **fixed candidate set**, not a bound on the full diffraction measure.

### Internal-window and source-depth sensitivity

At L=7, changing h from 0.35 to 0.70 to 1.40 gives N=967,1,923,3,855. This changes the limiting density and sinc-squared peak weights: it defines different model sets, not just better approximations to one object. Physical-volume convergence is not universally monotonic: h=0.35 has mean candidate error 0.00246761, 0.00296459, 0.00211989 as L increases.

With no fixed small acceptance interval, the irrational finite-source projection at L=3 has 429,863,1,309 distinct atoms for H=2,4,6. Counts keep increasing inside the same physical volume. It must not be presented as a stable locally finite 3D lattice.

### Field-window sensitivity

For the irrational field restriction, Hann-window grid maxima number 18 at L=4 and 24 at L=8 under the stated detection rule. The median nearest-mode offset decreases from 0.0579109 to 0.0336798 cycles/unit. The slab-averaged field gives 16 and 22 detected maxima: modes weakened by depth averaging need not pass a fixed threshold. These counts depend on window, resolution and threshold; the analytic supports remain 24.

The Figure 4 line is $q=q_{0}+(s,0,0)$, with $q_{0}=(-0.9501952984,-0.1366722967,-0.2797611301)$ cycles/unit, associated with $g=(-$½,½,½,$-$½). The physical-window line profiles show the expected narrowing with larger L and the different main-lobe/leakage behaviour of rectangular versus Hann apodization. Hann widths and raw peak heights must not be compared as if the observation operators were identical.

## 7. Figures and tables

![Finite lattice reductions](01_labeled_3d_geometry.png)

**Figure 1.** All real-space panels use |$y_{j}$|$\leq3$ and the same 3D view. The colour is the discarded internal coordinate t, not intensity. The rational projection retains all overlapping atomic contributions; its displayed N is not its distinct-position count. The three lower panels hold physical crop fixed and change only acceptance half-width.

![Sampled standing field](02_standing_field_3d.png)

**Figure 2.** The field is sampled on three orthogonal planes through each reduced 3D coordinate frame. These are colour-mapped amplitude surfaces, not an isosurface, a 3D density reconstruction, or the atomic projection. All use the same amplitude colour scale.

![Three-dimensional reciprocal positions](03_reciprocal_3d_peaks.png)

**Figure 3.** Top: ideal FCC reciprocal positions; irrational model-set ideal and finite powers, at the same bounded candidate positions, with marker size proportional to power and colour $\log_{10}$ power. The two irrational panels display only candidates with ideal power $\geq0.01$; the CSV includes every enumerated candidate. Bottom: actually detected 3D FFT field maxima for L=8, Hann, with a separate field-power colour scale. Point and field powers have different normalizations.

![Window sensitivity](04_window_sensitivity.png)

**Figure 4.** Physical-volume density, finite/ideal intensity error, source-depth counts, and an analytic finite-window line profile through one specified exact irrational field mode. The selected profile is a one-dimensional slice of the 3D transform, not a powder average.

Data files:

- `lattice_peak_intensities.csv`: 3,531 rows. Atomic operation, L, internal/source half-width, N, parent dual vector where applicable, q, internal dual coordinate, finite power, ideal power where defined, and probe/candidate label. Blank ideal powers for finite irrational source projections are intentional. For rational projections, ideal columns refer only to the stated joint simple-cubic limit, not the finite source.
- `field_mode_intensities.csv`: 252 rows. Exact projected modes, coherent coefficient, coefficient squared, analytic finite-window amplitudes/powers at exact q, parent multiplicity and parent vectors, for each field/L/window combination.
- `fft_detected_peaks.csv`: 238 rows. Grid-detected local maxima, rank, FFT power, nearest exact mode, offset and bin spacing, for all 12 field/window/volume cases. Ranks may exchange among symmetry-equal peaks through roundoff.
- `window_sensitivity.csv`: 18 rows. Atomic counts, distinct positions, density and the explicitly named sensitivity metric for each atomic-window test. Field-window results are in the field and FFT tables.
- `geometry_parameters_and_checks.json`: matrices, normalization, cutoffs, software versions and executed numerical checks.
- `geometry_and_samples.npz`: roots, shortest reciprocal shell, rational/irrational basis information, representative original 4D atomic samples (including the tilted rational section), and reduced field frequencies/coefficients. Keys encode sample windows; regenerate other windows with the code.

## 8. Reproduce and audit

The archive `d4_3d_reproducibility.zip` contains this report, the four figures, all tables, parameter/check records, numerical samples, `reproduce.py`, and `requirements.txt`.

After extracting, use an environment with Python $\geq3.10$ and NumPy, SciPy and Matplotlib, then run from any working directory:

```bash
python3 path/to/reproduce.py --out path/to/new-results
```

No input download, API access, random initialization or manuscript PDF is needed to reproduce the numerical outputs. The default output is the script’s own directory; choose `--out` to preserve the delivered files. `--fft-n 192` repeats the field calculations on a finer sampling grid; it changes sampling, not the physical window or analytic modes. The script regenerates numerical files and figures, not this narrative report or the ZIP.

Executed environment: Python 3.14.4; NumPy 2.5.4; SciPy 1.18.1; Matplotlib 3.11.2. See the JSON for the authoritative recorded versions. The delivered default run took approximately 18 seconds with one BLAS thread; runtime depends on hardware.

Checks executed as assertions:

1. Exactly 24 roots and 24 reciprocal-shell vectors; the $Q/\sqrt{2}$ map matches the sets.
2. B is orthonormal and orthogonal to n; the recorded irrational residual is below $2.3\times10^{-16}$.
3. Explicit Fourier field and closed form agree on test points, including the manuscript’$s 24/-8$ contrast.
4. Both rational sections have 12 nearest neighbours; the tilted-section coordinate isometry holds for all enumerated samples.
5. The tested irrational exact section contains only the origin, independently supported by the exact radical-independence argument above.
6. Rational field FFT powers match analytic coefficients squared.
7. All 12 field FFT cases match an independent factorized discrete Fourier sum at each exact mode’s nearest grid bin, with maximum power discrepancies below $4.5\times10^{-15}$. This validates the discrete transform; it is not a claim that an off-grid finite-window FFT recovers exact infinite-volume coefficients.

## 9. Interpretation limits

This computation answers the geometric part of §IX.1 for one explicitly specified irrational orientation and a documented family of windows. It does not choose an orientation or window from IRH dynamics, prove dynamical orientation selection, or settle §IX.2’s alternatives A/B/C. Other irrational normals can yield other patterns. A lattice section is not compactification, and field restriction, depth averaging and compactification are different operations.

A detector prediction would additionally require a coupling to $\Psi$ or to derived matter/defect variables, a spatial and temporal observation kernel, transfer function/resolution, units and scale calibration, and a noise/statistical model. A detector coupled to $\Psi^{2}$ would generally produce sum/difference wavevectors absent from the linear-field tables. Nothing here supplies or assumes those elements. Consequently the phrase “intensity” in this report denotes the stated mathematical squared Fourier amplitude or normalized Bragg weight only, not measured scattering power, a sky signature, or evidence for a physical four-spatial-dimensional substrate.
