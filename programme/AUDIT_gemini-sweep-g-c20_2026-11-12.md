# AUDIT — Gemini Sweep 4 (G-C20): Greensite one-loop mechanism

**Audit date:** 2026-11-12 (evening CST)
**Auditor:** local audit (CAIC), claim-by-claim, firsthand primary sources + independent SymPy re-derivation
**Subject:** Gemini Deep Research report, Sweep 4 (G-C20), run 2026-11-12 16:15–16:59 CST on gemini.google.com (Deep Research, Argon chat; 31 websites researched; \$0)
**Verbatim record:** `gemini-sweep-g-c20-2026-11-12.md` (818 lines; chat saved at https://gemini.google.com/u/1/app/3ab99307796e234c)
**Governing rules:** truth-seeking-frontier v5; cross-domain-discovery; HLRE v5.1 **as amended 2026-11-12** (human gate repealed; I1 bound repealed and replaced by external verification by a capable HLRE-constrained agent, audited locally claim-by-claim; grades follow the evidence under the remaining rules).
**Scope of this file:** reports only. Nothing filed, committed, or written into the manuscript. Local work only; no GCP spend; \$0.

## CLAIM and STATUS

| Item | Gemini's claim | Audit verdict |
|---|---|---|
| G-C20 (gap) | RESOLVED — upgraded from ABSTAIN/NOT RUN (toy G5/F3) to **Grade B (Track E) / F2 (Track F)** | **RESOLVED — Grade B (Track E) / F2 (Track F). CONFIRMED.** |
| G-C20.1 | Exact one-loop potential recovered | VERIFIED |
| G-C20.2 | $D = 4$ uniqueness, Cases I–V, dimension table | VERIFIED WITH CORRECTIONS (2 verdict-neutral corrections) |
| G-C20.3 | Curved-spacetime consistency (§3) | VERIFIED WITH CORRECTIONS (1 verdict-neutral correction) |
| G-C20.4 | §4 cosmological-constant subtraction, $D = 4$ only | VERIFIED WITH CORRECTIONS (1 transcription note + 1 omitted qualification) |
| G-C20.5 | §5 mass effects, $D = 6$ broken-SUSY exception | VERIFIED WITH CORRECTIONS (1 material precision correction + 1 omitted regime) |
| G-C20.6 | Regularization dependence (heat-kernel) | VERIFIED |
| G-C20.7 | Scope: C&G pp. 16–22 + Appendix eqs. 81–87; Elizalde 1994; C&G 1995 | **RESOLVED BY THE AUDIT** (Gemini's partial ABSTAIN superseded — material retrieved firsthand) |
| IRH-C20a | §IX.3 misattributes [17]/[18]; "no classical substrate" contradicted by [17]; graded D/F4 | **VERIFIED — manuscript sentences grade D (Track E).** Gemini's "F4" is **not a valid HLRE grade** (ladder is F1–F3); corrected to **F2** for the refutation claim. |
| IRH-C20b | $N_{\mathrm{gen}} \geq 3$ may follow from Greensite + unbroken $E_6$ | **CONDITIONAL** (Track E C / Track F F3). Arithmetic VERIFIED; premises NOT established in the manuscript. |
| Scoped narrower reading | No classical mechanism for single-scalar Swift–Hohenberg $D_4$ substrate without a tuned clock field found | ABSTAIN (scoped) — absence in consulted sources, not a proof of nonexistence. |

**Verdict counts (claims):** 10 items audited — 7 VERIFIED (2 clean, 4 with corrections, 1 refutation verified), 1 RESOLVED BY THE AUDIT (G-C20.7), 1 CONDITIONAL (IRH-C20b), 1 ABSTAIN (scoped reading). **0 of Gemini's claims REFUTED.** Every correction below is verdict-neutral except the grading-label correction (F4 $\to$ F2) and the scope qualification from Elizalde (topology dependence of $D = 4$ uniqueness).

**Checks:** 61 checks — 55 PASS, 4 CORRECTED (verdict-neutral), 1 FAIL (Gemini's "F4" grade label only), 1 NOT RUN (Gemini's unrecoverable SymPy link, superseded by the local re-derivation). (Detail in the checks table at the end.)

## Method and tools

Primary sources were fetched and read firsthand in full: Greensite 1993 (arXiv:gr-qc/9210008), Carlini & Greensite 1994 (arXiv:gr-qc/9308012, all 2,840 lines incl. Appendix eqs. 81–87), Mukohyama & Uzan 2013 (arXiv:1301.1361, all 2,574 lines), Kehayias, Mukohyama & Uzan 2014 (arXiv:1403.0580, lines 0–357 re-fetched this session; abstract, §I, §II.A–B), Elizalde, Odintsov & Romeo 1994 (arXiv:hep-th/9312132, all 950 lines — Gemini abstained on this; the audit retrieved it), Carlini & Greensite 1995 (arXiv:gr-qc/9502023, abstract page). Manuscript text is from the local PDF `~/workspace/research/IRH-Theory-Development-Workspace/IRH_v93_1.pdf` (md5 952116b3154824e3a19fcdc558898c5f), extracted with `pdftotext` to `/tmp/irh_v93_1.txt` (1,472 lines, 31 pages).

Independent re-derivation: Python 3.11.16, SymPy 1.14.0, mpmath (conda env `jacobian-conjecture-2d`); scripts `/tmp/gc20_sympy.py`, `/tmp/gc20_sympy2.py`, `/tmp/gc20_sympy3.py`; all three runs **exit code 0**. Gemini's cited SymPy recomputation link is unrecoverable (renders as an empty link) — confirmed; Gemini's computation therefore cannot be counted as an independent route, and the local re-derivation below is the single independent route (hence F2, not F1, for the gap as a whole).

---

## G-C20.1 — Exact one-loop potential recovered

**Gemini's claim:** the exact potential is $V(\theta) = (n_F - n_B) \Lambda^D/[D(4\pi)^{D/2}] \exp[-i(D-2)\theta/4]$; the toy $\mathrm{Re}\, V_{\mathrm{toy}} = \Delta \cos\theta$ missed the $(D-2)/4$ factor (in $D = 4$, $\mathrm{Re}\, V \propto \cos(\theta/2)$).

**VERIFIED.** Greensite 1993, eq. (9): $V_S(\theta) = -\Lambda^D/[D(4\pi)^{D/2}] \exp[-i(D-2)\theta/4]$; eq. (10): $V(\theta) = (n_F - n_B) \Lambda^D/[D(4\pi)^{D/2}] \exp[-i(D-2)\theta/4]$. Carlini & Greensite 1994, eqs. (15)–(17), reproduce the same form with the multi-species factor. The setup is confirmed verbatim: $\eta_{ab} = \mathrm{diag}\{e^{i\theta}, 1, \dots, 1\}$ (Greensite eq. (7); C&G eq. (1)), the interpolating path integral (Greensite eq. (6)), the two measure assumptions (equal-and-opposite boson/fermion contributions; real DeWitt measure), and the $[-\sqrt{\eta}\, \eta^{ab} \partial_a \partial_b]$ form (Greensite eq. (8)). The $(D-2)/4$ phase is confirmed in both papers; at $D = 4$, $\mathrm{Re}\, V \propto \cos(\theta/2)$, so the toy's cos $\theta$ was indeed missing the $(D-2)/4$ factor. The potential was re-derived locally from the Gaussian integrals and the proper-time integral (see Re-derivation, steps (a)–(b)): $V_S - (-\Lambda^D/[D(4\pi)^{D/2}] \exp[-i(D-2)\theta/4]) = 0$ (SymPy, exact), and $V = (n_F - n_B)(-V_S)$ matches eq. (10).

## G-C20.2 — $D = 4$ uniqueness, Cases I–V, dimension table

**Gemini's claim:** Cases I–V (C&G eq. (18)) give a unique Lorentzian solution at $\theta = \pi$, $\bar{\theta} = \pi$, $D = 4$ for the massless case; the dimension table lists stationary points, minima, and case assignments; fluctuations are suppressed as $\langle\delta\theta\rangle \sim l_P^3/V \sim (l_P/R)^3$.

**VERIFIED WITH CORRECTIONS.** C&G eq. (18) and Cases I–V confirmed verbatim from §2 (Case I: $n_F < n_B$, no solution; Case II: $D = 2$ or $n_F = n_B$, $V$ $\theta$-independent; Case III: $D = 1, 3$ with $(D-2)\pi/4 < \pi/2$, no stationary point; Case IV: $D \geq 5$ with $(D-2)\pi/4 > \pi/2$, stationary point $\neq$ minimum; Case V: $D = 4$ with $(D-2)\pi/4 = \pi/2$, i.e. $\bar{\theta} = \pi$, stationary point = minimum at $\theta = \pm\pi$). The dimension table was re-enumerated locally (exact enumeration, see Re-derivation step (c)): $D = 1, 3$ no stationary points, $\min \mathrm{Re}\, V = +0.707107\cdot C(n_F-n_B)$; $D = 2$ $\theta$-independent; $D = 4$ stationary at $\theta = \pm\pi$, $\mathrm{Re}\, V = 0$ there, $\min 0$; $D = 5$ stationary at $\theta = \pm 2\pi/3$, $\mathrm{Re}\, V = 0$, $\min -0.707107$ at $\theta = \pm\pi$; $D = 6$ stationary at $\theta = \pm\pi/2$, $\mathrm{Re}\, V = 0$, $\min -1$ at $\theta = \pm\pi$; $D = 7$ stationary at $\theta = \pm 2\pi/5$, $\mathrm{Re}\, V = 0$, $\min -1$ at $\theta = \pm 4\pi/5$.

- **CORRECTION 1 ($D = 7$ row):** Gemini's table gives the $D = 7$ global minimum as "$-C_7 (n_F - n_B) \sqrt{2}/2$" at "$\theta = \pm 4\pi/5$". That value is wrong. $\mathrm{Re}[V(\theta)]$ on $D = 7$ attains its minimum $-C_7 (n_F - n_B)$ at $\theta = \pm 4\pi/5$ (since $5\theta/4 = \pm\pi$ there); the value $-C_7 (n_F - n_B) \sqrt{2}/2$ is $\mathrm{Re}\, V$ at $\theta = \pm\pi$ ($\cos(5\pi/4) = -\sqrt{2}/2$), which is not the minimum. The correct minimum is **$-C_7 (n_F - n_B)$** at $\theta = \pm 4\pi/5$. Location right, value wrong. Verdict-neutral: $D = 7$ stays Case IV, no solution.
- **CORRECTION 2 (fluctuation number):** C&G eqs. (36)–(37) give $\langle\delta\theta\rangle \sim l_P^3/V$ and quote $10^{-184}$ rad for $R \sim 10^{10}$ ly. Recomputed locally: $(l_P/R)^3 = 4.99\times10^{-183}$ for $l_P = 1.616255\times10^{-35}$ m, $R = 10^{10}$ ly ($1.19\times10^{-183}$ with spherical volume). The paper's quoted $10^{-184}$ is ~50$\times$ too small. The qualitative conclusion (enormous suppression) is unaffected; the number as quoted is off by ~1.7 dex. Gemini repeated the paper's figure without recomputing.

## G-C20.3 — Curved-spacetime consistency (§3)

**Gemini's claim:** C&G §3 imposes three consistency requirements (flat tangent-space metric; -independence of the number of inequivalent vielbein degrees of freedom; consistent covariant derivative for Dirac spinors), rules out a multi-angle generalization (eq. (20)), and finds fluctuations away from Lorentzian signature enormously suppressed.

**VERIFIED WITH CORRECTIONS.** The three requirements are confirmed verbatim from C&G §1 (roadmap) and §3 (conclusion): "(i) the tangent space metric $\eta_{\mu\nu}$ is flat; (ii) the number of gravitational degrees of freedom is independent of $\eta_{\mu\nu}$; (iii) a spin connection with appropriate properties is obtained in the Dirac action" (§1), restated in §3 as requiring flat $g_{\mu\nu} = \eta_{\mu\nu}$, $\theta$-independence of the inequivalent-vielbein count, and a covariant derivative for spinors with appropriate properties. The single-angle result is confirmed: §3 shows the multi-angle generalization (eq. (20), independent $\theta_i$ for each direction) is ruled out and a single global Wick angle survives; eqs. (36)–(37) give the fluctuation suppression (subject to Correction 2 above on the quoted number). No further correction to this sub-item; the fluctuation-number correction is carried here as well since Gemini cites the $10^{-184}$ figure in this context.

## G-C20.4 — §4 cosmological-constant subtraction, $D = 4$ only

**Gemini's claim:** setting $V_T(\theta) = 0$ and $\frac{d}{d\theta} \mathrm{Im}[V_T(\theta)] = 0$ (eqs. (41)–(47)) forces $\bar{\theta} = (2n+1)\pi$ and $\theta = \pi$ with $\lambda_c = \lambda$, which is possible only in $D = 4$; then $V_T(\theta) = \lambda \cos(\theta/2)$ with minimum at $\theta = \pi$ (eq. (48)).

**VERIFIED WITH CORRECTIONS.** C&G §4, eqs. (38)–(48), confirmed from the full text: $V_T(\theta) = V_c(\theta) + V(\theta)$ (eq. (38)); $V_c(\theta) = \lambda_c e^{i\theta/2}$ (eq. (39), classical $\sqrt{g}$ piece); the $V_{T} = 0$ real/imaginary conditions (eqs. (42)–(43)); the stationarity condition (eq. (44)); the solution $\bar{\theta} = (2n+1)\pi$, $\theta = \pi$ (eq. (45)); $\lambda_c = \lambda$ (eq. (46)); the argument that $\mathrm{Re}[V_{T}(')] < 0$ for any other $' ($eq. (47)); and $V_T(\theta) = \lambda \cos(\theta/2)$ (eq. (48)) with $\theta = \pi$ the minimum. The $D = 4$-only logic was verified symbolically: $\bar{\theta} = \pi$ and $\theta = \pi$ simultaneously requires $(D-2)/2 = 1$, i.e. $D = 4$ (SymPy `solve`, exact). The minimum location is confirmed: $\cos(\theta/2)$ on $\theta \in [-\pi, \pi]$ is minimized ($0$) at $\theta = \pm\pi$.

- **CORRECTION $3 (V_{T}$ prefactor — transcription note):** the algebra from eqs. (39)–(46) gives $V_T(\theta) =$ **$2\lambda \cos(\theta/2)$** at $\theta = \pi$ ($V_T = \lambda_c e^{i\theta/2} + \lambda e^{-i\theta/2}$ with $\lambda_c = \lambda$, hence $\lambda(e^{i\theta/2} + e^{-i\theta/2}) = 2\lambda \cos(\theta/2)$; SymPy `rewrite(cos)` confirms the identity exactly). The browser OCR of the paper's eq. (48) reads "$V_T(\theta) = \lambda \cos(\theta/2)$". Either the paper's eq. (48) drops a factor of 2 or the OCR dropped it; the prefactor does not affect the minimum location or the $D = 4$-only conclusion. Flagged as a transcription note, not a verdict-changer.
- **OMITTED QUALIFICATION (masses undo the exact cancellation):** Gemini's §3.2 does not mention that C&G §5 states the §4 exact cancellation becomes approximate once masses are included: "since non-zero mass terms displace the stationary point slightly away from the minimum point at $D = 4$ ($n_F > n_B$) and $D = 6$ ($n_F = n_B$), the exact cancellation of the cosmological constant found in section 4 is no longer quite exact. Although the real part of $V_T(\theta)$ can be cancelled exactly at the minimum point ($|\theta| = \pi$), one would expect a small imaginary part, of order $m^4/\Lambda^4$, left over." Recorded here; it bears on G-C20.4's scope (the §4 result is exact only in the massless limit).

## G-C20.5 — §5 mass effects, $D = 6$ broken-SUSY exception

**Gemini's claim:** mass terms preserve the minimum of $\mathrm{Re}\, V$ at $\theta = \pi$ but shift the stationary point of $\mathrm{Im}[V(\theta)]$ by $O(m^2/\Lambda^2) \approx 10^{-8}$ (GUT masses, Planck cutoff), so the coincidence becomes approximate up to $O(m^2/\Lambda^2)$ (eq. (58)); the $D = 6$ Lorentzian solution requires two inequalities on the mass-spectrum differences ($\Delta(x)_{BF} < 0$ and $\Delta(x_3)_{BF} < 0$), so it is conditional on the spectrum; the paper proves it for the massive spectrum of broken supersymmetry.

**VERIFIED WITH CORRECTIONS.** C&G §5, eqs. (49)–(59), confirmed: mass-corrected potential with incomplete gamma functions $\Gamma(-D/2, x_{B(F)\pm})$; eq. (57) $\mathrm{Re}[V(\bar{\theta})]$; eq. (58) with the $O(m^2/\Lambda^2)$ error term ("if masses are on the order of the GUT scale and $\Lambda$ is on the order of the Planck scale, we would expect $m^2/\Lambda^2 \approx 10^{-8}$"); the $D = 4$ case (eqs. (60)–(64)); the $D = 2$ case (eqs. (65)–(66), no coincidence); the $\Delta(n)_{BF} = 0$ cases at $D = 2$–$6$ and $D > 6$ (eqs. (67)–(80)); the $D = 6$ case (eqs. (73)–(77)) with the two inequalities $\Delta(x)_{BF} < 0$ and $\Delta(x_3)_{BF} < 0$, giving min $\mathrm{Re}\, V$ at $|\theta| = \pi$ and the stationary point at $|\bar{\theta}| = \pi + \epsilon$ with $\epsilon$ positive and $O(m^4/\Lambda^4)$; §6 conclusions ("Lorentzian signature is dynamically selected, for $n_F > n_B$, uniquely in $D = 4$ dimensions. In broken supersymmetry theories, there is also a possibility for Lorentzian signature at $D = 6$").

- **CORRECTION 4 (shift size — material precision correction):** Gemini states the stationary point is shifted "by $O(m^2/\Lambda^2) \approx 10^{-8}$". That is not what the paper says. The paper's eq. (64) gives the shift as **$|\bar{\theta}| = \pi + O(10^{-16})$**. The $10^{-8}$ figure is the error term in eq. (58)'s approximate equality ($\min[\mathrm{Re}\, V] \approx \mathrm{Re}[V(\bar{\theta})]$ up to $O(m^2/\Lambda^2)$ corrections), not the shift. Gemini conflated the two. The shift is ~8 orders of magnitude smaller than Gemini states. The substance (coincidence becomes approximate; Lorentzian still optimal) stands; the numerical claim about the shift size is wrong.
- **OMITTED REGIME (additional solutions):** Gemini does not mention the §5 regime note: "If the Planck scale is not a fundamental cutoff, so that $\Lambda$ can be taken arbitrarily large, or if the mass generation scale is many orders of magnitude less than the presumed grand unification scale, then it is appropriate to treat $\Delta(x \ln x)_{BF} \gg \Delta(x)_{BF}$. In that case, in addition to Lorentzian solutions at $D = 4$ ($n_F > n_B$) and $D = 6$ ($n_F = n_B$) we find additional Lorentzian solutions at $D = 2$ ($\Delta(n)_{BF}$ arbitrary), and $D = 4$ ($n_F = n_B$)." The $D = 4$/$D = 6$ uniqueness therefore holds under the $\Delta(x \ln x)_{BF} \sim \Delta(x)_{BF}$ regime; in the $\Delta(x \ln x)_{BF} \gg \Delta(x)_{BF}$ regime there are additional solutions. Recorded as a scope qualification.

## G-C20.6 — Regularization dependence (heat-kernel)

**Gemini's claim:** the mechanism depends on the regularization choice; heat-kernel regularization is the one that preserves the $D = 4$ result, while zeta-function, dimensional, and lattice regularizations give different results (or none).

**VERIFIED.** C&G §2 regularization paragraph confirmed verbatim: "In fact, the choice of heat-kernel regularization is essentially unique in the present context. ... The reason is the following: The regularization must preserve the property that the contribution of a massless bosonic degree of freedom to $V(\theta)$ is the negative of the contribution of a massless fermionic degree of freedom... The heat-kernel regularization has this property, and no other regularization we know of (e.g. zeta-function, dimensional, or lattice regularization) has this property." The premise is therefore ledgered, not hidden: the $D = 4$ result depends on heat-kernel regularization, and the paper argues (rather than proves) that it is the appropriate choice. The mechanism's conclusion is conditional on that regularization premise; the paper's own argument for it is recorded, not independently verified by this audit (it is a judgment about regularization, not a computation).

## G-C20.7 — Scope: C&G pp. 16–22 + Appendix eqs. 81–87; Elizalde 1994; C&G 1995

**Gemini's claim:** partial ABSTAIN — C&G pp. 16–22 and Appendix eqs. 81–87 not extracted; Elizalde et al. 1994 full text inaccessible (abstract + secondary sources only); Carlini & Greensite 1995 (gr-qc/9502023) exists and is out of scope.

**RESOLVED BY THE AUDIT (Gemini's partial ABSTAIN superseded).**

- **Appendix eqs. 81–87 — RETRIEVED.** The audit read C&G 1994 lines 2503–2840 (end of paper). Eq. (81): $\Gamma(-D/2, x_\pm)$ expansion; eq. (82): $E_1(x_\pm)$ definition; eq. (83): stationarity-condition expansion up to $O[\Delta(x_4 \ln x)_{BF}]$, with Heaviside step function $h(y)$ defined in eq. (84); eq. (85): $\mathrm{Re}[V(\theta)]$ expansion; eq. (86): $\mathrm{Im}[V(\theta)]$ expansion; eq. (87): the $\mathrm{Re}[V(\bar{\theta})]$ form of eq. (57). The OCR is garbled in places but the equations and their structure are legible and consistent with §5. The §5 analysis on pp. 16–22 was also read firsthand (§5, eqs. (73)–(77), see G-C20.5). Nothing in the Appendix contradicts the §5 analysis; the expansions are in powers of $m^2/\Lambda^2$ with Heaviside factors $h(D-4)$, $h(D-6)$, $h(D-8)$.
- **Elizalde et al. 1994 — RETRIEVED IN FULL.** The audit fetched arXiv:hep-th/9312132 (all 950 lines). This resolves Gemini's ABSTAIN and adds a genuine scope qualification:
  - The paper applies the Greensite formalism to topology $R^4 \times T^n$. It restates the setup ($\eta_{ab}$ = diag$(e^{i}, 1, \dots)$, eq. (1); assumptions (i)–(ii); heat-kernel regularization; ($n_B - n_F$) multiplier) and the conditions (18): $\mathrm{Im}\, V$ stationary, $\mathrm{Re}\, V$ minimum.
  - Eq. (19), R $\to$ $\infty ($trivial topology): $n_F > n_B$, $\theta = \pm\pi$, $D = 4$ — the unique solution, as in Greensite/C&G.
  - Eq. (20), small radius, periodic boundary conditions: **$n_F > n_B$, $\theta = \pm\pi$, $D = 5$** — "the Lorentzian signature is singled out also in $D = 5$, but only if the fifth dimension is compactified with a very small radius. Therefore, the formalism of the dynamical degree of freedom associated to the Wick angle provides a window for Kaluza-Klein-type theories."
  - Eq. (21), $R^{D-n} \times T^n$ with small equal torus radii: **$n_F > n_B$, $\theta = \pm\pi$, $D = 4 + n$** — "an early universe with a nontrivial topology could have been multidimensional, and this is compatible with the Lorentzian signature."
  - Antiperiodic boundary conditions, small radius (eq. (22)): **no genuine solution** — "there is no genuine coincidence of stationary points and minima, unless very specific values of $b$ and $D$ are deliberately chosen for that purpose"; a plateau forms where $V$ becomes practically independent of $\theta$ and no signature is preferred.
  - Conclusions: "the Lorentzian signature can actually be dynamically induced in a multidimensional universe with the topology $R^4 \times T^n$, where the radii of the torus are small"; mass effects "might increase the resulting D until $D = 6$" and "the combination of both effects (topology and nonzero mass) may lead to changes in the above results."
  - **Scope consequence:** $D = 4$ uniqueness holds for trivial topology. With a compact dimension (periodic BC, small radius), $D = 5$ and $D = 4 + n$ also select Lorentzian. The manuscript's "four-dimensional optimality as evidence about spacetime" (Reading A, §IX.2) therefore depends on the trivial-topology assumption, which the manuscript does not establish. This does not overturn G-C20; it limits the uniqueness claim's scope. (Note the cross-link: the $R^4\times T^1$ compact case is the manuscript's Reading (B) — four spatial dimensions with one compactified — which §IX.2 says "breaks the $D_4$ symmetry the selection argument uses". The audit does not pursue that cross-link further; it is flagged for the record.)
- **Carlini & Greensite 1995 — EXISTS, OUT OF SCOPE CONFIRMED.** arXiv:gr-qc/9502023, "Square Root Actions, Metric Signature, and the Path-Integral of Quantum Gravity", A. Carlini, J. Greensite, submitted 9 Feb 1995 (v2 18 Jul 1995). Abstract: BSW square-root action, path integrand $\exp[\sqrt{i}\, S]$ rather than $\exp[iS]$, unitarity requires integration over manifolds of both Euclidean and Lorentzian signature; extends the approach to fermions. This is a different line of work from the one-loop Wick-angle potential; Gemini's out-of-scope characterization is correct.

---

## IRH-C20a — §IX.3 misattributes [17]/[18] (load-bearing for the manuscript)

**Gemini's claim:** IRH v93.1 §IX.3 misattributes Mukohyama & Uzan 2013 [17] and Kehayias, Mukohyama & Uzan 2014 [18] — they are classical clock-field models, not one-loop $V(\theta)$ models; the manuscript's "No purely classical Euclidean substrate is known to yield Lorentzian signature" is contradicted by [17]; graded D/F4. Narrower scoped reading: no classical mechanism was found for a single-scalar Swift–Hohenberg $D_4$ substrate without a tuned clock field.

**VERIFIED.** The manuscript text, the two cited papers, and the bibliography were all read firsthand.

Manuscript §IX.3 (p. 25), verbatim from the local PDF:

> "Lorentzian signature. Published dynamical-signature mechanisms [17] [18] require a one-loop effective potential with more fermionic than bosonic degrees of freedom — the condition first identified by Greensite [41] and refined by Carlini and Greensite [42]. No purely classical Euclidean substrate is known to yield Lorentzian signature. The v92 argument from $i^2 = -1$ is invalid: canonical quantization employs complex amplitudes in Euclidean field theory as well, and an ordinary Hilbert-space inner product is positive-definite, so obtaining $g_{00} = -1$ requires a separate construction."

Bibliography confirmed: [17] Mukohyama & Uzan 2013, [18] Kehayias et al. 2014, [41] Greensite 1993, [42] Carlini & Greensite 1994 — the numbers in §IX.3 refer to the clock-field papers, as Gemini states.

[17] Mukohyama & Uzan 2013 (arXiv:1301.1361), confirmed classical:
- Abstract: "at the microscopic level the metric is Riemannian, i.e. locally Euclidean, and ... the Lorentzian structure ... is in fact an effective property that emerges in some regions of a 4-dimensional space with a positive definite metric. ... one can construct a decent classical field theory for scalars, vectors and (Dirac) spinors in flat spacetime. ... The construction, while restricted to classical fields in this article, offers a new view on the notion of time."
- §I: "the fundamental physical theory is intrinsically purely Euclidean so that its field equations determine a static 4-dimensional field configuration. The Lorentzian dynamics ... has then to be thought of as an emergent property ... holding in a small patch of a Euclidean mathematical space." And: "We show that the whole standard model of particle physics can be constructed from a Euclidean theory, at the classical level."
- §II.A (clock field): $\phi$ in $M_0$, $\partial_\mu \phi = M^2 n_\mu$, $t \equiv \phi/M^2$; the scalar action flows to the Minkowski action in $M_0$.
- The paper's own limitations list, confirmed verbatim (browser find on the full text): "(1) It requires that the clock field satisfies $\partial_\mu \phi = \mathrm{const.} \neq 0$ in a region $M_0$ of the Euclidean space. It follows that the effective Lorentzian description is local and holds in $M_0$. ..." and "(2) It is limited to classical field theory in flat space. The extension to curved space is discussed in § III and § IV below and the quantum aspects are left for future investigations." Gemini's paraphrase ("[a nonvanishing gradient constraint]") is accurate; the section label "§IIG (p. 8)" was not independently verified by the audit and is not vouched for here.

[18] Kehayias, Mukohyama & Uzan 2014 (arXiv:1403.0580), confirmed classical:
- Abstract: "This article investigates the construction of fermions and the formulation of the Standard Model of particle physics in a theory in which the Lorentz signature emerges from an underlying microscopic purely Euclidean S theory. Couplings to a clock field are responsible for triggering the change of signature of the effective metric in which the standard fields propagate."
- §I: "In Ref. [11], two of us have proposed that at the microscopic level the metric is Riemannian and that the Lorentzian structure, usually thought of as fundamental, is in fact an effective property that emerges in some regions of a 4-dimensional space with a positive definite metric." And: "We argued that a decent classical field theory for scalars, vectors, and spinors in flat spacetime can be constructed..." And, in the authors' own words on the gaps: "(1) the construction is restricted to classical field theory and the spinor sector suffers from a severe fine-tuning to ensure CPT invariance..."
- §II.A–B: clock field $\phi$ (eq. (1)), $\partial_\mu \phi = M^2 n_\mu$ (eq. (3)); scalar and vector actions flow to the Minkowski actions in $M_0$ (eqs. (4)–(7)); Dirac fermions §II.B.

**Finding.** The first §IX.3 sentence is false as applied to [17]/[18]: neither paper requires, uses, or invokes a one-loop effective potential with $n_F > n_B$. Both are classical clock-field models. The second sentence ("No purely classical Euclidean substrate is known to yield Lorentzian signature") is contradicted by [17] itself, which is precisely a purely classical Euclidean substrate yielding Lorentzian signature (locally, in $M_0$, under the $\partial_\mu \phi = \mathrm{const.} \neq 0$ condition). The Greensite/C&G attribution in the same paragraph ([41]/[42] for the one-loop condition) is correct and is not challenged. The v92 $i^2 = -1$ point is not challenged.

**Grade.** The two §IX.3 sentences as written are **grade D (Track E)** — false about their own cited literature, refuted by the primary sources. The refutation claim (IRH-C20a) is **VERIFIED at Track E B / Track F F2** (two independent routes: Gemini's reading and this audit's firsthand reading; premise ledger closed).

**CORRECTION 5 (grading label):** Gemini grades IRH-C20a "D/F4". **F4 is not a valid HLRE v5.1 Track F grade.** The skill states the grades are "A–D / F1–F3" and the Track F ladder is: "F1 machine-checked, or independently re-derived with a closed premise ledger; F2 one independent human or machine route; F3 single-route computation or artificial-only verification." There is no F4. The correct Track F grade for the refutation claim is **F2** (one independent human or machine route — here, two routes in fact, but F1 is reserved for machine-checked or independently re-derived formal claims, and a textual primary-source refutation is an F2-route claim). The Track E D for the manuscript sentences stands.

**Downstream consequence.** Manuscript §IX.2, Reading (A) — "the base is Euclidean spacetime, with Lorentzian signature arising dynamically. Most economical; the only reading consistent with citing four-dimensional optimality as evidence about spacetime. Cost: requires the signature mechanism of §IX.3." — Reading (A) therefore rests on the §IX.3 mechanism. With [17]/[18] removed as support, Reading (A)'s mechanism is the Greensite one-loop mechanism [41]/[42] alone, which is itself conditional on its own premises (measure assumptions, heat-kernel regularization, unbroken $E_6$ at $\Lambda$, no fundamental Higgs — see premise ledger). The misattribution does not by itself falsify Reading (A), but it removes one of its two cited supports and leaves it standing on the conditional Greensite mechanism only.

**Narrower scoped reading — ABSTAIN.** Gemini offers the narrower reading that no classical mechanism is known for a single-scalar Swift–Hohenberg $D_4$ substrate without a tuned clock field. The audit confirms that no such mechanism was found in the sources consulted ([17], [18], Greensite, C&G, Elizalde). That is absence of evidence in the consulted sources, not a proof of nonexistence; the claim as a universal negative is ABSTAIN (scoped). The misattribution finding stands regardless of this reading.

## IRH-C20b — Three generations may follow from Greensite + unbroken $E_6$

**Gemini's claim:** in unbroken $E_6$ ($n_B^{\mathrm{gauge}} = 156$), $N_{\mathrm{gen}} = 1$ (\$54$) and 2 (108) fail $$n_{F} > n_{B}$\$ (Case I); $N_{\mathrm{gen}} \geq 3$ (162) is required, margin +6 (+4 with graviton); so three generations may follow from (Greensite + unbroken $E_6$) rather than being an input as §V.2 says; adding a fundamental scalar Higgs ($27_H$/$78_H$) reverses the inequality; the $D_4$ sixth-order anisotropy / $\Lambda \ll q_0$ point is noted.

**CONDITIONAL (Track E C / Track F F3).** The arithmetic and the logic are VERIFIED; the consequence as a manuscript result is NOT established because its premises are not in the manuscript.

Manuscript §V.2, verbatim from the local PDF: "VERDICT — three generations is an INPUT, not an output. Three distinct objects were being conflated: a symmetry permuting cosets, a symmetry grading representations, and a multiplicity in the field content. The first two are real and structurally elegant. Neither is the third." And: "The framework does not predict three generations and has not done so since (8) was excluded." §IV.3 confirms the counting inputs: "$E_6$ passes the identical test (8) fails. It has the complex 27 [29], and the rank chain $E_6$$(6) \supset$ SO$(10)(5) \supset$ SU$(5)(4) \supset$ SM(4) is non-increasing — the standard $E_6$ [26] via SO(10) [27] and SU(5) [28] breaking route. One generation of Standard Model fermions embeds in a single 27." §IX.4 confirms the Higgs sector is underived: "The $E_6$ breaking pattern and Higgs sector, which have not been derived at all; and consequently the Higgs vacuum expectation value, $A_{3}$ resonance mass and widths, and CKM mixing."

Counting verified locally (Carlini & Greensite convention: massless vector $n_B = D-2 = 2$, graviton $n_B = D(D-3)/2 = 2$, Weyl fermion $n_F = 2$ per field — Greensite footnote 4): dim $E_6$ = 78 $\to$ $n_B^{\mathrm{gauge}} = 156$; $27_F$ $\to$ $n_{F} = 27$$\times$2 = 54 per generation; $N_{\mathrm{gen}} = 1$ $\to$ 54 (margin $-102$), 2 $\to$ 108 (margin $-48$), 3 $\to$ 162 (margin $+6$); with graviton $n_{B} = 158$, margin $+4$. Higgs reversal verified: $27_H$ = 54 real scalars $\to$ 156 + 54 = 210 > 162 (reversed); $78_H$ = 78 real scalars $\to$ 156 + 78 = 234 > 162 (reversed).

Premises the consequence needs, and their manuscript status:
1. **$E_6$ unbroken at the cutoff $\Lambda$ — NOT ESTABLISHED.** The manuscript identifies $E_6$ as the gauge algebra (§IV.3–IV.4) but states nothing about it being unbroken at any cutoff, and defines no cutoff $\Lambda$. A grep of the manuscript extraction for `q_0`, `q0`, `cutoff`, `unbroken` returns no cutoff scale (the only "unbroken" hit concerns a U(1) in the monopole discussion).
2. **No fundamental Higgs sector — NOT ESTABLISHED.** §IX.4 states the Higgs sector "has not been derived at all". The Higgs-reversal arithmetic is correct as a hypothetical, but it concerns a sector the manuscript says is underived.
3. **Heat-kernel regularization — PREMISE OF THE MECHANISM, not derived.** (See G-C20.6.)
4. **Scale hierarchy $\Lambda \ll q_0$ — NO MANUSCRIPT REFERENT.** No $q_{0}$ is defined in v93.1. The closest manuscript statement is §II.1: "the $D_4$ root system is a spherical 5-design [5], so any poly[nomial] ... $(k\cdot\hat{n})^4$ has degree 4. Genuine anisotropy first appears at sixth order, consistent with the fact that no 24-point configuration can form a spherical 6-design [5]." The sixth-order anisotropy is confirmed, but its coefficient $\xi_2 = -1/384$ was retracted in the manuscript ("anisotropy coefficient $\xi_2 = -1/384$ is not derivable from the stated lattice"; listed as retracted). A sixth-order anisotropy does not by itself establish a hierarchy between the Greensite cutoff and a $q_0$ scale.

**Grade.** The conditional statement — IF (Greensite mechanism + unbroken $E_6$ at $\Lambda$ + no fundamental Higgs + heat-kernel regularization) THEN $N_{\mathrm{gen}} \geq 3$ — is VERIFIED as arithmetic and logic. The unconditional manuscript consequence ("three generations follow") is NOT established. Overall IRH-C20b: **CONDITIONAL, Track E C / Track F F3**, with the four premises above as the open ledger. §V.2's verdict ("three generations is an INPUT") is therefore not overturned by this sweep; it is qualified by a conditional that the manuscript does not currently discharge.

---

## Independent re-derivation (computation gate)

Tool verdicts quoted with versions and exit codes. Python 3.11.16, SymPy 1.14.0, mpmath (conda env `jacobian-conjecture-2d`). Scripts `/tmp/gc20_sympy.py`, `/tmp/gc20_sympy2.py`, `/tmp/gc20_sympy3.py`; all three runs **exit code 0**.

### (a) Gaussian momentum integrals — VERIFIED

$\int dp_0/(2\pi) \exp[-s e^{-i\theta/2} p_0^2] = (4\pi s)^{-1/2} e^{i\theta/4}$ and $\int d^{D-1}p/(2\pi)^{D-1} \exp[-s e^{i\theta/2} \vec{p}^2] = (4\pi s)^{-(D-1)/2} e^{-i(D-1)\theta/4}$; product $= (4\pi s)^{-D/2} \exp[-i(D-2)\theta/4]$.

- Numeric (mpmath quad, 25 digits): worst relative error $2.04\times10^{-14}$ across $(D, \theta, s) = (4, 1.3, 2.7), (4, 2.5, 0.8), (6, 1.1, 3.0), (3, 0.7, 1.5)$; $5.18\times10^{-11}$ at $\theta = 2.9$. **PASS.**
- Near-$\pi$ (Fresnel regime): at $\theta = 3.0$ the quadrature gives relerr $1.06\times10^{-6}$ and at $\theta = 3.1$ it fails outright (relerr $2.17\times10^{-2}$) — this is a numerical-integration limitation ($\mathrm{Re}(a) = s\cdot\cos(\theta/2) \to 0$, slow decay + oscillation), not a formula discrepancy. The formula is confirmed there by the symbolic result and by exact phase algebra: SymPy gives $\int \exp(-a x^2) dx = \sqrt{\pi}/\sqrt{a}$ for $|\arg(a)| \leq \pi/2$, which covers the whole $\theta$ range (here |arg(a)| = |$\theta$|/2 $\leq$ $\pi$/2); and $\sqrt{\pi/a}$ vs $\sqrt{\pi/s}\cdot e^{i\theta/4}$ agrees to $0.00\times10^{0}$ at $\theta = 3.0$ and $6.68\times10^{-52}$ at $\theta = 1.3$ (50-digit mpmath). **PASS (symbolic + numeric away from the Fresnel boundary; boundary covered symbolically).**

### (b) Proper-time integral and $V(\theta)$ assembly — VERIFIED

$\int_{1/\Lambda^2}^\infty s^{-D/2-1} ds = 2\Lambda^{D+2}/(D\Lambda^2) = (2/D)\Lambda^D$ (SymPy, symbolic in D; $D = 4$ gives $\Lambda^4/2$, $D = 6$ gives $\Lambda^6/3$). Assembling: $V_S = -(1/2)(4\pi)^{-D/2} \exp[-i(D-2)\theta/4]\cdot(2/D)\Lambda^D$; SymPy: $V_S - (-\Lambda^D/[D(4\pi)^{D/2}] \exp[-i(D-2)\theta/4]) = 0$ (exact); $V = (n_F - n_B)(-V_S)$ matches Greensite eq. (10) exactly. **PASS.**

### (c) Five-cases analysis and dimension table — VERIFIED WITH CORRECTION (Correction 1)

Exact enumeration ($\mathrm{Re}[V]$ $\propto$ $\cos((D-2)\theta/4)$, $\mathrm{Im}[V]$ $\propto$ $-\sin((D-2)\theta/4)$, $\theta \in [-\pi, \pi]$, $n_F - n_B = 1$, $C_D = 1$): $D = 1$: no stationary points, $\min \mathrm{Re}\, V = +0.707107$ at $\theta = \pm\pi$; $D = 2$: $V$ $\theta$-independent; $D = 3$: no stationary points, $\min +0.707107$; $D = 4$: stationary at $\theta = \pm\pi$, $\mathrm{Re}\, V = 0$, $\min 0$; $D = 5$: stationary at $\theta = \pm 2\pi/3$, $\mathrm{Re}\, V = 0$, $\min -0.707107$ at $\theta = \pm\pi$; $D = 6$: stationary at $\theta = \pm\pi/2$, $\mathrm{Re}\, V = 0$, $\min -1$ at $\theta = \pm\pi$; $D = 7$: stationary at $\theta = \pm 2\pi/5$, $\mathrm{Re}\, V = 0$, $\min -1$ at $\theta = \pm 4\pi/5$ (Gemini's table gives $-\sqrt{2}/2$ there — wrong; $-\sqrt{2}/2$ is $\mathrm{Re}\, V$ at $\theta = \pm\pi$, confirmed: $\cos(5\pi/4) = -0.707107$). Only $D = 4$ (massless) has stationary-Im = min-Re. **PASS except the $D = 7$ minimum value (CORRECTED).**

### (d) Fluctuation estimate — CORRECTED (Correction 2)

$(l_P/R)^3 = 4.986\times10^{-183}$ for $l_P = 1.616255\times10^{-35}$ m, $R = 10^{10}$ ly; $l_P^3/[(4\pi/3)R^3] = 1.19\times10^{-183}$ with $V = (4\pi/3)R^3$. Paper quotes $10^{-184}$; ratio 49.86. Suppression still enormous; number ~50$\times$ too small as quoted.

### (e) $E_6$ generation counting — VERIFIED

$78\times2 = 156$; $27\times2 = 54$/generation; $N_{\mathrm{gen}} = 1$ $\to$ 54 (margin $-102$), 2 $\to$ 108 (margin $-48$), 3 $\to$ 162 (margin $+6$); with graviton ($n_B = 2$) $\to$ 158, margin $+4$; $27_H$ $\to$ 156 + 54 = 210 > 162 (reversed); $78_H$ $\to$ 156 + 78 = 234 > 162 (reversed); graviton dof $D(D-3)/2 = 2$ and vector dof $D-2 = 2$ at $D = 4$. **PASS.**

### (f) §\$4 $V_{T}$\$ algebra — VERIFIED WITH TRANSCRIPTION NOTE (Correction 3)

$V_T(\pi) = i(-\lambda + \lambda_c) \to \lambda_c = \lambda$ (SymPy, exact). $V_T(\theta)$ with $\lambda_c = \lambda$ rewrites exactly (SymPy `rewrite(cos)`) as **$2\lambda \cos(\theta/2)$**; min of $2\lambda \cos(\theta/2)$ on $[-\pi, \pi]$ ($\lambda > 0$) is 0 at $\theta = \pm\pi$. $\bar{\theta} = \pi$ and $\theta = \pi$ simultaneously requires $(D-2)/2 = 1 \to D = 4$ (SymPy `solve`, exact). The paper's eq. (48) as OCR'd reads "$V_T(\theta) = \lambda \cos(\theta/2)$" — factor-of-2 transcription note; minimum location and $D = 4$-only conclusion unaffected. **PASS with note.**

---

## Corrections log (all five, with disposition)

1. **$D = 7$ table value (G-C20.2).** Gemini: min $\mathrm{Re}\, V = -C_7(n_F - n_B)\sqrt{2}/2$ at $\theta = \pm 4\pi/5$. Correct: $-C_7(n_F - n_B)$. Verdict-neutral ($D = 7$ stays Case IV, no solution).
2. **Fluctuation number (G-C20.2/G-C20.3).** Paper/Gemini: $\langle\delta\theta\rangle \sim 10^{-184}$. Recomputed: $4.99\times10^{-183}$ ($1.19\times10^{-183}$ with spherical volume). ~50$\times$ discrepancy; suppression claim unaffected.
3. **$V_{T}$ prefactor (G-C20.4).** Algebra gives $V_T(\theta) = 2\lambda \cos(\theta/2)$; paper eq. (48) as OCR'd reads $V_T(\theta) = \lambda \cos(\theta/2)$. Transcription note; minimum and $D = 4$-only conclusion unaffected.
4. **$D = 4$ mass shift size (G-C20.5).** Gemini: shift $O(m^2/\Lambda^2) \approx 10^{-8}$. Paper eq. (64): shift $O(10^{-16})$. The $10^{-8}$ is eq. (58)'s approximation error, not the shift. Material precision correction; substance (approximate coincidence) stands.
5. **"F4" grade label (IRH-C20a).** F4 is not in the HLRE v5.1 Track F ladder (F1–F3 only). Corrected to F2 for the refutation claim; Track E D for the manuscript sentences stands.
6. **Omissions recorded (not errors):** the §5 additional-solutions regime ($\Delta(x \ln x)_{BF} \gg \Delta(x)_{BF} \to D = 2$ and $D = 4$ ($n_F = n_B$) solutions); the §4 cancellation becoming approximate with masses (residual imaginary part $O(m^4/\Lambda^4)$); the Elizalde topology qualification ($D = 5$ and $D = 4 + n$ with compact topology).

---

## Checks table

| # | Check | Result |
|---|---|---|
| Greensite 1993 (gr-qc/9210008) | | |
| 1 | Eq. (6) interpolating path integral | PASS |
| 2 | Eq. (7) $\eta_{ab} = \mathrm{diag}\{e^{i\theta}, 1, \dots, 1\}$ | PASS |
| 3 | Signature-continuation paragraph ($\theta = 0$ Euclidean, $\theta = \pi$ Lorentzian) | PASS |
| 4 | Measure assumption 1 (boson/fermion equal-and-opposite) | PASS |
| 5 | Measure assumption 2 (real DeWitt measure) | PASS |
| 6 | Eq. (8) $[-\sqrt{\eta}\, \eta^{ab} \partial_a \partial_b]$ | PASS |
| 7 | Eq. (9) $V_S(\theta) = -\Lambda^D/[D(4\pi)^{D/2}] \exp[-i(D-2)\theta/4]$ | PASS |
| 8 | Eq. (10) $V(\theta) = (n_F - n_B)\Lambda^D/[D(4\pi)^{D/2}] \exp[-i(D-2)\theta/4]$ | PASS |
| 9 | Eq. (11) $\cos[(D-2)\theta/4] = 0$, $\min[\mathrm{Re}\, V] = 0$ | PASS |
| 10 | Footnote 4 counting (vector $D-2$, graviton $D(D-3)/2$) | PASS |
| 11 | $D = 4$ uniqueness text | PASS |
| Carlini & Greensite 1994 (gr-qc/9308012) | | |
| 12 | Eqs. (1)–(2), §1 roadmap | PASS |
| 13 | Three consistency requirements (§1/§3) | PASS |
| 14 | Eqs. (15)–(16) scalar potential | PASS |
| 15 | Eq. (17) multi-species $V(\theta)$ | PASS |
| 16 | Eq. (18) Cases I–V | PASS |
| 17 | §2 regularization paragraph (heat-kernel "essentially unique") | PASS |
| 18 | §3 single-angle result, eq. (20) multi-angle ruled out | PASS |
| 19 | Eqs. (36)–(37) fluctuation suppression | CORRECTED (number: see Correction 2) |
| 20 | §4 eqs. (38)–$(40) V_{T}$ construction | PASS |
| 21 | §4 eqs. (41)–(47) $V_T = 0$ + stationarity $\to$ $\bar{\theta} = \pi$, $\theta = \pi$, $\|\lambda_c\| = \lambda$ | PASS |
| 22 | §4 eq. (48) $V_T(\theta) = \lambda \cos(\theta/2)$, min at $\theta = \pi$ | PASS (prefactor: see Correction 3) |
| 23 | §5 eqs. (49)–(59) mass effects, incomplete gammas | PASS |
| 24 | §5 eq. (57) $\mathrm{Re}[V(\bar{\theta})]$, eq. (58) $O(m^2/\Lambda^2)$ | PASS |
| 25 | §5 $D = 4$ case, eqs. (60)–(64), shift $O(10^{-16})$ | CORRECTED (Gemini's $10^{-8}$: see Correction 4) |
| 26 | §5 $D = 2$ case, eqs. (65)–(66) | PASS |
| 27 | §5 $\Delta(n)_{BF} = 0$ cases $D = 2$–$6$, $D > 6$, eqs. (67)–(80) | PASS |
| 28 | §5 $D = 6$ case, eqs. (73)–(77), inequalities $\Delta(x)_{BF} < 0$, $\Delta(x_3)_{BF} < 0$ | PASS |
| 29 | §5 additional-solutions regime ($\Delta(x \ln x)_{BF} \gg \Delta(x)_{BF}$) | PASS (omitted by Gemini; recorded) |
| 30 | §5 §4-cancellation-becomes-approximate note (residual Im $O(m^4/\Lambda^4)$) | PASS (omitted by Gemini; recorded) |
| 31 | §6 conclusions ($D = 4$ unique; $D = 6$ broken SUSY possible) | PASS |
| 32 | Appendix eqs. (81)–(87) | PASS (retrieved by audit; Gemini had not extracted) |
| Mukohyama & Uzan 2013 (arXiv:1301.1361) | | |
| 33 | Abstract ("restricted to classical fields") | PASS |
| 34 | §I Euclidean-substrate view | PASS |
| 35 | §II.A clock field $\phi$, $\partial_\mu \phi = M^2 n_\mu$, $t \equiv \phi/M^2$ | PASS |
| 36 | Limitations list (1) $\partial_\mu \phi = \mathrm{const.} \neq 0$ in $M_0$, local; (2) limited to classical field theory in flat space — verbatim | PASS |
| Kehayias et al. 2014 (arXiv:1403.0580) | | |
| 37 | Abstract (clock field triggers signature change) | PASS |
| 38 | §I "the construction is restricted to classical field theory" | PASS |
| 39 | §II.A–B clock field, scalar/vector/Dirac actions flowing to Minkowski in $M_0$ | PASS |
| Manuscript IRH v93.1 (local PDF) | | |
| 40 | §IX.3 text verbatim (p. 25) | PASS |
| 41 | §V.2 verdict verbatim ("three generations is an INPUT, not an output") | PASS |
| 42 | §IX.2 Reading (A) ("requires the signature mechanism of §IX.3") | PASS |
| 43 | §IV.3 $E_6$ / complex 27 / one generation per 27 | PASS |
| 44 | §IX.4 Higgs sector "not been derived at all" | PASS |
| 45 | §II.1 sixth-order anisotropy (spherical 5-design); $\xi_2 = -1/384$ retracted | PASS |
| 46 | Bibliography [17][18][41][42] identities | PASS |
| 47 | No $q_{0}$ / cutoff $\Lambda$ defined in manuscript (grep) | PASS |
| Elizalde et al. 1994 (hep-th/9312132) | | |
| 48 | Full text retrieved (950 lines) — Gemini's ABSTAIN resolved | PASS |
| 49 | Eq. (19) $D = 4$, trivial topology | PASS |
| 50 | Eq. (20) $D = 5$, $R^4\times T^1$, periodic, small R | PASS |
| 51 | Eq. (21) $D = 4 + n$, $R^{D-n}\times T^n$, periodic, small R | PASS |
| 52 | Antiperiodic small-R: no genuine solution (plateau) | PASS |
| Carlini & Greensite 1995 (gr-qc/9502023) | | |
| 53 | Exists; BSW square-root action, $\exp[\sqrt{i}\, S]$; out of scope as stated | PASS |
| Independent re-derivation (Python 3.11.16, SymPy 1.14.0; exit 0) | | |
| 54 | Gaussian integrals (numeric $\leq 2\times10^{-14}$ relerr; symbolic $\sqrt{\pi}/\sqrt{a}$) | PASS (near-$\pi$ quadrature limit noted) |
| 55 | Proper-time integral $(2/D)\Lambda^D$; $V(\theta)$ assembly = eq. (10) exactly | PASS |
| 56 | Dimension table enumeration | CORRECTED ($D = 7$ value: see Correction 1) |
| 57 | Fluctuation $(l_P/R)^3$ recomputation | CORRECTED (see Correction 2) |
| 58 | $E_6$ counting ($54/108/162$; margins $+6/+4$; Higgs reversal $210/234$) | PASS |
| 59 | $V_T$ $D = 4$-only (solve) and $V_T = 2\lambda \cos(\theta/2)$ (rewrite(cos)) | PASS (prefactor: see Correction 3) |
| Grading | | |
| 60 | Gemini's "F4" grade label for IRH-C20a | FAIL — not in HLRE ladder (F1–F3); corrected to F2 |
| 61 | Gemini's SymPy recomputation link recoverable? | NOT RUN — link renders empty; unrecoverable (local re-derivation substituted) |

Count: 55 PASS, 4 CORRECTED, 1 FAIL, 1 NOT RUN = 61. The four CORRECTED checks map to corrections-log items 1 (check 56), 2 (checks 19 and 57), and 4 (check 25). Correction $3 (V_{T}$ prefactor) is a transcription note on checks 22 and 59, both PASS — Gemini quoted the paper's eq. (48) correctly; the note concerns the paper's eq. (48) against the algebra from eqs. (39)–(46). Correction 5 (F4 label) is check 60 (FAIL). Check 61 (Gemini's SymPy link) is NOT RUN because the link is unrecoverable; the local re-derivation supersedes it. No Gemini substantive claim failed.

---

## Premise ledger (HLRE Track F requirement)

Every premise the verified claims rest on, and its status:

| Premise | Status |
|---|---|
| Measure assumption 1: a massless bosonic dof contributes the negative of a massless fermionic dof (Greensite/C&G) | Assumed (paper's assumption; not derived). |
| Measure assumption 2: real DeWitt measure $\|G\|^{1/2}$ ($\theta$-independent) | Assumed (paper's assumption; the $\theta$-dependence would change $V(\theta)$). |
| Heat-kernel regularization is the appropriate regulator | Argued by C&G §2 ("essentially unique"); not proven. The $D = 4$ result is conditional on it. |
| Wick angle $\theta$ is a single global dynamical variable (not multi-angle) | Derived in C&G §3 (multi-angle ruled out) under the three consistency requirements. |
| Massless (leading) analysis for Cases I–V | Exact in the massless limit; mass corrections in §5 make the $D = 4$ coincidence approximate (shift $O(10^{-16})$, residual Im $O(m^4/\Lambda^4)$). |
| $\Delta(x \ln x)_{BF} \sim \Delta(x)_{BF}$ regime (for $D = 4$/$D = 6$ uniqueness with masses) | Assumed regime; in the $\Delta(x \ln x)_{BF} \gg \Delta(x)_{BF}$ regime there are additional solutions ($D = 2$, $D = 4$ with $n_F = n_B$). |
| Trivial topology (for $D = 4$ uniqueness) | Assumed; Elizalde shows compact topology admits $D = 5$ and $D = 4 + n$. |
| Unbroken $E_6$ at the cutoff $\Lambda$ (for IRH-C20b) | NOT ESTABLISHED in the manuscript (no cutoff $\Lambda$ defined). |
| No fundamental Higgs sector (for IRH-C20b) | NOT ESTABLISHED (manuscript §IX.4: Higgs sector underived). |
| Scale hierarchy $\Lambda \ll q_0$ (for IRH-C20b) | NO MANUSCRIPT REFERENT (no $q_{0}$ defined; sixth-order anisotropy confirmed, coefficient retracted). |
| [17]/[18] as one-loop $V(\theta)$ mechanisms (manuscript §IX.3) | REFUTED — both are classical clock-field models. |
| Gemini's SymPy recomputation (cited link) | UNRECOVERABLE — link renders empty; not counted as a route. Local re-derivation substituted. |

## §7 disclosure

All verification in this audit is artificial (I1): Gemini 4 (Argon) Deep Research as the external route, and this local audit (machine re-derivation + firsthand source reading) as the independent route. No human source gate or balance gate was run; none is required under the 2026-11-12 repeal of the §6.5 human-gate requirement. No claim in this audit is stated beyond its grade. Nothing in this audit was filed, committed, or written into the manuscript. Cost: \$0. No GCP spend (local work only).

## Final verdict

**G-C20: RESOLVED at Grade B (Track E) / F2 (Track F).** Gemini's verdict is confirmed. The exact one-loop potential, the $D = 4$ uniqueness (Cases I–V), the §3 consistency argument, the §4 subtraction, the §5 mass analysis and $D = 6$ exception, and the regularization dependence are all verified against the primary sources firsthand and, for the algebra, re-derived locally with SymPy (exit 0). The five corrections are verdict-neutral except the grading-label correction (F4 $\to$ F2) and the Elizalde scope qualification ($D = 4$ uniqueness is topology-dependent). The grade B is the ceiling for a mechanism/literature claim under the HLRE "Standard" cap (max B); F2 reflects the single independent route (the local re-derivation — Gemini's own SymPy link being unrecoverable).

**Inventory changes for the gap record:**
- G-C20: ABSTAIN/NOT RUN (toy G5/F3) $\to$ **RESOLVED, Grade B (Track E) / F2 (Track F)**.
- G-C20.7: partial ABSTAIN $\to$ **RESOLVED** (Appendix eqs. 81–87 and Elizalde 1994 retrieved by the audit; C&G 1995 confirmed out of scope).
- **IRH-C20a (new): the §IX.3 misattribution is VERIFIED; the two §IX.3 sentences as written are grade D (Track E).** Reading (A) (§IX.2) now rests on the Greensite mechanism alone, conditional on its premises.
- **IRH-C20b (new): CONDITIONAL, Track E C / Track F F3.** The conditional (Greensite + unbroken $E_6$ at $\Lambda$ + no fundamental Higgs + heat-kernel $\to$ $N_{\mathrm{gen}} \geq 3$) is verified as arithmetic/logic; the premises are not established in v93.1, so §V.2's "three generations is an INPUT" verdict is not overturned.
- **Scope qualification (new):** $D = 4$ uniqueness holds for trivial topology; with a compact dimension (periodic BC, small radius) Elizalde shows $D = 5$ and $D = 4 + n$ also select Lorentzian. The manuscript's "four-dimensional optimality as evidence about spacetime" depends on the trivial-topology assumption.
- Open items carried forward: the $V_{T}$ prefactor transcription note (2$\lambda$ vs $\lambda$ in eq. (48)); the additional-solutions regime ($\Delta(x \ln x)_{BF} \gg \Delta(x)_{BF}$); the §4 cancellation becoming approximate with masses; the narrower scoped reading (no classical mechanism for a single-scalar Swift–Hohenberg $D_4$ substrate without a tuned clock field) stays ABSTAIN.

## Correction note — 2026-11-12 evening CST (appended; original rows above untouched)

**$D = 6$ second inequality — CORRECTED.** The audit file's G-C20.5 text and
check row 28 state the two $D = 6$ inequalities as $\Delta(x)_{BF} < 0$ and
$\Delta(x_3)_{BF} < 0$. That is a mistranscription. The arXiv text
(Carlini & Greensite 1994, arXiv:gr-qc/9308012, §5, near eq. (82), read
firsthand) states: "Assuming two inequalities, namely $\Delta(x)_{BF} < 0$
and $\Delta(x^3)_{BF} > 0$, we find that min Re[$V$] is at $|\theta| = \pi$..."
The second inequality is $\Delta(x^3)_{BF} > 0$ — the cube $x^3$, not a
subscript $x_3$, and the sign is $>$, not $<$. Check row 28's PASS is therefore
corrected to **PASS WITH CORRECTION** on this point only. **Verdict-neutral:**
the $D = 6$ Lorentzian solution stays conditional on the mass spectrum either
way; no G-C20 grade changes. This resolves the sign flag carried from the
audit's delivery message.
