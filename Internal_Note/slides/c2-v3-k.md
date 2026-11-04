---
class: st pres c2
---

<script setup>
import ZoomablePlot from 'slidev-addon-ztautau/components/ZoomablePlot.vue'
</script>

# Calibration 2 · Version 3: the scale <LaTeX formula="k" /> per year and its energy dependence

<div class="st-sub"><LaTeX formula="k=\mu_\mathrm{data}/\mu_\mathrm{sim}" /> of <LaTeX formula="R=E_\mathrm{MAIN}/E_\mathrm{pred}" />, both channels, <LaTeX formula="T" /> = 0.5 GeV; bins truncated by the threshold excluded.</div>

<table class="c2t num first-nw">
<thead><tr><th>Year</th><th><LaTeX formula="E_\mathrm{pred}\ge5" /> GeV, <LaTeX formula="d^2E" /></th><th><LaTeX formula="\ge5" /> GeV, <LaTeX formula="5^\circ" /></th><th><LaTeX formula="\ge1" /> GeV, <LaTeX formula="d^2E" /> (<LaTeX formula="\chi^2/\mathrm{ndf}" />)</th><th>Version 2, raw, <LaTeX formula="5^\circ" />, <LaTeX formula="\ge5" /> GeV</th></tr></thead>
<tbody>
<tr><td>1992</td><td><LaTeX formula="1.016\pm0.008" /></td><td><LaTeX formula="1.023\pm0.008" /></td><td><LaTeX formula="1.016\pm0.008" /> (17.7/7)</td><td><LaTeX formula="0.999\pm0.009" /></td></tr>
<tr><td>1993</td><td><LaTeX formula="1.038\pm0.008" /></td><td><LaTeX formula="1.046\pm0.008" /></td><td><LaTeX formula="1.035\pm0.007" /> (2.8/8)</td><td><LaTeX formula="1.043\pm0.010" /></td></tr>
<tr><td>1994</td><td><LaTeX formula="0.988\pm0.005" /></td><td><LaTeX formula="0.989\pm0.006" /></td><td><LaTeX formula="0.987\pm0.005" /> (16.7/8)</td><td><LaTeX formula="0.958\pm0.008" /></td></tr>
<tr><td>1995</td><td><LaTeX formula="1.041\pm0.008" /></td><td><LaTeX formula="1.042\pm0.009" /></td><td><LaTeX formula="1.037\pm0.008" /> (23.5/8)</td><td><LaTeX formula="1.023\pm0.010" /></td></tr>
<tr class="hl"><td>all</td><td><LaTeX formula="1.016\pm0.004" /></td><td><LaTeX formula="1.019\pm0.004" /></td><td><LaTeX formula="1.010\pm0.004" /> (26.2/8)</td><td><LaTeX formula="0.995\pm0.005" /></td></tr>
</tbody>
</table>

<div class="st-fig" style="height:150px;margin-top:6px"><ZoomablePlot src="/figures/photon-calibration/v3/k_fit_vs_epred.png" alt="k versus E_pred per year and all years: v3 MAIN d2E, v3 MAIN 5 deg, v2 raw" /></div>

<div class="st-cols st-cols-2" style="margin-top:4px">
<div class="co ok"><b>Above 3 GeV</b> Flat in all years combined, 1993, 1994; 1995 rises 5 %, 1992 mildly.</div>
<div class="co warn"><b>Below 3 GeV</b> 0.90–0.95 in every year; estimator unstable.</div>
</div>

<div class="takeaway"><b>Takeaway</b> With the MAIN energy, <LaTeX formula="k" /> = 1.016 / 1.038 / 0.988 / 1.041 above 5 GeV; the two isolations agree within 0.008 and <LaTeX formula="k" /> is flat against the 0.5–3 GeV threshold. The year spread shrinks from 0.085 to 0.053.</div>

<div class="st-source">Source: version-3 <LaTeX formula="\ell^+\ell^-\gamma" /> calibration report (2026-11-04), section 5, and its <LaTeX formula="k(E_\mathrm{pred})" /> tables</div>

<!--
artifacts/llgamma-v3-20261104/REPORT.md section 5 (estimator as in v2: GaussExp fit of R in [0.6, 1.4], k = mu_data/mu_MC; truncated mean within +-1.5 sigma as the cross-check; threshold truncation: E_MAIN > T removes R < T/E_pred, effective threshold T_eff = max(T, 0.6 GeV) because of the PHOT floor, a bin is truncated and excluded when T_eff/E_lo > 0.6, so for T = 0.5 GeV only [0.5, 1) GeV is excluded). Section 5.1 table (eeg + mumug, 0.5 GeV regions, untruncated bins) copied: E_pred >= 5 d2E 1.016 +- 0.008 / 1.038 +- 0.008 / 0.988 +- 0.005 / 1.041 +- 0.008 / all 1.016 +- 0.004; >= 5, 5 deg 1.023 +- 0.008 / 1.046 +- 0.008 / 0.989 +- 0.006 / 1.042 +- 0.009 / 1.019 +- 0.004; >= 1 GeV d2E 1.016 +- 0.008 (17.7/7) / 1.035 +- 0.007 (2.8/8) / 0.987 +- 0.005 (16.7/8) / 1.037 +- 0.008 (23.5/8) / 1.010 +- 0.004 (26.2/8); v2 raw 5 deg >= 5 GeV 0.999 +- 0.009 / 1.043 +- 0.010 / 0.958 +- 0.008 / 1.023 +- 0.010 / 0.995 +- 0.005. Per channel (>= 5 GeV, d2E): eeg 1.007 / 1.027 / 0.989 / 1.044, mumug 1.007 / 1.050 / 0.991 / 1.029 (errors 0.007-0.016), agree within 1.3 sigma in every year. Truncated mean agrees with the fit within 0.01 above 3 GeV (1992: 0.994 vs 1.016 with the 1-3 GeV bins). Section 5.2 (d2E, comb, fit): all years 1-1.5 GeV 0.867 +- 0.055 (trunc 0.939 +- 0.018), 1.5-2 0.940 +- 0.028 (0.902 +- 0.038), 2-3 0.944 +- 0.027 (0.948 +- 0.020), 3-5 0.990 +- 0.011, 5-8 1.014 +- 0.009, 8-12 1.020 +- 0.010, 12-17 1.008 +- 0.009, 17-25 1.021 +- 0.007, 25-46 1.012 +- 0.010; per year e.g. 1995 12-17 1.03 +- 0.02, 17-25 1.08 +- 0.01; 1992 5-8/8-12/12-17 1.00/0.99/0.99, 17-46 1.05 +- 0.01. Fits a + b ln(E_pred/10 GeV) over untruncated bins: 1992 b = 0.027 +- 0.012 (p 0.03), 1993 0.006 +- 0.011 (0.55), 1994 -0.011 +- 0.007 (0.09), 1995 0.049 +- 0.014 (0.0004), all 0.017 +- 0.005 (0.0006); above 3 GeV a constant describes all years combined (6.7/5) and 1993, 1994 individually; 1995 rises by 5 % between 12 and 25 GeV in both channels; 1992 0.99 at 5-17 GeV, 1.05 at 17-46 (raw energy: 0.965 -> 1.043). Slopes of the full-range fits are driven by the 1-3 GeV bins: 0.90-0.95 in every year with both estimators, GaussExp tail parameter at its limit, fit errors 0.05-0.2. Section 5.3 inclusive k (all years, E_pred >= T_eff/0.6): eeg 1.006 (0.5) -> 1.011 (1) -> 1.012 (2) -> 1.013 (3 GeV); mumug 1.003 -> 1.008 -> 1.014 -> 1.016; d2E and 5 deg within 0.004 at every threshold; the 0.01 drift is the sub-3 GeV fall entering the inclusive sample. "Within 0.008" derived from the >= 5 GeV columns: 5 deg - d2E = 0.007 / 0.008 / 0.001 / 0.001 / all 0.003; REPORT.md section 1 states "within 0.007", which the rounded table values exceed by 0.001 in 1993, so the slide uses the derived 0.008. Year spread 0.085 -> 0.053: REPORT.md section 1 (v2 1.043 - 0.958 = 0.085; v3 1.041 - 0.988 = 0.053, derived check). Figure figures/k_fit_vs_epred.png (v3 d2E red, v3 5 deg green, v2 raw iso5 and iso5_e1p5 blue/purple; open = threshold-truncated, excluded).
-->
