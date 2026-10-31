---
class: st pres
---

# Simulation: eight energy points, four detector descriptions

<div class="st-sub">Seven processes per point, simulated with the detector description of the year. 90 % of generated events are converted by design.</div>

<div class="st-cols st-cols-21">
<div>
<table class="num first-nw">
<thead><tr><th>Point [GeV]</th><th>Detector</th><th><LaTeX formula="Z\to\tau\tau" /> converted</th><th>All processes: generated / converted</th></tr></thead>
<tbody>
<tr><td>1992 · 91.3</td><td><span class="id">v92e</span></td><td>3,018,599</td><td>8,374,000 / 7,520,747</td></tr>
<tr><td>1993 · 89.4</td><td><span class="id">v93d</span></td><td>401,400</td><td>1,909,000 / 1,718,098</td></tr>
<tr><td>1993 · 91.2</td><td><span class="id">v93d</span></td><td>2,062,799</td><td>5,749,000 / 5,174,097</td></tr>
<tr><td>1993 · 93.0</td><td><span class="id">v93d</span></td><td>577,800</td><td>2,137,000 / 1,922,399</td></tr>
<tr class="hl"><td>1994 · 91.2</td><td><span class="id">v94c</span></td><td>5,747,400</td><td>16,065,000 / 14,453,096</td></tr>
<tr><td>1995 · 89.4</td><td><span class="id">v95d</span></td><td>350,100</td><td>1,651,000 / 1,485,000</td></tr>
<tr><td>1995 · 91.3</td><td><span class="id">v95d</span></td><td>1,725,300</td><td>4,802,000 / 4,318,197</td></tr>
<tr><td>1995 · 93.0</td><td><span class="id">v95d</span></td><td>558,900</td><td>2,054,000 / 1,848,595</td></tr>
<tr><td>All</td><td></td><td>14,442,298</td><td>42,741,000 / 38,440,229</td></tr>
</tbody>
</table>
</div>
<div>
<div class="kv sim"><h3><span class="tag sim">simulation</span> Processes</h3><dl>
<dt>Signal</dt><dd><LaTeX formula="Z\to\tau\tau" />, PYTHIA 8.315</dd>
<dt>Z decays</dt><dd><LaTeX formula="ee,\ \mu\mu,\ q\bar q" />, PYTHIA 8.315</dd>
<dt>Two-photon</dt><dd><LaTeX formula="\gamma\gamma\to\ell\ell" />, hadrons</dd>
<dt>Bhabha</dt><dd>BHWIDE 1.05</dd>
</dl></div>
<div class="co warn"><b><LaTeX formula="Z\to ee" /> excluded</b> from every stack: it overlaps the Bhabha sample.</div>
<div class="co open"><b>Detector</b> Only the 1994 description is tested so far.</div>
</div>
</div>

<div class="st-source">Source: 1992–1995 run record (production tables, 2026-10-27) and the project guide (production and tau extensions, 2026-10-26)</div>

<!--
artifacts/run-record-1992-1995-20261027/REPORT.md section 1, per-point generation table (main + extension; generated = sum of plan.json task requests incl. the 26 excluded chunks of 1000 generated events; converted = manifest converted_events). Per process per point (generated): 1992 Z_qq 1,474,000, Z_ee 356,000, Z_mumu 356,000, Z_tautau 3,355,000, yy_qq 537,000, yy_ll 60,000, Bhabha 2,236,000; 1993_89p4 193k/48k/48k/446k/211k/24k/939k; 1993_91p2 1,010k/245k/245k/2,292k/368k/42k/1,547k; 1993_93p0 280k/68k/69k/642k/228k/26k/824k; 1994 2,811k/681k/682k/6,390k/1,030k/115k/4,356k; 1995_89p4 168k/42k/42k/390k/183k/21k/805k; 1995_91p2 843k/204k/204k/1,918k/306k/35k/1,292k; 1995_93p0 273k/67k/67k/621k/215k/24k/787k. Converted per process (all points): Z_qq 6,329,149; Z_tautau 14,442,298; Bhabha 11,506,485; yy_qq 2,769,299; Z_ee 1,539,000; Z_mumu 1,541,698; yy_ll 312,300.
Z_tautau converted per point = pooled main + extension samples (docs/PROJECT_GUIDE.md "Z_tautau extensions complete; pooled tau samples", table "Pooled Z_tautau samples"); 1994 = prod-20260923-v1 + tau-extra-20260923-v1 + tau-orthogonal-001. Sum 14,442,298 = the skim's Z_tautau rows.
Campaigns: 17 (REPORT section 1), jobs 60274560 ... 60297525 (1992/1993/1995, October 2026) and 58780381 / 58789165 / 59594561 (1994). Each 1000-event chunk runs generate -> fadgen -> DELSIM -> longDST -> EDM4hep (simulation fraction 0.9). Builds: builds/tau-extra-20260923-v1, delphi-sim-pipeline 8168fd7, delphi-edm4hep 3e40698. Lost chunks accepted without regeneration (owner decision 2026-10-26); mostly DELSIM hangs (7200 s timeout), one longdst segfault; the 1992 Z_qq hang rate (0.8 %) is the outlier. Generator settings as for 1994 (long_production/configs/catalog.json; GENERATOR_CONFIG_REVIEW.md): tune Monash 2013, lepton ISR/FSR, no beam spread; two-photon Q2 < 1 GeV2, W >= 5 GeV, hadronic resolved-resolved only; Bhabha s + t + interference. detector_status of v92e/v93d/v95d: needs-year-validation (guide 2026-10-26). The 2026-10-22 version of this slide showed the 1994 campaign only.
-->
