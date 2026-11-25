import GB6Counts
import GB6CountsD4Q
import GB6CountsA4Q
import Mathlib.Analysis.SpecialFunctions.Trigonometric.Basic
import Mathlib.Analysis.Real.Pi.Bounds
import Mathlib.Analysis.SpecialFunctions.Pow.Real
import Mathlib.Tactic
/-! w-gb6 EXP-1304: exact arithmetic / real claims C02–C09, C12, C14 (penalties), C18–C22.
Counts enter only through the kernel-proved count theorems. -/
namespace GB6
open Real

/-- τ² = T²/N³, q4 = Q/N², S = τ²/q4 (exact, in ℚ) -/
def tau2 (N T : Nat) : ℚ := (T : ℚ) ^ 2 / (N : ℚ) ^ 3
def q4 (N Q : Nat) : ℚ := (Q : ℚ) / (N : ℚ) ^ 2
def Sval (N T Q : Nat) : ℚ := tau2 N T / q4 N Q
/-- τ = T / N^{3/2} (real, rpow) -/
noncomputable def tauR (N T : Nat) : ℝ := (T : ℝ) / (N : ℝ) ^ ((3 : ℝ) / 2)

lemma rpow32 (x : ℝ) (hx : 0 < x) : x ^ ((3 : ℝ) / 2) = x * √x := by
  rw [show (3 : ℝ) / 2 = 1 + 1 / 2 by norm_num, Real.rpow_add hx, Real.rpow_one, Real.sqrt_eq_rpow]

-- C02 D4
theorem C02_D4_tau2 : tau2 (cntN D4) (cntT D4) = 8 / 3 := by
  rw [C01_D4_N, C01_D4_T]; unfold tau2; norm_num
theorem C02_D4_q4 : q4 (cntN D4) (cntQ D4) = 47 / 8 := by
  rw [C01_D4_N, C01_D4_Q]; unfold q4; norm_num
theorem C02_D4_S : Sval (cntN D4) (cntT D4) (cntQ D4) = 64 / 141 := by
  unfold Sval; rw [C02_D4_tau2, C02_D4_q4]; norm_num
theorem C02_D4_tau : tauR (cntN D4) (cntT D4) = 4 / √6 := by
  rw [C01_D4_N, C01_D4_T]; unfold tauR
  have h24 : √(24 : ℝ) = 2 * √6 := by
    rw [show (24 : ℝ) = 2 ^ 2 * 6 by norm_num, Real.sqrt_mul (by norm_num), Real.sqrt_sq (by norm_num)]
  have h6 : 0 < √(6 : ℝ) := Real.sqrt_pos.mpr (by norm_num)
  push_cast
  rw [rpow32 24 (by norm_num), h24]
  field_simp
  try ring

-- C03 A4* row (20,120,1860)
theorem C03_tau2 : tau2 (cntN A4r) (cntT A4r) = 9 / 5 := by
  rw [C03_A4r_N, C03_A4r_T]; unfold tau2; norm_num
theorem C03_q4 : q4 (cntN A4r) (cntQ A4r) = 93 / 20 := by
  rw [C03_A4r_N, C03_A4r_Q]; unfold q4; norm_num
theorem C03_S : Sval (cntN A4r) (cntT A4r) (cntQ A4r) = 12 / 31 := by
  unfold Sval; rw [C03_tau2, C03_q4]; norm_num

-- C04 BCC row (12,48,540)
theorem C04_tau2 : tau2 (cntN BCCr) (cntT BCCr) = 4 / 3 := by
  rw [C04_BCC_N, C04_BCC_T]; unfold tau2; norm_num
theorem C04_q4 : q4 (cntN BCCr) (cntQ BCCr) = 15 / 4 := by
  rw [C04_BCC_N, C04_BCC_Q]; unfold q4; norm_num
theorem C04_S : Sval (cntN BCCr) (cntT BCCr) (cntQ BCCr) = 16 / 45 := by
  unfold Sval; rw [C04_tau2, C04_q4]; norm_num
theorem C04_tau : tauR (cntN BCCr) (cntT BCCr) = 2 / √3 := by
  rw [C04_BCC_N, C04_BCC_T]; unfold tauR
  have h12 : √(12 : ℝ) = 2 * √3 := by
    rw [show (12 : ℝ) = 2 ^ 2 * 3 by norm_num, Real.sqrt_mul (by norm_num), Real.sqrt_sq (by norm_num)]
  have h3 : 0 < √(3 : ℝ) := Real.sqrt_pos.mpr (by norm_num)
  push_cast
  rw [rpow32 12 (by norm_num), h12]
  field_simp
  try ring

-- C05 FCC q4 = 27/8 (T=0 ⇒ S=0); SC q4 = 5/2
theorem C05_FCC_q4 : q4 (cntN FCCr) (cntQ FCCr) = 27 / 8 := by
  rw [C05_FCC_N, C05_FCC_Q]; unfold q4; norm_num
theorem C05_FCC_S : Sval (cntN FCCr) (cntT FCCr) (cntQ FCCr) = 0 := by
  unfold Sval tau2; rw [C05_FCC_T]; norm_num
theorem C05_SC_q4 : q4 (cntN SC) (cntQ SC) = 5 / 2 := by
  rw [C05_SC_N, C05_SC_Q]; unfold q4; norm_num
theorem C05_SC_S : Sval (cntN SC) (cntT SC) (cntQ SC) = 0 := by
  unfold Sval tau2; rw [C05_SC_T]; norm_num

-- C06 Z4 q4 = 21/8, A4 row q4 = 27/10, S = 0
theorem C06_Z4_q4 : q4 (cntN Z4) (cntQ Z4) = 21 / 8 := by
  rw [C06_Z4_N, C06_Z4_Q]; unfold q4; norm_num
theorem C06_Z4_S : Sval (cntN Z4) (cntT Z4) (cntQ Z4) = 0 := by
  unfold Sval tau2; rw [C06_Z4_T]; norm_num
theorem C06_A4_q4 : q4 (cntN A4sm) (cntQ A4sm) = 27 / 10 := by
  rw [C06_A4sm_N, C06_A4sm_Q]; unfold q4; norm_num
theorem C06_A4_S : Sval (cntN A4sm) (cntT A4sm) (cntQ A4sm) = 0 := by
  unfold Sval tau2; rw [C06_A4sm_T]; norm_num

-- C07 ratio and margin
theorem C07_ratio : Sval (cntN D4) (cntT D4) (cntQ D4) / Sval (cntN A4r) (cntT A4r) (cntQ A4r) = 496 / 423 := by
  rw [C02_D4_S, C03_S]; norm_num
theorem C07_margin : Sval (cntN D4) (cntT D4) (cntQ D4) / Sval (cntN A4r) (cntT A4r) (cntQ A4r) - 1 = 73 / 423 := by
  rw [C07_ratio]; norm_num
theorem C07_D4_wins : Sval (cntN A4r) (cntT A4r) (cntQ A4r) < Sval (cntN D4) (cntT D4) (cntQ D4) ∧
    Sval (cntN BCCr) (cntT BCCr) (cntQ BCCr) < Sval (cntN D4) (cntT D4) (cntQ D4) := by
  rw [C02_D4_S, C03_S, C04_S]; norm_num

-- C08 τ_D4 / τ_BCC = √2
theorem C08_tau_ratio : tauR (cntN D4) (cntT D4) / tauR (cntN BCCr) (cntT BCCr) = √2 := by
  rw [C02_D4_tau, C04_tau]
  have h3 : (0 : ℝ) < √3 := Real.sqrt_pos.mpr (by norm_num)
  have h6 : (0 : ℝ) < √6 := Real.sqrt_pos.mpr (by norm_num)
  have hpos : (0 : ℝ) ≤ 4 / √6 / (2 / √3) := by positivity
  have hsq : (4 / √6 / (2 / √3)) ^ 2 = (2 : ℝ) := by
    rw [div_pow, div_pow, div_pow, Real.sq_sqrt (by norm_num), Real.sq_sqrt (by norm_num)]; norm_num
  calc 4 / √6 / (2 / √3) = √((4 / √6 / (2 / √3)) ^ 2) := (Real.sqrt_sq hpos).symm
    _ = √2 := by rw [hsq]

/-- helper: rational bounds on a square root -/
lemma sqrt_bounds (y lo hi : ℝ) (hlo : 0 ≤ lo) (h1 : lo ^ 2 < y) (h2 : y < hi ^ 2) (hhi : 0 ≤ hi) :
    lo < √y ∧ √y < hi := by
  have hy : 0 ≤ y := by nlinarith
  have hs := Real.sq_sqrt hy
  have hn := Real.sqrt_nonneg y
  constructor
  · by_contra h; push_neg at h; nlinarith
  · by_contra h; push_neg at h; nlinarith

-- C09 printed decimals (|x - printed| ≤ half unit of last printed digit)
theorem C09_decimals :
    |(64 / 141 : ℝ) - 0.453901| < 0.0000005 ∧ |(12 / 31 : ℝ) - 0.387097| < 0.0000005 ∧
    |(16 / 45 : ℝ) - 0.355556| < 0.0000005 ∧ |(16 / 45 : ℝ) - 0.35556| < 0.000005 ∧
    |(73 / 423 : ℝ) * 100 - 17.26| < 0.005 ∧ |(2 / √3 : ℝ) - 1.1547| < 0.00005 := by
  obtain ⟨l3, h3⟩ := sqrt_bounds 3 1.7320508 1.7320509 (by norm_num) (by norm_num) (by norm_num) (by norm_num)
  refine ⟨?_, ?_, ?_, ?_, ?_, ?_⟩
  · rw [abs_lt]; constructor <;> norm_num
  · rw [abs_lt]; constructor <;> norm_num
  · rw [abs_lt]; constructor <;> norm_num
  · rw [abs_lt]; constructor <;> norm_num
  · rw [abs_lt]; constructor <;> norm_num
  · have hp : (0 : ℝ) < √3 := by linarith
    rw [abs_lt]; constructor
    · rw [lt_sub_iff_add_lt, lt_div_iff₀ hp]; nlinarith
    · rw [sub_lt_iff_lt_add, div_lt_iff₀ hp]; nlinarith

/-- D4 = the explicit list of the 24 roots ±e_i±e_j (kernel-checked) -/
theorem D4_eq_lit : D4 = [[-1, -1, 0, 0], [-1, 0, -1, 0], [-1, 0, 0, -1], [-1, 0, 0, 1], [-1, 0, 1, 0], [-1, 1, 0, 0], [0, -1, -1, 0], [0, -1, 0, -1], [0, -1, 0, 1], [0, -1, 1, 0], [0, 0, -1, -1], [0, 0, -1, 1], [0, 0, 1, -1], [0, 0, 1, 1], [0, 1, -1, 0], [0, 1, 0, -1], [0, 1, 0, 1], [0, 1, 1, 0], [1, -1, 0, 0], [1, 0, -1, 0], [1, 0, 0, -1], [1, 0, 0, 1], [1, 0, 1, 0], [1, 1, 0, 0]] := by decide +kernel

/-- real dot product of a real 4-vector with an integer vector -/
def dotIR : List ℝ → V → ℝ
  | a :: as, b :: bs => a * (b : ℝ) + dotIR as bs
  | _, _ => 0

-- C12 isotropy through fourth order
theorem C12_iso2 (k1 k2 k3 k4 : ℝ) :
    (D4.map fun α => (dotIR [k1, k2, k3, k4] α) ^ 2).sum = 12 * (k1 ^ 2 + k2 ^ 2 + k3 ^ 2 + k4 ^ 2) := by
  rw [D4_eq_lit]; simp [dotIR]; ring
theorem C12_iso4 (k1 k2 k3 k4 : ℝ) :
    (D4.map fun α => (dotIR [k1, k2, k3, k4] α) ^ 4).sum = 12 * (k1 ^ 2 + k2 ^ 2 + k3 ^ 2 + k4 ^ 2) ^ 2 := by
  rw [D4_eq_lit]; simp [dotIR]; ring

-- C14 penalties and mode ratio
theorem C14_penalties : ((7.5 : ℝ) - 8) ^ 2 = 0.25 ∧ ((7.5 : ℝ) - 7) ^ 2 = 0.25 ∧
    ((cntN C7 : ℚ) / cntN D4s = 8 / 3) ∧ |(8 / 3 : ℝ) - 2.7| < 0.05 := by
  refine ⟨by norm_num, by norm_num, ?_, ?_⟩
  · rw [C14_C7_N, C13_D4s_N]; norm_num
  · rw [abs_lt]; constructor <;> norm_num

-- C18 first-order transition algebra (v94 l.221–234)
theorem C18_Bstar_rc (r u v τ q B : ℝ) (hv : v ≠ 0) (hq : q ≠ 0) (hB : B ≠ 0)
    (hF : r / 2 * B ^ 2 - u / 3 * τ * B ^ 3 + v / 4 * q * B ^ 4 = 0)
    (hF' : r * B - u * τ * B ^ 2 + v * q * B ^ 3 = 0) :
    B = 2 * u * τ / (3 * v * q) ∧ r = 2 / 9 * (u ^ 2 * τ ^ 2 / (v * q)) := by
  have e1 : B * (r - u * τ * B + v * q * B ^ 2) = 0 := by linear_combination hF'
  have h1 : r - u * τ * B + v * q * B ^ 2 = 0 := (mul_eq_zero.mp e1).resolve_left hB
  have e2 : B ^ 2 * (r / 2 - u * τ * B / 3 + v * q * B ^ 2 / 4) = 0 := by linear_combination hF
  have h2 : r / 2 - u * τ * B / 3 + v * q * B ^ 2 / 4 = 0 :=
    (mul_eq_zero.mp e2).resolve_left (pow_ne_zero 2 hB)
  have e3 : B * (v * q * B / 2 - u * τ / 3) = 0 := by linear_combination h1 - 2 * h2
  have h3 : v * q * B / 2 - u * τ / 3 = 0 := (mul_eq_zero.mp e3).resolve_left hB
  have hB3 : 3 * v * q * B - 2 * u * τ = 0 := by linear_combination 6 * h3
  have h9 : 9 * v * q * r - 2 * u ^ 2 * τ ^ 2 = 0 := by
    linear_combination (9 * v * q) * h1 - (3 * v * q * B - u * τ) * hB3
  have hne3 : 3 * v * q ≠ 0 := mul_ne_zero (mul_ne_zero (by norm_num) hv) hq
  have hne : v * q ≠ 0 := mul_ne_zero hv hq
  constructor
  · rw [eq_div_iff hne3]; linear_combination hB3
  · rw [mul_div_assoc', eq_div_iff hne]; linear_combination h9 / 9
/-- non-vacuity / converse: B*, r_c solve F = 0 and F' = 0 -/
theorem C18_converse (u v τ q : ℝ) (hv : v ≠ 0) (hq : q ≠ 0) :
    (2 / 9 * (u ^ 2 * τ ^ 2 / (v * q))) / 2 * (2 * u * τ / (3 * v * q)) ^ 2
      - u / 3 * τ * (2 * u * τ / (3 * v * q)) ^ 3 + v / 4 * q * (2 * u * τ / (3 * v * q)) ^ 4 = 0 ∧
    (2 / 9 * (u ^ 2 * τ ^ 2 / (v * q))) * (2 * u * τ / (3 * v * q))
      - u * τ * (2 * u * τ / (3 * v * q)) ^ 2 + v * q * (2 * u * τ / (3 * v * q)) ^ 3 = 0 := by
  constructor
  · field_simp; ring
  · field_simp; ring
/-- r_c is (2u²/(9v)) · S, so ordering by r_c = ordering by S for fixed u, v > 0 -/
theorem C18_rc_prop_S (u v τ q : ℝ) : 2 / 9 * (u ^ 2 * τ ^ 2 / (v * q)) = (2 * u ^ 2 / (9 * v)) * (τ ^ 2 / q) := by
  ring

-- C19 one-mode free energy (WS-C task1 l.113–120, task2 l.57–61): r=-0.35, u=v=1, ψ̄=-0.18, N,T,Q from D4
noncomputable section
def rr : ℝ := -35 / 100
def ps : ℝ := -18 / 100
def reffAt (rsh : ℝ) : ℝ := rsh - 2 * 1 * ps + 3 * 1 * ps ^ 2
def ueff : ℝ := 1 - 3 * 1 * ps
def NN : ℝ := (cntN D4 : ℝ)
def TT : ℝ := (cntT D4 : ℝ)
def QQ : ℝ := (cntQ D4 : ℝ)
def Disc (rsh : ℝ) : ℝ := (TT * ueff) ^ 2 - 4 * 1 * QQ * NN * reffAt rsh
def Fmod (rsh A : ℝ) : ℝ := NN / 2 * reffAt rsh * A ^ 2 - TT / 3 * ueff * A ^ 3 + 1 * QQ / 4 * A ^ 4
def Astar : ℝ := (TT * ueff + √(Disc rr)) / (2 * 1 * QQ)
def Asmall : ℝ := (TT * ueff - √(Disc rr)) / (2 * 1 * QQ)
def rcEdge : ℝ := (TT * ueff) ^ 2 / (4 * 1 * QQ * NN)
end

lemma NN_v : NN = 24 := by simp [NN, C01_D4_N]
lemma TT_v : TT = 192 := by simp [TT, C01_D4_T]
lemma QQ_v : QQ = 3384 := by simp [QQ, C01_D4_Q]
lemma ueff_v : ueff = 77 / 50 := by unfold ueff ps; norm_num
lemma reff_v : reffAt rr = 67 / 625 := by unfold reffAt rr ps; norm_num

theorem C19_reff : reffAt rr = 0.1072 ∧ ueff = 1.54 := by
  rw [reff_v, ueff_v]; constructor <;> norm_num
/-- Z3 claim r_eff(ψ̄=0) < 0: with ψ̄ = 0, r_eff = r = -0.35 -/
theorem C19_reff_psi0 : rr - 2 * 1 * 0 + 3 * 1 * (0 : ℝ) ^ 2 < 0 := by unfold rr; norm_num

theorem C19_disc : Disc rr = 32875776 / 625 := by
  unfold Disc; rw [NN_v, TT_v, QQ_v, ueff_v, reff_v]; norm_num

theorem C19_Astar :
    (QQ * Astar ^ 2 - TT * ueff * Astar + NN * reffAt rr = 0) ∧
    (QQ * Asmall ^ 2 - TT * ueff * Asmall + NN * reffAt rr = 0) ∧
    0 < Asmall ∧ Asmall < Astar ∧ |Astar - 0.0775753| < 0.00000005 := by
  have hD := C19_disc
  have hs : √(Disc rr) ^ 2 = 32875776 / 625 := by rw [Real.sq_sqrt (by rw [hD]; norm_num), hD]
  obtain ⟨l, h⟩ := sqrt_bounds (Disc rr) (2 * 3384 * (0.0775753 - 0.00000005) - 192 * 1.54)
    (2 * 3384 * (0.0775753 + 0.00000005) - 192 * 1.54) (by norm_num) (by rw [hD]; norm_num)
    (by rw [hD]; norm_num) (by norm_num)
  unfold Astar Asmall
  rw [NN_v, TT_v, QQ_v, ueff_v, reff_v]
  generalize √(Disc rr) = s at hs l h
  refine ⟨?_, ?_, ?_, ?_, ?_⟩
  · linear_combination (1 / 13536) * hs
  · linear_combination (1 / 13536) * hs
  · apply div_pos _ (by norm_num); norm_num at h ⊢; linarith
  · rw [div_lt_div_iff_of_pos_right (by norm_num)]; norm_num at l ⊢; linarith
  · rw [abs_lt]; constructor
    · rw [lt_sub_iff_add_lt, lt_div_iff₀ (by norm_num)]; norm_num at l ⊢; linarith
    · rw [sub_lt_iff_lt_add, div_lt_iff₀ (by norm_num)]; norm_num at h ⊢; linarith

theorem C19_Fexc : |Fmod rr Astar - (-0.0076323)| < 0.00000005 := by
  have hD := C19_disc
  have hs : √(Disc rr) ^ 2 = 32875776 / 625 := by rw [Real.sq_sqrt (by rw [hD]; norm_num), hD]
  obtain ⟨l, h⟩ := sqrt_bounds (Disc rr) 229.3496 229.3497 (by norm_num) (by rw [hD]; norm_num)
    (by rw [hD]; norm_num) (by norm_num)
  -- exact reduction F(A*) = p + q·√D (p, q from support_quot.py; certificate checked by ring)
  have hred : Fmod rr Astar = -4157572102 / 1095008203125 - 2197426 / 131400984375 * √(Disc rr) := by
    unfold Fmod Astar; rw [NN_v, TT_v, QQ_v, ueff_v, reff_v]
    generalize √(Disc rr) = s at hs
    linear_combination (s ^ 2 / 2480110534656 + 77 * s / 484396588800 - 14269 / 672773040000) * hs
  rw [hred, abs_lt]; constructor <;> nlinarith

/-- ordered-branch edge: branch exists iff (T u_eff)² ≥ 4vQN r_eff; with r_shell = r + δ²,
δ = q0² − 8: r_eff = δ² + 0.1072, edge rc = (T u_eff)²/(4QN) ≈ 0.2691, |δ| ≤ √(rc − 0.1072) ≈ 0.4024 -/
theorem C19_edge :
    (∀ δ : ℝ, (0 ≤ Disc (rr + δ ^ 2) ↔ reffAt (rr + δ ^ 2) ≤ rcEdge)) ∧
    (∀ δ : ℝ, reffAt (rr + δ ^ 2) = δ ^ 2 + 1072 / 10000) ∧
    |rcEdge - 0.2691| < 0.00005 ∧ |√(rcEdge - 0.1072) - 0.4024| < 0.00005 := by
  have hrc : rcEdge = 23716 / 88125 := by unfold rcEdge; rw [NN_v, TT_v, QQ_v, ueff_v]; norm_num
  refine ⟨?_, ?_, ?_, ?_⟩
  · intro δ; unfold Disc rcEdge; rw [NN_v, TT_v, QQ_v]
    rw [le_div_iff₀ (by norm_num)]; constructor <;> intro h <;> linarith
  · intro δ; unfold reffAt rr ps; ring
  · rw [hrc, abs_lt]; constructor <;> norm_num
  · rw [hrc]
    obtain ⟨l, h⟩ := sqrt_bounds (23716 / 88125 - 0.1072) 0.40235 0.40245 (by norm_num) (by norm_num)
      (by norm_num) (by norm_num)
    rw [abs_lt]; constructor <;> linarith

/-- q0² = 7.5 (δ = −0.5): r_shell = −0.10, r_eff = 0.3572, no real stationary amplitude -/
theorem C19_detuned : rr + (7.5 - 8) ^ 2 = -0.10 ∧ reffAt (rr + (7.5 - 8) ^ 2) = 0.3572 ∧
    Disc (rr + (7.5 - 8) ^ 2) < 0 ∧
    ∀ A : ℝ, QQ * A ^ 2 - TT * ueff * A + NN * reffAt (rr + (7.5 - 8) ^ 2) ≠ 0 := by
  have hr : reffAt (rr + (7.5 - 8) ^ 2) = 893 / 2500 := by unfold reffAt rr ps; norm_num
  refine ⟨by unfold rr; norm_num, by rw [hr]; norm_num, ?_, ?_⟩
  · unfold Disc; rw [NN_v, TT_v, QQ_v, ueff_v, hr]; norm_num
  · intro A; rw [NN_v, TT_v, QQ_v, ueff_v, hr]; intro h
    nlinarith [sq_nonneg (A - 192 * (77 / 50) / (2 * 3384))]

-- C20 a0 = 2π/√8 = 2.221441, dt_max = (√3/2) a0 / c = 1.923825 (c = 1), ratios
theorem C20_a0_dt :
    |2 * π / √8 - 2.221441| < 0.0000005 ∧ |√3 / 2 * (2 * π / √8) / 1 - 1.923825| < 0.0000005 ∧
    (48 < (√3 / 2 * (2 * π / √8)) / 0.04 ∧ (√3 / 2 * (2 * π / √8)) / 0.04 < 49) ∧
    |(√3 / 2 * (2 * π / √8)) / 0.005 - 385| < 0.5 ∧
    (96 < (√3 / 2 * (2 * π / √8)) / 0.02 ∧ (√3 / 2 * (2 * π / √8)) / 0.02 < 96.5) := by
  have p1 := Real.pi_gt_d20
  have p2 := Real.pi_lt_d20
  obtain ⟨l8, h8⟩ := sqrt_bounds 8 2.8284271247 2.8284271248 (by norm_num) (by norm_num) (by norm_num) (by norm_num)
  have h8p : (0 : ℝ) < √8 := by linarith
  have h3p : (0 : ℝ) < √3 := Real.sqrt_pos.mpr (by norm_num)
  have hq0 : (0 : ℝ) ≤ √3 / √8 := by positivity
  have hq2 : (√3 / √8) ^ 2 = (3 / 8 : ℝ) := by
    rw [div_pow, Real.sq_sqrt (by norm_num), Real.sq_sqrt (by norm_num)]
  have e38 : √3 / √8 = √(3 / 8 : ℝ) := by rw [← hq2, Real.sqrt_sq hq0]
  obtain ⟨l38, h38b⟩ := sqrt_bounds (3 / 8) 0.6123724356 0.6123724357 (by norm_num) (by norm_num) (by norm_num) (by norm_num)
  have hdt : √3 / 2 * (2 * π / √8) = π * √(3 / 8 : ℝ) := by
    rw [← e38]; field_simp
  have pp : (0 : ℝ) < π - 3.14159265358979323846 := by linarith
  have ss : (0 : ℝ) < √(3 / 8 : ℝ) - 0.6123724356 := by linarith
  have ss2 : (0 : ℝ) < 0.6123724357 - √(3 / 8 : ℝ) := by linarith
  have pp2 : (0 : ℝ) < 3.14159265358979323847 - π := by linarith
  have lo : 3.14159265358979323846 * 0.6123724356 < π * √(3 / 8 : ℝ) := by nlinarith [mul_pos pp ss]
  have hi : π * √(3 / 8 : ℝ) < 3.14159265358979323847 * 0.6123724357 := by nlinarith [mul_pos pp2 ss2]
  refine ⟨?_, ?_, ?_, ?_, ?_⟩
  · rw [abs_lt]; constructor
    · rw [lt_sub_iff_add_lt, lt_div_iff₀ h8p]; nlinarith
    · rw [sub_lt_iff_lt_add, div_lt_iff₀ h8p]; nlinarith
  · rw [div_one, hdt, abs_lt]; constructor <;> norm_num at lo hi ⊢ <;> linarith
  · rw [hdt]; constructor
    · rw [lt_div_iff₀ (by norm_num)]; norm_num at lo ⊢; linarith
    · rw [div_lt_iff₀ (by norm_num)]; norm_num at hi ⊢; linarith
  · rw [hdt, abs_lt]; constructor
    · rw [lt_sub_iff_add_lt, lt_div_iff₀ (by norm_num)]; norm_num at lo ⊢; linarith
    · rw [sub_lt_iff_lt_add, div_lt_iff₀ (by norm_num)]; norm_num at hi ⊢; linarith
  · rw [hdt]; constructor
    · rw [lt_div_iff₀ (by norm_num)]; norm_num at lo ⊢; linarith
    · rw [div_lt_iff₀ (by norm_num)]; norm_num at hi ⊢; linarith

-- C21 (v94 l.505) conditional on the CARRIED input "bracket = 32" (hypothesis hbr; not derived here)
theorem C21_prefactor (Δt c a0 M : ℝ) (ha : a0 ≠ 0) (hM : M ≠ 0) :
    Δt ^ 2 * (2 * (M * c ^ 2 / 12)) / (4 * M * a0 ^ 2) = Δt ^ 2 * c ^ 2 / (24 * a0 ^ 2) := by
  field_simp; ring
theorem C21_sin2 (Δt c a0 bracket : ℝ) (ha : a0 ≠ 0) (hbr : bracket = 32) :
    Δt ^ 2 * c ^ 2 / (24 * a0 ^ 2) * bracket = 4 / 3 * (Δt * c / a0) ^ 2 := by
  rw [hbr]; field_simp; ring
theorem C21_values (c a0 : ℝ) (hc : 0 < c) (ha : 0 < a0) :
    4 / 3 * ((a0 / c) * c / a0) ^ 2 = 4 / 3 ∧
    4 / 3 * ((2 * π * a0 / c) * c / a0) ^ 2 = 16 * π ^ 2 / 3 ∧
    4 / 3 * ((√3 / 2 * a0 / c) * c / a0) ^ 2 = 1 ∧
    (a0 / c) / (√3 / 2 * a0 / c) = 2 / √3 ∧
    |16 * π ^ 2 / 3 - 52.6| < 0.05 ∧ |2 / √3 - 1.1547| < 0.00005 := by
  have h3 : (0 : ℝ) < √3 := Real.sqrt_pos.mpr (by norm_num)
  have s3 : √3 ^ 2 = (3 : ℝ) := Real.sq_sqrt (by norm_num)
  have p1 := Real.pi_gt_d6
  have p2 := Real.pi_lt_d6
  have hc0 : c ≠ 0 := ne_of_gt hc
  have ha0 : a0 ≠ 0 := ne_of_gt ha
  have e1 : (a0 / c) * c / a0 = 1 := by field_simp
  have e2 : (2 * π * a0 / c) * c / a0 = 2 * π := by field_simp
  have e3 : (√3 / 2 * a0 / c) * c / a0 = √3 / 2 := by field_simp
  refine ⟨?_, ?_, ?_, ?_, ?_, (C09_decimals).2.2.2.2.2⟩
  · rw [e1]; norm_num
  · rw [e2]; ring
  · rw [e3, div_pow, s3]; norm_num
  · field_simp
  · rw [abs_lt]; constructor <;> nlinarith

-- C22
theorem C22_grid25 : (25 : ℕ) ^ 4 = 390625 := by norm_num

end GB6
#print axioms GB6.C02_D4_tau2
#print axioms GB6.C02_D4_q4
#print axioms GB6.C02_D4_S
#print axioms GB6.C02_D4_tau
#print axioms GB6.C03_tau2
#print axioms GB6.C03_q4
#print axioms GB6.C03_S
#print axioms GB6.C04_tau2
#print axioms GB6.C04_q4
#print axioms GB6.C04_S
#print axioms GB6.C04_tau
#print axioms GB6.C05_FCC_q4
#print axioms GB6.C05_FCC_S
#print axioms GB6.C05_SC_q4
#print axioms GB6.C05_SC_S
#print axioms GB6.C06_Z4_q4
#print axioms GB6.C06_Z4_S
#print axioms GB6.C06_A4_q4
#print axioms GB6.C06_A4_S
#print axioms GB6.C07_ratio
#print axioms GB6.C07_margin
#print axioms GB6.C07_D4_wins
#print axioms GB6.C08_tau_ratio
#print axioms GB6.C09_decimals
#print axioms GB6.D4_eq_lit
#print axioms GB6.C12_iso2
#print axioms GB6.C12_iso4
#print axioms GB6.C14_penalties
#print axioms GB6.C18_Bstar_rc
#print axioms GB6.C18_converse
#print axioms GB6.C18_rc_prop_S
#print axioms GB6.C19_reff
#print axioms GB6.C19_reff_psi0
#print axioms GB6.C19_disc
#print axioms GB6.C19_Astar
#print axioms GB6.C19_Fexc
#print axioms GB6.C19_edge
#print axioms GB6.C19_detuned
#print axioms GB6.C20_a0_dt
#print axioms GB6.C21_prefactor
#print axioms GB6.C21_sin2
#print axioms GB6.C21_values
#print axioms GB6.C22_grid25
