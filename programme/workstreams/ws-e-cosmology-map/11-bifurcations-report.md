# Workstream E, Task 1 — Simulate cosmological bifurcations

**Date:** 2026-11-10. **Workstream:** ws-e-cosmology-map (tasks 11, 14, 15).
**Skills:** /truth-seeking-frontier v5, /cross-domain-discovery v2.0.0, /hlre-v5-1.
Mode for the literature-dependent parts of this workstream: deepest-research full mode
(stated plainly; not systematic review — no systematic-review form was chosen).
The skills themselves are DESIGN CLAIMS, ungraded; skill use is not evidence of reliability.

## CLAIM + STATUS

**CLAIM (as tasked):** "Simulate how cosmic expansion drives parameter changes and
bifurcation cascades, comparing scenarios and searching for conditions that produce its
predicted phase transitions."

**STATUS: SPLIT — the bifurcation part is VERIFIED by two independent tools; the
cosmic-expansion part is ABSTAIN.**

- The stated Landau functional's bifurcation structure (ordered branch, spinodal,
  coexistence, first-order character, detuning thresholds, homogeneous barrier) is
  recomputed exactly and agrees with every checkable number in the manuscript.
- **The manuscript states no coupling between cosmic expansion and any model
  parameter.** There is no scale factor, no Hubble parameter, no Friedmann equation,
  no expansion-driven parameter law anywhere in the text (grep-verified over the full
  1,638-line source rebuild). Any "expansion drives $\bar{\psi} / r / q_{0}$" claim is therefore
  **ABSTAIN — I cannot verify this with the available tools**, because the manuscript
  does not state it and inventing a cosmology is forbidden by the programme brief.
- The scenario trajectories in Fig. 4 are HYPOTHETICAL paths through the stated
  parameter space. They show which crossings would occur IF a driver moved the
  parameters along those paths. They are not manuscript predictions.

## 1. What the manuscript actually states (extraction)

Source: `IRH_v93_1_source_rebuilt.txt` (34 pp., sha256
`cebc3b6f010ed9c059129b4b0ff2c9e3a8ea858e74adc68c3e7fd7d9f34affa8`).
Greps run: `expansion|hubble|cosmolog|gravitational wave|CMB|microwave|redshift|
scale factor|inflation|monopole|bifurcat|nucleat|early universe|phase transition|
quench|dilut` and `cosmic|universe|inflation|dilution|gravitational|tensor mode|
power spectrum|scale factor|a(t)|friedmann|de sitter|reheat|big bang|kibble|
domain wall|stochastic background`. Results:

- **No expansion mechanism.** The only "cosmological" statements in the manuscript are:
  (a) §V.3: the monopole problem "requires the standard resolution: inflationary
  dilution, or a breaking pattern avoiding the relevant topology" — named, not derived,
  no inflation model, no e-fold number, no reheating; (b) §IX.$5: \bar{\psi}$ is "an initial datum
  rather than a tuned coupling, which reclassifies the fine-tuning objection as a
  cosmological initial-condition question"; (c) §II.9: "Any cosmological account within
  this framework must supply a nucleation mechanism" — and none is supplied.
- **The stated control parameters** (§II.3, §II.7): quench depth r, baseline tension $\bar{\psi}$
  ("the control parameter of the selection mechanism"), resonant scale $q_{0}$, sixth-order
  coupling $w_{6}$, nonlinear couplings u, v.
- **The stated functional** (§II.3): F(B) = $(r/2)B^{2} - (u\tau/3)B^{3} + ($vq${}_{4}/4)B^{4}$,
  $B = A\sqrt{N}$, $\tau \equiv T/N^{3/2}$, $q_{4} \equiv Q/N^{2}$. With $\bar{\psi} ($§II.7):
  F(A) = $(N/2)\cdotr_{eff}\cdotA^{2} - (T/3)\cdotu_{eff}\cdotA^{3} + ($vQ/$4)\cdotA^{4}$,
  $r_{eff} = r - 2u\bar{\psi} + 3v\bar{\psi}^{2}$, $u_{eff} = u - 3v\bar{\psi}$.
  Detuning penalty (§II.$7): r_{shell} = r + (q_{0}^{2} - 8)^{2}$.
  Stated values: N = 24, T = 192, Q = 3384, u = v = 1, fiducial $r = -0.35$, $\bar{\psi} = -0.18$.
- **The stated transition** (§II.9): first order; $r_{eff} = +0.107$ at $\bar{\psi} = -0.18$, so the
  disordered state is linearly stable and the $D_{4}$ state "must be nucleated across a
  barrier, not grown from fluctuations". At $\bar{\psi} = -0.10$, $r_{eff} = -0.120 ($linearly
  unstable); at $\bar{\psi} = 0, r_{eff} = -0.350$.
- **The stated band** (§II.7): the full 24-mode pattern is the global minimum in a
  band "occupying 11.85% of the scanned plane, approximately $-0.33$ ≲ $\bar{\psi}$ ≲ 0.03
  depending on quench depth", **conditional on $q_{0}$ tuned onto the $D_{4}$ shell**. The band
  was determined against sub-patterns within the shell (6-mode hexagonal etc.), not
  only against the disordered state: "At zero baseline field a 6-mode hexagonal
  sub-pattern has lower free energy than the full 24-mode pattern at every quench
  depth tested."
- **Known inconsistency (not mine to resolve):** the band is stated as both 11.85%
  (headline PREDICTION, §II.7) and 11.90% $(w_{6} = 0$ value, §II.7 sixth-order paragraph;
  Appendix A item 8 calls 11.9% "the correct" value). The source rebuild notes flag
  this as genuine. Brandon's call, unresolved.

## 2. Derivation (each step checkable)

All steps recomputed from the stated functional. Tool 1: SymPy 1.14.0 (exact
rational/symbolic), script `data/bifurcation_compute.py`, exit 0. Tool 2 (independent):
python-flint 0.8.0 (exact fmpq + rigorous arb balls), script
`data/bifurcation_flint_check.py`, exit 0. Tool 3 (figures only): numpy 2.4.6 +
matplotlib 3.11.2, script `data/make_figures.py`, exit 0. Python 3.11.16 (conda env
`jacobian-conjecture-2d`).

**Step 1 — Selection constants.** $\tau = 192/24^{3/2} = 4/\sqrt{6}$; $q_{4} = 3384/576 = 47/8$;
$S = \tau^{2}/q_{4} = 64/141 \approx 0.4539$. (SymPy exact; agrees with the manuscript's stated
64/141.)

**Step 2 — Stationary points.** $F'(A) = A\cdot(N\cdotr_{eff} - T\cdotu_{eff}\cdotA$ + vQ$\cdotA^{2})$. Nonzero
roots exist iff the discriminant $\Delta = T^{2}u_{eff}^{2} - 4$NvQ$\cdotr_{eff} \geq 0$, i.e. $r_{eff} \leq r_{spin}$
with $r_{spin}$,eff = $T^{2}u_{eff}^{2}/(4$NvQ). At the fiducial point the roots are
A = 0, 0.00980059, 0.07757530.

**Step 3 — Fiducial point.** A* = 0.07757530 (manuscript 0.0775753), F(A*) =
$-0.00763227 ($manuscript $-0.0076323)$. Agreement to the manuscript's quoted precision.
Flint arb balls: $A* = [0.077575296339281 \pm 3.33e-16]$,
F$(A*) = [-0.007632267318990 \pm 6.24e-16]$.

**Step 4 — Homogeneous barrier (new derived number, not in the manuscript).**
The local maximum sits at $A_{max} = 0.00980059$ with $F(A_{max}) = 3.8585\times10^{-5} ($same
F/V units as the manuscript). This is the homogeneous nucleation barrier of the
one-mode functional at the fiducial point. The inhomogeneous critical droplet
(thin-wall, gradient terms) is ws-a's task (IX.1), not this one.

**Step 5 — Spinodal and coexistence.** $r_{c}$,eff$(\bar{\psi}) = 2u_{eff}^{2}\tau^{2}/(9$vq${}_{4})$ =
$128\cdotu_{eff}^{2}/1269$; $r_{spin}$,eff$(\bar{\psi}) = (16/141)\cdotu_{eff}^{2}$. At $\bar{\psi} = -0.18$:
$r_{c}$,eff = 0.239216, $r_{spin}$,eff = 0.269118, $r_{eff} = 0.1072$. Ordering
$0 < r_{eff} < r_{c} < r_{spin}$ confirms the first-order character: ordered branch is the
global minimum while the disordered state is linearly stable.

**Step 6 — Band edges, $D_{4}$-vs-disordered only.** At fixed $r = -0.35$, solving
$r_{eff}(\bar{\psi}) = r_{c}$,eff$(\bar{\psi})$ gives $\bar{\psi} \in [-0.23816, +0.90483] ($SymPy exact radicals;
flint arb confirms to 1e-12). Solving $r_{eff} = r_{spin}$ gives $[-0.25432$, +0.92099].
**These are NOT the manuscript's band edges $(-0.33, +0.03)$.** The manuscript's band
is the region where $D_{4}$ beats the sub-patterns; the $D_{4}$-vs-disordered region is wider.
This is a scope distinction, not a contradiction: the sub-pattern free energies are
not stated in the text, so the sub-pattern competition cannot be re-derived from the
text. See §5.

**Step 7 — Detuning thresholds (refines the manuscript's table).** The manuscript's
table gives only $q_{0}^{2} = 7.5 ($no branch) and 8.0 (branch exists). From the stated
penalty: the ordered branch exists for $q_{0}^{2} \in (7.5976, 8.4024)$ and is the global
minimum for $q_{0}^{2} \in (7.6367, 8.3633)$ at (r, $\bar{\psi}) = (-0.35, -0.18)$. Both endpoints are
consistent with the manuscript's table (7.5 outside, 8.0 inside).

**Step 8 — Barrier vs $\bar{\psi}$.** At $r = -0.35$ the barrier rises steeply as $\bar{\psi}$ decreases
from the linear-instability edge and vanishes exactly at $r_{eff} = 0$, i.e.
$\bar{\psi} = (2 - \sqrt{8.2})/6 \approx -0.1439$. Full table in `data/bifurcation_table.json` (9 rows).
Note: the repo brief `problems/IX1-tractable-computation.md` says the barrier
should vanish "near the linearly-unstable edge $(\bar{\psi} \approx -0.10)$". That is loose: the
exact edge is $\bar{\psi} \approx -0.144$; at $\bar{\psi} = -0.10$ the state is already linearly unstable
$(r_{eff} = -0.120$, manuscript's own table). Minor correction to a repo working
document, not to the manuscript.

**Step 9 — The $w_{6}$ narrowing is NOT re-derivable.** The manuscript states H = 911,040
for the $D_{4}$ shell and that $w_{6}$ narrows the band 11.90% $\to 8.47$% at $w_{6} = 0.2$, but the
functional form of the $w_{6}$ term is not stated in the text. Without it, neither the
8.47% nor the joint (detuning $\times w_{6})$ map (repo problem IX.1.3, explicitly open) can
be recomputed. NOT RUN.

**Step 10 — Expansion coupling.** None stated; see §1. No computation was attempted
for it. ABSTAIN.

## 3. Checks run

| # | Check | Tool | Result |
|---|-------|------|--------|
| 1 | S = 64/141, $\tau = 4/\sqrt{6}$, $q_{4} = 47/8$ | SymPy 1.14.0, exit 0 | PASS |
| 2 | A* = 0.0775753, $F(A*) = -0.0076323$ at fiducial point | SymPy + flint arb, exit 0 | PASS (to quoted precision) |
| 3 | $r_{eff} = +0.107$, $u_{eff} = 1.54$ at $\bar{\psi} = -0.18$ | SymPy + flint fmpq, exit 0 | PASS |
| 4 | $r_{c}$,eff = 0.239216, $r_{spin}$,eff = 0.269118 | SymPy + flint fmpq, exit 0 | PASS (agree to 1e-12) |
| 5 | Detuning table: $q_{0}^{2}=7.5$ no branch, 8.0 branch + global min | SymPy + flint, exit 0 | PASS; thresholds refined to 7.5976 / 7.6367 |
| 6 | §II.8 ansatz gap 1.25% (0.0000953/0.0077276) | SymPy exact, exit 0 | PASS (1.233%) |
| 7 | Coexistence band edges at $r=-0.35$: $[-0.23816, +0.90483]$ | SymPy + flint arb, exit 0 | PASS — and $\neq$ manuscript band, by scope (see §5) |
| 8 | Barrier vanishes at $r_{eff} = 0 (\bar{\psi} \approx -0.1439)$ | numpy evaluation of verified formulas | PASS |
| 9 | 11.85% band fraction reproduced from text | — | NOT RUN (scan definition + sub-pattern data absent) |
| 10 | $w_{6}$ narrowing 11.90% $\to 8.47$% reproduced | — | NOT RUN $(w_{6}$ term form unstated) |
| 11 | Expansion $\to$ parameter coupling extracted | grep over full text | FAIL (no such statement exists$) \to$ ABSTAIN |
| 12 | H = 911,040 sixth-order count recomputed | — | NOT RUN (ws-a owns sixth-order; count stated, not re-derived) |

Two tool defects found and fixed during the run (recorded, not silently corrected):
(a) the first flint script used `float(fmpq)`, unsupported in python-flint 0.8.0 —
rewritten with an `arb` conversion helper; (b) the first figure/table logic treated
the linearly-unstable region $(r_{eff} < 0$, one positive root, zero barrier) as "no
branch" — corrected to a `branch()` helper; the corrected table confirms the barrier
vanishes at $\bar{\psi} \approx -0.144$ as the IX1 brief anticipated.

## 4. Figures and tables

- `figures/fig1_free_energy_curves.png` — F(A) at $r = -0.35$ for $\bar{\psi} = -0.30$, $-0.18$,
  $-0.10$, 0, +0.03. First-order character visible: at $\bar{\psi} = -0.18$ the ordered minimum
  sits below zero behind a barrier; at $\bar{\psi} = -0.30$ no ordered branch exists.
- `figures/fig2_phase_diagram.png` — $(\bar{\psi}, r)$ plane: coexistence, spinodal, and
  $r_{eff} = 0$ curves; $D_{4}$-global-min / metastable / no-branch regions; fiducial point;
  manuscript band edges shown as dotted lines with the explicit note that they are
  sub-pattern-competition edges, not these curves.
- `figures/fig3_barrier_vs_psibar.png` — homogeneous barrier $F(A_{max})$ and A*,
  F(A*) vs $\bar{\psi}$ at $r = -0.35$. Barrier vanishes at $\bar{\psi} \approx -0.144$.
- `figures/fig4_hypothetical_scenarios.png` — three HYPOTHETICAL trajectories:
  $(i) \bar{\psi}$ swept down at fixed r (unstable $\to$ metastable-first-order $\to$ coexistence at
  $-0.238 \to$ spinodal at $-0.254 \to$ no branch); (ii$) q_{0}^{2}$ drifted $7.5 \to 8.0$ at fixed
  (r, $\bar{\psi}) ($branch appears at 7.598, becomes global min at 7.637); (iii) r quenched
  at fixed $\bar{\psi} = -0.18 ($spinodal at $r = -0.188$, coexistence at $r = -0.218$, linear
  instability at $r = -0.457)$. No driver is stated for any of them.
- `data/bifurcation_values.json`, `data/bifurcation_table.json` — all numbers.
- Scripts: `data/bifurcation_compute.py`, `data/bifurcation_flint_check.py`,
  `data/make_figures.py`.

## 5. Rival / failure mode

- **Leading rival (outside this task's scope):** the one-mode Landau functional
  itself could misrepresent the full field (harmonic content lowers F by 1.25% at the
  fiducial point, §II.8). The bifurcation locations computed here inherit that
  approximation. A full-field computation could shift the spinodal/coexistence curves
  by ~1%.
- **The live failure mode inside this task** was misreading the manuscript's band
  edges as coexistence edges. It was caught by computing the coexistence edges
  explicitly and finding they differ $([-0.238, +0.905]$ vs $[-0.33, +0.03])$. The
  resolution is scope: the manuscript's band is set by sub-pattern competition,
  whose data are not in the text. Forcing agreement would have been fabrication.
- **Second failure mode:** inventing an expansion law (e.g. $\bar{\psi} \propto a(t)^{-n})$ to make the
  task "complete". Refused. The scenario figure is labelled HYPOTHETICAL throughout.

## 6. Evidence that would change the answer

- A stated expansion$\to$parameter coupling in the manuscript or a follow-up text
  (none exists in v93.1) would convert the ABSTAIN on the expansion part into a
  computable claim.
- The band-scan code with the sub-pattern free energies would let the 11.85% and
  the $(-0.33, +0.03)$ edges be re-derived rather than taken as stated. (Searched:
  no scan code in `verification/`; the scan is referenced only in the text.)
- A stated $w_{6}$ term form would let the 8.47% narrowing and the joint
  (detuning $\times w_{6})$ map be computed.
- A full-field (beyond one-mode) bifurcation computation would shift the curves by
  ~1% and is the natural next check; it is a heavier simulation and is costed in §8,
  not run here.

## 7. HLRE grades (per narrow claim; worst-of shown)

Tier: Standard (others will cite it). Track: E unless noted. Independence: I1
throughout (re-derivation of stated values with two independent tools; the targets
were known, so this is not I2).

| Claim | Independence bound | Caps / ceiling | Support in record | Grade |
|---|---|---|---|---|
| C1. Fiducial A*, F* reproduce manuscript values | $I1 \to C$ | none | exact, two tools | **C** (computation F2) |
| C2. Homogeneous barrier 3.8585e-05 at fiducial point | $I1 \to C$ | none (new derived number) | exact, two tools | **C** (computation F2) |
| C3. Spinodal/coexistence curves; detuning thresholds 7.5976 / 7.6367 | $I1 \to C$ | none | exact, two tools | **C** (computation F2) |
| C4. Coexistence edges at $r=-0.35$ are $[-0.238, +0.905]$ | $I1 \to C$ | none | exact, two tools | **C** (computation F2) |
| C5. Manuscript band edges are sub-pattern edges, not coexistence edges | $I1 \to C$ | none | textual + computed | **C** |
| C6. Barrier vanishes at $\bar{\psi} \approx -0.144 (r_{eff} = 0)$ | $I1 \to C$ | none | exact formula | **C** (computation F2) |
| C7. 11.85% band fraction | — | — | scan absent | **INCOMPLETE-EVIDENCE** (no grade) |
| C8. $w_{6}$ narrowing 11.90% $\to 8.47$% | — | — | term form unstated | **INCOMPLETE-EVIDENCE** (no grade) |
| C9. Cosmic expansion drives (r, $\bar{\psi}, q_{0})$ | — | — | no statement exists | **ABSTAIN** (no grade) |
| C10. What fixes $\bar{\psi}$ / what supplies nucleation (IX.5) | — | — | stated open in manuscript | **ABSTAIN** (no grade) |

Human gates (HLRE §6.5): not performed — all verification here is artificial (I1);
grades cap at C (Track E) / F3 (Track F) accordingly, and the computation grades
above are stated as F2 only for the arithmetic step, not as a claim about the physics.

## 8. Assumption, parameter and choice ledgers

**Assumptions (all from the manuscript, not added):** A1. One-mode ansatz (equal
amplitude on all 24 shell modes; harmonic content excluded — manuscript quantifies
the error at 1.25%). A2. u = v = 1. A3. The $\bar{\psi}$ expansion of §II.7 as stated.
A4. Detuning penalty $(q_{0}^{2} - 8)^{2}$ as stated. A5. No expansion coupling exists in the
model (absence verified by grep, not assumed).

**Parameters:** N = 24, T = 192, Q = 3384 (stated, §II.8); $\tau = 4/\sqrt{6}$, $q_{4} = 47/8$,
S = 64/141 (derived, verified); fiducial $r = -0.35$, $\bar{\psi} = -0.18 ($stated).
Free parameters in this computation: none — every number above is stated or derived.

**Choices:** C1. $\bar{\psi}$ sample values in Fig. $1 (-0.30, -0.18, -0.10, 0, +0.03)$ chosen
to span the manuscript's table (§II.9) and band edges. C2. Scenario paths in Fig. 4
chosen as the three minimal parameter motions (one parameter varied, two fixed);
they are illustrative, not exhaustive. C3. The 11.85% figure is cited with its
qualification every time, per the manuscript's own instruction.

## 9. Costed plan (not run)

No heavy simulation was needed: all computations ran locally in seconds. The natural
follow-up — a full-field (beyond one-mode) bifurcation computation, and the joint
(detuning $\times w_{6})$ band map — is BLOCKED on missing inputs $(w_{6}$ term form; sub-pattern
data), not on compute. If those inputs are supplied, a 2D scan at the sim7 scale
$(16^{4}$ grid, Model B) is a light local job (minutes, same conda env); a larger-volume
version is ws-a's territory. No GCP spend is proposed. No VM was touched.

## VERIFIED / UNVERIFIED / FAILED

**VERIFIED:** C1, C2, C3, C4, C5, C6 (all with two independent tools; values in §2
and `data/bifurcation_values.json`).
**UNVERIFIED (INCOMPLETE-EVIDENCE):** C7 (11.85% scan), $C8 (w_{6}$ narrowing), H = 911,040
count (stated, not recomputed).
**FAILED:** none — no computed claim failed its check. The expansion-coupling
extraction failed to find any statement, which is recorded as ABSTAIN (C9), not as a
failed computation.
**ABSTAIN:** C9 (expansion drives parameters), C10 (IX.5.1, IX.5.2).

## Citation record

- McCrary, B. D. (2026). IRH v93.1, `IRH_v93_1_source_rebuilt.txt` (§II.3, §II.7,
  §II.8, §II.9, §V.3, §IX.1, §IX.5). Zenodo DOI 10.5281/zenodo.22821689.
- IRH-Theory-Development-Workspace, `predictions/VI-predictions.md` (VI.2, VI.7),
  `problems/IX1-tractable-computation.md` (§1.2, §1.3).
- Tools: SymPy 1.14.0, python-flint 0.8.0, numpy 2.4.6, matplotlib 3.11.2,
  Python 3.11.16 (conda env `jacobian-conjecture-2d`). All scripts in `data/`,
  exit code 0.
