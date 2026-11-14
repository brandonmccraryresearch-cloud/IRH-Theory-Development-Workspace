#!/usr/bin/env python3
"""Task 4 paired figures: D4 vs A4* native-cell formation trajectories,
set against the A20 onset figure (onset-competition.png, prior source).
Reads d4/ and a4star/ field_trajectories.csv, field_outcomes.csv,
field_summary.csv. Produces paired_trajectories.png and formation_vs_onset.png.
All math in titles/labels uses $...$ delimiters.
"""
import csv
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.image import imread

BASE = Path.home() / "workspace/research/irh/co-scientist-tasks-2026-11-10"
A20 = BASE / "a20-onset"
OUT = BASE / "local-independent/task4-native-cells"
FAMS = ['random_full_weak', 'random_full_matched', 'six_1pct_full_noise',
        'twelve_1pct_full_noise', 'full_25pct_full_noise',
        'random_shell_matched_bridge']
FAM_LABELS = ['random weak', 'random matched', '6-mode + 1% noise',
              '12-mode + 1% noise', 'full + 25% noise', 'shell bridge']
BRANCH_E = {'D4': -0.007632267319, 'A4star': -0.005816677329}
STAR_N = {'D4': 24, 'A4star': 20}

def load(star):
    # D4 arm: prior 4d-field-test trajectories (identical cell, parameters and
    # seeds; replicated locally 10/10 in d4/). A4* arm: new runs in a4star/.
    d = (BASE / '4d-field-test') if star == 'D4' else (OUT / star.lower())
    traj = {}
    with open(d / 'field_trajectories.csv') as f:
        for row in csv.DictReader(f):
            traj.setdefault(row['family'], []).append(row)
    summ = {}
    with open(d / 'field_summary.csv') as f:
        for row in csv.DictReader(f):
            summ[row['family']] = row
    return traj, summ

def series(rows, key):
    ts = np.array([float(r['time']) for r in rows])
    vs = np.array([np.nan if r[key] in ('', None) else float(r[key]) for r in rows])
    return ts, vs

def main():
    data = {s: load(s) for s in ['D4', 'A4star']}
    colors = plt.get_cmap('tab10')(np.arange(len(FAMS)))
    fig, axes = plt.subplots(3, 2, figsize=(13, 10), sharex=True, constrained_layout=True)
    metrics = [('occupancy', 'star occupancy (modes)', (-1, 25), None),
               ('excess_energy', 'excess energy density', None, 'symlog'),
               ('shell_fraction', 'star shell / total power', (-0.03, 1.03), None)]
    for ci, star in enumerate(['D4', 'A4star']):
        traj, summ = data[star]
        for j, fam in enumerate(FAMS):
            reps = {}
            for row in traj[fam]:
                reps.setdefault(int(row['replicate']), []).append(row)
            for rep, rows in reps.items():
                for ri, (metric, title, ylim, yscale) in enumerate(metrics):
                    ax = axes[ri][ci]
                    ts, vs = series(rows, metric)
                    ax.plot(ts, vs, color=colors[j], alpha=.65, lw=1.1,
                            label=FAM_LABELS[j] if (rep == 0 and ci == 0 and ri == 0) else None)
        for ri, (metric, title, ylim, yscale) in enumerate(metrics):
            ax = axes[ri][ci]
            ax.set_title(title); ax.set_xscale('symlog', linthresh=.1); ax.grid(alpha=.15)
            if ylim: ax.set_ylim(*ylim)
            if yscale: ax.set_yscale(yscale, linthresh=.005)
            if ri == 0: ax.set_title(f'{"$D_4$" if star == "D4" else "$A_4^*$"} native cell — ' + title)
        axes[1][ci].axhline(BRANCH_E[star], color='k', ls=':', lw=1,
                            label='pure-branch energy')
        axes[2][ci].set_xlabel('Model B time')
    handles, labels = axes[0][0].get_legend_handles_labels()
    fig.legend(handles, labels, loc='outside lower center', ncol=3, fontsize=8)
    title = ('Paired native-cell formation: $D_4$ (left) vs $A_4^*$ (right), '
             'matched $r=-0.35$, $\\bar{\\psi}=-0.18$, $q_0^2=8$, RMS $0.38004$\n'
             'Faint lines are individual replicates (3 per family). '
             'Dotted line: pure equal-amplitude branch energy for that star.')
    fig.suptitle(title, fontsize=11)
    fig.savefig(OUT / 'paired_trajectories.png', dpi=170)
    plt.close(fig)

    # Second figure: onset figure (top) + paired energy/occupancy trajectories (bottom)
    onset = imread(A20 / 'onset-competition.png')
    fig = plt.figure(figsize=(13, 12), constrained_layout=True)
    gs = fig.add_gridspec(2, 2, height_ratios=[1.5, 1.0])
    ax_im = fig.add_subplot(gs[0, :])
    ax_im.imshow(onset); ax_im.axis('off')
    ax_im.set_title('Onset (A20): matched pure-branch energies vs $t=\\alpha v/\\beta^2$ '
                    '— $D_4$ lower above $t_\\times=-0.0566$', fontsize=11)
    for ci, star in enumerate(['D4', 'A4star']):
        ax = fig.add_subplot(gs[1, ci])
        traj, summ = data[star]
        for j, fam in enumerate(FAMS):
            reps = {}
            for row in traj[fam]:
                reps.setdefault(int(row['replicate']), []).append(row)
            for rep, rows in reps.items():
                ts, vs = series(rows, 'excess_energy')
                ax.plot(ts, vs, color=colors[j], alpha=.7, lw=1.1,
                        label=FAM_LABELS[j] if rep == 0 else None)
                ts2, vs2 = series(rows, 'occupancy')
        ax.axhline(BRANCH_E[star], color='k', ls=':', lw=1,
                   label='pure-branch energy')
        ax.set_xscale('symlog', linthresh=.1); ax.set_yscale('symlog', linthresh=.005)
        ax.set_xlabel('Model B time'); ax.set_ylabel('excess energy density')
        ax.set_title(f'{"$D_4$" if star == "D4" else "$A_4^*$"} native cell: formation energy')
        ax.grid(alpha=.15); ax.legend(fontsize=7, ncol=2)
    fig.suptitle('Formation on native cells set against the onset figure\n'
                 'Same quench and matched RMS in both cells; energies are '
                 'volume-normalised densities.', fontsize=12)
    fig.savefig(OUT / 'formation_vs_onset.png', dpi=170)
    plt.close(fig)
    print('wrote paired_trajectories.png and formation_vs_onset.png')

if __name__ == '__main__':
    main()
