import GB6HJ
/-! w-gb6 EXP-1304 C17: H(D4) = 911040 (ordered zero-sum 6-tuples of D4 roots, D-H reading). -/
namespace GB6
def Gin (x : Int) : Nat := WI litJ3 (fun y => ind (x + y == 0))
theorem C17J_P0 : WI litB0 Gin = 78498 := by decide +kernel
theorem C17J_P1 : WI litB1 Gin = 88661 := by decide +kernel
theorem C17J_P2 : WI litB2 Gin = 78995 := by decide +kernel
theorem C17J_P3 : WI litB3 Gin = 79356 := by decide +kernel
theorem C17J_P4 : WI litB4 Gin = 80112 := by decide +kernel
theorem C17J_P5 : WI litB5 Gin = 89147 := by decide +kernel
theorem C17J_P6 : WI litB6 Gin = 89147 := by decide +kernel
theorem C17J_P7 : WI litB7 Gin = 80112 := by decide +kernel
theorem C17J_P8 : WI litB8 Gin = 79356 := by decide +kernel
theorem C17J_P9 : WI litB9 Gin = 78995 := by decide +kernel
theorem C17J_P10 : WI litB10 Gin = 88661 := by decide +kernel
theorem C17_H : cntH D4 = 911040 := by
  rw [cntH_tableI]
  simp only [C17J_D3]
  show WI litJ3 Gin = 911040
  rw [show litJ3 = litB0 ++ litB1 ++ litB2 ++ litB3 ++ litB4 ++ litB5 ++ litB6 ++ litB7 ++ litB8 ++ litB9 ++ litB10 from rfl]
  simp only [WI_append, C17J_P0, C17J_P1, C17J_P2, C17J_P3, C17J_P4, C17J_P5, C17J_P6, C17J_P7, C17J_P8, C17J_P9, C17J_P10]
  all_goals norm_num
/-- strong control (expected to COMPILE): the perturbed value is refuted -/
theorem C17_H_ne : cntH D4 ≠ 911041 := by rw [C17_H]; decide
end GB6
#print axioms GB6.C17J_P0
#print axioms GB6.C17J_P1
#print axioms GB6.C17J_P2
#print axioms GB6.C17J_P3
#print axioms GB6.C17J_P4
#print axioms GB6.C17J_P5
#print axioms GB6.C17J_P6
#print axioms GB6.C17J_P7
#print axioms GB6.C17J_P8
#print axioms GB6.C17J_P9
#print axioms GB6.C17J_P10
#print axioms GB6.C17_H
#print axioms GB6.C17_H_ne
