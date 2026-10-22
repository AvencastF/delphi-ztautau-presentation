---
class: st pres
---

<script setup>
import NJUPlot from '../components/NJUPlot.vue'
</script>

# Appendix · child <LaTeX formula="\rho\rho" /> (4/13)

<div class="st-sub">Child <LaTeX formula="\rho\rho" /> <span class="id">inclusive_1p1p_rhorho</span> · order by charge: cand. 0 negative, cand. 1 positive · yield <span class="nw">389 data</span> / <span class="nw">378 simulated</span></div>

<div class="fig2x2">
<div><div class="st-fig"><NJUPlot src="/figures/datamc/children-rhorho/inclusive_1p1p_rhorho-selected-candidate0_photon_p-rate_lin.svg" alt="cand. 0 (rho): nearby photon p [GeV]" /></div><div class="st-cap">cand. 0 (<LaTeX formula="\rho" />): nearby photon <LaTeX formula="p" /> [GeV]<span class="badge n">no <LaTeX formula="\chi^2" /></span></div></div>
<div><div class="st-fig"><NJUPlot src="/figures/datamc/children-rhorho/inclusive_1p1p_rhorho-selected-candidate0_rho_costheta-rate_lin.svg" alt="cand. 0 (rho): rho candidate costheta" /></div><div class="st-cap">cand. 0 (<LaTeX formula="\rho" />): <LaTeX formula="\rho" /> candidate <LaTeX formula="\cos\theta" /><span class="badge a"><LaTeX formula="\chi^2/\mathrm{dof}" /> 52.5 / 32</span></div></div>
<div><div class="st-fig"><NJUPlot src="/figures/datamc/children-rhorho/inclusive_1p1p_rhorho-selected-candidate0_rho_energy-rate_lin.svg" alt="cand. 0 (rho): Erho candidate [GeV]" /></div><div class="st-cap">cand. 0 (<LaTeX formula="\rho" />): <LaTeX formula="E_\rho" /> candidate [GeV]<span class="badge a"><LaTeX formula="\chi^2/\mathrm{dof}" /> 133.1 / 46</span></div></div>
<div><div class="st-fig"><NJUPlot src="/figures/datamc/children-rhorho/inclusive_1p1p_rhorho-selected-candidate0_rho_p-rate_lin.svg" alt="cand. 0 (rho): prho candidate [GeV]" /></div><div class="st-cap">cand. 0 (<LaTeX formula="\rho" />): <LaTeX formula="p_\rho" /> candidate [GeV]<span class="badge a"><LaTeX formula="\chi^2/\mathrm{dof}" /> 136.2 / 46</span></div></div>
</div>

<div class="st-source">Source: archived data/MC plot set with the neutral rule applied to the frozen 2026-10-06 selection production</div>

<!--
Full-precision values are in SOURCES.md and the data folder. Figures: artifacts/exclusive-neutral-le3-plots-20261007/plots/ (job 59429001, source 4ae9ef3, neutral count <=3 per hemisphere applied to saved histograms). Black points = 1994 data; stack = signed luminosity-normalised simulation by true process, Z_ee excluded; lower panel = data / simulation. Inclusive sample 23,073 data / 23,198.93 MC. chi2/dof from agreement.json ("Total MC", status ok), statistical only, diagnostic.

-->
