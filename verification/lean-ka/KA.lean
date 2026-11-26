import Mathlib.MeasureTheory.Integral.Bochner.Basic
import Mathlib.Analysis.SpecialFunctions.Trigonometric.Basic
import Mathlib.Analysis.SpecialFunctions.Exp
import Mathlib.Analysis.Calculus.Deriv.Pow
import Mathlib.Analysis.Calculus.Deriv.Inv
import Mathlib.Analysis.Calculus.Deriv.Add
import Mathlib.Tactic
/-! w-ka EXP-1314 C-1314a (G-A27): kernel-checked lemmas for the disordered-phase
Swift–Hohenberg two-point function  G(s) = 1/(r + (q - s)^2),  s = |k|^2, q = q0^2, r > 0.

  * `G_strictMonoOn`      : G is strictly increasing on [0, q].
  * `G_hasDerivAt`, `G_deriv_pos` : G'(s) = 2(q-s)/(r+(q-s)^2)^2 > 0 for s < q.
  * `stieltjes_antitone`  : any ∫ ρ(dm)/(s+m) with ρ ≥ 0 supported in [0,∞) is non-increasing on (0,∞).
  * `no_KL`               : no such representation of G exists (for all s > 0).
  * `Ghat`, `Ghat_at_pi`, `Ghat_neg`, `Ghat_zero_pos` : the closed-form reflected kernel
        Ghat(x) = π e^{-βx}(α cos αx + β sin αx) / (2αβ(α²+β²))
    is positive at x = 0 and negative at x = π/α (α, β > 0).
  * `rp_diag` / `Ghat_not_rp` : a kernel K with Σ c_i c_j K(t_i+t_j) ≥ 0 for all finite families of
    positive times has K(2t) ≥ 0 for every t > 0; hence Ghat fails it.
  NOT formalised (premise, checked in SymPy + Wolfram, grade 4D): the identity
    ∫_ℝ e^{i k x} G(|k_⊥|² + k²) dk = Ghat(α, β, x) for x > 0, with α + iβ = √(q - |k_⊥|² + i√r).
-/
namespace KA
open MeasureTheory Real

/-- Swift–Hohenberg two-point function, `q` = q0², argument `s` = |k|². -/
noncomputable def G (r q s : ℝ) : ℝ := 1 / (r + (q - s) ^ 2)

theorem G_strictMonoOn (r q : ℝ) (hr : 0 < r) : StrictMonoOn (G r q) (Set.Icc 0 q) := by
  intro s1 hs1 s2 hs2 h12
  unfold G
  have h1 : 0 ≤ q - s2 := by linarith [hs2.2]
  have h2 : q - s2 < q - s1 := by linarith
  have hsq : (q - s2) ^ 2 < (q - s1) ^ 2 := by nlinarith
  apply one_div_lt_one_div_of_lt
  · positivity
  · linarith

theorem G_hasDerivAt (r q s : ℝ) (hr : 0 < r) :
    HasDerivAt (G r q) (2 * (q - s) / (r + (q - s) ^ 2) ^ 2) s := by
  have hpos : r + (q - s) ^ 2 ≠ 0 := by positivity
  have hd : HasDerivAt (fun t => r + (q - t) ^ 2) (-(2 * (q - s))) s := by
    have h := (((hasDerivAt_id s).const_sub q).pow 2).const_add r
    convert h using 1 <;> (try simp) <;> (try ring)
  have h2 := hd.inv hpos
  unfold G
  simp only [one_div]
  convert h2 using 1 <;> (try simp) <;> (try ring)

theorem G_deriv_pos (r q s : ℝ) (hr : 0 < r) (hs : s < q) :
    0 < 2 * (q - s) / (r + (q - s) ^ 2) ^ 2 := by
  apply div_pos
  · linarith
  · positivity

/-- Any Stieltjes (Källén–Lehmann) form with a positive measure supported in `[0,∞)` is
non-increasing on `(0,∞)`. -/
theorem stieltjes_antitone (ρ : Measure ℝ) (hsupp : ∀ᵐ m ∂ρ, 0 ≤ m) {s1 s2 : ℝ}
    (h1 : 0 < s1) (h12 : s1 ≤ s2)
    (hi1 : Integrable (fun m => 1 / (s1 + m)) ρ) (hi2 : Integrable (fun m => 1 / (s2 + m)) ρ) :
    ∫ m, 1 / (s2 + m) ∂ρ ≤ ∫ m, 1 / (s1 + m) ∂ρ := by
  apply integral_mono_ae hi2 hi1
  filter_upwards [hsupp] with m hm
  apply one_div_le_one_div_of_le
  · linarith
  · linarith

/-- No Källén–Lehmann representation of the SH two-point function (r > 0, q0² > 0). -/
theorem no_KL (r q : ℝ) (hr : 0 < r) (hq : 0 < q) (ρ : Measure ℝ) (hsupp : ∀ᵐ m ∂ρ, 0 ≤ m)
    (hrep : ∀ s, 0 < s → Integrable (fun m => 1 / (s + m)) ρ ∧ G r q s = ∫ m, 1 / (s + m) ∂ρ) :
    False := by
  have hq2 : 0 < q / 2 := by linarith
  obtain ⟨i1, e1⟩ := hrep (q / 2) hq2
  obtain ⟨i2, e2⟩ := hrep q hq
  have hmono := G_strictMonoOn r q hr ⟨le_of_lt hq2, by linarith⟩ ⟨le_of_lt hq, le_refl q⟩
    (by linarith : q / 2 < q)
  have hanti := stieltjes_antitone ρ hsupp hq2 (by linarith : q / 2 ≤ q) i1 i2
  rw [← e1, ← e2] at hanti
  linarith

/-- closed-form reflected kernel at fixed transverse momentum. -/
noncomputable def Ghat (α β x : ℝ) : ℝ :=
  π * exp (-β * x) * (α * cos (α * x) + β * sin (α * x)) / (2 * α * β * (α ^ 2 + β ^ 2))

theorem Ghat_at_pi (α β : ℝ) (hα : 0 < α) :
    Ghat α β (π / α) = -(π * exp (-β * (π / α)) / (2 * β * (α ^ 2 + β ^ 2))) := by
  unfold Ghat
  have h : α * (π / α) = π := by field_simp
  rw [h, cos_pi, sin_pi]
  field_simp
  ring

theorem Ghat_neg (α β : ℝ) (hα : 0 < α) (hβ : 0 < β) : Ghat α β (π / α) < 0 := by
  rw [Ghat_at_pi α β hα]
  have : 0 < π * exp (-β * (π / α)) / (2 * β * (α ^ 2 + β ^ 2)) := by
    apply div_pos
    · exact mul_pos pi_pos (exp_pos _)
    · positivity
  linarith

theorem Ghat_zero_pos (α β : ℝ) (hα : 0 < α) (hβ : 0 < β) : 0 < Ghat α β 0 := by
  unfold Ghat
  simp only [mul_zero, cos_zero, sin_zero, exp_zero, mul_one, add_zero]
  apply div_pos
  · nlinarith [pi_pos]
  · positivity

/-- Reflection-positivity form on the half line: diagonal entries are nonnegative. -/
theorem rp_diag (K : ℝ → ℝ)
    (hRP : ∀ (n : ℕ) (t : Fin n → ℝ) (c : Fin n → ℝ), (∀ i, 0 < t i) →
      0 ≤ ∑ i, ∑ j, c i * c j * K (t i + t j)) :
    ∀ t : ℝ, 0 < t → 0 ≤ K (2 * t) := by
  intro t ht
  have := hRP 1 (fun _ => t) (fun _ => 1) (fun _ => ht)
  simpa [two_mul] using this

theorem Ghat_not_rp (α β : ℝ) (hα : 0 < α) (hβ : 0 < β) :
    ¬ (∀ (n : ℕ) (t : Fin n → ℝ) (c : Fin n → ℝ), (∀ i, 0 < t i) →
      0 ≤ ∑ i, ∑ j, c i * c j * Ghat α β (t i + t j)) := by
  intro hRP
  have h := rp_diag (Ghat α β) hRP (π / α / 2) (by positivity)
  have e : 2 * (π / α / 2) = π / α := by ring
  rw [e] at h
  linarith [Ghat_neg α β hα hβ]

end KA

#print axioms KA.G_strictMonoOn
#print axioms KA.G_hasDerivAt
#print axioms KA.G_deriv_pos
#print axioms KA.stieltjes_antitone
#print axioms KA.no_KL
#print axioms KA.Ghat_at_pi
#print axioms KA.Ghat_neg
#print axioms KA.Ghat_zero_pos
#print axioms KA.rp_diag
#print axioms KA.Ghat_not_rp
