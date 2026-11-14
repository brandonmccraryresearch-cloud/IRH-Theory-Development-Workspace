#!/usr/bin/env python3
"""Step 4 (Task 6): figures + fit tables from the Bloch data (Kb=4 map,
Kb=2 coarse map, checks). No recomputation of spectra."""
import csv, json
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

WORK = Path('/home/hatch/workspace/research/irh/co-scientist-tasks-2026-11-10/local-independent/task6-bloch-growth')

def load_csv(name):
    with open(WORK / 'data' / name) as f:
        return list(csv.DictReader(f))

rows4 = load_csv('bloch_map_Kb4.csv')
rows2 = load_csv('bloch_coarse_Kb2.csv')
chk4 = json.loads((WORK / 'data/bloch_checks_Kb4.json').read_text())
chk2 = json.loads((WORK / 'data/bloch_checks.json').read_text())

def cut(rows, label):
    rs = [r for r in rows if r['label'] == label]
    rs.sort(key=lambda r: float(r['qnorm']))
    return rs

fig, axes = plt.subplots(2, 2, figsize=(11, 9))
# (a) axis + diagonal cuts, lam_max vs |q|
ax = axes[0, 0]
for lab, mk in [('axis_e1', 'o'), ('diag110', 's'), ('diag1110', '^'), ('diag1111', 'D')]:
    rs = cut(rows4, lab)
    ax.plot([float(r['qnorm']) for r in rs], [float(r['lam_max']) for r in rs],
            marker=mk, ls='-', ms=4, label=lab)
ax.axhline(0, color='k', lw=0.8)
ax.set_xlabel(r'$|q|$'); ax.set_ylabel(r'$\lambda_{\max}(q)$')
ax.set_title(r'(a) Least-damped rate vs $|q|$ (Kb=4)')
ax.legend(fontsize=8); ax.grid(alpha=0.3)
# (b) long-wave: lam vs |q|^2, axis cut, with Schur slope for mean channel
ax = axes[0, 1]
rs = cut(rows4, 'axis_e1')
rs = [r for r in rs if float(r['qnorm']) <= 0.2 and r['lam_mean'] != '']
x = np.array([float(r['qnorm']) ** 2 for r in rs])
ax.plot(x, [float(r['lam_max']) for r in rs], 'o-', label=r'$\lambda_{\max}$ (transverse)')
ax.plot(x, [float(r['lam_mean']) for r in rs], 's-',
        label=r'$\lambda_{\mathrm{mean}}$')
S = chk4['checks']['C3b']['Schur_S']
ax.plot(x, -S * x, 'k--', label=rf'Schur slope $-{S:.2f}|q|^2$')
ax.set_xlabel(r'$|q|^2$'); ax.set_ylabel(r'$\lambda$')
ax.set_title('(b) Long-wave channels, axis cut')
ax.legend(fontsize=8); ax.grid(alpha=0.3)
# (c) Kb=4 vs Kb=2 lam_max on the axis cut
ax = axes[1, 0]
rs4 = cut(rows4, 'axis_e1'); rs2 = cut(rows2, 'axis_e1')
ax.plot([float(r['qnorm']) for r in rs4], [float(r['lam_max']) for r in rs4], 'o-', label='Kb=4')
ax.plot([float(r['qnorm']) for r in rs2], [float(r['lam_max']) for r in rs2], 's--', label='Kb=2')
ax.axhline(0, color='k', lw=0.8)
ax.set_xlabel(r'$|q|$'); ax.set_ylabel(r'$\lambda_{\max}(q)$')
ax.set_title('(c) Cutoff comparison, axis cut')
ax.legend(fontsize=8); ax.grid(alpha=0.3)
# (d) random-BZ sample: histogram of lam_max + the least-damped points
ax = axes[1, 1]
rnd = [float(r['lam_max']) for r in rows4 if r['label'].startswith('randomBZ')]
ax.hist(rnd, bins=25, alpha=0.7)
ax.axvline(max(rnd), color='r', ls='--', label=f'max {max(rnd):.3f}')
ax.set_xlabel(r'$\lambda_{\max}(q)$'); ax.set_ylabel('count')
ax.set_title('(d) Random Brillouin-zone sample (150 pts)')
ax.legend(fontsize=8); ax.grid(alpha=0.3)
fig.tight_layout()
fig.savefig(WORK / 'figures/bloch_stability_map.png', dpi=150)
print('saved bloch_stability_map.png')

# Figure 2: lam_max over the axis cut on a fine scale + mean channel, Kb=4 vs Kb=2 bias
fig, ax = plt.subplots(figsize=(8, 5))
rs4 = cut(rows4, 'axis_e1')
ax.plot([float(r['qnorm']) for r in rs4], [float(r['lam_max']) for r in rs4], 'o-', label='Kb=4 transverse')
ax.plot([float(r['qnorm']) for r in rs4], [float(r['lam4']) for r in rs4], '^-', label='Kb=4 4th rate (longitudinal at small q)')
ax.plot([float(r['qnorm']) for r in rs4 if r['lam_mean'] != ''],
        [float(r['lam_mean']) for r in rs4 if r['lam_mean'] != ''], 's-', label='Kb=4 mean channel')
ax.axhline(0, color='k', lw=0.8)
ax.set_xlabel(r'$|q|$ along $(1,0,0,0)$'); ax.set_ylabel(r'$\lambda$')
ax.set_title('Long-wave branches on the axis cut (Kb=4)')
ax.legend(fontsize=8); ax.grid(alpha=0.3)
fig.tight_layout()
fig.savefig(WORK / 'figures/bloch_longwave_branches.png', dpi=150)
print('saved bloch_longwave_branches.png')

# Summary numbers to stdout for the report
print('Kb4 map rows:', len(rows4))
print('Kb4 lam_max overall max (all sampled q):', max(float(r['lam_max']) for r in rows4))
nz = [r for r in rows4 if float(r['qnorm']) > 0.2]
print('Kb4 lam_max max for |q|>0.2:', max(float(r['lam_max']) for r in nz),
      'at', max(nz, key=lambda r: float(r['lam_max'])))
print('Kb4 lam_max max for |q|>0.05:', max(float(r['lam_max']) for r in rows4 if float(r['qnorm']) > 0.05))
print('C3b Schur S:', chk4['checks']['C3b'])
print('fits_axis:', chk4['checks']['fits_axis'])
print('C4b:', chk4['checks']['C4b_Kb4_vs_Kb2'])
print('C5b:', chk4['checks']['C5b_K4_vs_K6_Kb4'])
print('C1b:', chk4['checks']['C1b_goldstone_Hv_over_v'], 'lam0 top:', chk4['checks']['C1b_lam0_top10'][:6])
print('C6:', chk4['checks']['C6_symmetry'])
