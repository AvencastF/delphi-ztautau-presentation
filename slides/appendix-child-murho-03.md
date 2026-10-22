---
class: st pres
---

<script setup>
import NJUPlot from '../components/NJUPlot.vue'
</script>

# Appendix · child μρ (3/10)

<div class="st-sub">Child μρ <span class="id">inclusive_1p1p_murho</span> · ordering by identified species: candidate 0 = μ, candidate 1 = ρ · frozen-run yield 1242 data / 1211 simulated</div>

<div class="fig2x2">
<div><div class="st-fig"><NJUPlot src="/figures/datamc/children-murho/inclusive_1p1p_murho-selected-candidate0_track_hcal_mean-rate_lin.svg" alt="candidate 0 (μ): hadron-calorimeter mean per hit layer [GeV]" /></div><div class="st-cap">candidate 0 (μ): hadron-calorimeter mean per hit layer [GeV]<span class="badge r">χ²/dof 199.7/24</span></div></div>
<div><div class="st-fig"><NJUPlot src="/figures/datamc/children-murho/inclusive_1p1p_murho-selected-candidate0_track_mass-rate_lin.svg" alt="candidate 0 (μ): track mass [GeV]" /></div><div class="st-cap">candidate 0 (μ): track mass [GeV]<span class="badge g">χ²/dof 0.8/1</span></div></div>
<div><div class="st-fig"><NJUPlot src="/figures/datamc/children-murho/inclusive_1p1p_murho-selected-candidate0_track_p-rate_lin.svg" alt="candidate 0 (μ): track p [GeV]" /></div><div class="st-cap">candidate 0 (μ): track p [GeV]<span class="badge g">χ²/dof 56.3/45</span></div></div>
<div><div class="st-fig"><NJUPlot src="/figures/datamc/children-murho/inclusive_1p1p_murho-selected-candidate0_truth_species-rate_lin.svg" alt="candidate 0 (μ): true species (simulation)" /></div><div class="st-cap">candidate 0 (μ): true species (simulation)<span class="badge n">no χ²</span></div></div>
</div>

<div class="st-source">Source: archived data/MC plot set with the neutral rule applied to the frozen 2026-10-06 selection production</div>

<!--
Figures: artifacts/exclusive-neutral-le3-plots-20261007/plots/ (job 59429001, source 4ae9ef3, neutral count <=3 per hemisphere applied to saved histograms). Black points = 1994 data; stack = signed luminosity-normalised simulation by true process, Z_ee excluded; lower panel = data / simulation. Inclusive sample 23,073 data / 23,198.93 MC. chi2/dof from agreement.json ("Total MC", status ok), statistical only, diagnostic.

-->
