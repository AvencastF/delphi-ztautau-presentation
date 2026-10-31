---
class: st pres
---

# Expected results: all 15 coefficients, 1992–1995 combined and 1994 alone

<div class="st-sub">Final model, ML reconstruction. Central values are the simulation's own state (Asimov); errors are statistical only.</div>

<div class="st-cols st-cols-21">
<table class="lg num first-nw">
<thead><tr><th>Quantity</th><th>1992–1995</th><th>1994 alone</th></tr></thead>
<tbody>
<tr><td>Six polarisations <LaTeX formula="B" />, error</td><td>0.031–0.036</td><td>0.049–0.052</td></tr>
<tr><td><LaTeX formula="C_{nn}" /></td><td><LaTeX formula="+0.80\pm0.11" /></td><td><LaTeX formula="+0.80\pm0.17" /></td></tr>
<tr><td><LaTeX formula="C_{rr}" /></td><td><LaTeX formula="-0.81\pm0.13" /></td><td><LaTeX formula="-0.82\pm0.19" /></td></tr>
<tr><td><LaTeX formula="C_{kk}" /></td><td><LaTeX formula="+1.03\pm0.14" /></td><td><LaTeX formula="+1.01\pm0.21" /></td></tr>
<tr><td>Six off-diagonal <LaTeX formula="C" />, error</td><td>0.150–0.172</td><td>0.225–0.243</td></tr>
<tr class="hl"><td>Witness <LaTeX formula="W" /></td><td><LaTeX formula="1.64\pm0.22" /></td><td><LaTeX formula="1.63\pm0.33" /></td></tr>
<tr><td>Concurrence</td><td><LaTeX formula="0.82\pm0.11" /></td><td><LaTeX formula="0.82\pm0.17" /></td></tr>
<tr><td>Bell <LaTeX formula="|C_{kk}-C_{rr}|" /></td><td><LaTeX formula="1.84\pm0.19" /></td><td><LaTeX formula="1.83\pm0.28" /></td></tr>
</tbody>
</table>
<div>
<div class="co ok"><b>Scaling</b> Combined errors ≈ 0.65 × 1994 alone.</div>
<div class="co warn"><b><LaTeX formula="C_{kk}\gt 1" /></b> The simulation's own state is slightly unphysical; treated as an analysing-power systematic.</div>
<div class="co open"><b>Not data</b> No systematics, no data fit yet.</div>
</div>
</div>

<div class="st-source">Source: final-model expected sensitivity, combined 1992–1995 and 1994 (2026-10-31); simulation only, statistics only, Asimov</div>

<!--
artifacts/joint-fit-20261031/modelC/combined-ml/summary.md and modelC/1994_91p2-ml/summary.md, sigma_C GLS (= toy std within 3 %). Combined (reference = pooled MC truth, luminosity-weighted over sqrt s): B_An .0313, B_Ar .0357, B_Ak .0315, B_Bn .0314, B_Br .0358, B_Bk .0316; C_nn +0.7965 +- .1063; C_nr .1693; C_nk .1503; C_rn .1684; C_rr -0.8135 +- .1281; C_rk .1715; C_kn .1512; C_kr .1717; C_kk +1.0307 +- .1372. Derived (GLS / toy): W 1.6407 +- 0.2200 / 0.2243; Bell 1.8442 +- 0.1889 / 0.1902; closed-form concurrence 0.8204 +- 0.1100 / 0.1121; magic 0.1962 +- 0.1814. Null-toy sigma of W is 0.2356 (used for Z_A). 1994: B .0488-.0521; C_nn +0.7992 +- .1668; C_rr -0.8168 +- .1881; C_kk +1.0146 +- .2117; off-diagonal .2247-.2432; W 1.6306 +- 0.3314 (toy 0.3325); Bell 1.8314 +- 0.2834; concurrence 0.8153 +- 0.1657. "0.65" derived: e.g. W 0.2200/0.3314 = 0.66, C_kk 0.1372/0.2117 = 0.65.
C_kk > 1: the MC reference has C_kk = 1.015 (1994) / 1.031 (combined); rho then has a negative eigenvalue (-0.010 / -0.013); unbinned moments give the same value, so it is not a binning artefact (joint-fit step 1). Treating the reference C_kk = 1.03 as an analysing-power systematic follows the owner's brief for this deck (2026-10-31); its origin has not been studied yet. The central values are the MC reference by construction (Asimov); they are not measurements.
-->
