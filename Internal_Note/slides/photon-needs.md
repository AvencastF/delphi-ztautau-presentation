---
class: st pres
---

<script setup>
import ZoomablePlot from 'slidev-addon-ztautau/components/ZoomablePlot.vue'
</script>

# Photon scale: the simulation changes per year, the data do not

<div class="st-sub">Simulation response = reconstructed / true photon energy (Gaussian core); <LaTeX formula="m_{\gamma\gamma}" /> peak of photon pairs in <LaTeX formula="\rho" /> legs, both photons in the barrel calorimeter.</div>

<table class="num first-nw">
<thead><tr><th>Year</th><th>Sim. photon response</th><th>Sim. merged-shower response</th><th>Data <LaTeX formula="m_{\gamma\gamma}" /> [GeV]</th><th>Sim. <LaTeX formula="m_{\gamma\gamma}" /> [GeV]</th></tr></thead>
<tbody>
<tr><td>1992</td><td>1.0073</td><td>1.0741</td><td>0.1326</td><td>0.1395</td></tr>
<tr><td>1993</td><td>0.9515</td><td>1.0821</td><td>0.1305</td><td>0.1276</td></tr>
<tr><td>1994</td><td>1.0017</td><td>1.1544</td><td>0.1333</td><td>0.1340</td></tr>
<tr><td>1995</td><td>0.9518</td><td>1.0766</td><td>0.1325</td><td>0.1275</td></tr>
</tbody>
</table>

<div class="st-cols st-cols-12" style="margin-top:8px">
<div>
<div class="co ok"><b>Must deliver</b> per year: scale versus energy <LaTeX formula="k(E)" />; the resolution; the <LaTeX formula="\pi^0" /> category rates.</div>
</div>
<div>
<div class="st-fig h190"><ZoomablePlot src="/figures/photon-calibration/step2b/scale_functions_and_efficiency.png" alt="electron E/p scale function per year, MC photon response vs true energy, MC pi0 category vs opening angle" /></div>
<div class="st-cap">Left: electron data/simulation <LaTeX formula="E/p" /> per momentum bin. Middle: simulated photon response vs true energy. Right: simulated category vs true opening angle.</div>
</div>
</div>

<div class="st-source">Source: step 2b of the <LaTeX formula="\rho" />-polarimeter study (photon/<LaTeX formula="\pi^0" /> calibration, 2026-11-02), simulation truth and all data</div>

<!--
artifacts/rho-polarimeter-step2b-calibration-20261102/REPORT.md (step 2b, 2026-11-02; calibration pass job 60714014, 1 node, 00:05:08; inputs = step-2 full pass job 60707582; tau_analysis HEAD bc0f904 + untracked joint_fit/rho_pi0_calib.py, rho_pi0_calib_legs.py, rho_pi0_calib_pass.py; constants calib_constants.json, calib_kE.json). Section 2a (photons matched to a generator pi0 photon within 2 deg, |cos theta| < 0.72; core = Gauss + pol1 on E_MAIN/E_true in [0.6, 1.4]): identified HPC photon core 1.0073 +- 0.0009 / 0.9515 +- 0.0009 / 1.0017 +- 0.0007 / 0.9518 +- 0.0009; merged-tagged shower core 1.0741 +- 0.0042 / 1.0821 +- 0.0042 / 1.1544 +- 0.0055 / 1.0766 +- 0.0048. Section 1a HPC-HPC m_gg (fit range [0.04, 0.25] GeV, pairs exist only inside the builder window): data 0.1326 +- 0.0020 / 0.1305 +- 0.0026 / 0.1333 +- 0.0019 / 0.1325 +- 0.0019; MC 0.1395 +- 0.0003 / 0.1276 +- 0.0002 / 0.1340 +- 0.0002 / 0.1275 +- 0.0002. Conclusion section 2: 'merged showers +7 to +15 %'. Requirements: per-year scale vs energy, resolution (MC E/p Gauss sigma 0.100/0.111/0.112/0.112 vs data 0.115-0.122, login-sample fits, section 2b; 'MC resolution is ~5-20 % narrower than data'), category/migration efficiencies (merged-tag MC/data 1.220/1.301/1.513/1.334, section 4). Figure plots/scale_functions_and_efficiency.png.
-->
