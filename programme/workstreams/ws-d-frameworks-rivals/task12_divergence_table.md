# Task 12 — Shared-conditions comparison table and divergence points — FINAL

Status: FINAL (assembled by the workstream-D parent agent from the child draft `task12_divergence_table_DRAFT.md`).
All numbers below are outputs of the executed models in `task12_models/`
(SymPy 1.14.0, numpy 2.4.6, python-flint 0.8.0; driver exit 0, 55 PASS / 0 FAIL).
See `task12_rival_accounts_DRAFT.md` for grades, ledgers and sources.

## Shared conditions

- Same comparison observables O1–O5 (below) for every account, where the
  account has an entry at all. Where an account has no entry, the cell says
  so — no observable was redefined to force a comparison.
- Same parameter conventions where comparable: dimensionless ratios,
  per-year fractional drift rates, diffusion scale $\sigma$ for $D_{s}$.
- IRH dimensional assignment: UNDECIDED (v93.1 §IX.2, readings A/B/C).
  Models that need a signature assume reading (A) provisionally and flag it;
  the IRH reference model itself is reading-independent for the quantities
  it checks.

## Comparison table

| Observable | IRH (v93.1, reference) | (b) Greensite / Carlini–Greensite (toy) | (c) Dirac / varying-$\alpha ($toy) | (d) Anthropic / multiverse (Weinberg window) | (e) CDT discrete spacetime (2005 fit) |
|---|---|---|---|---|---|
| O1 — Spacetime signature | NO PREDICTION. §IX.3: needs external structure; $v92 i^{2}=-1$ argument retracted. Reading (A) would need the §IX.3 mechanism. | Lorentzian favoured IFF $n_{F} > n_{B} (\Delta>0)$; Euclidean favoured iff $\Delta<0$; undetermined iff $\Delta=0$. Toy potential $\mathrm{Re} V = \Delta\cdot\cos \theta$, $\theta=\pi$ Lorentzian minimum iff $\Delta>0$. Full one-loop mechanism ABSTAINED. | No entry (signature not addressed by this rival). | No entry (signature not addressed). | No entry as modelled (CDT takes Lorentzian building blocks as input; signature is not its divergence observable here). |
| O2 — Present-day fractional drift of $\alpha$ | 0 exactly (no varying-constants mechanism; $\alpha$ value not derived). Consistent with Rosenband 2008. | No entry. | Toy linear drift $r = 1\times10^{-15}$/yr (ILLUSTRATIVE, not measured) is EXCLUDED: exceeds the Rosenband $1\sigma$ envelope edge $(3.9\times10^{-17}$/yr) by ~$25.6\times$. Dirac $G(t)=G_{0}t_{0}/t$ gives Ġ/$G = -7.25\times10^{-11}$/yr $(t_{0}=13.8$ Gyr, illustrative). | No entry $(\alpha$ drift not addressed). | No entry. |
| O2b — Measured constraint | Rosenband et al., Science 319, $1808 (2008): \dot{\alpha}/\alpha = (-1.6 \pm 2.3)\times10^{-17}$/yr; interval contains 0. | — | Same constraint; toy excluded by it. No primary-source Ġ/G constraint stated (ABSTAIN). | — | — |
| O3 — Spectral / effective dimension vs scale | D = 4 at ALL scales (field on $\mathbb{R}^{4}$, §I.2; SH term marginal at d=4, §III.4). No flow predicted. | No entry. | No entry. | No entry. | $D_{s}(\sigma) = 4.02 - 119/(54+\sigma)$: 1.82 at $\sigma\to0$, 2.16 at $\sigma=10$, 2.92 at $\sigma=54$, 3.25 at $\sigma=100$, 3.91 at $\sigma=1000$, 4.01 at $\sigma=10000$, $\to4.02$. Flow of ~2.2 at short scales. Later CDT work finds ~3/2 at small scales (Coumbe & Jurkiewicz 2015) — endpoint unsettled. |
| O4 — Value / typicality of $\Lambda (y = \Lambda/\Lambda_{obs})$ | NO ENTRY — no $\Lambda$ mechanism in v93.1. | No entry. | No entry. | Accommodates y~1 under every prior tried, but $P(0.5\leqy\leq2) = 0.0015 ($uniform [0,1000]) vs 0.1204 (log-uniform [0.01,1000]) vs 0.015 (uniform on window [0,100]): prior-dependence ~$80\times$. $P(y\leq100) = 0.10$ vs 0.80. No prior-independent number produced. | No entry. |
| O5 — Value of $\alpha^{-1}$ | ANSATZ ONLY: $137 + 1/(28-\pi/14) = 137.0360028\dots$, diff vs CODATA 2022 (137.035999177(\$21$)) = +3.6\times10^{-6}$$. Arithmetic exact; derivation ABSENT (Part VII downgrade). | No entry. | No entry for the value (Dirac varies G, not $$\alpha$$; the $$\alpha$\$ toy varies the rate, not the value). | No entry. | No entry. |
| O0 — Internal reference quantities (IRH only) | $S = \tau^{2}/q_{4}$: $D_{4} 64/141 \approx 0.4539$; $A_{4}* 12/31 \approx 0.3871$; ratio 496/423, margin $73/423 \approx 17.26$%; $\tau_{D}_{4}/\tau_{BCC} = \sqrt{2}$; $B* = 2u\tau/(3$vq${}_{4})$; $r_{c} = 2u^{2}\tau^{2}/(9$vq${}_{4})$; $r_{eff} = +0.1072$ at $\bar{\psi}=-0.18 ($nucleation required). Triad relations $c = a_{0}\Omega_{P}$, $\hbar = M*c a_{0}$, $G = 24c^{2}a_{0}/M$* are DEFINITIONS, not derivations. | — | — | — | — |

## Divergence points (observable, IRH value, rival value, discriminating test)

| # | Observable | IRH value | Rival value | Discriminating test |
|---|---|---|---|---|
| D1 | Signature (O1) | No prediction (UNDECIDED, §IX.2/IX.3) | Greensite toy: Lorentzian iff $n_{F} > n_{B}$ | Count the propagating fermionic vs bosonic DOF of the substrate's field content and check the sign of $\Delta$. IRH cannot do this: its substrate is one classical scalar, so $\Delta$ has no IRH counterpart — the transfer FAILS (Bartha, S4). The test discriminates the rival against IRH's silence, not against an IRH prediction. |
| D2 | $\alpha$ drift rate (O2) | 0 | Toy $r = 1\times10^{-15}$/yr | Rosenband-type clock comparison: the toy is already excluded by $(-1.6\pm2.3)\times10^{-17}$/yr. A rival must predict |r| ≲ $4\times10^{-17}$/yr to survive present-day tests; IRH's 0 survives trivially (it predicts nothing here). |
| D3 | Ġ/G (O2) | 0 (no mechanism) | Dirac: $-7.25\times10^{-11}$/yr at $t_{0} = 13.8$ Gyr | A primary-source Ġ/G bound (e.g. lunar laser ranging) — NOT verified in this run, so no verdict on Dirac is stated. The Dirac rate is ~$3\times10^{6}\times$ the Rosenband $\alpha$ scale, but that is a scale comparison across different observables, not a falsification. |
| D4 | Spectral dimension at short scales (O3) | 4 (no flow) | CDT fit: $D_{s} \approx 1.82$ at $\sigma\to0$; $\approx 2.92$ at $\sigma=54$ | A probe of effective dimension at short diffusion scales: IRH predicts no flow, CDT predicts flow of ~2.2. No such probe exists inside IRH's formalism; the test is a cross-framework comparison, and the CDT endpoint itself is disputed (~2 vs ~3/2). |
| D5 | Typicality of $\Lambda (O4)$ | No entry | Anthropic: P(near) = 0.0015–0.1204 depending on prior $(~80\times$ swing) | No discriminating test exists within the model: the answer is the prior. The divergence is prediction vs accommodation — the anthropic account accommodates the observed value under every prior and predicts no prior-independent number. A test would have to fix the prior independently (e.g. from a specified multiverse measure), which Weinberg 1987 does not supply. |
| D6 | Value of $\alpha^{-1} (O5)$ | Ansatz 137.0360028 (not derived) | No rival value modelled | None from this task: no rival here derives $\alpha^{-1}$ either. The shared finding is negative — neither IRH nor any rival formalised here derives the measured 137.035999177(21). The IRH ansatz's closeness $(+3.6\times10^{-6})$ is arithmetic, not evidence of a derivation. |
| D7 | Dimensional assignment (background) | UNDECIDED (A)/(B)/(C) mutually exclusive | Greensite needs reading (A)-like Euclidean base; CDT needs a Lorentzian causal structure as input; anthropic needs a multiverse measure | Deciding §IX.2 is a prerequisite for any shared-conditions comparison that touches signature or spacetime emergence. Until it is decided, cross-framework comparisons on O1 are comparisons against IRH's open question, not against an IRH claim. |

## Comparisons that could NOT be run under shared conditions (stated, not forced)

- **Greensite mechanism into IRH (D1):** no shared observable exists, because
  IRH's substrate has no fermion/boson DOF count. The toy was run standalone;
  the transfer into IRH FAILS the Bartha gate (S4).
- **Anthropic typicality vs IRH (D5):** IRH has no $\Lambda$ observable, so there is no
  shared-condition run — the model is reported standalone and the divergence
  is the absence of an IRH entry plus the prior-dependence.
- **Causal-set spectral dimension:** no $D_{s}(\sigma)$ formula was verified from a
  primary source in this run, so no causal-set column exists. ABSTAIN.
- **Einstein equations:** IRH's derivation is retracted (§IX.3, analogy not
  derivation); none of the rivals formalised here derives them either, so no
  shared-condition comparison was constructed.
- **Dirac Ġ/G vs Rosenband $\dot{\alpha}/\alpha$:** different observables; only a labelled
  scale comparison was made, never a falsification claim.
