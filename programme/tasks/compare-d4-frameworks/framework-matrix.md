# $D_{4}$ selection frameworks: cross-referenced evidence matrix

**Scope:** a focused comparison of weak-crystallization theory, pattern-forming field dynamics, particle crystallization, and geometric optimization. These are the families actually implicated by McCrary v93.1—not competing end-to-end theories of fundamental physics. Prepared 9 November 2026.

**Main conclusion:** IRH's selection argument belongs to the Alexander–McTague/Landau density-wave family, with a Swift–Hohenberg spectral operator and explicit dynamical tests. Particle simulations support the accessibility of $D_{4}$ under particular interactions; geometric theorems constrain its structure. Neither independently validates the complete interference-substrate mechanism.

## How to read the evidence

- **M:** reported in the supplied manuscript, with page and section; not automatically independently verified.
- **F:** relevant external full text read in this comparison.
- **A:** external abstract or institutional summary checked; numerical implementation not inspected.
- **R:** small exact calculation independently executed here; see `verification-audit.md`.
- **U:** artifact or assertion not verified in this comparison. “Not inspected” does not mean “does not exist.”

All comparator references below were first identified in the supplied manuscript (*from your workspace*); the indicated external checks supplement that source. No experimental or synthetic dataset was substituted. No common accuracy score is appropriate: the objectives and units differ.

## Evaluation criteria inferred from the paper

| ID | Criterion | Evidence needed |
|---|---|---|
| C1 | Select rather than prescribe $D_{4}$ | Declared competitor class, common normalization, no $D_{4}$ boundary imposed as the selection test |
| C2 | Rank onset correctly | Closed triads and quartets; coexistence threshold; 3D BCC limiting-case check |
| C3 | Produce the full symmetry | Occupancy and amplitudes of all 24 modes, phase locking, exclusion of 6-/12-mode sub-patterns |
| C4 | Demonstrate dynamical accessibility | Random-start success probability separately from seeded persistence; nucleation barriers and times |
| C5 | Delimit stability | Mean field, detuning, higher-order terms, volume, boundary geometry, timestep and resolution |
| C6 | Make reproduction possible | Executable scientific code, seeds, update rule, dealiasing, outputs and proof environment |
| C7 | Keep physical interpretation separate | No inference of spacetime dimension, gauge fields or gravity solely from geometric or crystallization results |

## Matrix A — mechanisms, assumptions and designs

| ID / family / principal papers | Assumptions and architecture | Data or computational objects | What it actually tests |
|---|---|---|---|
| **F1 — IRH equal-shell selection** [S0, §§II.3–5, pp.6–7] | Real scalar; single resonant reciprocal shell; equal amplitudes; local cubic/quartic functional. Normalize $B=A\sqrt{N}$, $\tau=T/N$^(3/2), $q_{4}=Q/N^{2}$. Coexistence gives $r_{c}=(2u^{2}/9v)\tau^{2}/q_{4}$. | Enumerated reciprocal stars of $D_{4}$, $A_{4}$*, $\mathbb{Z}^{4}$, $A_{4}$; 3D BCC/FCC/SC controls. | C1–2: onset ranking within this ansatz and candidate set, not global selection among all fields. |
| **F2 — IRH interference dynamics** [S0, §§I.2, II.6–9, VI.1] | Damped-wave equation driven by Swift–Hohenberg free energy; separate conserved Model B tests. Cubic on/off intervention; direct quench and annealing; seeded full-state relaxation. | $16^{4}$ periodic field; $L=2\pi$; $D_{4}$ star |k|${}^{2}=8$ versus triad-free |k|${}^{2}=7$ shell; both penalized equally at $q_{0}^{2}=7.5$. Full-state test instead tunes $q_{0}$ onto the $D_{4}$ shell and sets mean $\bar{\psi}=-0.18$. | C3–5: shell capture, within-shell symmetry and persistence are distinct endpoints. Damped-wave and conserved-gradient-flow trajectories must not be conflated. |
| **F3 — Alexander–McTague weak crystallization** [S1] | Landau expansion about a uniform liquid; nonzero critical wave number; cubic invariants from closed triangles; weak ordering. | Density-wave geometry, not measured training data. | C2: near-transition preference for BCC in 3D; a limiting-case baseline for IRH. |
| **F4 — higher-dimensional Landau selection** [S2, §§2–4] | Scalar order parameter; isotropic nonzero-q instability; equal-amplitude shell; cubic triangle counting over regular convex polytopes in flat noncompact dimensions. Quartic term stabilizes amplitude. | Analytic edge/triangle counts; explicit 4D special-case comparison. | C1–2: direct prior art for a 4D cross-polytope edge-star preference. Restricted candidate class, no time integration. |
| **F5 — density-functional counterbaseline** [S3] | Reconsider liquid–solid spinodal with density-functional theory; include additional accessible density-wave structures and nonperturbative free-energy behavior. | Analytic argument and explicit “Onsager solid” toy-model calculations. | C2/5: whether near-spinodal BCC preference determines the ultimately stable phase. |
| **F6 — Swift–Hohenberg / Model A–B ingredients** [S4–S5; implementation in S0] | Finite-wave-number pattern formation; nonconserved versus conserved order-parameter dynamics. These supply operators and dynamical classifications, not independent $D_{4}$ selectors. | Scalar field modes; analytical dynamical classifications. | C4–5: spectral selection and conservation constraints; $D_{4}$ requires added nonlinear geometry and appropriate conditions. |
| **F7 — Lennard–Jones versus WCA crystallization** [S6, §§II–III] | 4D Newtonian particles; shifted/truncated pair potential; attractive LJ versus repulsive WCA control; periodic hypercubic boxes. LJ NPT at zero pressure; WCA NVT at matched pre-nucleation density/temperature. | **500,000 particles**, dt=$\tau/125$; LJ cutoff $2.5\sigma$, WCA cutoff 2^$(1/6)\sigma$; energy, density, g(r), bond-order correlations. | C3–5: physically simulated nucleation into $D_{4}$ under specific interactions; not the scalar field's cubic-term mechanism. |
| **F8 — hard-sphere frustration / nucleation** [S7] | 4D excluded-volume particles; distinguish local dense-cluster compatibility from actual liquid polytetrahedral structure and nucleation cost. | Computational hard-sphere freezing study, compared with 3D behavior. | C4–5: why geometrically compatible local clusters do not guarantee easy crystallization. |
| **F9 — spherical-code / kissing optimization** [S8] | 24 unit vectors on $S^{3}$; minimum angle $\pi/3$; second-level Lasserre semidefinite hierarchy and exact feasibility certificate. | Rational SDP certificate; invariant polynomial matrices; rigorous positivity checks. | C1/C7: unique optimal kissing configuration up to isometry, not a dynamical attractor or universal energy minimum. |
| **F10 — potential-dependent optimality counterexample** [S9] | Pair-energy optimization for points constrained to $S^{3}$; vary absolutely monotonic inner-product potentials (equivalently the corresponding completely monotonic squared-distance formulation). | Mathematical construction and numerical exploration of deformed 24-point designs. | C5/C7: whether $D_{4}$ minimizes every potential in that class. This is a spherical-code problem, not automatically an infinite-lattice energy problem. |

## Matrix B — findings, implementation status and gaps

| ID | Reported findings / metrics | Code and access status | Gaps / discriminating condition |
|---|---|---|---|
| **F1** | $D_{4} S=64/141=0.453901$; $A_{4}* 12/31=0.387097$; $\mathbb{Z}^{4}$ and $A_{4}$ zero. Relative $D_{4}$ advantage 73/423=17.26%. BCC S=16/45. **M+R** for $D_{4}$/BCC counts and score; $A_{4}$* score checked against manuscript page image. | SymPy/enumeration reported. Scientific implementation absent from inspected Zenodo archive; see audit. | Non-equal amplitudes, additional shells, non-Bravais and quasiperiodic candidates. Zero cubic score means exclusion from this cubic first-order route, not impossibility of ordering. |
| **F2** | Author: $D_{4}$ shell power 84% direct, 100% annealed; cubic-off 44%. Manuscript-reported independent implementation: 77.1%, 89.5%, cubic-off 21.1%. Earlier noise starts occupy only 6/12 modes. Seeded full state relaxes to excess $F/V=-0.0077276$. Phase-locking parameter 0.26/1. **M** | §II.\$6: r=-0.35$, u=v=1, $$\gamma=1.2$$, dt=0.05, 6,000 steps; annealing 14,000 steps from $r=-0.05\$ to $-0.45$. Conserved scheme details not executable from inspected package. **U** for rerunning simulations/Lean. | Shell power alone cannot establish 24-mode symmetry. Mean-field band and $q_{0}$ tuning required. Need perturbed full-state basin tests, unbiased nucleation statistics, resolution/volume/box-shape convergence. |
| **F3** | Near-melting BCC preference; recovered by F1. **M**; foundational source not independently full-text audited here. | Analytic baseline; no code repository inspected. | Valid near transition; not a general ground-state or kinetic theorem. |
| **F4** | Cross-polytope wins the considered regular-polytope comparison, including the 4D 16-cell. Edge wavevectors have form $\pme_{i}\pme_{j}$: the 24-vector $D_{4}$ star at d=4. **F** | Equations and combinatorial construction available in full text; executable code not inspected. | Shares the Landau/cubic-invariant foundation with IRH. Separate exact quartet ranking and kinetic evidence from claims of mechanism-level independence. Compactness, irregular/nonconvex structures explicitly left open. |
| **F5** | FCC and other structures accessible at spinodal; unstable BCC branch still has lowest near-spinodal free energy, but toy-model stable phase can be FCC. **A** | Institutional abstract checked; full calculations/code not audited. | Direct caution against equating “orders first” with “globally stable at arbitrary quench.” No 4D quantitative comparison established here. |
| **F6** | IRH reports conserved mean preservation to $8.3\times10^{-17}$ versus drift under Model A; generic ingredient papers do not report IRH'$s D_{4}$ selection metrics. **M** | Foundational references from manuscript; implementations not inspected. | Derive one primary evolution law or explicitly compare them. Linear implicitness alone does not establish unconditional stability of explicit nonlinear terms. |
| **F7** | LJ crystallizes around 0.59<T<0.63 within ~$2\times10^{4}\tau$; matched WCA does not within $2.5\times10^{5}\tau$. $D_{4}$ identified using coordination tending to 24; representative $Z\approx23.81$ and 99.2% high-bond-order pairs after crystallization. **F** | Paper names **hdMD**, citing Hoy & Interiano-Alberto (2022). Code/input decks and trajectories not inspected. | Same $D_{4}$ endpoint supports compatibility, not IRH causality. Attractions matter. Source distinguishes its large systems from older 648-particle finite-size concerns. |
| **F8** | 4D nucleation less facile than 3D despite local dense-cluster/crystal compatibility; polytetrahedral frustration implicated. **A** | Abstract checked; full protocol and scientific code not inspected. | Local $D_{4}$ geometry insufficient to predict kinetic reachability; interaction-dependent comparison with F7 required. |
| **F9** | Exact kissing bound 24; unique optimal configuration up to isometry. Degree parameters $d_{1}=14$, $d_{2}=\delta=16$; reported numerical solve ~2 weeks on 8 cores/128 GB, followed by exact rounding and verification. **F** | Julia/Nemo scripts and data explicitly linked by paper; link target and code execution not audited. | Objective is angular separation; no time scale, nucleation or field equation. Does not prove densest unrestricted 4D packing or universal pair-energy optimality. |
| **F10** | $D_{4}$ is **not universally optimal** as a 24-point spherical code. **A** | arXiv abstract checked; counterexample implementation not inspected. | Must specify objective and configuration space. IRH's Gaussian $\beta$-window scan remains manuscript-reported and does not by itself transfer this spherical-code theorem to infinite lattices. |

## Source register

**S0.** Brandon D. McCrary (2026), *Dynamical Selection of $a D_{4}$ Substrate from Interference Dynamics*, v93.1. [DOI](https://doi.org/10.5281/zenodo.22821689). Supplied PDF read in full; selected numerical tables visually checked. PDF dated September 17; Zenodo publication September 18. Preprint, CC BY 4.0. Zenodo metadata and source ZIP inspected. Manuscript source for all M entries.

**S1.** S. Alexander & J. McTague (1978), *Should All Crystals Be bcc? Landau Theory of Solidification and Crystal Nucleation*. [DOI](https://doi.org/10.1103/PhysRevLett.41.702). S0 ref.1; manuscript-grounded baseline only in this rapid comparison.

**S2.** S. Elitzur, B. Karni & E. Rabinovici (2011), *A comment on BCC crystalization in higher dimensions*. [DOI](https://doi.org/10.1142/S0217984911026358); [full text checked](https://arxiv.org/html/1101.1631v1). S0 ref.45. The extra arXiv identifier math/0607446 printed in S0 ref.45 was not verified here; use 1101.1631.

**S3.** B. Groh & B. Mulder (1999), *Why all crystals need not be bcc: Symmetry breaking at the liquid–solid transition revisited*. [DOI](https://doi.org/10.1103/PhysRevE.59.5613); [institutional summary checked](https://ir.amolf.nl/pub/5083). S0 ref.44.

**S4.** J. Swift & P. C. Hohenberg (1977), *Hydrodynamic Fluctuations at the Convective Instability*. [DOI](https://doi.org/10.1103/PhysRevA.15.319). S0 ref.2; manuscript-grounded ingredient, not full-text audited here.

**S5.** P. C. Hohenberg & B. I. Halperin (1977), *Theory of Dynamic Critical Phenomena*. [DOI](https://doi.org/10.1103/RevModPhys.49.435). S0 ref.4; manuscript-grounded ingredient, not full-text audited here.

**S6.** R. S. Hoy (2024 journal paper; 2023 preprint), *Homogeneous crystallization in four-dimensional Lennard-Jones liquids*. [DOI](https://doi.org/10.1103/PhysRevE.109.044604); [full text checked](https://arxiv.org/html/2311.03465v1). S0 ref.40. Implementation reference: R. S. Hoy & K. A. Interiano-Alberto (2022), *Efficient d-dimensional molecular dynamics simulations for studies of the glass-jamming transition*, Physical Review E 105, 055305, as cited in S6.

**S7.** J. A. van Meel, D. Frenkel & P. Charbonneau (2009), *Geometrical frustration: A study of four-dimensional hard spheres*. [DOI](https://doi.org/10.1103/PhysRevE.79.030201); [abstract checked](https://arxiv.org/abs/0809.1775). S0 ref.39.

**S8.** D. de Laat, N. Leijenhorst & W. de Muinck Keizer (2024), *Optimality and uniqueness of the $D_{4}$ root system*. [Full text checked](https://arxiv.org/html/2404.18794v2). S0 ref.14. §5.1 supplies exact-certificate and implementation details.

**S9.** H. Cohn, J. H. Conway, N. D. Elkies & A. Kumar (2007), *The $D_{4}$ Root System Is Not Universally Optimal*. [DOI](https://doi.org/10.1080/10586458.2007.10129008); [abstract checked](https://arxiv.org/abs/math/0607447). S0 ref.13.

**Scope limits:** targeted bibliography-led evidence map, not a systematic review or citation census. No simulation trajectory, particle dataset or Lean build was reproduced. See `gap-memo.md` for prioritized tests and `verification-audit.md` for what was actually checked.
