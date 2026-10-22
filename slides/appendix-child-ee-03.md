---
class: st pres
---

<script setup>
import NJUPlot from '../components/NJUPlot.vue'
</script>

# Appendix · child ee (3/7)

<div class="st-sub">Child ee <span class="id">inclusive_1p1p_ee</span> · ordering by charge: candidate 0 negative, candidate 1 positive · frozen-run yield 882 data / 897 simulated</div>

<div class="fig2x2">
<div><div class="st-fig"><NJUPlot src="/figures/datamc/children-ee/inclusive_1p1p_ee-selected-candidate0_track_mass-rate_lin.svg" alt="candidate 0 (e): track mass [GeV]" /></div><div class="st-cap">candidate 0 (e): track mass [GeV]<span class="badge g">χ²/dof 0.3/1</span></div></div>
<div><div class="st-fig"><NJUPlot src="/figures/datamc/children-ee/inclusive_1p1p_ee-selected-candidate0_track_p-rate_lin.svg" alt="candidate 0 (e): track p [GeV]" /></div><div class="st-cap">candidate 0 (e): track p [GeV]<span class="badge g">χ²/dof 50.4/45</span></div></div>
<div><div class="st-fig"><NJUPlot src="/figures/datamc/children-ee/inclusive_1p1p_ee-selected-candidate0_truth_species-rate_lin.svg" alt="candidate 0 (e): true species (simulation)" /></div><div class="st-cap">candidate 0 (e): true species (simulation)<span class="badge n">no χ²</span></div></div>
<div><div class="st-fig"><NJUPlot src="/figures/datamc/children-ee/inclusive_1p1p_ee-selected-candidate1_neutral_all_count-rate_lin.svg" alt="candidate 1 (e): all neutrals" /></div><div class="st-cap">candidate 1 (e): all neutrals<span class="badge r">χ²/dof 13.3/4</span></div></div>
</div>

<div class="st-source">Source: archived data/MC plot set with the neutral rule applied to the frozen 2026-10-06 selection production</div>

<!--
Figures: artifacts/exclusive-neutral-le3-plots-20261007/plots/ (job 59429001, source 4ae9ef3, neutral count <=3 per hemisphere applied to saved histograms). Black points = 1994 data; stack = signed luminosity-normalised simulation by true process, Z_ee excluded; lower panel = data / simulation. Inclusive sample 23,073 data / 23,198.93 MC. chi2/dof from agreement.json ("Total MC", status ok), statistical only, diagnostic.

-->
