# Task 15 — Cosmological signatures: gravitational-wave and CMB forward model

**Workstream E (cosmology map), IRH Co-scientist task programme**
**Date:** 2026-11-10
**Comparison target (fixed):** IRH v93.1 (McCrary, Zenodo DOI 10.5281/zenodo.22821689), manuscript source `IRH_v93_1_source_rebuilt.txt` (1,638 lines), predictions file `predictions/VI-predictions.md` (VI.1–VI.7) in the repo clone `~/workspace/research/IRH-Theory-Development-Workspace/`.

## CLAIM + STATUS

**CLAIM.** There is nothing to forward-model. The manuscript states **zero** gravitational-wave predictions and **zero** CMB predictions: the terms "gravitational wave" and "CMB"/"cosmic microwave" occur **0 times** in the 1,638-line manuscript source (grep-verified in this session, with working control greps). The task as worded — "forward-model the gravitational-wave signatures and cosmic microwave background power-spectrum modifications predicted by the IRH framework" — presupposes a stated model that does not exist. What this report delivers instead, as the task's own rules require ("where the manuscript is silent, say so and ABSTAIN for that piece"), is:

1. the extraction proving the silence (§1);
2. the null observable grid — every observable's IRH prediction column reads **UNSTATED / ABSTAIN**, against verified instrument responses (§3);
3. the blockers that make a forward model impossible today, each gated to a manuscript passage (§4);
4. the requirements list a future forward model would have to satisfy (§5);
5. the one partial bridge that exists (first-order transition + defect spectrum, §6) and exactly what it still lacks.

**STATUS: EXTRACTION COMPLETE; FORWARD MODEL ABSTAINED.** The ABSTAIN is not a failure of effort: the forward model has no input. Any number produced here for a GW spectrum or a CMB power spectrum would be invented, not derived — and inventing it would violate the task's own instruction ("Do not invent a cosmology the manuscript does not state").

## 1. Extraction — the manuscript states no GW or CMB prediction

**Tool verdicts (this session, `grep -c` on `IRH_v93_1_source_rebuilt.txt`, 1,638 lines, exit 0):**

| Term | Count | Reading |
|---|---|---|
| "gravitational wave" | **0** | No GW prediction, no GW discussion. |
| "CMB" / "cosmic microwave" | **0** | No CMB prediction, no CMB discussion. |
| "photon" | 0 | No photon coupling stated. |
| "baryon" | 0 | No baryon coupling stated. |
| "graviton" | 1 | Line 1383 only (see §4, blocker B3). |
| "tensor" | 1 | Line 1376 only (the effective-metric passage, §4 B3). |
| "Hubble" / "Friedmann" / "scale factor" | 0 | No expansion history stated. |
| "monopole" (control) | 12 | Grep works on this file; the zeros above are real. |
| "inflation" (control) | 1 | §V.3 only (see below). |
| "D4" / "$D_{4}$" (control) | 83 | Grep works; the file is the full manuscript. |

**Second independent check:** the predictions file `predictions/VI-predictions.md` was read in full (earlier in this workstream) and its section headings re-grepped in this session (exit 0): VI.1 Triad phase locking; VI.2 The baseline-tension band; VI.3 Validity boundary of the non-relativistic limit; VI.4 Stability bound; VI.5 Isotropy to fourth order — a prediction of absence; VI.6 Defect spectrum; VI.7 Monopoles — predicted, not excluded. **None of VI.1–VI.7 is a GW or CMB prediction.** They are laboratory-scale pattern predictions (band, stability, isotropy, defect spectrum) plus the monopole statement. The two greps (manuscript source + predictions file) are independent of each other and agree: the cosmological observable set is empty.

**The only cosmology-adjacent statements in the manuscript** (all named, none derived):

- **§V.3 (monopoles), lines 1086–1090, verbatim:** "EXCLUDED — monopole absence, claimed in earlier versions, is inconsistent with an $E_{6}$ gauge group. IRH inherits the standard unified-theory monopole problem and requires the standard resolution: inflationary dilution, or a breaking pattern avoiding the relevant topology." — The resolution is *named*, not derived: no dilution factor, no monopole density, no breaking pattern is stated.
- **§II.9, line 641:** "Any cosmological account within this framework must supply a nucleation mechanism" — a requirement on a future account, not an account.
- **§IX.5, lines 1406–1410, verbatim:** "What fixes $\bar{\psi}$? Under conserved dynamics it is an initial datum rather than a tuned coupling, which reclassifies the fine-tuning objection as a cosmological initial-condition question — a different and weaker charge. But no mechanism sets its value, so whether occupying the $D_{4}$ band is a prediction or a tuning remains undetermined. What supplies the nucleation event? The transition is first order (§II.9), so the $D_{4}$ phase must$\dots$" — no mechanism sets $\bar{\psi}$; no nucleation event is supplied.

**What the manuscript's functional does give (for the record, from task 11):** F(A) = $(N/2)r_{eff}\cdotA^{2} - (T/3)u_{eff}\cdotA^{3} + ($vQ/\$4$)A^{4}$$, $$r_{eff} = r - 2u\bar{\psi} + 3v\bar{\psi}$^{2}$, $$u_{eff} = u - 3v\bar{\psi}$$, N = 24, T = 192, Q = 3384, u = v = 1, fiducial $r = -0.35$, $$\bar{\psi} = -0.18$\$. This is a *pattern-formation* free energy for a substrate field. It contains no scale factor, no Hubble parameter, no temperature of a cosmological plasma, no coupling to photons or baryons, and no tensor sector. It cannot be turned into a GW spectrum or a CMB power spectrum without adding a cosmology the manuscript does not state.

## 2. What the manuscript DOES predict (for contrast)

VI.1–VI.7 are real, quantitative, falsifiable predictions — at laboratory / pattern-formation scales:

| Item | Prediction | Cosmological relevance |
|---|---|---|
| VI.1 Triad phase locking | Phase relations among the 24 modes | None stated |
| VI.2 Baseline-tension band | $D_{4}$ exists for a band of $\bar{\psi} (11.85$% scan fraction — see task 11, INCOMPLETE-EVIDENCE on reproducibility) | None stated; the band is a substrate parameter range, not a cosmological epoch |
| VI.3 Non-relativistic validity boundary | Where the non-relativistic limit holds | None stated |
| VI.4 Stability bound | CFL-type bound on the substrate dynamics | None stated |
| VI.5 Isotropy to fourth order | A prediction of *absence* (no anisotropy to fourth order) | None stated |
| VI.6 Defect spectrum | Which defects exist (dislocations yes; monopoles, skyrmions, hopfions no — line 924) | Defects are the one item with a cosmological analogue (see §6), but no cosmological mapping is stated |
| VI.7 Monopoles | Predicted, not excluded (see §V.3) | The monopole *problem* is inherited; the resolution is named, not derived |

The gap is specific and total: **the manuscript predicts patterns, not cosmologies.**

## 3. The null observable grid

Every row's IRH column is UNSTATED / ABSTAIN. The instrument column is the verified response that a future IRH prediction would have to survive — included so the grid is usable the day a prediction exists, and so the *scale* of the constraint is visible now. Instrument numbers were verified by `browser.search` in this workstream (citations given); the two most load-bearing rows (LVK, BK18) were re-verified by fresh searches in this session (§7).

| # | Observable | IRH prediction | Instrument / dataset (response) | Status |
|---|---|---|---|---|
| G1 | Stochastic GW background, $\Omega_{GW}(25$ Hz) | **UNSTATED — ABSTAIN** | LVK O1–$O4a: \Omega_{GW}(25$ Hz$) \leq 2.8\times10^{-9} (\alpha = 0)$, $\leq 2.0\times10^{-9} (\alpha = 2/3)$, 95% CL (PRX 16, 041023, 2026, DOI 10.1103/dlfv-z6m2). O1–O4c1 improves $\times1.3$–1.5. | ABSTAIN (no prediction to compare) |
| G2 | Stochastic GW background, mHz band, $h^{2}\Omega$ | **UNSTATED — ABSTAIN** | LISA: $h^{2}\Omega_{sens} ~10^{-12}$ at $10^{-2}$ Hz, ~$10^{-13}$ at $10^{-8}$ Hz; launch mid-2030s; $\Omega_{gw}$ as low as $6\times10^{-13}$ detectable in one month. | ABSTAIN |
| G3 | Stochastic GW background, nHz band (PTA) | **UNSTATED — ABSTAIN** | NANOGrav 15-yr: $A_{GWB} = 2.4^{+0}\cdot^{7}_{-0}\cdot_{6}\times10^{-15}$ at f = 1/yr, Hellings–Downs correlation, Bayes factor >$10^{14} ($ApJL 2023, arXiv:2306.16213). A background is *detected* in this band (astrophysical origin favoured); any IRH contribution would have to fit under it. | ABSTAIN |
| G4 | Phase-transition GW spectrum (bubble collisions / sound waves / turbulence) | **UNSTATED — ABSTAIN** | LVK O1–O4a first-order-phase-transition constraints are part of the same PRX 16, 041023 analysis (the paper constrains first-order phase transitions explicitly). | ABSTAIN — see §6 for what is missing |
| C1 | CMB scalar tilt $n_{s}$ | **UNSTATED — ABSTAIN** | Planck \$2018: n_{s} = 0.9649 \pm 0.0042 (A$&A 641, A10, 2020, arXiv:1807.06211). | ABSTAIN |
| C2 | CMB tensor-to-scalar ratio r | **UNSTATED — ABSTAIN** | Planck alone: $r_{0}$.002 < 0.10; +BK15: < 0.056. BICEP/Keck BK\$18: $r_{0}$$.05 < 0.036, $$\sigma(r) = 0.009$\$, 95% CL (PRL 127, 151301, 2021). Newer combination (Planck PR4 + BK18): r < 0.032. | ABSTAIN |
| C3 | CMB B-mode power (primordial) | **UNSTATED — ABSTAIN** | BK18 (above); CMB-S4 design $\sigma(r) < 5\times10^{-4}$. | ABSTAIN |
| C4 | CMB TT/EE power-spectrum modifications | **UNSTATED — ABSTAIN** | Planck 2018 TT/EE spectra (A&A 641, A10, 2020). No IRH modification stated; there is no IRH field that couples to photons (photon count 0, §1). | ABSTAIN |
| C5 | Monopole relic density | **UNSTATED (named, not derived) — ABSTAIN** | Preskill 1979 (PRL 43, 1365–1368): relic density far above the bound without dilution; Turner 1984: the universe would have reached 3 K at ~10,000 yr if monopoles dominated; Guth 1981 (PRD 23, 347–356): inflationary dilution. IRH §V.3 names "inflationary dilution, or a breaking pattern avoiding the relevant topology" and derives neither. | ABSTAIN — the one row where the manuscript names a resolution; no number follows from it |

**Reading the grid.** The instrument column is not a constraint on IRH today — it is a constraint on any future version of IRH that states a prediction. The grid's content is the *emptiness* of the IRH column, and that emptiness is itself the finding: a framework that claims to derive spacetime and particle physics states no observable in the two channels (GW, CMB) by which early-universe physics is actually tested.

## 4. Blockers — why a forward model is impossible today

Each blocker is gated to a manuscript passage. Removing any one blocker would not suffice; all of B1–B6 must be resolved before a GW or CMB number can be derived.

| # | Blocker | Manuscript gate |
|---|---|---|
| B1 | **No expansion history.** No scale factor, Hubble parameter, Friedmann equation, or temperature–time relation is stated. A GW spectrum needs a redshifting history; a CMB spectrum needs a recombination epoch. There is no epoch to attach either to. | Grep: "Hubble"/"Friedmann"/"scale factor" = 0 (§1). |
| B2 | **Dimensional assignment undecided.** §IX.2 options A/B/C (which dimensions are the substrate's, which are emergent) are open. A GW prediction needs to know which dimensions the waves propagate in. | §IX.2 (manuscript Part IX open problems; programme brief). |
| B3 | **Einstein equations not recovered; tensor sector unrecovered.** The effective metric "obeys the substrate's own equation of motion, not $G\mu\nu = 8\piT\mu\nu$" (§IX.3, lines 1376–1380), and "the two transverse-traceless graviton polarizations is a separate and substantially harder [problem]" (line 1383). Without TT polarizations there is no gravitational radiation to compute; without Einstein's equations there is no tensor power spectrum. | §IX.3, lines 1376–1383 (quoted verbatim in §1). |
| B4 | **No nucleation mechanism, no $\bar{\psi}$ mechanism.** The transition is first order (§II.9), so a phase-transition GW signal is *conceivable* — but "no mechanism sets $[\bar{\psi}$'s] value" and "what supplies the nucleation event?" is unanswered (§IX.5). A first-order GW spectrum needs the transition temperature T\*, the strength $\alpha$, and the inverse duration $\beta/H$; none is derivable from the stated functional without a nucleation rate. | §IX.5, lines 1406–1410; §II.9, line 641. |
| B5 | **No photon or baryon coupling.** "photon" = 0, "baryon" = 0 (§1). A CMB power spectrum is a statement about photons (and baryons, which source the acoustic peaks). With no coupling stated, there is no CMB observable to compute — not even in principle, from the manuscript as written. | Grep counts, §1. |
| B6 | **No stated cosmological initial conditions.** $\bar{\psi}$ is "an initial datum" (§IX.5); whether occupying the $D_{4}$ band is a prediction or a tuning "remains undetermined". A CMB prediction needs initial perturbations (a scalar spectrum, a tilt); the manuscript states none. | §IX.5, lines 1406–1410. |

## 5. Requirements for a future forward model

A future version of IRH (or a follow-up paper) that wanted to fill the grid would have to supply, in order:

1. **An expansion history** — a scale factor a(t) or Hubble H(t), or an explicit statement of what plays that role in the substrate picture (B1).
2. **A dimensional assignment** — resolve §IX.2 A/B/C (B2).
3. **A tensor sector** — recover the two TT graviton polarizations and state the equation they obey (B3). Until then, every GW row stays ABSTAIN.
4. **Einstein recovery or a stated replacement** — either derive $G\mu\nu = 8\piT\mu\nu$ or state the modified gravity the effective metric obeys, with its own tensor spectrum (B3).
5. **A nucleation mechanism and rate** — what nucleates the $D_{4}$ phase, at what temperature T\*, with what strength $\alpha$ and duration $\beta/H (B4)$. These three numbers are the entire input to a first-order phase-transition GW spectrum.
6. **A mechanism fixing $\bar{\psi}$** — or a stated prior over $\bar{\psi}$, so the $D_{4}$ band is a prediction rather than a tuning (B6).
7. **Photon and baryon couplings** — fields that couple to the substrate and source CMB anisotropies (B5).
8. **Initial perturbations** — a scalar spectrum (amplitude, tilt $n_{s})$ and a tensor spectrum (amplitude, ratio r), or a derivation of them from the substrate dynamics (B6).
9. **A monopole number** — either a dilution factor or a breaking pattern, turning §V.3's named resolution into a relic-density prediction (C5).

Items 3 and 5 are the binding constraints for GW; items 7 and 8 for CMB. Items 1–2 gate everything.

## 6. The one partial bridge — and why it does not reach the grid

**The bridge.** The transition is first order (§II.9), and VI.6 states a defect spectrum (dislocations exist; monopoles, skyrmions, hopfions do not — manuscript line 924). A first-order cosmological phase transition is the standard source of a stochastic GW background (bubble collisions, sound waves, turbulence), and the LVK O1–O4a analysis explicitly constrains first-order phase transitions (PRX 16, 041023, 2026). So the *shape* of a future IRH GW prediction is visible: it would be a phase-transition spectrum, not an inflationary one.

**Why it does not reach the grid.** A phase-transition GW spectrum is fixed by (T\*, $\alpha, \beta/H, v_{w})$ — transition temperature, strength, inverse duration, wall velocity. The manuscript supplies none of the four: T\* needs an expansion history and a nucleation rate (B1, B4); $\alpha$ needs the latent heat relative to the radiation density, which needs a radiation density (B1, B5); $\beta/H$ needs the nucleation rate's time dependence (B4); $v_{w}$ needs the bubble-wall dynamics in the substrate (unstated). The task-11 numbers (barrier $3.8585\times10^{-5}$ at $A_{max} = 0.00980059$, homogeneous; coexistence edges) are *substrate* energetics at fixed $r = -0.35$, $\bar{\psi} = -0.18$ — they are not $\alpha$, $\beta$, or T\*, and converting them would require the missing cosmology. **No GW number is computed in this report, and none can be, from the stated model.** The defect spectrum (VI.6) likewise has no stated cosmological mapping: defects in the substrate are not, without further argument, defects in spacetime.

## 7. Checks

| Check | Result |
|---|---|
| Extraction grep — "gravitational wave" = 0, "CMB"/"cosmic microwave" = 0, "photon" = 0, "baryon" = 0, "Hubble"/"Friedmann"/"scale factor" = 0 (1,638-line source, exit 0) | **PASS** |
| Control greps — "monopole" = 12, "inflation" = 1, "$D4/D_{4}$" = 83 (same file, same session) | **PASS** — the zeros are real, not a grep failure |
| Second independent check — predictions file VI.1–VI.7 headings re-grepped; none is GW/CMB | **PASS** |
| Verbatim blocker quotes — §V.3 (lines 1086–1090), §IX.3 (lines 1376–1383), §IX.5 (lines 1406–1410) | **PASS** — quoted in §1/§4 |
| Instrument numbers — LVK O1–O4a and BK18 re-verified by fresh `browser.search` this session (PRX 16, 041023, DOI 10.1103/dlfv-z6m2; PRL 127, 151301, 2021); LISA, NANOGrav, Planck, CMB-S4 verified by `browser.search` earlier in this workstream (citations in §3) | **PASS** |
| Forward model (GW spectrum / CMB power spectrum) | **NOT RUN — ABSTAIN.** No stated prediction exists to forward-model; computing one would require inventing a cosmology. |
| Second-tool check on the extraction | **PASS** — two independent greps (manuscript source + predictions file) agree; control greps confirm the tool works on this file. |

**Computation gate (truth-seeking-frontier v5).** No number in this report is computed by me: the extraction is a grep output (quoted with counts), the instrument numbers are literature values (cited, two re-verified this session), and the ABSTAIN is the absence of a computation. Nothing here is presented above CLAIMED.

## 8. HLRE grades per narrow claim

Independence is I1 throughout (one pipeline). Computation is F2 where a tool output is quoted (grep counts, browser.search), F1 where the claim is a judgement on the manuscript.

| ID | Claim | Grade | Basis |
|---|---|---|---|
| S1 | The manuscript states zero GW predictions ("gravitational wave" = 0) | C / I1 / F2 | Grep, this session, with working controls. |
| S2 | The manuscript states zero CMB predictions ("CMB"/"cosmic microwave" = 0) | C / I1 / F2 | Grep, this session, with working controls. |
| S3 | No photon or baryon coupling is stated ("photon" = 0, "baryon" = 0) | C / I1 / F2 | Grep, this session. |
| S4 | No expansion history is stated ("Hubble"/"Friedmann"/"scale factor" = 0) | C / I1 / F2 | Grep, this session. |
| S5 | VI.1–VI.7 contain no GW/CMB prediction | C / I1 / F2 | Predictions file read + headings re-grepped. |
| S6 | Every observable in the grid is UNSTATED / ABSTAIN for IRH | C / I1 / F1 | Follows from S1–S5. |
| S7 | Instrument sensitivities as quoted (§3) | C / I1 / F2 | Literature values; LVK + BK18 re-verified this session, the rest verified earlier in this workstream. |
| S8 | Blockers B1–B6, each gated to a manuscript passage | C / I1 / F1 | Verbatim quotes in §1/§4. |
| S9 | Requirements list (§5) for a future forward model | C / I1 / F1 | Judgement on what a forward model needs, given B1–B6. |
| S10 | No GW number can be derived from the stated model (phase-transition parameters T\*, $\alpha, \beta/H, v_{w}$ all unstated) | C / I1 / F1 | Follows from B1/B4 + the stated functional's contents. |

**Worst-of computation:** all positive claims are C. **Overall: C (Track E), I1, F2.** The ABSTAIN is the report's central result and is not a grade — it is the correct output for a task whose input does not exist.

## 9. Rival / failure mode; evidence that would change the answer

**Rival reading.** "The manuscript's first-order transition *implies* a GW signal, so a spectrum can be estimated by analogy with standard phase-transition templates." Rejected: a template needs (T\*, $\alpha, \beta/H, v_{w})$, and the manuscript supplies none of the four. Plugging in fiducial values from another model (e.g. an electroweak-scale T\*) would be inventing a cosmology, not forward-modelling IRH. The same rejection applies to any CMB estimate: without a photon coupling, there is no spectrum to modify.

**Failure modes.** (a) The extraction missed a prediction stated in different words — e.g. a GW prediction phrased without the words "gravitational wave". Mitigation: the grep covered the predictions file in full (VI.1–VI.7, read cover-to-cover earlier in this workstream), the functional contains no tensor sector (one "tensor" mention, the effective-metric passage), and the manuscript's own Part IX lists what is open rather than what is predicted. A differently-worded prediction would still have to appear in VI.1–VI.7 or in the functional; it appears in neither. (b) A newer manuscript version states a prediction — this report is about v93.1 as retrieved; a v94+ would need a fresh extraction. (c) An instrument number is superseded — the BK18 row already carries the newer Planck PR4+BK18 combination (r < 0.032) as a footnote; the grid's IRH column is unaffected by any instrument update.

**Evidence that would change the answer.** (i) A manuscript passage stating a GW spectrum, a tensor-to-scalar ratio, a scalar tilt, or a CMB modification — the grid would gain a prediction column and the forward model would become computable. (ii) Resolution of any single blocker B1–B6 in a stated, derived form (not a named intention) — the requirements list (§5) would shorten by that item. (iii) A stated nucleation rate with T\*, $\alpha$, $\beta/H$ — the phase-transition GW spectrum (G4) would become computable with a standard template, and the LVK O1–O4a first-order-phase-transition constraints would then bite. Until then, the honest grid is all ABSTAIN.

## VERIFIED / UNVERIFIED / FAILED

**VERIFIED (grade C, I1 — see §8):**
- S1 — zero GW predictions stated.
- S2 — zero CMB predictions stated.
- S3 — no photon or baryon coupling stated.
- S4 — no expansion history stated.
- S5 — VI.1–VI.7 contain no GW/CMB prediction.
- S6 — every observable in the grid is UNSTATED / ABSTAIN for IRH.
- S7 — instrument sensitivities as quoted.
- S8 — blockers B1–B6, each gated to a manuscript passage.
- S9 — requirements list for a future forward model.
- S10 — no GW number derivable from the stated model.

**UNVERIFIED:**
- (none — the extraction is complete; there is no partially-verified prediction to list.)

**FAILED (claims that did not survive checking):**
- The task's presupposition that IRH states GW signatures and CMB power-spectrum modifications to forward-model — **FAILED on extraction**: the terms occur 0 times and VI.1–VI.7 contain no such prediction. The forward model is therefore ABSTAINED, not merely unattempted.
- Any phase-transition GW estimate from the task-11 barrier numbers — **FAILED as a derivation**: the barrier is substrate energetics at fixed (r, $\bar{\psi})$, not (T\*, $\alpha, \beta/H)$; the conversion needs the missing cosmology (B1, B4).

**Sources on disk:** manuscript source `IRH_v93_1_source_rebuilt.txt` (1,638 lines, sha256 cebc3b6f010ed9c059129b4b0ff2c9e3a8ea858e74adc68c3e7fd7d9f34affa8, per programme brief); predictions file `~/workspace/research/IRH-Theory-Development-Workspace/predictions/VI-predictions.md`; task-11 data and report (`11-bifurcations-report.md`, `data/bifurcation_values.json`) for the substrate numbers cited in §6.
