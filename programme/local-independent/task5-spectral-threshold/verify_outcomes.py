#!/usr/bin/env python3
"""Independent verification of threshold outcomes (second tool path).

Deliberately does NOT import run_threshold.py. It re-derives every
classification from the saved per-run NPZ checkpoints (compact initial
and final Fourier coefficients) with a fresh, minimal implementation:
direct scipy rfftn/irfftn evaluation of the same functional
(alpha=0.1072, beta=1.54, q0^2=8, mean=-0.18), star coefficients read
straight from the rFFT array, triad locking over the 32 unordered
zero-sum triads, occupancy/CV/lock/RHS-RMS rules as in the pilot.
It then compares each recomputed outcome with threshold_outcomes.csv
and writes verify_outcomes.csv + a PASS/FAIL verdict per run.
"""
import csv, itertools, json
from pathlib import Path
import numpy as np
from scipy.fft import rfftn, irfftn, fftfreq, rfftfreq

ALPHA = 0.1072
BETA = 1.54
N = 18
K = 4
KSTAR = np.array([k for k in itertools.product([-2, 0, 2], repeat=4)
                  if sum(x * x for x in k) == 8])
TRIADS = np.array([t for t in itertools.combinations(range(24), 3)
                   if np.all(KSTAR[list(t)].sum(axis=0) == 0)])

# rFFT wavevector grids
q = [np.rint(fftfreq(N) * N).astype(int)] * 3 + \
    [np.rint(rfftfreq(N) * N).astype(int)]
coords = np.meshgrid(*q, indexing='ij', sparse=True)
k2 = sum(x * x for x in coords)
mask = np.ones_like(k2, dtype=bool)
for x in coords:
    mask &= abs(x) <= K
mask[(0,) * 4] = False
L = ALPHA + (8.0 - k2) ** 2
weight = np.broadcast_to(np.where((q[3] == 0) | (q[3] == N // 2), 1., 2.),
                         k2.shape)


def star_coeffs(y):
    out = []
    for k in KSTAR:
        if k[3] >= 0:
            out.append(y[tuple(k[:3] % N) + (int(k[3]),)])
        else:
            out.append(y[tuple((-k[:3]) % N) + (int(-k[3]),)].conjugate())
    return np.array(out)


def from_compact(ks, coef):
    y = np.zeros(k2.shape, complex)
    for k, a in zip(ks, coef):
        if k[3] >= 0 and np.max(abs(k)) <= K:
            y[tuple(k[:3] % N) + (int(k[3]),)] = a
    return y * mask


def evaluate(y):
    x = irfftn(y, s=(N,) * 4, norm='forward', workers=1)
    x2 = x * x
    nonlin = rfftn(-BETA * x2 + x2 * x, norm='forward', workers=1) * mask
    energy = .5 * np.sum(weight * L * abs(y) ** 2) + \
        np.mean(-BETA / 3 * x2 * x + 1.0 / 4 * x2 * x2)
    mu = L * y + nonlin
    rhs = -k2 * mu
    return nonlin, float(energy), float(np.sqrt(np.sum(weight * abs(rhs) ** 2)))


def classify(y):
    a = star_coeffs(y)
    amp = abs(a)
    power = float(np.sum(weight * abs(y) ** 2))
    shell = float(np.sum(amp ** 2))
    if power < 1e-12:
        return dict(outcome='uniform', occupancy=0, amplitude_cv=None,
                    triad_lock=None, shell_fraction=None, power=power,
                    energy=None, rhs_rms=None)
    occ = amp >= max(1e-6, 0.1 * amp.max())
    z = np.prod(a[TRIADS], axis=1)
    lock = float(z.real.sum() / abs(z).sum())
    cv = float(amp.std() / amp.mean())
    _, energy, rhs = evaluate(y)
    full = int(occ.sum()) == 24 and cv <= 0.05 and lock >= 0.95
    outcome = ('stationary_' if rhs <= 1e-7 else 'finite_time_') + \
        ('full24' if full else 'other')
    return dict(outcome=outcome, occupancy=int(occ.sum()), amplitude_cv=cv,
                triad_lock=lock, shell_fraction=shell / power, power=power,
                energy=energy, rhs_rms=rhs)


def main():
    out = Path(__file__).resolve().parent
    with (out / 'threshold_outcomes.csv').open() as f:
        rows = list(csv.DictReader(f))
    verdicts = []
    for r in rows:
        z = np.load(out / (r['run_id'] + '.npz'), allow_pickle=False)
        ks = z['wavevectors']
        y0 = from_compact(ks, z['initial_coefficients'])
        yf = from_compact(ks, z['final_coefficients'])
        init_power = float(np.sum(weight * abs(y0) ** 2))
        init_shell = float(np.sum(abs(star_coeffs(y0)) ** 2)) / init_power
        fin = classify(yf)
        ok_outcome = fin['outcome'] == r['outcome']
        ok_s = abs(init_shell - float(r['s_value'])) < 1e-9
        ok_pow = abs(init_power - 0.1444302384510534) < 1e-12
        ok_e = (fin['energy'] is None or
                abs(fin['energy'] - float(r['final_energy'])) < 1e-9)
        ok_rhs = (fin['rhs_rms'] is None or
                  abs(fin['rhs_rms'] - float(r['rhs_rms'])) /
                  max(float(r['rhs_rms']), 1e-30) < 1e-6 or
                  abs(fin['rhs_rms'] - float(r['rhs_rms'])) < 1e-12)
        verdict = 'PASS' if (ok_outcome and ok_s and ok_pow and ok_e) else 'FAIL'
        verdicts.append(dict(run_id=r['run_id'], s_value=r['s_value'],
                             replicate=r['replicate'],
                             reported_outcome=r['outcome'],
                             recomputed_outcome=fin['outcome'],
                             recomputed_occupancy=fin['occupancy'],
                             recomputed_cv=fin['amplitude_cv'],
                             recomputed_lock=fin['triad_lock'],
                             recomputed_energy=fin['energy'],
                             recomputed_rhs_rms=fin['rhs_rms'],
                             recomputed_initial_shell_fraction=init_shell,
                             recomputed_initial_power=init_power,
                             outcome_match=ok_outcome,
                             shell_fraction_match=ok_s,
                             power_match=ok_pow, energy_match=ok_e,
                             verdict=verdict))
        print(r['run_id'], verdict, 'reported=', r['outcome'],
              'recomputed=', fin['outcome'], 's_init=%.12g' % init_shell,
              'E=%.12g' % (fin['energy'] if fin['energy'] is not None else float('nan')),
              flush=True)
    with (out / 'verify_outcomes.csv').open('w', newline='') as f:
        w = csv.DictWriter(f, fieldnames=list(verdicts[0]))
        w.writeheader()
        w.writerows(verdicts)
    print('VERIFY', sum(v['verdict'] == 'PASS' for v in verdicts), '/',
 len(verdicts))


if __name__ == '__main__':
    main()
