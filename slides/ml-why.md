---
class: st pres
---

# Why machine learning: three problems, one number each

<div class="tiles tiles-3">
<div class="tile ml"><b>2</b><span><b style="display:inline;font-size:13px">Ambiguity.</b> Mirror solutions per event; the default branch is right 59.1 % of the time</span></div>
<div class="tile ml"><b>0.59 <LaTeX formula="\to" /> 0.72</b><span><b style="display:inline;font-size:13px">Branch.</b> Correct branch, analytical default <LaTeX formula="\to" /> ML; best possible 0.91</span></div>
<div class="tile ml"><b>1.55<LaTeX formula="^\circ" /> <LaTeX formula="\to" /> 0.88<LaTeX formula="^\circ" /></b><span><b style="display:inline;font-size:13px">Resolution.</b> Median <LaTeX formula="\pi" />-leg direction error, analytical <LaTeX formula="\to" /> ML</span></div>
</div>

<div class="st-cols st-cols-2">
<div class="co warn"><b>Artefact</b> Default branch gives <LaTeX formula="C_{rn}" /> / <LaTeX formula="C_{nr}" /> = <LaTeX formula="-1.76" /> / +1.75; truth <LaTeX formula="\approx" /> 0; ML <LaTeX formula="0.000" /> / <LaTeX formula="-0.002" />.</div>
<div class="co warn"><b>Purity</b> Cut-based <LaTeX formula="\pi\pi" /> child matching fraction 0.173 <LaTeX formula="\to" /> second task: decay-mode classifier.</div>
</div>

<div class="st-source">Source: all-years neutrino evaluation (hold half, 1992–1995, 2026-10-27) and the 1992–1995 composition table</div>

<!--
artifacts/ml-all-years-v1-20261027/nu-eval-hold.md (2,359,482 Z->tautau events of the hold half, all years): inclusive branch accuracy analytical 0.591, analytical_best 0.910, nu 0.724; per channel best 0.854-0.981 (0.964-0.981 for lepton/pi channels), analytical 0.498-0.692; pi-leg median direction error analytical 1.55, nu 0.88 deg; C_rn/C_nr inclusive analytical -1.756 +- 0.003 / +1.752 +- 0.003, truth -0.000/+0.000, nu +0.000 +- 0.002 / -0.002 +- 0.002. Matching fraction of the cut-based pipi child, all years: 0.173 (exclusive_confusion.csv of all-years-rq-20261026). The 2026-10-22 version used the 1994 v5 numbers (0.593 / 0.740; 1.52 -> 0.89 deg; pipi matching 0.182).
-->
