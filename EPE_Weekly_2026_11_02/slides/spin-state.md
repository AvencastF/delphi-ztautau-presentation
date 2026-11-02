---
class: st pres tk
clicks: 3
---

<script setup>
import SpinState from '../components/SpinState.vue'
</script>

# Full Spin Density Matrix

<div class="st-sub">Six polarisations. Nine correlations.</div>

<SpinState :step="$clicks" />

<!--
rho = 1/4 (1 x 1 + sum_i B^-_i sigma_i x 1 + sum_j B^+_j 1 x sigma_j + sum_ij C_ij sigma_i x sigma_j). Frame: k along the tau flight, r in the production plane, n normal to that plane. 6 + 9 = 15. Classic LEP tau polarisation is B_k (LEP combination A_tau = 0.1439 +- 0.0043, Phys. Rept. 427 (2006) 257) -- notes only. Sketch schematic.
-->
