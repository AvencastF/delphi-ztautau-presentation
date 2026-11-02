---
class: st pres
---

<script setup>
import ZoomablePlot from 'slidev-addon-ztautau/components/ZoomablePlot.vue'
</script>

# Appendix · spin fit: 1994 studies of the reconstruction and simulation size

<div class="fig2x2">
<div><div class="st-fig"><ZoomablePlot src="/figures/fit/ml1994-analytical-vs-ml.png" alt="ml1994-analytical-vs-ml.png" /></div><div class="st-cap">1994, legacy fit: five reconstruction variants, cut-based to full ML; concurrence 0.34 → 0.16</div></div>
<div><div class="st-fig"><ZoomablePlot src="/figures/fit/ml1994-gain-decomposition.png" alt="ml1994-gain-decomposition.png" /></div><div class="st-cap">1994: per-region error ratio vs cut-based, split into acceptance and per-event information</div></div>
<div><div class="st-fig"><ZoomablePlot src="/figures/fit/mcstat-inflation.png" alt="mcstat-inflation.png" /></div><div class="st-cap">Error growth when simulation statistics enter the fit: 5.5 % with a 20 % cohort, about 1.2 % with all simulation</div></div>
<div><div class="st-fig"><ZoomablePlot src="/figures/fit/allyears-combined.png" alt="allyears-combined.png" /></div><div class="st-cap">1992–1995: coefficient errors per point (faint) and combined (pooled fit and inverse-variance), cut-based vs ML</div></div>
</div>

<div class="st-source">Source: 1994 sensitivity, gain and simulation-statistics studies (2026-10-24/25) and the 1992–1995 pooled legacy fits (2026-10-31); simulation only, statistics only</div>

<!--
Files: artifacts/legacy-fit-ml-20261024/comparison.png (v1-v5: concurrence 0.817 +0.344/-0.334 (v1 all rows), 0.803 +0.342/-0.336 (v2), +0.215/-0.218 (v3 ML region), +0.268/-0.260 (v4 ML nu), +0.157/-0.159 (v5); 20 % held-out cohort), per-region/gain_decomposition.png (combined v5/v2 0.432 = acceptance 0.597 x per-event 0.724), legacy-fit-mcstat-20261025/mcstat_inflation.png (v5 1.0557 geo-mean; predicted 1.0115 with 100 % MC), legacy-fit-ml-allyears-20261030/runs-combined/combined.png (pooled vs IV: within 0.6-3.5 %; 1995_89p4 analytical C_kk clipped scan excluded).
-->
