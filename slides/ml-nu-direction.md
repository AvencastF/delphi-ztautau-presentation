---
class: st pres
---

<script setup>
import NJUPlot from '../components/NJUPlot.vue'
</script>

# Neutrino model v5: direction error and branch choice

<div class="fig-lead">
<div><div class="st-fig"><NJUPlot src="/figures/ml/v5/06_direction.svg" alt="branch accuracy per channel and direction error per leg" /></div><div class="st-cap">Branch accuracy per channel (left), direction error per leg type (right); held-out simulation</div></div>
<div>
<table class="num">
<thead><tr><th>Median error [<LaTeX formula="^\circ" />]</th><th>analytical</th><th>best branch</th><th>ML v5</th></tr></thead>
<tbody>
<tr><td>e legs</td><td>2.09</td><td>1.38</td><td><span class="best">1.17</span></td></tr>
<tr><td><LaTeX formula="\mu" /> legs</td><td>1.96</td><td>1.28</td><td><span class="best">1.09</span></td></tr>
<tr><td><LaTeX formula="\pi" /> legs</td><td>1.52</td><td><span class="best">0.69</span></td><td>0.89</td></tr>
<tr><td><LaTeX formula="\rho" /> legs</td><td>1.41</td><td><span class="best">0.77</span></td><td>1.03</td></tr>
<tr><td>correct branch, inclusive</td><td>0.593</td><td>0.912</td><td><span class="best">0.740</span></td></tr>
<tr><td>correct branch, <LaTeX formula="\pi\pi" /></td><td>0.501</td><td>0.982</td><td><span class="best">0.764</span></td></tr>
</tbody>
</table>
<div class="co ok" style="margin-top:8px"><b>Takeaway</b> ML beats the default branch everywhere; the simulation ceiling stays out of reach for <LaTeX formula="\pi" />, <LaTeX formula="\rho" />.</div>
</div>
</div>

<div class="st-source">Source: version-5 neutrino evaluation summary (full tables in the appendix)</div>

<!--
artifacts/neutrino-ml-v5-20261021/eval/summary.md: direction error median / 84 % per leg (e, mu, pi, rho, other): analytical 2.09/3.84, 1.96/3.69, 1.52/3.38, 1.41/2.84, 1.25/2.34; analytical_best 1.38/2.55, 1.28/2.43, 0.69/1.85, 0.77/1.80, 0.81/1.65; nu 1.17/2.35, 1.09/2.21, 0.89/2.07, 1.03/2.07, 1.09/2.07; analytical+nu 1.71/3.18, 1.59/3.00, 1.02/2.54, 1.13/2.45, 1.09/2.10. Branch accuracy per channel (analytical / best / nu / hybrid): inclusive 0.593/0.912/0.740/0.736; ee 0.502/0.962/0.683/0.692; emu 0.501/0.974/0.687/0.697; epi 0.492/0.975/0.700/0.715; erho 0.622/0.876/0.739/0.725; mumu 0.508/0.983/0.706/0.721; mupi 0.504/0.979/0.717/0.727; murho 0.608/0.879/0.753/0.736; pipi 0.501/0.982/0.764/0.802; pirho 0.638/0.887/0.768/0.773; rhorho 0.702/0.859/0.771/0.769. Pair consistency: nu 0.16 deg / 0.15 GeV vs analytical 0.10 / 0.10. Figure eval/06_direction.svg.
-->
