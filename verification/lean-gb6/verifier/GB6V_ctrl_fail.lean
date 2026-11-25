import GB6Counts
import GB6CountsD4Q
import GB6Real
import GB6Analytic
import GB6HJ6
/-! v-gb6 controls written by the verifier: every example is a WRONG statement and must fail. -/
namespace GB6V
open GB6
-- F1: planted R-G value 3348 (must fail)
example : cntQ D4 = 3348 := by rw [C01_D4_Q]
-- F2: T off by one, by direct kernel decision
example : cntT D4 = 193 := by decide +kernel
-- F3: competitor shell size 63
example : cntN C7 = 63 := by decide +kernel
-- F4: unordered triads 16 (conjugation-identified reading)
example : cnt3sub D4 = 16 := by decide +kernel
-- F5: S ratio 64/142
example : Sval (cntN D4) (cntT D4) (cntQ D4) = 64 / 142 := by rw [C02_D4_S]; norm_num
-- F6: H off by one
example : cntH D4 = 911039 := by rw [C17_H]
-- F7: competitor T = 1
example : cntT C7 = 1 := by decide +kernel
-- F8: ratio 496/424
example : Sval (cntN D4) (cntT D4) (cntQ D4) / Sval (cntN A4r) (cntT A4r) (cntQ A4r) = 496 / 424 := by
  rw [C07_ratio]; norm_num
-- F9: partners 7
example : ∀ a ∈ D4, (D4.filter (fun b => dot a b == -1)).length = 7 := by decide +kernel
-- F10: BCC Q 541
example : cntQ BCCr = 541 := by decide +kernel
end GB6V
