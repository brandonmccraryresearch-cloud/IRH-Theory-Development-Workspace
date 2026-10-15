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

## Correction (2026-10-15, post Gemini adversarial audit) — RETRACTION

The "Minimality" section above contains a **false claim**, caught by the
Gemini Spark adversarial audit ("Renormalizable Scalar Potential
Analysis," 2026-10-15). Corrected as follows; the VEV-inconsistency
findings (steps 1–2, 66 Goldstones) are **unchanged**.

**Retracted:** "$H_{78}$ carries no VEV in the corrected chain — redundant
as written."

**Why it is false:** under $SU(5)$, $\mathbf{27} =
\mathbf{1}\oplus\mathbf{1}\oplus\mathbf{5}\oplus\bar{\mathbf{5}}\oplus
\bar{\mathbf{5}}\oplus\mathbf{10}$ (via $\mathbf{27} =
\mathbf{16}\oplus\mathbf{10}\oplus\mathbf{1}$ under $SO(10)$). Every SM
singlet $(\mathbf{1},\mathbf{1})_{0}$ in the $\mathbf{27}$ is one of the two
$SU(5)$ singlets. Hence **no number of $\mathbf{27}/\overline{\mathbf{27}}$
VEVs can break $SU(5) \to$ SM** — all 24 $SU(5)$ generators annihilate them
(54 Goldstones max). Step 3's $\langle H_{24}\rangle$ in
$(\mathbf{1},\mathbf{1})_{0}$ must come from a representation containing
$\mathbf{24}\subset SU(5)$: minimally $H_{78}$ ($\mathbf{78}\supset
\mathbf{45}_{0}\supset\mathbf{24}_{(0,0)}$), or $\mathbf{650}$/
$\mathbf{351}'$. **$H_{78}$ is load-bearing for stage 3, not redundant.**

**Refinement (two $\mathbf{27}$s required):** the two $SU(5)$-singlet
directions $e_{1}, e_{2}\subset\mathbf{27}$ form an $\mathfrak{su}(2)$
doublet (under $\mathfrak{su}(2)\subset\mathfrak{su}(6)\oplus\mathfrak{su}(2)
\subset\mathfrak{e}_{6}$). Any VEV $v_{1}e_{1}+v_{2}e_{2}$ inside a
**single** $\mathbf{27}$ is $E_{6}$-gauge-equivalent to a single direction,
giving only $SO(10)$ (33 Goldstones), never $SU(5)$. Steps 1–2 therefore
require **two linearly independent multiplets**
$\Phi_{1},\Phi_{2}\in\mathbf{27}$ (the note's "$H_{16}$" is the
$\mathbf{16}\subset\mathbf{27}$ of the second multiplet).

**Consequence for stage 3 (Gemini no-go, tree level):** with field content
$\{\Phi_{1},\Phi_{2}\in\mathbf{27}, H\in\mathbf{78}\}$, the tree-level
$d\le4$ potential restricted to $H\in\mathfrak{su}(5)$ depends only on
$\operatorname{Tr}(H^{2})$ — $E_{6}$ has Casimir degrees
$\{2,5,6,8,9,12\}$, so $\operatorname{Tr}_{27}(H^{4})\equiv
\frac{1}{12}[\operatorname{Tr}_{27}(H^{2})]^{2}$ identically (Okubo) —
giving an accidental $O(24)$ symmetry that cannot select the SM vacuum
over $SU(4)\times U(1)$ (11 pseudo-Goldstones). Stage 3 at tree level
requires either 1-loop Coleman–Weinberg / $d{=}6$ $\operatorname{Tr}(H^{6})$
or upgrading to $\Phi_{650}$/$\Phi_{351'}$. Decision pending (see main
chat 2026-10-15).

## What remains (unchanged)

Scalar potential and vacuum alignment; what sets $v_1, v_2, v_3$; explicit
Dimopoulos–Wilczek or missing-partner construction; Yukawa tables; IRH
substrate origin of the Higgs sector; monopole topology (3.4, joint with
4.1).
