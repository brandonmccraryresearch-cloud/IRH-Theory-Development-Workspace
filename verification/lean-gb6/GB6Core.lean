/-! w-gb6 (EXP-1304, G-B6): core definitions for finite shell combinatorics.
Pure Lean core, no Mathlib. Vectors are `List Int` of a fixed length. -/
namespace GB6

abbrev V := List Int

/-- coordinatewise sum -/
def vadd : V → V → V
  | a :: as, b :: bs => (a + b) :: vadd as bs
  | _, _ => []

def vneg (v : V) : V := v.map (fun x => -x)

def isZero (v : V) : Bool := v.all (fun x => x == 0)

def dot : V → V → Int
  | a :: as, b :: bs => a * b + dot as bs
  | _, _ => 0

def normSq (v : V) : Int := dot v v

/-- integers -r..r -/
def intRange (r : Nat) : List Int := (List.range (2 * r + 1)).map (fun (i : Nat) => (i : Int) - (r : Int))

/-- all integer vectors of length d with coordinates in [-r, r] -/
def box (r : Nat) : Nat → List V
  | 0 => [[]]
  | d + 1 => (intRange r).flatMap (fun x => (box r d).map (fun v => x :: v))

/-- all vectors of `box r d` with squared norm m -/
def shellOf (d r : Nat) (m : Int) : List V := (box r d).filter (fun v => normSq v == m)

/-- N: number of modes -/
def cntN (s : List V) : Nat := s.length

/-- T: number of ORDERED triples (a,b,c) ∈ s³ with a+b+c = 0 -/
def cntT (s : List V) : Nat :=
  (s.flatMap fun a => s.flatMap fun b => s.filter fun c => isZero (vadd (vadd a b) c)).length

/-- Q: number of ORDERED quadruples (a,b,c,d) ∈ s⁴ with a+b+c+d = 0 -/
def cntQ (s : List V) : Nat :=
  (s.flatMap fun a => s.flatMap fun b => s.flatMap fun c =>
     s.filter fun d => isZero (vadd (vadd (vadd a b) c) d)).length

end GB6

namespace GB6

/-- suffixes of a list (core has no `List.tails`) -/
def suffixes {α : Type} : List α → List (List α)
  | [] => [[]]
  | a :: r => (a :: r) :: suffixes r

/-- number of index triples i<j<k (positions in s) with s[i]+s[j]+s[k] = 0;
for a duplicate-free list this is the number of 3-element subsets summing to 0 -/
def cnt3sub (s : List V) : Nat :=
  ((suffixes s).flatMap fun t => match t with
    | [] => []
    | a :: r => (suffixes r).flatMap fun t2 => match t2 with
      | [] => []
      | b :: r2 => r2.filter fun c => isZero (vadd (vadd a b) c)).length

/-! ### Shell models (frozen in ADDENDUM w-gb6 sha256 41d3453c…) -/

/-- D4 roots ±e_i±e_j = all integer vectors in Z^4 of squared norm 2 -/
def D4 : List V := shellOf 4 1 2
/-- scaled D4 shell (±2,±2,0,0) and perms, |k|^2 = 8 (v94 l.296) -/
def D4s : List V := shellOf 4 2 8
/-- Z^4 minimal shell ±e_i -/
def Z4 : List V := shellOf 4 1 1
/-- A4 roots e_i - e_j in Z^5 (the reciprocal shell of the A4* crystal, row "A4*") -/
def A4r : List V := (shellOf 5 1 2).filter (fun v => v.sum == 0)
/-- A4* minimal shell ±(e_i - (1/5)(1,1,1,1,1)), scaled by 5 (row "A4"); T, Q scale-invariant -/
def A4sm : List V :=
  [[4,-1,-1,-1,-1], [-4,1,1,1,1], [-1,4,-1,-1,-1], [1,-4,1,1,1], [-1,-1,4,-1,-1],
   [1,1,-4,1,1], [-1,-1,-1,4,-1], [1,1,1,-4,1], [-1,-1,-1,-1,4], [1,1,1,1,-4]]
/-- BCC-crystal row: reciprocal minimal shell = FCC minimal vectors (±1,±1,0) perms, Z^3 norm 2 -/
def BCCr : List V := shellOf 3 1 2
/-- FCC-crystal row: reciprocal minimal shell = BCC minimal vectors (±1,±1,±1), Z^3 norm 3 -/
def FCCr : List V := shellOf 3 1 3
/-- SC row: ±e_i in Z^3 -/
def SC : List V := shellOf 3 1 1
/-- competitor: the full integer shell |k|^2 = 7 in Z^4 (box [-3,3]^4; completeness proved in GB6Complete) -/
def C7 : List V := shellOf 4 3 7

/-- 16^4 grid points n ∈ {0..15}^4 -/
def grid16 : List V :=
  let r : List Int := (List.range 16).map (fun (i : Nat) => (i : Int))
  r.flatMap fun a => r.flatMap fun b => r.flatMap fun c => r.map fun d => [a, b, c, d]

end GB6
