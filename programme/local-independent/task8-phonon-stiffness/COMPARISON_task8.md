# Comparison — Task 8: $D_{4}$ phonon stiffness and Burgers-vector costs

**Status: COMPARISON PENDING — Academia side not landed.** Checked 2026-11-14 ~03:10 CST: no Co-scientist result files for this task exist in `~/workspace/research/irh/co-scientist-tasks-2026-11-10/` outside `local-independent/`. Do not treat this comparison as complete.

**Local side:** `REPORT.md` in this directory (worker completed 2026-11-14 ~02:36 CST). Coordinator spot-checks re-run 2026-11-14 (conda python 3.11.16, exit 0): **$|W(F_{4})| = 1152$ independently confirmed** by BFS closure of exact-rational generators (signed permutations + one Hadamard-type triality generator); $D_{4}$ roots $24$; $S_{D_{4}} = 64/141$.

## Local result (summary)

- Long-wavelength stiffness, frozen-amplitude, exact SymPy identity + 200-strain numerical check + independent pseudospectral (Fourier) route recovering identical coefficients: $\lambda = \mu = 256 A_{*}^{2} = 1.5405892101$, bulk $B = 384 A_{*}^{2}$. Grade **B**; **F2 as a variational upper bound** on relaxed moduli, not as the relaxed moduli themselves.
- Quadratic stiffness exactly isotropic; first anisotropy at cubic order (biaxial $f_{3}$ varies 2.6%). Stiffness magnitudes are claimed as variational upper bounds.
- Burgers classes: one $W(F_{4})$ orbit per $|b|^{2}$ shell $\le 12$ (verified by a clean exact-rational breadth-first-search in under 60 seconds); group order 1152 verified. Grade **F2** (coordinator spot-check independently confirms the group order).
- Dislocation energies: $E/A = K \ln(R/r_{0})$, edge/screw factor exactly 2: $K_{\mathrm{edge}} = \lambda + 2\mu = 3\mu = 4.6217676304$, $K_{\mathrm{screw}} = \mu = 1.5405892101$. Grade **B**.
- Core radii (edge $0.064330$ $\approx 0.7 a$; screw $0.131559$ $\approx 1.43 a$, ratio $2.044540 \approx 2$) and split thresholds ($40\% <$ criterion $<$ $40.4\%$, screening length $2.9/|b|^{2}$, $R^{*} = 2.216220$) are class-dependent **C** (sheet formation is a theoretical construction, not simulation).
- Relaxed phonon dispersion: **ABSTAIN** (requires the relaxed-field Bloch spectrum; not yet computed).

## Academia side

PENDING. Launched 2026-11-14 as "Calculate $D_{4}$ phonon stiffness and Burgers-vector costs". No files landed yet.

## Per-number comparison checklist (complete when Academia lands)

| # | Quantity | Local value (grade) | Academia value | Agree? | Better supported | Settles |
|---|---|---|---|---|---|---|
| 1 | Lamé coefficients | $\lambda = \mu = 1.5405892101$ (B) | | | | Must agree with the exact root-sum identity $256 A_{*}^{2}$ if the same frozen-amplitude definition is used |
| 2 | Bulk modulus | $B = 384 A_{*}^{2}$ (B) | | | | |
| 3 | Isotropy / anisotropy | Quadratic exact isotropy; cubic biaxial variation 2.6% | | | | A quadratic anisotropy on Academia's side would indicate a different deformation class |
| 4 | Group order / orbits | $W(F_{4})$ order 1152; one orbit per $\|b\|^{2}$ shell $\le 12$ (F2) | | | | Exact arithmetic; any disagreement here is an error on one side (coordinator independently confirms 1152) |
| 5 | Dislocation cost factors | $K_{\mathrm{edge}} = 4.6217676304$, $K_{\mathrm{screw}} = 1.5405892101$, ratio exactly 2 (B) | | | | |
| 6 | Core radii / split thresholds | Edge $0.064330$, screw $0.131559$, criterion $40$–$40.4\%$ (C) | | | | Class definition is a caveat: sheet vs radial/cylindrical winding |
| 7 | Relaxed moduli / relaxed phonon dispersion | ABSTAIN (not computed) | | | | If Academia claims relaxed moduli, its method (relaxed Bloch spectrum) must be stated — the local side's numbers are frozen-amplitude upper bounds only |

## S3 invariance alignment (cross-domain-discovery)

Do both derivations reduce to the same equations? The stiffness coefficients reduce to a root-sum identity over the 24-mode star (`SymPy` exact) — that is the alignment target: does Academia's derivation reduce to the same identity, or to a different deformation class (e.g. one allowing amplitude relaxation)? The pseudospectral route is a second derivation of the same identity. The Burgers-orbit result reduces to exact group theory ($W(F_{4})$ acting on $D_{4}$ lattice vectors) — alignment is checkable by the same BFS. The critical alignment distinction: frozen-amplitude stiffness vs relaxed moduli are different quantities; the local side's numbers are **upper bounds** on the relaxed moduli, and any Academia number presented as a relaxed modulus must not be compared against them as if they were the same quantity.

## S4 Bartha articulation + transportability audit

- Transfer "frozen-amplitude stiffness $\to$ relaxed moduli": **fails as equality**; holds as a variational upper bound (F2 as bound).
- Transfer "sheet formation $\to$ dislocation cost": **class-dependent (C)** — the sheet's $40\%$ core criterion and edge/screw factors depend on the defect class; a radial winding (the other candidate class) would give different factors.
- Selection-diagram note: no formal diagram built; the $S$-nodes (amplitude relaxation, defect class) are named in the report.

## 8-check rubric (local side, as far as assessable now)

1. Independent test exists — PASS in part: stiffness by two independent derivations (SymPy exact + Fourier pseudospectral); group order by exact BFS, independently confirmed by the coordinator; Academia comparison pending.
2. Falsification boundary stated — PASS: a relaxed-modulus computation below the frozen values would be expected, not a contradiction; a value above them would contradict the bound.
3. Bartha articulation passes — PASS for the stated transfers (equality transfer fails, bound transfer holds).
4. Transportability audited — PARTIAL: defect-class dependence stated; no formal selection diagram.
5. Second independent tool — PASS: two derivations of stiffness; coordinator BFS as a third check of the group order.
6. No invented numbers — PASS: all numbers trace to run tables; core radii/split thresholds graded C with the class caveat.
7. Assumption ledger complete — PASS as reported; coordinator did not re-audit every ledger line.
8. Grade honest — PASS: relaxed dispersion ABSTAIN; core quantities C.

## Grade cap

This comparison report caps at **C (Track E) / F3 (Track F)** per the cross-domain-discovery skill's own grade cap until human source/balance gates are run. The comparison itself is a scaffold until the Academia side lands.

## What would settle the difference

Academia landing with its stiffness derivation and defect class; the relaxed-field Bloch phonon spectrum (GCP \$25 cap, needs approval); a direct full-field dislocation simulation (GCP \$50 cap, needs approval).
