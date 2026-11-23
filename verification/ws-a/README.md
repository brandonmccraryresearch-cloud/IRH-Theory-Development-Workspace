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
Not changed: WS-C `irh_models.make_analyzer` (l.167) carries the same
all-triad metric; it is outside EXP-1200's G-B3 scope and is recorded as
an open item in run-12 w-p0code CHANGES.md.
