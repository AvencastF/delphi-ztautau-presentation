---
class: st pres
---

<script setup>
import NJUPlot from '../components/NJUPlot.vue'
</script>

# Appendix · child <LaTeX formula="e\mu" /> (4/7)

<div class="st-sub">1992–1995 · child <LaTeX formula="e\mu" /> <span class="id">inclusive_1p1p_emu</span> · order by species: cand. 0 = <LaTeX formula="e" />, cand. 1 = <LaTeX formula="\mu" /> · yield <span class="nw">3,919 data</span> / <span class="nw">4,134 simulated</span></div>

<div class="fig2x2">
<div><div class="st-fig"><NJUPlot src="/figures/datamc-1992-1995/children-emu/inclusive_1p1p_emu-selected-candidate1_neutral_all_dr03_count-rate_lin.svg" alt="cand. 1 (mu): all neutrals, Delta Rlt 0.3" /></div><div class="st-cap">cand. 1 (<LaTeX formula="\mu" />): all neutrals, <LaTeX formula="\Delta R\lt 0.3" /><span class="badge r"><LaTeX formula="\chi^2/\mathrm{dof}" /> 35.1 / 4</span></div></div>
<div><div class="st-fig"><NJUPlot src="/figures/datamc-1992-1995/children-emu/inclusive_1p1p_emu-selected-candidate1_neutral_failed_photon_count-rate_lin.svg" alt="cand. 1 (mu): non-photon neutrals" /></div><div class="st-cap">cand. 1 (<LaTeX formula="\mu" />): non-photon neutrals<span class="badge r"><LaTeX formula="\chi^2/\mathrm{dof}" /> 81.4 / 4</span></div></div>
<div><div class="st-fig"><NJUPlot src="/figures/datamc-1992-1995/children-emu/inclusive_1p1p_emu-selected-candidate1_neutral_identified_photon_count-rate_lin.svg" alt="cand. 1 (mu): identified photons" /></div><div class="st-cap">cand. 1 (<LaTeX formula="\mu" />): identified photons<span class="badge r"><LaTeX formula="\chi^2/\mathrm{dof}" /> 19.7 / 4</span></div></div>
<div><div class="st-fig"><NJUPlot src="/figures/datamc-1992-1995/children-emu/inclusive_1p1p_emu-selected-candidate1_track_charge-rate_lin.svg" alt="cand. 1 (mu): track charge" /></div><div class="st-cap">cand. 1 (<LaTeX formula="\mu" />): track charge<span class="badge r"><LaTeX formula="\chi^2/\mathrm{dof}" /> 14.4 / 2</span></div></div>
</div>

<div class="st-source">Source: data/MC plots of the 1992–1995 run-quality rerun (selection job 60333695, plots job 60340876)</div>

<!--
Full-precision values are in SOURCES.md and the data folder. Figures: NERSC /pscratch/sd/a/avencast/Ztautau/analysis-runs/1992_1993_1994_1995/all-years-rq-20261026/plots/{all-years-baseline, all-years-children, all-years-children-inclusive_1p1p_<child>}/ (selection job 60333695, tau_analysis 67bffe7; plots job 60340876, recipes plotting_all_years_baseline.yaml / plotting_all_years_children.yaml), copied to public/figures/datamc-1992-1995/ (MANIFEST.md). Black points = 1992-1995 data after the run selection (status 0 + run quality); stack = signed simulation normalised per (year, process, point) to the run-quality luminosity, Z_ee excluded; lower panel = data / simulation. Inclusive sample 56,472 data / 57,520.06 MC (0.982). chi2/dof from agreement.json ("Total MC", status ok; Gaussian chi2 with data variance and finite-MC sumw2), statistical only, diagnostic. Luminosities user-supplied, uncertified.

-->
