# Independent second-route rerun of the C5 edge-split verdict (2026-11-17)

**Question.** With the corrected equilibrium edge stiffness, does the
$|b|^2 = 10$ edge split verdict at $R = 20$ really flip No $\to$ Yes?
First (single-route, float64) rerun (2026-11-14): $E/E_{\mathrm{elem}}$
$2.8052 \to 3.0238$, crossing $n_{\min} = 3$; $R^*$ $23.91 \to 19.52 < 20$;
margin only $\sim 0.8\%$.

**Route (deliberately different from `task8_stiffness_C5.py`).**
`c5_edge_split_rerun.py` uses exact SymPy rational arithmetic for $A^*$
($\alpha = 67/625$, $\beta = 77/50$, quadratic $141A^2 - 8\beta A + \alpha = 0$
solved in closed form), mpmath at 50 digits for every evaluation (no
float64, no numpy, no flint), an exhaustive enumeration for $n_{\min}(10)$,
and SymPy symbolic differentiation + mpmath quadrature for the
equilibrium-field angle average. Log: `rerun_independent_2026-11-17.log`;
machine record: `rerun_independent_2026-11-17.json`. Exit 0.

## Verdict: FLIP CONFIRMED

| Quantity | Old (trial field) | Corrected (equilibrium field) |
|---|---|---|
| $K_{\mathrm{edge}}$, elementary $\|b\|^2 = 2$ | $0.490385$ | $0.326923184091396$ |
| $E_{\mathrm{edge}}(R=20)$, elementary | $0.899008$ | $0.665616521922089$ |
| $r_0/\|b\|$ edge coefficient | $2.261184$ | $1.84624873903025$ |
| $\|b\|^2 = 10$: $E/E_{\mathrm{elem}}$ | $2.8052364$ | $3.0237773943359478297$ |
| $\|b\|^2 = 10$: split cheaper at $R=20$ | No | **Yes** |
| $\|b\|^2 = 10$: $R^*$ | $23.9091063871431$ | $19.5217036181396$ |

- $n_{\min}(10) = 3$ confirmed independently: exhaustive check shows 0 of
  the 144 $\|b\|^2 = 10$ vectors is a sum of 2 roots, and
  $(-3,-1,0,0) = (-1,-1,0,0) + (-1,0,-1,0) + (-1,0,1,0)$ is an explicit
  3-root decomposition. $n_{\min}$ for the other classes:
  $\{2: 1,\ 4: 2,\ 6: 2,\ 8: 2,\ 10: 3,\ 12: 3\}$.
- **Margin:** $\rho - 3 = 0.02377739434$, i.e. $+0.79258\%$ over $n_{\min} = 3$;
  $R^*$ sits $2.39148\%$ below 20. The margin is genuinely small, so any
  manuscript amendment should state it.
- **The flip is not a numerical artifact.** $\rho$ depends on the inputs
  only through the core-radius coefficient $c = r_0/\|b\|$; the flip boundary
  $\rho(c) = 3$ sits at $c = 1.89148321800635$, i.e. $c$ would have to rise
  $2.45008\%$ to un-flip — equivalently $|F|$ would have to fall $4.72577\%$
  (to $0.0072716$ from $0.0076323$) or $A^2$ rise $4.96018\%$. The quoted
  $|F| = 0.0076323$ (7 digits) moves $\rho$ by only $\sim 10^{-6}$
  ($d\rho/d\ln|F| = -0.9706$), negligible against the $0.0238$ margin.
- **Only $\|b\|^2 = 10$ changes.** All other edge verdicts at $R = 20$ are
  identical between the old and corrected fields; screw verdicts are
  unchanged throughout.
- **Equilibrium-field factor 4/3 confirmed independently.** SymPy symbolic
  differentiation of the Volterra displacement field + mpmath quadrature
  gives $\langle f\rangle = A^2((128/3)|b_e|^2 + 32|b_s|^2)/(\pi^2 r^2)$ with
  relative error $\lesssim 10^{-51}$ on four test Burgers vectors — the
  edge/screw factor is $(128/3)/32 = 4/3$ exactly, not 2.

## Controls

- **$\|b\|^2 = 4$ bound state survives.** $K_e \ln 2 = 0.226605883312631 > 0$,
  and $2E_{\mathrm{elem}} - E(4) = 0.226605883312631$ at $R = 20$, identical
  as the algebra requires ($E(4) = 1.104627161 < 2E_{\mathrm{elem}} =
  1.331233044$).
- **Screw leg unchanged.** $K_{\mathrm{screw}}$, $r_{0,\mathrm{screw}}$,
  $E_{\mathrm{screw}}(R=20)$, ratios, split flags, and $R^*$ all agree with
  the original trial-field CSV to $< 10^{-9}$ (worst absolute difference
  $4.76\times10^{-11}$).
- **First-rerun cross-check.** $K_{\mathrm{edge}}$, $r_{0,\mathrm{edge}}$,
  $E_{\mathrm{edge}}(R=20)$, $E/E_{\mathrm{elem}}$, and $R^*$ agree with
  `task8_summary_C5.json` to $< 10^{-9}$ (worst absolute difference
  $1.0\times10^{-15}$).

## Tool verdicts

- Python 3.11.16 (conda env `jacobian-conjecture-2d`), SymPy 1.14.0,
  mpmath 1.4.1 — script exit 0, all internal assertions passed.
- Inputs: $\alpha = 67/625 = 0.1072$, $\beta = 77/50 = 1.54$,
  $A^* = 0.0775752963392807571381705213366$,
  $A^{*2} = 0.00601792660212722643930681434658$,
  $\lambda = \mu = 256A^{*2} = 1.5405892101445699685$,
  $F_{\mathrm{dens}} = -0.0076323$, $R_{\mathrm{sys}} = 20$.

No manuscript, inventory, or repo-tracked file was edited. This directory
is the only thing written.
