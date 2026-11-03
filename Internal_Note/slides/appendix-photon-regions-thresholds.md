---
class: st pres
---

<script setup>
import ZoomablePlot from 'slidev-addon-ztautau/components/ZoomablePlot.vue'
</script>

# Appendix · photon calibration: <LaTeX formula="R" /> with lower photon-energy thresholds

<div class="st-sub">All years, selection v2, isolation <LaTeX formula="\ge10^\circ" />. The low-energy tail grows as the threshold drops.</div>

<div class="fig2x2">
<div><div class="st-fig"><ZoomablePlot src="/figures/photon-calibration/v2/llg_eeg_iso10_e2-single_photon_e_over_epred.png" alt="eeg R iso10_e2" /></div><div class="st-cap"><LaTeX formula="ee\gamma" />, <LaTeX formula="\ge10^\circ" />, <LaTeX formula="E_\gamma\gt2" /> GeV<span class="badge a"><LaTeX formula="\chi^2/\mathrm{dof}" /> 219.9 / 98</span></div></div>
<div><div class="st-fig"><ZoomablePlot src="/figures/photon-calibration/v2/llg_eeg_iso10_e1p5-single_photon_e_over_epred.png" alt="eeg R iso10_e1p5" /></div><div class="st-cap"><LaTeX formula="ee\gamma" />, <LaTeX formula="\ge10^\circ" />, <LaTeX formula="E_\gamma\gt1.5" /> GeV<span class="badge a"><LaTeX formula="\chi^2/\mathrm{dof}" /> 244.0 / 99</span></div></div>
<div><div class="st-fig"><ZoomablePlot src="/figures/photon-calibration/v2/llg_mumug_iso10_e2-single_photon_e_over_epred.png" alt="mumug R iso10_e2" /></div><div class="st-cap"><LaTeX formula="\mu\mu\gamma" />, <LaTeX formula="\ge10^\circ" />, <LaTeX formula="E_\gamma\gt2" /> GeV<span class="badge a"><LaTeX formula="\chi^2/\mathrm{dof}" /> 201.3 / 97</span></div></div>
<div><div class="st-fig"><ZoomablePlot src="/figures/photon-calibration/v2/llg_mumug_iso10_e1p5-single_photon_e_over_epred.png" alt="mumug R iso10_e1p5" /></div><div class="st-cap"><LaTeX formula="\mu\mu\gamma" />, <LaTeX formula="\ge10^\circ" />, <LaTeX formula="E_\gamma\gt1.5" /> GeV<span class="badge a"><LaTeX formula="\chi^2/\mathrm{dof}" /> 183.5 / 98</span></div></div>
</div>

<div class="st-source">Source: data/simulation plots of the version-2 <LaTeX formula="\ell^+\ell^-\gamma" /> run</div>

<!--
Run llgamma-v2-20261103: NERSC /pscratch/sd/a/avencast/Ztautau/analysis-runs/1992_1993_1994_1995/llgamma-v2-20261103, job 60747968 (coordinator brief), tau_analysis 5ac249d (configs/analysis_llgamma_v2.yaml, configs/plotting_llgamma_v2.yaml, analysis/single_photon.py); study artifacts/llgamma-v2-20261103/REPORT.md, peak_fits.json, tables/yields.md, tables/chi2_table.md, epred/REPORT.md, epred/k_epred.json (NERSC login node, light python only). Figures plots/llgamma-v2-<region>/<region>-selected-single_photon_e_over_epred-rate_lin.pdf (200 dpi); chi2 from plots/llgamma-v2-<region>/agreement.json ('Total MC'; values in data/photon-calibration/badges.json). The _2nd regions (>= 2 candidates, all others < 1 GeV) are disjoint from iso10; the 'second candidate below 1 GeV allowed' sample is their sum (REPORT does not fit them).
-->
