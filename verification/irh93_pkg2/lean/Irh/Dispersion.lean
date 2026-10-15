import Mathlib.Analysis.SpecialFunctions.Trigonometric.Basic
import Mathlib.Tactic

/-! # Exact lattice dispersion identity (IRH v93, Sec. III.1)

  ∑_{α ∈ Φ_D4} [cos(a₀ k·α) − 1] = 4 ∑_{i<j} cos(a₀k_i) cos(a₀k_j) − 24.

The 24 roots partition into 6 sign-quadruples ±e_i±e_j; on each,
cos(x+y)+cos(x−y)+cos(−x+y)+cos(−x−y) = 4 cos x cos y.
-/

theorem cos_quad (x y : ℝ) :
    Real.cos (x + y) + Real.cos (x - y) + Real.cos (-x + y) + Real.cos (-x - y)
      = 4 * Real.cos x * Real.cos y := by
  simp only [Real.cos_add, Real.cos_sub, Real.cos_neg, Real.sin_neg]
  ring

theorem pair_id (a0 x y : ℝ) :
    Real.cos (a0 * (x + y)) + Real.cos (a0 * (x - y))
      + Real.cos (a0 * (-x + y)) + Real.cos (a0 * (-x - y))
      = 4 * Real.cos (a0 * x) * Real.cos (a0 * y) := by
  have h := cos_quad (a0 * x) (a0 * y)
  have e1 : a0 * x + a0 * y = a0 * (x + y) := by ring
  have e2 : a0 * x - a0 * y = a0 * (x - y) := by ring
  have e3 : -(a0 * x) + a0 * y = a0 * (-x + y) := by ring
  have e4 : -(a0 * x) - a0 * y = a0 * (-x - y) := by ring
  rw [e1, e2, e3, e4] at h
  exact h

/-- The closed-form dispersion sum, with the 24 roots grouped by index pair. -/
theorem dispersion_identity (a0 : ℝ) (k : Fin 4 → ℝ) :
    ((Real.cos (a0 * (k 0 + k 1)) + Real.cos (a0 * (k 0 - k 1))
        + Real.cos (a0 * (-k 0 + k 1)) + Real.cos (a0 * (-k 0 - k 1)) - 4)
      + (Real.cos (a0 * (k 0 + k 2)) + Real.cos (a0 * (k 0 - k 2))
        + Real.cos (a0 * (-k 0 + k 2)) + Real.cos (a0 * (-k 0 - k 2)) - 4)
      + (Real.cos (a0 * (k 0 + k 3)) + Real.cos (a0 * (k 0 - k 3))
        + Real.cos (a0 * (-k 0 + k 3)) + Real.cos (a0 * (-k 0 - k 3)) - 4)
      + (Real.cos (a0 * (k 1 + k 2)) + Real.cos (a0 * (k 1 - k 2))
        + Real.cos (a0 * (-k 1 + k 2)) + Real.cos (a0 * (-k 1 - k 2)) - 4)
      + (Real.cos (a0 * (k 1 + k 3)) + Real.cos (a0 * (k 1 - k 3))
        + Real.cos (a0 * (-k 1 + k 3)) + Real.cos (a0 * (-k 1 - k 3)) - 4)
      + (Real.cos (a0 * (k 2 + k 3)) + Real.cos (a0 * (k 2 - k 3))
        + Real.cos (a0 * (-k 2 + k 3)) + Real.cos (a0 * (-k 2 - k 3)) - 4))
      = 4 * (Real.cos (a0 * k 0) * Real.cos (a0 * k 1)
        + Real.cos (a0 * k 0) * Real.cos (a0 * k 2)
        + Real.cos (a0 * k 0) * Real.cos (a0 * k 3)
        + Real.cos (a0 * k 1) * Real.cos (a0 * k 2)
        + Real.cos (a0 * k 1) * Real.cos (a0 * k 3)
        + Real.cos (a0 * k 2) * Real.cos (a0 * k 3)) - 24 := by
  have p01 := pair_id a0 (k 0) (k 1)
  have p02 := pair_id a0 (k 0) (k 2)
  have p03 := pair_id a0 (k 0) (k 3)
  have p12 := pair_id a0 (k 1) (k 2)
  have p13 := pair_id a0 (k 1) (k 3)
  have p23 := pair_id a0 (k 2) (k 3)
  linarith
