---
class: st pres
---

# Appendix · calibration 1: pair peaks, response, object rates

<div class="st-sub">First two rows: data/simulation <LaTeX formula="m_{\gamma\gamma}" /> peak by pair type. Response: reconstructed/true photon energy in simulation (Gaussian core).</div>

<table class="num first-nw">
<thead><tr><th>Quantity</th><th>1992</th><th>1993</th><th>1994</th><th>1995</th><th>All</th></tr></thead>
<tbody>
<tr><td>HPC–HPC</td><td><LaTeX formula="0.9505\pm0.0148" /></td><td><LaTeX formula="1.0227\pm0.0207" /></td><td><LaTeX formula="0.9952\pm0.0143" /></td><td><LaTeX formula="1.0385\pm0.0149" /></td><td><LaTeX formula="1.0003\pm0.0080" /></td></tr>
<tr><td>HPC–conversion</td><td><LaTeX formula="0.9644\pm0.0165" /></td><td><LaTeX formula="0.9753\pm0.0155" /></td><td><LaTeX formula="0.9934\pm0.0124" /></td><td><LaTeX formula="1.0054\pm0.0169" /></td><td><LaTeX formula="0.9796\pm0.0080" /></td></tr>
<tr><td>Sim. response, photon (core)</td><td>1.0073</td><td>0.9515</td><td>1.0017</td><td>0.9518</td><td></td></tr>
<tr><td>Sim. response, merged shower</td><td>1.0741</td><td>1.0821</td><td>1.1544</td><td>1.0766</td><td></td></tr>
<tr><td>Sim. response, track conversion</td><td>1.0012</td><td>0.9994</td><td>1.0009</td><td>1.0004</td><td></td></tr>
<tr><td>Merged tags per leg, sim./data</td><td>1.220</td><td>1.301</td><td>1.513</td><td>1.334</td><td></td></tr>
<tr><td>Identified photons per leg, sim./data</td><td>0.955</td><td>0.970</td><td>0.978</td><td>0.984</td><td></td></tr>
</tbody>
</table>


<div class="st-source">Source: step 2b of the <LaTeX formula="\rho" />-polarimeter study (2026-11-02), sections 1a, 2a and 4</div>

<!--
artifacts/rho-polarimeter-step2b-calibration-20261102/REPORT.md (step 2b, 2026-11-02; calibration pass job 60714014, 1 node, 00:05:08; inputs = step-2 full pass job 60707582; tau_analysis HEAD bc0f904 + untracked joint_fit/rho_pi0_calib.py, rho_pi0_calib_legs.py, rho_pi0_calib_pass.py; constants calib_constants.json, calib_kE.json). Section 1a (m_gg of pair legs, fit [0.04, 0.25] GeV): HPC-HPC data/MC as shown; HPC-conversion data/MC as shown; conversion-conversion all 1.0713 +- 0.0111 (105 pairs); with a PHOT conversion-associated photon all 1.0026 +- 0.0183. Section 2a (photons matched to a generator pi0 photon within 2 deg, |cos theta| < 0.72): identified HPC photon core 1.0073 +- 0.0009 (sigma 0.125) / 0.9515 +- 0.0009 (0.139) / 1.0017 +- 0.0007 (0.140) / 0.9518 +- 0.0009 (0.136); median / raw HPC median 1.0690/0.9624, 1.0039/0.9019, 1.0581/0.9011, 1.0022/0.9015; merged-tagged 1.0741 +- 0.0042 / 1.0821 +- 0.0042 / 1.1544 +- 0.0055 / 1.0766 +- 0.0048; PHOT conversion-associated 1.0116 / 0.9387 / 0.9830 / 0.9362; track conversion 1.0012 +- 0.0004 / 0.9994 +- 0.0005 / 1.0009 +- 0.0003 / 1.0004 +- 0.0005; PHOT fail 0.9973 / 0.9231 / 0.9161 / 0.9136. Section 4 objects per leg within 20 deg (E_MAIN > 0.5 GeV), MC/data: identified photons 0.955 / 0.970 / 0.978 / 0.984; merged-tagged 1.220 / 1.301 / 1.513 / 1.334; PHOT failures 0.833 / 0.871 / 0.820 / 0.865; track conversions 0.978 / 1.077 / 1.033 / 1.214; HPC without PHOT 1.225 / 1.239 / 1.146 / 1.264; hadronic 1.032 / 0.783 / 0.838 / 0.886. Merged-tag rate data/MC vs E_MAIN 1994: 5-8 0.941, 8-12 0.647, 12-20 0.608, 20-46 0.575 (other years 0.70-1.10).
-->
