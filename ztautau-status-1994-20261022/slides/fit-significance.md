---
class: st pres
---

# Expected significance: entanglement about 7σ, Bell about 2σ

<div class="st-sub">Median expected significance if the data follow the simulation. Statistics only; no systematic uncertainties yet.</div>

<table class="lg num first-nw">
<thead><tr><th>Test (final model)</th><th>1992–1995</th><th>1994 alone</th><th>How the p-value is obtained</th></tr></thead>
<tbody>
<tr class="hl"><td>Entanglement, witness <LaTeX formula="W\gt 0" /></td><td><LaTeX formula="7.0\,\sigma" /></td><td><LaTeX formula="4.6\,\sigma" /></td><td>extrapolated: 0 of 20,000 toys reach it</td></tr>
<tr><td>Entanglement, eigenvalue (legacy, cross-check)</td><td><LaTeX formula="6.8\,\sigma" /></td><td><LaTeX formula="4.3\,\sigma" /></td><td>extrapolated, depends on the null point</td></tr>
<tr><td>Bell, <LaTeX formula="|C_{kk}-C_{rr}|\gt\sqrt2" /></td><td><LaTeX formula="2.2\,\sigma" /></td><td><LaTeX formula="1.45\,\sigma" /></td><td>counted: 265 and 1,505 of 20,000 toys</td></tr>
</tbody>
</table>

<div class="st-cols st-cols-3" style="margin-top:12px">
<div class="co ok"><b><LaTeX formula="7\,\sigma" /></b> A world without entanglement would fake it about once in <LaTeX formula="10^{12}" /> tries.</div>
<div class="co warn"><b>Extrapolated</b> We can simulate only 20,000 fake experiments; beyond about <LaTeX formula="3.7\,\sigma" /> we use the known shape of the distribution.</div>
<div class="co open"><b>Bell</b> 1.3 % of local fake worlds reach it: not significant.</div>
</div>

<div class="co open" style="margin-top:6px"><b>Not a result</b> Simulation only; systematic uncertainties will lower these numbers.</div>

<div class="st-source">Source: final-model and legacy-model hypothesis tests, combined 1992–1995 and 1994 (2026-10-31); simulation only, statistics only, Asimov</div>

<!--
Witness (model C; artifacts/joint-fit-20261031/modelC/*/summary.md): combined Z_A = W_SM/sigma_null = 6.96 (sigma_null 0.2356), calibrated Z(q_A) 7.00 +- 0.04 (sqrt q-normal tail fit, extrapolated), sqrt q_A 7.46 (not used: V(c0) != V(c_ref), scale s 1.154); alternative null points 7.09 / 6.75; C_Vfit 7.33, C_Vgen 7.07. 1994: Z_A 4.60, calibrated 4.63 +- 0.02, alternatives 4.54 / 4.36, C_Vfit 4.80. 0/20,000 null toys reach q_A in both. Toy-count p-values exist only up to q ~ 16 (Z ~ 3.7) (witness_summary.md). Model A for comparison: combined 7.00 (Z_A) / 6.88 (calibrated); 1994 4.61 / 4.55.
Eigenvalue test lambda_min(rho^T_B) >= 0 (model A, step 2): combined toy-calibrated sqrt q-normal Z(q_A) 6.83 (6.93 / 7.54 at the alternative null points; scaled mixture 5.5, Gamma 6.0; honest range 6.6-7.1); 1994 4.25 (4.31 / 4.02). Slide rounds 6.83 -> 6.8 and 4.25 -> 4.3.
Bell (model C): combined Z_A 2.219, calibrated 2.215 +- 0.009, toy count 265/20,000 (Z 2.22; 1.3 % derived); 1994 Z_A 1.438, calibrated 1.453 +- 0.005, toy count 1505/20,000 (Z 1.44). Model A: 2.17-2.21 / 1.41-1.43.
"About once in 10^12": one-sided Gaussian tail at 7.0 sigma = 1.3e-12 (derived, textbook conversion). The witness figure moved to the previous slide.
-->
