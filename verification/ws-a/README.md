# WS-A core-computations code (provenance import, run 12, partial)

Imported 2026-11-23 by run-12 author w-p0code under EXP-1200 (R-CODE, G-B3, G-B4).

**Source (shipped package):** `d4-work-2026-11-10.zip`
(sha256 `e9acec99c808aa9d30965009a5b9122b9eaf3c908c32e9602265eaa1d34522e9`),
folder `d4-work-2026-11-10/ws-a-core-computations/`. Same bytes in
`~/workspace/research/irh/co-scientist-tasks-2026-11-10/ws-a-core-computations/`.
Only the files needed for G-B3 (`d4model.py`, `task5_basin.py`, `task5.log`,
`tables/task5_basin.json`, `figures/task5_basin.png`) and G-B4
(`task1_projections.py`, `tables/task1_*.json/csv`, `figures/task1_*.png`) are
imported; each is byte-identical to the zip member (`SHA256SUMS.import`).

Run from this folder (scripts use `sys.path.insert(0, ".")` and relative
`tables/`, `figures/` paths). Reports: `programme/workstreams/ws-a-core-computations/`.
Any change after the import commit is a run-12 artifact fix and cites EXP-1200.

## Run-12 fix G-B3 (EXP-1200): active-triad lock metric

`d4model.ModelB.analyze` now returns `lock` = mean cos S over triads whose
three modes are all active (`mag > 0.5*mag.max()`, the `ndom` criterion);
the shipped all-32-triad value is kept as `lock_all`, and `n_lock_triads`
counts the active triads. Patterns with no active triad (sq4, sq8) get
`lock = NaN` (undefined) instead of a roundoff-dependent number.
Not changed in run 12: WS-C `irh_models.make_analyzer` (l.167) carried the
same all-triad metric; it was outside EXP-1200's G-B3 scope and was recorded
as an open item in run-12 w-p0code CHANGES.md. Run 13 (EXP-1306 T-L167)
applies the same active-triad fix there; see `../ws-c/README.md`.
Run 13 (EXP-1306 T-B3) also states the active threshold in the
`analyze` docstring (code unchanged).

## Run-12 fix G-B4 (EXP-1200): task-1 JSON re-shipped from the current script

`tables/task1_projections.json` is now the output of the shipped
`task1_projections.py` (unchanged script), regenerated on lean-build-4
(conda env `jacobian-conjecture-2d`, NumPy 2.4.6) in run 12. The 2026-11-10
shipped file is kept verbatim as `tables/task1_projections.shipped-2026-11-10.json`.

Revision note. Leaf-by-leaf comparison: **0 numeric differences**; 14 keys
exist only in the shipped file -- `n_distinct_positions` and
`max_multiplicity` for each of the 7 directions -- which the current script
does not write (they came from another script revision):

| direction | n_distinct_positions | max_multiplicity |
|---|---|---|
| e4 (0,0,0,1) rational | 485 | 5 |
| d110 (1,1,0,0)/sqrt2 rational | 339 | 7 |
| d1111 (1,1,1,1)/2 rational | 485 | 5 |
| d1110 (1,1,1,0)/sqrt3 rational | 819 | 3 |
| phi1 (1,phi,0,0) irrational | 1465 | 1 |
| phi4 (1,phi,phi^2,phi^3) irrational | 1465 | 1 |
| sqrt (1,sqrt2,sqrt3,sqrt5) irrational | 1465 | 1 |

These values are carried only by the shipped file; run 12 did not recompute
them. `task1_slice_peaks.csv` and `task1_bragg.csv` regenerate byte-identical.
The regenerated task-1 PNGs differ in bytes and were not re-shipped.

Note on G-B3 and `tables/task5_basin.json`: re-running `task5_basin.py` with
the fixed `analyze` leaves every field of the hex6, fcc12 and four full-pattern
cases unchanged; only `lock` changes, in the six noise-seed cases (decayed
states, rms 0) and sq4/sq8 (no active triad -> NaN). The shipped JSON is kept
as shipped; the run-12 comparison is in w-p0code OUTPUTS.md.
