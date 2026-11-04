---
class: st pres c2
---

# Calibration 2 · Version 3: comparison with the DELPHI references

<div class="st-sub">DELPHI values for the simulated photon energy against version 3 (MAIN energy, <LaTeX formula="E_\mathrm{pred}\ge5" /> GeV, statistical errors).</div>

<table class="c2t first-nw">
<thead><tr><th>Quantity</th><th>Reference</th><th>Ours (version 3)</th><th>Comment</th></tr></thead>
<tbody>
<tr><td>Scale 1993 / 1995</td><td><LaTeX formula="1.014\pm0.002" /> / <LaTeX formula="1.030\pm0.003" /> (Lefébure)</td><td><LaTeX formula="1.038\pm0.008" /> / <LaTeX formula="1.041\pm0.008" /></td><td>+0.024 / +0.011</td></tr>
<tr class="hl"><td>Scale 1994</td><td><LaTeX formula="1.041\pm0.002" /> (Lefébure)</td><td><LaTeX formula="0.988\pm0.005" /></td><td>opposite sign, <LaTeX formula="-0.053" /></td></tr>
<tr><td>Scale, <LaTeX formula="\tau" /> sample</td><td>1.05, 1992–95 together (98-160)</td><td><LaTeX formula="1.016\pm0.004" /> (<LaTeX formula="\ge1" /> GeV: 1.010)</td><td>same sign, ours smaller</td></tr>
<tr><td>Extra smearing</td><td><LaTeX formula="0.2/\sqrt{E}" /> above 0.8 GeV (98-160)</td><td><LaTeX formula="(0.28\pm0.02)/\sqrt{E}" />, no constant</td><td>same form, 40 % larger</td></tr>
<tr><td>Energy dependence</td><td>none per year; non-linearity corrected in reconstruction</td><td>flat above 3 GeV except 1995, 1992; 5–10 % fall below 3 GeV</td><td>MAIN energy removed most of the 1992 slope</td></tr>
<tr><td>Precision</td><td>0.2 % (EPJ C14), <LaTeX formula="\le" />0.5 % (EPJ C46)</td><td>0.5–0.8 % per year, photons only</td><td>comparable per sample</td></tr>
<tr><td>Photon definition</td><td>good codes incl. conversions, merged, any above 6 GeV</td><td>resolved HPC codes 1/11/61</td><td>ours about 20 % smaller</td></tr>
</tbody>
</table>

<div class="st-cols st-cols-2" style="margin-top:6px">
<div class="co warn"><b>1994</b> Electrons 0.971, version 2 0.958, version 3 0.988: simulation high; Lefébure scaled up.</div>
<div class="co open"><b>Caveats</b> Sub-3 GeV estimator unstable; rate 6–7 % low; narrower photons.</div>
</div>

<div class="takeaway"><b>Takeaway</b> 1993 and 1995 lie 0.024 and 0.011 above DELPHI's values; the smearing has the published form. 1994 disagrees in sign: check the 1994 detector description.</div>

<div class="st-source">Source: version-3 <LaTeX formula="\ell^+\ell^-\gamma" /> calibration report (2026-11-04), sections 7–8; DELPHI 98-160, Lefébure thesis 1997, EPJ C14, EPJ C46 via the literature reports</div>

<!--
artifacts/llgamma-v3-20261104/REPORT.md section 7 table (rows copied, merged 1993/1995 into one row): MC scale 1993 1.014 +- 0.002 (Lefebure 1997 section 4.2.2, Bhabha E + pi0 mass 1-45 GeV) vs 1.038 +- 0.008, +0.024; 1994 1.041 +- 0.002 vs 0.988 +- 0.005, opposite sign, -0.053; 1995 1.030 +- 0.003 vs 1.041 +- 0.008, +0.011; tau sample 1.05 (98-160, 1992-95 together) vs 1.016 +- 0.004 (>= 5 GeV), 1.010 (>= 1 GeV), same sign, ours smaller; energy dependence: none per year, non-linearity corrected in the reconstruction (DELPHI 92-61: unseen energy 3 % at 50 GeV -> 20 % at 5 GeV) vs flat above 3 GeV except 1995 (+5 %) and 1992 (mild), 5-10 % fall below 3 GeV, "the MAIN energy removed most of the v2 1992 slope; the sub-3 GeV fall is a residual non-linearity of the MC"; extra MC smearing 0.2/sqrt(E) above 0.8 GeV (98-160), 20 %/sqrt(E) (1991, DELPHI 93-65), "random smearing" (Lefebure) vs 0.28 +- 0.02 /sqrt(E), no constant, same form, 40 % larger; scale precision 0.2 % (EPJ C14), <= 0.5 % (EPJ C46), electrons + photons + pi0 vs 0.5-0.8 % per year, statistical, photons only; photon codes: good PXPHOT codes incl. conversions, merged, any > 6 GeV vs resolved HPC codes 1/11/61 only, ours 20 % smaller, documented, not changed. Rows not shown (REPORT section 7): threshold 0.5 GeV (same floor as the reconstruction), isolation d^2 E >= 10 (implemented as printed, also 5 deg, same k), intrinsic resolution 0.043 (+) 0.32/sqrt(E) (NIM A378), 0.31/E^0.44 (+) 0.027 (Lefebure, EPJ C46) not measured here; calibration variable (Bhabha E/p, pi0 mass, Compton, l+l-gamma kinematic energy; the l+l-gamma note itself was not found); peak estimator not given in any source (ours GaussExp + truncated mean); systematic treatment shift MC scale and vary smearing (EPJ C46; rho: scale 0.008, resolution 0.010 on P_tau, DELPHI 94-121) vs planned as nuisances (rho study step 4). 1994 (REPORT section 7 reading): our electrons 0.971 (calibration 1 k_e 1994 = 0.9714 +- 0.0042, rho-polarimeter step 2b), v2 photons 0.958, v3 photons 0.988 all say the 1994 MC is high; Lefebure's MC was scaled up; "Different simulation versions are the obvious candidate; it has to be settled against the 1994 detector description, not by choosing a number." Caveats (REPORT section 8): below 3 GeV the peak estimator is unstable (tail parameter at its limit) and the data/MC rate is 6-7 % low; 0.90-0.95 there is an observation, not a calibration point (needs a truncated mean with a tighter window or a fit with the tail fixed from 3-5 GeV); d^2 formula as printed hardly uses dtheta in the barrel; photon definition narrower (no conversions, merged showers, high-energy other codes); nested regions and the two isolations share events (channel and year splits are the only independent comparisons); GaussExp describes MC poorly; per-year a/b separation weak; not applied anywhere, no calibration file written; the rho-leg pi0 categories, which a floor of 0 would change in a full production, are untouched. Lefebure thesis: https://inspirehep.net/files/eb6772cb66111f474e388fccb2d3f48b (broad literature report section 2); 98-160: cds.cern.ch/record/2627713.
-->
