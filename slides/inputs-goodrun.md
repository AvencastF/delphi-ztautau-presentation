---
class: st pres
---

# Why data yields are lower: the good-run (run-quality) selection

<div class="st-sub">A cassette counts only if its run has a run-quality record and vertex-detector and TPC flags <LaTeX formula="\ge 4" />. Luminosity is recomputed over good cassettes.</div>

<table class="num first-nw">
<thead><tr><th>Year</th><th>No luminosity record</th><th>Bad run quality</th><th>Luminosity [<LaTeX formula="\mathrm{pb}^{-1}" />]</th><th>Data / MC before <LaTeX formula="\to" /> after</th></tr></thead>
<tbody>
<tr><td>1992</td><td>6</td><td>2,699</td><td>24.04</td><td>0.994 <LaTeX formula="\to" /> 0.997</td></tr>
<tr><td>1993</td><td>1,418</td><td>3,566</td><td>9.67 · 16.45 · 9.99</td><td>0.991 <LaTeX formula="\to" /> 0.996</td></tr>
<tr class="hl"><td>1994</td><td>30,855</td><td>5,673</td><td>45.79</td><td>0.959 <LaTeX formula="\to" /> 0.969</td></tr>
<tr><td>1995</td><td>37,193</td><td>2,240</td><td>8.45 · 13.78 · 9.32</td><td>0.973 <LaTeX formula="\to" /> 0.977</td></tr>
</tbody>
</table>
<div class="st-cap">Events removed before any cut. Data/MC of the inclusive sample without <LaTeX formula="Z\to ee" />, before and after the run-quality rule; all years after: 0.982.</div>

<div class="st-cols st-cols-3" style="margin-top:8px">
<div class="co warn"><b>1994</b> Inclusive data 23,073 <LaTeX formula="\to" /> 22,304; luminosity 46.30 <LaTeX formula="\to" /> 45.79.</div>
<div class="co ok"><b>Why</b> Unrecorded runs are dropped; bad cassettes lower the luminosity, so simulation drops too.</div>
<div class="co decision"><b>Rule</b> Detector state only, never a spin observable.</div>
</div>

<div class="st-source">Source: run-quality yield study and owner decision (2026-10-26); rerun with run-quality tables, job 60333695</div>

<!--
Naming: the owner calls this the "trigger" selection in conversation; it is the run-quality rule (RUNQUALI records and vertex-detector / TPC flags), not a hardware trigger requirement. No trigger-level selection is applied anywhere in the analysis.
docs/PROJECT_GUIDE.md "2026-10-26 — run-quality selection adopted: owner decision": in addition to luminosity-table status 0, a data cassette is good only if its run has a RUNQUALI record (the cassette's own row, else the run's first row) and min(MVXA, MVXC) >= 4 and min(TPC0, TPC1) >= 4 (flag values 8 and 9 pass). Sources RUNQUALI.SUMARY92, SUMAR93C, SUMARY94, SUMARY95. Implemented tau_analysis 67bffe7. Exact good-cassette luminosities: 24.038755; 9.672698 / 16.454999 / 9.993902; 45.790648; 8.447493 / 13.78162 / 9.324159 pb-1 (before: 24.14; 9.70/16.59/10.02; 46.30; 8.45/13.81/9.46). Removed by quality: 1994 0.159 pb-1 (no RUNQUALI row: run 47637, fill 2519) + 0.341 (VD) + 0.011 (TPC); 1995_93p0 0.131 (VD).
"rerun with run-quality tables (all-years-rq-20261026)": job 60333695 (4 nodes, 2:57:05, revision 67bffe7); bad_quality events 1992 2,699, 1993 3,566, 1994 5,673, 1995 2,240; inclusive data/MC (Z_ee excluded) 1992 0.997, 1993 0.996, 1994 0.969, 1995 0.977 (before: 0.994 / 0.991 / 0.959 / 0.973 in all-years-20261026); per point 1993 0.994/1.001/0.977, 1995 0.998/0.974/0.973; all years 0.982 (rates-by-group.md: 56,472 / 57,520.061 = 0.98178).
"No luminosity record" column: bad status + not in table from the first all-years run (1992 0 + 6; 1993 1,304 + 114 = 1,418; 1994 0 + 30,855; 1995 0 + 37,193). Check: 2,395,361 - 69,472 - 14,178 = 2,311,711 = the "input" data row of the rerun cutflow (exact).
1994 comparison: frozen 1994 run all-event-detector-1994-20261012 inclusive data 23,073 with luminosity 46.301362 (no run selection); all-years-20261026 (run table only) 1994 data 22,311 / MC 23,269 (0.959); rerun 22,304 / 23,012.3 (0.969). Run quality removed only 7 selected 1994 events (the VD-dead fills and the fill without RUNQUALI row contain no selected events: tau_analysis/docs/RUN_QUALITY_YIELD_STUDY_20261026.md, 1.1 % of luminosity, 26 % of the deficit); the data decrease against the earlier deck comes from the luminosity-record lookup, the ratio improvement from the lower luminosity. Residual flat deficits 3.1 % (1994) / 2.3 % (1995) open; about half attributable to the 1994/1995 MC predicting 1.6-1.9 % more selected events per L sigma than 1993 MC (study).
-->
