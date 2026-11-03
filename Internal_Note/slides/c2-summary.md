---
class: st pres c2
---

# Calibration 2 · Summary

<div class="st-sub">Radiative <LaTeX formula="e^+e^-\gamma" /> and <LaTeX formula="\mu^+\mu^-\gamma" /> events, 1992–1995, barrel calorimeter, statistical errors only.</div>

<div class="st-cols st-cols-3">
<div class="kv"><h3>Measured</h3><dl>
<dt>Scale</dt><dd><LaTeX formula="k(E,\text{year})" /> for the simulated photon energy, 5–46 GeV</dd>
<dt>Values</dt><dd>1992 line in <LaTeX formula="\ln E" />; 1993 1.043, 1994 0.958, 1995 1.023</dd>
<dt>Closure</dt><dd>data/simulation 0.991–1.014 per year</dd>
<dt>Checks</dt><dd>channels swap within <LaTeX formula="1.7\sigma" />; energy points agree</dd>
</dl></div>
<div class="kv sim"><h3>For the <LaTeX formula="\rho" /> analysis (proposed)</h3><dl>
<dt>Scale</dt><dd>replace <LaTeX formula="k_e" /> per year by <LaTeX formula="k(E)" /></dd>
<dt>Error</dt><dd>replace <LaTeX formula="\sigma_k" /> by the fit errors, 0.008–0.011 (1992: line)</dd>
<dt>Resolution</dt><dd>add a smearing: data <LaTeX formula="1.2" />–<LaTeX formula="1.5\times" /> wider, not yet derived</dd>
</dl></div>
<div class="kv"><h3 style="color:var(--nju-coral)">Not done</h3><dl>
<dt>Applied</dt><dd>no; owner: not yet</dd>
<dt>Below 5 GeV</dt><dd>not covered; hadronic-<LaTeX formula="Z" /> <LaTeX formula="\pi^0" /> planned</dd>
<dt>Migration</dt><dd>category weights unchanged (calibration 1)</dd>
<dt>Split</dt><dd>only the channel swap is independent</dd>
</dl></div>
</div>

<div class="takeaway"><b>Takeaway</b> Radiative dilepton events give a per-year photon scale that closes data/simulation to about 1 % and confirms calibration 1 except in 1992; applying it is the owner's decision.</div>

<div class="st-source">Source: steps 1–7 of this chapter; the <LaTeX formula="\rho" />-polarimeter conclusion addendum A; the owner's instruction of 2026-11-03</div>

<!--
Measured: closure/REPORT.md sections 2.1, 3, 4; epred/REPORT.md section 6. Constants rounded to 3 decimals from 1.0429 +- 0.0100, 0.9577 +- 0.0075, 1.0232 +- 0.0104 (display precision: fractions 3 decimals). sigma_k proposal: the fit errors 0.0100 / 0.0075 / 0.0104 (range 0.008-0.011 shown, 0.0075 rounds to 0.008) and the 1992 line (a +- 0.0107, b +- 0.0179, cov -9.2e-5); statistical only; calibration 1 used sigma_k = max(|k_e - k_gg|, sigma_gg). Resolution: REPORT.md section 4 sigma ratio 1.21-1.51 (all years); closure section 3: not corrected by k. "About 1 %": closure after smooth 0.991-1.014 per year (1993 1.4 %, 1.1 sigma). "Except in 1992": step 7. Proposed changes are proposals of this chapter, not owner decisions. Not done: owner "not yet" (2026-11-03, coordinator brief); below 5 GeV excluded (threshold truncation; epred/REPORT.md section 3), hadronic-Z pi0 as low-energy anchor and for category rates (artifacts/rho-polarimeter-CONCLUSION-20261102.md addendum A); migration weights r_c from calibration 1 (step 2b section 4) unchanged, calibration 2 gives no category rates; closure/REPORT.md section 7: same-sample closure, only the channel exchange is statistically independent. Fit model poor on MC (38 of 65 p < 0.01) but k stable to <= 0.014 against the truncated mean.
-->
