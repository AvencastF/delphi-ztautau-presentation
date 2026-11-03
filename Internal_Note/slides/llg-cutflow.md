---
class: st pres
---

# Calibration 2: cutflow, 1994 (selection v1)

<div class="st-sub">Cumulative. Simulation in expected events (luminosity-weighted); data in events. The last row sums the two photon sides. Full table in the appendix.</div>

<table class="num first-nw">
<thead><tr><th>After cuts</th><th>Bhabha sim. (<LaTeX formula="ee\gamma" /> path)</th><th>Data, <LaTeX formula="ee\gamma" /></th><th><LaTeX formula="Z\to\mu\mu" /> sim. (<LaTeX formula="\mu\mu\gamma" /> path)</th><th>Data, <LaTeX formula="\mu\mu\gamma" /></th></tr></thead>
<tbody>
<tr><td>Input</td><td>859,648</td><td>792,322</td><td>67,343</td><td>792,322</td></tr>
<tr><td>Two tracks, one per side, opposite charge (1–3)</td><td>64,208</td><td>169,551</td><td>58,828</td><td>169,551</td></tr>
<tr><td>Tracks in barrel, off the gap (4–5)</td><td>42,384</td><td>109,262</td><td>38,702</td><td>109,262</td></tr>
<tr><td>Origin, momenta, visible energy (6–12)</td><td>32,138</td><td>69,194</td><td>38,035</td><td>69,194</td></tr>
<tr><td>Lepton identification (13; 14–15 for <LaTeX formula="ee" />)</td><td>23,893</td><td>21,690</td><td>34,771</td><td>33,596</td></tr>
<tr><td>One candidate, resolved, <LaTeX formula="E_\gamma\gt3" /> GeV (16–18)</td><td>801.6</td><td>757</td><td>1,180.3</td><td>1,182</td></tr>
<tr class="hl"><td>Photon in barrel, off gap, isolated (19–22)</td><td>258.8</td><td>229</td><td>380.2</td><td>405</td></tr>
</tbody>
</table>


<div class="st-cols st-cols-2" style="margin-top:10px">
<div class="co warn"><b>Largest loss</b> Exactly one photon candidate: 11 % of Bhabha and 10 % of <LaTeX formula="Z\to\mu\mu" /> events keep it.</div>
<div class="co ok"><b>Cross-channel</b> No Bhabha event in <LaTeX formula="\mu\mu\gamma" />, no <LaTeX formula="Z\to\mu\mu" /> event in <LaTeX formula="ee\gamma" />.</div>
</div>

<div class="st-source">Source: count table of the first <LaTeX formula="\ell^+\ell^-\gamma" /> run (1994 point, selection v1)</div>

<!--
Run llgamma-20261103: NERSC /pscratch/sd/a/avencast/Ztautau/analysis-runs/1992_1993_1994_1995/llgamma-20261103, jobs 60745549 + resume 60745978 (job ids from the coordinator brief of 2026-11-03), tau_analysis db00c4a (configs/analysis_llgamma.yaml, configs/plotting_llgamma.yaml) and 9c787d7 (finalize: confusion matrix n/a); local copy artifacts/llgamma-selection-20261103/ (cutflows/cutflow.csv sha256 258d18b94b34913628262fda4fe8c5f19e2548186f0f0cea6c4039d83911d1fb, agreement_table.json, plots/, plots-by-region/<region>/rates-by-group.md). cutflow.csv kind cumulative, samples 1994/Bhabha/1994_91p2, 1994/Z_mumu/1994_91p2, 1994/data; sumw shown for MC (display: integers above 1000, one decimal below), n for data. Exact: Bhabha input 3,920,397 rows / 859,647.782; opposite_charge 732,325 / 64,208.343; tracks_off_crack 553,207 / 42,383.698; visible_energy 388,785 / 32,138.060; eop_hemi1 286,828 / 23,892.970; one_photon_candidate 33,853 / 2,633.369; one_resolved_photon 21,231 / 1,583.555; photon_energy 11,911 / 801.600; gh0 isolated 2,026 / 131.764 + gh1 1,979 / 127.016 = 258.780 (derived sum). Z_mumu input 613,800 / 67,342.990; opposite_charge 536,191 / 58,828.128; tracks_off_crack 352,750 / 38,701.922; visible_energy 346,669 / 38,034.746; id_mumu 316,925 / 34,771.387; one_photon_candidate 33,079 / 3,629.258; one_resolved_photon 22,554 / 2,474.509; photon_energy 10,758 / 1,180.313; gh0 1,730 / 189.807 + gh1 1,735 / 190.355 = 380.162 (derived). Data 1994: input 792,322; opposite_charge 169,551; tracks_off_crack 109,262; visible_energy 69,194; ee: eop_hemi1 21,690, one_photon_candidate 2,466, one_resolved_photon 1,484, photon_energy 757, gh0 120 + gh1 109 = 229; mumu: id_mumu 33,596, one candidate 3,424, resolved 2,332, photon_energy 1,182, gh0 199 + gh1 206 = 405. Derived fractions: Bhabha one_photon_candidate / eop_hemi1 = 2,633.369 / 23,892.970 = 0.110; Z_mumu 3,629.258 / 34,771.387 = 0.104. Bhabha in llg_mumug and Z_mumu in llg_eeg: 0 rows after the ID cut.
-->
