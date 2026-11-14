#!/usr/bin/env python3
"""Figures for Task 2 grain locking (reads cheap/*/ and full/*/ outputs).

fig_phase.png: per-patch correlation rho_p(t) and phase theta_p(t).
fig_boundary.png: slab RMS / slab template-correlation profiles across
  the x1 interfaces, and boundary-vs-interior energy density vs time.
fig_shellpower.png: global shell power, shell fraction, off-shell power,
  total power and excess energy vs time for every config.
All math in the report uses $...$ delimiters; figure titles are plain.
"""
import csv, json
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

WD = Path(__file__).parent
LBOX = 4 * np.pi
TAPER = 1.0
CONFIGS = ['A', 'B', 'C', 'D', 'E', 'F']
LABELS = {
    'A': 'A aligned-2 (control)',
    'B': 'B antiphase-2',
    'C': 'C rotated-2 (shift only)',
    'D': 'D quad-4 (shifts only)',
    'E': 'E half-uniform',
    'F': 'F hex6-orientation-2',
}


def read_csv(path):
    with open(path, newline='') as f:
        return list(csv.DictReader(f))


def load(tier):
    data = {}
    for c in CONFIGS:
        d = WD / tier / c
        if not (d / 'grain_outcome.json').exists():
            continue
        out = json.loads((d / 'grain_outcome.json').read_text())
        traj = read_csv(d / 'grain_trajectories.csv')
        patch = read_csv(d / 'grain_patch_trajectories.csv')
        slab = read_csv(d / 'grain_slab_profiles.csv')
        data[c] = dict(out=out, traj=traj, patch=patch, slab=slab)
    return data


def plot_phase(data, tier, outname):
    cfgs = [c for c in CONFIGS if c in data]
    fig, axes = plt.subplots(2, len(cfgs), figsize=(4 * len(cfgs), 6.4),
                             sharex=True, constrained_layout=True)
    if len(cfgs) == 1:
        axes = axes.reshape(2, 1)
    for j, c in enumerate(cfgs):
        patch = data[c]['patch']
        times = sorted(set(float(r['time']) for r in patch))
        npatch = max(int(r['patch']) for r in patch) + 1
        for p in range(npatch):
            rows = [r for r in patch if int(r['patch']) == p]
            rows.sort(key=lambda r: float(r['time']))
            t = [float(r['time']) for r in rows]
            rho = [float(r['rho']) for r in rows]
            th = [float(r['theta']) for r in rows]
            axes[0, j].plot(t, rho, '.-', ms=3, label=f'patch {p}')
            axes[1, j].plot(t, th, '.-', ms=3, label=f'patch {p}')
        axes[0, j].set_title(LABELS[c])
        axes[0, j].set_ylim(-0.05, 1.05)
        axes[0, j].set_ylabel('local correlation $\\rho_p$')
        axes[0, j].grid(alpha=0.2)
        axes[1, j].set_xlabel('Model B time')
        axes[1, j].set_ylabel('local phase $\\theta_p$ (rad)')
        axes[1, j].set_ylim(-3.4, 3.4)
        axes[1, j].grid(alpha=0.2)
        axes[0, j].legend(fontsize=7)
    axes[0, 0].set_ylabel('local correlation $\\rho_p$')
    fig.suptitle(f'Patch phase evolution, {tier} tier '
                 f'(N={data[cfgs[0]]["out"]["n"]}, K={data[cfgs[0]]["out"]["cutoff"]})')
    fig.savefig(WD / outname, dpi=170)
    plt.close(fig)


def boundary_excess(data_c):
    """(times, boundary mean edens, interior mean edens) from slab rows.

    Boundary slabs: slab centres within 2.0 of an interface (x1 = 0 or
    L/2, periodic). Interior slabs: centres in the middle of a patch
    half, at least 2.0 from any interface."""
    slab = data_c['slab']
    times = sorted(set(float(r['time']) for r in slab))
    b, i = [], []
    for t in times:
        rows = [r for r in slab if float(r['time']) == t]
        bv, iv = [], []
        for r in rows:
            x = float(r['x1_center'])
            d = min(abs(x), abs(x - LBOX / 2), abs(x - LBOX))
            if d < 1.5:
                bv.append(float(r['slab_edens']))
            elif d > 2.5:
                iv.append(float(r['slab_edens']))
        b.append(float(np.mean(bv)))
        i.append(float(np.mean(iv)))
    return times, np.array(b), np.array(i)


def plot_boundary(data, tier, outname):
    cfgs = [c for c in ['A', 'B', 'C', 'E', 'F'] if c in data]
    fig, axes = plt.subplots(2, len(cfgs), figsize=(4.2 * len(cfgs), 6.4),
                             constrained_layout=True)
    if len(cfgs) == 1:
        axes = axes.reshape(2, 1)
    show_times = [0.0, 10.0, 50.0, 100.0]
    for j, c in enumerate(cfgs):
        slab = data[c]['slab']
        for t in show_times:
            rows = [r for r in slab if abs(float(r['time']) - t) < 1e-6]
            if not rows:
                continue
            rows.sort(key=lambda r: float(r['x1_center']))
            x = [float(r['x1_center']) for r in rows]
            rms = [float(r['slab_rms']) for r in rows]
            axes[0, j].plot(x, rms, '.-', ms=3, label=f't={t:g}')
        axes[0, j].axvline(0, color='k', ls=':', lw=1)
        axes[0, j].axvline(LBOX / 2, color='k', ls=':', lw=1)
        axes[0, j].axvline(LBOX, color='k', ls=':', lw=1)
        axes[0, j].set_title(LABELS[c] + ': slab RMS vs $x_1$')
        axes[0, j].set_xlabel('$x_1$')
        axes[0, j].set_ylabel('slab RMS')
        axes[0, j].grid(alpha=0.2)
        axes[0, j].legend(fontsize=7)
        times, bv, iv = boundary_excess(data[c])
        axes[1, j].plot(times, bv, '.-', ms=3, label='boundary slabs')
        axes[1, j].plot(times, iv, '.-', ms=3, label='interior slabs')
        axes[1, j].plot(times, bv - iv, '.-', ms=3, label='boundary excess')
        axes[1, j].set_xlabel('Model B time')
        axes[1, j].set_ylabel('mean energy density')
        axes[1, j].set_xscale('symlog', linthresh=0.1)
        axes[1, j].grid(alpha=0.2)
        axes[1, j].legend(fontsize=7)
    fig.suptitle(f'Grain-boundary behaviour, {tier} tier')
    fig.savefig(WD / outname, dpi=170)
    plt.close(fig)


def plot_shellpower(data, tier, outname):
    cfgs = [c for c in CONFIGS if c in data]
    fig, axes = plt.subplots(2, 3, figsize=(15, 8), constrained_layout=True)
    metrics = [('shell_power', 'D4 shell power'),
               ('shell_fraction', 'D4 shell fraction'),
               ('off_shell_power', 'off-shell power'),
               ('modulation_power', 'total modulation power'),
               ('excess_energy', 'excess energy density'),
               ('occupancy', 'D4 occupancy')]
    for ax, (metric, title) in zip(axes.flat, metrics):
        for c in cfgs:
            traj = data[c]['traj']
            t = [float(r['time']) for r in traj]
            v = [float(r[metric]) if r[metric] != '' else np.nan for r in traj]
            ax.plot(t, v, '.-', ms=3, label=LABELS[c])
        ax.set_title(title)
        ax.set_xlabel('Model B time')
        ax.set_xscale('symlog', linthresh=0.1)
        ax.grid(alpha=0.2)
        if metric in ('shell_power', 'off_shell_power', 'modulation_power'):
            ax.set_yscale('log')
        if metric == 'shell_fraction':
            ax.set_ylim(-0.05, 1.05)
        if metric == 'occupancy':
            ax.set_ylim(-1, 25)
    axes[0, 0].legend(fontsize=7, loc='lower right')
    fig.suptitle(f'Shell power vs time, {tier} tier')
    fig.savefig(WD / outname, dpi=170)
    plt.close(fig)


if __name__ == '__main__':
    for tier in ['cheap', 'full']:
        data = load(tier)
        if not data:
            print(f'{tier}: no runs yet')
            continue
        plot_phase(data, tier, f'fig_phase_{tier}.png')
        plot_boundary(data, tier, f'fig_boundary_{tier}.png')
        plot_shellpower(data, tier, f'fig_shellpower_{tier}.png')
        print(f'{tier}: figures written for {sorted(data)}')
