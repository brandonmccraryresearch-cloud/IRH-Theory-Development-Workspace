#!/usr/bin/env python3
"""Task 5 (local-independent): spectral-power threshold for full D4 formation.

Interpolation (frozen before any run):
  For each replicate rep, draw the SAME broadband Gaussian direction u used
  by the 4D field pilot: rng from SeedSequence([931241112, rep]), real iid
  Gaussian on the 18^4 grid, rFFT, sharp tensor mask |k_i|<=4, normalised
  to unit total modulation power (sum weight*|y|^2 = 1).
  Decompose u = u_shell + u_off in the weighted inner product, where
  u_shell is the projection onto the 24 D4 star coefficients and u_off is
  the orthogonal complement. Let p = ||u_shell||^2 (the pilot broadband
  shell fraction, 0.0017-0.0046).
  For target shell fraction s in [0,1]:
      y(s) = TARGET * ( sqrt(s) * u_shell/||u_shell||
                        + sqrt(1-s) * u_off/||u_off|| )
  with TARGET = sqrt(24)*A_star = 0.38003978535286725 (matched RMS).
  Then total power is TARGET^2 exactly (orthogonal unit components) and
  the shell fraction is exactly s. Endpoints are exact reproductions:
  y(p) == TARGET*u (pilot broadband matched start) and y(1) is the pilot
  shell-random bridge start (same direction, renormalised to TARGET).
  s=0 is a pure off-shell random start (shell power exactly zero).

Dynamics / diagnostics / outcome rule are identical to the pilot
(run_field_study.py, sha256 a7b03651...): periodic [0,2pi]^4 box,
phi = psi - (-0.18), alpha = 0.1072, beta = 1.54, r=-0.35, u=v=1,
N=18, K=4, ETD2 with exact linear propagator, startup caps dt/1000
until t=0.02 and dt/20 until t=0.2, energy-rejection tolerance
2e-13 + 2e-12*|F|, t_final=200, dt=0.1.
Full endpoint: occupancy 24, amplitude CV <= 0.05, signed triad lock
>= 0.95, projected RHS RMS <= 1e-7. Uniform: total power < 1e-12.

Coarse grid (Stage 1, frozen): s = 0, 0.05, 0.15, 0.30, 0.50, 0.70,
0.90, 1.00; replicates 0,1,2; 24 runs. Per-run NPZ checkpoints allow
resume; a run is never re-integrated once its checkpoint exists.
Usage:
  python run_threshold.py --out . --s-values 0,0.05,0.15,0.30
  python run_threshold.py --out . --s-values 0.50,0.70,0.90,1.00
  python run_threshold.py --out . --validation   # self-tests only
"""
import os
for key in ('OMP_NUM_THREADS', 'OPENBLAS_NUM_THREADS', 'MKL_NUM_THREADS'):
    os.environ[key] = '1'
import argparse, csv, hashlib, importlib.util, itertools, json, platform
import resource, time
from pathlib import Path
import numpy as np
import scipy
from scipy.fft import rfftn, irfftn, fftfreq, rfftfreq

PY = __import__('sys').executable
P = dict(r=-.35, mean=-.18, q0_squared=8., u=1., v=1., mobility=1.,
         box_length=2*np.pi, alpha=.1072, beta=1.54,
         master_seed=931241112, replicates=3, t_final=200., dt=.1,
         n=18, cutoff=4, occupancy_relative=.1, occupancy_absolute=1e-6,
         uniform_power=1e-12, stationary_rhs=1e-7, cv_max=.05,
         locking_min=.95)
KSTAR = np.array([k for k in itertools.product([-2, 0, 2], repeat=4)
                  if sum(x * x for x in k) == 8])
TRIADS = np.array([t for t in itertools.combinations(range(24), 3)
                   if np.all(KSTAR[list(t)].sum(axis=0) == 0)])
A_STAR = (8 * P['beta'] + np.sqrt((8 * P['beta']) ** 2 - 4 * 141 * P['alpha'])) / 282
TARGET = np.sqrt(24) * A_STAR
S_GRID = [0.0, 0.05, 0.15, 0.30, 0.50, 0.70, 0.90, 1.0]


def dump(path, x):
    path.write_text(json.dumps(x, indent=2, allow_nan=False) + '\n')


def csvwrite(path, rows):
    with path.open('w', newline='') as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0]))
        w.writeheader()
        w.writerows(rows)


class Field:
    def __init__(self, n, cutoff):
        assert n > 4 * cutoff
        self.n = n
        self.cutoff = cutoff
        self.shape = (n,) * 4
        q = [np.rint(fftfreq(n) * n).astype(int)] * 3 + \
            [np.rint(rfftfreq(n) * n).astype(int)]
        self.coords = np.meshgrid(*q, indexing='ij', sparse=True)
        self.k2 = sum(x * x for x in self.coords)
        self.mask = np.ones_like(self.k2, dtype=bool)
        for x in self.coords:
            self.mask &= abs(x) <= cutoff
        self.mask[(0,) * 4] = False
        self.L = P['alpha'] + (P['q0_squared'] - self.k2) ** 2
        self.linear = -self.k2 * self.L
        self.weight = np.broadcast_to(
            np.where((q[3] == 0) | (q[3] == n // 2), 1., 2.), self.k2.shape)
        self.nonzero_shape = (2 * cutoff + 1,) * 4
        self.compactK = np.array(list(itertools.product(
            range(-cutoff, cutoff + 1), repeat=4)))
        self.Ecache = {}

    def fft(self, x):
        return rfftn(x, norm='forward', workers=1)

    def real(self, y):
        return irfftn(y, s=self.shape, norm='forward', workers=1)

    def coefficients(self, y, ks=KSTAR):
        out = []
        for k in ks:
            if k[3] >= 0:
                out.append(y[tuple(k[:3] % self.n) + (int(k[3]),)])
            else:
                out.append(y[tuple((-k[:3]) % self.n) + (int(-k[3]),)].conjugate())
        return np.array(out)

    def from_compact(self, ks, coef):
        y = np.zeros(self.k2.shape, complex)
        for k, a in zip(ks, coef):
            if k[3] >= 0 and np.max(abs(k)) <= self.cutoff:
                y[tuple(k[:3] % self.n) + (int(k[3]),)] = a
        return y * self.mask

    def power(self, y):
        return float(np.sum(self.weight * abs(y) ** 2))

    def evaluate(self, y):
        x = self.real(y)
        x2 = x * x
        nonlin = self.fft(-P['beta'] * x2 + P['v'] * x2 * x) * self.mask
        energy = .5 * np.sum(self.weight * self.L * abs(y) ** 2) + \
            np.mean(-P['beta'] / 3 * x2 * x + P['v'] / 4 * x2 * x2)
        return nonlin, float(energy)

    def etd(self, dt):
        if dt not in self.Ecache:
            z = dt * self.linear
            E = np.exp(z)
            b = np.empty_like(z)
            c = np.empty_like(z)
            nz = abs(z) > 1e-7
            b[nz] = np.expm1(z[nz]) / self.linear[nz]
            c[nz] = dt * (np.expm1(z[nz]) - z[nz]) / (z[nz] ** 2)
            b[~nz] = dt * (1 + z[~nz] / 2 + z[~nz] ** 2 / 6)
            c[~nz] = dt * (.5 + z[~nz] / 6 + z[~nz] ** 2 / 24)
            self.Ecache[dt] = (E, b, c)
        return self.Ecache[dt]

    def step(self, y, nonlin, dt):
        E, b, c = self.etd(dt)
        Ny = -self.k2 * nonlin
        predictor = (E * y + b * Ny) * self.mask
        Na, _ = self.evaluate(predictor)
        trial = (predictor + c * (-self.k2 * Na - Ny)) * self.mask
        Nt, energy = self.evaluate(trial)
        return trial, Nt, energy

    def diagnostics(self, y, nonlin, energy):
        a = self.coefficients(y)
        amp = abs(a)
        power = self.power(y)
        shell = float(np.sum(amp ** 2))
        uniform = power < P['uniform_power']
        occ = amp >= max(P['occupancy_absolute'],
                         P['occupancy_relative'] * amp.max())
        z = np.prod(a[TRIADS], axis=1)
        den = abs(z).sum()
        lock = float(z.real.sum() / den) if den > 1e-24 and not uniform else None
        cv = float(amp.std() / amp.mean()) if amp.mean() > 1e-20 and not uniform else None
        mu = self.L * y + nonlin
        rhs = -self.k2 * mu
        spectrum = np.bincount(np.rint(self.k2).astype(int).ravel(),
                               weights=(self.weight * abs(y) ** 2).ravel())
        active = occ[TRIADS].all(axis=1)
        return dict(modulation_power=power, modulation_rms=np.sqrt(power),
                    shell_power=shell,
                    shell_fraction=shell / power if not uniform else None,
                    off_shell_power=max(0., power - shell),
                    off_shell_fraction=max(0., 1 - shell / power) if not uniform else None,
                    occupancy=0 if uniform else int(occ.sum()),
                    amplitude_cv=cv, triad_lock=lock,
                    active_triads=int(active.sum()) if not uniform else 0,
                    excess_energy=energy,
                    rhs_rms=float(np.sqrt(np.sum(self.weight * abs(rhs) ** 2))),
                    mean_realspace=float(P['mean'] + np.mean(self.real(y))),
                    mean_error=float(abs(np.mean(self.real(y))))), spectrum, a


def base_direction(m, rep):
    """Unit-power broadband Gaussian direction, pilot-identical seeds."""
    seed = int(np.random.SeedSequence([P['master_seed'], rep]).generate_state(1)[0])
    rng = np.random.default_rng(seed)
    noise = m.fft(rng.normal(size=m.shape)) * m.mask
    noise /= np.sqrt(np.sum(m.weight * abs(noise) ** 2))
    return noise, seed


def make_initial(m, s, rep):
    """Interpolated initial field at target shell fraction s (exact)."""
    u, seed = base_direction(m, rep)
    a = m.coefficients(u)
    p = float(np.sum(abs(a) ** 2))  # pilot broadband shell fraction
    shell_field = m.from_compact(KSTAR, a)
    off_field = u - shell_field
    off_power = m.power(off_field)
    assert abs(p + off_power - 1.0) < 1e-12, (p, off_power)
    assert abs(m.power(shell_field) - p) < 1e-12
    unit_shell = shell_field / np.sqrt(p)
    unit_off = off_field / np.sqrt(off_power)
    y = TARGET * (np.sqrt(s) * unit_shell + np.sqrt(1.0 - s) * unit_off)
    # Exactness checks: total power TARGET^2, shell fraction s.
    assert abs(m.power(y) - TARGET ** 2) < 1e-12 * TARGET ** 2
    assert abs(float(np.sum(abs(m.coefficients(y)) ** 2)) / m.power(y) - s) < 1e-9, s
    if abs(s - p) < 1e-15:
        assert np.max(abs(y - TARGET * u)) < 1e-12
    return y, seed, p


def integrate(m, y0, dt, tfinal):
    y = y0.copy()
    N, E = m.evaluate(y)
    t = 0.
    accepted = 0
    rejected = 0
    maxinc = 0.
    rows = []
    shell = []
    spectra = []
    save = np.unique(np.r_[0, np.geomspace(.01, 2, 12),
                           np.arange(5, tfinal, 5.), tfinal])
    save = save[save <= tfinal]
    si = 0
    while si < len(save):
        if abs(t - save[si]) < 1e-9:
            d, s, a = m.diagnostics(y, N, E)
            rows.append(dict(time=float(t), **d))
            shell.append(a)
            spectra.append(s)
            si += 1
            if si == len(save):
                break
        if t < .02 - 1e-12:
            cap = dt * .001
            boundary = .02
        elif t < .2 - 1e-12:
            cap = dt * .05
            boundary = .2
        else:
            cap = dt
            boundary = tfinal
        h = min(cap, save[si] - t, boundary - t)
        attempt = 0
        while True:
            yn, Nn, En = m.step(y, N, h)
            tolerance = 2e-13 + 2e-12 * abs(E)
            if np.isfinite(En) and En <= E + tolerance:
                break
            h *= .5
            rejected += 1
            attempt += 1
            if h < 1e-8 or attempt > 25:
                raise RuntimeError('Energy safeguard failed')
        maxinc = max(maxinc, En - E)
        y, N, E = yn, Nn, En
        t += h
        accepted += 1
    return y, rows, np.array(shell), np.array(spectra), dict(
        accepted_steps=accepted, rejected_steps=rejected,
        max_step_energy_increase=maxinc)


def outcome(d):
    if d['modulation_power'] < P['uniform_power']:
        return 'uniform'
    full = d['occupancy'] == 24 and d['amplitude_cv'] <= P['cv_max'] and \
        d['triad_lock'] is not None and d['triad_lock'] >= P['locking_min']
    return ('stationary_' if d['rhs_rms'] <= P['stationary_rhs']
            else 'finite_time_') + ('full24' if full else 'other')


def load_truncation(out_dir):
    cand = Path(out_dir) / 'basin_run_study.py'
    if not cand.exists():
        cand = Path(__file__).resolve().parent / 'basin_run_study.py'
    spec = importlib.util.spec_from_file_location('basin_run_study', str(cand))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod.Model(mod.DEFAULTS.copy())


def self_tests(out):
    m = Field(18, 4)
    big = Field(28, 6)
    rng = np.random.default_rng(91)
    y = m.fft(rng.normal(size=m.shape)) * m.mask
    y *= .15 / np.sqrt(np.sum(m.weight * abs(y) ** 2))
    N, E = m.evaluate(y)
    coef = m.coefficients(y, m.compactK)
    yb = big.from_compact(m.compactK, coef)
    Nb, Eb = big.evaluate(yb)
    mu = m.L * y + N
    d = m.fft(rng.normal(size=m.shape)) * m.mask
    d /= np.sqrt(np.sum(m.weight * abs(d) ** 2))
    eps = 1e-6
    fd = (m.evaluate(y + eps * d)[1] - m.evaluate(y - eps * d)[1]) / (2 * eps)
    grad = float(np.real(np.sum(m.weight * np.conj(mu) * d)))
    model = load_truncation(out)
    a = np.full(24, A_STAR, complex)
    sy = m.from_compact(KSTAR, a)
    Ns, Es = m.evaluate(sy)
    frhs = m.coefficients(-m.k2 * (m.L * sy + Ns))
    trhs = model.rhs(0, a)
    x = m.real(y)
    Nreal = -P['beta'] * x * x + P['v'] * x * x * x
    rhs = m.real(-m.k2 * (m.L * y + N))
    Lreal = m.real(m.L * y)
    diss_direct = float(np.mean((Lreal + Nreal) * rhs))
    diss_spectral = float(-np.sum(m.weight * m.k2 * abs(mu) ** 2))
    yl = m.from_compact(KSTAR, a * 1e-7)
    yf, _, _, _, _ = integrate(m, yl, .05, 1.)
    expected = yl * np.exp(-8 * P['alpha'])
    linear_error = float(np.linalg.norm(yf - expected) / np.linalg.norm(expected))
    # Interpolation exactness on all three replicate directions.
    interp = {}
    for rep in range(3):
        u, seed = base_direction(m, rep)
        p = float(np.sum(abs(m.coefficients(u)) ** 2))
        for s in [0.0, 0.05, 0.5, 1.0]:
            yy, _, _ = make_initial(m, s, rep)
            interp[f'rep{rep}_s{s}_pilot_p'] = p
            interp[f'rep{rep}_s{s}_shell_fraction'] = float(
                np.sum(abs(m.coefficients(yy)) ** 2)) / m.power(yy)
            interp[f'rep{rep}_s{s}_total_power'] = m.power(yy)
    tests = dict(dealias_energy_18_vs_28_same_K4=abs(E - Eb),
                 dealias_projected_nonlinearity_max=float(np.max(abs(
                     m.coefficients(N, m.compactK) - big.coefficients(Nb, m.compactK)))),
                 energy_gradient_fd_absolute_error=abs(fd - grad),
                 dissipation_identity_absolute_error=abs(diss_direct - diss_spectral),
                 shell_rhs_vs_exact_prior_truncation_max=float(np.max(abs(frhs - trhs))),
                 shell_energy_vs_exact_prior_truncation=float(abs(Es - model.energy(a))),
                 linear_decay_relative_error=linear_error,
                 unordered_triads=len(TRIADS), analytic_amplitude=float(A_STAR),
                 matched_rms=float(TARGET), target_power=float(TARGET ** 2),
                 **interp)
    assert tests['dealias_energy_18_vs_28_same_K4'] < 1e-10
    assert tests['dealias_projected_nonlinearity_max'] < 1e-12
    assert tests['energy_gradient_fd_absolute_error'] < 1e-7
    assert tests['dissipation_identity_absolute_error'] < 1e-8
    assert tests['shell_rhs_vs_exact_prior_truncation_max'] < 1e-12
    assert tests['shell_energy_vs_exact_prior_truncation'] < 1e-12
    assert linear_error < 1e-5
    for rep in range(3):
        for s in [0.0, 0.05, 0.5, 1.0]:
            assert abs(tests[f'rep{rep}_s{s}_shell_fraction'] - s) < 1e-9
            assert abs(tests[f'rep{rep}_s{s}_total_power'] - TARGET ** 2) < 1e-12
    dump(out / 'numerical_tests.json', tests)
    return tests


def wilson(k, n, z=1.959964):
    if n == 0:
        return 0.0, 0.0
    ph = k / n
    den = 1 + z * z / n
    cen = ph + z * z / (2 * n)
    rad = z * np.sqrt(ph * (1 - ph) / n + z * z / (4 * n * n))
    return float((cen - rad) / den), float((cen + rad) / den)


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--out', default='.')
    ap.add_argument('--s-values', default=','.join(str(s) for s in S_GRID))
    ap.add_argument('--replicates', type=int, default=3)
    ap.add_argument('--t-final', type=float, default=200.)
    ap.add_argument('--dt', type=float, default=.1)
    ap.add_argument('--validation', action='store_true')
    ap.add_argument('--half-dt', action='store_true',
                    help='Re-run listed runs at dt/2 (refinement; same initials)')
    args = ap.parse_args()
    out = Path(args.out)
    out.mkdir(parents=True, exist_ok=True)
    s_values = [float(x) for x in args.s_values.split(',') if x != '']
    tests = self_tests(out)
    print('SELF_TESTS ' + json.dumps(tests), flush=True)
    if args.validation:
        print('VALIDATION_ONLY', flush=True)
        return
    P.update(replicates=args.replicates, t_final=args.t_final, dt=args.dt)
    m = Field(P['n'], P['cutoff'])
    start = time.perf_counter()
    outcomes = []
    if (out / 'threshold_outcomes.csv').exists():
        with (out / 'threshold_outcomes.csv').open() as f:
            outcomes = list(csv.DictReader(f))
    done = {(r['s_value'], r['replicate']) for r in outcomes}
    # Normalise stored rows to full-precision numbers on rewrite.
    for r in outcomes:
        for k in ['s_value', 'initial_shell_fraction_pilot_p', 'initial_rms',
                  'initial_energy', 'final_energy', 'final_rms',
                  'final_shell_fraction', 'amplitude_cv', 'triad_lock',
                  'rhs_rms', 'elapsed_seconds']:
            if r.get(k) not in (None, ''):
                r[k] = float(r[k])
        r['replicate'] = int(r['replicate'])
        r['occupancy'] = int(r['occupancy']) if r.get('occupancy') not in (None, '') else 0
    for s in s_values:
        for rep in range(args.replicates):
            key = (str(s), rep)
            if key in done:
                continue
            rid = f's{s:g}_rep{rep:02d}'
            path = out / (rid + '.npz')
            y0, seed, p = make_initial(m, s, rep)
            dt_run = args.dt / 2 if args.half_dt else args.dt
            tick = time.perf_counter()
            if path.exists() and not args.half_dt:
                z = np.load(path, allow_pickle=False)
                yf = m.from_compact(z['wavevectors'], z['final_coefficients'])
                rows = json.loads(str(z['rows_json']))
                stats = json.loads(str(z['stats_json']))
                elapsed = stats['elapsed_seconds']
            else:
                yf, rows, sh, sp, stats = integrate(m, y0, dt_run, args.t_final)
                elapsed = time.perf_counter() - tick
                stats['elapsed_seconds'] = elapsed
                if not args.half_dt:
                    np.savez_compressed(
                        path, wavevectors=m.compactK,
                        initial_coefficients=m.coefficients(y0, m.compactK),
                        final_coefficients=m.coefficients(yf, m.compactK),
                        times=np.array([r['time'] for r in rows]),
                        shell_coefficients=sh, power_by_k_squared=sp,
                        rows_json=json.dumps(rows), stats_json=json.dumps(stats))
            result = dict(run_id=rid, s_value=s, replicate=rep, seed=seed,
                          initial_shell_fraction_pilot_p=p,
                          initial_rms=rows[0]['modulation_rms'],
                          initial_energy=rows[0]['excess_energy'],
                          outcome=outcome(rows[-1]),
                          occupancy=rows[-1]['occupancy'],
                          amplitude_cv=rows[-1]['amplitude_cv'],
                          triad_lock=rows[-1]['triad_lock'],
                          rhs_rms=rows[-1]['rhs_rms'],
                          final_energy=rows[-1]['excess_energy'],
                          final_rms=rows[-1]['modulation_rms'],
                          final_shell_fraction=rows[-1]['shell_fraction'],
                          dt_used=dt_run, elapsed_seconds=elapsed,
                          accepted_steps=stats['accepted_steps'],
                          rejected_steps=stats['rejected_steps'],
                          max_step_energy_increase=stats['max_step_energy_increase'])
            outcomes.append(result)
            done.add(key)
            csvwrite(out / 'threshold_outcomes.csv', outcomes)
            print(json.dumps({k: result[k] for k in
                              ['run_id', 'outcome', 'occupancy', 'final_energy',
                               'rhs_rms', 'elapsed_seconds', 'rejected_steps']}),
                  flush=True)
    # Summary table with Wilson intervals, written after every batch.
    summary = []
    for s in sorted({float(r['s_value']) for r in outcomes}):
        rr = [r for r in outcomes if float(r['s_value']) == s]
        k = sum(1 for r in rr if r['outcome'] == 'stationary_full24')
        lo, hi = wilson(k, len(rr))
        summary.append(dict(s_value=s, n=len(rr), full24=k,
                            uniform=sum(1 for r in rr if r['outcome'] == 'uniform'),
                            other=sum(1 for r in rr if r['outcome'] not in
                                      ('stationary_full24', 'uniform')),
                            recovery_fraction=k / len(rr) if rr else 0.0,
                            wilson_lo=lo, wilson_hi=hi,
                            mean_initial_energy=float(np.mean([r['initial_energy'] for r in rr])),
                            mean_elapsed_seconds=float(np.mean([r['elapsed_seconds'] for r in rr]))))
    csvwrite(out / 'threshold_summary.csv', summary)
    dump(out / 'parameters.json', dict(
        **{k: P[k] for k in ['r', 'mean', 'q0_squared', 'u', 'v', 'alpha', 'beta',
                             'master_seed', 't_final', 'dt', 'n', 'cutoff']},
        analytic_amplitude=float(A_STAR), matched_rms=float(TARGET),
        target_power=float(TARGET ** 2), s_grid=S_GRID,
        s_values_run=s_values, replicates=args.replicates,
        python=platform.python_version(), numpy=np.__version__,
        scipy=scipy.__version__, platform=platform.platform(),
        script_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        basin_source_sha256=hashlib.sha256(
            (Path(__file__).resolve().parent / 'basin_run_study.py').read_bytes()).hexdigest(),
        field_source_sha256='a7b03651eb4eb66efa6d59cfc6adfe6021b00b8b73babaa2dfecf154f24ef422',
        total_elapsed_this_invocation=time.perf_counter() - start,
        process_peak_rss_MiB=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1024,
        runs_completed=len(outcomes)))
    print('COMPLETED runs=' + str(len(outcomes)) +
          ' elapsed=' + str(time.perf_counter() - start), flush=True)


if __name__ == '__main__':
    main()
