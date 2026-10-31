---
class: st pres
---

<script setup>
import NJUPlot from '../components/NJUPlot.vue'
</script>

# Appendix · child <LaTeX formula="e\mu" /> (2/7)

<div class="st-sub">1992–1995 · child <LaTeX formula="e\mu" /> <span class="id">inclusive_1p1p_emu</span> · order by species: cand. 0 = <LaTeX formula="e" />, cand. 1 = <LaTeX formula="\mu" /> · yield <span class="nw">3,919 data</span> / <span class="nw">4,134 simulated</span></div>

<div class="fig2x2">
<div><div class="st-fig"><NJUPlot src="/figures/datamc-1992-1995/children-emu/inclusive_1p1p_emu-selected-candidate0_track_charge-rate_lin.svg" alt="cand. 0 (e): track charge" /></div><div class="st-cap">cand. 0 (<LaTeX formula="e" />): track charge<span class="badge r"><LaTeX formula="\chi^2/\mathrm{dof}" /> 14.5 / 2</span></div></div>
<div><div class="st-fig"><NJUPlot src="/figures/datamc-1992-1995/children-emu/inclusive_1p1p_emu-selected-candidate0_track_costheta-rate_lin.svg" alt="cand. 0 (e): costheta" /></div><div class="st-cap">cand. 0 (<LaTeX formula="e" />): <LaTeX formula="\cos\theta" /><span class="badge r"><LaTeX formula="\chi^2/\mathrm{dof}" /> 111.5 / 35</span></div></div>
<div><div class="st-fig"><NJUPlot src="/figures/datamc-1992-1995/children-emu/inclusive_1p1p_emu-selected-candidate0_track_energy-rate_lin.svg" alt="cand. 0 (e): track E [GeV]" /></div><div class="st-cap">cand. 0 (<LaTeX formula="e" />): track <LaTeX formula="E" /> [GeV]<span class="badge r"><LaTeX formula="\chi^2/\mathrm{dof}" /> 158.7 / 45</span></div></div>
<div><div class="st-fig"><NJUPlot src="/figures/datamc-1992-1995/children-emu/inclusive_1p1p_emu-selected-candidate0_track_hcal_mean-rate_lin.svg" alt="cand. 0 (e): HCAL mean per hit layer [GeV]" /></div><div class="st-cap">cand. 0 (<LaTeX formula="e" />): HCAL mean per hit layer [GeV]<span class="badge r"><LaTeX formula="\chi^2/\mathrm{dof}" /> 657.5 / 54</span></div></div>
</div>

<div class="st-source">Source: data/MC plots of the 1992–1995 run-quality rerun (selection job 60333695, plots job 60340876)</div>

<!--
Full-precision values are in SOURCES.md and the data folder. Figures: NERSC /pscratch/sd/a/avencast/Ztautau/analysis-runs/1992_1993_1994_1995/all-years-rq-20261026/plots/{all-years-baseline, all-years-children, all-years-children-inclusive_1p1p_<child>}/ (selection job 60333695, tau_analysis 67bffe7; plots job 60340876, recipes plotting_all_years_baseline.yaml / plotting_all_years_children.yaml), copied to public/figures/datamc-1992-1995/ (MANIFEST.md). Black points = 1992-1995 data after the run selection (status 0 + run quality); stack = signed simulation normalised per (year, process, point) to the run-quality luminosity, Z_ee excluded; lower panel = data / simulation. Inclusive sample 56,472 data / 57,520.06 MC (0.982). chi2/dof from agreement.json ("Total MC", status ok; Gaussian chi2 with data variance and finite-MC sumw2), statistical only, diagnostic. Luminosities user-supplied, uncertified.

-->
