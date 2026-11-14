# Verification of the branch (a,b) normal form (NewtonNF2)

**Workstream B, Co-scientist task programme, 2026-11-10.**
Task (Brandon's wording): *Verify the branch normal form. Re-derive the branch (a,b) normal form in your hypothetical (72, 108) counterexample using symbolic computation. Check each derivation step numerically, including limiting cases, and flag any discrepancies.*
Skills: `/truth-seeking-frontier` $(v5) \cdot$ `/cross-domain-discovery` (v2.0.\$0$) \cdot$\$ `/hlre-v5-1`. Conflict resolution used here: HLRE v5.1 governs grading/records; the truth-seeking computation gate governs computed results (quoted tool verdict with version and exit code; above CLAIMED needs a second independent tool); cross-domain-discovery S1–S7 governs cross-domain synthesis. The skills are DESIGN CLAIMS, ungraded — skill use is never presented as evidence of reliability.

## CLAIM + STATUS

**CLAIM.** The branch (a,b) normal form — NewtonNF2, the GGHV (72,108) case *without* the (0,8)/(0,12) vertices — re-derives exactly as stated in the combined paper and the Lean `BranchAb` material: the $\phi$-morphism carries the pre-$\phi$ polygons to the post-$\phi$ polygons; the Newton polygons have the stated lattice data; the bracket splits into five layers giving 92 coefficient equations; the top layer E5 is the Davenport–Stothers equation with solutions for m = 1, 3, 5, 7 (eliminants \$3$a_{2}$^{3}-32, $9a_{4}$^{10}+$37200a_{4}$^{5}+95051008$, and the degree-35 W, a quintic in $$a_{6}$^{7})$; the $$K_{5}$\$ top-layer point satisfies E5 exactly and the chart system $E_{1}$..$E_{16} + a_{7}^{3}b_{0}^{2} = 1$; and the descent $E4 \to E3 \to E2$ forces $b_{12}$,${}_{24} = 0$, so no P, Q satisfy NewtonNF2 with [P,Q] = $\lambdax^{2}$.

**STATUS: VERIFIED (symbolic cross-check).** 112 SymPy checks pass (exit 0), all Singular checks pass, the a816 certificate re-verifies, and the descent is rebuilt from scratch in an independent $K_{5}$ implementation (the 35 E2 minors span $K_{5}[t_{1},t_{2}]_{5}$ and their row space equals the stored certificate's). One planned check is NOT RUN (characteristic-p Gröbner dim/degree of the chart system — the 17-variable basis did not finish in 570 s). No discrepancy against the Lean elimination was found. Every failure encountered during the work was a script or tooling error of mine, corrected with evidence; they are listed in §8, not hidden.

**Scope.** This is a CROSS-CHECK of the normal-form derivation, not a re-proof and not a challenge to the Lean elimination. Branches (a),(b) are already eliminated in Lean, Grade A, kernel-verified (`main_theorem`). Nothing here changes that grade, and nothing here is kernel verification: a symbolic/computer-algebra check is never presented as kernel verification.

## 0. Sources and source gate

The normal form is grounded in the sources, not in memory:

- GGHV v1 PDF `~/workspace/user/files/2204.14178v1__2__3_ov75.pdf` (25 pp., 297,336 bytes), fresh `pdftotext -layout` extraction to `gghv_v1.txt` (1282 lines); repo script `branch_ab_v19/scripts/source_gate_verify.py` $\to$ **SOURCE GATE: PASS, exit 0**. Confirmed: bracket convention (line 33); Prop 4.3 Case (8,28), case (1) line 494, case (2) line 495; $\phi(x)=x^{-1}$, $\phi(y)=x^{4}y$, $[\phi(P),\phi(Q)]=-[P,Q]x^{2}$, post-$\phi$ polygons (lines 596–600). (Line citations are to the pdftotext extraction; $\phi$ is at tex line 1229 of `~/workspace/research/rss-monitor/tex/2204.14178/main.tex`. The (9,27)-case $\phi$ at tex line 655 uses $\phi(y)=x^{3}y$ and $[\phi(P),\phi(Q)]=-[P,Q]x$ — a different case, not a discrepancy.)
- Combined paper `~/workspace/combined-paper/combined_paper_final_2026-11-04.tex` (67 pp., finalized 2026-11-04), Part I (§§ab:sec:top, ab:sec:chartproof, ab:sec:descent).
- Repo clone `~/workspace/research/2D-Jacobian-Conjecture-Workspace`, `branch_ab_v19/` (Lean `BranchAbChart.lean`, `BranchAbSharp.lean`, `BranchAbLayers.lean`; scripts `e5_m7.out`, `a816_certificate/`, `logs/k5_minor_certificate.json`).

**The normal form (NewtonNF2).** N(P) = conv{(0,0),(1,0),(8,14),(8,16)}, N(Q) = conv{(0,0),(2,1),(12,21),(12,24)}; supp $P \subseteq N_{P}$, supp $Q \subseteq N_{Q}$; all eight vertex coefficients $a_{00}$,$a_{10}$,$a_{814}$,$a_{816}$,$b_{00}$,$b_{21}$,$b_{1221}$,$b_{1224} \neq 0$; [P,Q] = $\lambdax^{2}$, $\lambda \neq 0$. GGHV Prop 4.3 case (2) = branches (a),(b); case (1), with the extra vertices (0,8)/(0,12), is branch (c) = NewtonNFc. Half-plane predicates (Lean `BranchAbNewton.lean`): inNP: $m_{0} \leq 8 \land m_{1} \leq 2m_{0} \land 2m_{0} \leq m_{1}+2$; inNQ: $m_{0} \leq 12 \land m_{1} \leq 2m_{0} \land 2m_{0} \leq m_{1}+3 \land m_{0} \leq 2m_{1}$.

## 1. S1 — the $\phi$-morphism (script `scripts/wsb_s1_phi.py`, log `logs/wsb_s1_phi.log`, exit 0; 11 PASS)

- Prop 4.3 case (2) polygons and the $\phi$ passage are present in the tex.
- Pre-$\phi$ polygons in tex: $P: (-1,0)$,(0,0),2(28,8),2(24,7); Q: (2,1),(0,0),3(28,8),3(24,7).
- The $\phi$-exponent map (i,j) ↦ $(4j-i,j)$ sends the pre-$\phi$ vertices exactly to the post-$\phi$ vertices for both P and Q; the case-(c) extra vertices 2(16,4) ↦ (0,8) and 3(16,4) ↦ (0,12).
- Chain rule for generic monomials with symbolic exponents (SymPy exact); $\det D\phi = -x^{2}$; chain rule for one random integer polynomial pair $(\deg \leq 4$, Laurent arithmetic, SymPy exact).
- **Second tool (Singular, `scripts/wsb_s1f_sing.sing`, log `logs/wsb_s1f_sing.log`, exit 0):** the monomial identity $[\phi(m_{1})$,$\phi(m_{2})] = \det(D\phi)\cdot\phi([m_{1},m_{2}])$ checked exhaustively over all $25 \times 47 = **1175$** monomial pairs from the NewtonNF2 lattice points: **0 failures**. (This also confirms |N(P)| = 25, |N(Q)| = 47 independently of S2.)

## 2. S2 — lattice data, Pick's theorem, predicates (script `scripts/wsb_s2_lattice.py`, log `logs/wsb_s2_lattice.log`, exit 0; 10 PASS)

- |$N(P) \cap \mathbb{Z}^{2}$| = 25, |$N(Q) \cap \mathbb{Z}^{2}$| = 47.
- Pick: N(P) area 15, boundary 18, interior 7 (15 = $7 + 18/2 - 1$ ✓); N(Q) area 33, boundary 26, interior 21 (33 = $21 + 26/2 - 1$ ✓).
- inNP/inNQ cut out exactly the polygon lattice sets over the bounding boxes; all 8 vertices satisfy the predicates; each predicate inequality is tight on a polygon edge $(i\leq8$ on (8,14)–(8,16); $j\leq2i$ on (0,0)–(8,16); \$2i\leqj+2\$ on (1,0)–(8,14); $i\leq12$ on (12,21)–(12,24); $j\leq2i$ on (0,0)–(12,24); \$2i\leqj+3\$ on (2,1)–(12,21); $i\leq2j$ on (0,0)–(2,1)).

## 3. S3 — the five layers (script `scripts/wsb_s3_layers.py`, log `logs/wsb_s3_layers.log`, exit 0; 26 PASS)

With u = xy${}^{2}$, $P = A_{0} + y^{-1}A_{1} + y^{-2}A_{2}$, $Q = B_{0} + y^{-1}B_{1} + y^{-2}B_{2} + y^{-3}B_{3} ($layer $k = 2i-j)$, layerTerm(a,b)(A,$B) = a\cdotA\cdotB' - b\cdotA'\cdotB$, and the bracket-of-layers identity $[y^{-a}A(u), y^{-b}B(u)] = y$^$(1-a-b)\cdot$layerTerm(a,b)(A,B):

- **S3a:** the bracket-of-layers identity holds symbolically for all 11 (a,b) pairs (SymPy exact, generic coefficient symbols).
- **S3b:** the decomposition identities (the $y^{k}$ coefficient of [P,Q] equals the stated sum of layerTerms) hold in 3 random specializations (coefficients in $[-100,100])$ for all five layers E5..E1; the coefficient counts are 17/18/19/19/19 (max over trials), total **92 equations**.
- **S3c:** layer supports and u-degree ranges: $A_{0} u^{0}$..$u^{8} (9)$, $A_{1} u^{1}$..$u^{8} (8)$, $A_{2} u^{1}$..$u^{8} (8)$, $B_{0} u^{0}$..$u^{12} (13)$, $B_{1} u^{1}$..$u^{12} (12)$, $B_{2} u^{2}$..$u^{12} (11)$, $B_{3} u^{2}$..$u^{12} (11)$; total **72 unknowns**; layer keys P={0,1,2}, Q={0,1,2,3}.
- **S3d:** degree-range count with the identically-vanishing extremes named: $E5 u^{2}$..$u^{19}$ minus the $u^{19}$ cancellation $(2\cdot12-3\cdot8=0) = 17$; $E4 u^{2}$..$u^{19} = 18 (u^{19}$ coefficient \$8$a_{814}b_{1222}-12a_{815}b_{1221}$\$ not identically zero); $E3/E2 u^{1}$..$u^{19} = 19$ each; $E1 u^{1}$..$u^{19} = 19 (u^{0}$ vanishes because layerTerm(0,1) has a=0, so the $A_{0}B_{1}'$ term drops and $A_{1}B_{0}'$ starts at $u^{1})$.
- **Second tool (Singular, `scripts/wsb_s3b_sing.sing`, log `logs/wsb_s3b_sing.log`, exit 0):** one fixed integer specialization (coefficients ((i+1)(j+2) mod 7)+1 on the supports; 25 terms of P, 47 of Q): **all five layer identities hold exactly** (differences 0). Extracted term counts: E5=17, E4=18, E3=19, E2=19, E1=11. The E1 count of 11 (vs the generic 19) is accidental cancellation in this single small-coefficient specialization; the generic count 19 rests on the SymPy max-over-3-trials. The identity — the load-bearing claim — holds in both tools.

The five layer identities (E5..E1) are therefore: E5: layerTerm$(2,3)(A_{2},B_{3}) = \lambdau^{2}$; E4: layerTerm$(2,2)(A_{2},B_{2})$+layerTerm$(1,3)(A_{1},B_{3}) = 0$; E3: layerTerm$(2,1)(A_{2},B_{1})$+layerTerm$(1,2)(A_{1},B_{2})$+layerTerm$(0,3)(A_{0},B_{3}) = 0$; E2: layerTerm$(2,0)(A_{2},B_{0})$+layerTerm$(1,1)(A_{1},B_{1})$+layerTerm$(0,2)(A_{0},B_{2}) = 0$; E1: layerTerm$(1,0)(A_{1},B_{0})$+layerTerm$(0,1)(A_{0},B_{1}) = 0$. (The vanishing $E4=\dots=E1=0$ and $E5=\lambdau^{2}$ is the content of [P,Q]=$\lambdax^{2}; S3$ checks the decomposition identity, which holds for arbitrary P,Q. The vanishing itself is checked at the $K_{5}$ point in S4/S5.)

## 4. S4 — the top layer E5 / Davenport–Stothers (script `scripts/wsb_s4_e5.py`, log `logs/wsb_s4_e5.log`, exit 0; 21 PASS; Singular elimination `scripts/wsb_s4_elim3.sing`, log `logs/wsb_s4_elim3.log`, exit 0)

With $\alpha = A_{2}/u$, $\beta = B_{3}/u^{2} (\deg 7$ and 10), E5 is $\alpha\beta + u(2\alpha\beta' - 3\alpha'\beta) = 1$.

- **S4a:** substitution identity: with $u = s^{2}$, $f(s) = \alpha(s^{2})$, $g(s) = s\beta(s^{2})$, 2fg$' - 3f'g = 2\cdot(\alpha\beta + u(2\alpha\beta' - 3\alpha'\beta))$ for generic $\alpha$, $\beta ($SymPy exact).
- **S4b:** degree relation $1+2n-3m = 0$ gives (m,n) = (1,1), (3,4), (5,7), (7,10).
- **S4c:** m = 1 solved explicitly: the $u^{2}$ coefficient of E5 vanishes identically and the solution set is the 1-parameter family $(b_{0}=1, b_{1}=2a_{1}/3)$, every member satisfying E5.
- **S4d (m = 3) and S4e (m = 5) — Singular triangular elimination.** The $E_{k}$ are triangular in the $b'$$s (E_{k} = (1+2k)b_{k}$ + terms in $b_{1}..b_{k-1}$ and the a's), so $b_{1}$..$b_{n}$ are computed successively as polynomials in $a_{1}$..$a_{m-1}$; the remaining equations constrain only the a's. A dp-order Gröbner basis of that small system gives:
  - m = 3: 2 constraint equations $(E_{5}, E_{6})$, both degree 3; dim 0, **degree 3** (3 solutions). reduce$(3a_{2}^{3}-32) = 0$, gcd(T,$T') = 1 ($separable, 3 distinct roots), reduce$(8a_{1}-5a_{2}^{2}) = 0 ($the chart iff relation), factorize(T) irreducible over $\mathbb{Q}$.
  - m = 5: 4 constraint equations $(E_{8}..E_{11})$, all degree 6; dim 0, **degree 10** (10 solutions). reduce$(9a_{4}^{10}+37200a_{4}^{5}+95051008) = 0$, gcd(T,$T') = 1 ($separable, 10 distinct roots), reduce of all three chart iff relations = $0 (362a_{4}a_{1}=3a_{4}^{5}+13078; 181a_{4}^{2}a_{2}=15a_{4}^{5}+32448; 2172a_{4}^{3}a_{3}=861a_{4}^{5}+492128)$, factorize(T) irreducible over $\mathbb{Q}$.
  - Generation of the elimination ideal by T follows from: $T \in I ($reduce = 0), T squarefree (gcd(T,$T') = 1)$, degree(system) = deg T (3, resp. 10), and T has deg T distinct roots — so the elimination ideal is the principal ideal (T) (see §9, assumption A4). The m = 5 irreducibility is confirmed a third way by the a816 bundle's flint check (factor_list(T) = irreducible; T irreducible mod 11, degree 10 kept $\to$ irreducible over $\mathbb{Q})$.
- **S4f (m = 7 eliminant W, from `branch_ab_v19/scripts/e5_m7.out`, msolve output):** $W(a_{6})$ has degree 35 (36 coefficients parsed by regex — the file is not a plain Python literal: trailing `:` and `/ 2^127` interval fractions later on); all nonzero exponents are 0, 7, 14, 21, 28, 35, so $W = V(a_{6}^{7})$ with V a quintic; V irreducible over $\mathbb{Q} ($SymPy factor_list); disc$(V) \neq 0 ($separable; the discriminant is a 400-digit integer, quoted in the log); V has exactly one real root (Sturm count), real root $\approx 3208.612478738048; W$ irreducible over $\mathbb{Q} ($SymPy factor_list); W separable mod 101 (gcd(W,$W') = 1$ in 𝔽${}_{101})$.
- **S4g (Belyi identity$):** \phi = u\beta^{2}/\alpha^{3}$ satisfies $\phi'\cdot\alpha^{4} = \beta\cdotE5$lhs as a polynomial identity (SymPy exact expansion, no E5 assumed), via the product rule d/du$(u\beta^{2}) = \beta^{2} + 2u\beta\beta' ($checked separately) and the power rule for $\alpha^{-3}$. Hence $\phi' = \beta/\alpha^{4}$ whenever E5 holds with value 1.
- **S4h (the $K_{5}$ point satisfies E5 exactly):** with $A_{2}$, $B_{3}$ from the paper's topA/topB (Lean `BranchAbSharp.lean`), layerTerm$(2,3)(A_{2}$,$B_{3}) = u^{2}$ exactly over $K_{5} = \mathbb{Q}[w]/(R), R = w^{5}-w^{4}+3w^{3}+3w^{2}+26 ($SymPy, coefficients reduced mod R). $\alpha(0) = \beta(0) = 1 ($roots nonzero); $\gcd(\alpha$,$\beta) = 1, \gcd(\alpha$,$\alpha') = 1, \gcd(\beta$,$\beta') = 1$ over $K_{5} ($Euclidean algorithm in the independent $K_{5}$ implementation, `scripts/wsb_k5.py`); 2fg$'-3f'g = 2$ at the point (coefficients reduced mod R); **$\deg(g^{2} - c\cdotf^{3}) = 8 = k+1$** with $c = B^{2}/a_{7}^{3} (B$ = leading coefficient of $\beta$, $a_{7}$ = leading coefficient of $\alpha)$, nonzero degrees {8,6,4,2,0} — Davenport's bound, the pair is extremal. (On the constant c, see §8 item 4: the degree claim needs the leading-coefficient ratio, not the Wronskian constant 2.)
- **R(w) is irreducible over $\mathbb{Q}** ($SymPy factor_list: single factor, exponent 1) and separable (discriminant $\neq 0)$, so $K_{5}$ is a field. (Checked 2026-11-10 during this workstream; not in a script file — the one-line SymPy call is quoted here.)

## 5. S4-chart — the chart system and the $K_{5}$ chart point (script `scripts/wsb_s4_chart.py`, log `logs/wsb_s4_chart.log`, exit 0; 14 PASS)

Parsed programmatically (regex) from Lean `branch_ab_v19/lean/Jacobian/BranchAbChart.lean` — the witness fractions are never hand-transcribed.

- **S4c1:** the 16 Lean $E_{n}$ antecedents are exactly the coefficients $E_{n} = \Sigma_{i+k=n}(1+2k-3i)a_{i} b_{k} (n = 1..16)$ of $\alpha\beta + u(2\alpha\beta'-3\alpha'\beta)$, with $a_{0} = b_{10} = 1$ substituted $(\alpha = 1+a_{1}u+\dots+a_{7}u^{7}, \beta = b_{0}+\dots+b_{9}u^{9}+u^{10})$; the 17th antecedent is $a_{7}^{3}b_{0}^{2} = 1$; $E_{17}$ vanishes automatically $(1+2\cdot10-3\cdot7 = 0)$.
- **S4c2:** the parsed witness $(P_{j}$ for $a_{1}..a_{7}, Q_{k}$ for $b_{0}..b_{9})$ satisfies $E_{1}$..$E_{17} = 0$ exactly over $K_{5} (E5$lhs is the constant $b_{0})$ and **$a_{7}^{3}b_{0}^{2} = 1$** exactly over $K_{5}$.
- **S\$4$c3:** \kappa = B^{2}/a_{7}$^{3}\$ from the raw top point (B = topB[12], $a_{7}$ = topA[8]) equals the $\kappa$ element stated in `chart_K5_identities`; the witness is the $\kappa$-rescaling of the raw point: $a_{j} = \kappa^{j}\cdot$topA[j+1] (j = 1..7) and $b_{k}\cdot\kappa$^$(10-k)\cdotB$ = topB[k+2] (k = 0..9). (This resolves the apparent tension in §8 item 4: the raw witness has $a_{7}^{3} \neq 1$ because it is not in the chart normalization — $\beta_{10} = B \neq 1$. The chart point is the $\kappa$-rescaling, and it is the chart point that satisfies $a_{7}^{3}b_{0}^{2} = 1.)$
- **S4c4:** the inversion certificates in `chart_K5_identities` hold: $\kappa\cdot(64479051/1257728 + \dots) = 1$ and $B\cdot(26267455159/283855104 + \dots) = 1$ over $K_{5}$.

## 6. S5 — the descent $E4 \to E3 \to E2 ($script `scripts/wsb_s5_descent.py`, log `logs/wsb_s5_descent.log`, exit 0; 20 PASS)

Rebuilt from scratch in the independent pure-Python $K_{5}$ implementation (`scripts/wsb_k5.py`, Fractions-based, not a copy of the repo's Singular/flint code), starting only from the top-layer point (topA/topB) and the layer definitions. Second tool for the $K_{5}$-point and descent claims.

- **S5a:** E5 re-checked: layerTerm$(2,3)(A_{2},B_{3}) = u^{2}$ over $K_{5} ($independent implementation).
- **S5b (E\$4$):** 18\times19$\$ matrix (rows $u^{2}..u^{19}$; cols $A_{1} u^{1}..u^{8}, B_{2} u^{2}..u^{12})$, **rank 17, kernel dim 2** (parameters $t = (t_{1},t_{2}))$; both kernel basis vectors satisfy E4 exactly.
- **S5c (E\$3$):** 19\times20$\$ matrix (rows $u^{1}..u^{19}$; cols $A_{0} u^{1}..u^{8}$ — $a_{00}$ never appears, since layerTerm(0,3) uses only $A_{0}'$ — and $B_{1} u^{1}..u^{12})$, **rank 18, kernel dim 2** (parameters $s = (s_{1},s_{2}))$; left kernel dim 1; the E3 right-hand side is quadratic in t and **vᵀ$K_{11} = v$ᵀ$K_{12} = v$ᵀ$K_{22} = 0$**, so E3 is solvable for every t; particular solutions $x_{11}$, $x_{12}$, $x_{22}$ exist (one verified to satisfy E3 with residual 0).
- **S5d (E2):** the operator layerTerm$(2,0)(A_{2},B_{0}) = 2A_{2}B_{0}'$ is $a 19\times12$ matrix (unknowns $B_{0}$'$s u^{1}..u^{12}$ coefficients), **rank 12 (injective)**, left kernel dim **7**. The seven compatibility conditions have the form $b_{i}(t) + s_{1}M_{i}(t) + s_{2}L_{i}(t) = 0$ with $b_{i}$ cubic and $M_{i}$, $L_{i}$ linear in t. The **\$35** $3\times3$\$ minors of the $7\times3$ matrix [b|M|L] are homogeneous binary quintics; their $35\times6$ coefficient matrix has **rank 6** (spans $K_{5}[t_{1},t_{2}]_{5})$; the stored certificate matrix (`branch_ab_v19/logs/k5_minor_certificate.json`, $35\times6$, rank claimed 6, pivot rows [0,1,2,3,5,6]) independently has rank 6; and the rebuilt minors and the stored minors have the **same row space** (stacked rank 6). This is a full rebuild of the minors from the E2 compatibility conditions, not merely a re-check of the stored matrix.
- **S5e (t = 0 collapse):** the E2 right-hand side has no constant term (vanishes at t = s = 0); with rhs = 0, E2 reads $M_{2}x = 0$, whose unique solution is $x = 0 (M_{2}$ injective), so $B_{0}' = 0$, $B_{0}$ is constant, and **$b_{12}$,${}_{24} = 0** (B_{0}$'$s u^{12}$ coefficient; the $b_{12}$ column is $2\cdot12\cdotA_{2}\cdotu^{11}$, nonzero since $24 \neq 0$ in $K_{5}$, char 0). Hence the vertex coefficient $b_{12}$,${}_{24}$ vanishes, contradicting NewtonNF2 — the (a),(b) case is excluded. (Corollary $a_{8},{}_{16} = 0$ and the a816 certificate are covered in §7.)

## 7. The a816 certificate (repo bundle, log `logs_a816_bundle.txt`; ALL CHECKS PASSED)

The supplementary explicit identity $a_{8}$,${}_{16}^{2} = \Sigma_{k=1}$^{75} $H_{k} e_{k}$ over $K_{5} (76$ cofactors in Rabinowitsch form, 3464 terms, 10.65 MB, `branch_ab_v19/scripts/a816_certificate/a816_lift.txt`) was re-verified by the repo's `verify_bundle.sh` (background PID 23973, finished 2026-11-10):

- Source `a816_full.sing` md5 aa68d2ffa08a8db86627a03e41f4e94d. Note: `a816_lift_liftstd.txt` is NOT present (not committed, per README §2) — so only the main certificate was re-verified, not the second one.
- python-flint independent rebuild of J: 76 cofactors, 3464 terms, $F = \Sigmac_{k} g_{k} + c_{76}(a_{8},{}_{16}z-1) - 1$ has 24444 terms before reduction mod R(w); **F == 0 mod R(w): VALID**, 6.7 s, exit 0.
- Negative controls all rejected as required: perturb (10 terms remain, exit 1), drop_rabinowitsch (2 terms remain, exit 1), wrong_minpoly (10864 terms remain, exit 1).
- Singular over $\mathbb{Q}(w)$: VALID; round trip with CAIC's generators: VALID; CAIC generators vs repository ideal, entrywise mismatches: 0.
- B2.6 eliminant checks: factor_list(T) over $\mathbb{Q} = (1, [(9a^{10}+37200a^{5}+95051008, 1)])$ — irreducible; disc_$u = -2037996288$; T irreducible mod 11 (degree 10 kept$) \to$ irreducible over $\mathbb{Q}$.

## 8. Limiting cases (S6; script `scripts/wsb_s6_limits.py`, log `logs/wsb_s6_limits.log`, exit 0; 10 PASS)

- **$\lambda = 0 (S6a)$:** the degenerate family $\alpha(u) = u(u-1)^{6}$, $\beta(u) = u(u-1)^{9}$ satisfies 2fg$'-3f'g = 0$ and $g^{2} = f^{3} (c = 1)$, while E5lhs $\equiv 0 ($not 1), so it does NOT satisfy E5 = 1. It has $\alpha(0) = 0$ and $\beta(0) = 0$, so the chart normalizations $\alpha(0) = 1$ and $a_{7}^{3}b_{0}^{2} = 1$ exclude it. The $\lambda \neq 0$ hypothesis is load-bearing: at $\lambda = 0$ the top layer collapses to the degenerate locus.
- **$a_{7} = 0 (S6b)$:** substituting $a_{7} = 0$ into the chart equations, $E_{16}$..$E_{11}$ force $a_{6} = \dots = a_{1} = 0$ successively (coefficients 3, 6, 9, 12, 15, 18), and $E_{10}$ then reduces to **21 = 0**, a contradiction; $a_{7}^{3}b_{0}^{2} = 1$ already fails at $a_{7} = 0$. So the chart system has no solution with $a_{7} = 0$.
- **Characteristic 2 and 3 (S6c):** the chartproof S-recursion step \$2k\cdotS_{k}\$ breaks in characteristic 2 (2k = 0 mod 2 for all k); the $a_{7} = 0$ cascade coefficients 3, 6, 9, 12, 15, 18 all vanish mod 3, so the cascade breaks in characteristic 3. The derivation is characteristic-0 throughout (and the Lean `ChartClassification` carries a `CharZero` hypothesis, matching this).
- **Characteristic p, Gröbner dim/degree (NOT RUN):** the dim/degree of the 16 chart equations + $a_{7}^{3}b_{0}^{2} = 1$ over 𝔽${}_{101} ($control), 𝔽${}_{3}$, 𝔽${}_{5}$, 𝔽${}_{7}$ was attempted in Singular (`scripts/wsb_s6charp.sing`, log `logs/wsb_s6charp.log`) but did not finish even p = 101 in 570 s (263 s CPU; the log holds only `p = 101: #equations = 17`). Costed plan: the 17-variable bilinear Gröbner basis needs a faster machine (e.g. lean-build-4's 24 cores once leg-9 ends — never while it runs), a longer wall-clock budget (estimate: several hours at the throttled local rate, unmeasured), or a smarter method (msolve, or the S-recursion/torus route used by the Lean proof). The char-0 derivation does not depend on this check.

## 9. Discrepancies, errors found, and corrections (no silent correction)

No discrepancy against the Lean elimination or the paper was found. Every failure encountered was my own script or tooling error, or a misidentification of mine. Each is recorded here with its evidence and fix.

1. **S1 regex bugs (mine).** Two initial FAILs were doubled backslashes in a regex and a real TAB after `\;` in the tex. Fixed by line-based matching. The underlying claims were confirmed independently by the pdftotext source gate (PASS).
2. **S3 errors (mine).** (a) The first S3b script subtracted $\lambdau^{2}$ from the predicted E5 layer coefficient — wrong: the decomposition identity compares the raw $y^{-4}$ coefficient against layerTerm$(2,3)(A_{2},B_{3})$ with NO subtraction; the equality layerTerm = $\lambdau^{2}$ is the content of [P,Q] = $\lambdax^{2}$, which does not hold for random P,Q. (b) Coefficient counts used random integers in $[-5,5]$, letting genuinely nonzero coefficients accidentally vanish (E1 trial 0, E4 trial 1). Fixed: no subtraction, range $[-100,100]$, 3 trials, max count over trials, identity checked per trial separately. (c) My hand-count of the layer equations was 93; corrected to 92 (layerTerm(0,1) has a = 0, so the $A_{0}B_{1}'$ term drops and E1'$s u^{0}$ coefficient is 0).
3. **S4g slowness (mine).** Differentiating the rational function $\phi = u\beta^{2}/\alpha^{3}$ and expanding ran 570 s and was killed by timeout (242 s CPU; buffered output lost). Replaced by the quotient-rule-free polynomial identity (verified by expansion) plus the product-rule step checked separately. S4 now runs in ~3 s.
4. **S4h errors (mine).** (a) The c-check (`2fg′−3f′g = 2`) failed because the SymPy coefficients in w were not reduced mod R(w) before testing; the raw coefficients are nonzero polynomials in w that vanish mod R. The $K_{5}$ computation confirms c = 2. (b) The degree check used c = 2 (the Wronskian constant 2fg$'-3f'g)$. That is the WRONG c for the degree claim: $\deg(g^{2}-c\cdotf^{3}) = 8$ needs $c = B^{2}/a_{7}^{3}$, the leading-coefficient ratio (B = leading coefficient of $\beta$, $a_{7}$ of $\alpha)$. With c = 2 the degree is 42, not 8. The paper (line 480) writes "$\deg(g^{2}-c\cdotf^{3})=8$" where c is the Davenport constant making the leading terms cancel; my plan's "c = 2" was my own misidentification, not a paper error. With $c = B^{2}/a_{7}^{3}$ the degree is 8, nonzero degrees {8,6,4,2,0}. (c) Relatedly, $a_{7}^{3} \neq 1$ for the RAW witness (topA/topB) is NOT a discrepancy: the raw witness is not in the chart normalization $(\beta_{10} = B \neq 1)$. The chart point is the $\kappa$-rescaling $\kappa = B^{2}/a_{7}^{3}$, and S4c3 verifies $a_{7}^{3}b_{0}^{2} = 1$ for the chart witness.
5. **S5 E2 column error (mine).** The first S5d used $B_{0} = u^{0}$..$u^{11}$ as the E2 unknowns, dropping the $b_{12}$ column and keeping the constant-$B_{0}$ zero column; it reported rank 11 and left-kernel dim 8, contradicting the paper's rank 12 / 7 conditions. The correct unknowns are $B_{0}$'$s u^{1}$..$u^{12}$ coefficients $(B_{0}$'$s u^{0}$ coefficient never appears, since only $B_{0}'$ matters). Fixed to j = 1..12: rank 12, left-kernel dim 7. (Notably, the 35 minors built from 7 of the wrong 8 left-kernel vectors still spanned and matched the stored certificate; that result was not relied on — the corrected computation was re-run in full.)
6. **S4-chart parse off-by-one (mine).** Splitting the Lean antecedents on "$\to$" dropped the first equation (it sits in front of the first "$\to$"). Fixed by splitting after the $\forall$ binder. All \$16 $E_{n}$\$ then matched the coefficient formula exactly.
7. **Singular `continue` hang (tooling).** Singular 4.4.1 (conda-forge) HANGS on `continue` inside a for-loop in this environment (verified by bisection 2026-11-10: a 5-line loop with `continue` never terminates in 30 s; the same loop with if/else finishes in 0.1 s). This killed three runs: the first full elimination (`scripts/wsb_s4_elim.sing`, log empty), the triangular elimination (`scripts/wsb_s4_elim2.sing`, log empty), and delayed diagnosis. All elim scripts were rewritten without `continue`; the triangular elimination then finished in 0.3 s. The empty logs `logs/wsb_s4_elim.log` and `logs/wsb_s4_elim2.log` are the killed runs, superseded by `logs/wsb_s4_elim3.log`. **Flag for the parent: this quirk belongs in `TOOLS.md` (Singular `continue` hangs; use if/else).** Also note: `a1^2/21` in Singular parses as `a1^(2/21)` (`^` binds tighter than `/`) — a hard-coded test failed on this; generated scripts use integer coefficients and are unaffected.
8. **Char-p Gröbner timeout (tooling limit, not a failure of the claim).** See §8, last bullet, and §11.
9. **S3b Singular E1 count (not a discrepancy).** The single Singular specialization shows E1 with 11 nonzero terms (vs the generic 19) from accidental cancellation with small coefficients; the identity holds exactly and the generic count 19 rests on the SymPy max-over-3-trials.

## 10. Evidence that would change the answer

- A nonzero residual in any layer identity, in E5 at the $K_{5}$ point, or in any of the 17 chart equations at the parsed witness (all are exactly 0).
- The E2 35-minor matrix having rank < 6, or its row space differing from the stored certificate's (rank is 6; row spaces coincide).
- A root w of R(w) at which the $K_{5}$ point fails E5 (the point satisfies E5 exactly over $K_{5}$, i.e. uniformly in w).
- The m = 3 / m = 5 eliminants failing to lie in the constraint ideal, or being reducible (reduce = 0, gcd(T,$T') = 1$, factorize irreducible — all hold).
- A Lean kernel failure in `main_theorem` (outside this workstream; the Lean result is Grade A and is not re-checked here).
- The char-p Gröbner computation (if run) showing the chart system has solutions over 𝔽_p that do not lift to characteristic 0 — that would affect the characteristic-p scope only, not the characteristic-0 derivation.

## 11. Check summary

| Step | Script | Log | Result |
|---|---|---|---|
| Source gate | `branch_ab_v19/scripts/source_gate_verify.py` | — | PASS, exit 0 |
| $S1 \phi$-morphism | `scripts/wsb_s1_phi.py` | `logs/wsb_s1_phi.log` | 11 PASS, exit 0 |
| S1f monomial chain rule (Singular) | `scripts/wsb_s1f_sing.sing` | `logs/wsb_s1f_sing.log` | 1175 pairs, 0 failures, exit 0 |
| S2 lattice/Pick/predicates | `scripts/wsb_s2_lattice.py` | `logs/wsb_s2_lattice.log` | 10 PASS, exit 0 |
| S3 layers | `scripts/wsb_s3_layers.py` | `logs/wsb_s3_layers.log` | 26 PASS, exit 0 |
| S3b layers (Singular) | `scripts/wsb_s3b_sing.sing` | `logs/wsb_s3b_sing.log` | 5 identities PASS, exit 0 |
| S4 E5/Davenport–Stothers | `scripts/wsb_s4_e5.py` | `logs/wsb_s4_e5.log` | 21 PASS, exit 0 |
| S4d/S4e elimination (Singular) | `scripts/wsb_s4_elim3.sing` | `logs/wsb_s4_elim3.log` | m=3 deg 3, m=5 deg 10, all reduce/gcd/factorize as expected, exit 0 |
| S4-chart system + witness | `scripts/wsb_s4_chart.py` | `logs/wsb_s4_chart.log` | 14 PASS, exit 0 |
| S5 descent | `scripts/wsb_s5_descent.py` | `logs/wsb_s5_descent.log` | 20 PASS, exit 0 |
| S6 limiting cases | `scripts/wsb_s6_limits.py` | `logs/wsb_s6_limits.log` | 10 PASS, exit 0 |
| S6 char-p GB (Singular) | `scripts/wsb_s6charp.sing` | `logs/wsb_s6charp.log` | **NOT RUN** (timeout 570 s; see §8) |
| a816 certificate bundle | repo `verify_bundle.sh` | `logs_a816_bundle.txt` | ALL CHECKS PASSED |

Tool versions (quoted verdicts): Python 3.11.16, SymPy 1.14.0, python-flint 0.8.0, Singular 4.4.1 (`Singular --version < /dev/null`, exit 0). Conda env `~/miniconda3/envs/jacobian-conjecture-2d`. No Lean builds were run in this workstream (none needed — the Lean kernel verification is already on record as Grade A); no GCP compute was used; lean-build-4 was not touched; no repo commits, pushes, filing, or manuscript edits were made.

## 12. VERIFIED / UNVERIFIED / FAILED

**VERIFIED** (each by exact symbolic computation; grades in §13):

- V1. The $\phi$-morphism, its determinant, the chain rule, and the pre-$\phi \to$ post-$\phi$ polygon map (S1, S1f).
- V2. The Newton polygon lattice data, Pick's theorem values, and the half-plane predicates cutting out exactly the polygon lattice sets, with each inequality tight on an edge (S2).
- V3. The bracket-of-layers identity, the five-layer decomposition, the 92 coefficient equations, the 72 unknowns, and the layer supports/degree ranges (S3, S3b-Singular).
- V4. The E5 substitution identity, the degree relation, the m = 1 one-parameter family, and the m = 3 / m = 5 eliminants with their solution counts (3, 10), separability, irreducibility, and chart iff relations (S4a–S4e).
- V5. The m = 7 eliminant W (degree 35, quintic in $a_{6}^{7}$, irreducible, separable, exactly one real root $\approx 3208.612478738048)$ and the Belyi identity $\phi'\cdot\alpha^{4} = \beta\cdotE5$lhs (S4f, S4g).
- V6. The $K_{5}$ top-layer point satisfies E5 exactly; $\alpha$, $\beta$ are separable and coprime; 2fg$'-3f'g = 2$; $\deg(g^{2}-(B^{2}/a_{7}^{3})f^{3}) = 8 ($Davenport bound, extremal) (S4h).
- V7. The 16 Lean chart equations are exactly the E5 coefficient equations; the parsed chart witness satisfies all 17 chart equations; $\kappa = B^{2}/a_{7}^{3}$ and the witness is the $\kappa$-rescaling of the raw point; the $\kappa$ and B inversion certificates hold (S4-chart).
- V8. The descent: E4 rank 17 / kernel dim 2; E3 rank 18 / kernel dim 2 and solvable for every t; E2 operator rank 12 (injective) with 7 compatibility conditions; the 35 minors span $K_{5}[t_{1},t_{2}]_{5}$ and their row space equals the stored certificate's; the t = 0 collapse forces $b_{12}$,${}_{24} = 0 (S5)$.
- V9. The a816 certificate $(a_{8},{}_{16}^{2} = \Sigma H_{k} e_{k}$ over $K_{5})$ re-verifies, with all negative controls rejected (§7). Note: only the main certificate; the second certificate `a816_lift_liftstd.txt` is not committed and was not re-verified.
- V10. Limiting cases: the $\lambda = 0$ degenerate family (E5lhs $\equiv 0, g^{2} = f^{3}$, excluded by $\alpha(0) = 1)$; the $a_{7} = 0$ cascade $(E_{10}$ gives 21 = 0); the characteristic-2 S-recursion break and the characteristic-3 cascade break (S6).

**UNVERIFIED** (ABSTAIN — not claimed):

- U1. Characteristic-p Gröbner dim/degree of the chart system over 𝔽${}_{101}$, 𝔽${}_{3}$, 𝔽${}_{5}$, 𝔽${}_{7} ($NOT RUN — timed out; costed plan in §8).
- U2. The second a816 certificate (`a816_lift_liftstd.txt`) — not committed in the repo, so not re-verified here.
- U3. The GGHV exhaustiveness and the reduction chain on which the unconditional exclusion of (72,108) rests — out of scope for this workstream; the Lean elimination is conditional on them per the programme record.
- U4. The m = 7 classification's completeness argument via Riemann's existence theorem / the msolve parametrization ("35 exhibited points") — the eliminant W is verified (V5); the Belyi-bound completeness step itself is not re-derived here.

**FAILED:** (none). No claim failed. The failures encountered were script/tooling errors of mine, all corrected and listed in §9.

## 13. HLRE grades per narrow claim (Track F; worst-of computation shown)

Grading convention: Track F for deductive claims (F1 = kernel-verified in Lean — not claimed here; F2 = machine-checked by exact symbolic computation with a second independent tool; F3 = machine-checked with a single tool, or hand-checked). Independence I0–I4 (I1 = single tool; I2 = second independent tool; I3 = second independent tool + independent derivation). The grade of a composite claim is the worst (lowest) grade among its supporting checks.

| Claim | Grade | Independence | Basis (worst-of) |
|---|---|---|---|
| $C1 \phi$-morphism (V1) | F2 | I2 | SymPy exact + Singular 1175 monomial pairs |
| C2 lattice/Pick/predicates (V2) | F2 | I1 | Counts confirmed in two tools (SymPy + Singular enumeration); Pick areas and predicate-tightness are SymPy-only $\to I1$ governs |
| C3 layer decomposition, 92 equations (V3) | F2 | I2 | SymPy general identity + 3 specializations + Singular specialization (5 identities); E1 generic count rests on SymPy trials |
| C4 E5 eliminants m=1,3,5 (V4) | F2 | I2 | Singular triangular elimination + SymPy factor; m=5 irreducibility also by flint (bundle) |
| C5 m=7 eliminant W, Belyi identity (V5) | F2 | I1 | W's properties (irreducibility, discriminant, real-root count, separability mod 101) and the Belyi identity are SymPy-only; W itself is single-source (the msolve output file$) \to I1$ governs |
| $C6 K_{5}$ point, Davenport bound (V6) | F2 | I2 | SymPy mod-R + independent $K_{5}$ implementation (wsb_k5.py) |
| C7 chart system + witness (V7) | F2 | I2 | Lean file parsed programmatically + $K_{5}$ arithmetic in wsb_k5.py; the witness values are file data, the verification is the computation |
| C8 descent, 35 minors, $b_{12}$,${}_{24} = 0 (V8)$ | F2 | I3 | Rebuilt from scratch in an independent $K_{5}$ implementation (independent derivation + independent tool); row space matches the stored certificate |
| C9 a816 certificate (V9) | F2 | I2 | python-flint rebuild + Singular over $\mathbb{Q}(w)$ + negative controls (repo bundle script) |
| C10 limiting cases (V10) | F2 | I1 | SymPy only (char-p GB NOT RUN) |

**Overall: Track F, grade F2, independence I1 (worst-of across C1–C10).** The I1 is driven by C2 (Pick areas / predicate-tightness) and C10 (limiting cases), which rest on a single tool. Nothing here is F1 (kernel-verified) — that grade belongs to the Lean `main_theorem` alone and is not claimed by this symbolic cross-check. Nothing is stated beyond these grades.

## 14. Ledgers

**Assumptions.**
- A1. GGHV Prop 4.3 case (2) polygons and the $\phi$-morphism are as stated in the v1 paper (verified against the PDF extraction and the tex — source gate PASS).
- A2. The Lean `BranchAb` material (topA/topB, chart witness, chart equations) is as in `branch_ab_v19/` (the chart witness and equations are parsed from the file; topA/topB in `wsb_k5.py` / `wsb_s4_e5.py` were transcribed from the paper/Lean and are cross-validated by the E5 checks and the $\kappa$-relations in S4c3 — a transcription error there would break E5, which passes exactly twice).
- A3. $R(w) = w^{5}-w^{4}+3w^{3}+3w^{2}+26$ is irreducible over $\mathbb{Q} ($verified: SymPy factor_list, single factor; discriminant $\neq 0)$, so $K_{5}$ is a field of characteristic 0.
- A4. The elimination-ideal generation argument for S4d/$S4e (T \in I, T$ squarefree, degree(system) = deg T, T has deg T distinct roots $\Rightarrow I \cap \mathbb{Q}[a] = (T))$ — a standard consequence; the three premises are machine-checked, the implication is deductive.
- A5. The msolve output file `e5_m7.out` is the eliminant computation it claims to be (its first polynomial is verified to have the stated properties; the computation itself is not re-run here).

**Parameters.**
- $\lambda$: the bracket constant, [P,Q] = $\lambdax^{2}$, $\lambda \neq 0 ($normalized to 1 in the chart/E5; the raw witness has $\lambda = 1)$.
- w: any root of R (all checks are over $K_{5}$, i.e. uniform in w).
- $\kappa = B^{2}/a_{7}^{3}$: the chart rescaling (torus normalization) taking the raw top point to the chart point.
- $t = (t_{1},t_{2})$: the E4 kernel parameters; $s = (s_{1},s_{2})$: the E3 kernel parameters. The descent conclusion $(b_{12},{}_{24} = 0)$ holds for all t, s (the 35 minors span, forcing t = 0, and then s = 0).

**Choices.**
- SymPy 1.14.0 for symbolic identities and exact rational arithmetic; Singular 4.4.1 for independent cross-checks (monomial chain rule, layer specialization, eliminations, char-p attempt); a from-scratch pure-Python $K_{5}$ implementation (`scripts/wsb_k5.py`, Fractions-based) for the descent rebuild and the gcd/separability checks.
- The chart witness and equations are parsed from the Lean file by regex (never hand-transcribed); topA/topB are transcribed (validated as in A2).
- No Lean builds, no GCP compute, no repo commits/filing/manuscript edits in this workstream, per the programme brief.

## 15. Citation record

- GGHV paper v1: arXiv:2204.14178v1, PDF `~/workspace/user/files/2204.14178v1__2__3_ov75.pdf`; tex `~/workspace/research/rss-monitor/tex/2204.14178/main.tex` (Prop 4.3, $\phi$ at tex line 1229).
- Combined paper: `~/workspace/combined-paper/combined_paper_final_2026-11-04.tex` (Part I; E5 §ab:sec:top line 468–480; chartproof line 689; descent §ab:sec:descent).
- Lean: `~/workspace/research/2D-Jacobian-Conjecture-Workspace/branch_ab_v19/lean/Jacobian/BranchAbChart.lean` (465 lines; `ChartClassification`, `chart_K5_identities`, `chart_point_solves`), `BranchAbSharp.lean` (topA/topB), `BranchAbLayers.lean` (layers_of_jac), `BranchAbNewton.lean` (inNP/inNQ).
- Data: `branch_ab_v19/scripts/e5_m7.out` (msolve output, 2661 bytes); `branch_ab_v19/scripts/a816_certificate/a816_lift.txt` (76 cofactors, 3464 terms, 10.65 MB); `branch_ab_v19/logs/k5_minor_certificate.json` $(35\times6$, rank 6, pivot rows [0,1,2,3,5,6]).
- Davenport: H. Davenport, "On $f^{3}(t)-g^{2}(t)$", Det Kongelige Norske Videnskabers Selskabs Forhandlinger 38 (1965), 86–87 (combined paper bibitem Davenport).
- This workstream's deliverables: `~/workspace/research/irh/co-scientist-tasks-2026-11-10/ws-b-branch-normal-form/` — `REPORT.md` (this file), `scripts/` (wsb_s1_phi.py, wsb_s2_lattice.py, wsb_s3_layers.py, wsb_s4_e5.py, wsb_s4_chart.py, wsb_s4_elim.sing, wsb_s4_elim2.sing, wsb_s4_elim3.sing, wsb_s5_descent.py, wsb_s6_limits.py, wsb_s6charp.sing, wsb_s1f_sing.sing, wsb_s3b_sing.sing, wsb_k5.py), `logs/` (all run logs), `logs_a816_bundle.txt`. The S4d/S4e results are recorded in `logs/wsb_s4_elim3.log` (quoted in §4); there is no separate checker script for them.

## 16. Follow-ups for the parent agent

1. **TOOLS.md:** Singular 4.4.1 (conda-forge) hangs on `continue` inside a for-loop in this environment (verified by bisection). Recommend recording: avoid `continue` in Singular loops; use if/else. Also: `a^b/c` in Singular parses as `a^(b/c)` — parenthesize powers before dividing.
2. **Char-p GB (U1):** needs a faster machine or a smarter method; candidate: run on lean-build-4 (24 cores) after leg-9 ends, or via msolve. Do not run while leg-9 is active.
3. **Second a816 certificate (U2):** `a816_lift_liftstd.txt` is not committed; if Brandon wants it re-verified, it needs to be produced/committed first.
4. Nothing in this workstream changes any grade, file, or repo state. No action is requested of Brandon.
