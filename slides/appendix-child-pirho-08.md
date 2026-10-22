---
class: st pres
---

<script setup>
import NJUPlot from '../components/NJUPlot.vue'
</script>

# Appendix · child <LaTeX formula="\pi\rho" /> (8/10)

<div class="st-sub">Child <LaTeX formula="\pi\rho" /> <span class="id">inclusive_1p1p_pirho</span> · order by species: cand. 0 = <LaTeX formula="\pi" />, cand. 1 = <LaTeX formula="\rho" /> · yield <span class="nw">1,216 data</span> / <span class="nw">1,190 simulated</span></div>

<div class="fig2x2">
<div><div class="st-fig"><NJUPlot src="/figures/datamc/children-pirho/inclusive_1p1p_pirho-selected-candidate1_track_costheta-rate_lin.svg" alt="cand. 1 (rho): costheta" /></div><div class="st-cap">cand. 1 (<LaTeX formula="\rho" />): <LaTeX formula="\cos\theta" /><span class="badge g"><LaTeX formula="\chi^2/\mathrm{dof}" /> 40.5 / 34</span></div></div>
<div><div class="st-fig"><NJUPlot src="/figures/datamc/children-pirho/inclusive_1p1p_pirho-selected-candidate1_track_e_over_p-rate_lin.svg" alt="cand. 1 (rho): EM-calorimeter E/p" /></div><div class="st-cap">cand. 1 (<LaTeX formula="\rho" />): EM-calorimeter <LaTeX formula="E/p" /><span class="badge r"><LaTeX formula="\chi^2/\mathrm{dof}" /> 251.5 / 45</span></div></div>
<div><div class="st-fig"><NJUPlot src="/figures/datamc/children-pirho/inclusive_1p1p_pirho-selected-candidate1_track_energy-rate_lin.svg" alt="cand. 1 (rho): track E [GeV]" /></div><div class="st-cap">cand. 1 (<LaTeX formula="\rho" />): track <LaTeX formula="E" /> [GeV]<span class="badge a"><LaTeX formula="\chi^2/\mathrm{dof}" /> 126.5 / 44</span></div></div>
<div><div class="st-fig"><NJUPlot src="/figures/datamc/children-pirho/inclusive_1p1p_pirho-selected-candidate1_track_hcal_mean-rate_lin.svg" alt="cand. 1 (rho): HCAL mean per hit layer [GeV]" /></div><div class="st-cap">cand. 1 (<LaTeX formula="\rho" />): HCAL mean per hit layer [GeV]<span class="badge r"><LaTeX formula="\chi^2/\mathrm{dof}" /> 421.9 / 60</span></div></div>
</div>

<div class="st-source">Source: archived data/MC plot set with the neutral rule applied to the frozen 2026-10-06 selection production</div>

<!--
Full-precision values are in SOURCES.md and the data folder. Figures: artifacts/exclusive-neutral-le3-plots-20261007/plots/ (job 59429001, source 4ae9ef3, neutral count <=3 per hemisphere applied to saved histograms). Black points = 1994 data; stack = signed luminosity-normalised simulation by true process, Z_ee excluded; lower panel = data / simulation. Inclusive sample 23,073 data / 23,198.93 MC. chi2/dof from agreement.json ("Total MC", status ok), statistical only, diagnostic.

-->
