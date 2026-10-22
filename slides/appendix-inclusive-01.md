---
class: st pres
---

<script setup>
import NJUPlot from '../components/NJUPlot.vue'
</script>

# Appendix · inclusive sample (1/4)

<div class="st-sub">Inclusive <LaTeX formula="\tau\tau" /> sample, all 18 cuts <span class="id">inclusive_1p1p</span> · H0 / H1 = thrust hemispheres, not <LaTeX formula="\tau" /> charge · points: data, stack: simulation</div>

<div class="fig2x2">
<div><div class="st-fig"><NJUPlot src="/figures/datamc/inclusive/inclusive_1p1p-selected-leadtrack_hemi0_p-rate_lin.svg" alt="H0 leading-track p [GeV]" /></div><div class="st-cap">H0 leading-track <LaTeX formula="p" /> [GeV]<span class="badge g"><LaTeX formula="\chi^2/\mathrm{dof}" /> 53.5 / 46</span></div></div>
<div><div class="st-fig"><NJUPlot src="/figures/datamc/inclusive/inclusive_1p1p-selected-leadtrack_hemi1_p-rate_lin.svg" alt="H1 leading-track p [GeV]" /></div><div class="st-cap">H1 leading-track <LaTeX formula="p" /> [GeV]<span class="badge g"><LaTeX formula="\chi^2/\mathrm{dof}" /> 64.3 / 46</span></div></div>
<div><div class="st-fig"><NJUPlot src="/figures/datamc/inclusive/inclusive_1p1p-selected-exclusive_nearby_photon_count-rate_lin.svg" alt="identified photons, Delta Rlt 0.3" /></div><div class="st-cap">identified photons, <LaTeX formula="\Delta R\lt 0.3" /><span class="badge n">no <LaTeX formula="\chi^2" /></span></div></div>
<div><div class="st-fig"><NJUPlot src="/figures/datamc/inclusive/inclusive_1p1p-selected-exclusive_hemi1_hadron_source-rate_lin.svg" alt="H1 hadron-source category" /></div><div class="st-cap">H1 hadron-source category<span class="badge r"><LaTeX formula="\chi^2/\mathrm{dof}" /> 214.0 / 7</span></div></div>
</div>

<div class="st-source">Source: archived data/MC plot set with the neutral rule applied to the frozen 2026-10-06 selection production</div>

<!--
Full-precision values are in SOURCES.md and the data folder. Figures: artifacts/exclusive-neutral-le3-plots-20261007/plots/ (job 59429001, source 4ae9ef3, neutral count <=3 per hemisphere applied to saved histograms). Black points = 1994 data; stack = signed luminosity-normalised simulation by true process, Z_ee excluded; lower panel = data / simulation. Inclusive sample 23,073 data / 23,198.93 MC. chi2/dof from agreement.json ("Total MC", status ok), statistical only, diagnostic.

-->
