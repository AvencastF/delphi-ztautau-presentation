---
class: st pres
---

# Appendix · photon calibration: full cutflow 1994, channels (v1)

<div class="st-sub">Cumulative from the preselection; side-0 and side-1 regions start again from the channel result and are disjoint.</div>

<div class="st-cols st-cols-2">
<table class="xs num first-nw">
<thead><tr><th>After cut</th><th>Bhabha sim.</th><th>Data</th></tr></thead>
<tbody>
<tr><td><span class="id">eeg: id_ee</span></td><td>27,642</td><td>24,565</td></tr>
<tr><td><span class="id">eeg: eop_hemi0</span></td><td>25,535</td><td>22,968</td></tr>
<tr><td><span class="id">eeg: eop_hemi1</span></td><td>23,893</td><td>21,690</td></tr>
<tr><td><span class="id">eeg: one_photon_candidate</span></td><td>2,633</td><td>2,466</td></tr>
<tr><td><span class="id">eeg: one_resolved_photon</span></td><td>1,584</td><td>1,484</td></tr>
<tr><td><span class="id">eeg: photon_energy</span></td><td>801.6</td><td>757</td></tr>
<tr><td><span class="id">eeg_gh0: photon_hemi0</span></td><td>405.9</td><td>372</td></tr>
<tr><td><span class="id">eeg_gh0: photon_barrel_hemi0</span></td><td>395.6</td><td>365</td></tr>
<tr><td><span class="id">eeg_gh0: photon_off_crack_hemi0</span></td><td>391.6</td><td>362</td></tr>
<tr><td><span class="id">eeg_gh0: photon_isolated_hemi0</span></td><td>131.8</td><td>120</td></tr>
<tr><td><span class="id">eeg_gh1: photon_hemi1</span></td><td>395.7</td><td>385</td></tr>
<tr><td><span class="id">eeg_gh1: photon_barrel_hemi1</span></td><td>388.5</td><td>380</td></tr>
<tr><td><span class="id">eeg_gh1: photon_off_crack_hemi1</span></td><td>384.8</td><td>380</td></tr>
<tr><td><span class="id">eeg_gh1: photon_isolated_hemi1</span></td><td>127.0</td><td>109</td></tr>
</tbody>
</table>

<table class="xs num first-nw">
<thead><tr><th>After cut</th><th><LaTeX formula="Z\to\mu\mu" /> sim.</th><th>Data</th></tr></thead>
<tbody>
<tr><td><span class="id">mumug: id_mumu</span></td><td>34,771</td><td>33,596</td></tr>
<tr><td><span class="id">mumug: one_photon_candidate</span></td><td>3,629</td><td>3,424</td></tr>
<tr><td><span class="id">mumug: one_resolved_photon</span></td><td>2,475</td><td>2,332</td></tr>
<tr><td><span class="id">mumug: photon_energy</span></td><td>1,180</td><td>1,182</td></tr>
<tr><td><span class="id">mumug_gh0: photon_hemi0</span></td><td>591.8</td><td>571</td></tr>
<tr><td><span class="id">mumug_gh0: photon_barrel_hemi0</span></td><td>579.0</td><td>565</td></tr>
<tr><td><span class="id">mumug_gh0: photon_off_crack_hemi0</span></td><td>572.1</td><td>558</td></tr>
<tr><td><span class="id">mumug_gh0: photon_isolated_hemi0</span></td><td>189.8</td><td>199</td></tr>
<tr><td><span class="id">mumug_gh1: photon_hemi1</span></td><td>588.5</td><td>611</td></tr>
<tr><td><span class="id">mumug_gh1: photon_barrel_hemi1</span></td><td>577.6</td><td>595</td></tr>
<tr><td><span class="id">mumug_gh1: photon_off_crack_hemi1</span></td><td>569.7</td><td>586</td></tr>
<tr><td><span class="id">mumug_gh1: photon_isolated_hemi1</span></td><td>190.4</td><td>206</td></tr>
</tbody>
</table>

</div>

<div class="st-source">Source: count table of the first <LaTeX formula="\ell^+\ell^-\gamma" /> run (1994, selection v1)</div>

<!--
Run llgamma-20261103: NERSC /pscratch/sd/a/avencast/Ztautau/analysis-runs/1992_1993_1994_1995/llgamma-20261103, jobs 60745549 + resume 60745978 (job ids from the coordinator brief of 2026-11-03), tau_analysis db00c4a (configs/analysis_llgamma.yaml, configs/plotting_llgamma.yaml) and 9c787d7 (finalize: confusion matrix n/a); local copy artifacts/llgamma-selection-20261103/ (cutflows/cutflow.csv sha256 258d18b94b34913628262fda4fe8c5f19e2548186f0f0cea6c4039d83911d1fb, agreement_table.json, plots/, plots-by-region/<region>/rates-by-group.md). cutflow.csv kind cumulative, regions llg_eeg, llg_eeg_gh0, llg_eeg_gh1 (sample 1994/Bhabha/1994_91p2, sumw) and llg_mumug, llg_mumug_gh0, llg_mumug_gh1 (1994/Z_mumu/1994_91p2, sumw), data 1994 n. Region input rows omitted (equal to the parent's last row: llg_presel visible_energy for eeg/mumug; photon_energy for the gh regions).
-->
