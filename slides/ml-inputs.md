---
class: st pres
---

# Data/simulation audit of the ML inputs (2026-10-14/15)

<div class="st-cols st-cols-3">
<div class="kv"><h3>1 · Symptom</h3><dl><dt>Seen</dt><dd>simulated <LaTeX formula="\pi" /> legs classified as electrons</dd><dt>Yield <LaTeX formula="\chi^2" /></dt><dd>129 over 10 channels</dd></dl></div>
<div class="kv"><h3>2 · Cause</h3><dl><dt>Culprit</dt><dd>raw TPC dE/dx record <span class="id">MTPC_dEdxExtended</span></dd><dt>Mismatch</dt><dd><LaTeX formula="\chi^2/\mathrm{ndf}" /> 17,171; 0.87 vs 1.24</dd></dl></div>
<div class="kv"><h3>3 · Fix</h3><dl><dt>Replaced by</dt><dd>calibrated dE/dx <span class="id">BBDXGET</span>, 3 % shift left</dd><dt>Then</dt><dd>sub-GeV HCAL-only neutrals filtered</dd></dl></div>
</div>

<div class="tiles tiles-3" style="margin-top:12px">
<div class="tile ml"><b>129 <LaTeX formula="\to" /> 27</b><span>channel-yield <LaTeX formula="\chi^2" /> after masking the raw record</span></div>
<div class="tile ml"><b>0.61 vs 0.19</b><span>sub-GeV HCAL-only neutrals per event, data vs simulation, before the filter</span></div>
<div class="tile ml"><b>1.99 vs 1.98</b><span>neutral multiplicity per event after the fixes</span></div>
</div>

<div class="co ok"><b>After fixes</b> kinematic, calorimeter, muon and event-level inputs agree to <LaTeX formula="\chi^2/\mathrm{ndf}" /> <LaTeX formula="\lt 10." /></div>

<div class="st-source">Source: the classifier input audit note of 2026-10-14/15</div>

<!--
/Users/avencastmini/Downloads/skim-cls-eval/input-datamc/FINDINGS.md sections 1-8: 266 particle channels compared on leading tracks; MTPC.nempty chi2/ndf 17171, dedx65 5556 (data 0.87 vs MC 1.24), nsaturated 2480, dedx80 2215; masking whole MTPC block: chi2 129 -> 27, MC tau accuracy 0.850 -> 0.797; BBDXGET response data 1.444 vs MC 1.406 (chi2/ndf 10.9), error 0.090 vs 0.087; converter change 2026-10-15: 229 particle channels; second model residual pi<->rho migration from sub-GeV HCAL-only neutrals 0.61 vs 0.19 per event; fix neutral_filter require_emnc_below_gev 1.0; neutral multiplicity 1.99 vs 1.98.
-->
