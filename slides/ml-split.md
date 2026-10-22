---
class: st pres
---

# Split policy: what "held-out" means here

<div class="tiles tiles-3">
<div class="tile ml"><b>200,755</b><span>held-out simulated <LaTeX formula="Z\to\tau\tau" /> events, identical for versions 2–5</span></div>
<div class="tile ml"><b>20 %</b><span>last fifth of the training files = validation and checkpoint choice</span></div>
<div class="tile ml"><b>0</b><span>independent test events reserved</span></div>
</div>

<ul class="bl">
<li><b>Hash split</b> by event identity, seed 42, 100 files</li>
<li><b>Evaluation</b> drops training rows, rescales to full yield</li>
<li><b>Data</b> is never split, only predicted</li>
</ul>

<div class="st-cols st-cols-2">
<div class="co warn"><b>Guard</b> Only the fit's held-out option excludes training rows.</div>
<div class="co decision"><b>Decision 2026-10-22</b> Retrain the classifier on the shared conversion; not run yet.</div>
</div>

<div class="st-source">Source: converter configuration (split block), training configuration and the 1994 runbook</div>

<!--
converter-1994.yaml split: seed 42, parts {train: 10}, shards {train: 100}, statistics train; u = sha256({seed, identity})[:8]/2^64. train-neutrino.yaml:131 val_split [0.8, 1.0]. Evaluation mc_split heldout: 200,755 events (200,296 with charged daughters both legs, 2,944 true pipi). Conversions: classifier ml-runs/evenet-inputs-1994; neutrino v5 ml-runs/evenet-inputs-1994-v5 (job 60075055: 3,085,534 rows, 1,018,840 train / 25,223 predict, 74 conditions). predict.py converts each row group once per model. Owner 2026-10-22: predict-1994.yaml (one converted, classifier placeholder), evaluate-1994.yaml acceptance test; not run. RUNBOOK section 4.
-->
