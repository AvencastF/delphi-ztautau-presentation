---
class: st pres c2
---

# Calibration 2 · Step 7: the result <LaTeX formula="k(E,\text{year})" />, next to calibration 1

<div class="st-sub">Multiply the simulated photon energy by <LaTeX formula="k" />. Calibration 2: both channels, isolation <LaTeX formula="\ge5^\circ" />, valid 5–46 GeV. Calibration 1: in-sample, <LaTeX formula="\rho" /> study.</div>

<table class="sm num first-nw">
<thead><tr><th>Year</th><th>Calibration 2: <LaTeX formula="k(E)" /> applied</th><th>Lowest bin</th><th>Highest bin</th><th>Cal. 1: electrons <LaTeX formula="k_e" /></th><th><LaTeX formula="k_e(p)" />: 5–8 / 32–40 GeV</th><th>Photon pairs <LaTeX formula="k_{\gamma\gamma}" /></th></tr></thead>
<tbody>
<tr><td>1992</td><td><LaTeX formula="0.9812\,(\pm0.0107)+0.0636\,(\pm0.0179)\ln\frac{E}{10\,\mathrm{GeV}}" /></td><td><LaTeX formula="0.965\pm0.019" /></td><td><LaTeX formula="1.043\pm0.015" /></td><td><LaTeX formula="1.0087\pm0.0049" /></td><td>0.9655 / 1.0580</td><td><LaTeX formula="0.9505\pm0.0148" /></td></tr>
<tr><td>1993</td><td><LaTeX formula="1.0429\pm0.0100" /></td><td><LaTeX formula="1.039\pm0.046" /></td><td><LaTeX formula="1.051\pm0.023" /></td><td><LaTeX formula="1.0306\pm0.0058" /></td><td>0.9608 / 1.0383</td><td><LaTeX formula="1.0227\pm0.0207" /></td></tr>
<tr><td>1994</td><td><LaTeX formula="0.9577\pm0.0075" /></td><td><LaTeX formula="0.970\pm0.017" /></td><td><LaTeX formula="0.937\pm0.014" /></td><td><LaTeX formula="0.9714\pm0.0042" /></td><td>0.9745 / 0.9564</td><td><LaTeX formula="0.9952\pm0.0143" /></td></tr>
<tr><td>1995</td><td><LaTeX formula="1.0232\pm0.0104" /></td><td><LaTeX formula="1.068\pm0.055" /></td><td><LaTeX formula="1.025\pm0.012" /></td><td><LaTeX formula="1.0411\pm0.0057" /></td><td>1.0157 / 1.0328</td><td><LaTeX formula="1.0385\pm0.0149" /></td></tr>
</tbody>
</table>
<div class="st-cap">Lowest bin 5–8 GeV; highest 17–46 GeV (1992, 1995) or 25–46 GeV. <LaTeX formula="E" /> = simulated photon energy, clipped to 5–46 GeV.</div>

<div class="st-cols st-cols-3" style="margin-top:8px">
<div class="co ok"><b>1993–1995</b> Constant <LaTeX formula="k" /> within 0.018 of <LaTeX formula="k_e" /> (<LaTeX formula="\le1.6\sigma" />).</div>
<div class="co warn"><b>1992</b> Rises with energy, like the electron <LaTeX formula="k_e(p)" />; flat <LaTeX formula="k_e" /> averages over it.</div>
<div class="co open"><b>Status</b> Not applied; no calibration file written.</div>
</div>

<div class="takeaway"><b>Takeaway</b> Calibration 2 confirms calibration 1 in 1993–1995 and replaces the flat 1992 value by an energy-dependent one.</div>

<div class="st-source">Source: closure study (section 2.1), energy-binned study (sections 4, 4.1, 7) of the version-2 <LaTeX formula="\ell^+\ell^-\gamma" /> run; step 2b of the <LaTeX formula="\rho" />-polarimeter study (sections 1a, 2b)</div>

<!--
Calibration 2: artifacts/llgamma-v2-20261103/closure/REPORT.md section 2.1(b) smooth calibrations (comb, k_fit): 1992 a = 0.9812 +- 0.0107, b = 0.0636 +- 0.0179, cov(a,b) = -9.2e-5, E clipped to [5, 46] GeV (the line gives 0.937 at 5 GeV and 1.078 at 46 GeV, derived); 1993 1.0429 +- 0.0100; 1994 0.9577 +- 0.0075; 1995 1.0232 +- 0.0104. Binned (epred/REPORT.md section 4, iso5 comb k fit): lowest 5-8 GeV 0.965 +- 0.019 / 1.039 +- 0.046 / 0.970 +- 0.017 / 1.068 +- 0.055; highest 1992 17-46 1.043 +- 0.015, 1993 25-46 1.051 +- 0.023, 1994 25-46 0.937 +- 0.014, 1995 17-46 1.025 +- 0.012. Calibration 1: artifacts/rho-polarimeter-step2b-calibration-20261102/REPORT.md (job 60714014) section 2b k_e 1.0087 +- 0.0049 / 1.0306 +- 0.0058 / 0.9714 +- 0.0042 / 1.0411 +- 0.0057; k_e(p) from calib_kE.json mc_pi0_scale (grid 6.5 = 5-8 GeV, 36.0 = 32-40 GeV): 0.9655 / 1.058, 0.9608 / 1.0383, 0.9745 / 0.9564, 1.0157 / 1.0328 (section 2b errors 0.0393/0.0097, 0.1823/0.0111, 0.0232/0.0088, 0.0354/0.0092); section 1a k_gg 0.9505 +- 0.0148 / 1.0227 +- 0.0207 / 0.9952 +- 0.0143 / 1.0385 +- 0.0149. Derived differences calibration 2 constant - k_e: 1993 +0.0123 (1.06 sigma), 1994 -0.0137 (1.59 sigma), 1995 -0.0179 (1.51 sigma), errors in quadrature. Versus k_gg: 1993 +0.020 (0.9 sigma), 1994 -0.038 (2.3 sigma), 1995 -0.015 (0.8 sigma); calibration 1 used sigma_k = max(|k_e - k_gg|, sigma_gg) (1994: 0.0238). Different variables: E_pred/photon E (calibration 2) vs electron momentum (k_e(p)). Calibration 1 applied a flat k_e per year to simulated single and merged pi0 energies. Status: no calibration file written, rho study not rerun (owner: "not yet", 2026-11-03).
-->
