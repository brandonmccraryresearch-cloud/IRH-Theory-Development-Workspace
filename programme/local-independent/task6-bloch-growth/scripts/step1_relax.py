#!/usr/bin/env python3
"""Step 1 (Task 6): re-relax the frozen 24-mode D4 ansatz to a mean-constrained
stationary full field, by Model B (ETD2) integration, reusing the 4D field-test
solver (run_field_study.py, Field + integrate) as the prior source.
Frozen ansatz: psi0 = m + A * sum_{s in S} exp(i s.x), A = larger root of
alpha - 8*beta*A + 141*A^2 = 0, alpha=0.1072, beta=1.54, m=-0.18.
Targets from the 4D field test (independent run, same physics):
  relaxed excess energy K=4: -0.007726209285 ; K=6: -0.007727623601
  relaxed star amplitude: 0.07767566612344486 (six_1pct_full_noise_00 final)
  final RHS RMS <= ~1.2e-15 (their stationary endpoints)
Outputs: data/relaxed_K4.npz (compact Fourier coeffs of phi=psi-m),
         data/relaxed_K6.npz, data/relaxation_log.json, data/relaxation_trace.csv
Seed: none (deterministic, no noise added).
"""
import os
for k in ('OMP_NUM_THREADS', 'OPENBLAS_NUM_THREADS', 'MKL_NUM_THREADS'):
    os.environ[k] = '1'
import importlib.util, itertools, json, sys, time
from pathlib import Path
import numpy as np

BASE = Path('/home/hatch/workspace/research/irh/co-scientist-tasks-2026-11-10')
WORK = BASE / 'local-independent/task6-bloch-growth'
FIELD_SRC = BASE / '4d-field-test/run_field_study.py'

spec = importlib.util.spec_from_file_location('field_study', FIELD_SRC)
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)

A_FROZEN = (8 * 1.54 + np.sqrt((8 * 1.54) ** 2 - 4 * 141 * 0.1072)) / 282
print('A_frozen =', repr(float(A_FROZEN)), flush=True)

def compact_coeffs(m, y):
    """Full Fourier dict k->a_k for phi, from the rfft array y (norm forward)."""
    out = {}
    n, K = m.n, m.cutoff
    for k in itertools.product(range(-K, K + 1), repeat=4):
        if k == (0, 0, 0, 0):
            continue
        if k[3] >= 0:
            out[k] = complex(y[tuple(k[i] % n for i in range(3)) + (int(k[3]),)])
        else:
            kk = tuple(-x for x in k)
            out[k] = complex(y[tuple(kk[i] % n for i in range(3)) + (int(kk[3]),)].conjugate())
    ks = np.array(sorted(out.keys()))
    vals = np.array([out[tuple(k)] for k in ks])
    return ks, vals

def relax(cutoff, n, tfinal, dt=0.1, y0=None, tag=''):
    m = mod.Field(n, cutoff)
    if y0 is None:
        y = m.from_compact(mod.KSTAR, np.full(24, A_FROZEN))
    else:
        y = y0
    t0 = time.perf_counter()
    yf, rows, shell, spectra, stats = mod.integrate(m, y, dt, tfinal)
    el = time.perf_counter() - t0
    N, E = m.evaluate(yf)
    d, spec_arr, a = m.diagnostics(yf, N, E)
    ks, vals = compact_coeffs(m, yf)
    print(f'[{tag}] K={cutoff} N={n} t={tfinal} elapsed={el:.1f}s accepted={stats["accepted_steps"]} '
          f'rejected={stats["rejected_steps"]} energy={E:.15f} rhs_rms={d["rhs_rms"]:.3e} '
          f'star_amp_mean={np.abs(a).mean():.15f} star_amp_cv={d["amplitude_cv"]:.3e} '
          f'mod_power={d["modulation_power"]:.15f}', flush=True)
    return dict(ks=ks, vals=vals, energy=float(E), rhs_rms=float(d['rhs_rms']),
                star_amp=float(np.abs(a).mean()), star_cv=float(d['amplitude_cv']),
                elapsed=float(el), stats=stats, trace=rows, shell_power=float(d['shell_power']))

log = {}
# K=4 relaxation from the frozen ansatz, t=40 (star-mode rate ~2.7 => tau~0.4; harmonics ~1e3)
r4 = relax(4, 18, 40.0, tag='K4')
np.savez(WORK / 'data/relaxed_K4.npz', ks=r4['ks'], vals=r4['vals'],
         energy=r4['energy'], rhs_rms=r4['rhs_rms'])
log['K4'] = {k: r4[k] for k in ('energy', 'rhs_rms', 'star_amp', 'star_cv', 'elapsed')}
log['K4']['stats'] = r4['stats']
log['K4']['frozen_A'] = float(A_FROZEN)
log['K4']['targets_4d_report'] = dict(energy=-0.007726209285, star_amp=0.07767566612344486,
                                       rhs_rms_max=1.21e-15)
# K=6 relaxation: start from K=4 relaxed coefficients embedded in the K=6 band
m6 = mod.Field(28, 6)
y6 = m6.from_compact(np.array([tuple(k) for k in r4['ks']]), r4['vals'])
r6 = relax(6, 28, 40.0, y0=y6, tag='K6')
np.savez(WORK / 'data/relaxed_K6.npz', ks=r6['ks'], vals=r6['vals'],
         energy=r6['energy'], rhs_rms=r6['rhs_rms'])
log['K6'] = {k: r6[k] for k in ('energy', 'rhs_rms', 'star_amp', 'star_cv', 'elapsed')}
log['K6']['stats'] = r6['stats']
log['K6']['targets_4d_report'] = dict(energy=-0.007727623601,
                                       star_amp=0.07767566612344486)
# trace of K4 run
import csv
with open(WORK / 'data/relaxation_trace.csv', 'w', newline='') as f:
    rows = r4['trace']
    w = csv.DictWriter(f, fieldnames=list(rows[0])); w.writeheader(); w.writerows(rows)
(WORK / 'data/relaxation_log.json').write_text(json.dumps(log, indent=2))
print(json.dumps(log, indent=2))
