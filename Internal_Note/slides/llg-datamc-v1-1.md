---
class: st pres
---

<script setup>
import ZoomablePlot from 'slidev-addon-ztautau/components/ZoomablePlot.vue'
</script>

# Calibration 2, v1 data/simulation: photon energy and isolation

<div class="st-sub">All years. Badges: statistical <LaTeX formula="\chi^2" /> with many low-count bins, which overstates the disagreement.</div>

<div class="fig2x2">
<div><div class="st-fig"><ZoomablePlot src="/figures/photon-calibration/v1/llg_eeg_gh0-photon_candidate_energy.png" alt="eeg photon energy, photon in side 0" /></div><div class="st-cap"><LaTeX formula="ee\gamma" />, photon on side 0: <LaTeX formula="E_\gamma" /> [GeV]<span class="badge a"><LaTeX formula="\chi^2/\mathrm{dof}" /> 96.4 / 38</span></div></div>
<div><div class="st-fig"><ZoomablePlot src="/figures/photon-calibration/v1/llg_mumug_gh0-photon_candidate_energy.png" alt="mumug photon energy, photon in side 0" /></div><div class="st-cap"><LaTeX formula="\mu\mu\gamma" />, side 0: <LaTeX formula="E_\gamma" /> [GeV]<span class="badge g"><LaTeX formula="\chi^2/\mathrm{dof}" /> 53.1 / 38</span></div></div>
<div><div class="st-fig"><ZoomablePlot src="/figures/photon-calibration/v1/llg_eeg-photonid_candidate_nearest_track_angle_hemi0.png" alt="eeg photon-track angle before isolation" /></div><div class="st-cap"><LaTeX formula="ee\gamma" />, before isolation: photon–track angle, side 0 [deg]<span class="badge a"><LaTeX formula="\chi^2/\mathrm{dof}" /> 60.8 / 28</span></div></div>
<div><div class="st-fig"><ZoomablePlot src="/figures/photon-calibration/v1/llg_mumug-photonid_candidate_nearest_track_angle_hemi0.png" alt="mumug photon-track angle before isolation" /></div><div class="st-cap"><LaTeX formula="\mu\mu\gamma" />, before isolation: photon–track angle [deg]<span class="badge a"><LaTeX formula="\chi^2/\mathrm{dof}" /> 42.5 / 27</span></div></div>
</div>

<div class="st-source">Source: data/simulation plots of the first <LaTeX formula="\ell^+\ell^-\gamma" /> run (selection v1), all years</div>

<!--
Run llgamma-20261103: NERSC /pscratch/sd/a/avencast/Ztautau/analysis-runs/1992_1993_1994_1995/llgamma-20261103, jobs 60745549 + resume 60745978 (job ids from the coordinator brief of 2026-11-03), tau_analysis db00c4a (configs/analysis_llgamma.yaml, configs/plotting_llgamma.yaml) and 9c787d7 (finalize: confusion matrix n/a); local copy artifacts/llgamma-selection-20261103/ (cutflows/cutflow.csv sha256 258d18b94b34913628262fda4fe8c5f19e2548186f0f0cea6c4039d83911d1fb, agreement_table.json, plots/, plots-by-region/<region>/rates-by-group.md). Figures plots/<region>-selected-<variable>-rate_lin.pdf rasterised at 200 dpi (Ghostscript 10.05.0) to public/figures/photon-calibration/v1/. Black points = 1992-1995 data; stack = luminosity-normalised simulation (Z_ee excluded); lower panel data/MC. chi2/dof from agreement_table.json (recovered per region from NERSC plots/llgamma-<region>/agreement.json; 'Total MC', Gaussian chi2 with data variance and finite-MC sumw2, statistical only). Caveat: many bins have small expected counts (small_expected_bins in the JSON), so this Gaussian chi2 overstates the disagreement at low counts; the badges are diagnostics, not goodness-of-fit probabilities. Values: v1/llg_eeg_gh0/photon_candidate_energy: 96.44/38 p=5.6e-07, small-expected bins 32; v1/llg_mumug_gh0/photon_candidate_energy: 53.12/38 p=0.053, small-expected bins 27; v1/llg_eeg/photonid_candidate_nearest_track_angle_hemi0: 60.81/28 p=0.00032, small-expected bins 16; v1/llg_mumug/photonid_candidate_nearest_track_angle_hemi0: 42.46/27 p=0.03, small-expected bins 16
-->
