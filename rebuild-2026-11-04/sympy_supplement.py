"""Supplement: internal-consistency of the II.5/II.4 table rows.
Given stated (N, tau^2, q4), recover T = tau * N^(3/2) and Q = q4 * N^2.
These check the table's internal arithmetic; they do NOT derive T/Q from
shell geometry (that enumeration is not in the source text and is flagged)."""
import sympy as sp
from sympy import Rational as R, sqrt, simplify
ok = fail = 0
def check(name, cond, detail=""):
    global ok, fail
    print(("PASS " if cond else "FAIL ") + name + ((" | " + str(detail)) if detail else ""))
    if cond: ok += 1
    else: fail += 1
def recover(N, tau2, q4):
    tau = sqrt(tau2)
    T = simplify(tau * sp.Integer(N)**sp.Rational(3, 2))
    Q = simplify(q4 * N**2)
    return T, Q
T, Q = recover(20, R(9, 5), R(93, 20))
check("A4* recovers T = 120 from tau^2 = 9/5, N = 20", T == 120, T)
check("A4* recovers Q = 1860 from q4 = 93/20, N = 20", Q == 1860, Q)
T, Q = recover(8, 0, R(21, 8))
check("Z4 recovers Q = 168 from q4 = 21/8, N = 8", Q == 168, Q)
T, Q = recover(10, 0, R(27, 10))
check("A4 recovers Q = 270 from q4 = 27/10, N = 10", Q == 270, Q)
T, Q = recover(8, 0, R(27, 8))
check("FCC recovers Q = 216 from q4 = 27/8, N = 8", Q == 216, Q)
T, Q = recover(6, 0, R(5, 2))
check("SC recovers Q = 90 from q4 = 5/2, N = 6", Q == 90, Q)
T, Q = recover(12, R(4, 3), R(15, 4))
check("BCC recovers T = 48, Q = 540", (T, Q) == (48, 540), (T, Q))
print(f"\nTOTAL: {ok} PASS, {fail} FAIL")
