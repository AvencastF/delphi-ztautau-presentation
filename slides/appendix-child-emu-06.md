---
class: st pres
---

<script setup>
import NJUPlot from '../components/NJUPlot.vue'
</script>

# Appendix · child eμ (6/7)

<div class="st-sub">Child eμ <span class="id">inclusive_1p1p_emu</span> · ordering by identified species: candidate 0 = e, candidate 1 = μ · frozen-run yield 1638 data / 1717 simulated</div>

<div class="fig2x2">
<div><div class="st-fig"><NJUPlot src="/figures/datamc/children-emu/inclusive_1p1p_emu-selected-candidate1_track_p-rate_lin.svg" alt="candidate 1 (μ): track p [GeV]" /></div><div class="st-cap">candidate 1 (μ): track p [GeV]<span class="badge r">χ²/dof 179.1/45</span></div></div>
<div><div class="st-fig"><NJUPlot src="/figures/datamc/children-emu/inclusive_1p1p_emu-selected-candidate1_truth_species-rate_lin.svg" alt="candidate 1 (μ): true species (simulation)" /></div><div class="st-cap">candidate 1 (μ): true species (simulation)<span class="badge n">no χ²</span></div></div>
<div><div class="st-fig"><NJUPlot src="/figures/datamc/children-emu/inclusive_1p1p_emu-selected-erad_over_ebeam-rate_lin.svg" alt="radiative EM energy / E_beam" /></div><div class="st-cap">radiative EM energy / E_beam<span class="badge r">χ²/dof 211.9/20</span></div></div>
<div><div class="st-fig"><NJUPlot src="/figures/datamc/children-emu/inclusive_1p1p_emu-selected-identified_order_state-rate_lin.svg" alt="candidate-ordering state" /></div><div class="st-cap">candidate-ordering state<span class="badge r">χ²/dof 3.7/1</span></div></div>
</div>

<div class="st-source">Source: archived data/MC plot set with the neutral rule applied to the frozen 2026-10-06 selection production</div>

<!--
Figures: artifacts/exclusive-neutral-le3-plots-20261007/plots/ (job 59429001, source 4ae9ef3, neutral count <=3 per hemisphere applied to saved histograms). Black points = 1994 data; stack = signed luminosity-normalised simulation by true process, Z_ee excluded; lower panel = data / simulation. Inclusive sample 23,073 data / 23,198.93 MC. chi2/dof from agreement.json ("Total MC", status ok), statistical only, diagnostic.

-->
