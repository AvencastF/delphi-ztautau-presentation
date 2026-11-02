---
class: st pres
---

# The 1992–1995 models: classifier and neutrino model

<div class="st-cols st-cols-2">
<div class="kv ml"><h3><span class="tag ml">ML</span> Decay-mode classifier · all years v1</h3><dl>
<dt>Target</dt><dd>12 classes: 10 <LaTeX formula="\tau" /> channels + other <LaTeX formula="\tau" /> + lepton pairs</dd>
<dt>Training</dt><dd>training half of all eight points, 30 epochs, 1 h 14 min</dd>
<dt>Checkpoint</dt><dd>epoch 14, lowest validation loss, raw weights</dd>
<dt>Applied to</dt><dd>every selected event, data and simulation</dd>
</dl></div>
<div class="kv ml"><h3><span class="tag ml">ML</span> Neutrino-direction model · all years v1</h3><dl>
<dt>Target</dt><dd><LaTeX formula="(\delta\theta,\delta\phi)" /> of each <LaTeX formula="\tau" /> to its leading track</dd>
<dt>Conditions</dt><dd>84 event quantities via FiLM, incl. <LaTeX formula="\sqrt{s}" /> and the year</dd>
<dt>Training</dt><dd>epoch 97 of a 200-epoch schedule, stopped at 4 h</dd>
<dt>Checkpoint</dt><dd>EMA weights; 1 sample <LaTeX formula="\times" /> 50 steps</dd>
</dl></div>
</div>

<div class="tiles tiles-3" style="margin-top:12px">
<div class="tile ml"><b>84</b><span>condition channels: the 1994 layout + <LaTeX formula="\sqrt{s}" /> + year one-hot</span></div>
<div class="tile ml"><b>14.4 M</b><span>simulated <LaTeX formula="Z\to\tau\tau" /> rows predicted, 2 h 40 min on 4 GPUs</span></div>
<div class="tile ml"><b>1</b><span>model per task for all years and energy points</span></div>
</div>

<div class="co decision"><b>Owner</b> One model per task; neutrino training truncated at one 4 h allocation (2026-10-27).</div>

<div class="st-source">Source: all-years machine-learning record (2026-10-27) and the project guide (all-years ML decisions)</div>

<!--
artifacts/ml-all-years-v1-20261027/README.md: conversion ml-runs/evenet-inputs-all-years-v1 (train/hold halves, ecms and year one-hot conditions, 84 condition channels, point energies); classifier epoch 14 (lowest validation loss 0.4405 of 30 epochs, raw weights), job 60349069 (1:13:35, 4 GPUs); neutrino epoch 97 (single 4 h allocation of a 200-epoch schedule, owner decision 2026-10-27; validation loss 0.225, EMA weights), job 60349070 (TIMEOUT at 4:00:11; resume attempts refused); prediction skim-cls-nu (14.4 M Z_tautau rows; job 60360080, 2:40:43). Run record: artifacts/run-record-1992-1995-20261027/REPORT.md section 4 (conversion job 60348507: 14,531,950 rows read, 4,822,318 written: train 2,380,841, hold 2,379,380, predict 62,097).
docs/PROJECT_GUIDE.md 2026-10-27: sqrt(s) enters as the nominal energy of the event's run period (point energy) for data and MC; data run-header ECMS no longer used by the ML inputs; new conditions ecms + year one-hot. Pretrained EveNet checkpoint and the 7-slot particle token unchanged (owner measured ~10 % better classification with pretraining). Neutrino training was planned at 60 epochs in the conversion entry; the run used the 200-epoch schedule truncated at epoch 97. Checkpoint acceptance by the owner: pending. The 1994-only cards (classifier v1 epoch 29, neutrino v5) are in the appendix.
-->
