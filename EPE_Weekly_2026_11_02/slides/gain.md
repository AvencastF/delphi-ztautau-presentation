---
class: st pres tk
clicks: 2
---

<script setup>
import GainBars from '../components/GainBars.vue'
</script>

# Reconstruction impact on spin sensitivity

<div class="st-sub">Conventional and EveNet reconstruction · expected concurrence uncertainty</div>

<GainBars :step="$clicks" />

<div class="tk-foot">Expected, statistical uncertainties only, log scale. <span class="tk-label sim">simulation</span> Legacy-fit comparison; separate from the joint-fit precision shown previously.</div>

<!--
Per-point concurrence sigma cut / ML: 1992 0.58/0.25; 1993 2.12/0.74, 0.69/0.28, 2.20/0.71; 1994 0.34/0.16; 1995 2.36/0.71, 0.74/0.29, 2.19/0.66; combined 0.21/0.10. Geometric-mean coefficient ratio 0.43 -> (1/0.43)^2 = 5.4.
-->
