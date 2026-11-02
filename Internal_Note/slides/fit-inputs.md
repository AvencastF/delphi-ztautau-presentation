---
class: st pres
---

# Regions and samples: what is fitted and what is fixed

<div class="st-sub">A region = events whose two decays were reconstructed as one pair, e.g. <LaTeX formula="\pi" /> and <LaTeX formula="\rho" />. Composition of the simulation, 1994, ML.</div>

<div class="st-cols st-cols-21">
<div>
<table class="num first-nw">
<thead><tr><th>Region</th><th>MC events</th><th>Matched true pair</th><th>Other <LaTeX formula="\tau\tau" /> pairs</th><th><LaTeX formula="\tau" /> to other modes</th><th>Non-<LaTeX formula="\tau" /></th></tr></thead>
<tbody>
<tr><td><LaTeX formula="\pi\pi" /></td><td>272.5</td><td>68.9 %</td><td>22.0 %</td><td>8.2 %</td><td>0.9 %</td></tr>
<tr><td><LaTeX formula="\pi\rho" /></td><td>558.0</td><td>64.1 %</td><td>17.2 %</td><td>18.4 %</td><td>0.3 %</td></tr>
<tr><td><LaTeX formula="\rho\rho" /></td><td>1,885.7</td><td>66.3 %</td><td>4.9 %</td><td>28.8 %</td><td>0.1 %</td></tr>
<tr><td><LaTeX formula="ee" /></td><td>842.0</td><td>87.3 %</td><td>4.3 %</td><td>0.5 %</td><td>7.9 %</td></tr>
<tr><td><LaTeX formula="\mu\mu" /></td><td>881.2</td><td>93.8 %</td><td>3.0 %</td><td>0.2 %</td><td>3.0 %</td></tr>
<tr><td><LaTeX formula="\pi e" /></td><td>489.5</td><td>79.0 %</td><td>15.4 %</td><td>4.9 %</td><td>0.7 %</td></tr>
<tr><td><LaTeX formula="\rho e" /></td><td>1,046.5</td><td>81.3 %</td><td>3.4 %</td><td>15.1 %</td><td>0.3 %</td></tr>
<tr class="hl"><td>All 16</td><td>12,970.5</td><td colspan="2" style="text-align:center">87.4 % float in the fit</td><td>11.7 %</td><td>0.9 %</td></tr>
</tbody>
</table>
<div class="st-cap">Percent of the region's simulated events (derived). First two columns: spin-dependent signal; last two: fixed. Each region gives 15 histograms of 10 bins: 2,400 bins.</div>
</div>
<div>
<div class="co ok"><b>Signal</b> Any true <LaTeX formula="\pi,\rho,e,\mu" /> pair, even if mis-identified: its spin is modelled.</div>
<div class="co decision"><b>Fixed</b> Other <LaTeX formula="\tau" /> decay modes 12 %, non-<LaTeX formula="\tau" /> events 1 %: taken from simulation.</div>
<div class="co warn"><b>Why fixed</b> No analysing power is defined for the other modes.</div>
<div class="co ok"><b>Cross-check</b> Mis-identified pairs as background instead: errors grow only 1–3 %.</div>
</div>
</div>

<div class="st-source">Source: template inventory of the reweighted-template model and the matched-only variant fit, 1994 ML (2026-10-31); simulation only</div>

<!--
Fit cut (legacy processor): flags_valid > 0, theta_cm > 0.6, m_tautau > 80 GeV. Sums of weights (Asimov = all MC) from artifacts/legacy-fit-ml-allyears-20261030/runs-variants/1994_91p2-ml-matched-only/comparison.md (Asimov total, matched signal, moved S->B) and artifacts/joint-fit-20261031/modelB/1994_91p2-ml/summary.md (per-region Z->tautau sum, listed vs usable, Ztautau_others). Columns: matched = matched-only signal (pion regions) / listed template (others); "other tautau pairs" = listed cross-feed (pipi: pirho 19.5 + rhopi 17.8 = 37.2; pirho: rhorho 36.5) + unlisted cross-feed now floating in models B/C (pipi 22.7, pirho 59.5, rhorho 91.8, ee 36.3, mumu 26.1, pie 75.3, rhoe 35.1); "tau to other modes" = Ztautau_others (pipi 22.3, pirho 102.6, rhorho 543.0, ee 4.3, mumu 2.2, pie 24.1, rhoe 157.6); non-tau = total - Z->tautau (derived: pipi 2.4, pirho 1.5, rhorho 1.6, ee 66.2, mumu 26.3, pie 3.1, rhoe 3.0). Totals: all MC 12970.5, Z->tautau 12851.9, usable (floating) 11337.6, Ztautau_others 1514.2 (11.7 % of all MC; 11.8 % of Z->tautau), non-tau 118.6; fixed 1632.9 = 12.59 % (owner decision: Ztautau_others fixed, no analysing power invented). Legacy model A floated only the listed templates (fixed 18.7 %; per region 3.7-33.7 %). Matched-only variant (cross-feed in pipi/pirho/rhopi frozen as background): scan sigma ratio 1.014-1.017 (B), 1.023-1.032 (C), concurrence 1.028; 114.1 of 12,970 events moved.
Combined 1992-1995 ML: all MC 32335.8 after the fit cut (joint-fit step 1).
-->
