# verification/lean-ka — K-A (G-A27): the Swift–Hohenberg fluctuation measure is not reflection positive

Run 13, EXP-1314 (K-A), adjudicated by a-ka on 2026-11-25 (ruling `run13/adj/a-ka_RULING.md`, sha256 `986b7de9c37764c205fdd3a5772f2e6129d378bf53ea5076fb24743f444f0a93`). Gap G-A27 is **CLOSED-scoped** in `programme/IRH_GAP_INVENTORY_2026-11-12.md`. All files here are copied verbatim from the run tree; their sha256 values are in `MANIFEST.sha256`. Nothing was edited.

## What is kernel-checked

`KA.lean` (author w-ka) proves, with axioms ⊆ {propext, Classical.choice, Quot.sound} and no `sorry`:

- `G_strictMonoOn`, `G_hasDerivAt`, `G_deriv_pos` — $G(s)=1/(r+(q-s)^2)$ is strictly increasing on $[0,q)$ for $r>0$;
- `stieltjes_antitone`, `no_KL` — a positive Källén–Lehmann/Stieltjes form $G(s)=\int\rho(dm^2)/(s+m^2)$ is antitone, so none exists for $G$;
- `Ghat_at_pi`, `Ghat_neg`, `Ghat_zero_pos` — the closed-form reflected kernel $\hat G(\alpha,\beta,x)$ is negative at $x=\pi/\alpha$ and positive at $x=0$, for all $\alpha,\beta>0$;
- `rp_diag`, `Ghat_not_rp` — the $n=m=1$ Osterwalder–Schrader condition fails for that kernel.

`verifier/VKA.lean` (verifier v-ka) restates the theorem types exactly and adds an independent $K$, `Ghat_eq`, `K_not_rp` and `RO_sign` (the planted "+"-sign claim P13-O is false).

Must-fail controls: `KACtrl.lean` (author) and `verifier/VKACtrl1.lean` (R-O "+" sign), `VKACtrl2.lean`, `VKACtrl3.lean` (verifier). Each exits with EXIT=1, as required.

## What is NOT formalised (grade [MV]4D, not 4K)

- The Fourier/residue identity $\hat G(k_\perp,x)=\pi e^{-\beta x}(\alpha\cos\alpha x+\beta\sin\alpha x)/(2\alpha\beta(\alpha^2+\beta^2))$, $(\alpha+i\beta)^2=q_0^2-|k_\perp|^2+i\sqrt r$. It was checked by CAS only: SymPy 1.14.0 and Wolfram 15.0 (author), PARI/GP 2.15.2 and Wolfram (verifier). The optional scripts are in `crosscheck/`.
- The $\epsilon,\delta$ limit from the closed form to a 4D test function (Theorem A assembly). This is a hand step on a closed ledger.

The crystal-phase result (lattice-regularised $F_h$, site reflection along $e_4$ and $(1,1,0,0)/\sqrt2$, F2/I1) is numerical. Its codes are **not** in this folder; they stay in the run tree (`swarm/run13/w-ka/`, `swarm/run13/v-ka/`).

## Toolchain

- Lean 4.34.0 (x86_64-unknown-linux-gnu, commit `293d5d0c0c3f3dded4688b3ccd6a33939ac5102b`, Release), lean binary sha256 `e8baaa71855a616dc351028f3ad2200051b0671f423a1696a100e809302d5550`.
- Mathlib rev `5ed2965256430c3649e86755f9576b54eca72435`, prebuilt oleans via `LEAN_PATH`. No lakefile is provided here.
- Plain `lean`, `-j1` / `LEAN_NUM_THREADS=1`, `ulimit -v 16000000`.
- Build order: `KA` first; `KACtrl`, `verifier/VKA`, `verifier/VKACtrl1–3` each import `KA` only.

## Build logs (run tree, sha256)

| log | sha256 |
|---|---|
| author `w-ka/vm/logs/lean_KA_t3.log` (EXIT=0) | `354621ed01b16ea90d8df258125b0704aed87bdcdc41ad5c44f8c10b47f099ca` |
| author `w-ka/vm/logs/lc_KA_t3.log` (leanchecker, EXIT=0) | `e03b882432820d8e95a29f1a82f6efb444964ed8e88dd13189d4988603d1a8c0` |
| author `w-ka/vm/logs/lean_KACtrl_t3.log` (must fail, EXIT=1) | `70378f5216e58b3ce31249fa0b84ce248bd8fd9ee2b24db0569089e0fea5e7ca` |
| verifier `v-ka/logs/lean_KA_v1.log` (fresh rebuild, EXIT=0) | `8e419df869cadfda6c96f923091f2d228c4aafec3df2cc54987463837911ccae` |
| verifier `v-ka/logs/lean_VKA_v1.log` (EXIT=0) | `1c828c65b0a4d85063d039a23987e3533cd41988b8e990f5c81a500c1f348265` |
| verifier `v-ka/logs/lc_KA_VKA_v1.log` (leanchecker, EXIT=0) | `37d3acd691a91e10dd6ddb7f7580cff0ec3b5cab90d8bbe28776a28de39108a8` |
| verifier `v-ka/logs/lean_VKACtrl1_v1.log` (must fail) | `0e56210af4844712be7eb14f673dc698dd2584aa30ddf2d8a098d57a903f0f98` |
| verifier `v-ka/logs/lean_VKACtrl2_v1.log` (must fail) | `f23d196c3bee6b0a88f3b5886596afd61bebbad0a19769a7e301b517bf428782` |
| verifier `v-ka/logs/lean_VKACtrl3_v1.log` (must fail) | `b904f32550d4558da30053781740f2f2ff378727ac21dc3e73418b951d3aaadb` |

Oleans and logs are not committed.

## Layout

| path | what | provenance |
|---|---|---|
| `KA.lean` | core lemmas (10 theorems) | w-ka (author) |
| `KACtrl.lean` | must-fail control | w-ka |
| `verifier/VKA.lean` | independent restatement + `K_not_rp`, `RO_sign` | **v-ka (verifier)** |
| `verifier/VKACtrl1.lean`, `VKACtrl2.lean`, `VKACtrl3.lean` | must-fail controls (Ctrl1 = planted R-O "+") | **v-ka** |
| `crosscheck/ka_exact.py`, `crosscheck/ka_exact.wls` | author CAS checks of the residue identity and the sign | w-ka (optional) |
| `crosscheck/vka_exact.gp`, `crosscheck/vka_exact_v3.gp`, `crosscheck/vka_exact.wls` | verifier PARI/GP and Wolfram checks | v-ka (optional) |

## Grade (from the a-ka ruling; this commit changes no grade)

- Core lemmas: **B [MV]4K F1/I1**.
- Fourier/residue identity and the $\epsilon,\delta$ assembly: **B [MV]4D F1/I1**. So Theorem A (the disordered SH measure on $\mathbb R^4$ is not RP, in every direction) is B [MV]4D F1/I1, its weakest premise being 4D.
- Independence I1: every agent is of the same model family, and the same Lean binary was used.
- No continuum crystal RP claim is made either way. That residue is filed as a new open gap in the inventory.
