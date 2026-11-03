---
class: st pres c2
---

<script setup>
import ZoomablePlot from 'slidev-addon-ztautau/components/ZoomablePlot.vue'
</script>

# Calibration 2 · Step 6a: before and after scaling the simulation

<div class="st-sub">Same plot as step 3, per year: data unchanged, simulated photon energy <LaTeX formula="\times\,k(E)" />. Final selection, both channels, absolute normalisation.</div>

<div class="st-fig" style="height:190px"><ZoomablePlot src="/figures/photon-calibration/closure/after-R_comb_all.png" alt="R, all years: data vs simulation, left before, right after k(E)" /></div>
<div class="st-cap">All years, both channels. <b>Left</b> before, <b>right</b> after. Grey band: the fit window. Per year in the appendix.</div>

<div class="st-cols st-cols-21" style="gap:14px;margin-top:4px">
<table class="c2t num first-nw" style="font-size:12px">
<thead><tr><th>Year</th><th><LaTeX formula="k" /> applied</th><th>Peak before</th><th>after</th><th><LaTeX formula="\chi^2/40" /> before</th><th>after</th><th>Width</th></tr></thead>
<tbody>
<tr><td>1992</td><td>line in <LaTeX formula="\ln E" /></td><td><LaTeX formula="0.997\pm0.012" /></td><td><LaTeX formula="1.008\pm0.012" /></td><td>80.9</td><td>72.5</td><td>1.22 → 1.17</td></tr>
<tr><td>1993</td><td>1.0429</td><td><LaTeX formula="1.058\pm0.012" /></td><td><LaTeX formula="1.015\pm0.011" /></td><td>133.5</td><td>64.8</td><td>1.22 → 1.14</td></tr>
<tr><td>1994</td><td>0.9577</td><td><LaTeX formula="0.963\pm0.009" /></td><td><LaTeX formula="1.007\pm0.010" /></td><td>68.2</td><td>77.1</td><td>1.32 → 1.37</td></tr>
<tr><td>1995</td><td>1.0232</td><td><LaTeX formula="1.037\pm0.013" /></td><td><LaTeX formula="1.013\pm0.012" /></td><td>88.2</td><td>66.0</td><td>1.43 → 1.41</td></tr>
</tbody>
</table>
<div>
<div class="co ok"><b>Peak</b> data/simulation ratio of the fitted peak; <LaTeX formula="\chi^2" /> of the ratio panel over the 40 bins in <LaTeX formula="0.6\lt R\lt1.4" />; all selected events.</div>
<div class="co warn"><b>Width</b> data/simulation, not corrected: the ratio panel keeps a dip under the peak and <LaTeX formula="\chi^2" /> stays 1.6–1.9 per bin; 1994 slightly worse.</div>
</div>
</div>

<div class="takeaway"><b>Takeaway</b> The scale closes: peaks 0.963–1.058 before, 1.007–1.015 after. The remaining disagreement is the width (resolution), which a scale factor cannot fix.</div>

<div class="st-source">Source: before/after plots of the closure study of the version-2 <LaTeX formula="\ell^+\ell^-\gamma" /> run (2026-11-03c); in the 5–46 GeV window the closure study gives 0.991–1.014</div>

<!--
artifacts/llgamma-v2-20261103/closure/after_plots/{REPORT.md, after_table.md, after_table.json, R_comb_years_summary.png} (after_plots.py sha256 761aaee4..., NERSC login node, 40.7 s, 196 MB; inputs epred/epred_rows.npz and epred/k_epred.json; selection, processes and k identical to closure.py). Figure: 100 bins in [0, 2], stacked Bhabha + Z_mumu + Z_tautau, absolute luminosity weights, data points; ratio panel with chi2/ndf = sum over bins with 0.6 < centre < 1.4 and MC sumw > 0 of (d - m)^2 / (d + sumw2_MC), ndf = 40 bins, no fitted parameters (the pipeline rate-mode formula restricted to the window). comb rows of after_table.md: 1992 before 0.997 +- 0.012, chi2 80.9/40, width 1.22 -> after 1.008 +- 0.012, 72.5/40, 1.17; 1993 1.058 +- 0.012, 133.5 -> 1.015 +- 0.011, 64.8, width 1.22 -> 1.14; 1994 0.963 +- 0.009, 68.2 -> 1.007 +- 0.010, 77.1, width 1.32 -> 1.37; 1995 1.037 +- 0.013, 88.2 -> 1.013 +- 0.012, 66.0, width 1.43 -> 1.41. k applied: 1992 0.9812 + 0.0636 ln(clip(E,5,46)/10 GeV), 1993 1.0429, 1994 0.9577, 1995 1.0232, MC only, E = simulated photon energy. Peaks: GaussExp fit on [0.6, 1.4] (fit_core). Differences to the closure study (closure/REPORT.md section 3, which cuts 5 <= E_pred < 46 GeV): there, after 0.991 / 1.014 / 1.003 / 1.008; here all events enter and events outside the window get the clipped k, which lifts the after-values by about 1 %. Per-channel rows (eeg, mumug) in after_table.md; e.g. eeg 1994 0.949 -> 0.992, mumug 1994 0.976 -> 1.021. Width: the k < 1 of 1994 narrows the MC further (1.32 -> 1.37) and its window chi2 rises 68.2 -> 77.1 (mumug 1994 60.8 -> 74.7); the subagent's reading: the remaining chi2 is width and shape, not scale. The earlier per-year overlay figure (closure/closure_R_comb.png, MC normalised to data, dashed/red/green) is no longer shown on this slide.
-->
