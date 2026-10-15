# IX.4 Higgs candidate — VEV / unbroken-subgroup consistency check (2026-10-15)

**Status:** CAIC verification of the Grok-proposed candidate in
`problems/IX4-restart.md` (PR #4). Executed script:
`verification/ix4_vev_consistency.py` (exit 0).

## Method

For each breaking step, the unbroken subgroup is the set of generators $T$
with $T \cdot v = 0$ on the VEV $v$. A VEV in a singlet direction of a
subgroup $H$ leaves $H$'s non-abelian factors unbroken, but breaks every
$U(1)$ factor under which it carries nonzero charge. Branching rules and
charges per `problems/IX4-restart.md` (dimension-checked); SM branchings
standard.

## Findings

**Steps 1 and 2 of the candidate as written are inconsistent.**

| Step | Candidate claim | VEV | Actual unbroken | Goldstones |
|------|----------------|-----|-----------------|------------|
| 1. $E_6 \to SO(10)\times U(1)$ | 32 | $\langle H_{27}\rangle$ in $(\mathbf{1})_{4}$, $U(1)$ charge $4 \neq 0$ | $SO(10)$ ( $U(1)$ broken) | **33**, not 32 |
| 2. $SO(10) \to SU(5)\times U(1)$ | 20 | $\langle H_{16}\rangle$ in $\mathbf{1}_{5}$, $U(1)$ charge $5 \neq 0$ | $SU(5)$ ( $U(1)$ broken) | **21**, not 20 |
| 3. $SU(5) \to$ SM | 12 | $\langle H_{24}\rangle$ in $(\mathbf{1},\mathbf{1})_{0}$ | SM | 12 ✓ |

**Corrected chain:** $E_6 \to SO(10) \to SU(5) \to SM$,
Goldstones $33 + 21 + 12 = \mathbf{66}$ (candidate claimed 64).

**Consistency note:** the brief's own starting position (rank $6 \to 5 \to
4 \to 4$ for $E_6 \supset SO(10) \supset SU(5) \supset$ SM) already assumes
the $U(1)$ factors are broken — it matches the corrected chain, not the
candidate's $\times U(1)$ intermediate groups.

## $U(1)$-preserving variant (for the record)

Restoring the $U(1)$s requires reassigning VEVs to adjoint singlets:
$\langle H_{78}\rangle$ in $(\mathbf{1})_{0}$ gives $E_6 \to SO(10)\times
U(1)$ genuinely (32 broken), but the next step then needs $H_{78}$'s
$(\mathbf{1})_{0}$ inside its $\mathbf{45}_{0}$ (no $H_{45}$ in the field
content), leaving $SU(5)\times U(1)\times U(1)$ — two extra $U(1)$s survive
to the SM stage (extra $Z'$ bosons, excluded without further breaking).
Not minimal, not what the candidate wrote.

## Minimality

Field content $\{H_{27}, H_{78}, H_{16}, H_{5}, H_{\bar5}, H_{24}\}$:
the corrected chain assigns VEVs in the $\mathbf{27}$, $\mathbf{16}$,
$\mathbf{24}$, $\mathbf{5}\oplus\bar{\mathbf{5}}$. **$H_{78}$ carries no VEV
in the corrected chain — redundant as written** (load-bearing only in the
$U(1)$-preserving variant). The "minimal" label is unsupported.

## What remains (unchanged)

Scalar potential and vacuum alignment; what sets $v_1, v_2, v_3$; explicit
Dimopoulos–Wilczek or missing-partner construction; Yukawa tables; IRH
substrate origin of the Higgs sector; monopole topology (3.4, joint with
4.1).
