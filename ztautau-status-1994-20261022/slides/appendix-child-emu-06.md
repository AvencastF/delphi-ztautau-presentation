---
class: st pres
---

<script setup>
import ZoomablePlot from 'slidev-addon-ztautau/components/ZoomablePlot.vue'
</script>

# Appendix · child <LaTeX formula="e\mu" /> (6/7)

<div class="st-sub">1992–1995 · child <LaTeX formula="e\mu" /> <span class="id">inclusive_1p1p_emu</span> · order by species: cand. 0 = <LaTeX formula="e" />, cand. 1 = <LaTeX formula="\mu" /> · yield <span class="nw">3,919 data</span> / <span class="nw">4,134 simulated</span></div>

<div class="fig2x2">
<div><div class="st-fig"><ZoomablePlot src="/figures/datamc-1992-1995/children-emu/inclusive_1p1p_emu-selected-candidate1_track_p-rate_lin.svg" alt="cand. 1 (mu): p [GeV]" /></div><div class="st-cap">cand. 1 (<LaTeX formula="\mu" />): <LaTeX formula="p" /> [GeV]<span class="badge a"><LaTeX formula="\chi^2/\mathrm{dof}" /> 121.1 / 46</span></div></div>
<div><div class="st-fig"><ZoomablePlot src="/figures/datamc-1992-1995/children-emu/inclusive_1p1p_emu-selected-candidate1_truth_species-rate_lin.svg" alt="cand. 1 (mu): true species (simulation)" /></div><div class="st-cap">cand. 1 (<LaTeX formula="\mu" />): true species (simulation)<span class="badge n">no <LaTeX formula="\chi^2" /></span></div></div>
<div><div class="st-fig"><ZoomablePlot src="/figures/datamc-1992-1995/children-emu/inclusive_1p1p_emu-selected-erad_over_ebeam-rate_lin.svg" alt="Emathrmrad/Emathrmbeam" /></div><div class="st-cap"><LaTeX formula="E_\mathrm{rad}/E_\mathrm{beam}" /><span class="badge g"><LaTeX formula="\chi^2/\mathrm{dof}" /> 22.8 / 20</span></div></div>
<div><div class="st-fig"><ZoomablePlot src="/figures/datamc-1992-1995/children-emu/inclusive_1p1p_emu-selected-identified_order_state-rate_lin.svg" alt="candidate-ordering state" /></div><div class="st-cap">candidate-ordering state<span class="badge r"><LaTeX formula="\chi^2/\mathrm{dof}" /> 11.6 / 1</span></div></div>
</div>

<div class="st-source">Source: data/MC plots of the 1992–1995 run-quality rerun (selection job 60333695, plots job 60340876)</div>

<!--
Full-precision values are in SOURCES.md and the data folder. Figures: NERSC /pscratch/sd/a/avencast/Ztautau/analysis-runs/1992_1993_1994_1995/all-years-rq-20261026/plots/{all-years-baseline, all-years-children, all-years-children-inclusive_1p1p_<child>}/ (selection job 60333695, tau_analysis 67bffe7; plots job 60340876, recipes plotting_all_years_baseline.yaml / plotting_all_years_children.yaml), copied to public/figures/datamc-1992-1995/ (MANIFEST.md). Black points = 1992-1995 data after the run selection (status 0 + run quality); stack = signed simulation normalised per (year, process, point) to the run-quality luminosity, Z_ee excluded; lower panel = data / simulation. Inclusive sample 56,472 data / 57,520.06 MC (0.982). chi2/dof from agreement.json ("Total MC", status ok; Gaussian chi2 with data variance and finite-MC sumw2), statistical only, diagnostic. Luminosities user-supplied, uncertified.

-->
