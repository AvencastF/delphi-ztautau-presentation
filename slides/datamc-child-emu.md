---
class: st pres
---

<script setup>
import NJUPlot from '../components/NJUPlot.vue'
</script>

# Child eμ: the four most informative variables

<div class="st-sub">Child eμ <span class="id">inclusive_1p1p_emu</span> · ordering by identified species: candidate 0 = e, candidate 1 = μ · frozen-run yield 1638 data / 1717 simulated</div>

<div class="fig2x2">
<div><div class="st-fig"><NJUPlot src="/figures/datamc/children-emu/inclusive_1p1p_emu-selected-candidate0_track_p_over_pbeam-rate_lin.svg" alt="candidate 0 (e): track p / p_beam" /></div><div class="st-cap">candidate 0 (e): track p / p_beam<span class="badge a">χ²/dof 68.9/42</span></div></div>
<div><div class="st-fig"><NJUPlot src="/figures/datamc/children-emu/inclusive_1p1p_emu-selected-candidate1_track_p_over_pbeam-rate_lin.svg" alt="candidate 1 (μ): track p / p_beam" /></div><div class="st-cap">candidate 1 (μ): track p / p_beam<span class="badge a">χ²/dof 80.4/41</span></div></div>
<div><div class="st-fig"><NJUPlot src="/figures/datamc/children-emu/inclusive_1p1p_emu-selected-candidate0_track_e_over_p-rate_lin.svg" alt="candidate 0 (e): EM-calorimeter E / p" /></div><div class="st-cap">candidate 0 (e): EM-calorimeter E / p<span class="badge r">χ²/dof 382.0/58</span></div></div>
<div><div class="st-fig"><NJUPlot src="/figures/datamc/children-emu/inclusive_1p1p_emu-selected-candidate1_track_hcal_mean-rate_lin.svg" alt="candidate 1 (μ): hadron-calorimeter mean per hit layer [GeV]" /></div><div class="st-cap">candidate 1 (μ): hadron-calorimeter mean per hit layer [GeV]<span class="badge r">χ²/dof 119.6/25</span></div></div>
</div>

<div class="st-source">Source: archived data/MC plot set with the neutral rule applied to the frozen 2026-10-06 selection production</div>

<!--
Figures: artifacts/exclusive-neutral-le3-plots-20261007/plots/ (job 59429001, source 4ae9ef3, neutral count <=3 per hemisphere applied to saved histograms). Black points = 1994 data; stack = signed luminosity-normalised simulation by true process, Z_ee excluded; lower panel = data / simulation. Inclusive sample 23,073 data / 23,198.93 MC. chi2/dof from agreement.json ("Total MC", status ok), statistical only, diagnostic.
Exact signed MC yield 1717.109015 (Z_ee excluded). Four variables chosen: p/p_beam of both candidates plus the two channel-specific calorimeter / photon variables.
-->
