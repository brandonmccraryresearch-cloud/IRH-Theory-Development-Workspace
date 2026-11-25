import GB6Core
/-! w-gb6 EXP-1304: finite shell counts (C01 N,T; C03–C06; C10; C11; C13; C14 counts; C15).
All proofs `decide +kernel` (kernel evaluation; no native_decide). -/
namespace GB6

-- distinctness of every shell (so list counts = set counts)
theorem D4_nodup : D4.Nodup := by decide +kernel
theorem D4s_nodup : D4s.Nodup := by decide +kernel
theorem Z4_nodup : Z4.Nodup := by decide +kernel
theorem A4r_nodup : A4r.Nodup := by decide +kernel
theorem A4sm_nodup : A4sm.Nodup := by decide +kernel
theorem BCCr_nodup : BCCr.Nodup := by decide +kernel
theorem FCCr_nodup : FCCr.Nodup := by decide +kernel
theorem SC_nodup : SC.Nodup := by decide +kernel
theorem C7_nodup : C7.Nodup := by decide +kernel

-- C01 (Q in GB6CountsD4Q)
theorem C01_D4_N : cntN D4 = 24 := by decide +kernel
theorem C01_D4_T : cntT D4 = 192 := by decide +kernel
-- D4 = ±e_i±e_j : each element has exactly two nonzero coordinates, each ±1
theorem C01_D4_form : ∀ v ∈ D4, v.length = 4 ∧ (v.filter (· != 0)).length = 2 ∧
    ∀ x ∈ v, x = 0 ∨ x = 1 ∨ x = -1 := by decide +kernel

-- C03 A4* row (20,120,1860)  (Q in GB6CountsA4Q)
theorem C03_A4r_N : cntN A4r = 20 := by decide +kernel
theorem C03_A4r_T : cntT A4r = 120 := by decide +kernel
theorem C03_A4r_form : ∀ v ∈ A4r, v.length = 5 ∧ (v.filter (· == 1)).length = 1 ∧
    (v.filter (· == -1)).length = 1 ∧ (v.filter (· == 0)).length = 3 := by decide +kernel

-- C04 BCC row (12,48,540)
theorem C04_BCC_N : cntN BCCr = 12 := by decide +kernel
theorem C04_BCC_T : cntT BCCr = 48 := by decide +kernel
theorem C04_BCC_Q : cntQ BCCr = 540 := by decide +kernel

-- C05 FCC (8,0,216), SC (6,0,90)
theorem C05_FCC_N : cntN FCCr = 8 := by decide +kernel
theorem C05_FCC_T : cntT FCCr = 0 := by decide +kernel
theorem C05_FCC_Q : cntQ FCCr = 216 := by decide +kernel
theorem C05_SC_N : cntN SC = 6 := by decide +kernel
theorem C05_SC_T : cntT SC = 0 := by decide +kernel
theorem C05_SC_Q : cntQ SC = 90 := by decide +kernel

-- C06 Z4 (8,0,168), A4 row (10,0,270)
theorem C06_Z4_N : cntN Z4 = 8 := by decide +kernel
theorem C06_Z4_T : cntT Z4 = 0 := by decide +kernel
theorem C06_Z4_Q : cntQ Z4 = 168 := by decide +kernel
theorem C06_A4sm_N : cntN A4sm = 10 := by decide +kernel
theorem C06_A4sm_T : cntT A4sm = 0 := by decide +kernel
theorem C06_A4sm_Q : cntQ A4sm = 270 := by decide +kernel
-- A4sm vectors lie in the sum-zero hyperplane and all have the same norm (a single shell)
theorem C06_A4sm_shell : ∀ v ∈ A4sm, v.sum = 0 ∧ normSq v = 20 := by decide +kernel

-- C10 eight partners at dot −1 (cos = −1/2 since |α|^2 = 2), and they are exactly the triads
theorem C10_norm2 : ∀ a ∈ D4, normSq a = 2 := by decide +kernel
theorem C10_partners : ∀ a ∈ D4, (D4.filter (fun b => dot a b == -1)).length = 8 := by decide +kernel
theorem C10_triad_iff : ∀ a ∈ D4, ∀ b ∈ D4, D4.contains (vneg (vadd a b)) = (dot a b == -1) := by
  decide +kernel
theorem C10_T_eq_partner_pairs :
    cntT D4 = (D4.flatMap fun a => D4.filter fun b => dot a b == -1).length ∧
    (D4.flatMap fun a => D4.filter fun b => dot a b == -1).length = 24 * 8 := by decide +kernel

-- C11 fingerprint: for distinct roots the dot product lies in {−2,−1,0,1}
-- (cos = dot/2 ∈ {−1,−1/2,0,1/2}) and every value is attained
theorem C11_fingerprint_range : ∀ a ∈ D4, ∀ b ∈ D4, a ≠ b → dot a b ∈ [-2, -1, 0, 1] := by
  decide +kernel
theorem C11_fingerprint_attained : ∀ x ∈ ([-2, -1, 0, 1] : List Int),
    ∃ a ∈ D4, ∃ b ∈ D4, a ≠ b ∧ dot a b = x := by decide +kernel

-- C13 scaled shell: 24 modes, |k|^2 = 8, form (±2,±2,0,0)
theorem C13_D4s_N : cntN D4s = 24 := by decide +kernel
theorem C13_D4s_form : ∀ v ∈ D4s, v.length = 4 ∧ normSq v = 8 ∧ (v.filter (· != 0)).length = 2 ∧
    ∀ x ∈ v, x = 0 ∨ x = 2 ∨ x = -2 := by decide +kernel
theorem C13_D4s_T : cntT D4s = 192 := by decide +kernel

-- C14 competitor |k|^2=7: 64 modes, zero triad content, form (±2,±1,±1,±1)
theorem C14_C7_N : cntN C7 = 64 := by decide +kernel
theorem C14_C7_T : cntT C7 = 0 := by decide +kernel
theorem C14_C7_form : ∀ v ∈ C7, v.length = 4 ∧ (v.filter (fun x => x == 2 || x == -2)).length = 1 ∧
    (v.filter (fun x => x == 1 || x == -1)).length = 3 := by decide +kernel

-- C15 32 unordered closed triads; 192 = 6 * 32
theorem C15_unordered : cnt3sub D4 = 32 := by decide +kernel
theorem C15_ordered_vs_unordered : cntT D4 = 6 * cnt3sub D4 := by decide +kernel

end GB6

#print axioms GB6.D4_nodup
#print axioms GB6.C01_D4_N
#print axioms GB6.C01_D4_T
#print axioms GB6.C01_D4_form
#print axioms GB6.C03_A4r_N
#print axioms GB6.C03_A4r_T
#print axioms GB6.C03_A4r_form
#print axioms GB6.C04_BCC_N
#print axioms GB6.C04_BCC_T
#print axioms GB6.C04_BCC_Q
#print axioms GB6.C05_FCC_N
#print axioms GB6.C05_FCC_T
#print axioms GB6.C05_FCC_Q
#print axioms GB6.C05_SC_N
#print axioms GB6.C05_SC_T
#print axioms GB6.C05_SC_Q
#print axioms GB6.C06_Z4_N
#print axioms GB6.C06_Z4_T
#print axioms GB6.C06_Z4_Q
#print axioms GB6.C06_A4sm_N
#print axioms GB6.C06_A4sm_T
#print axioms GB6.C06_A4sm_Q
#print axioms GB6.C06_A4sm_shell
#print axioms GB6.C10_norm2
#print axioms GB6.C10_partners
#print axioms GB6.C10_triad_iff
#print axioms GB6.C10_T_eq_partner_pairs
#print axioms GB6.C11_fingerprint_range
#print axioms GB6.C11_fingerprint_attained
#print axioms GB6.C13_D4s_N
#print axioms GB6.C13_D4s_form
#print axioms GB6.C13_D4s_T
#print axioms GB6.C14_C7_N
#print axioms GB6.C14_C7_T
#print axioms GB6.C14_C7_form
#print axioms GB6.C15_unordered
#print axioms GB6.C15_ordered_vs_unordered
#print axioms GB6.D4s_nodup
#print axioms GB6.Z4_nodup
#print axioms GB6.A4r_nodup
#print axioms GB6.A4sm_nodup
#print axioms GB6.BCCr_nodup
#print axioms GB6.FCCr_nodup
#print axioms GB6.SC_nodup
#print axioms GB6.C7_nodup
