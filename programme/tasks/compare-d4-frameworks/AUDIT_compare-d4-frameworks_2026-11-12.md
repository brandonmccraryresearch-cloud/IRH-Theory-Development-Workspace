# Claim-by-claim audit — "Compare $D_{4}$ Selection Frameworks" (16th Co-scientist task)

**Date:** 2026-11-12. **Auditors:** three parallel file auditors (one per file) + coordinator's own independent checks.
**Grade key:** HLRE v5.1. Track E = comparative/textual claims (cap C, I1 here); Track F = exact-computation claims
(F3 single-route, F2 two-route — F2 is **not** claimed anywhere in this audit, see §5.4).
I-levels: I1 = single artificial pipeline unless stated otherwise.
**Rule applied throughout:** a Co-scientist summary is not verification. Nothing in these files upgrades any IRH grade.

## §0. Files audited

| File | Lines | md5 (verified) |
|---|---|---|
| `compare-d4-frameworks/framework-matrix.md` | 81 | `1b4c5388db42f831ee24ccb2e5aea070` |
| `compare-d4-frameworks/gap-memo.md` | 98 | `6b5a91a08038a1f7af997847809c815a` |
| `compare-d4-frameworks/verification-audit.md` | 66 | `726a851d1887f8330e1499294ea80d75` |

**Audited against:** manuscript text `IRH_v93_1_source_rebuilt.txt` (1,638 lines);
D4 package guide `SUMMARY_AND_REPLICATION_GUIDE.md`; consolidated summary
`CONSOLIDATED_SUMMARY_2026-11-12.md`; gap inventory `IRH_GAP_INVENTORY_2026-11-12.md`
(esp. G-E1, G-C14, G-A5); Hark replication audit review `HARK_REPLICATION_AUDIT_REVIEW.md`.
External sources re-checked where stated (arXiv full texts for S2/S6/S8, AMOLF abstract for S3,
van Meel and Cohn abstracts for S7/S9; live Zenodo API for record 22821689).
**No files written by the auditors, no GCP spend, no heavy simulations, no Academia launches, no contact.**

## §0.1 Scoreboard (189 claims total)

| File | Claims | VERIFIED | CORRECTED | REFUTED | ABSTAIN |
|---|---:|---:|---:|---:|---:|
| framework-matrix.md | 88 | 82 | 0 | 0 | 6 |
| gap-memo.md | 64 | 62 | 2 | 0 | 0 |
| verification-audit.md | 37 | 22 | 5 | 0 | 10 |
| **Total** | **189** | **166** | **7** | **0** | **16** |

**Headline:** no claim in any of the three files is REFUTED. No IRH grade moves on the strength of these
files. The load-bearing numbers $(D_{4}$/BCC triad/quartet counts, S = 64/141, margin 73/423) are exact and
were re-derived independently three times over (coordinator + two auditors, exact rational arithmetic).
The file set is unusually careful: every evidence label (M/F/A/R/U) is stated where it applies, and the
limitations it admits are genuine. The corrections are provenance, citation-placement, and staleness
items — not numerical errors.

## §1. Coordinator's own independent checks

### §1.1 Exact enumeration (conda env, exact `Fraction` arithmetic)

Roots $\pme_{i}\pme_{j}$, i<j; C(s) = multiplicity of ordered pair sums; $T = \Sigma_{c} C(-c)$; $Q = \Sigma_{s} C(s)C(-s)$;
$\tau^{2} = T^{2}/N^{3}$, $q_{4} = Q/N^{2}$, $S = T^{2}/($NQ). Run by the coordinator from the definitions:

| Star | N | T | Q | $\tau^{2}$ | $q_{4}$ | S |
|---|---:|---:|---:|---:|---:|---:|
| BCC reciprocal star (3D) | 12 | 48 | 540 | 4/3 | 15/4 | 16/45 |
| $D_{4}$ root star (4D) | 24 | 192 | 3384 | 8/3 | 47/8 | **64/141** |

Margin over $A_{4}* (12/31)$: (64/141)/$(12/31) - 1 = **73/423 \approx 17.26$%**, exact. Matches the manuscript
tables (rebuild lines 377, 387–388, 413–417) and both auditors' independent re-runs. The matrix
auditor additionally recomputed $A_{4}* (T=120, Q=1860, S=12/31$ via the \$20 $A_{4}$\$ roots), $A_{4} (S=0)$,
$\mathbb{Z}^{4} (S=0)$, FCC (S=0), SC (S=0) — all matching the manuscript table. So the $A_{4}$* score, which the
verification-audit file itself did **not** re-derive, is now independently re-derived by the matrix auditor.

### §1.2 Source email date — VERIFIED by direct Gmail lookup

The "Co-scientist finished" email for this task is message `1a1c2a6dead2cefa`, from Academia Co-scientist
<updates@academia-mail.com>, subject "Co-scientist finished: Compare $D_{4}$ Selection Frameworks",
sent **Mon, 9 Nov 2026 23:31:17 +0000 = 2026-11-09 17:31:17 CST**. The task finished overnight Nov $9\to10$;
the email is Nov 9. See the closing note (§6) for the G-E1 record correction.

### §1.3 Manuscript spot-checks (coordinator)

- N=648 appears in the manuscript at the Hoy context (line 433: "choice N = 648 promotes $a 3\times3\times3\times3$-cell
  $D_{4}$ single crystal") — the juxtaposition the memo corrects. No "$1\times10^{5}$" / "100,000" anywhere in the
  1,638-line rebuild (see §5.3 — the brief's premise was wrong, not the memo's).
- Annealed run populated only 6 of 24 modes (line 499) ✓; phase-locking 0.26 (line 1104) ✓;
  11.85% band (line 528), with the 11.85/11.90 inconsistency flagged in the source itself (lines 88–96) ✓.
- Hoy reference [40] at line 1621 ✓; $r=-0.35$, u=v=1, $\gamma=1.2$, dt=0.05, 6,000 steps (line 478) ✓.

## §2. `framework-matrix.md` — 88 claims: 82 VERIFIED, 0 CORRECTED, 0 REFUTED, 6 ABSTAIN

Grades: C = Track E, I1 (comparative/manuscript-attribution claims); F3 = Track F, I1 (exact-computation
claims as audited here — a two-route F2 reading exists but is **not** claimed, pending the open G-C17
decision). "M/F/A/R/U" are the file's own evidence labels.

### §2.1 Header / scope

| # | Claim | Verdict | Grade | Evidence |
|---|---|---|---|---|
| 1 | Scope: weak-crystallization, pattern-forming field dynamics, particle crystallization, geometric optimization — the families implicated by v93.1, not competing end-to-end theories | VERIFIED | C | All four families cited in the manuscript (refs [1],[2],[4],[13],[14],[39],[40],[44],[45]) |
| 2 | "Prepared 9 November 2026" | ABSTAIN | — | Provenance only; consistent with "finished overnight 2026-11-10" but not independently confirmable from any local record |
| 3 | Main conclusion: IRH's selection argument belongs to the Alexander–McTague/Landau density-wave family, with a Swift–Hohenberg spectral operator and explicit dynamical tests | VERIFIED | C | Manuscript §§II.3–6 (SH operator $(q_{0}^{2}+\nabla^{2})^{2}$, §I.2 line 194; Landau expansion §II.3) |
| 4 | "Particle simulations support the accessibility of $D_{4}$ under particular interactions; geometric theorems constrain its structure. Neither independently validates the complete interference-substrate mechanism." | VERIFIED | C | Hoy (F7) and de Laat/Cohn (F9/F10) support the two halves; negative half corroborated by WS-A/C (0/5 and 0/6 noise quenches reach 24/24) |

### §2.2 Matrix A

**F1 — IRH equal-shell selection**

| # | Claim | Verdict | Grade | Evidence |
|---|---|---|---|---|
| 5 | Real scalar; single resonant shell; equal amplitudes; local cubic/quartic functional; $B=A\sqrt{N}$, $\tau=T/N$^(3/2), $q_{4}=Q/N^{2}$; $r_{c}=(2u^{2}/9v)\tau^{2}/q_{4}$ | VERIFIED | C | Manuscript §II.3 lines 313–355 verbatim, including the $r_{c}$ derivation |
| 6 | Enumerated reciprocal stars of $D_{4}$, $A_{4}$*, $\mathbb{Z}^{4}$, $A_{4}$; 3D BCC/FCC/SC controls | VERIFIED | C | Manuscript tables lines 364, 387–390; auditor's recomputation confirms all seven stars |
| 7 | "Tests C1–2: onset ranking within this ansatz and candidate set, not global selection among all fields" | VERIFIED | C | Correct scope limitation; consistent with Hark F6 (C6 graded D as presented, restricted competitor set) |

**F2 — IRH interference dynamics**

| # | Claim | Verdict | Grade | Evidence |
|---|---|---|---|---|
| 8 | Damped-wave equation driven by Swift–Hohenberg free energy; separate conserved Model B tests; cubic on/off; direct quench and annealing; seeded full-state relaxation | VERIFIED | C | Manuscript §§II.6–II.8; damped-wave/Model B separation correctly stated (cf. Hark B1 — the matrix does not repeat the manuscript's §I.2 inconsistency) |
| 9 | $16^{4}$ periodic field; $L=2\pi$; $D_{4}$ star \|k\|${}^{2}=8$ vs triad-free \|k\|${}^{2}=7$ shell; both penalized equally at $q_{0}^{2}=7.5$ | VERIFIED | C | Manuscript §II.6 lines 456–483 (penalties both 0.25, 24 vs 64 modes) |
| 10 | Full-state test tunes $q_{0}$ onto the $D_{4}$ shell and sets mean $\bar{\psi}=-0.18$ | VERIFIED | C | Manuscript §II.8 (~line \$571: r=-0.35, $\bar{\psi}=-0.18, q_{0}$\$ tuned) |
| 11 | "C3–5: shell capture, within-shell symmetry and persistence are distinct endpoints. Damped-wave and conserved-gradient-flow trajectories must not be conflated." | VERIFIED | C | Correct methodological distinction; WS-C measured exactly this divergence (wave drifts $\bar{\psi}\to+0.0025$, Model B conserves it) |

**F3 — Alexander–McTague**

| # | Claim | Verdict | Grade | Evidence |
|---|---|---|---|---|
| 12 | Landau expansion about uniform liquid; nonzero critical wavenumber; cubic invariants from closed triangles; weak ordering | VERIFIED | C | Manuscript-grounded (§II.4); independent full-text check ABSTAIN (file itself says the source was not full-text audited here) |
| 13 | "Density-wave geometry, not measured training data" | VERIFIED | C | Characterization, consistent with the paper's analytic character |
| 14 | "Tests C2: near-transition preference for BCC in 3D; a limiting-case baseline for IRH" | VERIFIED | C | Manuscript §II.4 lines 364–373 |

**F4 — higher-dimensional Landau (Elitzur et al.)**

| # | Claim | Verdict | Grade | Evidence |
|---|---|---|---|---|
| 15 | Scalar order parameter; isotropic nonzero-q instability; equal-amplitude shell; cubic triangle counting over regular convex polytopes in flat noncompact dimensions; quartic stabilizes amplitude | VERIFIED | C | arXiv:1101.1631v1 §§2–3, read in full: $\Phi_{3}$ from equilateral triangles, $\Phi_{4}$ stabilization, "flat non compact dimensions" |
| 16 | Analytic edge/triangle counts; explicit 4D special-case comparison | VERIFIED | C | Same source, eqs. (6)–(8) and the 4D "direct check" (lines 143–144) |
| 17 | "Direct prior art for a 4D cross-polytope edge-star preference. Restricted candidate class, no time integration." | VERIFIED | C | Same source: "the cross-polytope, called a 16-cell in four dimensions, is preferred"; no dynamics in the paper |

**F5 — Groh & Mulder counterbaseline**

| # | Claim | Verdict | Grade | Evidence |
|---|---|---|---|---|
| 18 | Reconsider liquid–solid spinodal with density-functional theory; additional accessible density-wave structures; nonperturbative free-energy behavior | VERIFIED | C | AMOLF institutional summary (ir.amolf.nl/pub/5083), read by auditor: "many other solid structures also are simultaneously accessible, among them the fcc structure" |
| 19 | Analytic argument and explicit "Onsager solid" toy-model calculations | VERIFIED | C | Same abstract: "explicit calculations on a toy model, the 'Onsager solid'" |
| 20 | "Tests C2/5: whether near-spinodal BCC preference determines the ultimately stable phase" | VERIFIED | C | Same abstract: ultimately stable phase is FCC, "dictated by properties of the free energy that cannot be obtained perturbatively starting from the spinodal point" |

**F6 — Swift–Hohenberg / Model A–B**

| # | Claim | Verdict | Grade | Evidence |
|---|---|---|---|---|
| 21 | Finite-wavenumber pattern formation; nonconserved vs conserved order-parameter dynamics; operators/classifications, not independent $D_{4}$ selectors | VERIFIED | C | Manuscript refs [2],[4]; standard classification |
| 22 | "Scalar field modes; analytical dynamical classifications" | VERIFIED | C | Framing, consistent with S4/S5 |
| 23 | "Tests C4–5: spectral selection and conservation constraints; $D_{4}$ requires added nonlinear geometry and appropriate conditions" | VERIFIED | C | Correct; nothing in S4/S5 selects $D_{4}$ |

**F7 — Lennard-Jones vs WCA (Hoy)**

| # | Claim | Verdict | Grade | Evidence |
|---|---|---|---|---|
| 24 | 4D Newtonian particles; shifted/truncated pair potential; attractive LJ vs repulsive WCA; periodic hypercubic boxes; LJ NPT at zero pressure; WCA NVT at matched pre-nucleation density/temperature | VERIFIED | C | Hoy arXiv:2311.03465v1 Methods/Results, read in full (L107–124, L171–172) |
| 25 | 500,000 particles; dt=$\tau/125$; LJ cutoff $2.5\sigma$, WCA cutoff 2^$(1/6)\sigma$; energy, density, g(r), bond-order correlations | VERIFIED | C | Same source (L109–113, L120–127, L138–149) |
| 26 | "Tests C3–5: physically simulated nucleation into $D_{4}$ under specific interactions; not the scalar field's cubic-term mechanism" | VERIFIED | C | Correct scope; same source |

**F8 — hard-sphere frustration (van Meel et al.)**

| # | Claim | Verdict | Grade | Evidence |
|---|---|---|---|---|
| 27 | 4D excluded-volume particles; distinguish local dense-cluster compatibility from actual liquid polytetrahedral structure and nucleation cost | VERIFIED | C | van Meel et al. abstract (arXiv:0809.1775), read by auditor |
| 28 | Computational hard-sphere freezing study, compared with 3D behavior | VERIFIED | C | Same abstract: "computational study of freezing of 4d hard spheres" |
| 29 | "Tests C4–5: why geometrically compatible local clusters do not guarantee easy crystallization" | VERIFIED | C | Same abstract: "crystal nucleation in 4d is less facile than in \$3d\dots\$ geometrical frustration of polytetrahedral structures" |

**F9 — spherical code / kissing (de Laat et al.)**

| # | Claim | Verdict | Grade | Evidence |
|---|---|---|---|---|
| 30 | 24 unit vectors on $S^{3}$; minimum angle $\pi/3$; second-level Lasserre SDP hierarchy; exact feasibility certificate | VERIFIED | C | de Laat et al. arXiv:2404.18794v2 abstract + §1, read by auditor ("second level of the Lasserre hierarchy$\dots$ exact optimal solution") |
| 31 | Rational SDP certificate; invariant polynomial matrices; rigorous positivity checks | VERIFIED | C | Abstract/§5 per companion audit; auditor did not re-derive the certificate, and the file does not claim to have done so either |
| 32 | "Tests C1/C7: unique optimal kissing configuration up to isometry, not a dynamical attractor or universal energy minimum" | VERIFIED | C | Same source abstract: "unique optimal kissing configuration$\dots$ up to isometry" and "optimal spherical code"; negative half is correct scope (no dynamics in the paper) |

**F10 — potential-dependent optimality counterexample (Cohn et al.)**

| # | Claim | Verdict | Grade | Evidence |
|---|---|---|---|---|
| 33 | Pair-energy optimization for points on $S^{3}$; vary absolutely monotonic inner-product potentials (equivalently completely monotonic squared-distance formulation) | VERIFIED | C | Cohn et al. abstract (arXiv:math/0607447): "not a universally optimal spherical code"; manuscript §II.11 (Bernstein's theorem spans the completely-monotonic class) |
| 34 | Mathematical construction and numerical exploration of deformed 24-point designs | VERIFIED | C | Same abstract: "numerical computations suggesting that every 5-design$\dots$ is in a 3-parameter family$\dots$ of deformations of the $D_{4}$ root system" |
| 35 | "Tests C5/C7: whether $D_{4}$ minimizes every potential in that class. Spherical-code problem, not automatically an infinite-lattice energy problem." | VERIFIED | C | Correct scope; manuscript §II.11 draws the same distinction |

### §2.3 Matrix B

**F1**

| # | Claim | Verdict | Grade | Evidence |
|---|---|---|---|---|
| 36 | $D_{4} S=64/141=0.453901$; $A_{4}* 12/31=0.387097$; $\mathbb{Z}^{4}$ and $A_{4}$ zero; relative advantage 73/423=17.26%; BCC S=16/45 | VERIFIED | F3 | Auditor's independent recomputation (all counts, all scores); see §1.1. F2 not claimed — see §5.4 |
| 37 | "M+R for $D_{4}$/BCC counts and score; $A_{4}$* score checked against manuscript page image" | VERIFIED | F3 | Manuscript table lines 387–390; auditor's recomputation of $A_{4}* (T=120, Q=1860)$ is stronger than the file's image check |
| 38 | "SymPy/enumeration reported. Scientific implementation absent from inspected Zenodo archive; see audit." | VERIFIED | C | Companion audit §2 (ZIP inventory: PDF/TeX/Markdown, references, 10 PNGs, `md2tex.py` only) |
| 39 | Gaps: non-equal amplitudes, additional shells, non-Bravais and quasiperiodic candidates; "zero cubic score means exclusion from this cubic first-order route, not impossibility of ordering" | VERIFIED | C | Correct scope reading; matches manuscript lines 407–408 and gap-memo §2 |

**F2**

| # | Claim | Verdict | Grade | Evidence |
|---|---|---|---|---|
| 40 | Author: $D_{4}$ shell power 84% direct, 100% annealed; cubic-off 44% | VERIFIED | C | Manuscript §II.6 lines 486–487 |
| 41 | Manuscript-reported independent implementation: 77.1%, 89.5%, cubic-off 21.1% | VERIFIED | C | Manuscript §II.6 lines 491–492 and §VI.1 lines 1143–1146 |
| 42 | "Earlier noise starts occupy only 6/12 modes" | VERIFIED | C | Manuscript §II.7–II.8 ("only 6 of 24 modes"; "reached only a 6- or 12-mode sub-pattern") |
| 43 | Seeded full state relaxes to excess $F/V=-0.0077276$ | VERIFIED | C | Manuscript §II.8 table (relaxed field $-0.0077276)$ and line 40 |
| 44 | Phase-locking parameter 0.26/1 | VERIFIED | C | Manuscript §VI.1 line 1104 ("0.26 against a maximum of 1") |
| 45 | §II.\$6: r=-0.35$, u=v=1, $$\gamma=1.2$$, dt=0.05, 6,000 steps; annealing 14,000 steps from $r=-0.05\$ to $-0.45$ | VERIFIED | C | Manuscript §II.6 lines 476–480 verbatim |
| 46 | "Conserved scheme details not executable from inspected package. U for rerunning simulations/Lean." | VERIFIED | C | Companion audit §2/§5; honest U-label; WS-C used repo `verification/sim6/sim7`, not the Zenodo deposit |
| 47 | Gaps: "Shell power alone cannot establish 24-mode symmetry. Mean-field band and $q_{0}$ tuning required. Need perturbed full-state basin tests, unbiased nucleation statistics, resolution/volume/box-shape convergence." | VERIFIED | C | Correct; now partly answered after the fact by Hark F1 (perturbed hex6/fcc$12 \to$ full24, 5/5 and 4/4), which strengthens rather than contradicts the caution. The matrix predates WS-A task 5 (Nov 9 vs Nov 10), so the "need" is a snapshot, not a contradiction |

**F3**

| # | Claim | Verdict | Grade | Evidence |
|---|---|---|---|---|
| 48 | "Near-melting BCC preference; recovered by F1. M; foundational source not independently full-text audited here." | VERIFIED | C | Manuscript §II.4; honest limitation stated in the file |
| 49 | "Valid near transition; not a general ground-state or kinetic theorem." | VERIFIED | C | Manuscript §II.4 scope nuance + Groh–Mulder (F5) |

**F4**

| # | Claim | Verdict | Grade | Evidence |
|---|---|---|---|---|
| 50 | "Cross-polytope wins the considered regular-polytope comparison, including the 4D 16-cell. Edge wavevectors have form $\pme_{i}\pme_{j}$: the 24-vector $D_{4}$ star at d=4." | VERIFIED | F3 (count), C (comparison) | Elitzur §§3–4 (lines 143–144, eq. 9) plus auditor's enumeration (24 vectors) |
| 51 | "Equations and combinatorial construction available in full text; executable code not inspected." | VERIFIED | C | True of the arXiv HTML read by the auditor; honest limitation |
| 52 | Gaps: "Shares the Landau/cubic-invariant foundation with IRH. Separate exact quartet ranking and kinetic evidence from claims of mechanism-level independence. Compactness, irregular/nonconvex structures explicitly left open." | VERIFIED | C | Elitzur §4 explicitly leaves compact dimensions and nonconvex/irregular configurations open (lines 167–170); independence caution matches WS-C C1.6's split verdict and gap-memo §2 |

**F5**

| # | Claim | Verdict | Grade | Evidence |
|---|---|---|---|---|
| 53 | "FCC and other structures accessible at spinodal; unstable BCC branch still has lowest near-spinodal free energy, but toy-model stable phase can be FCC." | VERIFIED | C | AMOLF abstract, read by auditor (lines 6–11 of that page) |
| 54 | "Institutional abstract checked; full calculations/code not audited." | VERIFIED | C | Honest limitation, accurately stated |
| 55 | "Direct caution against equating 'orders first' with 'globally stable at arbitrary quench.' No 4D quantitative comparison established here." | VERIFIED | C | Correct inference from F5; properly scoped |

**F6**

| # | Claim | Verdict | Grade | Evidence |
|---|---|---|---|---|
| 56 | "IRH reports conserved mean preservation to $8.3\times10^{-17}$ versus drift under Model A; generic ingredient papers do not report IRH'$s D_{4}$ selection metrics." | VERIFIED | C | Manuscript lines 216–217 (Model A drift $1.8\times10^{-1}$; Model B preserved to $8.3\times10^{-17})$. Caveat carried: WS-C G-B1 — the $8.3\times10^{-17}$ value itself is not re-measured at full precision (best $1.1\times10^{-15})$; the file reports it as M (manuscript-reported), which is correct |
| 57 | "Foundational references from manuscript; implementations not inspected." | VERIFIED | C | Honest limitation |
| 58 | Gaps: "Derive one primary evolution law or explicitly compare them. Linear implicitness alone does not establish unconditional stability of explicit nonlinear terms." | VERIFIED | C | Correct; same point as gap-memo G5, and it correctly withholds assent from the manuscript's §II.6 "unconditionally stable" phrasing (which rests on the linear operator being treated implicitly) |

**F7**

| # | Claim | Verdict | Grade | Evidence |
|---|---|---|---|---|
| 59 | "LJ crystallizes around 0.59<T<0.63 within ~$2\times10^{4}\tau$; matched WCA does not within $2.5\times10^{5}\tau$." | VERIFIED | C | Hoy abstract + Results (L11–15, L160–172) |
| 60 | "$D_{4}$ identified using coordination tending to 24; representative $Z\approx23.81$ and 99.2% high-bond-order pairs after crystallization." | VERIFIED | C | Hoy L189–$193 (Z\approx23.81, Z\to24$ rules out $A_{4})$ and L231 (99.2%) |
| 61 | "Paper names hdMD, citing Hoy & Interiano-Alberto (2022). Code/input decks and trajectories not inspected." | VERIFIED | C | Hoy L107 ("performed using hdMD [30]"); honest limitation on code |
| 62 | The 2022 implementation reference's full bibliographic details (Phys. Rev. E 105, 055305) | ABSTAIN | — | Hoy ref [30] was not individually opened by the auditor; the file's citation is as-cited-in-S6 |
| 63 | Gaps: "Same $D_{4}$ endpoint supports compatibility, not IRH causality. Attractions matter. Source distinguishes its large systems from older 648-particle finite-size concerns." | VERIFIED | C | Hoy L55–57 and L168–169 (648-atom system was Skoge et al., a possible finite-size artifact; Hoy'$s N=5\times10^{5}$ removes that concern). **This corrects the manuscript**: manuscript §II.5 lines 431–433 places "the choice N=648 promotes $a 3\times3\times3\times3$-cell $D_{4}$ single crystal" beside Hoy's result; the 648 figure is not Hoy's (gap-memo §2 flags the same conflation) |

**F8**

| # | Claim | Verdict | Grade | Evidence |
|---|---|---|---|---|
| 64 | "4D nucleation less facile than 3D despite local dense-cluster/crystal compatibility; polytetrahedral frustration implicated." | VERIFIED | C | van Meel abstract, read by auditor (L33–35) |
| 65 | "Abstract checked; full protocol and scientific code not inspected." | VERIFIED | C | Honest limitation |
| 66 | "Local $D_{4}$ geometry insufficient to predict kinetic reachability; interaction-dependent comparison with F7 required." | VERIFIED | C | Correct inference, consistent with F7/F8 together |

**F9**

| # | Claim | Verdict | Grade | Evidence |
|---|---|---|---|---|
| 67 | "Exact kissing bound 24; unique optimal configuration up to isometry. Degree parameters $d_{1}=14$, $d_{2}=\delta=16$; reported numerical solve ~2 weeks on 8 cores/128 GB, followed by exact rounding and verification." | VERIFIED in part | C | Abstract (unique optimal, exact solution) plus: $d_{1}=14$ confirmed (paper: zonal matrices with \|$\lambda$\|$\leq14, L196)$; "about two weeks on 8 cores$\dots$ equipped with 128 GB" confirmed verbatim (L1408–1409). The $d_{2}=\delta=16$ parameter is split out as #68 |
| 68 | Degree parameter $d_{2}=\delta=16$ | ABSTAIN | — | Not located in the portion of the de Laat paper the auditor read (§§1, 5.1 region, compute paragraph); plausibly a §5 truncation parameter, but not verified. Not load-bearing for any conclusion |
| 69 | "Julia/Nemo scripts and data explicitly linked by paper; link target and code execution not audited." | VERIFIED | C | de Laat L1437–1438 ("scripts are written in Julia$\dots$ use the Nemo computer algebra system"); honest limitation |
| 70 | "Objective is angular separation; no time scale, nucleation or field equation. Does not prove densest unrestricted 4D packing or universal pair-energy optimality." | VERIFIED | C | Correct scope; the paper's own §1 contrasts kissing optimality with Cohn et al.'s non-universal-optimality |

**F10**

| # | Claim | Verdict | Grade | Evidence |
|---|---|---|---|---|
| 71 | "$D_{4}$ is not universally optimal as a 24-point spherical code." | VERIFIED | C | Cohn et al. abstract, read by auditor: "We prove that the $D_{4}$ root system$\dots$ is not a universally optimal spherical code." |
| 72 | "arXiv abstract checked; counterexample implementation not inspected." | VERIFIED | C | Honest limitation |
| 73 | "Must specify objective and configuration space. IRH's Gaussian $\beta$-window scan remains manuscript-reported and does not by itself transfer this spherical-code theorem to infinite lattices." | VERIFIED | C | Manuscript §II.$11 (\beta\in[0.05,2.4]\cup[3.1,12]$ optimum, [2.6,3.0] window where a competitor wins by $\leq0.007$%); same scope point as gap-memo §2 |

### §2.4 Source register S0–S9 and scope limits

| # | Claim | Verdict | Grade | Evidence |
|---|---|---|---|---|
| 74 | S0: McCrary (2026), v93.1, DOI 10.5281/zenodo.22821689; supplied PDF read in full; selected tables visually checked; PDF dated September 17; Zenodo publication September 18; preprint, CC BY 4.0; Zenodo metadata and source ZIP inspected | VERIFIED | C | DOI matches the guide and manuscript; dates and ZIP contents per companion audit §2 (matrix auditor did not re-fetch the Zenodo API himself) |
| 75 | S1: Alexander & McTague (1978), title, DOI 10.1103/PhysRevLett.41.702; S0 ref. 1 | VERIFIED | C | Manuscript ref [1] (line 1539); volume/page/year corroborated by the AMOLF summary ("Phys. Rev. Lett. 41, 702 (1978)") |
| 76 | S2: Elitzur, Karni & Rabinovici (2011), title; arXiv 1101.1631; S0 ref. 45; "the extra arXiv identifier math/0607446 printed in S0 ref. 45 was not verified here; use 1101.1631" | VERIFIED | C | arXiv:1101.1631v1 read in full; manuscript ref [45] indeed prints "arXiv:1101.1631; arXiv:math/0607446"; and math/0607446 is a typo for Cohn et al.'s math/0607447 (confirmed #86) — the matrix's correction is right |
| 77 | S2 journal DOI 10.1142/S0217984911026358 | ABSTAIN | — | Not checked against the publisher |
| 78 | S3: Groh & Mulder (1999), title, DOI 10.1103/PhysRevE.59.5613; AMOLF summary checked; S0 ref. 44 | VERIFIED | C | AMOLF page gives Phys. Rev. E 59, 5613–5620 (1999); manuscript ref [44] |
| 79 | S4: Swift & Hohenberg (1977), title, DOI 10.1103/PhysRevA.15.319; S0 ref. 2; "not full-text audited here" | VERIFIED | C | Manuscript ref [2] exists (line 1541); the file's own limitation is accurate. (DOI string itself not checked against publisher — sub-item noted, bullet counted on the manuscript-grounded attribution) |
| 80 | S5: Hohenberg & Halperin (1977), title, DOI 10.1103/RevModPhys.49.435; S0 ref. 4; "not full-text audited here" | VERIFIED | C | Manuscript ref [4] exists (line 1545); same DOI caveat as #79 |
| 81 | S6: Hoy (2024 journal paper; 2023 preprint), title; arXiv 2311.03465v1; S0 ref. 40 | VERIFIED | C | Preprint read in full; manuscript ref [40] |
| 82 | S6 journal DOI 10.1103/PhysRevE.109.044604 | ABSTAIN | — | Not checked against the publisher (only the arXiv preprint was read) |
| 83 | S7: van Meel, Frenkel & Charbonneau (2009), title; abstract arXiv:0809.1775; S0 ref. 39 | VERIFIED | C | Abstract page read; manuscript ref [39] |
| 84 | S7 journal DOI 10.1103/PhysRevE.79.030201 | ABSTAIN | — | Not checked against the publisher |
| 85 | S8: de Laat, Leijenhorst & de Muinck Keizer (2024), title; arXiv 2404.18794v2; S0 ref. 14; "§5.1 supplies exact-certificate and implementation details" | VERIFIED | C | Full text read through §5; manuscript ref [14] |
| 86 | S9: Cohn, Conway, Elkies & Kumar (2007), title; abstract arXiv:math/0607447; S0 ref. 13 | VERIFIED | C | Abstract page read; manuscript ref [13] prints arXiv:math/0607447 |
| 87 | S9 journal DOI 10.1080/10586458.2007.10129008 | ABSTAIN | — | Not checked against the publisher |
| 88 | "Targeted bibliography-led evidence map, not a systematic review or citation census. No simulation trajectory, particle dataset or Lean build was reproduced." | VERIFIED | C | Accurate self-description; matches the companion audit §5 ("Not performed") |

**Matrix tally: 82 VERIFIED, 0 CORRECTED, 0 REFUTED, 6 ABSTAIN** (#2 date provenance; #62 Hoy 2022 ref details;
#\$68 $d_{2}=\delta=16$\$; #77 S2 DOI; #82 S6 DOI; #84 S7 DOI; #87 S9 DOI — the four publisher DOIs are routine
bibliographic strings, not load-bearing claims; the underlying papers were verified via arXiv/AMOLF).

## §3. `gap-memo.md` — 64 claims: 62 VERIFIED, 2 CORRECTED, 0 REFUTED, 0 ABSTAIN

Grading convention: all memo claims cap at Track E **C**, I1 (single artificial pipeline; literature
checks single-route), except the exact shell-count claim (Track F **F3**, I1). Nothing in this memo
upgrades any IRH grade — it is a gap map, not verification.

### §3.1 Header and bottom line

| # | Claim | Verdict | Grade | Evidence |
|---|---|---|---|---|
| H1 | Paper is McCrary v93.1, DOI 10.5281/zenodo.22821689 | VERIFIED | C | Verification-audit §2: Zenodo API record 22821689, open CC BY 4.0, published 18 Sep 2026. (Manuscript txt itself carries no DOI string) |
| H2 | Companion `framework-matrix.md`, framework IDs F1–F10, refs S0–S9 | VERIFIED | C | Matrix file read in full; IDs F1–F10 and S0–S9 present as stated |
| B1 | Paper is an assessable advance over the retired static formulation: specifies a finite-wave-number field functional and tests the cubic coupling's effect | VERIFIED | C | Manuscript §II.3 functional + §II.6 cubic-off control (44% vs 84%, lines 487–492). Interpretive judgement, supported |
| B2 | Author independently recovered the $D_{4}$ and 3D BCC triad/quartet counts and exact selection scores | VERIFIED | F3 | Audit §1 table: BCC N=12, T=48, Q=540, S=16/45; $D_{4} N=24$, T=192, Q=3384, S=64/141. Gap-memo auditor's recheck: (8/3)/(47/8)=64/141, margin $73/423\approx17.26$%. Note: audit states the $A_{4}$* enumeration itself was **not** rerun — the memo does not claim it was. (The matrix auditor has since re-derived $A_{4}$*; see §1.1) |
| B3 | Unresolved step is stronger: unbiased emergence of the full phase-locked 24-mode pattern, vs shell power or seeded persistence | VERIFIED | C | Manuscript §II.7/§II.8 (see G1-E1/E2) + WS-C 0/5 and WS-A 0/6 noise quenches reaching 24/24 (Summary §2/§4). Gap statement, correct |
| B4 | F1/F3/F4 address onset ranking, F2 field trajectories, F7/F8 particle nucleation, F9/F10 geometric objectives; they can agree on $D_{4}$ while testing different propositions | VERIFIED | C | Matrix A/B columns "What it actually tests" support the mapping exactly |

### §3.2 G1 — Shell capture is not full-state selection

| # | Claim | Verdict | Grade | Evidence |
|---|---|---|---|---|
| G1-E1 | §II.7: annealing populated only 6 of 24 modes | VERIFIED | C | Manuscript line 499: "The annealed run populated only 6 of 24 modes" |
| G1-E2 | §II.8: earlier noise-initialized runs reached 6- or 12-mode sub-patterns | VERIFIED | C | Manuscript line 615: "Every earlier simulation, initialized from noise, reached only a 6- or 12-mode sub-pattern." |
| G1-E3 | Full-state result starts with all 24 modes in phase at the predicted amplitude | VERIFIED | C | Manuscript §II.8: "Seeding the substrate at exactly A\* = 0.0776 with all 24 modes in phase" |
| G1-E4 | §VI.1: phase locking 0.26 against a maximum of 1 | VERIFIED | C | Manuscript line 1104: "Measured in simulation at an order parameter of 0.26 against a maximum of 1" |
| G1-I1 | Even 100% $D_{4}$-shell power does not demonstrate full $D_{4}$ symmetry | VERIFIED | C | Logic + G1-E1: the annealed run reached 100% shell power (line 487) yet populated only 6/24 modes |
| G1-I2 | "Seeded stationarity supports existence and persistence; without perturbation and basin tests it does not establish a broad attracting basin" | **CORRECTED** | C | True of the manuscript at the memo's date (9 Nov), but **stale against delivered WS-A–E**: WS-A task 5 *did* run perturbation tests — full pattern recovers from 1.0 rad RMS phase and $\pm20$% amplitude perturbations (14 runs, grade C) — and Hark F1 ran transverse tests (hex6/fcc$12 + \varepsilon \to$ full24, 5/5 + 4/4). What remains open is the *unbiased-emergence* leg (0/6 noise WS-A, 0/5 WS-C), not perturbation robustness. No contradiction; premise superseded in part |
| G1-I3 | Different implementations' power fractions are not confidence intervals or replicate-level success rates | VERIFIED | C | Manuscript lines 487–492: author 84%/100%, independent 77.1%/89.5% — single runs, no intervals stated |
| G1-T1 | "Small decisive test": random fields, 6-/12-mode seeds, symmetric 24-mode seed, perturbed full-state seeds under same conserved dynamics; record shell power, occupancy (predeclared threshold), amplitude spread, triad phase locking, excess energy separately; 20 seeds/condition screening; binomial intervals; increase replication only if useful; rotated/translated copies count as same state | **CORRECTED** | C | Design elements are sound, but the label "decisive" is overstated at n=20: a 20-seed screen gives wide binomial intervals and cannot bound a small-but-nonzero emergence rate (cf. G-A4: 0/5 is an upper bound, not a zero). Downgrade "decisive" to "screening" — which the memo itself concedes ("screening study", "increase replication only if useful") |
| G1-P1 | Pass condition: unbiased starts reproducibly reach the full state in a specified region; or explicitly restrict the claim to conditional stability and shell selection | VERIFIED | C | Appropriate pass condition; matches the G-A5 framing of the headline gap |

### §3.3 G2 — Onset-score vs dynamical competition not matched

| # | Claim | Verdict | Grade | Evidence |
|---|---|---|---|---|
| G2-E1 | F1 ranks $D_{4}$ against $A_{4}$*, $\mathbb{Z}^{4}$, $A_{4}$ | VERIFIED | C | Manuscript §II.5 table (lines ~395–\$400$): D_{4} 64/141$$, $$A_{4}* 12/31$$, $$\mathbb{Z}$^{4}/$A_{4} S=0$\$ |
| G2-E2 | §II.6 equal-linear-penalty simulation compares $D_{4}$ with the integer shell \|k\|${}^{2}=7$, triad count zero — not with nearest nonzero-score rival $A_{4}$* | VERIFIED | C | Manuscript lines 471–472 table: competitor \|k\|${}^{2}=7$, 64 modes, T=0, penalty $0.25 = D_{4}$'s 0.25 |
| G2-E3 | Torus calculation in §II.2 already assumes $\Lambda\congD_{4}$, so tests self-resonance, not unbiased lattice selection | VERIFIED | C | Manuscript §II.2: "Compactifying the substrate on the torus $\mathbb{R}^{4}/\Lambda$ with $\Lambda \cong D_{4}$ forces the allowed mode content to be the reciprocal shell." |
| G2-I1 | Cubic-off intervention is useful evidence about shell competition but does not establish a dynamical win over the strongest analytic rival | VERIFIED | C | Follows from G2-E2: the beaten competitor had T=0, so the test cannot discriminate against $A_{4}* (S=12/31)$ |
| G2-I2 | Periodic integer wavevectors constrain which competitors and orientations are representable | VERIFIED | C | Manuscript §II.6: box $L=2\pi$, k integer-valued. Hark R4 substantiates the package consequence: no $A_{4}$* simulation, no commensurate cells (G-A20) |
| G2-T1 | First compare $D_{4}/A_{4}$* amplitude equations at same mean, shell penalty, normalization; then commensurate domains or documented approximation errors; include within-shell sub-patterns and unequal amplitudes | VERIFIED | C | Sound proposal; this is exactly candidate task A20 (see §3.7) |
| G2-P1 | Pass: $D_{4}$ advantage survives the same competitor set in analysis and dynamics, with finite-box restrictions disclosed | VERIFIED | C | Appropriate pass condition |

### §3.4 G3 — Stable band is conditional, not a probability of emergence

| # | Claim | Verdict | Grade | Evidence |
|---|---|---|---|---|
| G3-E1 | §II.7: full-state band covers 11.85% of scanned plane, conditional on $q_{0}$ tuning | VERIFIED | C | Manuscript line 528 ("11.85% of the scanned plane") and lines 558–$563 (q_{0}$-tuning qualification) |
| G3-E2 | At $r=-0.35$, $\bar{\psi}=-0.18$, $q_{0}^{2}=8$ supports the ordered branch, while $q_{0}^{2}=7.5$ adds 0.25 to the shell quadratic coefficient and removes it | VERIFIED | F3 | Manuscript lines 539, 558–559: penalty $(7.5-8)^{2}=0.25$, $r_{shell}=-0.10$, "none — disordered state is the only minimum". Auditor's recheck: $(7.5-8)^{2}=0.25$, $-0.35+0.25=-0.10$ |
| G3-E3 | Sixth-order scan narrows the band to 8.47% at $w_{6}=0.2$ | VERIFIED | C | Manuscript line 567: "(11.90% at $w_{6} = 0$ to 8.47% at $w_{6} = 0.2)$" |
| G3-E4 | §IX.5 leaves the initial mean unexplained | VERIFIED | C | Manuscript lines 1406–1408: "What fixes $\bar{\psi}? \dots$ no mechanism sets its value" |
| G3-I1 | 11.85% is an area fraction under a chosen scan domain/grid, not a cosmological probability or invariant tuning measure | VERIFIED | C | Manuscript's own wording is "of the scanned plane"; scan window unstated (G-A1, INCOMPLETE-EVIDENCE) |
| G3-I2 | Parameter-free ranking in u,v does not make the field model or the full phase diagram parameter-free | VERIFIED | C | Manuscript §II.3: S is parameter-free in u,v; §II.7: band conditional on $q_{0}$ tuning and $\bar{\psi}$. Both halves verified |
| G3-T1 | Scan detuning $\times$ mean $\times$ quench with and without sixth-order terms; release bounds, grid, candidate list; plot coexistence, linear instability, dynamical success as separate boundaries; check wavelength adapts when box size changes | VERIFIED | C | Sound design. **Precondition flagged:** the $w_{6}$ term form is unstated (G-A8), so the "with sixth-order" leg cannot be run as the manuscript'$s w_{6}$ until Brandon states the form |
| G3-P1 | Provide tolerances and connected stability regions rather than a single area percentage; supply a physical mechanism fixing the mean and resonant scale before claiming unconditional substrate selection | VERIFIED | C | Appropriate pass condition; maps to G-D2 |

### §3.5 G4 — Nucleation remains the access barrier

| # | Claim | Verdict | Grade | Evidence |
|---|---|---|---|---|
| G4-E1 | §II.9: positive effective quadratic coefficient $\approx0.107$ at $\bar{\psi}=-0.18$, so uniform state is linearly stable | VERIFIED | F3 | Manuscript lines 621–\$624: $r_{eff} = -0.35+0.36+0.097 = +0.107$$. Auditor's recheck: $-0.35-2(-0.18)+3(0.0324)=0.1072\$ |
| G4-E2 | Paper expressly requires nucleation | VERIFIED | C | Manuscript lines 624–625 ("must be nucleated across a barrier") and line 641 ("Any cosmological account $\dots$ must supply a nucleation mechanism") |
| G4-I1 | F8 shows local crystalline compatibility need not imply facile nucleation | VERIFIED | C | Matrix F8 (van Meel et al.); evidence is **abstract-checked only** (audit §4) — note the thinner basis |
| G4-I2 | F7 shows changing attractive interactions changes accessibility even with similar endpoint geometry | VERIFIED | C | Matrix F7 / audit §4 (Hoy full text checked): LJ crystallizes ~$2\times10^{4}\tau$ at 0.59<T<0.63; matched WCA does not within $2.5\times10^{5}\tau$ |
| G4-T1 | Seed droplets varying radius/amplitude, bracket growth vs decay; estimate critical droplet and barrier; compare thermal/stochastic nucleation with annealing through a linearly unstable region; state noise law and FDT interpretation | VERIFIED | C | Sound design. **Partial overlap (not contradiction):** WS-A task 4 already did 8 box droplet seeds + radial-ODE $R_{c}=12.57/\DeltaF*=555$; the full-PDE critical droplet (G-A10) is still open |
| G4-P1 | Demonstrated path from admissible initial conditions to $D_{4}$, with waiting-time distributions rather than persistence alone | VERIFIED | C | Appropriate pass condition |

### §3.6 G5 — Scientific code and proof artifacts not in the inspected deposit

| # | Claim | Verdict | Grade | Evidence |
|---|---|---|---|---|
| G5-E1 | Zenodo ZIP contains manuscript PDF/TeX/Markdown, references, ten PNGs, `md2tex.py` | VERIFIED | C | Audit §2 inventory: `IRH_v93_1.pdf`, `.tex`, `paper_v931.md`, `references.md`, `figs/fig01.png`–`fig10.png`, `md2tex.py` |
| G5-E2 | No simulation Python, Lean modules, Lake configuration, raw field arrays, or seed manifest in the archive | VERIFIED | C | Audit §2: "There are no scientific simulation scripts, .lean files, Lake/toolchain manifests, raw field data or seed manifest in this archive." |
| G5-E3 | Separate Google Drive "Independent Verification Data" link returned a sign-in page to the access method used | VERIFIED | C | Audit §2: link returned "Sign in" through the attempted access method; contents not inspected |
| G5-I1 | This is an artifact-access gap, not evidence the reported computations or Lean build are false | VERIFIED | C | Correct scope discipline; the memo states it explicitly |
| G5-I2 | Paper's Lean and independent-reproduction claims remain author-reported in this comparison | VERIFIED | C | Audit §5: no Lean build run, no time integration. Manuscript lines 1162–1170 claim eight modules / lake build exit 0 — author-reported here |
| G5-I3 | References to Lean and Mathlib identify software publications, not the actual project snapshot | VERIFIED | C | Manuscript refs [34] (de Moura et al.) and [35] (Mathlib) are software publications; no pinned toolchain/Mathlib revision appears in the deposit (G5-E2) |
| G5-I4 | Fix proposal's "eight Lean modules" | VERIFIED | C | Manuscript line 47 ("eight Lean 4 modules compile cleanly") and lines 1168–1170 ("producing all eight module .olean files") |
| G5-T1 | Deposit one versioned archive (shell counter, exact update equations, seed list, conserved/nonconserved timestep choices, nonlinear dealiasing, scan grids, raw outputs) + eight Lean modules, pinned toolchain/Mathlib revision, build command/logs; map each claim to script/theorem/expected output | VERIFIED | C | Appropriate fix; deposit change is Brandon's call |
| G5-I5 | Do not infer unconditional nonlinear stability from treating the linear operator implicitly | VERIFIED | C | Manuscript §II.6: "unconditionally stable with the linear operator treated implicitly in Fourier space" — the qualifier covers the linear operator only; nonlinear explicit terms are a separate stability question. Valid caution |
| G5-P1 | Fresh environment reproduces exact counts, representative energy, stated proof build; check linear-implicit vs nonlinear timestep stability separately | VERIFIED | C | Appropriate pass condition |

### §3.7 §2 — Source corrections and framing changes; §3 — Boundaries; order of work

| # | Claim | Verdict | Grade | Evidence |
|---|---|---|---|---|
| C1 | **Hoy system-size correction:** Hoy's Methods specifies $N=5\times10^{5}$; Results uses large boxes to exclude the earlier finite-size concern; his footnote about 648 particles refers to the older Skoge et al. study. A citation-context conflation, not a failure of Hoy's corroboration. | VERIFIED | C | **Independently re-checked two ways:** (1) audit §4 (S6 full HTML checked: "500,000-particle system; $\dots 648$-particle historical footnote"); (2) gap-memo auditor's own web search of Hoy 2024 (arXiv:2311.03465): Methods "Systems are composed of $N = 5\times10^{5}$ particles"; Introduction "crystallization occurred in a very-slowly-compressed, very small (648-atom) system [Skoge et al. 2006], but none was observed in a 10000-atom system". **Correction to the task brief's framing (see §5.3):** the memo does *not* say the manuscript cited $1\times10^{5}$, and the manuscript does not cite $1\times10^{5}$ anywhere (grep over the 1,638-line rebuild: no $1\times10^{5}/100,000)$. What the manuscript does (lines 433–435) is place the N=648 commensurability example ("choice N = 648 promotes $a 3\times3\times3\times3$-cell $D_{4}$ single crystal") directly beside Hoy's result without stating Hoy's N — that juxtaposition is the conflation the memo correctly identifies |
| C2 | Suggested replacement sentence (500,000-particle 4D LJ, large enough to address the PBC concern for earlier 648-particle simulations; shared endpoint consistent, interaction/selection differ) | VERIFIED | C | Each clause supported by C1 evidence above; manuscript lines 433–435 for the 648-cell statement |
| C3 | F4 and IRH share the Landau expansion, finite-q shell, cubic closed-triangle mechanism; S2 explicitly uses equal-magnitude amplitudes and triangle counts | VERIFIED | C | Audit §4: S2 (Elitzur et al.) full HTML §§2–4 checked; manuscript §II.3 equal-amplitude ansatz |
| C4 | Extra quartet normalization and explicit field trajectories are the relevant distinctions; calling the analytic routes independent without specifying the level overstates the separation | VERIFIED | C | Matrix F4: S2 has no time integration, triangle-only ranking; IRH adds $q_{4}$ normalization $(S=\tau^{2}/q_{4})$ and §II.6 dynamics. Framing judgement, supported |
| C5 | Suggested framing sentence ("extends the higher-dimensional Landau selection comparison by retaining candidate-dependent quartic counts $\dots$ and testing cubic-mediated shell competition dynamically"); scoped description, not a priority claim | VERIFIED | C | Accurate as scoped; memo itself disclaims priority ("broader novelty would need a wider search") |
| C6 | F9 proves uniqueness of the optimal kissing configuration, not dynamical selection or unrestricted 4D packing optimality | VERIFIED | C | Matrix F9; audit §4: S8 full HTML through §5 checked |
| C7 | F10's non-universal-optimality theorem concerns 24 points on $S^{3}$ | VERIFIED | C | Matrix F10; evidence is **abstract-checked only** (audit §4) — thinner basis, noted |
| C8 | §II.11's Gaussian $\beta$ scan needs its configuration space and objective spelled out before treating it as a reproduction of that theorem; if it optimized infinite lattices, it is a different problem | VERIFIED | C | Manuscript lines 656–\$663: $\beta$\$ windows [0.05,2.4]$\cup[3.1,12]$, competitor wins [2.6,3.0] by $\leq0.007$% — but no configuration space/objective stated in that passage. Valid scope caution |
| C9 | Zero triad count excludes a shell from the cubic first-order onset mechanism in the stated ansatz; does not exclude quartic-driven ordering at negative r, multiscale coupling, or another functional | VERIFIED | C | Scope inference from §II.3–II.5: S=0 blocks only the cubic route as formulated; quartic/multiscale routes are not excluded anywhere in the text |
| C10 | Highest onset threshold need not identify the stable phase far from onset; F5 supplies a concrete warning | VERIFIED | C | Matrix F5 (Groh & Mulder): near-spinodal BCC preference does not fix the ultimately stable phase (FCC accessible). Evidence **abstract-checked only** (audit §4); full calculations not audited |
| D1 | Dimension: marginality of the isolated $\int(\nabla^{2}\psi)^{2}$ term at d=4 is a scaling fact, not a demonstrated comparison of stable solutions of the full $q_{0}$-dependent functional across dimensions; base already $\mathbb{R}^{4}$; §IX.2 acknowledges unresolved interpretations | VERIFIED | C | Manuscript lines 835, 851–\$852: $(\nabla$^{2}$\psi)^{2} \to \lambda$^{4-d}\$, marginal at d=4. §IX.2: three mutually exclusive readings (A)/(B)/(C), "must be decided" |
| D2 | Physical scale: $a_{0}=2\pi/q_{0}$ relates wavelength to the model's resonant input; microscopic determination of $q_{0}$ and crystal-spacing convention still needed before calling an absolute length scale predicted | VERIFIED | C | Manuscript line ~560: "Since $a_{0} = 2\pi/q_{0} \dots$". No $q_{0}$-fixing mechanism is stated anywhere (cf. G-D2) |
| D3 | Gauge: 24-cell/2T/McKay association identifies an algebraic relationship; does not by itself construct local $E_{6}$ gauge degrees of freedom, their action, or coupling to the scalar; require a dynamical construction rather than counting it as selection evidence | VERIFIED | C | Manuscript §IV.3 (algebraic: 24-cell = 2T, McKay $\leftrightarrow$ affine $E_{6}$, lines 939–977). Inventory $G-C6: E_{6}$ breaking pattern/Higgs not derived; physical reading grade D |
| D4 | Matter/gravity: generation count, Lorentzian signature, Einstein equations, Higgs breaking remain outside the validated selection test, consistent with the paper's open-problem register; topological charge classification alone does not establish energetically stable, finite-energy soliton solutions | VERIFIED | C | Manuscript Part IX (G-C2/C3/C6/C7); §V.1 lists point solitons from $\pi_{3}$ classification (lines 1037, 1311) — a homotopy classification, with no finite-energy stability computation located in that section |
| R1 | Close the access gap and fix the Hoy attribution first: quick, directly improves checkability | VERIFIED | — (prioritisation judgement) | G5 fix + C1 are both cheap, checkability-only items |
| R2 | Run the full-pattern basin and matched-rival tests (G1–G2): most likely to change the strength of the central selection claim | VERIFIED | — (judgement) | Consistent with G-A5 as the programme's headline gap |
| R3 | Map detuning and nucleation (G3–G4): turns conditional stability into a quantified accessibility statement | VERIFIED | — (judgement) | Maps to G-A1/A3/A8/A10, G-D3 |
| R4 | "What this memo does not claim": no new field simulation or Lean build was run; no independent audit of the unnamed verification party was possible; exact shell counting and deposit inspection were performed and documented in `verification-audit.md` | VERIFIED | C | Audit §5 ("Not performed": no time integration, phase-diagram reconstruction, particle dynamics, Lean compilation) and §§1–2 (enumeration executed, deposit inspected) |

**Gap-memo tally: 62 VERIFIED, 2 CORRECTED, 0 REFUTED, 0 ABSTAIN.**

### §3.8 Test-to-gap mapping (memo's proposed tests $\to$ inventory)

| Memo test | Inventory gap(s) it would close | Owner of next step | Overlap note |
|---|---|---|---|
| G1 full-pattern basin test (random / 6-/12-mode / symmetric-24 / perturbed-full seeds, conserved dynamics, 20 seeds/condition) | **G-A5** (headline: selection vs spontaneous reach), **G-A4** (24/24-from-noise rate), **G-A13** (2-/8-mode transience), **G-A9** (larger-box/phase-locking convergence, via the box-size leg) | Co-scientist task — **the G-A5 arm is already RUNNING** (4D field test, chat `02dfb5cb-5423-47eb-9bbe-d8e3d25b6fdc`); local Muse audit when it lands. The within-truncation 20-seed screening arm is a small local/Co-scientist item | **Partial duplicate of the running 4D test:** both use random fields + patterned seeds and report mode occupancy/power/energy. Distinct: the running test permits off-shell modes (attacks the truncation gap); G1 as written does not specify off-shell permission and is framed under conserved dynamics. WS-A task 5 already covers the perturbed-full-state arm (1 rad / $\pm20$%) |
| G2 matched $D_{4}/A_{4}$* test (same mean/penalty/normalization; commensurate domains; sub-patterns + unequal amplitudes) | **G-A20** (no $A_{4}$* control; no preregistered competitor set, $\geq10$ seeds, commensurate cells), **G-A7** (stripe competitor omitted — the within-shell sub-pattern leg) | Co-scientist task **A20 — candidate, NOT launched; launch is Brandon's call**. The full fair test (preregistered set, $\geq10$ seeds, commensurate cells) is programme-scale, to be scoped and costed | No duplication with the running 4D test (different question: matched rival, not off-shell formation) |
| G3 detuning $\times$ mean $\times$ quench scan (with/without $w_{6}$; release bounds/grid/candidates; separate coexistence/instability/success boundaries; box-size wavelength check) | **G-A1** (11.85% not reproducible), **G-A2** (11.85% vs 11.90% canonical — Brandon's call), **G-A3** (measured slice vs quoted union; +0.03 edge), **G-$A8** (w_{6}$ term form unstated), **G-A19** (relaxed free-energy band, ~1% shift), **G-D2** (what fixes $\bar{\psi})$ | **Brandon's call first** (state scan window/definition, $w_{6}$ term form, canonical band value$) \to$ Co-scientist task (recompute) | Overlaps WS-A task 3's map (the tool for G-A3) but extends it to the joint detuning$\timesw_{6}$ map and the dynamical-success boundary |
| G4 nucleation test (droplet radius/amplitude bracketing; critical droplet/barrier; thermal vs annealing-through-unstable-region; noise law / FDT) | **G-A10** (full-PDE critical droplet), **G-A9** (larger-box droplet run), **G-D3** (what supplies the nucleation event); builds on closed **G-A18** (thin-wall shown to fail) | Co-scientist task, costed first; GCP-scale for the large-box leg (named cap needed, none authorised) | **Partially done:** WS-A task 4 did 8 box droplet seeds + ODE $R_{c}=12.57/\DeltaF*=555$. Still open: full-PDE droplet and waiting-time distributions |
| G5 artifact fix (versioned archive + eight Lean modules, pinned toolchain, build logs, claim$\to$script map) | **G-E1** (see §6 — this memo was "not located"; it is now located), plus preconditions of **G-A1/G-A8** (scan code / $w_{6}$ form) | **Brandon's call** (deposit/repo change$) \to$ local Muse verification (fresh-environment reproduction) | No duplication with any running task |

## §4. `verification-audit.md` — 37 claims: 22 VERIFIED, 5 CORRECTED, 0 REFUTED, 10 ABSTAIN

### §4.1 Header and §1 — Independent exact enumeration

| # | Claim | Verdict | Grade | Evidence |
|---|---|---|---|---|
| 1 | Date 9 Nov 2026 | ABSTAIN | — | No grade. Task date as stated; workspace mtimes are 2026-11-12 19:51 UTC (pull/copy time), so the date is not independently verifiable from the files |
| 2 | Purpose: distinguish this comparison's checks from McCrary v93.1's reported numerical/formal results | VERIFIED | C | The file does exactly this (R vs M coding; §5 boundary). Companion `framework-matrix.md` M/F/A/R/U key corroborates |
| 3 | Roots constructed as $\pme_{i}\pme_{j}$, i<j; 3D BCC = 12-vector reciprocal star, $D_{4} = 24$-vector root star | VERIFIED | F2 | Matches manuscript §II.2/II.4–5 (roots norm${}^{2}=2)$; verification auditor's re-derivation used the same definition and reproduces both stars |
| 4 | Counter/formula definitions for C(s), T, Q, $\tau^{2}$, $q_{4}$, S as exact rationals | VERIFIED | F2 | Matches manuscript $(\tau=T/N^{3/2}, q_{4}=Q/N^{2}, S=\tau^{2}/q_{4}$, lines 377–417); auditor's run implements them independently |
| 5 | BCC row (12, 48, 540, 4/3, 15/4, 16/45) | VERIFIED | F2 | Auditor's exact run reproduces every entry |
| 6 | $D_{4}$ row (24, 192, 3384, 8/3, 47/8, 64/141) | VERIFIED | F2 | Auditor's exact run reproduces every entry |
| 7 | "Matches S0 §§II.3–5 and II.8" | **CORRECTED** | C | §§II.3–5 match exactly (lines 377, 387, 413–417). The II.8 citation is misplaced: §II.8 (lines 571+) *reuses* N=24, T=192, Q=3384 for the stability/attractor derivation, but the selection-count table is in §§II.4–5. Minor citation error, not a numerical error |
| 8 | Relative advantage (64/141)/$(12/31)-1 = 73/423 \approx 17.26$% | VERIFIED as arithmetic | F2 | Exact (auditor's run). **Conditional:** it depends on the manuscript'$s A_{4}$* score 12/31, which the file did not re-derive (see #9). The matrix auditor has since re-derived $A_{4}* ($see §1.1) |
| 9 | "The $A_{4}$* enumeration itself was not rerun" | VERIFIED (honest limitation) | C | Stated plainly in the file. The verification auditor also did not re-derive $A_{4}* ($its shell is not the $\pme_{i}\pme_{j}$ construction); $A_{4}$* counts (N=20, T=120, Q=1860) remain manuscript-reported *in this file* — since re-derived by the matrix auditor |
| 10 | "This verifies discrete counting and score arithmetic, not global field minimization or physical selection" | VERIFIED | C | Correct and important scope limitation; consistent with gap-memo G1 and WS-A/WS-C (noise quenches 0/5, 0/6; Hark F1) |
| 11 | Headline meta-claim: "independently confirmed the exact $D_{4}$/BCC selection counts" | **CORRECTED** | — | Numbers F2, I1; the independence claim as stated is overstated. The *procedure described* is genuinely re-derivational (not a restatement of the manuscript table), and the numbers are correct per the auditor's independent re-run — but the file ships **no code, log, or output artifact** (no script in the directory; only prose), so its execution is unverifiable from the evidence shown. Confirmation is completed by this audit, not by the file alone |

### §4.2 §2 — Deposit inspection

| # | Claim | Verdict | Grade | Evidence |
|---|---|---|---|---|
| 12 | Zenodo API: v93.1 is an open CC BY 4.0 preprint, publication date 18 Sep 2026 | VERIFIED | C | Live Zenodo API fetch (`zenodo.org/api/records/22821689`): `access_right: open`, `license: cc-by-4.0`, `resource_type: preprint`, `publication_date: 2026-09-18`, DOI `10.5281/zenodo.22821689` |
| 13 | Supplied PDF itself dated 17 September | VERIFIED | C | Manuscript header reads "September 17, 2026" (rebuild lines 1–10) |
| 14 | `IRH_v93_1.pdf`: 1,839,188 bytes, MD5 `952116b3154824e3a19fcdc558898c5f` | VERIFIED | C | Zenodo API lists size 1839188 / that MD5; auditor downloaded the ZIP and recomputed the embedded PDF's MD5 — exact match |
| 15 | `IRH_v93_1_source_package.zip`: 3,202,228 bytes, MD5 `11a90f9a82d97652112c07608513316f` | VERIFIED | C | Zenodo API lists size 3202228 / that MD5; auditor's downloaded ZIP (3,202,228 bytes) recomputes to the same MD5 |
| 16 | ZIP inventory: figs 01–10, `IRH_v93_1.pdf/.tex`, `paper_v931.md`, `references.md`, `md2tex.py` | **CORRECTED** (trivial) | C | Auditor's listing of the downloaded ZIP confirms all contents (17 entries incl. directories) — but all paths sit under the `IRH_v93_1_source/` prefix, which the file's table omits. Contents correct; paths as printed are relative inside that folder, not archive-root paths |
| 17 | No simulation scripts, `.lean` files, Lake/toolchain manifests, raw field data, or seed manifest in the archive | VERIFIED | C | Auditor's ZIP listing: the only `.py` is `md2tex.py`; no `.lean`, no `lakefile.toml`/`lean-toolchain`, no `.npy/.csv/.json` data |
| 18 | `md2tex.py` is a manuscript-conversion utility, not the simulation implementation | VERIFIED | C | File header: "Convert the v93.1 manuscript Markdown to Overleaf-compatible XeLaTeX"; it reads `paper_v931.md` $\to$ `IRH_v93_1.tex` |
| 19 | "File hashes above are metadata values, not independently recomputed checksums" | **CORRECTED** | C | True of the file's own work (honest limitation), but **superseded by this audit**: the auditor recomputed both MD5s (ZIP and embedded PDF) and they match exactly |
| 20 | Drive "Independent Verification Data" link returned "Sign in"; contents not inspected | ABSTAIN | — | Verification auditor did not attempt Drive access, so the sign-in outcome is not re-verified by him. The link ID itself is verified: it matches the manuscript header (`1Sxkginzo_UmNrNETfunLK8_XUq4tbuXb`, rebuild line 8). No log/screenshot is shipped in the file |
| 21 | "This does not establish that access is impossible by every route or that the artifacts do not exist elsewhere" | VERIFIED | C | Correct hedging; the file does not overclaim from a failed access attempt |

### §4.3 §3 — Manuscript reading and visual checks

| # | Claim | Verdict | Grade | Evidence |
|---|---|---|---|---|
| 22 | "Read all 31 pages through the workspace PDF reader" | ABSTAIN | — | Page count not established by the auditor: no `pypdf`/`fitz` in the env; the source rebuild has 35 form-feed segments (including expansion notes) and the consolidated summary says 34 pp. 31 (PDF) vs 34 (rebuild) is plausibly a pagination difference, but is unresolved — flag, do not treat as contradiction |
| 23 | "Viewed pages 7 and 10 as printed to check the exact lattice scores, reciprocal-label convention, detuning table and energy comparison" | ABSTAIN | — | Unverifiable from the evidence shown: no screenshots/notes shipped, and rebuild pagination does not put those items on pp. 7/10 together (selection quantities are rebuild p. 9; II.6 is p. 10; detuning table is II.7, pp. 11–12; energy comparison II.8, p. 12). The underlying tables themselves exist in the manuscript (verified above); the specific page-check claim cannot be checked |
| 24 | "Reported percentages and other prose results are attributed to their sections in the matrix rather than presented as newly reproduced measurements" | VERIFIED | C | The companion `framework-matrix.md` does exactly this (M = manuscript-reported vs R = exact calculation executed here) |

### §4.4 §4 — External source checks (auditor did not re-fetch all nine sources; grades capped accordingly)

| # | Claim | Verdict | Grade | Evidence |
|---|---|---|---|---|
| 25 | S2 Elitzur et al., arXiv full HTML §§2–4 | ABSTAIN | — | Not re-checked by the verification auditor; the manuscript §II.5 corroborates the 4D cross-polytope claim in text, but not the file's reading of Elitzur. (The matrix auditor *did* read arXiv:1101.1631v1 in full — see §2.2, claims 15–17) |
| 26 | S3 Groh & Mulder, AMOLF institutional abstract | ABSTAIN | — | Not re-checked by the verification auditor; consistent with WS-C C1.6 (near-melting scope transfer FAILS), no conflict. (The matrix auditor read the AMOLF summary — see §2.2, claims 18–20) |
| 27 | S6 Hoy, arXiv abstract + full HTML Methods/Results; 500,000-particle system; LJ/WCA control; $D_{4}$ identification; 648-particle historical footnote | **CORRECTED** | C | The factual content is corroborated (manuscript §II.5; gap-memo §2 corrects the same 500k-vs-648 attribution), but the file's own full-text check is unevidenced (no quotes/extracts shipped). Content stands; the check itself is not independently evidenced |
| 28 | S7 van Meel et al., abstract/search summaries only; no detailed numerical extraction used | ABSTAIN | — | Not re-checked by the verification auditor; file honestly scopes it to abstract level. (The matrix auditor read the abstract — see §2.2, claims 27–29) |
| 29 | S8 de Laat et al., arXiv abstract + full HTML through §5 | ABSTAIN | — | Not re-checked by the verification auditor. (The matrix auditor read through §5 — see §2.2, claims 30–32) |
| 30 | S9 Cohn et al., arXiv abstract; non-universal optimality specifically for a spherical code | ABSTAIN | — | Not re-checked by the verification auditor; consistent with matrix F10 and WS-D task 9/12 handling. (The matrix auditor read the abstract — see §2.2, claims 33–35) |
| 31 | S1, S4, S5: manuscript references/descriptions only, "not independently full-text audited" | VERIFIED (honest limitation) | C | The file admits the limit plainly |
| 32 | All references selected from the supplied paper's bibliography; search targeted, not systematic | VERIFIED | C | Matrix source register confirms S0-anchored selection; the file states the limitation |
| 33 | Initial Academia search found the seed paper but no useful additional direct comparator | ABSTAIN | — | No search log shown; unverifiable from evidence |

### §4.5 §5 — Not performed

| # | Claim | Verdict | Grade | Evidence |
|---|---|---|---|---|
| 34 | No time integration, phase-diagram reconstruction, particle dynamics, Lean compilation, full source-code review of comparator implementations, or empirical test of the substrate interpretation | VERIFIED | C | True of the file's contents; nothing of that kind is shown |
| 35 | No new simulation percentages or error bars generated | VERIFIED | C | The file contains only the enumeration table and the deposit inventory |
| 36 | The comparison's proposed tests are proposals, not completed experiments | VERIFIED | C | Gap-memo §1 (G1–G5) states tests with pass conditions; none is claimed completed |
| 37 | Reproduction boundary: "exact combinatorics confirmed here; kinetic and proof-build claims remain manuscript-reported pending access to their scientific artifacts" | VERIFIED | C | Correct boundary; consistent with §2 artifact gap and with WS-A/WS-C/Hark F1 (no dynamical-selection claim is made here) |

**Verification-audit tally: 22 VERIFIED, 5 CORRECTED, 0 REFUTED, 10 ABSTAIN.**

## §5. Cross-cutting findings

### §5.1 Grade-moving findings: NONE

Nothing in any of the three files moves any IRH grade, and the files themselves claim no grade above
their M/F/A/R/U labels. In particular:

- The S = 64/141 arithmetic is exactly reproduced by three independent re-derivations (coordinator,
  matrix auditor, verification auditor), and the $A_{4}$* score 12/31 is now independently re-derived by the
  matrix auditor (T=120, Q=1860 via the \$20 $A_{4}$\$ roots) — but that does not upgrade C6, which stays
  **D as presented** (Hark F6): the arithmetic is verified, the physical selection claim (restricted
  competitor set, $q_{0}$ tuned, box-limited dynamics) is unchanged. The margin depends on the competitor set,
  and all verification here is artificial (I1).
- The Hoy correction (gap-memo C1/C2, matrix #63) is a citation-context correction only; the memo itself
  states it is "not a failure of Hoy's corroboration", and the $D_{4}$ endpoint corroboration is unchanged.
- The exact shell counts (gap-memo B2) were already the manuscript's stated values; re-deriving them adds
  a check, not a grade change.
- The memo's gap statements (G1–G5) restate or sharpen gaps already in the inventory (G-A1–A5, G-D2/D3);
  they do not close any of them.

### §5.2 Contradictions with WS-A–E (tasks 1–15): NONE direct

The file set aligns with the delivered work throughout. Two staleness / partial-supersession items
(the files are dated 9 Nov; the WS tasks were delivered 10 Nov):

1. **Gap-memo G1-I2** — "without perturbation and basin tests": WS-A task 5 (14 runs) and Hark F1
   transverse tests now supply the perturbation leg; only the unbiased-emergence leg remains open.
2. **Gap-memo G4-T1** — droplet bracketing: WS-A task 4 already ran 8 box droplet seeds and the exact
   radial ODE; the full-PDE droplet and waiting-time distributions remain open (G-A10).
3. **Matrix #47** — "need perturbed full-state basin tests": now partly answered by Hark F1
   (perturbed hex6/fcc$12 \to$ full24, 5/5 and 4/4), which strengthens rather than contradicts the caution.

The file set's scope cautions match WS-C C1.2 (FAILED as written: noise quench reaches 6/24 inside the
band), WS-C C1.6 (combinatorial PASS / scope FAIL), WS-A task 3 (11.85% bracketed, not reproduced),
and WS-C task 13 (attractor fixed point resolution-independent). The files contain no "143 basin runs"
figure anywhere — the 14-runs-not-143 guard (inventory G-E11) is respected; WS-A task 5 ran 14 runs.

### §5.3 Tensions with the manuscript (the file set is on the supported side in each)

1. Manuscript §II.5: "The two routes are independent and select the same winner" (Landau vs S-criterion)
   — the matrix (#52) withholds mechanism-level independence; supported by WS-C C1.6 and gap-memo §2
   (shared Landau/cubic-triangle foundation).
2. Manuscript §II.8: "a genuine dynamical attractor" (seeded 24-mode persistence) — the matrix (#47, #11)
   withholds the attractor reading; supported by Hark F1 (hex6/fcc12 are saddles at $\bar{\psi}=-0.18$ under
   transverse perturbation).
3. Manuscript §II.6: "unconditionally stable" (linear operator treated implicitly) — the matrix (#58)
   withholds unconditional stability for the explicit nonlinear terms; supported by gap-memo G5.
4. Manuscript §II.5: N=648 placed beside Hoy's result — the matrix (#63) and gap-memo (C1) correctly
   attribute 500,000 particles to Hoy and the 648-atom system to the older Skoge et al. study.
5. Manuscript ref [45] prints arXiv:math/0607446 — the matrix (#76) correctly flags it and directs use
   of 1101.1631 (math/0607446 is a typo for Cohn's math/0607447).

**Correction to the audit task brief itself (recorded, not a file error):** the brief framed the Hoy
correction as "the manuscript's cited $1\times10^{5}$" vs $N=5\times10^{5}$. That premise is wrong — neither the memo nor
the manuscript says $1\times10^{5}$ anywhere (coordinator's grep over the 1,638-line rebuild: no $1\times10^{5}/100,000)$.
The manuscript's actual text is the N=648 juxtaposition (lines 433–435), and the memo's Hoy wording is
accurate as written. The correction stands exactly as the memo states it.

### §5.4 The $F3\toF2$ question — NOT decided here

A two-route F2 reading for the exact counts is available (manuscript/task-10 SymPy+flint, plus the
coordinator's, matrix auditor's, and verification auditor's independent enumerations), but this audit
does **not** claim F2. The WS-$D F3\toF2$ question is open (inventory G-C17, Brandon's call — Hark's
two-route logic was applied to WS-A/B/C/E but not to WS-D). The counts are graded F3, I1 in this audit.
Do not report them as F2 until that question is decided.

### §5.5 Checks that are not actually checks (flagged, not false)

- The verification-audit §1 enumeration: procedure described, execution unevidenced (no code/log shipped).
  The numbers are right per this audit's three re-runs; the file's execution is not checkable from the
  file alone (see §4.1, claim 11).
- The verification-audit §3 page checks (pp. 7 and 10): no screenshots/notes shipped; rebuild pagination
  does not put those items on pp. 7/10 together. The underlying tables exist; the page-check claim itself
  cannot be checked (claims 22–23).
- The verification-audit §4 external checks for S2/S3/S7/S8/S9 and the Academia search: no extracts/logs
  shipped. The matrix auditor independently re-read S2 (full HTML), S3 (AMOLF abstract), S7 (abstract),
  S8 (through §5), S9 (abstract) — so the underlying content is corroborated in this audit even where
  the verification-audit file's own check is unevidenced.
- Thinner evidence bases (not errors): F8 (gap-memo G4-I1), F10 (C7), F5 (C10) rest on abstract /
  institutional-summary checks only — the memo's reliance on them is proportionate to that basis, but
  they should not be cited as full-text-verified.
- The $F9 d_{2}=\delta=16$ parameter (matrix #68) is the only substantive in-file number no auditor located;
  it is not load-bearing for any conclusion.

### §5.6 "143 basin runs" guard — INTACT

None of the three files contains the figure "143". WS-A task 5's 14 runs remain the correct count;
the email's "143 basin runs" is Academia's count, not ours, and is never cited as our count in these files.

## §6. Closing note — G-E1 is now LOCATED

**Gap inventory entry G-E1 is now LOCATED.** The three "Compare $D_{4}$ Selection Frameworks" files are present
in the workspace and were read in full and audited claim-by-claim in this report:

- `~/workspace/research/irh/co-scientist-tasks-2026-11-10/compare-d4-frameworks/framework-matrix.md`
  — md5 `1b4c5388db42f831ee24ccb2e5aea070`
- `~/workspace/research/irh/co-scientist-tasks-2026-11-10/compare-d4-frameworks/gap-memo.md`
  — md5 `6b5a91a08038a1f7af997847809c815a`
- `~/workspace/research/irh/co-scientist-tasks-2026-11-10/compare-d4-frameworks/verification-audit.md`
  — md5 `726a851d1887f8330e1499294ea80d75`

**The source email is dated Nov 9, 2026, 5:31 PM — NOT Nov 10 as previously recorded.** Verified by
direct Gmail lookup: message `1a1c2a6dead2cefa`, from Academia Co-scientist <updates@academia-mail.com>,
subject "Co-scientist finished: Compare $D_{4}$ Selection Frameworks", sent Mon, 9 Nov 2026 23:31:17 +0000
(2026-11-09 17:31:17 CST). The task finished overnight Nov $9\to10$; the email is Nov 9. The inventory's
and summary's "Nov 10" dating of this task should be corrected to Nov 9 (email) / overnight Nov $9\to10$
(completion), and G-E1 should be marked LOCATED with this audit as its record.

**What this audit does and does not do:** it verifies the file set's numbers, citations, and scope claims
against the manuscript and the delivered WS-A–E work, and maps the memo's proposed tests onto the gap
inventory (§3.8). It closes no gap: G-A5 (the headline selection-vs-spontaneous-reach gap) is attacked
by the 4D field test now running in Academia (chat `02dfb5cb-5423-47eb-9bbe-d8e3d25b6fdc`); A6
(off-shell instabilities) and A20 (matched $D_{4}/A_{4}$* onset branches) remain candidates awaiting Brandon's
word; the G5 artifact fix (versioned archive + eight Lean modules) is Brandon's call. Recommended
inventory updates from this audit: $G-E1 \to$ LOCATED (this report); G-A5 note — memo's G1 test partially
duplicates the running 4D test (distinct: the running test permits off-shell modes); G-C17 — $F3\toF2$
question for the exact counts still open, not decided here.

---
*Audit method: three parallel file auditors + coordinator's independent exact enumeration (conda env,
exact rationals) and Gmail lookup. Reports only — nothing filed, committed, or written into the
manuscript; no GCP spend; no heavy simulations; no Academia launches; no contact with anyone.*

---

## Amendment note — 2026-11-12 14:07 CST: HLRE §6.5 human-gate repeal; exact counts $F3 \to F2$

Brandon repealed the HLRE §6.5 human-gate requirement on 2026-11-12 14:07 CST,
in conversation, from his assessment and all future assessments
(amendment note `HLRE-6-5-HUMAN-GATE-REPEAL-2026-11-12.md` in the programme
directory). The repeal removes the fallback grade caps $(\leq C$ Track E / F3
Track F) for artificial-only verification. Track F F2 (one independent human
or machine route) is now reachable on machine routes alone. What does NOT
change: independence levels (all-artificial verification stays max I1; Track E
stays capped at C by the $I1\toC$ bound); premise ledgers; the §7 disclosure that
all verification is artificial (I1).

**Regrade applied by this note:** the exact $D_{4}$/BCC counts in §1 —
BCC N=12, T=48, Q=540, S=16/45; $D_{4} N=24$, T=192, Q=3384, S=64/141; margin
over $A_{4}* 73/423 \approx 17.26$% — are **F2, I1** (was F3, I1). Basis: three
independent re-derivations (coordinator + two auditors, exact rational
arithmetic), recorded in §1 of this audit. The audit's §1 statement that "a
two-route F2 reading for the exact counts is available, but this audit does
not claim F2" is superseded by this note; the F2 is claimed now. The
"Open item deliberately NOT decided" paragraph in the audit is likewise
superseded for the counts only — the WS-$D F3\toF2$ question (inventory G-C17)
is decided separately by the same repeal (G1/G5/$G8/G12 \to F2)$. No other grade
in this audit changes: the 7 corrections and 16 ABSTAINs stand as written.
