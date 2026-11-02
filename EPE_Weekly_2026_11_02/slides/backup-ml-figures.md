---
class: st pres tk
---

<script setup>
import ZoomablePlot from 'slidev-addon-ztautau/components/ZoomablePlot.vue'
</script>

# Backup · network-assigned channels in data and simulation

<div class="st-sub">Top: where simulated events of each true decay pair end up (both methods, network only, cut-based only, neither). Middle: purity and yield of each subset. Bottom: data / simulation of each subset.</div>

<div class="tk-fig" style="height:330px"><ZoomablePlot src="/figures/ml/channel-agreement.svg" alt="agreement of cut-based and network channel assignment: migration, purity and data over simulation per channel" /></div>
<div class="tk-cap">Data / simulation of the network-assigned channels is within 5–15 % of one; the 1994 <LaTeX formula="\rho" /> channels (0.94), the 1992 <LaTeX formula="\pi\pi" /> channel (1.24) and the 1995 <LaTeX formula="ee" /> channel (0.85) are the open items, linked to the photon calibration.</div>

<div class="tk-foot">All years. Yields are data events; the simulation is normalised to the luminosity.</div>
