#!/usr/bin/env python3
"""Post-hoc final-pattern analysis for Task 2 (cheap + full tiers).

For each run, the final state is (per the global diagnostics) a single
stationary full-24 pattern. This script answers WHICH pattern it is:
  - overlap O_p = |sum_k conj(a_k^{template,p}) a_k^{final}|
    / (||a^{template,p}|| ||a^{final}||) with each patch p's initial
    template coefficients (rotation + shift included). O_p = 1 means
    the final pattern IS patch p's pattern; O_p < 1 measures how far
    the compromise sits from it. (Per-patch rho/theta in the run
    diagnostics measure something narrower: fit onto the 2-D
    uniform-phase subspace of one template, which a translated pattern
    in general leaves.)
  - per-mode final phases, grouped by the patch-1 phase pattern, for
    the antiphase config B (winner vs compromise, mode by mode).
  - final-pattern self-consistency: the real-space field in each patch
    interior correlated against the pattern rebuilt from the final
    shell coefficients (must be ~1 if the box holds one pattern).
Template coefficients are rebuilt here from parameters.json
(rotations/shifts), independently of run_grain's PatchSet.
"""
import itertools, json
from pathlib import Path
import numpy as np

WD = Path(__file__).parent
A_AMP = 0.07757529633928076


def star_m():
    return np.array([m for m in itertools.product([-4, 0, 4], repeat=4)
                     if sum(x * x for x in m) == 32])


MODE_SETS = {
    'full24': np.array([m for m in itertools.product([-4, 0, 4], repeat=4)
                        if sum(x * x for x in m) == 32]),
    'hex6': np.array([(4, 4, 0, 0), (0, -4, 4, 0), (4, 0, 4, 0),
                      (-4, -4, 0, 0), (0, 4, -4, 0), (-4, 0, -4, 0)]),
}
MODE_SETS['hex6_swap13'] = np.array(
    [(v[2], v[1], v[0], v[3]) for v in MODE_SETS['hex6']])


def template_coeffs(patch):
    """Initial template shell coefficients for one patch.

    Pattern phi_p(x) = A_p * sum_{m in modes} cos((m/2).(x - s)).
    The Fourier coefficient of mode m (physical k = m/2) is then
    A_p * exp(-i (m/2).s) for m in the patch's mode set, 0 otherwise.
    (The requested rotation does NOT enter: for the full star it only
    permutes the sum, and for sub-patterns the orientation is carried
    by the mode set itself. An earlier draft indexed the coefficient by
    the rotated vector; that mis-indexing is corrected here.)
    A_p = pattern_rms / sqrt(n_modes)."""
    modes = MODE_SETS[patch.get('modes', 'full24')]
    s = np.array(patch['shift'], dtype=float)
    pattern_rms = patch.get('pattern_rms', float(np.sqrt(24) * A_AMP))
    a_patch = pattern_rms / np.sqrt(len(modes))
    star = star_m()
    out = np.zeros(24, dtype=complex)
    mode_set = {tuple(m) for m in modes}
    for i, m in enumerate(star):
        if tuple(m) in mode_set:
            out[i] = a_patch * np.exp(-1j * (np.asarray(m, dtype=float) / 2.0) @ s)
    return out


def final_shell(z, par):
    """Final shell coefficients from the compact coefficients in the NPZ,
    using the same reading convention as the solver (negative-m3 entries
    are conjugates of the opposite mode)."""
    n = par['n']
    comp = z['wavevectors']
    coef = z['final_coefficients']
    d = {tuple(k): a for k, a in zip(comp, coef)}
    star = star_m()
    out = []
    for m in star:
        key = tuple(m)
        if key in d:
            out.append(d[key])
        else:
            out.append(np.conj(d[tuple(-m)]))
    return np.array(out)


def main():
    rows = []
    for tier in ['cheap', 'full']:
        for d in sorted((WD / tier).glob('*')):
            if not (d / 'grain_state.npz').exists():
                continue
            par = json.loads((d / 'parameters.json').read_text())
            out = json.loads((d / 'grain_outcome.json').read_text())
            z = np.load(d / 'grain_state.npz')
            a_fin = final_shell(z, par)
            a_fin = a_fin / np.linalg.norm(a_fin)
            for p in par['patches']:
                a_tpl = template_coeffs(p)
                a_tpl = a_tpl / np.linalg.norm(a_tpl)
                ov = float(abs(np.vdot(a_tpl, a_fin)))
                rows.append(dict(tier=tier, config=par['config'],
                                 patch=p['index'], env_id=p['env_id'],
                                 overlap=ov))
                print(f"{tier} {par['config']} patch {p['index']}: "
                      f"final-pattern overlap O = {ov:.6f}")
            # per-mode final phases for B (grouped by k1 sign)
            if par['config'] == 'B':
                star = star_m()
                ph = np.angle(a_fin * np.linalg.norm(a_fin))
                print(f"  {tier} B final phases by mode:")
                for m, p in sorted(zip(star, ph), key=lambda t: tuple(t[0])):
                    print(f"    m={tuple(m)} phase={p:+.4f}")
    import csv
    with open(WD / 'final_pattern_overlap.csv', 'w', newline='') as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0]))
        w.writeheader()
        w.writerows(rows)


if __name__ == '__main__':
    main()
