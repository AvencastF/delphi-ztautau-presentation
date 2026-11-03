---
class: st pres c2
---

# Calibration 2 · Step 6c: independent cross-check — swap the channels

<div class="st-sub"><LaTeX formula="k" /> measured on one channel alone (constant per year) scales the simulation of the other. Disjoint events and different simulated processes: statistically independent.</div>

<table class="c2t num first-nw">
<thead><tr><th>Year</th><th><LaTeX formula="\mu\mu\gamma\to ee\gamma" />: before</th><th>after</th><th>pull</th><th><LaTeX formula="ee\gamma\to\mu\mu\gamma" />: before</th><th>after</th><th>pull</th></tr></thead>
<tbody>
<tr><td>1992</td><td><LaTeX formula="0.992\pm0.026" /></td><td><LaTeX formula="0.993\pm0.026" /></td><td><LaTeX formula="-0.24" /></td><td><LaTeX formula="0.996\pm0.025" /></td><td><LaTeX formula="1.014\pm0.025" /></td><td><LaTeX formula="+0.47" /></td></tr>
<tr><td>1993</td><td><LaTeX formula="1.047\pm0.020" /></td><td><LaTeX formula="0.965\pm0.018" /></td><td><LaTeX formula="-1.46" /></td><td><LaTeX formula="1.072\pm0.025" /></td><td><LaTeX formula="1.042\pm0.024" /></td><td><LaTeX formula="+1.51" /></td></tr>
<tr><td>1994</td><td><LaTeX formula="0.946\pm0.014" /></td><td><LaTeX formula="0.980\pm0.014" /></td><td><LaTeX formula="-1.16" /></td><td><LaTeX formula="0.970\pm0.012" /></td><td><LaTeX formula="1.029\pm0.013" /></td><td><LaTeX formula="+1.68" /></td></tr>
<tr><td>1995</td><td><LaTeX formula="1.036\pm0.018" /></td><td><LaTeX formula="1.028\pm0.018" /></td><td><LaTeX formula="+0.94" /></td><td><LaTeX formula="1.028\pm0.024" /></td><td><LaTeX formula="1.011\pm0.024" /></td><td><LaTeX formula="+0.41" /></td></tr>
<tr class="hl"><td><LaTeX formula="\chi^2" /> of the pulls</td><td colspan="3" style="text-align:center">4.4 / 4 (<LaTeX formula="p=0.35" />)</td><td colspan="3" style="text-align:center">5.5 / 4 (<LaTeX formula="p=0.24" />)</td></tr>
</tbody>
</table>
<div class="st-cap">Pull = <LaTeX formula="(\text{after}-1)/\text{error}" />, including the uncertainty of the applied <LaTeX formula="k" />. Peak ratio, 5–46 GeV.</div>

<div class="st-cols st-cols-2" style="margin-top:8px">
<div class="co ok"><b>Closes</b> No pull above 1.7; both directions consistent with 1.</div>
<div class="co warn"><b>Pattern</b> 1993–1994: <LaTeX formula="ee\gamma" /> about 0.03 below <LaTeX formula="\mu\mu\gamma" />, below <LaTeX formula="2\sigma" />.</div>
</div>

<div class="takeaway"><b>Takeaway</b> A scale measured in one channel corrects the other within <LaTeX formula="1.7\sigma" /> in every year: the two channels agree.</div>

<div class="st-source">Source: closure study of the version-2 <LaTeX formula="\ell^+\ell^-\gamma" /> run (2026-11-03), sections 2.1 and 4</div>

<!--
artifacts/llgamma-v2-20261103/closure/REPORT.md section 4, columns "before", "after, constant/line k", pull (the smooth version). Single-channel calibrations (section 2.1(b), constants, since the single-channel bins give no line fit or no significant slope): eeg 0.9822 +- 0.0177 (chi2 7.5/1), 1.0295 +- 0.0139, 0.9440 +- 0.0115, 1.0174 +- 0.0122; mumug 0.9981 +- 0.0125, 1.0768 +- 0.0156, 0.9669 +- 0.0094, 1.0072 +- 0.0242. mumug -> eeg: 1992 0.992 +- 0.026 -> 0.993 +- 0.026 (sigma_k 0.012, pull -0.24); 1993 1.047 +- 0.020 -> 0.965 +- 0.018 (0.016, -1.46); 1994 0.946 +- 0.014 -> 0.980 +- 0.014 (0.009, -1.16); 1995 1.036 +- 0.018 -> 1.028 +- 0.018 (0.024, +0.94). eeg -> mumug: 1992 0.996 +- 0.025 -> 1.014 +- 0.025 (0.018, +0.47); 1993 1.072 +- 0.025 -> 1.042 +- 0.024 (0.014, +1.51); 1994 0.970 +- 0.012 -> 1.029 +- 0.013 (0.012, +1.68); 1995 1.028 +- 0.024 -> 1.011 +- 0.024 (0.012, +0.41). Pull = (ratio - 1)/sqrt(sigma_ratio^2 + sigma_k^2). Chi2 of the four single-year pulls, after_smooth ratio_fit: mumug -> other 4.4/4 (p 0.35), eeg -> other 5.5/4 (p 0.24); the two directions are not independent of each other. Binned version: pulls -0.42, -1.05, -1.17, +0.51 and -0.14, +1.65, +1.26, -0.10 (max 1.65). All years summed: mumug -> eeg 1.000 +- 0.009; eeg -> mumug 1.023 +- 0.009 (pull +2.1, smooth). Channel difference (epred/REPORT.md section 5 and REPORT.md section 2): 1993 eeg 1.044 +- 0.023 vs mumug 1.072 +- 0.018 (1.0 sigma), 1994 0.949 +- 0.011 vs 0.976 +- 0.011 (1.7 sigma), derived.
-->
