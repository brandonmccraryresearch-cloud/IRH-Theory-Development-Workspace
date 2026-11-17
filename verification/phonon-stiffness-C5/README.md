# Correction C5 — equilibrium edge-field rerun (2026-11-14, local CPU, $0)

The local Task 8 dislocation calculation used the trial field
$u = (b/2\pi)\theta$ for the edge part. That field is not the
equilibrium field of the phase-only elastic energy ($\lambda = \mu$,
$\nu = 1/4$); its edge energy is $3/2$ too high. This rerun
(`task8_stiffness_C5.py`, a copy of `task8_stiffness.py` with the
dislocation section switched to the Volterra equilibrium edge field)
re-establishes the corrected edge leg:

- Equilibrium edge/screw factor $4/3$ (not $2$), verified by direct
  numerical angle-averaging of the Volterra field (rel. error
  $< 2\times10^{-16}$ on five Burgers vectors).
- $K_{\mathrm{edge}} = (256/3) A_*^2 |b|^2 / \pi$; elementary
  $0.490385 \to 0.326923$; $r_0^{\mathrm{edge}} = 1.846249\,|b|$
  (was $2.261184\,|b|$); $E/A(R=20)$ elementary edge $0.899008 \to
  0.665617$; edge $R^*$ rescaled by $\sqrt{2/3}$ ($16.62 \to 13.57$,
  $12.79 \to 10.44$, $23.91 \to 19.52$, $19.19 \to 15.67$).
- Screw values identical to the original run.
- $|b|^2 = 4$ bound state survives (margin $K_e \ln 2 = 0.226606$).
- One split verdict flips: $|b|^2 = 10$ edge at $R = 20$ goes from
  No to Yes ($E/E_{\mathrm{elem}}$ $2.8052 \to 3.0238$, crossing
  $n_{\min} = 3$; $R^*$ $23.91 \to 19.52 < 20$). The other nine
  edge/screw split verdicts at $R = 20$ are unchanged. The audit
  consequence "split verdicts at $R=20$ unchanged"
  (`COMPARISON_task8.md` §B) is therefore wrong for this one case;
  see the correction note there and `REPORT.md` correction C5.

Full record: `REPORT.md` §5/§8/§10 + withdrawal notes (correction
C5), in the Task 8 directory
(`local-independent/task8-phonon-stiffness/`); the audit
`COMPARISON_task8.md` open item O-T8-1 is marked DONE there.

The corrected coefficients are the ones decided at Track E B /
Track F F2 in IRH v94 (2026-11-14). The manuscript's local edge leg
stays at INCOMPLETE-EVIDENCE until this rerun's log + hash are
committed here — which this deposit does (hashes in `SHA256SUMS.txt`).
