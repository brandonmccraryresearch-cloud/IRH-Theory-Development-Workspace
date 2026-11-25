import GB6Counts
import GB6CountsD4Q
import GB6CountsA4Q
import GB6Grid
import GB6Real
import GB6Analytic
import GB6HJ6
/-! v-gb6 (verifier) statement-audit supplement. Printed-statement restatements in the
verifier's own words, each proved only from the author's kernel theorems, plus the
dual-shell half of the C11 isoduality fingerprint (v94 l.185), which the author's C11 omits. -/
namespace GB6V
open GB6

-- R-G: the printed D4 quadruple count (v94 l.277, l.372; WS-C task1 l.101) is 3384
theorem RG_Q : cntQ D4 = 3384 := C01_D4_Q

-- C11 dual side: P4 = 2·(minimal vectors of D4*) ; |h|^2 = 4, so cos = dot/4
theorem V11_dual_norm : ∀ a ∈ P4, normSq a = 4 := by decide +kernel
theorem V11_dual_range : ∀ a ∈ P4, ∀ b ∈ P4, a ≠ b → dot a b ∈ [-4, -2, 0, 2] := by decide +kernel
theorem V11_dual_attained : ∀ x ∈ ([-4, -2, 0, 2] : List Int),
    ∃ a ∈ P4, ∃ b ∈ P4, a ≠ b ∧ dot a b = x := by decide +kernel
theorem V11_dual_nodup : P4.Nodup := by decide +kernel
-- dual shell carries the same triad content (shell-model robustness for T)
theorem V_dual_T : cntT P4 = 192 := by decide +kernel

-- non-vacuity of hypotheses in C18 (an instance satisfying all hypotheses exists)
theorem V18_nonvacuous : ∃ r u v τ q B : ℝ, v ≠ 0 ∧ q ≠ 0 ∧ B ≠ 0 ∧
    r / 2 * B ^ 2 - u / 3 * τ * B ^ 3 + v / 4 * q * B ^ 4 = 0 ∧
    r * B - u * τ * B ^ 2 + v * q * B ^ 3 = 0 :=
  ⟨2 / 9, 1, 1, 1, 1, 2 / 3, by norm_num, by norm_num, by norm_num, by norm_num, by norm_num⟩

end GB6V
#print axioms GB6V.RG_Q
#print axioms GB6V.V11_dual_norm
#print axioms GB6V.V11_dual_range
#print axioms GB6V.V11_dual_attained
#print axioms GB6V.V11_dual_nodup
#print axioms GB6V.V_dual_T
#print axioms GB6V.V18_nonvacuous
#print axioms GB6.C01_D4_N
#print axioms GB6.C01_D4_T
#print axioms GB6.C01_D4_Q
#print axioms GB6.C01_D4_complete
#print axioms GB6.C02_D4_S
#print axioms GB6.C02_D4_tau
#print axioms GB6.C03_A4r_Q
#print axioms GB6.C03_S
#print axioms GB6.C04_S
#print axioms GB6.C04_tau
#print axioms GB6.C05_FCC_Q
#print axioms GB6.C05_SC_Q
#print axioms GB6.C06_Z4_Q
#print axioms GB6.C06_A4sm_Q
#print axioms GB6.C07_ratio
#print axioms GB6.C07_margin
#print axioms GB6.C07_D4_wins
#print axioms GB6.C08_tau_ratio
#print axioms GB6.C09_decimals
#print axioms GB6.C10_partners
#print axioms GB6.C10_T_eq_partner_pairs
#print axioms GB6.C11_fingerprint_range
#print axioms GB6.C12_iso4
#print axioms GB6.C13_D4s_T
#print axioms GB6.C14_C7_N
#print axioms GB6.C14_C7_T
#print axioms GB6.C14_C7_complete
#print axioms GB6.C14_penalties
#print axioms GB6.C15_unordered
#print axioms GB6.C16_grid_count
#print axioms GB6.C16_Psi_max_count
#print axioms GB6.C17_H
#print axioms GB6.C18_Bstar_rc
#print axioms GB6.C19_Astar
#print axioms GB6.C19_Fexc
#print axioms GB6.C19_edge
#print axioms GB6.C19_detuned
#print axioms GB6.C20_a0_dt
#print axioms GB6.C21_sin2
#print axioms GB6.C21_values
#print axioms GB6.C22_grid25
#print axioms GB6.C23_lattice_point
#print axioms GB6.C23_Z4_point
#print axioms GB6.C23_deep_hole
