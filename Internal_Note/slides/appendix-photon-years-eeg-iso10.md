---
class: st pres
---

<script setup>
import ZoomablePlot from 'slidev-addon-ztautau/components/ZoomablePlot.vue'
</script>

# Appendix · photon calibration: <LaTeX formula="R" /> per year, <LaTeX formula="ee\gamma" />, isolation <LaTeX formula="\ge10^\circ" />

<div class="st-sub">Selection v2, <LaTeX formula="E_\gamma\gt3" /> GeV. Badges: 100-bin statistical <LaTeX formula="\chi^2" />, many low-count bins; diagnostic only.</div>

<div class="fig2x2">
<div><div class="st-fig"><ZoomablePlot src="/figures/photon-calibration/v2/year-1992/llg_eeg_iso10-single_photon_e_over_epred.png" alt="eeg R iso10 1992" /></div><div class="st-cap">1992: <LaTeX formula="R" /><span class="badge a"><LaTeX formula="\chi^2/\mathrm{dof}" /> 212.6 / 86</span></div></div>
<div><div class="st-fig"><ZoomablePlot src="/figures/photon-calibration/v2/year-1993/llg_eeg_iso10-single_photon_e_over_epred.png" alt="eeg R iso10 1993" /></div><div class="st-cap">1993: <LaTeX formula="R" /><span class="badge a"><LaTeX formula="\chi^2/\mathrm{dof}" /> 227.1 / 87</span></div></div>
<div><div class="st-fig"><ZoomablePlot src="/figures/photon-calibration/v2/year-1994/llg_eeg_iso10-single_photon_e_over_epred.png" alt="eeg R iso10 1994" /></div><div class="st-cap">1994: <LaTeX formula="R" /><span class="badge r"><LaTeX formula="\chi^2/\mathrm{dof}" /> 299.3 / 89</span></div></div>
<div><div class="st-fig"><ZoomablePlot src="/figures/photon-calibration/v2/year-1995/llg_eeg_iso10-single_photon_e_over_epred.png" alt="eeg R iso10 1995" /></div><div class="st-cap">1995: <LaTeX formula="R" /><span class="badge a"><LaTeX formula="\chi^2/\mathrm{dof}" /> 190.9 / 83</span></div></div>
</div>

<div class="st-source">Source: data/simulation plots of the version-2 <LaTeX formula="\ell^+\ell^-\gamma" /> run, per-year views</div>

<!--
Run llgamma-v2-20261103: NERSC /pscratch/sd/a/avencast/Ztautau/analysis-runs/1992_1993_1994_1995/llgamma-v2-20261103, job 60747968 (coordinator brief), tau_analysis 5ac249d (configs/analysis_llgamma_v2.yaml, configs/plotting_llgamma_v2.yaml, analysis/single_photon.py); study artifacts/llgamma-v2-20261103/REPORT.md, peak_fits.json, tables/yields.md, tables/chi2_table.md, epred/REPORT.md, epred/k_epred.json (NERSC login node, light python only). Figures plots/llgamma-v2-llg_eeg_iso10/year-<YYYY>/llg_eeg_iso10-selected-single_photon_e_over_epred-rate_lin.pdf (200 dpi). chi2 from year-<YYYY>/agreement.json: 1992 212.63/86; 1993 227.10/87; 1994 299.27/89; 1995 190.89/83. Peak ratios for these samples: REPORT.md section 2 (and the main peak-ratio slide).
-->
