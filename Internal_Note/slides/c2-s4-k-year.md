---
class: st pres c2
---

<script setup>
import ZoomablePlot from 'slidev-addon-ztautau/components/ZoomablePlot.vue'
</script>

# Calibration 2 · Step 4: the scale <LaTeX formula="k" /> per year and channel

<div class="st-sub"><LaTeX formula="k=\mu_\mathrm{data}/\mu_\mathrm{sim}" /> of <LaTeX formula="R" />, all photon energies above 3 GeV. Isolation <LaTeX formula="\ge5^\circ" /> is used; <LaTeX formula="\ge10^\circ" /> shares most events.</div>

<table class="c2t num first-nw">
<thead><tr><th>Channel, isolation</th><th>All years</th><th>1992</th><th>1993</th><th>1994</th><th>1995</th></tr></thead>
<tbody>
<tr class="hl"><td><LaTeX formula="ee\gamma" />, <LaTeX formula="\ge5^\circ" /></td><td><LaTeX formula="0.995\pm0.009" /></td><td><LaTeX formula="1.005\pm0.022" /></td><td><LaTeX formula="1.044\pm0.023" /></td><td><LaTeX formula="0.949\pm0.011" /></td><td><LaTeX formula="1.045\pm0.018" /></td></tr>
<tr class="hl"><td><LaTeX formula="\mu\mu\gamma" />, <LaTeX formula="\ge5^\circ" /></td><td><LaTeX formula="1.007\pm0.007" /></td><td><LaTeX formula="0.991\pm0.016" /></td><td><LaTeX formula="1.072\pm0.018" /></td><td><LaTeX formula="0.976\pm0.011" /></td><td><LaTeX formula="1.033\pm0.019" /></td></tr>
<tr><td><LaTeX formula="ee\gamma" />, <LaTeX formula="\ge10^\circ" /></td><td><LaTeX formula="0.991\pm0.009" /></td><td><LaTeX formula="1.008\pm0.025" /></td><td><LaTeX formula="1.027\pm0.014" /></td><td><LaTeX formula="0.941\pm0.011" /></td><td><LaTeX formula="1.046\pm0.017" /></td></tr>
<tr><td><LaTeX formula="\mu\mu\gamma" />, <LaTeX formula="\ge10^\circ" /></td><td><LaTeX formula="1.007\pm0.007" /></td><td><LaTeX formula="0.988\pm0.012" /></td><td><LaTeX formula="1.070\pm0.021" /></td><td><LaTeX formula="0.983\pm0.012" /></td><td><LaTeX formula="1.026\pm0.021" /></td></tr>
</tbody>
</table>

<div class="st-cols st-cols-12" style="margin-top:8px">
<div>
<div class="co ok"><b>Cuts</b> Four separate isolation slices agree with a constant (<LaTeX formula="p=0.21" />, <LaTeX formula="0.64" />); 3 to 1.5 GeV moves <LaTeX formula="k" /> by <LaTeX formula="\le0.006" />.</div>
<div class="co warn"><b>Width</b> Data peak <LaTeX formula="1.21" />–<LaTeX formula="1.51\times" /> wider than simulation.</div>
</div>
<div class="st-fig" style="height:215px"><ZoomablePlot src="/figures/photon-calibration/v2/peak_ratio_vs_cuts.png" alt="peak and width ratio vs isolation and threshold, per year" /></div>
</div>

<div class="takeaway"><b>Takeaway</b> <LaTeX formula="k" /> differs by year (1994 below 1, 1993 and 1995 above) but not with the isolation cut or threshold; data resolution is <LaTeX formula="1.2" />–<LaTeX formula="1.5\times" /> simulation.</div>

<div class="st-source">Source: version-2 <LaTeX formula="\ell^+\ell^-\gamma" /> study report (fits of the saved histograms, 2026-11-03), sections 2–4</div>

<!--
artifacts/llgamma-v2-20261103/REPORT.md section 2 peak ratio data/MC (GaussExp mu), nested regions (columns all, 1992, 1993, 1994, 1995): llg_eeg_iso5 0.995 +- 0.009 / 1.005 +- 0.022 / 1.044 +- 0.023 / 0.949 +- 0.011 / 1.045 +- 0.018; llg_mumug_iso5 1.007 +- 0.007 / 0.991 +- 0.016 / 1.072 +- 0.018 / 0.976 +- 0.011 / 1.033 +- 0.019; llg_eeg_iso10 0.991 +- 0.009 / 1.008 +- 0.025 / 1.027 +- 0.014 / 0.941 +- 0.011 / 1.046 +- 0.017; llg_mumug_iso10 1.007 +- 0.007 / 0.988 +- 0.012 / 1.070 +- 0.021 / 0.983 +- 0.012 / 1.026 +- 0.021. Truncated mean e.g. eeg iso5 0.997 / 0.999 / 1.053 / 0.950 / 1.046; mumug iso5 1.011 / 0.986 / 1.071 / 0.976 / 1.042. Section 3: exclusive angle slices (>= 20, 15-20, 10-15, 5-10 deg) all years: eeg 0.995 +- 0.008, chi2 4.5/3 (p 0.21); mumug 1.010 +- 0.007, 1.7/3 (p 0.64); per year only eeg 1993 fit p = 0.011 (Hessian failure in a 30-event slice; trunc p = 0.46). Threshold: all-years ratio changes <= 0.006 (eeg), <= 0.004 (mumug) from E > 3 to E > 1.5 GeV. Section 4: sigma ratio 1.21-1.51 (all years, every region); MC GaussExp fits poor (38 of 65 p < 0.01); fit vs truncated mean all-years ratios differ by <= 0.014. Figure study/peak_ratio_vs_cuts.png (top peak ratio, bottom width ratio; filled = fit, open = truncated mean). Year pattern (REPORT.md section 3): 1994 below 1 in both channels, 1993 and 1995 above 1, 1992 about 1 (energy-integrated; step 5 shows 1992 energy dependence).
-->
