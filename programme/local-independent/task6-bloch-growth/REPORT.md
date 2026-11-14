# Task 6 — Bloch growth about the harmonically relaxed $D_{4}$ wave

## CLAIM and STATUS (together, at the top)

**CLAIM.** Linearising conserved Model B about the harmonically relaxed $D_{4}$ stationary field $\psi^{*}$ (mean $\bar{\psi}=-0.18$, box $[0,2\pi]^{4}$), the Bloch growth rate $\lambda(q)$ is negative at every one of 259 distinct sampled fractional wavevectors $q$ in the Brillouin zone, with the four $q=0$ Goldstone zeros recovered exactly. The least-damped non-Goldstone rate sampled is $\lambda_{\max}=-1.332276$ at $q=(0.32,0.32,0.32,0)$. The long-wave branches are: transverse displacement $\lambda_{T}/|q|^{2}\to-42.4$, longitudinal displacement $\lambda_{L}/|q|^{2}\to-128.0$, and conserved-mean $\lambda_{M}/|q|^{2}\to-64.26$, the last matching the analytic Schur-complement prediction $-64.255220$ to $0.01\%$ at the smallest sampled $|q|$.

**STATUS.** Sampled stability map: **COMPLETE** at $K_{b}=4$ (259 distinct $q$, 262 rows). Continuum stability over the whole Brillouin zone: **UNVERIFIED** — a finite sample cannot establish it, and no interval enclosure was run. The frozen-ansatz positive quartet $+0.0228772435$ from A6 does **not** survive relaxation: it was an artefact of linearising about a non-stationary field, and the corresponding branch at the relaxed field is the Goldstone zero. The $K_{b}=2$ coarse map's $\lambda_{\max}(0)=-0.00876$ is likewise withdrawn as a truncation artefact (see §7, withdrawal ledger). Headline grades (§8): sampled-map stability **C** (Track E, I1); analytic zero-mode and mean-channel checks **F2** (Track F, I1); continuum stability **ABSTAIN / UNVERIFIED**.

## 1. Model, parameters, and what was reused from prior work

Parameters (verified from the prior files, not assumed from this brief): $r=-0.35$, $\bar{\psi}=m=-0.18$, $q_{0}^{2}=8$, $u=v=1$, mobility $1$, box $[0,2\pi]^{4}$. Derived: $\alpha=r-2um+3vm^{2}=0.1072$, $\beta=u-3vm=1.54$. Frozen amplitude $A=0.07757529633928076$, the larger root of $\alpha-8\beta A+141A^{2}=0$. Sources: `a6-offshell/parameters_validation.json` and `4d-field-test/parameters.json` (identical values in both), `ws-a-core-computations/d4model.py` (same functional).

Functional and dynamics (A6 §1, 4D-test §"Functional"):

$$F[\psi]=\int d^{4}x\left[\frac12\psi\{r+(q_{0}^{2}+\nabla^{2})^{2}\}\psi-\frac{u}{3}\psi^{3}+\frac{v}{4}\psi^{4}\right],\qquad \partial_{t}\psi=\nabla^{2}\mu,\qquad \mu=\{r+(q_{0}^{2}+\nabla^{2})^{2}\}\psi-u\psi^{2}+v\psi^{3}.$$

**Frozen-ansatz reuse, stated plainly.** REUSED: (i) the parameter values and the operator construction pattern (exact $W$ convolution, symmetrised $B=-D^{1/2}HD^{1/2}$) from A6; (ii) the ETD2 field solver from the 4D field test, to relax the field; (iii) the frozen 24-mode ansatz itself, only as the *starting point* of the relaxation. NOT REUSED: the A6 growth rates $+0.0228772435$ and the A6 spectra are not premises anywhere below — they are rates about a different (non-stationary) base field, and §6 shows they are superseded. The linearisation below is about the relaxed field only.

## 2. Step 1 — the relaxed stationary field (recomputed locally)

The frozen ansatz $\psi_{0}=m+A\sum_{s\in S}e^{is\cdot x}$ ($S$ the 24 vectors $2(\pm e_{i}\pm e_{j})$) was integrated under Model B with the 4D-test ETD2 solver (`Field`/`integrate` in `run_field_study.py`, imported, not copied), $K=4$, $N=18$, $dt=0.1$, to $t=40$; then re-relaxed at $K=6$, $N=28$, to $t=40$ from the embedded $K=4$ coefficients. No noise was added; the run is deterministic.

| Quantity | This run ($K=4$) | 4D-test target | Difference |
|---|---|---|---|
| Excess energy | $-0.007726209284874$ | $-0.007726209285$ | $1.3\times10^{-13}$ |
| Star amplitude | $0.077675666123445$ | $0.07767566612344486$ | $1.4\times10^{-16}$ |
| Final RHS RMS | $1.074\times10^{-15}$ | $\le1.21\times10^{-15}$ (their endpoints) | — |
| Modulation power | $0.144806953602124$ | $0.14480695360212426$ (refinement table) | $1\times10^{-16}$ |

$K=6$ check: energy $-0.007727623601437$ vs target $-0.007727623601$ (difference $4.4\times10^{-13}$), RHS RMS $1.454\times10^{-15}$, star amplitude $0.077681748362012$. Accepted steps 640, rejected 0, at both cutoffs; largest step energy increase $5.2\times10^{-18}$. The relaxed field is therefore reproduced independently of the 4D-test *driver* (same ETD2 code, so this checks my driver and the relaxation, not the solver itself — recorded honestly as one pipeline, I1).

Saved: `data/relaxed_K4.npz` (6,560 coefficients), `data/relaxed_K6.npz` (28,560 coefficients), `data/relaxation_log.json`, `data/relaxation_trace.csv`.

## 3. Step 2 — Bloch operator about $\psi^{*}$

For a Bloch wavevector $q\in[0,1)^{4}$ write $\eta(x)=e^{iq\cdot x}u(x)$ with $u$ $2\pi$-periodic. Fourier modes are $k=n+q$, $n\in\mathbb{Z}^{4}$, $|n_{i}|\le K_{b}$. With $\psi^{*}$ stationary, $\partial_{t}\eta=L_{q}\eta+O(\eta^{2})$ with

$$L_{q}=-D_{q}H_{q},\qquad D_{q}=\mathrm{diag}(|n+q|^{2}),$$
$$(H_{q})_{n,n'}=\{r+(8-|n+q|^{2})^{2}\}\delta_{n,n'}+W_{\,n-n'},\qquad W_{p}=\widehat{w}_{p},\quad w(x)=-2\psi^{*}(x)+3\psi^{*}(x)^{2}.$$

$B_{q}=-D_{q}^{1/2}H_{q}D_{q}^{1/2}$ is real symmetric (below) and similar to $L_{q}$ since $D_{q}>0$; its eigenvalues are the growth rates $\lambda(q)$. At $q=0$ the $n=0$ row/column is excluded (mean fixed); for $q\ne0$, $n=0$ is the $k=q$ mode and is included.

$W$ was built by FFT on an $N=28$ grid from the relaxed coefficients (exact for the quadratic product: relaxed support $|k_{i}|\le4$, $W$ support $|p_{i}|\le8<14$). Audit of $W$ (K4 field): $W_{0}=0.8916208608$; odd-shift $\max|W_{p}|=1.483\times10^{-17}$ (roundoff); $\max|\mathrm{Im}\,W_{p}|=5.13\times10^{-16}$.

**Parity sectors (structural fact, checked).** The relaxed field has Fourier support only on vectors with all components even (the star is even, and Model B preserves even support). Hence $W_{p}\ne0$ only for $p$ even, so $H_{q}$ and $B_{q}$ block-diagonalise by $n\bmod 2$: 16 parity sectors, sizes 256–625 at $K_{b}=4$. This makes the $K_{b}=4$ problem 16 dense eigensolves of size $\le625$ per $q$, instead of one $6{,}561\times6{,}561$ diagonalisation. The off-diagonal part of $H_{q}$ is $q$-independent; only the diagonal changes with $q$.

## 4. Step 3 — analytic zero-mode checks (before trusting numerics)

**C1b — Goldstone.** If $\psi^{*}$ is stationary, $\mu[\psi^{*}]$ is constant, so $\partial_{j}\mu[\psi^{*}]=0$, and $\partial_{j}\mu=H\,\partial_{j}\psi^{*}$ (linearisation), hence $H\,\partial_{j}\psi^{*}=0$ and $L\,\partial_{j}\psi^{*}=0$ for $j=1,\dots,4$. At $K_{b}=4$ (full relaxed band):

$$\|H\,\partial_{j}\psi^{*}\|/\|\partial_{j}\psi^{*}\| = 1.99\times10^{-15},\ 2.00\times10^{-15},\ 1.94\times10^{-15},\ 2.01\times10^{-15}.$$

The four largest eigenvalues at $q=0$ are $+1.54\times10^{-12}$, $-7.71\times10^{-12}$, $-2.61\times10^{-11}$, $-5.74\times10^{-11}$ (four Goldstone zeros to $\le6\times10^{-11}$); the next rate is $-2.738137332915544$ (star distortions). **PASS.**

**C2 — Finite-difference check of $H$.** Centred difference of $\mu[\psi^{*}+\varepsilon\eta]$ vs $H\eta$, $\varepsilon=10^{-6}$, random Hermitian $\eta$ (seed 20261114): relative $L^{2}$ error $8.435\times10^{-11}$. **PASS.** (Checked at $K_{b}=3$; it validates the $H$ construction, not the cutoff.)

**C3b — Conserved-mean channel (Schur complement).** At $q=0$, partition $H$ as $n=0$ versus the rest $Q$. The dressed mean mode has $y_{Q}=-H_{QQ}^{-1}H_{Q0}$ and $(Hy)_{0}=S$, $S=H_{00}-H_{0Q}H_{QQ}^{-1}H_{Q0}$, giving the small-$q$ prediction $\lambda_{M}(q)=-|q|^{2}S+O(|q|^{4})$. At $K_{b}=4$: $H_{00}=64.541621$, $H_{QQ}$ minimum eigenvalue $-1.52\times10^{-12}$ (the Goldstone zero lives in $Q$, as it must — it does not contaminate $S$ because $(H\,\partial_{j}\psi^{*})_{0}=0$), $S=64.255220$, so the predicted slope is $-64.255220$. Measured $\lambda_{M}/|q|^{2}$ on the axis cut: $-64.25$ at $t=0.02$ and $t=0.025$, $-64.21$ at $0.05$, $-64.09$ at $0.10$, $-63.86$ at $0.15$ — converging to the Schur value as $q\to0$. **PASS** (agreement $0.01\%$ at the smallest $|q|$).

## 5. Step 4 — the Bloch map ($K_{b}=4$)

259 distinct $q$ (262 rows; 3 duplicate list entries), comprising structured cuts — axis $(t,0,0,0)$, diagonals $(t,t,0,0)$, $(t,t,t,0)$, $(t,t,t,t)$, fine 0.02-step cuts, zone-boundary points ($q_{i}=0.5$), 4 generic points — and 150 random points uniform in $[0,0.5]^{4}$ (seed 20261114; the spectrum is invariant under sign flips and permutations of $q$, check C6). Full spectrum per $q$ (all eigenvalues, all 16 sectors).

| Scope | Least-damped $\lambda_{\max}$ sampled | Where |
|---|---|---|
| All $q\ne0$ sampled | $-0.016973$ | $q=(0.02,0,0,0)$ (Goldstone branch) |
| $\|q\|>0.05$ | $-0.146324$ | $q=(0.06,0,0,0)$ (Goldstone branch) |
| $\|q\|>0.2$ | $-1.064954$ | random point, $\|q\|=0.2005$ |
| $\|q\|>0.25$ (and $>0.3$, $>0.4$, $>0.5$) | $-1.332276$ | $q=(0.32,0.32,0.32,0)$ |
| Zone corners | $-7.292740$ at $(0.5,0.5,0.5,0.5)$; $-3.972657$ at $(0.5,0.5,0,0)$; $-2.385206$ at $(0.5,0,0,0)$ | — |

**No positive growth rate was found at any sampled $q$.** The least-damped region away from the Goldstone asymptote is the $(t,t,t,0)$ diagonal around $t=0.32$–$0.34$ ($\lambda_{\max}\approx-1.33$), where modes with $|n+q|^{2}\approx8.67$ approach the resonant sphere; it stays negative by a margin of $1.33$.

**Long-wave branches (axis cut $q=(t,0,0,0)$).** Eigenvector overlaps with $\partial_{j}\psi^{*}$ identify the branches (file `data/goldstone_overlaps.csv`): ranks 1–3 are transverse displacement (overlap $0.999$ with $\partial_{2},\partial_{3},\partial_{4}$, zero with $\partial_{1}$); rank 5 at $t=0.05$ is longitudinal displacement (overlap $1.000$ with $\partial_{1}$); rank 4 is the mean channel (overlap $0.000$ with all $\partial_{j}$).

| $t$ | $\lambda_{T}/t^{2}$ | $\lambda_{M}/t^{2}$ | $\lambda_{L}/t^{2}$ | Mean-channel $n=0$ power |
|---|---|---|---|---|
| $0.02$ | $-42.43$ | $-64.25$ | $-127.97$ | $0.726$ |
| $0.025$ | $-42.30$ | $-64.25$ | $-127.97$ | $0.726$ |
| $0.05$ | $-41.25$ | $-64.21$ | $-127.92$ | $0.724$ |
| $0.075$ | $-39.55$ | $-64.16$ | $-127.78$ | $0.718$ |
| $0.10$ | $-37.31$ | $-64.09$ | $-127.42$ | $0.704$ |
| $0.125$ | $-34.67$ | $-63.99$ | $-126.62$ | $0.672$ |
| $0.15$ | $-31.81$ | $-63.86$ | (branch below $-2.75$) | $0.614$ |

Reading: $\lambda_{T}/|q|^{2}\to-42.4$ and $\lambda_{L}/|q|^{2}\to-128.0$ as $q\to0$ (two smallest points agree to $0.3\%$ and $0.01\%$ respectively); the transverse branch then bends toward the star-mode plateau ($-2.74$) and has no single quadratic coefficient over $t\le0.15$ (through-origin fit $-33.56$ is a summary, not a stiffness, and is **not** quoted as one). The mean channel is the cleanest: $\lambda_{M}=-64.255220\,|q|^{2}$ to $O(|q|^{4})$, per §4. At $t\ge0.2$ the mean-channel identification by maximum $n=0$ power weakens (power $0.35$ at $t=0.2$, $0.014$ at $t=0.25$; $82/262$ rows have power $<0.3$), so $\lambda_{M}$ values there are reported as max-$n=0$-power rates, not as a clean branch label; the slope claim is restricted to $|q|\le0.15$ where the power is $\ge0.61$.

## 6. Checks run (quoted tool verdicts)

Tools: conda env `jacobian-conjecture-2d` python, Python 3.11.16, NumPy 2.4.6, SciPy 1.17.1, Matplotlib 3.11.2. All scripts below exit 0 unless noted. Singular was not used in this task (no symbolic step required) — recorded as NOT RUN, not as a gap in the numerics.

| Check | Result | Verdict |
|---|---|---|
| Relaxation reproduces 4D-test energy/star amplitude (K4/K6) | $\Delta E=1.3\times10^{-13}$ / $4.4\times10^{-13}$; $\Delta A=1.4\times10^{-16}$; RHS RMS $1.07\times10^{-15}$ / $1.45\times10^{-15}$ | **PASS** |
| C1b Goldstone $H\,\partial_{j}\psi^{*}$ at $K_{b}=4$ | $1.94$–$2.01\times10^{-15}$ relative; $q=0$ eigenvalues within $6\times10^{-11}$ of zero | **PASS** |
| C2 FD vs $H$ | relative $L^{2}$ error $8.435\times10^{-11}$ | **PASS** |
| C3b Schur slope vs measured mean slope | $-64.255220$ vs $-64.25$ at smallest $q$ ($0.01\%$) | **PASS** |
| C4b $K_{b}=4$ vs $K_{b}=2$ $\lambda_{\max}$ (9 points) | $K_{b}=4-K_{b}=2=+0.0071$ to $+0.0210$; mean-channel differences $\le0.0078$ | **PASS** (quantifies bias; see §7) |
| C5b K6-relaxed vs K4-relaxed $W$, $K_{b}=4$ (7 points) | $\lambda_{\max}$ shifts $-0.00082$ to $-0.00051$ (K6 more negative) | **PASS** (systematic $\le8.2\times10^{-4}$) |
| C6 symmetry duplicates (perm/sign/reverse) | max top-6 differences $1.20\times10^{-11}$, $7.88\times10^{-12}$, $8.85\times10^{-12}$ | **PASS** |
| Goldstone overlaps identify transverse/longitudinal/mean branches | sums $0.99$–$1.00$ at $t=0.05$; longitudinal overlap $1.000$ | **PASS** |
| Coarse $K_{b}=2$ map (48 points, step 2) | all rates negative; $\lambda_{\max}(0)=-0.00876$ | **SUPERSEDED** (§7) |
| Dense 0.01-step cuts; full 4D dense grid; interval spectral enclosure | not run | **NOT RUN** (costed in §9) |
| External verification (Manus / Gemini / Co-scientist audit) | not run by this worker (independence: must not use Co-scientist output) | **NOT RUN** |

Two runs hit the 580 s foreground timeout and were superseded, with no data lost: the first $K_{b}=4$ attempt (step 3) printed C1b/C3b and partial cuts before the timeout; step 3b wrote its map incrementally (208 rows survived) and step 3c completed it (262 rows) plus all checks, exit 0 in 161 s. The $K=6$ relaxation ran as a background job, exit 0 in 198 s.

## 7. The $K_{b}=2$ artefact — withdrawal ledger (no silent correction)

**Withdrawn statement** (from the coarse $K_{b}=2$ run, step 2): "$\lambda_{\max}(q=0)=-0.0087576211$ at the relaxed field." **Error family:** cutoff truncation of the base field's own band (the relaxed field lives on $|n_{i}|\le4$; $K_{b}=2$ and $K_{b}=3$ drop its $|n_{i}|=4$ even modes). **Why it looked consistent:** the relaxed field has only even Fourier support, so $K_{b}=2$ and $K_{b}=3$ have the *identical* even sector (components $-2,0,2$ only) and agreed to $10^{-9}$ while both being wrong by $0.0088$. The $K_{b}=3$ Goldstone check C1 gave $1.639\times10^{-3}$, the same artefact. **Correction:** at $K_{b}=4$ the even sector is complete in-band, C1b is $2\times10^{-15}$, and $\lambda_{\max}(0)=+1.5\times10^{-12}$ (roundoff). The $K_{b}=2$ CSV is retained as `data/bloch_coarse_Kb2.csv` as a sensitivity record only; no conclusion in §5 uses it except through C4b. The A6 frozen quartet $+0.0228772435$ is likewise not a property of the relaxed field: A6's own §4 shows it follows from the frozen field's residual (norm $4.25853893$) via a Schur-complement minimum of $-0.00286$; at the relaxed field that Schur minimum is $0$ to $10^{-12}$.

## 8. Rival / failure mode

The main rival to "no Bloch instability" is a **narrow instability band** between sampled $q$ points, where some $|n+q|^{2}$ crosses $8$ exactly and the coupling $W$ pushes $H$ negative. Against it: (i) the map samples the resonance region on 0.02-step fine cuts along the axis and the $(t,t,t,0)$ diagonal, plus 150 random points; the least-damped rate there is $-1.33$, and observed $|\nabla_{q}\lambda_{\max}|\lesssim10$ per unit $q$ along cuts, so a positive band narrower than $\sim0.1$ in $q$ would need a gradient $\gtrsim13$ per unit $q$ with no precursor in neighbouring points — possible in principle, not seen; (ii) the K6 sensitivity shifts rates by only $\le8.2\times10^{-4}$, far below the $1.33$ margin. The second rival is **longer-wave / larger-box instability**: this calculation is on the $2\pi$ box with the tuned $q_{0}^{2}=8$; $q\to0$ is covered by the Goldstone/mean analysis, but a larger box (smaller $q_{0}$ spacing, incommensurate modes) is a different calculation and is not covered here. The third rival is **nonlinear / finite-amplitude instability**: linear Bloch rates say nothing about nucleation or large perturbations; the 4D field test's patterned recovery is the only evidence there, and it is a separate (finite-box, $t=200$) result.

## 9. Evidence that would change the answer; costed pending work

What would change the answer: (a) any sampled $q$ with $\lambda_{\max}>0$ on a finer grid; (b) a K6/K8 Bloch computation (full band of the K6 field) shifting some $\lambda_{\max}$ by $>1.33$ — the measured shift is $8\times10^{-4}$, so this would require a qualitatively different effect; (c) an interval enclosure proving a positive eigenvalue somewhere; (d) a larger-box computation showing a growing incommensurate mode.

Costed caps (all **PENDING**, none started, no GCP spend on my authority):
- Dense 1D cuts at 0.01 steps (axis + 3 diagonals, $\approx$200 $q$, $\approx$2 s per $q$ measured): $\approx$400–550 s local, $\$0$.
- Full 4D dense map at 0.05 steps over $[0,0.5]^{4}$: $11^{4}=14{,}641$ $q$ $\times\approx$2 s $\approx8.1$ h single-thread ($\approx$2 h on 4 workers); local $\$0$; on GCP lean-build-4 ($\approx\$1.22$/h) $\approx\$2.44$. Needs Brandon's approval before any GCP spend.
- Interval-certified spectral enclosure: NOT RUN; no tooling in place; implementation + verification cost TBD.
- External audit of this report by an authorised verifier (Manus / Gemini 4 Argon / Academia Co-scientist, under HLRE): via the parent agent, not this worker.

## 10. Per-claim HLRE grades (v5.1 as amended 2026-11-12)

Tier: Standard (search exceeds hand enumeration). Independence: **I1** throughout — all verification is local and artificial, sharing the model, the ETD2 solver family, and this worker's own code; no external verifier has audited this report. (The I1$\to$C bound is repealed; grades below follow the remaining rules: worst of independence bound, caps, postulation ceiling, support in the record.)

| # | Narrow claim | Track | Grade computation | Grade |
|---|---|---|---|---|
| R1 | Relaxed field reproduces the 4D-test stationary state (energy, star amplitude, RHS) | F | F2 (two routes: my ETD2 driver vs the 4D-test run; agreement $10^{-13}$–$10^{-15}$) | **F2** |
| G1 | At $q=0$ the relaxed field has four Goldstone zeros ($H\,\partial_{j}\psi^{*}\sim2\times10^{-15}$, eigenvalues within $6\times10^{-11}$ of zero) | F | F2 (analytic identity + direct computation + FD check C2) | **F2** |
| M1 | Conserved-mean slope $\lambda_{M}/|q|^{2}\to-64.26$, matching Schur $S=64.255220$ | F | F2 (analytic Schur derivation + Bloch fit, $0.01\%$ at smallest $q$) | **F2** |
| L1 | Tabulated long-wave ratios ($c_{T}\approx42.4$, $c_{L}\approx128.0$, $c_{M}=64.26$) at the smallest sampled $q$ | F | F2 for the tabulated ratios; the $q\to0$ limit reading is extrapolation | **F2** (ratios); limit reading **C** |
| D1 | $K_{b}=2$ Bloch rates are biased by $+0.007$ to $+0.021$ vs $K_{b}=4$; $K_{b}=4$ is the in-band cutoff | F | F2 (direct two-cutoff comparison, 9 points) | **F2** |
| K1 | K6-relaxed field shifts $\lambda_{\max}$ by $\le8.2\times10^{-4}$ | F | F2 (direct comparison, 7 points) | **F2** |
| S1 | No positive Bloch rate at the 259 sampled $q$; least-damped non-Goldstone rate $-1.332276$ | E | Evidence-guided (ceiling C); sampled support only; no continuum proof $\to$ | **C** |
| S2 | The relaxed $D_{4}$ wave is Bloch-stable for **all** $q$ in the Brillouin zone | E | No proof; finite sample + smoothness argument only | **UNVERIFIED / ABSTAIN** |

No grade above is raised by external verification, because none was performed for this report.

## 11. UNVERIFIED / ABSTAIN list

- (S2) Bloch stability for all $q$ in the Brillouin zone (continuum claim): **ABSTAIN** — the map is a sample, not a proof.
- A dense ($0.01$-step) 1D-cut map and a full 4D dense map: **NOT RUN** (costed, §9).
- Interval-certified eigenvalue enclosures: **NOT RUN**.
- Stability in a larger box / incommensurate orientations: **NOT RUN** (different calculation; the $2\pi$ box and tuned $q_{0}^{2}=8$ are imposed here).
- Nonlinear (finite-amplitude) stability and nucleation: **NOT RUN** (linear analysis only).
- External audit of this report: **NOT RUN** (via parent agent).
- Singular use: **NOT RUN** (no symbolic step in this task).

## 12. Ledgers

**Parameter ledger** (all from prior files): $r=-0.35$ (measured input, manuscript §II.6/II.7); $m=-0.18$ (convention/fixed mean); $q_{0}^{2}=8$ (tuned onto shell, assumed — D4 band is conditional on this tuning, per programme brief); $u=v=1$ (convention); mobility $1$ (convention); box $L=2\pi$ (convention); $K_{b}=4$ (choice — in-band cutoff, justified by C4b/C5b); $K=4$/$N=18$ relaxation, $K=6$/$N=28$ check (choices, per 4D test); $dt=0.1$, $t_{\mathrm{final}}=40$ (choices; convergence checked by RHS RMS $10^{-15}$ and energy agreement).

**Choice ledger:** Bloch $q$ grid (structured cuts + 150 random points, seed 20261114 — a choice that can change the conclusion is part of the method; the grid is listed in §5 and the CSV); $W$-shift threshold $|W|>10^{-12}$ (sensitivity: omitted row sum $\le8\times10^{-8}$, negligible vs $10^{-3}$ effects); dense sector eigensolves (`numpy.linalg.eigh`, one thread) — second route: symmetry checks C6 and the independent FD/Schur checks; mean-channel defined as max-$n=0$-power eigenvector (weak where power $<0.3$, flagged in §5); frozen ansatz as relaxation start (choice; the relaxed state is the attractor for patterned starts per the 4D test, and the energy/amplitude agreement confirms the same state was reached).

**Assumption ledger:** (i) the relaxed field is the intended $\psi^{*}$ (supported by energy/amplitude agreement with the 4D test, not by an independent derivation of the manuscript's relaxed field); (ii) $q_{0}^{2}$ tuned onto the shell (per brief, the D4 band is conditional on this); (iii) linear stability is the claim — nonlinear behaviour is out of scope; (iv) the $2\pi$ periodic box (no larger-box or rotated-crystal claims).

**Dependency ledger:** R1/G1/M1/L1/D1/K1 depend on the ETD2 solver code (4D test, shared with the target run — I1) and on `numpy` eigensolves; S1 depends on R1+G1 (the base field) plus the sampled grid. If the relaxation were withdrawn, G1/M1/S1 all demote to INCOMPLETE-EVIDENCE.

## 13. Files

Work dir: `~/workspace/research/irh/co-scientist-tasks-2026-11-10/local-independent/task6-bloch-growth/`

- `REPORT.md` — this report.
- `data/bloch_map_Kb4.csv` — 262 rows (259 distinct $q$), $\lambda_{\max}$ and top-6 rates, dominant modes, mean-channel rate/power per $q$.
- `data/bloch_coarse_Kb2.csv` — 48 rows, $K_{b}=2$ map (superseded; sensitivity record only).
- `data/goldstone_overlaps.csv` — 36 rows, Goldstone-branch overlaps at 6 small $q$.
- `data/relaxed_K4.npz`, `data/relaxed_K6.npz` — relaxed field coefficients (6,560 / 28,560 modes).
- `data/relaxation_log.json`, `data/relaxation_trace.csv` — relaxation diagnostics.
- `data/bloch_checks.json` (step-2 checks C1/C2/C3), `data/bloch_checks_Kb4.json` (C1b/C3b/C4b/C5b/C6/fits).
- `figures/bloch_stability_map.png` — (a) $\lambda_{\max}$ vs $|q|$ on cuts, (b) long-wave channels vs $|q|^{2}$ with Schur slope, (c) $K_{b}=4$ vs $K_{b}=2$ axis cut, (d) random-BZ histogram (150 points, max $-1.065$).
- `figures/bloch_longwave_branches.png` — transverse / longitudinal / mean branches on the axis cut.
- `scripts/step1_relax.py`, `scripts/step2_bloch.py`, `scripts/step3_bloch_kb4.py`, `scripts/step3b_bloch_kb4_fast.py`, `scripts/step3c_resume.py`, `scripts/step4_figures.py` — reproducible scripts (pinned seeds: 20261114 for the FD vector and the random-BZ sample; 931 for the unused eigsh $v_{0}$ in step 2).

Nothing in this directory was filed, committed, or written into the manuscript or any repo; no git commands were run in the IRH or Jacobian repos. No browser or Academia use; local compute only.
