---
class: st pres
---

<script setup>
import ZoomablePlot from 'slidev-addon-ztautau/components/ZoomablePlot.vue'
</script>

# Calibration 2, v1 data/simulation: electron <LaTeX formula="E/p" /> and visible energy

<div class="st-sub">All years, before the photon-side split. The electron <LaTeX formula="E/p" /> uses track-linked showers, calibrated in data for 1993–1995 only.</div>

<div class="fig2x2">
<div><div class="st-fig"><ZoomablePlot src="/figures/photon-calibration/v1/llg_eeg-lead_hpc_e_over_p_hemi0.png" alt="eeg electron E/p side 0" /></div><div class="st-cap"><LaTeX formula="ee\gamma" />: electron <LaTeX formula="E/p" />, side 0<span class="badge a"><LaTeX formula="\chi^2/\mathrm{dof}" /> 75.3 / 38</span></div></div>
<div><div class="st-fig"><ZoomablePlot src="/figures/photon-calibration/v1/llg_eeg-lead_hpc_e_over_p_hemi1.png" alt="eeg electron E/p side 1" /></div><div class="st-cap"><LaTeX formula="ee\gamma" />: electron <LaTeX formula="E/p" />, side 1<span class="badge a"><LaTeX formula="\chi^2/\mathrm{dof}" /> 56.4 / 37</span></div></div>
<div><div class="st-fig"><ZoomablePlot src="/figures/photon-calibration/v1/llg_eeg-evis_over_ecm.png" alt="eeg visible energy over sqrt s" /></div><div class="st-cap"><LaTeX formula="ee\gamma" />: <LaTeX formula="E_\mathrm{vis}/\sqrt{s}" /><span class="badge a"><LaTeX formula="\chi^2/\mathrm{dof}" /> 50.9 / 23</span></div></div>
<div><div class="st-fig"><ZoomablePlot src="/figures/photon-calibration/v1/llg_mumug-evis_over_ecm.png" alt="mumug visible energy over sqrt s" /></div><div class="st-cap"><LaTeX formula="\mu\mu\gamma" />: <LaTeX formula="E_\mathrm{vis}/\sqrt{s}" /><span class="badge a"><LaTeX formula="\chi^2/\mathrm{dof}" /> 81.0 / 28</span></div></div>
</div>

<div class="st-source">Source: data/simulation plots of the first <LaTeX formula="\ell^+\ell^-\gamma" /> run (selection v1), all years</div>

<!--
Run llgamma-20261103: NERSC /pscratch/sd/a/avencast/Ztautau/analysis-runs/1992_1993_1994_1995/llgamma-20261103, jobs 60745549 + resume 60745978 (job ids from the coordinator brief of 2026-11-03), tau_analysis db00c4a (configs/analysis_llgamma.yaml, configs/plotting_llgamma.yaml) and 9c787d7 (finalize: confusion matrix n/a); local copy artifacts/llgamma-selection-20261103/ (cutflows/cutflow.csv sha256 258d18b94b34913628262fda4fe8c5f19e2548186f0f0cea6c4039d83911d1fb, agreement_table.json, plots/, plots-by-region/<region>/rates-by-group.md). Figures plots/<region>-selected-<variable>-rate_lin.pdf rasterised at 200 dpi (Ghostscript 10.05.0) to public/figures/photon-calibration/v1/. Black points = 1992-1995 data; stack = luminosity-normalised simulation (Z_ee excluded); lower panel data/MC. chi2/dof from agreement_table.json (recovered per region from NERSC plots/llgamma-<region>/agreement.json; 'Total MC', Gaussian chi2 with data variance and finite-MC sumw2, statistical only). Caveat: many bins have small expected counts (small_expected_bins in the JSON), so this Gaussian chi2 overstates the disagreement at low counts; the badges are diagnostics, not goodness-of-fit probabilities. Values: v1/llg_eeg/lead_hpc_e_over_p_hemi0: 75.32/38 p=0.00029, small-expected bins 40; v1/llg_eeg/lead_hpc_e_over_p_hemi1: 56.38/37 p=0.022, small-expected bins 40; v1/llg_eeg/evis_over_ecm: 50.90/23 p=0.0007, small-expected bins 44; v1/llg_mumug/evis_over_ecm: 81.02/28 p=4.7e-07, small-expected bins 45
-->
