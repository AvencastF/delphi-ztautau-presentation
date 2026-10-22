---
class: st pres
---

<script setup>
import NJUPlot from '../components/NJUPlot.vue'
</script>

# Appendix · inclusive sample (2/4)

<div class="st-sub">Inclusive τ-pair sample after all 18 cuts <span class="id">inclusive_1p1p</span> · H0 / H1 = geometric thrust hemispheres, not τ charge · points: data, stack: simulation by true process</div>

<div class="fig2x2">
<div><div class="st-fig"><NJUPlot src="/figures/datamc/inclusive/inclusive_1p1p-selected-exclusive_hemi1_nearby_photon_energy-rate_lin.svg" alt="H1 nearby photon energy [GeV]" /></div><div class="st-cap">H1 nearby photon energy [GeV]<span class="badge n">no χ²</span></div></div>
<div><div class="st-fig"><NJUPlot src="/figures/datamc/inclusive/inclusive_1p1p-selected-exclusive_hemi1_hadron_photon_mass-rate_lin.svg" alt="H1 m(track + photons) [GeV]" /></div><div class="st-cap">H1 m(track + photons) [GeV]<span class="badge r">χ²/dof 527.1/58</span></div></div>
<div><div class="st-fig"><NJUPlot src="/figures/datamc/inclusive/inclusive_1p1p-selected-exclusive_hemi0_nearby_diphoton_mass-rate_lin.svg" alt="H0 diphoton mass [GeV]" /></div><div class="st-cap">H0 diphoton mass [GeV]<span class="badge g">χ²/dof 64.0/50</span></div></div>
<div><div class="st-fig"><NJUPlot src="/figures/datamc/inclusive/inclusive_1p1p-selected-exclusive_hemi1_nearby_diphoton_mass-rate_lin.svg" alt="H1 diphoton mass [GeV]" /></div><div class="st-cap">H1 diphoton mass [GeV]<span class="badge a">χ²/dof 79.0/50</span></div></div>
</div>

<div class="st-source">Source: archived data/MC plot set with the neutral rule applied to the frozen 2026-10-06 selection production</div>

<!--
Figures: artifacts/exclusive-neutral-le3-plots-20261007/plots/ (job 59429001, source 4ae9ef3, neutral count <=3 per hemisphere applied to saved histograms). Black points = 1994 data; stack = signed luminosity-normalised simulation by true process, Z_ee excluded; lower panel = data / simulation. Inclusive sample 23,073 data / 23,198.93 MC. chi2/dof from agreement.json ("Total MC", status ok), statistical only, diagnostic.

-->
