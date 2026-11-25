# AI-authorship-tell self-audit: v94 vs v95 draft

Counted by script over the document body (from `\begin{document}` to the bibliography; bibliography `\textbf` volume numbers excluded). Script inline in the audit run; method: regex counts, math replaced by a token before sentence statistics.

| marker | v94 | v95 draft |
|---|---|---|
| `\textbf` in body | 239 (319 incl. bibliography) | 0 (only journal volume numbers in the bibliography) |
| `itemize` environments | 3 | 0 |
| `enumerate` environments | 1 | 0 |
| `\item` | 42 | 0 |
| `\expansion{}` side-boxes | 26 | 0 (folded into the derivations) |
| `\boxed` | 3 | 0 |
| em-dashes (`---` or `—`) | 103 | 0 |
| ALL-CAPS labels (DERIVATION, PREDICTION, EXCLUDED, VERDICT, CONFIRMED) | 54 | 0 (small-caps labels, used sparingly) |
| filler words (moreover, furthermore, notably, crucial, robust/robustness, delve, landscape, pivotal, seamless, leverage, underscore, tapestry, importantly, in conclusion, it is worth noting, comprehensive, intricate, holistic, realm, showcase, navigate, foster) | robustness ×5 | 0 (last "robustness" reworded) |
| mean sentence length (words) | 23.7 | 21.5 |
| sentence-length std. dev. | 18.0 | 14.5 |

Other checks done by reading, not by count: no rule-of-three cadences left in the abstract or assessment that were not lists of three actual things; first person plural "we" throughout; definitions placed before each chain of algebra (shells, designs, $T$, $Q$, $\tau$, $q_4$, $r_{\rm eff}$, $u_{\rm eff}$, Lamé constants, OS condition, reflected kernel); AI mentioned only in the final "A note on assistance".

Residual tells to watch on Brandon's read: the abstract is long (two paragraphs), and some status sentences in §18 keep a "X is partial … Y is open" rhythm because they follow the ToE-bar tiers one by one.

## Prose second pass (2026-11-25): the 14 regex heuristics of PROSE_CHECKLIST.md §B

Script `validation/ai_tell_heuristics.py` (body from `\begin{document}` to the bibliography, comments removed, math replaced by a token; heuristic 10 run on the raw text with displays and tabulars removed, so table cells starting with `$` are not counted).

| # | heuristic | before (8357443) | after |
|---|---|---|---|
| 1 | bold (`\textbf`, `**`) | 0 | 0 |
| 2 | list lines | 0 | 0 |
| 3 | bold-header list items | 0 | 0 |
| 4 | em-dashes | 0 | 0 |
| 5 | excess vocabulary | 0 | 0 |
| 6 | significance inflation | 0 | 0 |
| 7 | stock hedges | 0 | 0 |
| 8 | trailing participle tail | 0 | 0 |
| 9 | paragraphs with ≥2 tricolons | 4 | 4 |
| 10 | sentence starts with a symbol | 1 | 0 |
| 11 | empty assurance (clearly, trivially, …) | 1 | 0 |
| 12 | "we have that" | 0 | 0 |
| 13 | symbolic logic in prose | 0 | 0 |
| 14 | bare "eq. (n)" references | 0 | 0 |

Body words ≈12,255 before, ≈12,544 after. The four tricolon paragraphs (§6.2 odd-sector test, §13.2 reflected kernel, Appendix A "This edition adds", Appendix B protocol) were read and kept: each list names actual distinct items (three test points, three residue quantities, the frozen protocol's three conditions), not cadence. By reading: every `\eqref` now has a noun phrase before it; all displays end in punctuation or continue the sentence.
