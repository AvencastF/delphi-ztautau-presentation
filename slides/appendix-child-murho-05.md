---
class: st pres
---

<script setup>
import NJUPlot from '../components/NJUPlot.vue'
</script>

# Appendix · child μρ (5/10)

<div class="st-sub">Child μρ <span class="id">inclusive_1p1p_murho</span> · ordering by identified species: candidate 0 = μ, candidate 1 = ρ · frozen-run yield 1242 data / 1211 simulated</div>

<div class="fig2x2">
<div><div class="st-fig"><NJUPlot src="/figures/datamc/children-murho/inclusive_1p1p_murho-selected-candidate1_neutral_energy-rate_lin.svg" alt="candidate 1 (ρ): neutral-system energy [GeV]" /></div><div class="st-cap">candidate 1 (ρ): neutral-system energy [GeV]<span class="badge r">χ²/dof 159.5/46</span></div></div>
<div><div class="st-fig"><NJUPlot src="/figures/datamc/children-murho/inclusive_1p1p_murho-selected-candidate1_neutral_failed_photon_count-rate_lin.svg" alt="candidate 1 (ρ): neutrals not identified as photons" /></div><div class="st-cap">candidate 1 (ρ): neutrals not identified as photons<span class="badge g">χ²/dof 2.1/3</span></div></div>
<div><div class="st-fig"><NJUPlot src="/figures/datamc/children-murho/inclusive_1p1p_murho-selected-candidate1_neutral_identified_photon_count-rate_lin.svg" alt="candidate 1 (ρ): identified photons" /></div><div class="st-cap">candidate 1 (ρ): identified photons<span class="badge g">χ²/dof 3.0/3</span></div></div>
<div><div class="st-fig"><NJUPlot src="/figures/datamc/children-murho/inclusive_1p1p_murho-selected-candidate1_neutral_mass-rate_lin.svg" alt="candidate 1 (ρ): neutral-system mass [GeV]" /></div><div class="st-cap">candidate 1 (ρ): neutral-system mass [GeV]<span class="badge a">χ²/dof 51.0/18</span></div></div>
</div>

<div class="st-source">Source: archived data/MC plot set with the neutral rule applied to the frozen 2026-10-06 selection production</div>

<!--
Figures: artifacts/exclusive-neutral-le3-plots-20261007/plots/ (job 59429001, source 4ae9ef3, neutral count <=3 per hemisphere applied to saved histograms). Black points = 1994 data; stack = signed luminosity-normalised simulation by true process, Z_ee excluded; lower panel = data / simulation. Inclusive sample 23,073 data / 23,198.93 MC. chi2/dof from agreement.json ("Total MC", status ok), statistical only, diagnostic.

-->
