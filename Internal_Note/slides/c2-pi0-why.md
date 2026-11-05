---
class: st pres c2
---

# Calibration 2 · Final <LaTeX formula="\pi^0" /> step (calibration v3 stored): why, references, sample

<div class="st-sub">Naming: "Version 3" on the previous slides is the third <LaTeX formula="\ell^+\ell^-\gamma" /> study; "v3" here is the third <b>stored</b> calibration, which adds this <LaTeX formula="\pi^0" /> step to that shape.</div>

<div class="st-cols st-cols-2" style="gap:14px">
<div>
<table class="c2t first-nw">
<thead><tr><th>Reference</th><th>What it did</th></tr></thead>
<tbody>
<tr><td>ALEPH, Phys. Rept. 421 (2005) 191, §5.2.5</td><td>closed the photon calibration with the <LaTeX formula="\tau" /> <LaTeX formula="\pi^0" /> mass and resolution versus energy, data against simulation</td></tr>
<tr><td>DELPHI, EPJ C14 (2000) 585, §4.6</td><td>lists the <LaTeX formula="\tau" /> <LaTeX formula="\pi^0" /> among its energy-scale samples</td></tr>
<tr class="hl"><td>Owner, 2026-11-04</td><td>do the same as the final step of calibration 2</td></tr>
</tbody>
</table>
<div class="co ok" style="margin-top:8px"><b>What it adds</b> the <LaTeX formula="\rho" /> builder's own photons, down to 0.5 GeV, below the <LaTeX formula="\ell^+\ell^-\gamma" /> reach.</div>
</div>
<div>
<table class="c2t first-nw">
<thead><tr><th>Sample</th><th>Definition</th><th>In the fit</th></tr></thead>
<tbody>
<tr><td>Photons</td><td>resolved HPC showers, <LaTeX formula="E\ge0.5" /> GeV; merged <LaTeX formula="\pi^0" /> (code 101) and conversions excluded</td><td>yes</td></tr>
<tr><td>Pairs</td><td>two photons of one hemisphere, within <LaTeX formula="20^\circ" /> of the prong, <LaTeX formula="m_{\gamma\gamma}\lt0.4" /> GeV</td><td>yes</td></tr>
<tr><td>Class A</td><td>1-prong + 1-prong events, <LaTeX formula="\rho" /> legs</td><td>yes</td></tr>
<tr><td>Class B</td><td>other 1-prong legs (no <LaTeX formula="e" />/<LaTeX formula="\mu" /> tag)</td><td>yes</td></tr>
<tr class="hl"><td>Class C</td><td>3-prong hemispheres</td><td>no: 1992 class test <LaTeX formula="p=0.04" /></td></tr>
</tbody>
</table>
<div class="st-cap">Data pairs in the fit (A+B): 5,642 / 5,392 / 11,232 / 4,893 (1992–95); simulated <LaTeX formula="\pi^0" /> fraction in the peak window 0.8 (A), 0.5 (B).</div>
</div>
</div>

<div class="takeaway"><b>Takeaway</b> The last step fits the <LaTeX formula="\tau" /> <LaTeX formula="\pi^0\to\gamma\gamma" /> peak and width, as ALEPH and DELPHI did, on 27,000 data pairs from 1-prong hemispheres; 3-prong hemispheres are left out.</div>

<div class="st-source">Source: final-calibration report of 2026-11-04 (status, sections 2–3, 4.5); ALEPH Phys. Rept. 421 §5.2.5 and DELPHI EPJ C14 §4.6 as cited there</div>

<!--
artifacts/pi0-final-calib-20261104/CALIBRATION_V3_REPORT.md (2026-11-04; owner decision 2026-11-04 to take the final MC photon energy calibration from the tau pi0 -> gamma gamma peak and width, as ALEPH Phys. Rept. 421 (2005) 191 section 5.2.5 and DELPHI EPJ C14 (2000) 585 section 4.6; owner decision 2026-11-05: v3 is the nominal). Version naming: the deck's "Calibration 2 - Version 3" slides (c2-v3-*) describe artifacts/llgamma-v3-20261104 (third l+l-gamma study); the stored calibration versions are v1 (apply, all photons), v2 (code 101 skipped; l+l-gamma v4 bins from 3 GeV plus a pi0 conversion shape below, docs/PROJECT_GUIDE.md entries of 2026-11-04) and v3 (this step). The l+l-gamma v4 rerun is not described in this deck (PROJECT_GUIDE 2026-11-04: K_year 1993 1.039, 1995 1.038; bins for 1992, 1994). Section 2 table: HPC+HPC pairs from the 1p1p baseline skim (bit 0) and the pi0-calib skim (bits 1, 2), raw MC energies; photons delphi_98160 codes 1/11/61, E >= 0.5 GeV, no conversions, no code 101 (photon_pass, kind 'resolved HPC'); pairs: both photons within 20 deg of the summed prong momentum, all pairs, 0-0.4 GeV, 5 MeV bins; class A = exclusive per-hemisphere reason 'rho', B = other 1-prong (reasons e, mu excluded; also the 1-prong side of 1p3p), C = 3-prong. Section 3: pair extraction job 60823286 (4 nodes, 2 min 20 s); baseline 1p1p 14,544,588 rows read, 2,403,855 pairs stored; pi0-calib 906,367 pairs. Pairs per year/class (data): 1992 A/B/C 1134/4508/1293, 1993 1106/4286/1190, 1994 2137/9095/2595, 1995 948/3945/1204; pi0 fraction (MC same-pi0 share in the 0.10-0.17 GeV window) A 0.78-0.82, B 0.44-0.51, C 0.29-0.39 (slide rounds to 0.8 / 0.5). Stored fit (A+B) 5,642 / 5,392 / 11,232 / 4,893 data pairs; "27,000" = derived sum 27,159. Section 4.5: chi2 on (b, a) about the weighted mean 1992 10.0/4 (p 0.040; A-C p 0.031, B-C p 0.010), 1993 4.1/4 (0.39), 1994 4.6/4 (0.33), 1995 A-B 4.6/2 (0.10; C vertex outside the grid); C excluded in all years (one rule); A and B agree in every year (p >= 0.10). Even/odd data pairs balanced (16,761 / 16,680).
-->
