---
class: st pres
---

<script setup>
import ZoomablePlot from 'slidev-addon-ztautau/components/ZoomablePlot.vue'
</script>

# Calibration 1: data/simulation before and after (1/2)

<div class="st-sub">Each figure: years in rows (last row: all years), barrel / forward / both in columns. Badges: all years, both regions. Click to zoom.</div>

<div class="st-grid st-grid-4">
<div><div class="st-fig h330"><ZoomablePlot src="/figures/photon-calibration/step2b/before-datamc_e_pi0_usable.png" alt="E_pi0 usable legs before calibration" /></div><div class="st-cap"><LaTeX formula="E_{\pi^0}" /> usable legs, <b>before</b><span class="badge a"><LaTeX formula="\chi^2/\mathrm{dof}" /> 109.6 / 46</span></div></div>
<div><div class="st-fig h330"><ZoomablePlot src="/figures/photon-calibration/step2b/after-datamc_e_pi0_usable.png" alt="E_pi0 usable legs after calibration" /></div><div class="st-cap"><LaTeX formula="E_{\pi^0}" />, <b>after</b><span class="badge a"><LaTeX formula="\chi^2/\mathrm{dof}" /> 84.6 / 46</span></div></div>
<div><div class="st-fig h330"><ZoomablePlot src="/figures/photon-calibration/step2b/before-datamc_cos_star_merged.png" alt="cos theta star merged legs before" /></div><div class="st-cap"><LaTeX formula="\cos\theta^*" />, merged, <b>before</b><span class="badge r"><LaTeX formula="\chi^2/\mathrm{dof}" /> 250.8 / 20</span></div></div>
<div><div class="st-fig h330"><ZoomablePlot src="/figures/photon-calibration/step2b/after-datamc_cos_star_merged.png" alt="cos theta star merged legs after" /></div><div class="st-cap"><LaTeX formula="\cos\theta^*" />, merged, <b>after</b><span class="badge g"><LaTeX formula="\chi^2/\mathrm{dof}" /> 24.2 / 20</span></div></div>
</div>

<div class="st-source">Source: step 2 (before) and step 2b (after) data/simulation plots of the <LaTeX formula="\rho" />-polarimeter study; all data, full simulation</div>

<!--
Before: artifacts/rho-polarimeter-step2-20261102/plots-full/datamc_<var>.png (step-2 full pass, job 60707582). After: artifacts/rho-polarimeter-step2b-calibration-20261102/plots-calibrated/datamc_<var>.png (nominal calibration = k_e + migration, variants/nominal, report 'python -m joint_fit.rho_pi0 report variants/nominal --out plots-calibrated'). chi2/ndf all years, barrel+forward, from REPORT.md section 5 table, identical to report.json datamc_chi2 ['all years|barrel+forward']: E_pi0 109.6/46 -> 84.6/46 (after per year 96.2, 53.3, 68.7, 63.8 /46); merged cos theta* 250.8/20 -> 24.2/20; v_k cone 81.6/30 -> 58.2/30 (after per year 30.3, 31.1, 60.5, 37.7); photon candidates 277.0/4 -> 21.1/4 (5.8, 2.8, 28.2, 12.7). MC absolute normalisation (run-quality luminosities, uncertified). Each figure: rows = 1992, 1993, 1994, 1995, all years; columns = barrel, forward, barrel+forward. Remaining excess concentrated in 1994 (E_pi0, m_pipi0, |h|, v_k) and in the 1992 single-photon category (E_pi0 96.2/46).
-->
