"""Two explanatory figures for the spin-fit chapter (second 2026-10-31 revision), made from the audited fit outputs.
No fit is re-run: the numbers are read from the saved model-B templates and the model-B / model-C summaries.

1. public/figures/fit-explainer/template-ckk.svg
   pi-pi region, observable cos(theta_A^k) * cos(theta_B^k), combined 1992-1995, ML reconstruction.
   Prediction for any C_kk: expected = A0 + (C_kk - C_kk_ref) * T[C_kk] (linear model, base_templates.npz note).
   Points = Asimov pseudo-data (the simulation at its own C_kk_ref) with sqrt(N) error bars.
2. public/figures/fit-explainer/pull-widths.svg
   pull width per coefficient, 2000 event-level toys at the expected state, combined 1992-1995:
   "Poisson per histogram" (model B, column "pull std B") vs "full covariance" (model C, column "C pull std").

Usage (deck root): /Users/avencastmini/miniforge3/bin/python3 data/make_fit_explainer_figs.py
"""
import os, re
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

ART = '/Users/avencastmini/ZtautauLEP/artifacts/joint-fit-20261031'
OUT = 'public/figures/fit-explainer'
os.makedirs(OUT, exist_ok=True)
BLUE, AMBER, ROSE, INK, MUTED = '#1f6fb2', '#d08a1c', '#b84a62', '#1d2127', '#6b7280'
plt.rcParams.update({'font.family': ['sans-serif'], 'font.sans-serif': ['DejaVu Sans', 'Helvetica', 'Arial'], 'font.size': 11, 'axes.edgecolor': MUTED, 'axes.labelcolor': INK,
                     'xtick.color': MUTED, 'ytick.color': MUTED, 'svg.fonttype': 'none', 'axes.spines.top': False,
                     'axes.spines.right': False})

# ---- 1. template picture
d = np.load(f'{ART}/modelB/combined-ml/base_templates.npz')
bc, regions = list(d['bc_names']), list(d['regions'])
m, r = bc.index('C_kk'), regions.index('pipi')
edges, ref = d['bin_edges'], float(d['reference'][m])
A0, T = d['A0'][m, r], d['T'][m, m, r]
asimov = d['all_mc'][m, r]
assert np.allclose(A0, asimov, rtol=1e-9), 'A0 should equal the Asimov histogram'
centres = 0.5 * (edges[1:] + edges[:-1])
fig, ax = plt.subplots(figsize=(6.4, 3.6), dpi=100)
for c, col, ls, lab in [(-1.0, ROSE, (0, (5, 2)), r'$C_{kk}=-1$ (opposite)'), (0.0, AMBER, (0, (1.5, 1.5)), r'$C_{kk}=0$ (no correlation)'),
                        (ref, BLUE, '-', rf'$C_{{kk}}={ref:.2f}$ (simulation)')]:
    y = A0 + (c - ref) * T
    ax.stairs(y, edges, color=col, lw=2, ls=ls, label=lab)
ax.errorbar(centres, asimov, yerr=np.sqrt(asimov), fmt='o', ms=4.5, color=INK, lw=1.2, label='pseudo-data (= simulation)', zorder=5)
ax.set_xlabel(r'$\cos\theta^{k}_{A}\,\cdot\,\cos\theta^{k}_{B}$  (both $\tau$ decays, $k$ axis)')
ax.set_ylabel('events per bin')
ax.set_xlim(-1, 1)
ax.set_ylim(0, None)
ax.grid(axis='y', color='#e5e7eb', lw=0.8)
ax.legend(frameon=False, fontsize=9, loc='upper right')
ax.set_title(r'$\pi\pi$ region, 1992–1995, ML reconstruction: three predictions', fontsize=10.5, color=INK, loc='left')
fig.tight_layout()
fig.savefig(f'{OUT}/template-ckk.svg')
print('template-ckk.svg  ref C_kk', ref, 'events', asimov.sum())

# ---- 2. pull widths, model B vs model C (combined)
def table(path, col):
    rows, hdr = {}, None
    for line in open(path):
        cells = [c.strip() for c in line.strip().strip('|').split('|')]
        if cells and cells[0] == 'coeff':
            hdr = cells if col in cells else None; continue
        if hdr and len(cells) == len(hdr) and re.match(r'^[BC]_', cells[0]):
            rows[cells[0]] = float(cells[hdr.index(col)])
        elif hdr and not line.startswith('|'):
            if rows: break
    return rows
pB = table(f'{ART}/modelB/combined-ml/summary.md', 'pull std B')
pC = table(f'{ART}/modelC/combined-ml/summary.md', 'C pull std')
assert len(pB) == 15 and len(pC) == 15, (len(pB), len(pC))
names = bc
lab = [re.sub(r'([BC])_(\w)(\w)', lambda g: f'${g.group(1)}_{{{g.group(2)}{g.group(3)}}}$', n) for n in names]
x = np.arange(15)
fig, ax = plt.subplots(figsize=(6.4, 3.2), dpi=100)
ax.bar(x - 0.2, [pB[n] for n in names], 0.38, color=ROSE, label='Poisson per histogram (events counted up to 15 times)')
ax.bar(x + 0.2, [pC[n] for n in names], 0.38, color=BLUE, label='full covariance (final model)')
ax.axhline(1, color=INK, lw=1, ls=(0, (4, 2)))
ax.text(14.6, 1.04, 'correct = 1', ha='right', va='bottom', fontsize=9, color=INK)
ax.set_xticks(x, lab, fontsize=9)
ax.set_ylabel('pull width')
ax.set_ylim(0, 2.6)
ax.grid(axis='y', color='#e5e7eb', lw=0.8)
ax.legend(frameon=False, fontsize=9, loc='upper left')
fig.tight_layout()
fig.savefig(f'{OUT}/pull-widths.svg')
print('pull-widths.svg  B', min(pB.values()), max(pB.values()), ' C', min(pC.values()), max(pC.values()))

# browsers do not ship DejaVu Sans: give every text run (including mathtext) a sans-serif fallback
for name in ('template-ckk.svg', 'pull-widths.svg'):
    p = f'{OUT}/{name}'
    s = open(p).read()
    s = re.sub(r"font-family: 'DejaVu Sans( Display)?'(?=[;\"])", "font-family: 'DejaVu Sans', 'Helvetica', 'Arial', sans-serif", s)
    open(p, 'w').write(s)
