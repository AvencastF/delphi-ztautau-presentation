---
class: st pres
---

<script setup>
import NJUPlot from '../components/NJUPlot.vue'
</script>

# Appendix · child <LaTeX formula="\pi\pi" /> (3/7)

<div class="st-sub">Child <LaTeX formula="\pi\pi" /> <span class="id">inclusive_1p1p_pipi</span> · order by charge: cand. 0 negative, cand. 1 positive · yield <span class="nw">952 data</span> / <span class="nw">947 simulated</span></div>

<div class="fig2x2">
<div><div class="st-fig"><NJUPlot src="/figures/datamc/children-pipi/inclusive_1p1p_pipi-selected-candidate0_track_mass-rate_lin.svg" alt="cand. 0 (pi): track mass [GeV]" /></div><div class="st-cap">cand. 0 (<LaTeX formula="\pi" />): track mass [GeV]<span class="badge g"><LaTeX formula="\chi^2/\mathrm{dof}" /> 0.0 / 1</span></div></div>
<div><div class="st-fig"><NJUPlot src="/figures/datamc/children-pipi/inclusive_1p1p_pipi-selected-candidate0_track_p-rate_lin.svg" alt="cand. 0 (pi): p [GeV]" /></div><div class="st-cap">cand. 0 (<LaTeX formula="\pi" />): <LaTeX formula="p" /> [GeV]<span class="badge g"><LaTeX formula="\chi^2/\mathrm{dof}" /> 49.3 / 44</span></div></div>
<div><div class="st-fig"><NJUPlot src="/figures/datamc/children-pipi/inclusive_1p1p_pipi-selected-candidate0_truth_species-rate_lin.svg" alt="cand. 0 (pi): true species (simulation)" /></div><div class="st-cap">cand. 0 (<LaTeX formula="\pi" />): true species (simulation)<span class="badge n">no <LaTeX formula="\chi^2" /></span></div></div>
<div><div class="st-fig"><NJUPlot src="/figures/datamc/children-pipi/inclusive_1p1p_pipi-selected-candidate1_neutral_all_count-rate_lin.svg" alt="cand. 1 (pi): all neutrals" /></div><div class="st-cap">cand. 1 (<LaTeX formula="\pi" />): all neutrals<span class="badge g"><LaTeX formula="\chi^2/\mathrm{dof}" /> 4.7 / 4</span></div></div>
</div>

<div class="st-source">Source: archived data/MC plot set with the neutral rule applied to the frozen 2026-10-06 selection production</div>

<!--
Full-precision values are in SOURCES.md and the data folder. Figures: artifacts/exclusive-neutral-le3-plots-20261007/plots/ (job 59429001, source 4ae9ef3, neutral count <=3 per hemisphere applied to saved histograms). Black points = 1994 data; stack = signed luminosity-normalised simulation by true process, Z_ee excluded; lower panel = data / simulation. Inclusive sample 23,073 data / 23,198.93 MC. chi2/dof from agreement.json ("Total MC", status ok), statistical only, diagnostic.

-->
