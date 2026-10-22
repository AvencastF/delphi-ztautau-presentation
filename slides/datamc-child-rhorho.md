---
class: st pres
---

<script setup>
import NJUPlot from '../components/NJUPlot.vue'
</script>

# Child <LaTeX formula="\rho\rho" />: four most informative variables

<div class="st-sub">Child <LaTeX formula="\rho\rho" /> <span class="id">inclusive_1p1p_rhorho</span> · order by charge: cand. 0 negative, cand. 1 positive · yield <span class="nw">389 data</span> / <span class="nw">378 simulated</span></div>

<div class="fig2x2">
<div><div class="st-fig"><NJUPlot src="/figures/datamc/children-rhorho/inclusive_1p1p_rhorho-selected-candidate0_track_p_over_pbeam-rate_lin.svg" alt="cand. 0 (rho): p/pmathrmbeam" /></div><div class="st-cap">cand. 0 (<LaTeX formula="\rho" />): <LaTeX formula="p/p_\mathrm{beam}" /><span class="badge r"><LaTeX formula="\chi^2/\mathrm{dof}" /> 164.0 / 40</span></div></div>
<div><div class="st-fig"><NJUPlot src="/figures/datamc/children-rhorho/inclusive_1p1p_rhorho-selected-candidate1_track_p_over_pbeam-rate_lin.svg" alt="cand. 1 (rho): p/pmathrmbeam" /></div><div class="st-cap">cand. 1 (<LaTeX formula="\rho" />): <LaTeX formula="p/p_\mathrm{beam}" /><span class="badge r"><LaTeX formula="\chi^2/\mathrm{dof}" /> 346.6 / 40</span></div></div>
<div><div class="st-fig"><NJUPlot src="/figures/datamc/children-rhorho/inclusive_1p1p_rhorho-selected-candidate0_rho_mass-rate_lin.svg" alt="cand. 0 (rho): mrho candidate [GeV]" /></div><div class="st-cap">cand. 0 (<LaTeX formula="\rho" />): <LaTeX formula="m_\rho" /> candidate [GeV]<span class="badge g"><LaTeX formula="\chi^2/\mathrm{dof}" /> 6.6 / 11</span></div></div>
<div><div class="st-fig"><NJUPlot src="/figures/datamc/children-rhorho/inclusive_1p1p_rhorho-selected-candidate1_rho_mass-rate_lin.svg" alt="cand. 1 (rho): mrho candidate [GeV]" /></div><div class="st-cap">cand. 1 (<LaTeX formula="\rho" />): <LaTeX formula="m_\rho" /> candidate [GeV]<span class="badge g"><LaTeX formula="\chi^2/\mathrm{dof}" /> 12.3 / 11</span></div></div>
</div>

<div class="st-source">Source: archived data/MC plot set with the neutral rule applied to the frozen 2026-10-06 selection production</div>

<!--
Full-precision values are in SOURCES.md and the data folder. Figures: artifacts/exclusive-neutral-le3-plots-20261007/plots/ (job 59429001, source 4ae9ef3, neutral count <=3 per hemisphere applied to saved histograms). Black points = 1994 data; stack = signed luminosity-normalised simulation by true process, Z_ee excluded; lower panel = data / simulation. Inclusive sample 23,073 data / 23,198.93 MC. chi2/dof from agreement.json ("Total MC", status ok), statistical only, diagnostic.
Exact signed MC yield 378.267116 (Z_ee excluded). Four variables chosen: p/p_beam of both candidates plus the two channel-specific calorimeter / photon variables.
-->
