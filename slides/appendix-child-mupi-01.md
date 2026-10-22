---
class: st pres
---

<script setup>
import NJUPlot from '../components/NJUPlot.vue'
</script>

# Appendix · child μπ (1/7)

<div class="st-sub">Child μπ <span class="id">inclusive_1p1p_mupi</span> · ordering by identified species: candidate 0 = μ, candidate 1 = π · frozen-run yield 1912 data / 1938 simulated</div>

<div class="fig2x2">
<div><div class="st-fig"><NJUPlot src="/figures/datamc/children-mupi/inclusive_1p1p_mupi-selected-candidate0_neutral_all_count-rate_lin.svg" alt="candidate 0 (μ): all neutrals" /></div><div class="st-cap">candidate 0 (μ): all neutrals<span class="badge r">χ²/dof 35.3/4</span></div></div>
<div><div class="st-fig"><NJUPlot src="/figures/datamc/children-mupi/inclusive_1p1p_mupi-selected-candidate0_neutral_all_dr03_count-rate_lin.svg" alt="candidate 0 (μ): all neutrals, ΔR<0.3" /></div><div class="st-cap">candidate 0 (μ): all neutrals, ΔR<0.3<span class="badge r">χ²/dof 15.8/4</span></div></div>
<div><div class="st-fig"><NJUPlot src="/figures/datamc/children-mupi/inclusive_1p1p_mupi-selected-candidate0_neutral_failed_photon_count-rate_lin.svg" alt="candidate 0 (μ): neutrals not identified as photons" /></div><div class="st-cap">candidate 0 (μ): neutrals not identified as photons<span class="badge r">χ²/dof 29.0/4</span></div></div>
<div><div class="st-fig"><NJUPlot src="/figures/datamc/children-mupi/inclusive_1p1p_mupi-selected-candidate0_neutral_identified_photon_count-rate_lin.svg" alt="candidate 0 (μ): identified photons" /></div><div class="st-cap">candidate 0 (μ): identified photons<span class="badge r">χ²/dof 13.0/4</span></div></div>
</div>

<div class="st-source">Source: archived data/MC plot set with the neutral rule applied to the frozen 2026-10-06 selection production</div>

<!--
Figures: artifacts/exclusive-neutral-le3-plots-20261007/plots/ (job 59429001, source 4ae9ef3, neutral count <=3 per hemisphere applied to saved histograms). Black points = 1994 data; stack = signed luminosity-normalised simulation by true process, Z_ee excluded; lower panel = data / simulation. Inclusive sample 23,073 data / 23,198.93 MC. chi2/dof from agreement.json ("Total MC", status ok), statistical only, diagnostic.

-->
