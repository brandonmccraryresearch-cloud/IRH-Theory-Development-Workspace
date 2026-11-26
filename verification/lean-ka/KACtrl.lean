import KA
/-! negative control: the reflected kernel at x = π/α is claimed nonnegative (false); must fail. -/
open Real
example (α β : ℝ) (hα : 0 < α) (hβ : 0 < β) : 0 ≤ KA.Ghat α β (π / α) := by
  rw [KA.Ghat_at_pi α β hα]
  positivity
