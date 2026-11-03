---
class: st pres
---

<script setup>
import ZoomablePlot from 'slidev-addon-ztautau/components/ZoomablePlot.vue'
</script>

# Calibration 1: check with the <LaTeX formula="\tau" /> polarisation, and its limits

<div class="st-sub">2-D shape fit of the <LaTeX formula="\rho" /> energy fraction and decay angle, usable legs; LEP <LaTeX formula="P_\tau=-0.144\pm0.004" />. After: <LaTeX formula="\pm" /> stat <LaTeX formula="\pm" /> calibration.</div>

<div class="st-cols st-cols-21">
<div>
<table class="num first-nw">
<thead><tr><th>Year</th><th>Before</th><th>After</th><th>Pull</th><th><LaTeX formula="|\mathrm{pull}|\lt2" /></th></tr></thead>
<tbody>
<tr><td>1992</td><td><LaTeX formula="-0.0995\pm0.0518" /></td><td><LaTeX formula="-0.1470\pm0.0513\pm0.0421" /></td><td><LaTeX formula="-0.05" /></td><td>yes</td></tr>
<tr><td>1993</td><td><LaTeX formula="-0.0377\pm0.0500" /></td><td><LaTeX formula="-0.1052\pm0.0495\pm0.0271" /></td><td><LaTeX formula="+0.68" /></td><td>yes</td></tr>
<tr><td>1994</td><td><LaTeX formula="+0.0073\pm0.0374" /></td><td><LaTeX formula="-0.0155\pm0.0370\pm0.0288" /></td><td><LaTeX formula="+2.73" /></td><td><b>no</b></td></tr>
<tr><td>1995</td><td><LaTeX formula="-0.1038\pm0.0539" /></td><td><LaTeX formula="-0.2118\pm0.0531\pm0.0209" /></td><td><LaTeX formula="-1.19" /></td><td>yes</td></tr>
<tr class="hl"><td>All</td><td><LaTeX formula="-0.0426\pm0.0232" /></td><td><LaTeX formula="-0.0970\pm0.0230\pm0.0326" /></td><td><LaTeX formula="+1.17" /></td><td>yes</td></tr>
</tbody>
</table>

<div class="co open"><b>Limits</b> Scale from electrons, not photons. Migration from the same legs. <LaTeX formula="\rho" /> regions about 80 % pure.</div>
</div>
<div>
<div class="st-fig h250"><ZoomablePlot src="/figures/photon-calibration/step2b/ptau_before_after.png" alt="P_tau before and after calibration per year and category" /></div>
<div class="st-cap"><LaTeX formula="P_\tau" /> per year: open = before, filled = after; line = LEP value.</div>
<div class="co warn"><b>1994</b> fails at <LaTeX formula="2.7\sigma" />: keep its <LaTeX formula="\rho" /> legs direction-only for now.</div>
</div>
</div>

<div class="st-source">Source: step 2b of the <LaTeX formula="\rho" />-polarimeter study, section 5, and the study conclusion with addendum A (2026-11-02/03); data check</div>

<!--
artifacts/rho-polarimeter-step2b-calibration-20261102/REPORT.md (step 2b, 2026-11-02; calibration pass job 60714014, 1 node, 00:05:08; inputs = step-2 full pass job 60707582; tau_analysis HEAD bc0f904 + untracked joint_fit/rho_pi0_calib.py, rho_pi0_calib_legs.py, rho_pi0_calib_pass.py; constants calib_constants.json, calib_kE.json) section 5 (re-validation, all data, full MC, nominal calibration). P_tau: 2-D (E_rho/E_beam, cos theta*) shape fit, normalisation free, exact pair reweighting, usable legs. Errors: stat (data + MC templates) [data only] +- calibration systematic (k +- sigma_k, migration +- 1 sigma, k(E) - flat k, quadrature); pull = (P_tau + 0.144)/sqrt(stat^2 + syst^2 + 0.004^2). MC -0.146, LEP -0.144 +- 0.004. Rows (usable): 1992 before -0.0995 +- 0.0518, after -0.1470 +- 0.0513 [0.0507] +- 0.0421 (k 0.0414 / migration 0.0072 / k(E) 0.0009), chi2 197.0/108, pull -0.05; 1993 -0.0377 +- 0.0500 -> -0.1052 +- 0.0495 [0.0490] +- 0.0271, 109.3/108, +0.68; 1994 +0.0073 +- 0.0374 -> -0.0155 +- 0.0370 [0.0366] +- 0.0288, 107.3/108, +2.73 (fail); 1995 -0.1038 +- 0.0539 -> -0.2118 +- 0.0531 [0.0525] +- 0.0209, 119.7/108, -1.19; all -0.0426 +- 0.0232 -> -0.0970 +- 0.0230 [0.0227] +- 0.0326, 138.8/108, +1.17. Effect decomposition (shape, usable, all years): photon scale -0.0050, migration -0.0497. Conclusion section 2: 'Before calibration the combined value was -0.031 +- 0.023 (5 sigma off)' (absolute-normalisation variant). Provenance limits: artifacts/rho-polarimeter-CONCLUSION-20261102.md (sections 1-3, addendum A of 2026-11-03) addendum A 'Calibration provenance, honestly stated': scale from an in-sample control (tau -> e legs) cross-checked by the gamma-gamma peak; migration weights derived from the rho legs themselves (shape-only validation); rho regions are the ML fit regions, about 80 % pure. Recommendation (section 5, conclusion section 4): 1994 rho legs direction-only (kappa 0.434) until the 1994 HPC simulation is understood. Figure plots/ptau_before_after.png.
-->
