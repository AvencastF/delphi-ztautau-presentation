---
class: st pres
---

# Why machine learning: three problems, one number each

<div class="tiles tiles-3">
<div class="tile ml"><b>2</b><span><b style="display:inline;font-size:13px">Ambiguity.</b> Mirror solutions per event; the default branch is right 59.3 % of the time</span></div>
<div class="tile ml"><b>0.98 → 0.74</b><span><b style="display:inline;font-size:13px">Branch ceiling.</b> Best possible branch choice 0.96–0.98 per channel; analytical 0.50–0.59; ML v5 0.74</span></div>
<div class="tile ml"><b>1.52° → 0.89°</b><span><b style="display:inline;font-size:13px">Resolution.</b> Median π-leg direction error, analytical → ML v5 (e: 2.09° → 1.17°)</span></div>
</div>

<div class="st-cols st-cols-2">
<div class="co warn"><b>Artefact</b> Default branch gives C_rn / C_nr = −1.74 / +1.75; truth ≈ 0; ML −0.01 / +0.01.</div>
<div class="co warn"><b>Purity</b> Cut-based ππ child matching fraction 0.182 → second task: decay-mode classifier.</div>
</div>

<div class="st-source">Source: version-5 neutrino evaluation summary and the first-model evaluation note</div>

<!--
artifacts/neutrino-ml-v5-20261021/eval/summary.md: inclusive branch accuracy analytical 0.593, analytical_best 0.912, nu 0.740; per channel best 0.859-0.983 (0.96-0.98 for lepton/pi channels), analytical 0.492-0.702; C_rn/C_nr inclusive analytical -1.743 +- 0.009 / +1.750 +- 0.009, truth +0.007/+0.004, nu -0.008/+0.005. Direction errors per leg see ml-ambiguity notes. artifacts/neutrino-ml-eval-20261016/README.md headline.
-->
