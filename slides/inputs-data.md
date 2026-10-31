---
class: st pres
---

# Data: every run looked up in the DELPHI luminosity tables

<div class="st-sub">Leptonic data streams 1992–1995, converted once. A table decides which events count, and at which point.</div>

<div class="tiles tiles-3">
<div class="tile data"><b>2,395,361</b><span>converted events in 334 files, 1992–1995</span></div>
<div class="tile data"><b>69,472</b><span>events without a luminosity record: excluded, counted</span></div>
<div class="tile data"><b>100 %</b><span>point assignment agrees with LEP energy tables</span></div>
</div>

<div class="st-cols st-cols-2">
<div class="kv"><h3><span class="tag data">data</span> The run-to-point lookup</h3><dl>
<dt>1 · Lookup</dt><dd>run and cassette in the DELPHI tables <span class="id">SATLUM92/93, STILUM94/95</span>, status 0 only</dd>
<dt>2 · Point</dt><dd>run energy <LaTeX formula="\lt 90.3" /> GeV <LaTeX formula="\to" /> 89.4; <LaTeX formula="\gt 92.3" /> GeV <LaTeX formula="\to" /> 93.0; otherwise 91.2</dd>
<dt>3 · Missing</dt><dd>run not in the table: excluded</dd>
<dt>Converter</dt><dd><a href="https://github.com/AvencastF/delphi-edm4hep/tree/3e40698">delphi-edm4hep</a> <span class="id">3e40698</span></dd>
</dl></div>
<div>
<div class="co ok"><b>Consistent</b> Luminosity and events from the same rows.</div>
<div class="co warn"><b>1994 before</b> All 828,850 events used; 3.7 % had no record.</div>
<div class="co open"><b>Luminosity</b> User-supplied tables, not certified.</div>
</div>
</div>

<div class="st-source">Source: project guide, run selection and energy-point assignment (2026-10-26); luminosity certification note (2026-10-26)</div>

<!--
docs/PROJECT_GUIDE.md "2026-10-26 — data run selection and energy-point assignment: decision" (decided by the analysis agent at the owner's request; applies to all years): luminosity, good-run list and point assignment from SATLUM92, SATLUM93, STILUM94, STILUM95, status 0 only; per-run lookup (scan points interleave), never a run range; point split Ecm < 90.3 GeV -> 89p4, > 92.3 GeV -> 93p0, else 91p2; rows whose run is absent get an explicit unassigned state and are excluded with the count reported; point energies stay the configured luminosity-weighted means; LEP Energy Working Group fill tables are a cross-check only.
"2026-10-26 — multi-year tau_analysis inputs deployed" (tau_analysis b7836bf): run tables configs/run_points/<year>.json from SATLUM92.24JAN94, SATLUM93.25JAN96, STILUM94.03FEB98, STILUM95.03FEB98 reproduce the configured luminosities and point energies within 0.5 MeV; LEP energy tables agree on the point for 100 % of records (max |delta| 37 MeV, 1993); lookup key (run, fileSeq) = luminosity-table cassette ("File") number.
"first 1992-1995 production (all-years-20261026)": good / bad status / not in table: 1992 521,167 / 0 / 6; 1993 570,999 / 1,304 / 114; 1994 797,995 / 0 / 30,855; 1995 435,728 / 0 / 37,193 (excluded total 69,472, derived); 1994 exclusions = 24,741 events in 154 runs absent from STILUM94 + 6,114 in absent cassettes; no excluded event inside a listed cassette's event range. The frozen 2026-10-07 1994 production used all 828,850 data events; 3.7 % had no luminosity record. Luminosity consistency: all contributing cassettes in the table.
tau_analysis/docs/LUMINOSITY_CERTIFICATION_20261026.md: configured luminosities are the final table versions; hadrons per nb-1 agree 1993 vs 1994 to <= 0.3 %; excluded runs have no luminosity record anywhere (about 1.55 pb-1 in 1994, 2.2 pb-1 in 1995 by hadron-count estimate); 1993 SATLUM93 vs LUMI93_SJAN96 agree to 0.015 %.
Conversion: 64/61/132/77 files, 2,395,361 events, campaign long_production/data_conversion/1992-1995-20260923-identityfix (jobs 58783709/58783812/58783853); IFLRNQ=0 at conversion (run selection is applied in tau_analysis). Data per-event sDST_EVT_ECMS is the uncalibrated run-header value (about 0.06 % above the table energy at 91.2 GeV); the ML inputs use the point energy.
-->
