---
class: st pres
---

<script setup>
import ZoomablePlot from 'slidev-addon-ztautau/components/ZoomablePlot.vue'
</script>

# Appendix · spin fit: legacy-model pseudo-experiments (1992–1995)

<div class="fig2x2">
<div><div class="st-fig"><ZoomablePlot src="/figures/fit/step1-derived-toys.png" alt="step1-derived-toys.png" /></div><div class="st-cap">Derived quantities from 2,000 toys: legacy and Wootters concurrence, best Bell combination, CHSH (biased upward by noise)</div></div>
<div><div class="st-fig"><ZoomablePlot src="/figures/fit/step1-correlation.png" alt="step1-correlation.png" /></div><div class="st-cap">Correlations of the 15 coefficients, legacy model, from toys</div></div>
<div><div class="st-fig"><ZoomablePlot src="/figures/fit/step1-pulls.png" alt="step1-pulls.png" /></div><div class="st-cap">Pulls of the 15 coefficients, legacy model</div></div>
<div><div class="st-fig"><ZoomablePlot src="/figures/fit/step2-Bell-null.png" alt="step2-Bell-null.png" /></div><div class="st-cap">Bell quantity from free fits: null toys vs expected-state toys</div></div>
</div>

<div class="st-source">Source: legacy-model toy studies of 2026-10-31, combined 1992–1995; simulation only, statistics only</div>

<!--
Files: artifacts/joint-fit-20261031/combined-ml/{derived_toy_distributions,correlation_matrix,pulls}.png (step 1: 2000 toys; toy sigma = likelihood sigma within 2.5 %; pull widths 0.975-1.027; legacy concurrence 0.809 +- 0.103, toy median 0.798 [0.697, 0.906]; Wootters toy median 0.634 vs nominal 0.790; CHSH toy median 2.91 vs nominal 2.63 (unphysical values > 2.83: noise bias); 99.2 % of toys give non-PSD rho). step2/combined-ml/Bell_null_distribution.png (null sigma 0.199).
-->
