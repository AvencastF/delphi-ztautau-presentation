---
class: st pres
---

<script setup>
import NJUPlot from '../components/NJUPlot.vue'
</script>

# Appendix · child <LaTeX formula="\mu\pi" /> (4/7)

<div class="st-sub">Child <LaTeX formula="\mu\pi" /> <span class="id">inclusive_1p1p_mupi</span> · order by species: cand. 0 = <LaTeX formula="\mu" />, cand. 1 = <LaTeX formula="\pi" /> · yield <span class="nw">1,912 data</span> / <span class="nw">1,938 simulated</span></div>

<div class="fig2x2">
<div><div class="st-fig"><NJUPlot src="/figures/datamc/children-mupi/inclusive_1p1p_mupi-selected-candidate1_neutral_all_count-rate_lin.svg" alt="cand. 1 (pi): all neutrals" /></div><div class="st-cap">cand. 1 (<LaTeX formula="\pi" />): all neutrals<span class="badge g"><LaTeX formula="\chi^2/\mathrm{dof}" /> 1.5 / 4</span></div></div>
<div><div class="st-fig"><NJUPlot src="/figures/datamc/children-mupi/inclusive_1p1p_mupi-selected-candidate1_neutral_all_dr03_count-rate_lin.svg" alt="cand. 1 (pi): all neutrals, Delta Rlt 0.3" /></div><div class="st-cap">cand. 1 (<LaTeX formula="\pi" />): all neutrals, <LaTeX formula="\Delta R\lt 0.3" /><span class="badge g"><LaTeX formula="\chi^2/\mathrm{dof}" /> 5.7 / 4</span></div></div>
<div><div class="st-fig"><NJUPlot src="/figures/datamc/children-mupi/inclusive_1p1p_mupi-selected-candidate1_neutral_failed_photon_count-rate_lin.svg" alt="cand. 1 (pi): non-photon neutrals" /></div><div class="st-cap">cand. 1 (<LaTeX formula="\pi" />): non-photon neutrals<span class="badge g"><LaTeX formula="\chi^2/\mathrm{dof}" /> 2.6 / 4</span></div></div>
<div><div class="st-fig"><NJUPlot src="/figures/datamc/children-mupi/inclusive_1p1p_mupi-selected-candidate1_neutral_identified_photon_count-rate_lin.svg" alt="cand. 1 (pi): identified photons" /></div><div class="st-cap">cand. 1 (<LaTeX formula="\pi" />): identified photons<span class="badge r"><LaTeX formula="\chi^2/\mathrm{dof}" /> 26.5 / 3</span></div></div>
</div>

<div class="st-source">Source: archived data/MC plot set with the neutral rule applied to the frozen 2026-10-06 selection production</div>

<!--
Full-precision values are in SOURCES.md and the data folder. Figures: artifacts/exclusive-neutral-le3-plots-20261007/plots/ (job 59429001, source 4ae9ef3, neutral count <=3 per hemisphere applied to saved histograms). Black points = 1994 data; stack = signed luminosity-normalised simulation by true process, Z_ee excluded; lower panel = data / simulation. Inclusive sample 23,073 data / 23,198.93 MC. chi2/dof from agreement.json ("Total MC", status ok), statistical only, diagnostic.

-->
