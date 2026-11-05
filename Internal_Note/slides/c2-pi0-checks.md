---
class: st pres c2
---

<script setup>
import ZoomablePlot from 'slidev-addon-ztautau/components/ZoomablePlot.vue'
</script>

# Calibration 2 · Final <LaTeX formula="\pi^0" /> step (v3): cross-checks and closure on the odd events

<div class="st-sub">Scale against <LaTeX formula="\ell^+\ell^-\gamma" />, year and half-sample independence, estimator closure on simulation; then the even-event constants applied to the odd-event pairs.</div>

<div class="st-cols" style="display:grid;grid-template-columns:1.55fr 1fr;gap:12px">
<div>
<table class="c2t num first-nw" style="font-size:11.5px">
<thead><tr><th>Check</th><th>1992</th><th>1993</th><th>1994</th><th>1995</th><th>Verdict</th></tr></thead>
<tbody>
<tr class="hl"><td><LaTeX formula="\pi^0" />-only scale (<LaTeX formula="\ell^+\ell^-\gamma" /> = 1.000)</td><td>1.025</td><td>1.026</td><td>1.039</td><td>1.069</td><td><LaTeX formula="\chi^2" /> 10.5/4 (<LaTeX formula="p" /> 0.033): open</td></tr>
<tr class="hl"><td>pull of the <LaTeX formula="\ell^+\ell^-\gamma" /> scale</td><td>+0.95</td><td>+1.20</td><td>+1.69</td><td>+2.30</td><td>all positive</td></tr>
<tr><td>Year independence</td><td colspan="4"><LaTeX formula="b" />: <LaTeX formula="\chi^2" /> 5.2/3; <LaTeX formula="a" />: 1.1/3</td><td>consistent</td></tr>
<tr><td>Even vs odd events, <LaTeX formula="p" /></td><td>0.87</td><td>—</td><td><b>0.013</b></td><td>0.52</td><td>1994 slope disagrees; 1993 odd fit not valid</td></tr>
<tr><td>Simulation closure of the estimator</td><td colspan="4">12 pulls: mean <LaTeX formula="-0.16" />, RMS 1.09</td><td>no bias</td></tr>
<tr><td>Odd-event pairs, A+B, all years: peak</td><td colspan="4"><LaTeX formula="0.974\to0.987\pm0.013" /></td><td>closes</td></tr>
<tr><td>Odd-event pairs: width</td><td colspan="4"><LaTeX formula="1.32\to0.95\pm0.07" /></td><td>closes; class A alone 0.78</td></tr>
</tbody>
</table>
<style>.c2t td:last-child, .c2t td[colspan] { white-space: normal !important; }</style>
<div class="st-cap">Peak and width: data/simulation of a Gaussian + linear fit to <LaTeX formula="m_{\gamma\gamma}" />, before (raw simulation) → after v3. Per year the peak scatters by ±0.05 (1992 1.07, 1995 0.96).</div>
</div>
<div>
<div class="st-fig" style="height:132px"><ZoomablePlot src="/figures/photon-calibration/pi0-v3/closure_odd_summary.png" alt="odd-event pair closure: peak and width data/MC before and after per year and class" /></div>
<div class="st-fig" style="height:150px;margin-top:4px"><ZoomablePlot src="/figures/photon-calibration/pi0-v3/mgg_odd_closure_AB.png" alt="m_gammagamma of odd-event pairs per year, data against MC before and after v3" /></div>
</div>
</div>

<div class="takeaway"><b>Takeaway</b> The estimator is unbiased and the years agree; on the independent odd half the <LaTeX formula="\pi^0" /> width closes (1.32 → 0.95). Two tensions stay open: the <LaTeX formula="\pi^0" /> wants 2.5–7 % more simulated energy above 3 GeV than <LaTeX formula="\ell^+\ell^-\gamma" />, and the 1994 halves disagree on the slope.</div>

<div class="st-source">Source: final-calibration report of 2026-11-04, sections 4.3, 4.6–4.8, 5, and its tables T3, T6–T8; closure figures of that report</div>

<!--
artifacts/pi0-final-calib-20261104/CALIBRATION_V3_REPORT.md section 4.3 / tables_v3.md T3: pi0-only s 1.025 +- 0.025 / 1.026 +- 0.024 / 1.039 +- 0.023 / 1.069 +- 0.030 against the l+l-gamma scale relative to g 1.000 +- 0.008 / 0.996 +- 0.007 / 1.000 +- 0.004 / 0.997 +- 0.008; pulls +0.95 / +1.20 / +1.69 / +2.30; chi2 10.5/4 (p 0.033); 24 per-bin pulls mean +0.81 RMS 0.62 (T3 lists mean +1.34, RMS 0.61 for the per-bin table; the report text gives +0.81 / 0.62 - the two numbers differ in the source, neither is on the slide); "2.5-7 % more energetic at >= 3 GeV" from the report text. Section 4.6 / T6: b weighted mean +0.027 +- 0.024, chi2 5.2/3 (p 0.16); a 0.277 +- 0.037, chi2 1.1/3 (p 0.79). Section 4.7 / T7: even/odd chi2/3 (p) 1992 0.7 (0.87), 1993 odd not valid (vertex outside the grid), 1994 10.7 (0.013), 1995 2.3 (0.52); sum 13.7/9 -> S = 1.236. Section 4.8 / T8: pseudo-data odd-event Z -> tau tau MC with s = 1, b = -0.05, a = 0.30, even-event templates, pi0-only grid, all classes; 12 pulls mean -0.16, RMS 1.09. Section 5 (even -> odd pair closure, Gaussian + linear, binned Poisson, 0.05-0.23 GeV, 5 MeV; before = raw MC): A+B all years 3491 data pi0 signal, mu data/MC 0.974 +- 0.013 -> 0.987 +- 0.013, sigma 1.32 +- 0.10 -> 0.95 +- 0.07; per year 1992 1.004 -> 1.073 +- 0.027 (sigma 1.26 -> 0.93), 1993 0.955 -> 0.966 (1.12 -> 0.85), 1994 0.962 -> 0.972 (1.43 -> 0.95), 1995 0.995 -> 0.957 (1.29 -> 0.90); class A alone 0.980 -> 0.981, sigma 1.07 -> 0.78 +- 0.05 (MC too wide; class A is selected on raw MC energies - selection bias, report sections 5 and 8); class B 0.961 -> 0.977, 1.55 -> 1.10. Figures artifacts/pi0-final-calib-20261104/figures/closure_odd_summary.png and mgg_odd_closure_AB.png, copied unchanged to public/figures/photon-calibration/pi0-v3/.
-->
