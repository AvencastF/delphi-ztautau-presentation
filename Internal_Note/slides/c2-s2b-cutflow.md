---
class: st pres c2
---

# Calibration 2 · Step 2b: cutflow, 1994

<div class="st-sub">Cumulative, final selection. Simulation in expected events (luminosity-weighted, signal process only); data in events.</div>

<table class="c2t num first-nw">
<thead><tr><th>After cuts</th><th>Bhabha sim.</th><th>Data, <LaTeX formula="ee\gamma" /></th><th><LaTeX formula="Z\to\mu\mu" /> sim.</th><th>Data, <LaTeX formula="\mu\mu\gamma" /></th></tr></thead>
<tbody>
<tr><td>Input</td><td>859,648</td><td>792,322</td><td>67,343</td><td>792,322</td></tr>
<tr><td>Two tracks, one per side, opposite charge (1)</td><td>64,208</td><td>169,551</td><td>58,828</td><td>169,551</td></tr>
<tr><td>Barrel, origin, momenta, visible energy (2–5)</td><td>32,138</td><td>69,194</td><td>38,035</td><td>69,194</td></tr>
<tr><td>Lepton identification (6)</td><td>23,893</td><td>21,690</td><td>34,771</td><td>33,596</td></tr>
<tr><td>One resolved photon in the barrel (7–8)</td><td>1,624</td><td>1,553</td><td>2,503</td><td>2,396</td></tr>
<tr><td>No other candidate (9)</td><td>1,528</td><td>1,445</td><td>2,393</td><td>2,261</td></tr>
<tr><td><LaTeX formula="E_\gamma\gt3" /> GeV (10)</td><td>776.4</td><td>742</td><td>1,142</td><td>1,144</td></tr>
<tr class="hl"><td>Isolation <LaTeX formula="\ge5^\circ" /> (11)</td><td>502.8</td><td>477</td><td>750.0</td><td>762</td></tr>
</tbody>
</table>

<div class="st-cols st-cols-2" style="margin-top:8px">
<div class="co warn"><b>Largest loss</b> Exactly one resolved photon: 7 % of the identified pairs keep it.</div>
<div class="co ok"><b>Cross-channel</b> No Bhabha event in <LaTeX formula="\mu\mu\gamma" />, no <LaTeX formula="Z\to\mu\mu" /> event in <LaTeX formula="ee\gamma" />.</div>
</div>

<div class="takeaway"><b>Takeaway</b> After the lepton identification, data follow the simulation at every photon cut; 1994 ends with 477 <LaTeX formula="ee\gamma" /> (502.8 expected) and 762 <LaTeX formula="\mu\mu\gamma" /> (750.0).</div>

<div class="st-source">Source: count table of the version-2 <LaTeX formula="\ell^+\ell^-\gamma" /> run (1994 point); full version-1 cutflow in the appendix</div>

<!--
artifacts/llgamma-v2-20261103/cutflows/cutflow.csv (run llgamma-v2-20261103, job 60747968, tau_analysis 5ac249d), kind cumulative, samples 1994/Bhabha/1994_91p2, 1994/Z_mumu/1994_91p2, 1994/data; MC sumw (display: integers above 1000, one decimal below), data n. Exact: Bhabha llg_presel_wide input 859,647.8 / opposite_charge 64,208.3 / llg_presel barrel_tracks 32,138.1; llg_eeg eop_hemi1 23,892.97, photon_off_crack 1,624.38; llg_eeg_iso5 one_photon_candidate 1,528.45, photon_e3 776.43, photon_iso5 502.76. Z_mumu input 67,343.0 / opposite_charge 58,828.1 / barrel_tracks 38,034.7; llg_mumug id_mumu 34,771.39, photon_off_crack 2,503.25; iso5 one_photon_candidate 2,392.77, photon_e3 1,141.80, photon_iso5 750.01. Data: input 792,322; opposite_charge 169,551; barrel_tracks 69,194; ee eop_hemi1 21,690, off_crack 1,553, one candidate 1,445, e3 742, iso5 477; mumu id 33,596, off_crack 2,396, one candidate 2,261, e3 1,144, iso5 762. Row 3 groups tracks_wide, tracks_off_crack, z_origin, d_origin, one_close, relative_z, p_hemi0/1, visible_energy (llg_presel_wide) and barrel_tracks (llg_presel). Derived fraction one resolved photon in barrel / identified: Bhabha 1,624.38 / 23,892.97 = 0.068, Z_mumu 2,503.25 / 34,771.39 = 0.072 (row "7 %"). Bhabha in llg_mumug and Z_mumu in llg_eeg: 0 after the ID cut (sumw 0.0). The "Input" data row is the same for both channels (one data stream per year). Before lepton identification data exceed Bhabha+Z_mumu because the other processes (Z_tautau, Z_qq, two-photon, Z_ee) are not shown.
-->
