---
class: st pres c2
---

# Calibration 2 · Summary

<div class="st-sub">Radiative <LaTeX formula="e^+e^-\gamma" /> and <LaTeX formula="\mu^+\mu^-\gamma" /> events, 1992–1995, barrel calorimeter, statistical errors only.</div>

<div class="st-cols st-cols-3">
<div class="kv"><h3>Measured (version 3)</h3><dl>
<dt>Scale</dt><dd><LaTeX formula="k" /> per year for the simulated MAIN photon energy, <LaTeX formula="E_\mathrm{pred}\ge5" /> GeV</dd>
<dt>Values</dt><dd>1.016 / 1.038 / 0.988 / 1.041 (<LaTeX formula="\pm" />0.005–0.008)</dd>
<dt>Energy</dt><dd>flat above 3 GeV except 1995 (+5 %) and 1992 (mild)</dd>
<dt>Smearing</dt><dd><LaTeX formula="\sigma/E=(0.28\pm0.02)/\sqrt{E}" />, no constant term</dd>
<dt>Checks</dt><dd><LaTeX formula="d^2E" /> vs <LaTeX formula="5^\circ" /> within 0.008; channels within <LaTeX formula="1.3\sigma" /></dd>
</dl></div>
<div class="kv sim"><h3>For the <LaTeX formula="\rho" /> analysis (proposed)</h3><dl>
<dt>Scale</dt><dd>replace <LaTeX formula="k_e" /> per year by the version-3 <LaTeX formula="k" />, measured on the MAIN energy the <LaTeX formula="\pi^0" /> uses</dd>
<dt>Error</dt><dd>fit errors 0.005–0.008, as nuisances</dd>
<dt>Resolution</dt><dd>smear the simulation by <LaTeX formula="0.28/\sqrt{E}" /></dd>
<dt>Closure</dt><dd>version 2 only (0.991–1.014); redo for version 3</dd>
</dl></div>
<div class="kv"><h3 style="color:var(--nju-coral)">Not done</h3><dl>
<dt>Applied</dt><dd>no; owner: not yet</dd>
<dt>Below 3 GeV</dt><dd>0.90–0.95 observed, not yet a calibration point; 30 % of the <LaTeX formula="\rho" /> photons are there</dd>
<dt>1994</dt><dd>0.988, opposite sign to the thesis (1.041)</dd>
<dt>Photons</dt><dd>definition narrower than DELPHI's, about 20 % fewer</dd>
</dl></div>
</div>

<div class="takeaway"><b>Takeaway</b> Following DELPHI practice, radiative dilepton events give a per-year scale of the MAIN photon energy above 3–5 GeV and a smearing of the published form. 1993 and 1995 sit near DELPHI's values; 1994 and the photons below 3 GeV remain open, so nothing is applied yet.</div>

<div class="st-source">Source: steps 1–7 and version 3 of this chapter; version-3 calibration report (2026-11-04), sections 1, 5–8; the owner's instruction of 2026-11-03</div>

<!--
Measured: closure/REPORT.md sections 2.1, 3, 4; epred/REPORT.md section 6. Constants rounded to 3 decimals from 1.0429 +- 0.0100, 0.9577 +- 0.0075, 1.0232 +- 0.0104 (display precision: fractions 3 decimals). sigma_k proposal: the fit errors 0.0100 / 0.0075 / 0.0104 (range 0.008-0.011 shown, 0.0075 rounds to 0.008) and the 1992 line (a +- 0.0107, b +- 0.0179, cov -9.2e-5); statistical only; calibration 1 used sigma_k = max(|k_e - k_gg|, sigma_gg). Resolution: REPORT.md section 4 sigma ratio 1.21-1.51 (all years); closure section 3: not corrected by k. "About 1 %": closure after smooth 0.991-1.014 per year (1993 1.4 %, 1.1 sigma). "Except in 1992": step 7. Proposed changes are proposals of this chapter, not owner decisions. Not done: owner "not yet" (2026-11-03, coordinator brief); below 5 GeV excluded (threshold truncation; epred/REPORT.md section 3); coverage from rho-polarimeter-step2-20261102/photon_energy_coverage/REPORT.md (used photon objects < 5 GeV: 44.0 % data / 46.4 % MC; pair photons 77.1 / 77.6 %); raw HPC shower energy (single_photon.py hpc_energy_gev) vs MAIN energy of the pi0 builder: not reconciled, hadronic-Z pi0 as low-energy anchor and for category rates (artifacts/rho-polarimeter-CONCLUSION-20261102.md addendum A); migration weights r_c from calibration 1 (step 2b section 4) unchanged, calibration 2 gives no category rates; closure/REPORT.md section 7: same-sample closure, only the channel exchange is statistically independent. Fit model poor on MC (38 of 65 p < 0.01) but k stable to <= 0.014 against the truncated mean. Revision 2026-11-04 (owner request: add the version-3 results): "Measured" now carries version 3 (artifacts/llgamma-v3-20261104/REPORT.md): section 5.1 E_pred >= 5 GeV d2E 1.016 +- 0.008 / 1.038 +- 0.008 / 0.988 +- 0.005 / 1.041 +- 0.008 (errors 0.005-0.008); section 5.2 flat above 3 GeV except 1995 (+5 % between 12 and 25 GeV) and 1992 (0.99 at 5-17, 1.05 at 17-46 GeV); section 6 a only, all years d2E 0.281 +- 0.015 = (0.28 +- 0.02)/sqrt(E), b 0 (UL 0.038); checks: 5 deg - d2E per year 0.007 / 0.008 / 0.001 / 0.001 (derived), channels within 1.3 sigma (section 5.1). Proposed column: proposals of this chapter, not owner decisions; v3 k is measured on the MAIN energy, which is the energy the pi0 builder uses (coverage study), removing the raw-vs-MAIN caveat of version 2; nuisance treatment as planned in the rho study step 4 (REPORT section 7, "systematic treatment"); no closure study was run for version 3 (REPORT: calibration only, no fit tests). Not done: below 3 GeV (REPORT section 8: estimator unstable, tail parameter at its limit, rate 6-7 % low; 0.90-0.95 an observation); 30 % = all usable rho photon objects below 3 GeV, 29.5 % data / 31.1 % MC (coverage study, step 7b); 1994 0.988 +- 0.005 vs Lefebure 1.041 +- 0.002 (REPORT section 7); photon definition: resolved HPC codes 1/11/61 vs 98-160 good codes incl. conversions, merged, any > 6 GeV, about +20 % (REPORT section 3). Removed from this slide on 2026-11-04 (still true): migration weights unchanged (calibration 1), only the channel swap is independent (v2 closure section 7), raw shower vs MAIN energy (resolved by version 3).
-->
