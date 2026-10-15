#!/usr/bin/env python3
"""
IX.4 candidate Higgs chain — VEV / unbroken-subgroup consistency check.

Question: for each breaking step, does the proposed VEV direction leave the
claimed intermediate subgroup unbroken? A VEV v breaks every generator T with
T.v != 0. If v is a singlet under subgroup H but carries nonzero charge under
a U(1) factor of H, that U(1) is broken and the claimed intermediate group is
wrong (and the Goldstone count changes).

Branching data: CAIC-corrected rules in problems/IX4-restart.md
(dimension-checked at every stage). SM branchings are standard Slansky.

Convention: E6 -> SO(10) x U(1): 27 -> 16_1 + 10_-2 + 1_4
             78 -> 45_0 + 16_1 + 16b_-1 + 1_0
             SO(10) -> SU(5) x U(1): 16 -> 10_1 + 5b_-3 + 1_5
             10 -> 5_2 + 5b_-2 ; 45 -> 24_0 + 10_4 + 10b_-4 + 1_0
Dimensions: E6=78, SO(10)=45, SU(5)=24, SM=12.
"""

DIM = {"E6": 78, "SO10": 45, "SU5": 24, "SM": 12,
       "SO10xU1": 46, "SU5xU1": 25}

print("=" * 70)
print("IX.4 candidate chain — VEV consistency check")
print("=" * 70)

# ---------------------------------------------------------------- Step 1
# Candidate: E6 -> SO(10) x U(1) via <H_27> in singlet (1)_4, v1 >> vEW.
# Claimed broken: 78 - 46 = 32.
print("\n--- Step 1: E6 -> SO(10) x U(1) via <H_27> in (1)_4 ---")
print("VEV rep under SO(10) x U(1): singlet of SO(10), U(1) charge = 4")
so10_unbroken = True    # singlet -> trivial SO(10) action
u1_unbroken = (4 == 0)  # charge 4 != 0 -> broken
actual_H = "SO(10)" if (so10_unbroken and not u1_unbroken) else "SO(10)xU(1)"
broken_1 = DIM["E6"] - DIM["SO10"]
print(f"SO(10) unbroken: {so10_unbroken} | U(1) unbroken: {u1_unbroken}")
print(f"Actual unbroken group: {actual_H} (dim {DIM['SO10']})")
print(f"Actual Goldstones: 78 - 45 = {broken_1}  (candidate claimed 32)")
ok1 = (actual_H == "SO(10)xU(1)")
print(f"Consistent with candidate's 'SO(10) x U(1)'? {ok1}")

# ---------------------------------------------------------------- Step 2
# Candidate: SO(10) -> SU(5) x U(1) via <H_16> in singlet 1_5.
# Claimed broken: 45 - 25 = 20.
print("\n--- Step 2: SO(10) -> SU(5) x U(1) via <H_16> in 1_5 ---")
print("VEV rep under SU(5) x U(1): singlet of SU(5), U(1) charge = 5")
su5_unbroken = True
u1_2_unbroken = (5 == 0)
actual_H2 = "SU(5)" if (su5_unbroken and not u1_2_unbroken) else "SU(5)xU(1)"
broken_2 = DIM["SO10"] - DIM["SU5"]
print(f"SU(5) unbroken: {su5_unbroken} | U(1) unbroken: {u1_2_unbroken}")
print(f"Actual unbroken group: {actual_H2} (dim {DIM['SU5']})")
print(f"Actual Goldstones: 45 - 24 = {broken_2}  (candidate claimed 20)")
ok2 = (actual_H2 == "SU(5)xU(1)")
print(f"Consistent with candidate's 'SU(5) x U(1)'? {ok2}")

# ---------------------------------------------------------------- Step 3
# Candidate: SU(5) -> SM via <H_24> in SM-singlet (1,1)_0. Claimed: 24-12=12.
print("\n--- Step 3: SU(5) -> SM via <H_24> in (1,1)_0 ---")
print("VEV rep under SU(3)xSU(2)xU(1)_Y: (1,1) singlet, hypercharge 0")
sm_unbroken = True
broken_3 = DIM["SU5"] - DIM["SM"]
print(f"SM fully unbroken: {sm_unbroken}")
print(f"Goldstones: 24 - 12 = {broken_3}  (candidate claimed 12)")
ok3 = True
print(f"Consistent? {ok3}")

# ---------------------------------------------------------------- Verdict
print("\n" + "=" * 70)
print("VERDICT on the candidate as written")
print("=" * 70)
total_claimed = 32 + 20 + 12
total_actual = broken_1 + broken_2 + broken_3
print(f"Candidate chain:  E6 -> SO(10)xU(1) -> SU(5)xU(1) -> SM, "
      f"Goldstones {total_claimed}")
print(f"Actual chain:     E6 -> SO(10) -> SU(5) -> SM, "
      f"Goldstones {total_actual}")
print(f"Steps 1 and 2 INCONSISTENT as written: charged-singlet VEVs break "
      f"the retained U(1) factors.")
print(f"Note: the brief's own starting position (rank 6 -> 5 -> 4 -> 4 for "
      f"E6 > SO(10) > SU(5) > SM) matches the CORRECTED chain, not the "
      f"candidate's xU(1) intermediate groups.")

# ------------------------------------------------- U(1)-preserving variant
print("\n" + "=" * 70)
print("Variant: U(1)-preserving chain (adjoint-singlet VEVs)")
print("=" * 70)
print("Step 1': <H_78> in (1)_0 (adjoint singlet, U(1) charge 0):")
print("  E6 -> SO(10) x U(1) genuinely; broken = 78 - 46 = 32.")
print("  (Requires H_78 VEV, not H_27 as the candidate wrote.)")
print("Step 2': SO(10) -> SU(5) x U(1): needs a U(1)-neutral SU(5) singlet.")
print("  From 45 -> 24_0 + 10_4 + 10b_-4 + 1_0: the 1_0 works, but it lives")
print("  in H_78's 45_0 (no H_45 in the field content). So H_78 must supply")
print("  a second VEV in a different direction.")
print("  Result: SU(5) x U(1)_psi x U(1)_chi -- TWO U(1) factors survive.")
print("Step 3': SU(5) -> SM via 24's (1,1)_{0,0}: both U(1)s unbroken.")
print("  Leftover: SU(3) x SU(2) x U(1)_Y x U(1)' x U(1)'' -- extra Z' bosons,")
print("  phenomenologically excluded unless broken at a further stage.")
print("Conclusion: the U(1)-preserving variant needs extra breaking stages;")
print("it is NOT minimal and NOT what the candidate wrote.")

# ---------------------------------------------------------------- Minimality
print("\n" + "=" * 70)
print("Minimality of field content {H_27, H_78, H_16, H_5, H_5b, H_24}")
print("=" * 70)
print("Corrected (U(1)-broken) chain uses VEVs in: 27 (step 1), 16 (step 2),")
print("24 (step 3), 5+5b (electroweak).")
print("H_78: NO VEV assigned in the corrected chain -> redundant as written.")
print("  (It becomes load-bearing only in the U(1)-preserving variant.)")
print("H_5b: needed alongside H_5 for the EW Higgs sector (Yukawas).")
print("'Minimal' claim: UNSUPPORTED -- H_78 is unused in the chain the")
print("candidate actually (if inconsistently) describes.")

print("\nDone.")
