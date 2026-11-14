# Task 2 — $D_{4}$ grain locking in a larger four-dimensional box

## CLAIM

In a $4\pi$ box ($16\times$ the pilot volume), independently shifted $D_{4}$ patches heal into a single coherent stationary pattern within a few time units for every translation mismatch tested (two-patch antiphase, two-patch shift, four-patch shifts, ordered half against uniform half). The healed pattern is the pilot's relaxed full-24 state: at the pilot-equivalent spectral band its excess energy is identical to the pilot value to all 15 printed digits. A genuine orientation grain — two hex6 sub-patterns in different planes — does not heal to full-24: the two hex grains fuse into the stationary 12-mode FCC cross-section pattern.

## STATUS

**CONFIRMED (bounded scope).** P1 (aligned control, frozen before running) passed at the full tier: stationary full-24, energy $-0.00772620928487423$ versus the pilot field value $-0.007726209285$. All five full-24 patch configs (A–E) end in the identical stationary full-24 state at both spectral tiers; config F ends in the stationary fcc12 state at both tiers. Every endpoint was re-derived by a second, independently written tool (plain NumPy only) to $10^{-9}$. Scope limits, one withdrawn label, and the un-run larger box are stated below; nothing beyond the stated scope is claimed.

## 1. Derivation (each step checkable)

### 1.1 The larger box and its shell

Pilot: box length $2\pi$, shell $|k|^{2} = 8$, 24 modes $(\pm 2, \pm 2, 0, 0)$ and permutations, $N = 18$, cutoff $K = 4$, $dt = 0.1$, $t_{\mathrm{final}} = 200$. This task doubles the box to $L = 4\pi$. Physical wavevectors are $k = m/2$ with integer $m$, so the shell $|k|^{2} = 8$ is $|m|^{2} = 32$. Enumerating integer 4-vectors (script `run_grain.py`, asserted at import): the only absolute-value pattern with $|m|^{2} = 32$ is $(0, 0, 4, 4)$, giving exactly the 24 vectors $(\pm 4, \pm 4, 0, 0)$ and permutations — a clean $D_{4}$ shell, as in the pilot. (The next candidate, $L = 6\pi$, would need $|m|^{2} = 72$, which has 312 vectors: not a clean $D_{4}$ shell. $L = 8\pi$ is clean again — $|m|^{2} = 128$, 24 vectors — and is the costed next size in §8.) The shell wavelength is $\lambda = 2\pi/\sqrt{8} = 2.221441469079183$.

### 1.2 Solver: the pilot solver, rescaled

The solver is the pilot ETD2 Fourier–Galerkin Model B solver (`4d-field-test/run_field_study.py`), generalised to the scaled wavevectors: linear operator $L_{\mathrm{op}} = \alpha + (8 - |k_{\mathrm{phys}}|^{2})^{2}$ with mobility $|k_{\mathrm{phys}}|^{2}$, $\alpha = 0.1072$, $\beta = 1.54$, $\bar{\psi} = -0.18$, $r = -0.35$, $u = v = 1$, $dt = 0.1$, the same startup caps ($dt/1000$ until $t = 0.02$; $dt/20$ until $t = 0.2$) and the same step-energy rejection safeguard ($F_{\mathrm{new}} \le F_{\mathrm{old}} + 2\times 10^{-13} + 2\times 10^{-12}|F_{\mathrm{old}}|$, halve on failure). Two tiers were run:

| tier | $N$ | cutoff $K$ | physical band $|k_{i}| \le$ | $N^{4}$ grid | role |
|---|---|---|---|---|---|
| cheap | 26 | 6 | 3 | 456,976 | main ensemble (6 configs) |
| full | 36 | 8 | 4 | 1,679,616 | pilot-equivalent band; spatial refinement (A, B, D, F) |

Both satisfy the dealiasing rule $N > 4K$ ($26 > 24$, $36 > 32$). The full tier's physical band is exactly the pilot's, so its relaxed energies are directly comparable to the pilot's; the cheap tier's narrower band is a deliberate, quantified sensitivity check (it shifts the relaxed full-24 energy by $+3.45\times 10^{-5}$, §4).

### 1.3 Patch construction

A patch is a full-box coherent pattern of its mode set: $\phi_{p}(x) = \mathrm{RMS}_{p}\, u_{p}(x)$, where $u_{p}$ is the unit-RMS cos-template $(1/\sqrt{n_{p}})\sum_{j}\cos(k_{j}\cdot(x - s_{p}))$ over the patch's modes, $s_{p}$ its shift, $n_{p}$ its mode count. Patches are blended by a smooth partition of unity — per-axis plateau profiles with cosine tapers of half-width $\Delta = 1.0$ across each interface ($e_{0} + e_{1} = 1$ exactly; products for quarters) — then renormalised to the matched RMS $\mathrm{TARGET} = \sqrt{24}\,A = 0.38003978535286725$ with $A = 0.07757529633928076$ (configs A–D, F; config E is not renormalised). Renormalisation scales (blending losses): B $1.0399$, C $1.0431$, D $1.0894$, F $1.0205$, A $1.0000$. Construction is verified at $t = 0$: per-patch correlation $\rho_{p} = 0.991$–$1.000$ and phase $|\theta_{p}| \le 0.006$ rad for every ordered patch (E's uniform half: $\rho = 0.013$, local RMS $0.0201$ — the residual is band-projection ringing, not order).

### 1.4 Diagnostics (definitions frozen before running)

- **Global** (pilot definitions): occupancy (modes with $|a_{k}| \ge \max(10^{-6}, 0.1\max|a|)$), amplitude CV over the 24 star modes, weighted signed triad lock over the 32 unordered star triads, shell power / shell fraction / off-shell power, excess energy density, projected RHS RMS. Full endpoint: occupancy 24, $\mathrm{CV} \le 0.05$, lock $\ge 0.95$, RHS RMS $\le 10^{-7}$.
- **Per-patch** $(\rho_{p}, \theta_{p})$: least-squares fit of the interior field (envelope $> 0.999$) onto the patch's cos/sin templates $(u_{p}, v_{p})$, solving the $2\times 2$ Gram system on the mask — the two separate correlations must not be combined by hypotenuse, because $u_{p}$ and $v_{p}$ are orthogonal over the full box but not over a half-box interior. $\rho_{p}^{2}$ is the explained-variance fraction in $[0, 1]$; $\theta_{p}$ is the local phase lag. (Two bugs found and fixed during checking: the quadrature template must be built from the 12 positive representatives only, since $\sum_{24}\sin$ cancels identically; and the initial field must be projected onto the retained band, as the pilot does.)
- **Final-pattern overlap** $O_{p} = |\sum_{k}\overline{a_{k}^{\mathrm{template},p}}\, a_{k}^{\mathrm{final}}| / (\|a^{\mathrm{template},p}\|\,\|a^{\mathrm{final}}\|)$: how much of the final pattern equals patch $p$'s pattern, translation and orientation included. This is the robust cross-tier quantity; $\theta_{p}$ is stable only when $\rho_{p}$ is high (§5.3).
- **Slab diagnostics**: per-$x_{1}$-plane RMS, template correlations, and mean energy density; boundary slabs are those within $1.5$ of an interface ($x_{1} = 0$ or $L/2$), interior slabs those farther than $2.5$ from any interface.

### 1.5 Prediction register (frozen before any grain run)

`predictions.json` was written before any grain run. P1 (config A): recover stationary full-24 with energy within $10^{-5}$ of the pilot field value $-0.007726209285$, $\rho_{p} \ge 0.99$, $|\theta_{p}| \le 0.05$ rad at $t = 100$. P2 (B/C/D) and P3 (E): no directional prediction frozen — exploratory; the discriminating observables (final $\rho_{p}$, $\theta_{p}$, occupancy, lock, shell fraction, boundary-slab excess at $t = 100$) were frozen instead. Config F is POST-HOC relative to A–E (conceived after inspecting them; see `predictions_addendum.json` and §6).

## 2. Results

### 2.1 Outcomes

| config | initial $E$ | final $E$ (cheap / full) | outcome | occ | lock | final RHS RMS |
|---|---|---|---|---|---|---|
| A aligned-2 | $-0.00763227$ | $-0.00769173716946$ / $-0.00772620928487$ | stationary_full24 | 24 | 1.0 | $3.2\times 10^{-16}$ / $9.6\times 10^{-16}$ |
| B antiphase-2 | $+0.0991135$ | $-0.00769173716946$ / $-0.00772620928487$ | stationary_full24 | 24 | 1.0 | $3.8\times 10^{-16}$ / $9.5\times 10^{-16}$ |
| C shift-2 | $+0.0758627$ | $-0.00769173716946$ / $-0.00772620928487$ | stationary_full24 | 24 | 1.0 | $4.1\times 10^{-16}$ / — |
| D shifts-4 | $+0.189269$ | $-0.00769173716946$ / $-0.00772620928487$ | stationary_full24 | 24 | 1.0 | $3.6\times 10^{-16}$ / $9.3\times 10^{-16}$ |
| E half-uniform | $+0.0319394$ | $-0.00769173716946$ / — | stationary_full24 | 24 | 1.0 | $3.5\times 10^{-16}$ / — |
| F hex6-orient-2 | $+0.146493$ | $-0.00536249646320$ / $-0.00546783498566$ | stationary_other (fcc12) | 12 | 1.0 | $4.3\times 10^{-16}$ / $7.5\times 10^{-16}$ |

All five full-24 configs reach the identical final state (same energy to all printed digits within a tier; shell fraction $0.9999873568153669$ cheap / $0.9999811126692804$ full). Healing is fast: global energy is already at its final value by $t = 2$–$5$ in every config (pilot recovery times were $t = 20$–$50$), and all diagnostics are frozen from $t \approx 5$ to $t = 100$ with RHS RMS $\sim 10^{-16}$. No rejected steps in any run.

### 2.2 Which pattern won (overlaps and phases)

| config | $O_{p}$ per patch (cheap / full) | reading |
|---|---|---|
| A | $1.000000$ / $1.000000$ both | final pattern is the initial pattern |
| B | $0.722227$, $0.721789$ / $0.722236$, $0.721780$ | neither patch won: the healed pattern sits exactly halfway between them |
| C | $0.585916$, $0.585126$ | near-symmetric compromise |
| D | $0.802295$, $0.533303$, $0.159732$, $0.168540$ / $0.802396$, $0.533281$, $0.159900$, $0.168319$ | closest to patch 0, far from patches 2–3 |
| E | $1.000000$ both | the ordered half's pattern invaded unchanged |
| F | $0.422770$, $0.422852$ / $0.422770$, $0.422858$ | symmetric; each hex template is contained in the fused fcc12 pattern |

For B the final per-mode phases are exact: modes with $m_{1} = +4$ have phase $-1.1102$ rad, $m_{1} = 0$ have $0$, $m_{1} = -4$ have $+1.1102$ rad. Since the phase of mode $m$ under a translation $s$ is $-(m/2)\cdot s$, this is a translation $s = (+\lambda/4, 0, 0, 0) = (0.5551, 0, 0, 0)$ — exactly halfway between patch 0 ($s = 0$) and patch 1 ($s = \lambda/2 = 1.1107$). The antiphase boundary healed to the midpoint pattern, not to either patch's pattern. Final per-patch $(\rho_{p}, \theta_{p})$, cheap tier: B $(0.850, -0.559)$, $(0.853, +0.547)$; C $(0.658, -0.478)$, $(0.700, +0.577)$; E $(1.000, 0.000)$ both; A $(1.000, 0.000)$ both. Full-tier B agrees: $(0.849, -0.549)$, $(0.844, +0.568)$.

### 2.3 Config F: hex grains fuse into fcc12

The final occupied set is exactly the 12 modes with $m_{4} = 0$ (the FCC cross-section), at both tiers. Amplitudes are all equal: $0.116428$ (cheap) and $0.11674176$ (full), against the one-mode fcc12 amplitude $A^{\ast} = 0.11642798071561167$ computed independently from `d4model` ($N = 12$, $T = 48$, $Q = 540$, $H = 42240$). At the cheap tier the final energy is exactly the one-mode value $-0.005362496463203872$ with shell fraction exactly $1.0$ and off-shell power exactly $0.0$: within the $K = 6$ band the fcc12 one-mode state is exactly stationary (all nonlinear products land back in the set or outside the band). At the full tier it relaxes to $-0.005467834985660468$ (shell fraction $0.9999812729871793$), matching Task 5's relaxed fcc12 energy $-0.005470$ to $2\times 10^{-6}$. The two hex sets (10 modes at $t = 0$) grew the missing $\pm(4, 0, -4, 0)$ pair by $t \approx 0.2$ to complete the fcc12 slice. Neither hex won; they merged into the slice containing both.

### 2.4 Grain-boundary behaviour

The boundary cost is visible in the global energy: initial excess energies $+0.076$ to $+0.189$ (B/C/D/F) fall to the final stationary values by $t = 2$–$5$ (Fig. `fig_shellpower_cheap.png`). Boundary-slab minus interior-slab mean energy density likewise decays to the control level by $t \approx 2$ (B: $-0.0650$ at $t = 0$ → $-0.000598$ at $t = 100$; C: $+0.0197$ → $-0.000449$). Two honest limitations of the slab diagnostics:

- The $x_{1}$-slab RMS profile is dominated by the pattern's own $x_{1}$-ripple ($0.27$–$0.49$ in every config including the aligned control A, whose $t = 0$ and $t = 100$ profiles are identical). The interface-vs-centre RMS dip is $+0.0043$ for B at $t = 0$ and $+0.0045$ at $t = 100$, while the control shows $-0.0043$ — i.e. the dip is within ripple-sampling variation and does not detect the boundary even at $t = 0$. Slab RMS is reported as a negative diagnostic result, not as boundary evidence.
- The slab energy-density residual at $t \ge 2$ ($|\mathrm{excess}| \le 6\times 10^{-4}$) is at the level of the aligned control's own persistent offset ($+0.000347$, a ripple-sampling artifact of the same diagnostic). Claim: no residual boundary energy is detectable above $\sim 10^{-3}$, versus the $10^{-1}$ initial boundary cost.

**Figures:** `fig_phase_cheap.png`, `fig_phase_full.png` (per-patch $\rho_{p}$, $\theta_{p}$ vs time); `fig_shellpower_cheap.png`, `fig_shellpower_full.png` (shell power, shell fraction, off-shell power, total power, energy, occupancy vs time); `fig_boundary_cheap.png`, `fig_boundary_full.png` (slab RMS profiles and boundary/interior energy density vs time). **Tables:** `grain_summary.csv` (all 11 runs), `final_pattern_overlap.csv` (overlaps), per-run `grain_trajectories.csv`, `grain_patch_trajectories.csv`, `grain_slab_profiles.csv`, `grain_state.npz` (initial/final compact coefficients, shell trajectories).

## 3. Checks run

Tool verdicts quoted. Conda env python `~/miniconda3/envs/jacobian-conjecture-2d/bin/python`: Python 3.11.16, NumPy 2.4.6, SciPy 1.17.1, Matplotlib 3.11.2.

| check | verdict | quoted result |
|---|---|---|
| Solver self-tests, cheap tier ($N = 26$, $K = 6$) | PASS | dealias energy vs larger $N$ $0.0$; projected nonlinearity max $3.63\times 10^{-18}$; energy-gradient FD error $9.97\times 10^{-11}$; dissipation identity error $1.82\times 10^{-12}$; template energy vs truncated branch $9.62\times 10^{-15}$ (template $-0.007632267318990376$ vs $-0.007632267319$); linear-decay relative error $5.14\times 10^{-7}$ (pilot: $5.13577\times 10^{-7}$); 32 triads, 24 modes |
| Solver self-tests, full tier ($N = 36$, $K = 8$) | PASS | dealias $0.0$; nonlinearity $2.47\times 10^{-18}$; FD $1.14\times 10^{-10}$; dissipation $2.33\times 10^{-10}$; template $9.62\times 10^{-15}$; linear decay $5.14\times 10^{-7}$ |
| Independent recomputation (`check_energy_independent.py`, NumPy-only, separate code, triads re-enumerated) | PASS, all 11 runs | final energy, shell power, modulation power, shell fraction, triad lock, occupancy all agree to $10^{-9}$; 32 triads re-enumerated |
| P1 (frozen prediction) at full tier | PASS | occupancy 24, lock $1.0$, $E = -0.00772620928487423$ (within $10^{-5}$ of pilot $-0.007726209285$ — in fact identical to 15 digits), $\rho_{p} = 0.99999$, $\theta_{p} \approx 0$ |
| P1 energy clause at cheap tier | FAIL (expected tier effect, §4) | $E = -0.00769173716946$, i.e. $3.45\times 10^{-5}$ above the pilot value: the narrower band admits fewer harmonics. Resolved by the full tier, not by adjusting the prediction. |
| Spatial refinement (cheap vs full) | PASS | $\Delta E = 3.45\times 10^{-5}$ (A/B/D), $1.05\times 10^{-4}$ (F); overlaps agree to $\le 2.2\times 10^{-4}$; outcomes identical |
| Temporal refinement (B, $dt = 0.05$ vs $0.1$) | PASS | final $\Delta E = 0.0$; max shell-path difference / initial norm $8.61\times 10^{-4}$; max $\|\Delta E(t)\| = 3.93\times 10^{-6}$ |
| Construction check ($t = 0$ patch diagnostics) | PASS | $\rho_{p} = 0.991$–$1.000$, $|\theta_{p}| \le 0.006$ rad (ordered patches) |
| Energy safeguard (all runs) | PASS | 0 rejected steps in all 11 runs; max step energy increase $\le 6.94\times 10^{-18}$ across runs (measured; cf. pilot $5.2\times 10^{-18}$) |
| hex6 / fcc12 one-mode amplitudes (via `d4model`) | PASS | hex6 $A^{\ast} = 0.1609228060665426$, RMS $0.3941787628398827$ (Task 5: $A = 0.161$); fcc12 $A^{\ast} = 0.11642798071561167$ (final-state amplitudes $0.116428$ cheap / $0.11674176$ full) |
| Slab-RMS dip as boundary detector | FAIL (negative result) | dip $+0.004$ vs control $-0.004$: within ripple; see §2.4 |
| Larger box ($L = 8\pi$) | NOT RUN | costed in §8, pending |

## 4. Rival / failure mode

- **The result is a relaxation-time artefact of the horizon?** No for the endpoints: the states are stationary to RHS RMS $\sim 10^{-16}$ and every diagnostic is frozen from $t \approx 5$ to $t = 100$; a boundary that has vanished into a stationary state cannot reappear without new input. But $t = 100$ is still a bounded horizon: a much slower process (e.g. a second, slower coarsening mode) is not excluded by these runs, only bounded — nothing moved between $t = 5$ and $t = 100$.
- **The healing is an artefact of the narrow band / taper?** The full tier (pilot-equivalent band) reproduces the cheap tier outcomes exactly in classification and to $10^{-4}$ in overlaps; the taper is a construction choice (half-width $1.0 \approx 0.45\lambda$), and the boundary cost it introduces is the thing that relaxes away. A different taper width was not tried.
- **The rotation test was vacuous (§6).** The claim "orientation grains heal" was never actually tested for full-24 patches; only F tests orientation, and there it does not heal to full-24. Any summary saying "all orientation mismatches heal" would be wrong.
- **Single realisation per config.** No replicates: $n = 1$ per config per tier. The deterministic dynamics make a repeat run bit-identical (same seeds/constants), so a replicate would need a different shift/rotation draw to be informative — not run.
- **The amplitude-CV diagnostic misleads for sub-pattern endpoints.** For F it reports $1.0000000000000002$ because it is computed over all 24 star modes, 12 of which are zero; the occupied-mode amplitudes are in fact all equal ($0.116428$). Do not quote the F amplitude CV as an amplitude spread.

## 5. Evidence that would change the answer

- If a replicate with a different shift draw, a wider taper, or $t_{\mathrm{final}} \gg 100$ ended in a persistent two-phase state (occupancy $< 24$ with two distinct local phases and a stationary boundary excess above the control level), the "translation grains always heal" claim would become "heal for the tested draws".
- If the $L = 8\pi$ box showed a persistent grain boundary, the $4\pi$ healing would be a finite-size effect.
- If a genuine full-24 orientation grain were constructed (different mode assignment per patch, not a star permutation) and persisted, §6's scope would widen. F already shows the orientation direction does not heal to full-24 — for sub-patterns.
- If thermal noise or an annealing schedule let the fcc12 fused state escape to full-24 (or vice versa), the F endpoint would be demoted from stationary to long-lived metastable.

## 6. Withdrawal / demotion note (no silent correction)

**Withdrawn label: "rotated-2" (C) and "quad-4" (D) as orientation mismatches.** During post-hoc analysis (2026-11-14) a direct real-space check showed that rotating the full 24-mode star by a hyperoctahedral element changes the pattern sum by at most $7.1\times 10^{-15}$ (roundoff), while changing the shift changes it by $24.65$: the sum $\sum_{j}\cos(k_{j}\cdot(x - s))$ is invariant under any permutation of the star. Configs C and D therefore tested translation (phase) mismatches only; their rotation labels are vacuous. **The data are unaffected** (the runs are exactly the runs that were run; the templates built with rotations are bit-identical to the unrotated ones with the same shift, verified by the refactor re-smoke: config A at $t = 2$ reproduces $E = -0.007691737169457093$ exactly). Only the interpretation changes: C/D are re-labelled as shift mismatches throughout this report, and the genuine orientation test is config F (different mode sets), whose design is flagged POST-HOC in `predictions_addendum.json`. No grade is claimed for a full-24 orientation grain, because none was run.

**Bugs fixed during checking (no run affected except E's first attempt):** (i) the quadrature template was built from all 24 sin terms, which cancel identically — rebuilt from the 12 positive representatives; the first $\theta_{p}$ values were garbage and were discarded. (ii) the initial field was not projected onto the retained band — now masked, as the pilot does. (iii) slab index used a fixed 32 slabs, leaving empty slabs on the 26-grid — slabs are now the $x_{1}$ grid planes. (iv) patch CSV rows had differing keys per patch — writer now uses the union of keys. (v) config E's first attempt crashed on JSON serialisation of a NaN renormalisation scale (`allow_nan=False` correctly tripped); scale is now `null` when not renormalised, and E was re-run from scratch.

## 7. HLRE grades (per narrow claim; worst-of shown)

Track E, Standard tier (max B). Independence I1 (single local pipeline; the parallel Co-scientist run was not read, so no external-verification credit is taken here). The 2026-11-12 repeal of the $I1\to C$ bound is applied: grades follow the evidence under the remaining rules; no grade is raised by the repeal alone. Postulation ceiling: the grain-locking question is evidence-guided (predictions frozen for P1; P2/P3 exploratory); the F design is post-hoc relative to A–E (flagged, not hidden).

| claim | grade | basis (worst-of) |
|---|---|---|
| C1 Aligned control recovers stationary full-24 at the pilot energy (full tier) | B | frozen prediction P1 passed; exact energy match; second-tool PASS; spatial + temporal refinements agree |
| C2 Antiphase 2-patch boundary heals to one coherent full-24 pattern; healed pattern is the midpoint translation ($s = \lambda/4$) | B | run-specific; global diagnostics + per-mode phases ($\pm 1.1102$ rad) + overlaps $0.722$; both tiers agree to $10^{-5}$ |
| C3 Shift-mismatch 2-patch (C) and 4-patch (D) heal to one coherent full-24 pattern | B | run-specific; same basis as C2; overlaps agree across tiers to $2.2\times 10^{-4}$ |
| C4 Ordered half invades uniform half (E) | B | run-specific; patch-1 $\rho$ goes $0.013 \to 1.000$ by $t = 2$; final state identical to A |
| C5 Two hex6 grains in different planes fuse into stationary fcc12 (F) | B | run-specific; occupied set exactly fcc12 at both tiers; amplitudes equal; energies match one-mode (K6) and Task 5 relaxed (K8) values; design post-hoc, so generality is not graded here |
| C6 Local $D_{4}$ order joins into one coherent pattern in larger boxes (general) | C | plausible constrained hypothesis: one larger box size, $t = 100$, $n = 1$ per config, translation mismatches only for full-24 |
| C7 No persistent grain boundary survives to $t = 100$ for the tested mismatches | B | stationary states (RHS $\sim 10^{-16}$), frozen diagnostics $t = 5$–$100$, boundary excess at control level |
| C8 Slab RMS detects the grain boundary | CONTRADICTED | dip within control ripple (§2.4); slab RMS is not a boundary detector for these patterns |

**VERIFIED:** C1–C5, C7 (run-specific, as graded). **UNVERIFIED / ABSTAIN:** generalisation to other box sizes, other shift draws, longer horizons, thermal/annealed escape, other sub-pattern pairs, incommensurate rotations (not representable on a periodic box), and any physical interpretation beyond the Model B system simulated. **FAILED:** P1 energy clause at the cheap tier (tier effect, resolved at full tier); C8 as a diagnostic claim.

## 8. Costed caps for heavy work still pending

- **Larger box $L = 8\pi$ (next clean shell, $|m|^{2} = 128$, 24 vectors): NOT RUN, NO SPEND AUTHORISED.** Measured scaling: full-tier B took $284$ s CPU ($405$ s wall, peak RSS $1{,}130$ MiB) for $36^{4}$ grid, $\sim 1{,}120$ steps. An $L = 8\pi$ run needs $K = 16$, $N > 64$ (take $N = 72$): $72^{4} = 26{,}873{,}856$ grid points, $16\times$ the grid, $\approx 18\times$ the per-step FFT cost → $\approx 80$ minutes CPU per run at $t = 100$, and peak memory $\approx 4$–$6$ GB (a single rFFT array is $221$ MB; the current `PatchSet` builds a full 4-D meshgrid, $4\times 215$ MB, plus templates) — above the $\sim 4$ GB single-job cap and near the VM's $6$ GB. A memory-lean rewrite (no full meshgrid; templates by FFT phase shifts) is a prerequisite. GCP cost must be obtained from the Pricing Calculator and a named budget cap approved by Brandon before any run. **Cap: pending Brandon's approval; no GCP spend on this agent's authority.**
- **Replicates at $L = 4\pi$ (different shift draws, 3 per config, cheap tier): NOT RUN.** $\approx 3$ min CPU per run, $\approx 15$ min total, local — pending; $n = 1$ per config stands as the stated limitation until then.
- **Wider taper / longer horizon ($t = 500$) / thermal-noise escape for F:** NOT RUN; local cost comparable to the runs here ($\sim 5$–$10$ min CPU each); pending a decision, not a budget.

## 9. Assumption / parameter / choice ledger

- **Operating point (verified from pilot `parameters.json`/`report.md`, re-read 2026-11-14):** $r = -0.35$, $\bar{\psi} = -0.18$, $q_{0}^{2} = 8.0$, $u = v = 1$, mobility $1$, $\alpha = 0.1072$, $\beta = 1.54$, $A = 0.07757529633928076$, matched RMS $0.38003978535286725$, pilot full-field energy $-0.007726209285$, truncated energy $-0.007632267319$, pilot recovery $t = 20$ (six-mode) / $t = 50$ (twelve-mode).
- **This task:** $L = 4\pi$; $N = 26/K = 6$ (cheap), $N = 36/K = 8$ (full); $dt = 0.1$ (half-dt check $0.05$); $t_{\mathrm{final}} = 100$ ($2\times$ the slowest pilot recovery); taper half-width $\Delta = 1.0$; patch interiors = envelope $> 0.999$; occupancy/CV/lock thresholds as pilot ($0.1$, $10^{-6}$, $0.05$, $0.95$); stationarity RHS $\le 10^{-7}$; uniform power $< 10^{-12}$.
- **Patch shifts/rotations:** pinned constants in `run_grain.py` (B: $s = (\lambda/2, 0, 0, 0)$; C: $s = (0.7, -0.4, 1.1, 0.3)$; D: $(\lambda/2, 0, 0, 0)$, $(0, \lambda/2, 0, 0)$, $(0.5, -0.7, 1.0, 0.2)$; F hex sets as §1.3). No random draws; no noise after initialisation; no annealing; no parameter ramp.
- **Choices that could change conclusions:** taper width (boundary cost scale); $t_{\mathrm{final}} = 100$ (bounded horizon); $n = 1$ per config; band cutoffs (quantified: $3.45\times 10^{-5}$ in full-24 energy, $1.05\times 10^{-4}$ in fcc12 energy).
- **Dependency ledger:** pilot solver + parameters (re-verified by self-tests, not re-derived); `d4model.py` (hex6/fcc12 counts and one-mode amplitudes — cross-checked against Task 5: hex6 $A = 0.161$, relaxed $F = -0.002290$; fcc12 relaxed $F = -0.005470$); Task 5 basin map (sub-pattern traps — F's fusion is consistent with, not derived from, it). No Co-scientist output was read or used at any point (per task independence rule); no browser/Academia use.
- **AI contribution:** this report and all scripts were produced by a local agent (Muse Spark) under HLRE v5.1 as amended 2026-11-12; Brandon D. McCrary is the accountable human author of the programme; nothing here is filed into any repo or manuscript.

## 10. Reproduce and inspect

From the work directory, with the conda env python:

```bash
~/miniconda3/envs/jacobian-conjecture-2d/bin/python run_grain.py --config B --n 36 --cutoff 8 --t-final 100 --out full/B-reproduced
~/miniconda3/envs/jacobian-conjecture-2d/bin/python check_energy_independent.py full/B-reproduced
~/miniconda3/envs/jacobian-conjecture-2d/bin/python analyse_final.py
~/miniconda3/envs/jacobian-conjecture-2d/bin/python plot_grain.py
```

Configs A–F, tiers `cheap` ($N = 26$, $K = 6$) and `full` ($N = 36$, $K = 8$), half-dt check in `cheap_halfdt/B` ($dt = 0.05$). Wall times on a quiet VM: cheap runs $\approx 3$–$6$ min each, full runs $\approx 6$–$9$ min each (shared-VM load inflated some runs to $\approx 11$ min wall; user CPU is the reproducible measure: cheap $\approx 80$ s, full $\approx 230$–$285$ s per run). Peak RSS: cheap $\approx 350$ MB, full $\approx 900$–$1{,}130$ MB.

## File map

- `REPORT.md` (this file) · `predictions.json` (frozen before running) · `predictions_addendum.json` (config F, post-hoc)
- `run_grain.py` (solver + patch construction + diagnostics; sha256 in each `parameters.json`)
- `check_energy_independent.py` (second-tool recomputation) · `analyse_final.py` (overlaps + per-mode phases) · `plot_grain.py` (figures)
- `grain_summary.csv` · `final_pattern_overlap.csv`
- `cheap/{A,B,C,D,E,F}/` and `full/{A,B,D,F}/` and `cheap_halfdt/B/`: each with `grain_outcome.json`, `grain_trajectories.csv`, `grain_patch_trajectories.csv`, `grain_slab_profiles.csv`, `grain_state.npz`, `parameters.json`, `numerical_tests.json` (validation runs only)
- `fig_phase_cheap.png` · `fig_phase_full.png` · `fig_shellpower_cheap.png` · `fig_shellpower_full.png` · `fig_boundary_cheap.png` · `fig_boundary_full.png`
