---
class: st pres
---

<script setup>
import NJUPlot from '../components/NJUPlot.vue'
</script>

# Appendix · child <LaTeX formula="e\pi" /> (2/7)

<div class="st-sub">Child <LaTeX formula="e\pi" /> <span class="id">inclusive_1p1p_epi</span> · order by species: cand. 0 = <LaTeX formula="e" />, cand. 1 = <LaTeX formula="\pi" /> · yield <span class="nw">1,694 data</span> / <span class="nw">1,752 simulated</span></div>

<div class="fig2x2">
<div><div class="st-fig"><NJUPlot src="/figures/datamc/children-epi/inclusive_1p1p_epi-selected-candidate0_track_charge-rate_lin.svg" alt="cand. 0 (e): track charge" /></div><div class="st-cap">cand. 0 (<LaTeX formula="e" />): track charge<span class="badge g"><LaTeX formula="\chi^2/\mathrm{dof}" /> 2.4 / 2</span></div></div>
<div><div class="st-fig"><NJUPlot src="/figures/datamc/children-epi/inclusive_1p1p_epi-selected-candidate0_track_costheta-rate_lin.svg" alt="cand. 0 (e): costheta" /></div><div class="st-cap">cand. 0 (<LaTeX formula="e" />): <LaTeX formula="\cos\theta" /><span class="badge a"><LaTeX formula="\chi^2/\mathrm{dof}" /> 54.7 / 34</span></div></div>
<div><div class="st-fig"><NJUPlot src="/figures/datamc/children-epi/inclusive_1p1p_epi-selected-candidate0_track_e_over_p-rate_lin.svg" alt="cand. 0 (e): EM-calorimeter E/p" /></div><div class="st-cap">cand. 0 (<LaTeX formula="e" />): EM-calorimeter <LaTeX formula="E/p" /><span class="badge r"><LaTeX formula="\chi^2/\mathrm{dof}" /> 252.9 / 58</span></div></div>
<div><div class="st-fig"><NJUPlot src="/figures/datamc/children-epi/inclusive_1p1p_epi-selected-candidate0_track_energy-rate_lin.svg" alt="cand. 0 (e): track E [GeV]" /></div><div class="st-cap">cand. 0 (<LaTeX formula="e" />): track <LaTeX formula="E" /> [GeV]<span class="badge a"><LaTeX formula="\chi^2/\mathrm{dof}" /> 110.6 / 45</span></div></div>
</div>

<div class="st-source">Source: archived data/MC plot set with the neutral rule applied to the frozen 2026-10-06 selection production</div>

<!--
Full-precision values are in SOURCES.md and the data folder. Figures: artifacts/exclusive-neutral-le3-plots-20261007/plots/ (job 59429001, source 4ae9ef3, neutral count <=3 per hemisphere applied to saved histograms). Black points = 1994 data; stack = signed luminosity-normalised simulation by true process, Z_ee excluded; lower panel = data / simulation. Inclusive sample 23,073 data / 23,198.93 MC. chi2/dof from agreement.json ("Total MC", status ok), statistical only, diagnostic.

-->
