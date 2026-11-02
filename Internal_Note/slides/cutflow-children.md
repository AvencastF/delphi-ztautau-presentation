---
class: st pres
---

# Yields of the ten children, per year

<div class="st-sub">Matching fraction = simulated <LaTeX formula="\tau" /> pairs whose true decay equals the child / all simulated <LaTeX formula="\tau" /> pairs in the child.</div>

<div class="st-cols st-cols-21">
<div>
<table class="num first-nw">
<thead><tr><th>Child</th><th>All years: data / MC</th><th>1992</th><th>1993</th><th>1994</th><th>1995</th><th>Matching</th></tr></thead>
<tbody>
<tr><td><LaTeX formula="ee" /></td><td>2,028 / 2,266</td><td>0.86</td><td>0.92</td><td>0.95</td><td>0.78</td><td><span class="badge g">0.907</span></td></tr>
<tr><td><LaTeX formula="e\mu" /></td><td>3,919 / 4,134</td><td>1.00</td><td>0.96</td><td>0.93</td><td>0.93</td><td><span class="badge g">0.922</span></td></tr>
<tr><td><LaTeX formula="e\pi" /></td><td>4,253 / 4,452</td><td>0.90</td><td>0.98</td><td>0.94</td><td>1.01</td><td><span class="badge r">0.423</span></td></tr>
<tr><td><LaTeX formula="e\rho" /></td><td>2,628 / 2,644</td><td>1.04</td><td>0.93</td><td>0.98</td><td>1.06</td><td><span class="badge a">0.703</span></td></tr>
<tr><td><LaTeX formula="\mu\mu" /></td><td>2,728 / 2,545</td><td>1.19</td><td>1.08</td><td>1.06</td><td>0.97</td><td><span class="badge g">0.943</span></td></tr>
<tr><td><LaTeX formula="\mu\pi" /></td><td>4,727 / 4,819</td><td>1.04</td><td>0.98</td><td>0.96</td><td>0.97</td><td><span class="badge r">0.429</span></td></tr>
<tr><td><LaTeX formula="\mu\rho" /></td><td>2,996 / 2,899</td><td>1.14</td><td>1.03</td><td>1.00</td><td>0.99</td><td><span class="badge a">0.717</span></td></tr>
<tr><td><LaTeX formula="\pi\pi" /></td><td>2,488 / 2,480</td><td>1.03</td><td>0.95</td><td>0.98</td><td>1.08</td><td><span class="badge r">0.173</span></td></tr>
<tr><td><LaTeX formula="\pi\rho" /></td><td>3,075 / 2,999</td><td>1.07</td><td>0.98</td><td>0.99</td><td>1.10</td><td><span class="badge r">0.328</span></td></tr>
<tr><td><LaTeX formula="\rho\rho" /></td><td>979 / 922</td><td>1.21</td><td>1.09</td><td>1.00</td><td>1.01</td><td><span class="badge a">0.546</span></td></tr>
</tbody>
</table>
<div class="st-cap">Year columns: data / MC ratio. Statistical error of a year ratio: 3–8 %.</div>
</div>
<div>
<div class="tiles tiles-2" style="margin:0 0 10px">
<div class="tile data"><b>29,821</b><span>data events in children, of 56,472 inclusive</span></div>
<div class="tile sim"><b>0.173</b><span>matching fraction of the <LaTeX formula="\pi\pi" /> child</span></div>
</div>
<div class="co open"><b><LaTeX formula="ee" /></b> 1992 and 1995 data 14 % and 22 % low.</div>
<div class="co open"><b><LaTeX formula="\mu\mu" /></b> 1992 data 19 % high.</div>
<div class="co warn"><b>Not purity</b> Non-matching events are mostly other <LaTeX formula="\tau" /> decays.</div>
</div>
</div>

<div class="st-source">Source: count and composition tables of the 1992–1995 run-quality rerun (job 60333695)</div>

<!--
data/nersc-all-years-rq-20261026/cutflows/cutflow.csv, last cut of each region inclusive_1p1p_<child> (id_<child>), and exclusive_confusion.csv (sha256 faa4495f77003b0db3f2c43a8bd71ba2bf470108684c5bc5a2b087e53e6e0fda; all years together: the confusion table has no year split). Data / signed MC without Z_ee: ee 1992 400/464.067, 1993 446/485.000, 1994 851/891.413, 1995 331/425.418; matching 1680.47/1853.09; emu 1992 805/806.237, 1993 813/850.848, 1994 1585/1702.984, 1995 716/773.763; matching 3808.89/4130.70; epi 1992 859/952.677, 1993 934/951.789, 1994 1642/1741.337, 1995 818/806.376; matching 1789.06/4225.81; erho 1992 526/506.319, 1993 524/564.337, 1994 1050/1076.789, 1995 528/496.597; matching 1852.34/2633.34; mumu 1992 556/466.592, 1993 566/524.494, 1994 1125/1057.593, 1995 481/496.003; matching 2126.28/2255.38; mupi 1992 1023/987.153, 1993 999/1023.459, 1994 1844/1919.032, 1995 861/888.873; matching 2032.08/4731.91; murho 1992 605/528.417, 1993 630/609.586, 1994 1207/1201.839, 1995 554/559.249; matching 2078.57/2897.17; pipi 1992 585/565.522, 1993 515/543.596, 1994 919/935.586, 1995 469/434.818; matching 422.96/2449.10; pirho 1992 654/611.177, 1993 640/654.521, 1994 1173/1179.077, 1995 608/553.940; matching 983.83/2996.34; rhorho 1992 202/166.341, 1993 220/201.430, 1994 377/375.419, 1995 180/178.865; matching 503.20/922.01. Children data sum 29,821, MC 30158.532; inclusive 56,472. Year-ratio statistical errors 3-8 % (derived from the counts, e.g. 1995 ee 331 events: 5.5 % data alone). The ML classifier evaluation of 2026-10-27 shows the same pattern for the cut-based selection (1992 ee 0.859 +- 0.044, 1995 ee 0.78 classic; mumu 0.97-1.21). Badge colours: green >= 0.9, amber 0.5-0.9, red < 0.5 (presentation choice). The 2026-10-22 version showed the frozen 1994 run (12,161 data events in children).
-->
