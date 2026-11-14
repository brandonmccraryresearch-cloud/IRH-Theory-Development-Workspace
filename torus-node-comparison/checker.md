# Checker report — "A Torus-Node Model for Emergent Spacetime, Gravity, and Gauge Structure" (Youngik (Tom) Lee)

**Mode (stated plainly):** deepest-research **FULL mode**. **NOT systematic-review mode** — that form was not chosen.
**Skills:** `/deepest-research` (full) + `/cross-domain-discovery` v2.0.0 (stages S1–S7, applied as: S1 claim registration before checking; S2 retrieval from the extracted text; S3 structural/symbolic alignment by runnable tools; S4 Bartha/transport audit — not applicable beyond noting where a transfer is asserted without its prior association; S5/S6 blending and tournament — not applicable to a checker task, no candidate was generated or evolved; S7 formal verification — exact symbolic/numeric checks run as tools, Lean/Z3 not used because the claims checked are arithmetic identities, not formal proofs) + `/truth-seeking-frontier` v5 (computation gate: every load-bearing number below carries a quoted tool verdict with version, script, and exit code; above CLAIMED a second independent tool was used where stated; ABSTAIN used as UNVERIFIED where the text does not supply the inputs) + `/hlre-v5-1` (grades per narrow claim; "derives" reserved for deductive results; these checks are Track F arithmetic, graded F2 where a second independent tool confirmed the result, F3 where single-route; the paper's own headline numbers that depend on unstated inputs are INCOMPLETE-EVIDENCE, carrying no grade; independence of this check is I1 — artificial verification by one checker agent, no human source/balance gate performed).

**Source checked:** `~/workspace/research/irh/torus-node-comparison/torus_node_model.txt` (9,583 lines, extracted text). All section/equation/line references are to that file. I worked independently of the readers: every equation and input below was read from the text as written.

**Tools (tool inventory, run 2026-11-11):** `~/miniconda3/envs/jacobian-conjecture-2d/bin/python` — Python 3.11.16, SymPy 1.14.0, numpy 2.4.6, scipy 1.17.1, mpmath 1.4.1, python-flint 0.8.0 (flint available, not needed). System `python3` was NOT used. No GCP spend, no VM work, no repo commits, no manuscript edits, no filing, no contact with the author, Gemini grader NOT called.

**Scripts (all under `~/workspace/research/irh/torus-node-comparison/checks/`):**

| Script | Covers | Exit code |
|---|---|---|
| `check_d4.py` | D4 counts, H matrix, Hurwitz integers, spherical designs, Weyl groups, S4/P spectrum, Prop 13.2, finite-model counts, Lemma 4.10 | 0 |
| `check_anomaly.py` | Anomaly traces, charges, catalogue counts, strong sector, Prop 6.7 | 0 |
| `check_gravity.py` | Prop 5.8/5.10, eq. (5.5), entropy ratio R, Num. result 13.4, Table 18, curvature bound | 0 |
| `check_matching.py` | Table 16 axion masses, mt margin, eq. (13.6) 1-loop cross-check, eqs. (13.7)/(13.8), $\alphas$ running, lepton fit (13.9), Prop 9.19 | 0 |
| `check_misc.py` | §9 electroweak numerics, eqs. (9.11)–(9.18), §17.5, §8.7, §15 seeds, §11 | 0 |

Exit code 0 means the script ran to completion; per-check FAILs are findings printed in the output, not script errors. Verdicts used: PASS / FAIL / NOT RUN / UNVERIFIED.

## CLAIM and STATUS (top line)

- **Most stated arithmetic in the paper checks out exactly** (D4 combinatorics, anomaly traces, axion-mass table, dipole-ratio table, electroweak identities, §9 Gaussian moments). The paper's internal arithmetic is generally careful.
- **Six FAILs** (see §FAILs): (F1) the Lemma 4.10 source-weight application — wt = 5/4 and anisotropy $-1/24$ are wrong, and odd monomials are dropped; (F2) eq. (5.5) as printed yields $c_{2}^{b}(1) = 1.84\times10^{-5}$, $54\times$ below the stated $c_{2} \approx 1.0\times10^{-3}$, which also breaks the R = 1.05 entropy-ratio derivation; $(F3) \alphas \approx 1/45$ at the cutoff contradicts the paper's own running inputs (1/49.3 1-loop, 1/49.8 2-loop); (F4) the |$\Omegak$| < $3\times10^{-12}$ bound does not follow over the paper's own stated k range; (F5) the §15 "six to seven orders" As excess is 6–10 orders over the full stated ranges; (F6) the affine diagnostic (9.14) cannot produce the stated combined stress $K \simeq 1.23$.
- **The headline mt bounds (172.89 / 174.31 / 173.0–173.9 GeV) are UNVERIFIED from the text as written** — the 3-loop RG + NNLO matching integration and the heavy-threshold prescription are not specified in reproducible detail, and the paper itself labels the load-bearing premises unproved. The "exact gauge-coupling solutions" claim is likewise UNVERIFIED as a reproducible result (see Check 1b).

---

## Check 1 — The mt ≲ 173.0–173.9 GeV bound and the matching equations (§16, §13.7, §9.6)

### 1a. mt bounds: do the stated inputs yield the stated bound?

**Claim as written (§16.5, Table 19; §13.7):** "Top mass mt ≲ 173.0–173.9 GeV — heavy-state threshold at M∗ (plausible, not proved)"; option (a) "mt ≲ 174.31 GeV at $\alphas = 0.1180$" from "$\LambdaI($mt, $\alphas) \geq M$∗ $\geq$ µ$\infty$" with µ$\infty \simeq 5.906\times10^{8}$ GeV; V1 bound "mt $\leq 172.89$ GeV at $\alphas = 0.1180$" (Prop 9.19).

**Script:** `check_matching.py` (exit 0). **Verdict: UNVERIFIED.**

**Reason (precise missing inputs):** reproducing any of these bounds requires (i) the three-loop SM beta functions, four-loop QCD beta function, and NNLO matching formulae of Buttazzo et al. [48], integrated as an interval ODE with bisection in mt; (ii) the instability scale function $\LambdaI($mt, $\alphas) ($quoted only as $\LambdaI \simeq 4.6\times10^{10}$ GeV at mt = 172.57 GeV, $\alphas = 0.1180)$; (iii) for option (b), the heavy-state threshold prescription itself — no equation for how the threshold shifts the bound is given anywhere in the text, and the 173.0–173.9 GeV range width (0.9 GeV) has no stated source. None of (i)–(iii) is stated in the text in reproducible form. The paper itself flags the load-bearing premises: option (a) rests on "an unproved global-infimum premise" ("If every finite-shape solution satisfies M∗ $\geq$ µ$\infty ($numerically supported, not proved)"); option (b)'s threshold is "plausible but not proved". So the answer to "do the stated inputs yield the stated bound?" is: **the text does not contain enough stated input to decide** — the bounds are outputs of an external numerical pipeline, not derivations from inputs printed in the paper. Grade: INCOMPLETE-EVIDENCE (no HLRE grade); the paper's own labelling ("input-dependent outputs, not parameter-free predictions", abstract line 34) is accurate.

**What *could* be checked (and was):**
- Margin arithmetic (§$16.3): (172.89 - 172.57)/0.29 = **1.103** \to$ "margin $1.1\sigma$" — **PASS** (`check_matching.py`, exit 0).
- $\tan \beta$ from $\cos^{2}2\beta = 0.031 ($Prop $9.19): \cos 2\beta = -\sqrt{0.031}$, $\tan \beta = \sqrt{[}(1-$cos$2\beta)/(1$+cos$2\beta)] = **1.1947** \to$ "$\tan \beta \approx 1.19$" — **PASS**.
- D-flat identity (§9.6): with $\lambda_{1} = \lambda_{2} = (g_{2}^{2}$+gY${}^{2})/4$, $\lambda_{3} = (g_{2}^{2}-$gY${}^{2})/4$, $\lambda_{4} = -g_{2}^{2}/2$, $\lambda_{3}+\lambda_{4}+\sqrt{(\lambda_{1}\lambda_{2})} = **0$ exactly** (SymPy) — **PASS**.
- Eq. (13.6) 1-loop cross-check: with the paper's stated inputs $\alpha$em${}^{-1}($MZ) = 127.95, $\sin^{2}\thetaW = 0.23122$, $\alphas($MZ) = 0.1179, solving $\alphaY^{-1}($µ$\infty) = \alpha_{2}^{-1}($µ$\infty) + (5/3)\alpha_{3}^{-1}($µ$\infty)$ under **1-loop** SM running gives µ$\infty = **6.95\times10^{8}$ GeV**, vs the paper's 2-loop **$5.906\times10^{8}$ GeV** (ratio 1.18) — **PASS as an order-of-magnitude consistency check**; the exact 2-loop value is UNVERIFIED (2-loop coefficients not stated in the text). Second tool: the 1-loop solve used scipy `brentq` on closed-form 1-loop formulae, independent of the SymPy algebra checks.
- $\alphas$ sensitivity "$\pm0.32$ GeV per $\pm0.0009$ in $\alphas$", V2 bound 172.41 GeV, "one-loop threshold band $-0.08$ GeV": **UNVERIFIED** (same missing RG pipeline).

### 1b. "Exact gauge-coupling solutions": do the matching equations as written admit the stated solutions?

**Claim as written (§13.7, eqs. 13.4–13.5):** matching requires $\alpha_{3}^{-1}(M$∗) = KV${}_{a}$, $\alpha_{2}^{-1}(M$∗) = KV_b, $\alphaY^{-1}(M$∗) = KV_Y; "Eliminating $K = \alpha_{3}^{-1}/V_{a}$ leaves two residual equations for $(\chi_{1}, \chi_{2}, \chi_{3}, M$∗); at a regular point their solution set has dimension two, so exact matching leaves continuous freedom even after the class is fixed. The numerical solver finds roots in all ten classes. This is an existence calculation at finite precision, not an interval-certified enumeration of every root, and the three couplings are inputs."

**Script:** `check_matching.py` (exit 0). **Verdict: UNVERIFIED (as a reproducible result); the equations as written do NOT determine the tabulated solutions.**

**Reason:** the paper itself states the solution set is 2-dimensional per class, so "the stated solutions" (the per-row M∗, $1/\alpha$∗ of Table 16) are *selections* from a continuum, made by an unnamed numerical solver at finite precision with no solver data, seed, or per-row winding data Vx$(\chi)$ in the text. The tabulated M∗/$\alpha$∗ values therefore cannot be reproduced or checked from the text as written. What was checked:
- Eq. $(13.7) \to (13.8)$ algebra: from MP${}^{2} = \kappag\Lambda^{2}q^{6}\prod\chi_{i}$ with $\Lambda$ = qM∗, MP${}^{2} = \kappa$gM∗${}^{2}q^{8}\prod\chi_{i}$ follows exactly (SymPy) — **PASS**; and M∗_bridge = MP$\cdot(\kappaA/K)^{4/3}/\sqrt{(\kappag\prod\chi_{i})}$ inverts it — **PASS**. But the **printed (13.8) is garbled** in the extraction ("M∗bridge = $p Q A^{4/3}/(\kappag\prod\chi_{i}K^{4/3})$", missing MP and square roots), so the printed formula itself is **UNVERIFIED as printed**.
- The gravity–gauge selection ("agrees with the observed MP for about half of the gauge-matched points of one class"): **UNVERIFIED** — no counts or MP values per point are given in the text.
- The joint fit "impos[ing] the common-radius area relation $\kappa_{2}/\kappa_{3} = \chi_{2}/\chi_{3}$ has not been carried out" (paper's own words) — noted, not a failure.

### 1c. Lepton fit, eq. (13.9) (§13.7)

**Claim as written:** "The fit reproduces the observed charged-lepton ratios with $\kappa_{2} \simeq 0.5724$ and $w \simeq 0.2429$ at the declared separation; uniqueness in the separation y is not established."

**Script:** `check_matching.py` (exit 0). **Verdict: PASS (conditionally) / UNVERIFIED as stated.**

**Numbers:** with the periodised-Gaussian reading $c_{k} = \Sigma_{\ell} \exp(-\pi\kappa_{2}(k/3+y+\ell)^{2} + 2\pii(k/3+y+\ell)w)$ — the square is required, since the text states "The sum converges absolutely", which fails without it — the singular-value ratios at $\kappa_{2} = 0.5724$, w = 0.2429 are $s_{1}/s_{3} = 2.874\times10^{-4} ($observed $m_{e}/m_{\tau} = 2.876\times10^{-4})$ and $s_{2}/s_{3} = 0.059477 ($observed $m_{\mu}/m_{\tau} = 0.059464)$, worst log-error **0.0005** at best y. **The ratios are y-independent to <0.1% over the whole range $y \in [0,1)** ($samples: y = 0.00/0.13/0.37/0.71/0.99 give $s_{1}/s_{3} = 2.8743/2.8732/2.8741/2.8741/2.8743\times10^{-4}, s_{2}/s_{3} = 0.059477$ throughout; 2001-point scan, worst log-error < 0.001 everywhere). So the missing y is immaterial to the ratios, and the fit is real — but it is **2 parameters $(\kappa_{2}, w)$ fitting 2 ratios**: an accommodation (HLRE I0, post-hoc fit, grade D as a prediction), not a test. The separation y is not given numerically anywhere in the text ("at the declared separation"), so the fit **as stated** remains UNVERIFIED as written; the scan only establishes existence/robustness. Second tool: mpmath (30-digit) evaluation, independent of the SymPy algebra elsewhere.

---

## Check 2 — D4 lattice counts (§3–§4, §13.5)

**Script:** `check_d4.py` (exit 0). All **PASS** except the Lemma 4.10 application (F1 below).

- **D4 roots (3.6):** $R = {\pme_{i}\pme_{j}}$ has **24** elements, all of norm${}^{2} 2$ — PASS (direct enumeration).
- **t-layers (Prop 3.6, Fig. 6$):** t = -1/0/+1$ counts **6/12/6** — PASS. **Weights (Def. 3.7, $\beta = 1)$:** w = 2 on the six $-(e_{i}+e_{j})$, 1 on the twelve $\pm(e_{i}-e_{j})$, 1/2 on the six +$(e_{i}+e_{j})$ — PASS (exact fractions).
- **Cuboctahedron (§3.5):** the t = 0 layer has **12** vertices, all in 1^$\perp$ — PASS; it is a **spherical 3-design** (exact rational check of all monomials of degree $\leq 3$ against sphere averages) — PASS; the **24-cell is a spherical 5-design** (all monomials degree $\leq 5)$ — PASS. Second tool: the design checks used exact `Fraction` arithmetic, independent of the float group enumerations.
- **H matrix (3.8):** symmetric, $H^{2} = I ($hence $H^{-1} = H)$, $\det = -1$ — PASS (SymPy exact).
- **Hurwitz integers (§3.2):** norm-2 Hurwitz integers number **24**; units (binary tetrahedral group) number **24** — PASS (exhaustive enumeration over Z and Z+½ coordinates).
- **Weyl groups (Prop 4.9):** |$W(D_{4})$| = **192**, |$W(F_{4})$| = |Aut$(D_{4})$| = **1152** — PASS (explicit matrix-group enumeration, exact Fractions and float cross-check agree). Scalar case: dim of Sym${}^{2}($Vp*) invariants under $W(F_{4}) = **1** ($character average 1.000000000000) — PASS. The full multiplicity claims of Prop 4.9 (Dirac/gauge/graviton, "multiplicity one"; "three" for the graviton under $W(D_{4}))$ are **NOT RUN**: the constrained representation spaces are not specified numerically in the text. (Unconstrained gauge-type invariant dimension under $W(F_{4})$ computes to 2, which is not the paper's constrained claim and is reported only as information.)
- **S4 representation numbers (Thm 6.4, Remark 6.5):** irrep dims 1,1,2,3,3 with 1+1+4+9+9 = 24 — PASS; the central operator P = $(1/6)\SigmaL($ij) has eigenvalues {1, $-1, 0, 1/3, -1/3}$ with multiplicities {1, 1, 4, 9, 9} — PASS (explicit $24\times24$ left-regular matrices, numpy eigvalsh).
- **Prop $13.2:** \sigma_{1}(2) = **3$**; |GL${}_{2}(F_{2})$| = **6**; |SL${}_{2}(F_{3})$| = 24, |PSL${}_{2}(F_{3})$| = **12**; |GL${}_{2}(F_{3})$| = 48, |PGL${}_{2}(F_{3})$| = **24**; lines in $F_{2}^{2} = **3$**, in $F_{3}^{2} = **4$**; cusp permutation module dim 1+3 = 4; $\det 2 \equiv -1 ($mod 3), a nonsquare — all PASS. $V_{4}$ is the **unique** normal subgroup of order 4 in $S_{4}$ — PASS (brute-force over $S_{4})$.
- **Finite model (Def. 3.13, Props. 3.16–3.17, Thm 3.18):** |Trans$(S_{4})$| = 6, |H∗| = 7, µ_H normalisation ½ + $6\times(1/12) = 1$, |E∗| = 7, |D∗| = 49 — all PASS. Prop 3.17 bound: $(\log 5)^{2} + 3/(4\kappat) = 3.221774 < 2(\log 5)^{2} + 3/(2\kappat) = 6.443548 < 6.444$ — PASS (given $\kappat)$. Thm 3.18 variance bound $2/\kappat^{2} = 1.417855 \leq 2$ — PASS. **UNVERIFIED:** the values $\alpha = 0.48047629504141964$ and $\kappat = 1.1876789651362785 ($"maximum-entropy parameters", eq. E.6) have **no defining equation in the text**; $Z_{\alpha} = 1 + 2(2$^$(-\alpha)+3$^$(-\alpha)+5$^$(-\alpha)) = 4.536195\dots$ was computed but cannot be tied to $\kappat$ from the text.
- **Lemma 4.10 itself (uniform weights):** the quartic formula (4.3) matches the symbolic sum over all 24 roots exactly (SymPy), and the isotropic case wt = ws = w gives $-(w/2)(k^{2})^{2}$ — **PASS**.

### FAIL F1 — Lemma 4.10 application to the source weights (§4.4)

**Claim as written:** "With the source weights of Definition 3.7 the time roots come in pairs with weights 2 and 1/2, so the even quartic term sees wt = 5/4 and ws = 1; the weighted crystal therefore keeps the anisotropy coefficient $-1/24$ at quartic order."

**Verdict: FAIL** (`check_d4.py`, exit 0; SymPy exact expansion).

**Numbers:** the true source-weighted quartic, $\Sigma_{r} w(r)(k\cdotr)^{4}$ with w(r) = 2^$(-t(r))$, is

> $-(1/24)[ (27/2)(k^{2})^{2} + 2\Sigma_{i\neqj}k_{i}^{3}k_{j} + 2k_{0}^{3}(k_{1}+k_{2}+k_{3}) + 2k_{0}(k_{1}^{3}+k_{2}^{3}+k_{3}^{3}) ]$.

Consequences, each verified by exact SymPy expansion:
1. The **even part is exactly isotropic**, $-(9/16)(k^{2})^{2}$ — effective weight 9/8 (= the mean source weight over all 24 roots: $(6\cdot2 + 12\cdot1 + 6\cdot$½)/24 = 9/8), reproduced exactly by (4.3) at (wt, ws) = (9/8, 9/8). Its anisotropy (deviation from isotropy) is **0, not $-1/24$**.
2. The paper's (wt, ws) = (5/4, 1) **does not reproduce** the true quartic: the difference contains even terms $(k_{0}^{4}/16, k_{0}^{2}k_{i}^{2}/8, -k_{i}^{4}/48, -k_{i}^{2}k_{j}^{2}/8)$ as well as odd terms. The 5/4 comes from averaging only the six $t = \pm1$ time-root pairs, (2+½)/2, while ignoring the six weight-1 time roots $\pm(e_{0}-e_{i})$ — and the spatial roots are split the same way, which no single (wt, ws) in (4.3) captures.
3. The true quartic contains **twelve odd monomials** $(k_{0}^{3}k_{i}, k_{0}k_{i}^{3}, k_{i}^{3}k_{j}, k_{i}k_{j}^{3})$, all with coefficient **$-1/12$**, which lie outside the form (4.3) entirely. The paper does not mention them.
The lemma itself is correct; its application to the source weights is not. (The downstream remark that the crystal's quartic dispersion "is not a prediction" is unaffected in substance, but the quoted anisotropy value $-1/24$ is wrong.)

---

## Check 3 — Anomaly cancellation (§6)

**Script:** `check_anomaly.py` (exit 0). All **PASS** (exact rational arithmetic, `Fraction`).

- **Charges (Thm 6.13(c)):** with 6Y charges (Q, $u^{c}, d^{c}, L, e^{c}) = (1, -4, 2, -3, 6)$, **tr $Y^{3} = 0$**, **tr Y = 0** (mixed gauge–gravity), **tr $Y\cdotT^{2}$_SU(2) = 0**, **tr $Y\cdotT^{2}$_SU(3) = 0** for one generation, hence for three — PASS. The quoted 6Y tuple equals $6\times$ the standard SM hypercharges (1/6, $-2/3, 1/3, -1/2, 1)$ — PASS.
- **SU(2) global anomaly:** 3 colours of Q + 1 L = **4 doublets per generation (even)** — PASS.
- **Charge quantisation (Thm 6.13(b)):** bifundamental charges $\pm1$ in $Y = Q_{a}/6 - Q_{c}/2 + Q_{d}/2$ give values in $(1/6)\mathbb{Z}$ — PASS; the kernel vector y = (1/6, 0, $-1/2, 1/2)$ of Prop 6.16 **is exactly the coefficient vector of Y** — PASS.
- **Catalogue counts (Prop 6.15, Table 16):** copy numbers sum to **76** (8+4+4+16+4+4+8+4+8+16) — PASS; 52/76 = **68.4%** $\to$ "68%" — PASS. **UNVERIFIED detail:** Table 16 identifies only **44** copies with ranks (2,2,1,1) (V1, V2, V4–V7, V8, V9, V12); the claimed 52 requires exactly 8 of the 16 "mixed" V13–V16 copies to be (2,2,1,1), which the text does not specify.
- **Axion-bearing vacua (Remark $10.3):** 76 - 8 (V10) - 8 (V12) = **60$** — PASS.
- **Strong sector (§$10):** b_{3} = -11 + (2/3)\cdot6 = **-7$** — PASS; $\beta = 6/g^{2} = 270/(4\pi) = **21.4859** \to$ "21.49" **given $\alphas = 1/45$** — PASS (the $\alphas$ value itself fails; see F3).
- **Prop 6.7 wave law:** $\partial\log \omega/\partial\log A = -1/2$, $\partial_{x}\log \omega = r($rx$-s)/D$, $\partial$_{log y}$\log \omega = r^{2}y^{2}/D - 1/2$ — all PASS (SymPy).

---

## Check 4 — Coupling-matching algebra (§13.7, §16)

- **Matching equations (13.5) as written:** see Check 1b — UNVERIFIED as a reproducible result (2-dimensional solution set per class, solver unstated, per-row winding data unstated).
- **Eq. (13.6) 1-loop cross-check:** $6.95\times10^{8}$ GeV vs $5.906\times10^{8}$ GeV — PASS as order-of-magnitude; exact value UNVERIFIED (Check 1a).
- **Eqs. (13.7)/(13.8) algebra:** PASS from (13.7); printed (13.8) garbled — UNVERIFIED as printed (Check 1b).
- **Lepton fit (13.9):** PASS conditionally — see Check 1c.
- **Other §13.7 numbers — UNVERIFIED from the text:** "4236 admissible configurations and 126 intersection patterns" (|n| $\leq 5$ scan; stack/tilt domain not fully specified); $\chi^{2} = 373$ "against a pass threshold fixed in advance" (the threshold value is **not stated**, so pass/fail cannot be checked); $\sin^{2}\thetaW$ percentiles 0.117/0.309/0.488 and "24th percentile" (measure computation not reproducible from the text); $\tan \beta = 1.2$–1.5 for option (b) (no derivation); M∗ $\approx 5.8\times10^{16}$ GeV selected point (depends on the unverifiable matching solve).

---

## Check 5 — Other numerically stated identities (§5, §9, §13, §15, §16, §18)

### §5 gravity — PASS except F2

**Script:** `check_gravity.py` (exit 0).
- **Prop 5.8:** kg = $16\pi\cdot5\cdot1.6475\times10^{-7} = **4.1406\times10^{-5}** \to$ "$4.14\times10^{-5}$" PASS; kA = $4\pi\cdot4\cdot1.5614\times10^{-4} = **7.8485\times10^{-3}** \to$ "$7.85\times10^{-3}$" PASS; $P\chi = 1.25\times3.2\times1 = **4$** PASS; $\varepsilon^{-1}$ = MP/$(\sqrt{(kgP}$kgP$\chi)\cdotL^{3}) = **6.748\times10^{17}$ GeV** given L = 11.2 (paper: $6.77\times10^{17}, 0.3$% — consistent with rounding of L and kg) PASS; MP/$6.77\times10^{17} = **18.0207** \to$ "18.02" PASS; (MP/$\Lambda)^{2} = (1.22\times10^{19}/6.8\times10^{17})^{2} = **321.9** \to$ "$\approx322$" PASS. **UNVERIFIED:** L = 11.2 itself depends on the unstated catalogue value K (implied $K = L^{3}$kA = 11.03); the $\varepsilon^{-1}/M$∗ chain is conditional on K.
- **Prop $5.10:** s_{cell} = \varepsilon^{2}/(4\ell_{P}^{2}) = 18.02^{2}/4 = **81.18** \to$ "81.2 nats" PASS; $L^{6}P\chi = 11.2^{6}\times4 = **7.895\times10^{6}** \to$ "order $10^{6}$–$10^{7}$" PASS.
- **Entropy ratio R (§5.2, §16.2):** R = 1.05 requires $c_{2} = \kappaS/(4\pi\cdot1.05) = **1.043\times10^{-3}** (m^{2} = 0.5, \kappaS = 0.01376)$ and **$0.950\times10^{-3}** (m^{2} = 1, \kappaS = 0.01254)$ — both $\approx 1.0\times10^{-3}$, consistent with Num. result 5.6 — PASS as consistency; the $\kappaS$ ratio 0.01376/0.01254 = 1.097 matches the quoted $\pm0.08$ spread — PASS. The exact R value is **UNVERIFIED** $(c_{2}$ is only ever quoted as $\approx 1.0\times10^{-3})$. The factor 3.1 in $D\alpha ($§16.2 step 6) has no derivation in the text — UNVERIFIED (Table 18's internal consistency with 3.1 was verified; see below).
- **Num. result $13.4:** -1/k = **1.686$, 2.865, 1.041** for $k = -0.593$, $-0.349$, $-0.961 \to$ "1.69, 2.86, 1.04" — PASS (rounding note: $-1/0.349 = 2.865$ rounds to 2.87, so the stated 2.86 implies unrounded $k \approx -0.3494$, consistent with printed $-0.349)$.
- **Table 18 (sky dipoles):** with $D\alpha \approx 3.1\cdotk\cdot\sqrt$|$\Omegak$|, the three rows imply $k \in **[0.242, 0.968]$, [0.255, 0.959], [0.252, 0.968]** — mutually consistent, and matching §14.3's k = 0.25–0.96 — PASS. G-dipole/$D\alpha$ endpoint ratios are 1.36–1.46 and 3.27–3.30, matching the bridge-vacua range 1.4–3.3 — PASS. $A 10^{-5}$ dipole needs |$\Omegak$| $\in [1.13\times10^{-11}, 1.66\times10^{-10}] \to$ "$\approx10^{-11}$–$2\times10^{-10}$" — PASS.

### FAIL F2 — Eq. (5.5) does not yield the stated $c_{2} ($§5.2)

**Claim as written:** eq. (5.5), $c_{2}^{b}($µ${}^{2}) = [1/(24\pi^{2}(2$+µ${}^{2})^{2})]\cdot\Sigma_{\ell\geq1}(2/(2$+µ${}^{2}))^{\ell}\cdot\ell(\ell+1)/(\ell+2)^{4}$, averaged over the internal Brillouin zone; Num. result 5.6: "Two independent evaluations give $c_{2} \approx 1.0\times10^{-3} > 0$ in node units."

**Verdict: FAIL** (`check_gravity.py`, exit 0; float sum cross-checked by mpmath at 30 digits: sum = $0.0393235671843279\dots$, and by an exact $\zeta$-function evaluation at µ${}^{2} = 0)$.

**Numbers:** $c_{2}^{b}($µ${}^{2}=1) = **1.8446\times10^{-5}$** — a factor **54.2** below $1.0\times10^{-3}$. The function decreases in µ${}^{2}$, and even its maximum, $c_{2}^{b}(0) = **2.1468\times10^{-4}** ($exact: sum 0.203410 via $\zeta(2), \zeta(3), \zeta(4))$, is ~$5\times$ below $1.0\times10^{-3}$. A Brillouin-zone **average** cannot exceed that maximum, so no averaging prescription rescues (5.5) as printed. **Downstream consequence:** with $c_{2}^{b}(1) = 1.84\times10^{-5}$, $R = \kappaS/(4\pic_{2}) = 0.01376/(4\pi\cdot1.8446\times10^{-5}) = **59.4$**, not the quoted $R = 1.05 \pm 0.08$. So either (5.5) is misprinted in the paper/extraction $(a (\ell+2)^{2}$ denominator would give the right order — noted as speculation, not a finding), or $c_{2}$ in Num. result 5.6 / R is a differently-normalised quantity from $c_{2}^{b}$ in (5.5), in which case the text does not say so. As written, (5.5) and R = 1.05 are mutually inconsistent by a factor ~54.

### FAIL F3 — $\alphas \approx 1/45$ at the cutoff (§10, Prop 10.2)

**Claim as written:** "At the cutoff $\Lambda \approx 6.8\times10^{17}$ GeV the strong coupling is $\alphas \approx 1/45$, so the lattice theory starts at weak coupling, $\beta = 6/g^{2} \approx 21$."

**Verdict: FAIL** (`check_matching.py`, exit 0; two independent runnings).

**Numbers:** from the paper's own $\alphas($MZ) = 0.1179, standard 1-loop running with nf = 5 below mt and nf = 6 above gives $\alphas(6.8\times10^{17}$ GeV) = 0.020298 = **1/49.27**; 2-loop running (scipy `solve_ivp`, $\beta_{0} = 11-2$nf/3, $\beta_{1} = 102-38$nf/3) gives 0.020084 = **1/49.79**. Both are ~10% away from 1/45. With $\alphas = 1/49.8, \beta = 6/(4\pi\alphas) = **23.77$**, not 21.49. $(\beta = 21.49$ follows exactly from $\alphas = 1/45$ — that conditional algebra PASSES; it is the $\alphas$ value that fails.) §17.5's use of $\beta = 21.49$ inherits this value.

### FAIL F4 — Curvature bound |$\Omegak$| < $3\times10^{-12} ($§14.3, Table 13)

**Claim as written:** "Per Hubble radius, $\Delta\alpha/\alpha \approx k\sqrt$|$\Omegak$|$\dots$ The bound |$\Delta\alpha/\alpha$| < $10^{-6}$ implies |$\Omegak$| < $3\times10^{-12}$", with $k = d \ln \alpha/d \ln \chi = 0.25$–0.96 stated in the same paragraph.

**Verdict: FAIL as stated** (`check_gravity.py`, exit 0).

**Numbers:** |$\Omegak$| < $(10^{-6}/k)^{2}$. At k = 0.593 (V1's middle torus) this is $2.84\times10^{-12} \approx 3\times10^{-12}$ — the quoted bound is reproduced at a representative k. But over the paper's own stated range $k \in [0.25, 0.96]$ the bound is $(1.09\times10^{-12}, 1.60\times10^{-11})$; the weakest-k end, k = 0.25, gives **$1.6\times10^{-11}$**, five times weaker than claimed. The implication as stated ("implies") does not hold for the full stated k range; $3\times10^{-12}$ is a representative-k value $(k \approx 0.58)$, not the range-wide implication. (The atomic-clock ratio in the same paragraph checks out: $10^{-11}/10^{-18} = 10^{7}$, "$10^{6}$–$10^{7}$" — PASS.)

### §9 electroweak numerics — PASS except F6

**Script:** `check_misc.py` (exit 0).
- $\beta = 4/g^{2} = 9.52 \to g^{2} = 0.4202$, $g = 0.6482 \in [0.5, 0.65]$ — PASS. Anharmonicity $\beta\theta_{0}^{4}/24 = 0.0248 \leq 0.5$ at $\theta_{0} = 0.5$ — PASS. hF${}^{2} = 15/32 = **0.46875$** exactly — PASS.
- K-diagnostic products: $e\cdotB\cdot\varepsilon$ with B = sup BL $\leq 8.464$: $e\times8.464\times0.01994986283 = **0.458997215** \to$ "0.458997216 < 3/4" PASS; $e\times8.464\times0.03634456227 = **0.836199** \to$ "> 3/4" PASS. (Note: the paper's notation "$e(8.464)\varepsilon$" is Euler's number times B times $\varepsilon; e^{B\varepsilon}$ would give 1.184, not 0.459.)
- Eq. $(9.11): 1 - \cos z - z^{2}/2 \leq 0 \leq$ cosh $\theta_{0} - 1 - \theta_{0}^{2}/2$ — PASS (standard inequality; the bound is vacuous in the sense that the left side is never positive). The quoted 53-step maximum 0.4698097675 is **UNVERIFIED** (per-step $(\beta, \theta_{0})$ unstated; at $\beta = 9.52, \theta_{0} = 0.5$ the bound is 0.0250).
- Eq. $(9.12): \int$_R^$\infty 2\pi^{2}r^{3}e^{-\lambdar4/4}$dr = $(2\pi^{2}/\lambda)e^{-\lambdaR4/4}$ — PASS (SymPy exact).
- Lemma 9.12: Var$(X^{4}) = (105-9)\sigma^{8} = 96\sigma^{8}$ — PASS. Lemma 9.13: ERg = $(1-a)/g^{2} - s/2$ and the ERg${}^{2}$ formula (9.16) match the Gaussian moment expansion exactly (SymPy, including $E X^{2}\cos($gX$) = (s-g^{2}s^{2})a)$ — PASS.
- Eq. (9.18) radial expectations (mpmath, 30 digits, second tool independent of the SymPy checks): E cos(gR/$2) = (1-u)e^{-u/2}$, $E R^{2}\cos($gR/$2) = s(u^{2}-6u+3)e^{-u/2}$, $E \cos^{2}($gR/2) = $[1+(1-4u)e^{-2u}]/2$, ER${}^{2} = 3s$, ER${}^{4} = 15s^{2}$ — all agree to <$10^{-20}$ — PASS. ‖Wg $-$ EWg‖${}_{2} = **0.025247626672$** at $g^{2} = 0.4194$ vs quoted 0.02524762667 — PASS.
- **UNVERIFIED (values, not reproducible from the text):** the Kotecký–Preiss values 0.863 (c = 10) / 0.214 $(c = 20) (z_{small}, z_{large}$ unstated); margins +$0.092 / \lambda_{eff} = +0.0018$; $\varepsilon_{3}/\varepsilon_{4}/\varepsilon_{H}$ ranges and $K = 0.13\to0.40$; the 0.5897571764 / 0.6025322010 totals; $\sup_{L} B_{L} \leq 8.464$; "block averaging over 24 blocks" (a factor-2 block in 4D contains 16 sites; what the 24 counts is not defined in the text — flagged as unexplained, not graded FAIL).

### FAIL F6 — Affine diagnostic (9.14) / Numerical result 9.10(vi)

**Claim as written:** K(f,q) = 0.19739677 + 0.18525147f + 0.18203288q, "baseline 0.39659930. Each single change passes (fmax = 2.00036, qmax = 2.94414), but the combined stress case gives $K \simeq 1.23$"; earlier: "counting twenty neighbouring polymers separately gives K = 0.69, replacing the measured irrelevant fraction 0.09 by 0.25 gives K = 0.42, while imposing both changes gives K = 1.23."

**Verdict: FAIL** (`check_misc.py`, exit 0).

**Numbers:** the baseline 0.39659930 with $q_{0} = 1$ implies $f_{0} = **0.09268** ($vs the "measured" 0.09); fmax = 2.00036 is reproduced exactly as the K = 0.75 crossing at q = 1; qmax = 2.94414 is reproduced only with $f_{0} = 0.09$ exactly (which would give baseline 0.39610, not 0.39660) — a rounding-level inconsistency of 0.0005 in K, noted but not the main failure. The main failure: the affine model predicts the combined effect of the two stated single changes as K(0.25, $q_{20}) = **0.719** (q_{20} = 2.612$ from K = 0.69 alone), and K(fmax, qmax) = **1.104** — neither is 1.23. Additivity also fails: $0.69 + 0.42 - 0.40 ($baseline$) = 0.71 \neq 1.23$. The value 1.23 would require a large interaction term that the affine form excludes, or unstated (f, q) inputs. As printed, (9.14) and the stated 1.23 are mutually inconsistent.

### FAIL F5 — §15 As excess "six to seven orders"

**Claim as written (§15):** the matter-bounce HB $\sim 7\times10^{16}$–$2\times10^{17}$ GeV "gives As six to seven orders of magnitude too large" (vs the needed HB $\approx 10^{12}$–$5\times10^{13}$ GeV).

**Verdict: FAIL as a range statement** (`check_misc.py`, exit 0).

**Numbers:** As $\propto$ HB${}^{2}$, so the excess factor over the full stated ranges is $(7\times10^{16}/5\times10^{13})^{2} = **1.96\times10^{6}$** at the low end and $(2\times10^{17}/10^{12})^{2} = **4.0\times10^{10}$** at the high end — i.e. **6–10 orders**, not 6–7. "Six to seven" holds only for the upper-to-upper pairing. Related: the needed-HB range itself is **UNVERIFIED** — As $\approx ($HB/MP$)^{2}/(12\pi^{2}$cs$) = 2.1\times10^{-9}$ with cs < $1.5\times10^{-3}$ reproduces HB $\in [10^{12}, 5\times10^{13}]$ only with the **reduced** Planck mass $(2.435\times10^{18}$ GeV: HB = $1.00\times10^{12}$ at cs = $6.8\times10^{-7}, 4.70\times10^{13}$ at cs = $1.5\times10^{-3})$; with the paper's own MP = $1.22\times10^{19}$ GeV (§5.8) the same cs range gives HB $\in [5.0\times10^{12}, 2.36\times10^{14}]$. Neither MP convention nor the cs range is stated in §15.

### §15 / §8 / §11 / §17 — other PASSes

- Matter-bounce tilt: ns = 1 + 12w/(1+3w) = **0.964894** at $w = -0.0029 \to$ "0.9649" PASS. r = 24cs < $0.036 \to$ cs < **0.0015** PASS.
- Node-scale thermal seed: $(\ellP/\varepsilon)^{4} = (1/18.02)^{4} = **9.484\times10^{-6}** \to$ "$9.5\times10^{-6}$" PASS; ratio to As = $2.1\times10^{-9}$ is **$4516** \to$ "at least $5\times10^{3}$ times too large" PASS.
- M∗ = $5.8\times10^{16}$ vs $V^{1/4} = 1.4\times10^{16}$: ratio **$4.14** \to$ "within a factor of about four" PASS.
- Poisson fluctuations on cosmological scales: 4-volume count gives $N^{-1/2} = **4.86\times10^{-120}** \to$ "$\sim10^{-120}$" PASS (using $H_{0} = 70$ km/s/Mpc, $\ellP = 1.616\times10^{-35} m, \varepsilon = 18.02\ellP$ — external standard inputs, noted; a 3-volume count would give $10^{-90})$.
- $m^{2}/\Lambda^{2} \sim 10^{-36}$ for m = 1 GeV, $\Lambda = 6.8\times10^{17}$ GeV: $(1/6.8\times10^{17})^{2} = 2.16\times10^{-36}$ PASS (which mass m is, is unstated).
- $t_{Page} = (1-2^{-3/2})t_{ev} = **0.64645** \to$ "$\approx0.646$" PASS. Cutoff scale $p \approx 2\pi$/rc = **4.189** (rc = 1.5), above the tested p ≲ 3.5 — PASS.
- §8.7: 3.038/1.614 = **$1.8823** \to$ "ratio about 1.88" PASS; 0.074/0.03 = 2.47, $0.107/0.03 = 3.57 \to$ "2.5–3.6 times" PASS.
- §17.5: box link count |$\Lambda$| = $4\cdot16^{p}\cdotl$µ$\cdotl\nu$ and Lµ$L\nu = 4^{p}\cdotA_{C}$ verified; the last factor (c|$\Lambda$|)^${4^{-p}} \to 1$ as $p \to \infty ($values 2.83, 1.54, 1.16, 1.05, 1.015, 1.004 at $p = 1\dots6)$ — PASS. The intermediate bound as extracted, "$(64p c A_{C})$^${4^{-p}}$", is **UNVERIFIED (extraction ambiguity)**: the $64^{p}$ reading makes it valid $(4\cdot16^{p} \leq 64^{p}$ for $p \geq 1)$; the 64p reading fails for $p \geq 2$. The limit conclusion holds either way.

### §16 axion masses — PASS (all rows)

**Script:** `check_matching.py` (exit 0). ma = 5.70 µeV $\times 10^{12}/M$∗: V$1 **358.5** \to 358$; V$2 **70.11** \to 70.1$; V$3 **10.46** \to 10.5$; V4–V$7 **5.816** \to 5.82$; V$8 **4.161** \to 4.16$; V$9 **0.5327** \to 0.53$; V$11 **0.01662** \to 0.017$; V13–V16 range **[0.000613, 0.003563]** $\to 0.0006$–0.0036; selected class **0.0983 neV** $\to$ "$\approx0.1$ neV"; eq. (16.5) interval **[123.9, 9651]** µeV $\to$ "124–9651 µeV" — all PASS. Table 16 copy sum 76 — PASS (Check 3).

### §18 collected Lagrangian

Eq. (18.1)/(18.2) is a summary of terms whose coefficients the paper itself states are "not fixed" $(G_{eff}, \Lambda)$, "require matching/vacuum input" $(g_{s}, g_{2}, g_{Y})$, or "declared identifications" $(f_{a} = M$∗). No independently checkable number is asserted there beyond the E/N values already checked (2/3 V1, 4/3 V11 — from the catalogue, UNVERIFIED from the text as written since the winding data are not given). Nothing further to check.

---

## UNVERIFIED / NOT RUN register (summary)

| # | Item | Precise reason |
|---|---|---|
| U1 | mt bounds 172.89 / 172.41 / 174.31 / 173.0–173.9 GeV; $\LambdaI \simeq 4.6\times10^{10}$ GeV; µ$\infty \simeq 5.906\times10^{8}$ GeV (exact) | 3-loop RG + NNLO matching pipeline and threshold prescription not stated in reproducible form; premises labelled unproved by the paper itself |
| U2 | "Exact" gauge-coupling solutions; Table 16 M∗/1/$\alpha$∗ per row; L = 11.2 | 2-dim solution set per class; solver, seeds, per-row winding data Vx$(\chi)$ and K unstated |
| U3 | Lepton fit as stated $(\kappa_{2}, w)$ | separation y unstated (immaterial to ratios — see 1c — but the fit as stated cannot be reproduced verbatim); 2 params fit 2 ratios |
| U4 | $\alpha = 0.48047629504141964$, $\kappat = 1.1876789651362785$ | no defining equation in the text |
| U5 | $R = 1.05 \pm 0.08 ($exact); $\kappaS$, Ig, IA values; $\Pi$TT$(0) \approx 0.135$; $5\times10^{-15}$ agreement | regulator/computation outputs; inputs/code not in the text |
| U6 | KP sums 0.863/0.214; $c' \leq 0.3147$; HW P = 0.046/0.0112; Landau ratio 0.999–0.995; $\chi^{2}$ values (§11); $\varepsilon/K/\lambda_{eff}$/margins (§9.4–9.5); 0.5897/0.6025 totals; 4236/126 scan; percentiles; $\chi^{2} = 373$ threshold; wall-bias factor ~1.2; $\thetai \approx 1.6\times10^{-3} / \pi-\thetai \approx 1.4\times10^{-3}$; $\delta\theta \approx 10^{-12}$; $D\alpha$ factor 3.1; "MP for half the points" | inputs, thresholds, or derivations not stated in the text |
| U7 | Prop 4.9 multiplicities (Dirac/gauge/graviton constrained) | constrained representation spaces not specified numerically in the text |
| U8 | §17.5 intermediate bound (64p vs $64^{p})$ | extraction ambiguity; both readings analysed |
| U9 | §$8.3 b_{1} = 4 ($odd L) / 8 (even L) | the D4 root-link complex is not specified in the text in checkable detail |
| U10 | 52-copy rank count detail | needs 8 of 16 "mixed" V13–V16 copies to be (2,2,1,1); not specified |

---

## Verdict tally (per-check)

- **PASS:** 123 sub-check lines across the five scripts (each script prints one line per sub-check).
- **FAIL:** F1 (§4.4 source-weight quartic), F2 (eq. 5.5 vs $c_{2} \approx 10^{-3} / R = 1.05)$, $F3 (\alphas \approx 1/45$ at the cutoff), F4 (|$\Omegak$| < $3\times10^{-12}$ implication), F5 (§15 "six to seven orders"), F6 (eq. 9.14 combined stress 1.23).
- **UNVERIFIED:** U1–U10 above (missing inputs, not contradictions — except where noted, these are gaps, not errors).
- **NOT RUN:** Prop 4.9 constrained multiplicities (U7), §8.3 Betti numbers (U9), Hartman–Watson tail probabilities (U6 — no closed form or density in the text; would need the HW law evaluated independently).

## Notes for the coordinator

1. The two most consequential FAILs are F2 and F3: F2 breaks the internal link between the paper's own induced-gravity formula (5.5) and its entropy-ratio headline (R = 1.05); F3 shifts the Wilson $\beta$ used in §10/§17 from 21.49 to ~23.8 (the "weak-coupling side" conclusion is unaffected in substance, but the number is wrong).
2. F1 is a genuine algebraic error in §4.4 with a clean correction (even part isotropic at weight 9/8; odd monomials at $-1/12)$.
3. The mt bound — the task's headline item — cannot be adjudicated from the text: the paper's own framing ("plausible but not proved", "unproved global-infimum premise", "input-dependent outputs") is the operative fact, and no input in the text reproduces 173.0–173.9 GeV.
4. No claim in this report goes beyond its grade: arithmetic identities that passed are Track F (F2 where a second independent tool confirmed them — the (5.5) sum, the radial expectations, the 1-loop µ$\infty$ solve, the spherical designs; F3 otherwise). Nothing here upgrades any physics claim of the paper.

*— Checker, 2026-11-11. Scripts: `~/workspace/research/irh/torus-node-comparison/checks/check_d4.py`, `check_anomaly.py`, `check_gravity.py`, `check_matching.py`, `check_misc.py` (all exit 0). Tool: conda env Python 3.11.16, SymPy 1.14.0, numpy 2.4.6, scipy 1.17.1, mpmath 1.4.1.*
