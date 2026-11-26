import N7Bracket
import Mathlib.Tactic
/-! v-n7 (verifier-authored, run 13, EXP-1313) independent cross-check of the author's N7 module.
  Different encoding of the root set: pairs (i<j) x sign pairs (s,t) in {±1}², evaluated by the
  pair identity Σ_{s,t}(1-cos(s x + t y)) = 4 - 4 cos x cos y (v94 l.473), NOT via N7.B_closed.
  Bridge N7.B = B2 proved by unfolding N7.B directly (no trig identities used in the bridge).
  Also: integer norm-2 vectors are exactly the list (closes the author's informal step),
  the corner (π,π,π,π) gives 0, and C21_sin2's hypothesis is satisfiable by bracket := 32 itself. -/
namespace VN7
open Real

noncomputable def pairTerm (x y : ℝ) : ℝ :=
  (1 - cos (x + y)) + (1 - cos (x - y)) + (1 - cos (-x + y)) + (1 - cos (-x - y))

theorem pairTerm_eq (x y : ℝ) : pairTerm x y = 4 - 4 * (cos x * cos y) := by
  unfold pairTerm
  have h1 : cos (-x + y) = cos (x - y) := by
    rw [show -x + y = -(x - y) by ring, cos_neg]
  have h2 : cos (-x - y) = cos (x + y) := by
    rw [show -x - y = -(x + y) by ring, cos_neg]
  rw [h1, h2, cos_add, cos_sub]
  ring

/-- bracket, pair-and-sign encoding of the 24 roots ±e_i±e_j -/
noncomputable def B2 (k : Fin 4 → ℝ) : ℝ :=
  pairTerm (k 0) (k 1) + pairTerm (k 0) (k 2) + pairTerm (k 0) (k 3)
  + pairTerm (k 1) (k 2) + pairTerm (k 1) (k 3) + pairTerm (k 2) (k 3)

theorem B2_le (k : Fin 4 → ℝ) : B2 k ≤ 32 := by
  simp only [B2, pairTerm_eq]
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

theorem B2_attained : B2 ![0, 0, π, π] = 32 := by
  simp [B2, pairTerm_eq]
  norm_num

/-- the corner (π,π,π,π) is a MINIMUM (value 0), not a maximiser -/
theorem B2_pi4 : B2 ![π, π, π, π] = 0 := by
  simp [B2, pairTerm_eq]

/-- bridge: the author's list-based B equals the pair encoding (direct unfolding, no B_closed) -/
theorem B_eq_B2 (k : Fin 4 → ℝ) : N7.B k = B2 k := by
  simp only [N7.B, N7.roots, N7.dot, List.map_cons, List.map_nil, List.sum_cons, List.sum_nil,
    Fin.sum_univ_four, Matrix.cons_val_zero, Matrix.cons_val_one, Matrix.cons_val_two,
    Matrix.cons_val_three, Matrix.head_cons, Matrix.tail_cons]
  push_cast
  simp only [B2, pairTerm]
  ring_nf

theorem N7B_le_indep (k : Fin 4 → ℝ) : N7.B k ≤ 32 := by
  rw [B_eq_B2]; exact B2_le k

theorem N7B_sSup_indep : sSup (Set.range N7.B) = 32 := by
  refine IsGreatest.csSup_eq ⟨⟨![0, 0, π, π], ?_⟩, ?_⟩
  · rw [B_eq_B2]; exact B2_attained
  · rintro _ ⟨k, rfl⟩; exact N7B_le_indep k

theorem N7B_pi4 : N7.B ![π, π, π, π] = 0 := by
  rw [B_eq_B2]; exact B2_pi4

/-- every integer vector of squared norm 2 is in the author's list (closes the informal
  "entries in {-1,0,1}" step for the completeness direction) -/
theorem int_norm2_mem (v : Fin 4 → ℤ) (h : ∑ i, v i ^ 2 = 2) : v ∈ N7.roots := by
  have hb : ∀ i, -1 ≤ v i ∧ v i ≤ 1 := by
    intro i
    have hi : v i ^ 2 ≤ 2 := by
      rw [← h]
      exact Finset.single_le_sum (f := fun j => v j ^ 2) (fun j _ => sq_nonneg (v j))
        (Finset.mem_univ i)
    constructor <;> nlinarith
  rw [Fin.sum_univ_four] at h
  have hv : v = ![v 0, v 1, v 2, v 3] := by
    ext i; fin_cases i <;> rfl
  obtain ⟨l0, u0⟩ := hb 0
  obtain ⟨l1, u1⟩ := hb 1
  obtain ⟨l2, u2⟩ := hb 2
  obtain ⟨l3, u3⟩ := hb 3
  rw [hv]
  generalize v 0 = a at *
  generalize v 1 = b at *
  generalize v 2 = c at *
  generalize v 3 = d at *
  clear hv hb
  revert h
  interval_cases a <;> interval_cases b <;> interval_cases c <;> interval_cases d <;> decide

/-- vacuity probe: C21_sin2's hypothesis hbr is met by bracket := 32 with rfl, so C21_sin2 alone
  carries no information about the printed bracket; the content is in N7B_sSup_indep. -/
theorem C21_hbr_trivial (Δt c a0 : ℝ) (ha : a0 ≠ 0) :
    Δt ^ 2 * c ^ 2 / (24 * a0 ^ 2) * 32 = 4 / 3 * (Δt * c / a0) ^ 2 :=
  GB6.C21_sin2 Δt c a0 32 ha rfl

end VN7

#print axioms VN7.pairTerm_eq
#print axioms VN7.B2_le
#print axioms VN7.B2_attained
#print axioms VN7.B2_pi4
#print axioms VN7.B_eq_B2
#print axioms VN7.N7B_le_indep
#print axioms VN7.N7B_sSup_indep
#print axioms VN7.N7B_pi4
#print axioms VN7.int_norm2_mem
#print axioms VN7.C21_hbr_trivial
