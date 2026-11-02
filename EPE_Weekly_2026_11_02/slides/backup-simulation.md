---
class: st pres tk
---

# Backup · the new simulation

<div class="st-sub">Eight energy points, four detector descriptions: seven processes per point through the preserved DELPHI simulation and reconstruction.</div>

<div class="tk-split wide">
<div>
<table class="num first-nw" style="font-size:13px">
<thead><tr><th>Point</th><th><LaTeX formula="Z\to\tau\tau" /> events</th><th>All processes</th></tr></thead>
<tbody>
<tr><td>1992 · 91.3 GeV</td><td>3,018,599</td><td>7,520,747</td></tr>
<tr><td>1993 · 89.4 GeV</td><td>401,400</td><td>1,718,098</td></tr>
<tr><td>1993 · 91.2 GeV</td><td>2,062,799</td><td>5,174,097</td></tr>
<tr><td>1993 · 93.0 GeV</td><td>577,800</td><td>1,922,399</td></tr>
<tr class="hl"><td>1994 · 91.2 GeV</td><td>5,747,400</td><td>14,453,096</td></tr>
<tr><td>1995 · 89.4 GeV</td><td>350,100</td><td>1,485,000</td></tr>
<tr><td>1995 · 91.3 GeV</td><td>1,725,300</td><td>4,318,197</td></tr>
<tr><td>1995 · 93.0 GeV</td><td>558,900</td><td>1,848,595</td></tr>
<tr><td>All</td><td>14,442,298</td><td>38,440,229</td></tr>
</tbody>
</table>
</div>
<div>
<div class="kv sim"><h3>Processes and generators</h3><dl>
<dt>Signal</dt><dd><LaTeX formula="Z\to\tau^+\tau^-" />, PYTHIA 8.3 with <LaTeX formula="\tau" /> spin correlations</dd>
<dt><LaTeX formula="Z" /> decays</dt><dd><LaTeX formula="ee,\ \mu\mu,\ q\bar q" />, PYTHIA 8.3</dd>
<dt>Two-photon</dt><dd><LaTeX formula="\gamma\gamma\to\ell\ell" />, <LaTeX formula="\gamma\gamma\to" /> hadrons</dd>
<dt>Bhabha</dt><dd>BHWIDE</dd>
<dt>Detector</dt><dd>preserved DELPHI full simulation and reconstruction, one description per year</dd>
</dl></div>
<ul class="tk-points" style="margin-top:10px">
<li class="ok"><b>Size</b> About 45 times the data after selection; half trains the networks, half serves evaluation and the fit.</li>
<li class="open"><b>Validation</b> 1994 checked against data in detail; the other years are being validated.</li>
</ul>
</div>
</div>

<div class="tk-foot">Reconstructed event counts; <LaTeX formula="Z\to ee" /> is simulated but replaced by the Bhabha sample, which contains it.</div>

<style>
.tk .kv { font-size: 13px; }
.tk .kv dl { gap: 3px 10px; }
.tk .tk-points li { font-size: 13.5px; padding: 6px 12px; }
</style>
