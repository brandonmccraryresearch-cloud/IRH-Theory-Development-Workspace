import GB6H
/-! w-gb6 EXP-1304 C17 (route 2): the same reduction with INTEGER keys. Each D4 root (length 4, entries in
[-1,1]) is encoded as enc v = v0 + 13 v1 + 169 v2 + 2197 v3. A sum of six roots has entries in [-6,6], so it is
zero iff the sum of the codes is zero (base 13 > 2·6; proved by omega). All lemmas are proved here. -/
namespace GB6

def enc : V → Int
  | [x0, x1, x2, x3] => x0 + 13 * x1 + 169 * x2 + 2197 * x3
  | _ => 0

lemma four (a : V) (h : a.length = 4) : ∃ x0 x1 x2 x3 : Int, a = [x0, x1, x2, x3] := by
  rcases a with _ | ⟨x0, _ | ⟨x1, _ | ⟨x2, _ | ⟨x3, _ | ⟨x4, t⟩⟩⟩⟩⟩
  all_goals first | exact ⟨_, _, _, _, rfl⟩ | (simp at h) | (simp at h; omega)

abbrev Pb (a : V) : Prop := a.length = 4 ∧ ∀ x ∈ a, -1 ≤ x ∧ x ≤ 1

theorem D4_Pb : ∀ a ∈ D4, a.length = 4 ∧ ∀ x ∈ a, -1 ≤ x ∧ x ≤ 1 := by decide +kernel

lemma key (a b c d e f : V) (ha : Pb a) (hb : Pb b) (hc : Pb c) (hd : Pb d) (he : Pb e) (hf : Pb f) :
    isZero (vadd (vadd (vadd a b) c) (vadd (vadd d e) f)) =
      (enc a + enc b + enc c + (enc d + enc e + enc f) == 0) := by
  obtain ⟨a0, a1, a2, a3, rfl⟩ := four a ha.1
  obtain ⟨b0, b1, b2, b3, rfl⟩ := four b hb.1
  obtain ⟨c0, c1, c2, c3, rfl⟩ := four c hc.1
  obtain ⟨d0, d1, d2, d3, rfl⟩ := four d hd.1
  obtain ⟨e0, e1, e2, e3, rfl⟩ := four e he.1
  obtain ⟨f0, f1, f2, f3, rfl⟩ := four f hf.1
  have a0b := ha.2 a0 (by simp)
  have a1b := ha.2 a1 (by simp)
  have a2b := ha.2 a2 (by simp)
  have a3b := ha.2 a3 (by simp)
  have b0b := hb.2 b0 (by simp)
  have b1b := hb.2 b1 (by simp)
  have b2b := hb.2 b2 (by simp)
  have b3b := hb.2 b3 (by simp)
  have c0b := hc.2 c0 (by simp)
  have c1b := hc.2 c1 (by simp)
  have c2b := hc.2 c2 (by simp)
  have c3b := hc.2 c3 (by simp)
  have d0b := hd.2 d0 (by simp)
  have d1b := hd.2 d1 (by simp)
  have d2b := hd.2 d2 (by simp)
  have d3b := hd.2 d3 (by simp)
  have e0b := he.2 e0 (by simp)
  have e1b := he.2 e1 (by simp)
  have e2b := he.2 e2 (by simp)
  have e3b := he.2 e3 (by simp)
  have f0b := hf.2 f0 (by simp)
  have f1b := hf.2 f1 (by simp)
  have f2b := hf.2 f2 (by simp)
  have f3b := hf.2 f3 (by simp)
  simp only [vadd, isZero, enc, List.all_cons, List.all_nil, Bool.and_true]
  rw [Bool.eq_iff_iff]
  simp only [Bool.and_eq_true, beq_iff_eq]
  constructor
  · intro h; omega
  · intro h; omega

def RI (L : List Int) (g : Int → Nat) : Nat :=
  (L.map fun a => (L.map fun b => (L.map fun c => g (a + b + c)).sum).sum).sum

def E4 : List Int := D4.map enc

theorem cntH_link_gen (s : List V) (hs : ∀ a ∈ s, Pb a) :
    cntH s = RI (s.map enc) (fun x => RI (s.map enc) (fun y => ind (x + y == 0))) := by
  rw [cntH_eq]
  unfold R3 RI
  simp only [List.map_map, Function.comp_def]
  refine congrArg List.sum (List.map_congr_left ?_); intro a ha
  refine congrArg List.sum (List.map_congr_left ?_); intro b hb
  refine congrArg List.sum (List.map_congr_left ?_); intro c hc
  refine congrArg List.sum (List.map_congr_left ?_); intro d hd
  refine congrArg List.sum (List.map_congr_left ?_); intro e he
  refine congrArg List.sum (List.map_congr_left ?_); intro f hf
  rw [key a b c d e f (hs a ha) (hs b hb) (hs c hc) (hs d hd) (hs e he) (hs f hf)]

theorem cntH_link : cntH D4 = RI E4 (fun x => RI E4 (fun y => ind (x + y == 0))) :=
  cntH_link_gen D4 D4_Pb

/-! integer-keyed tables (same lemmas as GB6H, key type Int) -/
def WI (D : List (Int × Nat)) (g : Int → Nat) : Nat := (D.map fun p => p.2 * g p.1).sum
lemma WI_cons (p : Int × Nat) (D : List (Int × Nat)) (g : Int → Nat) : WI (p :: D) g = p.2 * g p.1 + WI D g := by
  simp [WI]
lemma WI_append (D1 D2 : List (Int × Nat)) (g : Int → Nat) : WI (D1 ++ D2) g = WI D1 g + WI D2 g := by
  simp [WI]
def stepI (L : List Int) (D : List (Int × Nat)) : List (Int × Nat) := D.flatMap fun p => L.map fun a => (p.1 + a, p.2)
lemma WI_shift (L : List Int) (p : Int × Nat) (g : Int → Nat) :
    WI (L.map fun a => (p.1 + a, p.2)) g = p.2 * (L.map fun a => g (p.1 + a)).sum := by
  induction L with
  | nil => simp [WI]
  | cons a L ih =>
    rw [List.map_cons, WI_cons, ih]
    simp only [List.map_cons, List.sum_cons]
    ring
lemma WI_step (L : List Int) (D : List (Int × Nat)) (g : Int → Nat) :
    WI (stepI L D) g = WI D (fun x => (L.map fun a => g (x + a)).sum) := by
  induction D with
  | nil => simp [stepI, WI]
  | cons p D ih =>
    have : stepI L (p :: D) = (L.map fun a => (p.1 + a, p.2)) ++ stepI L D := by simp [stepI]
    rw [this, WI_append, WI_shift, ih, WI_cons]
def insI (q : Int × Nat) : List (Int × Nat) → List (Int × Nat)
  | [] => [q]
  | p :: r => if p.1 = q.1 then (p.1, p.2 + q.2) :: r else p :: insI q r
lemma WI_ins (q : Int × Nat) (D : List (Int × Nat)) (g : Int → Nat) : WI (insI q D) g = q.2 * g q.1 + WI D g := by
  induction D with
  | nil => simp [insI, WI]
  | cons p r ih =>
    by_cases h : p.1 = q.1
    · rw [show insI q (p :: r) = (p.1, p.2 + q.2) :: r by simp [insI, h], WI_cons, WI_cons]
      dsimp only
      rw [h]; ring
    · rw [show insI q (p :: r) = p :: insI q r by simp [insI, h], WI_cons, WI_cons, ih]
      ring
def cmpI (D : List (Int × Nat)) : List (Int × Nat) := D.foldr insI []
lemma WI_cmp (D : List (Int × Nat)) (g : Int → Nat) : WI (cmpI D) g = WI D g := by
  induction D with
  | nil => rfl
  | cons p D ih =>
    show WI (insI p (cmpI D)) g = WI (p :: D) g
    rw [WI_ins, ih, WI_cons]
def DI1 (L : List Int) : List (Int × Nat) := L.map fun a => (a, 1)
lemma WI_D1 (L : List Int) (g : Int → Nat) : WI (DI1 L) g = (L.map g).sum := by
  induction L with
  | nil => rfl
  | cons a L ih =>
    rw [show DI1 (a :: L) = (a, 1) :: DI1 L from rfl, WI_cons, ih]
    simp
def DI3 (L : List Int) : List (Int × Nat) := cmpI (stepI L (cmpI (stepI L (DI1 L))))
lemma RI_eq (L : List Int) (g : Int → Nat) : RI L g = WI (DI3 L) g := by
  unfold DI3
  rw [WI_cmp, WI_step, WI_cmp, WI_step, WI_D1]
  rfl
theorem cntH_tableI :
    cntH D4 = WI (DI3 E4) (fun x => WI (DI3 E4) (fun y => ind (x + y == 0))) := by
  rw [cntH_link]
  simp only [RI_eq]
end GB6
#print axioms GB6.four
#print axioms GB6.D4_Pb
#print axioms GB6.key
#print axioms GB6.cntH_link
#print axioms GB6.cntH_tableI
