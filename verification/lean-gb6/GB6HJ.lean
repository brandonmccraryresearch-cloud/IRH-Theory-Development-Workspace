import GB6HI2
import GB6HJLit
/-! w-gb6 EXP-1304 C17 (route 2b): the 3-sum table is compressed bucket-by-bucket (key mod 11), so every
kernel evaluation stays small. All reduction lemmas are proved; the literal tables are checked by evaluation. -/
namespace GB6

lemma WI_split (D : List (Int × Nat)) (g : Int → Nat) : WI D g = WI (D.filter fun q => q.1 % 11 == 0) g + WI (D.filter fun q => q.1 % 11 == 1) g + WI (D.filter fun q => q.1 % 11 == 2) g + WI (D.filter fun q => q.1 % 11 == 3) g + WI (D.filter fun q => q.1 % 11 == 4) g + WI (D.filter fun q => q.1 % 11 == 5) g + WI (D.filter fun q => q.1 % 11 == 6) g + WI (D.filter fun q => q.1 % 11 == 7) g + WI (D.filter fun q => q.1 % 11 == 8) g + WI (D.filter fun q => q.1 % 11 == 9) g + WI (D.filter fun q => q.1 % 11 == 10) g := by
  induction D with
  | nil => simp [WI]
  | cons q D ih =>
    have h : q.1 % 11 = 0 ∨ q.1 % 11 = 1 ∨ q.1 % 11 = 2 ∨ q.1 % 11 = 3 ∨ q.1 % 11 = 4 ∨ q.1 % 11 = 5 ∨ q.1 % 11 = 6 ∨ q.1 % 11 = 7 ∨ q.1 % 11 = 8 ∨ q.1 % 11 = 9 ∨ q.1 % 11 = 10 := by omega
    rcases h with h|h|h|h|h|h|h|h|h|h|h <;> simp [List.filter_cons, h, WI_cons, ih] <;> ring

theorem C17J_B0 : cmpI ((stepI E4 litI2).filter fun q => q.1 % 11 == 0) = litB0 := by decide +kernel
lemma C17J_W0 (G : Int → Nat) : WI ((stepI E4 litI2).filter fun q => q.1 % 11 == 0) G = WI litB0 G := by
  rw [← WI_cmp, C17J_B0]
theorem C17J_B1 : cmpI ((stepI E4 litI2).filter fun q => q.1 % 11 == 1) = litB1 := by decide +kernel
lemma C17J_W1 (G : Int → Nat) : WI ((stepI E4 litI2).filter fun q => q.1 % 11 == 1) G = WI litB1 G := by
  rw [← WI_cmp, C17J_B1]
theorem C17J_B2 : cmpI ((stepI E4 litI2).filter fun q => q.1 % 11 == 2) = litB2 := by decide +kernel
lemma C17J_W2 (G : Int → Nat) : WI ((stepI E4 litI2).filter fun q => q.1 % 11 == 2) G = WI litB2 G := by
  rw [← WI_cmp, C17J_B2]
theorem C17J_B3 : cmpI ((stepI E4 litI2).filter fun q => q.1 % 11 == 3) = litB3 := by decide +kernel
lemma C17J_W3 (G : Int → Nat) : WI ((stepI E4 litI2).filter fun q => q.1 % 11 == 3) G = WI litB3 G := by
  rw [← WI_cmp, C17J_B3]
theorem C17J_B4 : cmpI ((stepI E4 litI2).filter fun q => q.1 % 11 == 4) = litB4 := by decide +kernel
lemma C17J_W4 (G : Int → Nat) : WI ((stepI E4 litI2).filter fun q => q.1 % 11 == 4) G = WI litB4 G := by
  rw [← WI_cmp, C17J_B4]
theorem C17J_B5 : cmpI ((stepI E4 litI2).filter fun q => q.1 % 11 == 5) = litB5 := by decide +kernel
lemma C17J_W5 (G : Int → Nat) : WI ((stepI E4 litI2).filter fun q => q.1 % 11 == 5) G = WI litB5 G := by
  rw [← WI_cmp, C17J_B5]
theorem C17J_B6 : cmpI ((stepI E4 litI2).filter fun q => q.1 % 11 == 6) = litB6 := by decide +kernel
lemma C17J_W6 (G : Int → Nat) : WI ((stepI E4 litI2).filter fun q => q.1 % 11 == 6) G = WI litB6 G := by
  rw [← WI_cmp, C17J_B6]
theorem C17J_B7 : cmpI ((stepI E4 litI2).filter fun q => q.1 % 11 == 7) = litB7 := by decide +kernel
lemma C17J_W7 (G : Int → Nat) : WI ((stepI E4 litI2).filter fun q => q.1 % 11 == 7) G = WI litB7 G := by
  rw [← WI_cmp, C17J_B7]
theorem C17J_B8 : cmpI ((stepI E4 litI2).filter fun q => q.1 % 11 == 8) = litB8 := by decide +kernel
lemma C17J_W8 (G : Int → Nat) : WI ((stepI E4 litI2).filter fun q => q.1 % 11 == 8) G = WI litB8 G := by
  rw [← WI_cmp, C17J_B8]
theorem C17J_B9 : cmpI ((stepI E4 litI2).filter fun q => q.1 % 11 == 9) = litB9 := by decide +kernel
lemma C17J_W9 (G : Int → Nat) : WI ((stepI E4 litI2).filter fun q => q.1 % 11 == 9) G = WI litB9 G := by
  rw [← WI_cmp, C17J_B9]
theorem C17J_B10 : cmpI ((stepI E4 litI2).filter fun q => q.1 % 11 == 10) = litB10 := by decide +kernel
lemma C17J_W10 (G : Int → Nat) : WI ((stepI E4 litI2).filter fun q => q.1 % 11 == 10) G = WI litB10 G := by
  rw [← WI_cmp, C17J_B10]

theorem C17J_D3 (G : Int → Nat) : WI (DI3 E4) G = WI litJ3 G := by
  unfold DI3
  rw [WI_cmp, C17I_D2, WI_split, C17J_W0, C17J_W1, C17J_W2, C17J_W3, C17J_W4, C17J_W5, C17J_W6, C17J_W7, C17J_W8, C17J_W9, C17J_W10]
  unfold litJ3
  simp only [WI_append]
  all_goals omega
end GB6
#print axioms GB6.WI_split
#print axioms GB6.C17J_B0
#print axioms GB6.C17J_B1
#print axioms GB6.C17J_B2
#print axioms GB6.C17J_B3
#print axioms GB6.C17J_B4
#print axioms GB6.C17J_B5
#print axioms GB6.C17J_B6
#print axioms GB6.C17J_B7
#print axioms GB6.C17J_B8
#print axioms GB6.C17J_B9
#print axioms GB6.C17J_B10
#print axioms GB6.C17J_D3
