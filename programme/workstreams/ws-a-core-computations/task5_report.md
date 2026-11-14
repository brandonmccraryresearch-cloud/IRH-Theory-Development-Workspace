# Task 5 — Basin of the full 24-mode D4 pattern

**CLAIM:** Under conserved Model B dynamics $(L = \pi, q0^{2} = 8.0, \bar{\psi} = -0.18)$,
the full 24-mode D4 pattern is a strong attractor — it recovers from
phase perturbations up to 1.0 rad RMS and $\pm20$% amplitude perturbations —
but it is NOT the only attractor: the 6-mode hexagonal and 12-mode FCC
sub-patterns are stable attractors in their own right (a hex6 start stays
hex6, an fcc12 start stays fcc12, both fully converged by step 3000),
while the 4- and 8-mode square patterns decay to uniform (they have no
triads, hence no cubic term to sustain them), and small random noise
decays to uniform in all six seeds. The basin of the full pattern is
therefore: large-amplitude / full-pattern starts $\to$ full24; hex6/fcc12
starts $\to$ trapped in the sub-pattern; small noise or triad-less starts $\to$
uniform.

**STATUS:** VERIFIED for the 14-run protocol (6000 steps each). All runs
fully converged by step 3000 (Fexc and rms identical at steps 3000 and
6000 to 6 decimals). The sub-pattern trapping is the direct analogue of
the manuscript's "annealing leaves 6 modes occupied" — here demonstrated
under Model B rather than annealing, and extended to fcc12.

## 1. Results (final state at 6000 steps)

| start | D4 | ndom | lock | Fexc | rms | outcome |
|---|---|---|---|---|---|---|
| noise seeds 1–6 (amp 0.05) | 0.000 | — | — | 0.000000 | 0.000 | **uniform** (all six decay) |
| partial hex6 | 1.000 | 6 | 1.000 | $-0.002290$ | 0.395 | **hex6 (trapped)** |
| partial fcc12 | 1.000 | 12 | 1.000 | $-0.005470$ | 0.404 | **fcc12 (trapped)** |
| partial sq4 | 0.000 | 4 | — | 0.000000 | 0.000 | **uniform** (decays) |
| partial sq8 | 0.000 | 8 | — | 0.000000 | 0.000 | **uniform** (decays) |
| full, phase $\delta\phi = 0.1$ rad | 1.000 | 24 | 1.000 | $-0.007728$ | 0.381 | **full24 (recovers)** |
| full, phase $\delta\phi = 0.5$ rad | 1.000 | 24 | 1.000 | $-0.007728$ | 0.381 | **full24 (recovers)** |
| full, phase $\delta\phi = 1.0$ rad | 1.000 | 24 | 1.000 | $-0.007728$ | 0.381 | **full24 (recovers)** |
| full, amplitude $\pm20$% | 1.000 | 24 | 1.000 | $-0.007728$ | 0.381 | **full24 (recovers)** |

Dominant-mode identification is data-first (modes with |A| > $0.5\cdot\max$,
matched against the sub-pattern index sets): hex6's dominant set is
exactly the 6 seeded modes (overlap 6/6), fcc12's exactly the 12 seeded
modes (12/12), and the recovered full runs are all 24 modes (24/24).
For the decayed runs (noise, sq4, sq8) the "dominant" lists in the raw
output are roundoff noise on a uniform field (rms = 0) and carry no
information — the outcome is uniform, full stop. (For sq4/sq8 the listed
modes are the seeded ones, which decay slowest but still vanish.)

Relaxed vs one-mode free energies: hex6 relaxed $-0.002290$ vs one-mode
$-0.002254$; fcc12 relaxed $-0.005470$ vs one-mode $-0.005362$; full relaxed
$-0.007728$ vs one-mode $-0.007632$. Relaxation lowers each by ~1–2%, and
the relaxed amplitudes match the one-mode values (hex6 A = 0.161,
fcc12 A = 0.117, full A = 0.0777, from rms = $A\cdot\sqrt{n})$.

## 2. Basin map (reading)

- **Full pattern basin:** any start with all 24 modes present at ~A*
  (even with 1.0-rad phase noise or $\pm20$% amplitude noise) returns to the
  full pattern. The pattern is robust: the triad lock $(\langle\cos S\rangle = 1.000)$
  re-forms from strongly dephased starts.
- **Sub-pattern traps:** hex6 and fcc12 are genuine local attractors of
  the Model B dynamics — they persist unchanged for 6000 steps with
  locked triads and stationary free energy. A system prepared in hex6
  does NOT grow into full24 under these dynamics. This is the mechanism
  behind the manuscript's annealed 6-mode outcome, now shown for Model B.
- **No-triad patterns decay:** sq4 and sq8 have T = 0 (no closed triads),
  so their one-mode functional has no cubic term and no ordered minimum
  at $r_{eff} > 0$; under Model B they decay to uniform, as predicted.
- **Noise decays:** small random starts (amp 0.05) decay in all six
  seeds — the uniform state is metastable $(r_{eff} = +0.107 > 0)$, so
  nucleation needs a localised large-amplitude seed (Task 4), not
  homogeneous noise.

## 3. Protocol difference vs the manuscript (stated explicitly)

The manuscript's annealed run used damped-wave dynamics at $q0^{2} = 7.5$
and reported 6 of 24 modes occupied. These runs use conserved Model B
dynamics at $q0^{2} = 8.0 ($the tuned shell) with fixed 6000-step runs and
no annealing schedule. The comparison is therefore qualitative: both
protocols trap in sub-patterns (hex6 here, 6 modes there), but the
trapping mechanism and the $q0^{2}$ differ, and no claim is made that the
Model B basin equals the annealed basin. A direct annealed comparison
(damped-wave, $q0^{2} = 7.5)$ was not run.

## 4. Checks

| check | verdict |
|---|---|
| All 14 runs finite, $\bar{\psi}$ conserved $(-0.18000)$ | PASS |
| All runs converged by step 3000 (Fexc, rms identical at 3000/6000) | PASS |
| hex6/fcc12 dominant sets exactly the seeded sets (6/6, 12/12) | PASS |
| Recovered full runs: D4 = 1.000, Fexc = $-0.007728 ($matches sim6 relaxed value) | PASS |
| sq4/sq8 decay predicted by T = 0 (no one-mode ordered minimum) | PASS |
| Noise seeds decay in 6/6 (uniform state metastable, $r_{eff} > 0)$ | PASS |
| Perturbation seeds are real fields (antisymmetric phases, pairwise amplitudes) | PASS (construction) |
| check_model.py re-run after the stepper fix: ALL CHECKS PASSED | PASS |

**Withdrawal / demotion note (bugs found during checking):**
(i) The first Task 5 launch crashed immediately (`ValueError: (2,2,0,0)
is not in list`): the script used SCALED sub-pattern vectors for
Fourier-space seeding and ROOTS indexing, but `seed_subset` and ROOTS
use UNSCALED labels. Fixed by using `SUBPATTERN_LABELS` (the shared
module provides both conventions explicitly). No run was affected — the
crash happened before the first run. (ii) The Model B Hermitian-symmetry
artifact (see Task 4 report §6) was found and fixed before these runs;
all 14 runs used the fixed stepper. (iii) The first Task 5 launch was
killed by a service restart after 1 run; the script now saves results
incrementally after each run, and the relaunch completed all 14 runs
(EXIT:0).

## 5. Rival / failure mode

The main rival is run length: 6000 steps (30 time units) is long vs the
pattern-formation time (~250–500 steps), and the states are stationary
to 6 decimals from step 3000, so longer runs are unlikely to change the
outcomes — but a much longer run (or a finite-temperature / noise-driven
escape) could in principle let hex6/fcc12 escape to full24 over a
barrier. The basin boundaries (e.g. the critical phase-noise amplitude
between 1.0 rad and full dephasing, or the amplitude threshold for
noise-induced nucleation) were not mapped — only the stated points were
run. A second failure mode: the $\pi$-box is small (1.4 wavelengths across),
so periodic images may stabilise sub-patterns that would be unstable in
a larger box.

## 6. Evidence that would change the answer

- If a hex6 or fcc12 start grew into full24 on a longer run (or with
  added thermal noise), the "stable trap" claim would become "long-lived
  metastable" — the 6000-step stationarity bounds this but does not
  exclude very slow escape.
- If a noise seed grew to the full pattern, the nucleation threshold
  would be lower than stated; 0/6 grew here.
- A larger-box repeat would test whether the sub-pattern traps survive
  without periodic-image stabilisation (costed, not run — see Task 4 §8).

## 7. HLRE grades (per narrow claim; worst-of shown)

| claim | grade | basis |
|---|---|---|
| Full pattern recovers from $\delta\phi \leq 1.0$ rad and $\pm20$% amplitude | B | 4 direct runs, fully converged; protocol-specific (Model B, $q0^{2} = 8.0)$ |
| hex6 is a stable attractor under Model B (stays hex6) | B | direct run, stationary to 6 decimals from step 3000; 6000-step horizon |
| fcc12 is a stable attractor under Model B (stays fcc12) | B | same basis as hex6 |
| sq4/sq8 decay to uniform | B | direct runs + one-mode prediction (T = 0) agree |
| Noise seeds decay (6/6) | B | direct runs; small-sample (n = 6) |
| Basin map as stated (full / sub-pattern traps / uniform) | B | 14-run protocol; box-size and run-length caveats in §5 |

## 8. Deliverables

- Figure: `figures/task5_basin.png` (Fexc trajectories + final-state map)
- Table: `tables/task5_basin.json` (all 14 runs, full time series)
- Code: `task5_basin.py` (uses shared `d4model.py`, fixed stepper)

## 9. Assumption / parameter / choice ledger

- Model $B: L = \pi$, N = 16, $q0^{2} = 8.0$, $r = -0.35$, u = v = 1, dt = 0.005,
  6000 steps/run; $\bar{\psi} = -0.18$ conserved.
- Noise starts: Gaussian, amp 0.05, seeds 1–6 (numpy default_rng).
- Partial starts: sub-pattern modes at A* = 0.0776, zero phases.
- Perturbed full starts: phases ~ N(0, $\delta\phi)$ antisymmetric
  $(\phi_{-n} = -\phi_{n})$; amplitudes uniform in [0.8, 1.2]$\timesA$* pairwise
  (|ph[n]| = |ph$[-n]$|) — both keep the field real.
- Dominant modes: |A| > $0.5\cdot\max$; sub-pattern match by index-set overlap.
