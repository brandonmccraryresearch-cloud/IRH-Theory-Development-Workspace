import GB6Core
import Mathlib.Tactic
/-! w-gb6 EXP-1304 C17: H (D-H reading) = number of ORDERED 6-tuples in s⁶ summing to 0.
The direct 24⁶ enumeration is too heavy for the kernel, so (as frozen in the ADDENDUM) the count is
reduced by Lean-PROVED lemmas to a weighted table computation:
  cntH s = Σ_{(k,c) ∈ D3} c · Σ_{(k',c') ∈ D3} c' · [k + k' = 0],
where D3 is the (compressed) multiset of ordered 3-sums. Nothing here is assumed. -/
namespace GB6

/-- H: ordered zero-sum 6-tuples (same nesting style as cntT / cntQ) -/
def cntH (s : List V) : Nat :=
  (s.flatMap fun a => s.flatMap fun b => s.flatMap fun c => s.flatMap fun d => s.flatMap fun e =>
     s.filter fun f => isZero (vadd (vadd (vadd (vadd (vadd a b) c) d) e) f)).length

theorem vadd_assoc : ∀ x y z : V, vadd (vadd x y) z = vadd x (vadd y z)
  | a :: as, b :: bs, c :: cs => by
      show ((a + b) + c) :: vadd (vadd as bs) cs = (a + (b + c)) :: vadd as (vadd bs cs)
      rw [vadd_assoc as bs cs, Int.add_assoc]
  | [], _, _ => rfl
  | _ :: _, [], _ => rfl
  | _ :: _, _ :: _, [] => rfl

def ind (b : Bool) : Nat := if b then 1 else 0

lemma len_flatMap {α β : Type} (l : List α) (f : α → List β) :
    (l.flatMap f).length = (l.map fun a => (f a).length).sum := by
  induction l with
  | nil => rfl
  | cons a l ih => simp [List.flatMap_cons, ih]

lemma len_filter {α : Type} (l : List α) (p : α → Bool) :
    (l.filter p).length = (l.map fun a => ind (p a)).sum := by
  induction l with
  | nil => rfl
  | cons a l ih =>
    cases h : p a
    · simp [List.filter_cons, h, ind, ih]
    · simp [List.filter_cons, h, ind, ih] <;> omega

def R3 (s : List V) (g : V → Nat) : Nat :=
  (s.map fun a => (s.map fun b => (s.map fun c => g (vadd (vadd a b) c)).sum).sum).sum

lemma cntH_eq (s : List V) : cntH s = R3 s (fun x => R3 s (fun y => ind (isZero (vadd x y)))) := by
  unfold cntH R3
  simp only [len_flatMap, len_filter, vadd_assoc]

/-- weighted sum over a (key, multiplicity) table -/
def W (D : List (V × Nat)) (g : V → Nat) : Nat := (D.map fun p => p.2 * g p.1).sum

lemma W_nil (g : V → Nat) : W [] g = 0 := rfl
lemma W_cons (p : V × Nat) (D : List (V × Nat)) (g : V → Nat) : W (p :: D) g = p.2 * g p.1 + W D g := by
  simp [W]
lemma W_append (D1 D2 : List (V × Nat)) (g : V → Nat) : W (D1 ++ D2) g = W D1 g + W D2 g := by
  simp [W]

def step (s : List V) (D : List (V × Nat)) : List (V × Nat) := D.flatMap fun p => s.map fun a => (vadd p.1 a, p.2)

lemma W_shift (s : List V) (p : V × Nat) (g : V → Nat) :
    W (s.map fun a => (vadd p.1 a, p.2)) g = p.2 * (s.map fun a => g (vadd p.1 a)).sum := by
  induction s with
  | nil => simp [W]
  | cons a s ih =>
    rw [List.map_cons, W_cons, ih]
    simp only [List.map_cons, List.sum_cons]
    ring

lemma W_step (s : List V) (D : List (V × Nat)) (g : V → Nat) :
    W (step s D) g = W D (fun x => (s.map fun a => g (vadd x a)).sum) := by
  induction D with
  | nil => simp [step, W]
  | cons p D ih =>
    have : step s (p :: D) = (s.map fun a => (vadd p.1 a, p.2)) ++ step s D := by simp [step]
    rw [this, W_append, W_shift, ih, W_cons]

def ins (q : V × Nat) : List (V × Nat) → List (V × Nat)
  | [] => [q]
  | p :: r => if p.1 = q.1 then (p.1, p.2 + q.2) :: r else p :: ins q r

lemma W_ins (q : V × Nat) (D : List (V × Nat)) (g : V → Nat) : W (ins q D) g = q.2 * g q.1 + W D g := by
  induction D with
  | nil => simp [ins, W]
  | cons p r ih =>
    by_cases h : p.1 = q.1
    · rw [show ins q (p :: r) = (p.1, p.2 + q.2) :: r by simp [ins, h], W_cons, W_cons]
      dsimp only
      rw [h]; ring
    · rw [show ins q (p :: r) = p :: ins q r by simp [ins, h], W_cons, W_cons, ih]
      ring

def cmp (D : List (V × Nat)) : List (V × Nat) := D.foldr ins []

lemma W_cmp (D : List (V × Nat)) (g : V → Nat) : W (cmp D) g = W D g := by
  induction D with
  | nil => rfl
  | cons p D ih =>
    show W (ins p (cmp D)) g = W (p :: D) g
    rw [W_ins, ih, W_cons]

def D1 (s : List V) : List (V × Nat) := s.map fun a => (a, 1)

lemma W_D1 (s : List V) (g : V → Nat) : W (D1 s) g = (s.map g).sum := by
  induction s with
  | nil => rfl
  | cons a s ih =>
    rw [show D1 (a :: s) = (a, 1) :: D1 s from rfl, W_cons, ih]
    simp

def D3 (s : List V) : List (V × Nat) := cmp (step s (cmp (step s (D1 s))))

lemma R3_eq (s : List V) (g : V → Nat) : R3 s g = W (D3 s) g := by
  unfold D3
  rw [W_cmp, W_step, W_cmp, W_step, W_D1]
  rfl

/-- the reduction: H = Σ_{(k,c)∈D3} c · Σ_{(k',c')∈D3} c' [k+k' = 0] -/
theorem cntH_table (s : List V) :
    cntH s = W (D3 s) (fun x => W (D3 s) (fun y => ind (isZero (vadd x y)))) := by
  rw [cntH_eq]
  simp only [R3_eq]

end GB6
#print axioms GB6.vadd_assoc
#print axioms GB6.cntH_eq
#print axioms GB6.cntH_table
