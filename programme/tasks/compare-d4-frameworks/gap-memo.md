# Gap memo: what would distinguish $D_{4}$ selection from conditional $D_{4}$ stability?

**Paper:** McCrary v93.1, DOI 10.5281/zenodo.22821689. **Companion:** `framework-matrix.md`, framework IDs F1–F10 and references S0–S9. This memo separates manuscript-reported results from this comparison's checks and proposed tests.

## Bottom line

Your paper makes an assessable advance over its retired static formulation: it specifies a finite-wave-number field functional and tests the effect of the cubic coupling. I independently recovered the $D_{4}$ and 3D BCC triad/quartet counts and their exact selection scores. The unresolved step is stronger: **unbiased emergence of the full, phase-locked 24-mode $D_{4}$ pattern, rather than concentration of power on its shell or persistence of a deliberately seeded state.**

The best comparison is therefore not a single winner table. F1/F3/F4 address onset ranking, F2 addresses field trajectories, F7/F8 address particle nucleation, and F9/F10 address geometric objectives. They can agree on $D_{4}$ while testing different propositions.

## 1. Highest-priority evidence gaps

### G1 — Shell capture is not full-state selection

**Evidence:** S0 §II.7 reports that annealing populated only six of 24 modes; §II.8 says earlier noise-initialized runs reached six- or twelve-mode sub-patterns. The full-state result starts with all 24 modes in phase at the predicted amplitude. §VI.1 reports phase locking of 0.26 against a maximum of one.

**Inference:** Even 100% $D_{4}$-shell power does not demonstrate full $D_{4}$ symmetry. Seeded stationarity supports existence and persistence; without perturbation and basin tests it does not establish a broad attracting basin. The different implementations' power fractions are not confidence intervals or replicate-level success rates.

**Small decisive test:** compare random fields, 6-/12-mode seeds, the symmetric 24-mode seed and perturbed full-state seeds under the same conserved dynamics. Record shell power, mode occupancy using a predeclared threshold, amplitude spread, triad phase locking and excess energy separately. Begin with 20 seeds per condition as a screening study; report binomial intervals for full-pattern success, and increase replication only if useful. Rotated or translated copies must count as the same state.

**Pass condition:** unbiased starts reproducibly reach the full state in a specified parameter region; or explicitly restrict the claim to conditional stability and shell selection.

### G2 — Onset-score competition and dynamical competition are not matched

**Evidence:** F1 ranks $D_{4}$ against $A_{4}$*, $\mathbb{Z}^{4}$ and $A_{4}$. The equal-linear-penalty simulation in §II.6 compares $D_{4}$ with the integer shell |k|${}^{2}=7$, whose triad count is zero—not with the nearest nonzero-score rival $A_{4}$*. The torus calculation in §II.2 already assumes $\Lambda\congD_{4}$ and therefore tests self-resonance, not unbiased lattice selection.

**Inference:** The cubic-off intervention is useful evidence about this shell competition, but does not establish a dynamical win over the strongest analytic rival. Periodic integer wavevectors also constrain which competitors and orientations are representable.

**Small decisive test:** first compare $D_{4}$ and $A_{4}$* amplitude equations at the same mean, shell penalty and normalization. Then design commensurate domains or document approximation errors before comparing them in a field solver. Include within-shell sub-patterns and unequal mode amplitudes.

**Pass condition:** the $D_{4}$ advantage survives the same competitor set in analysis and dynamics, with finite-box restrictions disclosed.

### G3 — The stable band is conditional, not a probability of emergence

**Evidence:** §II.7 reports a full-state band covering 11.85% of its scanned plane, conditional on $q_{0}$ tuning. At $r=-0.35$ and $\bar{\psi}=-0.18$, $q_{0}^{2}=8$ supports the ordered branch, while $q_{0}^{2}=7.5$ adds 0.25 to the shell quadratic coefficient and removes that branch. The sixth-order scan narrows the reported band to 8.47% at $w_{6}=0.2$. §IX.5 leaves the initial mean unexplained.

**Inference:** 11.85% is an area fraction under a chosen scan domain and grid, not a cosmological probability or invariant measure of tuning. The parameter-free ranking in u,v does not make the field model or the full phase diagram parameter-free.

**Small decisive test:** scan detuning $\times$ mean $\times$ quench with and without sixth-order terms. Release scan bounds, grid spacing and candidate list. Plot coexistence, linear instability and actual dynamical success as separate boundaries. Check whether wavelength adapts when box size changes.

**Pass condition:** provide tolerances and connected stability regions rather than a single area percentage; supply a physical mechanism for fixing the mean and resonant scale before claiming unconditional substrate selection.

### G4 — Nucleation remains the access barrier

**Evidence:** §II.9 gives positive effective quadratic coefficient $\approx0.107$ at $\bar{\psi}=-0.18$, so the uniform state is linearly stable. The paper expressly requires nucleation. F8 shows why local crystalline compatibility need not imply facile nucleation; F7 shows that changing attractive interactions changes accessibility even with similar endpoint geometry.

**Small decisive test:** seed droplets with varying radius/amplitude and bracket growth versus decay; estimate a critical droplet and barrier. Compare thermal/stochastic nucleation with annealing through a linearly unstable region. State the noise law and whether it has a fluctuation–dissipation interpretation.

**Pass condition:** a demonstrated path from admissible initial conditions to $D_{4}$, with waiting-time distributions rather than persistence alone.

### G5 — Scientific code and proof artifacts are not in the inspected deposit

**Evidence:** the Zenodo ZIP contains manuscript PDF/TeX/Markdown, references, ten PNGs and `md2tex.py`. It contains no simulation Python, Lean modules, Lake configuration, raw field arrays or seed manifest. The separate Google Drive “Independent Verification Data” link returned a sign-in page to the access method used here.

**Inference:** this is an artifact-access gap, not evidence that the reported computations or Lean build are false. The paper's Lean and independent-reproduction claims remain author-reported in this comparison. References to Lean and Mathlib identify software publications, not the actual project snapshot.

**Small decisive fix:** deposit one versioned archive with the shell counter, exact update equations, seed list, conserved/nonconserved timestep choices, nonlinear dealiasing, scan grids and raw outputs. Add the eight Lean modules, pinned toolchain/Mathlib revision, build command and logs. Map each claim to its script/theorem and expected output.

**Pass condition:** a fresh environment reproduces the exact counts, representative energy and stated proof build. Check linear-implicit versus nonlinear timestep stability separately; do not infer unconditional nonlinear stability from treating the linear operator implicitly.

## 2. Source corrections and framing changes

### Correct the Hoy system-size attribution

S0 §II.5 places the N=648 commensurability example beside Hoy's result. Hoy's Methods specifies **$N=5\times10^{5}$**, and the Results uses large boxes to exclude the earlier finite-size concern. His footnote about 648 particles refers to the older Skoge et al. study. This is a citation-context conflation, not a failure of Hoy's corroboration.

**Suggested replacement:** “Hoy observed $D_{4}$ crystallization in 500,000-particle four-dimensional Lennard–Jones systems, large enough to address the periodic-boundary concern raised for earlier 648-particle simulations. The shared $D_{4}$ endpoint is consistent with our prediction, although the interaction model and selection mechanism differ.” [S6, Methods and Results]

### Distinguish shared theory from independent implementation

F4 and IRH share the Landau expansion, finite-q shell and cubic closed-triangle mechanism. S2 explicitly uses equal-magnitude amplitudes and triangle counts. The extra quartet normalization and explicit field trajectories are the relevant distinctions; calling the analytic routes independent without specifying the level of independence overstates the separation.

**Suggested framing:** “Our analysis extends the higher-dimensional Landau selection comparison by retaining candidate-dependent quartic counts in the coexistence score and testing cubic-mediated shell competition dynamically.” This is a scoped description, not a priority claim; broader novelty would need a wider search.

### Separate geometric problems

F9 proves uniqueness of the optimal **kissing configuration**, not dynamical selection or unrestricted four-dimensional packing optimality. F10's non-universal-optimality theorem concerns **24 points on $S^{3}$**. S0 §II.11's Gaussian $\beta$ scan needs its configuration space and objective spelled out before treating it as a reproduction of that theorem. If it optimized infinite lattices, it is a different problem.

### Keep “excluded” tied to the tested route

Zero triad count excludes a shell from the cubic first-order onset mechanism in the stated ansatz. It does not exclude quartic-driven ordering at negative r, multiscale coupling or another functional. Likewise, the highest onset threshold need not identify the stable phase far from onset; F5 supplies a concrete warning.

## 3. Boundaries of the substrate interpretation

These are downstream of the selection benchmark and should not be mixed into its score:

- **Dimension:** marginality of the isolated $\int(\nabla^{2}\psi)^{2}$ term at d=4 is a scaling fact, not a demonstrated comparison of stable solutions of the full $q_{0}$-dependent functional across dimensions. The base is already $\mathbb{R}^{4}$ in the primary model; S0 §IX.2 acknowledges unresolved interpretations.
- **Physical scale:** $a_{0}=2\pi/q_{0}$ relates wavelength to the model's resonant input. A microscopic determination of $q_{0}$ and the crystal-spacing convention is still needed before calling an absolute length scale predicted.
- **Gauge extension:** the 24-cell/2T/McKay association identifies an algebraic relationship. It does not, by itself, construct local $E_{6}$ gauge degrees of freedom, their action or their coupling to the original scalar. Require a dynamical construction rather than count this as selection evidence.
- **Matter and gravity:** generation count, Lorentzian signature, Einstein equations and Higgs breaking remain outside the validated selection test, consistent with the paper's own open-problem register. Topological charge classification alone also does not establish energetically stable, finite-energy soliton solutions.

## Recommended order of work

1. **Close the access gap** and fix the Hoy attribution: quick, directly improves checkability.
2. **Run the full-pattern basin and matched-rival tests** (G1–G2): most likely to change the strength of the central selection claim.
3. **Map detuning and nucleation** (G3–G4): turns conditional stability into a quantified accessibility statement.

**What this memo does not claim:** no new field simulation or Lean build was run; no independent audit of the unnamed verification party was possible. Exact shell counting and deposit inspection were performed and documented in `verification-audit.md`. This is a focused evidence map, not an exhaustive review of all higher-dimensional crystallization models.
