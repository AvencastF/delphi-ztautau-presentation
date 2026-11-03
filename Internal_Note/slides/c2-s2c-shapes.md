---
class: st pres c2
---

<script setup>
import ZoomablePlot from 'slidev-addon-ztautau/components/ZoomablePlot.vue'
</script>

# Calibration 2 · Step 2c: data/simulation shapes of the selected events

<div class="st-sub">Final selection, all years, before any photon calibration. Badges: statistical <LaTeX formula="\chi^2" />, inflated by many low-count bins.</div>

<div class="fig2x2" style="gap:6px 14px">
<div><div class="st-fig" style="height:163px"><ZoomablePlot src="/figures/photon-calibration/v2/llg_eeg_iso5-single_photon_energy.png" alt="eeg photon energy, final selection" /></div><div class="st-cap"><LaTeX formula="ee\gamma" />: photon energy <LaTeX formula="E_\gamma" /> [GeV]<span class="badge g"><LaTeX formula="\chi^2/\mathrm{dof}" /> 56.5 / 39</span></div></div>
<div><div class="st-fig" style="height:163px"><ZoomablePlot src="/figures/photon-calibration/v2/llg_mumug_iso5-single_photon_track_angle_min.png" alt="mumug photon angle to the nearer track, final selection" /></div><div class="st-cap"><LaTeX formula="\mu\mu\gamma" />: photon angle to the nearer track [deg]<span class="badge g"><LaTeX formula="\chi^2/\mathrm{dof}" /> 93.1 / 85</span></div></div>
<div><div class="st-fig" style="height:163px"><ZoomablePlot src="/figures/photon-calibration/v2/llg_eeg_iso5-lead_hpc_e_over_p_hemi0.png" alt="eeg electron E/p side 0, final selection" /></div><div class="st-cap"><LaTeX formula="ee\gamma" />: electron <LaTeX formula="E/p" />, side 0<span class="badge a"><LaTeX formula="\chi^2/\mathrm{dof}" /> 63.6 / 37</span></div></div>
<div><div class="st-fig" style="height:163px"><ZoomablePlot src="/figures/photon-calibration/v2/llg_mumug_iso5-evis_over_ecm.png" alt="mumug visible energy over sqrt s, final selection" /></div><div class="st-cap"><LaTeX formula="\mu\mu\gamma" />: <LaTeX formula="E_\mathrm{vis}/\sqrt{s}" /><span class="badge a"><LaTeX formula="\chi^2/\mathrm{dof}" /> 66.4 / 28</span></div></div>
</div>

<div class="takeaway"><b>Takeaway</b> Shapes agree (no red badge; amber from low-count bins), so the sample is understood before any calibration.</div>

<div class="st-source">Source: data/simulation plots of the version-2 <LaTeX formula="\ell^+\ell^-\gamma" /> run, isolation <LaTeX formula="\ge5^\circ" /> regions, all years</div>

<!--
Run llgamma-v2-20261103 (job 60747968, tau_analysis 5ac249d). Figures plots/llgamma-v2-llg_<ch>_iso5/llg_<ch>_iso5-selected-<var>-rate_lin.pdf rasterised at 200 dpi (data/make_photon_calibration_figs.py; the E/p and E_vis copies added 2026-11-03b). Black points = 1992-1995 data, stack = luminosity-normalised simulation (Z_ee excluded), lower panel data/MC. chi2/dof from plots/llgamma-v2-<region>/agreement.json ('Total MC', Gaussian chi2 with data variance and finite-MC sumw2, statistical only), collected in data/photon-calibration/badges.json: v2/llg_eeg_iso5/single_photon_energy 56.45/39 p=0.035, small-expected bins 23; v2/llg_mumug_iso5/single_photon_track_angle_min 93.13/85 p=0.26, 7; v2/llg_eeg_iso5/lead_hpc_e_over_p_hemi0 63.61/37 p=0.0042, 41; v2/llg_mumug_iso5/evis_over_ecm 66.36/28 p=5.9e-05, 45. Badge colours per dof: green <= 1.5, amber <= 3. Other channel views: eeg photon-track angle 144.5/85 (amber), mumug photon energy 29.3/39 (green), eeg E_vis 50.9/23 (amber) (badges.json; REPORT.md section 5). The R = E/E_pred shape itself differs (data wider), see steps 3-4. Electron E/p uses track-linked showers calibrated in data for 1993-1995 only. The photon-track angle in v1 (before isolation, both channels) was well modelled down to 0-5 deg (owner review 2026-11-03; v1 figures in public/figures/photon-calibration/v1/).
-->
