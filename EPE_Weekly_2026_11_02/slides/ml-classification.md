---
class: st pres tk tk-academic
---

# CLS: cut-based versus EveNet

<div class="st-sub">1992–1995 · same held-out simulation · purity normalisation within each selected class</div>
<div class="cls-matrix"><ZoomablePlot src="/figures/ml/02_confusion_purity.svg" alt="Cut-based and ML confusion matrices, normalised by selected class, on the same held-out simulation" /></div>
<div class="cls-findings"><div><label>Correct decay-pair assignment</label><strong>40.8% <LaTeX formula="\longrightarrow" /> 88.4%</strong><span>+47.6 percentage points</span></div><div><label><LaTeX formula="\pi\pi" /> purity · full MC stack</label><strong>16.9% <LaTeX formula="\longrightarrow" /> 66.4%</strong><span>3.93-fold increase</span></div><div><label>ML accuracy across years</label><strong>87.5–88.7%</strong><span>One classifier for all four years</span></div></div>

<!--
Original all-years confusion purity plot from Internal_Note/public/figures/ml-all-years/cls/02_confusion_purity.svg, no numerical modification. Methods and channels: artifacts/ml-all-years-v1-20261027/cls-eval-hold.md and metrics JSON. Accuracy .4079/.8841; difference47.622 percentage points, displayed47.6. Pi-pi purity .169/.664 from the same MC-stack table, ratio3.929, displayed3.93. This supersedes previous claim of fourfold efficiency (incorrect). Per-year accuracy .8752/.8861/.8869/.8856 from ml-cls-allyears.md. Accuracy and column-normalised purity are different metrics; accuracy uses simulated tau channel assignment, purity includes stack backgrounds. No observed spin-sensitivity claim.
-->
