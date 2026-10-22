---
class: st pres
---

<script setup>
import NJUPlot from '../components/NJUPlot.vue'
</script>

# Appendix · child eπ (1/7)

<div class="st-sub">Child eπ <span class="id">inclusive_1p1p_epi</span> · ordering by identified species: candidate 0 = e, candidate 1 = π · frozen-run yield 1694 data / 1752 simulated</div>

<div class="fig2x2">
<div><div class="st-fig"><NJUPlot src="/figures/datamc/children-epi/inclusive_1p1p_epi-selected-candidate0_neutral_all_count-rate_lin.svg" alt="candidate 0 (e): all neutrals" /></div><div class="st-cap">candidate 0 (e): all neutrals<span class="badge r">χ²/dof 24.6/4</span></div></div>
<div><div class="st-fig"><NJUPlot src="/figures/datamc/children-epi/inclusive_1p1p_epi-selected-candidate0_neutral_all_dr03_count-rate_lin.svg" alt="candidate 0 (e): all neutrals, ΔR<0.3" /></div><div class="st-cap">candidate 0 (e): all neutrals, ΔR<0.3<span class="badge r">χ²/dof 15.0/4</span></div></div>
<div><div class="st-fig"><NJUPlot src="/figures/datamc/children-epi/inclusive_1p1p_epi-selected-candidate0_neutral_failed_photon_count-rate_lin.svg" alt="candidate 0 (e): neutrals not identified as photons" /></div><div class="st-cap">candidate 0 (e): neutrals not identified as photons<span class="badge a">χ²/dof 6.2/4</span></div></div>
<div><div class="st-fig"><NJUPlot src="/figures/datamc/children-epi/inclusive_1p1p_epi-selected-candidate0_neutral_identified_photon_count-rate_lin.svg" alt="candidate 0 (e): identified photons" /></div><div class="st-cap">candidate 0 (e): identified photons<span class="badge r">χ²/dof 23.1/4</span></div></div>
</div>

<div class="st-source">Source: archived data/MC plot set with the neutral rule applied to the frozen 2026-10-06 selection production</div>

<!--
Figures: artifacts/exclusive-neutral-le3-plots-20261007/plots/ (job 59429001, source 4ae9ef3, neutral count <=3 per hemisphere applied to saved histograms). Black points = 1994 data; stack = signed luminosity-normalised simulation by true process, Z_ee excluded; lower panel = data / simulation. Inclusive sample 23,073 data / 23,198.93 MC. chi2/dof from agreement.json ("Total MC", status ok), statistical only, diagnostic.

-->
