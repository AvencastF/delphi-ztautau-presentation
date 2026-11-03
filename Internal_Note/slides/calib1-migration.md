---
class: st pres
---

# Calibration 1: category migration weights and the <LaTeX formula="m(\pi\pi^0)" /> closure

<div class="st-sub">Data have fewer resolved pairs and merged-shower <LaTeX formula="\pi^0" /> tags than the simulation; weights <LaTeX formula="r_c" /> restore the per-year category fractions.</div>

<table class="num first-nw">
<thead><tr><th>Year</th><th><LaTeX formula="r_\mathrm{pair}" /></th><th><LaTeX formula="r_\mathrm{merged}" /></th><th><LaTeX formula="r_\mathrm{single}" /></th><th><LaTeX formula="r_\mathrm{fallback}" /></th></tr></thead>
<tbody>
<tr><td>1992</td><td><LaTeX formula="0.9323\pm0.0288" /></td><td><LaTeX formula="0.8157\pm0.0432" /></td><td><LaTeX formula="1.1037\pm0.0125" /></td><td><LaTeX formula="0.8161\pm0.0306" /></td></tr>
<tr><td>1993</td><td><LaTeX formula="0.9182\pm0.0281" /></td><td><LaTeX formula="0.7700\pm0.0385" /></td><td><LaTeX formula="1.0535\pm0.0121" /></td><td><LaTeX formula="1.0753\pm0.0423" /></td></tr>
<tr><td>1994</td><td><LaTeX formula="0.8824\pm0.0202" /></td><td><LaTeX formula="0.6596\pm0.0260" /></td><td><LaTeX formula="1.0778\pm0.0089" /></td><td><LaTeX formula="1.1311\pm0.0323" /></td></tr>
<tr><td>1995</td><td><LaTeX formula="0.8219\pm0.0289" /></td><td><LaTeX formula="0.7529\pm0.0408" /></td><td><LaTeX formula="1.0793\pm0.0130" /></td><td><LaTeX formula="1.1349\pm0.0467" /></td></tr>
</tbody>
</table>


<div class="st-cols st-cols-21" style="margin-top:8px">
<table class="sm num first-nw">
<thead><tr><th>Year</th><th><LaTeX formula="m(\pi\pi^0)" /> data/sim., single, after <LaTeX formula="k_e" /></th><th>Merged, after <LaTeX formula="k_e" /></th><th>Merged tags per leg: data | sim.</th></tr></thead>
<tbody>
<tr><td>1992</td><td><LaTeX formula="1.0059\pm0.0069" /></td><td><LaTeX formula="1.0347\pm0.0122" /></td><td>0.0702 | 0.0856</td></tr>
<tr><td>1993</td><td><LaTeX formula="1.0078\pm0.0067" /></td><td><LaTeX formula="0.9874\pm0.0179" /></td><td>0.0781 | 0.1016</td></tr>
<tr><td>1994</td><td><LaTeX formula="1.0047\pm0.0049" /></td><td><LaTeX formula="0.9753\pm0.0172" /></td><td>0.0692 | 0.1046</td></tr>
<tr><td>1995</td><td><LaTeX formula="1.0011\pm0.0076" /></td><td><LaTeX formula="1.0060\pm0.0177" /></td><td>0.0772 | 0.1030</td></tr>
<tr><td>All</td><td><LaTeX formula="1.0049\pm0.0031" /></td><td><LaTeX formula="1.0048\pm0.0082" /></td><td></td></tr>
</tbody>
</table>

<div>
<div class="co open"><b>Not independent</b> <LaTeX formula="r_c" /> comes from the same <LaTeX formula="\rho" /> legs it is checked on.</div>
<div class="co warn"><b>Left over</b> Merged 1992 <LaTeX formula="2.8\sigma" />, 1994 <LaTeX formula="1.4\sigma" />; no further factor applied.</div>
</div>
</div>

<div class="st-source">Source: step 2b of the <LaTeX formula="\rho" />-polarimeter study (2026-11-02), sections 3 and 4</div>

<!--
artifacts/rho-polarimeter-step2b-calibration-20261102/REPORT.md (step 2b, 2026-11-02; calibration pass job 60714014, 1 node, 00:05:08; inputs = step-2 full pass job 60707582; tau_analysis HEAD bc0f904 + untracked joint_fit/rho_pi0_calib.py, rho_pi0_calib_legs.py, rho_pi0_calib_pass.py; constants calib_constants.json, calib_kE.json). Section 4 migration table r_c = f_c(data)/f_c(MC) with binomial errors from the data counts; uncertainty: pair and merged factors +-1 sigma coherently; assumption: migrating legs carry the kinematics of the category they end up in (pure rate reweighting). Objects per leg within 20 deg (E_MAIN > 0.5 GeV), merged-tagged data | all MC | MC/data: 0.0702|0.0856|1.220, 0.0781|0.1016|1.301, 0.0692|0.1046|1.513, 0.0772|0.1030|1.334. Section 3 (m(pi pi0) peak, Gauss + pol2 in [0.45, 1.15], data/MC) with k_e: single 1.0059 +- 0.0069 / 1.0078 +- 0.0067 / 1.0047 +- 0.0049 / 1.0011 +- 0.0076 / all 1.0049 +- 0.0031; merged 1.0347 +- 0.0122 / 0.9874 +- 0.0179 / 0.9753 +- 0.0172 / 1.0060 +- 0.0177 / all 1.0048 +- 0.0082; before (no k) single 1.0084 / 1.0179 / 0.9959 / 1.0154, merged 1.0375 / 0.9993 / 0.9661 / 1.0228; with k_mgg single 1992 1.0280 (worse), hence k_e adopted. Residual merged 1992 1.0347 (2.8 sigma) and 1994 0.9753 (1.4 sigma) enter as k variants. 1994 detector-description check (section 4): MC merged-shower response 1.154, data merged-tag rate lowest (0.0692) while MC highest (0.1046); inference from reconstructed showers, DELSIM description not inspected.
-->
