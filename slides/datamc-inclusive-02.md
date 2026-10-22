---
class: st pres
---

<script setup>
import NJUPlot from '../components/NJUPlot.vue'
</script>

# Inclusive sample: calorimeter response

<div class="st-sub">Inclusive τ-pair sample after all 18 cuts <span class="id">inclusive_1p1p</span> · H0 / H1 = geometric thrust hemispheres, not τ charge · points: data, stack: simulation by true process</div>

<div class="fig2x2">
<div><div class="st-fig"><NJUPlot src="/figures/datamc/inclusive/inclusive_1p1p-selected-exclusive_e_over_p-rate_lin.svg" alt="EM-calorimeter E / p (per measured track)" /></div><div class="st-cap">EM-calorimeter E / p (per measured track)<span class="badge n">no χ²</span></div></div>
<div><div class="st-fig"><NJUPlot src="/figures/datamc/inclusive/inclusive_1p1p-selected-exclusive_hemi0_hcal_mean-rate_lin.svg" alt="H0 hadron-calorimeter mean per hit layer [GeV]" /></div><div class="st-cap">H0 hadron-calorimeter mean per hit layer [GeV]<span class="badge r">χ²/dof 315.1/60</span></div></div>
<div><div class="st-fig"><NJUPlot src="/figures/datamc/inclusive/inclusive_1p1p-selected-exclusive_hemi1_hcal_mean-rate_lin.svg" alt="H1 hadron-calorimeter mean per hit layer [GeV]" /></div><div class="st-cap">H1 hadron-calorimeter mean per hit layer [GeV]<span class="badge r">χ²/dof 548.4/60</span></div></div>
<div><div class="st-fig"><NJUPlot src="/figures/datamc/inclusive/inclusive_1p1p-selected-exclusive_hemi0_hadron_source-rate_lin.svg" alt="H0 hadron-source category" /></div><div class="st-cap">H0 hadron-source category<span class="badge r">χ²/dof 118.5/7</span></div></div>
</div>

<div class="st-source">Source: archived data/MC plot set with the neutral rule applied to the frozen 2026-10-06 selection production</div>

<!--
Figures: artifacts/exclusive-neutral-le3-plots-20261007/plots/ (job 59429001, source 4ae9ef3, neutral count <=3 per hemisphere applied to saved histograms). Black points = 1994 data; stack = signed luminosity-normalised simulation by true process, Z_ee excluded; lower panel = data / simulation. Inclusive sample 23,073 data / 23,198.93 MC. chi2/dof from agreement.json ("Total MC", status ok), statistical only, diagnostic.

-->
