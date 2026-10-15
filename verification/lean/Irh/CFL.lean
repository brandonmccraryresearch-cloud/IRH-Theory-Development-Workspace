import Mathlib.Analysis.Real.Sqrt
import Mathlib.Tactic

/-! # The CFL stability bound (IRH v93, Sec. III.2)

Real frequencies require sin²(ωΔt/2) ≤ 1 for every k. With the spatial
sum's maximum 32 (verified numerically in the accompanying Python suite)
and the small-k matching J = M*c²/12, stability forces
  Δt ≤ (√3/2)·(a₀/c).
We formalize the algebraic derivation of the bound from those two inputs.
-/

theorem cfl_bound (M J c a0 dt : ℝ) (hM : 0 < M) (hc : 0 < c) (ha : 0 < a0)
    (hdt : 0 ≤ dt) (hJ : J = M * c ^ 2 / 12)
    (hstab : dt ^ 2 / (4 * M) * ((2 * J / a0 ^ 2) * 32) ≤ 1) :
    dt ≤ Real.sqrt 3 / 2 * a0 / c := by
  have hpos : (0:ℝ) < 4 * c ^ 2 / (3 * a0 ^ 2) := by positivity
  have e : dt ^ 2 / (4 * M) * ((2 * J / a0 ^ 2) * 32)
      = dt ^ 2 * (4 * c ^ 2 / (3 * a0 ^ 2)) := by
    rw [hJ]; field_simp; ring
  rw [e] at hstab
  -- hstab : dt^2 * (4*c^2/(3*a0^2)) ≤ 1, so dt^2 ≤ 3*a0^2/(4*c^2)
  have hle : dt ^ 2 ≤ 3 * a0 ^ 2 / (4 * c ^ 2) := by
    have h := (le_div_iff₀ hpos).mpr hstab
    rwa [one_div_div] at h
  have h2 : dt ≤ Real.sqrt (3 * a0 ^ 2 / (4 * c ^ 2)) := by
    have h := Real.sqrt_le_sqrt hle
    rwa [Real.sqrt_sq hdt] at h
  have h3 : Real.sqrt (3 * a0 ^ 2 / (4 * c ^ 2)) = Real.sqrt 3 / 2 * a0 / c := by
    rw [Real.sqrt_div (by positivity : (0:ℝ) ≤ 3 * a0 ^ 2)]
    rw [Real.sqrt_mul (by norm_num : (0:ℝ) ≤ 3), Real.sqrt_sq (by positivity : (0:ℝ) ≤ a0)]
    have h4 : (4:ℝ) * c ^ 2 = (2 * c) ^ 2 := by ring
    rw [h4, Real.sqrt_sq (by positivity : (0:ℝ) ≤ 2 * c)]
    ring
  rw [h3] at h2
  exact h2
