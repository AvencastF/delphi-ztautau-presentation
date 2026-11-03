---
class: st pres
---

<script setup>
import ZoomablePlot from 'slidev-addon-ztautau/components/ZoomablePlot.vue'
</script>

# Appendix · photon calibration: photon energy and isolation, selection v2

<div class="st-sub">All years, isolation <LaTeX formula="\ge5^\circ" />, <LaTeX formula="E_\gamma\gt3" /> GeV.</div>

<div class="fig2x2">
<div><div class="st-fig"><ZoomablePlot src="/figures/photon-calibration/v2/llg_eeg_iso5-single_photon_energy.png" alt="eeg photon energy iso5" /></div><div class="st-cap"><LaTeX formula="ee\gamma" />: <LaTeX formula="E_\gamma" /> [GeV]<span class="badge g"><LaTeX formula="\chi^2/\mathrm{dof}" /> 56.5 / 39</span></div></div>
<div><div class="st-fig"><ZoomablePlot src="/figures/photon-calibration/v2/llg_mumug_iso5-single_photon_energy.png" alt="mumug photon energy iso5" /></div><div class="st-cap"><LaTeX formula="\mu\mu\gamma" />: <LaTeX formula="E_\gamma" /> [GeV]<span class="badge g"><LaTeX formula="\chi^2/\mathrm{dof}" /> 29.3 / 39</span></div></div>
<div><div class="st-fig"><ZoomablePlot src="/figures/photon-calibration/v2/llg_eeg_iso5-single_photon_track_angle_min.png" alt="eeg photon angle to nearer track iso5" /></div><div class="st-cap"><LaTeX formula="ee\gamma" />: angle to the nearer track [deg]<span class="badge a"><LaTeX formula="\chi^2/\mathrm{dof}" /> 144.5 / 85</span></div></div>
<div><div class="st-fig"><ZoomablePlot src="/figures/photon-calibration/v2/llg_mumug_iso5-single_photon_track_angle_min.png" alt="mumug photon angle to nearer track iso5" /></div><div class="st-cap"><LaTeX formula="\mu\mu\gamma" />: angle to the nearer track [deg]<span class="badge g"><LaTeX formula="\chi^2/\mathrm{dof}" /> 93.1 / 85</span></div></div>
</div>

<div class="st-source">Source: data/simulation plots of the version-2 <LaTeX formula="\ell^+\ell^-\gamma" /> run</div>

<!--
Run llgamma-v2-20261103: NERSC /pscratch/sd/a/avencast/Ztautau/analysis-runs/1992_1993_1994_1995/llgamma-v2-20261103, job 60747968 (coordinator brief), tau_analysis 5ac249d (configs/analysis_llgamma_v2.yaml, configs/plotting_llgamma_v2.yaml, analysis/single_photon.py); study artifacts/llgamma-v2-20261103/REPORT.md, peak_fits.json, tables/yields.md, tables/chi2_table.md, epred/REPORT.md, epred/k_epred.json (NERSC login node, light python only). Figures plots/llgamma-v2-llg_<ch>_iso5/llg_<ch>_iso5-selected-<var>-rate_lin.pdf (200 dpi); chi2 from agreement.json: v2/llg_eeg_iso5/single_photon_energy 56.45/39 (small-expected 23); v2/llg_mumug_iso5/single_photon_energy 29.33/39 (small-expected 21); v2/llg_eeg_iso5/single_photon_track_angle_min 144.53/85 (small-expected 23); v2/llg_mumug_iso5/single_photon_track_angle_min 93.13/85 (small-expected 7). REPORT.md section 4: per-year track-angle chi2 is dominated by sparsely populated bins.
-->
