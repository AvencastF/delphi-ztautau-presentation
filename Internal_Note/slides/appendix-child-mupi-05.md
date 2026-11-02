---
class: st pres
---

<script setup>
import ZoomablePlot from 'slidev-addon-ztautau/components/ZoomablePlot.vue'
</script>

# Appendix · child <LaTeX formula="\mu\pi" /> (5/7)

<div class="st-sub">1992–1995 · child <LaTeX formula="\mu\pi" /> <span class="id">inclusive_1p1p_mupi</span> · order by species: cand. 0 = <LaTeX formula="\mu" />, cand. 1 = <LaTeX formula="\pi" /> · yield <span class="nw">4,727 data</span> / <span class="nw">4,819 simulated</span></div>

<div class="fig2x2">
<div><div class="st-fig"><ZoomablePlot src="/figures/datamc-1992-1995/children-mupi/inclusive_1p1p_mupi-selected-candidate1_track_charge-rate_lin.svg" alt="cand. 1 (pi): track charge" /></div><div class="st-cap">cand. 1 (<LaTeX formula="\pi" />): track charge<span class="badge g"><LaTeX formula="\chi^2/\mathrm{dof}" /> 1.8 / 2</span></div></div>
<div><div class="st-fig"><ZoomablePlot src="/figures/datamc-1992-1995/children-mupi/inclusive_1p1p_mupi-selected-candidate1_track_costheta-rate_lin.svg" alt="cand. 1 (pi): costheta" /></div><div class="st-cap">cand. 1 (<LaTeX formula="\pi" />): <LaTeX formula="\cos\theta" /><span class="badge a"><LaTeX formula="\chi^2/\mathrm{dof}" /> 65.0 / 37</span></div></div>
<div><div class="st-fig"><ZoomablePlot src="/figures/datamc-1992-1995/children-mupi/inclusive_1p1p_mupi-selected-candidate1_track_energy-rate_lin.svg" alt="cand. 1 (pi): track E [GeV]" /></div><div class="st-cap">cand. 1 (<LaTeX formula="\pi" />): track <LaTeX formula="E" /> [GeV]<span class="badge a"><LaTeX formula="\chi^2/\mathrm{dof}" /> 70.2 / 45</span></div></div>
<div><div class="st-fig"><ZoomablePlot src="/figures/datamc-1992-1995/children-mupi/inclusive_1p1p_mupi-selected-candidate1_track_mass-rate_lin.svg" alt="cand. 1 (pi): track mass [GeV]" /></div><div class="st-cap">cand. 1 (<LaTeX formula="\pi" />): track mass [GeV]<span class="badge a"><LaTeX formula="\chi^2/\mathrm{dof}" /> 1.7 / 1</span></div></div>
</div>

<div class="st-source">Source: data/MC plots of the 1992–1995 run-quality rerun (selection job 60333695, plots job 60340876)</div>

<!--
Full-precision values are in SOURCES.md and the data folder. Figures: NERSC /pscratch/sd/a/avencast/Ztautau/analysis-runs/1992_1993_1994_1995/all-years-rq-20261026/plots/{all-years-baseline, all-years-children, all-years-children-inclusive_1p1p_<child>}/ (selection job 60333695, tau_analysis 67bffe7; plots job 60340876, recipes plotting_all_years_baseline.yaml / plotting_all_years_children.yaml), copied to public/figures/datamc-1992-1995/ (MANIFEST.md). Black points = 1992-1995 data after the run selection (status 0 + run quality); stack = signed simulation normalised per (year, process, point) to the run-quality luminosity, Z_ee excluded; lower panel = data / simulation. Inclusive sample 56,472 data / 57,520.06 MC (0.982). chi2/dof from agreement.json ("Total MC", status ok; Gaussian chi2 with data variance and finite-MC sumw2), statistical only, diagnostic. Luminosities user-supplied, uncertified.

-->
