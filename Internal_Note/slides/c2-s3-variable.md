---
class: st pres c2
---

# Calibration 2 · Step 3: the calibration variable <LaTeX formula="R=E_\mathrm{HPC}/E_\mathrm{pred}" />

<div class="st-sub">Measured photon energy over the energy predicted from the three directions.</div>

<div class="st-cols st-cols-2">
<div>
<LaTeX formula="E_\mathrm{pred}=\sqrt{s}\;\frac{\sin\theta_{12}}{\sin\theta_{12}+\sin\theta_{1\gamma}+\sin\theta_{2\gamma}}" block />
<div class="kv"><dl>
<dt><LaTeX formula="\theta_{12}" /></dt><dd>angle between the two leptons</dd>
<dt><LaTeX formula="\theta_{i\gamma}" /></dt><dd>angle between lepton <LaTeX formula="i" /> and the photon</dd>
<dt><LaTeX formula="\sqrt{s}" /></dt><dd>per-event collision energy</dd>
<dt>Biased by</dt><dd>beam-axis radiation (cut 5), masses, resolution</dd>
</dl></div>
<div class="co ok"><b>Why it works</b> Three massless particles with zero total momentum: each energy follows from the angles.</div>
</div>
<div>
<LaTeX formula="f(R)\propto\begin{cases}e^{-t^2/2} & t\ge-k_t\\ e^{k_t^2/2+k_t t} & t\lt-k_t\end{cases},\quad t=\frac{R-\mu}{\sigma}" block />
<div class="co ok"><b>Fit</b> <LaTeX formula="0.6\lt R\lt1.4" />, bins of 0.02: Gaussian core with an exponential low-side tail.</div>
<div class="co ok"><b>Scale</b> <LaTeX formula="k=\mu_\mathrm{data}/\mu_\mathrm{sim}" />; width ratio <LaTeX formula="\sigma_\mathrm{data}/\sigma_\mathrm{sim}" />.</div>
<div class="co warn"><b>Cross-check</b> Truncated mean within <LaTeX formula="\pm1.5" /> widths.</div>
</div>
</div>

<div class="takeaway"><b>Takeaway</b> <LaTeX formula="R" /> compares the calorimeter energy with an energy fixed by angles alone; the data/simulation ratio of its peak, <LaTeX formula="k" />, is the calibration.</div>

<div class="st-source">Source: the single-photon variable code and the selection note (section 9); method section of the version-2 study report</div>

<!--
tau_analysis/analysis/single_photon.py (5ac249d) function epred(sqrt_s, theta_12, theta_1g, theta_2g) = sqrt_s * sin(theta_12) / (sin theta_12 + sin theta_1g + sin theta_2g); single_photon_e_over_epred = single_photon_energy / single_photon_epred (invalid if E_pred <= 0). Track directions = MAIN momenta of the two leading tracks; photon direction = its MAIN momentum; photon energy = stored HPC (EMNC) shower energy, uncalibrated. sqrt(s) = per-event sDST_EVT_ECMS after raw-row calibration (data: calibrated beam energy; MC: generated value). Derivation (sine rule): momenta sum to zero -> coplanar, |p_1|/sin(theta_2g) = |p_2|/sin(theta_1g) = |p_gamma|/sin(theta_12); E = |p|, sum E = sqrt(s). tau_analysis/docs/LLGAMMA_SELECTION_20261103.md section 9.1: exact for a massless three-body final state with no further radiation (tests/check_single_photon_variables.py); lepton masses, a fourth photon, angular resolution bias it. Fit (artifacts/llgamma-v2-20261103/REPORT.md section 1, study/fit_peaks.py): R in [0.6, 1.4], 40 bins of 0.02; GaussExp (S. Das arXiv:1603.08591), free N, mu, sigma, k_t; data binned Poisson likelihood, MC binned chi2 with sumw2; Hessian errors. Truncated mean: iterated mu +- 1.5 s, 300-replica bootstrap. Ratios data/MC with errors in quadrature.
-->
