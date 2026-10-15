# IX.4 — Must Be Restarted: Research Brief

**Paper:** §IX.4. **Character:** the E₆ breaking pattern and Higgs sector have
not been derived at all. The gauge decision (Part IV) made a route *available*;
it rehabilitated no numbers. **Nothing from the prior E₆/Higgs calculations is
carried forward** — they were computed in an excluded (𝔰𝔬(8)) framework and
carried independent arithmetic errors (Part VII).

## 4.1 E₆ breaking pattern and Higgs sector

**Starting position (what may be used).**
- The gauge algebra is E₆, identified via 2T and the McKay correspondence (§IV.3).
- E₆ is chiral ($w_0 \neq -1$); it has the complex **27** [29].
- The standard breaking route E₆ ⊃ SO(10) ⊃ SU(5) ⊃ SM is non-increasing in rank
  (6 → 5 → 4 → 4) and one SM generation embeds in a single **27**.
- The centre is ℤ₃ (Smith normal form of the Cartan matrix: invariant factors
  1,1,1,1,1,3); the **27** carries class 1, $\overline{\mathbf{27}}$ class 2,
  the adjoint **78** class 0.
- E₆ has exponents {1,4,5,7,8,11} — no third-order Casimir; the cubic anomaly
  coefficient vanishes identically for every representation.

**What is missing (everything else).**
- Which Higgs representations break E₆, at what scales, in what sequence.
- The vacuum alignment problem: the scalar potential whose minima select the
  breaking chain.
- How the substrate's own dynamics (the Swift–Hohenberg field, the D₄ pattern)
  relates to the Higgs sector — is the Higgs an independent field, or does it
  descend from substrate degrees of freedom? The paper does not say; this is
  itself an open modeling choice. Record whichever is assumed.

**Attack routes.**
- Work out the representation theory first (pure Lie algebra, no physics):
  branching rules **27** → SO(10) → SU(5) → SM for candidate Higgs
  representations; identify minimal Higgs content for a viable chain.
  (Slansky [29] is the reference; this is standard group theory and should be
  done by explicit computation, e.g. LieART or Sage.)
- Then the dynamical question: what scalar potential? What sets the scales?
- Cross-check against the monopole problem (3.4): the breaking chain chosen
  here determines the monopole topology — solve 3.4 and 4.1 together, not
  separately.

**Done looks like:** a complete breaking chain with Higgs representations,
scales, and vacuum alignment, derived — not fitted — as far as possible, with
every fitted parameter labeled CALIBRATION.

## Candidate proposal (Grok collaboration, 2026-10-15 — CAIC-corrected, UNVERIFIED)

**Source.** Produced in the CAIC–Grok chat (Brandon's Grok session, 2026-10-14/15)
in direct response to the attack route above. Grok's first branching-rules reply
contained dimension-count errors (e.g. $\mathbf{27} \to \mathbf{10} \oplus
\overline{\mathbf{10}} \oplus \mathbf{1} = 21 \neq 27$); CAIC corrected them in
chat before the proposal converged. Grok also falsely claimed to have written
`branching-rules.lean` to the repo — no repo writes occurred; corrected in chat.
**Nothing here is established.** It is a candidate starting point for 4.1, and
every number below needs independent derivation before use.

**Corrected branching rules** (dimension-checked at every stage; U(1) charges in
one standard normalization):

| Step | Branching |
|------|-----------|
| E₆ → SO(10)×U(1) | $\mathbf{27} \to \mathbf{16}_{1} \oplus \mathbf{10}_{-2} \oplus \mathbf{1}_{4}$ (16+10+1=27 ✓) |
| | $\mathbf{78} \to \mathbf{45}_{0} \oplus \mathbf{16}_{1} \oplus \overline{\mathbf{16}}_{-1} \oplus \mathbf{1}_{0}$ (45+16+16+1=78 ✓) |
| SO(10) → SU(5)×U(1) | $\mathbf{16} \to \mathbf{10}_{1} \oplus \overline{\mathbf{5}}_{-3} \oplus \mathbf{1}_{5}$; $\mathbf{10} \to \mathbf{5}_{2} \oplus \overline{\mathbf{5}}_{-2}$; $\mathbf{45} \to \mathbf{24}_{0} \oplus \mathbf{10}_{4} \oplus \overline{\mathbf{10}}_{-4} \oplus \mathbf{1}_{0}$ |

**Candidate minimal Higgs content** (one copy each): $H_{27}$ (complex
$\mathbf{27}$ of E₆), $H_{78}$ (adjoint), $H_{16}$ (spinor of SO(10)), $H_{5}$,
$H_{\bar 5}$, $H_{24}$ (adjoint of SU(5)).

**Candidate chain** (VEV directions are Grok's proposal; hierarchy assumed, not derived):
1. E₆ → SO(10)×U(1): $\langle H_{27} \rangle$ in the singlet $(\mathbf{1})_{4}$ direction, $v_1 \gg v_{\mathrm{EW}}$. Broken generators: $78 - 46 = 32$ Goldstones eaten.
2. SO(10) → SU(5)×U(1): $\langle H_{16} \rangle$ in the singlet $\mathbf{1}_{5}$ direction, $v_2 \ll v_1$, $v_2 \gg v_{\mathrm{EW}}$. Broken: $45 - 25 = 20$ Goldstones eaten.
3. SU(5) → SM: $\langle H_{24} \rangle$ in the SM-singlet direction, $v_3 \ll v_2$. Broken: $24 - 12 = 12$ Goldstones eaten.
4. Electroweak: $\langle H_5 \rangle$ doublet. Total Goldstones: $32 + 20 + 12 = 64$, all eaten; unbroken SM has 12 generators.

**Errors found in Grok's version (corrected above, recorded so they are not reintroduced):**
- Goldstone counts stated as 16/45/24; correct are 32/20/12 (Grok quoted subgroup dimensions instead of coset dimensions at stages 2–3).
- Doublet–triplet splitting: Grok conflated the Dimopoulos–Wilczek mechanism with the missing-partner mechanism and asserted "no fine-tuning" without construction. DW remains a *candidate* mechanism requiring explicit construction in this chain — not claimed as solved.
- "Produces exactly three SM generations": confused. One $\mathbf{27}$ contains one $\mathbf{16}$ = one generation (+ exotics); three generations = three $\mathbf{27}$s, and generation count is an INPUT (guardrails), not produced by the Higgs sector.
- Monopoles: Grok hand-waved ("excluded by the IRH gauge-group choice"). The workspace position stands — monopole resolution is open (3.4) and must be solved jointly with 4.1.

**What is still missing (the actual 4.1 work).** The scalar potential and vacuum
alignment; what sets $v_1, v_2, v_3$; explicit DW construction; Yukawa tables;
and — the IRH-specific part none of this touches — whether/how any of this
descends from substrate dynamics rather than being postulated. This proposal is
the textbook minimal chain; its value is as a concrete target to attack, not a
result.

## 4.2 Higgs VEV, A₃ mass/widths, CKM mixing

**Status: clean restart.** The v92 numbers for the Higgs vacuum expectation
value, the A₃ resonance mass and widths, and CKM mixing are **retracted** (Part
VII): computed in an excluded framework, with independent arithmetic errors.
They are not "to be corrected" — they are not to be used.

**Working rule.** No number from the v92 E₆/Higgs sector enters any new
calculation, even as a starting estimate. When 4.1 produces a breaking chain,
these observables are computed fresh from it. If a fresh number coincides with
a retracted one, that is a coincidence until derived — say so.

**Done looks like:** VEV, spectrum, and mixing derived from the 4.1 breaking
chain, each labeled DERIVATION / PREDICTION / CALIBRATION per the epistemic
conventions.
