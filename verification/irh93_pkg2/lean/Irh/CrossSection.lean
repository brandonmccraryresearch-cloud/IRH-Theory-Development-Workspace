import Mathlib.Tactic

/-! # D₄ cross-section is FCC (IRH v93, Sec. II.10)

D₄ = {x ∈ ℤ⁴ : x₀+x₁+x₂+x₃ even}; intersecting with x₃ = 0 gives
{x₀+x₁+x₂ even}, i.e. D₃, the FCC lattice.
-/

def D4lat : Set (Fin 4 → ℤ) := {x | Even (x 0 + x 1 + x 2 + x 3)}

theorem cross_section :
    {x : Fin 4 → ℤ | x ∈ D4lat ∧ x 3 = 0} =
      {x : Fin 4 → ℤ | x 3 = 0 ∧ Even (x 0 + x 1 + x 2)} := by
  ext x
  simp only [Set.mem_setOf_eq, D4lat]
  constructor
  · rintro ⟨he, h3⟩
    refine ⟨h3, ?_⟩
    rw [h3] at he
    simpa using he
  · rintro ⟨h3, he⟩
    refine ⟨?_, h3⟩
    rw [h3]
    simpa using he
