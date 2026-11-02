---
class: st pres tk tk-academic
---

# CLS: working points and performance

<div class="st-sub">1992–1995 · held-out simulation · efficiency relative to each preselected truth channel</div>
<div class="cls-wps"><div><b>Cut-based reference</b><span>Exclusive PID + neutral-activity cuts</span></div><div><b>ML assignment</b><span><LaTeX formula="\hat c=\arg\max_c P(c\mid x)" /> · table values</span></div><div><b>Threshold scan</b><span><LaTeX formula="P(c\mid x)>t_c" /> · efficiency–purity curves</span></div></div>
<div class="cls-performance"><div class="cls-curves"><ZoomablePlot src="/figures/ml/05_efficiency_purity.svg" alt="Ten channel efficiency-purity curves with cut-based reference and ML argmax working points" /></div><div class="cls-numbers"><h2>Representative channels</h2><div class="cls-table-note">Cut-based <LaTeX formula="\longrightarrow" /> ML argmax · %</div><table><thead><tr><th>Channel</th><th>Efficiency</th><th>Purity</th></tr></thead><tbody>
<tr><td><LaTeX formula="e\mu" /></td><td>68.8 <LaTeX formula="\to" /> 96.3</td><td>92.1 <LaTeX formula="\to" /> 95.0</td></tr>
<tr><td><LaTeX formula="\pi\pi" /></td><td>51.7 <LaTeX formula="\to" /> 74.6</td><td>16.9 <LaTeX formula="\to" /> 66.4</td></tr>
<tr><td><LaTeX formula="\pi\rho" /></td><td>23.3 <LaTeX formula="\to" /> 81.9</td><td>32.8 <LaTeX formula="\to" /> 64.9</td></tr>
<tr><td><LaTeX formula="\rho\rho" /></td><td>10.4 <LaTeX formula="\to" /> 82.9</td><td>54.7 <LaTeX formula="\to" /> 65.0</td></tr>
</tbody></table><div class="cls-gain"><b><LaTeX formula="\rho\rho" /> efficiency: <LaTeX formula="7.97\times" /></b><span>Higher efficiency and purity<br/>in all ten decay-pair channels</span></div></div></div>
<div class="cls-definition"><LaTeX formula="\epsilon_c=N(\mathrm{selected}\ c,\mathrm{true}\ c)/N(\mathrm{preselected\ true}\ c)" /><LaTeX formula="p_c=N(\mathrm{selected}\ c,\mathrm{true}\ c)/N(\mathrm{selected}\ c)" /></div>

<!--
Original 05_efficiency_purity.svg from all-years internal-note classifier figures. Legend distinguishes score threshold scans, ML argmax and classic regions. Scans are one-vs-rest score selections, not a declared final optimised spin-fit working point; no threshold value invented. Table copied from cls-eval-hold.md (same MC stack, unseen split). All ten channels have higher central efficiency and purity at ML argmax than cuts. Rhorho ratio .829/.104=7.971, rounded7.97; derived from displayed report precision. Pi-pi efficiency gain .746/.517=1.44, NOT fourfold. Full statistical uncertainties in source. Training and evaluation halves are disjoint.
-->
