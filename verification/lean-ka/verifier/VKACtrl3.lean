import KA
-- must FAIL: sign at x=0 reversed
example (α β : ℝ) (hα : 0 < α) (hβ : 0 < β) : KA.Ghat α β 0 < 0 := by
  unfold KA.Ghat; simp; nlinarith [Real.pi_pos]
