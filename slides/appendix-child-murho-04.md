---
class: st pres
---

<script setup>
import NJUPlot from '../components/NJUPlot.vue'
</script>

# Appendix · child μρ (4/10)

<div class="st-sub">Child μρ <span class="id">inclusive_1p1p_murho</span> · ordering by identified species: candidate 0 = μ, candidate 1 = ρ · frozen-run yield 1242 data / 1211 simulated</div>

<div class="fig2x2">
<div><div class="st-fig"><NJUPlot src="/figures/datamc/children-murho/inclusive_1p1p_murho-selected-candidate1_neutral_all_count-rate_lin.svg" alt="candidate 1 (ρ): all neutrals" /></div><div class="st-cap">candidate 1 (ρ): all neutrals<span class="badge g">χ²/dof 3.2/3</span></div></div>
<div><div class="st-fig"><NJUPlot src="/figures/datamc/children-murho/inclusive_1p1p_murho-selected-candidate1_neutral_all_dr03_count-rate_lin.svg" alt="candidate 1 (ρ): all neutrals, ΔR<0.3" /></div><div class="st-cap">candidate 1 (ρ): all neutrals, ΔR<0.3<span class="badge r">χ²/dof 9.2/3</span></div></div>
<div><div class="st-fig"><NJUPlot src="/figures/datamc/children-murho/inclusive_1p1p_murho-selected-candidate1_neutral_costheta-rate_lin.svg" alt="candidate 1 (ρ): neutral-system cos θ" /></div><div class="st-cap">candidate 1 (ρ): neutral-system cos θ<span class="badge g">χ²/dof 24.3/32</span></div></div>
<div><div class="st-fig"><NJUPlot src="/figures/datamc/children-murho/inclusive_1p1p_murho-selected-candidate1_neutral_count-rate_lin.svg" alt="candidate 1 (ρ): photons in neutral system" /></div><div class="st-cap">candidate 1 (ρ): photons in neutral system<span class="badge g">χ²/dof 2.6/2</span></div></div>
</div>

<div class="st-source">Source: archived data/MC plot set with the neutral rule applied to the frozen 2026-10-06 selection production</div>

<!--
Figures: artifacts/exclusive-neutral-le3-plots-20261007/plots/ (job 59429001, source 4ae9ef3, neutral count <=3 per hemisphere applied to saved histograms). Black points = 1994 data; stack = signed luminosity-normalised simulation by true process, Z_ee excluded; lower panel = data / simulation. Inclusive sample 23,073 data / 23,198.93 MC. chi2/dof from agreement.json ("Total MC", status ok), statistical only, diagnostic.

-->
