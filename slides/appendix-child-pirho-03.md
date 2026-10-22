---
class: st pres
---

<script setup>
import NJUPlot from '../components/NJUPlot.vue'
</script>

# Appendix · child <LaTeX formula="\pi\rho" /> (3/10)

<div class="st-sub">Child <LaTeX formula="\pi\rho" /> <span class="id">inclusive_1p1p_pirho</span> · order by species: cand. 0 = <LaTeX formula="\pi" />, cand. 1 = <LaTeX formula="\rho" /> · yield <span class="nw">1,216 data</span> / <span class="nw">1,190 simulated</span></div>

<div class="fig2x2">
<div><div class="st-fig"><NJUPlot src="/figures/datamc/children-pirho/inclusive_1p1p_pirho-selected-candidate0_track_hcal_mean-rate_lin.svg" alt="cand. 0 (pi): HCAL mean per hit layer [GeV]" /></div><div class="st-cap">cand. 0 (<LaTeX formula="\pi" />): HCAL mean per hit layer [GeV]<span class="badge r"><LaTeX formula="\chi^2/\mathrm{dof}" /> 531.8 / 60</span></div></div>
<div><div class="st-fig"><NJUPlot src="/figures/datamc/children-pirho/inclusive_1p1p_pirho-selected-candidate0_track_mass-rate_lin.svg" alt="cand. 0 (pi): track mass [GeV]" /></div><div class="st-cap">cand. 0 (<LaTeX formula="\pi" />): track mass [GeV]<span class="badge g"><LaTeX formula="\chi^2/\mathrm{dof}" /> 0.6 / 1</span></div></div>
<div><div class="st-fig"><NJUPlot src="/figures/datamc/children-pirho/inclusive_1p1p_pirho-selected-candidate0_track_p-rate_lin.svg" alt="cand. 0 (pi): p [GeV]" /></div><div class="st-cap">cand. 0 (<LaTeX formula="\pi" />): <LaTeX formula="p" /> [GeV]<span class="badge a"><LaTeX formula="\chi^2/\mathrm{dof}" /> 84.8 / 44</span></div></div>
<div><div class="st-fig"><NJUPlot src="/figures/datamc/children-pirho/inclusive_1p1p_pirho-selected-candidate0_truth_species-rate_lin.svg" alt="cand. 0 (pi): true species (simulation)" /></div><div class="st-cap">cand. 0 (<LaTeX formula="\pi" />): true species (simulation)<span class="badge n">no <LaTeX formula="\chi^2" /></span></div></div>
</div>

<div class="st-source">Source: archived data/MC plot set with the neutral rule applied to the frozen 2026-10-06 selection production</div>

<!--
Full-precision values are in SOURCES.md and the data folder. Figures: artifacts/exclusive-neutral-le3-plots-20261007/plots/ (job 59429001, source 4ae9ef3, neutral count <=3 per hemisphere applied to saved histograms). Black points = 1994 data; stack = signed luminosity-normalised simulation by true process, Z_ee excluded; lower panel = data / simulation. Inclusive sample 23,073 data / 23,198.93 MC. chi2/dof from agreement.json ("Total MC", status ok), statistical only, diagnostic.

-->
