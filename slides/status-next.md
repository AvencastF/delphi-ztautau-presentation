---
class: st pres
---

# Next steps toward a data result, and where the code stands

<div class="st-cols st-cols-12">
<div>
<ol class="steps" style="font-size:14.5px">
<li><b>Data recipe</b>: covariance at the fitted point, iterated</li>
<li><b>Coverage</b>: linearity and coverage over many injected states</li>
<li><b>Systematics</b> as nuisance parameters in the fit</li>
<li><b>Control regions</b>: validate inputs away from the signal observables</li>
<li><b>Luminosity</b>: certify and cross-check per point</li>
<li><b>Unblinding plan</b>: tests fixed in advance</li>
</ol>
<div class="co warn"><b>Approval</b> Every NERSC job needs the owner's go-ahead.</div>
</div>
<div>
<table class="first-nw">
<thead><tr><th>Component</th><th>Status</th><th>Action</th></tr></thead>
<tbody>
<tr><td>Production scripts</td><td><span class="status nogit">not under git</span></td><td>decide git vs receipts</td></tr>
<tr><td><a href="https://github.com/AvencastF/delphi-sim-pipeline/tree/feature/nersc-long-production">Simulation pipeline</a></td><td><span class="status clean">clean</span></td><td>none</td></tr>
<tr><td><a href="https://github.com/AvencastF/delphi-edm4hep/tree/3e40698">Converter</a></td><td><span class="status clean">clean, pinned</span></td><td>none</td></tr>
<tr><td><a href="https://github.com/AvencastF/delphi-ztautau-ana">Analysis framework</a></td><td><span class="status dirty">fit code uncommitted</span></td><td>review, commit, deploy</td></tr>
<tr><td>ML (EveNet-Align)</td><td><span class="status clean">committed 10-30</span></td><td>accept checkpoints</td></tr>
<tr><td>Old ML pipeline</td><td><span class="status ref">reference only</span></td><td>deprecate or archive</td></tr>
</tbody>
</table>
</div>
</div>

<div class="st-source">Source: fit-study summaries and caveats (2026-10-31), project guide (repository states to 2026-10-30)</div>

<!--
Next steps from the caveat and finding sections of artifacts/joint-fit-20261031/modelC/*/summary.md (data fit should use C_Vfit, V at the fitted point, or iterate; toy-calibrated tail), the AGENTS.md rules (calibration and validation independent; do not tune spin correlations using signal observables), and docs/PROJECT_GUIDE.md (luminosity uncertified; residual 1994/1995 deficit). These steps are proposals for the group; no order has been decided by the owner.
Repository states: tau_analysis HEAD 427b4a3 (GitHub AvencastF/delphi-ztautau-ana main); uncommitted: joint_fit/ (new: model_c.py, model_b.py, witness.py, hypothesis.py, step2*.py, run_joint_fit.py, README.md, ...), legacy_fit/parquet_inputs.py and run_legacy_fit.py (select / pooling / heldout_representative edits of 2026-10-30), docs/README.md, docs/RUN_RECORD_1992_1995_20261027.md (git status 2026-10-31). EveNet-Align b5cc2c2 on Ztautau-dev committed and pushed 2026-10-30, NERSC checkout fast-forwarded, clean on both sides (PROJECT_GUIDE 2026-10-30); checkpoint acceptance by the owner pending. delphi-sim-pipeline 8168fd7, delphi-edm4hep 3e40698 (RUNBOOK_1994 section 6). long_production manual copy with receipts. ztautau_ml_pipeline reference only.
-->
