---
class: st pres
---

<script setup>
import ZoomablePlot from 'slidev-addon-ztautau/components/ZoomablePlot.vue'
</script>

# How a template fit works: one histogram, one coefficient

<div class="fig-lead">
<div><div class="st-fig" style="height:300px"><ZoomablePlot src="/figures/fit-explainer/template-ckk.svg" alt="pi-pi histogram of the product of the two k-axis decay angles, prediction for three values of C_kk" /></div><div class="st-cap"><LaTeX formula="\pi\pi" /> events, 1992–1995, ML. Lines: simulation for three values of <LaTeX formula="C_{kk}" />. Points: pseudo-data equal to the simulation, <LaTeX formula="\sqrt N" /> errors.</div></div>
<div>
<ol class="steps" style="font-size:14.5px">
<li><b>Measure</b> a histogram of one decay-angle combination</li>
<li><b>Predict</b> its shape from simulation for any value of the coefficient</li>
<li><b>Compare</b> data and prediction with a <LaTeX formula="\chi^2" /></li>
<li><b>Choose</b> the value with the best agreement; its error comes from how fast the <LaTeX formula="\chi^2" /> grows</li>
</ol>
<div class="co ok"><b>Real fit</b> Same idea, 15 coefficients and 2,400 bins at once.</div>
</div>
</div>

<div class="st-source">Source: templates of the reweighted-template model, combined 1992–1995, ML (2026-10-31); figure made for this deck</div>

<!--
Figure public/figures/fit-explainer/template-ckk.svg, made by data/make_fit_explainer_figs.py from artifacts/joint-fit-20261031/modelB/combined-ml/base_templates.npz: region pipi, observable cos_theta_A_k_times_cos_theta_B_k (the C_kk observable), 10 bins in [-1, 1]; expected(C_kk) = A0 + (C_kk - C_kk_ref) T[C_kk] with C_kk_ref = 1.0307 (pooled MC reference; npz note "expected(delta) = A0 + sum_m delta_m T[m]"); A0 = Asimov (all MC after the fit cut, 670.3 weighted events in this region). Lines for C_kk = -1, 0, 1.03, all other coefficients at the reference; points = A0 with sqrt(N) error bars (Asimov pseudo-data, not real data). The same templates enter model C (final model) with the full covariance; no fit was re-run to make the figure.
-->
