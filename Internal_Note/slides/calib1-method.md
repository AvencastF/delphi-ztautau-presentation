---
class: st pres
---

# Calibration 1 (in-sample): four control samples, simulation corrected

<div class="st-sub">Used in the <LaTeX formula="\rho" />-polarimeter study. All data, full simulation; corrections applied to the <b>simulation only</b>, data untouched.</div>

<table class="first-nw">
<thead><tr><th>Control</th><th>Sample</th><th>Gives</th></tr></thead>
<tbody>
<tr><td><LaTeX formula="\tau\to e" /> legs</td><td>electron-identified side, <LaTeX formula="|\cos\theta|\lt0.72" />, <LaTeX formula="5\lt p\lt40" /> GeV</td><td>photon scale <LaTeX formula="k_e" /> per year</td></tr>
<tr><td>Photon pairs in <LaTeX formula="\rho" /> legs</td><td>two resolved photons, <LaTeX formula="0.04\lt m_{\gamma\gamma}\lt0.25" /> GeV</td><td>cross-check <LaTeX formula="k_{\gamma\gamma}" />, error <LaTeX formula="\sigma_k" /></td></tr>
<tr><td><LaTeX formula="m(\pi\pi^0)" /> peak</td><td>single-photon and merged legs</td><td>closure after the scale</td></tr>
<tr><td>Category fractions</td><td>all reconstructed <LaTeX formula="\rho" /> legs</td><td>migration weights <LaTeX formula="r_c" /></td></tr>
</tbody>
</table>


<div class="st-cols st-cols-21" style="margin-top:8px">
<div>
<LaTeX formula="k_e=\dfrac{\mu\big[(E/p)_\mathrm{data}/s_\mathrm{data}\big]}{\mu\big[(E/p)_\mathrm{sim}\big]}" block />
<LaTeX formula="\sigma_k=\max\big(|k_e-k_{\gamma\gamma}|,\ \sigma_{\gamma\gamma}\big)" block />
<LaTeX formula="r_c=\dfrac{f_c^\mathrm{data}}{f_c^\mathrm{sim}},\qquad \textstyle\sum_c f_c^\mathrm{sim}\,r_c=1" block />
</div>
<div>
<div class="co ok"><b>Applied</b> Simulated single and merged <LaTeX formula="E_{\pi^0}\times k_e" />; each simulated leg weighted by <LaTeX formula="r_c" /> of its category.</div>
<div class="co warn"><b>Peaks</b> <LaTeX formula="\mu" /> = Gaussian mean with linear (<LaTeX formula="E/p" />) or quadratic (masses) background.</div>
</div>
</div>

<div class="st-source">Source: step 2b of the <LaTeX formula="\rho" />-polarimeter study (2026-11-02), sections 0, 1b, 2b, 2c and 4</div>

<!--
artifacts/rho-polarimeter-step2b-calibration-20261102/REPORT.md (step 2b, 2026-11-02; calibration pass job 60714014, 1 node, 00:05:08; inputs = step-2 full pass job 60707582; tau_analysis HEAD bc0f904 + untracked joint_fit/rho_pi0_calib.py, rho_pi0_calib_legs.py, rho_pi0_calib_pass.py; constants calib_constants.json, calib_kE.json). Electron definition (1b): leading tracks whose hemisphere exclusive-ID reason is 'e', |cos theta| < 0.72, 5 < p < 40 GeV (full MC pass; 3 < p < 40 in the login-sample checkpoint), E = stored linked HPC energy. s_data = the calibration 'data_scale' multiplying track-linked data showers in the baseline skim (1993 0.9645 / 0.967 / 0.967, 1994 1.0315, 1995 0.9625 / 0.961 / 0.9615 per point; 1992 none); 'raw' = stored / data_scale; MC showers get a mean-preserving smear; neutral (photon) showers are not corrected. Fit E/p: Gauss + pol1 in [0.65, 1.3]; masses: Gauss + pol2; binned chi2, variance max(n,1) data, sum w^2 MC; only ratios interpreted. k_gg = HPC-HPC m_gg data/MC (section 1a, window [0.04, 0.25]). sigma_k = max(|k_e - k_mgg|, sigma_mgg) (2c). Migration (section 4): r_c = f_c(data)/f_c(MC), c = pair, merged, single, fallback, reco-level category fractions of all reco-rho legs, MC = all compositions; sum_c f_c r_c = 1 keeps the per-year MC yield; energy integrated per year (E_pi0-binned factors would absorb the spin-dependent rho energy spectrum). Correction to MC only: single and merged pi0 energy x k_e(year) (flat 5-40 GeV value), direction and m_pi0 kept; pair legs unchanged (common scale absorbed by the mass fit; pair P_tau moves < 0.0015). Full pass job 60714014: 1,874,723 electrons, 1,901,246 photons in reco-rho cones, 796,991 MC true-rho legs; rows read 14,538,667.
-->
