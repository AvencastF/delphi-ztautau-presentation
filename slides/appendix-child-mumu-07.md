---
class: st pres
---

<script setup>
import NJUPlot from '../components/NJUPlot.vue'
</script>

# Appendix · child <LaTeX formula="\mu\mu" /> (7/7)

<div class="st-sub">Child <LaTeX formula="\mu\mu" /> <span class="id">inclusive_1p1p_mumu</span> · order by charge: cand. 0 negative, cand. 1 positive · yield <span class="nw">1,160 data</span> / <span class="nw">1,068 simulated</span></div>

<div class="fig2x2">
<div><div class="st-fig"><NJUPlot src="/figures/datamc/children-mumu/inclusive_1p1p_mumu-selected-prad_over_pbeam-rate_lin.svg" alt="pmathrmrad/pmathrmbeam" /></div><div class="st-cap"><LaTeX formula="p_\mathrm{rad}/p_\mathrm{beam}" /><span class="badge g"><LaTeX formula="\chi^2/\mathrm{dof}" /> 18.6 / 19</span></div></div>
<div><div class="st-fig"><NJUPlot src="/figures/datamc/children-mumu/inclusive_1p1p_mumu-selected-visible_tautau_mass-rate_lin.svg" alt="visible mtautau [GeV]" /></div><div class="st-cap">visible <LaTeX formula="m_{\tau\tau}" /> [GeV]<span class="badge a"><LaTeX formula="\chi^2/\mathrm{dof}" /> 80.5 / 47</span></div></div>
</div>

<div class="st-source">Source: archived data/MC plot set with the neutral rule applied to the frozen 2026-10-06 selection production</div>

<!--
Full-precision values are in SOURCES.md and the data folder. Figures: artifacts/exclusive-neutral-le3-plots-20261007/plots/ (job 59429001, source 4ae9ef3, neutral count <=3 per hemisphere applied to saved histograms). Black points = 1994 data; stack = signed luminosity-normalised simulation by true process, Z_ee excluded; lower panel = data / simulation. Inclusive sample 23,073 data / 23,198.93 MC. chi2/dof from agreement.json ("Total MC", status ok), statistical only, diagnostic.

-->
