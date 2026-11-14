# Audit of the Hark replication audit — D4 work package (WS-A, WS-C, WS-E), 2026-11-10

**Section-number note (2026-11-11):** the guide references in this
review (§6.1, §8, §9, §5.1, §5.2, §4.5) are to the guide as of
2026-11-10 22:50 CST. WS-D was inserted as guide §6 on 2026-11-11,
shifting WS-E to §7 and the later sections by one; the review's
references were correct when written and are left as-is.

**Audited document:** `D4_package_2026-11-10_replication_audit_4_yq6o.md`
(uploaded by Brandon 2026-11-10 22:36 CST; auditor "Hark (IRH project)").
**This review:** claim-by-claim check of Hark's audit against (a) the
manuscript text (`IRH_v93_1_source_rebuilt.txt`, 1,638 lines), (b) the repo
record (IRH-Theory-Development-Workspace; 2026-10-30 deepest-research
report; 2026-11-02 v5 test report), and (c) the package itself
(`d4-work-2026-11-10.zip` as delivered, plus the workstream directories).
**Standard:** HLRE v5.1; truth-seeking computation gate.
**My independence: I1.** I re-ran the package's own code and wrote my own
checks on the package's stepper. I did NOT re-run Hark's `hark_checks/`
(they are not in my workspace), and I did NOT re-run Hark's full
replication table — the rows I re-ran or checked by reading code are
listed per finding below. No grade here moves above C (Track E) / F2
(Track F, two-route) on the strength of this review.

**Amendment note.** The audited document opens with an amendment dated
2026-11-10 22:33 CST stating Brandon repealed the HLRE §6.5 human-gate
requirement for this assessment. That repeal is recorded in Hark's
document, not in my own conversation record with Brandon; I assess the
audit on its terms (Track E unchanged, $I1 \to C$; Track F two-route claims
$F3 \to F2)$ and flag the provenance here rather than silently adopting it.
Nothing in this review depends on the repeal for its Track E conclusions:
WS-A's A/B grades fall to C on the independence bound alone.

## Verdict summary

| Hark claim | verdict | one line |
|---|---|---|
| §1 replication table (all rows) | PARTLY VERIFIED (see §1) | every row I re-ran or checked reproduces; rows I did not re-run are NOT independently confirmed by me |
| F1 hex6/fcc12 "stable attractors" FAILED as written | **VERIFIED — by my own run** | 5/5 hex6 + 4/4 fcc12 transverse perturbations $\to$ full24 at $\bar{\psi}=-0.18$; control stays hex6 |
| $F1 \bar{\psi}=0 (24$-mode+noise $\to 6$-mode) and $\bar{\psi}=+0.10 (\to 2$-mode stripe) | REPORTED, NOT RE-RUN | consistent with the WS-C numbers quoted; my check covered $\bar{\psi}=-0.18$ only |
| F1 stripe side-result (one run, not graded) | UNVERIFIED | single Hark run; not re-run; plausible, not established |
| F2 lock metric ill-defined for partial patterns | **VERIFIED** (code reading) | `analyze` averages cos S over all 32 triads incl. roundoff modes; fix (active triads only) is correct |
| F3 flint band-edge leg vacuous | **VERIFIED — by my own run** | `bifurcation_flint_check.py` prints `coexistence band edges (flint): []`; values confirmed by Hark arb + my SymPy solve |
| F4 task2d/make_figures provenance gap | **VERIFIED — by my own re-run** | task2d (T=5 only) overwrites the CSV; make_figures then crashes `IndexError` line 88; shipped T=0.5/1.0 rows match Hark's regeneration |
| §1 task1 JSON provenance gap (extra fields) | **VERIFIED — by my own re-run** | fresh output lacks `n_distinct_positions`/`max_multiplicity`; shipped JSON came from another script revision |
| §1 task1 "different lattice basis" | NOT REPRODUCED in my env | my re-run gives basis identical to shipped for all 7 directions (NumPy 2.4.6); Hark's env (NumPy 2.5.4) may differ — environment-dependent, no number changes |
| §1 "29 vs 31 checks" | RESOLVED, not a discrepancy | 29 check() call sites; the $r_{eff}$ table loops over 3 rows $\to 31 [$PASS] lines. Guide wording must state both |
| F5 WS-A grade inflation $(A/B \to C)$ | **VERIFIED** | independence bound $I1 \to C$ caps Track E; WS-A's A/B grades fall regardless of the human-gate amendment |
| F6 brief "established facts" vs round-1 review | **SUBSTANTIATED, with nuance** | review grades C6/C8 D (see §F6); brief's "do not re-litigate" label overstates them, but the brief itself demands the qualification travel with the claim |
| §3 "round-1 review had $\approx [-0.235, -0.14]$ with stripes/A2/A3" | **UNVERIFIED — source not located** | no such band in the 2026-10-30 report, the v5 test report, CORE.md, or the manuscript |
| §4 B1 (§I.2 inconsistent; Model B vs MPFC) | SUBSTANTIATED on manuscript text | manuscript §I.2 states $\partial^{2}_{t}\psi+\gamma\partial_{t}\psi = -\deltaF/\delta\psi ($non-conserved RHS) then demands conserved dynamics; the conserved-MPFC form appears in neither manuscript nor package |
| §\$4 $R4 (L=\pi$\$ box cannot hold A4*; no fair test) | SUBSTANTIATED as a statement about the package | no A4* simulation exists in the package; "Step 1.2" citation unlocated |
| §4 common-tangent diagram still fixed-$\bar{\psi}$ | SUBSTANTIATED | package does fixed-$\bar{\psi}$ minimisation everywhere |
| §4 B2/B3 untouched by design | TRUE | programme scope; no claim made |
| §6 regrade table | ACCEPTED (with the amendment) | $M6 \to F2 ($two routes in the package, verified); Aut(D4) stays F3 (one route); WS-E C1–$C3/C6 \to F2$; $C4 \to F2 ($SymPy + arb); WS-C C1.4/$C2.1/C2.5 \to F2$ |

## §1. The replication table — what I checked myself

Hark re-ran guide §9 in order in a different environment (Python 3.12.16,
NumPy 2.5.4, flint 0.9.0, z3 5.3.3). I re-ran or checked the following rows
directly; the rest I did not re-run and do not independently confirm.

- **WS-E bifurcation_flint_check.py — CONFIRMED.** My own run (conda env,
  python-flint 0.8.0) prints `coexistence band edges (flint): []` and
  `ALL FLINT CHECKS DONE`. All other values $(r_{c}$,eff, $r_{spin}$,eff,
  thresholds, A\*, F(A\*)) agree with SymPy. This is F3 (see below).
- **WS-C exact_checks.py — CONFIRMED, 31 [PASS].** My own run prints 31
  `[PASS]` lines, 0 FAIL, `ALL CHECKS PASSED`. The script has 29 check()
  call sites; the $r_{eff}$ sign-table loop (lines 81–84) executes one call
  site 3 times $(-0.18, -0.10, 0.0)$, so 29 statements $\to 31$ executions.
  The guide's "29 checks" and Hark's "31 [PASS]" are both true under
  different countings. The guide must state both numbers; Hark's
  parenthetical framing it as a discrepancy is a counting-convention
  difference, not a package error.
- **WS-C task2d_transient.py + make_figures.py — CONFIRMED (F4).** In a
  scratch copy I re-ran task2d (rc=0; T=5 rows reproduce the shipped
  T=5 rows exactly: $\langleA\rangle = 0.077682$, Fexc = $-0.007728$ at all four dt);
  the re-run overwrote `results/task2_transient.csv` with T=5-only rows
  (4 rows); make_figures.py then crashed with
  `IndexError: index -1 is out of bounds for axis 0 with size 0` at
  line 88 (`ref = err[-1] ...` on the empty T=0.5 filter). Hark's "rc 1"
  is the script's exit code on uncaught exception (my shell echo
  captured the pipeline's rc, not the script's — the traceback is the
  evidence). The shipped CSV's T=0.5 rows $(\langleA\rangle = 0.07803$, 0.078126,
  0.078177, 0.078203) match Hark's regenerated values exactly, so the
  $p \approx 0.95$ claim stands; the provenance is broken, not the numbers.
- **WS-A task1_projections.py — CONFIRMED, with one correction to Hark.**
  My re-run (scratch copy, conda env) gives lattice_fraction identical
  to shipped for all 7 directions (1.0 rational; 0.16996587030716723 =
  249/1465 irrational) and **lattice_basis identical to shipped for all
  7 directions** — Hark's "different (equivalent) lattice basis" does
  NOT reproduce in my environment (NumPy 2.4.6 vs Hark's 2.5.4; the
  greedy rank scan may be version-sensitive). No number changes either
  way. The provenance gap itself is CONFIRMED: the fresh output does
  NOT contain `n_distinct_positions` or `max_multiplicity` (the script
  contains neither string outside `json.dump`), while the shipped JSON
  carries both per direction — the shipped JSON came from a different
  script revision. Minor.
- **WS-A task 5 / WS-C A5 `lock` discrepancy (0.304 / 0.455 vs shipped
  1.000) — NOT RE-RUN, but the mechanism is confirmed by code reading
  (F2).** I did not re-run the 14-run task 5 (~10 min) or the WS-C
  quench ladder. The audit attributes the difference to platform
  dependence in the ill-defined metric; the code reading (F2) shows
  exactly why the metric is platform-dependent, so the explanation is
  accepted. My transverse runs printed lock = 1.000 for full24 final
  states (all modes active $\to$ the metric is well-defined there), which
  is consistent.
- **All other §1 rows (WS-A tasks 1–4, WS-C 1a–2d, WS-E compute/figs) —
  NOT RE-RUN by me.** Hark's "identical" verdicts stand on Hark's logs,
  which are not in my workspace. I record them as reported, not
  independently confirmed.

## F1. "hex6 and fcc12 are stable attractors" / "both patterns are local minima at both $\bar{\psi}$" — FAILED as written (VERIFIED by my own run)

**What the package claims.** WS-A task5_report.md CLAIM + §2: "the 6-mode
hexagonal and 12-mode FCC sub-patterns are stable attractors in their own
right (a hex6 start stays hex6, an fcc12 start stays fcc12, both fully
converged by step 3000)" and "This is the mechanism behind the
manuscript's annealed 6-mode outcome, now shown for Model B." Grade B.
WS-C task1 report finding 6: "The 24-mode is a local minimum outside the
band; the 6-mode is the global minimum there" $(A3 \bar{\psi}=0, A4 \bar{\psi}=+0.10$:
seeded 24-mode PERSISTS). Finding 7: "Both patterns are local minima at
both $\bar{\psi}$" $(A5 \bar{\psi}=-0.18, A6 \bar{\psi}=0$: seeded 6-mode persists). The task-5
report's own §5/§6 already flag run-length and box-size caveats, and §6
states the claim would become "long-lived metastable" if a hex6/fcc12
start grew into full24 — which is what has now happened.

**Hark's argument (sound).** The sub-patterns were seeded with the other
D4 modes exactly zero (`seed_subset`, d4model.py lines 302–309: `ph =
np.zeros(...)`, only the listed modes set). That start sits in a subspace
the dynamics preserves — persistence there says nothing about stability
to the absent modes. Stability requires transverse stability, which the
package never tested. Hark tested it: hex$6 + \varepsilon\cdotA$\* in the 18 absent modes
$\to$ full24, 5/5 at $\bar{\psi}=-0.18$; fcc12 + same $\to$ full24, 4/4; at $\bar{\psi}=0$,
24-mode + 2% amplitude / 0.2 rad phase noise $\to 6$-mode; at $\bar{\psi}=+0.10 \to$
2-mode stripe-like.

**My independent check.** I wrote my own transverse test
(`hark_audit_check/transverse_subpattern_check.py`, package's own
`d4model.ModelB` fixed stepper, $L=\pi$, N=16, $q0^{2}=8.0$, $r=-0.35$, $\bar{\psi}=-0.18$,
dt=0.005, 6000 steps; $\varepsilon\cdotA$\* with random conjugate phases in the absent
modes). Results (log: `hark_audit_check/transverse_subpattern_check.log`):

| run | result |
|---|---|
| hex$6 \varepsilon=0.002$, 0.01, 0.03 (seed 0); $\varepsilon=0.002 ($seeds 1, 2) | **$5/5 \to$ full24** (ndom=24, D4=0.999981, Fexc=$-0.007728$, rms=0.381, amp=0.077682) |
| fcc$12 \varepsilon=0.002$, 0.01, 0.03 (seed 0); $\varepsilon=0.002 ($seed 1) | **$4/4 \to$ full24** (Fexc $-0.007728$; one run $-0.007727$, amp 0.077680) |
| hex$6 \varepsilon=0$ control | stays hex6 (ndom=6, Fexc=$-0.002290$, rms=0.395) — reproduces the package run exactly |

The control reproducing the package run is the signature of the
invariant-subspace artefact: with absent modes exactly zero, hex6
persists; with a 0.2% transverse perturbation, it goes to full24. At
$\bar{\psi}=-0.18$ the 24-mode state is the only attractor seen from any perturbed
start; hex6/fcc12 are saddles. **F1 is VERIFIED.** Corrected statement
(I1, C-capped): at $\bar{\psi}=-0.18$ the 24-mode attracts perturbed hex6 and fcc12
starts; at $\bar{\psi}=0$ hex6 is stable and the 24-mode is not (Hark'$s \bar{\psi}=0$ result,
not re-run by me); the "24-mode is metastable outside the band" reading
(WS-C finding 6) is an invariant-subspace artefact; WS-A's sentence
"this is the mechanism behind the manuscript's annealed 6-mode outcome,
now shown for Model B" is withdrawn — under Model B at $\bar{\psi}=-0.18$ hex6 is
not a trap. (The damped-wave 6-mode quench outcomes in WS-C are
unaffected: those start from noise in all modes, and that dynamics drifts
$\bar{\psi} \to +0.0025$, where hex6 is the lower state — consistent with F1.)

**What I did not re-run.** Hark'$s \bar{\psi}=0$ and $\bar{\psi}=+0.10$ transverse runs, and
the stripe side-result (one run: one-mode stripes Fexc $\approx -0.0451$ vs hex6
$-0.0539$ at $\bar{\psi}=+0.10$; metastable alternative, not the global minimum).
The $\bar{\psi}=0$/​+0.10 results are consistent with the WS-C numbers they quote
(A6 6-mode Fexc $-0.041306$ at $\bar{\psi}=0$ matches the task-1 report exactly), but
I record them as reported, not independently confirmed. The stripe
result is a single run and I mark it UNVERIFIED. The WS-C one-mode
competitor set {24-mode, 6-mode, disordered} omitting stripes is a real
gap in the band analysis either way; the audit's claim that stripes are
metastable rather than global-minimum rests on that one run.

**Consequences for the package.** WS-A task 5's "hex6/fcc12 stable
attractor" claims (grade B) and WS-C findings 6–7 ("local minima at both
$\bar{\psi}$") are FAILED as written. The full-pattern recovery claims $(\delta\phi \leq 1.0$
rad, $\pm20$% amplitude) are untouched by F1 — those starts have all 24
modes present. The guide is corrected accordingly (§4.5, §5.1, §8) and
the WS-A grades fall to C on the independence bound (F5).

## F2. Triad `lock` metric ill-defined for partial patterns — VERIFIED

`d4model.analyze` (lines 273–282) builds the triad list over all 24
roots and computes `lock = mean(cos(pha[a]+pha[b]+pha[c]))` over all 32
triads, with no amplitude filter. For a partial pattern the absent modes
sit at roundoff amplitude with noise phases, so their triads contribute
noise to the mean — the metric is platform-dependent for partial
patterns, which is exactly what Hark's rerun shows (hex6 0.304 vs
shipped 1.000; WS-C A5 0.455 vs 1.000). Hark's fix (restrict to triads
with all three modes active; `active_lock` gives 1.000 for hex6/fcc12/
full) is correct. **Severity: minor.** No load-bearing conclusion rests
on the sub-pattern lock value except the WS-A task-5 §2 phrase "locked
triads" ("they persist unchanged for 6000 steps with locked triads and
stationary free energy") — the persistence claim itself rests on
stationarity (Fexc/rms identical at steps 3000/6000), not on lock. The
guide now notes the metric defect and the fix; the workstream code is
left as-is pending Brandon's call on script fixes (see §"Actions").

## F3. WS-E task 11 "flint arb confirms band edges to 1e-12" — vacuous as run (VERIFIED)

`bifurcation_flint_check.py` computes the coexistence edges via
`fmpq_poly.roots()` (line: `roots = poly.roots()`). `fmpq_poly.roots()`
returns rational roots only; the edges are irrational, so the script
prints `coexistence band edges (flint): []`. **My own run confirms it:**
the output contains exactly `coexistence band edges (flint): []` (flint
0.8.0; Hark reports the same in 0.9.0). The task-11 report's C4 row
("SymPy + flint arb, exit 0", "exact, two tools") therefore had only
one tool behind the band edges until this audit. The values themselves
stand: Hark re-did the edges with arb
$([-0.238164846446380 \pm 3.4e-16], [0.90483151311305 \pm 4.1e-15])$, and I
confirmed them independently with a SymPy solve of the same quadratic
(coeffs ascending: $c0=-11443/25380, c1=-590/423, c2=295/141)$ giving
$[-0.238164846446379897, 0.904831513113046563]$, agreeing with Hark's arb
values to <1e-12. (My first solve used the coefficients in descending
order and gave wrong roots [1.105..., $-4.199...]$; the corrected solve
above is the one that counts.) C4's basis is therefore SymPy + arb, F2
— but the arb leg is Hark's (and my SymPy solve is a third route, same
tool family as the first). The record correction is: C4's "two tools"
basis was one tool until the audit. The guide is corrected (§6.1, §8).
Note also, for the record, that the same script prints
`F(A_max) = [3.858520750506e-5 ± 6.50e-18] contains 0.0000386: False` —
that is a rounding artefact (0.0000386 = 3.86e-05 is outside the tight
arb interval around the exact 3.858520750506e-05), not an error; the
report's value 3.858520750506e-05 is the exact one.

## F4. WS-C task 13 Richardson result not regenerable from the shipped script — VERIFIED

`task2d_transient.py` runs T=5 only (`steps = int(5 / dt)`) and writes
the CSV with mode `'w'` (overwrite). The shipped CSV contains 12 rows:
4 at T=5, 4 at T=0.5, 4 at T=1.0 — and the T=0.5/1.0 rows carry
`seconds=0`, a tell that they were not produced by this script (which
records real wall times: 5.5–41.7 s). `make_figures.py` line 85 filters
`r["T"] == "0.5"` and line 88 indexes `err[-1]`; with only T=5 rows the
filter is empty and it crashes. **My own re-run in a scratch copy
confirms the whole chain:** task2d rc=0, T=5 rows reproduce the shipped
T=5 rows exactly, CSV overwritten to 4 rows, make_figures crashes with
`IndexError: index -1 is out of bounds for axis 0 with size 0` at line
88. The numbers stand: the shipped T=0.5 rows $(\langleA\rangle = 0.07803, 0.078126$,
0.078177, 0.078203) match Hark's regenerated values exactly, and the
successive differences (9.578e-5, 5.105e-5, \$2.625$e-5 \to p = 0.908, 0.960)$\$
support the $p \approx 0.95$ claim. This is a provenance gap, not a numerical
error — but it breaks guide §9 as written (run task2d, then
make_figures crashes). The guide is corrected (§5.2, §9, §8): the
T=0.5/1.0 rows depend on an unshipped run, and the clean-run order must
not promise that make_figures succeeds after a task2d re-run.

## F5 / §6. Grade inflation in WS-A; the regrade — VERIFIED, amendment applied

Hark's original F5 invoked the HLRE §6.5 human-gate fallback (every
claim capped C / F3 until a human gate runs). The amendment repeals the
human-gate requirement for this assessment, so F5 as originally written
is superseded — but its Track E conclusion survives on independent
grounds: **all verification in the package is artificial (I1), and the
independence bound caps every Track E claim at C.** WS-A grades claims A
and B (M6 mean 15: A; global min 12 / max 18: A/B; band fractions B;
basin map B; task-5 sub-pattern claims B). WS-C and WS-E apply the C cap
correctly. The audit is right: WS-A's A/B grades are inflated, and they
fall to C regardless of the human-gate question.

The §6 regrade table (amendment applied) is accepted entry by entry:

| claim | old | new | my check |
|---|---|---|---|
| All Track E empirical/simulation claims | C | **C** | $I1 \to C$; unchanged |
| WS-A M6 mean 15, min 12, max 18 | $A/B \to F3$ | **F2** | two routes in the package itself, verified by reading task2_report.md: exact symbolic (Lagrange + AM-GM) + independent numerical optimisation (scipy, 200 random starts: max 18.000000000000014, min 11.99999999999999) |
| WS-A \|Aut(D4)\| = $1152 \to$ no icosahedral projection | $B \to F3$ | **F3** | one enumeration route (Gram enumeration); "matches the known order of W(F4)" is a cross-check, not a re-derivation — F3 stands |
| WS-E Landau values, thresholds, barrier (C1–C3, C6) | C / F2 | **F2** | SymPy exact + python-flint, both run (I re-ran the flint check, rc=0) |
| WS-E band edges at $r=-0.35 (C4)$ | C / F2 claimed | **F2** | SymPy + Hark arb (package flint leg was vacuous, F3); my SymPy solve confirms the values to <1e-12 |
| WS-$C C1.4 (a_{0}$, CFL), C2.5 CFL leg | F3 | **F2** | exact_checks uses SymPy + flint + Z3, 31 PASS (I re-ran it) |
| WS-C C2.1 analytic A\*, F/V | F3 | **F2** | two tools (exact_checks + WS-E bifurcation checks) |
| WS-C C1.2, C2.2, P4; F1 hex6/fcc12 "stable attractor" | FAILED as written | **FAILED as written** | unaffected by the regrade; F1 adds the WS-A task-5 / WS-C finding 6–7 failures |

Still required by HLRE §7 for any deposit: a disclosure that all
verification is artificial (I1), with the independence level of every
pipeline stated. That disclosure was already in the guide §1; it stands.

## F6. Programme brief's "established facts" vs the round-1 review — SUBSTANTIATED, with nuance

The brief (PROGRAMME_BRIEF.md lines 55–58) lists under "Established IRH
facts (do not re-litigate; cite the qualification every time)": "D4
selected, $S = \tau^{2}/q4 = 64/141 \approx 0.454 (17.3$% margin over A4*)" and "E6
via 2T/McKay. SO(8) EXCLUDED. Three generations INPUT, not derived."
The round-1 review is the 2026-10-30 deepest-research report
(`D4-interference-deepest-research.md`, §5 claim record), corroborated by
the 2026-11-02 v5 test report:

- **C8** "IRH: gauge algebra is E6 via 2T/McKay; SO(8) excluded" —
  **D as a physical claim** (mathematics A, physical reading IRH's
  postulate; novelty budget). The v5 test report repeats: "any physical
  reading of D4/E6 beyond the manuscript's own premises (graded D in
  the 2026-10-30 deepest-research report...)".
- **C6** "IRH: $S_{D}4 = 64/141$ wins over A4\* by 17.3%" — **D as presented
  here** (IRH computation, I0/I1; needs independent re-derivation for C,
  frozen I2 test for B). Hark's gloss "a retrodiction within a
  restricted, box-limited competitor set" is Hark's characterisation,
  not a verbatim quote — the report does not contain the words
  "retrodiction" or "box-limited" — but the grade D itself is verbatim,
  and the dependency ledger (C6–C8 "depend on IRH v93.1's definitions...
  none re-derived here") supports the substance.

So the brief's label "Established IRH facts (do not re-litigate)"
overstates the review grades for these two items: the review grades them
D as physical claims / as presented, and the package correctly says it
"does not change" them — but presenting them as settled in the brief's
framing is the error Hark identifies. **Nuance:** the brief itself says
"cite the qualification every time", which mitigates the framing — the
qualification $(q_{0}$ tuned onto the shell; the D grades) was in fact cited
throughout the package. F6 is substantiated as a framing correction, not
as a finding that the package mis-graded anything. The review's grades
govern for this project, as Hark states.

## §3 / §4. What the package settles / does not settle

**§3 (settled) — accepted, except one provenance item.** The settled list
is a fair restatement of the package plus F1's correction. One item I
could not verify: "the round-1 review had $\approx [-0.235, -0.14]$ with
stripes/A2/A3 included." I searched the 2026-10-30 deepest-research
report, the v5 test report, the repo CORE.md, the task-14 report, and
the manuscript text — no $[-0.235, -0.14]$ band and no "stripe" competitor
set appears in any of them (the manuscript's band is "$-0.33$ ≲ $\bar{\psi}$ ≲ 0.03
depending on quench depth", line 528; the manuscript contains no
"stripe"). The $-0.235$ lower edge coincides with WS-C's measured edge,
which makes the attribution suspicious. **UNVERIFIED — source not
located in the workspace.** It may come from a review document Hark
holds that I do not have; from my side it cannot be cited. The rest of
§3 stands: 11.85% bracketed not reproduced; band $\bar{\psi} \in (-0.235, -0.125)$
under the one-mode ansatz with competitors {6-mode, disordered};
spinodal $\bar{\psi} = -0.1439$; detuning windows; $\kappa = 192$; thick-walled droplet;
resolution-independent fixed point; $\bar{\psi}$ drift ~1e-15; Model B fixed point
recovers from 1 rad / $\pm20$% noise; noise quenches never produce 24-mode;
anti-Hermitian instability + fix; WS-E ABSTAIN correct; Klein 2001
caveat; selection-principle change.

**§4 (not settled) — substance verified, citations unlocated.**

- **B1 (equation of motion).** Substantiated on the manuscript text
  itself. Manuscript §I.2 (lines 185–191) states the dynamical equation
  as $\partial^{2}_{t}\psi + \gamma\partial_{t}\psi = **-\deltaF/\delta\psi$** — a damped wave equation with a
  NON-conserved right-hand side — and §I.3 (lines 215–219) then derives
  that conserved dynamics is a requirement, citing Model B
  $\partial_{t}\psi = \nabla^{2}(\deltaF/\delta\psi)$ preserving the mean to 8.3e-17. The manuscript's own
  §I.2 is therefore internally inconsistent: its stated equation is not
  the conserved dynamics its simulations use. The package uses Model B
  (first-order conserved), inherited from the repo verification code
  (sim6/sim7) — "fine as a limit" of the conserved-MPFC form
  $\partial^{2}_{t}\psi + \gamma\partial_{t}\psi = \nabla^{2}\deltaF/\delta\psi$, which appears in NEITHER the manuscript nor
  the package. Hark's citation "REVISION_PLAN 1.1" is **unlocated**: no
  REVISION_PLAN document exists anywhere in the workspace (full-tree
  grep for REVISION_PLAN/UNDERDETERMINED found only the skill prompt
  files and a WS-D table entry using UNDERDETERMINED as a grade word).
  The B1 substance stands on the manuscript text; the citation does not.
- **R4 (fair test).** Substantiated as a statement about the package:
  every simulation box is $L=\pi$ hypercubic; no A4\* (or 600-cell / 2O)
  control was simulated; no preregistered competitor set, no $\geq10$ seeds,
  no commensurate cells. "Step 1.2 remains needed" cites the same
  unlocated REVISION_PLAN — the need itself is real, the citation is
  not verifiable.
- **Common-tangent diagram.** Substantiated: the package does fixed-$\bar{\psi}$
  minimisation everywhere (WS-A task 3, WS-C task 7); no
  coexistence-aware common-tangent construction was done.
- **B2, B3 (E6 mechanism, overclaims, Lean coverage).** True: untouched
  by design; the programme scope excludes them.

**§5 (optional human checks).** Noted: lake build + #print axioms,
source re-reads, balance gate. Klein 2001 and WS-E's citation
corrections were not opened by Hark — I record that limitation; it does
not affect the findings above, which rest on code and numbers, not on
those citations.

## Corrections applied to the guide (SUMMARY_AND_REPLICATION_GUIDE.md)

The audit proved errors and gaps in my delivered guide. Corrected in
place, and the zip rebuilt and re-verified (see below):

1. "29 checks" $\to$ "29 check statements, 31 [PASS] lines (the $r_{eff}$ table
   loops over 3 rows)" (§5 intro, §5.2, §9).
2. WS-A task 5: hex6/fcc12 "stable attractors" $\to$ FAILED as written (F1);
   corrected statement (24-mode is the only attractor seen from
   perturbed starts at $\bar{\psi}=-0.18$; hex6/fcc12 are saddles); WS-A §2
   mechanism sentence withdrawn; grades $B \to C$.
3. WS-C findings 6–7: "local minima at both $\bar{\psi}$" $\to$ FAILED as written
   (F1); corrected statement; grades unchanged (C).
4. WS-E C4: "two tools" basis $\to$ one tool until the audit (flint leg
   vacuous); values confirmed by Hark arb + my SymPy solve; grade F2.
5. WS-C replication: task\$2$d \to$\$ make_figures crashes (F4); T=0.5/1.0 rows
   depend on an unshipped run; guide §9 order corrected.
6. Lock metric: ill-defined for partial patterns (F2); fix noted (active
   triads only).
7. WS-A task 1 JSON: provenance gap noted (shipped JSON carries fields
   the shipped script does not write).
8. §8 register: F1 FAILED items, F3 record correction, F4 provenance
   gap added.
9. §1 grades: WS-$A A/B \to C ($independence bound); §6 regrade table
   applied.

## What this review did NOT verify (stated plainly)

- Hark's full §1 replication table rows I did not re-run (WS-A tasks
  1–4, WS-C 1a–2d, WS-E compute/figs, task-5 lock values).
- Hark'$s \bar{\psi}=0$ and $\bar{\psi}=+0.10$ transverse runs; the stripe side-result (one
  run).
- Hark's arb band-edge computation (I confirmed the values by an
  independent SymPy solve, not by re-running arb).
- The "round-1 review $[-0.235, -0.14]$ band" and the REVISION_PLAN /
  B1/R4/R6/Step 1.2 citations (sources not located in the workspace).
- Klein 2001 and WS-E's citation corrections (not opened by Hark or by
  me).

## Actions taken / offered

- **Done in this turn:** this review; guide corrections 1–9 above; zip
  rebuilt from the corrected guide and re-verified (new sha256 in the
  delivery message); transcript + dated log appended.
- **Offered, not done (Brandon's call):** fix the workstream scripts
  themselves — (a) WS-C `make_figures.py` / `task2d_transient.py`
  (ship the T=0.5/1.0 rows or regenerate them in-script); (b)
  `d4model.analyze` lock over active triads only; (c) WS-A task-1 JSON
  provenance (re-ship from the current script or record the revision).
  Fixing them changes the workstreams' artifacts, so I have not touched
  them.
- **Separately (not part of this audit):** WS-D's deliverables appear to
  be on disk (task8, task9, task10, task12 reports + ws-d_summary.md,
  written 2026-11-10 17:05–17:20 CST). I have not verified or delivered
  them yet — that is the next item unless you say otherwise.
