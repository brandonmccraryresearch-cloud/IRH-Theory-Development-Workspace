import GB6Counts
import GB6Grid
import Mathlib.Analysis.SpecialFunctions.Trigonometric.Basic
import Mathlib.Tactic
/-! w-gb6 EXP-1304: (i) completeness of the box-filtered shells ("all integer vectors of norm m");
(ii) C16 analytic part: on the 16^4 grid, Ψ = Σ_k cos(k·x) equals 24 exactly at the 32 counted points;
(iii) C23 Ψ test-point table under the stated (unprinted) convention. -/
namespace GB6
open Real

/-! ### (i) completeness -/
lemma mem_intRange (r : Nat) (x : Int) (h1 : -(r : Int) ≤ x) (h2 : x ≤ r) : x ∈ intRange r := by
  unfold intRange
  rw [List.mem_map]
  refine ⟨(x + r).toNat, ?_, ?_⟩
  · rw [List.mem_range]; omega
  · omega

lemma mem_box (r : Nat) : ∀ (v : V) (d : Nat), v.length = d →
    (∀ x ∈ v, -(r : Int) ≤ x ∧ x ≤ r) → v ∈ box r d := by
  intro v
  induction v with
  | nil => intro d hd _; subst hd; simp [box]
  | cons a v ih =>
    intro d hd hx
    cases d with
    | zero => simp at hd
    | succ d =>
      simp only [List.length_cons, Nat.add_right_cancel_iff] at hd
      unfold box
      rw [List.mem_flatMap]
      refine ⟨a, mem_intRange r a (hx a (by simp)).1 (hx a (by simp)).2, ?_⟩
      rw [List.mem_map]
      exact ⟨v, ih d hd (fun x hxv => hx x (by simp [hxv])), rfl⟩

lemma dot_self_nonneg : ∀ v : V, 0 ≤ dot v v := by
  intro v; induction v with
  | nil => simp [dot]
  | cons a v ih => simp only [dot]; nlinarith [mul_self_nonneg a]

lemma sq_le_normSq : ∀ v : V, ∀ x ∈ v, x * x ≤ normSq v := by
  intro v; induction v with
  | nil => simp
  | cons a v ih =>
    intro x hx
    unfold normSq at ih ⊢; simp only [dot]
    rcases List.mem_cons.mp hx with h | h
    · subst h; nlinarith [dot_self_nonneg v]
    · nlinarith [ih x h, mul_self_nonneg a]

/-- every integer vector of length d and squared norm m (< (r+1)^2) lies in `shellOf d r m` -/
theorem shell_complete (d r : Nat) (m : Int) (hm : m < ((r : Int) + 1) ^ 2) :
    ∀ v : V, v.length = d → normSq v = m → v ∈ shellOf d r m := by
  intro v hl hn
  unfold shellOf
  rw [List.mem_filter]
  refine ⟨mem_box r v d hl (fun x hx => ?_), by simp [hn]⟩
  have h := sq_le_normSq v x hx
  rw [hn] at h
  constructor <;> nlinarith

theorem C01_D4_complete : ∀ v : V, v.length = 4 → normSq v = 2 → v ∈ D4 :=
  shell_complete 4 1 2 (by norm_num)
theorem C13_D4s_complete : ∀ v : V, v.length = 4 → normSq v = 8 → v ∈ D4s :=
  shell_complete 4 2 8 (by norm_num)
theorem C14_C7_complete : ∀ v : V, v.length = 4 → normSq v = 7 → v ∈ C7 :=
  shell_complete 4 3 7 (by norm_num)
theorem C06_Z4_complete : ∀ v : V, v.length = 4 → normSq v = 1 → v ∈ Z4 :=
  shell_complete 4 1 1 (by norm_num)
theorem C04_BCC_complete : ∀ v : V, v.length = 3 → normSq v = 2 → v ∈ BCCr :=
  shell_complete 3 1 2 (by norm_num)
theorem C05_FCC_complete : ∀ v : V, v.length = 3 → normSq v = 3 → v ∈ FCCr :=
  shell_complete 3 1 3 (by norm_num)
theorem C05_SC_complete : ∀ v : V, v.length = 3 → normSq v = 1 → v ∈ SC :=
  shell_complete 3 1 1 (by norm_num)
theorem C03_A4r_complete : ∀ v : V, v.length = 5 → normSq v = 2 → v.sum = 0 → v ∈ A4r := by
  intro v hl hn hs
  unfold A4r; rw [List.mem_filter]
  exact ⟨shell_complete 5 1 2 (by norm_num) v hl hn, by simp [hs]⟩

/-! ### (ii) C16: Ψ(x) = Σ_{k ∈ D4s} cos(k·x) at x = 2πn/16 equals 24 iff every k·n ≡ 0 (mod 16) -/
noncomputable def PsiG (n : V) : ℝ := (D4s.map fun k => Real.cos (2 * π * ((dot k n : ℤ) : ℝ) / 16)).sum

lemma sum_le_length (L : List ℝ) (h : ∀ x ∈ L, x ≤ 1) : L.sum ≤ L.length := by
  induction L with
  | nil => simp
  | cons a L ih =>
    simp only [List.sum_cons, List.length_cons, Nat.cast_add, Nat.cast_one]
    have ha := h a (by simp)
    have := ih (fun x hx => h x (by simp [hx]))
    linarith

lemma sum_eq_length_iff (L : List ℝ) (h : ∀ x ∈ L, x ≤ 1) : L.sum = L.length ↔ ∀ x ∈ L, x = 1 := by
  induction L with
  | nil => simp
  | cons a L ih =>
    have ha := h a (by simp)
    have hL : ∀ x ∈ L, x ≤ 1 := fun x hx => h x (by simp [hx])
    have hle := sum_le_length L hL
    simp only [List.sum_cons, List.length_cons, Nat.cast_add, Nat.cast_one, List.mem_cons, forall_eq_or_imp]
    constructor
    · intro hs
      have h1 : a = 1 := by linarith
      have h2 : L.sum = L.length := by linarith
      exact ⟨h1, (ih hL).mp h2⟩
    · rintro ⟨h1, h2⟩
      rw [h1, (ih hL).mpr h2]; ring

lemma cos_grid_eq_one (m : ℤ) : Real.cos (2 * π * (m : ℝ) / 16) = 1 ↔ m % 16 = 0 := by
  rw [Real.cos_eq_one_iff]
  constructor
  · rintro ⟨j, hj⟩
    have hpi : (π : ℝ) ≠ 0 := Real.pi_ne_zero
    have : (m : ℝ) = 16 * j := by
      field_simp at hj
      linarith
    have hm : m = 16 * j := by exact_mod_cast this
    omega
  · intro h
    refine ⟨m / 16, ?_⟩
    have hm : m = 16 * (m / 16) := by omega
    conv_rhs => rw [hm]
    push_cast; ring

theorem C16_Psi_max_iff : ∀ n : V, PsiG n = 24 ↔ D4s.all (fun k => dot k n % 16 == 0) = true := by
  intro n
  have hlen : (D4s.map fun k => Real.cos (2 * π * ((dot k n : ℤ) : ℝ) / 16)).length = 24 := by
    rw [List.length_map]; exact C13_D4s_N
  unfold PsiG
  rw [show (24 : ℝ) = ((D4s.map fun k => Real.cos (2 * π * ((dot k n : ℤ) : ℝ) / 16)).length : ℝ) by
    rw [hlen]; norm_num]
  rw [sum_eq_length_iff _ (by intro x hx; rw [List.mem_map] at hx; obtain ⟨k, _, rfl⟩ := hx; exact Real.cos_le_one _)]
  rw [List.all_eq_true]
  simp only [List.mem_map, forall_exists_index, and_imp, forall_apply_eq_imp_iff₂, beq_iff_eq]
  exact forall₂_congr (fun k _ => cos_grid_eq_one _)

/-- the grid points where Ψ = 24 are exactly the 32 points counted in C16_grid_count -/
theorem C16_Psi_max_count :
    (∀ n ∈ grid16, PsiG n = 24 ↔ n ∈ grid16.filter (fun n => D4s.all (fun k => dot k n % 16 == 0))) ∧
    (grid16.filter (fun n => D4s.all (fun k => dot k n % 16 == 0))).length = 32 ∧
    (∀ n : V, PsiG n ≤ 24) := by
  refine ⟨fun n hn => ?_, C16_grid_count, fun n => ?_⟩
  · rw [List.mem_filter, C16_Psi_max_iff]; simp [hn]
  · have := sum_le_length (D4s.map fun k => Real.cos (2 * π * ((dot k n : ℤ) : ℝ) / 16))
      (by intro x hx; rw [List.mem_map] at hx; obtain ⟨k, _, rfl⟩ := hx; exact Real.cos_le_one _)
    have hl : D4s.length = 24 := C13_D4s_N
    unfold PsiG; rw [List.length_map, hl] at this; exact_mod_cast this

/-! ### (iii) C23 under the convention: D4 = {y ∈ Z^4 : Σy even}; its dual's minimal shell is
{±e_i} ∪ {(±1/2)^4} (24 vectors, norm 1); Ψ(x) = Σ_g cos(2π g·x). With g = h/2, h ∈ P4 = all integer
vectors of squared norm 4, 2π g·x = π (h·y)/2 for x = y/2. -/
def P4 : List V := shellOf 4 2 4

theorem C23_P4_shell : cntN P4 = 24 ∧ (∀ h ∈ P4, (∀ x ∈ h, x = 2 ∨ x = -2 ∨ x = 0) ∨ (∀ x ∈ h, x = 1 ∨ x = -1)) := by
  constructor <;> decide +kernel
theorem C23_P4_complete : ∀ v : V, v.length = 4 → normSq v = 4 → v ∈ P4 :=
  shell_complete 4 2 4 (by norm_num)

noncomputable def PsiH (y : V) : ℝ := (P4.map fun h => Real.cos (π * ((dot h y : ℤ) : ℝ) / 2)).sum

def sgn (n : ℤ) : ℤ := if n % 2 = 0 then 1 else -1

lemma neg_one_zpow_sgn (n : ℤ) : ((-1 : ℝ) ^ n) = ((sgn n : ℤ) : ℝ) := by
  unfold sgn
  rcases Int.emod_two_eq_zero_or_one n with h | h
  · rw [if_pos h, Even.neg_one_zpow (Int.even_iff.mpr h)]; norm_num
  · rw [if_neg (by omega), Odd.neg_one_zpow (Int.odd_iff.mpr h)]; norm_num

lemma sumcos (L : List V) (y : V) (h : ∀ g ∈ L, dot g y % 2 = 0) :
    (L.map fun g => Real.cos (π * ((dot g y : ℤ) : ℝ) / 2)).sum =
      (((L.map fun g => sgn (dot g y / 2)).sum : ℤ) : ℝ) := by
  induction L with
  | nil => simp
  | cons g L ih =>
    simp only [List.map_cons, List.sum_cons, Int.cast_add]
    rw [ih (fun g' hg' => h g' (by simp [hg']))]
    congr 1
    have he := h g (by simp)
    have hd : dot g y = 2 * (dot g y / 2) := by omega
    rw [show π * ((dot g y : ℤ) : ℝ) / 2 = ((dot g y / 2 : ℤ) : ℝ) * π by
      conv_lhs => rw [hd]
      push_cast; ring]
    rw [Real.cos_int_mul_pi, neg_one_zpow_sgn]

/-- x = (1,1,0,0) ∈ D4 (y = 2x) -/
theorem C23_lattice_point : PsiH [2, 2, 0, 0] = 24 := by
  unfold PsiH
  rw [sumcos P4 _ (by decide +kernel)]
  have : (P4.map fun g => sgn (dot g [2, 2, 0, 0] / 2)).sum = 24 := by decide +kernel
  rw [this]; norm_num
/-- x = (1,0,0,0) ∈ Z^4 \ D4 -/
theorem C23_Z4_point : PsiH [2, 0, 0, 0] = -8 := by
  unfold PsiH
  rw [sumcos P4 _ (by decide +kernel)]
  have : (P4.map fun g => sgn (dot g [2, 0, 0, 0] / 2)).sum = -8 := by decide +kernel
  rw [this]; norm_num
/-- deep hole x = (1/2,1/2,1/2,1/2) -/
theorem C23_deep_hole : PsiH [1, 1, 1, 1] = -8 := by
  unfold PsiH
  rw [sumcos P4 _ (by decide +kernel)]
  have : (P4.map fun g => sgn (dot g [1, 1, 1, 1] / 2)).sum = -8 := by decide +kernel
  rw [this]; norm_num
/-- the two test points are as described: (1,1,0,0) ∈ D4 (even sum), (1,0,0,0) ∈ Z^4 with odd sum -/
theorem C23_points : ([1, 1, 0, 0] : List Int).sum % 2 = 0 ∧ ([1, 0, 0, 0] : List Int).sum % 2 = 1 := by decide

end GB6
#print axioms GB6.C01_D4_complete
#print axioms GB6.C13_D4s_complete
#print axioms GB6.C14_C7_complete
#print axioms GB6.C06_Z4_complete
#print axioms GB6.C04_BCC_complete
#print axioms GB6.C05_FCC_complete
#print axioms GB6.C05_SC_complete
#print axioms GB6.C03_A4r_complete
#print axioms GB6.C16_Psi_max_iff
#print axioms GB6.C16_Psi_max_count
#print axioms GB6.C23_P4_shell
#print axioms GB6.C23_P4_complete
#print axioms GB6.C23_lattice_point
#print axioms GB6.C23_Z4_point
#print axioms GB6.C23_deep_hole
#print axioms GB6.C23_points
