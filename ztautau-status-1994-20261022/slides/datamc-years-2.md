---
class: st pres
---

<script setup>
import ZoomablePlot from 'slidev-addon-ztautau/components/ZoomablePlot.vue'
</script>

# Year by year: radiative energy and visible mass

<div class="st-sub">Top: shapes per year (ratio to 1994). Bottom: absolute data/simulation for 1992 and 1995, the two years flagged on 2026-10-26</div>

<div class="fig2x2">
<div><div class="st-fig"><ZoomablePlot src="/figures/datamc-1992-1995/overlay-year/inclusive_1p1p-selected-erad_over_ebeam-overlay.svg" alt="Emathrmrad/Emathrmbeam, shape per year" /></div><div class="st-cap"><LaTeX formula="E_\mathrm{rad}/E_\mathrm{beam}" />, shape per year<span class="badge n">shape, no <LaTeX formula="\chi^2" /></span></div></div>
<div><div class="st-fig"><ZoomablePlot src="/figures/datamc-1992-1995/overlay-year/inclusive_1p1p-selected-visible_tautau_mass-overlay.svg" alt="visible mtautau [GeV], shape per year" /></div><div class="st-cap">visible <LaTeX formula="m_{\tau\tau}" /> [GeV], shape per year<span class="badge n">shape, no <LaTeX formula="\chi^2" /></span></div></div>
<div><div class="st-fig"><ZoomablePlot src="/figures/datamc-1992-1995/year-1992/inclusive_1p1p-selected-erad_over_ebeam-rate_lin.svg" alt="1992: Emathrmrad/Emathrmbeam" /></div><div class="st-cap">1992: <LaTeX formula="E_\mathrm{rad}/E_\mathrm{beam}" /><span class="badge r"><LaTeX formula="\chi^2/\mathrm{dof}" /> 188.3 / 20</span></div></div>
<div><div class="st-fig"><ZoomablePlot src="/figures/datamc-1992-1995/year-1995/inclusive_1p1p-selected-erad_over_ebeam-rate_lin.svg" alt="1995: Emathrmrad/Emathrmbeam" /></div><div class="st-cap">1995: <LaTeX formula="E_\mathrm{rad}/E_\mathrm{beam}" /><span class="badge r"><LaTeX formula="\chi^2/\mathrm{dof}" /> 60.7 / 20</span></div></div>
</div>

<div class="st-source">Source: data/MC plots of the 1992–1995 run-quality rerun (selection job 60333695, plots job 60340876)</div>

<!--
Full-precision values are in SOURCES.md and the data folder. Figures: NERSC /pscratch/sd/a/avencast/Ztautau/analysis-runs/1992_1993_1994_1995/all-years-rq-20261026/plots/{all-years-baseline, all-years-children, all-years-children-inclusive_1p1p_<child>}/ (selection job 60333695, tau_analysis 67bffe7; plots job 60340876, recipes plotting_all_years_baseline.yaml / plotting_all_years_children.yaml), copied to public/figures/datamc-1992-1995/ (MANIFEST.md). Black points = 1992-1995 data after the run selection (status 0 + run quality); stack = signed simulation normalised per (year, process, point) to the run-quality luminosity, Z_ee excluded; lower panel = data / simulation. Inclusive sample 56,472 data / 57,520.06 MC (0.982). chi2/dof from agreement.json ("Total MC", status ok; Gaussian chi2 with data variance and finite-MC sumw2), statistical only, diagnostic. Luminosities user-supplied, uncertified.
Per-year figures: plots/all-years-baseline/year-YYYY/; chi2 from year-YYYY/agreement.json. PROJECT_GUIDE 2026-10-27: neutral-shower inputs (erad_over_ebeam, EMNC energies) mismodelled in 1992 and in the 1995 peak period.
-->
