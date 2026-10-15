import Mathlib.Tactic

/-! # Baseline tension tunes the triad coupling (IRH v93, Sec. II.7)

Expanding ψ = ψ̄ + Aσ in F, the A³ coefficient is
  -(T/3)·(u - 3vψ̄),
i.e. u_eff = u - 3vψ̄. We verify the coefficient identity.
-/

theorem u_eff_identity (T u v ψbar : ℝ) :
    -(T / 3) * (u - 3 * v * ψbar) = -u * T / 3 + v * ψbar * T := by
  ring
