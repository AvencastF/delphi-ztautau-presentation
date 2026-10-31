---
class: st pres
---

# Classifier on the hold half, year by year

<div class="st-sub">Same model for every year. Accuracy = fraction of simulated <LaTeX formula="\tau" /> pairs assigned their true decay channel.</div>

<table class="num first-nw">
<thead><tr><th>Hold half</th><th>All years</th><th>1992</th><th>1993</th><th>1994</th><th>1995</th><th>1994-only model</th></tr></thead>
<tbody>
<tr><td><LaTeX formula="\tau" />-channel accuracy, cut-based</td><td>0.408</td><td>0.385</td><td>0.409</td><td>0.415</td><td>0.416</td><td>—</td></tr>
<tr class="hl"><td><LaTeX formula="\tau" />-channel accuracy, ML</td><td>0.884</td><td>0.875</td><td>0.886</td><td>0.887</td><td>0.886</td><td>0.880</td></tr>
<tr><td><LaTeX formula="\pi\pi" /> efficiency / purity</td><td>0.746 / 0.664</td><td>0.727 / 0.651</td><td>0.747 / 0.666</td><td>0.760 / 0.668</td><td>0.734 / 0.669</td><td>0.766 / 0.746</td></tr>
<tr><td><LaTeX formula="ee" /> purity</td><td>0.867</td><td>0.857</td><td>0.863</td><td>0.877</td><td>0.863</td><td>0.909</td></tr>
<tr><td>Data/MC yields <LaTeX formula="\chi^2/10" />, ML</td><td>60.4</td><td>25.5</td><td>21.8</td><td>41.8</td><td>24.3</td><td>25.3</td></tr>
<tr><td>Data/MC yields <LaTeX formula="\chi^2/10" />, cut-based</td><td>70.0</td><td>56.4</td><td>15.6</td><td>25.2</td><td>39.8</td><td>15.0</td></tr>
</tbody>
</table>

<div class="st-cols st-cols-3" style="margin-top:10px">
<div class="co ok"><b>Uniform</b> Accuracy 0.875–0.887 in every year.</div>
<div class="co warn"><b>1994-only column</b> Training events included: purities biased high.</div>
<div class="co open"><b>Data/MC</b> 1994 <LaTeX formula="\rho" /> channels 0.94; 1992 <LaTeX formula="\pi\pi" /> 1.24; 1995 <LaTeX formula="ee" /> 0.85.</div>
</div>

<div class="st-source">Source: all-years classifier evaluations (hold half, all years and per year, 2026-10-27); simulation closure only</div>

<!--
artifacts/ml-all-years-v1-20261027/README.md "Classifier (hold half)" and cls-eval-hold.md / cls-eval-year-YYYY.md (mc_split unseen; NERSC skim-cls-nu-cls-eval and skim-cls-nu-cls-eval-year-YYYY, jobs 60363881 / 60366303). Cut-based tau channel accuracy: all 0.4079, 1992 0.3851, 1993 0.4085, 1994 0.4152, 1995 0.4164; ML 0.8841 / 0.8752 / 0.8861 / 0.8869 / 0.8856. Signal fraction of selected events: ML 0.7862 (all), 0.7746 / 0.7885 / 0.7909 / 0.7865; cut-based 0.5728. Channel-yield chi2/ndf data vs MC (stat.): ML 60.4 / 25.5 / 21.8 / 41.8 / 24.3, classic 70.0 / 56.4 / 15.6 / 25.2 / 39.8. 1994-only classifier v1: reference-1994-cls-v1-eval-all-rows.md (evaluated on all rows, training rows included: purities biased high; the comparison on identical unseen rows is impossible because every 1994 row was in its training, PROJECT_GUIDE 2026-10-27). Data/MC per channel (ML selection): 1994 erho / murho / rhorho 0.94 (classic 0.97-1.01); 1992 pipi 1.24 +- 0.08, mupi 1.11 +- 0.04; 1995 ee 0.85 +- 0.04 (classic 0.78); mumu 1.04-1.10 in every year. Inclusive preselection per year: 1992 11,679 / 11,717.5; 1993 12,046 / 12,100.4; 1994 22,304 / 23,012.3; 1995 10,443 / 10,689.8.
-->
