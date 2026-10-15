# IX.1 — Tractable Computation: Research Brief

**Paper:** §IX.1. **Character:** specified computations requiring no new physics.
These are the lowest-risk, highest-executability items in the register — each has a
well-posed numerical answer.

## 1.1 Larger-volume simulation: single-crystal ordering and phase-locking convergence

**The problem.** The §II.6 runs were on a $16^4$ periodic grid (two pattern periods
per direction). The independent reproduction reached 89.5% D₄ spectral power under
annealing and was *still increasing* at step 14000 — the run ended before
convergence. Prediction VI.1 (triad phase locking, $\phi_1+\phi_2+\phi_3=0 \bmod
2\pi$) measured an order parameter of 0.26 against a maximum of 1 — "real but
incomplete locking, consistent with a defected state in a small box."

**Attack routes.**
- Rerun the §II.6 protocol on $24^4$ and $32^4$ grids (three and four pattern
  periods per direction). Track: D₄ spectral power vs. annealing step,
  single-crystal vs. poly-crystal final states, triad phase-locking order
  parameter.
- **Baseline:** `verification/sim7_fairtest.py` — the v93.0
  fair-test implementation (D₄ 77.1% direct quench, 89.5% annealed and still
  rising at step 14000; control 21% vs 79%). Extend it; do not reimplement
  from scratch. Keep its parameter conventions ($L=2\pi$, $q_0^2=7.5$).
- Pass criterion (from VI.1): phase locking "should drive toward unity" in larger
  volume. If it saturates well below 1, the locking claim weakens and the defect
  density becomes the story.
- Cost estimate: the $16^4$ annealed run was 14000 steps; $32^4$ is 16× the
  modes. Pseudo-spectral cost scales as $N^4 \log N$. This is a Colab-Pro-class
  job, not a laptop job.

**Done looks like:** a volume-scaling curve of final D₄ power fraction and
locking order parameter, with error bars over seeds, published as a direct test
of VI.1.

## 1.2 Nucleation barrier height and critical droplet size

**The problem.** §II.9: at $\bar\psi=-0.18$, $r_{\mathrm{eff}}=+0.107>0$ — the
disordered state is linearly stable, so the D₄ state must be nucleated across a
barrier. Neither the barrier height nor the critical droplet size was computed.
This is also the computational half of open question 5.2 (what supplies the
nucleation event).

**Attack routes.**
- Construct the critical droplet by constrained minimization: seed a D₄-ordered
  ball of radius $R$ in a disordered background, relax under conserved (Model B)
  dynamics, and find the $R$ at which the droplet grows rather than collapses.
  Barrier height = free-energy difference at the critical radius.
- **Seeded-state protocol:** `verification/sim6_units.py` — the
  II.8 implementation (seed all 24 modes in phase at $A^*=0.0776$,
  $\bar\psi=-0.18$, $L=\pi$, $q_0^2=8.0$; Model B holds to four significant
  figures). Start droplet runs from this protocol. Note the unit convention:
  $q_0^2=8.0$ requires $L=\pi$ (see `verification/README.md`).
- Vary $\bar\psi$ across the band ($-0.33 \lesssim \bar\psi \lesssim 0.03$) and map
  barrier height vs. position in the band; near the linearly-unstable edge
  ($\bar\psi \approx -0.10$) the barrier should vanish — check.
- Analytical complement: thin-wall estimate from the Landau functional
  ($N=24$, $T=192$, $Q=3384$ coefficients) as a cross-check on the numerics.

**Done looks like:** barrier height $\Delta F(R_c)$ and critical radius $R_c$ as
functions of $\bar\psi$, with a thin-wall cross-check. Feeds directly into the
cosmological nucleation narrative (5.2).

## 1.3 D₄ band under simultaneous detuning and higher-order terms

**The problem.** The 11.85% band figure (§II.7) is conditional twice over: it
assumes $q_0$ tuned exactly onto the D₄ shell (a detuning of 0.5 in $q_0^2$
destroys the ordered branch entirely), and it was computed at $w_6=0$ (adding
sixth-order terms narrows the band 11.90% → 8.47% at $w_6=0.2$). The joint
effect — detuning *and* $w_6>0$ simultaneously — was not mapped.

**Attack routes.**
- Two-parameter scan: $(q_0^2 - 8)$ detuning × $w_6$, recomputing the ordered
  branch and band fraction at each point. The paper's §II.7 table gives the
  single-parameter endpoints; fill the interior.
- Question to answer: is there a finite region where the band survives both, or
  does the tuning requirement become effectively measure-zero once $w_6$ is
  physical? This determines whether the "conditional on $q_0$ tuning"
  qualification is mild or fatal.

**Done looks like:** a 2D band-fraction map; a stated verdict on how much tuning
the framework actually requires.

## 1.4 Defect homotopy beyond elementary Burgers vectors

**The problem.** §V.1 classifies elementary defects: dislocation sheets
($\pi_1=\mathbb{Z}^4$, Burgers vectors in D₄), no line defects ($\pi_2=0$),
integer-charged point solitons ($\pi_3=\mathbb{Z}$). Composite and bound defect
configurations were not worked out.

**Attack routes.**
- Enumerate low-energy defect composites: dislocation junctions (Burgers vector
  addition in D₄), point-soliton–dislocation bound states, soliton–antisoliton
  pairs.
- The point group is $W(F_4)$ of order 1152 — use it to classify defect
  orientations, not just charges.
- Physical target: which composites are stable, and do any carry quantum numbers
  suggestive of particle identification? (Careful: this is exploration, not a
  claim — label accordingly.)

**Done looks like:** a defect composite catalog with stability analysis; explicit
statement of which composites exist and which are forbidden.

## 1.5 Projection of D₄ to three dimensions along irrational directions

**The problem.** §II.10 shows $D_4 \cap \{x_4=0\} = D_3$ = FCC. Projection (not
cross-section) along irrational directions gives quasiperiodic 3D structures —
the 4D→3D analog of cut-and-project quasicrystals.

**Attack routes.**
- Compute the projected point sets for a sample of irrational directions;
  characterize diffraction (Bragg spectra) and local isomorphism classes.
- Question: does any projection direction yield a 3D pattern with distinguished
  physical relevance (e.g., icosahedral symmetry — the 3D quasicrystal story)?
- This is the cleanest mathematical item in IX.1; it may also constrain reading
  (B) of the dimensional assignment (2.1).

**Done looks like:** classification of projected structures by direction;
diffraction signatures; a stated verdict on physical relevance vs. mathematical
curiosity.

## Cross-links

- 1.2 → 5.2 (nucleation event); 1.1 → VI.1 test; 1.3 → the tuning debate around
  5.1; 1.5 → 2.1 (dimensional assignment).
