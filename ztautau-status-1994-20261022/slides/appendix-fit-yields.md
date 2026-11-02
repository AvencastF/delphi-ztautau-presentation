---
class: st pres
---

<script setup>
import ZoomablePlot from 'slidev-addon-ztautau/components/ZoomablePlot.vue'
</script>

# Appendix · 1992–1995 fit inputs per region, and legacy-model closure

<div class="st-cols st-cols-21">
<div>
<table class="sm num first-nw">
<thead><tr><th>Region</th><th>Data, cut-based</th><th>MC</th><th>Ratio</th><th>Data, ML</th><th>MC</th><th>Ratio</th></tr></thead>
<tbody>
<tr><td><LaTeX formula="\pi\pi" /></td><td>2,482</td><td>2,485</td><td>1.00</td><td>965</td><td>910</td><td>1.06</td></tr>
<tr><td><LaTeX formula="\pi\rho" /></td><td>1,553</td><td>1,497</td><td>1.04</td><td>1,846</td><td>1,877</td><td>0.98</td></tr>
<tr><td><LaTeX formula="\rho\pi" /></td><td>1,516</td><td>1,503</td><td>1.01</td><td>1,902</td><td>1,881</td><td>1.01</td></tr>
<tr><td><LaTeX formula="\rho\rho" /></td><td>978</td><td>922</td><td>1.06</td><td>5,902</td><td>6,188</td><td>0.95</td></tr>
<tr><td><LaTeX formula="ee" /></td><td>2,025</td><td>2,433</td><td>0.83</td><td>2,776</td><td>2,911</td><td>0.95</td></tr>
<tr><td><LaTeX formula="\mu\mu" /></td><td>2,726</td><td>2,523</td><td>1.08</td><td>3,181</td><td>3,006</td><td>1.06</td></tr>
<tr><td><LaTeX formula="e\mu" /></td><td>2,007</td><td>2,069</td><td>0.97</td><td>2,698</td><td>2,709</td><td>1.00</td></tr>
<tr><td><LaTeX formula="\mu e" /></td><td>1,903</td><td>2,051</td><td>0.93</td><td>2,631</td><td>2,710</td><td>0.97</td></tr>
<tr><td><LaTeX formula="\pi e" /></td><td>2,146</td><td>2,284</td><td>0.94</td><td>1,701</td><td>1,654</td><td>1.03</td></tr>
<tr><td><LaTeX formula="e\pi" /></td><td>2,094</td><td>2,240</td><td>0.93</td><td>1,677</td><td>1,635</td><td>1.03</td></tr>
<tr><td><LaTeX formula="\pi\mu" /></td><td>2,357</td><td>2,401</td><td>0.98</td><td>1,719</td><td>1,732</td><td>0.99</td></tr>
<tr><td><LaTeX formula="\mu\pi" /></td><td>2,364</td><td>2,405</td><td>0.98</td><td>1,780</td><td>1,725</td><td>1.03</td></tr>
<tr><td><LaTeX formula="\rho e" /></td><td>1,337</td><td>1,331</td><td>1.00</td><td>3,191</td><td>3,380</td><td>0.94</td></tr>
<tr><td><LaTeX formula="e\rho" /></td><td>1,289</td><td>1,319</td><td>0.98</td><td>3,222</td><td>3,348</td><td>0.96</td></tr>
<tr><td><LaTeX formula="\rho\mu" /></td><td>1,478</td><td>1,450</td><td>1.02</td><td>3,563</td><td>3,725</td><td>0.96</td></tr>
<tr><td><LaTeX formula="\mu\rho" /></td><td>1,515</td><td>1,446</td><td>1.05</td><td>3,539</td><td>3,705</td><td>0.96</td></tr>
<tr class="hl"><td>All 16</td><td>29,770</td><td>30,359</td><td>0.98</td><td>42,293</td><td>43,096</td><td>0.98</td></tr>
</tbody>
</table>
<div class="st-cap">Eight points pooled; the two orderings of a pair (e.g. πe, eπ) are separate regions. Ratios derived.</div>
</div>
<div>
<div class="st-fig" style="height:300px"><ZoomablePlot src="/figures/fit/step2-closure-pulls.png" alt="legacy-model closure pulls per region and observable" /></div>
<div class="st-cap"><b>Legacy model</b> on reweighted simulation: largest bin pull per observable and region, for each injected state</div>
</div>
</div>

<div class="st-source">Source: pooled 1992–1995 fit inputs (2026-10-31) and the legacy-model closure study (2026-10-31); simulation expectation, data counted only</div>

<!--
artifacts/legacy-fit-ml-allyears-20261030/runs-combined/summary.md (c) "Yields (16 regions)": data A / MC exp A / data ML / MC exp ML per region, before the legacy fit cut; Z->tautau expected A 29048.8, ML 42600.9; ee and mumu carry most non-tau background (Bhabha, Z->mumu, gamma gamma -> ll). Pooled input = 8 slim-by-point files concatenated (pool_inputs.py). Ratios derived on the slide. Region names: pipi, pirho, rhopi, rhorho, ee, mumu, emu, mue, pie, epi, pimu, mupi, rhoe, erho, rhomu, murho (ordered hemisphere pairs). Figure: artifacts/joint-fit-20261031/step2/combined-ml/closure_pulls.png (max |pull| 1.31 at c0 entanglement, 3.3 at C_kk lowered to E = 0, about 11 sigma from SM).
-->
