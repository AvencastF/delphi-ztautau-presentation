---
class: st pres tk
---

<script setup>
import ZoomablePlot from 'slidev-addon-ztautau/components/ZoomablePlot.vue'
</script>

# Backup · fit validation on pseudo-experiments

<div class="tk-split even">
<div><div class="tk-fig" style="height:196px"><ZoomablePlot src="/figures/fit/pulls.png" alt="pull distributions of the 15 coefficients in 2,000 pseudo-experiments" /></div><div class="tk-cap"><b>Pulls</b> of the 15 coefficients, 2,000 pseudo-experiments, 1992–1995. Blue: final model with full covariance; grey outline: diagonal covariance only (too narrow errors for <LaTeX formula="B_k" /> and <LaTeX formula="C_{kk}" />).</div></div>
<div><div class="tk-fig" style="height:196px"><ZoomablePlot src="/figures/fit/correlation.png" alt="correlation matrix of the fitted coefficients: analytic, pseudo-experiments minus analytic, final minus one-observable fit" /></div><div class="tk-cap"><b>Correlations</b> between the 15 coefficients: analytic (left), pseudo-experiments minus analytic (middle, within <LaTeX formula="\pm 0.05" />), final model minus one-observable-per-coefficient fit (right).</div></div>
</div>

<table class="num first-nw" style="margin-top:8px;max-width:640px;font-size:13px">
<thead><tr><th>Check</th><th>1992–1995</th><th>1994</th></tr></thead>
<tbody>
<tr><td>Closure, 20 injected states (fitted / injected)</td><td>1.000</td><td>1.000</td></tr>
<tr><td>Pull widths</td><td>0.97–1.03</td><td>0.98–1.03</td></tr>
<tr><td>Covariance vs pseudo-experiments, <LaTeX formula="z" /> spread</td><td>1.003</td><td>0.999</td></tr>
<tr><td>Largest correlation</td><td><LaTeX formula="C_{nr}" />–<LaTeX formula="C_{rn}" /> <LaTeX formula="-0.35" />; others <LaTeX formula="\le 0.11" /></td><td><LaTeX formula="-0.22" /></td></tr>
</tbody>
</table>

<div class="tk-foot">Pseudo-experiments are Poisson fluctuations of the simulated sample; the finite simulation size is not yet included in the uncertainty. <span class="tk-label sim">simulation</span></div>
