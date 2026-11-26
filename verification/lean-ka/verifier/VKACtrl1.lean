import KA
-- must FAIL: checklist R-O sign (+) as an equality
open Real
example (α β : ℝ) (hα : 0 < α) (hβ : 0 < β) :
    KA.Ghat α β (π / α) = π * exp (-π * β / α) / (2 * β * (α ^ 2 + β ^ 2)) := by
  rw [KA.Ghat_at_pi α β hα]; field_simp; ring_nf
