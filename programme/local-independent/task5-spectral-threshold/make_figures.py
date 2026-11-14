#!/usr/bin/env python3
"""Figures for Task 5 spectral threshold: recovery fraction vs shell
concentration, with Wilson 95% intervals (n=3 per point), plus the
initial-energy and final-energy companion panels. Reads
threshold_summary.csv and threshold_outcomes.csv in this directory.
"""
import csv
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

OUT = Path(__file__).resolve().parent


def read_csv(name):
    with (OUT / name).open() as f:
        return list(csv.DictReader(f))


def main():
    summary = read_csv('threshold_summary.csv')
    outcomes = read_csv('threshold_outcomes.csv')
    s = np.array([float(r['s_value']) for r in summary])
    frac = np.array([float(r['recovery_fraction']) for r in summary])
    lo = np.array([float(r['wilson_lo']) for r in summary])
    hi = np.array([float(r['wilson_hi']) for r in summary])
    n = np.array([int(r['n']) for r in summary])

    fig, axes = plt.subplots(1, 3, figsize=(15, 4.8), constrained_layout=True)
    ax = axes[0]
    ax.errorbar(s, frac, yerr=[frac - lo, hi - frac], fmt='o-', color='tab:blue',
                capsize=4, lw=1.6, label='recovery fraction (n=3 per point)')
    ax.plot(s, frac, 'o', color='tab:blue', ms=5)
    for xi, fi, ki in zip(s, frac, [int(r['full24']) for r in summary]):
        if xi <= 0.10:
            ax.annotate(f'{ki}/3', (xi, fi), textcoords='offset points',
                        xytext=(0, 8), ha='center', fontsize=8)
    ax.axhline(0.5, color='k', ls=':', lw=1, label='50% recovery')
    ax.axhline(1.0, color='gray', ls='--', lw=0.8)
    ax.set_xlabel('Initial D4 shell power fraction  s')
    ax.set_ylabel('Fraction reaching stationary full 24')
    ax.set_title('Threshold curve: full-pattern recovery vs shell concentration')
    ax.set_xlim(-0.03, 1.03)
    ax.set_ylim(-0.05, 1.12)
    ax.grid(alpha=0.2)
    ax.legend(fontsize=8, loc='lower right')

    ax = axes[1]
    for rep in sorted({int(r['replicate']) for r in outcomes}):
        rr = [r for r in outcomes if int(r['replicate']) == rep]
        ax.plot([float(r['s_value']) for r in rr],
                [float(r['initial_energy']) for r in rr], 'o-',
                ms=4, lw=1, label=f'replicate {rep}')
    ax.set_xlabel('Initial D4 shell power fraction  s')
    ax.set_ylabel('Initial excess energy density')
    ax.set_title('Initial energy falls as power concentrates on-shell')
    ax.set_yscale('symlog', linthresh=0.05)
    ax.grid(alpha=0.2)
    ax.legend(fontsize=8)

    ax = axes[2]
    for r in outcomes:
        y = float(r['final_energy'])
        c = 'tab:green' if r['outcome'] == 'stationary_full24' else 'tab:red'
        m = 'o' if r['outcome'] == 'stationary_full24' else 'x'
        ax.plot(float(r['s_value']), y, m, color=c, ms=6)
    ax.axhline(-0.007726209285, color='k', ls=':', lw=1,
               label='field full branch -0.0077262')
    ax.axhline(-0.007632267319, color='gray', ls='--', lw=1,
               label='24-mode full branch -0.0076323')
    ax.set_xlabel('Initial D4 shell power fraction  s')
    ax.set_ylabel('Final excess energy density')
    ax.set_title('Final energy: two clusters (full 24 vs uniform)')
    ax.set_yscale('symlog', linthresh=0.005)
    ax.grid(alpha=0.2)
    ax.legend(fontsize=8)
    fig.suptitle('Task 5: spectral-power threshold for full D4 formation '
                 '(fixed total power, RMS 0.3800398, t=200, N=18, K=4)',
                 fontsize=11)
    fig.savefig(OUT / 'threshold_curve.png', dpi=170)
    plt.close(fig)
    print('WROTE threshold_curve.png')


if __name__ == '__main__':
    main()
