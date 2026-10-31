---
class: st pres
---

<script setup>
import NJUPlot from '../components/NJUPlot.vue'
</script>

# Appendix · 1992–1995 classifier: data/simulation channel yields per year

<div class="fig2x2">
<div><div class="st-fig"><NJUPlot src="/figures/ml-all-years/year-1992/06_agreement.svg" alt="1992 channel yields" /></div><div class="st-cap"><b>1992</b> channel yields, cut-based vs ML</div></div>
<div><div class="st-fig"><NJUPlot src="/figures/ml-all-years/year-1993/06_agreement.svg" alt="1993 channel yields" /></div><div class="st-cap"><b>1993</b></div></div>
<div><div class="st-fig"><NJUPlot src="/figures/ml-all-years/year-1994/06_agreement.svg" alt="1994 channel yields" /></div><div class="st-cap"><b>1994</b></div></div>
<div><div class="st-fig"><NJUPlot src="/figures/ml-all-years/year-1995/06_agreement.svg" alt="1995 channel yields" /></div><div class="st-cap"><b>1995</b></div></div>
</div>

<div class="st-source">Source: per-year classifier evaluations (hold half, 2026-10-27); absolute normalisation, uncertified luminosity</div>

<!--
NERSC analysis-runs/1992_1993_1994_1995/all-years-rq-20261026/skim-cls-nu-cls-eval-year-YYYY/06_agreement.svg (job 60366303, evaluate.py --select year=YYYY, mc_split unseen), copied to public/figures/ml-all-years/year-YYYY/ (MANIFEST.md). Channel-yield chi2/10 per year (ML; classic): 1992 25.5; 56.4 · 1993 21.8; 15.6 · 1994 41.8; 25.2 · 1995 24.3; 39.8 (artifacts/ml-all-years-v1-20261027/cls-eval-year-YYYY.md).
-->
