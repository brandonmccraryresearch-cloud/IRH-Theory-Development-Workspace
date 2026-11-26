import VN7Indep
/-! v-n7 negative controls (must each FAIL; expect exactly 3 errors, one per theorem) -/
open Real
-- C1: the corner (π,π,π,π) as maximiser (true value 0)
theorem vctrl_pi4_is_32 : VN7.B2 ![π, π, π, π] = 32 := by
  simp [VN7.B2, VN7.pairTerm_eq]
  norm_num
-- C2: wrong attainment point (0,0,π/2,π/2) (true value 20)
theorem vctrl_halfpi_is_32 : N7.B ![0, 0, π / 2, π / 2] = 32 := by
  rw [VN7.B_eq_B2]
  simp [VN7.B2, VN7.pairTerm_eq]
  norm_num
-- C3: bound 31 with the verifier's own bound proof
theorem vctrl_le_31 (k : Fin 4 → ℝ) : VN7.B2 k ≤ 31 := by
  simp only [VN7.B2, VN7.pairTerm_eq]
  have e : (cos (k 0) + cos (k 1) + cos (k 2) + cos (k 3)) ^ 2
      = cos (k 0) ^ 2 + cos (k 1) ^ 2 + cos (k 2) ^ 2 + cos (k 3) ^ 2
        + 2 * (cos (k 0) * cos (k 1) + cos (k 0) * cos (k 2) + cos (k 0) * cos (k 3)
          + cos (k 1) * cos (k 2) + cos (k 1) * cos (k 3) + cos (k 2) * cos (k 3)) := by ring
  have hs := sq_nonneg (cos (k 0) + cos (k 1) + cos (k 2) + cos (k 3))
  have q0 := cos_sq_le_one (k 0)
  have q1 := cos_sq_le_one (k 1)
  have q2 := cos_sq_le_one (k 2)
  have q3 := cos_sq_le_one (k 3)
  linarith
