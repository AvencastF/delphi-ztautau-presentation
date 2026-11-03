---
class: st pres
---

<script setup>
import ZoomablePlot from 'slidev-addon-ztautau/components/ZoomablePlot.vue'
</script>

# Appendix · photon calibration: <LaTeX formula="R" /> in the <LaTeX formula="ee\gamma" /> isolation variants

<div class="st-sub">All years, selection v2; one candidate and <LaTeX formula="E_\gamma\gt3" /> GeV unless stated.</div>

<div class="fig2x2">
<div><div class="st-fig"><ZoomablePlot src="/figures/photon-calibration/v2/llg_eeg_iso20-single_photon_e_over_epred.png" alt="eeg R iso20" /></div><div class="st-cap"><LaTeX formula="ee\gamma" />, isolation <LaTeX formula="\ge20^\circ" /><span class="badge a"><LaTeX formula="\chi^2/\mathrm{dof}" /> 234.5 / 97</span></div></div>
<div><div class="st-fig"><ZoomablePlot src="/figures/photon-calibration/v2/llg_eeg_iso15-single_photon_e_over_epred.png" alt="eeg R iso15" /></div><div class="st-cap"><LaTeX formula="ee\gamma" />, <LaTeX formula="\ge15^\circ" /><span class="badge a"><LaTeX formula="\chi^2/\mathrm{dof}" /> 253.4 / 97</span></div></div>
<div><div class="st-fig"><ZoomablePlot src="/figures/photon-calibration/v2/llg_eeg_iso10-single_photon_e_over_epred.png" alt="eeg R iso10" /></div><div class="st-cap"><LaTeX formula="ee\gamma" />, <LaTeX formula="\ge10^\circ" /><span class="badge a"><LaTeX formula="\chi^2/\mathrm{dof}" /> 236.7 / 97</span></div></div>
<div><div class="st-fig"><ZoomablePlot src="/figures/photon-calibration/v2/llg_eeg_iso10_2nd-single_photon_e_over_epred.png" alt="eeg R iso10_2nd" /></div><div class="st-cap"><LaTeX formula="ee\gamma" />, <LaTeX formula="\ge10^\circ" />, other candidates <LaTeX formula="\lt1" /> GeV<span class="badge a"><LaTeX formula="\chi^2/\mathrm{dof}" /> 153.9 / 61</span></div></div>
</div>

<div class="st-source">Source: data/simulation plots of the version-2 <LaTeX formula="\ell^+\ell^-\gamma" /> run</div>

<!--
Run llgamma-v2-20261103: NERSC /pscratch/sd/a/avencast/Ztautau/analysis-runs/1992_1993_1994_1995/llgamma-v2-20261103, job 60747968 (coordinator brief), tau_analysis 5ac249d (configs/analysis_llgamma_v2.yaml, configs/plotting_llgamma_v2.yaml, analysis/single_photon.py); study artifacts/llgamma-v2-20261103/REPORT.md, peak_fits.json, tables/yields.md, tables/chi2_table.md, epred/REPORT.md, epred/k_epred.json (NERSC login node, light python only). Figures plots/llgamma-v2-<region>/<region>-selected-single_photon_e_over_epred-rate_lin.pdf (200 dpi); chi2 from plots/llgamma-v2-<region>/agreement.json ('Total MC'; values in data/photon-calibration/badges.json). The _2nd regions (>= 2 candidates, all others < 1 GeV) are disjoint from iso10; the 'second candidate below 1 GeV allowed' sample is their sum (REPORT does not fit them).
-->
