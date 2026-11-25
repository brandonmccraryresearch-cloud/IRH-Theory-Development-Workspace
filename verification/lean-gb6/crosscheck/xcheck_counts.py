#!/usr/bin/env python3
"""w-gb6 second-tool cross-check (EXP-1304). Independent Python enumeration.
Prints computed numbers only (no verdict strings). Shell models as frozen in
ADDENDUM w-gb6 sha256 41d3453c... . Exact arithmetic via fractions.Fraction."""
import itertools, sys
from fractions import Fraction
from collections import Counter

def signs_perms(base):
    out = set()
    for p in itertools.permutations(base):
        for s in itertools.product((1, -1), repeat=len(p)):
            out.add(tuple(a * b for a, b in zip(p, s)))
    return sorted(out)

def add(a, b):
    return tuple(x + y for x, y in zip(a, b))

def neg(a):
    return tuple(-x for x in a)

def counts(shell, want_h=False):
    n = len(shell)
    assert n > 0 and len(set(shell)) == n
    S = set(shell)
    # T: ordered triples a+b+c=0  <=> c = -(a+b) in shell
    T = sum(1 for a in shell for b in shell if neg(add(a, b)) in S)
    m2 = Counter(add(a, b) for a in shell for b in shell)
    Q = sum(c * m2.get(neg(v), 0) for v, c in m2.items())
    H = None
    if want_h:
        m3 = Counter()
        for v, c in m2.items():
            for a in shell:
                m3[add(v, a)] += c
        H = sum(c * m3.get(neg(v), 0) for v, c in m3.items())
    return n, T, Q, H

def brute_T(shell):
    return sum(1 for a, b, c in itertools.product(shell, repeat=3) if add(add(a, b), c) == (0,) * len(a))

def brute_Q(shell):
    z = (0,) * len(shell[0])
    return sum(1 for a, b, c, d in itertools.product(shell, repeat=4) if add(add(a, b), add(c, d)) == z)

shells = {}
shells["D4"] = signs_perms((1, 1, 0, 0))
shells["D4scaled"] = signs_perms((2, 2, 0, 0))
shells["A4roots_Z5"] = sorted({tuple((1 if k == i else 0) - (1 if k == j else 0) for k in range(5)) for i in range(5) for j in range(5) if i != j})
a4s = []
for i in range(5):
    v = tuple((5 if k == i else 0) - 1 for k in range(5))
    a4s += [v, neg(v)]
shells["A4star_min_Z5x5"] = sorted(a4s)
shells["Z4"] = signs_perms((1, 0, 0, 0))
shells["BCCrow_fcc12"] = signs_perms((1, 1, 0))
shells["FCCrow_bcc8"] = signs_perms((1, 1, 1))
shells["SC6"] = signs_perms((1, 0, 0))
shells["comp7_box"] = sorted(v for v in itertools.product(range(-3, 4), repeat=4) if sum(x * x for x in v) == 7)

print("python", sys.version.split()[0])
res = {}
for name, sh in shells.items():
    n, T, Q, H = counts(sh, want_h=(name == "D4"))
    norms = sorted({sum(x * x for x in v) for v in sh})
    bt = brute_T(sh)
    bq = brute_Q(sh) if len(sh) <= 24 else None
    res[name] = (n, T, Q)
    print(f"{name}: N={n} T={T} Q={Q} H={H} norms2={norms} bruteT={bt} bruteQ={bq}")
    if T:
        tau2 = Fraction(T * T, n ** 3)
        q4 = Fraction(Q, n * n)
        print(f"  tau2={tau2} q4={q4} S={tau2 / q4} S_float={float(tau2 / q4)!r}")
    else:
        print(f"  q4={Fraction(Q, n * n)} S=0")

d4 = shells["D4"]
dot = lambda a, b: sum(x * y for x, y in zip(a, b))
partners = Counter(sum(1 for b in d4 if dot(a, b) == -1) for a in d4)
print("D4 partners at dot -1 histogram:", dict(partners))
print("D4 distinct-pair dot set:", sorted({dot(a, b) for a in d4 for b in d4 if a != b}))
unordered = {frozenset((a, b, neg(add(a, b)))) for a in d4 for b in d4 if neg(add(a, b)) in set(d4)}
print("D4 unordered zero-sum 3-subsets:", len(unordered), "sizes", Counter(len(s) for s in unordered))
# 16^4 grid maxima, scaled shell, x = 2*pi*n/16
sc = shells["D4scaled"]
cnt = sum(1 for n in itertools.product(range(16), repeat=4) if all(dot(k, n) % 16 == 0 for k in sc))
print("grid16 maxima count:", cnt)
S_D4 = Fraction(64, 141); S_A = Fraction(12, 31)
print("ratio", S_D4 / S_A, "margin", S_D4 / S_A - 1, float(S_D4 / S_A - 1))
print("25^4", 25 ** 4)
