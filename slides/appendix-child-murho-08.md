---
class: st pres
---

<script setup>
import NJUPlot from '../components/NJUPlot.vue'
</script>

# Appendix · child μρ (8/10)

<div class="st-sub">Child μρ <span class="id">inclusive_1p1p_murho</span> · ordering by identified species: candidate 0 = μ, candidate 1 = ρ · frozen-run yield 1242 data / 1211 simulated</div>

<div class="fig2x2">
<div><div class="st-fig"><NJUPlot src="/figures/datamc/children-murho/inclusive_1p1p_murho-selected-candidate1_track_costheta-rate_lin.svg" alt="candidate 1 (ρ): track cos θ" /></div><div class="st-cap">candidate 1 (ρ): track cos θ<span class="badge g">χ²/dof 34.7/34</span></div></div>
<div><div class="st-fig"><NJUPlot src="/figures/datamc/children-murho/inclusive_1p1p_murho-selected-candidate1_track_e_over_p-rate_lin.svg" alt="candidate 1 (ρ): EM-calorimeter E / p" /></div><div class="st-cap">candidate 1 (ρ): EM-calorimeter E / p<span class="badge r">χ²/dof 196.9/48</span></div></div>
<div><div class="st-fig"><NJUPlot src="/figures/datamc/children-murho/inclusive_1p1p_murho-selected-candidate1_track_energy-rate_lin.svg" alt="candidate 1 (ρ): track energy [GeV]" /></div><div class="st-cap">candidate 1 (ρ): track energy [GeV]<span class="badge g">χ²/dof 63.1/43</span></div></div>
<div><div class="st-fig"><NJUPlot src="/figures/datamc/children-murho/inclusive_1p1p_murho-selected-candidate1_track_hcal_mean-rate_lin.svg" alt="candidate 1 (ρ): hadron-calorimeter mean per hit layer [GeV]" /></div><div class="st-cap">candidate 1 (ρ): hadron-calorimeter mean per hit layer [GeV]<span class="badge r">χ²/dof 625.6/60</span></div></div>
</div>

<div class="st-source">Source: archived data/MC plot set with the neutral rule applied to the frozen 2026-10-06 selection production</div>

<!--
Figures: artifacts/exclusive-neutral-le3-plots-20261007/plots/ (job 59429001, source 4ae9ef3, neutral count <=3 per hemisphere applied to saved histograms). Black points = 1994 data; stack = signed luminosity-normalised simulation by true process, Z_ee excluded; lower panel = data / simulation. Inclusive sample 23,073 data / 23,198.93 MC. chi2/dof from agreement.json ("Total MC", status ok), statistical only, diagnostic.

-->
