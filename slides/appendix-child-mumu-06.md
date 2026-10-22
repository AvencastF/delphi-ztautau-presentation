---
class: st pres
---

<script setup>
import NJUPlot from '../components/NJUPlot.vue'
</script>

# Appendix · child <LaTeX formula="\mu\mu" /> (6/7)

<div class="st-sub">Child <LaTeX formula="\mu\mu" /> <span class="id">inclusive_1p1p_mumu</span> · order by charge: cand. 0 negative, cand. 1 positive · yield <span class="nw">1,160 data</span> / <span class="nw">1,068 simulated</span></div>

<div class="fig2x2">
<div><div class="st-fig"><NJUPlot src="/figures/datamc/children-mumu/inclusive_1p1p_mumu-selected-candidate1_track_p-rate_lin.svg" alt="cand. 1 (mu): p [GeV]" /></div><div class="st-cap">cand. 1 (<LaTeX formula="\mu" />): <LaTeX formula="p" /> [GeV]<span class="badge g"><LaTeX formula="\chi^2/\mathrm{dof}" /> 41.8 / 45</span></div></div>
<div><div class="st-fig"><NJUPlot src="/figures/datamc/children-mumu/inclusive_1p1p_mumu-selected-candidate1_truth_species-rate_lin.svg" alt="cand. 1 (mu): true species (simulation)" /></div><div class="st-cap">cand. 1 (<LaTeX formula="\mu" />): true species (simulation)<span class="badge n">no <LaTeX formula="\chi^2" /></span></div></div>
<div><div class="st-fig"><NJUPlot src="/figures/datamc/children-mumu/inclusive_1p1p_mumu-selected-erad_over_ebeam-rate_lin.svg" alt="Emathrmrad/Emathrmbeam" /></div><div class="st-cap"><LaTeX formula="E_\mathrm{rad}/E_\mathrm{beam}" /><span class="badge g"><LaTeX formula="\chi^2/\mathrm{dof}" /> 20.2 / 20</span></div></div>
<div><div class="st-fig"><NJUPlot src="/figures/datamc/children-mumu/inclusive_1p1p_mumu-selected-identified_order_state-rate_lin.svg" alt="candidate-ordering state" /></div><div class="st-cap">candidate-ordering state<span class="badge r"><LaTeX formula="\chi^2/\mathrm{dof}" /> 7.4 / 2</span></div></div>
</div>

<div class="st-source">Source: archived data/MC plot set with the neutral rule applied to the frozen 2026-10-06 selection production</div>

<!--
Full-precision values are in SOURCES.md and the data folder. Figures: artifacts/exclusive-neutral-le3-plots-20261007/plots/ (job 59429001, source 4ae9ef3, neutral count <=3 per hemisphere applied to saved histograms). Black points = 1994 data; stack = signed luminosity-normalised simulation by true process, Z_ee excluded; lower panel = data / simulation. Inclusive sample 23,073 data / 23,198.93 MC. chi2/dof from agreement.json ("Total MC", status ok), statistical only, diagnostic.

-->
