# Run-14 manuscript notes (status-note candidates for v94 → v95)

Author: w-rec14e (run 14 end-of-run record commit, Dragon subagent, I1), 2026-11-28. Branch `run14/record-end`, cut from main `374a5104b524fb9839da55717eea611671438bb5`.

**What this file is.** A list of manuscript-facing notes that follow from the four adjudicated run-14 rulings. **None is applied.** No `.tex` or PDF is edited on this branch, and the `paper/v95-draft-2026-11-25` branch is not touched. Every item touching v94 §IX.2 or a major revision waits for the deepest-research gate (Brandon's standing gate, 2026-11-04), and manuscript wording is Brandon's call. Line numbers refer to `programme/v94/IRH_v94.tex` at main `374a5104` (sha256 `e69c95656cc237e09c71256b45f012a776bfaaaa319dea21a13bfb9540975993`). Each item names its source ruling (in `swarm/run14/adj/`) and that file's sha256. Text in quotation marks is copied from the ruling. Grades are those of the rulings; nothing here raises a grade.

**Scope note.** None of the four run-14 rulings proposes a direct `.tex` edit (a `grep` of the rulings for "manuscript", "erratum", "v95" and "status note" finds only the "I edit no repo or manuscript" disclaimers). The items below are the ruling-named wordings (for the ToE bar, the RUN14 report and record citations) that any v95 status note on the same topic should follow, plus citation hygiene. They are candidates only.

## 1. Dimensional reading (C), K-B2–K-B4 — a-kbc

Source: `a-kbc_RULING.md`, sha256 `7322cc93726c2e51a979c439bcc2da94f1471f6be5edeb04d900086383520bda`. v94 §IX.2 (l.940–950) is unchanged and deepest-research gated.

- **Citation hygiene (X1 / R3).** "v94 §IX.2 item (C) is at l.947 (sha e69c9565…); l.948 is `\end{itemize}`." Any v95 text or note citing the (C) item by v94 line number should cite l.947. (`git grep` finds no "l.948" on `paper/v95-draft-2026-11-25`.)
- **(B) cost list, l.946 (pointer).** v94 l.946 says (B) "predicts Kaluza–Klein modes". Under the working reading (C), K-B3 is MOOT: the KK table "stays scoped substrate numbers", and its T6-falsifier role passes to requirement R6.1 for any (C) construction (a-kbc §1, §7). This adds to the run-13 RF-3/RF-4 candidates for l.946/l.950 in `RUN13_MANUSCRIPT_NOTES.md` §2; it is not a new erratum.
- **Gauge sector / reading-independence (R1, §4).** If v95 states which gauge results are reading-independent, use the ruled split: "K-B4a — no local (gauge) redundancy in the v94 $F$ or its evolution laws, tested by Noether second-theorem identities — is reading-independent. The type of an elasticity (fracton) dual, abelian and noncompact, is reading-independent wherever the duality applies; its applicability (inertial physical time, γ→0, crystal elasticity in the low-energy sector; H2a) and the emergent non-abelian gauge question K-B4c (H1–H3) are reading-dependent." No result is established yet (G-A33–G-A35 OPEN, no grade).
- **Common-speed lemma (§3, R5).** If v95 cites the phonon-sector obstruction: lemma "minor-symmetric $C_{ijkl}$ in $d$ dimensions with $\Gamma_{ik}(n)=c^2|n|^2\delta_{ik}$ ⇒ isotropic, $\lambda=-\mu=-c^2$, $C_{iijj}=d(2-d)c^2$" at B [MV]4D / F2 / I1; the instability is "against homogeneous dilation, contradicting the measured $K>0$ of the relaxed crystal" (X7), not against clamped finite-wavelength phonons; the application to "all gapless $m=0$ modes share one speed" is C/F3/I1.
- **Chirality / Nielsen–Ninomiya (X5, R4).** "NN premise applicability to a 4-spatial-dimensional lattice is not established; under H2a 3+1 chirality is not defined at lattice level." Kaplan (PLB 288 (1992) 342) is a lead only (abstract read, body CANNOT CHECK). No v94 line carries NN text (`grep -i nielsen` on v94: 0 hits); recorded for completeness.

## 2. Nucleation / $D_4$ selection at $L=5\pi$ — a-gd3c

Source: `a-gd3c_RULING.md`, sha256 `ca0aebed68bdfe07675685e861eff8f570aff0d9de409187028994a6edb78856`. v94 §IX.5.2 (G-D3) and §II.9 l.641 state no nucleation mechanism.

- **Status-note wording (RF2, ToE bar T1.1).** "$D_4$ (up to rotation among the 97 shell subsystems) is selected at $L=5\pi$, P1, 80/80 over two routes (F2/I1). At P2 the fraction is 0.975 per route ('mixed' at frozen n=40). Under prior U\* (Dragon's choice, swappable) the 62-point sliver label is 'selects $D_4$' (F2/I1). The only competitor is $2.14\times10^{-3}$ above $D_4$. T1.1 stays PARTIAL: box-scoped, three box sizes, no infinite-volume claim."
- **Prior sentence (RF3).** Every pooled rate must carry "under prior U\* (Dragon's choice, swappable)". Do not write "D4 is selected on the sliver" without it. The prior is Dragon's choice under Brandon's 2026-11-27 delegation (`coord/D-1403-prior.md`, sha256 `a6f9be78abaf…`); a manuscript may swap it, using the per-point table (P1 1.0, P2 0.975, S0–S3 1.0).
- **Do not cite** "$D_4$ dynamically selected" without the box scope; no infinite-volume statement is established. Member-type ordering at $N=32$ (including "star highest") is grid aliasing (C/I1).

## 3. Projection / icosahedral signature S2 — a-ga12s2d

Source: `a-ga12s2d_RULING.md`, sha256 `b9b422d9fc19516fdab9ad82dc2234e87f693bc0539189997af6e607e610863a`. v94 §II.10 / §IX.1.5 (G-A12).

- **Status-note wording (ToE bar T1.3).** "93.769% certified (C/I1), 0 U leaves; ball cover 11/13 charts tiled (F3/I1); tier status unchanged (PARTIAL)." The coverage figure is the run-13 measurement; run 14 gives only the frozen bound [0.93769, 0.93771]. Any "96.769%" is a transcription error.

## 4. G-E5 ($p=5$) — a-ge5

Source: `a-ge5_RULING.md`, sha256 `86692787cb0eb90e55e9b2c4e6f357821a546fc461b1920d86e3d3485a0452a9`. G-E5 is Jacobian-conjecture work, not IRH physics; no v94/v95 note follows. If a Jacobian paper cites it: "$\deg\bar V$ undetermined, $9171\le\deg\bar V\le40959$ (C/I1); E0–E7 alone cannot certify a section; E5 at D=10 cuts the mixed chart; the cover is incomplete on $\{\alpha=0\}$ and 68 mixed charts" (RF-3).
