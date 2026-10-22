---
class: st pres
---

<script setup>
import NJUPlot from '../components/NJUPlot.vue'
</script>

# Classifier figures (same 2026-10-15 evaluation)

<div class="fig2x2">
<div><div class="st-fig"><NJUPlot src="/figures/ml/classifier/02_confusion_purity.svg" alt="confusion matrix, purity view" /></div><div class="st-cap">Confusion matrix, purity view (per predicted class)</div></div>
<div><div class="st-fig"><NJUPlot src="/figures/ml/classifier/08_migration.svg" alt="cut-based child to ML class migration" /></div><div class="st-cap">Migration: cut-based child → ML class, data vs simulation</div></div>
<div><div class="st-fig"><NJUPlot src="/figures/ml/classifier/05_efficiency_purity.svg" alt="efficiency and purity per channel" /></div><div class="st-cap">Efficiency and purity per channel, cuts vs ML</div></div>
<div><div class="st-fig"><NJUPlot src="/figures/ml/classifier/06_agreement.svg" alt="data/MC channel yields" /></div><div class="st-cap">Data/simulation channel yields, cuts vs ML</div></div>
</div>

<div class="st-source">Source: classifier evaluation figures of 2026-10-15 (optimistic: training events included)</div>

<!--
/Users/avencastmini/Downloads/skim-cls-eval/{svg/02_confusion/purity.svg, 08_migration.svg, 05_efficiency_purity.svg, 06_agreement.svg}; also 02_confusion efficiency view and 04_roc.svg in public/figures/ml/classifier/ (appendix).
-->
