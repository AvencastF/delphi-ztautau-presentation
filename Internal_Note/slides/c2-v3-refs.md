---
class: st pres c2
---

# Calibration 2 · Version 3: what DELPHI did, and where version 2 differed

<div class="st-sub">DELPHI <LaTeX formula="\tau" /> analyses of 1992–1995 data against version 2 (steps 1–7). Owner decision 2026-11-04: follow DELPHI practice.</div>

<table class="c2t first-nw">
<thead><tr><th>Item</th><th>DELPHI</th><th>Source</th><th>Our version 2</th></tr></thead>
<tbody>
<tr><td>Samples</td><td>photons from <LaTeX formula="e^+e^-\gamma" />, <LaTeX formula="\mu^+\mu^-\gamma" />; electrons from Bhabha, Compton; <LaTeX formula="\pi^0" /> from <LaTeX formula="\tau" />; 0.5–40 GeV</td><td>EPJ C14 §4.6; EPJ C46 §4.2.4</td><td><LaTeX formula="e^+e^-\gamma" />, <LaTeX formula="\mu^+\mu^-\gamma" /> only</td></tr>
<tr><td>Photon threshold</td><td><LaTeX formula="E_\mathrm{shower}\gt0.5" /> GeV</td><td>98-160 §2.2; EPJ C14 §4.3</td><td>3 GeV</td></tr>
<tr><td>Isolation</td><td><LaTeX formula="d^2E\ge10\ \mathrm{deg^2\,GeV}" />, <LaTeX formula="d^2=\Delta\phi^2+\Delta\theta^2/\tan^2\theta" /> (printed <LaTeX formula="\tan\theta^2" />)</td><td>98-160 §2.2; EPJ C46 §4.2.3</td><td>fixed <LaTeX formula="5^\circ" /> to the nearer track</td></tr>
<tr><td>Photon energy</td><td>MAIN energy: “corrected for non-linearities and crack losses”</td><td>long DST manual 97-148</td><td>raw cluster energy</td></tr>
<tr><td>Simulation correction</td><td>per-year scale 1.014 / 1.041 / 1.030 (1993–95) + smearing; or <LaTeX formula="\times1.05" /> and <LaTeX formula="0.2/\sqrt{E}" /> above 0.8 GeV</td><td>Lefébure 1997 §4.2.2; 98-160 §3.2</td><td>scale <LaTeX formula="k" /> per year, no smearing</td></tr>
<tr><td>Systematics</td><td>shift the simulated scale by its error, vary the smearing, redo the analysis; precision 0.2 % / <LaTeX formula="\le" />0.5 %</td><td>EPJ C46 §8.7; EPJ C14; EPJ C46</td><td>not yet</td></tr>
<tr><td>Resolution</td><td><LaTeX formula="\sigma/E=0.043\oplus0.32/\sqrt{E}" /></td><td>NIM A378 §11.1</td><td>not measured</td></tr>
</tbody>
</table>

<div class="co open" style="margin-top:6px"><b>Not found</b> DELPHI's own <LaTeX formula="\ell\ell\gamma" /> calibration cuts and formula.</div>

<div class="takeaway"><b>Takeaway</b> DELPHI calibrated the corrected MAIN energy from 0.5 GeV with a <LaTeX formula="d^2E" /> isolation, and corrected the simulation per year by a scale plus an <LaTeX formula="a/\sqrt{E}" /> smearing. Version 2 differed in all three: 3 GeV, <LaTeX formula="5^\circ" />, raw energy.</div>

<div class="st-source">Source: the two DELPHI photon-calibration literature reports of 2026-11-04 (DELPHI 98-160, Lefébure thesis 1997, NIM A378, EPJ C14, EPJ C46, long DST manual)</div>

<!--
Calibration 2, version 3 (owner decision 2026-11-04: redo the l+l-gamma calibration following DELPHI practice: threshold 0.5 GeV, isolation d^2 E > 10 deg^2 GeV, MAIN photon energy; pi0 -> gamma gamma left out; calibration only). Literature: artifacts/delphi-photon-calibration-literature-20261104.md (Zotero PDFs) sections A1-A3, A6, E; artifacts/delphi-photon-calibration-literature-broad-20261104.md sections 0, 1.1, 1.6, 1.7, 2 and the addendum on the 98-160 isolation formula. Samples: EPJ C14 (2000) 585 section 4.6 pp. 593-594 ("These photons or electrons covered the full energy range 0.5 GeV to 40 GeV"; precision 0.2 %); EPJ C46 (2006) 1 section 4.2.4 p. 10 (isolated photons in mumugamma, eegamma and Compton; "A precision of 0.5% or better"; journal reference not printed in the Zotero preprint CERN-PH-EP/2004-046, from the first literature report's knowledge). Threshold: DELPHI 98-160 PHYS 802 CAL 142 (Lopez, Matorras, 1998, cds 2627713) section 2.2 E_shower < 0.5 GeV rejected; EPJ C14 section 4.3 "energy greater than 0.5 GeV"; EPJ C46 section 4.2.3 E_sh > 500 MeV. Isolation: 98-160 section 2.2, re-read from the page image (printed page 2): reject if d^2_shw-char * E_shower < 10 degree^2 GeV, d^2 = dphi^2 + dtheta^2/tan theta^2 ("tan theta^2" as typeset, read as tan^2 theta), d = distance on the HPC inner surface between the shower and the track extrapolation, minimum over tracks; which polar angle and units not stated. EPJ C46 4.2.3: d^2 E > 10 deg^2 GeV, d = opening angle at the HPC inner surface. MAIN energy: long DST manual DELPHI 97-148 PROG-223 v1.05 (printed p. 60): the HPC cluster energy "is not corrected for non-linearities in the HPC"; for neutrals the MAIN-module energy "is corrected for non-linearities and crack losses"; ELEPHANT 96-82 PROG 217: PXNECO "null on short and long DST's". MC correction: Lefebure thesis 1997 section 4.2.2: MC HPC energy scaled by 1.014 +- 0.002 (1993), 1.041 +- 0.002 (1994), 1.030 +- 0.003 (1995) plus a random smearing (value not given), tuned to Bhabha E and the pi0 mass 1-45 GeV. 98-160 section 3.2 [verified page image]: "extra MC smearing (with sigma = 0.2/sqrt(E) if E > 0.8 GeV) and calibration (MC energies were scaled up by 1.05)"; absolute or relative sigma not stated. 1991: 20 %/sqrt(E) smearing (DELPHI 93-91, 93-65). Systematics: EPJ C46 section 8.7 (shift the MC HPC scale by the 4.2.4 uncertainty, smear MC energies, redo); rho: EPJ C14 Table 3 energy scale/resol. 0.011; DELPHI 94-121 scale 0.008, resolution 0.010. Resolution: NIM A378 (1996) 57 section 11.1 (preprint p. 45) sigma/E = 0.043 (+) 0.32/sqrt(E), sample not stated; EPJ C46 0.31 E^-0.44 (+) 0.027. Version 2: tau_analysis 5ac249d configs/analysis_llgamma_v2.yaml (photon_e3: 3 GeV on hpc_energy_gev; iso5: opening angle >= 5 deg), single_photon.py hpc_energy_gev = raw cluster energy. Not found in either report: the DELPHI note with the l+l-gamma photon-scale cuts and the explicit reference-energy formula (broad report section 4; first report D1-D2).
-->
