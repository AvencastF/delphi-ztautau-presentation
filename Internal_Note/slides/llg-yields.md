---
class: st pres
---

# Calibration 2: final yields per year and purity (selection v1)

<div class="st-sub">Fiducial samples (photon on either side). Simulation: signal process plus <LaTeX formula="Z\to\tau\tau" />, luminosity-weighted.</div>

<table class="num first-nw">
<thead><tr><th>Year</th><th><LaTeX formula="ee\gamma" /> data / sim.</th><th>Ratio</th><th><LaTeX formula="\mu\mu\gamma" /> data / sim.</th><th>Ratio</th><th><LaTeX formula="Z\to\tau\tau" /> in sim.: <LaTeX formula="ee\gamma" /> / <LaTeX formula="\mu\mu\gamma" /></th></tr></thead>
<tbody>
<tr><td>1992</td><td>101 / 128.4</td><td><LaTeX formula="0.787\pm0.082" /></td><td>191 / 194.5</td><td><LaTeX formula="0.982\pm0.075" /></td><td>0.023 / 0.070</td></tr>
<tr><td>1993</td><td>148 / 140.3</td><td><LaTeX formula="1.055\pm0.092" /></td><td>223 / 211.3</td><td><LaTeX formula="1.055\pm0.075" /></td><td>0.035 / 0.047</td></tr>
<tr><td>1994</td><td>229 / 258.8</td><td><LaTeX formula="0.885\pm0.061" /></td><td>405 / 380.3</td><td><LaTeX formula="1.065\pm0.056" /></td><td>0.059 / 0.129</td></tr>
<tr><td>1995</td><td>121 / 135.1</td><td><LaTeX formula="0.896\pm0.086" /></td><td>161 / 187.3</td><td><LaTeX formula="0.859\pm0.071" /></td><td>0.012 / 0.012</td></tr>
<tr class="hl"><td>All</td><td>599 / 662.6</td><td><LaTeX formula="0.904\pm0.039" /></td><td>980 / 973.4</td><td><LaTeX formula="1.007\pm0.034" /></td><td>0.129 / 0.258</td></tr>
</tbody>
</table>


<div class="st-cols st-cols-2" style="margin-top:10px">
<div class="co ok"><b>Purity</b> <span class="tag sim">sim</span> <LaTeX formula="Z\to\tau\tau" /> below 0.1 % in every year and channel; <LaTeX formula="Z\to q\bar q" />, two-photon and cross-channel: zero events.</div>
<div class="co warn"><b>Rates</b> <LaTeX formula="ee\gamma" /> data below simulation in 1992, 1994, 1995; luminosity uncertified, not a calibration input.</div>
</div>

<div class="st-source">Source: count table of the first <LaTeX formula="\ell^+\ell^-\gamma" /> run (selection v1); ratios from the rate table of the identical version-2 sample</div>

<!--
Run llgamma-20261103: NERSC /pscratch/sd/a/avencast/Ztautau/analysis-runs/1992_1993_1994_1995/llgamma-20261103, jobs 60745549 + resume 60745978 (job ids from the coordinator brief of 2026-11-03), tau_analysis db00c4a (configs/analysis_llgamma.yaml, configs/plotting_llgamma.yaml) and 9c787d7 (finalize: confusion matrix n/a); local copy artifacts/llgamma-selection-20261103/ (cutflows/cutflow.csv sha256 258d18b94b34913628262fda4fe8c5f19e2548186f0f0cea6c4039d83911d1fb, agreement_table.json, plots/, plots-by-region/<region>/rates-by-group.md). Data and MC = sums over gh0 + gh1 of the last cumulative cutflow row (derived sums), MC = Bhabha + Z_tautau (eeg) or Z_mumu + Z_tautau (mumug), signed sumw, Z_ee excluded (Z_ee sumw in the eeg fiducial sample, not stacked: 103.91 / 113.39 / 220.70 / 106.59). Exact: eeg 1992 101 / 128.3734 (Bhabha 128.3500 + tautau 0.0234), 1993 148 / 140.2617 (0.0353), 1994 229 / 258.8384 (0.0585), 1995 121 / 135.1153 (0.0118); mumug 1992 191 / 194.4699 (Z_mumu 194.3996 + tautau 0.0703), 1993 223 / 211.3334 (0.0470), 1994 405 / 380.2906 (0.1286), 1995 161 / 187.3421 (0.0118). Z_tautau share max 0.0703/194.47 = 0.036 % (derived). Z_qq, yy_ll, yy_qq: 0 rows in llg_eeg and llg_mumug in every year; Bhabha in mumug and Z_mumu in eeg: 0. Ratios +- stat: artifacts/llgamma-v2-20261103/tables/yields.md, region llg_eeg_iso20 / llg_mumug_iso20 (the v2 counterpart of the v1 fiducial sample, isolation to the nearer of both tracks; same data and MC yields to the shown precision). v1 per-hemisphere rates: plots-by-region/llg_<ch>_gh{0,1}/rates-by-group.md (e.g. llg_eeg_gh0 all 310 / 333.4442, gh1 289 / 329.14463; llg_mumug_gh0 477 / 487.42319, gh1 503 / 486.01285). Parent regions llg_eeg / llg_mumug all years 1990 / 2042.9578 (0.974 +- 0.023) and 2824 / 2872.9854 (0.983 +- 0.019).
-->
