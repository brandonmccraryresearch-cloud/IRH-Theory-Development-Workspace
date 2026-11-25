import GB6Counts
import GB6CountsD4Q
import GB6Real
import GB6HJ6
/-! v-gb6 strong controls: negations of the wrong statements, must COMPILE. -/
namespace GB6V
open GB6
theorem N1 : cntQ D4 ≠ 3348 := by rw [C01_D4_Q]; decide
theorem N2 : cntT D4 ≠ 193 := by rw [C01_D4_T]; decide
theorem N3 : cntN C7 ≠ 63 := by rw [C14_C7_N]; decide
theorem N4 : cnt3sub D4 ≠ 16 := by rw [C15_unordered]; decide
theorem N5 : Sval (cntN D4) (cntT D4) (cntQ D4) ≠ 64 / 142 := by rw [C02_D4_S]; norm_num
theorem N6 : cntH D4 ≠ 911039 := by rw [C17_H]; decide
theorem N7 : cntQ BCCr ≠ 541 := by rw [C04_BCC_Q]; decide
end GB6V
#print axioms GB6V.N1
#print axioms GB6V.N6
