---
class: st pres
---

<script setup>
import NJUPlot from '../components/NJUPlot.vue'
</script>

# Child <LaTeX formula="e\pi" />: four most informative variables

<div class="st-sub">1992–1995 · child <LaTeX formula="e\pi" /> <span class="id">inclusive_1p1p_epi</span> · order by species: cand. 0 = <LaTeX formula="e" />, cand. 1 = <LaTeX formula="\pi" /> · yield <span class="nw">4,253 data</span> / <span class="nw">4,452 simulated</span></div>

<div class="fig2x2">
<div><div class="st-fig"><NJUPlot src="/figures/datamc-1992-1995/children-epi/inclusive_1p1p_epi-selected-candidate0_track_p_over_pbeam-rate_lin.svg" alt="cand. 0 (e): p/pmathrmbeam" /></div><div class="st-cap">cand. 0 (<LaTeX formula="e" />): <LaTeX formula="p/p_\mathrm{beam}" /><span class="badge g"><LaTeX formula="\chi^2/\mathrm{dof}" /> 60.7 / 42</span></div></div>
<div><div class="st-fig"><NJUPlot src="/figures/datamc-1992-1995/children-epi/inclusive_1p1p_epi-selected-candidate1_track_p_over_pbeam-rate_lin.svg" alt="cand. 1 (pi): p/pmathrmbeam" /></div><div class="st-cap">cand. 1 (<LaTeX formula="\pi" />): <LaTeX formula="p/p_\mathrm{beam}" /><span class="badge g"><LaTeX formula="\chi^2/\mathrm{dof}" /> 56.8 / 40</span></div></div>
<div><div class="st-fig"><NJUPlot src="/figures/datamc-1992-1995/children-epi/inclusive_1p1p_epi-selected-candidate1_track_e_over_p-rate_lin.svg" alt="cand. 1 (pi): EM-calorimeter E/p" /></div><div class="st-cap">cand. 1 (<LaTeX formula="\pi" />): EM-calorimeter <LaTeX formula="E/p" /><span class="badge r"><LaTeX formula="\chi^2/\mathrm{dof}" /> 974.8 / 60</span></div></div>
<div><div class="st-fig"><NJUPlot src="/figures/datamc-1992-1995/children-epi/inclusive_1p1p_epi-selected-candidate1_track_hcal_mean-rate_lin.svg" alt="cand. 1 (pi): HCAL mean per hit layer [GeV]" /></div><div class="st-cap">cand. 1 (<LaTeX formula="\pi" />): HCAL mean per hit layer [GeV]<span class="badge r"><LaTeX formula="\chi^2/\mathrm{dof}" /> 342.4 / 60</span></div></div>
</div>

<div class="st-source">Source: data/MC plots of the 1992–1995 run-quality rerun (selection job 60333695, plots job 60340876)</div>

<!--
Full-precision values are in SOURCES.md and the data folder. Figures: NERSC /pscratch/sd/a/avencast/Ztautau/analysis-runs/1992_1993_1994_1995/all-years-rq-20261026/plots/{all-years-baseline, all-years-children, all-years-children-inclusive_1p1p_<child>}/ (selection job 60333695, tau_analysis 67bffe7; plots job 60340876, recipes plotting_all_years_baseline.yaml / plotting_all_years_children.yaml), copied to public/figures/datamc-1992-1995/ (MANIFEST.md). Black points = 1992-1995 data after the run selection (status 0 + run quality); stack = signed simulation normalised per (year, process, point) to the run-quality luminosity, Z_ee excluded; lower panel = data / simulation. Inclusive sample 56,472 data / 57,520.06 MC (0.982). chi2/dof from agreement.json ("Total MC", status ok; Gaussian chi2 with data variance and finite-MC sumw2), statistical only, diagnostic. Luminosities user-supplied, uncertified.
Exact signed MC yield 4452.179227 (Z_ee excluded). Four variables chosen: p/p_beam of both candidates plus the two channel-specific calorimeter / photon variables.
-->
