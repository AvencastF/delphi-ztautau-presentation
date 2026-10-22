---
class: st pres
---

<script setup>
import NJUPlot from '../components/NJUPlot.vue'
</script>

# Appendix · child <LaTeX formula="\rho\rho" /> (2/13)

<div class="st-sub">Child <LaTeX formula="\rho\rho" /> <span class="id">inclusive_1p1p_rhorho</span> · order by charge: cand. 0 negative, cand. 1 positive · yield <span class="nw">389 data</span> / <span class="nw">378 simulated</span></div>

<div class="fig2x2">
<div><div class="st-fig"><NJUPlot src="/figures/datamc/children-rhorho/inclusive_1p1p_rhorho-selected-candidate0_neutral_energy-rate_lin.svg" alt="cand. 0 (rho): neutral-system E [GeV]" /></div><div class="st-cap">cand. 0 (<LaTeX formula="\rho" />): neutral-system <LaTeX formula="E" /> [GeV]<span class="badge r"><LaTeX formula="\chi^2/\mathrm{dof}" /> 358.4 / 45</span></div></div>
<div><div class="st-fig"><NJUPlot src="/figures/datamc/children-rhorho/inclusive_1p1p_rhorho-selected-candidate0_neutral_failed_photon_count-rate_lin.svg" alt="cand. 0 (rho): non-photon neutrals" /></div><div class="st-cap">cand. 0 (<LaTeX formula="\rho" />): non-photon neutrals<span class="badge a"><LaTeX formula="\chi^2/\mathrm{dof}" /> 5.2 / 3</span></div></div>
<div><div class="st-fig"><NJUPlot src="/figures/datamc/children-rhorho/inclusive_1p1p_rhorho-selected-candidate0_neutral_identified_photon_count-rate_lin.svg" alt="cand. 0 (rho): identified photons" /></div><div class="st-cap">cand. 0 (<LaTeX formula="\rho" />): identified photons<span class="badge g"><LaTeX formula="\chi^2/\mathrm{dof}" /> 1.9 / 3</span></div></div>
<div><div class="st-fig"><NJUPlot src="/figures/datamc/children-rhorho/inclusive_1p1p_rhorho-selected-candidate0_neutral_mass-rate_lin.svg" alt="cand. 0 (rho): neutral-system mass [GeV]" /></div><div class="st-cap">cand. 0 (<LaTeX formula="\rho" />): neutral-system mass [GeV]<span class="badge r"><LaTeX formula="\chi^2/\mathrm{dof}" /> 88.1 / 17</span></div></div>
</div>

<div class="st-source">Source: archived data/MC plot set with the neutral rule applied to the frozen 2026-10-06 selection production</div>

<!--
Full-precision values are in SOURCES.md and the data folder. Figures: artifacts/exclusive-neutral-le3-plots-20261007/plots/ (job 59429001, source 4ae9ef3, neutral count <=3 per hemisphere applied to saved histograms). Black points = 1994 data; stack = signed luminosity-normalised simulation by true process, Z_ee excluded; lower panel = data / simulation. Inclusive sample 23,073 data / 23,198.93 MC. chi2/dof from agreement.json ("Total MC", status ok), statistical only, diagnostic.

-->
