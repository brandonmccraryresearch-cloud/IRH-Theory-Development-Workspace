import N7Bracket
/-! w-n7 negative control 2 (must FAIL): wrong root set (root ![1,0,1,0] dropped, 23 roots),
  claimed attainment 32 at (0,0,π,π) with the production attainment proof (true value 30) -/
open Real
noncomputable def B23 (k : Fin 4 → ℝ) : ℝ :=
  ((N7.roots.eraseIdx 4).map (fun α => 1 - Real.cos (N7.dot k α))).sum
theorem N7ctrl_roots23_attained : B23 ![0, 0, π, π] = 32 := by
  simp only [B23, N7.roots, N7.dot, List.eraseIdx, List.map_cons, List.map_nil, List.sum_cons,
    List.sum_nil, Fin.sum_univ_four, Matrix.cons_val_zero, Matrix.cons_val_one, Matrix.cons_val_two,
    Matrix.cons_val_three, Matrix.head_cons, Matrix.tail_cons]
  push_cast
  simp
  norm_num
