import KA
-- must FAIL: G antitone (Stieltjes-like) on [0,q]
example (r q : ℝ) (hr : 0 < r) (hq : 0 < q) : KA.G r q q ≤ KA.G r q (q/2) := by
  unfold KA.G; apply one_div_le_one_div_of_le <;> nlinarith
