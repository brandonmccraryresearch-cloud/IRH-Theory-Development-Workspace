# Task 10 — Check your derivations (IRH v93.1 spacetime & dimensionless constants)

**Workstream D, task 10 — Co-scientist task programme, 2026-11-10.**
**Mode: deepest-research FULL mode for the literature leg (CODATA primary
source); systematic-review mode NOT chosen and NOT used.**
**Tools: SymPy 1.14.0 + python-flint 0.8.0 + numpy 2.4.6, conda env
`jacobian-conjecture-2d`, Python 3.11.16 (local control plane; no GCP
spend, no VM touched, no repo commits, no manuscript edits).**

---

## CLAIM and STATUS (together, at the top)

**CLAIM.** The spacetime/constants derivations of IRH v93.1 were
transcribed into symbolic computation (SymPy) and checked a second time
with an independent tool (python-flint exact rationals + arb, numpy).
**78 checks pass (45 SymPy + 33 flint/numpy), 0 fail on re-run.** The
manuscript's arithmetic is, with two exceptions, exactly as stated:
the selection rationals $(D_{4} S = 64/141, A_{4}$\* 12/31, BCC 16/45, margin
73/423, $\tau$ ratio $\sqrt{2})$, the ordered-branch values (A\* = 0.0775753,
$F = -0.0076323$, uniform baseline $-0.0034636$, detuned no-branch
discriminant < 0), the resonance maximum (24, unique in the scanned
domain), the 24-cell/2T/McKay arithmetic (576 products, $Q_{8}$ normal,
3 cosets; $E_{6}$ Cartan det 3, Smith diag(1,1,1,1,1,3)), the Weyl orders
(192/1920), the Derrick scaling and d = 4 marginality, the isotropy
moments, and the CFL bound $(\Deltat \leq (\sqrt{3}/2)a_{0}/c$, worst-case sum exactly 32)
all reproduce.

**The two exceptions:**

1. **Printed dispersion relation (7) in §III.1 is WRONG — FAILED.**
   The printed formula has a factor of 2 too many in the $\Sigma$ term and
   misplaces $\mu^{2}$. The formula derived from the manuscript's own equation
   of motion is
   $\sin^{2}(\omega\Deltat/2) = (\Deltat^{2}\cdot2J/(4M$\*$a_{0}^{2}))\cdot\Sigma_{\alpha}(1-\cos(a_{0}k\cdot\alpha)) + (\Deltat^{2}\mu^{2})/(4M$\*),
   while the printed (7) is
   $\sin^{2}(\omega\Deltat/2) = (\Deltat^{2}\cdot2J/(4M$\*$a_{0}^{2}))\cdot[2\Sigma_{\alpha}(1-\cos(a_{0}k\cdot\alpha)) + \mu^{2}]$.
   Three independent internal-consistency checks all favour the
   EOM-derived formula, and the manuscript's own §III.2 expansion
   ("at the worst case the bracket equals 32") uses the EOM-derived
   formula, contradicting the printed (7). **The CFL bound itself is
   CORRECT** — it was computed with the right effective formula. This
   is a manuscript erratum (one printed equation), not a refutation of
   the bound.
2. **The §III.3 envelope validity table $(4\times10^{-5}, 0.1$%, 1.0%, 11%, 133%)
   is NOT REPRODUCIBLE from the text as written — UNVERIFIED.** The
   table'$s \Deltat$, carrier $\theta ($or $\mu)$, direction, and error definition are
   unstated. Under the natural reading (exact lattice dispersion vs
   $\omega = c$|k|) the computed errors are $1.67\times10^{-5}, 4.17\times10^{-4}, 3.75\times10^{-3}$,
   4.11%, 36.3% $(\Deltat\to0)$ — smaller than the table by factors 2.4–3.7.
   The zone-edge 133% is unreachable under that reading (it would
   require $\sin^{2} > 1$ or $\omega_{exact} \approx 2.33\cdotc$|k|, which the manuscript's
   dispersion formula cannot produce at any stable $\Deltat). A$ second
   reading (error in $\omega^{2}$, or envelope-vs-quadratic) also fails to
   reproduce the table. The numbers may be correct under the author's
   unstated conditions; they cannot be checked from the manuscript.

**STATUS.** Transcription + two-tool verification COMPLETE. 78/78 checks
PASS on the final runs. One printed equation FAILED (erratum). One
table UNVERIFIED (underdetermined from source). One claim ABSTAIN
(R = 2589 — no derivation inputs in the source; the manuscript itself
already downgrades it). The $\alpha^{-1}$ ansatz arithmetic is exact and is
$174\sigma$ from the CODATA 2022 value (the manuscript itself already
downgrades it to a numerical ansatz; this check confirms the
downgrade). The $\xi_{2} = -1/384$ retraction is arithmetically confirmed
(the stated substitution yields $-1/768, a$ factor of 2).

---

## 1. Claim register (S1 — registered before the checks were run)

The transcription was written from the manuscript before any check was
executed; the headline finding (printed (7) wrong) emerged from the
checks, not from a post-hoc register change. Check groups:

| ID | Narrow claim (manuscript location) | What counts as evidence |
|----|-----------------------------------|------------------------|
| D1 | Planck triad closes iff $L_{P}^{2} = \hbarG/c^{3}$; the triad is a definitional circle (§I.1) | SymPy simplification of the two M\* routes |
| D2 | $\alpha^{-1}$ ansatz = $137 + 1/(28-\pi/14) = 137.0360028219\dots$; differs from CODATA 2022 by $3.645\times10^{-6} (~174\sigma) ($Part VII) | 50-digit SymPy + flint.arb; CODATA 2022 primary source (NIST SP 959) |
| D3 | Derrick scaling dE/$d\lambda$|${}_{1} = (2-d)I_{grad} -$ dI_pot + $(4-d)I_{curv}$; curvature marginal iff d = 4 (§III.4) | SymPy differentiation of the scaling law |
| D4 | Dispersion identity $\Sigma[\cos(a_{0}k\cdot\alpha)-1] = 4\Sigma\cos \cos - 24$, pair by pair (§III.1) | SymPy trigsimp (pair + full) |
| D5 | Printed (7) vs EOM-derived dispersion: printed has $2\Sigma$ and $\mu^{2}$ misplaced (§III.1) | SymPy EOM derivation + three internal-consistency checks (small-k J; k = 0 vs §III.3; CFL table) |
| D6 | CFL bound $\Deltat \leq (\sqrt{3}/2)a_{0}/c$; worst-case $\Sigma(1-\cos) = 32$ at (0,0,$\pi,\pi)$-type points; candidate values 4/3, $16\pi^{2}/3$, 1 (§III.2) | SymPy + numpy $48^{4}$ Brillouin-zone scan + flint.arb candidates |
| D7 | Isotropy moments $\Sigma(k\cdot\alpha)^{2} = 12$\|k\|${}^{2}$, $\Sigma(k\cdot\alpha)^{4} = 12$\|k\|${}^{4} ($§II.1) | SymPy |
| D8 | Selection rationals: $D_{4} \tau^{2} = 8/3$, $q_{4} = 47/8$, S = 64/141; $A_{4}$\* 9/5, 12/31; ratio 496/423, margin 73/423; BCC 4/3, 15/4, 16/45; $\tau$ ratio $\sqrt{2}$; FCC $q_{4} = 27/8$, SC 5/2 (§II.3, §II.6) | SymPy + flint.fmpq exact |
| D9 | $r_{eff}$ and $u_{eff}$ values; ordered branch A\* = 0.0775753, $F = -0.0076323$, uniform baseline $-0.0034636$; detuned $(r_{shell} = -0.10)$ no branch (§§II.7–9) | SymPy + flint.fmpq exact + float solve |
| D10 | $\xi_{2}$ retraction: stated substitution yields $-1/768$, not $-1/384 ($Part VII) | SymPy ratio = 2 |
| D11 | $E_{6}$ Cartan det 3, Smith form diag(1,1,1,1,1,3) (§IV.3) | SymPy |
| D12 | 24-cell = 2T: 24 vertices, all 576 products in the set, $Q_{8}$ has 8 elements and is normal, $2T/Q_{8}$ has 3 cosets of 8 (§IV.2–3) | SymPy exact integer arithmetic (half-unit tuples) |
| D13 | \|$W(D_{4})$\| = 192, \|$W(D_{5})$\| = 1920 (§IV.1) | SymPy |
| D14 | Resonance table $\Psi = 24.0 / -8.0 / -8.0$; maximum 24 unique; second-highest >0.1% below; $16^{4}$ grid maxima = 32 (§II.2, §II.6) | numpy $25^{4}$ scan + $16^{4}$ grid (hand-derived dual shell, verified by the scan) |
| D15 | Every root has exactly 8 partners at $120^\circ ($dot $-1)$; $24\times8 = 192$ ordered triads (§II.5) | numpy enumeration |
| D16 | Shell counts $24 (D_{4}$ scaled) / 64 (competitor \|k\|${}^{2} = 7)$; penalties 0.25/0.25; ratio 64/24 (§II.6) | numpy enumeration |
| D17 | Envelope validity table $(4\times10^{-5}, 0.1$%, 1.0%, 11%, 133%) (§III.3) | numpy reproduction attempt under stated assumption sets |
| D18 | R = 2589 normalization (Part VII) | Source inspection: derivation inputs present or absent |
| D19 | Side finding: at $\Deltat = a_{0}/c$ the discrete dispersion is exactly linear $(\omega = c$\|k\|) along axis and body-diagonal directions | Hand identity $S = 24\sin^{2}(x/2)$ + numpy (errors ~$10^{-13})$ |

**BPMF facets (S1).** Background: IRH v93.1 manuscript §§I–V, VII, IX
+ repo CORE.md / EXCLUDED.md / INPUTS.md / VI-predictions.md.
Purpose: check each derivation step of the spacetime/constants account
symbolically and numerically, including limiting cases. Mechanism:
transcription into SymPy (tool 1) and independent re-check in
python-flint + numpy (tool 2). Findings: §4–§5 below.

**Scope boundary.** Only the derivations in the manuscript's
spacetime/constants account (§§I.1–I.3, II.1–II.9, III.1–III.4, IV.1–
IV.3, Part VII) were transcribed. The $\alpha^{-1}$ and R = 2589 items are
checked as arithmetic, not as physics (the manuscript itself
downgrades both). No rival framework is formalized here (that is
task 12). No Lean formalization was attempted in this task (S7:
the DVP notational-collapse guard has nothing to check — no
formalization was produced).

---

## 2. Method

1. **Transcription.** Each manuscript equation was transcribed into
   `task10_sympy_checks.py` (SymPy 1.14.0) and, independently, the
   numeric/arithmetic subset into `task10_numeric_checks.py`
   (python-flint 0.8.0 fmpq/arb + numpy 2.4.6). The two scripts share
   no code; the numeric script re-derives its quantities from the
   manuscript's definitions (e.g. the ordered-branch quadratic is
   re-solved from $F_{mod}$'s coefficients, the resonance scan re-derives
   the dual shell by hand and confirms it by the scan).
2. **Computation gate (truth-seeking-frontier v5).** Every load-bearing
   number is quoted with its tool, version, and exit code. Above
   CLAIMED, a second independent tool is required — supplied here by
   the flint/numpy script. First run: 3 FAILs, of which 2 were script
   bugs (see §3) and 1 was the F1 check restated as the exact
   difference; all fixed, both scripts re-run to ALL PASS.
3. **Environment (verified).** `~/miniconda3/envs/jacobian-conjecture-2d/bin/python`:
   Python 3.11.16, SymPy 1.14.0, python-flint **0.8.0** (the programme
   brief says 0.9.0 — the local env actually has 0.8.0; recorded here
   as the actual version), numpy 2.4.6.
4. **Primary source for the external constant.** CODATA 2022
   $\alpha^{-1} = 137.035999177(21)$, $\alpha = 7.2973525643(11)\times10^{-3}$, NIST SP 959
   (May 2024), physics.nist.gov; Mohr et al., Rev. Mod. Phys. 97,
   025002 (2025). Verified by web search 2026-11-10.
5. **HLRE v5.1 grading.** Per narrow claim, worst-of computation
   shown (§8). All new claims in this report are I1 (artificial
   verification sharing this pipeline) and cap at **C** (Track E) /
   F3 (Track F); the human source/balance gates were not run.
   Manuscript-carried grades (geometric core A) are cited, not
   re-earned.

---

## 3. Run record (honest history)

| Run | Tool | Result |
|-----|------|--------|
| SymPy, first run | SymPy 1.14.0 | All PASS except 3 FAILs: E2, F1, O2/O4 |
| SymPy, re-run after fixes | SymPy 1.14.0 | **ALL PASS (45 checks), exit 0** |
| Numeric (flint + numpy), first run | flint 0.8.0, numpy 2.4.6 | 2 script bugs (arb precision API; fmpq float conversion) fixed before any check ran |
| Numeric, re-run after fixes | flint 0.8.0, numpy 2.4.6 | **ALL PASS (33 checks), exit 0** (after the assembly fix below) |

**What the first-run FAILs were (and why they were script bugs, not
manuscript errors):**

- **E2:** the script mis-stated the identity it was testing — it
  compared $\Sigma\cos$ against $4\Sigma\cos \cos - 24$ instead of $4\Sigma\cos \cos$. The
  manuscript's identity is $\Sigma[\cos-1] = 4\Sigma\cos \cos - 24$, i.e.
  $\Sigma\cos = 4\Sigma\cos \cos$. Fixed the script; the manuscript's identity
  passes (trigsimp residual 0).
- **O2/O4 (quaternion products):** the script's `qmul` returned the
  formal integer product instead of dividing by 2. The tuples are in
  half-units; every product's components are even, so //2 is exact.
  Fixed; all 576 products close, $Q_{8}$ normal.
- **F1:** restated as the exact difference
  printed $-$ derived = pref$\cdotS + \mu^{2}\cdot($pref $-$ dt${}^{2}/(4M$\*)) (plus F1b for
  the $\mu^{2}$ terms). The difference is the finding itself (§4.1).
- **G3-f (found in assembly, after the first re-run):** the check call
  was indented *outside* its `for` loop, so only the third dt value
  $((\sqrt{3}/2)a_{0}/c \to 1)$ was actually checked; the first two values
  $(a_{0}/c \to 4/3, 2\pia_{0}/c \to 16\pi^{2}/3)$ were printed but never checked.
  Fixed (check moved inside the loop) and re-run: all three cases
  now PASS, and the numeric count is 33 checks, not 32. The earlier
  report text stating "46 SymPy + 32 numeric" was corrected to
  "45 SymPy + 33 numeric" (the SymPy count was also off by one: the
  `def check` line had been counted as a check).

**Logs (verbatim tool output):**
`task10_scripts/task10_sympy_run_2026-11-10.log` (45 PASS, 0 FAIL),
`task10_scripts/task10_numeric_run_2026-11-10.log` (33 PASS, 0 FAIL).

---

## 4. Derivation — the headline finding in full

### 4.1 Printed dispersion relation (7) is wrong by a factor of 2 — FAILED

**The manuscript's own equation of motion (§III.1).** From the site-field
action, by symbolic variation:

M\*$[\phi(n,s+1) - 2\phi(n,s) + \phi(n,s-1)] = (2J\Deltat^{2}/a_{0}^{2})\cdot\Sigma_{\alpha}[\phi(n+\alpha,s) - \phi(n,s)]$
$$- \Deltat^{2}\mu^{2}\phi(n,s)$$

**Plane-wave substitution** $\phi \propto \exp(i(k\cdotn - \omegas\Deltat))$ gives, exactly:

$-4M$\*$\cdot\sin^{2}(\omega\Deltat/2) = -(2J\Deltat^{2}/a_{0}^{2})\cdot\Sigma_{\alpha}(1 - \cos(a_{0}k\cdot\alpha)) - \Deltat^{2}\mu^{2}$

i.e. the **EOM-derived formula**

$\sin^{2}(\omega\Deltat/2) = (\Deltat^{2}\cdot2J/(4M$\*$a_{0}^{2}))\cdot\Sigma_{\alpha}(1 - \cos(a_{0}k\cdot\alpha)) + (\Deltat^{2}\mu^{2})/(4M$\*).

**The printed formula (7)** in the same section is

$\sin^{2}(\omega\Deltat/2) = (\Deltat^{2}\cdot2J/(4M$\*$a_{0}^{2}))\cdot[2\Sigma_{\alpha}(1 - \cos(a_{0}k\cdot\alpha)) + \mu^{2}]$.

**The exact difference** (SymPy F1, PASS):

printed $-$ derived = pref$\cdot\Sigma(1-\cos) + \mu^{2}\cdot($pref $- \Deltat^{2}/(4M$\*)),
where pref = $\Deltat^{2}\cdot2J/(4M$\*$a_{0}^{2})$.

Two separate errors in one printed equation: (i) the $\Sigma$ term is
doubled; (ii$) \mu^{2}$ is placed inside the bracket, so it is multiplied
by pref instead of by $\Deltat^{2}/(4M$\*) (F1b: the $\mu^{2}$ terms differ too,
unless $2J = a_{0}^{2}$, which is nowhere stated).

**Three independent internal-consistency checks all favour the
EOM-derived formula:**

1. **Small-k limit (F2/F3).** Matching the small-k limit to a continuum
   wave speed c fixes J. From the derived formula: J = M\*$c^{2}/12$ —
   the manuscript's own value (§III.2). From the printed formula:
   J = M\*$c^{2}/24$. The manuscript's J is the derived formula's J.
2. **k = 0 (F4).** At k = 0 the derived formula gives
   $\sin^{2}(\theta/2) = \Deltat^{2}\mu^{2}/(4M$\*) — exactly as §III.3 states for the
   rest-mass absorption. The printed formula does not (unless
   $2J = a_{0}^{2}$, unstated).
3. **The CFL table (F5/G-checks).** The manuscript's §III.2 table
   $(\Deltat = a_{0}/c \to 4/3; 2\pia_{0}/c \to 16\pi^{2}/3; (\sqrt{3}/2)a_{0}/c \to 1)$ matches the
   derived formula with worst-case bracket $\Sigma(1-\cos) = 32$. The printed
   formula would give bracket 64 and $\sin^{2} = 8/3$ at $\Deltat = a_{0}/c$, and
   $\Deltat_{max} = \sqrt{(3/8)}a_{0}/c \approx 0.612a_{0}/c$ — contradicting the stated
   $(\sqrt{3}/2)a_{0}/c \approx 0.866a_{0}/c$.

**The manuscript contradicts itself on this point.** The §III.2
"Expansion (source rebuild)" states: "With J = M\*$c^{2}/12$ and $\mu = 0$,
the prefactor in (7) is $\Deltat^{2}\cdot2J/(4M$\*$a_{0}^{2}) = \Deltat^{2}c^{2}/(24a_{0}^{2})$; at the
worst case the bracket equals 32, so $\sin^{2} = (4/3)(\Delta$tc/$a_{0})^{2}$." But
under the printed (7) the bracket at the worst case is
$2\cdot32 + 0 = 64$, not 32 — the expansion treats the bracket as
$\Sigma(1-\cos)$ itself, i.e. it uses the EOM-derived formula while citing
(7). The CFL table and the expansion are correct; the printed (7)
is not.

**Consequence.** One printed equation needs an erratum: replace
$[2\Sigma(1-\cos) + \mu^{2}]$ by $[\Sigma(1-\cos)]$ with the $\mu^{2}$ term outside the bracket
at coefficient $\Deltat^{2}/(4M$\*). **Nothing else changes:** the CFL bound,
the J value, the §III.3 rest-mass absorption, and the §III.1 claim
that "Taylor-expanding reproduces the isotropic result of §II.1
term for term" all follow from the EOM-derived formula — and indeed
the printed formula does NOT reproduce the §II.1 isotropy result
(it gives J = M\*$c^{2}/24)$, so the manuscript's own cross-check
statement is evidence for the derived formula and against the
printed one. The bound is VERIFIED; the printed equation is FAILED.

### 4.2 The CFL bound is correct — VERIFIED (both tools)

- Worst-case $\Sigma_{\alpha}(1-\cos(a_{0}k\cdot\alpha)) = 32$ exactly, at (0,0,$\pi,\pi)$-type
  points (G1-f: exact evaluation; G2-f: numpy $48^{4}$ Brillouin-zone
  scan, grid max 32.000000 at $a_{0}k = (0, \pi, \pi, 0)$; the manuscript's
  "maximum exactly 32" is confirmed independently, not merely quoted).
- Candidate values (flint.arb, $G3-f): \Deltat = a_{0}/c \to \sin^{2} = 4/3$;
  $\Deltat = 2\pia_{0}/c \to 16\pi^{2}/3 = 52.637890$; $\Deltat = (\sqrt{3}/2)a_{0}/c \to 1$ exactly.
- $\Deltat_{max} = (\sqrt{3}/2)a_{0}/c \approx 0.866a_{0}/c$; the $a_{0}/c$ candidate exceeds it by
  $2/\sqrt{3} = 1.1547 ($roughly 15%), as the manuscript states.
- The printed formula would give 8/3 at $\Deltat = a_{0}/c (G4-f)$ —
  contradicting the table; recorded as part of the (7) failure.

### 4.3 The envelope validity table is not reproducible from the text — UNVERIFIED

The §III.3 table states "Comparing the exact transcendental dispersion
against the quadratic approximation mode by mode":

| $a_{0}$\|k\| | table | computed, $\Deltat\to0 (\omega$ vs c\|k\|) | computed, $\Deltat$ = CFL max | computed, error in $\omega^{2} (\Deltat\to0)$ | computed, envelope-vs-quadratic |
|--------|-------|------------------------------|------------------------|-------------------------------|----------------------------------|
| 0.02 | $4\times10^{-5}$ | $1.67\times10^{-5}$ | $4.17\times10^{-6}$ | $3.33\times10^{-5}$ | $6.67\times10^{-5}$ |
| 0.10 | 0.1% | $4.17\times10^{-4}$ | $1.04\times10^{-4}$ | $8.33\times10^{-4}$ | $1.67\times10^{-3}$ |
| 0.30 | 1.0% | $3.75\times10^{-3}$ | $9.44\times10^{-4}$ | $7.50\times10^{-3}$ | $1.50\times10^{-2}$ |
| 1.00 | 11% | 4.11% | 1.12% | 8.22% | 8.1% |
| 3.14 | 133% | 36.3% | 23.0% | 59.5% | 59.5% |

(All computed columns from the numeric script, section Q, using the
correct dispersion and the identity $S(k) = 24 - 4\Sigma_{i<j}\cos(a_{0}k_{i})$
$\cos(a_{0}k_{j})$; directions (1,0,0,0) and (1,1,1,1)/2 give identical
values in every column.)

No $(\Deltat$, direction, error-definition) in these natural readings
reproduces the table. The table's values exceed the $\omega$-reading by
factors $2.4 (\Deltat\to0)$ to ~10 (CFL $\Deltat)$ at every entry, consistently.
The zone-edge 133% is unreachable under the $\omega$-reading: it would
require $\omega_{exact} \approx 2.33\cdotc$|k| at $a_{0}$|k| = $\pi$, i.e. $\sin^{2}(\omega\Deltat/2) \approx 1.33\cdot$
$(\Delta$tc/$a_{0})^{2}\cdot(S/24)$ with $S \leq 32$ — but $\sin^{2} \leq (4/3)(\Delta$tc/$a_{0})^{2}$ while
the required value exceeds that bound at every stable $\Deltat ($the
small-$\Deltat$ expansion gives $\sin^{2} \approx 13.4\cdot(\Delta$tc/$a_{0})^{2}\cdot(S/32)$ vs the
required $\leq 1.33\cdot(\Delta$tc/$a_{0})^{2}\cdot(S/32)$ — a factor-10 gap in the wrong
direction). Under the $\omega^{2}$-reading the zone edge gives 59.5%, still
$2.2\times$ below 133%.

The table'$s \Deltat$, carrier $\theta ($or $\mu)$, direction, and error definition
are unstated in the text, and the Figure 6 caption ("Exact dispersion
against the envelope approximation") suggests the comparison may be
against the envelope (Schrödinger) dispersion, whose $\theta$ is also
unstated. **Verdict: UNVERIFIED, not FAILED** — the numbers may be
correct under the author's unstated conditions, but they cannot be
reproduced from the manuscript as written, and the zone-edge entry
cannot be produced by the manuscript's own dispersion formula under
the natural reading. What would settle it: the author stating $\Deltat$, $\theta$
(or $\mu)$, the direction, and the error definition used for the table.

### 4.4 Side finding: exact linearity at $\Deltat = a_{0}/c$ — VERIFIED

Along the axis direction (1,0,0,0) and the body diagonal
(1,1,1,1)/2, the lattice sum satisfies S$(k) = 24\sin^{2}(a_{0}$|k|/2)
exactly (hand identity; both directions). Hence at $\Deltat = a_{0}/c$ the
discrete dispersion gives $\sin^{2}(\omega\Deltat/2) = \sin^{2}(a_{0}$|k|/2), i.e.
$\omega = c$|k| **exactly** — the discrete dispersion is exactly linear
along those directions. The numeric script confirms: at
$\Deltat\cdotc/a_{0} = 1.0$ the relative errors are ~$10^{-13} ($machine precision)
at all five table points, in both directions. This is a property of
the manuscript's own equations, not a manuscript claim (the
manuscript does not state it). It does not rescue the §III.3 table
(the table's values are non-zero at every entry, so the table was
not computed at $\Deltat = a_{0}/c$ under this reading either).

---

## 5. Checks run (PASS / FAIL / NOT RUN)

### 5.1 SymPy checks — 45 PASS, 0 FAIL (exit 0)

| # | Check | Verdict |
|---|-------|---------|
| A1 | $c = a_{0}\Omega_{P}$ | PASS |
| A2 | triad closes iff $L_{P}^{2} = \hbarG/c^{3} ($ratio = $\hbarG/(c^{3}L_{P}^{2}))$ | PASS |
| A3 | with $L_{P}^{2} = \hbarG/c^{3}$ the two M\* agree | PASS |
| B1 | $\alpha^{-1}$ ansatz = 137.03600282194111918739454715858134949265661452923 | PASS |
| B2 | ansatz $-$ CODATA $2022 = 3.645\times10^{-6} (~174\sigma$; rel $2.660\times10^{-8})$ | PASS (the ansatz is NOT the measured value) |
| D1 | dE/$d\lambda$\|${}_{1} = (2-d)I_{grad} -$ dI_pot + $(4-d)I_{curv}$ | PASS |
| D2 | two-derivative stationarity is $(d-2)I_{grad}$ + dI_pot = 0 | PASS |
| D3 | curvature term marginal (exponent 0) iff d = 4 | PASS |
| E1 | pair identity (cos addition, applied twice) | PASS |
| E2 | full identity $\Sigma\cos = 4\Sigma\cos \cos ($trigsimp residual 0) | PASS (after script-bug fix, §3) |
| F1 | printed $-$ derived = pref$\cdotS + \mu^{2}\cdot($pref $-$ dt${}^{2}/(4M$\*)) | PASS (this difference IS the (7) failure) |
| F1b | $\mu^{2}$ terms differ too (unless $2J = a_{0}^{2}$, unstated) | PASS |
| F2 | J from derived formula at small k = M\*$c^{2}/12 ($manuscript's value) | PASS |
| F3 | J from printed formula at small k = M\*$c^{2}/24$ | PASS (contradicts the manuscript's J) |
| F4 | at k = 0, derived gives $\sin^{2}(\theta/2) = \Deltat^{2}\mu^{2}/(4M$\*) as §III.3 states | PASS |
| F5 | printed formula at k = 0 does NOT give the §III.3 relation | PASS (the CFL-table comparison itself is in the numeric script, G3-f/G4-f) |
| G1 | $\Sigma(k\cdot\alpha)^{2} = 12$\|k\|${}^{2}$ | PASS |
| G2 | $\Sigma(k\cdot\alpha)^{4} = 12$\|k\|${}^{4}$ | PASS |
| H1 | B\* = $2u\tau/(3$vq${}_{4})$ solves the amplitude equations | PASS |
| H2 | $r_{c} = 2u^{2}\tau^{2}/(9$vq${}_{4})$ | PASS |
| I1 | $D_{4} \tau^{2} = 8/3$ | PASS |
| I2 | $D_{4} q_{4} = 47/8$ | PASS |
| I3 | $D_{4} S = 64/141$ | PASS |
| I4 | $A_{4}$\*: $\tau^{2} = 9/5$, $q_{4} = 93/20$, S = 12/31 | PASS |
| I5 | ratio $S_{D}4/S_{A}4$\* = 496/423, margin 73/423 | PASS |
| I6 | BCC: $\tau^{2} = 4/3$, $q_{4} = 15/4$, S = 16/45 | PASS |
| I7 | $\tau_{D}4/\tau_{BCC} = \sqrt{2}$ | PASS |
| I8 | FCC $q_{4} = 27/8$, SC $q_{4} = 5/2 (Q$ recovery) | PASS |
| J1 | $r_{eff}(-0.18) = +0.1072$ | PASS |
| J2 | $r_{eff}(-0.10) = -0.12$ | PASS |
| J3 | $r_{eff}(0) = -0.35$ | PASS |
| J4 | $u_{eff}(-0.18) = 1.54$ | PASS |
| J5 | $A^{2}$ potential coefficient + (r/2)N = $(N/2)r_{eff}$ | PASS |
| J6 | $A^{3}$ coefficient = $-(T/3)u_{eff}$ | PASS |
| J7 | $A^{4}$ coefficient = vQ/4 | PASS |
| N1 | \|$W(D_{4})$\| = $2^{3}\cdot4! = 192$ | PASS |
| N2 | \|$W(D_{5})$\| = $2^{4}\cdot5! = 1920$ | PASS |
| N3 | $(-1/384)/(-1/768) = 2 (\xi_{2}$ retraction factor) | PASS |
| P1 | $\det(E_{6}$ Cartan) = 3 | PASS |
| P2 | Smith form = diag(1,1,1,1,1,3) | PASS |
| O1 | 24 vertices | PASS |
| O2 | all 576 products in the set | PASS (after script-bug fix, §3) |
| O3 | $Q_{8}$ has 8 elements | PASS |
| O4 | $Q_{8}$ normal in 2T | PASS (after script-bug fix, §3) |
| O5 | $2T/Q_{8}$ has 3 cosets of 8 | PASS |

### 5.2 Numeric checks (python-flint + numpy) — 33 PASS, 0 FAIL (exit 0)

| # | Check | Verdict |
|---|-------|---------|
| B2-f | $\alpha$ ansatz $-$ CODATA in $[3.6\times10^{-6}, 3.7\times10^{-6}] ($flint.arb, 200-bit precision) | PASS $(3.6449411\dots\times10^{-6})$ |
| B2-g | ansatz is ~$174\sigma$ from CODATA $(\sigma = 2.1\times10^{-8})$ | PASS |
| I1-f | $D_{4} S = 64/141 ($fmpq exact) | PASS |
| I3-f | $A_{4}$\* S = 12/31 (fmpq exact) | PASS |
| I5-f | ratio 496/423 (fmpq exact) | PASS |
| I6-f | BCC S = 16/45 (fmpq exact) | PASS |
| K1 | $r_{eff} = 67/625 = 0.1072$ exactly | PASS |
| K2 | $u_{eff} = 77/50 = 1.54$ exactly | PASS |
| K3 | stationarity discriminant > 0 (ordered branch exists) | PASS (disc = 32875776/625) |
| K4 | larger root A\* = 0.0775753 to 7 digits | PASS (0.0775753) |
| K5 | F(A\*$) = -0.0076323$ to 7 digits | PASS |
| K6 | F(A\*) < 0 (ordered below uniform) | PASS |
| K7 | $F_{unif} = -0.0034636$ to 7 digits | PASS |
| K8 | gap \|relaxed $-$ one-mode\| $\approx 9.53\times10^{-5} (1.23$% of relaxed); baseline ~$3.5\times10^{-3}$ cannot explain it | PASS |
| K9 | detuned discriminant < 0 (no ordered branch, as §II.7 states) | PASS $(-28614.7584)$ |
| G1-f | S at worst-case point = 32 exactly | PASS |
| G2-f | $48^{4}$ Brillouin-zone scan: grid max S = 32 (to $10^{-9})$ at (0,$\pi,\pi,0)$ | PASS |
| $G3-f (a_{0}/c)$ | $\sin^{2} = 4/3$ | PASS |
| $G3-f (2\pia_{0}/c)$ | $\sin^{2} = 16\pi^{2}/3 = 52.637890$ | PASS |
| $G3-f ((\sqrt{3}/2)a_{0}/c)$ | $\sin^{2} = 1$ exactly | PASS |
| G4-f | printed formula contradicts the CFL table (8/3 vs 4/3 at $\Deltat = a_{0}/c)$ | PASS (part of the (7) failure) |
| L1 | $\Psi($lattice point) = 24.0 | PASS |
| L2 | $\Psi($nearest $\mathbb{Z}^{4}$ point not in $D_{4}) = -8.0$ | PASS |
| L3 | $\Psi($deep hole$) = -8.0$ | PASS |
| L4 | $25^{4}$ scan: $\max \Psi = 24.0$, unique in the domain | PASS (1 maximum) |
| L5 | no other point within 0.1% of max (second-highest 23.8110, 0.79% below) | PASS |
| L6 | $16^{4}$ grid maxima = 32 | PASS |
| M1 | every root has exactly 8 partners with dot $-1 (120^\circ)$ | PASS |
| M2 | $24\times8 = 192$ ordered triads | PASS |
| S6-1 | $D_{4}$ scaled shell has 24 modes | PASS |
| S6-2 | competitor \|k\|${}^{2} = 7$ shell has 64 modes | PASS |
| S6-3 | penalties $(7.5-8)^{2} = (7.5-7)^{2} = 0.25$ | PASS |
| S6-4 | mode ratio 64/24 = 2.667 | PASS |

### 5.3 NOT RUN

- **Lean formalization** of any derivation (S7 — no formalization
  attempted in this task; the DVP guard therefore has nothing to
  check). The manuscript's Lean modules (8 modules, `lake build`
  exit 0 per CORE.md) are carried, not re-run.
- **R = 2589 derivation** — ABSTAIN (§6): no inputs in the source.
- **Envelope table under the author's unstated conditions** — the
  table is UNVERIFIED (§4.3); no further assumption set was invented
  to force a match.

---

## 6. ABSTAIN

**R = 2589 normalization (Part VII).** "I cannot verify this with the
available tools" — the source supplies no derivation inputs for the
number. The manuscript itself already downgrades it ("arithmetic
exact; the subtraction of 3 not forced"). Nothing in this task changes
that; no derivation was attempted from nothing.

---

## 7. Rival / failure mode (steelman and defeat)

**Strongest rival to the (7) verdict.** The printed (7) might be a
notational variant: perhaps the manuscript'$s \Sigma$ in (7) is meant to
denote half the neighbour sum, or $\mu^{2}$ is meant to carry a different
normalization, so that the printed form is "right under a different
reading". **Answer:** the manuscript itself blocks that escape. The
§III.2 expansion evaluates "the bracket" at the worst case as 32 —
the value of $\Sigma(1-\cos)$, not of $2\Sigma(1-\cos)$ — and the small-k J, the
k = 0 rest-mass statement, and the CFL table all agree with the
EOM-derived formula and disagree with the printed one. A notational
variant would have to be inconsistent with the manuscript's own
three uses of the formula. The verdict stands as a printed-equation
erratum, not as a claim that the physics is wrong.

**Strongest rival to the table verdict (UNVERIFIED).** The table's
author may have used a specific $(\Deltat, \theta$, direction, error definition)
under which all five entries are exactly right. **Answer:** that is
precisely why the verdict is UNVERIFIED rather than FAILED — the
table is underdetermined by the text, and no natural assumption set
reproduces it. The burden is on the unstated conditions, not on the
checks.

**Failure mode of this task.** A transcription check can pass a
manuscript's arithmetic while missing a wrong premise (e.g. the
definitional circle of §I.1, D1/A2: the triad closes iff
$L_{P}^{2} = \hbarG/c^{3}$, which is the definition of $L_{P}$ — a change of variables,
not a derivation, exactly as the manuscript itself says). Guard:
every check is labelled as arithmetic/identity verification, never
as a derivation of the constants; the Planck triad, the $\alpha$ ansatz,
and R = 2589 are all handled under the manuscript's own downgrades.

---

## 8. Grade summary (worst-of computations)

All new claims in this report: independence **I1** (artificial
verification sharing this pipeline's sources$) \to$ cap **C** (Track E).
Human source/balance gates not performed. Manuscript-carried grades
are cited, not re-earned.

| Claim | Independence bound | Caps | Postulation ceiling | Record | Final |
|-------|-------------------|------|---------------------|--------|-------|
| D1 Planck triad is a definitional circle | $I1 \to C$ | — | definitional $\to C$ | SymPy + manuscript's own statement | **C** |
| $D2 \alpha$ ansatz arithmetic exact; $174\sigma$ from CODATA | $I1 \to C$ | — | arithmetic $\to C$ | 50-digit SymPy + flint.arb; NIST SP 959 | **C** |
| D2-physical ("$\alpha$ derived") | — | — | — | manuscript itself downgrades to ansatz | **NOT CLAIMED (downgraded)** |
| D3 Derrick scaling; d = 4 marginality | $I1 \to C$ | — | derivation within stated premises $\to C$ | SymPy | **C** |
| D4 dispersion identity | $I1 \to C$ | — | identity $\to C$ | SymPy trigsimp | **C** |
| D5 printed (7) WRONG (factor $2 + \mu^{2}$ misplaced) | $I1 \to C$ | — | algebraic comparison $\to C$ | SymPy EOM derivation + 3 internal checks + manuscript's own §III.2 expansion | **C (FAILED as printed)** |
| D6 CFL bound + worst-case 32 + candidate values | $I1 \to C$ | — | derivation $\to C$ | SymPy + numpy $48^{4}$ scan + flint.arb | **C** |
| D7 isotropy moments | $I1 \to C$ | — | identity $\to C$ | SymPy | **C** |
| D8 selection rationals | $I1 \to C$ | — | arithmetic $\to C$ | SymPy + flint.fmpq | **C** |
| D9 ordered branch A\*/F/baseline/detuned | $I1 \to C$ | — | arithmetic $\to C$ | SymPy + flint.fmpq | **C** |
| $D10 \xi_{2}$ retraction factor 2 | $I1 \to C$ | — | arithmetic $\to C$ | SymPy | **C** |
| $D11 E_{6}$ Cartan det 3, Smith form | $I1 \to C$ | — | identity $\to C$ | SymPy | **C** |
| D12 24-cell = 2T closure | $I1 \to C$ | — | exact arithmetic $\to C$ | SymPy (half-unit integers) | **C** |
| D13 Weyl orders 192/1920 | $I1 \to C$ | — | arithmetic $\to C$ | SymPy | **C** |
| D14 resonance maximum 24 unique; $16^{4} 32$-count | $I1 \to C$ | — | numerical scan $\to C$ | numpy $25^{4} + 16^{4}$ | **C** |
| D15 8 partners at $120^\circ$; 192 triads | $I1 \to C$ | — | enumeration $\to C$ | numpy | **C** |
| D16 shell counts 24/64; penalties 0.25 | $I1 \to C$ | — | enumeration $\to C$ | numpy | **C** |
| D17 envelope validity table | $I1 \to C$ | underdetermined from source | — | numpy reproduction attempt (§4.3) | **UNVERIFIED** |
| D18 R = 2589 | — | no inputs in source | — | source inspection | **ABSTAIN** |
| D19 exact linearity at $\Deltat = a_{0}/c ($axis + body diagonal) | $I1 \to C$ | — | identity + numeric $\to C$ | hand identity + numpy $(~10^{-13})$ | **C** |
| Geometric core (carried) | (repo record) | — | — | CORE.md / verification/ | **A (carried)** |

---

## 9. Evidence that would change the answer

- **For the (7) verdict:** a derivation from the stated action that
  yields the printed $[2\Sigma + \mu^{2}]$ form — e.g. a different neighbour
  convention in which the EOM'$s \Sigma$ is half the $(7) \Sigma$ — together with
  a correction of the §III.2 expansion (which currently evaluates
  the bracket as 32). Absent that, the erratum stands.
- **For the CFL bound:** nothing short of a different worst-case
  sum (the $48^{4}$ scan pins it at 32) or a different J (the small-k
  match pins it at M\*$c^{2}/12)$.
- **For the envelope table:** the author stating $\Deltat$, $\theta ($or $\mu)$, the
  direction, and the error definition used; the table can then be
  re-checked in minutes.
- **For the $\alpha$ ansatz:** a derivation (not an arithmetic identity)
  connecting $137 + 1/(28-\pi/14)$ to the fine-structure constant; the
  manuscript itself records that no such derivation exists.
- **For R = 2589:** derivation inputs in the source.

---

## VERIFIED / UNVERIFIED / FAILED branch lists

**VERIFIED (both tools agree, at grade C unless carried):**
- D1, D2 (arithmetic), D3, D4, D6, D7, D8, D9, D10, D11, D12, D13,
  D14, D15, D16, D19.
- The CFL bound and its candidate values; the worst-case sum 32.
- The ordered-branch values to 7 digits; the detuned no-branch
  discriminant.
- The resonance maximum 24 (unique) and the $16^{4} 32$-count.
- The manuscript's own downgrades: $\alpha$ ansatz is not the measured
  value $(174\sigma)$; $\xi_{2} = -1/384$ is retracted (factor 2 confirmed).

**UNVERIFIED:**
- D17 envelope validity table (underdetermined from source; §4.3).
- Manuscript-carried grades (geometric core A) — cited, not re-run.

**FAILED:**
- **D5 printed dispersion relation (7) — FAILED as printed.** Factor
  of 2 in the $\Sigma$ term; $\mu^{2}$ misplaced inside the bracket. The
  EOM-derived formula is correct (three internal checks + the
  manuscript's own §III.2 expansion). The CFL bound computed from
  it is VERIFIED. Erratum, not refutation.

**ABSTAIN:**
- D18 R = 2589 (no derivation inputs in the source).

---

## 10. Ledgers

### 10.1 Assumption ledger

| # | Assumption | Where it enters | Status |
|---|------------|-----------------|--------|
| A1 | Manuscript equations transcribed as printed (including (7) as printed) | D5 | Transcription (verified against the rebuilt source text) |
| A2 | $L_{P}^{2} = \hbarG/c^{3} ($definition of the Planck length) | D1 | Definition (manuscript §I.1 states the circle) |
| A3 | CODATA $2022 \alpha^{-1} = 137.035999177(21) ($NIST SP 959) | D2 | Primary source, verified by web search |
| A4 | Dual shell = ${\pme_{i}} \cup {(\pm$½,$\pm$½,$\pm$½,$\pm$½)} for the §II.2 resonance scan | D14 | Hand-derived; confirmed by the scan (max 24 unique, $-8$ at the two test points) |
| A5 | §II.6 normalization: box $L = 2\pi$, shell ${(\pm2,\pm2,0,0)}$, grid step $\pi/8$ | D14 (L6) | Manuscript's stated normalization; 32-count reproduced |
| A6 | Envelope table readings tried: $\omega$ vs c\|k\| $(\Deltat\to0, \Deltat$ = CFL), error in $\omega^{2}$, envelope-vs-quadratic | D17 | Stated assumption sets (§4.3); none reproduces the table |
| A7 | This report: symbolic + numeric verification only; no Lean formalization | All | Method choice (stated §2) |

### 10.2 Parameter ledger

| Parameter | Value | Provenance | Role |
|---|---|---|---|
| $\alpha^{-1}$ ansatz | 137.03600282194111918739454715858134949265661452923 | SymPy 50-digit + flint.arb (agree) | Arithmetic only; NOT the measured value |
| $\alpha^{-1}$ CODATA 2022 | 137.035999177(21) | NIST SP 959 | Primary reference |
| ansatz $-$ CODATA | $3.6449411\times10^{-6} ($rel $2.6598420\times10^{-8}, ~174\sigma)$ | Both tools | Confirms the manuscript's downgrade |
| J | M\*$c^{2}/12 ($derived formula); M\*$c^{2}/24 ($printed formula) | SymPy small-k match | Discriminates D5 |
| worst-case $\Sigma(1-\cos)$ | 32 exactly | numpy $48^{4}$ scan + exact evaluation | CFL bound |
| $\Deltat_{max}$ | $(\sqrt{3}/2)a_{0}/c \approx 0.866a_{0}/c$ | Both tools | CFL bound |
| A\* | 0.0775753 | flint.fmpq + float solve | Ordered branch |
| F(A\*) | $-0.0076323$ | Both tools | Ordered branch |
| $F_{unif}$ | $-0.0034636$ | Both tools | Uniform baseline |
| detuned discriminant | $-28614.7584$ | flint.fmpq | No branch at $r_{shell} = -0.10$ |
| $S(D_{4})$ | $64/141 \approx 0.4539$ | Both tools (exact rationals) | Selection |
| $S(A_{4}$\*) | $12/31 \approx 0.3871$ | Both tools | Selection |
| margin | $73/423 \approx 17.26$% | Both tools | Selection |
| resonance max | 24.0 (unique); second 23.8110 | numpy $25^{4}$ scan | §II.2 |
| $16^{4}$ maxima | 32 | numpy | §II.6 |
| $\det(E_{6}$ Cartan) | 3; Smith diag(1,1,1,1,1,3) | SymPy | §IV.3 |
| 2T products | 576 closed; $Q_{8}$ normal; 3 cosets | SymPy | §IV.2–3 |

### 10.3 Choice ledger

| Choice | Why | Effect if changed |
|--------|-----|-------------------|
| Two tools: SymPy + (flint + numpy) | Truth-seeking computation gate: above CLAIMED needs a second independent tool | A single tool would cap the arithmetic at CLAIMED |
| python-flint 0.8.0 recorded as actual (brief said 0.9.0) | Ground truth is the installed version | None on the results |
| Envelope table graded UNVERIFIED, not FAILED | The numbers may be right under unstated conditions | A FAILED grade would overstate the evidence |
| (7) graded FAILED as printed, bound VERIFIED | The two are separable: the bound was computed with the right formula | Conflating them would either falsely condemn the bound or falsely excuse the equation |
| R = 2589 ABSTAIN, not FAILED | No inputs to check against | A FAILED grade would claim a refutation that was never performed |

---

## 11. Scripts

- `task10_scripts/task10_sympy_checks.py` — SymPy 1.14.0 transcription
  and checks (45 checks). Run log:
  `task10_scripts/task10_sympy_run_2026-11-10.log` (exit 0).
- `task10_scripts/task10_numeric_checks.py` — python-flint 0.8.0 +
  numpy 2.4.6 second-tool checks (33 checks). Run log:
  `task10_scripts/task10_numeric_run_2026-11-10.log` (exit 0).

Both scripts print [PASS]/[FAIL] per check and exit non-zero on any
FAIL. Both were re-run after the first-run fixes (§3) to ALL PASS.

---

*Report prepared 2026-11-10 (workstream D, task 10, direct session work).
AI contribution: transcription, symbolic and numeric checking, drafting
under HLRE v5.1 / truth-seeking-frontier v5 / cross-domain-discovery
v2.0.0. Human author and accountable party: Brandon D. McCrary. All
verification artificial (I1); human source/balance gates not performed;
new claims cap at C. No repo commits, no manuscript edits, no filing.*
