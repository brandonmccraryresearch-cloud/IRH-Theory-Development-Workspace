import GB6Core
/-! w-gb6 CONTROLS (expected to FAIL): perturbed count statements, same proof method.
Each `theorem` below must produce an error. -/
namespace GB6
theorem K01_N : cntN D4 = 25 := by decide +kernel
theorem K01_T : cntT D4 = 191 := by decide +kernel
theorem K03_N : cntN A4r = 21 := by decide +kernel
theorem K03_T : cntT A4r = 121 := by decide +kernel
theorem K04_T : cntT BCCr = 49 := by decide +kernel
theorem K04_Q : cntQ BCCr = 541 := by decide +kernel
theorem K05_FCC_Q : cntQ FCCr = 217 := by decide +kernel
theorem K05_SC_Q : cntQ SC = 91 := by decide +kernel
theorem K06_Z4_Q : cntQ Z4 = 169 := by decide +kernel
theorem K06_A4_Q : cntQ A4sm = 271 := by decide +kernel
theorem K06_A4_T : cntT A4sm = 1 := by decide +kernel
theorem K10_partners : ∀ a ∈ D4, (D4.filter (fun b => dot a b == -1)).length = 9 := by decide +kernel
theorem K11_fp : ∀ a ∈ D4, ∀ b ∈ D4, a ≠ b → dot a b ∈ [-2, -1, 0] := by decide +kernel
theorem K13_N : cntN D4s = 23 := by decide +kernel
theorem K14_N : cntN C7 = 63 := by decide +kernel
theorem K14_T : cntT C7 = 1 := by decide +kernel
theorem K15 : cnt3sub D4 = 33 := by decide +kernel
end GB6
