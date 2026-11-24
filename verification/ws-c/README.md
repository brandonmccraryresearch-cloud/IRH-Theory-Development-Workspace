# WS-C substrate-convergence code (provenance import, run 12)

Imported 2026-11-23 by run-12 author w-p0code under EXP-1200 (R-CODE, G-B2).

**Source (shipped package):** `d4-work-2026-11-10.zip`
(sha256 `e9acec99c808aa9d30965009a5b9122b9eaf3c908c32e9602265eaa1d34522e9`),
folder `d4-work-2026-11-10/ws-c-substrate-convergence/{code,results,figures}`.
The same bytes sit in the local WS-C deliverable
`~/workspace/research/irh/co-scientist-tasks-2026-11-10/ws-c-substrate-convergence/`.
Every file in the import commit is byte-identical to the zip member
(sha256 compared file by file; list in `SHA256SUMS.import`).

Not imported: `results/task1_q1_final.npy` (1 MB raw field; not read by
`make_figures.py`) and `__pycache__/`.

The reports that use this code are in
`programme/workstreams/ws-c-substrate-convergence/`.
Any change after the import commit is a run-12 artifact fix and cites EXP-1200.
Run from this folder's `code/`; scripts write to `../results` and `../figures`.

## Run-12 fix G-B2 (EXP-1200): regenerating fig 3

`task2d_transient.py` now loops over T in (5, 0.5, 1.0) and writes all 12
rows of `results/task2_transient.csv` (plus an `amp_raw` column), so

    cd code && python task2d_transient.py && python make_figures.py

regenerates the T=0.5/1.0 rows in-script and `make_figures.py` no longer
crashes. Rounding note: the shipped T=0.5/1.0 rows' `err_vs_Astar` was
evidently computed from the unrounded amplitude, while the script (shipped
and fixed) subtracts after rounding to 6 decimals; this gives 1e-6
differences in two `err_vs_Astar` cells (T=1.0, dt=0.02 and dt=0.0025).
The `seconds` column of the shipped T=0.5/1.0 rows is 0 (not produced by the
shipped script). Evidence: run-12 w-p0code OUTPUTS.md.

## Run-13 fix T-L167 (EXP-1306): active-triad lock metric in `make_analyzer`

`irh_models.make_analyzer`'s `analyze` (formerly l.167) averaged cos S over
all 32 closed triads, including modes at roundoff amplitude, so `lock` was
platform-dependent for partial patterns (same defect as WS-A G-B3 / Hark F2).
`lock` is now the mean over triads whose three modes are all active
(`mag > 0.5*mag.max()`, the `modes` criterion; NaN if none); the old value is
kept as `lock_all`, and `n_lock_triads` counts the active triads. Full
24-mode states are unchanged (all 32 triads active). The shipped
`results/*.csv` files were NOT regenerated: their `lock` column is the old
all-triad metric (for partial patterns, e.g. A5/A6 and the 6-mode quenches,
it is the roundoff-dependent value). Evidence: run-13 w-art OUTPUTS.md.
