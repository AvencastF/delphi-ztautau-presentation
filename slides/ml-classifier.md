---
class: st pres
---

# Classifier: the evaluation on record

<div class="co warn"><b>Caveat</b> Dated 2026-10-15, earlier epoch-27 checkpoint, training events included: optimistic, not the frozen model.</div>

<div class="tiles tiles-3">
<div class="tile ml"><b>0.42 <LaTeX formula="\to" /> 0.88</b><span><LaTeX formula="\tau" />-channel accuracy, cut-based <LaTeX formula="\to" /> ML</span></div>
<div class="tile ml"><b>0.59 <LaTeX formula="\to" /> 0.84</b><span>true-<LaTeX formula="\tau" />-pair fraction of selected events</span></div>
<div class="tile ml"><b>15.0 <LaTeX formula="\to" /> 25.3</b><span><LaTeX formula="\chi^2/10" /> of data vs simulation channel yields (worse for ML)</span></div>
</div>

<table class="num">
<thead><tr><th>Channel</th><th>Efficiency cuts <LaTeX formula="\to" /> ML</th><th>Purity cuts <LaTeX formula="\to" /> ML</th><th>Data/MC ML</th></tr></thead>
<tbody>
<tr><td>ee</td><td>0.643 <LaTeX formula="\to" /> <span class="best">0.946</span></td><td>0.755 <LaTeX formula="\to" /> <span class="best">0.909</span></td><td><LaTeX formula="1.043\pm0.031" /></td></tr>
<tr><td><LaTeX formula="e\mu" /></td><td>0.707 <LaTeX formula="\to" /> <span class="best">0.963</span></td><td>0.922 <LaTeX formula="\to" /> <span class="best">0.962</span></td><td><LaTeX formula="0.977\pm0.021" /></td></tr>
<tr><td><LaTeX formula="\pi\pi" /></td><td>0.516 <LaTeX formula="\to" /> <span class="best">0.766</span></td><td>0.181 <LaTeX formula="\to" /> <span class="best">0.746</span></td><td><LaTeX formula="1.091\pm0.057" /></td></tr>
<tr><td><LaTeX formula="\pi\rho" /></td><td>0.236 <LaTeX formula="\to" /> <span class="best">0.802</span></td><td>0.338 <LaTeX formula="\to" /> <span class="best">0.747</span></td><td><LaTeX formula="1.000\pm0.024" /></td></tr>
<tr><td><LaTeX formula="\rho\rho" /></td><td>0.106 <LaTeX formula="\to" /> <span class="best">0.799</span></td><td>0.551 <LaTeX formula="\to" /> <span class="best">0.750</span></td><td><LaTeX formula="0.953\pm0.022" /></td></tr>
</tbody>
</table>

<div class="st-source">Source: classifier evaluation summary of 2026-10-15 (all ten channels in the appendix)</div>

<!--
/Users/avencastmini/Downloads/skim-cls-eval/summary.md (identical header on NERSC skim-cls-eval): checkpoint epoch=27_train=0.1167_val=0.5280.ckpt, mc_split all. Full per-channel table in appendix slide. Summary: tau channel accuracy classic 0.4164 vs ML 0.8799; signal fraction 0.5857 vs 0.8431; channel yields chi2/ndf 15.0/10 vs 25.3/10. Inclusive preselection data 23,073 / MC 23,198.9. Frozen classifier (not evaluated held-out) is epoch=29_train=0.1037_val=0.4805.ckpt (RUNBOOK section 4). AUC 0.983-0.999.
-->
