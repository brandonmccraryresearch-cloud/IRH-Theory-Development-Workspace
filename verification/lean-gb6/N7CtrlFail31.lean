import N7Bracket
/-! w-n7 negative control 1 (must FAIL): bound 31 with the production proof script -/
open Real
theorem N7ctrl_le_31 : ∀ k : Fin 4 → ℝ, N7.B k ≤ 31 := by
  intro k
  rw [N7.B_closed]
  nlinarith [sq_nonneg (cos (k 0) + cos (k 1) + cos (k 2) + cos (k 3)),
    cos_sq_le_one (k 0), cos_sq_le_one (k 1), cos_sq_le_one (k 2), cos_sq_le_one (k 3)]
