---
class: st pres
---

<script setup>
import NJUPlot from '../components/NJUPlot.vue'
</script>

# Child ee: the four most informative variables

<div class="st-sub">Child ee <span class="id">inclusive_1p1p_ee</span> · ordering by charge: candidate 0 negative, candidate 1 positive · frozen-run yield 882 data / 897 simulated</div>

<div class="fig2x2">
<div><div class="st-fig"><NJUPlot src="/figures/datamc/children-ee/inclusive_1p1p_ee-selected-candidate0_track_p_over_pbeam-rate_lin.svg" alt="candidate 0 (e): track p / p_beam" /></div><div class="st-cap">candidate 0 (e): track p / p_beam<span class="badge g">χ²/dof 42.8/42</span></div></div>
<div><div class="st-fig"><NJUPlot src="/figures/datamc/children-ee/inclusive_1p1p_ee-selected-candidate1_track_p_over_pbeam-rate_lin.svg" alt="candidate 1 (e): track p / p_beam" /></div><div class="st-cap">candidate 1 (e): track p / p_beam<span class="badge a">χ²/dof 88.0/42</span></div></div>
<div><div class="st-fig"><NJUPlot src="/figures/datamc/children-ee/inclusive_1p1p_ee-selected-candidate0_track_e_over_p-rate_lin.svg" alt="candidate 0 (e): EM-calorimeter E / p" /></div><div class="st-cap">candidate 0 (e): EM-calorimeter E / p<span class="badge r">χ²/dof 211.8/58</span></div></div>
<div><div class="st-fig"><NJUPlot src="/figures/datamc/children-ee/inclusive_1p1p_ee-selected-candidate1_track_e_over_p-rate_lin.svg" alt="candidate 1 (e): EM-calorimeter E / p" /></div><div class="st-cap">candidate 1 (e): EM-calorimeter E / p<span class="badge r">χ²/dof 171.7/53</span></div></div>
</div>

<div class="st-source">Source: archived data/MC plot set with the neutral rule applied to the frozen 2026-10-06 selection production</div>

<!--
Figures: artifacts/exclusive-neutral-le3-plots-20261007/plots/ (job 59429001, source 4ae9ef3, neutral count <=3 per hemisphere applied to saved histograms). Black points = 1994 data; stack = signed luminosity-normalised simulation by true process, Z_ee excluded; lower panel = data / simulation. Inclusive sample 23,073 data / 23,198.93 MC. chi2/dof from agreement.json ("Total MC", status ok), statistical only, diagnostic.
Exact signed MC yield 896.952225 (Z_ee excluded). Four variables chosen: p/p_beam of both candidates plus the two channel-specific calorimeter / photon variables.
-->
