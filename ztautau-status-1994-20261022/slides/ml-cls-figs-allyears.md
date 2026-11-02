---
class: st pres
---

<script setup>
import ZoomablePlot from 'slidev-addon-ztautau/components/ZoomablePlot.vue'
</script>

# Classifier figures, 1992–1995 hold half

<div class="fig2x2">
<div><div class="st-fig"><ZoomablePlot src="/figures/ml-all-years/cls/02_confusion_purity.svg" alt="confusion matrix, purity view" /></div><div class="st-cap">Confusion matrix, purity view (per predicted class)</div></div>
<div><div class="st-fig"><ZoomablePlot src="/figures/ml-all-years/cls/08_migration.svg" alt="cut-based child to ML class migration" /></div><div class="st-cap">Migration: cut-based child <LaTeX formula="\to" /> ML class, data vs simulation</div></div>
<div><div class="st-fig"><ZoomablePlot src="/figures/ml-all-years/cls/05_efficiency_purity.svg" alt="efficiency and purity per channel" /></div><div class="st-cap">Efficiency and purity per channel, cut-based vs ML</div></div>
<div><div class="st-fig"><ZoomablePlot src="/figures/ml-all-years/cls/06_agreement.svg" alt="data/MC channel yields" /></div><div class="st-cap">Data/simulation channel yields, cut-based vs ML, all years</div></div>
</div>

<div class="st-source">Source: all-years classifier evaluation figures (hold half, 2026-10-27); per-year yield figures in the appendix</div>

<!--
NERSC analysis-runs/1992_1993_1994_1995/all-years-rq-20261026/skim-cls-nu-cls-eval/{svg/02_confusion/purity.svg, 08_migration.svg, 05_efficiency_purity.svg, 06_agreement.svg} (job 60363881), copied to public/figures/ml-all-years/cls/ (MANIFEST.md, sha256 checked against NERSC). Per-year 06_agreement.svg in public/figures/ml-all-years/year-YYYY/ (appendix).
-->
