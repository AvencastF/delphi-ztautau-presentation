---
class: st pres
---

<script setup>
import NJUPlot from '../components/NJUPlot.vue'
</script>

# Appendix · child <LaTeX formula="\mu\pi" /> (3/7)

<div class="st-sub">Child <LaTeX formula="\mu\pi" /> <span class="id">inclusive_1p1p_mupi</span> · order by species: cand. 0 = <LaTeX formula="\mu" />, cand. 1 = <LaTeX formula="\pi" /> · yield <span class="nw">1,912 data</span> / <span class="nw">1,938 simulated</span></div>

<div class="fig2x2">
<div><div class="st-fig"><NJUPlot src="/figures/datamc/children-mupi/inclusive_1p1p_mupi-selected-candidate0_track_hcal_mean-rate_lin.svg" alt="cand. 0 (mu): HCAL mean per hit layer [GeV]" /></div><div class="st-cap">cand. 0 (<LaTeX formula="\mu" />): HCAL mean per hit layer [GeV]<span class="badge r"><LaTeX formula="\chi^2/\mathrm{dof}" /> 174.5 / 27</span></div></div>
<div><div class="st-fig"><NJUPlot src="/figures/datamc/children-mupi/inclusive_1p1p_mupi-selected-candidate0_track_mass-rate_lin.svg" alt="cand. 0 (mu): track mass [GeV]" /></div><div class="st-cap">cand. 0 (<LaTeX formula="\mu" />): track mass [GeV]<span class="badge g"><LaTeX formula="\chi^2/\mathrm{dof}" /> 0.4 / 1</span></div></div>
<div><div class="st-fig"><NJUPlot src="/figures/datamc/children-mupi/inclusive_1p1p_mupi-selected-candidate0_track_p-rate_lin.svg" alt="cand. 0 (mu): p [GeV]" /></div><div class="st-cap">cand. 0 (<LaTeX formula="\mu" />): <LaTeX formula="p" /> [GeV]<span class="badge g"><LaTeX formula="\chi^2/\mathrm{dof}" /> 24.0 / 45</span></div></div>
<div><div class="st-fig"><NJUPlot src="/figures/datamc/children-mupi/inclusive_1p1p_mupi-selected-candidate0_truth_species-rate_lin.svg" alt="cand. 0 (mu): true species (simulation)" /></div><div class="st-cap">cand. 0 (<LaTeX formula="\mu" />): true species (simulation)<span class="badge n">no <LaTeX formula="\chi^2" /></span></div></div>
</div>

<div class="st-source">Source: archived data/MC plot set with the neutral rule applied to the frozen 2026-10-06 selection production</div>

<!--
Full-precision values are in SOURCES.md and the data folder. Figures: artifacts/exclusive-neutral-le3-plots-20261007/plots/ (job 59429001, source 4ae9ef3, neutral count <=3 per hemisphere applied to saved histograms). Black points = 1994 data; stack = signed luminosity-normalised simulation by true process, Z_ee excluded; lower panel = data / simulation. Inclusive sample 23,073 data / 23,198.93 MC. chi2/dof from agreement.json ("Total MC", status ok), statistical only, diagnostic.

-->
