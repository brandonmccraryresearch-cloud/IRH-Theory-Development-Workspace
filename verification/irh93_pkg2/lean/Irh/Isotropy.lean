import Mathlib.Algebra.BigOperators.Fin
import Mathlib.LinearAlgebra.Matrix.Notation
import Mathlib.Tactic

/-! # D4 isotropy through fourth order (IRH v93, Sec. II.1)

The 24 roots of D4 are ±e_i ± e_j. We verify symbolically:
  ∑_α (k·α)² = 12 |k|²   and   ∑_α (k·α)⁴ = 12 |k|⁴
for a general wavevector k : Fin 4 → ℝ, with zero residual.
-/

/-- The 24 roots of D4, grouped by index pair. -/
def d4roots : List (Fin 4 → ℝ) :=
  [ ![1,-1,0,0], ![1,1,0,0], ![-1,1,0,0], ![-1,-1,0,0],
    ![1,0,-1,0], ![1,0,1,0], ![-1,0,1,0], ![-1,0,-1,0],
    ![1,0,0,-1], ![1,0,0,1], ![-1,0,0,1], ![-1,0,0,-1],
    ![0,1,-1,0], ![0,1,1,0], ![0,-1,1,0], ![0,-1,-1,0],
    ![0,1,0,-1], ![0,1,0,1], ![0,-1,0,1], ![0,-1,0,-1],
    ![0,0,1,-1], ![0,0,1,1], ![0,0,-1,1], ![0,0,-1,-1] ]

theorem d4_second_moment (k : Fin 4 → ℝ) :
    (d4roots.map fun α => (∑ i, k i * α i) ^ 2).sum = 12 * ∑ i, (k i) ^ 2 := by
  simp only [d4roots, List.map_cons, List.map_nil, List.sum_cons, List.sum_nil,
    Fin.sum_univ_four, Matrix.cons_val_zero, Matrix.cons_val_one,
    Matrix.cons_val_two, Matrix.cons_val_three, Matrix.head_cons, Matrix.tail_cons]
  ring

theorem d4_fourth_moment (k : Fin 4 → ℝ) :
    (d4roots.map fun α => (∑ i, k i * α i) ^ 4).sum = 12 * (∑ i, (k i) ^ 2) ^ 2 := by
  simp only [d4roots, List.map_cons, List.map_nil, List.sum_cons, List.sum_nil,
    Fin.sum_univ_four, Matrix.cons_val_zero, Matrix.cons_val_one,
    Matrix.cons_val_two, Matrix.cons_val_three, Matrix.head_cons, Matrix.tail_cons]
  ring
