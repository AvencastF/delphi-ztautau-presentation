---
class: st pres
---

<script setup>
import NJUPlot from '../components/NJUPlot.vue'
</script>

# Spin-observable resolution per channel

<div class="fig-lead">
<div><div class="st-fig"><NJUPlot src="/figures/ml/v5/07_residual_width.svg" alt="residual width per observable and channel" /></div><div class="st-cap">68 % residual width per observable and true channel; analytical, ML, hybrid (version 5)</div></div>
<div>
<table class="num">
<thead><tr><th>Median 68 % width</th><th>v2</th><th>v3</th><th>v5</th></tr></thead>
<tbody>
<tr><td>ee</td><td>0.291</td><td>0.312</td><td><span class="best">0.289</span></td></tr>
<tr><td><LaTeX formula="\mu\mu" /></td><td><span class="best">0.258</span></td><td>0.278</td><td>0.259</td></tr>
<tr><td><LaTeX formula="e\rho" /></td><td><span class="best">0.246</span></td><td>0.310</td><td>0.251</td></tr>
<tr><td><LaTeX formula="\pi\pi" /></td><td>0.146</td><td><span class="best">0.135</span></td><td>0.142</td></tr>
<tr><td><LaTeX formula="\pi\rho" /></td><td>0.185</td><td>0.221</td><td><span class="best">0.182</span></td></tr>
<tr><td><LaTeX formula="\rho\rho" /></td><td><span class="best">0.222</span></td><td>0.315</td><td>0.223</td></tr>
</tbody>
</table>
<div class="co ok" style="margin-top:8px"><b>Takeaway</b> v5 = v2 within 0.005; 10–30 % better than v3 outside <LaTeX formula="\pi\pi" />.</div>
</div>
</div>

<div class="st-source">Source: version comparison table of the v5 archive (all channels and versions in the appendix)</div>

<!--
artifacts/neutrino-ml-v5-20261021/compare_versions.md "Observable residuals per truth channel": 15 observables B_i = 3<h_i>, C_ij = 9<h-_i h+_j>, charged track as analyser; median w68 (v2/v3/v4/v5): ee .291/.312/.315/.289; emu .279/.297/.300/.281; mumu .258/.278/.276/.259; epi .202/.212/.219/.203; mupi .190/.195/.203/.186; erho .246/.310/.308/.251; murho .236/.284/.289/.238; pipi .146/.135/.145/.142; pirho .185/.221/.241/.182; rhorho .222/.315/.289/.223. C_kk pipi .105/.080/.082/.104. Full table in appendix.
-->
