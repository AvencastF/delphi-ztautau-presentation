---
class: st pres
---

<script setup>
import ZoomablePlot from 'slidev-addon-ztautau/components/ZoomablePlot.vue'
</script>

# Year by year: do the shapes change between 1992 and 1995?

<div class="st-sub">Inclusive sample · overlays: each year normalised to unit area, ratio panel to 1994, data and simulation separately</div>

<div class="fig2x2">
<div><div class="st-fig"><ZoomablePlot src="/figures/datamc-1992-1995/overlay-year/inclusive_1p1p-selected-leadtrack_hemi0_p_over_pbeam-overlay.svg" alt="H0 leading-track p/pmathrmbeam, shape per year" /></div><div class="st-cap">H0 leading-track <LaTeX formula="p/p_\mathrm{beam}" />, shape per year<span class="badge n">shape, no <LaTeX formula="\chi^2" /></span></div></div>
<div><div class="st-fig"><ZoomablePlot src="/figures/datamc-1992-1995/overlay-year/inclusive_1p1p-selected-leadtrack_hemi0_costheta-overlay.svg" alt="H0 leading-track costheta, shape per year" /></div><div class="st-cap">H0 leading-track <LaTeX formula="\cos\theta" />, shape per year<span class="badge n">shape, no <LaTeX formula="\chi^2" /></span></div></div>
<div><div class="st-fig"><ZoomablePlot src="/figures/datamc-1992-1995/overlay-year/inclusive_1p1p-selected-exclusive_e_over_p-overlay.svg" alt="EM-calorimeter E/p per track, shape per year" /></div><div class="st-cap">EM-calorimeter <LaTeX formula="E/p" /> per track, shape per year<span class="badge n">shape, no <LaTeX formula="\chi^2" /></span></div></div>
<div><div class="st-fig"><ZoomablePlot src="/figures/datamc-1992-1995/overlay-year/inclusive_1p1p-selected-exclusive_hemi0_hcal_mean-overlay.svg" alt="H0 HCAL mean per hit layer [GeV], shape per year" /></div><div class="st-cap">H0 HCAL mean per hit layer [GeV], shape per year<span class="badge n">shape, no <LaTeX formula="\chi^2" /></span></div></div>
</div>

<div class="st-source">Source: data/MC plots of the 1992–1995 run-quality rerun (selection job 60333695, plots job 60340876)</div>

<!--
Full-precision values are in SOURCES.md and the data folder. Figures: NERSC /pscratch/sd/a/avencast/Ztautau/analysis-runs/1992_1993_1994_1995/all-years-rq-20261026/plots/{all-years-baseline, all-years-children, all-years-children-inclusive_1p1p_<child>}/ (selection job 60333695, tau_analysis 67bffe7; plots job 60340876, recipes plotting_all_years_baseline.yaml / plotting_all_years_children.yaml), copied to public/figures/datamc-1992-1995/ (MANIFEST.md). Black points = 1992-1995 data after the run selection (status 0 + run quality); stack = signed simulation normalised per (year, process, point) to the run-quality luminosity, Z_ee excluded; lower panel = data / simulation. Inclusive sample 56,472 data / 57,520.06 MC (0.982). chi2/dof from agreement.json ("Total MC", status ok; Gaussian chi2 with data variance and finite-MC sumw2), statistical only, diagnostic. Luminosities user-supplied, uncertified.
Overlays: plots/all-years-baseline/overlay-year/*.svg and overlay.json (overlay_by year, reference 1994, normalisation in-range signed sumw per group, statistical errors only). No chi2 is computed for overlays.
-->
