# Independent Verification Package — `irh93_pkg2`

**Source:** independent verification audit of *Intrinsic Resonance Holography*
v93/v93.0 by Enigma, 2026-09-17. Supplied by the author; preserved here
verbatim as the executed record behind Part VI-A of v93.1.

## Contents

| Path | What it is |
|------|------------|
| `FINAL_AUDIT.md` | The full audit report: 51/51 claim checks passed, II.8 reproduced, II.6 partial (then completed in the addendum), Lean 8 modules compiling (`lake build` exit 0). Includes the v93.0 re-verification addendum. |
| `verify_claims.py` | Claim-verification suite: 51 checks covering every numerically/combinatorially checkable claim — D₄ root enumeration, moment isotropy, resonance maximum, shell combinatorics (N/T/Q), selection criterion exact rationals, stationary state, CFL bound, dispersion identity, cross-section, Weyl groups, quaternion/group checks. **51 passed, 0 failed.** |
| `sim6_units.py` | Faithful II.8/II.6 simulations with the paper's $q_0^2 = 8.0$. Documents the critical unit correction: the D₄ shell sits on resonance only with box length $L=\pi$ (using $L=16$ leaves the mean and harmonics unstable). Seeded 24-mode state at $A^*=0.0776$, $\bar\psi=-0.18$; Model B holds, Model A drifts — matching the paper to all quoted digits. |
| `sim7_fairtest.py` | The exact II.6 fair test with v93.0 fully-specified parameters: $16^4$ grid, $L=2\pi$, $q_0^2=7.5$, D₄ shell (24 modes, $T=192$) vs. triad-free competitor (integer shell $\|\mathbf{k}\|^2=7$, 64 modes, $T=0$) at exactly degenerate linear penalty. Result: triads on → D₄ 77.1% (direct quench), 89.5% (annealed, still rising); triads off → D₄ 21% vs competitor 79%. The cubic term flips the winner. |
| `lean/` | Lean 4 + Mathlib formalization, 8 modules, `lake build` exit 0, no sorry/admit/axiom/native_decide: `Isotropy` (2nd/4th moments), `Selection` (criterion, exact rationals, √2 ratio, 73/423 margin), `WeylD4` ($-I \in W(D_4)$), `CFL` (stability bound), `CrossSection` (D₄∩{x₃=0}=D₃), `UEff` ($u_{\mathrm{eff}}$ identity), `Dispersion` (exact lattice sum), `Basic`. |
| `AUDIT_2026-10-15.md` | CAIC's independent re-verification of the external 2026-10-15 consolidated audit: per-item verdicts (confirmed / refined / downgraded / resolved), with the τ-ratio erratum, CFL fixes, SO(8) inference refinement, and the correction register. |
| `reconcile_resonance_count.py` | Authoritative 16-vs-32 reconciliation (executed, exit 0): exhaustive enumeration of the §II.6 physical grid ($16^4$, $L=2\pi$, scaled $D_4$ shell) proves exactly 32 maxima — 16 corners + 16 body-centres — matching the analytic prediction point-for-point. |

## How it maps to this workspace

- `established/CORE.md` — the claims these scripts check are the verified core.
- `predictions/VI-predictions.md` — VI.1 (triad phase locking) extends
  `sim7_fairtest.py`; VI.4 (stability bound) is exercised by both sim scripts.
- `problems/IX1-tractable-computation.md` — 1.1 (larger volume) extends
  `sim7_fairtest.py`; 1.2 (nucleation barrier) builds on the `sim6_units.py`
  seeded-state protocol; the unit conventions ($L=\pi$ vs $L=2\pi$) and the
  32-image / excess-$F$ conventions documented in `FINAL_AUDIT.md` apply to all
  new simulation work.
- `problems/IX5-genuinely-open.md` — 5.2 (nucleation event) starts from the
  II.9 consistency check in `FINAL_AUDIT.md` and the `sim6_units.py` protocol.

## Conventions fixed by this package (do not re-litigate)

- Resonance maximum is **unique modulo D₄ periodicity**: 32 periodic images on
  the $16^4$ grid (checkerboard: corner + body-centre sublattices).
- Free energy $F$ is the **excess over the uniform state** ($F=0$ for disorder).
- Box/shell conventions: $q_0^2=8.0$ requires $L=\pi$; the v93.0 fair test uses
  $L=2\pi$ with the scaled shell. Check which convention a script uses before
  comparing numbers across scripts.
