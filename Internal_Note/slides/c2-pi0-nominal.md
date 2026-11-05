---
class: st pres c2
---

# Calibration 2 · Final <LaTeX formula="\pi^0" /> step (v3): the accepted calibration and its systematics

<div class="st-sub"><span class="tag decision">decision</span> Owner, 2026-11-05: v3 is the nominal photon energy calibration; the unresolved tensions are carried as systematics, not tuned further. <span class="id">all-years-calib98160-v3-20261104, tau_analysis f362ac7</span></div>

<div class="st-cols st-cols-3">
<div class="kv"><h3>Nominal</h3><dl>
<dt>Constants</dt><dd>per year <LaTeX formula="(s,b,a)" />, stored as a <LaTeX formula="k(E)" /> table 0.5–46 GeV plus <LaTeX formula="a/\sqrt{E}" /></dd>
<dt>Applied to</dt><dd>resolved HPC photons in simulation; merged <LaTeX formula="\pi^0" /> showers and conversions unscaled</dd>
<dt>Used by</dt><dd>the ML retraining and the spin fit, on the v3 skim</dd>
<dt>Nuisances</dt><dd><LaTeX formula="(s,b,a)" /> with their covariance, per year</dd>
</dl></div>
<div class="kv sim"><h3>Systematic variations</h3><dl>
<dt>Scale</dt><dd>one-sided per year: <LaTeX formula="\pi^0" />-only minus nominal, +2.2 / +2.7 / +3.7 / +6.6 %</dd>
<dt>Resolution</dt><dd>vary <LaTeX formula="a" /> so the simulated width moves by the <LaTeX formula="\rho" />-leg ratio 0.948 ± 0.031 (1995: 0.829 ± 0.058)</dd>
<dt>Conversions</dt><dd>±2.7 % energy scale (<LaTeX formula="\ell^+\ell^-\gamma" /> 1.011 vs <LaTeX formula="\pi^0" /> 0.973)</dd>
</dl></div>
<div class="kv"><h3 style="color:var(--nju-coral)">Open, not acted on</h3><dl>
<dt>1994</dt><dd>even/odd halves disagree on the slope <LaTeX formula="b" /> (<LaTeX formula="p" /> 0.013)</dd>
<dt>Smear</dt><dd>class A prefers a smaller <LaTeX formula="a" /> than class B in every year</dd>
<dt>Shapes</dt><dd>opening angle of classes B and C disagrees with simulation (<LaTeX formula="\chi^2" /> 93/10, 55/10)</dd>
<dt>Width bound</dt><dd>the <LaTeX formula="\rho" />-leg ratio is an upper bound on "too wide" (legs selected on raw energies)</dd>
</dl></div>
</div>

<div class="takeaway"><b>Takeaway</b> Calibration 2 is closed: v3 is the nominal, with a per-year scale variation of 2–7 %, a resolution variation from the <LaTeX formula="\rho" />-leg width, ±2.7 % on conversions and the fit covariance as nuisances. Everything downstream runs on the v3 skim.</div>

<div class="st-source">Source: project guide, owner decision of 2026-11-05; final-calibration report of 2026-11-04 (status, sections 1, 6, 8) and its table T3</div>

<!--
docs/PROJECT_GUIDE.md entry "Owner decision 2026-11-05: v3 accepted as the nominal photon calibration" (v3 skim analysis-runs/1992_1993_1994_1995/all-years-calib98160-v3-20261104/, job 60828758; tau_analysis f362ac7 constants in configs/calibration/calibration_result_<year>.yaml, deployed and hash-verified): scale variation = pi0-only minus nominal per year +2.2 / +2.7 / +3.7 / +6.6 % (derived check from tables_v3.md T3: 1.0250 - 1.0028 = 0.0222, 1.0262 - 0.9994 = 0.0268, 1.0391 - 1.0025 = 0.0366, 1.0692 - 1.0029 = 0.0663), treated as a one-sided per-year shift of s, redo, in addition to the (s, b, a) covariance nuisances; resolution: rho-leg pi0 width data/MC after v3 0.948 +- 0.031 overall, 0.829 +- 0.058 for 1995 (upper bound on "MC too wide" since the rho legs are selected on raw energies), vary a so the MC width moves by this ratio; conversions unscaled, +-2.7 % (l+l-gamma conversion subset 1.011 +- 0.009 vs c_conv 0.973 +- 0.016, CALIBRATION_V3_REPORT section 6); open items noted, not acted on: 1994 even/odd slope (p 0.013), class dependence of the smear (section 8.5: A 0.15-0.29, B 0.16-0.50 within errors), opening-angle shapes of classes B and C (section 8.6: chi2 93/10 and 55/10; class A 17/9). CALIBRATION_V3_REPORT status: stored and deployed (tau_analysis f362ac7 pushed, pulled on NERSC, sha256 of the six changed files identical; tests/check_calibration.py and run.py validate-config pass in the container), skip_codes [101], track-reconstructed conversions not in the photon_energy section. Slurm for v3: 4.02 node-h; chain total about 12.9 of 24 approved node-h (report section 9). "Calibration 2 is closed" = the owner decision ("no further tuning"); the open items are listed on the slide.
-->
