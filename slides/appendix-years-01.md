---
class: st pres
---

<script setup>
import NJUPlot from '../components/NJUPlot.vue'
</script>

# Appendix · per year: H0 leading-track momentum

<div class="st-sub">Absolute data/simulation per year, inclusive sample</div>

<div class="fig2x2">
<div><div class="st-fig"><NJUPlot src="/figures/datamc-1992-1995/year-1992/inclusive_1p1p-selected-leadtrack_hemi0_p_over_pbeam-rate_lin.svg" alt="1992: H0 leading-track p/pmathrmbeam" /></div><div class="st-cap">1992: H0 leading-track <LaTeX formula="p/p_\mathrm{beam}" /><span class="badge g"><LaTeX formula="\chi^2/\mathrm{dof}" /> 39.0 / 42</span></div></div>
<div><div class="st-fig"><NJUPlot src="/figures/datamc-1992-1995/year-1993/inclusive_1p1p-selected-leadtrack_hemi0_p_over_pbeam-rate_lin.svg" alt="1993: H0 leading-track p/pmathrmbeam" /></div><div class="st-cap">1993: H0 leading-track <LaTeX formula="p/p_\mathrm{beam}" /><span class="badge g"><LaTeX formula="\chi^2/\mathrm{dof}" /> 43.7 / 42</span></div></div>
<div><div class="st-fig"><NJUPlot src="/figures/datamc-1992-1995/year-1994/inclusive_1p1p-selected-leadtrack_hemi0_p_over_pbeam-rate_lin.svg" alt="1994: H0 leading-track p/pmathrmbeam" /></div><div class="st-cap">1994: H0 leading-track <LaTeX formula="p/p_\mathrm{beam}" /><span class="badge a"><LaTeX formula="\chi^2/\mathrm{dof}" /> 81.4 / 42</span></div></div>
<div><div class="st-fig"><NJUPlot src="/figures/datamc-1992-1995/year-1995/inclusive_1p1p-selected-leadtrack_hemi0_p_over_pbeam-rate_lin.svg" alt="1995: H0 leading-track p/pmathrmbeam" /></div><div class="st-cap">1995: H0 leading-track <LaTeX formula="p/p_\mathrm{beam}" /><span class="badge g"><LaTeX formula="\chi^2/\mathrm{dof}" /> 33.7 / 42</span></div></div>
</div>

<div class="st-source">Source: data/MC plots of the 1992–1995 run-quality rerun (selection job 60333695, plots job 60340876)</div>

<!--
Full-precision values are in SOURCES.md and the data folder. Figures: NERSC /pscratch/sd/a/avencast/Ztautau/analysis-runs/1992_1993_1994_1995/all-years-rq-20261026/plots/{all-years-baseline, all-years-children, all-years-children-inclusive_1p1p_<child>}/ (selection job 60333695, tau_analysis 67bffe7; plots job 60340876, recipes plotting_all_years_baseline.yaml / plotting_all_years_children.yaml), copied to public/figures/datamc-1992-1995/ (MANIFEST.md). Black points = 1992-1995 data after the run selection (status 0 + run quality); stack = signed simulation normalised per (year, process, point) to the run-quality luminosity, Z_ee excluded; lower panel = data / simulation. Inclusive sample 56,472 data / 57,520.06 MC (0.982). chi2/dof from agreement.json ("Total MC", status ok; Gaussian chi2 with data variance and finite-MC sumw2), statistical only, diagnostic. Luminosities user-supplied, uncertified.

-->
