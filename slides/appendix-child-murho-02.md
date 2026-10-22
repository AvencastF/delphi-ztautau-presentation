---
class: st pres
---

<script setup>
import NJUPlot from '../components/NJUPlot.vue'
</script>

# Appendix · child <LaTeX formula="\mu\rho" /> (2/10)

<div class="st-sub">Child <LaTeX formula="\mu\rho" /> <span class="id">inclusive_1p1p_murho</span> · order by species: cand. 0 = <LaTeX formula="\mu" />, cand. 1 = <LaTeX formula="\rho" /> · yield <span class="nw">1,242 data</span> / <span class="nw">1,211 simulated</span></div>

<div class="fig2x2">
<div><div class="st-fig"><NJUPlot src="/figures/datamc/children-murho/inclusive_1p1p_murho-selected-candidate0_track_charge-rate_lin.svg" alt="cand. 0 (mu): track charge" /></div><div class="st-cap">cand. 0 (<LaTeX formula="\mu" />): track charge<span class="badge g"><LaTeX formula="\chi^2/\mathrm{dof}" /> 0.8 / 2</span></div></div>
<div><div class="st-fig"><NJUPlot src="/figures/datamc/children-murho/inclusive_1p1p_murho-selected-candidate0_track_costheta-rate_lin.svg" alt="cand. 0 (mu): costheta" /></div><div class="st-cap">cand. 0 (<LaTeX formula="\mu" />): <LaTeX formula="\cos\theta" /><span class="badge g"><LaTeX formula="\chi^2/\mathrm{dof}" /> 46.8 / 37</span></div></div>
<div><div class="st-fig"><NJUPlot src="/figures/datamc/children-murho/inclusive_1p1p_murho-selected-candidate0_track_e_over_p-rate_lin.svg" alt="cand. 0 (mu): EM-calorimeter E/p" /></div><div class="st-cap">cand. 0 (<LaTeX formula="\mu" />): EM-calorimeter <LaTeX formula="E/p" /><span class="badge r"><LaTeX formula="\chi^2/\mathrm{dof}" /> 137.4 / 43</span></div></div>
<div><div class="st-fig"><NJUPlot src="/figures/datamc/children-murho/inclusive_1p1p_murho-selected-candidate0_track_energy-rate_lin.svg" alt="cand. 0 (mu): track E [GeV]" /></div><div class="st-cap">cand. 0 (<LaTeX formula="\mu" />): track <LaTeX formula="E" /> [GeV]<span class="badge g"><LaTeX formula="\chi^2/\mathrm{dof}" /> 57.0 / 45</span></div></div>
</div>

<div class="st-source">Source: archived data/MC plot set with the neutral rule applied to the frozen 2026-10-06 selection production</div>

<!--
Full-precision values are in SOURCES.md and the data folder. Figures: artifacts/exclusive-neutral-le3-plots-20261007/plots/ (job 59429001, source 4ae9ef3, neutral count <=3 per hemisphere applied to saved histograms). Black points = 1994 data; stack = signed luminosity-normalised simulation by true process, Z_ee excluded; lower panel = data / simulation. Inclusive sample 23,073 data / 23,198.93 MC. chi2/dof from agreement.json ("Total MC", status ok), statistical only, diagnostic.

-->
