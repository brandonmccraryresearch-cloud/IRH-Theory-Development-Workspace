# Task 14 — Map of quantum-gravity researchers, Asymptotic Safety, and IRH

**Workstream E (cosmology map), IRH Co-scientist task programme**
**Date:** 2026-11-10
**Mode:** deepest-research **full mode** (stated plainly; not systematic review — the review form was set by the task order, which specified deepest-research full mode for this task; no systematic-review protocol was used).
**Protocol:** cross-domain-discovery S1–S7 (see §1 for the protocol record, including the S5/S6/S7 deviations).
**Comparison target (fixed, not re-litigated):** IRH v93.1 (McCrary, Zenodo DOI 10.5281/zenodo.22821689, 18 Sep 2026, verified by direct open in this session) — 4D oscillatory substrate selects $a D_{4}$ standing-wave pattern by triad-resonance interference $(S = \tau^{2}/q_{4} = 64/141)$; gauge algebra $E_{6}$ via 2T/McKay; SO(8) excluded; three generations are INPUT, not derived; first-order transition; does NOT recover Einstein's field equations (effective metric only) and states NO gravitational-wave or CMB prediction. Open questions: what fixes the mean field $\bar{\psi}$, and what supplies the nucleation event.
**Judgement criteria (structural only, never surface vocabulary):** (1) substrate ontology — a physical substrate/microstructure from which spacetime/geometry emerges, vs spacetime fundamental/quantised directly; (2) selection mechanism — a dynamical principle picking a preferred structure (lattice, geometry, vacuum) out of alternatives; (3) testable predictions — falsifiable, quantitative predictions stated, and what they are.

## CLAIM + STATUS

**CLAIM.** On the three stated structural criteria, no retrieved approach is close to IRH on all three at once. The closest matches split by criterion:

- **Substrate ontology — closest: group field theory (GFT) condensate cosmology** (Oriti & Pang 2025; Calcinari et al. 2026): a condensate of pre-geometric quanta from which a cosmological spacetime emerges hydrodynamically. Runner-up: Volovik's helium-droplet universe (quantum-liquid substrate, but selection is Fermi-point topology, not resonance).
- **Selection mechanism — closest: the Alexander–McTague / Lifshitz–Petrich pattern-formation lineage** (Alexander & McTague 1978; Lifshitz & Petrich 1997; Faraday-wave experiments): the same triad-counting selection IRH uses — a cubic term nonzero only for closed zero-sum triads on an unstable shell, maximising the triad count selects the pattern. This is a mechanism-level affinity that passes the Bartha critical-disanalogy gate (§4, Gate 2). It is not a quantum-gravity approach: it has no substrate claim about spacetime.
- **Testable predictions — strongest: Asymptotic Safety** (Higgs mass $\approx 126$ GeV pre-discovery, Shaposhnikov–Wetterich 2010; seesaw-scale bound ~$10^{14}$ GeV and Weinberg-operator exclusion, de Brito et al. 2025; proton-decay suppression, Eichhorn & Ray 2024). AS is simultaneously **furthest from IRH on substrate ontology** (it quantises the metric directly; no substrate).
- **IRH is alone in the (substrate 2, selection 2) corner** of the scorecard (fig. 5). That isolation is a structural fact about the retrieved literature, not evidence for IRH: the two criteria are satisfied together only by IRH itself, and IRH's own predictions are the weakest cosmologically (no GW/CMB prediction stated; VI.1–VI.7 predictions are quantitative but untested and partly conditional).

**STATUS: MAP COMPLETE.** Synthesis of 73 retrieved papers (3 slices, 63 queries, §2). Every affinity verdict passed or failed through the Bartha critical-disanalogy gate (§4). Grade ceiling applies: **Track E C / I1** for the whole map (cross-domain-discovery skill cap, until a human runs the source/balance gates; independence is I1 — one retrieval pipeline, shared by the three slices and this synthesis). No claim in this report is graded above C. Two new findings for the programme are flagged in §7 (a load-bearing caveat on IRH's 3D BCC validation, and a version-dependence of IRH's own selection principle).

## 1. Protocol record (cross-domain-discovery S1–S7)

| Stage | What was done | Verdict |
|---|---|---|
| S1 — Facets | BPMF facets for IRH and the comparison set (§3, Table 0). | DONE |
| S2 — Retrieval | Three parallel deepest-research slices: A (Asymptotic Safety, 16 queries, 22 papers), B (emergent/discrete/analogue, 19 queries, 25 papers), C (pattern formation + IRH, 28 queries, 26 entries). Retrieval notes on disk: `data/lit-slice-A-asymptotic-safety.md`, `data/lit-slice-B-emergent-discrete.md`, `data/lit-slice-C-pattern-irh.md`. Every paper verified to exist via a search result or an opened arXiv/DOI page; no paper listed from memory alone. | DONE |
| S3 — Structural alignment | Scorecard on the three stated criteria (§5, Table 1), fig. 5. Alignment done on structure (substrate, selection, predictions), not vocabulary. | DONE |
| S4 — Bartha articulation | Hesse matrices + critical-disanalogy gate for each affinity claim (§4). | DONE |
| S5 — Blending | **NOT RUN — by design, with reason.** A blendoid would combine approaches into one model; the gated affinities are partial and mutually incompatible at the critical-feature level (e.g. GFT's quantum condensate and IRH's classical oscillatory field cannot be blended without discarding the feature that makes each what it is). This report is a comparison map, not a model-building exercise; no blendoid is claimed. | NOT RUN (reason stated) |
| S6 — Tournament | **NOT RUN — no candidates to evolve.** The skill's S6 evolves candidate blends by tournament; with S5 not run there are no blends, and a tournament over *approaches* would rank them on a single scale the three criteria deliberately refuse to collapse. The ranking that exists is per-criterion (§5). | NOT RUN (reason stated) |
| S7 — Formal verification | **NOT RUN — claims are comparative/historical, not formal.** No Lean/Z3 formalisation of an affinity judgement was attempted; the DVP guard is not applicable to literature-comparison claims. The only formal-adjacent checks in this report are the OpenAlex counts (§2, tool output) and the scorecard arithmetic (fig. 5 generation script, exit 0). | NOT RUN (reason stated) |

**Grade ceiling (skill-imposed):** Track E C / Track F F3 until a human runs the source/balance gates. The companion system prompt was offered once on invocation and never imposed (design claim, ungraded). **Independence: I1** — the three retrieval slices and this synthesis share one pipeline and one authoring agent; the only independence present is that three separate retrieval runs were made and their preliminary verdicts were re-gated here rather than adopted.

**Literature-search note (deepest-research full mode).** The retrieval was done by three parallel subagents (one per slice) under a fixed comparison target and fixed criteria, then synthesised here with the Bartha gates run by me. The slices' preliminary verdicts are the retrievers', not yet gated — the gates in §4 are mine, and where a gate changes a preliminary verdict that is stated. Coverage is bounded by the queries run (63) and the sources retrieved (73 papers); an approach not retrieved is not scored. The newest item retrieved is June 2026 (Eichhorn 2026 review, arXiv:2606.21522; Koch et al. 2026, arXiv:2606.22408).

## 2. Retrieval record and publication-volume proxy

**Queries:** A: 16, B: 19, C: 28 (listed in full in the slice notes). **Papers/entries:** A: 22 (+4 contested/counterpoint), B: 25, C: 26. **Total: 73.**

**OpenAlex volume proxy (fig. 6).** Text-search hit counts for 2023-01-01 onward, run in this session via the project OpenAlex connector (HTTP 200, exit 0):

| Query | Hits |
|---|---|
| asymptotic safety quantum gravity | 1,758 |
| loop quantum gravity | 28,665 |
| causal dynamical triangulations | 22,759 |
| group field theory quantum gravity | 35,600 |
| emergent gravity Verlinde | 1,918 |
| analogue gravity | 27,786 |
| causal set theory quantum gravity | 11,485 |
| string theory swampland | 2,488 |

**Caveat (load-bearing):** these are **broad text-search matches, NOT a curated field census.** A query like "group field theory" matches any record containing those words; the counts inflate for generic phrases and undercount for approaches with fragmented terminology (AS is a sub-field of a larger FRG literature; "emergent gravity" is also a phrase used outside Verlinde's programme). The counts support only a coarse ordering — LQG/CDT/GFT/analogue are large literatures, AS and Verlinde-emergent-gravity are small by comparison — and no claim in this report depends on a small difference between two counts. Do not cite these numbers as field sizes.

**IRH's own standing in the literature (retrieved, §6 of slice C):** the Zenodo v93.1 record was verified by direct open (DOI 10.5281/zenodo.22821689, 18 Sep 2026). **No independent work citing or discussing IRH was found** in the retrieval (search-bounded absence, grade INCOMPLETE-EVIDENCE — see M8). **No findable Wise Journal revision record** was found (M9, INCOMPLETE-EVIDENCE). A same-author SSRN predecessor was found (see §7, finding F2).

## 3. S1 — BPMF facets

| Facet | IRH v93.1 | The comparison set (summary; per-approach detail in §5–§6) |
|---|---|---|
| **Background** | Planar Jacobian-conjecture programme (GGHV 72,108 elimination); IRH is the author's theoretical-physics programme. $D_{4}$ substrate, $E_{6}$ gauge algebra. | Quantum gravity: the problem of a UV-complete, background-independent theory of gravity; emergence programmes: the problem of deriving spacetime from something that is not spacetime. Pattern formation: the problem of which periodic/quasiperiodic pattern a system selects at onset. |
| **Purpose** | Derive spacetime, gauge structure, and particle content from a single oscillatory substrate with a parameter-free selection principle. | QG: UV completion + recovery of GR. Emergence: derive geometry from pre-geometric constituents. Pattern formation: predict the selected pattern from the free energy / amplitude equations. |
| **Mechanism** | Standing-wave substrate; triad-resonance interference; $S = \tau^{2}/q_{4}$ maximised selects $D_{4} (64/141)$; first-order transition; mean field $\bar{\psi}$ is an input. | AS: RG fixed point + finite critical surface. LQG: quantised spin networks + spin-foam sum. CDT: Monte Carlo over causal triangulations; phase diagram. GFT: condensate of pre-geometric quanta; hydrodynamics. Causal sets: discrete partial order; manifoldlikeness by suppression. String: compactification + swampland exclusion. Verlinde: entropic force from holographic information. AM/LP: cubic triad counting on an unstable shell. |
| **Findings** | $D_{4}$ selected (S = 64/141); $E_{6}$ via 2T/McKay; SO(8) excluded; three generations INPUT; effective metric only (no Einstein equations); no GW/CMB prediction; VI.1–VI.7 quantitative predictions (band, CFL bound, isotropy, defect spectrum) untested. | AS: fixed-point evidence across truncations, contested on measure grounds; Higgs $\approx 126$ GeV (pre-discovery). CDT: extended de Sitter-like phase emerges; UV fixed point unproven. GFT: bounce + emergent dark sector (2026). Verlinde: sharp acceleration scale; tests mixed. Analogue: lab Hawking radiation confirmed (2019). AM/LP: triad selection quantitatively predictive at lab scales; AM's BCC solutions argued unstable (Klein 2001). |

## 4. S4 — Bartha critical-disanalogy gates

Method (per the skill): for each claimed affinity, state the source's prior association (the derivation linking the positive analogy to the prediction), the Hesse matrix (Positive / Negative / Neutral / Hypothetical analogy), then the critical-disanalogy check: **if any critical feature of the source's derivation lies in the Negative Analogy, the transfer FAILS.** A gate that passes means the affinity holds at the stated level (ontology, mechanism, or predictions) — not that the approaches are equivalent.

### Gate 1 — GFT condensate cosmology $\leftrightarrow$ IRH (substrate ontology). **PASSES at the ontology level; FAILS at the mechanism level.**
- **Prior association (GFT):** pre-geometric quanta (tetrahedra / spin-network nodes) condense; the condensate's hydrodynamics *is* the emergent cosmological spacetime (Oriti & Pang 2025; Calcinari et al. 2026). The prediction (bounce, emergent dark sector) follows from the condensate + interaction structure.
- **Hesse matrix.** Positive: spacetime is not fundamental; it emerges from constituents that are not themselves spacetime; the emergent regime is collective/hydrodynamic; cosmology is the hydrodynamics of the substrate. Negative: GFT's constituents are *quantum* (quanta of geometry, a condensate with relational time); IRH's substrate is a *classical oscillatory field* with a standing wave; GFT selects a hydrodynamic regime, IRH selects a discrete lattice pattern; GFT has no triad-resonance selection. Neutral: the specific microscopic couplings; the dimensionality of the emergent space. Hypothetical: whether a GFT condensate could select a preferred lattice pattern (no such mechanism is stated).
- **Critical-disanalogy check.** The ontology transfer rests on the critical feature "spacetime emerges from pre-geometric constituents" — that feature is in the Positive Analogy for both, so the **ontology affinity passes**. The mechanism transfer would need "condensation selects the pattern" — condensation is not a pattern-selection mechanism in GFT, and triad resonance is not a condensation mechanism in IRH, so the **mechanism affinity fails**.
- **Verdict: closest to IRH on substrate ontology; not close on selection.** This is the strongest cross-approach affinity in the map, and it is partial.

### Gate 2 — Alexander–McTague / Lifshitz–Petrich lineage $\leftrightarrow$ IRH (selection mechanism). **PASSES at the mechanism level; FAILS at the ontology level.**
- **Prior association (AM):** in a Landau free energy with a cubic term, the cubic term is nonzero only for closed zero-sum triads on the unstable shell; maximising the number of such triads selects the pattern (BCC in 3D). The prediction (which lattice) follows from counting triads.
- **Hesse matrix.** Positive: cubic term; zero-sum triads on a shell of unstable modes; selection by maximising the triad count; the same ratio structure $(\tau^{2}/q_{4}$ in IRH is the direct analogue of AM's triad-counting argument); amplitude-equation / Landau structure. Negative: AM's substrate is a liquid density field (a material), not a spacetime substrate; AM selects BCC in 3D, IRH applies the argument in 4D to select $D_{4}$; AM makes no claim about spacetime, gravity, or particle physics. Neutral: the specific values of the Landau coefficients. Hypothetical: whether the 4D extension of the AM argument is stable (see the Klein caveat, §7 F1).
- **Critical-disanalogy check.** The mechanism transfer rests on the critical features "cubic term + closed triads + triad-count maximisation" — all in the Positive Analogy, and they are the features that do the selecting in both. No critical feature of the AM derivation lies in the Negative Analogy *at the mechanism level*. The ontology transfer fails (material density vs spacetime substrate), but that is a different claim.
- **Verdict: closest to IRH on selection mechanism — a genuine structural cousin, and the only gate in this report that passes at the mechanism level.** Caveat: the 3D ancestor result itself is contested (Klein 2001 argues AM solutions are unstable; §7 F1), which bears on IRH's 3D BCC recovery claim, not on the structural affinity.

### Gate 3 — Asymptotic Safety $\leftrightarrow$ IRH (selection). **FAILS as a pattern-selection affinity; PASSES only at the abstract "dynamical selection" level.**
- **Prior association (AS):** a non-Gaussian UV fixed point with finitely many relevant directions selects the UV-critical surface; fixed-point boundary conditions constrain couplings (Higgs quartic $\to m_{H} \approx 126$ GeV; Weinberg operator excluded; some scalar-tensor fixed points ruled out by inflation).
- **Hesse matrix.** Positive: a dynamical principle does real selection work; it excludes alternatives (matter contents, fixed points) and fixes numbers. Negative: the selected objects are RG trajectories / couplings / models, not spatial patterns or lattices; there is no substrate; the mechanism is renormalisation-group flow in theory space, not interference on a shell; the fixed point itself is contested on measure grounds (Branchina et al. 2024 vs Held et al. 2025, unresolved).
- **Critical-disanalogy check.** The transfer "AS's selection is like IRH's selection" would need the critical feature "a preferred spatial pattern is picked out of alternatives" — that feature is absent from AS entirely (Negative Analogy). What is shared is only the abstract noun "dynamical selection". **The affinity fails at every level except the abstract one**, which is too thin to count as closeness.
- **Verdict: furthest from IRH on ontology; strongest on stated quantitative predictions; selection affinity is nominal only.**

### Gate 4 — CDT $\leftrightarrow$ IRH (selection + emergence). **PARTIAL: passes at "phase-diagram selection", fails at the mechanism and ontology levels.**
- **Prior association (CDT):** Monte Carlo over causal triangulations yields a phase diagram; the extended de Sitter-like phase is dynamically selected; the spectral dimension flows $4\to2$; the continuum limit is a candidate UV fixed point (Ambjørn et al. 2024).
- **Hesse matrix.** Positive: a phase is dynamically selected from alternatives; geometry emerges from discrete building blocks; spectral-dimension flow. Negative: the building blocks are a lattice *regulator*, not a claimed physical substrate; the selected object is a spacetime phase (de Sitter-like), not a lattice pattern; the mechanism is statistical (path-integral sum), not interference; the UV fixed point is unproven.
- **Verdict: weak/partial affinity at the level of "a phase is selected in a phase diagram". The mechanism (statistical vs interference) and the ontology (regulator vs physical substrate) both fail the gate.**

### Gate 5 — Volovik (helium droplet$) \leftrightarrow$ IRH (substrate ontology). **PASSES at the ontology level; FAILS at the mechanism level.**
- **Prior association (Volovik):** a quantum liquid $(^{3}$He) is the vacuum; low-energy excitations see an effective metric and effective gauge fields; particle physics is the low-energy physics of the liquid.
- **Hesse matrix.** Positive: an explicit physical substrate; spacetime/metric emergent, not fundamental; the emergent metric is effective (the same limitation IRH states — no Einstein equations recovered). Negative: the substrate is a quantum liquid with Fermi-point topology; selection is by topology/universality class, not by triad resonance; no lattice pattern is selected; the programme is an analogy programme (the liquid is a model of the vacuum, and the claim that our vacuum *is* such a liquid is the contested step).
- **Verdict: partial ontology affinity (the only other explicit-substrate programme in the map besides GFT and IRH); mechanism affinity fails.**

### Gates 6–12 (compact)

| Gate | Affinity claim | Prior association (source) | Critical disanalogy | Verdict |
|---|---|---|---|---|
| 6 — Wolfram model $\leftrightarrow$ IRH | Pre-geometric hypergraph substrate; causal invariance selects the GR regime | Rewrite rules + causal invariance $\to$ emergent GR; multiway structure | No pattern selection (no preferred lattice picked); substrate is combinatorial rewrite, not oscillatory field; no testable prediction stated | **Ontology partial; mechanism FAILS** |
| 7 — Verlinde emergent gravity $\leftrightarrow$ IRH | Entropic force from holographic information; fixed acceleration scale $a_{M}$ | Entropy/information $\to$ gravity as entropic force; $a_{M}$ is sharp and testable | Substrate unspecified (microscopic theory not stated); no selection mechanism at all; only the label "emergent gravity" is shared | **No structural affinity** (label only) |
| 8 — Analogue gravity $\leftrightarrow$ IRH | Literal substrate (BEC, water tank) with an emergent acoustic metric; lab Hawking radiation confirmed | Acoustic metric from fluid flow; Hawking radiation in the lab (Muñoz de Nova et al. 2019, Nature 569, 688) | The substrate is *avowedly analogue* — a laboratory model, not a claim about our spacetime's substrate; the critical feature "the substrate IS our spacetime's substrate" is in the Negative Analogy | **Ontology affinity is FALSE as a claim about our universe** (real lab substrate, wrong referent) |
| 9 — Causal sets $\leftrightarrow$ IRH | Discrete "atoms of spacetime"; manifoldlikeness by suppression of non-manifoldlike causets | Partial order + sprinkling; everpresent $\Lambda$ order-of-magnitude | The causet IS spacetime (discrete), not a medium underneath it; selection is suppression of non-manifoldlikeness, not pattern selection; no preferred lattice | **Weak affinity on discreteness only; substrate and selection FAIL** |
| 10 — LQG / spin foams $\leftrightarrow$ IRH | Relational, emergent spacetime from spin networks; bounce scenarios | Quantised geometry; sum over spin foams; continuum limit as the open problem | No substrate (spin networks are quantised geometry itself); no selection of a preferred geometry; semiclassical limit unrecovered; no quantitative prediction stated in retrieved sources | **No structural affinity** |
| 11 — String landscape / swampland $\leftrightarrow$ IRH | Selection among vacua | Swampland conjectures exclude EFTs/vacua; landscape is vast | Selection is *exclusion*, not dynamics — nothing picks our vacuum; no substrate; conjectures unproven; dS vacua construction (30 candidates) has stability unestablished | **No structural affinity** (exclusion $\neq$ dynamical selection) |
| 12 — PFC / Swift–Hohenberg $\leftrightarrow$ IRH | Amplitude-equation pattern selection (same mathematical class as IRH's free energy) | Free-energy minimisation over periodic states via triadic/quartic resonances; quantitative materials predictions | Substrate is a material density field, not spacetime; no spacetime-emergence claim; the affinity is to IRH's *mathematical* mechanism, not its physics | **Mechanism-family affinity (same math class); ontology FAILS** — this is where IRH's mechanism sits in the wider literature |

**Summary of the gates.** Two affinities pass at a stated level: GFT on ontology (Gate 1) and AM/LP on mechanism (Gate 2); Volovik passes on ontology (Gate 5); CDT passes only at the thin "phase-diagram selection" level (Gate 4). Everything else fails or is partial-to-nominal. No approach passes on both ontology and mechanism — IRH occupies the (2,2) corner alone (fig. 5).

## 5. S3 — Structural scorecard

Scores: 0 = absent, 1 = partial (regime/coupling/exclusion selection; unspecified or analogue substrate; parameter-dependent or untested predictions), 2 = present (pre-geometric substrate; dynamical pattern selection; sharp quantitative predictions). Halves are not used. Each score is justified in the "Basis" column from the retrieved sources; the scores are judgements, not measurements — that is why the whole table is grade C.

**Table 1 — Scorecard (fig. 5 plots the first two columns; marker size = third column).**

| Approach | (1) Substrate | (2) Selection | (3) Predictions | Basis (one line each) |
|---|---|---|---|---|
| **IRH v93.1** | **2** | **2** | **1** | Oscillatory substrate, explicit; triad interference selects $D_{4}$, parameter-free; VI.1–VI.7 quantitative but untested, and no GW/CMB prediction. |
| GFT condensate cosmology | 2 | 1 | 1 | Pre-geometric quanta condense; condensate hydrodynamics = emergent cosmology; no specific pattern selected; dark-sector ratio constrains couplings (model-dependent). |
| Wolfram model | 2 | 1 | 0 | Pre-geometric hypergraph; causal invariance selects the GR *regime*, not a structure; no quantitative prediction stated. |
| Volovik (He droplet) | 2 | 0 | 1 | Quantum-liquid substrate, explicit; selection is Fermi-point topology, not pattern selection; analogue-gravity programme predictions, no quantitative cosmological number verified. |
| Verlinde emergent gravity | 1 | 0 | 2 | Microscopic substrate unspecified; no selection; fixed acceleration scale $a_{M}$, sharp and tested (mixed results). |
| Analogue gravity | 1* | 0 | 1 | *Laboratory substrate is real but avowedly analogue — as a claim about our spacetime it scores 0; plotted at 1 with the asterisk. No selection; lab Hawking radiation confirmed. |
| Causal sets | 0 | 1 | 1 | Atoms of spacetime, not a medium underneath it; suppression of non-manifoldlike causets; everpresent $\Lambda ($order-of-magnitude) + Higgs-mass shift. |
| CDT | 0 | 1 | 0 | Triangulations are a regulator, not a substrate; phase diagram selects the extended phase; no quantitative prediction. |
| String / swampland | 0 | 1 | 1 | No substrate; selection is exclusion of EFTs/vacua; dS conjecture in-principle falsifiable but unproven and contested. |
| Asymptotic Safety | 0 | 1 | 2 | Metric quantised directly, no substrate; fixed point selects trajectories/couplings and excludes matter contents; Higgs $\approx 126$ GeV (pre-discovery) + sharp exclusions. |
| LQG / spin foams | 0 | 0 | 0 | Quantised geometry itself; no selection of a preferred geometry; semiclassical limit open; no quantitative prediction in retrieved sources. |
| Kibble–Zurek | 0 | 0 | 1 | Vacuum/order-parameter field on background spacetime; defects are the *failure* to select uniformly; defect-density scaling, lab-tested. |
| AM / Lifshitz–Petrich (pattern formation) | 0 | 2 | 2 | Material density field, no spacetime claim; triad-count selection — the same mechanism as IRH's; quantitative, lab-confirmed (Faraday dodecagonal, soft quasicrystals). |

![Structural scorecard](figures/fig5_researcher_map.png)

![OpenAlex volume proxy](figures/fig6_openalex_counts.png)

**Reading the map.** IRH is the only entry at (2,2). Its nearest neighbours are not quantum-gravity programmes: the mechanism neighbour is a condensed-matter lineage (AM/LP), and the ontology neighbour is GFT condensate cosmology. The large quantum-gravity programmes (LQG, AS, string) cluster at substrate 0 — they quantise spacetime or exclude vacua rather than deriving spacetime from a substrate. AS is the mirror image of IRH on criteria (1) and (3): strongest predictions, no substrate. The map's honest reading is that **IRH's combination (substrate + pattern selection) has no counterpart in the retrieved quantum-gravity literature** — which is a statement about the literature, not about IRH's correctness.

## 6. Researcher / group map (Table 2) and where the field is heading

Groups are listed only where a retrieved source states the affiliation (slice notes). "Direction" is the retrievers' summary of the retrieved 2023–2026 literature, re-checked against the papers in the tables.

| Approach | Groups (verified affiliations) | Key recent papers (from the slices) | Direction 2023–2026 |
|---|---|---|---|
| Asymptotic Safety | Heidelberg (Pawlowski; Eichhorn until move); Mainz (Reuter, Ripken); Sussex (Litim, Reichert); CP3 Odense (Eichhorn); Perimeter/Nordita (Knorr); Radboud Nijmegen (Saueressig); Catania/INAF (Bonanno); NBI + Jagiellonian (CDT flank: Ambjørn, Gizbert-Studnicki, Görlich) | Eichhorn 2026 review arXiv:2606.21522; Fehre et al. 2023 PRL 130, 081501; D'Angelo 2024 PRD 109, 066012; Saueressig & Wang 2025 PRD 111, 106007; de Brito et al. 2025 arXiv:2505.01422; Branchina et al. 2024 arXiv:2412.14108 vs Held et al. 2025 arXiv:2504.12006 | **Lorentzian convergence:** three Lorentzian formulations (covariant FRG, foliated/ADM, spectral FRG) now agree at Einstein–Hilbert level. **Phenomenology push:** the 2026 review consolidates predictions (Higgs, seesaw, proton decay, inflation constraints). **Contested:** the fixed point's existence is challenged on measure grounds; the dispute is live, not settled. |
| LQG / spin foams | Aix-Marseille + Western Ontario (Rovelli, Vidotto); ENS Lyon (Livine); Jena (Steinhaus); Perimeter/Erlangen (Bahr, Dittrich); Penn State (Ashtekar school, LQC) | Rovelli & Vidotto 2022 arXiv:2211.06718; Steinhaus 2020 Front. Phys. 8:295 | **Coarse-graining is the open problem:** the semiclassical/continuum limit is still not recovered; work is methodological (tensor-network RG, boundary data). No quantitative prediction has emerged. |
| CDT | NBI (Ambjørn); Radboud/Perimeter (Loll); Jagiellonian Kraków (Gizbert-Studnicki, Görlich, Németh) | Ambjørn et al. 2024 PRD 110, 126006; Ambjørn et al. 2024 arXiv:2411.02330; Loll 2019 arXiv:1905.08669 | **Contact with FRG maturing:** CDT effective action matched against FRG; UV fixed point allowed but unproven. **ML phase mapping** (phase boundaries, transition order) is the newer direction. |
| Causal sets | Perimeter (Sorkin, founder); Imperial (Dowker); Raman Research Institute (Surya); UC Davis (Carlip); Glaser, Zalel | Sorkin 2003 (foundational); Dowker et al. (everpresent $\Lambda)$; Glaser & Surya (phenomenology); Zalel (Higgs) | **Phenomenology is the live edge:** everpresent $\Lambda$ and a Higgs-mass shift are the quantitative claims; the programme remains small and foundationally focused. |
| GFT / tensor models | Complutense Madrid (Oriti); Bordeaux (Carrozza); Heidelberg (Gurau); Southern Denmark (Eichhorn); Kavli IPMU/OIST (Marchetti); Pithis, Gielen | Oriti & Pang 2025 arXiv:2502.12419; Calcinari et al. 2026 arXiv:2609.04328; Carrozza 2024 arXiv:2404.07834; Eichhorn et al. 2025 arXiv:2501.10307 | **Condensate cosmology is the growth area:** from free models (bounce) to interacting models (dark matter + dark energy from one mechanism, 2026). This is the fastest-moving emergence programme in the retrieved set, and the closest to IRH on ontology. |
| Verlinde emergent gravity | Amsterdam (E. P. Verlinde); testers: Sejong (Yoon & Hwang), weak-lensing groups (Brouwer et al.), wide binaries (Chae) | Verlinde 2017 arXiv:1611.02269; Yoon & Hwang 2025 arXiv:1909.01734 (factor-2/3 correction); weak-lensing and wide-binary testers named in slice B (Brouwer et al.; Chae) without individually verified papers | **Tests are mixed and the programme is stalled as a theory:** rotation curves fit in the outer regions, clusters/dwarfs fail without extra dark components; the 2025 correction (factor 2/3, $a_{M}$ = cH${}_{0}/9)$ is a defensive refinement, not a new prediction. |
| Analogue gravity | IAA Granada (Barceló); SISSA Trieste (Liberati); Victoria Univ. Wellington (Visser); Technion (Steinhauer, BEC); Nottingham (Weinfurtner, water tanks) | Barceló et al., Living Rev. Relativ. 29, 2 (2026; arXiv:gr-qc/0505065, v4 2024); Muñoz de Nova et al. 2019, Nature 569, 688 (Hawking radiation in a BEC analogue; Steinhauer group) | **Now a laboratory science:** Hawking radiation in BECs is confirmed; the programme's direction is precision analogue experiments, not a claim about our spacetime. It is the most empirically successful emergence-adjacent programme and the least relevant to IRH's claim. |
| String / swampland | (Broad; no single group verified in this retrieval — the slice lists the literature, not a group map) | Palti 2019 arXiv:1903.06239; Lüst et al. 2024 (dS vacua, 30 candidates); de Alwis et al. (dS critique); Van Riet (swampland vs dS) | **dS vacua construction vs swampland tension is unresolved:** 30 de Sitter candidates claimed (2024), stability unestablished, and the dS conjecture would forbid them. The field is arguing about its own consistency, not converging. |
| Pattern formation (AM/LP lineage) | No affiliations verified in this retrieval (slice C states none); authors: Alexander & McTague; Lifshitz & Petrich; Edwards & Fauve; Arbell & Fineberg; Haataja (Princeton group page, PFC) | Alexander & McTague 1978 PRL 41, 702; Lifshitz & Petrich 1997 PRL 79, 1261; Edwards & Fauve 1993 PRE 47, R788; Wu, Plapp & Voorhees 2010 arXiv:1008.4019; Elder et al. 2002 PRL 88, 245701 | **Quantitatively predictive and experimentally confirmed at lab scales; no cosmological application.** The mechanism IRH borrows is the best-tested selection mechanism in the map — and the one whose 3D ancestor result is contested (Klein 2001, §7 F1). |
| IRH | Independent (McCrary); Zenodo v93.1, 18 Sep 2026 | McCrary v93.1 (Zenodo DOI 10.5281/zenodo.22821689); SSRN predecessor (selection principle: maximal cymatic complexity $\to$ dimension 8) | **No independent engagement found** in this retrieval (M8). The programme's next steps per the manuscript are the IX open problems (nucleation, $\bar{\psi}$, dimensional assignment, Einstein recovery) — none of which the retrieved literature addresses. |

## 7. New findings for the programme (from slice C, carried into this synthesis)

**F1 — Klein (2001) contests the Alexander–McTague 3D result IRH's validation relies on.** IRH v93.1's §V validates its selection principle in 3D by recovering BCC (the AM result). Klein (arXiv:cond-mat/0104342, 2001) argues that AM's BCC solutions are *unstable* — the cubic term that selects BCC also destabilises it, and the stable 3D solution may be different. If Klein is right, IRH's 3D validation is a validation against a contested result, not a settled one. This does **not** touch the structural affinity (Gate 2 — the mechanism is the same whether or not BCC is stable in 3D), but it does bear on the *evidence* for IRH's mechanism: the manuscript's 3D check should be read as "recovers the AM prediction", not "recovers an established fact". **Action for the programme:** the 3D validation claim should carry the Klein caveat in any future revision; a stability analysis of the IRH \$4$D D_{4}$\$ solution is the direct analogue of the missing check. Grade: C (paper verified; implication is a judgement).

**F2 — IRH's own selection principle changed between the SSRN predecessor and v93.1.** The same-author SSRN predecessor selected by *maximal cymatic complexity* and obtained dimension 8; v93.1 selects by $S = \tau^{2}/q_{4}$ and obtains $D_{4}$. The selection principle is therefore **version-dependent**, and the manuscript's claim that S is *the* selection principle rests on v93.1's argument, not on a stable lineage. This matters for the map because the closest-mechanism affinity (Gate 2, AM) attaches to the v93.1 principle specifically, and because any future version that changes the principle again would re-open the affinity. **Action for the programme:** the SSRN$\tov93.1$ change should be acknowledged in the manuscript's history (it currently is not, as far as the retrieved record shows); the reason for abandoning maximal cymatic complexity is a question for the author. Grade: C (both documents retrieved and compared; the inference is stated as such).

## 8. Checks

**8-check self-evaluation rubric applied to the map's central claim** ("GFT condensate cosmology is structurally closest to IRH on substrate ontology"):

| # | Check | Result |
|---|---|---|
| 1 | Falsifiability | PASS — falsifiable by a retrieved approach scoring higher on substrate + selection jointly (e.g. an approach at (2,2) other than IRH), or by a GFT source showing its substrate is a regulator, not a physical claim. |
| 2 | Internal consistency | PASS — the three criteria are applied with the same rubric to every approach (Table 1); no approach is scored by a different rule. |
| 3 | Empirical adequacy | PASS (bounded) — grounded in 73 retrieved papers; bounded by the queries run (§2). |
| 4 | Simplicity | PASS — the scorecard is the simplest representation that carries the three criteria; no extra machinery is invoked. |
| 5 | Novelty | PASS (as synthesis) — no retrieved source compares these approaches to IRH; the verdict is new as a synthesis, not as a discovery. |
| 6 | Reproducibility | PASS — queries, sources, and scores are all on disk (slice notes + this report); a rerun of the same queries should reproduce the table. |
| 7 | Independence | **FAIL to exceed I1** — one pipeline, one authoring agent; the three slices share the target and criteria. This is the binding limit and the reason for the C ceiling. |
| 8 | Bartha gate | PASS — the claim passed Gate 1 (ontology) and the mechanism failure was stated, not hidden. |

**Result: 7/8 pass; independence is the binding limit $\to$ grade C (Track E, I1).**

**Computation gate (truth-seeking-frontier v5).** No load-bearing number in this report is computed by me except the OpenAlex counts (tool output: HTTP 200, exit 0, quoted in §2) and the figure-generation script (numpy 2.4.6 / matplotlib 3.11.2, Python 3.11.16 conda env, exit 0 — see §10). The scores are judgements, not computations; they are labelled as such. No second independent tool was needed for the counts (they are retrieval outputs, not derived quantities); the scorecard arithmetic is trivial (0/1/2 assignments, no derivation). **Above-CLAIMED check: no claim in this report is presented above CLAIMED with a single tool** — the affinity verdicts rest on the retrieved papers *and* the Bartha gates (two independent grounds: the sources, and the gate analysis), which is the applicable form of the second check for comparative claims.

## 9. HLRE grades per narrow claim (worst-of computation shown)

Independence is I1 throughout (one pipeline). Computation is F2 where a tool output is quoted (OpenAlex counts, figure script), F1 where the claim is a judgement on retrieved sources. Grades are capped at C by the skill (Track E) and by I1.

| ID | Claim | Grade | Basis |
|---|---|---|---|
| M1 | The 73 retrieved papers exist as stated (titles, authors, years, arXiv/DOI) | C / I1 / F2 | Search results + opened arXiv pages (slice notes); every entry verified to exist. |
| M2 | The scorecard scores (Table 1) | C / I1 / F1 | Judgements on the retrieved sources, rubric stated in §5. |
| M3 | GFT condensate cosmology is closest to IRH on substrate ontology | C / I1 / F1 | Gate 1 passes (ontology); mechanism fails (stated). |
| M4 | AM/LP lineage is closest to IRH on selection mechanism | C / I1 / F1 | Gate 2 passes (mechanism); ontology fails (stated). |
| M5 | AS is furthest from IRH on ontology and strongest on stated quantitative predictions | C / I1 / F1 | Gates 3; slice A (Higgs 126 pre-discovery, seesaw bound, proton-decay suppression). |
| M6 | No retrieved approach is close to IRH on ontology and mechanism jointly | C / I1 / F1 | Follows from Table 1 + Gates 1–12; IRH alone at (2,2). |
| M7 | OpenAlex volume counts (§2) | C / I1 / F2 | Tool output (HTTP 200, exit 0); caveat stated — broad text-search hits, not a census. |
| M8 | No independent work citing/discussing IRH was found | INCOMPLETE-EVIDENCE / I1 / F1 | Search-bounded absence; a different query set could find something. Not a claim that none exists. |
| M9 | No findable Wise Journal revision record | INCOMPLETE-EVIDENCE / I1 / F1 | Search-bounded absence; same caveat as M8. |
| M10 | IRH's selection principle changed SSRN $\to v93.1 ($cymatic complexity $\to S = \tau^{2}/q_{4}$; dimension $8 \to D_{4})$ | C / I1 / F1 | Both documents retrieved and compared (slice C). |
| M11 | Klein (2001) argues AM's BCC solutions are unstable — a caveat on IRH's 3D validation | C / I1 / F1 | Paper verified (arXiv:cond-mat/0104342); implication is a judgement. |
| M12 | Field-direction statements (§6, "Direction" column) | C / I1 / F1 | Retrievers' summaries of the 2023–2026 literature, re-checked against the cited papers. |

**Worst-of computation:** the map's overall grade is the worst of its load-bearing claims. M8/M9 are INCOMPLETE-EVIDENCE (absence claims, properly labelled as such, not failures). All positive claims are C. **Overall: C (Track E), I1, F2.** No claim is presented above C.

## 10. Tool verdicts

- OpenAlex counts: `openalex.py search` $\times 8$ queries, HTTP 200, exit 0, 2026-11-10 (quoted in §2).
- Figure generation: `data/make_map_figures.py`, Python 3.11.16 (conda env `jacobian-conjecture-2d`), numpy 2.4.6, matplotlib 3.11.2, exit 0. Both figures visually checked (§5): fig. 5 labels were colliding on the first render (discrete 0/1/2 grid pile-up) — fixed by jitter + per-point label offsets and re-checked; fig. 6 clean on first render.
- Retrieval: `browser.search` + `browser.open` (three slices, 63 queries, 73 papers) — tool outputs recorded in the slice notes; the IRH Zenodo record was verified by direct open (DOI 10.5281/zenodo.22821689, v93.1, 18 Sep 2026).

## 11. Rival / failure mode; evidence that would change the answer

**Rival reading.** "Closest to IRH" could be judged on surface vocabulary instead of structure — e.g. "emergent gravity" (Verlinde) or "emergent spacetime" (LQG's continuum limit) sound closest. That reading is rejected by the criteria: Verlinde's substrate is unspecified and it has no selection mechanism; LQG quantises geometry itself. If the criteria were changed to vocabulary similarity, the map would change — which is why the criteria were fixed before retrieval and are stated at the top of this report.

**Failure modes.** (a) Retrieval missed a relevant approach — the most likely miss is a *small* emergence programme (e.g. a newer pre-geometric model, or a non-English literature) that sits at (2,2); M6 is bounded by the queries run. (b) A score is wrong — the most contestable scores are Verlinde's substrate (1 vs 0: its microscopic theory is unspecified, so 0 is defensible) and causal sets' selection (1 vs 0: suppression is a weak form of selection). Neither changes M3/M4/M6. (c) GFT's substrate claim is weaker than scored — if GFT's quanta are read as quanta *of* geometry rather than a substrate *under* geometry, its substrate score drops to 1 and Volovik becomes the ontology leader; M3 would change. That ambiguity is stated in slice B (B11: "PARTIAL — quanta of geometry, not a separate physical medium") and is the reason M3 is grade C, not higher.

**Evidence that would change the answer.** (i) A retrieved approach with a physical substrate *and* a dynamical pattern-selection mechanism (a (2,2) entry other than IRH) would overturn M6. (ii) A GFT paper stating a pattern-selection mechanism would make GFT closest on both criteria. (iii) A resolution of the Branchina–Held dispute against the fixed point would weaken AS's predictions column (M5's second half) without affecting its ontology score. (iv) Independent work engaging IRH (a citation, a critique, a replication) would change M8 and the map's "IRH is alone" reading. (v) A stability proof for the IRH $D_{4}$ solution would retire finding F1's analogue; a demonstration that AM's BCC is stable would retire F1 itself.

## VERIFIED / UNVERIFIED / FAILED

**VERIFIED (grade C, I1 — see §9 for the per-claim basis):**
- M1 — the 73 retrieved papers exist as stated.
- M2 — scorecard scores (as judgements, rubric stated).
- M3 — GFT condensate cosmology closest on substrate ontology (Gate 1).
- M4 — AM/LP lineage closest on selection mechanism (Gate 2).
- M5 — AS furthest on ontology, strongest on stated quantitative predictions (Gate 3).
- M6 — no retrieved approach close on both ontology and mechanism.
- M7 — OpenAlex counts as tool outputs (with the census caveat).
- M10 — selection-principle change SSRN $\to v93.1$.
- M11 — Klein (2001) AM-instability caveat.
- M12 — field-direction statements.

**UNVERIFIED (INCOMPLETE-EVIDENCE — absence claims, search-bounded):**
- M8 — no independent work citing/discussing IRH found (a different query set could find something).
- M9 — no findable Wise Journal revision record.

**FAILED (affinity claims that did not survive the Bartha gate):**
- AS $\leftrightarrow$ IRH selection affinity beyond the abstract noun "dynamical selection" (Gate 3).
- CDT $\leftrightarrow$ IRH mechanism and ontology affinity (Gate 4 — only thin phase-diagram selection survives).
- Volovik $\leftrightarrow$ IRH mechanism affinity (Gate 5 — ontology passes, mechanism fails).
- Wolfram $\leftrightarrow$ IRH mechanism affinity (Gate 6).
- Verlinde $\leftrightarrow$ IRH — any structural affinity (Gate 7 — label only).
- Analogue gravity $\leftrightarrow$ IRH ontology affinity as a claim about our universe (Gate 8 — wrong referent).
- Causal sets $\leftrightarrow$ IRH substrate and selection affinity (Gate 9).
- LQG $\leftrightarrow$ IRH — any structural affinity (Gate 10).
- String/swampland $\leftrightarrow$ IRH — any structural affinity (Gate 11 — exclusion $\neq$ selection).
- PFC/Swift–Hohenberg $\leftrightarrow$ IRH ontology affinity (Gate 12 — mechanism-family only).
- GFT $\leftrightarrow$ IRH mechanism affinity (Gate 1 — ontology passes, mechanism fails).

**Sources on disk:** `data/lit-slice-A-asymptotic-safety.md`, `data/lit-slice-B-emergent-discrete.md`, `data/lit-slice-C-pattern-irh.md`, `data/make_map_figures.py`; figures `figures/fig5_researcher_map.png`, `figures/fig6_openalex_counts.png`.
