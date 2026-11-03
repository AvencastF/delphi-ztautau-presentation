---
class: st pres c2
---

<script setup>
import ZoomablePlot from 'slidev-addon-ztautau/components/ZoomablePlot.vue'
</script>

# Calibration 2 · Step 3: the measured <LaTeX formula="R" /> distributions

<div class="st-sub">Final selection, all years, simulation not yet scaled. Fitted peak positions <LaTeX formula="\mu" /> below.</div>

<div class="st-cols st-cols-2" style="gap:14px">
<div><div class="st-fig" style="height:205px"><ZoomablePlot src="/figures/photon-calibration/v2/llg_eeg_iso5-single_photon_e_over_epred.png" alt="eeg R distribution, final selection" /></div><div class="st-cap"><LaTeX formula="ee\gamma" />: <LaTeX formula="R=E_\mathrm{HPC}/E_\mathrm{pred}" /><span class="badge a"><LaTeX formula="\chi^2/\mathrm{dof}" /> 232.8 / 97</span></div></div>
<div><div class="st-fig" style="height:205px"><ZoomablePlot src="/figures/photon-calibration/v2/llg_mumug_iso5-single_photon_e_over_epred.png" alt="mumug R distribution, final selection" /></div><div class="st-cap"><LaTeX formula="\mu\mu\gamma" />: <LaTeX formula="R" /><span class="badge a"><LaTeX formula="\chi^2/\mathrm{dof}" /> 240.9 / 97</span></div></div>
</div>

<table class="c2t num first-nw" style="margin-top:6px">
<thead><tr><th>All years</th><th>Data peak</th><th>Simulation peak</th><th>Simulation peak, per year</th><th>Width ratio data/sim.</th></tr></thead>
<tbody>
<tr><td><LaTeX formula="ee\gamma" /></td><td><LaTeX formula="0.930\pm0.008" /></td><td><LaTeX formula="0.934\pm0.002" /></td><td>0.923–0.960</td><td><LaTeX formula="1.435\pm0.060" /></td></tr>
<tr><td><LaTeX formula="\mu\mu\gamma" /></td><td><LaTeX formula="0.941\pm0.007" /></td><td><LaTeX formula="0.935\pm0.002" /></td><td>0.924–0.962</td><td><LaTeX formula="1.251\pm0.048" /></td></tr>
</tbody>
</table>

<div class="takeaway"><b>Takeaway</b> The simulation peaks near 0.93, not 1: both energies carry offsets. The calibration is the data/simulation peak ratio, so common offsets cancel; data are wider.</div>

<div class="st-source">Source: data/simulation plots and peak fits of the version-2 <LaTeX formula="\ell^+\ell^-\gamma" /> run (study report, sections 2, 4 and the full fit table)</div>

<!--
Run llgamma-v2-20261103 (job 60747968, tau_analysis 5ac249d). Figures plots/llgamma-v2-llg_<ch>_iso5/llg_<ch>_iso5-selected-single_photon_e_over_epred-rate_lin.pdf rasterised at 200 dpi. Badges from agreement.json ('Total MC'): eeg 232.76/97 (62 small-expected bins), mumug 240.89/97 (57): the pipeline chi2 uses 100 bins in [0, 2], many with small expectation; REPORT.md section 4: the rebinned shape test in [0.6, 1.4] also disagrees (p < 0.01 in 42 of 65 region x year cases). Peaks: artifacts/llgamma-v2-20261103/REPORT.md full fit table, llg_eeg_iso5 all: data 0.930 +- 0.008, MC 0.934 +- 0.002, width ratio 1.435 +- 0.060; per year MC peak 0.960 / 0.927 / 0.932 / 0.923 (1992-1995); llg_mumug_iso5 all: data 0.941 +- 0.007, MC 0.935 +- 0.002, width ratio 1.251 +- 0.048; per year MC 0.962 / 0.926 / 0.930 / 0.924. Why the simulation peak is below 1 is not separated in the study: candidate contributions are the HPC response (calibration 1: simulated photon response 0.95-1.01 of the true energy, step 2b section 2a) and the E_pred biases (lepton masses, extra radiation, angular resolution; selection note 9.1). The owner brief stated "MC peak at 0.95: the stored HPC energy underestimates in the simulation"; the slide shows the measured values and does not attribute the offset. k is the ratio, so any multiplicative offset common to data and simulation cancels.
-->
