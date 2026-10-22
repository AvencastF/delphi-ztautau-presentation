---
class: st pres
---

# Model versions 2 to 5: what changed and what it bought

<table>
<thead><tr><th>Version</th><th>Inputs</th><th>Target</th><th>Verdict</th></tr></thead>
<tbody>
<tr><td>v2 · 2026-10-16</td><td>46 event quantities</td><td>angles to leading track, detector frame</td><td>universal baseline</td></tr>
<tr><td>v3 · 2026-10-17</td><td>as v2</td><td>cone frame of the leading track</td><td>best π legs in ππ, worse elsewhere</td></tr>
<tr><td>v4 · 2026-10-21</td><td>74 quantities (per-leg cone)</td><td>frame chosen per leg</td><td>reproduces v3</td></tr>
<tr class="hl"><td>v5 · 2026-10-21</td><td>as v4</td><td>as v2</td><td>= v2 within statistics; <span class="tag decision">baseline</span></td></tr>
</tbody>
</table>

<table class="num" style="margin-top:10px">
<thead><tr><th>Median direction error [°]</th><th>v2</th><th>v3</th><th>v4</th><th>v5</th></tr></thead>
<tbody>
<tr><td>e legs</td><td><span class="best">1.16</span></td><td>1.35</td><td>1.35</td><td>1.17</td></tr>
<tr><td>ρ legs</td><td><span class="best">1.01</span></td><td>1.38</td><td>1.36</td><td>1.03</td></tr>
<tr><td>π legs in ππ</td><td>0.78</td><td><span class="best">0.61</span></td><td>0.68</td><td>0.75</td></tr>
<tr><td>correct branch, ρρ</td><td><span class="best">0.773</span></td><td>0.673</td><td>0.693</td><td>0.771</td></tr>
</tbody>
</table>

<div class="co ok"><b>Takeaway</b> The target frame, not the inputs, sets the performance.</div>

<div class="st-source">Source: model history in the converter documentation and the v5 version comparison (full tables in the appendix)</div>

<!--
EveNet-Align/Ztautau/converter/README.md "Model history"; artifacts/neutrino-ml-v5-20261021/README.md, compare_versions.md. Direction error inclusive median/84 % (v2/v3/v4/v5): e 1.16/2.32, 1.35/2.77, 1.35/2.75, 1.17/2.35; mu 1.08/2.18, 1.27/2.65, 1.27/2.63, 1.09/2.21; pi 0.90/2.08, 0.97/2.46, 1.01/2.48, 0.89/2.07; rho 1.01/2.02, 1.38/2.89, 1.36/2.80, 1.03/2.07. Per channel medians: pipi pi .78/.61/.68/.75; pirho pi .88/1.02/1.09/.87; pirho rho .90/1.09/1.17/.90; rhorho rho .98/1.44/1.33/1.00; ee 1.27/1.38/1.39/1.29; mumu 1.11/1.24/1.23/1.11; erho rho 1.09/1.42/1.41/1.10. Branch accuracy table in appendix. Twelve per-leg cone globals add nothing measurable (rhorho 1.00 vs 0.98 deg; pipi gain 0.03 deg vs v3's 0.61).
-->
