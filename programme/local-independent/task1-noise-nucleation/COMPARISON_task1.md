# Comparison — Task 1: Noise-driven $D_{4}$ nucleation in the envelope model

**Status: COMPARISON PENDING — Academia side not landed.** Checked 2026-11-14 ~03:10 CST: no Co-scientist result files for this task exist in `~/workspace/research/irh/co-scientist-tasks-2026-11-10/` outside `local-independent/`. The Academia launch (parent browser task, 2026-11-14) is still in flight as far as this directory shows. Do not treat this comparison as complete.

**Local side:** `REPORT.md` in this directory (worker completed 2026-11-14 ~02:40 CST). Coordinator spot-check re-run 2026-11-14: `scripts/verify_params.py`, conda python 3.11.16, exit 0 — $r_{\mathrm{eff}} = 0.1072$, $u_{\mathrm{eff}} = 1.54$, $A^{*} = 0.07757529633928076$, spinodal $-0.143927$, ODE $\Delta F^{*} = 555.199$ (trap) / $554.664$ (Simpson), $R_{c} = 12.570884$.

## Local result (summary)

- Route B (radial-envelope Langevin, dilation $\lambda$ of the ODE critical profile): Arrhenius slope $567$, bootstrap 95% interval $[456, 670]$, consistent with $\Delta F^{*} = 555.20$ (not a 2% verification). 80/80 transited. Kramers prefactor $6.0$ vs predicted $9.4$–$11.6$ (factor $< 2$). Distributions broadly exponential (CV $0.81$–$1.43$). Grade **B** (slope), **C** (prefactor).
- Route A (full 4D Model B + explicitly defined conserved band-limited noise): graded crossover $0/5$ at $D = 0.1, 0.3$; $2/5$ at $D = 0.5$ (waits $11.0, 12.5$); $3/5$ at $D = 0.7$; $5/5$ at $D = 1.0$ and $3.0$. Pre-transition shell amplitude tracks the Ornstein–Uhlenbeck prediction $0.012\sqrt{D}$ to ~10% at all 7 $D$ values. Grade **B** (crossover curve).
- Synthesis (the result): the box transition is a homogeneous shell-amplitude crossing with total barrier $\approx 0.0038$, five orders below the droplet $\Delta F^{*} = 555$ — box waiting times do **not** measure the droplet barrier, for a stated finite-size reason. Any physical nucleation rate, temperature, or cosmological timescale: **ABSTAIN** (IX.5.2 stays open as physics).

## Academia side

PENDING. Launched 2026-11-14 as "Estimate noise-driven $D_{4}$ nucleation in the envelope model". No files landed yet.

## Per-number comparison checklist (complete when Academia lands)

| # | Quantity | Local value (grade) | Academia value | Agree? | Better supported | Settles |
|---|---|---|---|---|---|---|
| 1 | Arrhenius slope vs saddle barrier | $567$, 95% $[456,670]$ vs $555.20$ (B) | | | | A slope interval excluding 555 would refute the Route B recovery; agreement within intervals supports it |
| 2 | Kramers prefactor | $6.0$ vs $9.4$–$11.6$ (C) | | | | Factor-2 agreement is the current bar; a prefactor outside $[3, 20]$ would need explanation |
| 3 | Crossover $D$ values / transition fractions | $0/5, 0/5, 2/5, 3/5, 5/5, 5/5$ at $D = 0.1, 0.3, 0.5, 0.7, 1.0, 3.0$ (B) | | | | Same noise definition required; different noise (white flux vs band-limited conserved) is not the same measurement |
| 4 | Waiting-time distribution shape | Broadly exponential, CV $0.81$–$1.43$ | | | | Non-exponential shapes would indicate a different mechanism |
| 5 | Pre-transition shell amplitude vs OU prediction | $0.012\sqrt{D}$ to ~10% | | | | |
| 6 | Box barrier vs droplet barrier | $\approx 0.0038$ vs $555$ — different regimes, stated | | | | Agreement on this *distinction* is the key check, not agreement on one number |

## S3 invariance alignment (cross-domain-discovery)

Do both derivations reduce to the same equations? Route B reduces to a 1D Langevin equation on the dilation coordinate with the ODE saddle as its barrier; Route A reduces to conserved Model B with an explicit noise term. The alignment question for the Academia side is its noise definition: is it conserved (mean-preserving), band-limited, and explicitly defined — or white flux noise, which the local side tested and rejected (it gave $F_{\mathrm{exc}} \approx 2.4$ at $D = 10^{-5}$ with zero shell response)? If Academia used a different noise, the waiting times are not comparable quantities, and the comparison must say so rather than force agreement. The two local routes agree on mechanism structure (rare fluctuation crossing a saddle, then fast deterministic growth) while disagreeing on barrier value for a stated finite-size reason — that is the S3 verdict to test against Academia's derivation.

## S4 Bartha articulation + transportability audit

- Transfer "box waiting time $\to$ droplet barrier": **FAILS** — established by the local side itself (five orders of magnitude, finite-size reason). Any Academia claim that box waiting times measure $\Delta F^{*} = 555$ must be rejected on this ground.
- Transfer "envelope Langevin waiting time $\to$ physical nucleation rate": **FAILS as physics** — no physical bath, no temperature, no fluctuation–dissipation relation (ABSTAIN as physics, both sides).
- Selection-diagram note: no formal Pearl–Bareinboim diagram was built on either side yet; transportability between the envelope and the field regimes is **not established** — the local side's position is that they are different regimes, and any claim of transport must name the $S$-nodes (noise definition, box size, wall width).

## 8-check rubric (local side, as far as assessable now)

1. Independent test exists — PASS in part: two routes (envelope Langevin + full field) test the same mechanism structure independently; the Academia comparison itself is pending.
2. Falsification boundary stated — PASS: slope interval excluding 555, non-exponential distributions, crossover absent would each count against the claims.
3. Bartha articulation passes — PASS for the stated transfers (both named transfers fail, and the failures are the result).
4. Transportability audited — PARTIAL: regime difference stated and quantified; no formal selection diagram built.
5. Second independent tool — PASS: two integrators/routes; deterministic inputs re-verified by two quadratures.
6. No invented numbers — PASS: all numbers trace to runs/tables in the work dir.
7. Assumption ledger complete — PASS as reported (noise definition, box, horizons ledgered); coordinator did not re-audit every ledger line.
8. Grade honest — PASS: grades shown with worst-of reasoning; ABSTAIN stated for physics.

## Grade cap

This comparison report caps at **C (Track E) / F3 (Track F)** per the cross-domain-discovery skill's own grade cap until human source/balance gates are run. The comparison itself is a scaffold until the Academia side lands.

## What would settle the difference

Academia landing with an explicit noise definition and waiting-time curves at matched noise strengths; a third route (full radial-PDE stochastic run, costed, not yet run) agreeing with either side's barrier value; or a larger-box Route A showing the box barrier growing toward the droplet value.
