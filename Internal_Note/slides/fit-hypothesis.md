---
class: st pres
---

<script setup>
import ZoomablePlot from 'slidev-addon-ztautau/components/ZoomablePlot.vue'
</script>

# Testing entanglement: could a world without it produce our result?

<div class="st-cols st-cols-2">
<div>
<ol class="steps" style="font-size:14px">
<li><b>Null hypothesis</b>: the non-entangled spin state closest to what we measure</li>
<li><b>Fake experiments</b>: 20,000 datasets drawn from that world, each fitted like data</li>
<li><b>p-value</b>: fraction of them that look at least as entangled as ours</li>
</ol>
<div class="co decision"><b>Witness</b> <LaTeX formula="W=C_{nn}-C_{rr}+C_{kk}-1" /> is a straight line in the coefficients.</div>
<div class="co ok"><b>Why it works</b> Every non-entangled state has <LaTeX formula="W\le 0" />: <LaTeX formula="W\gt 0" /> proves entanglement.</div>
<div class="co ok"><b>Bell</b> Same recipe with <LaTeX formula="|C_{kk}-C_{rr}|\le\sqrt2" /> as the null.</div>
</div>
<div>
<div class="st-fig" style="height:250px"><ZoomablePlot src="/figures/fit/step2-W-null.png" alt="witness from fits: no-entanglement fake experiments vs expected" /></div>
<div class="st-cap"><b>Witness</b> from fits to fake experiments, 1992–1995: world without entanglement (blue) vs the expected entangled state (orange); legacy fit model</div>
</div>
</div>

<div class="st-source">Source: hypothesis-test studies of 2026-10-31 (witness test, owner decision); simulation only, statistics only</div>

<!--
Null construction: c0 = argmin chi^2 subject to the null (W <= 0; |C_kk - C_rr| <= sqrt 2), on the SM Asimov data; for model C the exact projection c0 = c_hat - g F^-1 a / (a^T F^-1 a). Null pseudo-data: simulation reweighted to c0, event-level Poisson; free and constrained fit per toy; test statistic q = chi2_null - chi2_free; p-value = fraction of null toys with q >= q_observed (model C: 20,000 null toys per test, + 4,000 x 2 at alternative null points; legacy model A step 2: 40,000). Witness: W = C_nn - C_rr + C_kk - 1 (owner decision 2026-10-31: headline entanglement test, eigenvalue test lambda_min(rho^T_B) as cross-check); every separable two-qubit state has sum_i |C_ii| <= 1, so W <= 0 (step2/combined-ml/witness_summary.md). Figure: artifacts/joint-fit-20261031/step2/combined-ml/W_null_distribution.png (legacy model A; null sigma 0.2344, SM-toy sigma 0.2256, Z_A = 7.00). The q-distribution comparison (q = 0 fraction, tail) of the previous version is in the appendix.
-->
