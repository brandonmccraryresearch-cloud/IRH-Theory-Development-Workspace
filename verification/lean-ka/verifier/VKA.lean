import KA
/-! v-ka (verifier) EXP-1314: statement audit of KA by exact restatement, plus an
independent from-scratch kernel proof of the sign lemma and the 1x1 RP obstruction. -/
open MeasureTheory Real

namespace VKA
-- (S1) the definitions are literally the stated objects
example (r q s : ℝ) : KA.G r q s = 1 / (r + (q - s) ^ 2) := rfl
example (α β x : ℝ) : KA.Ghat α β x =
    π * exp (-β * x) * (α * cos (α * x) + β * sin (α * x)) / (2 * α * β * (α ^ 2 + β ^ 2)) := rfl
-- (S2) exact restatement of the theorem types (fails to compile if KA states something else)
example : ∀ (r q : ℝ), 0 < r → 0 < q → ∀ (ρ : Measure ℝ), (∀ᵐ m ∂ρ, 0 ≤ m) →
    (∀ s, 0 < s → Integrable (fun m => 1 / (s + m)) ρ ∧ KA.G r q s = ∫ m, 1 / (s + m) ∂ρ) → False :=
  fun r q hr hq ρ hs hrep => KA.no_KL r q hr hq ρ hs hrep
example : ∀ (r q s : ℝ), 0 < r → s < q → 0 < deriv (KA.G r q) s := by
  intro r q s hr hs
  rw [(KA.G_hasDerivAt r q s hr).deriv]; exact KA.G_deriv_pos r q s hr hs
example : ∀ (α β : ℝ), 0 < α → 0 < β → KA.Ghat α β (π / α) < 0 := KA.Ghat_neg

-- (I1) independent own kernel: K(x) = e^{-βx}(α cos αx + β sin αx) (positive prefactor dropped)
noncomputable def K (α β x : ℝ) : ℝ := exp (-β * x) * (α * cos (α * x) + β * sin (α * x))

theorem K_at_pi (α β : ℝ) (hα : 0 < α) : K α β (π / α) = -(α * exp (-β * (π / α))) := by
  unfold K
  rw [show α * (π / α) = π by field_simp, cos_pi, sin_pi]; ring

theorem K_neg (α β : ℝ) (hα : 0 < α) : K α β (π / α) < 0 := by
  rw [K_at_pi α β hα]; have := exp_pos (-β * (π / α)); nlinarith

theorem K_zero (α β : ℝ) : K α β 0 = α := by unfold K; simp

/-- KA.Ghat is a POSITIVE multiple of my K (so its sign is K's sign). -/
theorem Ghat_eq (α β x : ℝ) (hα : 0 < α) (hβ : 0 < β) :
    KA.Ghat α β x = (π / (2 * α * β * (α ^ 2 + β ^ 2))) * K α β x := by
  unfold KA.Ghat K; field_simp

/-- my own 1x1 obstruction, stated for complex-free real families on positive times -/
theorem K_not_rp (α β : ℝ) (hα : 0 < α) :
    ¬ (∀ t c : ℝ, 0 < t → 0 ≤ c * c * K α β (t + t)) := by
  intro h
  have := h (π / α / 2) 1 (by positivity)
  rw [show π / α / 2 + π / α / 2 = π / α by ring] at this
  linarith [K_neg α β hα]

/-- R-O as written in the checklist (positive sign) is the NEGATION of what holds. -/
theorem RO_sign (α β : ℝ) (hα : 0 < α) (hβ : 0 < β) :
    KA.Ghat α β (π / α) ≠ π * exp (-π * β / α) / (2 * β * (α ^ 2 + β ^ 2)) := by
  intro h
  have hn := KA.Ghat_neg α β hα hβ
  have : 0 < π * exp (-π * β / α) / (2 * β * (α ^ 2 + β ^ 2)) := by
    apply div_pos (mul_pos pi_pos (exp_pos _)); positivity
  linarith
end VKA
#print axioms VKA.K_neg
#print axioms VKA.Ghat_eq
#print axioms VKA.K_not_rp
#print axioms VKA.RO_sign
#print axioms KA.no_KL
#print axioms KA.Ghat_not_rp
#print axioms KA.stieltjes_antitone
#print axioms KA.G_deriv_pos
#print axioms KA.G_hasDerivAt
#print axioms KA.G_strictMonoOn
#print axioms KA.Ghat_at_pi
#print axioms KA.Ghat_neg
#print axioms KA.Ghat_zero_pos
#print axioms KA.rp_diag
