---
class: st pres
---

<script setup>
import NJUPlot from '../components/NJUPlot.vue'
</script>

# Appendix · child <LaTeX formula="e\rho" /> (1/10)

<div class="st-sub">Child <LaTeX formula="e\rho" /> <span class="id">inclusive_1p1p_erho</span> · order by species: cand. 0 = <LaTeX formula="e" />, cand. 1 = <LaTeX formula="\rho" /> · yield <span class="nw">1,076 data</span> / <span class="nw">1,083 simulated</span></div>

<div class="fig2x2">
<div><div class="st-fig"><NJUPlot src="/figures/datamc/children-erho/inclusive_1p1p_erho-selected-candidate0_neutral_all_count-rate_lin.svg" alt="cand. 0 (e): all neutrals" /></div><div class="st-cap">cand. 0 (<LaTeX formula="e" />): all neutrals<span class="badge g"><LaTeX formula="\chi^2/\mathrm{dof}" /> 1.9 / 4</span></div></div>
<div><div class="st-fig"><NJUPlot src="/figures/datamc/children-erho/inclusive_1p1p_erho-selected-candidate0_neutral_all_dr03_count-rate_lin.svg" alt="cand. 0 (e): all neutrals, Delta Rlt 0.3" /></div><div class="st-cap">cand. 0 (<LaTeX formula="e" />): all neutrals, <LaTeX formula="\Delta R\lt 0.3" /><span class="badge g"><LaTeX formula="\chi^2/\mathrm{dof}" /> 3.7 / 4</span></div></div>
<div><div class="st-fig"><NJUPlot src="/figures/datamc/children-erho/inclusive_1p1p_erho-selected-candidate0_neutral_failed_photon_count-rate_lin.svg" alt="cand. 0 (e): non-photon neutrals" /></div><div class="st-cap">cand. 0 (<LaTeX formula="e" />): non-photon neutrals<span class="badge g"><LaTeX formula="\chi^2/\mathrm{dof}" /> 1.7 / 4</span></div></div>
<div><div class="st-fig"><NJUPlot src="/figures/datamc/children-erho/inclusive_1p1p_erho-selected-candidate0_neutral_identified_photon_count-rate_lin.svg" alt="cand. 0 (e): identified photons" /></div><div class="st-cap">cand. 0 (<LaTeX formula="e" />): identified photons<span class="badge r"><LaTeX formula="\chi^2/\mathrm{dof}" /> 32.2 / 4</span></div></div>
</div>

<div class="st-source">Source: archived data/MC plot set with the neutral rule applied to the frozen 2026-10-06 selection production</div>

<!--
Full-precision values are in SOURCES.md and the data folder. Figures: artifacts/exclusive-neutral-le3-plots-20261007/plots/ (job 59429001, source 4ae9ef3, neutral count <=3 per hemisphere applied to saved histograms). Black points = 1994 data; stack = signed luminosity-normalised simulation by true process, Z_ee excluded; lower panel = data / simulation. Inclusive sample 23,073 data / 23,198.93 MC. chi2/dof from agreement.json ("Total MC", status ok), statistical only, diagnostic.

-->
