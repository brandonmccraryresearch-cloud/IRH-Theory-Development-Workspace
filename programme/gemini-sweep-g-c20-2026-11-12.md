# Gemini 4 (Argon) Sweep 4 — G-C20: the full Greensite one-loop mechanism

**Date:** 2026-11-12 16:15–16:59 CST (harness-measured; report completed
16:48 CST)
**Agent:** Gemini Deep Research on gemini.google.com, account
autopoieticdragon@gmail.com (Pro), chat model picker "Argon" (Gemini 4
Argon, "Code & analysis") at submission; while the research ran the
composer showed "Hydrogen"; after completion "Argon" again. The Deep
Research agent's underlying research model is NOT labeled Argon in the
UI. IRH_v93_1.pdf attached (accepted). Conversation SAVED (not
Temporary) at https://gemini.google.com/u/1/app/3ab99307796e234c.
Cost \$0. 31 websites researched.
**Prompt:** as specified in `GEMINI-SWEEPS-SPECS-2026-11-12.md` Sweep 4
(pasted exactly) + the full HLRE amendment block from the skill + the
manuscript PDF. Run as Deep Research (agent with compute) per Brandon's
16:18 CST instruction; the first plain-chat attempt was stopped before
producing any response and discarded.
**Status:** Gemini's report, UNVERIFIED — local claim-by-claim audit to
follow (`AUDIT_gemini-sweep-g-c20_2026-11-12.md`). Do not cite the verdict
as established until the audit lands.
**RECORD NOTE:** the report references an independent SymPy symbolic
recomputation, but the hyperlink in the rendered report has no visible
destination or label — the link destination could not be recovered, so it
is not reproduced here; the audit must redo the recomputation locally.
During the wait Brandon sent "Give me the Sweep 4 Audit Report here in a
chat response"; the report text below is that chat response.

---

## FULL REPORT TEXT (verbatim from the Gemini Deep Research report)

### Sweep 4 Audit Report: Gap G-C20 and Recovery of the Exact Greensite One-Loop Dynamical Signature Mechanism

Gap G-C20 (formerly graded ABSTAIN under WS-D Task 12, G6) is RESOLVED
via primary-source recovery from Jeff Greensite's foundational paper,
"Dynamical Origin of the Lorentzian Signature of Spacetime", Physics
Letters B 300, 34–37 (1993) (https://arxiv.org/abs/gr-qc/9210008, PDF:
https://arxiv.org/pdf/gr-qc/9210008), and Alberto Carlini and Jeff
Greensite's extended treatise, "Why is Spacetime Lorentzian?", Physical
Review D 49, 866–878 (1994) (https://arxiv.org/abs/gr-qc/9308012, PDF:
https://arxiv.org/pdf/gr-qc/9308012). Both the exact one-loop functional
determinant and the $D = 4$ uniqueness argument have been recovered verbatim
and verified by symbolic recomputation, upgrading Gap G-C20 from ABSTAIN
/ NOT RUN (and G5 / F3 on the prior toy sign-flip) to Grade B (Track E) /
F2 (Track F) under HLRE v5.1 as amended 2026-11-12.

The prior audit state captured only a toy potential $\mathrm{Re}\, V_{\mathrm{toy}}(\theta) = \Delta \cos\theta$,
which missed how spacetime dimensionality D enters the effective
potential. In the primary-source derivation, parameterizing the local
tangent-space metric as $\eta_{ab} = \mathrm{diag}\{e^{i\theta}, 1, \dots, 1\}$ in D dimensions
introduces both $\sqrt{\eta} = e^{i\theta/2}$ and the inverse metric $\eta^{ab} = \mathrm{diag}\{e^{-i\theta}, 1, \dots, 1\}$ into the kinetic operator. Consequently, the exact
one-loop scalar determinant is $\det{}^{-1/2}[-\sqrt{\eta}\, \eta^{ab} \partial_a \partial_b]$, whose
momentum-space eigenvalue is $e^{-i\theta/2} p_0^2 + e^{i\theta/2} \vec{p}^2$. Evaluating
the D-dimensional Gaussian momentum integral under proper-time
(heat-kernel) regularization with a Planck-scale cutoff $\Lambda$ yields a
$1/(4\pi s)^{1/2} \cdot e^{i\theta/4}$ factor from $p_0$ and a $1/(4\pi s)^{(D-1)/2} \cdot e^{-i(D-1)\theta/4}$ factor from $\vec{p} \in \mathbb{R}^{D-1}$, producing the exact
multi-species one-loop effective potential:

$$V(\theta) = (n_F - n_B) \frac{\Lambda^D}{D(4\pi)^{D/2}} \exp[-i(D-2)\theta/4]$$

Because $V(\theta)$ is complex, dynamical selection of a signature $\theta \in [-\pi, \pi]$
requires simultaneously minimizing $\mathrm{Re}[V(\theta)]$ and rendering $\mathrm{Im}[V(\theta)]$
stationary. Stationarity of $\mathrm{Im}[V(\theta)]$ requires $\cos[(D-2)\theta/4] = 0$, which
forces $\mathrm{Re}[V(\theta)] = 0$ at the stationary point; for $\mathrm{Re}[V(\theta)] = 0$ to
simultaneously be the global minimum on $\theta \in [-\pi, \pi]$, one must have $n_F > n_B$ and $((D-2)/4)\pi = \pi/2$, which uniquely selects $D = 4$ and $\theta = \pm\pi$
(Lorentzian signature) for massless non-supersymmetric field theories
under heat-kernel regularization.

Auditing the Intrinsic Resonance Holography (IRH v93.1) manuscript
(uploaded: IRH_v93_1.pdf) against these primary sources yields three
principal findings. First, IRH v93.1 rightly retracts v92's invalid $i^2 = -1$ signature argument (§VII) and accurately identifies the Greensite and
Carlini–Greensite mechanism as requiring a quantum one-loop effective
potential with $n_F > n_B$ (§IX.3). Second, IRH v93.1 §IX.3 misattributes
references [17] (Mukohyama & Uzan 2013, https://arxiv.org/abs/1301.1361)
and [18] (Kehayias, Mukohyama & Uzan 2014,
https://arxiv.org/pdf/1403.0580) as requiring a one-loop $n_F > n_B$
effective potential while asserting that "No purely classical Euclidean
substrate is known to yield Lorentzian signature"; in reality, [17] and
[18] construct a classical Euclidean clock-field mechanism where an
effective Lorentzian metric emerges from a non-vanishing scalar gradient
without a one-loop $n_F > n_B$ potential. Third, applying Greensite's $n_F > n_B$ criterion to IRH v93.1's unbroken $E_6$ gauge group (§IV.3–IV.4, $\dim E_6 = 78$, $n_B^{\mathrm{gauge}} = 156$) exposes a sharp structural constraint: one
fermion generation (27 of $E_6$, $n_F = 54$) or two generations ($n_F = 108$)
violate $n_F > n_B$, making $N_{\mathrm{gen}} \geq 3$ ($n_F = 162$ for $N_{\mathrm{gen}} = 3$) necessary
for Lorentzian signature selection in an unbroken $E_6$ gauge theory,
provided no large fundamental scalar Higgs sector ($27_H, 78_H, 351_H$)
propagates at the cutoff scale $\Lambda$.

### 1. Audit Scope, Prior State, and What IRH v93.1 Claims
1.1 Prior Audit State of Gap G-C20

In the prior verification cycle (WS-D Task 12, G6), the full Greensite
one-loop mechanism was marked ABSTAIN (no grade), while a simplified toy
model was graded G5 / F3 on the qualitative sign-flip $\mathrm{Re}\, V_{\mathrm{toy}}(\theta) = \Delta \cdot \cos\theta$, which stated that Lorentzian signature ($\theta = \pi$) is favored over
Euclidean signature ($\theta = 0$) if and only if $n_F > n_B$. That toy reduction
left three core elements unrecovered (NOT RUN):

- The exact one-loop functional determinant in D dimensions and the
  explicit measure assumptions fixing its complex phase.
- The exact proper-time (heat-kernel) evaluation of the complex effective
  potential $V(\theta)$, in which the angular dependence in $D = 4$ is
  $\exp(-i\theta/2)$ (giving $\mathrm{Re}\, V(\theta) \propto \cos(\theta/2)$, rather than cos $\theta$).
- The $D = 4$ uniqueness argument explaining why Lorentzian signature
  ($\theta = \pm\pi$) is selected uniquely in four dimensions.

1.2 Claims in the Audited Manuscript (IRH v93.1)

In Intrinsic Resonance Holography: Dynamical Selection of a $D_4$ Substrate
from Interference Dynamics (Version 93.1, September 17, 2026, uploaded:
IRH_v93_1.pdf), spacetime signature is addressed across Parts VII, VIII,
and IX. In Part VII (Retractions from v92, p. 22), the manuscript retracts
the v92 claim "Lorentzian signature from $i^2 = -1$" for the stated reason:
"canonical $i\hbar$ is present in Euclidean field theory also; does not select
signature". In Part VIII (Complete Claim Ledger, Figure 10, p. 23), it
lists "Lorentzian signature (needs quantum sector)" and "Dimensional
assignment (A/B/C unresolved)" under OPEN. In Part IX (§IX.2 Modeling
Decisions, p. 25), Reading (A) of the dimensional assignment states: "(A)
the base is Euclidean spacetime, with Lorentzian signature arising
dynamically. Most economical; the only reading consistent with citing
four-dimensional optimality as evidence about spacetime. Cost: requires
the signature mechanism of §IX.3."

Finally, Part IX (§IX.3 Requires External Structure, p. 25) makes the
following load-bearing statement regarding the external
dynamical-signature literature:

"Lorentzian signature. Published dynamical-signature mechanisms [17] [18]
require a one-loop effective potential with more fermionic than bosonic
degrees of freedom — the condition first identified by Greensite [41] and
refined by Carlini and Greensite [42]. No purely classical Euclidean
substrate is known to yield Lorentzian signature. The v92 argument from
$i^2 = -1$ is invalid: canonical quantization employs complex amplitudes in
Euclidean field theory as well, and an ordinary Hilbert-space inner
product is positive-definite, so obtaining $g_{00} = -1$ requires a separate
construction."

[The report's §1.2 also contains an expandable "Learn More" detail quoting
the manuscript's Part VII discussion: "Note carefully: the phase ($i^2 = -1$) in the Lorentzian metric cannot be generated by the Euclidean
substrate dynamics: $g_{00} = -1$, which is purely formal in Euclidean
quantum gravity. In the IRH, $g_{00} = -1$ is 'chosen' by hand — it is not
generated by the substrate. In the IRH, the Lorentzian metric is a
consequence of the generalized Wick rotation (Wick angle $\theta = \pi$) in the
quantum one-loop effective action — see $\mathrm{Re}\, V_{\mathrm{toy}}(\theta) = \Delta \cdot \cos\theta$."]

### 2. Primary-Source Recovery: The Exact Greensite One-Loop Determinant and Effective Potential $V(\theta)$
2.1 Generalized Tetrad Metric and Interpolating Path Integral

In both Greensite (1993) (https://arxiv.org/pdf/gr-qc/9210008) and
Carlini & Greensite (1994) (https://arxiv.org/pdf/gr-qc/9308012), the
spacetime metric g_μν in D dimensions is written in terms of a real
vielbein (tetrad) e_μ^a and a generalized diagonal tangent-space metric
$\eta_{ab}$ in which the Wick rotation angle $\theta$ is promoted from a formal
contour-rotation parameter to a dynamical degree of freedom.

Verbatim from Greensite (1993), arXiv:gr-qc/9210008, pp. 1–2:

"Comparing the Feynman and Euclidean path integrals, it is easy to write
down a slightly more general path integral which interpolates between
them, namely (in D dimensions):

$$(6)\quad Z = \int d\mu(e, \phi, \psi, \bar{\psi}) \exp\left(-\int d^D x\, \sqrt{g}\, L\right)$$

where:

$$(7)\quad \eta_{ab} = \mathrm{diag}\{e^{i\theta}, 1, \dots, 1\}$$

and we obtain the Euclidean theory for $\theta = 0$, and the Feynman theory for
$\theta = \pi$, with the correct $i\epsilon$ prescription for propagators supplied
automatically as $\theta \to \pi$. The theory at $\theta \to -\pi$ converts to the Feynman
theory under a time inversion."

Greensite explains why this represents a continuation in the tangent-space
signature $\eta_{ab}$ rather than a coordinate transformation $t \to e^{i\theta}t$
(arXiv:gr-qc/9210008, p. 2):

"It should be stressed that for quantum gravity, the continuation from the
Minkowski to the Euclidean theory is really a continuation in signature
$\eta_{ab}$, rather than just a rotation $t \to e^{i\theta}t$ of the time coordinate.
Without continuation in the signature, the local frame invariance of
general relativity would be $O(3,1)$ in both Minkowski and Euclidean space,
instead of changing from $O(3,1)$ to $O(4)$ in Euclidean space. Moreover,
expectation values of certain diffeomorphism invariant quantities (such as
$\langle R\sqrt{g}\, R_p\rangle$) have no dependence whatever on time intervals, and the
difference between expectation values in the Euclidean and Minkowski
theories resides entirely in their dependence on the determinant of the
signature $\det(\eta)$."

2.2 Measure Assumptions Fixing the $\theta$-Dependence

In a path integral where $\det(\eta) = e^{i\theta}$ is dynamical, the $\theta$-dependence
of the functional integration measure dμ(e, $\phi$, $\psi$, $\psi$̄) directly determines
the complex phase of the one-loop determinant. If the measure cancelled
the $\sqrt{\eta} = e^{i\theta/2}$ factor in the action density, the $\theta$-dependence of the
one-loop effective potential would change. Greensite (1993)
(arXiv:gr-qc/9210008, p. 2) and Carlini & Greensite (1994)
(arXiv:gr-qc/9308012, Section 2, p. 5) fix the measure via two explicit
assumptions.

Verbatim from Greensite (1993), arXiv:gr-qc/9210008, p. 2 (repeated
verbatim in Carlini & Greensite 1994, arXiv:gr-qc/9308012, Section 2):

"The following simple assumptions fix the $\theta$-dependence of the measure:

For free fields of mass m, the contributions to Z in eq. (6) from each
(propagating) bosonic degree of freedom are equal, and inverse to the
contributions from each fermionic degree of freedom. Thus, e.g., Z = 1 at
any $\theta$ for a supersymmetric combination of free fields.

The integration measure for scalar fields is given by the real-valued,
invariant volume measure (DeWitt measure) in superspace $d\mu(\phi) = D\phi\, |G|$,
where G is the determinant of the scalar field supermetric $G(x,y) = \sqrt{g}\, \delta(x-y)$."

Because the DeWitt measure uses the real modulus $|G|$ (where $|g| = |\det(e)^2 e^{i\theta}| = \det(e)^2$ is independent of $\theta$), the scalar integration
measure dμ($\phi$) is independent of the phase angle $\theta$, while the classical
action in the exponent retains the complex density $\sqrt{g} = \det(e)\, \sqrt{\eta} = \det(e)\, e^{i\theta/2}$.

2.3 Recovery of the Exact One-Loop Determinant and Heat-Kernel Evaluation

In a flat background ($e_\mu^a = \delta_\mu^a$, $g_{\mu\nu} = \eta_{\mu\nu}$), the action for a
massless real scalar field $\phi$ is:

$$S_S[\phi; \theta] = \int d^D x\, \sqrt{\eta}\, \tfrac{1}{2}\, \eta^{ab} \partial_a \phi\, \partial_b \phi = \tfrac{1}{2} \int d^D x\, \phi\, (-\sqrt{\eta}\, \eta^{ab} \partial_a \partial_b)\, \phi$$

Integrating out $\phi$ with the $\theta$-independent DeWitt measure yields the exact
one-loop determinant.

Verbatim from Carlini & Greensite (1994), arXiv:gr-qc/9308012, Section 2,
p. 5 (matching eqs. (8)–(9) of Greensite 1993, arXiv:gr-qc/9210008, p. 3):

"Under these assumptions, the one-loop contribution to $V_{\mathrm{eff}}(\theta)$ due to a
massless scalar field propagating in flat ($g_{\mu\nu} = \eta_{\mu\nu}$) space is

$$\exp\left[-\int d^D x\, V_S(\theta)\right] = \det{}^{-1/2}[-\sqrt{\eta}\, \eta^{ab} \partial_a \partial_b] \quad (15)$$

and heat-kernel regulation of the determinant gives

$$V_S(\theta) = -\tfrac{1}{2} \int_{1/\Lambda^2}^{\infty} \frac{ds}{s} \int \frac{d^D p}{(2\pi)^D} \exp[-s(e^{-i\theta/2} p_0^2 + e^{i\theta/2} \vec{p}^2)] = -\frac{\Lambda^D}{D(4\pi)^{D/2}} \exp[-i(D-2)\theta/4] \quad (16)$$

where $\Lambda$ is a high-momentum cutoff which, given the non-renormalizability
of gravity, is taken to exist at the Planck scale."

Step-by-Step Derivation of Equation (16) / Equation (9)

To make the origin of the $\exp[-i(D-2)\theta/4]$ phase explicit, the five
algebraic steps verified symbolically in [link — destination not
recoverable from the page] proceed as follows:

1. Metric determinant and inverse: From $\eta_{ab} = \mathrm{diag}\{e^{i\theta}, 1, \dots, 1\}$ in D
dimensions, $\det(\eta) = e^{i\theta}$, so $\sqrt{\eta} = e^{i\theta/2}$, while the inverse metric
is $\eta^{ab} = \mathrm{diag}\{e^{-i\theta}, 1, \dots, 1\}$.

2. Momentum-space operator eigenvalue: Acting on a plane wave $e^{ip_a x^a}$ $(\partial_a \to ip_a)$, the operator $-\sqrt{\eta}\, \eta^{ab} \partial_a \partial_b$ has eigenvalue:

$$\lambda(p_0, \vec{p}; \theta) = e^{i\theta/2}(e^{-i\theta} p_0^2 + \vec{p}^2) = e^{-i\theta/2} p_0^2 + e^{i\theta/2} \vec{p}^2$$

Because $\mathrm{Re}[\lambda(p_0, \vec{p}; \theta)] = \cos(\theta/2)(p_0^2 + \vec{p}^2)$, the Gaussian momentum
integral converges if and only if $\cos(\theta/2) \geq 0$, which restricts $\theta$ to the
fundamental interval $\theta \in [-\pi, \pi]$ (gr-qc/9210008, p. 3).

3. Gaussian integration over $p_0$ and $\vec{p}$: Separating the D-dimensional
momentum integral into $p_0$ $\in$ $\mathbb{R}$ and $\vec{p} \in \mathbb{R}^{D-1}$ at fixed proper time s >
0:

$$\int_{-\infty}^{\infty} \frac{dp_0}{2\pi} \exp(-s e^{-i\theta/2} p_0^2) = \frac{1}{(4\pi s)^{1/2}} (e^{-i\theta/2})^{-1/2} = \frac{1}{(4\pi s)^{1/2}} e^{+i\theta/4}$$

$$\int_{\mathbb{R}^{D-1}} \frac{d^{D-1}p}{(2\pi)^{D-1}} \exp(-s e^{i\theta/2} \vec{p}^2) = \frac{1}{(4\pi s)^{(D-1)/2}} (e^{i\theta/2})^{-(D-1)/2} = \frac{1}{(4\pi s)^{(D-1)/2}} e^{-i(D-1)\theta/4}$$

Multiplying the temporal and spatial factors yields the exact
D-dependent phase:

$$\int \frac{d^D p}{(2\pi)^D} \exp[-s(e^{-i\theta/2} p_0^2 + e^{i\theta/2} \vec{p}^2)] = \frac{1}{(4\pi s)^{D/2}} \exp[i\theta/4 - i(D-1)\theta/4] = \frac{1}{(4\pi s)^{D/2}} \exp[-i(D-2)\theta/4]$$

4. Proper-time integration: Integrating over s $\in$ [1/$\Lambda$^2, ∞) gives:

$$\int_{1/\Lambda^2}^{\infty} \frac{ds}{s}\, s^{-D/2} = \left[-\frac{2}{D}\, s^{-D/2}\right]_{1/\Lambda^2}^{\infty} = \frac{2}{D}\, \Lambda^D$$

Multiplying by the prefactor $-\tfrac{1}{2}$ from $\det^{-1/2}$ immediately yields eq.
(16) (gr-qc/9308012) / eq. (9) (gr-qc/9210008):

$$V_S(\theta) = -\frac{\Lambda^D}{D(4\pi)^{D/2}} \exp[-i(D-2)\theta/4]$$

5. Summation over n_B bosonic and n_F fermionic degrees of freedom:
Applying Measure Assumption 1 (each propagating massless bosonic degree
of freedom contributes +$V_S(\theta)$, and each massless fermionic degree of
freedom contributes $-V_S(\theta)$), Carlini & Greensite obtain eq. (17)
(gr-qc/9308012, p. 6; eq. (10) of gr-qc/9210008, p. 3):

"For n_B massless, propagating, bosonic degrees of freedom, and n_F
massless fermionic degrees of freedom, the one-loop contribution to
$V_{\mathrm{eff}}(\theta)$ becomes

$$V(\theta) = (n_F - n_B) \frac{\Lambda^D}{D(4\pi)^{D/2}} \exp[-i(D-2)\theta/4] \quad (17)$$"

### 3. Primary-Source Recovery: The $D = 4$ Uniqueness Argument and Refinements
3.1 The Simultaneous Minimum/Stationarity Criterion and the Five Cases

Because the effective potential $V(\theta)$ in eq. (17) is complex-valued, the
one-loop weight in the partition function for a constant mode $\theta$ over
spacetime volume $\Omega$ is $\exp[-\Omega V(\theta)] = \exp(-\Omega\, \mathrm{Re}[V(\theta)])\, \exp(-i\Omega\, \mathrm{Im}[V(\theta)])$.
For the integral over $\theta \in [-\pi, \pi]$ to be dominated by a well-defined
saddle/peak, the real part $\mathrm{Re}[V(\theta)]$ must be minimized while the rapidly
oscillating phase $\mathrm{Im}[V(\theta)]$ must be stationary ($\frac{d}{d\theta} \mathrm{Im}[V(\theta)] = 0$).

Verbatim from Carlini & Greensite (1994), arXiv:gr-qc/9308012, Section 2,
p. 6 (matching eq. (11) and surrounding text of Greensite 1993,
arXiv:gr-qc/9210008, pp. 3–4):

"This potential is complex. We therefore look for a value of $\theta$ in the
range [$-\pi$, $\pi$] for which, simultaneously, (i) Re(V) is a minimum; and (ii)
Im(V) is stationary. These conditions together give us

$$\left. \begin{aligned} \cos[(D-2)\theta/4] &= 0 \\ \min[\mathrm{Re}[V(\theta)]] &= 0 \end{aligned} \right\} \quad \theta \in [-\pi, \pi] \quad (18)$$

In searching for a solution of (18), there are five cases to consider:

I. $n_F < n_B$. Then $\min \mathrm{Re}[V] < 0$ $\to$ no solution.

II. $n_F = n_B$ or $D = 2$. Then $V(\theta)$ is independent of $\theta$, and no $\theta$ is
preferred.

III. $n_F > n_B$ and $((D-2)/4)\pi < \pi/2$. Then $\min \mathrm{Re}[V] > 0$ $\to$ no solution.

IV. $n_F > n_B$ and $((D-2)/4)\pi > \pi/2$. Then $\min \mathrm{Re}[V] < 0$ $\to$ no solution.

V. $n_F > n_B$ and $((D-2)/4)\pi = \pi/2$. In this case, both conditions are
satisfied at $\theta = \pm\pi$, which corresponds to Lorentzian signature. The
equality $((D-2)/4)\pi = \pi/2$ can, of course, only be achieved for a
spacetime dimensionality $D = 4$.

Since case (V), above, is the unique solution of the conditions (18), we
have found an interesting connection between spacetime signature and
spacetime dimension: Lorentzian signature seems to be singled out by the
dynamics only in $D = 4$ dimensions."

Mathematical Anatomy of the $D = 4$ Uniqueness Argument

Write $$V(\theta) = C_D (n_F - n_B) e^{-iu(\theta)}$$, where $C_D \equiv \Lambda^D/[D(4\pi)^{D/2}] > 0$ and $u(\theta) \equiv (D-2)\theta/4$. Then:

$$\mathrm{Re}[V(\theta)] = C_D (n_F - n_B) \cos u(\theta), \quad \mathrm{Im}[V(\theta)] = -C_D (n_F - n_B) \sin u(\theta)$$

Assuming $D \neq 2$ and $n_F \neq n_B$, the stationarity condition for the
imaginary part is:

$$\frac{d}{d\theta} \mathrm{Im}[V(\theta)] = -\frac{D-2}{4} C_D (n_F - n_B) \cos u(\theta) = 0 \iff \cos[(D-2)\theta/4] = 0$$

Because $\mathrm{Re}[V(\theta)]$ is proportional to the exact same factor $\cos[(D-2)\theta/4]$,
any stationary point $\theta^*$ of $\mathrm{Im}[V(\theta)]$ automatically satisfies Re[V($\theta^*$)] =
0. Consequently, for $\theta^*$ to simultaneously be the global minimum of
$\mathrm{Re}[V(\theta)]$ on $\theta \in [-\pi, \pi]$, the global minimum of $\mathrm{Re}[V(\theta)]$ on [$-\pi$, $\pi$] must
equal zero ($\min[\mathrm{Re}[V(\theta)]] = 0$).

If $n_F < n_B$ (Case I), $\mathrm{Re}[V(0)] = C_D (n_F - n_B) < 0$, so the minimum of
$\mathrm{Re}[V(\theta)]$ on [$-\pi$, $\pi$] is strictly negative and cannot equal zero. If $n_F > n_B$, $\mathrm{Re}[V(\theta)]$ has the sign of $\cos u(\theta)$ for $u \in [-u_{\max}, u_{\max}]$, where
$u_{\max} = |D-2|\pi/4$. On the symmetric interval $[-u_{\max}, u_{\max}]$, $\min \cos u = 0$ holds if and only if $u_{\max} = \pi/2$. Specifically, for $D = 3$ (Case III, and
similarly for $D = 1$ where $\cos(-u) = \cos u$), the maximum argument is $\pi/4$
< $\pi/2$, so min $\cos u$ = $\cos(\pi/4) = \sqrt{2}/2 > 0$ and $\mathrm{Im}[V]$ has no stationary
point on [$-\pi$, $\pi$]. For $D \geq 5$ (Case IV), $(D-2)\pi/4 \geq 3\pi/4 > \pi/2$, so $\cos u$
becomes strictly negative on ($\pi/2$, $u_{\max}$] ($\min \mathrm{Re}[V] < 0$), meaning the
minimum of $\mathrm{Re}[V]$ occurs where $\mathrm{Im}[V]$ is not stationary. Only for $D = 4$
(Case V) does $(4-2)\pi/4 = \pi/2$, placing both the global minimum $\mathrm{Re}[V(\pm\pi)] = 0$ and the stationary point $\left.\frac{d}{d\theta} \mathrm{Im}[V]\right|_{\theta=\pm\pi} = 0$ at the boundary points
$\theta = \pm\pi$, which correspond to Lorentzian signature $\eta_{ab} = \mathrm{diag}\{-1, 1, 1, 1\}$.

Dimension table ($D$ | Phase endpoint $u(\pi) = (D-2)\pi/4$ | $\cos(u(\pm\pi))$ at $\theta = \pm\pi$ | Stationary point of $\mathrm{Im}[V(\theta)]$ on $\theta \in [-\pi, \pi]$ | Global minimum of $\mathrm{Re}[V(\theta)]$ ($n_F > n_B$) | Simultaneous solution to eq. (18)?):
- $D = 1$ | $-\pi/4$ | $+\sqrt{2}/2$ | None | $+C_1 (n_F - n_B) \sqrt{2}/2 > 0$ | No (Case
  III)
- $D = 2$ | 0 | +1 | All $\theta \in [-\pi, \pi]$ (degenerate) | $+C_2 (n_F - n_B)$ (constant) | No preference (Case II)
- $D = 3$ | $+\pi/4$ | $+\sqrt{2}/2$ | None | $+C_3 (n_F - n_B) \sqrt{2}/2 > 0$ | No (Case
  III)
- $D = 4$ | +$\pi/2$ | 0 | $\theta = \pm\pi$ (Lorentzian) | $0$ at $\theta = \pm\pi$ | Yes — Unique
  Solution (Case V)
- $D = 5$ | $+3\pi/4$ | $-\sqrt{2}/2$ | $\theta = \pm 2\pi/3$ ($\mathrm{Re}[V] = 0$) | $-C_5 (n_F - n_B) \sqrt{2}/2 < 0$ at $\theta = \pm\pi$ | No (Case IV)
- $D = 6$ | $+\pi$ | $-1$ | $\theta = \pm\pi/2$ ($\mathrm{Re}[V] = 0$) | $-C_6 (n_F - n_B) < 0$ at $\theta = \pm\pi$ | No for massless; possible for broken SUSY ($n_F = n_B$)
- $D = 7$ | $+5\pi/4$ | $-\sqrt{2}/2$ | $\theta = \pm 2\pi/5$ ($\mathrm{Re}[V] = 0$) | $-C_7 (n_F - n_B) \sqrt{2}/2 < 0$ at $\theta = \pm 4\pi/5$ | No (Case IV)

3.2 Extensions and Scope Caveats in Carlini & Greensite (1994)

Beyond reviewing the flat-space massless result of Greensite (1993),
Carlini & Greensite (1994) (arXiv:gr-qc/9308012) establish four
refinements that bound the scope of the mechanism.

First, in Section 3 (Consistency Constraints and Suppression of Signature
Fluctuations), Carlini & Greensite impose three consistency requirements
in curved spacetime (arXiv:gr-qc/9308012, Section 3, p. 8): (i) flatness
of the tangent-space metric $g_{\mu\nu} = \eta_{\mu\nu}$, (ii) $\theta$-independence of the number
of inequivalent vielbein degrees of freedom, and (iii) existence of a
consistent covariant derivative for Dirac spinors. These conditions rule
out multi-angle generalizations $\eta = \mathrm{diag}[\exp(i\theta_1), \exp(i\theta_2), \dots, \exp(i\theta_D)]$ (eq. (2)) and restrict $\theta(x) = \theta(T(x))$ to a single dynamical
degree of freedom per constant-T hypersurface. Consequently, a fluctuation
$\delta\theta = \pi - \theta$ over one Planck time $l_P$ across a spatial 3-volume $V \sim R^3$
induces an action variation $\Delta S \sim \Lambda^4 V l_P\, \delta\theta \sim (V/l_P^3)\, \delta\theta$ (eq. (36)),
suppressing expected quantum signature fluctuations to (eq. (37)):

$$\langle\delta\theta\rangle \sim l_P^3/V \sim (l_P/R)^3$$

For a universe with length scale $R \sim 10^{10}$ light years, Carlini &
Greensite estimate $\delta\theta \sim 10^{-184}$ radians.

Second, in Section 4 (Cosmological Constant Subtraction), because eq.
(17) is quartically divergent ($\propto \Lambda^4$ in $D = 4$), Carlini & Greensite test
whether adding a bare cosmological constant counterterm $S_c = \int d^D x\, \sqrt{g}\, \lambda_c$ (eq. (38)) alters the $D = 4$ selection (arXiv:gr-qc/9308012, Section 4,
pp. 12–13):

"The total effective potential becomes:

$$V_T(\theta) = \lambda_c e^{i\theta/2} + \lambda e^{-i(D-2)\theta/4} \quad (40)$$

It is clearly impossible to choose $\lambda$_c such that $V_T(\theta) = 0$ for all $\theta$.
Instead, the object would be to choose $\lambda$_c such that V_T = 0 at the
minimum/stationary point of $V_T(\theta)$. It will now be shown that it is only
possible to make such a choice in $D = 4$ dimensions, where the
minimum/stationary point is again Lorentzian signature."

Setting $V_T(\theta) = 0$ and $\frac{d}{d\theta} \mathrm{Im}[V_T(\theta)] = 0$ (eqs. (41)–(47)) forces $\bar{\theta} \equiv ((D-2)/2)\theta = \pi$ and $\theta = \pi$ with $|\lambda_c| = \lambda$, which holds only in $D = 4$,
reducing the total potential to $V_T(\theta) = \lambda \cos(\theta/2)$ (eq. (48)), whose
minimum is $\theta = \pm\pi$.

Third, in Section 5 (Mass Effects and $D = 6$ Broken Supersymmetry), when
field masses $m_B, m_F \ll \Lambda$ are included via an expansion in $x_{B(F)} \equiv m_{B(F)}^2/\Lambda^2$ (eqs. (57)–(59)), two qualifications emerge
(arXiv:gr-qc/9308012, Abstract & Section 5, pp. 1, 14–16). In $D = 4$ with
$n_F > n_B$, mass terms preserve the minimum of $\mathrm{Re}[V(\theta)]$ at $\theta = \pm\pi$ but
shift the stationary point of $\mathrm{Im}[V(\theta)]$ by $O(m^2/\Lambda^2) \approx 10^{-8}$ (for
GUT-scale masses and Planck-scale $\Lambda$), so the coincidence of minimum and
stationary point becomes approximate up to $O(m^2/\Lambda^2)$ (eq. (58)).
Meanwhile, in supersymmetric theories ($n_F = n_B$, Case II), the leading
$\Lambda^D$ term in eq. (17) vanishes identically; mass-squared splittings
$\Delta(x_n)_{BF}$ lift this degeneracy, and Carlini & Greensite state: "Mass
effects lift this degeneracy, and we show that a dynamical origin of
Lorentzian signature is also possible for (broken) supersymmetry theories
in D=6 dimensions, in addition to the more general non-supersymmetric case
in D=4 dimensions." Thus, $D = 4$ uniqueness applies strictly to
non-supersymmetric theories ($n_F \neq n_B$).

Fourth, in Section 2 (Regularization Dependence), Carlini & Greensite
note that the mechanism depends on using a continuous proper-time
(heat-kernel) cutoff rather than zeta-function, dimensional, or lattice
regularization (arXiv:gr-qc/9308012, Section 2, p. 5):

"For our purposes, the choice of heat-kernel regularization is essentially
unique. Zeta function and dimensional regulation methods contain implicit
subtractions which remove non-logarithmically (e.g. quadratically)
divergent terms; these happen to be the terms of interest here. On the
other hand, a naive momentum-space cutoff does not uniformly respect the
spacetime symmetries at $\theta = 0$, $\pm\pi$... The same objection applies to a
lattice cutoff; moreover, a regular lattice, even at $\theta = 0$, does not
respect the full $O(D)$ symmetry."

Subsequent work by Elizalde, Odintsov, and Romeo (1994), "Dynamical
Determination of the Metric Signature in Spacetime of Nontrivial
Topology", Classical and Quantum Gravity 11, L61–L67
(https://arxiv.org/abs/hep-th/9312132, PDF:
https://arxiv.org/pdf/hep-th/9312132), analyzed Greensite's formalism on
spacetimes with nontrivial topology under zeta-function regularization.
Because the full PDF body of hep-th/9312132 beyond its abstract snippet
was inaccessible in this sweep, the exact topological zeta-function
equations of Elizalde et al. (1994) are marked ABSTAIN (Unverified) rather
than guessed.

### 4. Audit of IRH v93.1 Against the Recovered Primary Literature
4.1 Citation and Mechanism Misattribution in IRH v93.1 §IX.3 ([17] and [18])

In §IX.3 (p. 25), IRH v93.1 states:

"Published dynamical-signature mechanisms [17] [18] require a one-loop
effective potential with more fermionic than bosonic degrees of freedom —
the condition first identified by Greensite [41] and refined by Carlini
and Greensite [42]. No purely classical Euclidean substrate is known to
yield Lorentzian signature."

Auditing references [17] and [18] directly against the primary literature
reveals a factual misattribution in IRH v93.1 §IX.3. Reference [17] is S.
Mukohyama and J.-P. Uzan, "From configuration to dynamics: Emergence of
Lorentz signature in classical field theory", Physical Review D 87, 065020
(2013) (https://arxiv.org/abs/1301.1361,
https://link.aps.org/doi/10.1103/PhysRevD.87.065020). As its title
explicitly indicates, Mukohyama & Uzan (2013) construct a classical field
theory on a Riemannian (Euclidean) space in which fields couple to the
gradient of a shift-symmetric scalar "clock field" $\phi$. Verbatim from
Physical Review D 87, 065020
(https://link.aps.org/doi/10.1103/PhysRevD.87.065020):

"(1) It requires that the clock field satisfies [a nonvanishing gradient
constraint] in a region $M_0$ of the Euclidean space. It follows that the
effective Lorentzian description is local and holds in $M_0$ ... (2) It is
limited to classical field theory in flat space. The extension to curved
space is discussed in Secs. III and IV below and the quantum aspects are
left for future investigations."

Reference [18] is J. Kehayias, S. Mukohyama, and J.-P. Uzan, "Emergent
Lorentz Signature, Fermions, and the Standard Model", Physical Review D
89, 105017 (2014) (https://arxiv.org/pdf/1403.0580,
https://arxiv.org/html/1403.0580v2), which extends the classical
clock-field effective metric of [17] to spinors and the Standard Model.
Verbatim from arXiv:1403.0580:

"Couplings to a clock field are responsible for triggering the change of
signature of the effective metric in which the standard fields propagate."

Neither [17] nor [18] uses Greensite's one-loop effective potential $V(\theta)$
or requires $n_F > n_B$. Conversely, IRH v93.1's universal negative claim
("No purely classical Euclidean substrate is known to yield Lorentzian
signature") is contradicted by [17], which achieves an emergent
Lorentzian effective metric in classical Euclidean field theory via a
clock field $\phi$ (subject to tuned clock-field couplings so different species
share a common light cone, and restricted to the region $M_0$). With respect
to the narrower question of whether a single-scalar Swift–Hohenberg $D_4$
standing-wave substrate without a tuned clock field can generate
Lorentzian signature classically, no such mechanism was found in the
literature sweep. A wider sweep that still finds nothing STRENGTHENS a
scoped bound — it does not prove a universal negative.

4.2 Structural Audit: Greensite's $n_F > n_B$ Condition vs. IRH v93.1's $E_6$ Gauge Sector and Generation Count

If IRH v93.1 adopts Reading (A) in §IX.2 (a 4D Euclidean base with
Lorentzian signature arising dynamically via the Greensite–Carlini
mechanism of §IX.3), the substrate's quantum field content at the UV
cutoff scale $\Lambda$ must satisfy $n_F > n_B$ (Case V of eq. (18)). Evaluating
n_F and n_B under Carlini & Greensite's propagating degree-of-freedom
convention (Assumption 1, where each real scalar has n_B = 1, each
massless vector boson in $D = 4$ has n_B = 2, the graviton has n_B = 2, and
each chiral Weyl fermion has n_F = 2) links Part IV ($E_6$ gauge group),
Part V.2 (generation count), and Part IX.3–IX.4:

Field-content table (Field-Content Model at Cutoff $\Lambda$ | Massless Bosonic
Propagating DOF (n_B) | Massless Fermionic Propagating DOF (n_F) | Net
Difference $\Delta_{FB} = n_F - n_B$ | Satisfies Greensite Condition $n_F > n_B$?):
- Standard Model (SU(3)_C $\times$ SU(2)_L $\times$ U(1)_Y + 1 Higgs doublet, $N_{\mathrm{gen}} = 1$, 15 Weyl) | $12 \times 2 + 4 = 28$ ($30$ w/ graviton) | $15 \times 2 = 30$ ($32$ w/ $\nu_R$) | $+2$ ($0$ to $+2$ w/ graviton) | Yes (marginal for $N_{\mathrm{gen}} = 1$)
- Standard Model ($N_{\mathrm{gen}} = 3$, 45 Weyl) | 28 ($30$ w/ graviton) | $45 \times 2 = 90$ ($96$ w/ $3\nu_R$) | $+62$ ($+60$ to $+66$ w/ graviton) | Yes (strongly
  satisfied)
- IRH v93.1 Unbroken $E_6$ Pure Gauge + 1 Generation ($27_F$, §IV.3) | $78 \times 2 = 156$ ($158$ w/ graviton) | $1 \times 27 \times 2 = 54$ | $-102$ ($-104$ w/ graviton) | No — Fails ($n_F < n_B$, Case I)
- IRH v93.1 Unbroken $E_6$ Pure Gauge + 2 Generations (2 $\times$ $27_F$) | 156
  ($158$ w/ graviton) | $2 \times 27 \times 2 = 108$ | $-48$ ($-50$ w/ graviton) | No —
  Fails ($n_F < n_B$, Case I)
- IRH v93.1 Unbroken $E_6$ Pure Gauge + 3 Generations (3 $\times$ $27_F$, §V.2
  Input) | 156 ($158$ w/ graviton) | $3 \times 27 \times 2 = 162$ | $+6$ ($+4$ w/ graviton) | Yes — Minimum viable $N_{\mathrm{gen}} = 3$
- Unbroken $E_6$ + 3 Generations + Fundamental Scalar Higgs (e.g., $27_H$ +
  $78_H$) | $156 + 54 + 78 = 288$ | 162 | $-126$ | No — Fails unless Higgs is
  composite or $E_6$ breaks above $\Lambda$

This comparison highlights two structural consequences for IRH v93.1.
First, in §V.2 (p. 19), IRH v93.1 concludes that $N_{\mathrm{gen}} = 3$ is an
un-derived INPUT after closing five geometric and algebraic routes.
However, if IRH invokes the Greensite mechanism in the unbroken $E_6$ phase
($\dim E_6 = 78$, so $n_B^{\mathrm{gauge}} = 156$), then $N_{\mathrm{gen}} = 1$ ($n_F = 54$) and $N_{\mathrm{gen}} = 2$ ($n_F = 108$) both fall into Case I ($n_F < n_B$), where min $\mathrm{Re}[V(\theta)]$ < 0
and no Lorentzian solution exists. Three generations ($N_{\mathrm{gen}} = 3$, giving
$n_F = 162$ > 156) is the minimum integer generation count for which $n_F > n_B$ holds in pure $E_6$ gauge theory (with a margin of $\Delta_{FB} = +6$, or $+4$
including the graviton). Second, because the margin $n_F - n_B^{\mathrm{gauge}} = +6$
at $N_{\mathrm{gen}} = 3$ is narrow, adding even one fundamental scalar Higgs multiplet
in the $27_H$ (54 real scalars) or $78_H$ (78 real scalars) at the cutoff
scale $\Lambda$ reverses the inequality to $n_F - n_B$ < 0. Furthermore, Carlini &
Greensite note that a discrete lattice cutoff breaks $O(D)$ invariance at
$\theta = 0$ and $O(D-1,1)$ invariance at $\theta = \pm\pi$ (arXiv:gr-qc/9308012, p. 5).
Although IRH v93.1 proves that the $D_4$ root system is a spherical
5-design and therefore isotropic at second and fourth order in k (§II.1,
$\Sigma_\alpha (k\cdot\alpha)^2 = 12|k|^2$, $\Sigma_\alpha (k\cdot\alpha)^4 = 12|k|^4$), sixth-order anisotropy
enters at the scale $q_0 = 2\pi/a_0$, meaning that applying Greensite's
heat-kernel integral to a $D_4$ substrate requires the signature cutoff $\Lambda$ to
lie in the continuum regime $\Lambda \ll q_0$ where $O(4)$ isotropy holds.

### 5. HLRE v5.1 Claim Ledger, Premise Ledger, Search Record, and Disclosures
5.1 Grading Protocol Under HLRE v5.1 as Amended (2026-11-12)

Under the 2026-11-12 amendments to HLRE v5.1:

Human-Gate Repeal (14:07 CST): The human-source and balance gates,
fallback grade caps ($\leq$ C Track E / F3 Track F), and the "unverified-by-human
preprint" label are repealed; Track F F2 is reachable on machine routes
alone.

External Verification Authorization (14:21 CST) & Replacement of I_1 $\to$ C
Bound (14:45–14:47 CST): The automatic I_1 $\to$ C independence bound is
repealed and replaced by external verification via an authorized
HLRE-constrained agent (Manus, Gemini 4 Argon, or Academia Co-Scientist)
audited locally claim-by-claim, with evidence grades following I_0 $\to$ D,
I_2 $\to$ B, I_3 $\to$ B, I_4 $\to$ A. Within this self-contained audit step, claims
verified across two primary peer-reviewed publications (Physics Letters B
300, 34 and Physical Review D 49, 866) plus independent local symbolic
computation (SymPy in [link — not recoverable]) achieve I_2 $\to$ B (Track E)
/ F2 (Track F) for mathematical derivation, accompanied by the §7
artificial-verification (I_1) disclosure in §5.4.

5.2 Complete HLRE v5.1 Claim Ledger for Sweep 4 (G-C20)

- G-C20.1 | Generalized Dynamical Signature Metric: the D-dimensional
  path integral interpolates from Euclidean ($\theta = 0$) to Lorentzian Feynman
  ($\theta = \pm\pi$) via $\eta_{ab} = \mathrm{diag}\{e^{i\theta}, 1, \dots, 1\}$. | Greensite (1993), Phys.
  Lett. B 300, 34; Carlini & Greensite (1994), Phys. Rev. D 49, 866 |
  Bound: I_2 $\to$ B (two peer-reviewed primary texts + algebraic check).
  Caps: Human-gate cap repealed. Postulation Ceiling: C as physical
  postulate; B / F2 as mathematical definition. Final: B (Track E) / F2
  (Track F).
- G-C20.2 | Exact One-Loop Scalar Determinant & Heat-Kernel Integral:
  under the DeWitt measure, a massless scalar contributes
  $\det{}^{-1/2}[-\sqrt{\eta}\, \eta^{ab} \partial_a \partial_b]$, yielding $V_S(\theta) = -\Lambda^D/[D(4\pi)^{D/2}] e^{-i(D-2)\theta/4}$. | Greensite (1993), eqs. (8)–(9); Carlini & Greensite
  (1994), eqs. (15)–(16) | Bound: I_2 $\to$ B (primary derivations + SymPy
  symbolic integration [link — not recoverable]). Ceiling: B / F2
  (conditional on Measure Assumptions 1–2 and heat-kernel cutoff $\Lambda$).
  Final: B / F2.
- G-C20.3 | Exact Multi-Species One-Loop Potential $V(\theta)$: for n_B bosonic
  and n_F fermionic massless propagating DOF, $V(\theta) = (n_F - n_B) \Lambda^D/[D(4\pi)^{D/2}] e^{-i(D-2)\theta/4}$. | Greensite (1993), eq. (10); Carlini
  & Greensite (1994), eq. (17) | Bound: I_2 $\to$ B. Ceiling: B / F2
  (resolves prior toy model $\mathrm{Re}\, V_{\mathrm{toy}} = \Delta \cos\theta$, which lacked the $(D-2)/4$
  factor). Final: B / F2.
- G-C20.4 | $D = 4$ Uniqueness Argument (Massless Non-SUSY): simultaneous
  minimization of $\mathrm{Re}[V(\theta)]$ and stationarity of $\mathrm{Im}[V(\theta)]$ on [$-\pi$, $\pi$] holds
  iff $n_F > n_B$ and $D = 4$ at $\theta = \pm\pi$. | Greensite (1993), eq. (11); Carlini
  & Greensite (1994), eq. (18) & Cases I–V | Bound: I_2 $\to$ B (primary texts
  + symbolic case-by-case verification [link — not recoverable]). Caps:
  Scoped to massless / non-SUSY ($n_F \neq n_B$) theories under heat-kernel
  regularization. Final: B / F2.
- G-C20.5 | Curved-Space Single-Angle Constraint & Fluctuation
  Suppression: consistency in curved space rules out multiple Wick angles
  and suppresses $\langle$$\delta$$\theta$$\rangle$ $\sim$ $(l_P/R)^3$ $\sim$ $10^{-184}$ rad. | Carlini & Greensite
  (1994), Abstract & Section 3, eqs. (2), (36)–(37) | Bound: I_2 $\to$ B
  (primary source derivation + order-of-magnitude check). Caps: Depends on
  constant-T hypersurface slicing constraint $\theta$ = $\theta$(T(x)). Final: B / F2.
- G-C20.6 | One-Loop Cosmological Constant Subtraction Uniqueness:
  cancelling $V_T(\theta)$ via a counterterm $\lambda_c \sqrt{g}$ at the minimum/stationary
  point is possible uniquely in $D = 4$ at $\theta = \pm\pi$. | Carlini & Greensite
  (1994), Section 4, eqs. (38)–(48) | Bound: I_2 $\to$ B (primary derivation
  in Section 4 verified algebraically). Caps: One-loop flat-background
  level. Final: B / F2.
- G-C20.7 | Mass Effects & $D = 6$ Broken-SUSY Exception: for $n_F = n_B$
  (broken SUSY), mass effects lift the Case II degeneracy and allow
  Lorentzian signature selection in $D = 6$. | Carlini & Greensite (1994),
  Abstract & Section 5, eqs. (57)–(59) | Bound: I_1/I_2 $\to$ C (statement
  and eqs. (57)–(59) verified in primary text, but intermediate pages
  16–22 and Appendix eqs. 81–87 were truncated in extraction). Final: C /
  F3 (Partial ABSTAIN on intermediate algebra).
- IRH-C20a | IRH v93.1 §IX.3 Citation of [17] and [18]: IRH claims [17]
  (Mukohyama & Uzan 2013) and [18] (Kehayias et al. 2014) require a
  one-loop $n_F > n_B$ potential and that no classical Euclidean model
  yields Lorentzian signature. | Manuscript (uploaded: IRH_v93_1.pdf, p.
  25) vs. PRD 87, 065020 & PRD 89, 105017 | Bound: I_0 $\to$ D (contradicts
  primary sources [17] and [18], which are classical clock-field models,
  not one-loop $n_F > n_B$ models). Final: D / F4 (Refuted Citation /
  Conflation).
- IRH-C20b | IRH v93.1 $E_6$ Gauge Sector vs. $n_F > n_B$: in unbroken $E_6$
  ($n_B^{\mathrm{gauge}} = 156$), $N_{\mathrm{gen}} = 1$ ($n_F = 54$) and $N_{\mathrm{gen}} = 2$ ($n_F = 108$) fail
  $n_F > n_B$; $N_{\mathrm{gen}} \geq 3$ ($n_F = 162$) is required, with no large fundamental
  UV Higgs sector. | Manuscript (§§IV.3, V.2, IX.3–IX.4) + DOF computation
  | Bound: I_2 $\to$ B on the algebraic degree-of-freedom inequality (54
  N_gen > 156 $\iff$ $N_{\mathrm{gen}} \geq 3$); ABSTAIN / OPEN on IRH's unconstructed $E_6$
  Higgs sector (§IX.4). Final: B / F2 (DOF constraint); OPEN (IRH UV
  completion).

5.3 Premise Ledger and Unverified / Abstain Register

Premise P1 (Complex Dynamical Tangent-Space Metric): the Greensite
mechanism assumes that the tangent-space metric $\eta_{ab} = \mathrm{diag}\{e^{i\theta}, 1, \dots, 1\}$ fluctuates quantum-mechanically over $\theta \in [-\pi, \pi]$ while the $D-1$ spatial
entries remain fixed at +1.

Premise P2 (DeWitt Supermetric Modulus Measure): the phase
$\exp[-i(D-2)\theta/4]$ depends directly on defining the scalar functional measure
via the real modulus $|G|$ rather than an analytic continuation of G that
would cancel $\sqrt{\eta} = e^{i\theta/2}$ in the kinetic operator.

Premise P3 (Proper-Time Heat-Kernel Cutoff Without Subtraction): the
potential $V(\theta) \propto \Lambda^D$ relies on retaining the power-law UV divergence
under a continuous proper-time cutoff s $\geq$ 1/$\Lambda$^2. As Carlini & Greensite
explicitly state (arXiv:gr-qc/9308012, p. 5), zeta-function and dimensional
regularization subtract power divergences and remove this term, while a
discrete lattice cutoff breaks $O(D)$ and $O(D-1,1)$ symmetry.

ABSTAIN Item 1 — Elizalde, Odintsov, and Romeo (1994), Classical and
Quantum Gravity 11, L61–L67 (https://arxiv.org/abs/hep-th/9312132):
bibliographic metadata and abstract snippet verified, but the full PDF
text and explicit zeta-regularized equations on nontrivial topologies were
inaccessible in this sweep. Graded ABSTAIN (Unverified).

ABSTAIN Item 2 — Carlini & Greensite (1994)
(https://arxiv.org/pdf/gr-qc/9308012), Equations (49)–(56), Pages 16–22,
Section 6 Full Text, and Appendix Equations (81)–(87): while Sections 1–4
and the core equations of Section 5 (eqs. (57)–(59)) were recovered
verbatim, the intermediate algebraic steps of the $D = 6$ broken-SUSY
expansion on pages 16–22 and Appendix eqs. (81)–(87) were omitted in the
text extraction. Those specific intermediate equations are graded ABSTAIN
(Unverified).

ABSTAIN Item 3 — Carlini & Greensite (1995), Physical Review D 52,
6947–6964 (https://arxiv.org/abs/gr-qc/9502023): identified in the search
record as a follow-up paper on square-root actions and metric signature,
but not required for the one-loop determinant of Gap G-C20 and not read in
full; recorded as ABSTAIN / Out of Scope.

5.4 Search Record and §7 Artificial Verification Disclosure

Open-literature queries were executed across arXiv (gr-qc/9210008,
gr-qc/9308012, hep-th/9312132, gr-qc/9502023, 1301.1361, 1403.0580), APS
Physical Review D (10.1103/PhysRevD.49.866, 10.1103/PhysRevD.87.065020,
10.1103/PhysRevD.89.105017), Elsevier Physics Letters B
(10.1016/0370-2693(93)90744-3), and IOP Classical and Quantum Gravity.
Full-text extraction succeeded for gr-qc/9210008 (complete paper, eqs.
1–11) and gr-qc/9308012 (Abstract, Sections 1–4 complete, Section 5
partial eqs. 57–59), and primary property and abstract extraction succeeded
for Physical Review D 87, 065020 (1301.1361) and 1403.0580.

In accordance with HLRE v5.1 §7 and the 2026-11-12 amendments, all
literature retrieval, equation extraction, symbolic SymPy recomputation
(), and claim-by-claim auditing in this report were performed entirely by
artificial systems (I_1 machine verification, cross-checked against two
peer-reviewed primary sources for I_2 mathematical bounds). No human gate
was applied, and no manuscript files were edited or external authors
contacted.

Sources used (as listed by the report):
1. arxiv.org — Dynamical Origin of the Lorentzian Signature of Spacetime
2. arxiv.org — (Greensite 1993 PDF)
3. arxiv.org — [gr-qc/9308012] Why is Spacetime Lorentzian?
4. arxiv.org — arXiv:gr-qc/9308012v1 12 Aug 1993
5. IRH_v93_1.pdf (uploaded manuscript)
6. arxiv.org — Emergence of Lorentz signature in classical field theory
7. indico.yukawa.kyoto-u.ac.jp — arXiv: 1301.1361 with Jean-Philippe Uzan
8. link.aps.org — Emergence of Lorentz signature in classical field
   theory | Phys. Rev. D
9. arxiv.org — Emergent Lorentz Signature, Fermions, and the Standard
   Model
10. arxiv.org — arXiv:1403.0580v2 [hep-th] 27 May 2014
11. arxiv.org — [hep-th/9312132] Dynamical Determination of the Metric
    Signature
12. sigma-journal.com — Emergent Models for Gravity: an Overview of
    Microscopic Models?
13. arxiv.org — Dynamical Determination of the Metric Signature in
    Spacetime of (nontrivial topology)
14. arxiv.org — arXiv:2310.17266v2 [gr-qc] 26 Jan 2024
15. arxiv.org — [gr-qc/9502023] Square Root Actions, Metric Signature,
    and the Path
16. arxiv.org — Square Root Actions, Metric Signature, and the
    Path-Integral of
17. sigma-journal.com — Emergent Models for Gravity: an Overview of
    Microscopic Models

Sources browsed but not used (as listed by the report): arxiv.org (Is the
Lorentz signature of the metric of spacetime electromagnetic in…;
arXiv:1812.01275v4; High Energy Physics - Theory Aug 1993;
arXiv:gr-qc/9301023v1; arXiv:1508.01458v1; Why do we live in 3+1
dimensions?; Minkowski metric signature as a statistical prediction of
piecewise-flat…; arXiv:1301.1361v2; arXiv:1811.03369v1; From configuration
to dynamics Emergence of Lorentz signature in…; arXiv:2310.17266v2 [gr-qc];
arXiv:gr-qc/9308012 is used; The emergent Big Bang scenario ($\times$2);
Emergent Lorentzian dispersion relations from a Euclidean scalar; High
Energy Physics - Theory Dec 1993; Signature change events: A challenge
for quantum gravity? ($\times$2)), www-library.desy.de (E-Preprints gr-qc/9308),
gist.github.com (Reading List), journals.aps.org (PRD Volume 49 Issue 2;
Emergent big bang scenario), mdpi.com (Minimum Spacetime Length…; The
Primordial Particle Accelerator of the Cosmos), fr.scribd.com
(Fluctuations Quantiques à l'Échelle de Planck), researchgate.net
(Динамическое образование массы Планка…; (PDF) Causal structures in
Gauss-Bonnet gravity), scribd.com (Insights on 2D Quantum Gravity
Solutions), markscenter.sas.upenn.edu (John Kehayias), www2.yukawa.kyoto-u.ac.jp
(Research Experience), iap.fr (liste sur SPIRES), academic.oup.com
(Exact black hole solutions in shift symmetric scalar–tensor theories),
alphaxiv.org (The emergent Big Bang scenario; Emergent Lorentz Signature,
Fermions, and the Standard Model), preprints.org (Emergence and Exclusivity
of Lorentzian Signature and Unit-Norm…), semanticscholar.org (Dynamical
generation of spacetime signature by massive quantum…), mathnet.ru
(Динамическое образование массы Планка…), universal-physics.khe.money
(13.62 The Indefinite-Metric / Krein Carrier Route), pure.mpg.de
(Non-perturbative Lorentzian quantum gravity…; arXiv:hep-th/0001124 v2),
pergamos.lib.uoa.gr (Κ$\lambda$ασική και κβαντική $\pi$εριγρα$\phi$ή αν$\eta$γμένων $\delta$ράσεων τ$\eta$ς
βαρύτ$\eta$τας), d-nb.info (JHEP08(2022)129), arxiv.org (Feynman's $i\epsilon$
prescription, almost real spacetimes, and acceptable…).

--- END OF REPORT TEXT ---

Work left undone / notes for the local audit: nothing was edited, filed,
or sent to any author; the manuscript was only attached to the Gemini
chat. The one item not reproducible from the page is the destination of
the SymPy recomputation link cited in the report (it renders as an empty
link). The earlier plain-chat run produced no response text and was
discarded. The \$300/service/month spend ceiling was not approached: this
run cost \$0.
