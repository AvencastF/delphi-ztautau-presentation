---
class: st pres c2
---

# Calibration 2 · Step 2a: selection — two barrel leptons and one isolated photon

<div class="st-sub">Final selection (version 2, isolation <LaTeX formula="\ge5^\circ" />), identical for all years. HPC = barrel electromagnetic calorimeter. Thresholds are working values.</div>

<table class="c2t first-nw">
<thead><tr><th>#</th><th>Cut</th><th>Requirement</th><th>Purpose</th></tr></thead>
<tbody>
<tr><td>1</td><td>Two tracks, one per side, opposite charge</td><td><LaTeX formula="=2" />; true; true</td><td>dilepton topology</td></tr>
<tr><td>2</td><td>Tracks in the barrel, off the <LaTeX formula="90^\circ" /> gap</td><td><LaTeX formula="0.035\lt|\cos\theta|\lt0.72" /> both</td><td>both leptons in the HPC</td></tr>
<tr><td>3</td><td>Track origin</td><td><LaTeX formula="|z_0|\lt45,\ |d_0|\lt15,\ |d_0|_\mathrm{min}\lt3,\ \Delta z_0\lt30" /> mm</td><td>cosmics, beam gas</td></tr>
<tr><td>4</td><td>Track momenta</td><td><LaTeX formula="p/p_\mathrm{beam}\gt0.33" /> both</td><td>removes <LaTeX formula="\tau\tau" />, two-photon</td></tr>
<tr><td>5</td><td>Visible energy</td><td><LaTeX formula="E_\mathrm{vis}/\sqrt{s}\gt0.8" /></td><td>no radiation lost along the beam</td></tr>
<tr><td>6</td><td>Lepton identification</td><td><LaTeX formula="ee" />: ELID <LaTeX formula="\ge3" />, no MUID <LaTeX formula="\ge7" />, <LaTeX formula="E/p\ge0.6" />; <LaTeX formula="\mu\mu" />: MUID <LaTeX formula="\ge7" />, no ELID <LaTeX formula="\ge3" /></td><td>channel, both legs</td></tr>
<tr><td>7</td><td>One resolved photon</td><td><LaTeX formula="=1" /> passing the resolved-HPC working point</td><td>single clean shower</td></tr>
<tr><td>8</td><td>Photon in the barrel, off the gap</td><td><LaTeX formula="0.035\lt|\cos\theta_\gamma|\lt0.72" /></td><td>as for the tracks</td></tr>
<tr><td>9</td><td>No other photon candidate</td><td>at any energy</td><td>one photon only</td></tr>
<tr><td>10</td><td>Photon energy</td><td><LaTeX formula="E_\gamma\gt3" /> GeV, stored, uncalibrated</td><td>above the low-energy region</td></tr>
<tr class="hl"><td>11</td><td>Isolation</td><td><LaTeX formula="\ge5^\circ" /> to the nearer track</td><td>photon not merged with a lepton</td></tr>
</tbody>
</table>

<style>
.c2t td, .c2t th { padding: 2.5px 8px !important; }
</style>

<div class="co ok" style="margin-top:6px"><b>Cut choice</b> Isolation <LaTeX formula="20^\circ" />–<LaTeX formula="5^\circ" /> and thresholds 1.5–3 GeV were run; <LaTeX formula="k" /> is flat against both (step 4), so the loosest isolation is used.</div>

<div class="takeaway"><b>Takeaway</b> Two identified barrel leptons plus exactly one isolated barrel photon above 3 GeV; the loosest isolation, <LaTeX formula="5^\circ" />, keeps the most events without changing <LaTeX formula="k" />.</div>

<div class="st-source">Source: the <LaTeX formula="\ell^+\ell^-\gamma" /> selection configuration (version 2), its selection note and the photon working-point note</div>

<!--
tau_analysis/configs/analysis_llgamma_v2.yaml (5ac249d), regions llg_presel_wide -> llg_presel -> llg_<ch> -> llg_<ch>_iso5. Cuts in config order: two_tracks ncharged equals 2; hemispheres equals 1; opposite_charge os equals 1; tracks_wide lead_abs_costheta_max max 0.9; tracks_off_crack lead_abs_costheta_min min 0.035; z_origin lead_abs_z0_max max 45; d_origin lead_abs_d0_max max 15; one_close lead_abs_d0_min max 3; relative_z delta_z0 max 30 (mm, beam-spot impact parameters); p_hemi0/p_hemi1 leadtrack_hemi{0,1}_p_over_pbeam min 0.33 (about 15 GeV); visible_energy evis_over_ecm min 0.8; barrel_tracks lead_abs_costheta_max max 0.72 (applied last in llg_presel; row 2 of the slide combines tracks_wide, tracks_off_crack and barrel_tracks). llg_eeg: id_ee (exclusive_pair_ee: both legs ELID >= 3 and no MUID >= 7), eop_hemi0 / eop_hemi1 (lead_hpc_e_over_p min 0.6 inclusive), one_resolved_photon (selected_photon_count equals 1), photon_barrel (single_photon_abs_costheta max 0.72), photon_off_crack (min 0.035). llg_mumug: id_mumu (MUID >= 7 both, no ELID >= 3), one_resolved_photon, photon_barrel, photon_off_crack. llg_<ch>_iso5: one_photon_candidate (photon_candidate_count equals 1: no other PHOT/HPC candidate at any energy), photon_e3 (single_photon_energy min 3), photon_iso5 (single_photon_track_angle_min min 5 inclusive: angle to the nearer of both leading tracks). Resolved-HPC working point (tau_analysis/analysis/photon_quality.py, docs/PHOTON_WORKING_POINT_20260928.md, existing_input_resolved_hpc_v1): accepted neutral MAIN with valid PHOT record, one uniquely owned HPC shower, profile code 1/11/61, not conversion / merged pi0 (-101) / secondary, HPC energy > 0.5 GeV; unknown codes make the event unusable, never zero photons. Photon energy = stored EMNC shower energy (raw-row calibration scales only track-linked showers). Cut choice: owner decision 2026-11-03 after llgamma-20261103 (samples pure, angle well modelled down to 0-5 deg, threshold can be lowered); variants iso20/15/10/5 and iso10 with E > 2 / 1.5 GeV in the same run; REPORT.md section 3: exclusive angle slices consistent with a constant (all years p = 0.21 eeg, 0.64 mumug), threshold 3 -> 1.5 GeV moves the all-years ratio by <= 0.006 / 0.004; below 3 GeV the selected R peaks at 0.74-0.82 (threshold bias), so the 3 GeV cut is kept. Variant yields: appendix slide "isolation and threshold variants". Leg E/p in data uses track-linked showers calibrated in 1993-1995 (not 1992).
-->
