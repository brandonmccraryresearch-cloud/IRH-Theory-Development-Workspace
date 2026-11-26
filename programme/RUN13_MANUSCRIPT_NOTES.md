# Run-13 manuscript notes (status-note and erratum candidates for v94 → v95)

Author: w-rec13e (run 13 end-of-run record commit, Dragon subagent), 2026-11-26. Branch `run13/record-end`, cut from main `1ea6c14ac4bd793a62daec6f3b2c946d5c1744c6`.

**What this file is.** A list of manuscript-facing notes that run-13 adjudicated rulings proposed for Brandon's manuscript. **None is applied.** No `.tex` or PDF is edited on this branch. Every item touching v94 §IX.2 or a major revision waits for the deepest-research gate (Brandon's standing gate, 2026-11-04), and the wording of the manuscript is Brandon's call. Line numbers refer to `programme/v94/IRH_v94.tex` at main `1ea6c14a`. Each item names its source ruling (in `swarm/run13/adj/` unless stated) and that file's sha256. Text in quotation blocks is copied from the ruling.

Grades are those of the rulings. Nothing here raises a grade.

## 1. Critical droplet / nucleation barrier — a-ga10 §6 E1–E4

Source: `a-ga10_RULING.md`, sha256 `96c3db44c144fe9e6f931b8cc38735d7467e6f40ed680849f47d11d0959230ef`. The ruling states that v94 makes no physical claim from the barrier value, so no physical claim in v94 is falsified; E1–E4 are scope qualifiers.

- **E1, l.436** (erratum candidate, v95 note): "radial restricted-envelope saddle $550.93057$ … expected at barrier/noise ≈34 **within the radial envelope model**; the unrestricted-field critical droplet has $\Delta F^*\approx119.06$ (run 13, F2/I1), ≈4.6× lower, giving ≈7.3 at the same noise."
- **E2, l.319:** add "(radial-envelope barrier; ≈7.3 for the full-field barrier)".
- **E3, l.938:** add "against the full-field droplet 119.06 (run 13) the mismatch is $3.2\times$ / $0.86\times$". An observation, not a new claim of agreement.
- **E4, l.89 and l.920:** qualify "Deterministic saddle/threshold B / F2 (decided)" as "(radial restricted envelope)". The full-field barrier F2/I1 is a separate, new row.

## 2. Dimensional reading / phonon sector — a-kb1 RF-1..RF-6

Source: `a-kb1_RULING.md`, sha256 `f8df06b8dfdd2a910e41b058500e897404a477d3064f60de6d3d255131ecb10d`. All are status notes; RF-3 and RF-4 sit in §IX.2 and are deepest-research gated (the G-C8 memo, `programme/G-C8_DECISION_2026-11-25.md`, already defers the §IX.2 rewrite).

- **RF-1, l.408** ("with $L/T=3.016$ against $3$; extraction of $\lambda_{\mathrm{relaxed}},\mu_{\mathrm{relaxed}}$ is still open."): 3.016 is $\lambda_L/\lambda_T$ at $\lvert q\rvert=0.02$ along $e_1$, including the $q^2$ dispersion; the $q\to0$ value is 2.99977 (F2/I1); $\mu_{\rm relaxed}=c_T^2\rho=1.54465$ (F2/I1); $\lambda_{\rm relaxed}=W_{1122}=1.54447$ (author route, F3/I1); Cauchy $\lambda=\mu$ holds exactly at one-mode order (B). Proposed note: "q→0 ratio 2.99977; λ_relaxed, μ_relaxed extracted (run 13 K-B1)".
- **RF-2, l.85 and l.720** ("Stiffness $\lambda=\mu=1.54058921014457$ agrees exactly on both sides."): the printed value equals the one-mode formula $256A^2$ at $A=0.0775753$ (l.393); the relaxed state has $A=0.0776817$ (F2/I1) and relaxed $\mu=1.54465$, about 0.27% above. **Candidate only:** the provenance of $A=0.0775753$ must be checked against the run records before any note is written.
- **RF-3, l.946** (costs of reading (B)): the cost list omits the decisive one, two light cones, $c_L/c_T=\sqrt3$, with no tuning in the stable regime; (B) is dropped as the working reading under the pre-registered rule.
- **RF-4, l.950** ("This must be decided. It is not resolvable by further calculation."): K-A (G-A27, not RP) and K-B1 (no common $c$) are calculations that eliminated the constructive routes of (A) and (B), within their scopes; the second sentence is overtaken.
- **RF-5, l.764** (no anisotropic quartic Lorentz-violating term): not contradicted on anisotropy, but the dominant Lorentz violation of the phonon sector is isotropic and species-dependent at leading order (two cones). Proposed note: the leading LV is the cone mismatch, not anisotropy.
- **RF-6, l.311 / l.145–151** ($\gamma=1.2$), optional: at $\gamma=1.2$ the long-wave modes are overdamped; $\gamma$ is a relaxation parameter of the simulations, not a physical damping, under any reading in which phonons propagate.

## 3. Reading (A) and reflection positivity — a-ka row 6a

Source: `a-ka_RULING.md`, sha256 `986b7de9c37764c205fdd3a5772f2e6129d378bf53ea5076fb24743f444f0a93`. No erratum (v94 makes no positivity claim that K-A contradicts). One status-note candidate, deepest-research gated:

- **l.945**, reading (A): "(A) has no Osterwalder–Schrader route at Gaussian level: the SH fluctuation measure is not reflection positive (disordered phase, grade B; $D_4$ crystal, lattice-regularised, tested directions, F2/I1; G-A27)".

## 4. Monopoles — a-abst §5 E-2 (optional nit)

Source: `a-abst_RULING.md`, sha256 `6db0a198e48a9d47fab43a567d5a8f6ab321b8424b98a955dc5860ff501ff3a1`. E-2 (the l.748 remedy) is already on main via the tex-errata merge (v94 l.748 now reads "since $E_6$ is semisimple…"). The optional nit is already satisfied at `1ea6c14a`: l.746 reads "$\pi_2(G/H)\supseteq\mathbb{Z}$". Nothing left to do; recorded so the item is closed in the notes.

## 5. Model B scope tag at l.406 — a-b1 §1 (optional)

Source: `a-b1_RULING.md`, sha256 `00f02ffaa5efce98306c6e74cc39348e9864ab8141e50b8f56093e2900b25bc8`. No erratum E-A4b; the l.406 bold sentence and the l.867 row stand. Optional, not mandated: a later tex branch may append to l.406 the tag "[Model B linear stability: index 0 mod translations, F2/I1; verification run 13, 2026-11-24.]", parallel to the existing Model A tag. A scope tag, not a correction.

## 6. FoR / M6 — a-b1 §5 (pointer)

Source: `a-b1_RULING.md` (sha above) and `G-E10_Q5_NOTE.md`, sha256 `90ceff7e073c8d3b71d6ae9fc760ad13ae9a3a271dfb8ec5ddf6b4e32e5d3473`. The M6 correction is recorded in the inventory G-E10 entry and as a dated note under the M6 row of `programme/workstreams/ws-e-cosmology-map/14-researcher-map-report.md`. Any manuscript sentence that says IRH is the only approach at (2,2), or the only one stating resonance / closed-triad selection, should carry that correction; reconciliation with v94 l.448 is listed in the G-E10 entry.

## 7. $D_4$ selection at $L=3\pi$ — a-gd3b Q3 and Q4.6

Source: `a-gd3b_RULING.md`, sha256 `c42524f43311b3876133053cc4af9134b4101998f772fcc1665ac3fee555c11f`.

- **Q4.6:** no v94 erratum. v94's "$D_4$ dynamically selected" is untouched as a manuscript claim; EXP-1312 narrows but does not settle it. Manuscript-facing wording (the rotated-$D_4$ point, the box/point dependence) is a status-note candidate held for the deepest-research gate.
- **Q3**, ToE-bar T1.1 delta wording (for the bar's owner; `IRH_TOE_BAR.md` is not in this repo and is not edited here):

> **T1.1 — PARTIAL (box-scoped), moved.** EXP-1312 is adjudicated (a-gd3b), and it is the first run with competitor orbits on the unstable shell ($L=3\pi$, 312 modes, 41 $D_4$ subsystems).
> - $D_4$ (up to rotation) wins at P1 with 29/30, $[0.833,0.994]$, at F2/I1.
> - At P2 it wins in $0.82$, $[0.692,0.902]$, at F2/I1. The rest goes to a metastable 42-mode non-$D_4$ minimum $7.7\times10^{-4}$ above $D_4$ (F3/I1).
> - The kill criterion is not triggered: no majority competitor and no lower-$F$ competitor.
> - The bar is not met. One box size, two points, $\ge0.9$ selection not shown at P2, no infinite-volume trend, and no stated $\bar\psi$ measure.
> - Next box: $L=5\pi$, **not** $4\pi$. $L=4\pi$ carries only the $D_4$ star.
> - The earlier "unadjudicated, CLAIMED" sub-bullet for EXP-1312 is superseded.

## 8. EXP-1310 gate advisories — g-1310 A1–A3

Source: `swarm/run13/g-1310/GATE_REPORT.md` §5 (l.112–121), sha256 `d80d6bece66adf5b68b91b5fad1d698d0262596b069f7d96b3d2ac15bcc991a8`. Non-blocking; not part of the gate's pass rule.

- **A1 (pre-existing, Brandon's call).** l.364, l.367 and l.758 say "at a detuning of only 0.5 … the ordered branch vanishes entirely" and "the D₄ band is conditional on $q_0$ being tuned onto the shell". Per inventory G-A17 this is true at the operating point $(\bar\psi,r)=(-0.18,-0.35)$ but false plane-wide: the band persists in-window at $\delta=0.5$ (8.18% in W1), shifted by exactly $\delta^2$ in $r$. The l.866 ledger row "D₄ phase band (tuned $q_0$)" carries the same wording. Rewording is an author decision.
- **A2 (precision, optional).** l.748: "since $E_6$ is semisimple" is sufficient but indirect; more precise: "since $\pi_2(E_6)=0$ (Cartan) and $\pi_1(E_6)$ is finite". At l.746/748, "containing an unbroken $U(1)$" means "with a $U(1)$ factor" (PDG phrasing). The mathematics is correct as written.
- **A3 (cosmetic).** l.794: Unicode "≈1.03" and "1×10⁻⁴" sit outside math mode; converting to $\approx1.03$ and $1\times10^{-4}$ is optional.
