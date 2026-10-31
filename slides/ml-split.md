---
class: st pres
---

# Split policy: a fixed half that never enters training

<div class="tiles tiles-3">
<div class="tile ml"><b>2,380,841</b><span>training-half events; a validation part picks the checkpoint</span></div>
<div class="tile ml"><b>2,379,380</b><span>hold-half events: evaluations and fits</span></div>
<div class="tile ml"><b>0</b><span>hold events ever seen in training</span></div>
</div>

<ul class="bl">
<li><b>Split</b> by a hash of the event identity, fixed once</li>
<li><b>Evaluation</b> drops training and validation rows</li>
<li><b>Fits</b> keep the hold half, weights <LaTeX formula="\times 2.00" /></li>
<li><b>Data</b> is never split, only predicted</li>
</ul>

<div class="st-cols st-cols-2">
<div class="co decision"><b>Owner 2026-10-27</b> No cross-training: simulation is not limiting.</div>
<div class="co ok"><b>Cost</b> About 2 % larger fit errors.</div>
</div>

<div class="st-source">Source: project guide (all-years ML decisions, 2026-10-27) and the 1992–1995 run record (conversion)</div>

<!--
docs/PROJECT_GUIDE.md "2026-10-27 — all-years ML conversion prepared" (owner decisions): one model per task trained on a fixed half of the MC; the other half (hold) never enters any training; evaluations, closure, response and calibration use the hold half (predict <prefix>_split == hold; evaluate*.py mc_split: unseen also drops the validation rows); no odd/even cross-training (MC statistics not limiting; half of 1994 behind the expected data inflates the fit sigma by ~2 %). Conversion job 60348507 (REPORT.md section 4): 14,531,950 rows read -> 4,822,318 written (train 2,380,841, hold 2,379,380, predict 62,097). Hold-half Z_tautau events evaluated: 2,359,482 (nu-eval-hold.md). Fit inputs: hold cohort rule heldout_representative (tau_analysis/legacy_fit/parquet_inputs.py), Z_tautau 1994 scale 2.00070 (inputs-1992-1995 notes). Split seed and hash: converter-all-years.yaml split block (as for 1994: sha256 of seed and identity). The 2026-10-22 version described the 1994 split (200,755 held-out events, no test part).
-->
