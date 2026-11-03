---
class: st pres
---

<script setup>
import ZoomablePlot from 'slidev-addon-ztautau/components/ZoomablePlot.vue'
</script>

# Calibration 2: the <LaTeX formula="R" /> distributions, isolation <LaTeX formula="\ge5^\circ" />

<div class="st-sub">Selection v2, one candidate, <LaTeX formula="E_\gamma\gt3" /> GeV, all years. The <LaTeX formula="R" /> badges use 100 bins, about 60 with small expectation: diagnostic only.</div>

<div class="fig2x2">
<div><div class="st-fig"><ZoomablePlot src="/figures/photon-calibration/v2/llg_eeg_iso5-single_photon_e_over_epred.png" alt="eeg R distribution iso5" /></div><div class="st-cap"><LaTeX formula="ee\gamma" />: <LaTeX formula="R=E_\mathrm{HPC}/E_\mathrm{pred}" /><span class="badge a"><LaTeX formula="\chi^2/\mathrm{dof}" /> 232.8 / 97</span></div></div>
<div><div class="st-fig"><ZoomablePlot src="/figures/photon-calibration/v2/llg_mumug_iso5-single_photon_e_over_epred.png" alt="mumug R distribution iso5" /></div><div class="st-cap"><LaTeX formula="\mu\mu\gamma" />: <LaTeX formula="R" /><span class="badge a"><LaTeX formula="\chi^2/\mathrm{dof}" /> 240.9 / 97</span></div></div>
<div><div class="st-fig"><ZoomablePlot src="/figures/photon-calibration/v2/llg_mumug_iso5-single_photon_epred.png" alt="mumug E_pred spectrum iso5" /></div><div class="st-cap"><LaTeX formula="\mu\mu\gamma" />: <LaTeX formula="E_\mathrm{pred}" /> [GeV]<span class="badge g"><LaTeX formula="\chi^2/\mathrm{dof}" /> 57.7 / 47</span></div></div>
<div><div class="st-fig"><ZoomablePlot src="/figures/photon-calibration/v2/llg_eeg_iso5-single_photon_hpc_module_distance.png" alt="eeg photon distance to HPC module boundary" /></div><div class="st-cap"><LaTeX formula="ee\gamma" />: photon distance to an HPC module boundary [deg]<span class="badge g"><LaTeX formula="\chi^2/\mathrm{dof}" /> 34.6 / 30</span></div></div>
</div>

<div class="st-source">Source: data/simulation plots of the version-2 <LaTeX formula="\ell^+\ell^-\gamma" /> run, isolation <LaTeX formula="\ge5^\circ" /> regions</div>

<!--
Run llgamma-v2-20261103: NERSC /pscratch/sd/a/avencast/Ztautau/analysis-runs/1992_1993_1994_1995/llgamma-v2-20261103, job 60747968 (coordinator brief), tau_analysis 5ac249d (configs/analysis_llgamma_v2.yaml, configs/plotting_llgamma_v2.yaml, analysis/single_photon.py); study artifacts/llgamma-v2-20261103/REPORT.md, peak_fits.json, tables/yields.md, tables/chi2_table.md, epred/REPORT.md, epred/k_epred.json (NERSC login node, light python only). Figures plots/llgamma-v2-llg_<ch>_iso5/llg_<ch>_iso5-selected-<var>-rate_lin.pdf rasterised at 200 dpi. chi2/dof from plots/llgamma-v2-<region>/agreement.json ('Total MC'): v2/llg_eeg_iso5/single_photon_e_over_epred: 232.76/97 p=3.6e-13, small-expected bins 62; v2/llg_mumug_iso5/single_photon_e_over_epred: 240.89/97 p=3.1e-14, small-expected bins 57; v2/llg_mumug_iso5/single_photon_epred: 57.66/47 p=0.14, small-expected bins 19; v2/llg_eeg_iso5/single_photon_hpc_module_distance: 34.58/30 p=0.26, small-expected bins 0. REPORT.md section 4: the pipeline chi2 of R uses all 100 bins in [0, 2] with 73-95 bins flagged small-expected and should not be read as shape quality without rebinning; the rebinned shape test in [0.6, 1.4] (0.04 bins) also disagrees (p < 0.01 in 42 of 65 region x year cases; data have more events than MC on the high side, about 1.06-1.3, mainly 1993 and 1995). Z_tautau adds 0.13-0.20 (eeg) and 0.26-0.50 (mumug) weighted events per region; Z_ee, Z_qq, yy_ll, yy_qq histograms empty in every studied region.
-->
