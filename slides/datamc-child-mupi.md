---
class: st pres
---

<script setup>
import NJUPlot from '../components/NJUPlot.vue'
</script>

# Child μπ: the four most informative variables

<div class="st-sub">Child μπ <span class="id">inclusive_1p1p_mupi</span> · ordering by identified species: candidate 0 = μ, candidate 1 = π · frozen-run yield 1912 data / 1938 simulated</div>

<div class="fig2x2">
<div><div class="st-fig"><NJUPlot src="/figures/datamc/children-mupi/inclusive_1p1p_mupi-selected-candidate0_track_p_over_pbeam-rate_lin.svg" alt="candidate 0 (μ): track p / p_beam" /></div><div class="st-cap">candidate 0 (μ): track p / p_beam<span class="badge g">χ²/dof 35.2/41</span></div></div>
<div><div class="st-fig"><NJUPlot src="/figures/datamc/children-mupi/inclusive_1p1p_mupi-selected-candidate1_track_p_over_pbeam-rate_lin.svg" alt="candidate 1 (π): track p / p_beam" /></div><div class="st-cap">candidate 1 (π): track p / p_beam<span class="badge a">χ²/dof 99.1/40</span></div></div>
<div><div class="st-fig"><NJUPlot src="/figures/datamc/children-mupi/inclusive_1p1p_mupi-selected-candidate1_track_e_over_p-rate_lin.svg" alt="candidate 1 (π): EM-calorimeter E / p" /></div><div class="st-cap">candidate 1 (π): EM-calorimeter E / p<span class="badge r">χ²/dof 516.5/60</span></div></div>
<div><div class="st-fig"><NJUPlot src="/figures/datamc/children-mupi/inclusive_1p1p_mupi-selected-candidate1_track_hcal_mean-rate_lin.svg" alt="candidate 1 (π): hadron-calorimeter mean per hit layer [GeV]" /></div><div class="st-cap">candidate 1 (π): hadron-calorimeter mean per hit layer [GeV]<span class="badge r">χ²/dof 556.0/60</span></div></div>
</div>

<div class="st-source">Source: archived data/MC plot set with the neutral rule applied to the frozen 2026-10-06 selection production</div>

<!--
Figures: artifacts/exclusive-neutral-le3-plots-20261007/plots/ (job 59429001, source 4ae9ef3, neutral count <=3 per hemisphere applied to saved histograms). Black points = 1994 data; stack = signed luminosity-normalised simulation by true process, Z_ee excluded; lower panel = data / simulation. Inclusive sample 23,073 data / 23,198.93 MC. chi2/dof from agreement.json ("Total MC", status ok), statistical only, diagnostic.
Exact signed MC yield 1938.235467 (Z_ee excluded). Four variables chosen: p/p_beam of both candidates plus the two channel-specific calorimeter / photon variables.
-->
