# Verification audit

**Date:** 9 November 2026. **Purpose:** distinguish checks performed in this comparison from numerical and formal-verification results reported by McCrary v93.1.

## 1. Independent exact enumeration — executed

Constructed the roots $\pme_{i}\pme_{j}$ for i<j using integer tuples. For the 3D BCC crystal this is its 12-vector reciprocal star; for $D_{4}$ it is its 24-vector root star.

For each star, a counter stores the multiplicity C(s) of every ordered pair sum. Then:

- $T = \Sigma$ over root c of $C(-c)$, counting ordered zero-sum triples.
- $Q = \Sigma$ over sums s of $C(s)C(-s)$, counting ordered zero-sum quadruples.
- $\tau^{2}=T^{2}/N^{3}$, $q_{4}=Q/N^{2}$, $S=T^{2}/($NQ), evaluated as exact rational numbers.

| Star | N | T | Q | $\tau^{2}$ | $q_{4}$ | S |
|---|---:|---:|---:|---:|---:|---:|
| BCC reciprocal star (3D) | 12 | 48 | 540 | 4/3 | 15/4 | 16/45 |
| $D_{4}$ root star (4D) | 24 | 192 | 3384 | 8/3 | 47/8 | 64/141 |

**Outcome:** matches S0 §§II.3–5 and II.8. With the manuscript'$s A_{4}$* score 12/31, the relative advantage is exactly (64/141)/$(12/31)-1=73/423\approx17.26$%. The $A_{4}$* enumeration itself was not rerun. This verifies discrete counting and score arithmetic, not global field minimization or physical selection.

## 2. Deposit inspection — performed

[Zenodo record API](https://zenodo.org/api/records/22821689) identifies v93.1 as an open CC BY 4.0 preprint, publication date 18 September 2026. The supplied PDF itself is dated 17 September.

The record lists:

- `IRH_v93_1.pdf`: 1,839,188 bytes; MD5 952116b3154824e3a19fcdc558898c5f.
- `IRH_v93_1_source_package.zip`: 3,202,228 bytes; declared MD5 11a90f9a82d97652112c07608513316f.

The source ZIP was downloaded temporarily and its entire filename inventory inspected. It contains:

| Contents | Count / names |
|---|---|
| Figures | `figs/fig01.png` through `figs/fig10.png` |
| Manuscript formats | `IRH_v93_1.pdf`, `IRH_v93_1.tex`, `paper_v931.md` |
| References | `references.md` |
| Conversion utility | `md2tex.py` |

There are **no scientific simulation scripts, .lean files, Lake/toolchain manifests, raw field data or seed manifest in this archive**. The Python filename is a manuscript-conversion utility, not the simulation implementation. File hashes above are metadata values, not independently recomputed checksums.

The PDF's separate [Independent Verification Data link](https://drive.google.com/file/d/1Sxkginzo_UmNrNETfunLK8_XUq4tbuXb/view) returned “Sign in” through the attempted access method. Its underlying contents were not inspected. This does not establish that access is impossible by every route or that the artifacts do not exist elsewhere.

## 3. Manuscript reading and visual checks — performed

Read all 31 pages through the workspace PDF reader. Viewed pages 7 and 10 as printed to check the exact lattice scores, reciprocal-label convention, detuning table and energy comparison. Reported percentages and other prose results are attributed to their sections in the matrix rather than presented as newly reproduced measurements.

## 4. External source checks — performed

| Source ID in matrix | Material actually checked | Use |
|---|---|---|
| S2: Elitzur et al. | arXiv full HTML, especially §§2–4 | Shared cubic-invariant assumptions; regular-polytope restriction; 4D special case |
| S3: Groh & Mulder | AMOLF institutional abstract | Near-spinodal preference does not fix final stable crystal |
| S6: Hoy | arXiv abstract and full HTML, Methods/Results | 500,000-particle system; LJ/WCA control; $D_{4}$ identification; 648-particle historical footnote |
| S7: van Meel et al. | Abstract/search summaries | Frustration and suppressed crystallization; no detailed numerical extraction used |
| S8: de Laat et al. | arXiv abstract and full HTML through §5 | Exact kissing result; Julia/Nemo implementation described; objective scope |
| S9: Cohn et al. | arXiv abstract | Non-universal optimality specifically for a spherical code |
| S1, S4, S5 | References and descriptions in supplied manuscript | Historical baseline and model ingredients; not independently full-text audited |

All references were selected from the supplied paper's bibliography; the search was targeted, not systematic. An initial Academia search found the seed paper but no useful additional direct comparator, so primary arXiv/institutional sources were used.

## 5. Not performed

No time integration, phase-diagram reconstruction, particle dynamics, Lean compilation, full source-code review of the comparator implementations, or empirical test of the substrate interpretation. No new simulation percentages or error bars were generated. The comparison's proposed tests are proposals, not completed experiments.

**Reproduction boundary:** exact combinatorics confirmed here; kinetic and proof-build claims remain manuscript-reported pending access to their scientific artifacts.
