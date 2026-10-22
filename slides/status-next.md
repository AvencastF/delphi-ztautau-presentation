---
class: st pres
---

# Where each component stands, and the next three steps

<div class="st-cols st-cols-12">
<div>
<ol class="steps">
<li><b>Commit</b> analysis and ML work; verify hashes on NERSC</li>
<li><b>Rerun 1994</b> with one shared ML conversion, retrain classifier</li>
<li><b>Extend</b> to 1992–1995: eight points, four detector descriptions</li>
</ol>
<div class="co warn"><b>Approval</b> Every job submission on NERSC needs the owner's explicit go-ahead.</div>
</div>
<div>
<table>
<thead><tr><th>Component</th><th>Status</th><th>Action</th></tr></thead>
<tbody>
<tr><td>Production scripts</td><td><span class="status nogit">not under git</span></td><td>decide git vs receipts</td></tr>
<tr><td><a href="https://github.com/AvencastF/delphi-sim-pipeline/tree/feature/nersc-long-production">Simulation pipeline</a></td><td><span class="status clean">clean</span></td><td>none</td></tr>
<tr><td><a href="https://github.com/AvencastF/delphi-edm4hep/tree/3e40698">Converter</a></td><td><span class="status clean">clean, pinned</span></td><td>none</td></tr>
<tr><td><a href="https://github.com/AvencastF/delphi-ztautau-ana">Analysis framework</a></td><td><span class="status dirty">uncommitted fit code</span></td><td>review, commit, pull on NERSC</td></tr>
<tr><td><a href="https://github.com/UW-EPE-ML/EveNet-Align">EveNet-Align</a></td><td><span class="status dirty">v4/v5 uncommitted</span></td><td>commit, push, add chain scripts</td></tr>
<tr><td>Old ML pipeline</td><td><span class="status ref">reference only</span></td><td>deprecate or archive</td></tr>
</tbody>
</table>
</div>
</div>

<div class="st-source">Source: the 1994 runbook, synchronisation table and path contract; the 1992–1995 pipeline review</div>

<!--
docs/RUNBOOK_1994.md section 6: long_production manual copy with receipts (FULL_PRODUCTION_DEPLOYMENT_20261013.json, 35 inputs match); delphi-sim-pipeline 8168fd7 everywhere; delphi-edm4hep 3e40698; tau_analysis GitHub/NERSC c4d829e, local uncommitted run.py fit, spin_fit/* (+444/-26), 15 configs/fit_*.yaml, 17 tests/check_spin_*.py, 2 docs; EveNet-Align v4/v5 uncommitted on Ztautau-dev, synced by file with sha256; capture chain-v5.sh and *-v5.sh into Ztautau/scripts/; ztautau_ml_pipeline reference only. Section 4 path contract: converter run.input_dir = <run>/skim, run.output = predict converted = one conversion; predict output_dir = <run>/skim-cls-nu = evaluation input_dirs; conversion directory ml-runs/evenet-inputs-1994 must not reuse an existing one. Launcher requires PASS audit receipt and one-node >=128-CPU m5019 interactive allocation. artifacts/pipeline-review-1992-1995-20261022/REPORT.md.
-->
