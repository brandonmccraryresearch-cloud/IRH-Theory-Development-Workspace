# Task 3 — Chart the D4 stability band under detuning

**CLAIM:** The full 24-mode D4 pattern wins a band in the $(\bar{\psi}, r)$ plane
whose extent is set by two boundaries — the coexistence line $F_{full} = 0$
and the competition line $F_{full} = F_{hex}$ — and which detuning shifts to
deeper quench depth by exactly $\delta^{2} (\delta = q0^{2} - 8)$ while the sixth-order
coupling w6 narrows it. In the pre-fixed window W1
$(\bar{\psi} \in [-0.6, 0.2] \times r \in [-0.6, 0.1], 161\times161)$ the band is 11.60% of the
plane at $(\delta = 0, w6 = 0)$ and 8.36% at $(\delta = 0, w6 = 0.2)$; detuning to
$\delta = 0.5$ shrinks it to 8.18% (w6 = 0) but does NOT annihilate it in-window.
The manuscript's 11.85% / 11.90% figures are window-dependent and are not
reproduced exactly (their window is unstated); the endpoints and trends
check out, with one correction: "$\delta = 0.5$ kills the ordered branch" holds
at the operating point, not across the plane.

**STATUS:** VERIFIED for the stated windows and the one-mode Landau
functional with the sub-pattern family {hex6, fcc12, sq4, sq8} (tri3
excluded for cause, §6). Minimiser validated against scipy bounded Brent
at 12 random points (agreement < 1e-6).

## 1. Method

One-mode functional per pattern S (exact counts n, T, Q, H from the shared
module):

$F_{S}(A) = (n/2) r_{eff} A^{2} - (T/3) u_{eff} A^{3} + ($vQ/\$4$) A^{4} + (w6$\cdotH/$6) A^{6}$\$,
$r_{eff} = r_{shell} - 2u\bar{\psi} + 3v\bar{\psi}^{2}$, $r_{shell} = r + \delta^{2}$, $u_{eff} = u - 3v\bar{\psi}$.

Detuning enters only through $r_{shell} ($all competitors are shell modes).
Minimisation is vectorised over the grid: exact quadratic formula for
w6 = 0; Newton from the w6 = 0 roots plus a coarse A-scan for w6 > 0.
The band is the set of grid points where the full 24-mode pattern is the
unique lowest minimum and below zero. Two windows were fixed BEFORE
computing: $W1 (\bar{\psi} \in [-0.6, 0.2], r \in [-0.6, 0.1])$ and W2
$(\bar{\psi} \in [-0.5, 0.5], r \in [-0.5, 0.5])$, both $161\times161$.

## 2. Band fractions (full sub-pattern family; hex-only in brackets)

W1:

| $\delta$ \ w6 | 0 | 0.05 | 0.1 | 0.2 |
|---|---|---|---|---|
| 0.0 | **11.60%** (12.94%) | 10.29% (11.68%) | 9.50% (10.87%) | **8.36%** (9.68%) |
| 0.1 | 11.50% (12.84%) | 10.25% (11.64%) | 9.41% (10.77%) | 8.31% (9.62%) |
| 0.2 | 11.18% (12.47%) | 9.98% (11.32%) | 9.22% (10.54%) | 8.19% (9.44%) |
| 0.3 | 10.58% (11.84%) | 9.53% (10.81%) | 8.81% (10.07%) | 7.86% (9.08%) |
| 0.4 | 9.69% (10.85%) | 8.82% (9.98%) | 8.20% (9.36%) | 7.37% (8.51%) |
| 0.5 | 8.18% (9.12%) | 7.51% (8.48%) | 7.06% (8.04%) | 6.42% (7.34%) |

W2 (sensitivity window$): \delta = 0$, w6 = 0 gives 6.26% (hex-only 6.98%);
$\delta = 0.5$, w6 = 0.2 gives 2.93% (3.36%). Full table:
`tables/task3_band.csv`.

## 3. Manuscript endpoint checks

- **11.85% / 11.90%:** my W1 gives 11.60% (full family) and 12.94%
  (hex-only competitor, the manuscript's construction) at $(\delta = 0, w6 = 0)$;
  the manuscript's 11.85% lies between them. The percentages are
  window-dependent and the manuscript's window is unstated, so exact
  reproduction is not expected — but the value is bracketed, not
  contradicted.
- **$w6 0 \to 0.2$ narrows the band:** confirmed. W1: 11.60% $\to 8.36$%
  (manuscript: 11.90% $\to 8.47$%). The w6 = 0.2 value agrees to 0.1
  percentage points.
- **$\delta = 0.5$ kills the ordered branch:** TRUE at the operating point
  $(\bar{\psi}, r) = (-0.18, -0.35)$ — verified: at $\delta = 0.5$ the stationary points
  vanish (discriminant < 0) and $F_{min} = 0$ there, matching the manuscript's
  $q0^{2} = 7.5$ result. But FALSE as a statement about the whole plane: the
  band persists in-window at $\delta = 0.5 (8.18$% in W1), shifted to deeper
  r. The precise statement is that detuning shifts the band by $\delta^{2}$ in r:
  the coexistence line at $\bar{\psi} = -0.18$ moves from $r = -0.218 (\delta = 0)$ to
  $r = -0.468 (\delta = 0.5)$, exactly $-\delta^{2}$. Within a fixed window the band
  shrinks; it vanishes only when $\delta^{2}$ exceeds the window's depth.
- **Operating point:** at $(-0.18, -0.35)$, $\delta = 0$: A* = 0.0776,
  $F = -0.007632 ($manuscript $-0.0076323)$ — full beats hex $(-0.002254)$ and
  fcc\$12 (-0.005362)\$; sq4 and sq8 have no ordered minimum (T = 0, no
  cubic term) at $r_{eff} > 0$.

## 4. Band boundaries $(\delta = 0, w6 = 0$; exact brentq on the large root)

Coexistence line $F_{full} = 0$ and competition line $F_{full} = F_{hex}$:

| $\bar{\psi}$ | $r (F_{full} = 0)$ | $r (F_{full} = F_{hex})$ |
|---|---|---|
| $-0.33$ | $-0.5873$ | — |
| $-0.31$ | $-0.5326$ | — |
| $-0.29$ | $-0.4796$ | — |
| $-0.27$ | $-0.4283$ | — |
| $-0.25$ | $-0.3786$ | — |
| $-0.23$ | $-0.3306$ | — |
| $-0.21$ | $-0.2843$ | — |
| $-0.19$ | $-0.2397$ | $-0.5636$ |
| $-0.18$ | $-0.2180$ | $\approx -0.53$ |
| $-0.17$ | $-0.1967$ | $-0.4964$ |
| $-0.15$ | $-0.1554$ | $-0.4317$ |
| $-0.13$ | $-0.1158$ | $-0.3697$ |
| $-0.11$ | $-0.0779$ | $-0.3103$ |
| $-0.09$ | $-0.0416$ | $-0.2536$ |
| $-0.07$ | $-0.0070$ | $-0.1994$ |
| $-0.05$ | +0.0259 | $-0.1479$ |
| $-0.03$ | +0.0571 | $-0.0990$ |
| $-0.01$ | +0.0867 | $-0.0527$ |
| +0.01 | +0.1146 | $-0.0090$ |
| +0.03 | +0.1408 | +0.0320 |
| +0.05 | +0.1654 | +0.0704 |

(— = no crossing in the scanned r-range: for $\bar{\psi} \leq -0.35$ the ordered
branch does not exist even at $r = -0.6$; for $\bar{\psi} \leq -0.21$ full beats hex
throughout the ordered region.) The $\bar{\psi} = -0.18$ coexistence value
$-0.2180$ independently matches the Task 4 coexistence computation
$(-0.217984)$. Full table: `tables/task3_boundaries.csv`.

The phase map (winner at each grid point, $\delta = 0, w6 = 0)$ is
`figures/task3_phasemap.png`; the band-fraction heatmap is
`figures/task3_band_heatmap.png`; the boundary curves are
`figures/task3_boundaries.png`.

## 5. Checks

| check | verdict |
|---|---|
| Vectorised minimiser vs scipy bounded Brent, 12 random points, agreement < 1e-6 | PASS |
| Operating point A* = 0.0776, $F = -0.007632 ($manuscript $-0.0076323)$ | PASS |
| Coexistence at $\bar{\psi} = -0.18$: $r = -0.2180$, matches Task 4'$s -0.217984 ($independent route) | PASS |
| $\delta = 0.5$ kills the ordered branch at the operating point (disc < 0) | PASS |
| Detuning shifts coexistence by exactly $-\delta^{2} ($verified $-0.218 \to -0.468)$ | PASS |
| w6 narrowing direction and magnitude (11.60% $\to 8.36$% vs manuscript 11.90% $\to 8.47$%) | PASS |
| Band fractions in two windows (W1 11.60%, W2 6.26% at $\delta = 0, w6 = 0)$ | PASS (window dependence demonstrated) |

**Withdrawal / demotion note (bugs found during checking, all fixed in
the delivered code):**
(i) First run: the full-family band was 0.00% everywhere — tri3 (Q = 0)
divided by zero in the vectorised quadratic formula, giving NaN minima
that blocked the band. Fixed with a Q = 0-safe linear root and +inf
marking at w6 = 0. (ii) Second run: the full-family band was 0.00% at
every w6 > 0 — tri3's functional, stabilised only by the sextic, has a
deep minimum at unphysical amplitude $A \approx 2.7 (F \approx -33)$, so it "won"
everywhere. tri3 is now EXCLUDED from the competitor family at all w6
(see §6); the band is then sensible and smooth in w6. (iii) The boundary
computation first used brentq on $F_{min}$, which returns the bracket endpoint
because $F_{min}$ is flat (= 0) above coexistence; it now uses brentq on
$F(A_{large}(r))$, which is smooth through coexistence.

## 6. Why tri3 is excluded (and what it would take to include it)

tri3 (3 modes) has quartic coefficient Q = 0 exactly. Its one-mode
functional is F = $(3/2)r_{eff}\cdotA^{2} - 2\cdotu_{eff}\cdotA^{3} + (w6\cdot90/6)A^{6}$: a cubic with
no quartic term. At w6 = 0 it is unbounded below (no minimum exists); at
w6 > 0 the sextic stabilises it only at $A \approx 2.7$, where the pattern
amplitude dwarfs the mean field (|$\bar{\psi}$| $\leq 0.6)$ and the one-mode ansatz has
broken down. Including it as a competitor would assert that a 3-mode
pattern with amplitude 2.7 and $F \approx -33$ is the ground state — a truncation
artefact, not a physical prediction. It is excluded from the band
determination; re-including it would require a truncation in which its
amplitude is bounded by higher-order physics (e.g. a physical eighth-order
term or a two-mode analysis), which is outside this task.

## 7. Rival / failure mode

The main rival is the competitor set: the band is defined against
{hex6, fcc12, sq4, sq8}. A pattern family not considered (e.g. a 12-mode
pattern other than fcc12, or a mixed pattern) could in principle beat the
full pattern somewhere and shrink the band further. The one-mode
approximation itself is the second failure mode: it treats each pattern's
amplitude as uniform and ignores cross-pattern couplings and the relaxed
(fully nonlinear) free energy — the relaxed value at the operating point
$(-0.0077276)$ is 1.2% below the one-mode value, so the band edges would
shift slightly in a full treatment. The detuning model $(r_{shell} = r + \delta^{2})$
assumes all competitors are shell modes, which is exact for the family
used.

## 8. Evidence that would change the answer

- If the manuscript's window were stated, the 11.85% could be checked
  exactly; as it stands the bracket (11.60% full family, 12.94% hex-only
  in W1) is the check.
- A new competing sub-pattern with a lower minimum inside the band would
  shrink the band; the band fractions would need recomputation with the
  enlarged family.
- A full (relaxed) free-energy band computation would shift the boundaries
  by ~1% in F; the qualitative picture (detuning shift $\delta^{2}, w6$ narrowing)
  would not change.

## 9. HLRE grades (per narrow claim; worst-of shown)

| claim | grade | basis |
|---|---|---|
| Band fractions in W1/W2 at $(\delta, w6)$ grid | B | exact minimisation on stated windows, validated vs scipy; window-dependent by construction |
| w6 narrows the band 11.60% $\to 8.36$% (manuscript 11.90% $\to 8.47$%) | B | computation + manuscript comparison; the manuscript's window is unstated so the comparison is at trend level |
| Detuning shifts the band by $\delta^{2}$ in r (coexistence $-0.218 \to -0.468)$ | B | exact root-finding; the shift is a property of the one-mode functional |
| $\delta = 0.5$ kills the ordered branch at the operating point | B | discriminant computation + manuscript sim7 agreement |
| "$\delta = 0.5$ kills the ordered branch" as a plane-wide claim | C (corrected) | REFUTED in-window (8.18% remains); the correct statement is the shift |
| Band boundaries (coexistence + competition lines) | B | exact brentq on the large stationary root; cross-checked vs Task 4 |
| Manuscript 11.85% reproduced | C | bracketed (11.60% / 12.94%) but not reproduced exactly; window unstated |

## 10. Deliverables

- Figures: `figures/task3_phasemap.png`,
  `figures/task3_band_heatmap.png`, `figures/task3_boundaries.png`
- Tables: `tables/task3_band.csv`, `tables/task3_band.json`,
  `tables/task3_boundaries.csv`, `tables/task3_winner_W1.npy`,
  `tables/task3_winF_W1.npy`
- Code: `task3_band.py` (uses shared `d4model.py`)

## 11. Assumption / parameter / choice ledger

- Windows fixed BEFORE computing: $W1 \bar{\psi} \in [-0.6, 0.2] \times r \in [-0.6, 0.1]$;
  $W2 \bar{\psi} \in [-0.5, 0.5] \times r \in [-0.5, 0.5]$; both $161\times161$.
- Detuning grid $\delta \in {0, 0.1, 0.2, 0.3, 0.4, 0.5}$; $w6 \in {0, 0.05, 0.1, 0.2}$.
- Competitor family {hex6, fcc12, sq4, sq8}; tri3 excluded for cause (§6).
- Band = grid fraction where full24 is the unique lowest minimum and
  F < 0 (tolerance 1e-12 against competitors).
- Parameters $r = -0.35$, u = v = 1, $q0^{2} = 8.0 ($tuned), $\bar{\psi} = -0.18$ at the
  operating point — all from the manuscript / repo verification code, none
  invented.
