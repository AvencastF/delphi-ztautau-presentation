---
class: st pres
---

<script setup>
import ZoomablePlot from 'slidev-addon-ztautau/components/ZoomablePlot.vue'
</script>

# Appendix · inclusive sample (1/4)

<div class="st-sub">1992–1995, all eight points · inclusive <LaTeX formula="\tau\tau" /> sample, all 18 cuts <span class="id">inclusive_1p1p</span> · H0 / H1 = thrust hemispheres · points: data, stack: simulation</div>

<div class="fig2x2">
<div><div class="st-fig"><ZoomablePlot src="/figures/datamc-1992-1995/inclusive/inclusive_1p1p-selected-leadtrack_hemi0_p-rate_lin.svg" alt="H0 leading-track p [GeV]" /></div><div class="st-cap">H0 leading-track <LaTeX formula="p" /> [GeV]<span class="badge a"><LaTeX formula="\chi^2/\mathrm{dof}" /> 86.0 / 47</span></div></div>
<div><div class="st-fig"><ZoomablePlot src="/figures/datamc-1992-1995/inclusive/inclusive_1p1p-selected-leadtrack_hemi1_p-rate_lin.svg" alt="H1 leading-track p [GeV]" /></div><div class="st-cap">H1 leading-track <LaTeX formula="p" /> [GeV]<span class="badge a"><LaTeX formula="\chi^2/\mathrm{dof}" /> 112.2 / 47</span></div></div>
<div><div class="st-fig"><ZoomablePlot src="/figures/datamc-1992-1995/inclusive/inclusive_1p1p-selected-exclusive_nearby_photon_count-rate_lin.svg" alt="identified photons, Delta Rlt 0.3" /></div><div class="st-cap">identified photons, <LaTeX formula="\Delta R\lt 0.3" /><span class="badge n">no <LaTeX formula="\chi^2" />: correlated entries</span></div></div>
<div><div class="st-fig"><ZoomablePlot src="/figures/datamc-1992-1995/inclusive/inclusive_1p1p-selected-exclusive_hemi1_hadron_source-rate_lin.svg" alt="H1 hadron-source category" /></div><div class="st-cap">H1 hadron-source category<span class="badge r"><LaTeX formula="\chi^2/\mathrm{dof}" /> 898.2 / 7</span></div></div>
</div>

<div class="st-source">Source: data/MC plots of the 1992–1995 run-quality rerun (selection job 60333695, plots job 60340876)</div>

<!--
Full-precision values are in SOURCES.md and the data folder. Figures: NERSC /pscratch/sd/a/avencast/Ztautau/analysis-runs/1992_1993_1994_1995/all-years-rq-20261026/plots/{all-years-baseline, all-years-children, all-years-children-inclusive_1p1p_<child>}/ (selection job 60333695, tau_analysis 67bffe7; plots job 60340876, recipes plotting_all_years_baseline.yaml / plotting_all_years_children.yaml), copied to public/figures/datamc-1992-1995/ (MANIFEST.md). Black points = 1992-1995 data after the run selection (status 0 + run quality); stack = signed simulation normalised per (year, process, point) to the run-quality luminosity, Z_ee excluded; lower panel = data / simulation. Inclusive sample 56,472 data / 57,520.06 MC (0.982). chi2/dof from agreement.json ("Total MC", status ok; Gaussian chi2 with data variance and finite-MC sumw2), statistical only, diagnostic. Luminosities user-supplied, uncertified.

-->
