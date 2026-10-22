---
class: st pres
---

# Classifier: the evaluation on record

<div class="co warn"><b>Caveat</b> Dated 2026-10-15, earlier epoch-27 checkpoint, training events included: optimistic, not the frozen model.</div>

<div class="tiles tiles-3">
<div class="tile ml"><b>0.42 → 0.88</b><span>τ-channel accuracy, cut-based → ML</span></div>
<div class="tile ml"><b>0.59 → 0.84</b><span>true-τ-pair fraction of selected events</span></div>
<div class="tile ml"><b>15.0 → 25.3</b><span>χ²/10 of data vs simulation channel yields (worse for ML)</span></div>
</div>

<table class="num">
<thead><tr><th>Channel</th><th>Efficiency cuts → ML</th><th>Purity cuts → ML</th><th>Data/MC ML</th></tr></thead>
<tbody>
<tr><td>ee</td><td>0.643 → <span class="best">0.946</span></td><td>0.755 → <span class="best">0.909</span></td><td>1.043 ± 0.031</td></tr>
<tr><td>eμ</td><td>0.707 → <span class="best">0.963</span></td><td>0.922 → <span class="best">0.962</span></td><td>0.977 ± 0.021</td></tr>
<tr><td>ππ</td><td>0.516 → <span class="best">0.766</span></td><td>0.181 → <span class="best">0.746</span></td><td>1.091 ± 0.057</td></tr>
<tr><td>πρ</td><td>0.236 → <span class="best">0.802</span></td><td>0.338 → <span class="best">0.747</span></td><td>1.000 ± 0.024</td></tr>
<tr><td>ρρ</td><td>0.106 → <span class="best">0.799</span></td><td>0.551 → <span class="best">0.750</span></td><td>0.953 ± 0.022</td></tr>
</tbody>
</table>

<div class="st-source">Source: classifier evaluation summary of 2026-10-15 (all ten channels in the appendix)</div>

<!--
/Users/avencastmini/Downloads/skim-cls-eval/summary.md (identical header on NERSC skim-cls-eval): checkpoint epoch=27_train=0.1167_val=0.5280.ckpt, mc_split all. Full per-channel table in appendix slide. Summary: tau channel accuracy classic 0.4164 vs ML 0.8799; signal fraction 0.5857 vs 0.8431; channel yields chi2/ndf 15.0/10 vs 25.3/10. Inclusive preselection data 23,073 / MC 23,198.9. Frozen classifier (not evaluated held-out) is epoch=29_train=0.1037_val=0.4805.ckpt (RUNBOOK section 4). AUC 0.983-0.999.
-->
