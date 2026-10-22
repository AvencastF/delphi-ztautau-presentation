---
class: st pres
---

<script setup>
import NJUPlot from '../components/NJUPlot.vue'
</script>

# Appendix · inclusive sample (4/4)

<div class="st-sub">Inclusive τ-pair sample after all 18 cuts <span class="id">inclusive_1p1p</span> · H0 / H1 = geometric thrust hemispheres, not τ charge · points: data, stack: simulation by true process</div>

<div class="fig2x2">
<div><div class="st-fig"><NJUPlot src="/figures/datamc/inclusive/inclusive_1p1p-selected-neutral_combined_identified_photon_dr01_count-rate_lin.svg" alt="identified photons, ΔR<0.1" /></div><div class="st-cap">identified photons, ΔR<0.1<span class="badge n">no χ²</span></div></div>
<div><div class="st-fig"><NJUPlot src="/figures/datamc/inclusive/inclusive_1p1p-selected-neutral_combined_identified_photon_dr05_count-rate_lin.svg" alt="identified photons, ΔR<0.5" /></div><div class="st-cap">identified photons, ΔR<0.5<span class="badge n">no χ²</span></div></div>
<div><div class="st-fig"><NJUPlot src="/figures/datamc/inclusive/inclusive_1p1p-selected-neutral_combined_failed_photon_dr03_count-rate_lin.svg" alt="non-photon neutrals, ΔR<0.3" /></div><div class="st-cap">non-photon neutrals, ΔR<0.3<span class="badge n">no χ²</span></div></div>
</div>

<div class="st-source">Source: archived data/MC plot set with the neutral rule applied to the frozen 2026-10-06 selection production</div>

<!--
Figures: artifacts/exclusive-neutral-le3-plots-20261007/plots/ (job 59429001, source 4ae9ef3, neutral count <=3 per hemisphere applied to saved histograms). Black points = 1994 data; stack = signed luminosity-normalised simulation by true process, Z_ee excluded; lower panel = data / simulation. Inclusive sample 23,073 data / 23,198.93 MC. chi2/dof from agreement.json ("Total MC", status ok), statistical only, diagnostic.

-->
