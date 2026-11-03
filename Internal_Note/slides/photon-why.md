---
class: st pres
---

# Why calibrate photons: the <LaTeX formula="\rho" /> polarimeter needs each <LaTeX formula="\pi^0" />

<div class="st-sub">The polarimeter vector of <LaTeX formula="\tau\to\rho\nu\to\pi\pi^0\nu" /> uses the full <LaTeX formula="\pi^0" /> four-momentum; the older direction-only <LaTeX formula="\rho" /> uses none of it.</div>

<table class="num first-nw">
<thead><tr><th>How the <LaTeX formula="\pi^0" /> is built</th><th>Share of true <LaTeX formula="\rho" /> legs</th><th><LaTeX formula="E_{\pi^0}" /> reco/true, median (half-68)</th></tr></thead>
<tbody>
<tr><td>Two resolved photons (pair)</td><td>0.210</td><td><LaTeX formula="0.983" /> (0.142)</td></tr>
<tr><td>Merged shower tagged as <LaTeX formula="\pi^0" /></td><td>0.102</td><td><LaTeX formula="0.922" /> (0.128)</td></tr>
<tr><td>One photon (single)</td><td>0.585</td><td><LaTeX formula="0.887" /> (0.237)</td></tr>
<tr><td>None: direction only (fallback)</td><td>0.104</td><td>—</td></tr>
<tr class="hl"><td>Usable (pair + merged + single)</td><td>0.897</td><td></td></tr>
</tbody>
</table>

<div class="st-cap">Simulation, 796,991 true <LaTeX formula="\rho" /> legs in the reconstructed-<LaTeX formula="\rho" /> regions, 1992–1995.</div>

<div class="st-cols st-cols-2" style="margin-top:10px">
<div class="tiles tiles-2" style="margin-top:0">
<div class="tile sim"><b>0.68</b><span>correlation of the reconstructed polarimeter with the true one (0.30 direction only)</span></div>
<div class="tile sim"><b>2.5</b><span>gain in effective statistics for the Bell test, expected</span></div>
</div>
<div>
<div class="co warn"><b>Consequence</b> The <LaTeX formula="\pi^0" /> energy enters the polarimeter directly: a data/simulation photon-scale difference becomes a bias.</div>
<div class="co open"><b>Status</b> <span class="tag sim">sim</span> Asimov, statistics only; no data fit.</div>
</div>
</div>

<div class="st-source">Source: the <LaTeX formula="\rho" />-polarimeter study conclusion and its addendum (2026-11-02/03), simulation only</div>

<!--
artifacts/rho-polarimeter-CONCLUSION-20261102.md (sections 1-3, addendum A of 2026-11-03). Addendum A: reconstructable pi0 per true rho leg (MC, 796,991 true-rho legs in reco-rho regions): pair 0.210, merged 0.102, single 0.585, fallback 0.104; usable 0.897 (1992 0.857, other years about 0.907); generator pi0 photons matched to a stored object 58.4 %. E_pi0 reco/true median (half-68): pair 0.983 (0.142), merged 0.922 (0.128), single 0.887 (0.237). Polarimeter correlation with truth (n/r/k) 0.66/0.68/0.68 reconstructed; 0.76/0.76/0.75 with true pi and pi0; direction-only 0.30/0.30/0.33. Section 3: gain in effective statistics (Bell) 2.5 (reco, all years) vs baseline 1; sigma(W) 0.220 -> 0.140; expected Z(Bell) 1.9 -> 3.0; model C, Asimov, MC only, statistics only. Side finding: direction-only rho analysing power in this MC is 0.434, not 0.41.
-->
