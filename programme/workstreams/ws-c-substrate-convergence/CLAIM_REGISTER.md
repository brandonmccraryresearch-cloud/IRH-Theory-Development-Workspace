# Claim register — WS-C (substrate models + D4 convergence)
# Registered BEFORE substantive analysis. HLRE v5.1 Gate 1.
# Programme: ~/workspace/research/irh/co-scientist-tasks-2026-11-10/PROGRAMME_BRIEF.md
# Sources: IRH v93.1 source rebuild (sha256 cebc3b6f...ffa8), IRH repo clone
# (HEAD 94a862b), verification/ (sim6_units.py, sim7_fairtest.py, verify_claims.py 51/51).
# Tier: Standard (mechanism proposed; others may cite). Track E except C1.4/C2.1a (Track F).
# Independence ceiling for all simulation claims: I1 (artificial verification, shared pipeline).
# Cross-domain-discovery grade caps apply to S1-S7 transfer claims: Track E C / Track F F3
# until a human runs the source/balance gates. No claim here exceeds C on Track E.

## Task 1 — Formalize Substrate Selection Models

- C1.1 [Track E] The static-D4 account (v92 ontology: D4 postulated as a static lattice,
  fields at sites) predicts the full 24-mode interference pattern under ALL conditions
  (psi-bar, q0 detuning, triad coupling, initial condition) because the pattern is
  postulated, not produced. Falsifier: any manuscript statement giving the static
  account a selection dynamics.
- C1.2 [Track E] The dynamically selected D4 account (v93.1: tension-relaxation damped
  wave + Model B conserved dynamics) predicts the full 24-mode pattern ONLY inside
  the psi-bar band (approx -0.33..0.03, quench-dependent) with q0 tuned onto the shell
  and triads active; outside it predicts sub-patterns or disorder. Falsifier: a noise
  quench outside the band reaching 24/24 modes, or inside the band failing to.
- C1.3 [Track E] The two accounts' interference-pattern predictions DIVERGE exactly
  when (psi-bar outside band) OR (ordered branch absent: $(T u_{eff})^{2} < 4 v Q N r_{eff}$,
  which at psi-bar=-0.18, r=-0.35 is |$q0^{2}-8$| > 0.4024; the manuscript'$s q0^{2}=7.5$
  example, detuning 0.5, lies past this edge) OR (triad coupling off) OR (initial
  condition outside the full-pattern basin); they AGREE (both full 24-mode) only
  inside the band with q0 tuned, triads on, seeded/basin initial condition.
  Agreement there is not evidence for the static account (it postulates what the
  dynamic account derives). Falsifier: a probe point where the stated boundary is wrong.
- C1.4 [Track F] The v93.1 ontology change dissolves the v92 circularity objection:
  a0 = 2*pi/q0 is an output of the substrate dispersion, not an input defined via $L_{P}$.
  (Deductive: definitional + the dispersion derivation of §III.1; checkable by the
  a0 identity and the CFL derivation chain.)
- C1.5 [Track E] The static account CANNOT explain: (a) selection among lattices
  (why D4 not Z4); (b) the finite psi-bar band; (c) the 6-mode annealed outcome;
  (d) nucleation (first-order transition); (e) the Model A vs Model B distinction.
  Each is a negative claim, established by the absence of the relevant structure in
  the static formulation (manuscript §I.1) plus the probe results.
- C1.6 [Track E] Equilibrium Landau selection (Alexander-McTague / Elitzur-Karni-
  Rabinovici) and particle crystallization (Hoy 4D Lennard-Jones MD) select the SAME
  winner (D4) by independent routes; they corroborate the winner, they do not rival
  the dynamic account's interference-pattern predictions (different observables:
  near-melting equilibrium / particle trajectories vs field interference pattern).
  Transport of the 3D BCC result to 4D D4 via the S-criterion is a deductive
  combinatorics transfer (same code, same functional); the near-melting scope does
  NOT transfer (Bartha gate: scope is a critical feature of the 3D prior association
  that has no 4D counterpart in the dynamic claim).

## Task 2 — Check D4 Dynamics Convergence

- C2.1 [Track E/F] The reference tension-relaxation model (sim6 Model B semi-implicit
  attractor, N=16, L=pi, $q0^{2}=8.0$, r=-0.35, u=v=1, psi-bar=-0.18, dt=0.005, T=30)
  reproduces the analytic stationary state: A* = 0.0775753 (F), F/V excess = -0.0076323
  one-mode ansatz (F), D4 power 1.0000, 24/24 modes, psi-bar conserved to ~1e-16.
- C2.2 [Track E] Discretization error in <A>, D4 power, Fexc decreases with N and dt
  along the ladder N in {8,12,16,20} x dt in {0.02,0.01,0.005,0.0025}, with a
  measurable convergence order (Richardson fit where monotone).
- C2.3 [Track E] Input error (seed-to-seed spread over 5 seeds; psi-bar +/-0.01;
  $q0^{2} +/-0.1)$ is quantified separately and compared with the discretization error
  at reference resolution.
- C2.4 [Track E] Model-form error is quantified separately: (a) one-mode ansatz vs
  full-field relaxation F/V gap (~1.25% manuscript value, re-measured); (b) Model B
  semi-implicit vs damped-wave RK4 scheme difference on the same seeded attractor;
  (c) sim$6 (q0^{2}=8.0, L=\pi)$ vs sim$7 (q0^{2}=7.5, L=2\pi)$ setup difference.
- C2.5 [Track F] CFL bound respected: all dt used are << (sqrt(3)/2)*a0/c with
  a0 = 2*pi/q0; Model B psi-bar conservation achieved at the 1e-16 level in the
  reference run (reported as measured, not assumed).

## Prediction register (frozen before viewing validation results)

- P1: At psi-bar = 0.00, $q0^{2} = 8.0$, triads on, noise quench reaches a sub-pattern
  (<=12 modes), NOT 24/24. (Manuscript §II.7: 6-mode sub-pattern lower F at psi-bar=0.)
- P2: At psi-bar = -0.18, $q0^{2} = 7.5 ($detuned), noise quench reaches NO ordered
  24-mode state (ordered branch vanishes at $r_{shell} = -0.10)$.
- P3: At psi-bar = -0.18, $q0^{2} = 8.0$, triads off (u=0), noise quench D4 shell
  fraction < 0.35 (control value 21.1% in the independent reproduction).
- P4: Attractor <A> error vs A* decreases with dt at fixed N=16 (dt ladder
  0.02 -> 0.0025), monotone within seed noise.
- P5: Model B psi-bar drift |psi-bar_final - psi-bar_0| < 1e-12 at every ladder
  point (conservation is a scheme property, not a resolution property).

## Assumption ledger (task-level)

- A1: The sim6/sim7 integrators are faithful implementations of the manuscript
  dynamics (semi-implicit spectral Model B; semi-implicit damped wave; RK4 damped
  wave). Provenance: repo verification/ (FINAL_AUDIT: II.8 reproduced, II.6 partial).
- A2: N=16, L=pi, $q0^{2}=8.0$ is the reference configuration (only the D4 shell
  linearly unstable). Provenance: sim6 docstring + FINAL_AUDIT §II.8.
- A3: The 6-mode sub-pattern reached in noise quenches is identified by its occupied
  modes as measured, NOT assumed to be the manuscript's "hexagonal" pattern: the
  manuscript does not specify which 6 modes. Any (N,T,Q) computed for the observed
  subset is POST-HOC (selected after inspection) and graded D as a prediction.
- A4: The static account is formalized as the imposed interference pattern
  Psi(x) = sum_g cos(g.x) with amplitude from the one-mode ansatz at the same
  parameters. This is the most charitable static formalization available: it grants
  the static account the Landau functional it did not possess in v92. Any divergence
  found under this charitable reading is therefore a strong divergence.
- A5: Hoy [40] LJ-MD result is taken as manuscript-reported (not re-simulated:
  4D particle MD is out of local scope; costed as NOT RUN, not as failed).

## Choice ledger

- Grid ladder N in {8,12,16,20}: smallest grid holding the shell (N=8) to one step
  past reference (N=20). N=24 not run: cost/benefit (see cost note in report).
- dt ladder {0.02,0.01,0.005,0.0025}: factor-2 refinement around the reference 0.005.
- Physical time fixed at T=30 (attractor) / T=50 (quench) across the ladder, so
  refinement changes resolution, not evolution time.
- Quench filter K2<64 (RK4 stability) and attractor filter K2<200 retained exactly
  as in sim6; changing them would change the model, not the resolution.
- Seeds 1..5 for input-error spread; seed 1 is the sim6/sim7 reference seed.
