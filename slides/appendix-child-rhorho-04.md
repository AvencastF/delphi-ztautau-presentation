---
class: st pres
---

<script setup>
import NJUPlot from '../components/NJUPlot.vue'
</script>

# Appendix · child <LaTeX formula="\rho\rho" /> (4/13)

<div class="st-sub">1992–1995 · child <LaTeX formula="\rho\rho" /> <span class="id">inclusive_1p1p_rhorho</span> · order by charge: cand. 0 negative, cand. 1 positive · yield <span class="nw">979 data</span> / <span class="nw">922 simulated</span></div>

<div class="fig2x2">
<div><div class="st-fig"><NJUPlot src="/figures/datamc-1992-1995/children-rhorho/inclusive_1p1p_rhorho-selected-candidate0_photon_p-rate_lin.svg" alt="cand. 0 (rho): nearby photon p [GeV]" /></div><div class="st-cap">cand. 0 (<LaTeX formula="\rho" />): nearby photon <LaTeX formula="p" /> [GeV]<span class="badge n">no <LaTeX formula="\chi^2" />: correlated entries</span></div></div>
<div><div class="st-fig"><NJUPlot src="/figures/datamc-1992-1995/children-rhorho/inclusive_1p1p_rhorho-selected-candidate0_rho_costheta-rate_lin.svg" alt="cand. 0 (rho): rho candidate costheta" /></div><div class="st-cap">cand. 0 (<LaTeX formula="\rho" />): <LaTeX formula="\rho" /> candidate <LaTeX formula="\cos\theta" /><span class="badge g"><LaTeX formula="\chi^2/\mathrm{dof}" /> 32.0 / 32</span></div></div>
<div><div class="st-fig"><NJUPlot src="/figures/datamc-1992-1995/children-rhorho/inclusive_1p1p_rhorho-selected-candidate0_rho_energy-rate_lin.svg" alt="cand. 0 (rho): Erho candidate [GeV]" /></div><div class="st-cap">cand. 0 (<LaTeX formula="\rho" />): <LaTeX formula="E_\rho" /> candidate [GeV]<span class="badge a"><LaTeX formula="\chi^2/\mathrm{dof}" /> 76.3 / 46</span></div></div>
<div><div class="st-fig"><NJUPlot src="/figures/datamc-1992-1995/children-rhorho/inclusive_1p1p_rhorho-selected-candidate0_rho_p-rate_lin.svg" alt="cand. 0 (rho): prho candidate [GeV]" /></div><div class="st-cap">cand. 0 (<LaTeX formula="\rho" />): <LaTeX formula="p_\rho" /> candidate [GeV]<span class="badge a"><LaTeX formula="\chi^2/\mathrm{dof}" /> 80.1 / 46</span></div></div>
</div>

<div class="st-source">Source: data/MC plots of the 1992–1995 run-quality rerun (selection job 60333695, plots job 60340876)</div>

<!--
Full-precision values are in SOURCES.md and the data folder. Figures: NERSC /pscratch/sd/a/avencast/Ztautau/analysis-runs/1992_1993_1994_1995/all-years-rq-20261026/plots/{all-years-baseline, all-years-children, all-years-children-inclusive_1p1p_<child>}/ (selection job 60333695, tau_analysis 67bffe7; plots job 60340876, recipes plotting_all_years_baseline.yaml / plotting_all_years_children.yaml), copied to public/figures/datamc-1992-1995/ (MANIFEST.md). Black points = 1992-1995 data after the run selection (status 0 + run quality); stack = signed simulation normalised per (year, process, point) to the run-quality luminosity, Z_ee excluded; lower panel = data / simulation. Inclusive sample 56,472 data / 57,520.06 MC (0.982). chi2/dof from agreement.json ("Total MC", status ok; Gaussian chi2 with data variance and finite-MC sumw2), statistical only, diagnostic. Luminosities user-supplied, uncertified.

-->
