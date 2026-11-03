---
class: st pres
---

# Appendix · calibration 1: data/simulation <LaTeX formula="\chi^2" /> before and after

<div class="st-sub">All years, barrel and forward; per-year columns after calibration: 1992, 1993, 1994, 1995. The direction-only vector uses all neutrals and is not touched.</div>

<table class="sm num first-nw">
<thead><tr><th>Variable</th><th>Before</th><th>After</th><th>After, per year</th></tr></thead>
<tbody>
<tr><td><LaTeX formula="E_{\pi^0}" /></td><td>109.6/46</td><td>84.6/46</td><td>96.2, 53.3, 68.7, 63.8 /46</td></tr>
<tr><td><LaTeX formula="m(\pi\pi^0)" /></td><td>99.0/44</td><td>84.5/44</td><td>65.1, 39.5, 86.3, 37.8 /44</td></tr>
<tr><td><LaTeX formula="\cos\theta^*" /></td><td>64.0/20</td><td>49.2/20</td><td>34.5, 29.0, 53.8, 22.9 /20</td></tr>
<tr><td><LaTeX formula="E_\rho/E_\mathrm{beam}" /></td><td>91.4/22</td><td>75.4/22</td><td>77.8, 20.9, 57.3, 27.9 /22</td></tr>
<tr><td><LaTeX formula="h_k" /> (cone)</td><td>81.6/30</td><td>58.2/30</td><td>30.3, 31.1, 60.5, 37.7 /30</td></tr>
<tr><td><LaTeX formula="|h|" /> (cone)</td><td>75.7/21</td><td>48.2/21</td><td>41.2, 21.1, 97.2, 30.5 /21</td></tr>
<tr><td>Photon candidates</td><td>277.0/4</td><td>21.1/4</td><td>5.8, 2.8, 28.2, 12.7 /4</td></tr>
<tr><td><LaTeX formula="m_{\gamma\gamma}" /> (pair)</td><td>204.3/21</td><td>108.6/21</td><td>49.6, 60.3, 71.8, 43.4 /21</td></tr>
<tr><td>Merged: <LaTeX formula="E_{\pi^0}" />, <LaTeX formula="\cos\theta^*" />, <LaTeX formula="h_k" /></td><td>288.6, 250.8, 264.7</td><td>74.4/42, 24.2/20, 32.7/30</td><td></td></tr>
<tr><td>Direction-only <LaTeX formula="a_k" />, all legs</td><td>289.3/18</td><td>291.7/18</td><td>62.0, 70.2, 166.7, 90.1 /18</td></tr>
</tbody>
</table>


<div class="st-source">Source: step 2b of the <LaTeX formula="\rho" />-polarimeter study (2026-11-02), section 5</div>

<!--
artifacts/rho-polarimeter-step2b-calibration-20261102/REPORT.md (step 2b, 2026-11-02; calibration pass job 60714014, 1 node, 00:05:08; inputs = step-2 full pass job 60707582; tau_analysis HEAD bc0f904 + untracked joint_fit/rho_pi0_calib.py, rho_pi0_calib_legs.py, rho_pi0_calib_pass.py; constants calib_constants.json, calib_kE.json) section 5 table 'chi2/ndf all years (barrel+forward = barrel), before -> after; after per year 1992 / 1993 / 1994 / 1995'. Also: v_n / v_r / v_k off-shell 56.2, 85.1, 74.4 /30 -> 50.0, 81.8, 57.1 /30; v_n / v_r cone 76.0, 55.6 -> 67.1, 51.2 /30; pair E_pi0 / cos theta* / v_k 157.4, 122.0, 117.9 -> 66.6/46, 31.0/20, 25.1/30; single 104.8, 50.5, 51.1 -> 88.4/46, 39.1/20, 45.5/30. Outputs variants/<v>/ and plots-calibrated/ (report.json, ptau_calibrated{,_shape}.json).
-->
