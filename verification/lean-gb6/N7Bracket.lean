import GB6Real
import Mathlib.Analysis.SpecialFunctions.Trigonometric.Basic
import Mathlib.Tactic
/-! w-n7 EXP-1313 (G-B6 N7): the v94 l.468/l.480/l.505 bracket
  B(k) = Σ_{α ∈ Φ_{D4}} (1 − cos(k·α)),  Φ_{D4} = {±e_i ± e_j} (v94 l.171),
  satisfies B k ≤ 32 for all k ∈ ℝ⁴, with equality at (0,0,π,π); hence sup = 32,
  which discharges hypothesis `hbr` of `GB6.C21_sin2` (GB6Real.lean l.321). -/
namespace N7
open Real

/-- the 24 roots ±e_i ± e_j (i<j) of D4, listed pair by pair -/
def roots : List (Fin 4 → ℤ) :=
  [ ![1,1,0,0], ![1,-1,0,0], ![-1,1,0,0], ![-1,-1,0,0],
    ![1,0,1,0], ![1,0,-1,0], ![-1,0,1,0], ![-1,0,-1,0],
    ![1,0,0,1], ![1,0,0,-1], ![-1,0,0,1], ![-1,0,0,-1],
    ![0,1,1,0], ![0,1,-1,0], ![0,-1,1,0], ![0,-1,-1,0],
    ![0,1,0,1], ![0,1,0,-1], ![0,-1,0,1], ![0,-1,0,-1],
    ![0,0,1,1], ![0,0,1,-1], ![0,0,-1,1], ![0,0,-1,-1] ]

/-- faithfulness of the root list: 24 distinct vectors, each of squared norm 2 -/
theorem roots_length : roots.length = 24 := by decide
theorem roots_nodup : roots.Nodup := by decide +kernel
theorem roots_norm2 : ∀ α ∈ roots, ∑ i, α i ^ 2 = 2 := by decide +kernel

/-- g : Fin 3 → ℤ, 0 ↦ -1, 1 ↦ 0, 2 ↦ 1 -/
def g (t : Fin 3) : ℤ := (t : ℤ) - 1
/-- completeness: every vector with entries in {-1,0,1} and squared norm 2 is in the list
  (together with `roots_norm2`: the list is exactly the norm-2 vectors of ℤ⁴ with entries in {-1,0,1},
  i.e. {±e_i ± e_j}) -/
theorem roots_complete : ∀ w : Fin 4 → Fin 3,
    ∑ i, g (w i) ^ 2 = 2 → (fun i => g (w i)) ∈ roots := by decide +kernel

/-- dot product k·α -/
noncomputable def dot (k : Fin 4 → ℝ) (α : Fin 4 → ℤ) : ℝ := ∑ i, k i * (α i : ℝ)

/-- the bracket of v94 eq. (7) at a₀ = 1 -/
noncomputable def B (k : Fin 4 → ℝ) : ℝ := (roots.map (fun α => 1 - Real.cos (dot k α))).sum

/-- closed form (v94 l.466): B k = 24 − 4 Σ_{i<j} cos k_i cos k_j -/
theorem B_closed (k : Fin 4 → ℝ) :
    B k = 24 - 4 * (cos (k 0) * cos (k 1) + cos (k 0) * cos (k 2) + cos (k 0) * cos (k 3)
      + cos (k 1) * cos (k 2) + cos (k 1) * cos (k 3) + cos (k 2) * cos (k 3)) := by
  simp only [B, roots, dot, List.map_cons, List.map_nil, List.sum_cons, List.sum_nil,
    Fin.sum_univ_four, Matrix.cons_val_zero, Matrix.cons_val_one, Matrix.cons_val_two,
    Matrix.cons_val_three, Matrix.head_cons, Matrix.tail_cons]
  push_cast
  simp only [mul_one, mul_zero, add_zero, zero_add, mul_neg, neg_add_eq_sub, ← sub_eq_add_neg]
  simp only [cos_add, cos_sub, cos_neg, sin_neg, cos_zero, sin_zero]
  ring

/-- (i) the bound -/
theorem bracket_le_32 : ∀ k : Fin 4 → ℝ, B k ≤ 32 := by
  intro k
  rw [B_closed]
  nlinarith [sq_nonneg (cos (k 0) + cos (k 1) + cos (k 2) + cos (k 3)),
    cos_sq_le_one (k 0), cos_sq_le_one (k 1), cos_sq_le_one (k 2), cos_sq_le_one (k 3)]

/-- (ii) attainment at (0,0,π,π) -/
theorem bracket_attained : B ![0, 0, π, π] = 32 := by
  rw [B_closed]
  simp [Matrix.cons_val_zero, Matrix.cons_val_one, Matrix.cons_val_two, Matrix.cons_val_three]
  norm_num

/-- the bracket's maximum over ℝ⁴ is 32, attained -/
theorem bracket_isGreatest : IsGreatest (Set.range B) 32 :=
  ⟨⟨![0, 0, π, π], bracket_attained⟩, by rintro _ ⟨k, rfl⟩; exact bracket_le_32 k⟩

/-- (iii) connector: `hbr` of `GB6.C21_sin2` holds for bracket := sup_k B k -/
theorem hbr_discharged : sSup (Set.range B) = 32 := bracket_isGreatest.csSup_eq

/-- C21 with condition (i) discharged (the eq. (7) prefactor reading, condition (ii), stays carried
  exactly as in GB6.C21_prefactor) -/
theorem C21_sin2_unconditional (Δt c a0 : ℝ) (ha : a0 ≠ 0) :
    Δt ^ 2 * c ^ 2 / (24 * a0 ^ 2) * sSup (Set.range B) = 4 / 3 * (Δt * c / a0) ^ 2 :=
  GB6.C21_sin2 Δt c a0 (sSup (Set.range B)) ha hbr_discharged

/-- printed form with lattice spacing a₀: B_{a₀}(k) = Σ_α (1 − cos(a₀ k·α)) -/
noncomputable def Ba (a0 : ℝ) (k : Fin 4 → ℝ) : ℝ :=
  (roots.map (fun α => 1 - Real.cos (a0 * dot k α))).sum

theorem Ba_eq (a0 : ℝ) (k : Fin 4 → ℝ) : Ba a0 k = B (fun i => a0 * k i) := by
  have : ∀ α : Fin 4 → ℤ, a0 * dot k α = dot (fun i => a0 * k i) α := by
    intro α; simp only [dot, Finset.mul_sum]; congr 1; ext i; ring
  simp only [Ba, B, this]

theorem Ba_le_32 (a0 : ℝ) (k : Fin 4 → ℝ) : Ba a0 k ≤ 32 := by
  rw [Ba_eq]; exact bracket_le_32 _

theorem Ba_attained (a0 : ℝ) (ha : a0 ≠ 0) : Ba a0 ![0, 0, π / a0, π / a0] = 32 := by
  rw [Ba_eq]
  have : (fun i => a0 * (![0, 0, π / a0, π / a0] : Fin 4 → ℝ) i) = ![0, 0, π, π] := by
    ext i; fin_cases i <;> simp [mul_div_cancel₀ _ ha]
  rw [this]; exact bracket_attained

theorem Ba_sSup (a0 : ℝ) (ha : a0 ≠ 0) : sSup (Set.range (Ba a0)) = 32 :=
  IsGreatest.csSup_eq ⟨⟨_, Ba_attained a0 ha⟩, by rintro _ ⟨k, rfl⟩; exact Ba_le_32 a0 k⟩

/-- zone reading (v94 l.518: D4 zone facets at π e_i and π(±½)⁴, a₀ = 1):
  Z = {x : ∀ i, |x i| ≤ π, Σ |x i| ≤ 2π}; the maximiser (0,0,π,π) lies in Z, so the max over Z is 32 too -/
def Zone : Set (Fin 4 → ℝ) := {x | (∀ i, |x i| ≤ π) ∧ ∑ i, |x i| ≤ 2 * π}

theorem attain_in_zone : (![0, 0, π, π] : Fin 4 → ℝ) ∈ Zone := by
  refine ⟨?_, ?_⟩
  · intro i; fin_cases i <;> simp [abs_of_pos pi_pos, pi_pos.le]
  · simp [Fin.sum_univ_four, abs_of_pos pi_pos]; linarith

theorem zone_sSup : sSup (B '' Zone) = 32 :=
  IsGreatest.csSup_eq ⟨⟨_, attain_in_zone, bracket_attained⟩,
    by rintro _ ⟨k, _, rfl⟩; exact bracket_le_32 k⟩

end N7

#print axioms N7.roots_nodup
#print axioms N7.roots_norm2
#print axioms N7.roots_complete
#print axioms N7.B_closed
#print axioms N7.bracket_le_32
#print axioms N7.bracket_attained
#print axioms N7.bracket_isGreatest
#print axioms N7.hbr_discharged
#print axioms N7.C21_sin2_unconditional
#print axioms N7.Ba_le_32
#print axioms N7.Ba_attained
#print axioms N7.Ba_sSup
#print axioms N7.attain_in_zone
#print axioms N7.zone_sSup
