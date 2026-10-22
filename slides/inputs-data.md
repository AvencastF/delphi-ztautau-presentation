---
class: st pres
---

# Data: the official 1994 leptonic DELPHI stream, converted once

<div class="tiles tiles-3">
<div class="tile data"><b>828,850</b><span>events in 132 EDM4hep files</span></div>
<div class="tile data"><b>0</b><span>duplicate event identities</span></div>
<div class="tile data"><b>678</b><span>published files checksum-verified</span></div>
</div>

<div class="st-cols st-cols-2">
<div class="kv"><h3><span class="tag data">data</span> Conversion</h3><dl>
<dt>Stream</dt><dd>official 1994 leptonic longDST stream <span class="id">lolept94_c2</span></dd>
<dt>Converter</dt><dd><a href="https://github.com/AvencastF/delphi-edm4hep/tree/3e40698">delphi-edm4hep</a> <span class="id">3e40698</span>, script <a href="https://github.com/AvencastF/delphi-edm4hep/blob/3e40698/scripts/production/convert.sh">convert.sh --data</a></dd>
<dt>Identity</dt><dd>run number, file sequence, event number</dd>
<dt>Settings</dt><dd>no good-run selection <span class="id">IFLRNQ=0</span>, first pass only</dd>
</dl></div>
<div>
<div class="co open"><b>Open</b> No good-run, trigger or luminosity matching applied anywhere yet.</div>
<div class="co warn"><b>Beam spot</b> 13,399 flagged events fail the impact-parameter cuts.</div>
<div class="co warn"><b>Caveat</b> Conversion success is not detector or physics validation.</div>
</div>
</div>

<div class="st-source">Source: the 1994 runbook, data-conversion stage, and the September-23 conversion campaign's results note</div>

<!--
docs/RUNBOOK_1994.md section 2; artifacts/pipeline-review-1992-1995-20261022/REPORT.md Stage 2; tau_analysis/analysis/physics.py (nonzero sDST_EVT_BeamSpotErrorCode makes d0/z0 NaN). Input raw_data/lolept94_c2; campaign long_production/data_conversion/1992-1995-20260923-identityfix/ (jobs 58783709/58783812/58783853); output analysis_ready/data/1994/*.edm4hep.root + files.txt, manifest.json, per-file .conditions.json; IFLRNQ=0, IFLCUT=3, IFLSTR=11. Good-run hook: delphi-edm4hep/scripts/runquality/runquality.py (unused). All four years converted: 64/61/132/77 files, 2,395,361 events.
-->
