---
class: st pres
---

<script setup>
import ZoomablePlot from 'slidev-addon-ztautau/components/ZoomablePlot.vue'
</script>

# Calibration 2: peak ratio <LaTeX formula="k" /> per year and channel, all energies

<div class="st-sub"><LaTeX formula="k=\mu_\mathrm{data}/\mu_\mathrm{sim}" /> of <LaTeX formula="R" /> (fit), <LaTeX formula="E_\gamma\gt3" /> GeV. The nested variants share events, so their points are correlated.</div>

<table class="num first-nw">
<thead><tr><th>Channel, isolation</th><th>All years</th><th>1992</th><th>1993</th><th>1994</th><th>1995</th></tr></thead>
<tbody>
<tr><td><LaTeX formula="ee\gamma" />, <LaTeX formula="\ge10^\circ" /></td><td><LaTeX formula="0.991\pm0.009" /></td><td><LaTeX formula="1.008\pm0.025" /></td><td><LaTeX formula="1.027\pm0.014" /></td><td><LaTeX formula="0.941\pm0.011" /></td><td><LaTeX formula="1.046\pm0.017" /></td></tr>
<tr><td><LaTeX formula="ee\gamma" />, <LaTeX formula="\ge5^\circ" /></td><td><LaTeX formula="0.995\pm0.009" /></td><td><LaTeX formula="1.005\pm0.022" /></td><td><LaTeX formula="1.044\pm0.023" /></td><td><LaTeX formula="0.949\pm0.011" /></td><td><LaTeX formula="1.045\pm0.018" /></td></tr>
<tr><td><LaTeX formula="\mu\mu\gamma" />, <LaTeX formula="\ge10^\circ" /></td><td><LaTeX formula="1.007\pm0.007" /></td><td><LaTeX formula="0.988\pm0.012" /></td><td><LaTeX formula="1.070\pm0.021" /></td><td><LaTeX formula="0.983\pm0.012" /></td><td><LaTeX formula="1.026\pm0.021" /></td></tr>
<tr><td><LaTeX formula="\mu\mu\gamma" />, <LaTeX formula="\ge5^\circ" /></td><td><LaTeX formula="1.007\pm0.007" /></td><td><LaTeX formula="0.991\pm0.016" /></td><td><LaTeX formula="1.072\pm0.018" /></td><td><LaTeX formula="0.976\pm0.011" /></td><td><LaTeX formula="1.033\pm0.019" /></td></tr>
</tbody>
</table>


<div class="st-cols st-cols-12" style="margin-top:8px">
<div>
<div class="co ok"><b>Flat</b> Four independent angle slices agree with a constant (all years: <LaTeX formula="p=0.21" />, <LaTeX formula="0.64" />). Lowering 3 to 1.5 GeV moves <LaTeX formula="k" /> by <LaTeX formula="\le0.006" />.</div>
<div class="co warn"><b>Width</b> Data peak <LaTeX formula="1.21" />–<LaTeX formula="1.51\times" /> wider than simulation.</div>
</div>
<div class="st-fig h210"><ZoomablePlot src="/figures/photon-calibration/v2/peak_ratio_vs_cuts.png" alt="peak and width ratio vs isolation and threshold, per year" /></div>
</div>

<div class="st-source">Source: version-2 <LaTeX formula="\ell^+\ell^-\gamma" /> study report (fits of the saved histograms, 2026-11-03), sections 2–4</div>

<!--
Run llgamma-v2-20261103: NERSC /pscratch/sd/a/avencast/Ztautau/analysis-runs/1992_1993_1994_1995/llgamma-v2-20261103, job 60747968 (coordinator brief), tau_analysis 5ac249d (configs/analysis_llgamma_v2.yaml, configs/plotting_llgamma_v2.yaml, analysis/single_photon.py); study artifacts/llgamma-v2-20261103/REPORT.md, peak_fits.json, tables/yields.md, tables/chi2_table.md, epred/REPORT.md, epred/k_epred.json (NERSC login node, light python only). REPORT.md section 2 peak ratio data/MC (GaussExp mu) nested regions: llg_eeg_iso10 0.991 +- 0.009 / 1.008 +- 0.025 / 1.027 +- 0.014 / 0.941 +- 0.011 / 1.046 +- 0.017; llg_eeg_iso5 0.995 +- 0.009 / 1.005 +- 0.022 / 1.044 +- 0.023 / 0.949 +- 0.011 / 1.045 +- 0.018; llg_mumug_iso10 1.007 +- 0.007 / 0.988 +- 0.012 / 1.070 +- 0.021 / 0.983 +- 0.012 / 1.026 +- 0.021; llg_mumug_iso5 1.007 +- 0.007 / 0.991 +- 0.016 / 1.072 +- 0.018 / 0.976 +- 0.011 / 1.033 +- 0.019 (columns all, 1992, 1993, 1994, 1995). Truncated-mean cross-check e.g. eeg iso5 0.997 / 0.999 / 1.053 / 0.950 / 1.046; mumug iso5 1.011 / 0.986 / 1.071 / 0.976 / 1.042. Section 3: exclusive angle slices (>= 20, 15-20, 10-15, 5-10 deg, by histogram subtraction) weighted mean and chi2 vs constant, all years: eeg fit 0.995 +- 0.008, 4.5/3 (p 0.21); trunc 0.998 +- 0.008, 5.7/3 (0.13); mumug fit 1.010 +- 0.007, 1.7/3 (0.64); trunc 1.005 +- 0.006, 5.9/3 (0.12); per year only eeg 1993 fit p = 0.011 (15-20 deg slice with a Hessian failure, 30 events; trunc p = 0.46). Threshold: inclusive all-years fit ratio changes <= 0.006 (eeg) and <= 0.004 (mumug) from E > 3 to E > 1.5 GeV; the 2-3 and 1.5-2 GeV slices are selection-biased (peaks near 0.74-0.82 in data and MC), not a scale measurement. Section 4: data wider than MC in every region, sigma ratio 1.21-1.51 (all years); MC GaussExp fits poor (38 of 65 p < 0.01), fit vs truncated-mean all-years ratio differ by <= 0.014. Figure study/peak_ratio_vs_cuts.png (top: peak ratio, bottom: width ratio; filled fit, open truncated mean). No calibration constant derived; no calibration/validation split.
-->
