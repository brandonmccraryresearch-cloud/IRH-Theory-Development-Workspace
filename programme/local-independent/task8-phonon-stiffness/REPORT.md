# Task 8 — D4 phonon stiffness and Burgers-vector costs

**CLAIM:** Deforming the phase-locked 24-mode D4 standing wave gives an exactly isotropic harmonic stiffness with Lamé coefficients $\lambda = \mu = 256 A_*^2 = 1.5405892101$ (phase-only, frozen amplitude — a variational upper bound on the relaxed moduli); the first anisotropy enters at cubic order in strain. Burgers-vector classes are the single $W(F_4)$ orbit on each $D_4$ shell $|b|^2 = 2, 4, 6, 8, 10, 12$ (verified computationally); a dislocation sheet's energy per unit area is $E/A = K \ln(R/r_0)$ with $K$ proportional to $|b|^2$ and a factor $2$ between edge and screw character, and at the reference radius $R = 20$ the $|b|^2 = 4$ dislocation is bound against splitting into elementaries at all $R$, while $|b|^2 = 6, 8, 12$ split for $R$ above $16.6$, $12.8$, $19.2$ (edge) and $|b|^2 = 10$ splits only above $R = 23.9$ (edge).

**STATUS:** VERIFIED for the stiffness coefficients, the Burgers-vector classification, and the edge/screw energy coefficients (Track E grade B, Track F grade F2 for the exact identities; see §8). The core radii and the $R = 20$ split verdicts rest on an estimated core criterion and are grade C. The phonon (phase-mode) relaxation rate of the **relaxed** standing wave is ABSTAIN — the trial-mode numbers computed here are not that rate (§6, §9).

Local independent work only. No Co-scientist output was read or used; no browser, no Academia, no GCP spend, no commits, no manuscript edits.

## 1. Inputs (all verified from the prior sources, nothing assumed)

The functional, from the manuscript §§II.6–II.9 and `d4model.py`:

$$F[\psi] = \int d^4x\, \left[ \tfrac12 \psi \left(r + (q_0^2 + \nabla^2)^2\right) \psi - \tfrac{u}{3}\psi^3 + \tfrac{v}{4}\psi^4 \right], \quad r = -0.35,\ u = v = 1,\ q_0^2 = 8,\ \bar\psi = -0.18.$$

Derived parameters, re-verified in `task8_stiffness.py` (NumPy roots vs python-flint arb, 50 digits, difference $1.4\times10^{-17}$):

$$r_{\mathrm{eff}} = r - 2u\bar\psi + 3v\bar\psi^2 = 0.1072, \qquad \beta = u - 3v\bar\psi = 1.54, \qquad A_* = 0.077575296339281, \qquad A_*^2 = 0.006017926602,$$

where $A_*$ is the larger root of $141 A^2 - 8\beta A + r_{\mathrm{eff}} = 0$ (A6 report §1; manuscript §II.8 gives $A_* = 0.0776$, $F/V = -0.0076323$ excess over the uniform state). The $D_4$ lattice is $\Lambda = \{x \in \mathbb{Z}^4 : \sum_i x_i \text{ even}\}$; its $24$ roots are $\pm e_i \pm e_j$ ($|a|^2 = 2$, unscaled); the reciprocal shell is $g = 2a$, $|g|^2 = 8$ (`d4model.py`, `d4_roots`). The standing wave is $\psi_0(x) = \bar\psi + A_* \sum_{g \in S} e^{ig\cdot x}$ with $|S| = 24$ (A6 report §1), triad phase-locked ($\phi_1 + \phi_2 + \phi_3 = 0$ on every closed triad, manuscript VI.1). Condensation density used for the core estimate: $|F|/V = 0.0076323$ (one-mode, manuscript §II.8; relaxed value $0.0077276$ differs by $1.25\%$).

Correction to a prior-source statement (see §10, item C4): `task2_report.md` describes its moments over the scaled roots $(\pm2,\pm2,0,0)$, but $M_2 = 12|k|^2$ and $M_4 = 12|k|^4$ hold for the **unscaled** roots (for $k = e_1$, the scaled sum gives $48$, the unscaled sum gives $12$). All moment values in task 2 are unscaled-root values; this report uses unscaled roots for moments and scaled roots $g$ for the shell, and the distinction is stated wherever it matters.

## 2. Derivation — harmonic stiffness

**Step 1 — phase deformation.** Let $u(x)$ be a slowly varying displacement field, $|\nabla u| \ll 1$, $|q| \ll q_0$ for its Fourier content. The deformed pattern is

$$\psi_u(x) = \bar\psi + A_* \sum_{g \in S} e^{ig\cdot(x + u(x))}.$$

Only phases move; the per-mode amplitude $A_*$ is frozen (justification and cost in §7). The local wavevector of mode $g$ is $k_g = g + (\nabla u)^T g$, so

$$|k_g|^2 = |g|^2 + 2\, g^T \varepsilon\, g + O(|\nabla u|^2), \qquad \varepsilon_{ij} = \tfrac12(\partial_i u_j + \partial_j u_i).$$

Only the symmetric strain $\varepsilon$ enters at this order: $g^T \Omega\, g = 0$ for the antisymmetric part $\Omega$ of $\nabla u$, and a finite rotation costs exactly zero (the wavevectors rotate rigidly, $|k_g|$ unchanged) — the $O(\Omega^2)$ length change of the linearised rotation is cancelled by the symmetric part of the finite rotation.

**Step 2 — gradient term.** On the shell $q_0^2 - |k_g|^2 = -2\, g^T\varepsilon\, g + O(|\nabla u|^2)$, and the linear term vanishes because the shell is tuned ($q_0^2 = 8 = |g|^2$). The quadratic (Brazovskii) part of $F$ therefore contributes, per unit volume,

$$\frac{\Delta F}{V} = \frac12 A_*^2 \sum_{g \in S} \left(q_0^2 - |k_g|^2\right)^2 = 2 A_*^2 \sum_{g \in S} (g^T \varepsilon\, g)^2 + O(|\varepsilon|^3).$$

**Step 3 — nonlinear terms contribute nothing at this order.** For a uniform strain the deformed field is locally a translated copy of $\psi_0$; the volume averages $\langle \psi^3 \rangle$ and $\langle \psi^4 \rangle$ depend only on the triad/quadruple phase sums, which the deformation preserves ($g_1 + g_2 + g_3 = 0 \Rightarrow \phi_1 + \phi_2 + \phi_3 = 0$ still). Hence the cubic/quartic terms give no $O(\varepsilon)$ or $O(\varepsilon^2)$ stiffness for uniform strain. (At finite modulation wavevector $q$ they do contribute a $q$-independent constant that exactly cancels the $r$-term of the gradient part — measured in §4, not assumed.)

**Step 4 — the root sum (exact).** Summing over the $24$ roots gives the exact identity, verified symbolically in SymPy 1.14.0 and numerically over $200$ random strains (max deviation $9.1\times10^{-13}$):

$$\sum_{g \in S} (g^T \varepsilon\, g)^2 = 128\, \mathrm{Tr}(\varepsilon^2) + 64\, (\mathrm{Tr}\,\varepsilon)^2.$$

Equivalently over unscaled roots, $\sum_a (a^T\varepsilon\, a)^2 = 8\, \mathrm{Tr}(\varepsilon^2) + 4\, (\mathrm{Tr}\,\varepsilon)^2$. Therefore

$$\frac{\Delta F}{V} = 256 A_*^2\, \mathrm{Tr}(\varepsilon^2) + 128 A_*^2\, (\mathrm{Tr}\,\varepsilon)^2 + O(|\varepsilon|^3).$$

Writing the elastic density in the standard form $f = \tfrac12 \lambda (\mathrm{Tr}\,\varepsilon)^2 + \mu\, \mathrm{Tr}(\varepsilon^2)$:

$$\lambda = \mu = 256 A_*^2 = 1.5405892101, \qquad B_{\mathrm{(4D)}} = 384 A_*^2 = 2.3108838152, \qquad \lambda + 2\mu = 768 A_*^2 = 4.6217676304.$$

The quadratic stiffness is **exactly isotropic** — no direction appears — as it must be, since it depends only on the fourth moment of the root system, which is isotropic through fourth order (task 2). Note $\lambda = \mu = 1.5405892101$ is numerically close to $\beta = 1.54$ (difference $+0.000589$, $0.038\%$); that is a coincidence, not an identity — no derivation connects them, and the two numbers are not interchanged anywhere in this report.

Spot values (from `tables/task8_stiffness_coefficients.csv`): uniaxial strain $\varepsilon = e\,\hat n \hat n^T$ along any of $\langle100\rangle$, $\langle110\rangle$, $\langle111\rangle$, $\langle1111\rangle$ gives $f = 384 A_*^2 e^2 = 2.310884\, e^2$; hydrostatic $\varepsilon = e I$ gives $f = 18.487071\, e^2$; pure shear $\varepsilon_{12} = \varepsilon_{21} = 1/2$ gives $f = 128 A_*^2 = 0.770295$ at unit engineering shear.

## 3. Derivation — cubic (anharmonic) correction and first anisotropy

Expanding $(q_0^2 - |k_g|^2)^2$ to the next order, with $M = \nabla u$ and $M = \varepsilon$ (pure strain),

$$\frac{\Delta F}{V} = 2 A_*^2 \sum_g (g^T\varepsilon\, g)^2 + 2 A_*^2 \sum_g (g^T\varepsilon\, g)(g^T\varepsilon^2 g) + O(|\varepsilon|^4),$$

so the cubic coefficient is $f_3 = 2 A_*^2 \sum_g (g^T\varepsilon\, g)(g^T\varepsilon^2 g)$. Results (exact root sums, `task8_stiffness.py`):

- Uniaxial strain in **any** direction: $f_3 = 384 A_*^2 = 2.310884$, i.e. $f_3/f_2 = +1$ exactly (verified over $200$ random directions, spread $5.8\times10^{-15}$). The sixth moment does not enter here because $\sum_g (g\cdot\hat n)^4$ is the isotropic fourth moment.
- Pure shear and the biaxial states $\mathrm{diag}(1,-1,0,0)$, $\mathrm{diag}(\tfrac12,\tfrac12,-\tfrac12,-\tfrac12)$: $f_3 = 0$ exactly.
- Hydrostatic: $f_3 = 3072 A_*^2 = 18.487071$, $f_3/f_2 = +1$.
- Diagonal strains have the closed form (verified against the direct root sum on $200$ random diagonal strains, max deviation $4.3\times10^{-14}$):

$$f_3 = 128 A_*^2 \sum_{i<j} (e_i + e_j)(e_i^2 + e_j^2), \qquad \varepsilon = \mathrm{diag}(e_1, e_2, e_3, e_4).$$

- Anisotropy first appears for multi-axial strains: for $\varepsilon = \mathrm{diag}(\cos t, \sin t, 0, 0)$, $f_3$ ranges over $[-2.371862,\, +2.371862]$ (721-point scan, `tables/task8_biaxial_f3.csv`; extrema at $t \approx 80.5^\circ$ and $260.5^\circ$), exceeding the uniaxial value by $2.6\%$. Over $300$ random unit-Frobenius-norm strains, $f_3 \in [-2.301,\, +2.339]$ with mean $0.05$ and standard deviation $1.13$. This is the elastic counterpart of the task-2 sixth-moment anisotropy ($M_6$ mean $15$, min $12$, max $18$): the sixth moment is the first directionally dependent moment, and it enters the elastic energy at third order in strain.

**Regime of validity (harmonic/linear).** For uniaxial strain $f_3/f_2 = e$, so the harmonic approximation is $10\%$-accurate at $|e| \lesssim 0.1$ and breaks down at $|e| \sim 1$; the long-wave condition is $|q| \ll q_0 = \sqrt{8} \approx 2.828$ (wavelength $\gg a_0 = 2\pi/q_0 \approx 2.221$). The stiffness is **not** extrapolated beyond this regime anywhere in this report.

## 4. Independent real-space check of the stiffness (§2–§3)

A second, independent route (`task8_phonon_rates.py`, pseudospectral, box $L = 4\pi$, $N = 32$ per axis, displacement amplitude $U = 0.01$): for $u(x) = U\cos(qx_1)\hat e$ the exact linearised operator $H\eta = (r + (q_0^2 + \nabla^2)^2)\eta - 2\psi_0\eta + 3\psi_0^2\eta$ (A6 construction) is applied to the phase perturbation $\eta$, and $\Delta F/V = \tfrac12\langle\eta, H\eta\rangle$ is compared with §2. The $H$ application itself is validated by centred finite differences of $\mu[\psi]$ (rel. $L^2$ error $4.185\times10^{-9}$ at $\delta = 10^{-3}$; see §10, item C3 for the $\delta$-sweep diagnosis). Findings, $q \le 1.5$:

- The gradient part $\tfrac12\langle\eta, H_{\mathrm{grad}}\eta\rangle$ matches its analytic mode-sum formula to $\sim 10^{-15}$ relative error at every $q$ and polarisation.
- The nonlinear part is **exactly** $\Delta F_{\mathrm{nl}} = +4.2\, A_*^2 U^2 = -12r\, A_*^2 U^2$ at every $q \le 1.5$ and both polarisations — the constant that cancels the gradient part's $12r$ term at $q = 0$ (Goldstone cancellation). This confirms §2 Step 3's claim in the precise finite-$q$ form: the nonlinear terms contribute a $q$-independent constant, not stiffness.
- The full curvature is exactly

$$\frac{\Delta F}{V} = A_*^2 U^2 \left(C_0 q^2 + 12 q^4\right), \qquad C_0 = 192\ \text{(longitudinal)},\quad C_0 = 64\ \text{(transverse)},$$

with the $q \le 1.5$ fit returning $C_0 = 192.0000$ / $64.0000$ and slope $12.0000$ (Fig. 1b). Since $\tfrac14(\lambda + 2\mu) = 192 A_*^2$ and $\tfrac14\mu = 64 A_*^2$, this is the §2 stiffness recovered from a fully independent real-space route. The $q^4$ term ($12 A_*^2 U^2 q^4$) is the first finite-wavelength correction; it is $6.25\%$ of the leading term at $q = 1$ (longitudinal), $25\%$ at $q = 2$ — hence the long-wave regime is $q \lesssim 1$.
- The $q = 2$ points are **excluded for cause**: at $q = 2$ the trial mode's Fourier components collide ($g + q = g' - q$ for distinct roots, with cancelling coefficients), its support collapses from $24$ to $12$ nonzero coefficients (verified numerically; the coefficient at $k = (0,2,0,0)$ is $\sim 10^{-19}$), and the analytic gradient formula fails by $7$–$10\%$. The measured $q = 2$ curvatures are retained in `tables/task8_phonon_rates.csv` and plotted as excluded markers.

| $q$ | pol. | $\Delta F/V$ measured | analytic ($\S2$) | rel. err. | $\Delta F_{\mathrm{grad}}$ vs formula | $\Delta F_{\mathrm{nl}}/(A_*^2U^2)$ |
|---|---|---|---|---|---|---|
| 0.5 | L | $2.933739\times10^{-5}$ | $2.888605\times10^{-5}$ | $1.6\%$ | $3.8\times10^{-16}$ | $+4.2000$ |
| 0.5 | T | $1.008003\times10^{-5}$ | $9.628683\times10^{-6}$ | $4.7\%$ | $3.4\times10^{-16}$ | $+4.2000$ |
| 1.0 | L | $1.227657\times10^{-4}$ | $1.155442\times10^{-4}$ | $6.3\%$ | $6.8\times10^{-16}$ | $+4.2000$ |
| 1.0 | T | $4.573624\times10^{-5}$ | $3.851473\times10^{-5}$ | $18.8\%$ | $3.1\times10^{-16}$ | $+4.2000$ |
| 1.5 | L | $2.965333\times10^{-4}$ | $2.599744\times10^{-4}$ | $14.1\%$ | $7.4\times10^{-16}$ | $+4.2000$ |
| 1.5 | T | $1.232170\times10^{-4}$ | $8.665814\times10^{-5}$ | $42.2\%$ | $7.4\times10^{-16}$ | $+4.2000$ |

(The "rel. err." column is the expected $12q^4/(C_0 q^2)$ finite-wavelength correction, not a discrepancy: the full $C_0 q^2 + 12q^4$ law accounts for it exactly.)

## 5. Derivation — Burgers-vector classes and dislocation energies

**Lattice and point group.** Burgers vectors live in the $D_4$ lattice $\Lambda$. The pattern's point group is $W(F_4)$, order $1152$ (manuscript §V.1). It is generated here by signed permutations plus the Hadamard (triality) matrix $H_0 = \tfrac12\begin{pmatrix}1&1&1&1\\1&1&-1&-1\\1&-1&1&-1\\1&-1&-1&1\end{pmatrix}$; exact-rational BFS closure returns **1152** distinct matrices, and all $1152$ preserve the $D_4$ root set exactly. Burgers-vector classes are defined as orbits under this group (a class = one defect charge up to point-group symmetry). Verified computationally for $|b|^2 \le 12$ (`task8_stiffness.py`): **each shell is a single $W(F_4)$ orbit** — there is one class per $|b|^2$. Under signed permutations alone ($384$ elements, no triality) the shells $|b|^2 = 4, 10, 12$ split into two orbits each ($8+16$, $48+96$, $32+64$); triality merges them. This is the concrete content of "defect homotopy beyond elementary Burgers vectors" (manuscript IX.1): the next classes are not new shapes, they are the same orbit structure at larger radius, and the $\langle100\rangle$-type vectors $(\pm2,0,0,0)$ and the body-diagonal-type $(\pm1,\pm1,\pm1,\pm1)$ are the **same** class.

| $\|b\|^2$ | vectors | $W(F_4)$ orbits | signed-perm orbits | representative |
|---|---|---|---|---|
| 2 | 24 | 1 (24) | 1 (24) | $(-1,-1,0,0)$ |
| 4 | 24 | 1 (24) | 2 (8, 16) | $(-2,0,0,0)$ |
| 6 | 96 | 1 (96) | 1 (96) | $(-2,-1,-1,0)$ |
| 8 | 24 | 1 (24) | 1 (24) | $(-2,-2,0,0)$ |
| 10 | 144 | 1 (144) | 2 (48, 96) | $(-3,-1,0,0)$ |
| 12 | 96 | 1 (96) | 2 (32, 64) | $(-3,-1,-1,-1)$ |

($|b|^2$ is always even for $D_4$: $|b|^2 \equiv \sum_i x_i \equiv 0 \pmod 2$. The elementary class $|b|^2 = 2$ is the manuscript's "elementary dislocation charges: $24$, the shortest $D_4$ lattice vectors", §V.1.)

**Dislocation sheet.** Take a sheet spanning the $(x_3,x_4)$ plane, transverse plane $(x_1,x_2)$, and displacement $u = (b/2\pi)\theta$ with $\theta = \mathrm{atan2}(x_2,x_1)$ (circulation $\oint du = b$). Writing $b = b_e + b_s$ with $b_e$ in the transverse plane (edge part) and $b_s$ in the sheet plane (screw part), the angle-averaged elastic density is (derived from $\varepsilon_{ij} = (b_j \partial_i\theta + b_i \partial_j\theta)/4\pi$ and the §2 moduli, and verified numerically for edge, screw and mixed $b$ to rel. error $< 2\times10^{-16}$):

$$\langle f \rangle_\theta = \frac{A_*^2}{\pi^2 r^2}\left(64\,|b_e|^2 + 32\,|b_s|^2\right).$$

A pure screw dislocation costs exactly **half** the elastic density of a pure edge dislocation with the same $|b|$ — the $2{:}1$ edge/screw factor is exact in this model (it follows from $\lambda = \mu$). Integrating over the transverse plane gives, per unit sheet area,

$$\frac{E}{A} = K \ln\!\left(\frac{R}{r_0}\right), \qquad K_{\mathrm{edge}} = \frac{128 A_*^2 |b|^2}{\pi},\quad K_{\mathrm{screw}} = \frac{64 A_*^2 |b|^2}{\pi},$$

for a system of radius $R$ with core radius $r_0$. The core radius is **estimated** by energy-density balance, $\langle f\rangle(r_0) = |F|/V = 0.0076323$ (the amplitude must collapse where the elastic density exceeds the condensation density):

$$r_0^{\mathrm{edge}} = 2.261184\,|b|, \qquad r_0^{\mathrm{screw}} = 1.598898\,|b|.$$

This is much larger than the strain-unity radius $|b|/2\pi = 0.159155\,|b|$: the core is set by the small condensation density, not by order-unity strain (at $r_0$ the strain is $|\nabla u| \sim 1/(2\pi \cdot 2.26) \approx 0.07$). The core estimate is the weakest input in this section (grade C, §8); the $K$ coefficients do not depend on it. Exact nesting: $E_{\mathrm{screw}}(|b|^2) = E_{\mathrm{edge}}(|b|^2/2)$ at every $R$ (same $K$ and $r_0$), visible in the table below.

**Defect-energy map** (reference radius $R = 20 \approx 9 a_0$; full $E/A$ vs $R$ curves in `figures/task8_defect_energy_map.png`; full table in `tables/task8_burgers_classes.csv`):

| $\|b\|^2$ | $K_{\mathrm{edge}}$ | $r_0^{\mathrm{edge}}$ | $E/A$ edge ($R=20$) | $K_{\mathrm{screw}}$ | $r_0^{\mathrm{screw}}$ | $E/A$ screw ($R=20$) | $E/E_{\mathrm{elem}}$ edge | $E/E_{\mathrm{elem}}$ screw |
|---|---|---|---|---|---|---|---|---|
| 2 | 0.490385 | 3.197797 | 0.899008 | 0.245192 | 2.261184 | 0.534481 | 1.0000 | 1.0000 |
| 4 | 0.980770 | 4.522367 | 1.458107 | 0.490385 | 3.197797 | 0.899008 | 1.6219 | 1.6820 |
| 6 | 1.471154 | 5.538746 | 1.888909 | 0.735577 | 3.916485 | 1.199386 | 2.1011 | 2.2440 |
| 8 | 1.961539 | 6.395593 | 2.236396 | 0.980770 | 4.522367 | 1.458107 | 2.4876 | 2.7281 |
| 10 | 2.451924 | 7.150491 | 2.521929 | 1.225962 | 5.056160 | 1.685851 | 2.8052 | 3.1542 |
| 12 | 2.942309 | 7.832970 | 2.758092 | 1.471154 | 5.538746 | 1.888909 | 3.0679 | 3.5341 |

**Splitting.** The minimal number $n_{\min}$ of elementary roots summing to a representative of each class was found by BFS over root sums: $n_{\min} = 1, 2, 2, 2, 3, 3$ for $|b|^2 = 2, 4, 6, 8, 10, 12$ (e.g. $(2,2,0,0) = (1,1,0,0) + (1,1,0,0)$; $(3,1,1,1) = (1,1,0,0) + (1,0,1,0) + (1,0,0,1)$). Comparing a composite dislocation with $n_{\min}$ infinitely separated elementary sheets of the same character (interaction energy between separated sheets not included — see §7):

| $\|b\|^2$ | $n_{\min}$ | edge: split cheaper at $R=20$? | edge $R^*$ | screw: split cheaper at $R=20$? | screw $R^*$ |
|---|---|---|---|---|---|
| 4 | 2 | No | none (bound at all $R$) | No | none (bound at all $R$) |
| 6 | 2 | Yes | 16.62 | Yes | 11.75 |
| 8 | 2 | Yes | 12.79 | Yes | 9.04 |
| 10 | 3 | No | 23.91 | Yes | 16.91 |
| 12 | 3 | Yes | 19.19 | Yes | 13.57 |

For $|b|^2 = 4$, $K_b = n_{\min} K_e$ exactly, so the composite is cheaper by a constant $K_e \ln 2$ ($0.3399$ edge, $0.16995$ screw) at **every** $R$ — the doubled root is a bound state, never driven to split by system size. The other classes cross over at the tabulated $R^*$: below $R^*$ the composite is cheaper, above it the split state is. (At asymptotically large $R$ the ratio $E/E_{\mathrm{elem}} \to |b|^2/2$, so every class with $n_{\min} < |b|^2/2$ eventually splits; only $|b|^2 = 4$ has $n_{\min} = |b|^2/2$.)

## 6. Phonon relaxation rates — ABSTAIN

For the trial phase perturbation $\eta$ the formal dissipation diagnostic $\Gamma_{\mathrm{trial}} = -\langle|\nabla\mu|^2\rangle / (2\,\Delta F/V)$ with $\mu = H\eta$ gives:

| $q$ | $\Gamma_{\mathrm{trial}}$ (L) | $\Gamma_{\mathrm{trial}}$ (T) |
|---|---|---|
| 0.5 | $-43.44$ | $-49.71$ |
| 1.0 | $-251.83$ | $-227.98$ |
| 1.5 | $-927.27$ | $-754.78$ |
| 2.0 | $-2885.57$ | $-1788.63$ |

These numbers are **not** the phonon relaxation rate of the standing wave, and are not presented as such. Reasons: (i) $\eta$ is a phase perturbation of the **unrelaxed** frozen ansatz, whose residual has Fourier $L^2$ norm $4.25853893$ (A6 §4) — $\mu = H\eta$ is $O(1)$ (pointwise) even though its inner product with $\eta$ is the small elastic curvature, because the gradient and nonlinear parts of $H\eta$ nearly cancel in the inner product but not pointwise, so $\langle|\nabla\mu|^2\rangle$ is dominated by non-phase content; (ii) $\eta$ is not an eigenmode of $H$, so the dissipation identity does not give a modal decay rate (and the background field itself decays, entangling the $O(1)$ and $O(\eta)$ terms); (iii) the $q \to 0$ extrapolation of $\Gamma_{\mathrm{trial}}/q^2$ ($\approx -150$, from $-174, -252, -412$ at $q = 0.5, 1.0, 1.5$) is an exploratory number only. The relaxed phonon dispersion requires first relaxing $\psi_0$ under Model B and then computing the Bloch spectrum about the relaxed field — costed as pending work in §9. **ABSTAIN** on any relaxed phonon rate, frequency, or lifetime.

## 7. Checks run

| check | verdict |
|---|---|
| $A_*$ NumPy roots vs python-flint arb (50 digits): diff $1.4\times10^{-17}$ | PASS |
| $\sum_g (g^T\varepsilon\, g)^2 = 128\,\mathrm{Tr}(\varepsilon^2) + 64\,(\mathrm{Tr}\,\varepsilon)^2$: SymPy 1.14.0 exact expansion $= 0$ | PASS |
| Same identity, direct summation over $200$ random strains: max deviation $9.1\times10^{-13}$ | PASS |
| Diagonal cubic formula $f_3 = 128A_*^2\sum_{i<j}(e_i+e_j)(e_i^2+e_j^2)$ vs direct sum, $200$ random diagonal strains: max deviation $4.3\times10^{-14}$ | PASS |
| Uniaxial $f_3$ direction-independent over $200$ random directions: spread $5.8\times10^{-15}$ | PASS |
| $H$ application vs centred finite difference of $\mu[\psi]$, $\delta = 10^{-3}$: rel. $L^2$ error $4.185\times10^{-9}$ | PASS |
| Gradient part of $\Delta F$ vs analytic mode-sum formula, $q \le 1.5$, both polarisations: rel. error $\sim 10^{-15}$ | PASS |
| Full curvature law $\Delta F/(A_*^2U^2q^2) = C_0 + 12q^2$, $q \le 1.5$: fit $C_0 = 192.0000$ (L), $64.0000$ (T), slope $12.0000$ | PASS |
| $W(F_4)$ group order by exact-rational BFS closure $= 1152$; all $1152$ elements preserve the $D_4$ root set exactly | PASS |
| Each $\|b\|^2 \le 12$ shell is a single $W(F_4)$ orbit (orbit enumeration) | PASS |
| Dislocation angle-averaged density vs $A_*^2(64\|b_e\|^2 + 32\|b_s\|^2)/(\pi^2 r^2)$ for $b = (1,1,0,0)$, $(0,0,1,1)$, $(1,0,1,0)$, $(2,0,0,0)$: rel. error $\le 1.3\times10^{-16}$ | PASS |
| Minimal root decompositions $n_{\min} = 1,2,2,2,3,3$ by BFS over root sums | PASS |
| Relaxed-field phonon (Bloch) spectrum | NOT RUN (costed, §9) |
| Direct full-field dislocation simulation (core energy measurement) | NOT RUN (costed, §9) |
| External verification (Manus / Gemini 4 (Argon) / Co-scientist audit of this report) | NOT RUN (parent to arrange, §9) |

Tool verdicts quoted: Python 3.11.16 (conda env `jacobian-conjecture-2d`), NumPy 2.4.6, SciPy 1.17.1, SymPy 1.14.0, python-flint 0.8.0, matplotlib 3.11.2; `task8_stiffness.py` exit 0; `task8_phonon_rates.py` exit 0; `task8_figures.py` exit 0. No single local job exceeded $\sim 70$ s or the $\sim 4$ GB limit.

## 8. HLRE grades (per narrow claim; worst-of shown)

Track E unless noted. Independence is **I1** throughout: local independent re-derivation by up to three routes inside one pipeline (symbolic + direct numeric + pseudospectral); no external verification has been run for this task. The 2026-11-12 amendment (I1 bound repealed, replaced by external verification through Manus / Gemini 4 (Argon) / Co-scientist, audited locally) is the remaining gate for any grade above B; nothing here is graded A.

| claim | grade | worst-of computation |
|---|---|---|
| $\lambda = \mu = 256 A_*^2 = 1.5405892101$, $B = 384 A_*^2$ (phase-only) | B (Track E) | support B (exact symbolic + two numeric routes) / postulation ceiling B (deduced from stated premises, no fitting) / independence I1, external verification pending (caps at B, not A) |
| Quadratic stiffness exactly isotropic | B (Track E) | follows from the root-moment identity above (worst-of B) |
| Root-sum identities $\sum_g (g^T\varepsilon\, g)^2 = 128\,\mathrm{Tr}(\varepsilon^2) + 64\,(\mathrm{Tr}\,\varepsilon)^2$ and diagonal $f_3$ formula | F2 (Track F) | SymPy exact identity + independent direct summation; premise ledger closed (roots, $\varepsilon$ symmetric); external check not run |
| Cubic correction $f_3$, first anisotropy at $O(\varepsilon^3)$ (biaxial range $\pm 2.371862$ vs uniaxial $\pm 2.310884$) | B (Track E) | exact root sums + numeric scans (worst-of B, same caps as stiffness) |
| Finite-$q$ curvature law $\Delta F/(A_*^2U^2q^2) = C_0 + 12q^2$, $q \le 1.5$ | B (Track E) | pseudospectral route agrees with the analytic law to 4 decimal places at 3 $q$ values per polarisation; $q = 2$ excluded for diagnosed cause |
| Phase-only stiffness is a variational upper bound on the relaxed moduli | F2 (Track F) | deductive from the variational principle (freezing amplitude restricts the minimisation space); the *amount* of lowering is not bounded here |
| Burgers classes = one $W(F_4)$ orbit per $\|b\|^2$ shell, $\|b\|^2 \le 12$; triality merges the signed-perm split at $\|b\|^2 = 4, 10, 12$ | F2 (Track F) | exact-rational group closure (order 1152) + orbit enumeration; stated as verified to $\|b\|^2 \le 12$ only, not as a general theorem |
| Dislocation energy coefficients $K_{\mathrm{edge}} = 128A_*^2\|b\|^2/\pi$, $K_{\mathrm{screw}} = 64A_*^2\|b\|^2/\pi$; edge/screw factor $2$ | B (Track E) | exact derivation from the §2 tensor + numeric angle-average check to $10^{-16}$ (worst-of B, external verification pending) |
| Core radii $r_0 = 2.261184\|b\|$ (edge), $1.598898\|b\|$ (screw); $E/A$ values at $R = 20$ | C (Track E) | $K$ exact, but $r_0$ rests on the energy-density-balance estimate (unmeasured core criterion) and the one-mode $F$ density; $E/A$ inherits the $r_0$ uncertainty through $\ln(R/r_0)$ |
| Split verdicts and crossover radii $R^*$ | C (Track E) | depend on the $r_0$ estimate and on infinitely separated sheets (dislocation–dislocation interactions omitted); the $|b\|^2 = 4$ bound is $r_0$-independent in sign but its margin ($K_e \ln 2$) uses the $K$ values |
| Relaxed phonon dispersion / relaxation rates | ABSTAIN (no grade) | not measured; §6 trial-mode numbers are not this quantity |

## 9. Rival / failure mode

- **Amplitude relaxation.** The headline stiffness freezes the amplitude. Relaxing it can only lower the energy at fixed imposed deformation (variational bound), so $\lambda, \mu$ are upper bounds on the relaxed moduli; the manuscript's one-mode vs relaxed gap is $1.25\%$ at the operating point, suggesting the lowering is small there, but no bound on the lowering *under strain* is computed here. If amplitude relaxation under strain were large, the true moduli would be lower and the dislocation $K$ coefficients (which use the frozen-amplitude tensor) would overestimate the costs.
- **Core criterion.** $r_0$ is estimated, not measured: a full-field dislocation (relaxed amplitude collapsing at the sheet) could give a different $r_0$ by an $O(1)$ factor, shifting every $E/A$ by $K \ln(\text{factor})$ and moving the $R^*$ crossovers. The ordering of classes by $K$ is unaffected.
- **Sheet interactions and character mixing.** Split comparisons ignore the interaction energy between separated sheets (same-sign dislocations repel, like-sign interaction $\propto \ln$ distance) and assume each sheet takes a pure edge or pure screw character; a real configuration minimises over orientations and separations jointly.
- **Long-wave breakdown.** Everything in §2–§4 assumes $|\varepsilon| \lesssim 0.1$ and $|q| \lesssim 1$; at $q = 2$ the trial-mode construction already fails by mode collision. No number here is extrapolated past its regime.
- **Wrong lattice.** If the substrate lattice were not $D_4$ (or the shell not tuned, $q_0^2 \ne 8$), the linear term in $(q_0^2 - |k_g|^2)$ would not vanish and the stiffness would acquire a linear-in-strain prestress term; the derivation is conditional on the tuned shell, as stated.

## 10. Evidence that would change the answer

- A direction with quadratic stiffness differing from $256 A_*^2$ by more than the $10^{-12}$-level checks would falsify §2 (the identity is exact, so this would mean an error in the functional or the shell, not in the algebra).
- A relaxed-field computation giving moduli below $\lambda = \mu = 1.5405892101$ by more than a few percent would demote the stiffness from "the substrate stiffness" to "the frozen-amplitude upper bound" (the bound itself would stand).
- A measured dislocation core radius differing from $2.261184|b|$ (edge) would rescale all $E/A$ values and $R^*$ crossovers logarithmically; it would not change $K$, the class list, or the $|b|^2 = 4$ bound.
- A $D_4$ vector of given $|b|^2$ outside the single $W(F_4)$ orbit found here (for $|b|^2 \le 12$) would falsify the one-class-per-shell claim; the enumeration is exact, so this would mean the group generators are incomplete.
- A relaxed Bloch spectrum giving a phonon rate $\Gamma(q)$ would replace the §6 ABSTAIN with a measured dispersion.

**Withdrawal / correction notes (nothing silently corrected).**
- **C1 — edge/screw character.** The first dislocation calculation assumed one density $\langle f\rangle = 64A_*^2|b|^2/(\pi^2r^2)$ for all $b$. The numeric angle-average check for screw $b = (0,0,1,1)$ returned exactly half that value. Corrected to the character-dependent formula $\langle f\rangle = A_*^2(64|b_e|^2 + 32|b_s|^2)/(\pi^2r^2)$; all $E/A$, $r_0$ and split numbers were recomputed. The edge-only numbers in the first run are withdrawn.
- **C2 — split counts.** The first split comparison used $|b|^2/2$ elementary copies. Corrected to BFS minimal root-decomposition counts $n_{\min} = 1,2,2,2,3,3$; verdicts for $|b|^2 = 8, 10, 12$ changed.
- **C3 — finite-difference threshold.** The $H$-application check first used $\delta = 10^{-6}$ and failed ($4.4\times10^{-6}$ vs a $10^{-8}$ threshold). A $\delta$-sweep showed pure $1/\delta$ roundoff scaling ($4.2\times10^{-9}$ at $10^{-3}$, $4.5\times10^{-8}$ at $10^{-4}$, $4.4\times10^{-6}$ at $10^{-6}$), driven by $\|\mu[\psi_0]\| \approx 11.6$ (dominated by the $k = 0$ mode $(r + q_0^4)\bar\psi$). The check was redone at $\delta = 10^{-3}$: PASS at $4.185\times10^{-9}$. No code was changed, only the validated step size.
- **C4 — task-2 moment normalisation.** `task2_report.md` describes its moments over the scaled roots, but $M_2 = 12|k|^2$ holds for the unscaled roots. Noted in §1; no task-2 number changes (they are unscaled-root values).

## 11. UNVERIFIED / ABSTAIN list

- Relaxed phonon dispersion and relaxation rates $\Gamma(q)$ of the standing wave (ABSTAIN, §6).
- Measured (vs estimated) dislocation core radii and core energies (UNVERIFIED — estimated by energy-density balance only).
- Dislocation–dislocation interaction energies and the jointly optimised (orientation + separation) split energetics (UNVERIFIED).
- Whether each $|b|^2$ shell is a single $W(F_4)$ orbit for $|b|^2 > 12$ (UNVERIFIED beyond 12; enumeration stopped there).
- External verification of this report by an authorised HLRE external agent (NOT RUN).
- Any claim about the physical (as opposed to model) stiffness of a real substrate: the substrate itself is a model postulate, and all grades above are grades of derivations *within* that model.

## 12. Heavy work still pending (costed, no spend authorised)

1. **Relaxed-field Bloch phonon spectrum** (resolves the §6 ABSTAIN). Step 1 (local, \$0): relax the one-mode seed under Model B on the $N = 16$ grid with the `d4model.py` Model B stepper (a few thousand steps, minutes, single local job well under $10$ min / $4$ GB). Step 2: Bloch eigensolve about the relaxed field at small $q$ (shift-invert on the symmetrised operator, A6-style, $83{,}520$ mean-zero degrees of freedom at $K = 8$). Cost to be measured on **one** $q$-value locally first; if local is too slow, proposed GCP cap **\$25** for the $q$-scan — PENDING, no spend authorised by this task. (Local prototype first; nothing starts on GCP without Brandon's explicit approval naming the cap.)
2. **Direct full-field dislocation simulation** (measures $r_0$ and core energy, lifts the grade-C items). Prototype locally: place one dislocation sheet in an $N = 16$ box, relax under Model B, extract $E/A$ vs $R$ (local, minutes, \$0). Production at $N = 32$ would be $\sim 16\times$ the cost; proposed GCP cap **\$50** — PENDING, no spend authorised.
3. **External verification** of this report through an authorised agent (Manus / Gemini 4 (Argon) / Academia Co-scientist) under the HLRE skill, audited locally claim-by-claim (2026-11-12 amendment). To be arranged by the parent agent; spend ceiling 300 USD/service/month applies; no run started here.

## 13. Deliverables

- This report: `REPORT.md`.
- `tables/task8_stiffness_coefficients.csv` — $f_2, f_3$ coefficients per strain state.
- `tables/task8_biaxial_f3.csv` — $f_3(t)$ for $\mathrm{diag}(\cos t, \sin t, 0, 0)$, 721 points.
- `tables/task8_burgers_classes.csv` — Burgers classes, $K$, $r_0$, $E/A$ at $R = 20$, $n_{\min}$, split costs, $R^*$ crossovers (edge and screw).
- `tables/task8_phonon_rates.csv` — phase-mode curvature, gradient/nonlinear split, trial-mode $\Gamma$ per $(q, \mathrm{pol})$.
- `tables/task8_summary.json` — all headline numbers in machine-readable form.
- `figures/task8_defect_energy_map.png` — $E/A$ vs $R$ per class, edge and screw.
- `figures/task8_stiffness.png` — (a) cubic-coefficient anisotropy, (b) phase-mode curvature vs $q^2$ with the exact $C_0 + 12q^2$ lines.
- `task8_stiffness.py`, `task8_phonon_rates.py`, `task8_figures.py` — reproducible scripts (pinned seed `20261114` where randomness is used; headline numbers are deterministic). Logs: `task8_stiffness.log`, `task8_phonon_rates.log`, `task8_figures.log`.

## 14. Assumption / parameter / choice ledgers

**Parameters (all from prior sources, verified in §1):** $r = -0.35$, $u = v = 1$, $q_0^2 = 8.0$, $\bar\psi = -0.18$, $r_{\mathrm{eff}} = 0.1072$, $\beta = 1.54$, $A_* = 0.077575296339281$, $F/V = -0.0076323$ (one-mode excess), $a_0 = 2\pi/q_0 \approx 2.221$.
**Assumptions:** (A1) the manuscript functional and the tuned 24-mode ansatz are taken as given (model premises, not re-derived); (A2) phase-only deformation with frozen per-mode amplitude (gives a variational upper bound — stated, not hidden); (A3) $D_4$ lattice $= \{x \in \mathbb{Z}^4 : \sum x_i \text{ even}\}$; Burgers classes $=$ $W(F_4)$ orbits; (A4) dislocation sheet is straight, isolated, and infinitely extended in its 2-plane; core radius by energy-density balance (estimate, grade C); (A5) split comparison uses infinitely separated sheets of pure character, interactions omitted.
**Choices:** reference radius $R = 20$ for the $E/A$ table (the $K \ln(R/r_0)$ form lets any $R$ be recomputed); displacement amplitude $U = 0.01$ and box $L = 4\pi$, $N = 32$ for the pseudospectral check; $200$ random strains/directions for the numeric checks (seed $20261114$); $|b|^2 \le 12$ enumeration bound; $q = 2$ excluded from the curvature fit for the diagnosed mode-collision cause.
**Model scope:** all results are derivations within the IRH v93.1 substrate model as stated; no claim is made about a physical substrate outside that model, and no grade above B is claimed without the (not yet run) external verification gate.
