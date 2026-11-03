---
class: st pres
---

<script setup>
import ZoomablePlot from 'slidev-addon-ztautau/components/ZoomablePlot.vue'
</script>

# Calibration 2: limits and next steps

<div class="st-cols st-cols-2">
<div>
<h3 style="margin:0 0 6px;font-size:16px">Limits</h3>
<ol class="steps" style="font-size:14px">
<li><b>Below 5 GeV</b>: 3 GeV cut inside the fit window.</li>
<li><b>Resolution</b>: data <LaTeX formula="1.2" />–<LaTeX formula="1.5\times" /> wider; not propagated.</li>
<li><b>Fit model</b>: poor on simulation; <LaTeX formula="k" /> stable.</li>
<li><b>Channels</b>: 1993, 1994 differ by <LaTeX formula="\lt2\sigma" />.</li>
<li><b>No split</b> into calibration and validation events.</li>
</ol>
</div>
<div>
<h3 style="margin:0 0 6px;font-size:16px">Next</h3>
<ol class="steps" style="font-size:14px">
<li><b>Low energy</b>: hadronic-<LaTeX formula="Z" /> <LaTeX formula="\pi^0" /> as anchor and for category rates.</li>
<li><b>Apply</b>: calibration file, rerun the <LaTeX formula="\rho" /> study. Owner: not yet.</li>
<li><b>1994</b>: shower response vs detector description.</li>
</ol>
<div class="co open"><b>Status</b> No constant adopted; not a physics measurement.</div>
<div class="st-fig h150" style="margin-top:6px"><ZoomablePlot src="/figures/photon-calibration/v2/width_ratio_vs_epred_iso5.png" alt="data over simulation width ratio of R per E_pred bin and year" /></div>
<div class="st-cap">Width ratio data/simulation of <LaTeX formula="R" /> per <LaTeX formula="E_\mathrm{pred}" /> bin and year, isolation <LaTeX formula="\ge5^\circ" />.</div>
</div>
</div>

<div class="st-source">Source: version-2 study reports (sections 4, 8 and E_pred method), the <LaTeX formula="\rho" />-polarimeter conclusion addendum A, and the owner's instruction of 2026-11-03</div>

<!--
Below 5 GeV: epred/REPORT.md section 3 threshold truncation (iso5: E_pred < 5 GeV, iso5_e1p5: < 3 GeV excluded from k(E) fits). Resolution: REPORT.md section 4 'data are wider than MC in every region: sigma ratio 1.21-1.51 (all years)'; epred section 4.2 per-bin 1.27-1.58 (figure epred/width_ratio_vs_epred_iso5.png); k is a peak-position ratio and does not account for it; step 2b: MC E/p width 5-20 % narrower than data, no smearing fitted. Fit model: 38 of 65 MC fits p < 0.01 (REPORT section 4), 82 of 215 in the E_pred study; all-years ratio fit vs truncated mean differ by <= 0.014. Channels: epred section 5 and REPORT section 2 (1994 0.949 +- 0.011 vs 0.976 +- 0.011; 1993 1.044 +- 0.023 vs 1.072 +- 0.018). Same events: REPORT section 8 'No calibration/validation split was made; the same events serve every number here'; section 8 also: no per-|cos theta| or per-module dependence from 1-D histograms (the E_pred study used the skim columns), no separation of resolution contributions, year differences cannot be attributed. Next: artifacts/rho-polarimeter-CONCLUSION-20261102.md (sections 1-3, addendum A of 2026-11-03) addendum A ('A data-fit-grade calibration would use radiative l+l-gamma for the photon scale and resolution, hadronic-Z pi0 for pairing and merged-tag efficiencies, and a clean rho mass-window sample as closure'); conclusion section 4 (1994 HPC response study against the detector description). Calibration file + rho rerun: owner 'not yet' (2026-11-03, relayed in the coordinator brief). Any NERSC job needs the owner's approval.
-->
