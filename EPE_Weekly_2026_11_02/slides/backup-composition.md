---
class: st pres tk
---

<script setup>
import ZoomablePlot from 'slidev-addon-ztautau/components/ZoomablePlot.vue'
</script>

# Backup · composition of each selected channel

<div class="st-sub">Column-normalised confusion matrices in simulation (1992–1995, events not used in training): what the events assigned to each channel really are. Diagonal = purity.</div>

<div class="tk-fig" style="height:318px"><ZoomablePlot src="/figures/ml/confusion-purity.svg" alt="column-normalised confusion matrices: cut-based, network, and their difference" /></div>
<div class="tk-cap">Left: cut-based identification. Middle: network. Right: difference. Rows: true process or decay pair, including other single-prong <LaTeX formula="\tau" /> decays and the non-<LaTeX formula="\tau" /> backgrounds; the last column collects events assigned to no channel.</div>

<div class="tk-foot">Simulation only. <span class="tk-label sim">simulation</span></div>
