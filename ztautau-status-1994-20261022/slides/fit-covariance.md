---
class: st pres
---

<script setup>
import ZoomablePlot from 'slidev-addon-ztautau/components/ZoomablePlot.vue'
</script>

# Why a covariance: every event fills all 15 histograms

<div class="fig-lead">
<div><div class="st-fig" style="height:280px"><ZoomablePlot src="/figures/fit-explainer/pull-widths.svg" alt="pull width per coefficient, Poisson per histogram vs full covariance" /></div><div class="st-cap"><b>Pull width</b> per coefficient in 2,000 pseudo-experiments, 1992–1995. Correct errors give 1.</div></div>
<div>
<div class="co warn"><b>Naive</b> Each histogram treated as independent counts every event up to 15 times.</div>
<div class="co warn"><b>Result</b> Quoted errors too small: pulls up to 2.3 wide.</div>
<div class="co ok"><b>Fix</b> Bin-to-bin covariance from the events themselves: widths 0.97–1.03.</div>
<div class="co ok"><b>Bonus</b> Using the correlations makes errors up to 6 % smaller than the legacy fit.</div>
</div>
</div>

<div class="st-source">Source: Poisson-template and full-covariance model studies, combined 1992–1995 (2026-10-31); simulation only, statistics only</div>

<!--
Figure public/figures/fit-explainer/pull-widths.svg (data/make_fit_explainer_figs.py) from artifacts/joint-fit-20261031/modelB/combined-ml/summary.md column "pull std B" (model B: reweighted templates, product Poisson likelihood over the 15 histograms) and modelC/combined-ml/summary.md column "C pull std" (model C: full covariance), identical event-level SM toys (2000, seeds 20261031). Model B pull widths: C_kk 2.283, B_Ak 2.220, B_Bk 2.188, C_nn 1.189, C_rr 1.183, others 0.98-1.05; model C 0.972-1.026 (stat +-0.016). 1994: B C_kk 2.29. Pull = (fitted - injected) / quoted error. Precision: sigma_C / sigma_A (HESSE) 0.936-0.988 for 13 coefficients, C_nr 1.066 and C_rn 1.065 (real C_nr-C_rn correlation -0.35 that model A ignores); "up to 6 %" = 1 - 0.936. Covariance V_ab = sum_i w_i 1[i in a] 1[i in b] (Poisson per event). Full three-model table and error ratios: appendix.
-->
