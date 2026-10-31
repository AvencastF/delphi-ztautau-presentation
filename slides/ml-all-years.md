---
class: st pres
---

# 1992–1995 models: one classifier and one neutrino model for all years

<div class="st-sub">Trained on a fixed half of the simulation; the other half never enters training and feeds every evaluation and fit.</div>

<div class="st-cols st-cols-21">
<div>
<table class="num first-nw">
<thead><tr><th>Held-out half</th><th>All years</th><th>1992</th><th>1993</th><th>1994</th><th>1995</th></tr></thead>
<tbody>
<tr><td>Decay-pair accuracy</td><td>0.884</td><td>0.875</td><td>0.886</td><td>0.887</td><td>0.886</td></tr>
<tr><td>Correct neutrino branch</td><td>0.724</td><td>0.695</td><td>0.687</td><td>0.746</td><td>0.747</td></tr>
<tr><td><LaTeX formula="\pi" /> leg, median error [<LaTeX formula="^\circ" />]</td><td>0.88</td><td>0.97</td><td>1.01</td><td>0.81</td><td>0.83</td></tr>
<tr><td><LaTeX formula="\rho" /> leg, median error [<LaTeX formula="^\circ" />]</td><td>0.98</td><td>1.04</td><td>1.04</td><td>0.93</td><td>0.95</td></tr>
</tbody>
</table>
<div class="st-cap">For comparison, the 1994-only neutrino model v5: branch 0.740, <LaTeX formula="\pi" /> leg 0.89°, <LaTeX formula="\rho" /> leg 1.03°.</div>
</div>
<div>
<div class="co ok"><b>1994</b> Slightly better than v5 on every leg.</div>
<div class="co warn"><b>1992–1993</b> Weaker: no vertex-detector z measurement before 1994.</div>
<div class="co open"><b>Data/MC</b> 1994 <LaTeX formula="\rho" /> channels 0.94; 1992 <LaTeX formula="\pi\pi" /> 1.24; 1995 ee 0.85.</div>
<div class="co decision"><b>Inputs</b> <LaTeX formula="\sqrt{s}" /> and year enter as conditions.</div>
</div>
</div>

<div class="st-source">Source: all-years machine-learning evaluation of 2026-10-27 (held-out half, per year); simulation closure only</div>

<!--
artifacts/ml-all-years-v1-20261027/README.md (evaluations cls-eval-hold.md, nu-eval-hold.md, *-year-YYYY.md; mc_split: unseen = train and val rows dropped). Classifier epoch 14 (val loss 0.4405), neutrino epoch 97 (single 4 h allocation of a 200-epoch schedule, owner decision 2026-10-27; val loss 0.225, EMA). Conversion ml-runs/evenet-inputs-all-years-v1 (84 condition channels: v5 layout + ecms + year one-hot); prediction skim-cls-nu (14.4 M Z_tautau rows). pipi eff/purity all years 0.746/0.664. Data/MC yields chi2/10 ML vs classic: all 60.4 vs 70.0; 1994 41.8 vs 25.2. Data/MC per channel (ML selection): 1994 erho/murho/rhorho 0.94 (classic 0.97-1.01); 1992 pipi 1.24 +- 0.08, mupi 1.11 +- 0.04; 1995 ee 0.85 +- 0.04 (classic 0.78); mumu 1.04-1.10. Not done: owner checkpoint acceptance, per-point views. EveNet-Align committed b5cc2c2 on Ztautau-dev (2026-10-30). The 1994 slides before this one describe the 1994-only models (classifier v1, neutrino v5).
-->
