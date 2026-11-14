# Workstream D — Frameworks & Rivals: summary (tasks 8, 9, 10, 12)

**Co-scientist task programme, 2026-11-10. Workstream D.**
**Method:** deepest-research FULL mode throughout (stated plainly in each
report; systematic-review mode NOT chosen and NOT used). Skills:
truth-seeking-frontier v5, cross-domain-discovery v2.0.0 (S1–S7),
HLRE v5.1. Where the skills conflict, the one that made more sense in
the instance governed (programme brief). All new claims: artificial
verification, I1 max, Track E cap C / Track F cap F3 (human
source/balance gates not performed). IRH geometric-core grades are
carried from the repo record, cited not re-earned. No repo commits, no
manuscript edits, no filing, no GCP spend, no VM touched, Gemini grader
never called.

---

## 1. Deliverables (all in this directory)

| File | Task | Status |
|------|------|--------|
| `task8_qg_frameworks.md` | 8 — Compare quantum gravity frameworks | FINAL (assembled; 6 assembly corrections — see its Assembly notes) |
| `task8_qg_matrix.md` | 8 — cross-referenced matrix | FINAL |
| `task9_spacetime_frameworks.md` | 9 — Compare spacetime frameworks | FINAL (assembled; 1 assembly correction — K2 clean re-check) |
| `task9_spacetime_matrix.md` | 9 — cross-referenced matrix | FINAL |
| `task10_derivations_check.md` | 10 — Check your derivations | FINAL (direct session work) |
| `task10_scripts/task10_sympy_checks.py` + `task10_sympy_run_2026-11-10.log` | 10 — SymPy transcription | 45 PASS / 0 FAIL, exit 0 |
| `task10_scripts/task10_numeric_checks.py` + `task10_numeric_run_2026-11-10.log` | 10 — second tool (flint + numpy) | 33 PASS / 0 FAIL, exit 0 |
| `task12_rival_accounts.md` | 12 — Formalize rival accounts | FINAL (assembled; driver re-run verified) |
| `task12_divergence_table.md` | 12 — shared-conditions table, D1–D7 | FINAL |
| `task12_models/` (5 models + `compare_driver.py` + `driver_output.txt` + `driver_rerun_2026-11-10.log`) | 12 — executable models | 55 PASS / 0 FAIL, exit 0 (re-run verified) |
| `task8_qg_frameworks_DRAFT.md`, `task9_spacetime_frameworks_DRAFT.md`, `task12_rival_accounts_DRAFT.md` | — | Children's verbatim drafts, preserved |

---

## 2. Headline findings (one paragraph per task)

**Task 8 — quantum gravity frameworks.** No framework in the set
derives Lorentzian signature, the Einstein equations with
diffeomorphism invariance, the Standard Model gauge structure, and a
confirmed prediction all at once. The strongest derived emergence
result is CDT's numerical 4D de Sitter universe with spectral
dimension running $4.02 \pm 0.1 \to 1.80 \pm 0.25 ($Ambjørn–Jurkiewicz–Loll
2004/2005; numbers verified in assembly via Giasemidis et al. 2012,
eq. 7); the only prediction-in-advance is causal sets' heuristic
$\Lambda \sim 10^{-120} ($Sorkin 1997, pre-1998); LQG's sharpest derived result is
kinematic (discrete area/volume, Rovelli–Smolin 1995) with the EPRL
classical limit still open; AdS/CFT remains a conjecture (Maldacena
1997) formulated in AdS, not de Sitter; asymptotic safety's Reuter
fixed point is truncation-only evidence; GFT condensate cosmology
yields a modified Friedmann equation but the condensate-as-GR-geometry
step is unestablished. IRH's position is the narrowest and most
checked at the geometric level — $D_{4}$ selection $(S = 64/141 \approx 0.454)$
and $E_{6}$ via 2T/McKay are Grade A (carried) — while its gravity side
is open or retracted by its own Part IX. The Bartha gate (S4) FAILS
the transfer "substrate dynamics $\Rightarrow$ Einstein equations" for IRH and
analogue gravity generally, confirming IRH v93.1's own retraction
against Barceló–Liberati–Visser 2011 and Sindoni 2012.

**Task 9 — spacetime frameworks.** IRH's constants account is its
weakest part by its own ledger: the §I.1 triad relations are
definitional re-expressions of measured Planck quantities (SymPy
confirms $a_{0}\Omega_{P} = c$ — algebraic consistency only); the $\alpha^{-1}$ ansatz
$137 + 1/(28 - \pi/14) = 137.036002821941$ is arithmetic-exact but differs
from CODATA 2022 by +$3.64\times10^{-6}$ and remains a downgraded numerical
ansatz in the Eddington class; the dimensional assignment (A)/(B)/(C)
is undecided and not resolvable by calculation; no signature mechanism
or Einstein-equation derivation exists in IRH. Of the rivals, only
Greensite/Carlini–Greensite (quantum, one-loop, fermion-dominant) and
Mukohyama–Uzan/Kehayias et al. (classical, clock field,
Galileon-not-GR gravity) claim a signature derivation, and every
derivation-transfer into IRH FAILS the Bartha S4 audit; analog gravity
gives an effective metric, never $G = 8\piT$; no surveyed account derives
$\alpha$. IRH's distinctive Grade A result $(D_{4}$ selection) is a question no
rival attempts, so the matrices code rather than crown a winner.

**Task 10 — derivations check (the new finding of this workstream).**
78 checks pass (45 SymPy + 33 flint/numpy), 0 fail on re-run — with
two exceptions. (1) **Printed dispersion relation (7) in §III.1 is
WRONG by a factor of 2, and misplaces $\mu^{2}$ — FAILED as printed.** The
EOM-derived formula is $\sin^{2}(\omega\Deltat/2) = (\Deltat^{2}\cdot2J/(4M$\*$a_{0}^{2}))\cdot\Sigma(1-\cos)$ +
$(\Deltat^{2}\mu^{2})/(4M$\*); the printed (7) has $[2\Sigma(1-\cos) + \mu^{2}]$ inside one
bracket. Three internal checks favour the derived formula (small-k J
= M\*$c^{2}/12$, the manuscript's own value, vs M\*$c^{2}/24$ from the printed
formula; k = 0 gives $\sin^{2}(\theta/2) = \Deltat^{2}\mu^{2}/(4M$\*) as §III.3 states; the
CFL table matches the derived formula), and the manuscript's own
§III.2 expansion ("at the worst case the bracket equals 32") uses the
derived formula, contradicting the printed (7). **The CFL bound
itself is CORRECT** (worst-case sum 32 confirmed by $a 48^{4}$
Brillouin-zone scan; candidate values 4/3, $16\pi^{2}/3$, 1 reproduced).
This is a manuscript erratum to one printed equation, not a refutation
of the bound. (2) **The §III.3 envelope validity table $(4\times10^{-5}, 0.1$%,
1.0%, 11%, 133%) is NOT REPRODUCIBLE from the text as written —
UNVERIFIED.** Under the natural reading the computed errors are
$1.67\times10^{-5}$, $4.17\times10^{-4}$, $3.75\times10^{-3}$, 4.11%, 36.3% $(\Deltat\to0)$; the zone-edge
133% is unreachable under that reading. Note: the summary claim
"<1% for $a_{0}$|k| ≲ 0.3" (VI.3) still holds under the recomputed values
(0.042% at 0.10, 0.375% at 0.30) — the boundary survives; the table's
exact entries do not reproduce. Also verified: $\alpha$ ansatz $174\sigma$ from
CODATA; $\xi_{2}$ retraction factor 2; R = 2589 ABSTAIN (no inputs in source).
Side finding: at $\Deltat = a_{0}/c$ the discrete dispersion is exactly linear
$(\omega = c$|k|) along axis and body-diagonal directions.

**Task 12 — rival formalizations.** Five rival accounts formalised as
executable models and run under shared conditions against IRH as
reference (55 checks, all PASS). Sharpest divergences: (D1) the
Greensite signature mechanism predicts Lorentzian signature iff
$n_{F} > n_{B}$, where IRH predicts nothing — and the transfer into IRH
FAILS Bartha (no DOF count in a single classical scalar substrate);
(D2) a toy linear $\alpha$ drift of $1\times10^{-15}$/yr is excluded ~$25.6\times$ by the
Rosenband 2008 bound $\dot{\alpha}/\alpha = (-1.6\pm2.3)\times10^{-17}$/yr, while Dirac $G\propto1/t$
gives Ġ/$G = -7.25\times10^{-11}$/yr; (D3) Ġ/G has no verified primary-source
bound in this run (ABSTAIN — no verdict on Dirac); (D4) CDT spectral
dimension flows $1.82\to4.02$ while IRH holds D = 4 at all scales (gap
~2.18 at $\sigma\to0$; endpoint disputed, ~2 vs ~3/2); (D5) the anthropic
account accommodates the observed $\Lambda$ under every prior but its
typicality number swings ~$80\times$ with the prior (0.0015 uniform vs
0.1204 log-uniform) — prediction vs accommodation is the divergence;
(D6) no rival here derives $\alpha^{-1}$, and neither does IRH; (D7) deciding
§IX.2 is a prerequisite for any signature comparison.

---

## 3. Consolidated grades (worst-of; all new claims I1, cap C / F3)

| Area | Grade | Basis |
|------|-------|-------|
| IRH geometric core $(D_{4}$ selection, $E_{6}$, isotropy, CFL, envelope, d = 4) | **A (carried)** | Repo record (CORE.md / verification/); cited, not re-earned |
| IRH physical/substrate reading | **C/D (carried)** | Manuscript Part X |
| Task 8 comparative claims C1–C12 | **C** | $I1 \to C$; primary sources confirmed in session |
| Task 8 C9-interpretation ("gravity is emergent") | **D** | Exploratory; live alternatives |
| Task 9 rival characterisations C1–C6, C8 | **C** | $I1 \to C$; scoped to surveyed sources |
| Task 9 C7 (no rival derives $\alpha)$ | **C scoped / UNVERIFIED universal** | Verified for surveyed sources only |
| Task 10 derivation checks D1–D16, D19 | **C** | Two independent tools agree |
| Task 10 D5 printed (7) | **C (FAILED as printed)** | EOM derivation + 3 internal checks + manuscript's own §III.2 expansion |
| Task 10 D17 envelope table | **UNVERIFIED** | Underdetermined from source |
| Task 10 D18 R = 2589 | **ABSTAIN** | No inputs in source |
| Task 12 formal claims G1, G5, G8, G12 | **F3** | Two tools; capped (human gates not run) |
| Task 12 physical claims G2, G9, G13, G14 | **C** | $I1 \to C$ |
| Task \$12 $G4 (\alpha$\$ ansatz) | **D (ansatz only)** | Manuscript downgrade |
| Task 12 G11 (anthropic typicality) | **D (accommodation)** | ~$80\times$ prior swing demonstrated |

No IRH grade is changed by any task in this workstream.

---

## 4. Consolidated ABSTAINs

1. Barbero–Immirzi numerical value / quantitative LQG black-hole-entropy matching (task 8; secondary only).
2. String landscape vacuum counts; SUSY/extra-dimension exclusion limits (task 8).
3. Strominger–Vafa microstate counting as a load-bearing claim (task 8; not verified in session).
4. 2023 GFT mean-field interpretive gloss "justified" — SECONDARY-ONLY (task 8).
5. Current post-2011 status of varying-$\alpha$ observations; present best bound on $\dot{\alpha}/\alpha ($task 9).
6. Current standing of the Greensite mechanism beyond 1993–94 (task 9).
7. Whether any specific NCG coupling/Higgs-mass prediction has been falsified/confirmed (task 9).
8. Universal negative "no framework anywhere derives $\alpha$" (task 9; verified only for surveyed sources).
9. Any head-to-head IRH-vs-rival ranking (task 9; no shared prediction exists).
10. Full Greensite one-loop mechanism — exact $V(\theta)$, D = 4 uniqueness (task 12; toy sign-flip only).
11. Causal-set spectral-dimension numbers (task 12; no formula verified from a primary source).
12. Any primary-source Ġ/G constraint; no verdict on Dirac varying-G (task 12).
13. CDT small-scale endpoint (~2 vs ~3/2) — literature tension, unresolved (task 12).
14. R = 2589 (task 10; no derivation inputs in the source).
15. **Withdrawn in assembly:** task 8's ABSTAIN on precise CDT spectral-dimension numbers $(4.02 \pm 0.1 / 1.80 \pm 0.25)$ — verified in the primary literature (Giasemidis et al. 2012, eq. 7).

---

## 5. Consolidated FAILED / Bartha results

- **Printed dispersion relation (7) — FAILED as printed** (task 10; factor of $2 + \mu^{2}$ misplaced). CFL bound VERIFIED.
- **Transfer "substrate dynamics $\Rightarrow$ Einstein equations" — Bartha FAIL** (task 8 §6.1; task 9 F3; task 12 — no such transfer constructed). Confirms IRH v93.1's own retraction.
- **Jacobson $\Rightarrow$ IRH transport — FAILS / NOT ESTABLISHED** (task 8 §6.2; thermodynamic premises have no positive analogue in IRH).
- **Dynamical signature $\Rightarrow$ IRH reading (A) — FAILS for v93.1** (task 8 §6.3; task 9 F1; task 12 G7 — fermion-dominant loop absent from a single real scalar).
- **Mukohyama–Uzan clock-field signature $\Rightarrow$ IRH — FAILS** (task 9 F2; no clock field, no coupling, Galileon-not-GR gravity).
- **"IRH'$s E_{6}$ identification derives coupling values / $\alpha$" — FAILED** (task 9 F4; no breaking pattern, no RG running; §IX.4).
- **"Anthropic reasoning explains $\alpha$ or IRH's tunings" — FAILED / NOT SUPPORTED** (task 9 F5; ensemble unobserved; not in the manuscript).
- **Eddington's derivation of $\alpha$ — FAILED by measurement** (task 9 F6; historical control case).
- **Triad relations as derivations of c, $\hbar$, G — NOT A DERIVATION** (task 10 D1; task 12 G3; definitional identities only).
- **Anthropic typicality as a prediction — FAILED as prediction** (task 12 G11; retained as an accommodation, grade D).

---

## 6. Cross-references between the four tasks

- Task 10's eq. (7) erratum bears on tasks 8 and 9 wherever they cite
  the §III.1 dispersion or the §III.3 envelope validity: the CFL bound
  and J value they carry are unaffected (computed with the right
  formula); the §III.3 table's exact entries are UNVERIFIED (task 10
  §4.3), but the VI.3 summary boundary (<1% for $a_{0}$|k| ≲ 0.3) survives
  the recomputation.
- Task 10's clean flint.arb $\alpha$-ansatz value $(137.036002821941119\dots$,
  diff +$3.6449411\times10^{-6})$ is the second-tool confirmation for task 9's
  K2 (whose ad-hoc flint run errored after printing) and for task 12's
  Model $A \alpha$ check.
- Task 8's CDT numbers, verified in assembly (Giasemidis et al. 2012,
  eq. 7), are the primary-source basis for task 12's Model E fit
  evaluation (1.82 at $\sigma\to0$, within $1.80 \pm 0.25)$.
- Task 12's Model B toy and task 9's §3.2–3.3 agree on the Greensite /
  Mukohyama–Uzan Bartha FAILs by independent routes (toy sign-flip vs
  literature audit).
- Task 9's Eddington analysis (§3.7a) is the control case for task 10's
  and task 12's handling of the $\alpha$ ansatz (arithmetic exact, derivation
  absent, honestly labelled).

---

## 7. Assembly verification record (parent agent, 2026-11-10)

Work done in assembly beyond the children's drafts:

- **Task 10 (direct session work):** SymPy script written, run, two
  script bugs fixed (E2 mis-stated identity; O2/O4 quaternion product
  missing /2), re-run to ALL PASS (45 checks, exit 0). Numeric
  second-tool script written and run (33 checks, exit 0, after an
  assembly fix to the G3-f loop indentation — see task 10 report §3).
  Logs saved.
  Manuscript §III.1–III.3 re-read in the rebuilt source to quote the
  printed (7), the §III.2 expansion, and the §III.3 table verbatim.
  CODATA 2022 verified via web search (NIST SP 959).
- **Task 8 spot-checks:** arXiv:1703.07556 shown to be Dowker & Zalel
  2017, not a survey — citation corrected to Surya LRR 2019
  (arXiv:1903.11544, full text read; "only successful prediction"
  phrase not found there and dropped); arXiv:2307.13743 confirmed
  (Das–Nasiri–Yazdi, everpresent-$\Lambda$ tests); arXiv:0712.2485 abstract
  confirms 17–28 Planck lengths; Giasemidis et al. 2012 eq. (7) read
  in full text, verifying the CDT numbers and withdrawing the ABSTAIN.
- **Task 9:** no citation re-check beyond task 10'$s \alpha$ cross-check
  (clean flint.arb run supersedes the child's errored ad-hoc run).
- **Task 12:** driver independently re-run (exit 0; 55 `[PASS]`,
  0 `[FAIL]`; check lines identical to saved `driver_output.txt`);
  Rosenband 2008 bound confirmed (PubMed/NIST); CDT fit formula
  confirmed (Giasemidis et al. 2012, eq. 7, full text read).
- **EXCLUDED-claims audit (all four reports):** grep for so(8), Kerr
  solitons, three generations derived, $\xi_{2} = -1/384$, v92 time steps,
  monopole absence, universal $D_{4}$ optimality — every occurrence is in
  an exclusion list, a retraction context, or an "EXCLUDED by theorem"
  statement. No EXCLUDED claim is revived as a live claim in any
  report.
- **Known imperfection in the record:** one exec in the task-12
  child's history exited non-zero per the runtime record (command not
  shown); no result depends on it — the final driver state was
  re-verified independently (above).

---

## 8. What would change the answers (consolidated)

- A derivation of (7)'s printed form from the stated action, with a
  correction of the §III.2 expansion (task 10).
- The author stating $\Deltat$, $\theta ($or $\mu)$, direction, and error definition for
  the §III.3 envelope table (task 10).
- A derivation of $\alpha^{-1} ($or of $c/\hbar/G)$ from substrate premises — not a
  change of variables, not closeness to a future CODATA value
  (tasks 9, 10, 12).
- A classical Euclidean substrate yielding Lorentzian signature; a
  substrate thermodynamics supporting a Jacobson-type argument; an
  IX.2 decision with a construction (tasks 8, 9, 12).
- A multiverse measure fixed independently of the observed $\Lambda$ value
  (task 12); a verified primary-source Ġ/G bound tighter than
  ~$7\times10^{-11}$/yr (task 12); a settled CDT small-scale endpoint (task 12).
- A proved continuum/classical limit for EPRL/CDT/GFT, a proved
  AdS/CFT duality, or a demonstrated Reuter fixed point beyond
  truncations (task 8).

---

*Workstream D complete 2026-11-10. Three child agents (tasks 8, 9, 12)
produced drafts; task 10 was done directly by the parent session; the
parent agent verified, corrected (see the Assembly notes in each final
report), and assembled the finals. Human author and accountable party:
Brandon D. McCrary. All verification artificial (I1); human
source/balance gates not performed; new claims cap at C / F3.*
