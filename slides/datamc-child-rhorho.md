---
class: st pres
---

<script setup>
import NJUPlot from '../components/NJUPlot.vue'
</script>

# Child ρρ: the four most informative variables

<div class="st-sub">Child ρρ <span class="id">inclusive_1p1p_rhorho</span> · ordering by charge: candidate 0 negative, candidate 1 positive · frozen-run yield 389 data / 378 simulated</div>

<div class="fig2x2">
<div><div class="st-fig"><NJUPlot src="/figures/datamc/children-rhorho/inclusive_1p1p_rhorho-selected-candidate0_track_p_over_pbeam-rate_lin.svg" alt="candidate 0 (ρ): track p / p_beam" /></div><div class="st-cap">candidate 0 (ρ): track p / p_beam<span class="badge r">χ²/dof 164.0/40</span></div></div>
<div><div class="st-fig"><NJUPlot src="/figures/datamc/children-rhorho/inclusive_1p1p_rhorho-selected-candidate1_track_p_over_pbeam-rate_lin.svg" alt="candidate 1 (ρ): track p / p_beam" /></div><div class="st-cap">candidate 1 (ρ): track p / p_beam<span class="badge r">χ²/dof 346.6/40</span></div></div>
<div><div class="st-fig"><NJUPlot src="/figures/datamc/children-rhorho/inclusive_1p1p_rhorho-selected-candidate0_rho_mass-rate_lin.svg" alt="candidate 0 (ρ): ρ candidate mass [GeV]" /></div><div class="st-cap">candidate 0 (ρ): ρ candidate mass [GeV]<span class="badge g">χ²/dof 6.6/11</span></div></div>
<div><div class="st-fig"><NJUPlot src="/figures/datamc/children-rhorho/inclusive_1p1p_rhorho-selected-candidate1_rho_mass-rate_lin.svg" alt="candidate 1 (ρ): ρ candidate mass [GeV]" /></div><div class="st-cap">candidate 1 (ρ): ρ candidate mass [GeV]<span class="badge g">χ²/dof 12.3/11</span></div></div>
</div>

<div class="st-source">Source: archived data/MC plot set with the neutral rule applied to the frozen 2026-10-06 selection production</div>

<!--
Figures: artifacts/exclusive-neutral-le3-plots-20261007/plots/ (job 59429001, source 4ae9ef3, neutral count <=3 per hemisphere applied to saved histograms). Black points = 1994 data; stack = signed luminosity-normalised simulation by true process, Z_ee excluded; lower panel = data / simulation. Inclusive sample 23,073 data / 23,198.93 MC. chi2/dof from agreement.json ("Total MC", status ok), statistical only, diagnostic.
Exact signed MC yield 378.267116 (Z_ee excluded). Four variables chosen: p/p_beam of both candidates plus the two channel-specific calorimeter / photon variables.
-->
