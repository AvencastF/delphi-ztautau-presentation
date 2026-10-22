---
class: st pres
---

<script setup>
import NJUPlot from '../components/NJUPlot.vue'
</script>

# Appendix · child <LaTeX formula="\mu\rho" /> (4/10)

<div class="st-sub">Child <LaTeX formula="\mu\rho" /> <span class="id">inclusive_1p1p_murho</span> · order by species: cand. 0 = <LaTeX formula="\mu" />, cand. 1 = <LaTeX formula="\rho" /> · yield <span class="nw">1,242 data</span> / <span class="nw">1,211 simulated</span></div>

<div class="fig2x2">
<div><div class="st-fig"><NJUPlot src="/figures/datamc/children-murho/inclusive_1p1p_murho-selected-candidate1_neutral_all_count-rate_lin.svg" alt="cand. 1 (rho): all neutrals" /></div><div class="st-cap">cand. 1 (<LaTeX formula="\rho" />): all neutrals<span class="badge g"><LaTeX formula="\chi^2/\mathrm{dof}" /> 3.2 / 3</span></div></div>
<div><div class="st-fig"><NJUPlot src="/figures/datamc/children-murho/inclusive_1p1p_murho-selected-candidate1_neutral_all_dr03_count-rate_lin.svg" alt="cand. 1 (rho): all neutrals, Delta Rlt 0.3" /></div><div class="st-cap">cand. 1 (<LaTeX formula="\rho" />): all neutrals, <LaTeX formula="\Delta R\lt 0.3" /><span class="badge r"><LaTeX formula="\chi^2/\mathrm{dof}" /> 9.2 / 3</span></div></div>
<div><div class="st-fig"><NJUPlot src="/figures/datamc/children-murho/inclusive_1p1p_murho-selected-candidate1_neutral_costheta-rate_lin.svg" alt="cand. 1 (rho): neutral-system costheta" /></div><div class="st-cap">cand. 1 (<LaTeX formula="\rho" />): neutral-system <LaTeX formula="\cos\theta" /><span class="badge g"><LaTeX formula="\chi^2/\mathrm{dof}" /> 24.3 / 32</span></div></div>
<div><div class="st-fig"><NJUPlot src="/figures/datamc/children-murho/inclusive_1p1p_murho-selected-candidate1_neutral_count-rate_lin.svg" alt="cand. 1 (rho): photons in neutral system" /></div><div class="st-cap">cand. 1 (<LaTeX formula="\rho" />): photons in neutral system<span class="badge g"><LaTeX formula="\chi^2/\mathrm{dof}" /> 2.6 / 2</span></div></div>
</div>

<div class="st-source">Source: archived data/MC plot set with the neutral rule applied to the frozen 2026-10-06 selection production</div>

<!--
Full-precision values are in SOURCES.md and the data folder. Figures: artifacts/exclusive-neutral-le3-plots-20261007/plots/ (job 59429001, source 4ae9ef3, neutral count <=3 per hemisphere applied to saved histograms). Black points = 1994 data; stack = signed luminosity-normalised simulation by true process, Z_ee excluded; lower panel = data / simulation. Inclusive sample 23,073 data / 23,198.93 MC. chi2/dof from agreement.json ("Total MC", status ok), statistical only, diagnostic.

-->
