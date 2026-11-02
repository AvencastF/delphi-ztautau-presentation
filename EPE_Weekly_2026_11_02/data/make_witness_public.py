"""Public-language redraw of the entanglement-witness toy distributions.

Uses the reported Gaussian widths of the 20,000-toy histograms
(Internal_Note fit-hypothesis / SOURCES slide 22), not the production PNG.
The original figure is kept at public/figures/fit/witness-null.png for backup.
"""

from pathlib import Path

import numpy as np
import matplotlib.pyplot as plt

NULL_SIGMA = 0.2344
SM_SIGMA = 0.2256
W_SM = 1.6407

OUT = Path(__file__).resolve().parent.parent / "public" / "figures" / "fit" / "witness-public.svg"

x = np.linspace(-1.05, 2.55, 800)
null = np.exp(-0.5 * (x / NULL_SIGMA) ** 2) / (NULL_SIGMA * np.sqrt(2 * np.pi))
sm = np.exp(-0.5 * ((x - W_SM) / SM_SIGMA) ** 2) / (SM_SIGMA * np.sqrt(2 * np.pi))

plt.rcParams.update({
    "font.family": "sans-serif",
    "font.sans-serif": ["DM Sans", "Helvetica Neue", "Helvetica", "Arial", "DejaVu Sans"],
    "font.size": 11,
    "axes.linewidth": 0.8,
    "xtick.direction": "out",
    "ytick.direction": "out",
})

fig, ax = plt.subplots(figsize=(6.4, 3.55), dpi=160)
fig.patch.set_facecolor("white")
ax.set_facecolor("white")

ax.fill_between(x, null, color="#3b7eb8", alpha=0.16, linewidth=0)
ax.plot(x, null, color="#2b6ea8", lw=2.15, label="no entanglement")
ax.fill_between(x, sm, color="#e07a3d", alpha=0.16, linewidth=0)
ax.plot(x, sm, color="#d4652a", lw=2.15, label="Standard Model")
ax.axvline(0.0, color="#5c6370", lw=1.05, zorder=2)
ax.axvline(W_SM, color="#c0392b", lw=1.7, label="expected value 1.64", zorder=3)

ax.set_xlim(-1.05, 2.55)
ax.set_ylim(0.0, 2.05)
ax.set_xlabel(r"entanglement witness $W$")
ax.set_ylabel("density")
ax.legend(frameon=False, loc="upper left", fontsize=10.5)
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)
ax.tick_params(length=3.5, width=0.8)
fig.tight_layout(pad=0.35)
fig.savefig(OUT, format="svg")
print(f"wrote {OUT}")
