---
class: st pres tk
---

<script setup>
import ZoomablePlot from 'slidev-addon-ztautau/components/ZoomablePlot.vue'
</script>

# Backup · reconstruction gain by energy point

<div class="tk-split wide">
<div><div class="tk-fig" style="height:310px"><ZoomablePlot src="/figures/fit/per-point.png" alt="expected concurrence uncertainty per point and ratio of uncertainties network over conventional for all 15 coefficients" /></div><div class="tk-cap"><b>Top</b> expected concurrence uncertainty per point, conventional (blue) and network (orange), with the <LaTeX formula="\sqrt N" /> expectation from 1994 as bars. <b>Bottom</b> uncertainty ratio network / conventional for each of the 15 coefficients.</div></div>
<div>
<table class="num first-nw">
<thead><tr><th>Concurrence uncertainty</th><th>Conventional</th><th>Network</th><th>Ratio</th></tr></thead>
<tbody>
<tr><td>1992 · 91 GeV</td><td>0.58</td><td>0.25</td><td>0.43</td></tr>
<tr><td>1993 · 89 / 91 / 93</td><td>2.12 / 0.69 / 2.20</td><td>0.74 / 0.28 / 0.71</td><td>0.32–0.41</td></tr>
<tr class="hl"><td>1994 · 91 GeV</td><td>0.34</td><td>0.16</td><td>0.46</td></tr>
<tr><td>1995 · 89 / 91 / 93</td><td>2.36 / 0.74 / 2.19</td><td>0.71 / 0.29 / 0.66</td><td>0.30–0.40</td></tr>
<tr><td>Combined</td><td>0.21</td><td>0.10</td><td>0.50</td></tr>
</tbody>
</table>
<ul class="tk-points" style="margin-top:10px">
<li class="ok"><b>Per coefficient</b> Ratios 0.35–0.6 everywhere; average 0.43.</li>
<li class="warn"><b>Off-peak</b> The small points scale worse than <LaTeX formula="\sqrt N" /> with the conventional reconstruction.</li>
</ul>
</div>
</div>

<div class="tk-foot">One-observable-per-coefficient fit, expected, statistical only; the outlier at 1995 · 89 GeV is a clipped scan of the conventional fit. <span class="tk-label sim">simulation</span></div>
