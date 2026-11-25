import GB6Real
import GB6Grid
/-! w-gb6 STRONG CONTROLS (expected to COMPILE): the negation of every perturbed statement is
kernel-proved from the true theorems, so the perturbed statements are refuted, not merely unproved. -/
namespace GB6
open Real
theorem N01 : cntN D4 ≠ 25 ∧ cntT D4 ≠ 191 ∧ cntQ D4 ≠ 3385 := by
  rw [C01_D4_N, C01_D4_T, C01_D4_Q]; decide
theorem N03 : cntN A4r ≠ 21 ∧ cntT A4r ≠ 121 ∧ cntQ A4r ≠ 1861 := by
  rw [C03_A4r_N, C03_A4r_T, C03_A4r_Q]; decide
theorem N04 : cntT BCCr ≠ 49 ∧ cntQ BCCr ≠ 541 := by rw [C04_BCC_T, C04_BCC_Q]; decide
theorem N05 : cntQ FCCr ≠ 217 ∧ cntQ SC ≠ 91 := by rw [C05_FCC_Q, C05_SC_Q]; decide
theorem N06 : cntQ Z4 ≠ 169 ∧ cntQ A4sm ≠ 271 ∧ cntT A4sm ≠ 1 := by
  rw [C06_Z4_Q, C06_A4sm_Q, C06_A4sm_T]; decide
theorem N10 : ¬ ∀ a ∈ D4, (D4.filter (fun b => dot a b == -1)).length = 9 := by
  intro h; have := h _ (by decide +kernel : [1, 1, 0, 0] ∈ D4)
  rw [C10_partners _ (by decide +kernel : [1, 1, 0, 0] ∈ D4)] at this; exact absurd this (by decide)
theorem N11 : ¬ ∀ a ∈ D4, ∀ b ∈ D4, a ≠ b → dot a b ∈ ([-2, -1, 0] : List Int) := by
  intro h
  obtain ⟨a, ha, b, hb, hab, hd⟩ := C11_fingerprint_attained 1 (by decide)
  have := h a ha b hb hab; rw [hd] at this; exact absurd this (by decide)
theorem N13 : cntN D4s ≠ 23 := by rw [C13_D4s_N]; decide
theorem N14 : cntN C7 ≠ 63 ∧ cntT C7 ≠ 1 := by rw [C14_C7_N, C14_C7_T]; decide
theorem N15 : cnt3sub D4 ≠ 33 := by rw [C15_unordered]; decide
theorem N02 : Sval (cntN D4) (cntT D4) (cntQ D4) ≠ 64 / 142 := by rw [C02_D4_S]; norm_num
theorem N03S : Sval (cntN A4r) (cntT A4r) (cntQ A4r) ≠ 12 / 30 := by rw [C03_S]; norm_num
theorem N04S : Sval (cntN BCCr) (cntT BCCr) (cntQ BCCr) ≠ 16 / 44 := by rw [C04_S]; norm_num
theorem N05q : q4 (cntN FCCr) (cntQ FCCr) ≠ 27 / 7 := by rw [C05_FCC_q4]; norm_num
theorem N06q : q4 (cntN Z4) (cntQ Z4) ≠ 21 / 9 := by rw [C06_Z4_q4]; norm_num
theorem N07 : Sval (cntN D4) (cntT D4) (cntQ D4) / Sval (cntN A4r) (cntT A4r) (cntQ A4r) ≠ 496 / 424 := by
  rw [C07_ratio]; norm_num
theorem N08 : tauR (cntN D4) (cntT D4) / tauR (cntN BCCr) (cntT BCCr) ≠ √3 := by
  rw [C08_tau_ratio]; intro h
  have h2 := congrArg (fun x => x ^ 2) h
  simp only [Real.sq_sqrt (show (0:ℝ) ≤ 2 by norm_num), Real.sq_sqrt (show (0:ℝ) ≤ 3 by norm_num)] at h2
  norm_num at h2
theorem N09 : ¬ |(64 / 141 : ℝ) - 0.453911| < 0.0000005 := by
  rw [abs_lt]; intro ⟨h1, _⟩; norm_num at h1
theorem N12 : ¬ ∀ k1 k2 k3 k4 : ℝ,
    (D4.map fun α => (dotIR [k1, k2, k3, k4] α) ^ 2).sum = 11 * (k1 ^ 2 + k2 ^ 2 + k3 ^ 2 + k4 ^ 2) := by
  intro h; have := h 1 0 0 0; rw [C12_iso2] at this; norm_num at this
theorem N14p : ((7.5 : ℝ) - 7) ^ 2 ≠ 0.26 := by norm_num
theorem N18 : ¬ ∀ r u v τ q B : ℝ, v ≠ 0 → q ≠ 0 → B ≠ 0 →
    r / 2 * B ^ 2 - u / 3 * τ * B ^ 3 + v / 4 * q * B ^ 4 = 0 →
    r * B - u * τ * B ^ 2 + v * q * B ^ 3 = 0 → B = 2 * u * τ / (4 * v * q) := by
  intro h
  have := h (2 / 9) 1 1 1 1 (2 / 3) (by norm_num) (by norm_num) (by norm_num) (by norm_num) (by norm_num)
  norm_num at this
theorem N19A : ¬ |Astar - 0.0775763| < 0.00000005 := by
  have := C19_Astar.2.2.2.2; rw [abs_lt] at this ⊢; intro ⟨h1, h2⟩; norm_num at *; linarith
theorem N19F : ¬ |Fmod rr Astar - (-0.0076333)| < 0.00000005 := by
  have := C19_Fexc; rw [abs_lt] at this ⊢; intro ⟨h1, h2⟩; norm_num at *; linarith
theorem N19e : ¬ |rcEdge - 0.2701| < 0.00005 := by
  have := C19_edge.2.2.1; rw [abs_lt] at this ⊢; intro ⟨h1, h2⟩; norm_num at *; linarith
theorem N19d : reffAt (rr + (7.5 - 8) ^ 2) ≠ 0.3582 := by rw [C19_detuned.2.1]; norm_num
theorem N20 : ¬ |2 * π / √8 - 2.221451| < 0.0000005 := by
  have := C20_a0_dt.1; rw [abs_lt] at this ⊢; intro ⟨h1, h2⟩; norm_num at *; linarith
theorem N21 : ¬ ∀ Δt c a0 bracket : ℝ, a0 ≠ 0 → bracket = 32 →
    Δt ^ 2 * c ^ 2 / (24 * a0 ^ 2) * bracket = 5 / 3 * (Δt * c / a0) ^ 2 := by
  intro h; have := h 1 1 1 32 (by norm_num) rfl; norm_num at this
theorem N22 : (25 : ℕ) ^ 4 ≠ 390624 := by norm_num
theorem N16 : (grid16.filter (fun n => D4s.all (fun k => dot k n % 16 == 0))).length ≠ 33 := by
  rw [C16_grid_count]; decide
end GB6
