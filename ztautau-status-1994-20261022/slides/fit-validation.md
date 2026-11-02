---
class: st pres
---

<script setup>
import NJUPlot from '../components/NJUPlot.vue'
</script>

# Validation: the fit returns what was put in, with the right error bars

<div class="fig-lead">
<div><div class="st-fig" style="height:300px"><NJUPlot src="/figures/fit/modelC-pulls.png" alt="pull distributions of the 15 coefficients" /></div><div class="st-cap"><b>Pulls</b> of the 15 coefficients in 2,000 pseudo-experiments (blue: final model; grey: diagonal-only covariance, too narrow errors)</div></div>
<div>
<table class="num first-nw">
<thead><tr><th>Check</th><th>1992–1995</th><th>1994</th></tr></thead>
<tbody>
<tr><td>Closure, 20 injected states</td><td>1.000</td><td>1.000</td></tr>
<tr><td>Pull widths</td><td>0.97–1.03</td><td>0.98–1.03</td></tr>
<tr><td>Covariance vs toys, z spread</td><td>1.003</td><td>0.999</td></tr>
<tr><td>Entries beyond <LaTeX formula="3\sigma" /></td><td>0.27 %</td><td>0.28 %</td></tr>
</tbody>
</table>
<div class="st-cap">Closure = fitted / injected shift. Gaussian expectation beyond <LaTeX formula="3\sigma" />: 0.27 %.</div>
<div class="co ok" style="margin-top:8px"><b>Pull</b> <LaTeX formula="(\text{fitted}-\text{true})/\text{error}" />: width 1 if errors are right.</div>
<div class="co warn"><b>Caveat</b> Pseudo-data reuse the template events.</div>
</div>
</div>

<div class="st-source">Source: final-model validation, combined 1992–1995 and 1994 (2026-10-31); simulation only, statistics only</div>

<!--
artifacts/joint-fit-20261031/modelC/combined-ml/summary.md and modelC/1994_91p2-ml/summary.md. Closure on own pseudo-data at the 18 model-B points (+-1, +-2 sigma on C_kk, C_nn, B_Ak; combined shift; c0 points of A and B) and the 2 model-C null points: fitted/injected 1.000000, max |fitted - injected| 2.9e-12 sigma_A (combined), 4.5e-13 (1994); yields to 3e-13. Pull widths: combined 0.972-1.026 (stat +-0.016, rms deviation from 1 0.018), 1994 0.981-1.026 (5000 toys, rms 0.012). Covariance check: z = (cov_toy - V)/sigma over all 181,200 upper-triangle entries: combined mean +0.047, std 1.003, |z|>3 0.27 %; 1994 mean +0.02, std 0.999, 0.28 % (Gaussian 0.27 %). On step-2 pseudo-data (per-category normalisation n_cat, legacy generator) C still shows an n_cat-driven C_kk bias (+2 sigma: 0.93; W +0.08 at c0(W)); pi-pi category at C_kk(ref) > 1 makes 1/f heavy-tailed. Caveat: MC template statistics not included; toys are fluctuations of the same MC rows that build templates and V. Figure: modelC/combined-ml/pulls_modelC.png (C vs C_diag).
-->
