import GB6Real
/-! w-gb6 CONTROLS (expected to FAIL): perturbed real/rational statements with the SAME proof scripts
as the true theorems in GB6Real. Each theorem below must produce an error. -/
namespace GB6
open Real
theorem K02_S : Sval (cntN D4) (cntT D4) (cntQ D4) = 64 / 142 := by
  unfold Sval; rw [C02_D4_tau2, C02_D4_q4]; norm_num
theorem K03_S : Sval (cntN A4r) (cntT A4r) (cntQ A4r) = 12 / 30 := by
  unfold Sval; rw [C03_tau2, C03_q4]; norm_num
theorem K04_S : Sval (cntN BCCr) (cntT BCCr) (cntQ BCCr) = 16 / 44 := by
  unfold Sval; rw [C04_tau2, C04_q4]; norm_num
theorem K05_q4 : q4 (cntN FCCr) (cntQ FCCr) = 27 / 7 := by
  rw [C05_FCC_N, C05_FCC_Q]; unfold q4; norm_num
theorem K06_q4 : q4 (cntN Z4) (cntQ Z4) = 21 / 9 := by
  rw [C06_Z4_N, C06_Z4_Q]; unfold q4; norm_num
theorem K07_ratio : Sval (cntN D4) (cntT D4) (cntQ D4) / Sval (cntN A4r) (cntT A4r) (cntQ A4r) = 496 / 424 := by
  rw [C02_D4_S, C03_S]; norm_num
theorem K08 : tauR (cntN D4) (cntT D4) / tauR (cntN BCCr) (cntT BCCr) = √3 := by
  rw [C02_D4_tau, C04_tau]
  have h3 : (0 : ℝ) < √3 := Real.sqrt_pos.mpr (by norm_num)
  have h6 : (0 : ℝ) < √6 := Real.sqrt_pos.mpr (by norm_num)
  have hpos : (0 : ℝ) ≤ 4 / √6 / (2 / √3) := by positivity
  have hsq : (4 / √6 / (2 / √3)) ^ 2 = (3 : ℝ) := by
    rw [div_pow, div_pow, div_pow, Real.sq_sqrt (by norm_num), Real.sq_sqrt (by norm_num)]; norm_num
  calc 4 / √6 / (2 / √3) = √((4 / √6 / (2 / √3)) ^ 2) := (Real.sqrt_sq hpos).symm
    _ = √3 := by rw [hsq]
theorem K09 : |(64 / 141 : ℝ) - 0.453911| < 0.0000005 := by rw [abs_lt]; constructor <;> norm_num
theorem K12 (k1 k2 k3 k4 : ℝ) :
    (D4.map fun α => (dotIR [k1, k2, k3, k4] α) ^ 2).sum = 11 * (k1 ^ 2 + k2 ^ 2 + k3 ^ 2 + k4 ^ 2) := by
  rw [D4_eq_lit]; simp [dotIR]; ring
theorem K14 : ((7.5 : ℝ) - 7) ^ 2 = 0.26 := by norm_num
theorem K18 (r u v τ q B : ℝ) (hv : v ≠ 0) (hq : q ≠ 0) (hB : B ≠ 0)
    (hF : r / 2 * B ^ 2 - u / 3 * τ * B ^ 3 + v / 4 * q * B ^ 4 = 0)
    (hF' : r * B - u * τ * B ^ 2 + v * q * B ^ 3 = 0) :
    B = 2 * u * τ / (4 * v * q) := by
  have e1 : B * (r - u * τ * B + v * q * B ^ 2) = 0 := by linear_combination hF'
  have h1 : r - u * τ * B + v * q * B ^ 2 = 0 := (mul_eq_zero.mp e1).resolve_left hB
  have e2 : B ^ 2 * (r / 2 - u * τ * B / 3 + v * q * B ^ 2 / 4) = 0 := by linear_combination hF
  have h2 : r / 2 - u * τ * B / 3 + v * q * B ^ 2 / 4 = 0 :=
    (mul_eq_zero.mp e2).resolve_left (pow_ne_zero 2 hB)
  have e3 : B * (v * q * B / 2 - u * τ / 3) = 0 := by linear_combination h1 - 2 * h2
  have h3 : v * q * B / 2 - u * τ / 3 = 0 := (mul_eq_zero.mp e3).resolve_left hB
  have hB3 : 3 * v * q * B - 2 * u * τ = 0 := by linear_combination 6 * h3
  have hne4 : 4 * v * q ≠ 0 := mul_ne_zero (mul_ne_zero (by norm_num) hv) hq
  rw [eq_div_iff hne4]; linear_combination hB3
theorem K19_A : |Astar - 0.0775763| < 0.00000005 := by
  have hD := C19_disc
  obtain ⟨l, h⟩ := sqrt_bounds (Disc rr) (2 * 3384 * (0.0775763 - 0.00000005) - 192 * 1.54)
    (2 * 3384 * (0.0775763 + 0.00000005) - 192 * 1.54) (by norm_num) (by rw [hD]; norm_num)
    (by rw [hD]; norm_num) (by norm_num)
  unfold Astar; rw [NN_v, TT_v, QQ_v, ueff_v]
  generalize √(Disc rr) = s at l h
  rw [abs_lt]; constructor
  · rw [lt_sub_iff_add_lt, lt_div_iff₀ (by norm_num)]; norm_num at l ⊢; linarith
  · rw [sub_lt_iff_lt_add, div_lt_iff₀ (by norm_num)]; norm_num at h ⊢; linarith
theorem K19_F : |Fmod rr Astar - (-0.0076333)| < 0.00000005 := by
  have hD := C19_disc
  have hs : √(Disc rr) ^ 2 = 32875776 / 625 := by rw [Real.sq_sqrt (by rw [hD]; norm_num), hD]
  obtain ⟨l, h⟩ := sqrt_bounds (Disc rr) 229.3496 229.3497 (by norm_num) (by rw [hD]; norm_num)
    (by rw [hD]; norm_num) (by norm_num)
  have hred : Fmod rr Astar = -4157572102 / 1095008203125 - 2197426 / 131400984375 * √(Disc rr) := by
    unfold Fmod Astar; rw [NN_v, TT_v, QQ_v, ueff_v, reff_v]
    generalize √(Disc rr) = s at hs
    linear_combination (s ^ 2 / 2480110534656 + 77 * s / 484396588800 - 14269 / 672773040000) * hs
  rw [hred, abs_lt]; constructor <;> nlinarith
theorem K19_edge : |rcEdge - 0.2701| < 0.00005 := by
  have hrc : rcEdge = 23716 / 88125 := by unfold rcEdge; rw [NN_v, TT_v, QQ_v, ueff_v]; norm_num
  rw [hrc, abs_lt]; constructor <;> norm_num
theorem K19_det : reffAt (rr + (7.5 - 8) ^ 2) = 0.3582 := by
  have hr : reffAt (rr + (7.5 - 8) ^ 2) = 893 / 2500 := by unfold reffAt rr ps; norm_num
  rw [hr]; norm_num
theorem K20 : |2 * π / √8 - 2.221451| < 0.0000005 := by
  have p1 := Real.pi_gt_d20
  have p2 := Real.pi_lt_d20
  obtain ⟨l8, h8⟩ := sqrt_bounds 8 2.8284271247 2.8284271248 (by norm_num) (by norm_num) (by norm_num) (by norm_num)
  have h8p : (0 : ℝ) < √8 := by linarith
  rw [abs_lt]; constructor
  · rw [lt_sub_iff_add_lt, lt_div_iff₀ h8p]; nlinarith
  · rw [sub_lt_iff_lt_add, div_lt_iff₀ h8p]; nlinarith
theorem K21 (Δt c a0 bracket : ℝ) (ha : a0 ≠ 0) (hbr : bracket = 32) :
    Δt ^ 2 * c ^ 2 / (24 * a0 ^ 2) * bracket = 5 / 3 * (Δt * c / a0) ^ 2 := by
  rw [hbr]; field_simp; ring
theorem K22 : (25 : ℕ) ^ 4 = 390624 := by norm_num
end GB6
