---
class: st pres
---

<script setup>
import NJUPlot from '../components/NJUPlot.vue'
</script>

# Pseudo-experiments: thousands of fake datasets give the error bars

<div class="st-sub">A toy = one fake dataset drawn from the simulation, fitted like real data. The spread of 2,000 toys gives errors; their co-movement, correlations (1992–1995).</div>

<div class="st-fig" style="height:170px"><NJUPlot src="/figures/fit/modelC-correlation.png" alt="correlation matrix of the 15 coefficients" /></div>
<div class="st-cap"><b>Correlations</b> of the 15 coefficients: analytic (left), toys minus analytic (middle, within ±0.05), final minus legacy (right)</div>

<div class="st-cols st-cols-21" style="margin-top:8px">
<table class="num first-nw">
<thead><tr><th>Derived quantity</th><th>Expected</th><th>Analytic <LaTeX formula="\sigma" /></th><th>Toy spread</th><th>Toy 2.5–97.5 %</th></tr></thead>
<tbody>
<tr><td>Witness <LaTeX formula="W" /></td><td>1.64</td><td>0.220</td><td>0.224</td><td>1.20 – 2.10</td></tr>
<tr><td>Concurrence</td><td>0.82</td><td>0.110</td><td>0.112</td><td>0.60 – 1.05</td></tr>
<tr><td>Bell <LaTeX formula="|C_{kk}-C_{rr}|" /></td><td>1.84</td><td>0.189</td><td>0.190</td><td>1.47 – 2.23</td></tr>
</tbody>
</table>
<div>
<div class="co ok"><b>Small</b> Largest correlation <LaTeX formula="C_{nr}" />–<LaTeX formula="C_{rn}" /> −0.35; all others ≤ 0.11.</div>
<div class="co ok"><b>Gaussian</b> Toy spreads match the analytic errors.</div>
</div>
</div>

<div class="st-source">Source: final-model pseudo-experiments, combined 1992–1995 (2026-10-31); simulation only, statistics only</div>

<!--
artifacts/joint-fit-20261031/modelC/combined-ml/summary.md "Event-level SM toys" and "Derived observables": toys use the step-1 seeds (20261031), k_i ~ Poisson(w_i) per MC row, all 15 x 16 x 10 bins refilled coherently (identical pseudo-data for models A, B, C). Correlations: max |toy - GLS| 0.047 (noise 0.022); largest GLS |rho| > 0.1: B_An-C_nk -0.10, B_Ar-C_rk -0.11, C_nn-C_rr -0.10, C_nr-C_rn -0.35 (model A toys: B_i-C_ij +0.15...+0.21, an artefact of A's cross-talk). Derived (nominal; sigma lin GLS; toy std; 2.5-97.5 %): W +1.6407, 0.2200, 0.2243, [+1.2024, +2.0972]; |C_kk - C_rr| +1.8442, 0.1889, 0.1902, [+1.4724, +2.2255]; closed-form concurrence +0.8204, 0.1100, 0.1121, [+0.6012, +1.0486]; lambda_min(rho^T_B) -0.4102, 0.0550, 0.0558; magic +0.1962, 0.1814, 0.1896. Toy fractions: concurrence <= 0: 0; W <= 0: 0; Bell <= sqrt 2: 0.0110. Step 1 (legacy model, 2000 combined / 5000 1994 toys) established toy sigma = likelihood sigma and the legacy-concurrence issue (see caveats slide); figure step1-derived-toys.png in the appendix. 1994: 5000 toys.
-->
