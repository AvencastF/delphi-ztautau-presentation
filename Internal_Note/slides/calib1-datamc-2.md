---
class: st pres
---

<script setup>
import ZoomablePlot from 'slidev-addon-ztautau/components/ZoomablePlot.vue'
</script>

# Calibration 1: data/simulation before and after (2/2)

<div class="st-sub">Polarimeter component along the <LaTeX formula="\tau" /> flight and the number of photon candidates per leg. Remaining excess: 1994 and the 1992 single-photon legs.</div>

<div class="st-grid st-grid-4">
<div><div class="st-fig h330"><ZoomablePlot src="/figures/photon-calibration/step2b/before-datamc_v_k_cone_usable.png" alt="polarimeter k component cone before" /></div><div class="st-cap"><LaTeX formula="h_k" /> (cone), <b>before</b><span class="badge a"><LaTeX formula="\chi^2/\mathrm{dof}" /> 81.6 / 30</span></div></div>
<div><div class="st-fig h330"><ZoomablePlot src="/figures/photon-calibration/step2b/after-datamc_v_k_cone_usable.png" alt="polarimeter k component cone after" /></div><div class="st-cap"><LaTeX formula="h_k" /> (cone), <b>after</b><span class="badge a"><LaTeX formula="\chi^2/\mathrm{dof}" /> 58.2 / 30</span></div></div>
<div><div class="st-fig h330"><ZoomablePlot src="/figures/photon-calibration/step2b/before-datamc_n_cand_usable.png" alt="photon candidates per leg before" /></div><div class="st-cap">photon candidates, <b>before</b><span class="badge r"><LaTeX formula="\chi^2/\mathrm{dof}" /> 277.0 / 4</span></div></div>
<div><div class="st-fig h330"><ZoomablePlot src="/figures/photon-calibration/step2b/after-datamc_n_cand_usable.png" alt="photon candidates per leg after" /></div><div class="st-cap">photon candidates, <b>after</b><span class="badge r"><LaTeX formula="\chi^2/\mathrm{dof}" /> 21.1 / 4</span></div></div>
</div>

<div class="st-source">Source: step 2 (before) and step 2b (after) data/simulation plots of the <LaTeX formula="\rho" />-polarimeter study; all data, full simulation</div>

<!--
Before: artifacts/rho-polarimeter-step2-20261102/plots-full/datamc_<var>.png (step-2 full pass, job 60707582). After: artifacts/rho-polarimeter-step2b-calibration-20261102/plots-calibrated/datamc_<var>.png (nominal calibration = k_e + migration, variants/nominal, report 'python -m joint_fit.rho_pi0 report variants/nominal --out plots-calibrated'). chi2/ndf all years, barrel+forward, from REPORT.md section 5 table, identical to report.json datamc_chi2 ['all years|barrel+forward']: E_pi0 109.6/46 -> 84.6/46 (after per year 96.2, 53.3, 68.7, 63.8 /46); merged cos theta* 250.8/20 -> 24.2/20; v_k cone 81.6/30 -> 58.2/30 (after per year 30.3, 31.1, 60.5, 37.7); photon candidates 277.0/4 -> 21.1/4 (5.8, 2.8, 28.2, 12.7). MC absolute normalisation (run-quality luminosities, uncertified). Each figure: rows = 1992, 1993, 1994, 1995, all years; columns = barrel, forward, barrel+forward. Remaining excess concentrated in 1994 (E_pi0, m_pipi0, |h|, v_k) and in the 1992 single-photon category (E_pi0 96.2/46).
-->
