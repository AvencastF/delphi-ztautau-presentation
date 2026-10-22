---
class: st pres
---

<script setup>
import NJUPlot from '../components/NJUPlot.vue'
</script>

# Appendix · child μμ (5/7)

<div class="st-sub">Child μμ <span class="id">inclusive_1p1p_mumu</span> · ordering by charge: candidate 0 negative, candidate 1 positive · frozen-run yield 1160 data / 1068 simulated</div>

<div class="fig2x2">
<div><div class="st-fig"><NJUPlot src="/figures/datamc/children-mumu/inclusive_1p1p_mumu-selected-candidate1_track_costheta-rate_lin.svg" alt="candidate 1 (μ): track cos θ" /></div><div class="st-cap">candidate 1 (μ): track cos θ<span class="badge a">χ²/dof 58.6/37</span></div></div>
<div><div class="st-fig"><NJUPlot src="/figures/datamc/children-mumu/inclusive_1p1p_mumu-selected-candidate1_track_e_over_p-rate_lin.svg" alt="candidate 1 (μ): EM-calorimeter E / p" /></div><div class="st-cap">candidate 1 (μ): EM-calorimeter E / p<span class="badge a">χ²/dof 93.4/44</span></div></div>
<div><div class="st-fig"><NJUPlot src="/figures/datamc/children-mumu/inclusive_1p1p_mumu-selected-candidate1_track_energy-rate_lin.svg" alt="candidate 1 (μ): track energy [GeV]" /></div><div class="st-cap">candidate 1 (μ): track energy [GeV]<span class="badge g">χ²/dof 41.8/45</span></div></div>
<div><div class="st-fig"><NJUPlot src="/figures/datamc/children-mumu/inclusive_1p1p_mumu-selected-candidate1_track_mass-rate_lin.svg" alt="candidate 1 (μ): track mass [GeV]" /></div><div class="st-cap">candidate 1 (μ): track mass [GeV]<span class="badge r">χ²/dof 7.2/1</span></div></div>
</div>

<div class="st-source">Source: archived data/MC plot set with the neutral rule applied to the frozen 2026-10-06 selection production</div>

<!--
Figures: artifacts/exclusive-neutral-le3-plots-20261007/plots/ (job 59429001, source 4ae9ef3, neutral count <=3 per hemisphere applied to saved histograms). Black points = 1994 data; stack = signed luminosity-normalised simulation by true process, Z_ee excluded; lower panel = data / simulation. Inclusive sample 23,073 data / 23,198.93 MC. chi2/dof from agreement.json ("Total MC", status ok), statistical only, diagnostic.

-->
