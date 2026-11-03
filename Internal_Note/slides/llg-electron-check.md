---
class: st pres
---

# The electron check: <LaTeX formula="E/p" /> of the <LaTeX formula="ee\gamma" /> electrons per year

<div class="st-sub">Data/simulation of the <LaTeX formula="E/p" /> peak, <LaTeX formula="|\cos\theta|\lt0.72" />. The <LaTeX formula="ee\gamma" /> electrons have <LaTeX formula="p\gt15" /> GeV; the calibration-1 electrons <LaTeX formula="5\lt p\lt40" /> GeV.</div>

<table class="lg num first-nw">
<thead><tr><th>Year</th><th><LaTeX formula="ee\gamma" /> electrons, stored (vs Bhabha)</th><th>Calibration 1, stored</th><th>Calibration 1, raw = <LaTeX formula="k_e" /></th></tr></thead>
<tbody>
<tr><td>1992</td><td><LaTeX formula="1.0616\pm0.0079" /></td><td><LaTeX formula="1.0087\pm0.0049" /></td><td><LaTeX formula="1.0087\pm0.0049" /></td></tr>
<tr><td>1993</td><td><LaTeX formula="1.0047\pm0.0074" /></td><td><LaTeX formula="0.9962\pm0.0056" /></td><td><LaTeX formula="1.0306\pm0.0058" /></td></tr>
<tr><td>1994</td><td><LaTeX formula="1.0011\pm0.0053" /></td><td><LaTeX formula="1.0020\pm0.0043" /></td><td><LaTeX formula="0.9714\pm0.0042" /></td></tr>
<tr><td>1995</td><td><LaTeX formula="0.9973\pm0.0075" /></td><td><LaTeX formula="1.0009\pm0.0055" /></td><td><LaTeX formula="1.0411\pm0.0057" /></td></tr>
</tbody>
</table>

<div class="st-cap">"Stored": data with their track-shower correction (none in 1992). <LaTeX formula="ee\gamma" /> column: coordinator's truncated-mean fit of the saved histograms, 2026-11-03.</div>

<div class="st-cols st-cols-2" style="margin-top:10px">
<div class="co warn"><b>1992</b> <LaTeX formula="ee\gamma" /> electrons 1.062; calibration 1 at 32–40 GeV: <LaTeX formula="k_e=1.058" />.</div>
<div class="co ok"><b>1993–1995</b> Stored ratios within 0.005 of 1 in both samples.</div>
</div>

<div class="st-source">Source: saved histograms of the first <LaTeX formula="\ell^+\ell^-\gamma" /> run (fit by the coordinator, 2026-11-03) and step 2b of the <LaTeX formula="\rho" />-polarimeter study</div>

<!--
eeg column: values supplied by the coordinator on 2026-11-03 ('eeg calibrated stored E/p data/MC ... truncated mean, |cos|<0.72, from llgamma-20261103 histograms/summary.json lead_hpc_e_over_p_hemi0 in llg_eeg; Bhabha MC'); not recomputed here; histograms/summary.json is on NERSC only (Run llgamma-20261103: NERSC /pscratch/sd/a/avencast/Ztautau/analysis-runs/1992_1993_1994_1995/llgamma-20261103, jobs 60745549 + resume 60745978 (job ids from the coordinator brief of 2026-11-03), tau_analysis db00c4a (configs/analysis_llgamma.yaml, configs/plotting_llgamma.yaml) and 9c787d7 (finalize: confusion matrix n/a); local copy artifacts/llgamma-selection-20261103/ (cutflows/cutflow.csv sha256 258d18b94b34913628262fda4fe8c5f19e2548186f0f0cea6c4039d83911d1fb, agreement_table.json, plots/, plots-by-region/<region>/rates-by-group.md)). Values 1992 1.0616 +- 0.0079, 1993 1.0047 +- 0.0074, 1994 1.0011 +- 0.0053, 1995 0.9973 +- 0.0075. Step 2b (artifacts/rho-polarimeter-step2b-calibration-20261102/REPORT.md (step 2b, 2026-11-02; calibration pass job 60714014, 1 node, 00:05:08; inputs = step-2 full pass job 60707582; tau_analysis HEAD bc0f904 + untracked joint_fit/rho_pi0_calib.py, rho_pi0_calib_legs.py, rho_pi0_calib_pass.py; constants calib_constants.json, calib_kE.json)) section 2b: data/MC stored 1.0087 +- 0.0049 / 0.9962 +- 0.0056 / 1.0020 +- 0.0043 / 1.0009 +- 0.0055; raw = k_e 1.0087 +- 0.0049 / 1.0306 +- 0.0058 / 0.9714 +- 0.0042 / 1.0411 +- 0.0057. calib_kE.json mc_pi0_scale 1992 k at e = 36.0 GeV (32-40 GeV electron bin) 1.058 (section 2b: 1.0580 +- 0.0097). 'Stored' = with the calibration data_scale on track-linked data showers (1992: HPC correction disabled in the 1992 calibration file, docs/CALIBRATION_INTERFACE_20261101.md, so stored = raw). p > 15 GeV: llg_presel cut p/p_beam > 0.33 (14.8-15.3 GeV). 'within 0.005' derived: max |ratio - 1| = 0.0047 (eeg 1993) and 0.0038 (step 2b 1993).
-->
