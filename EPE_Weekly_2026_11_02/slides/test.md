---
class: st pres tk
clicks: 3
---

<script setup>
import ZoomablePlot from 'slidev-addon-ztautau/components/ZoomablePlot.vue'
</script>

# Backup · testing entanglement with pseudo-experiments

<div class="tk-split">
<div>
<ol class="steps" style="font-size:14.5px">
<li v-click="1"><b>Null hypothesis</b> constrained best fit with <LaTeX formula="W\le 0" /> imposed</li>
<li v-click="2"><b>Pseudo-experiments</b> 20,000 event-level datasets under the constrained null</li>
<li v-click="3"><b>p-value</b> the fraction with <LaTeX formula="q=\chi^2_{\rm null}-\chi^2_{\rm free}" /> at least as large as the reference value</li>
</ol>
<ul class="tk-points" style="margin-top:10px">
<li v-click="1"><b>Why the witness</b> <LaTeX formula="W=C_{nn}-C_{rr}+C_{kk}-1" /> is linear in the coefficients: its distribution under the null is Gaussian and easy to calibrate.</li>
<li v-click="3"><b>Bell</b> Same recipe with <LaTeX formula="|C_{kk}-C_{rr}|\le\sqrt2" /> as the null hypothesis.</li>
</ul>
</div>
<div>
<div class="tk-fig" style="height:258px"><ZoomablePlot src="/figures/fit/witness-null.png" alt="distribution of the fitted witness in pseudo-experiments: world without entanglement versus the expected entangled state" /></div>
<div class="tk-cap"><b>Fitted witness</b> in pseudo-experiments, 1992–1995 simulation: boundary witness null (blue, centred on <LaTeX formula="W=0" />) against the Standard Model state (orange). Red line: the expected value, 1.64.</div>
</div>
</div>

<div class="tk-foot">Null state: constrained fit to the simulation prediction; pseudo-data: Poisson fluctuations of the simulation reweighted to that state. <span class="tk-label sim">simulation</span></div>

<!--
Null construction: c0 = argmin chi2 subject to the null (W <= 0, or |C_kk - C_rr| <= sqrt 2) on the Asimov data; exact projection for the linear witness. Null pseudo-data: the simulation reweighted to c0, event-level Poisson fluctuations; free and constrained fit per toy; test statistic q = chi2_null - chi2_free; p = fraction of null toys with q >= q_expected. 20,000 null toys per test (final model), plus 2 x 4,000 at alternative null points. Every separable two-qubit state has sum_i |C_ii| <= 1, hence W <= 0. Figure: fitted W of the free fit for null toys (sigma 0.234) and Standard-Model-point toys (sigma 0.226); W_expected = 1.6407; the figure's own title quotes Z_A = 7.00 (expected/null-width), made with the one-observable-per-coefficient fit, which gives the same significance as the final model (7.0).
-->
