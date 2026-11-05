---
class: st pres c2
---

<script setup>
import ZoomablePlot from 'slidev-addon-ztautau/components/ZoomablePlot.vue'
</script>

# Calibration 2 · Final <LaTeX formula="\pi^0" /> step (v3): the stored constants per year

<div class="st-sub">Classes A+B, <LaTeX formula="\pi^0" /> + <LaTeX formula="\ell^+\ell^-\gamma" /> constraints; errors <LaTeX formula="\times1.236" />. <LaTeX formula="k" /> stored as a table 0.5–46 GeV, linear in <LaTeX formula="\ln E" />, data untouched.</div>

<table class="c2t num first-nw">
<thead><tr><th>Year</th><th><LaTeX formula="s" /></th><th><LaTeX formula="b" /></th><th><LaTeX formula="a" /> [<LaTeX formula="\sqrt{\mathrm{GeV}}" />]</th><th><LaTeX formula="k(1\ \mathrm{GeV})" /></th><th><LaTeX formula="k(2\ \mathrm{GeV})" /></th><th><LaTeX formula="k(3\ \mathrm{GeV})" /></th></tr></thead>
<tbody>
<tr><td>1992</td><td><LaTeX formula="1.0028\pm0.0093" /></td><td><LaTeX formula="+0.035\pm0.052" /></td><td><LaTeX formula="0.225\pm0.091" /></td><td><LaTeX formula="0.929\pm0.054" /></td><td><LaTeX formula="0.952\pm0.020" /></td><td><LaTeX formula="0.966\pm0.009" /></td></tr>
<tr><td>1993</td><td><LaTeX formula="0.9994\pm0.0085" /></td><td><LaTeX formula="+0.085\pm0.067" /></td><td><LaTeX formula="0.256\pm0.098" /></td><td><LaTeX formula="0.941\pm0.075" /></td><td><LaTeX formula="1.002\pm0.027" /></td><td><LaTeX formula="1.038\pm0.009" /></td></tr>
<tr><td>1994</td><td><LaTeX formula="1.0025\pm0.0062" /></td><td><LaTeX formula="-0.064\pm0.060" /></td><td><LaTeX formula="0.319\pm0.079" /></td><td><LaTeX formula="1.058\pm0.064" /></td><td><LaTeX formula="1.014\pm0.023" /></td><td><LaTeX formula="0.989\pm0.006" /></td></tr>
<tr><td>1995</td><td><LaTeX formula="1.0029\pm0.0095" /></td><td><LaTeX formula="+0.059\pm0.058" /></td><td><LaTeX formula="0.299\pm0.111" /></td><td><LaTeX formula="0.973\pm0.064" /></td><td><LaTeX formula="1.016\pm0.024" /></td><td><LaTeX formula="1.040\pm0.010" /></td></tr>
</tbody>
</table>

<div class="st-cols st-cols-21" style="gap:12px;margin-top:6px">
<div class="st-fig" style="height:168px"><ZoomablePlot src="/figures/photon-calibration/pi0-v3/k_years_v3.png" alt="k(E) per year: v3 with its band, pi0-only, the v2 table, and the l+l-gamma bins" /></div>
<div class="st-fig" style="height:168px"><ZoomablePlot src="/figures/photon-calibration/pi0-v3/smear_v3.png" alt="smearing a per year: v3 from the pi0 width against v2 from l+l-gamma" /></div>
</div>
<div class="st-cap"><b>Left</b> <LaTeX formula="k(E)" /> per year: v3 (line, band), <LaTeX formula="\pi^0" />-only (dotted), stored v2 (dashed), <LaTeX formula="\ell^+\ell^-\gamma" /> bins (points). <b>Right</b> smearing <LaTeX formula="a" />: v3 from the <LaTeX formula="\pi^0" /> width against v2 from <LaTeX formula="\ell^+\ell^-\gamma" /> (0.268 / 0.312 / 0.276 / 0.287).</div>

<div class="takeaway"><b>Takeaway</b> Above 3 GeV the <LaTeX formula="\ell^+\ell^-\gamma" /> scale stands (<LaTeX formula="s" /> = 1 within 0.3 %); below it the simulated photons are scaled down 5–7 % in 1992–93 and 1995 and up 6 % in 1994 at 1 GeV, and smeared by <LaTeX formula="0.23" />–<LaTeX formula="0.32/\sqrt{E}" />.</div>

<div class="st-source">Source: final-calibration report of 2026-11-04, section 1 and its tables T2, T9; figures of that report</div>

<!--
artifacts/pi0-final-calib-20261104/CALIBRATION_V3_REPORT.md section 1 table (stored: form table, valid_gev [0.5, 46], knots 0.5, 0.75, 1, 1.5, 2 GeV plus the v2 knots from 3 GeV, linear in ln E, held outside; errors = profile errors x 1.236, fully correlated through (s, b); covariances in json/final_v3.json; skip_codes [101]; conversions not in the section): 1992 s 1.0028 +- 0.0093, b +0.035 +- 0.052, a 0.225 +- 0.091, k(0.5) 0.905 +- 0.088, k(1) 0.929 +- 0.054, k(2) 0.952 +- 0.020, k(3) 0.966 +- 0.009, from 3 GeV 0.966 / 1.003 / 1.021 / 1.000 / 1.012 / 1.060 at 3.93 / 6.43 / 9.80 / 14.3 / 20.5 / 29.9-46 GeV; 1993 0.9994 +- 0.0085, +0.085 +- 0.067, 0.256 +- 0.098, 0.880 +- 0.123, 0.941 +- 0.075, 1.002 +- 0.027, 1.038 +- 0.009 (flat); 1994 1.0025 +- 0.0062, -0.064 +- 0.060, 0.319 +- 0.079, 1.101 +- 0.104, 1.058 +- 0.064, 1.014 +- 0.023, 0.989 +- 0.006, from 3 GeV 0.989 / 1.007 / 1.015 / 0.998 / 0.978 / 0.954; 1995 1.0029 +- 0.0095, +0.059 +- 0.058, 0.299 +- 0.111, 0.930 +- 0.106, 0.973 +- 0.064, 1.016 +- 0.024, 1.040 +- 0.010 (flat). Correlations (s,b) +0.21..+0.28, (b,a) -0.21..-0.46, (s,a) -0.07..+0.10. tables_v3.md T2 (stored k(E) table), T9 (v3 vs v2 at the knots; v2 1992 k(1) 0.983, k(2) 0.971, a 0.268 +- 0.026; 1993 1.060, 1.046, 0.312 +- 0.028; 1994 1.006, 0.994, 0.276 +- 0.020; 1995 1.059, 1.045, 0.287 +- 0.030). Takeaway: "s = 1 within 0.3 %" derived from the s column (largest |s - 1| = 0.0029); "5-7 % down at 1 GeV" derived from k(1) 0.929 / 0.941 / 0.973 (1992, 1993, 1995), "+6 %" from 1994 1.058. Figures artifacts/pi0-final-calib-20261104/figures/k_years_v3.png (v3 line and band x1.24, pi0-only dotted, v2 table dashed, l+l-gamma v4 bins as points) and smear_v3.png (v3 pi0 width vs v2 l+l-gamma v4), copied unchanged to public/figures/photon-calibration/pi0-v3/ (sha256 in public/figures/MANIFEST.md); made by scripts/pi0_v3_plots.py of that artifact.
-->
