import Mathlib.Analysis.Real.Sqrt
import Mathlib.Tactic

/-! # The selection criterion (IRH v93, Sec. II.3 and II.5)

For F(B) = r/2 B² - u/3 τ B³ + v/4 q₄ B⁴, the ordered minimum becomes
degenerate with the disordered state where F = 0 and F' = 0 simultaneously.
We verify that the paper's closed forms
  B* = 2uτ/(3vq₄),    r_c = (2/9) u²τ²/(v q₄)
indeed solve that system, and we verify the exact closed-form values
τ_D4 = 4/√6, S_D4 = 64/141, τ_BCC = 2/√3, S_BCC = 16/45,
the √2 ratio, and the 17.3% margin (exactly 73/423).
-/

/-- The (B*, r_c) quoted in Sec. II.3 solve F = 0 and F' = 0. -/
theorem selection_criterion (u v τ q₄ : ℝ) (hu : u ≠ 0) (hv : v ≠ 0)
    (hτ : τ ≠ 0) (hq : q₄ ≠ 0) :
    let B := 2 * u * τ / (3 * v * q₄)
    let r := 2 / 9 * u ^ 2 * τ ^ 2 / (v * q₄)
    (r / 2 * B ^ 2 - u / 3 * τ * B ^ 3 + v / 4 * q₄ * B ^ 4 = 0) ∧
      (r * B - u * τ * B ^ 2 + v * q₄ * B ^ 3 = 0) := by
  have h1 : (3 : ℝ) * v * q₄ ≠ 0 := mul_ne_zero (mul_ne_zero (by norm_num) hv) hq
  have h2 : (9 : ℝ) ≠ 0 := by norm_num
  have h3 : v * q₄ ≠ 0 := mul_ne_zero hv hq
  simp only
  constructor <;> field_simp <;> ring

/-- τ_D4² = (4/√6)² = 8/3 = 192²/24³. -/
theorem tau_D4_sq : (4 / Real.sqrt 6) ^ 2 = 8 / 3 := by
  rw [div_pow, Real.sq_sqrt (by norm_num)]; norm_num

/-- τ_BCC² = (2/√3)² = 4/3 = 48²/12³. -/
theorem tau_BCC_sq : (2 / Real.sqrt 3) ^ 2 = 4 / 3 := by
  rw [div_pow, Real.sq_sqrt (by norm_num)]; norm_num

/-- S_D4 = τ²/q₄ = (8/3)/(47/8) = 64/141 ≈ 0.45390. -/
theorem S_D4 : (8 / 3 : ℝ) / (47 / 8) = 64 / 141 := by norm_num

/-- S_BCC = (4/3)/(15/4) = 16/45 ≈ 0.35556. -/
theorem S_BCC : (4 / 3 : ℝ) / (15 / 4) = 16 / 45 := by norm_num

/-- τ_D4 / τ_BCC = √2 exactly (Sec. II.5). -/
theorem tau_ratio : 4 / Real.sqrt 6 = Real.sqrt 2 * (2 / Real.sqrt 3) := by
  have e : (4 / Real.sqrt 6) ^ 2 = (Real.sqrt 2 * (2 / Real.sqrt 3)) ^ 2 := by
    rw [tau_D4_sq, mul_pow, tau_BCC_sq, Real.sq_sqrt (by norm_num : (0:ℝ) ≤ 2)]
    norm_num
  have p1 : (0:ℝ) ≤ 4 / Real.sqrt 6 := by positivity
  have p2 : (0:ℝ) ≤ Real.sqrt 2 * (2 / Real.sqrt 3) := by positivity
  rcases sq_eq_sq_iff_eq_or_eq_neg.mp e with h | h
  · exact h
  · -- a = -b with both nonneg forces a = b = 0, but a > 0
    have hpos : (0:ℝ) < 4 / Real.sqrt 6 := by positivity
    linarith

/-- D4 beats the 20-vector shell by exactly 73/423 ≈ 17.26% (Sec. II.5). -/
theorem selection_margin : (64 / 141 - 12 / 31 : ℝ) / (12 / 31) = 73 / 423 := by
  norm_num
