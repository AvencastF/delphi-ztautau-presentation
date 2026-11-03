---
class: st pres
---

# Calibration 2: radiative <LaTeX formula="e^+e^-\gamma" /> and <LaTeX formula="\mu^+\mu^-\gamma" /> events — samples

<div class="st-sub">Photon energy predicted from the two lepton directions; read in every converted event of every year, not in the <LaTeX formula="\tau" /> skim.</div>

<table class="num first-nw">
<thead><tr><th>Year</th><th><LaTeX formula="\sqrt{s}" /> points [GeV]</th><th>Luminosity [<LaTeX formula="\mathrm{pb}^{-1}" />]</th><th>Data events read</th><th>Bhabha sim. events</th><th><LaTeX formula="Z\to\mu\mu" /> sim. events</th></tr></thead>
<tbody>
<tr><td>1992</td><td>91.28</td><td>24.04</td><td>518,468</td><td>2,012,397</td><td>320,399</td></tr>
<tr><td>1993</td><td>89.43 / 91.22 / 93.02</td><td>9.67 / 16.45 / 9.99</td><td>567,433</td><td>2,978,098</td><td>325,799</td></tr>
<tr><td>1994</td><td>91.20</td><td>45.79</td><td>792,322</td><td>3,920,397</td><td>613,800</td></tr>
<tr><td>1995</td><td>89.44 / 91.30 / 92.97</td><td>8.45 / 13.78 / 9.32</td><td>433,488</td><td>2,595,593</td><td>281,700</td></tr>
</tbody>
</table>


<div class="st-cols st-cols-3" style="margin-top:10px">
<div class="co ok"><b>Data</b> <span class="tag data">data</span> Converted leptonic long-DST streams after the good-run selection.</div>
<div class="co ok"><b>Signal</b> <span class="tag sim">sim</span> Bhabha (includes <LaTeX formula="Z\to ee" />) for <LaTeX formula="ee\gamma" />; <LaTeX formula="Z\to\mu\mu" /> for <LaTeX formula="\mu\mu\gamma" />. Background: <LaTeX formula="Z\to\tau\tau" />, <LaTeX formula="Z\to q\bar q" />, two-photon.</div>
<div class="co open"><b>Caveats</b> Luminosity uncertified. Stream preselection acts on data only; its <LaTeX formula="\ell\ell\gamma" /> efficiency is unchecked.</div>
</div>

<div class="st-source">Source: per-year sample configurations of the analysis framework and the <LaTeX formula="\ell^+\ell^-\gamma" /> selection note (2026-11-03); count table of the first <LaTeX formula="\ell^+\ell^-\gamma" /> run</div>

<!--
Points and luminosities: tau_analysis/configs/1992.yaml ... 1995.yaml (points.ecm_gev, lumi_pb; DELPHI SATLUM92/SATLUM93/STILUM94/STILUM95 status 0 + RUNQUALI rule, good-cassette sums, uncertified): 1992_91p2 91.278 GeV 24.038755 pb-1; 1993_89p4 89.43234 / 9.672698, 1993_91p2 91.223296 / 16.454999, 1993_93p0 93.015116 / 9.993902; 1994_91p2 91.202 / 45.790648 (pending trigger certification); 1995_89p4 89.43761 / 8.447493, 1995_91p2 91.295352 / 13.78162, 1995_93p0 92.96528 / 9.324159. Display: sqrt(s) 2 decimals, luminosity 2 decimals. Event counts: Run llgamma-20261103: NERSC /pscratch/sd/a/avencast/Ztautau/analysis-runs/1992_1993_1994_1995/llgamma-20261103, jobs 60745549 + resume 60745978 (job ids from the coordinator brief of 2026-11-03), tau_analysis db00c4a (configs/analysis_llgamma.yaml, configs/plotting_llgamma.yaml) and 9c787d7 (finalize: confusion matrix n/a); local copy artifacts/llgamma-selection-20261103/ (cutflows/cutflow.csv sha256 258d18b94b34913628262fda4fe8c5f19e2548186f0f0cea6c4039d83911d1fb, agreement_table.json, plots/, plots-by-region/<region>/rates-by-group.md), kind cumulative, region llg_presel, cut 'input' (data after the run selection; MC raw n summed over points): data 518,468 / 567,433 / 792,322 / 433,488 (= 2,311,711, the run-quality total); Bhabha 2,012,397 / 2,978,098 / 3,920,397 / 2,595,593; Z_mumu 320,399 / 325,799 / 613,800 / 281,700. Also read: Z_ee, Z_qq, Z_tautau, yy_ll, yy_qq. tau_analysis/docs/LLGAMMA_SELECTION_20261103.md section 1: data = converted leptonic longDST streams lolept92_e2, lolept93_d2, lolept94_c2, lolept95_d2 (334 files, 2,395,361 events before run selection); every MC process converted event is processed; the tau ML skim is a separate downstream product not read here; caveat: DELPHI leptonic-stream preselection applies to data only, its l+l-gamma efficiency not inspected. Z_ee excluded from the stacks: BHWIDE Bhabha contains the s-channel, the samples overlap (docs/agent/DEVELOPMENT.md). Analysis inputs: TAU_PREPARED_INPUTS=/pscratch/sd/a/avencast/Ztautau/analysis-inputs/all_years-20261026.
-->
