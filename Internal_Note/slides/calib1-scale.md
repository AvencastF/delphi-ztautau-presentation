---
class: st pres
---

<script setup>
import ZoomablePlot from 'slidev-addon-ztautau/components/ZoomablePlot.vue'
</script>

# Calibration 1: electron scale, checked with photon pairs

<div class="st-sub">Electron <LaTeX formula="E/p" /> peak, data with the stored data correction removed ("raw"), over simulated <LaTeX formula="\tau\to e" />; <LaTeX formula="k_{\gamma\gamma}" /> = data/simulation <LaTeX formula="m_{\gamma\gamma}" /> peak.</div>

<table class="num first-nw">
<thead><tr><th>Year</th><th>Data <LaTeX formula="E/p" />, raw</th><th>Sim. <LaTeX formula="E/p" /></th><th><LaTeX formula="k_e" /> (adopted)</th><th><LaTeX formula="k_{\gamma\gamma}" /></th><th><LaTeX formula="\sigma_k" /></th></tr></thead>
<tbody>
<tr><td>1992</td><td>0.9663</td><td><LaTeX formula="0.9580\pm0.0004" /></td><td><LaTeX formula="1.0087\pm0.0049" /></td><td><LaTeX formula="0.9505\pm0.0148" /></td><td>0.058</td></tr>
<tr><td>1993</td><td>0.9575</td><td><LaTeX formula="0.9291\pm0.0005" /></td><td><LaTeX formula="1.0306\pm0.0058" /></td><td><LaTeX formula="1.0227\pm0.0207" /></td><td>0.021</td></tr>
<tr><td>1994</td><td>0.9014</td><td><LaTeX formula="0.9279\pm0.0003" /></td><td><LaTeX formula="0.9714\pm0.0042" /></td><td><LaTeX formula="0.9952\pm0.0143" /></td><td>0.024</td></tr>
<tr><td>1995</td><td>0.9642</td><td><LaTeX formula="0.9261\pm0.0005" /></td><td><LaTeX formula="1.0411\pm0.0057" /></td><td><LaTeX formula="1.0385\pm0.0149" /></td><td>0.015</td></tr>
</tbody>
</table>

<div class="st-cols st-cols-2" style="margin-top:8px">
<div>
<div class="co warn"><b>1992</b> Electrons and photon pairs disagree by <LaTeX formula="3.7\sigma" />, hence <LaTeX formula="\sigma_k=0.058" />.</div>
<div class="co ok"><b>Closure</b> After <LaTeX formula="k_e" />, <LaTeX formula="m(\pi\pi^0)" /> data/simulation: single <LaTeX formula="1.005\pm0.003" />, merged <LaTeX formula="1.005\pm0.008" />.</div>
</div>
<div>
<div class="st-fig h190"><ZoomablePlot src="/figures/photon-calibration/step2b/mgg_by_year_pair.png" alt="m_gg of pair legs per year and pair class, data vs MC shape" /></div>
<div class="st-cap"><LaTeX formula="m_{\gamma\gamma}" /> per year (columns) and pair type (rows): data points, simulation shape.</div>
</div>
</div>

<div class="st-source">Source: step 2b of the <LaTeX formula="\rho" />-polarimeter study (2026-11-02), sections 1a, 1b, 2b, 2c and 3; conclusion addendum A</div>

<!--
artifacts/rho-polarimeter-step2b-calibration-20261102/REPORT.md (step 2b, 2026-11-02; calibration pass job 60714014, 1 node, 00:05:08; inputs = step-2 full pass job 60707582; tau_analysis HEAD bc0f904 + untracked joint_fit/rho_pi0_calib.py, rho_pi0_calib_legs.py, rho_pi0_calib_pass.py; constants calib_constants.json, calib_kE.json). Section 2b (|cos theta| < 0.72, 5 < p < 40 GeV; Gauss + pol1 in [0.65, 1.3]): data stored 0.9663 +- 0.0046 / 0.9256 +- 0.0052 / 0.9298 +- 0.0040 / 0.9269 +- 0.0050; data raw (/ data_scale) 0.9663 / 0.9575 / 0.9014 / 0.9642; MC tau->e 0.9580 +- 0.0004 / 0.9291 +- 0.0005 / 0.9279 +- 0.0003 / 0.9261 +- 0.0005; data/MC stored 1.0087 / 0.9962 / 1.0020 / 1.0009; k_e = data/MC raw 1.0087 +- 0.0049 / 1.0306 +- 0.0058 / 0.9714 +- 0.0042 / 1.0411 +- 0.0057. k_gg = section 1a HPC-HPC data/MC 0.9505 +- 0.0148 / 1.0227 +- 0.0207 / 0.9952 +- 0.0143 / 1.0385 +- 0.0149. sigma_k (2c) 0.0582 / 0.0207 / 0.0238 / 0.0149. Tension 1992 3.7 sigma (section 1b comparison, with the login-sample electron values 1.0064 etc.; 1993 0.3, 1994 1.2, 1995 0.0 sigma). Closure: conclusion addendum A 'After k the m(pi pi0) peak ratio is 1.005 +- 0.003 (single) and 1.005 +- 0.008 (merged)' = section 3 all-years 1.0049 +- 0.0031 / 1.0048 +- 0.0082. The year pattern of the MC m_gg (1992 high, 1993/1995 low) mirrors the HPC data_scale pattern. Figure plots/mgg_by_year_pair.png (rows hpc_hpc, hpc_conv, conv_conv, with_ca).
-->
