# Task 2 — First directional anisotropy of D4 waves

**CLAIM:** The D4 root system's sixth moment is the first directionally
dependent moment: it is exactly isotropic through fourth order, and at
sixth order $M6(\hat{n}) = 60\cdotS4 - 48\cdotS6$ on the unit sphere, with mean 15,
global minimum 12 (at $\langle100\rangle$ axes and $\langle111\rangle$ body diagonals), global maximum
18 (at $\langle110\rangle$ face diagonals) — $a \pm20$% directional signature, max/min = 3/2.

**STATUS:** VERIFIED. The moment polynomial is an exact symbolic identity
(SymPy expansion, cross-checked against direct summation at 50 random
directions, max error < 1e-9). The extrema are exact (Lagrange-multiplier
enumeration) and confirmed by independent numerical optimization (scipy,
200 random starts). The lower bound has an AM-GM proof; the upper bound is
numerically verified, not hand-proven. M6 is the root-system moment, NOT
the sextic Landau count H = 911040 — the two must not be confused.

## 1. Derivation

For a direction k (not necessarily unit), the sixth moment over the 24 D4
roots $\alpha$ is

$M6(k) = \Sigma_{\alpha} (k\cdot\alpha)^{6}$.

Expanding with SymPy over the root set ${(\pm2,\pm2,0,0)$ and permutations}:

**M6(k) = 60 |k|${}^{2} \Sigma_{i} k_{i}^{4} - 48 \Sigma_{i} k_{i}^{6}$.**

Cross-check: direct summation at 50 random directions, max deviation
< 1e-9. (The second, fourth, and sixth moments were computed the same way;
M2 = 12|k|${}^{2}$ and M4 = 12|k|${}^{4}$ are direction-independent — exact isotropy
through fourth order, as in v93.1.)

On the unit sphere (|k| = 1), writing $S4 = \Sigma \hat{n}_{i}^{4}$ and $S6 = \Sigma \hat{n}_{i}^{6}$:

**$M6(\hat{n}) = 60\cdotS4 - 48\cdotS6$.**

Mean over $S^{3}$: E[S4] = 1/2, E[S6] = 5/16 (exact spherical moments), so
**E[M6] = $60\cdot(1/2) - 48\cdot(5/16) = 30 - 15 = 15$ exactly.**

## 2. Extrema (exact)

Critical points by Lagrange multipliers (maximise M6 on $S^{3}$; at a critical
point the nonzero $\hat{n}_{i}^{2}$ take at most two values, and the quadratic they
satisfy has root-sum 5/6):

| value | directions (representative) |
|---|---|
| **12** (global min) | $\langle100\rangle$ axes; $\langle111\rangle$ body diagonals |
| $44/3 \approx 14.667$ | $\langle1110\rangle$; (a,a,a,b) with $a^{2} = 1/12$, $b^{2} = 3/4$ |
| $46/3 \approx 15.333$ | (a,a,b,0) with $a^{2} = 1/6$, $b^{2} = 2/3$ |
| **18** (global max) | $\langle110\rangle$ face diagonals |

So **max/min = 18/12 = 3/2**, i.e. **$\pm20$% about the mean 15**:
minimum 20% below, maximum 20% above. Independent check: scipy
optimization from 200 random starts gives max 18.000000000000014 and min
11.99999999999999.

**Lower bound (proven$):** M6 - 12$|k|${}^{6} \geq 0$ has an AM-GM proof (recorded in
the script comments): writing M6 in terms of S4, S6 and applying AM-GM to
the coordinate sixth powers against the fourth powers gives the bound,
with equality at $\langle100\rangle$ and $\langle111\rangle$.

**Upper bound (numerically verified, NOT proven$):** M6 \leq 18$|k|${}^{6}$ is
established by the Lagrange enumeration (which lists all critical points
of a polynomial on a compact sphere, hence the global max is among them)
plus the 200-start numerical confirmation. No hand proof of the upper
bound is given; the Lagrange argument itself is exact but was executed
symbolically/numerically rather than written as a closed-form proof.

## 3. Directional signature (for the manuscript)

The sharp prediction: along $\langle110\rangle$ face diagonals the sixth-order response
is 50% stronger than along $\langle100\rangle$ axes or $\langle111\rangle$ body diagonals
(18 vs 12), with the spherical mean 15. A measurement (or simulation) of
any sixth-order D4 observable as a function of direction should show this
pattern: maxima on the $12 \langle110\rangle$ directions, minima on the $6 \langle100\rangle$ axes
and $8 \langle111\rangle$ diagonals. Figure `task2_disk.png` shows M6 over a disk
through the sphere; `task2_path.png` shows M6 along a path through the
extremal directions.

## 4. Checks

| check | verdict |
|---|---|
| M6 polynomial by SymPy expansion vs direct summation, 50 random directions, max err < 1e-9 | PASS |
| M2 = 12\|k\|${}^{2}$, M4 = 12\|k\|${}^{4}$ symbolically + numerically over 400 random directions (max dev ~1e-14) | PASS |
| Mean over $S^{3} = 15$ exactly (spherical moments) | PASS |
| Critical points enumerated exactly via Lagrange multipliers | PASS |
| scipy optimization, 200 random starts: max 18.000000000000014, min 11.99999999999999 | PASS |
| Lower bound $M6 \geq 12$\|k\|${}^{6}$ by AM-GM | PASS (proof) |
| M6 distinguished from the sextic Landau count H = 911040 | PASS (stated; different objects) |

## 5. Rival / failure mode

The main rival is that a sixth-order *observable* need not track M6
directly: M6 is the moment of the root system, and any particular
sixth-order term in an effective theory carries its own coefficient and
may combine M6 with other invariants. The directional *pattern* (maxima
at $\langle110\rangle$, minima at $\langle100\rangle/\langle111\rangle)$ is a property of M6 itself; whether a
given experiment sees it depends on the observable's coupling to M6. A
second failure mode: the Lagrange enumeration assumes the critical-point
classification (at most two distinct nonzero $\hat{n}_{i}^{2})$ is complete — it is
derived in the script, and the 200-start numerical sweep found no
additional critical values, but a missed degenerate family would change
the extremal list (it would not change min 12 / max 18 unless it lay
outside [12, 18], which the numerical sweep constrains).

## 6. Evidence that would change the answer

- A direction with $M6(\hat{n})$ outside [12, 18] would falsify the extremal
  values; the 200-start sweep and the Lagrange enumeration both bound it
  to [12, 18].
- A hand proof of the upper bound $M6 \leq 18$|k|${}^{6}$ would raise that claim from
  numerically verified to proven (grade $B \to A)$.
- If the manuscript's isotropy claim is meant at a different order (e.g.
  a sixth-order term that vanishes by a further symmetry), the relevance
  of M6 to that observable would need re-examination — but M6 itself, as
  a property of the root system, would stand.

## 7. HLRE grades (per narrow claim; worst-of shown)

| claim | grade | basis |
|---|---|---|
| M6(k) = 60\|k\|${}^{2}\Sigmak_{i}^{4} - 48\Sigmak_{i}^{6}$ | B | SymPy identity + 50-direction cross-check; computer algebra, not hand proof |
| Exact isotropy through fourth order (M2, M4 direction-free) | B | symbolic + numerical cross-check (same basis) |
| Mean over $S^{3} = 15$ exactly | A | exact spherical-moment computation |
| Global min 12 at $\langle100\rangle$, $\langle111\rangle$ | A | Lagrange enumeration + AM-GM proof of the lower bound |
| Global max 18 at $\langle110\rangle$ | B | Lagrange enumeration + 200-start numerical confirmation; no hand proof of the upper bound |
| Directional signature $\pm20$%, max/min 3/2 | B | follows from the min/max (worst-of B) |

## 8. Deliverables

- Figures: `figures/task2_path.png`, `figures/task2_disk.png`
- Tables: `tables/task2_moment_values.csv`,
  `tables/task2_critical_points.csv`, `tables/task2_summary.json`
- Code: `task2_anisotropy.py` (uses shared `d4model.py`)

## 9. Assumption / parameter / choice ledger

- Roots: the 24 D4 roots $(\pm2,\pm2,0,0)$ and permutations (scaled form;
  the moment is homogeneous of degree 6, so the scale factors out).
- M6 is defined as $\Sigma_{\alpha} (k\cdot\alpha)^{6}$ over the root set; no model parameters
  (r, u, v, $\bar{\psi})$ enter — this is a root-system property.
- Numerical checks: 50 random directions (polynomial identity),
  400 random directions (M2/M4), 200 random starts (extrema).
- Distinction recorded: M6 (root-system sixth moment$) \neq H = 911040$
  (ordered sextuple count in the Landau functional).
