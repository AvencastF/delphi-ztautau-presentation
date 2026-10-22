---
class: st pres
---

<script setup>
import NJUPlot from '../components/NJUPlot.vue'
</script>

# Appendix · child μρ (1/10)

<div class="st-sub">Child μρ <span class="id">inclusive_1p1p_murho</span> · ordering by identified species: candidate 0 = μ, candidate 1 = ρ · frozen-run yield 1242 data / 1211 simulated</div>

<div class="fig2x2">
<div><div class="st-fig"><NJUPlot src="/figures/datamc/children-murho/inclusive_1p1p_murho-selected-candidate0_neutral_all_count-rate_lin.svg" alt="candidate 0 (μ): all neutrals" /></div><div class="st-cap">candidate 0 (μ): all neutrals<span class="badge r">χ²/dof 20.8/4</span></div></div>
<div><div class="st-fig"><NJUPlot src="/figures/datamc/children-murho/inclusive_1p1p_murho-selected-candidate0_neutral_all_dr03_count-rate_lin.svg" alt="candidate 0 (μ): all neutrals, ΔR<0.3" /></div><div class="st-cap">candidate 0 (μ): all neutrals, ΔR<0.3<span class="badge a">χ²/dof 7.9/4</span></div></div>
<div><div class="st-fig"><NJUPlot src="/figures/datamc/children-murho/inclusive_1p1p_murho-selected-candidate0_neutral_failed_photon_count-rate_lin.svg" alt="candidate 0 (μ): neutrals not identified as photons" /></div><div class="st-cap">candidate 0 (μ): neutrals not identified as photons<span class="badge r">χ²/dof 20.4/4</span></div></div>
<div><div class="st-fig"><NJUPlot src="/figures/datamc/children-murho/inclusive_1p1p_murho-selected-candidate0_neutral_identified_photon_count-rate_lin.svg" alt="candidate 0 (μ): identified photons" /></div><div class="st-cap">candidate 0 (μ): identified photons<span class="badge a">χ²/dof 7.7/4</span></div></div>
</div>

<div class="st-source">Source: archived data/MC plot set with the neutral rule applied to the frozen 2026-10-06 selection production</div>

<!--
Figures: artifacts/exclusive-neutral-le3-plots-20261007/plots/ (job 59429001, source 4ae9ef3, neutral count <=3 per hemisphere applied to saved histograms). Black points = 1994 data; stack = signed luminosity-normalised simulation by true process, Z_ee excluded; lower panel = data / simulation. Inclusive sample 23,073 data / 23,198.93 MC. chi2/dof from agreement.json ("Total MC", status ok), statistical only, diagnostic.

-->
