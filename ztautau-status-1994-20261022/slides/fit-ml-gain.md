---
class: st pres
---

<script setup>
import ZoomablePlot from 'slidev-addon-ztautau/components/ZoomablePlot.vue'
</script>

# Machine learning halves the expected errors at every energy point

<div class="st-sub">Legacy fit, expected (Asimov), each point alone: cut-based vs ML decay identification and neutrino reconstruction.</div>

<div class="st-cols st-cols-2">
<div>
<div class="st-fig" style="height:300px"><ZoomablePlot src="/figures/fit/allyears-per-point.png" alt="concurrence error per point, analytical vs ML" /></div>
<div class="st-cap"><b>Top</b> concurrence error per point with <LaTeX formula="\sqrt N" /> expectation from 1994; <b>bottom</b> ML / cut-based error ratio for all 15 coefficients</div>
</div>
<div>
<table class="num first-nw">
<thead><tr><th>Concurrence error</th><th>Cut-based</th><th>ML</th><th>Ratio</th></tr></thead>
<tbody>
<tr><td>1992 · 91.3</td><td>0.58</td><td>0.25</td><td>0.43</td></tr>
<tr><td>1993 · 89.4 / 91.2 / 93.0</td><td>2.12 / 0.69 / 2.20</td><td>0.74 / 0.28 / 0.71</td><td>0.32–0.41</td></tr>
<tr class="hl"><td>1994 · 91.2</td><td>0.34</td><td>0.16</td><td>0.46</td></tr>
<tr><td>1995 · 89.4 / 91.3 / 93.0</td><td>2.36 / 0.74 / 2.19</td><td>0.71 / 0.29 / 0.66</td><td>0.30–0.40</td></tr>
<tr><td>Combined, one fit</td><td>0.21</td><td>0.10</td><td>0.50</td></tr>
</tbody>
</table>
<div class="co ok"><b>Where</b> <LaTeX formula="\pi" /> regions: purity. Lepton regions: acceptance and resolution.</div>
<div class="co ok"><b>Worth</b> Ratio 0.43 on the coefficients: like 5× more data.</div>
<div class="co warn"><b>Off-peak</b> Small points scale worse than <LaTeX formula="\sqrt N" />.</div>
</div>
</div>

<div class="st-source">Source: per-point and combined legacy Asimov fits, 1992–1995 (2026-10-31), and the 1994 per-region gain study (2026-10-25); simulation only, statistics only</div>

<!--
artifacts/legacy-fit-ml-allyears-20261030/runs-fits/summary.md "Concurrence sigma" and "Scaling with yield" (sym sigma = (up+down)/2): analytical / ML / ratio: 1992 0.5831/0.2490/0.427; 1993_89p4 2.1161/0.7447/0.352; 1993_91p2 0.6857/0.2794/0.407; 1993_93p0 2.2045/0.7077/0.321; 1994 0.3416/0.1562/0.457; 1995_89p4 2.3617/0.7103/0.301 (analytical C_kk scan clipped at this point, sigma underestimated, ratio unreliable; audit note); 1995_91p2 0.7357/0.2904/0.395; 1995_93p0 2.1891/0.6595/0.301. Combined pooled fit (runs-combined/summary.md): concurrence 0.2076 vs 0.1034, ratio 0.498; geometric-mean coefficient sigma 0.1952 vs 0.0838, ratio 0.429 (pooled; IV 0.430). "Like 5x more data": (1/0.429)^2 = 5.4, derived, assuming sigma ~ 1/sqrt N. sqrt N scaling: concurrence obs/exp 1.19-2.06 (analytical, low-yield points) and 1.02-1.43 (ML); geometric-mean coefficient sigma close to sqrt N (0.82-1.26). Concurrence here is the legacy definition and legacy finite-difference propagation (nonlinear for O(1) coefficient errors). Gain source (artifacts/legacy-fit-ml-20261024/per-region/breakdown.md, 1994, v5 vs v2, same held-out cohort): combined acceptance factor 0.597 x per-event factor 0.724 = 0.432; pipi per-event 0.478 (purity/resolution); lepton-lepton regions acceptance 0.72-0.76 and per-event 0.63-0.66; rhorho acceptance 0.256 (ML finds many more rho-rho events). 1994 study: v5 concurrence 0.157 vs v2 0.336 (ratio 0.466), v3 (ML region only) 0.639, v4 (ML neutrino only) 0.779.
-->
