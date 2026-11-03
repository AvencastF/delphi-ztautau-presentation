---
class: st pres c2
---

# Calibration 2 · Step 1: samples — radiative <LaTeX formula="e^+e^-\gamma" /> and <LaTeX formula="\mu^+\mu^-\gamma" /> events

<div class="st-sub">Data: the converted leptonic long-DST streams of 1992–1995 after the good-run selection. Simulation: Bhabha (includes <LaTeX formula="Z\to ee" />) for <LaTeX formula="ee\gamma" />, <LaTeX formula="Z\to\mu\mu" /> for <LaTeX formula="\mu\mu\gamma" />.</div>

<table class="c2t num first-nw">
<thead><tr><th>Year</th><th><LaTeX formula="\sqrt{s}" /> points [GeV]</th><th>Luminosity [<LaTeX formula="\mathrm{pb}^{-1}" />]</th><th>Data events read</th><th>Bhabha sim. events</th><th><LaTeX formula="Z\to\mu\mu" /> sim. events</th></tr></thead>
<tbody>
<tr><td>1992</td><td>91.28</td><td>24.04</td><td>518,468</td><td>2,012,397</td><td>320,399</td></tr>
<tr><td>1993</td><td>89.43 / 91.22 / 93.02</td><td>9.67 / 16.45 / 9.99</td><td>567,433</td><td>2,978,098</td><td>325,799</td></tr>
<tr><td>1994</td><td>91.20</td><td>45.79</td><td>792,322</td><td>3,920,397</td><td>613,800</td></tr>
<tr><td>1995</td><td>89.44 / 91.30 / 92.97</td><td>8.45 / 13.78 / 9.32</td><td>433,488</td><td>2,595,593</td><td>281,700</td></tr>
</tbody>
</table>

<div class="st-cols st-cols-3" style="margin-top:10px">
<div class="co ok"><b>Why</b> The photon energy follows from the three directions (step 3): no calorimeter input.</div>
<div class="co ok"><b>Independent</b> No <LaTeX formula="\tau" /> event is used; the <LaTeX formula="\tau" /> sample stays for validation.</div>
<div class="co open"><b>Caveats</b> Luminosity uncertified; stream preselection acts on data only.</div>
</div>

<div class="takeaway"><b>Takeaway</b> Two radiative-dilepton samples in every year give a photon-energy reference that uses neither the calorimeter nor any <LaTeX formula="\tau" /> event.</div>

<div class="st-source">Source: per-year sample configurations, the <LaTeX formula="\ell^+\ell^-\gamma" /> selection note (2026-11-03) and the count table of the version-2 <LaTeX formula="\ell^+\ell^-\gamma" /> run</div>

<!--
Points and luminosities: tau_analysis/configs/1992.yaml ... 1995.yaml (points.ecm_gev, lumi_pb; DELPHI SATLUM92/SATLUM93/STILUM94/STILUM95 status 0 + RUNQUALI rule, good-cassette sums, uncertified): 1992_91p2 91.278 GeV 24.038755 pb-1; 1993_89p4 89.43234 / 9.672698, 1993_91p2 91.223296 / 16.454999, 1993_93p0 93.015116 / 9.993902; 1994_91p2 91.202 / 45.790648 (pending trigger certification); 1995_89p4 89.43761 / 8.447493, 1995_91p2 91.295352 / 13.78162, 1995_93p0 92.96528 / 9.324159. Event counts: artifacts/llgamma-v2-20261103/cutflows/cutflow.csv (run llgamma-v2-20261103, job 60747968, tau_analysis 5ac249d), region llg_presel_wide, cut input, kind cumulative, n summed over points: data 518,468 / 567,433 / 792,322 / 433,488 (= 2,311,711 after the run selection); Bhabha 2,012,397 / 2,978,098 / 3,920,397 / 2,595,593; Z_mumu 320,399 / 325,799 / 613,800 / 281,700 (identical to the v1 run llgamma-20261103). tau_analysis/docs/LLGAMMA_SELECTION_20261103.md section 1: data = lolept92_e2, lolept93_d2, lolept94_c2, lolept95_d2 (334 files, 2,395,361 events before run selection); the tau ML skim is not read; DELPHI leptonic-stream preselection applies to data only, its l+l-gamma efficiency not inspected. Z_ee excluded from the stacks (BHWIDE Bhabha contains the s-channel; docs/agent/DEVELOPMENT.md). Backgrounds read: Z_tautau, Z_qq, two-photon yy_ll, yy_qq. Why: E_pred formula, step 3 (analysis/single_photon.py). Independence: owner priority "Keep calibration and validation statistically independent" (AGENTS.md); the tau sample is not used in calibration 2.
-->
