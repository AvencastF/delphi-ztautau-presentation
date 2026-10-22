---
class: st pres
---

<script setup>
import NJUPlot from '../components/NJUPlot.vue'
</script>

# Appendix · child <LaTeX formula="\rho\rho" /> (6/13)

<div class="st-sub">Child <LaTeX formula="\rho\rho" /> <span class="id">inclusive_1p1p_rhorho</span> · order by charge: cand. 0 negative, cand. 1 positive · yield <span class="nw">389 data</span> / <span class="nw">378 simulated</span></div>

<div class="fig2x2">
<div><div class="st-fig"><NJUPlot src="/figures/datamc/children-rhorho/inclusive_1p1p_rhorho-selected-candidate0_track_hcal_mean-rate_lin.svg" alt="cand. 0 (rho): HCAL mean per hit layer [GeV]" /></div><div class="st-cap">cand. 0 (<LaTeX formula="\rho" />): HCAL mean per hit layer [GeV]<span class="badge r"><LaTeX formula="\chi^2/\mathrm{dof}" /> 591.9 / 58</span></div></div>
<div><div class="st-fig"><NJUPlot src="/figures/datamc/children-rhorho/inclusive_1p1p_rhorho-selected-candidate0_track_mass-rate_lin.svg" alt="cand. 0 (rho): track mass [GeV]" /></div><div class="st-cap">cand. 0 (<LaTeX formula="\rho" />): track mass [GeV]<span class="badge g"><LaTeX formula="\chi^2/\mathrm{dof}" /> 0.3 / 1</span></div></div>
<div><div class="st-fig"><NJUPlot src="/figures/datamc/children-rhorho/inclusive_1p1p_rhorho-selected-candidate0_track_p-rate_lin.svg" alt="cand. 0 (rho): p [GeV]" /></div><div class="st-cap">cand. 0 (<LaTeX formula="\rho" />): <LaTeX formula="p" /> [GeV]<span class="badge r"><LaTeX formula="\chi^2/\mathrm{dof}" /> 166.3 / 43</span></div></div>
<div><div class="st-fig"><NJUPlot src="/figures/datamc/children-rhorho/inclusive_1p1p_rhorho-selected-candidate0_truth_species-rate_lin.svg" alt="cand. 0 (rho): true species (simulation)" /></div><div class="st-cap">cand. 0 (<LaTeX formula="\rho" />): true species (simulation)<span class="badge n">no <LaTeX formula="\chi^2" /></span></div></div>
</div>

<div class="st-source">Source: archived data/MC plot set with the neutral rule applied to the frozen 2026-10-06 selection production</div>

<!--
Full-precision values are in SOURCES.md and the data folder. Figures: artifacts/exclusive-neutral-le3-plots-20261007/plots/ (job 59429001, source 4ae9ef3, neutral count <=3 per hemisphere applied to saved histograms). Black points = 1994 data; stack = signed luminosity-normalised simulation by true process, Z_ee excluded; lower panel = data / simulation. Inclusive sample 23,073 data / 23,198.93 MC. chi2/dof from agreement.json ("Total MC", status ok), statistical only, diagnostic.

-->
