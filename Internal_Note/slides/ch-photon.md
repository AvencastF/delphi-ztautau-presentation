---
title: Chapter — Photon calibration
class: nju-chapter-bridge
---

<div class="chapter-copy">
<h1>Photon energy calibration.</h1>
<p>The <LaTeX formula="\rho" /> polarimeter needs the <LaTeX formula="\pi^0" /> energy of every leg, and the simulated photon energy scale changes from year to year. Two calibrations so far: the in-sample one used in the <LaTeX formula="\rho" /> study, and a dedicated one from radiative <LaTeX formula="e^+e^-\gamma" /> and <LaTeX formula="\mu^+\mu^-\gamma" /> events.</p>
<div class="chapter-context"><span class="tag data">data</span><span>1992–1995, barrel calorimeter</span><span class="context-rule"></span><span class="tag open">open</span><span>no calibration constant adopted yet</span></div>
</div>

<DeckChapters :active="7" />

<!--
Chapter added 2026-11-03 at the owner's request (explain the calibration procedure, samples, cuts, formulas, tables and plots). Calibration 1 = rho-polarimeter step 2b (artifacts/rho-polarimeter-step2b-calibration-20261102/REPORT.md (step 2b, 2026-11-02; calibration pass job 60714014, 1 node, 00:05:08; inputs = step-2 full pass job 60707582; tau_analysis HEAD bc0f904 + untracked joint_fit/rho_pi0_calib.py, rho_pi0_calib_legs.py, rho_pi0_calib_pass.py; constants calib_constants.json, calib_kE.json)). Calibration 2 = radiative dilepton study: tau_analysis/docs/LLGAMMA_SELECTION_20261103.md; Run llgamma-20261103: NERSC /pscratch/sd/a/avencast/Ztautau/analysis-runs/1992_1993_1994_1995/llgamma-20261103, jobs 60745549 + resume 60745978 (job ids from the coordinator brief of 2026-11-03), tau_analysis db00c4a (configs/analysis_llgamma.yaml, configs/plotting_llgamma.yaml) and 9c787d7 (finalize: confusion matrix n/a); local copy artifacts/llgamma-selection-20261103/ (cutflows/cutflow.csv sha256 258d18b94b34913628262fda4fe8c5f19e2548186f0f0cea6c4039d83911d1fb, agreement_table.json, plots/, plots-by-region/<region>/rates-by-group.md); Run llgamma-v2-20261103: NERSC /pscratch/sd/a/avencast/Ztautau/analysis-runs/1992_1993_1994_1995/llgamma-v2-20261103, job 60747968 (coordinator brief), tau_analysis 5ac249d (configs/analysis_llgamma_v2.yaml, configs/plotting_llgamma_v2.yaml, analysis/single_photon.py); study artifacts/llgamma-v2-20261103/REPORT.md, peak_fits.json, tables/yields.md, tables/chi2_table.md, epred/REPORT.md, epred/k_epred.json (NERSC login node, light python only). HPC = DELPHI barrel electromagnetic calorimeter (High-density Projection Chamber). No calibration file has been written and the rho study has not been rerun with the l+l-gamma scale (owner: 'not yet', 2026-11-03, relayed by the coordinator). Luminosities are user-supplied run-quality values, uncertified.
-->
