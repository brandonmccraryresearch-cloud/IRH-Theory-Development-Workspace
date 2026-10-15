# Established Core — What New Work May Build On

Compressed from Part VIII.1 of v93.1. Each item was derived symbolically,
validated against a known limiting case, confirmed by simulation, excluded by
theorem, independently reproduced, or machine-checked in Lean 4 (eight modules,
`lake build` exit 0). New work may cite these without re-derivation; the paper
section is given for the full argument.

## Geometry and selection

- D₄ isotropic through 4th order (exact; spherical 5-design) — §II.1.
- D₄ isodual; unique interference maximum (modulo lattice periodicity; 32
  periodic images on the $16^4$ grid — proved by exhaustive enumeration in
  `verification/reconcile_resonance_count.py`, exit 0) — §II.2.
- Selection criterion $S = \tau^2/q_4$ parameter-free in $u,v$; BCC recovered
  in 3D (Alexander–McTague) — §II.3–II.4.
- D₄ selected in 4D: $S = 64/141 \approx 0.454$, exact rationals, 17.3% margin
  over A₄*; ℤ⁴ and A₄ structurally excluded ($T=0$) — §II.5.
- Independent corroboration: 4D Lennard-Jones crystallization to D₄ (Hoy [40]).
- Dynamical shell selection from noise; triad term causally responsible
  (77.1% vs 21.1% control; 89.5% annealed, independent reproduction) — §II.6.
- $u_{\mathrm{eff}} = u - 3v\bar\psi$; $\bar\psi$ is the control parameter —
  §II.7.
- D₄ phase band: 11.85% of scanned plane **(conditional on $q_0$ tuned onto
  shell — always cite the qualification)** — §II.7.
- Full 24-mode state is a genuine dynamical attractor ($F/V=-0.0077276$ relaxed;
  one-mode ansatz accurate to 1.25%) — §II.8.
- First-order transition character ($r_{\mathrm{eff}}=+0.107$ at
  $\bar\psi=-0.18$; nucleation required) — §II.9.
- $D_4 \cap \{x_4=0\} = \mathrm{FCC}$ — §II.10.
- D₄ not universally optimal (narrow window loss ≤0.007%) — §II.11.

## Dynamics

- $a_0 = 2\pi/q_0$ derived, not postulated; site-field action retired — §I.3.
- Conserved (Model B) dynamics required; $\bar\psi$ preserved to
  $8.3\times10^{-17}$ — §I.3.
- Exact dispersion, Hamiltonian positivity, CFL bound
  $\Delta t \le \frac{\sqrt{3}}{2}\,a_0/c$ (worst-case spatial sum exactly 32) —
  §III.1–III.2.
- Corrected envelope equation + quantified validity ($<1\%$ for
  $a_0|\mathbf{k}| \lesssim 0.3$) — §III.3.
- $d=4$ marginality of the Swift–Hohenberg term (new structural argument for
  four-dimensionality) — §III.4.

## Algebra

- 24-cell vertices = binary tetrahedral group $2T \subset SU(2)$ (exhaustive) —
  §IV.3.
- $2T/Q_8 \cong \mathbb{Z}_3$ (8+8+8 coset decomposition) — §IV.3.
- McKay: $2T \leftrightarrow$ affine E₆ (unique; irreps {1,1,1,2,2,2,3}) —
  §IV.3.
- E₆ chiral ($w_0 \neq -1$); complex **27**; E₆ ⊃ SO(10) ⊃ SU(5) ⊃ SM chain
  non-increasing in rank — §IV.3–IV.4.
- **Gauge algebra of IRH is E₆**, read off the substrate — §IV.4.

## Matter and defects

- Order-parameter space $M = T^4 \times S^3$: dislocation sheets (Burgers
  vectors in D₄), no line defects, integer-charged point solitons — §V.1.
- Point group $W(F_4)$, order 1152.

## Verification

- Independent re-derivation of load-bearing claims — §VI-A.1.
- Lean 4 formalization, machine-checked end to end (no sorry/admit/axiom) —
  §VI-A.2.
- **Executed record:** `verification/` — `verify_claims.py` (51/51
  checks passed: root enumeration, moment isotropy, resonance maximum, shell
  combinatorics, selection exact rationals, stationary state, CFL bound,
  dispersion identity, cross-section, Weyl groups, quaternion checks);
  `sim6_units.py` (II.8 seeded-state reproduction, Model B holds / Model A
  drifts, matching the paper to all quoted digits); `sim7_fairtest.py` (II.6
  fair test: cubic term flips the winner, 77.1% vs 21.1% control, 89.5%
  annealed); `lean/` (8 modules, `lake build` exit 0); `FINAL_AUDIT.md` (full
  report + v93.0 re-verification addendum). See `verification/README.md`.
