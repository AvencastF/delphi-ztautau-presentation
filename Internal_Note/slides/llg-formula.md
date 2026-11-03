---
class: st pres
---

# Calibration 2: the calibration variable <LaTeX formula="R=E_\mathrm{HPC}/E_\mathrm{pred}" />

<div class="st-sub">Three massless bodies with zero total momentum lie in a plane; each energy is proportional to the sine of the angle between the other two.</div>

<div class="st-cols st-cols-2">
<div>
<LaTeX formula="E_\mathrm{pred}=\sqrt{s}\;\frac{\sin\theta_{12}}{\sin\theta_{12}+\sin\theta_{1\gamma}+\sin\theta_{2\gamma}}" block />
<div class="kv"><dl>
<dt><LaTeX formula="\theta_{12}" /></dt><dd>angle between the two leading tracks</dd>
<dt><LaTeX formula="\theta_{i\gamma}" /></dt><dd>angle between track <LaTeX formula="i" /> and the photon</dd>
<dt><LaTeX formula="\sqrt{s}" /></dt><dd>per-event beam energy sum (data: calibrated; simulation: generated)</dd>
<dt>Broken by</dt><dd>radiation along the beam (removed by <LaTeX formula="E_\mathrm{vis}/\sqrt{s}\gt0.8" />), masses, angular resolution</dd>
</dl></div>
</div>
<div>
<LaTeX formula="f(R)\propto\begin{cases}e^{-t^2/2} & t\ge-k_t\\ e^{k_t^2/2+k_t t} & t\lt-k_t\end{cases},\quad t=\frac{R-\mu}{\sigma}" block />
<div class="co ok"><b>Fit</b> <LaTeX formula="0.6\lt R\lt1.4" />, bins of 0.02: data Poisson likelihood, simulation <LaTeX formula="\chi^2" /> with weights.</div>
<div class="co ok"><b>Scale</b> <LaTeX formula="k=\mu_\mathrm{data}/\mu_\mathrm{sim}" />; width ratio <LaTeX formula="\sigma_\mathrm{data}/\sigma_\mathrm{sim}" />.</div>
<div class="co warn"><b>Cross-check</b> Truncated mean within <LaTeX formula="\pm1.5" /> widths, bootstrap errors.</div>
</div>
</div>

<div class="st-source">Source: the single-photon variable code and the selection note (section 9); method section of the version-2 study report</div>

<!--
tau_analysis/analysis/single_photon.py (5ac249d) function epred(sqrt_s, theta_12, theta_1g, theta_2g) = sqrt_s * sin(theta_12) / (sin theta_12 + sin theta_1g + sin theta_2g), None if undefined; single_photon_e_over_epred = single_photon_energy / single_photon_epred (invalid if E_pred <= 0). Track directions = MAIN momenta of the two leading tracks; photon direction = its MAIN momentum; photon energy = stored HPC (EMNC type-1) shower energy, uncalibrated (the run's hpc_scale section scales only track-linked showers). sqrt(s) = per-event sDST_EVT_ECMS after raw-row calibration (data: calibrated beam energy; MC: generated value), the same as in evis_over_ecm and p_over_pbeam. tau_analysis/docs/LLGAMMA_SELECTION_20261103.md section 9.1: exact for a massless three-body final state with no further radiation (checked in tests/check_single_photon_variables.py against an event built from energy-momentum conservation); lepton masses, a fourth (ISR/FSR) photon, track angular and photon direction resolution bias it, not modelled. Derivation (sine rule): sum of momenta zero -> momenta coplanar, |p_1|/sin(theta_2g) = |p_2|/sin(theta_1g) = |p_gamma|/sin(theta_12); with E = |p| and sum E = sqrt(s) the formula follows. Fit (artifacts/llgamma-v2-20261103/REPORT.md section 1, study/fit_peaks.py): single_photon_e_over_epred in [0.6, 1.4] (40 bins of 0.02); GaussExp (Gaussian core mu, sigma joined with continuous derivative to an exponential low-side tail at (x - mu)/sigma = -k; S. Das arXiv:1603.08591), integrated per bin, free N, mu, sigma, k; data binned Poisson likelihood, goodness = Baker-Cousins chi2; MC binned chi2 with stored sumw2; Hessian errors (scipy). Peak = mu, width = sigma (core). Also data fit with k fixed to MC. Truncated mean: iterated, mu +- 1.5 s, s = rms_window/0.7375, bins weighted by overlap, 300-replica bootstrap. Ratios data/MC with errors in quadrature.
-->
