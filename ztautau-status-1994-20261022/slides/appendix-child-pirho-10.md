---
class: st pres
---

<script setup>
import ZoomablePlot from 'slidev-addon-ztautau/components/ZoomablePlot.vue'
</script>

# Appendix · child <LaTeX formula="\pi\rho" /> (10/10)

<div class="st-sub">1992–1995 · child <LaTeX formula="\pi\rho" /> <span class="id">inclusive_1p1p_pirho</span> · order by species: cand. 0 = <LaTeX formula="\pi" />, cand. 1 = <LaTeX formula="\rho" /> · yield <span class="nw">3,075 data</span> / <span class="nw">2,999 simulated</span></div>

<div class="fig2x2">
<div><div class="st-fig"><ZoomablePlot src="/figures/datamc-1992-1995/children-pirho/inclusive_1p1p_pirho-selected-identified_order_state-rate_lin.svg" alt="candidate-ordering state" /></div><div class="st-cap">candidate-ordering state<span class="badge a"><LaTeX formula="\chi^2/\mathrm{dof}" /> 1.9 / 1</span></div></div>
<div><div class="st-fig"><ZoomablePlot src="/figures/datamc-1992-1995/children-pirho/inclusive_1p1p_pirho-selected-prad_over_pbeam-rate_lin.svg" alt="pmathrmrad/pmathrmbeam" /></div><div class="st-cap"><LaTeX formula="p_\mathrm{rad}/p_\mathrm{beam}" /><span class="badge a"><LaTeX formula="\chi^2/\mathrm{dof}" /> 35.5 / 19</span></div></div>
<div><div class="st-fig"><ZoomablePlot src="/figures/datamc-1992-1995/children-pirho/inclusive_1p1p_pirho-selected-visible_tautau_mass-rate_lin.svg" alt="visible mtautau [GeV]" /></div><div class="st-cap">visible <LaTeX formula="m_{\tau\tau}" /> [GeV]<span class="badge g"><LaTeX formula="\chi^2/\mathrm{dof}" /> 43.7 / 47</span></div></div>
</div>

<div class="st-source">Source: data/MC plots of the 1992–1995 run-quality rerun (selection job 60333695, plots job 60340876)</div>

<!--
Full-precision values are in SOURCES.md and the data folder. Figures: NERSC /pscratch/sd/a/avencast/Ztautau/analysis-runs/1992_1993_1994_1995/all-years-rq-20261026/plots/{all-years-baseline, all-years-children, all-years-children-inclusive_1p1p_<child>}/ (selection job 60333695, tau_analysis 67bffe7; plots job 60340876, recipes plotting_all_years_baseline.yaml / plotting_all_years_children.yaml), copied to public/figures/datamc-1992-1995/ (MANIFEST.md). Black points = 1992-1995 data after the run selection (status 0 + run quality); stack = signed simulation normalised per (year, process, point) to the run-quality luminosity, Z_ee excluded; lower panel = data / simulation. Inclusive sample 56,472 data / 57,520.06 MC (0.982). chi2/dof from agreement.json ("Total MC", status ok; Gaussian chi2 with data variance and finite-MC sumw2), statistical only, diagnostic. Luminosities user-supplied, uncertified.

-->
