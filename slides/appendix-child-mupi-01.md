---
class: st pres
---

<script setup>
import NJUPlot from '../components/NJUPlot.vue'
</script>

# Appendix · child <LaTeX formula="\mu\pi" /> (1/7)

<div class="st-sub">1992–1995 · child <LaTeX formula="\mu\pi" /> <span class="id">inclusive_1p1p_mupi</span> · order by species: cand. 0 = <LaTeX formula="\mu" />, cand. 1 = <LaTeX formula="\pi" /> · yield <span class="nw">4,727 data</span> / <span class="nw">4,819 simulated</span></div>

<div class="fig2x2">
<div><div class="st-fig"><NJUPlot src="/figures/datamc-1992-1995/children-mupi/inclusive_1p1p_mupi-selected-candidate0_neutral_all_count-rate_lin.svg" alt="cand. 0 (mu): all neutrals" /></div><div class="st-cap">cand. 0 (<LaTeX formula="\mu" />): all neutrals<span class="badge r"><LaTeX formula="\chi^2/\mathrm{dof}" /> 73.3 / 4</span></div></div>
<div><div class="st-fig"><NJUPlot src="/figures/datamc-1992-1995/children-mupi/inclusive_1p1p_mupi-selected-candidate0_neutral_all_dr03_count-rate_lin.svg" alt="cand. 0 (mu): all neutrals, Delta Rlt 0.3" /></div><div class="st-cap">cand. 0 (<LaTeX formula="\mu" />): all neutrals, <LaTeX formula="\Delta R\lt 0.3" /><span class="badge r"><LaTeX formula="\chi^2/\mathrm{dof}" /> 27.1 / 4</span></div></div>
<div><div class="st-fig"><NJUPlot src="/figures/datamc-1992-1995/children-mupi/inclusive_1p1p_mupi-selected-candidate0_neutral_failed_photon_count-rate_lin.svg" alt="cand. 0 (mu): non-photon neutrals" /></div><div class="st-cap">cand. 0 (<LaTeX formula="\mu" />): non-photon neutrals<span class="badge r"><LaTeX formula="\chi^2/\mathrm{dof}" /> 80.4 / 4</span></div></div>
<div><div class="st-fig"><NJUPlot src="/figures/datamc-1992-1995/children-mupi/inclusive_1p1p_mupi-selected-candidate0_neutral_identified_photon_count-rate_lin.svg" alt="cand. 0 (mu): identified photons" /></div><div class="st-cap">cand. 0 (<LaTeX formula="\mu" />): identified photons<span class="badge a"><LaTeX formula="\chi^2/\mathrm{dof}" /> 9.7 / 4</span></div></div>
</div>

<div class="st-source">Source: data/MC plots of the 1992–1995 run-quality rerun (selection job 60333695, plots job 60340876)</div>

<!--
Full-precision values are in SOURCES.md and the data folder. Figures: NERSC /pscratch/sd/a/avencast/Ztautau/analysis-runs/1992_1993_1994_1995/all-years-rq-20261026/plots/{all-years-baseline, all-years-children, all-years-children-inclusive_1p1p_<child>}/ (selection job 60333695, tau_analysis 67bffe7; plots job 60340876, recipes plotting_all_years_baseline.yaml / plotting_all_years_children.yaml), copied to public/figures/datamc-1992-1995/ (MANIFEST.md). Black points = 1992-1995 data after the run selection (status 0 + run quality); stack = signed simulation normalised per (year, process, point) to the run-quality luminosity, Z_ee excluded; lower panel = data / simulation. Inclusive sample 56,472 data / 57,520.06 MC (0.982). chi2/dof from agreement.json ("Total MC", status ok; Gaussian chi2 with data variance and finite-MC sumw2), statistical only, diagnostic. Luminosities user-supplied, uncertified.

-->
