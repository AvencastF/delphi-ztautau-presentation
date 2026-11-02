---
class: st pres
---

<script setup>
import ZoomablePlot from 'slidev-addon-ztautau/components/ZoomablePlot.vue'
</script>

# Appendix · spin fit: closure and null distributions

<div class="fig2x2">
<div><div class="st-fig"><ZoomablePlot src="/figures/fit/modelC-closure.png" alt="modelC-closure.png" /></div><div class="st-cap">Closure: fitted / injected (left) and largest deviation per injected state (right); final model on its own pseudo-data at 1e-12</div></div>
<div><div class="st-fig"><ZoomablePlot src="/figures/fit/step2-closure-linearity.png" alt="step2-closure-linearity.png" /></div><div class="st-cap">Legacy model: fitted vs injected shift, all vs listed templates reweighted</div></div>
<div><div class="st-fig"><ZoomablePlot src="/figures/fit/step2-q-null-witness.png" alt="step2-q-null-witness.png" /></div><div class="st-cap">Witness and eigenvalue statistics on the same 40,000 null toys, legacy model</div></div>
<div><div class="st-fig"><ZoomablePlot src="/figures/fit/step2-q-null-entanglement.png" alt="step2-q-null-entanglement.png" /></div><div class="st-cap">Eigenvalue test statistic under the null at three separable points, legacy model</div></div>
</div>

<div class="st-source">Source: closure and hypothesis-test studies of 2026-10-31, combined 1992–1995; simulation only, statistics only</div>

<!--
Files: artifacts/joint-fit-20261031/modelC/combined-ml/closure_A_vs_C.png; step2/combined-ml/{closure_linearity,q_null_witness,q_null_entanglement}.png. Legacy closure C_kk 0.96-1.01, B_Ak 1.09 (all reweighted) / 0.99 (listed only), cross-talk ~0.11 sigma per sigma of C_kk. Eigenvalue null: q=0 fraction 0.217, P(q>9) 0.0075 (5.6x half-chi2_1), tail depends on the null point (lowCkk 0.027 q=0). Witness on the same toys: 0.420, shift explained by the closure bias +0.204 sigma_null.
-->
