# IX.5 — The Genuinely Open Physical Questions: Research Brief

**Paper:** §IX.5. **Character:** "Two questions are sharper than the rest and
would most advance the programme." These are the highest-leverage targets in
the workspace. Everything else in Part IX is either computation (IX.1),
decision (IX.2), import (IX.3), or restart (IX.4) — these two are where new
physics has to come from.

---

## 5.1 What fixes $\bar\psi$?

**The problem, in the paper's words.** Under conserved (Model B) dynamics the
baseline tension $\bar\psi$ is an initial datum rather than a tuned coupling —
which reclassifies the fine-tuning objection as a cosmological
initial-condition question, "a different and weaker charge." But no mechanism
sets its value, so whether occupying the D₄ band is a prediction or a tuning
remains undetermined.

**Why it is sharp.** The entire selection result is conditional on
$\bar\psi$ lying in the band $-0.33 \lesssim \bar\psi \lesssim 0.03$ (11.85% of
the scanned plane, §II.7) *and* on $q_0$ being tuned onto the shell. Two
tunings, no mechanism for either. If a dynamical mechanism drives $\bar\psi$
into the band, the framework's central result upgrades from "conditional
prediction" to "prediction." If no such mechanism exists, the band occupancy is
an initial condition and the framework must own that as cosmology, not hide it
as dynamics.

**Attack routes.**
- **Dynamical relaxation:** does $\bar\psi$ flow toward the band under any
  extension of the dynamics? Under pure Model B it is exactly conserved
  ($8.3\times10^{-17}$ drift) — so the mechanism, if it exists, is not in the
  current equation. Candidate extensions: coupling to a slowly-rolling
  auxiliary field; backreaction of the pattern amplitude on the mean;
  higher-order terms ($w_6$) generating an effective potential for $\bar\psi$.
  Compute the effective potential $V_{\mathrm{eff}}(\bar\psi)$ including
  sixth-order terms and check for minima inside the band.
- **Cosmological selection:** if $\bar\psi$ is an initial datum, what
  cosmological history sets it? This couples to 5.2 (nucleation) and 3.4
  (inflation for monopole dilution) — a single early-universe narrative should
  address all three, not three separate patches.
- **Anthropic / environmental:** the weakest route; only if the dynamical and
  cosmological routes fail. Record explicitly if ever invoked — it changes the
  theory's character.

**Done looks like:** a mechanism (dynamical or cosmological) that places
$\bar\psi$ in the D₄ band, with the residual tuning quantified — or a theorem
that no such mechanism exists within the framework's dynamics, promoting the
band occupancy to a stated cosmological input.

## 5.2 What supplies the nucleation event?

**The problem, in the paper's words.** The transition is first order (§II.9):
at $\bar\psi=-0.18$, $r_{\mathrm{eff}}=+0.107>0$, the disordered state is
linearly stable, and the D₄ phase must be nucleated across a barrier.
"Spontaneous emergence from a featureless substrate does not occur at the
relevant baseline tension."

**Why it is sharp.** The framework's origin story — "spacetime crystallizes
from noise" — is literally false at the baseline tension where the D₄ phase is
the global minimum. Something must seed it. An unanswered 5.2 leaves the
framework without a beginning.

**Attack routes.**
- **Computational (→ 1.2):** barrier height and critical droplet size first —
  the numbers determine what kind of seed is needed (a rare thermal
  fluctuation? a pre-existing defect?). The II.9 consistency check
  ($r_{\mathrm{eff}}=+0.107>0$ confirmed) is in
  `verification/irh93_pkg2/FINAL_AUDIT.md` Part 2; droplet simulations extend
  the `verification/irh93_pkg2/sim6_units.py` seeded-state protocol.
- **The linearly-unstable path:** at lower $|\bar\psi|$ ($\bar\psi \approx
  -0.10$, $r_{\mathrm{eff}} < 0$) the disordered state is linearly unstable and
  the pattern *grows from noise* — no nucleation needed. A cosmological
  trajectory in which $\bar\psi$ evolves from the unstable region into the band
  would sidestep nucleation entirely. This couples to 5.1: if a mechanism
  drives $\bar\psi$, its trajectory matters as much as its endpoint.
- **Seed inventory:** topological defects as nucleation sites (cf. 1.4 —
  dislocation sheets and point solitons pre-exist in the disordered phase?);
  collisions; external driving during a quench.
- **Inflationary embedding (→ 3.4):** if the framework needs inflation for
  monopoles anyway, the inflaton dynamics may supply the seed or the
  $\bar\psi$ trajectory. One early-universe story, not three.

**Done looks like:** a stated nucleation mechanism with computed rates (or a
trajectory through the unstable region with computed evolution), consistent
with the 1.2 barrier numbers and the 5.1 $\bar\psi$ mechanism.

---

## The combined program

5.1 and 5.2 are not independent: the nucleation event happens *at* a value of
$\bar\psi$, and whatever fixes $\bar\psi$ determines whether nucleation is
needed at all. The highest-value single deliverable in this workspace is a
**joint early-universe narrative** — a cosmological history of the substrate
that (a) sets $\bar\psi$, (b) supplies or sidesteps the nucleation event, and
(c) dilutes the monopoles (3.4) — with each step computed, not asserted. That
narrative is currently missing in its entirety, and the framework has no
beginning without it.
