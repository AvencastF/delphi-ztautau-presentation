---
class: st pres
---

<script setup>
import ZoomablePlot from 'slidev-addon-ztautau/components/ZoomablePlot.vue'
</script>

# Calibration 2: scale versus predicted energy, <LaTeX formula="k(E_\mathrm{pred})" />

<div class="st-sub">Both channels combined, isolation <LaTeX formula="\ge5^\circ" />, fit estimator. Bins below 5 GeV are excluded: the 3 GeV cut lies inside the fit window there.</div>

<table class="sm num first-nw">
<thead><tr><th>Year</th><th>5–8 GeV</th><th>8–12</th><th>12–17</th><th>17–25</th><th>25–46</th><th>Slope <LaTeX formula="p" />: fit / trunc.</th></tr></thead>
<tbody>
<tr><td>1992</td><td><LaTeX formula="0.965\pm0.019" /></td><td><LaTeX formula="0.975\pm0.022" /></td><td><LaTeX formula="0.964\pm0.025" /></td><td colspan="2" style="text-align:center"><LaTeX formula="1.043\pm0.015" /> (17–46)</td><td><LaTeX formula="\lt0.001" /> / <LaTeX formula="\lt0.001" /></td></tr>
<tr><td>1993</td><td><LaTeX formula="1.039\pm0.046" /></td><td><LaTeX formula="1.035\pm0.018" /></td><td><LaTeX formula="1.113\pm0.029" /></td><td><LaTeX formula="1.021\pm0.017" /></td><td><LaTeX formula="1.051\pm0.023" /></td><td>0.92 / 0.65</td></tr>
<tr><td>1994</td><td><LaTeX formula="0.970\pm0.017" /></td><td><LaTeX formula="0.968\pm0.022" /></td><td><LaTeX formula="0.963\pm0.019" /></td><td><LaTeX formula="0.963\pm0.015" /></td><td><LaTeX formula="0.937\pm0.014" /></td><td>0.15 / 0.025</td></tr>
<tr><td>1995</td><td><LaTeX formula="1.068\pm0.055" /></td><td><LaTeX formula="0.970\pm0.053" /></td><td><LaTeX formula="1.020\pm0.024" /></td><td colspan="2" style="text-align:center"><LaTeX formula="1.025\pm0.012" /> (17–46)</td><td>0.99 / 0.24</td></tr>
<tr class="hl"><td>All</td><td><LaTeX formula="0.983\pm0.011" /></td><td><LaTeX formula="0.996\pm0.015" /></td><td><LaTeX formula="0.996\pm0.011" /></td><td><LaTeX formula="1.003\pm0.009" /></td><td><LaTeX formula="0.997\pm0.013" /></td><td>0.24 / 0.41</td></tr>
</tbody>
</table>


<div class="st-fig h158" style="margin-top:6px"><ZoomablePlot src="/figures/photon-calibration/v2/k_vs_epred_iso5.png" alt="k versus E_pred per year, eeg, mumug, combined, with constant and line fits" /></div>
<div class="co warn"><b>1992</b> 0.96–0.98 below 17 GeV, 1.043 above: constant rejected (<LaTeX formula="p=0.001" />), slope significant in both estimators. Other years: no slope significant in both.</div>

<div class="st-source">Source: E_pred-binned study of the version-2 <LaTeX formula="\ell^+\ell^-\gamma" /> run (2026-11-03), sections 2–4</div>

<!--
artifacts/llgamma-v2-20261103/epred/REPORT.md and k_epred.json (extract_epred.py from the skim parquet: data.parquet, Bhabha/*.parquet, Z_mumu/*.parquet, Z_tautau.parquet; fit_epred.py with fit_core.py = the GaussExp and truncated-mean functions of study/fit_peaks.py; NERSC login node, wall 2.8 s + 4 min 19 s). Selection iso5 = region bit llg_<ch>_iso5. Bins requested [1.5,3), [3,5), [5,8), [8,12), [12,17), [17,25), [25,46); merged low to high until >= 60 data events with 0.6 < R < 1.4 (1992, 1995: 17-46 merged). Threshold truncation: E > E_cut implies R > E_cut/E_pred; bins with E_cut/E_lo > 0.6 (iso5: E_pred < 5 GeV) are excluded from the k(E) fits. Section 4 iso5 comb k fit (k trunc): 1992 5-8 0.965 +- 0.019 (0.956), 8-12 0.975 +- 0.022 (0.973), 12-17 0.964 +- 0.025 (0.964), 17-46 1.043 +- 0.015 (1.042); 1993 1.039 +- 0.046, 1.035 +- 0.018, 1.113 +- 0.029, 17-25 1.021 +- 0.017, 25-46 1.051 +- 0.023; 1994 0.970 +- 0.017, 0.968 +- 0.022, 0.963 +- 0.019, 0.963 +- 0.015, 0.937 +- 0.014; 1995 1.068 +- 0.055 (flag), 0.970 +- 0.053, 1.020 +- 0.024, 17-46 1.025 +- 0.012; all 0.983 +- 0.011, 0.996 +- 0.015, 0.996 +- 0.011, 1.003 +- 0.009, 0.997 +- 0.013; truncated 1.5-5 bins: 1992 1.017, 1993 1.078, 1994 0.983, 1995 1.083, all 1.018 (excluded). Section 4.1: constant k (chi2/ndf, p) and slope b = dk/d ln E: 1992 0.999 +- 0.009 (15.8/3, 0.001), b +0.064 +- 0.018 p < 0.001, trunc +0.072 +- 0.020 p < 0.001; 1993 1.043 +- 0.010 (7.8/4, 0.10), b -0.002 +- 0.022 p 0.92, trunc p 0.65; 1994 0.958 +- 0.008 (3.1/4, 0.54), b -0.019 +- 0.013 p 0.15, trunc -0.031 +- 0.014 p 0.025 (driven by 25-46 GeV, 0.927); 1995 1.023 +- 0.010 (1.7/3, 0.64), b -0.000 +- 0.032 p 0.99, trunc p 0.24; all 0.995 +- 0.005 (2.0/4, 0.74), p 0.24 / 0.41. 1992 line itself not rejected (p 0.20 / 0.06 fit, 0.30 / 0.44 trunc). iso5_e1p5 (E > 1.5 GeV) gives the same pattern; all-years slope significant there only through the 3-5 GeV bin. Width ratio per bin 1.27-1.58 (all years). Z_tautau <= 0.08 % of MC sumw in every bin. Figure epred/k_vs_epred_iso5.png.
-->
