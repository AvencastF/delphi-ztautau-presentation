---
class: st pres c2
---

# Calibration 2 · Final <LaTeX formula="\pi^0" /> step (v3): formula and fit

<div class="st-sub">Three parameters per year: scale <LaTeX formula="s" />, low-energy slope <LaTeX formula="b" />, smearing <LaTeX formula="a" />. Simulated photon energy <LaTeX formula="E\to k(E)\,(1+\sigma N)\,E" />; data untouched.</div>

<div class="st-cols" style="display:grid;grid-template-columns:1fr 1.15fr;gap:16px">
<div style="font-size:14.5px">
<LaTeX block formula="k(E)=s\,g(E)\qquad (E\ge3\ \mathrm{GeV})" />
<LaTeX block formula="k(E)=s\,g(3)\,\bigl[1+b\ln(E/3\ \mathrm{GeV})\bigr]\quad (E\lt3\ \mathrm{GeV})" />
<LaTeX block formula="\sigma_\mathrm{extra}/E=a/\sqrt{E}" />
<div class="co ok" style="margin-top:4px"><b><LaTeX formula="g(E)" /></b> the <LaTeX formula="\ell^+\ell^-\gamma" /> shape (fourth run, <LaTeX formula="E_\mathrm{pred}\ge3" /> GeV); its bins enter as Gaussian constraints on <LaTeX formula="s" />.</div>
<div class="co warn"><b>Constant term</b> tested, not significant: <LaTeX formula="2\Delta\mathrm{NLL}" /> = 0.09 / 0.32 / 3.41 / 0.70.</div>
</div>
<div>
<table class="c2t first-nw">
<thead><tr><th>Fit</th><th>Choice</th></tr></thead>
<tbody>
<tr><td>Likelihood</td><td>binned Poisson of <LaTeX formula="m_{\gamma\gamma}" /> in 2-D <LaTeX formula="(E_1,E_2)" /> bins, <LaTeX formula="\ge200" /> data pairs per bin (18–39 bins per year)</td></tr>
<tr><td>Templates</td><td>simulated same-<LaTeX formula="\pi^0" /> pairs and background, re-binned on the calibrated energies; both normalisations free per bin</td></tr>
<tr><td>Estimator</td><td>profiled NLL on a grid, quadratic fit (ripple 1–1.4 units)</td></tr>
<tr><td>Independence</td><td>fit on even events, closure on odd; stored: all events, errors <LaTeX formula="\times1.236" /> from the even/odd <LaTeX formula="\chi^2" /> 13.7/9</td></tr>
<tr class="hl"><td>Ten free knots</td><td>not fittable: no positive-definite likelihood, knots below 3 GeV oscillate 0.76–1.24</td></tr>
</tbody>
</table>
</div>
</div>

<div class="takeaway"><b>Takeaway</b> The <LaTeX formula="\pi^0" /> sample cannot fix ten free energy knots; it constrains one scale, one low-energy slope and one smearing per year, with the <LaTeX formula="\ell^+\ell^-\gamma" /> shape above 3 GeV.</div>

<div class="st-source">Source: final-calibration report of 2026-11-04, sections 2, 4.1, 4.4, 4.7, and its tables T1, T4, T7</div>

<!--
artifacts/pi0-final-calib-20261104/CALIBRATION_V3_REPORT.md status + section 2 (model: k at knots, smear a/sqrt(E) (+) c; E' = k(1 + sigma N) E, m'^2 = m^2 E1' E2' / (E1 E2); re-binning of (E_lo', E_hi'), floor and mass range applied after calibration; templates: signal = Z -> tau tau same-pi0 pairs, background = all other MC pairs, both normalisations free per energy bin (profiled exactly), background smoothed (Gaussian 10 MeV) and thinned to 50 %; free signal norm because the data/MC pi0 yield is not calibrated; fit: 2-D bins of >= 200 data pairs (18-39 per year), l+l-gamma v4 bins (E_pred >= 3 GeV, GaussExp, d2E, eeg + mumug) as Gaussian constraints at their <E_pred>; centre and covariance from a quadratic fit to the profiled NLL on a 3-D grid). Section 4.1: 10 knots (job 60826631): response surface not positive definite in any year; knots below 3 GeV 1992 1.15/0.80/1.02/0.81/0.89, 1993 0.94/0.76/1.16/0.94/1.10, 1994 1.07/0.89/1.20/1.15/0.90, 1995 0.90/1.03/0.81/1.24/1.08 (range 0.76-1.24), errors 0.12-0.32; 7 knots also not PD (1992-94), ripple 4-8 NLL units; cause: template re-sampling (template statistics ~80x data) and bin migration, ripple 0.5-1.5 units; adopted (s, b, a) on a grid s 0.985-1.015 x b -0.15..0.15 x a 0.10-0.46, quadratic to points within dNLL < 8 (86-186 points; ripple RMS 1.0-1.4; tables_v3.md T1: 1.29 / 1.19 / 1.41 / 1.02). Section 4.4 / T4: 2dNLL(c = 0 vs best) 0.09 / 0.32 / 3.41 / 0.70, best c 0.03 / 0.03 / 0.08 / 0.06, rule > 3.84; c = 0 stored. Section 4.7 / T7: even/odd chi2 sum 13.7/9 -> S = 1.236 applied to the stored covariance. g(E) = "l+l-gamma v4 shape already in v2" (the v4 rerun of the l+l-gamma study is not described in this deck; PROJECT_GUIDE.md entry of 2026-11-04). Formula on the slide copied from the report status ("What v3 is").
-->
