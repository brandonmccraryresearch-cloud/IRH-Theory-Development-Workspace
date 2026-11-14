# Matched $D_{4}$–$A_{4}$* onset branches

**Result.** Exact enumeration reproduces both v93.1 stars and their 17.26% difference in the onset score. At the manuscript point, $D_{4}$ has lower excess energy than $A_{4}$* under identical mean and shell penalty. The pure equal-amplitude branches cross deeper into the quench, but shared sub-patterns already have lower variational energies there. Neither comparison establishes which pattern a field trajectory reaches.

**Active source:** `uploads/IRH_v93.1_source_rebuild_2(1).pdf`, the newly designated 33-page v93.1 rebuild. §§II.3–6 were read on pp. 6–9; mean and excess-energy conventions were checked against §§II.7–9, pp. 9–13 and the functional on p. 4. The corresponding equations and $D_{4}/A_{4}$* coefficients agree with the originally requested PDF, so the source change does not alter the computed branches. The older `co-scientist-outputs/d4-framework-comparison/gap-memo.md`, G2, supplies the question, not the active manuscript. All counts, branches and stability checks below were computed for this task. No field simulation was run. The live Academia posting was not independently checked.

## 1. Geometry and exact representation

The manuscript names **crystals**, not reciprocal stars. Its $A_{4}$* crystal uses the 20-vector **$A_{4}$ root star**, not the 10-vector minimal star of the $A_{4}$* lattice.

- **$D_{4}$:** $\alpha=\pm e_i\pm e_j$, $1\le i<j\le4$, giving 24 vectors with $|\alpha|^2=2$. Physical vectors were $k=2\alpha$, so $|k|^2=8$, exactly as in §II.6.
- **$A_{4}$* crystal:** $\alpha=e_i-e_j$, $1\le i\ne j\le5$, in $H=\{x\in\mathbb R^5:\sum_i x_i=0\}$. This is a four-dimensional space; all 20 roots have squared length 2. Physical vectors were again $k=2\alpha$, giving the **same squared length 8**.

`stars.json` gives lexicographically indexed integer intrinsic coordinates. For $A_{4}$ it also gives four-dimensional Cartesian coordinates using the orthonormal Helmert basis

\[
h_j=\frac{e_1+\cdots+e_j-j e_{j+1}}{\sqrt{j(j+1)}},\quad j=1,\ldots,4,\qquad k_j=2\alpha\cdot h_j.
\]

Cartesian floats are for inspection only. Every resonance test used exact integer coordinates in the intrinsic space. Embedding $A_{4}$ in five coordinates did **not** introduce a fifth physical dimension or five-dimensional dynamics.

### Why no shared periodic field solver was used

$A_{4}$ is periodic on its own oblique four-torus; it is not intrinsically quasiperiodic. The obstruction is a **common** torus with the matched $D_{4}$ star. Both stars span rank-four reciprocal lattices. Their unscaled primitive Gram determinants are $\det G_{D_4}=4$ and $\det G_{A_4}=5$. Scaling both stars by 2 gives determinants 1024 and 1280, respectively, and reciprocal covolumes 32 and $16\sqrt5$.

If both belonged to one discrete rank-four reciprocal lattice, their covolume ratio would be a ratio of finite integer indices. Instead it is $\sqrt5/2$, irrational. Rotation cannot change this. Thus **no common four-dimensional periodic torus, rectangular or oblique, contains both exact stars at the same radius**. In particular the manuscript's $L=2\pi$ integer grid cannot hold this $A_{4}$ star exactly, at any orientation.

Separate native cells give valid volume-normalized pure-state energies. An irrational superposition on $\mathbb R^4$, or a higher-rank periodic embedding, is a different representation, not a common 4D box. Rational approximants would change lengths/angles and possibly exact resonances; none were substituted here. Allowing unequal radii changes the matching problem and introduces differential penalties. Mixed-star states and their cross-invariants were not calculated.

## 2. Exact resonance coefficients

For the signed star $S$, let $C(s)=\#\{(k,l)\in S^2:k+l=s\}$. Ordered counts were

\[
T=\sum_{k\in S}C(-k),\qquad Q=\sum_s C(s)C(-s).
\]

An independent enumeration of all nondecreasing index triples and quartets was also performed. A multiset with repetition counts $n_j$ contributes $p!/\prod_j n_j!$ ordered tuples. `resonances.csv` lists **every** such zero-sum multiset and its weight, including opposite-pair quartets. No tolerance or FFT aliasing entered these counts.

| Crystal / audit pattern | N | Ordered T | Ordered Q | Unordered triads | Unordered quartets | $\tau^{2} = T^{2}/N^{3}$ | $q_{4} = Q/N^{2}$ | $S = \tau^{2}/q_{4}$ |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| $D_{4}$ | 24 | 192 | 3384 | 32 | 150 | 8/3 | 47/8 | 64/141 |
| $A_{4}$* | 20 | 120 | 1860 | 20 | 85 | 9/5 | 93/20 | 12/31 |
| Shared $A_{3}$ subsystem | 12 | 48 | 540 | 8 | 27 | 4/3 | 15/4 | 16/45 |
| Shared $A_{2}$ hexagonal subsystem | 6 | 12 | 90 | 2 | 6 | 2/3 | 5/2 | 4/15 |
| One opposite pair / lamellar | 2 | 0 | 6 | 0 | 1 | 0 | 3/2 | 0 |

$D_{4}$ has 1656 ordered opposite-pair-reducible quartets and 1728 others. $A_{4}$* has 1140 and 720, respectively. The score ratio is $496/423$, so the relative onset-score advantage is $73/423$, not a percentage difference in the shifted bare quench.

## 3. Matched amplitude and mean conventions

A real, equal-phase field was written as

\[
\psi(x)=m+\phi(x),\qquad \phi=A\sum_{k\in S}e^{ik\cdot x},\qquad B=\sqrt N A.
\]

Here **N counts both signs**. The coefficient of a cosine on an independent $\pm$ pair is \$2A$; $$\langle\phi$^$2\rangle$=NA^$2=B^{2}$\$. Signed B specifies the sign of the common Fourier coefficient; its absolute value is the modulation RMS. Spatial averages were native-cell volume averages (equivalently exact zero-wavevector extraction).

For shell radius $K^2=8$, define

\[
\delta=(q_0^2-K^2)^2,\quad
\alpha=r+\delta-2um+3vm^2,\quad \beta=u-3vm.
\]

Subtracting the uniform state at **the same mean** gives

\[
f=\frac{N\alpha}{2}A^2-\frac{T\beta}{3}A^3+\frac{vQ}{4}A^4
=\frac\alpha2B^2-\frac{\beta\tau}{3}B^3+\frac{vq_4}{4}B^4.
\]

Thus equal per-mode A would **not** match total modulation power across different N. The comparison matches the definitions, controls and penalty, and solves each stationary amplitude rather than forcing the two optimized amplitudes to agree.

**Absolute baseline caveat.** The literal functional on p. 4 gives $f_{\rm unif}=\tfrac12(r+q_0^4)m^2-um^3/3+vm^4/4$. At $r=-0.35,m=-0.18,q_0^2=8$, this is 1.03333644. The manuscript's quoted $-0.0034636$ instead equals the **local-potential-only** baseline, omitting $q_0^4m^2/2=1.0368$. This does not affect any fixed-mean excess energy here. It must be resolved before comparing absolute energies or common tangents across different means; it was not silently propagated into the calculation.

### Candidate amplitude equations

Write $g=\partial f/\partial B=\alpha B-\beta\tau B^2+vq_4B^3$. Fixed-mean projected Model A gives $\dot B=-\Gamma g$; conserved Model B with scalar mobility M gives $\dot B=-MK^2g$, hence the **same factor 8M for both stars**. The fixed-mean projected damped-wave equation is $\ddot B+\gamma\dot B=-g$. Projection or a mean constraint is required for the nonconserved equations; unrestricted Model A does not keep m fixed.

In per-mode amplitudes the two conserved equations are explicitly

\[
\dot A_{D_4}=-8M[\alpha A-8\beta A^2+141vA^3],\qquad
\dot A_{A_4^*}=-8M[\alpha A-6\beta A^2+93vA^3].
\]

For unequal complex amplitudes, $a_{-k}=a_k^*$, the shell-Galerkin equation is

\[
\dot a_k=-MK^2\left[\alpha a_k-\beta\!\sum_{p+q=k}a_pa_q
+v\!\sum_{p+q+s=k}a_pa_qa_s\right],
\]

where summed vectors belong to S. Off-shell harmonics are excluded; this is a candidate amplitude system, not the full field PDE.

## 4. Stationary branches and boundaries

Besides $B=0$, the signed stationary branches are

\[
B_\pm=\frac{\beta\tau\pm\sqrt{\beta^2\tau^2-4vq_4\alpha}}{2vq_4},\qquad
f_*=\frac{\beta\tau}{6}B_*^3-\frac{vq_4}{4}B_*^4.
\]

Both real roots were retained, including the barrier branch and negative-amplitude branches. The second derivative is $f''=\alpha-2\beta\tau B+3vq_4B^2$. In the scanned region $\beta$ is positive, so the positive large root is the preferred equal-phase ordered branch. For $\beta = 0$ the bifurcation is continuous at $\alpha = 0$; for $\beta < 0$ the preferred sign reverses.

For $s=2um-3vm^2-\delta$, the characteristic bare-quench values are

\[
r_{\rm fold}=s+\frac{\beta^2 S}{4v},\qquad
r_{\rm deg}=s+\frac{2\beta^2 S}{9v},\qquad
r_{\rm linear,shell}=s.
\]

At fixed mean, $r_{\rm deg}$ is ordered/uniform equal energy. It is the manuscript's “coexistence” convention, **not** a conserved-system common-tangent construction permitting two different means. For $\delta > 0$, $r_{\rm linear,shell}$ is the candidate-shell threshold, not necessarily the first instability of the unrestricted continuum field.

With $t=\alpha v/\beta^2$, numerical root finding between $-0.2$ and 0 gave the pure $D_{4}/A_{4}$* equal-energy crossing

\[
t_\times=-0.05660244647912457,\qquad r_\times=s+(\beta^2/v)t_\times.
\]

$D_{4}$ has the lower ordered-branch energy above this crossing, wherever both branches exist; $A_{4}$* is lower below it **only within this pairwise equal-amplitude comparison**.

### Numerical check at the manuscript point

$u=v=1,\ m=-0.18,\ r=-0.35,\ \delta=0$ gives $\alpha=0.1072,\beta=1.54$.

| Branch | Per-mode A | RMS B | Excess f | Within full star |
|---|---:|---:|---:|---|
| Uniform | 0 | 0 | 0 | Linearly stable on shell |
| $D_{4}$ large root | 0.07757529634 | 0.3800397854 | $-0.007632267319$ | Local minimum modulo translations |
| $A_{4}$* large root | 0.08594252409 | 0.3843466521 | $-0.005816677329$ | Local minimum modulo translations |
| $D_{4}$ small root | 0.00980059019 | 0.04801289027 | +0.000038585208 | One negative Hessian eigenvalue |
| $A_{4}$* small root | 0.01341231462 | 0.05998169443 | +0.000059264885 | One negative Hessian eigenvalue |

The $D_{4}$ energy agrees with §II.8. The matched $A_{4}$* comparison is new here. At $\delta = 0.25$ the same point has $\alpha = 0.3572$ and **neither full-star branch exists**.

| Characteristic r at $m = -0.18$, $\delta = 0$ | $D_{4}$ | $A_{4}$* |
|---|---:|---:|
| Ordered fold | $-0.188082270$ | $-0.227690323$ |
| Fixed-mean uniform degeneracy | $-0.217984240$ | $-0.253191398$ |
| Uniform candidate-shell linear threshold | $-0.457200000$ | $-0.457200000$ |
| Pairwise equal energy | $-0.591438362$ | $-0.591438362$ |
| First full-star nonradial instability | $-1.026165167$ | $-0.613354733$ |

The last $D_{4}$ value is an analytic continuation outside the bounded r scan, explicitly flagged in `boundaries.csv`. Adding $\delta = 0.25$ shifts **every** listed r down by 0.25; it does not change the intrinsic ranking.

## 5. Unequal-mode/phase stability and shared sub-patterns

Radial minima were not automatically classified as stable patterns. The real-field Hessian was calculated on all 24 or 20 real shell degrees of freedom, including phases:

\[
H_{kl}=\alpha\delta_{kl}-2\beta A\,1_S(k-l)+3vA^2C(k-l).
\]

On a stationary branch its eigenvalues have the form $\lambda=l\beta A+h vA^2$. The joint coefficient pairs and multiplicities are in `stability-spectrum.csv`. For $D_{4}$ they are $(-8,282)_1,(8,-102)_9,(12,-108)_8,(16,-78)_2,(0,0)_4$. For $A_{4}$* they are $(-6,186)_1,(4,-54)_4,(10,-60)_6,(10,-54)_5,(0,0)_4$. The four identically zero eigenvalues are translations, not instabilities.

The first nonradial losses on the preferred large branch are exactly

\[
t_{D_4}=-208/867,\quad A=4\beta/(51v)\quad(9\text{ modes});\qquad
 t_{A_4^*}=-16/243,\quad A=2\beta/(27v)\quad(4\text{ modes}).
\]

$A_{4}$* is therefore locally stable within its star only over a short interval below the pairwise crossing; deeper down its equal-amplitude energy belongs to a saddle. $D_{4}$ also eventually loses stability. These checks do not test off-shell harmonics, sidebands or spatial envelopes.

The shared 12-mode $A_{3}$, 6-mode $A_{2}$ and 2-mode lamellar patterns were added as a **variational audit**, not as an exhaustive candidate search. $D_{4}$ and $A_{3}$ cross at $t=-0.0120858493890$, before the $D_{4}/A_{4}$* crossing. The audit envelope subsequently changes from $A_{3}$ to $A_{2}$ at $-0.0489684787460$ and from $A_{2}$ to lamellar at $-1.91312923045$. At the $D_{4}/A_{4}$* crossing, their scaled energies are both $-0.00537193764$; $A_{3}$ is $-0.00590135977$ and $A_{2}$ is $-0.00599488680$. Thus the apparent $A_{4}$* victory is **preempted in this enlarged variational set**. This does not establish global equilibrium, since other unequal-amplitude and mixed states were not optimized. Sub-pattern Hessian labels in the tables concern their occupied subspace, not all omitted parent-star modes.

## 6. Concise computational methods and reproduction

Integer root lists were constructed directly, without downloads or lattice-library conventions. Pair-counter counts were cross-checked against complete unordered multiset enumeration. Hessian coefficient matrices were checked to commute exactly. Joint eigenvalue pairs were discovered numerically and then **certified by rational Gaussian elimination** of each joint nullspace, with dimensions summing to N. Independent real cosine/sine finite-difference checks gave directional Hessian errors below $2.1\times10^{-8}$. Stationarity residuals were checked below $10^{-11}$.

The bounded scan used **u = v = 1**, **$m \in [-0.35, 0.25]$ in steps of 0.01**, **$r \in [-0.80, 0.50]$ in steps of 0.01**, and **$\delta \in {0, 0.25}$**: 7,991 points per penalty, 15,982 total. For fixed $K^2=8$, these penalties can be realized by $q_0^2=8$ and 7.5, respectively. Every real nonzero signed root and the uniform state were tabulated. Figure colors show the lowest energy among the explicitly included ansätze, not observed dynamical outcomes. Boundaries were evaluated from analytic formulas or the universal scalar energy root, not inferred from colored grid pixels. Values outside the scan were retained with explicit in-bounds flags.

`scan-branches.csv.gz` contains 90,024 stationary rows, including 15,982 uniform rows. Columns give candidate, branch, r, mean, penalty, $\alpha$, $\beta$, signed RMS B, Fourier A, excess energy, radial curvature/type, and within-star Hessian negative/zero counts and type. Uniform Hessian counts are blank because no single occupied star is assigned; its shell-linear classification is reported. `representative-branches.csv` is the small readable subset, including characteristic points. Missing patterned rows mean that no real nonzero stationary branch exists at that point, not that an energy was replaced by zero.

From the workspace root, rerun:

```bash
python3 co-scientist-outputs/d4-a4star-onset/reproduce.py
# To preserve these outputs while checking a second run:
python3 co-scientist-outputs/d4-a4star-onset/reproduce.py --out co-scientist-outputs/d4-a4star-onset-rerun
```

The archive includes the source and every deliverable. Dependencies are Python 3 with NumPy, SciPy and Matplotlib; the recorded run used Python 3.14.4, NumPy 2.5.4, SciPy 1.18.1 and Matplotlib 3.11.2. `validation.json` records checks, bounds, software versions and source-file SHA-256 hashes. A second run into a separate output directory reproduced eight generated files byte-for-byte and the compressed scan table identically after decompression. No random field initial condition, box approximation, stochastic success rate or time integration enters these results.

**Scope of the selection statement.** $D_{4}$ orders first among these pure equal-phase stars, with matched controls, and is locally stable within its star near onset. At positive $\alpha$ the uniform state is also locally stable, so access requires a finite perturbation or another path. The calculation closes the exact-combinatorics and matched-pure-branch part of G2. It does not close its dynamical-competition, nucleation or unbiased-emergence parts.
