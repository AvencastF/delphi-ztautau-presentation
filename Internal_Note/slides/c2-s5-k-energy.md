---
class: st pres c2
---

<script setup>
import ZoomablePlot from 'slidev-addon-ztautau/components/ZoomablePlot.vue'
</script>

# Calibration 2 · Step 5: energy dependence <LaTeX formula="k(E_\mathrm{pred})" />

<div class="st-sub">Both channels combined, isolation <LaTeX formula="\ge5^\circ" />. Bins below 5 GeV excluded: there the 3 GeV cut distorts <LaTeX formula="R" />.</div>

<table class="sm num first-nw">
<thead><tr><th>Year</th><th>5–8 GeV</th><th>8–12</th><th>12–17</th><th>17–25</th><th>25–46</th><th>Constant fit (<LaTeX formula="p" />)</th><th>Slope <LaTeX formula="p" />: fit / trunc.</th></tr></thead>
<tbody>
<tr><td>1992</td><td><LaTeX formula="0.965\pm0.019" /></td><td><LaTeX formula="0.975\pm0.022" /></td><td><LaTeX formula="0.964\pm0.025" /></td><td colspan="2" style="text-align:center"><LaTeX formula="1.043\pm0.015" /> (17–46)</td><td>0.999 (0.001)</td><td><LaTeX formula="\lt0.001" /> / <LaTeX formula="\lt0.001" /></td></tr>
<tr><td>1993</td><td><LaTeX formula="1.039\pm0.046" /></td><td><LaTeX formula="1.035\pm0.018" /></td><td><LaTeX formula="1.113\pm0.029" /></td><td><LaTeX formula="1.021\pm0.017" /></td><td><LaTeX formula="1.051\pm0.023" /></td><td>1.043 (0.10)</td><td>0.92 / 0.65</td></tr>
<tr><td>1994</td><td><LaTeX formula="0.970\pm0.017" /></td><td><LaTeX formula="0.968\pm0.022" /></td><td><LaTeX formula="0.963\pm0.019" /></td><td><LaTeX formula="0.963\pm0.015" /></td><td><LaTeX formula="0.937\pm0.014" /></td><td>0.958 (0.54)</td><td>0.15 / 0.025</td></tr>
<tr><td>1995</td><td><LaTeX formula="1.068\pm0.055" /></td><td><LaTeX formula="0.970\pm0.053" /></td><td><LaTeX formula="1.020\pm0.024" /></td><td colspan="2" style="text-align:center"><LaTeX formula="1.025\pm0.012" /> (17–46)</td><td>1.023 (0.64)</td><td>0.99 / 0.24</td></tr>
</tbody>
</table>

<div class="st-fig" style="height:185px;margin-top:8px"><ZoomablePlot src="/figures/photon-calibration/v2/k_vs_epred_iso5.png" alt="k versus E_pred per year, eeg, mumug, combined, with constant and line fits" /></div>
<div class="co ok" style="margin-top:4px"><b>Rule</b> Line in <LaTeX formula="\ln E" /> if its slope is significant (<LaTeX formula="p\lt0.05" />, fit), otherwise a constant.</div>

<div class="takeaway"><b>Takeaway</b> 1992 needs an energy-dependent <LaTeX formula="k(E)" /> (0.964–0.975 below 17 GeV, 1.043 above); 1993, 1994 and 1995 are flat.</div>

<div class="st-source">Source: energy-binned study of the version-2 <LaTeX formula="\ell^+\ell^-\gamma" /> run (2026-11-03), sections 2–4.1; the rule from the closure study, section 2.1</div>

<!--
artifacts/llgamma-v2-20261103/epred/REPORT.md and k_epred.json (extract_epred.py from the skim parquet; fit_epred.py with fit_core.py = the GaussExp and truncated-mean functions of study/fit_peaks.py; NERSC login node). Selection iso5 = region bit llg_<ch>_iso5. Bins requested [5,8), [8,12), [12,17), [17,25), [25,46); merged until >= 60 data events with 0.6 < R < 1.4 (1992, 1995: 17-46 merged). Threshold truncation: E > E_cut implies R > E_cut/E_pred; bins with E_cut/E_lo > 0.6 (E_pred < 5 GeV for E_cut = 3) excluded. Section 4 iso5 comb k fit: 1992 0.965 +- 0.019, 0.975 +- 0.022, 0.964 +- 0.025, 17-46 1.043 +- 0.015; 1993 1.039 +- 0.046, 1.035 +- 0.018, 1.113 +- 0.029, 1.021 +- 0.017, 1.051 +- 0.023; 1994 0.970 +- 0.017, 0.968 +- 0.022, 0.963 +- 0.019, 0.963 +- 0.015, 0.937 +- 0.014; 1995 1.068 +- 0.055, 0.970 +- 0.053, 1.020 +- 0.024, 17-46 1.025 +- 0.012. Section 4.1 constant fits (chi2/ndf, p): 1992 0.999 +- 0.009 (15.8/3, 0.001); 1993 1.043 +- 0.010 (7.8/4, 0.10); 1994 0.958 +- 0.008 (3.1/4, 0.54); 1995 1.023 +- 0.010 (1.7/3, 0.64). Slope b = dk/d ln E, p fit / trunc: 1992 +0.064 +- 0.018 p < 0.001 / +0.072 +- 0.020 p < 0.001; 1993 0.92 / 0.65; 1994 -0.019 +- 0.013 p 0.15 / -0.031 +- 0.014 p 0.025 (driven by 25-46 GeV); 1995 0.99 / 0.24. Rule (closure/REPORT.md 2.1): line a + b ln(E/10 GeV) if the fit-estimator slope has p < 0.05, else constant; so 1994 is constant although its truncated-mean slope has p = 0.025. Width ratio per bin 1.27-1.58. Figure epred/k_vs_epred_iso5.png. "Below 17 GeV": 1992 bins 5-8, 8-12, 12-17 = 0.965, 0.975, 0.964.
-->
