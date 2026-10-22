---
class: st pres
---

<script setup>
import NJUPlot from '../components/NJUPlot.vue'
</script>

# Appendix · child <LaTeX formula="\rho\rho" /> (1/13)

<div class="st-sub">Child <LaTeX formula="\rho\rho" /> <span class="id">inclusive_1p1p_rhorho</span> · order by charge: cand. 0 negative, cand. 1 positive · yield <span class="nw">389 data</span> / <span class="nw">378 simulated</span></div>

<div class="fig2x2">
<div><div class="st-fig"><NJUPlot src="/figures/datamc/children-rhorho/inclusive_1p1p_rhorho-selected-candidate0_neutral_all_count-rate_lin.svg" alt="cand. 0 (rho): all neutrals" /></div><div class="st-cap">cand. 0 (<LaTeX formula="\rho" />): all neutrals<span class="badge g"><LaTeX formula="\chi^2/\mathrm{dof}" /> 1.8 / 3</span></div></div>
<div><div class="st-fig"><NJUPlot src="/figures/datamc/children-rhorho/inclusive_1p1p_rhorho-selected-candidate0_neutral_all_dr03_count-rate_lin.svg" alt="cand. 0 (rho): all neutrals, Delta Rlt 0.3" /></div><div class="st-cap">cand. 0 (<LaTeX formula="\rho" />): all neutrals, <LaTeX formula="\Delta R\lt 0.3" /><span class="badge g"><LaTeX formula="\chi^2/\mathrm{dof}" /> 1.8 / 3</span></div></div>
<div><div class="st-fig"><NJUPlot src="/figures/datamc/children-rhorho/inclusive_1p1p_rhorho-selected-candidate0_neutral_costheta-rate_lin.svg" alt="cand. 0 (rho): neutral-system costheta" /></div><div class="st-cap">cand. 0 (<LaTeX formula="\rho" />): neutral-system <LaTeX formula="\cos\theta" /><span class="badge a"><LaTeX formula="\chi^2/\mathrm{dof}" /> 54.8 / 32</span></div></div>
<div><div class="st-fig"><NJUPlot src="/figures/datamc/children-rhorho/inclusive_1p1p_rhorho-selected-candidate0_neutral_count-rate_lin.svg" alt="cand. 0 (rho): photons in neutral system" /></div><div class="st-cap">cand. 0 (<LaTeX formula="\rho" />): photons in neutral system<span class="badge g"><LaTeX formula="\chi^2/\mathrm{dof}" /> 2.2 / 2</span></div></div>
</div>

<div class="st-source">Source: archived data/MC plot set with the neutral rule applied to the frozen 2026-10-06 selection production</div>

<!--
Full-precision values are in SOURCES.md and the data folder. Figures: artifacts/exclusive-neutral-le3-plots-20261007/plots/ (job 59429001, source 4ae9ef3, neutral count <=3 per hemisphere applied to saved histograms). Black points = 1994 data; stack = signed luminosity-normalised simulation by true process, Z_ee excluded; lower panel = data / simulation. Inclusive sample 23,073 data / 23,198.93 MC. chi2/dof from agreement.json ("Total MC", status ok), statistical only, diagnostic.

-->
