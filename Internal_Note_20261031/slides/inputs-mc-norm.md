---
class: st pres
---

# Simulation normalisation per year, process and energy point

<div class="st-cols st-cols-2">
<div>
<ul class="bl">
<li><b>Weight</b> = <LaTeX formula="L\cdot\sigma" /> / signed <LaTeX formula="\textstyle\sum w" /> per (year, process, point)</li>
<li><b><LaTeX formula="L" /></b> run-quality luminosity; <b><LaTeX formula="\sigma" /></b> from the production itself</li>
<li><b><LaTeX formula="Z\to\tau\tau" /></b> weight 0.0118 everywhere: about 85<LaTeX formula="\times" /> the data</li>
<li><b>Data/MC</b> absolute unless marked "shape"</li>
</ul>
<div class="co decision"><b>Owner</b> Cross sections from the samples; lost chunks accepted (2026-10-26).</div>
</div>
<div>
<ul class="bl">
<li><span class="tag open">open</span> <b>Luminosity</b> user-supplied, uncertified</li>
<li><span class="tag open">open</span> <b>Detectors</b> 1992, 1993, 1995 not yet validated</li>
<li><span class="tag open">open</span> <b>Rates</b> 1994 and 1995 data 3.1 % and 2.3 % low</li>
<li><span class="tag open">open</span> <b>Lost chunks</b> 26 of 42,741; survivor bias not measured</li>
<li><span class="tag open">open</span> <b>Phase space</b> two-photon and Bhabha limits</li>
</ul>
</div>
</div>

<div class="st-source">Source: project guide (sample cross sections, pooled tau samples, run quality; 2026-10-26) and the 1992–1995 run record</div>

<!--
docs/PROJECT_GUIDE.md "Z_tautau extensions complete; pooled tau samples and sample-derived cross sections" (owner decisions 2026-10-26): analysis cross section per point x process derived from the production per-file generator sigma (long_production/scripts/derive_sample_xsec.py, configs/sample_cross_sections_20261026b.json; Z_tautau pools main + extension); "pool weights are per (year, process, point) from configured L sigma over the signed survivor sum". Effective L sigma / sum w_converted for Z_tautau 0.0118 at every point (0.0106 per generated event); "about 85x" = 1/0.0118 = 84.7, derived. Bhabha (BHWIDE) weighted: sumw/N 0.89 / 1.04 / 0.96 at 91.2 / 89.4 / 93.0 GeV, normalised with sigma x sum w / sumw_gen; Pythia sumw = N within 0.01 %. Sample-derived vs scan sigma: one |pull| > 3 (1995_89p4 Z_qq +0.68 %).
Luminosity: run-quality good-cassette values (tau_analysis 67bffe7). Residual deficits after the rule (inclusive, Z_ee excluded): 1994 0.969, 1995 0.977; about half attributable to the 1994/1995 MC predicting 1.6-1.9 % more selected events per L sigma than 1993 MC (RUN_QUALITY_YIELD_STUDY_20261026.md); open MC-side question.
Lost chunks: run record REPORT.md section 1, 26 excluded chunks in the plans of 17 campaigns (42,741 planned chunks of 1000 events, derived from 42,741,000 generated); accepted by the owner, normalisation uses per-manifest survivor counts and sumw. Two extension chunks hold 899 instead of 900 events (file metadata only).
Detectors: v94c tested; v92e/v93d/v95d needs-year-validation. Phase space: 23:mMin = 10 GeV; two-photon Q2max = 1 GeV2, Wmin = 5 GeV, no direct/single-resolved hadronic gamma-gamma; Bhabha excludes one-leg-forward and very soft configurations (GENERATOR_CONFIG_REVIEW.md). Data ECMS: uncalibrated run-header value, about 0.06 % above the table energy; MC uses the calibrated point energy (open owner decision).
-->
