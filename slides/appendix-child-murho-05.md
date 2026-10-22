---
class: st pres
---

<script setup>
import NJUPlot from '../components/NJUPlot.vue'
</script>

# Appendix · child <LaTeX formula="\mu\rho" /> (5/10)

<div class="st-sub">Child <LaTeX formula="\mu\rho" /> <span class="id">inclusive_1p1p_murho</span> · order by species: cand. 0 = <LaTeX formula="\mu" />, cand. 1 = <LaTeX formula="\rho" /> · yield <span class="nw">1,242 data</span> / <span class="nw">1,211 simulated</span></div>

<div class="fig2x2">
<div><div class="st-fig"><NJUPlot src="/figures/datamc/children-murho/inclusive_1p1p_murho-selected-candidate1_neutral_energy-rate_lin.svg" alt="cand. 1 (rho): neutral-system E [GeV]" /></div><div class="st-cap">cand. 1 (<LaTeX formula="\rho" />): neutral-system <LaTeX formula="E" /> [GeV]<span class="badge r"><LaTeX formula="\chi^2/\mathrm{dof}" /> 159.5 / 46</span></div></div>
<div><div class="st-fig"><NJUPlot src="/figures/datamc/children-murho/inclusive_1p1p_murho-selected-candidate1_neutral_failed_photon_count-rate_lin.svg" alt="cand. 1 (rho): non-photon neutrals" /></div><div class="st-cap">cand. 1 (<LaTeX formula="\rho" />): non-photon neutrals<span class="badge g"><LaTeX formula="\chi^2/\mathrm{dof}" /> 2.1 / 3</span></div></div>
<div><div class="st-fig"><NJUPlot src="/figures/datamc/children-murho/inclusive_1p1p_murho-selected-candidate1_neutral_identified_photon_count-rate_lin.svg" alt="cand. 1 (rho): identified photons" /></div><div class="st-cap">cand. 1 (<LaTeX formula="\rho" />): identified photons<span class="badge g"><LaTeX formula="\chi^2/\mathrm{dof}" /> 3.0 / 3</span></div></div>
<div><div class="st-fig"><NJUPlot src="/figures/datamc/children-murho/inclusive_1p1p_murho-selected-candidate1_neutral_mass-rate_lin.svg" alt="cand. 1 (rho): neutral-system mass [GeV]" /></div><div class="st-cap">cand. 1 (<LaTeX formula="\rho" />): neutral-system mass [GeV]<span class="badge a"><LaTeX formula="\chi^2/\mathrm{dof}" /> 51.0 / 18</span></div></div>
</div>

<div class="st-source">Source: archived data/MC plot set with the neutral rule applied to the frozen 2026-10-06 selection production</div>

<!--
Full-precision values are in SOURCES.md and the data folder. Figures: artifacts/exclusive-neutral-le3-plots-20261007/plots/ (job 59429001, source 4ae9ef3, neutral count <=3 per hemisphere applied to saved histograms). Black points = 1994 data; stack = signed luminosity-normalised simulation by true process, Z_ee excluded; lower panel = data / simulation. Inclusive sample 23,073 data / 23,198.93 MC. chi2/dof from agreement.json ("Total MC", status ok), statistical only, diagnostic.

-->
