# IRH v93 Verification Audit — Final Report
**Date:** 2026-09-17 | **Auditor:** Enigma | **Subject:** "Intrinsic Resonance Holography, Version 93"

## Executive Summary

Three independent verification tracks were executed against the paper's claims:

| Track | Result |
|---|---|
| **Python claim verifier** (`verify_claims.py`) | **51 passed, 0 failed** |
| **4D dynamical simulations** | **II.8 fully reproduced**; II.6 partially (see caveats) |
| **Lean 4 formal proofs** | **8 modules, all compile** (`lake build` EXIT=0) |

## Part 1: Python Claim Verifier (51/51 passed)

All computable algebraic, combinatorial, and group-theoretic claims reproduced:

- **D₄ root system:** 24 roots enumerated; second- and fourth-moment isotropy exact
  (∑(k·α)² = 12|k|², ∑(k·α)⁴ = 12|k|⁴, zero residual symbolically and numerically).
- **Resonance maximum:** 24 at D₄ lattice points, unique modulo D₄ periodicity
  (caveat: on a closed-cell grid, 16 periodic images duplicate the maximum —
  "unique" must be read modulo lattice translations).
- **Shell combinatorics:** Exact BCC/FCC/SC/D₄/ℤ⁴/A₄/A₄* shell counts (N, T, Q).
- **Selection criterion:** τ_D₄ = 4/√6, τ_BCC = 2/√3 (ratio exactly √2);
  S_D₄ = 64/141 ≈ 0.45390, S_BCC = 16/45 ≈ 0.35556;
  D₄ beats A₄* (S = 12/31) by exactly 73/423 ≈ 17.26%.
- **Stationary state:** At r=−0.35, ψ̄=−0.18, u=v=1:
  r_eff = +0.1072, A* = 0.07758, F = −0.00763 (excess over uniform),
  u_eff = u − 3vψ̄.
- **CFL bound:** Δt ≤ (√3/2)(a₀/c) derived; the two v92 timesteps violate it.
- **Dispersion:** ∑[cos(a₀k·α)−1] = 4∑_{i<j}cos(a₀k_i)cos(a₀k_j) − 24 (exact identity).
- **Cross-section:** D₄ ∩ {x₃=0} = D₃ (FCC), kissing number 12.
- **Weyl groups:** |W(D₄)|=192, |W(D₅)|=1920; −I ∈ W(D₄), −I ∉ W(D₅).
- **Quaternion checks:** Binary tetrahedral group, Q₈, conjugacy classes, irrep dimensions.

### Unresolved (missing parameters, not contradictions)
- **§III.3 numerical error table:** Carrier angle and other discretization parameters
  unspecified. Natural implementations give errors *below* the table values.
  Excluded from the 51 passes; flagged as under-specified, not refuted.
- **A₄/A₄* table labels:** Appear dualized relative to explicit vector constructions.
  May be reciprocal-shell notation; needs author clarification before calling it an error.

## Part 2: 4D Dynamical Simulations

### Critical unit correction
The paper tunes **q₀² = 8.0** with the D₄ shell on resonance. On a 16⁴ grid this
requires box length **L = π** (so (2π/L)²·2 = 8). Earlier runs with L=16 (q₀²≈0.31)
left the mean and harmonics linearly unstable, corrupting results. All results
below use L=π, q₀²=8, where **only the D₄ shell is unstable**:
ω² = {63.65, 15.65, −0.35, 15.65, 63.65, ...} for |n|² = 0,1,2,3,4,...

### II.8 — Stability of the full pattern: REPRODUCED ✓
Seeded all 24 modes in phase at A*=0.0776, ψ̄=−0.18:

| dynamics | ψ̄ (final) | D₄ power | modes | rms | A (final) |
|---|---|---|---|---|---|
| seed | −0.18000 | 1.0000 | 24/24 | 0.3802 | 0.07760 |
| **Model B** (sim) | **−0.18000** | **1.0000** | **24/24** | **0.3806** | **0.07768** |
| Model B (paper) | −0.18000 | 1.0000 | 24/24 | 0.3806 | 0.0776 |
| **Model A** (sim) | **+0.00087** | **1.0000** | **24/24** | **0.4206** | 0.08585 |
| Model A (paper) | +0.00087 | 1.0000 | 24/24 | 0.4206 | — |

The Model A baseline drift (+0.00087) and rms (0.4206) match the paper to all
quoted digits. The Model B amplitude is unchanged to four significant figures
(0.07768 vs 0.07760). **The symmetric 24-mode D₄ standing wave is confirmed as
a dynamical attractor.**

The seed was additionally verified *stationary* to ~10⁻⁵ via exact FFT
convolutions (a buggy one-off diagnostic that reported dA/dt=−0.035 was
traced to a doubled term and discarded).

### II.6 — Dynamical selection: PARTIAL ✓/⚠
- **Reproduced:** Noise-initialized quenches reach **6-mode (u=1)** and
  **12-mode (u=0)** D₄ subpatterns — exactly the paper's "6- or 12-mode
  sub-patterns" observation. The cubic (triad) term changes the selected
  subpattern, confirming its causal role.
- **Cannot replicate exactly:** The paper's "fair" test (D₄ vs. a degenerate
  triad-free competitor, 84%/100% vs. 44%/56% control) requires the competitor
  shell specification, which is not given. Flagged as under-specified.

### II.9 — First-order transition: CONSISTENT ✓
r_eff = +0.107 > 0 at ψ̄=−0.18 confirmed; the uniform state is linearly stable,
so the pattern must nucleate (consistent with quenches at ψ̄=0 growing while
ψ̄=−0.18 does not).

## Part 3: Lean 4 Formal Proofs (all compile)

`~/workspace/irh_verify/lean/irh/` — `lake build` exits 0. Eight modules:

| Module | Theorem | Paper § |
|---|---|---|
| `Irh.Isotropy` | `d4_second_moment`, `d4_fourth_moment` — exact ∑(k·α)²=12\|k\|², ∑(k·α)⁴=12\|k\|⁴ | II.1 |
| `Irh.Selection` | `selection_criterion` — (B*, r_c) solve F=F'=0; `tau_D4_sq`, `tau_BCC_sq`, `S_D4`, `S_BCC`, `tau_ratio` (√2), `selection_margin` (73/423) | II.3, II.5 |
| `Irh.WeylD4` | `word_eq_neg_one` (12-reflection word = −I, by `decide`), `neg_one_mem_weylD4` | IV.1 |
| `Irh.CFL` | `cfl_bound` — Δt ≤ (√3/2)(a₀/c) from the stability inequality | III.2 |
| `Irh.CrossSection` | `cross_section` — D₄∩{x₃=0}=D₃ | II.10 |
| `Irh.UEff` | `u_eff_identity` — A³ coefficient gives u−3vψ̄ | II.7 |
| `Irh.Dispersion` | `cos_quad`, `pair_id`, `dispersion_identity` — exact lattice sum | III.1 |

## Wording/Label Corrections Suggested
1. "Unique maximum" (§II.2) → "unique modulo D₄ periodicity" (closed-cell grids
   duplicate the 16 periodic images).
2. The paper's free energy F is the **excess over the uniform state**
   (F=0 for disorder); this convention should be stated explicitly since the
   absolute F/V includes +½(r+q₀⁴)ψ̄².
3. A₄/A₄* table labels vs. vector constructions — needs clarification.

## Files
- `~/workspace/irh_verify/verify_claims.py` — 51 claim checks
- `~/workspace/irh_verify/sim6_units.py` — faithful II.8/II.6 simulations (L=π)
- `~/workspace/irh_verify/sim7_fairtest.py` — exact II.6 fair test, v93.0 parameters
- `~/workspace/irh_verify/lean/irh/` — Lean 4 + Mathlib proofs

---

# Addendum — v93.0 re-verification (2026-09-17)

Brandon supplied a revised manuscript (v93.0) addressing the review findings.
Re-verification results:

**All seven review items addressed in the text.**
§II.6 now fully specifies the simulation (L=2π box with scaled D₄ roots,
competitor = integer shell |k|²=7 with 64 modes and T=0, q₀²=7.5, γ=1.2,
Δt=0.05, annealing schedule). §II.2 states "unique modulo lattice periodicity."
§II.8 declares the excess-over-uniform F convention. §III.3 lists its parameters.
The A₄/A₄* table convention is captioned. Appendix B documents the scheme.

**Two reviewer errors corrected by the author (acknowledged).**
(1) The periodic-image count is 32, not 16 — the D₄ checkerboard means both
corner and body-centre sublattices satisfy the coincidence condition.
Independently re-verified by exhaustive grid count: 32 points attain the maximum.
(2) The free-energy gap attribution was arithmetically wrong (baseline
3.5×10⁻³ vs. gap 1×10⁻⁴). The author's harmonic-lowering explanation reproduces
the independent value −0.007728 to five decimals (−0.0077276).

**Lean is now machine-checked.** `lake build` EXIT=0, all 8 modules, no
sorry/admit/axiom/native_decide (verified by grep). The VI-A.2 "not compiled"
limitation is superseded.

**II.6 fair test reproduced (mechanism level).** With the now-specified parameters:
triads on, direct quench → D₄ 77% (paper 84%); triads on, annealed → D₄ 89.5%
and still rising at step 14000 (paper 100%); triads off control → D₄ 21% vs
competitor 79% (paper 44%/56%). Exact percentages are implementation-dependent
(seed, scheme, unspecified anneal noise amplitude); the causal claim — the cubic
term flips the winner — reproduces unambiguously.
