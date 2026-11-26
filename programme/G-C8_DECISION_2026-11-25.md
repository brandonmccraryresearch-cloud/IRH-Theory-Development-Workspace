# G-C8 decision — dimensional assignment and the role of $t$

**Decided by:** Dragon, under Brandon's explicit delegation (main chat, 2026-11-25 05:37 CST: "You make the decision and make sure to integrate this into the program. This should be attacking exactly what brings this closer to a toe.")
**Date:** 2026-11-25 ~05:45 CST
**Status:** DECIDED for the programme (working reading). Manuscript text NOT changed: the v94 §IX.2 wording is a major revision and goes through the deepest-research gate first.

## Decision

**Reading (B) is adopted.** The base is four spatial dimensions. The evolution time $t$ is physical time, so the bare arena is $4+1$. Observed $3+1$ spacetime comes from compactifying one spatial direction. Lorentz invariance has to emerge from the long-wavelength excitations (phonons/sound) of the relaxed $D_4$ crystal, evolving in $t$ under the v94 damped-wave dynamics.

Reading (A) is rejected as the working reading. Reading (C) is held as the fallback.

## Why

1. **(A) fails at the Gaussian level by an elementary argument** (grade C/I1; the formal proof is run-14 item K-A).
   - Write $s=k^2\ge0$ (Euclidean). The Swift–Hohenberg two-point function is $G(s)=1/(r+(q_0^2-s)^2)$.
   - SymPy 1.14.0, EXIT 0, gives $dG/ds = 2(q_0^2-s)/(\dots)^2 > 0$ for $0\le s<q_0^2$. So $G$ *increases* in $k^2$ below the shell.
   - Its poles in $s$ are the complex pair $q_0^2\pm i\sqrt r$.
   - An O(4)-invariant reflection-positive (Osterwalder–Schrader) two-point function has a Källén–Lehmann form $\int\rho(m^2)\,dm^2/(s+m^2)$ with $\rho\ge0$, which is non-increasing in $s$.
   - So the free SH measure in the disordered phase is not reflection positive, and reading (A) has no OS route to a Lorentzian QFT.
   - Its other route, a dynamical signature mechanism, is also absent: v94 l.956 says no mechanism is known for a single-scalar SH $D_4$ substrate without a tuned clock field.
   - Caveat: the ordered (crystal) phase is not O(4)-invariant, so the argument is not yet a theorem about the crystal. K-A must settle that.
2. **(B) turns the ToE blockers into computations rather than decisions.**
   - Signature is not a problem in (B): $t$ is time.
   - Emergent Lorentz invariance becomes a concrete phonon calculation: speeds, the common-$c$ problem G-A29, and the 6th-order anisotropy $\xi_6$ (G-A28/G-A30). The $D_4$ 5-design gives elastic isotropy to 4th order, which is exactly what this calculation needs.
   - Quantisation is ordinary Hamiltonian quantisation of the $\gamma\to0$ phonon field, so positivity reduces to $F$ bounded below ($v>0$).
   - It predicts Kaluza–Klein modes, a data-facing falsifier, which T6 needs.
3. **(C)** has no construction (v94 l.948) and nothing falsifiable yet.

## Costs of (B), stated (v94 l.946)

- **Compactification mechanism needed.** Item K-B2 below.
- **Breaks the $D_4$ symmetry the selection argument uses.** Selection happens in the 4D bulk before compactification. The 3D cross-section is FCC (§II.10), so this is a cost, not a contradiction. The physical consequences must be restated in 3D terms.
- **Known risk:** $c_L/c_T=\sqrt3$ (verified, run-8/9 audit). Two sound speeds means two light cones unless a branch is gapped or decouples. **This is the main way (B) can die.**

## Pre-registered reversal rule

(B) is dropped, and (C) becomes the working reading, if any of these happens:

- **K-B1** (common light cone) shows that no branch structure of the relaxed $D_4$ crystal, after compactification, gives a single massless sector with a common $c$ without tuning.
- **K-B2** shows that no compactification of the $D_4$ crystal is dynamically stable.

(A) is reinstated only if **K-A** shows the crystal-phase fluctuation measure *is* reflection positive in some direction.

## Run-14 items this creates

| ID | Item | Kind | Kill |
|---|---|---|---|
| K-A | Formal reflection-positivity analysis of the SH propagator (disordered phase; then the crystal phase along a lattice direction). Closes G-A27 either way. | Track F, small | a positive spectral representation exists |
| K-B1 | Phonon spectrum of the relaxed $D_4$ crystal: branches, speeds, $z$, $\xi_6$; then after compactifying one direction. Gapless count and common $c$. (ToE bar blocker 3) | numerics + exact | no common-$c$ massless sector |
| K-B2 | Stability of the compactified crystal (radius selection; Bloch stability on $T^1\times\mathbb R^3$) | numerics | every radius unstable |
| K-B3 | KK spectrum and its scale relative to the phonon cutoff — the first falsifier for T6 | exact | — (prediction) |
| K-B4 | Gauge route under (B): (i) Track-F no-go for gauge fields in the v94 $F$ (ToE bar blocker 2); (ii) elasticity/tensor-gauge (fracton) duality lead — sources to be opened before use | Track F | — |

ToE-bar blockers 4 (quantum theory: prescription for G-A10) and 5 (generic selection, EXP-1312 / $L=4\pi$, $\bar\psi$ prior) carry over unchanged.

## What this does not do

- It changes no grade.
- It does not edit v94; a §IX.2 rewrite waits on the deepest-research gate.
- It does not make IRH a ToE. It picks the reading under which the remaining blockers are computable and falsifiable.
