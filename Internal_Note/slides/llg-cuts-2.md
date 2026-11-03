---
class: st pres
---

# Calibration 2: selection v1, lepton ID and photon (cuts 13–22)

<div class="st-sub"><b>Resolved-HPC working point</b>: stored shower-profile code 1, 11 or 61; not a conversion, merged <LaTeX formula="\pi^0" /> or secondary; HPC energy <LaTeX formula="\gt0.5" /> GeV. Unknown codes make the event unusable, never zero photons.</div>

<table class="first-nw">
<thead><tr><th>#</th><th>Cut</th><th>Requirement</th><th>Meaning</th></tr></thead>
<tbody>
<tr><td>13</td><td>Lepton pair</td><td><LaTeX formula="ee" />: ELID <LaTeX formula="\ge3" />, no MUID <LaTeX formula="\ge7" />; <LaTeX formula="\mu\mu" />: MUID <LaTeX formula="\ge7" />, no ELID <LaTeX formula="\ge3" /></td><td>frozen DELPHI tags, both legs</td></tr>
<tr><td>14–15</td><td>Electron <LaTeX formula="E/p" /> (<LaTeX formula="ee" /> only)</td><td><LaTeX formula="\ge0.6" /> both</td><td>linked HPC energy over momentum; no shower fails</td></tr>
<tr><td>16</td><td>One photon candidate</td><td><LaTeX formula="=1" /></td><td>tagged neutral with its own HPC shower, any energy</td></tr>
<tr><td>17</td><td>Resolved photon</td><td><LaTeX formula="=1" /></td><td>it passes the resolved-HPC working point</td></tr>
<tr><td>18</td><td>Photon energy</td><td><LaTeX formula="\gt3" /> GeV</td><td>stored HPC shower energy, not calibrated</td></tr>
<tr><td>19</td><td>Photon side</td><td>side 0 or side 1</td><td>two disjoint regions, summed</td></tr>
<tr><td>20–21</td><td>Photon in barrel, off gap</td><td><LaTeX formula="0.035\lt|\cos\theta_\gamma|\lt0.72" /></td><td>as for the tracks</td></tr>
<tr><td>22</td><td>Isolation</td><td><LaTeX formula="\gt20^\circ" /></td><td>angle to the track on the same side</td></tr>
</tbody>
</table>


<div class="st-source">Source: the <LaTeX formula="\ell^+\ell^-\gamma" /> selection configuration (version 1), its selection note and the photon working-point note</div>

<!--
tau_analysis/configs/analysis_llgamma.yaml (db00c4a): region llg_eeg (parent llg_presel) cuts id_ee (exclusive_pair_ee equals 1: both legs ELID >= 3 and no MUID >= 7, exclusive_id.classify_leg), eop_hemi0 / eop_hemi1 (lead_hpc_e_over_p_hemi{0,1} min 0.6 inclusive; complement of the frozen charged-hadron clause E/p < 0.6; missing HPC shower fails; track-linked showers calibrated in 1993-95, not 1992), one_photon_candidate (photon_candidate_count equals 1: PHOT-tagged accepted neutral MAIN with uniquely owned HPC shower(s), any energy; invalid if a candidate is ambiguous), one_resolved_photon (selected_photon_count equals 1), photon_energy (photon_candidate_energy min 3 GeV; with one candidate = its stored HPC shower energy); llg_mumug: id_mumu (exclusive_pair_mumu: MUID >= 7 numeric both legs, no ELID >= 3; no momentum threshold), one_photon_candidate, one_resolved_photon, photon_energy. Grandchildren llg_<ch>_gh0/gh1: photon_hemi{h} (selected_photon_count_hemi{h} equals 1), photon_barrel_hemi{h} (photonid_candidate_max_abs_costheta_hemi{h} max 0.72), photon_off_crack_hemi{h} (same, min 0.035), photon_isolated_hemi{h} (photonid_candidate_nearest_track_angle_hemi{h} min 20 deg, to the leading track of the SAME hemisphere). Fiducial sample = gh0 + gh1 (disjoint). The photon geometry exists only per thrust hemisphere, hence the split. 'No second photon above 1 GeV' could not be expressed: cuts 16-17 are stricter (no second PHOT/HPC candidate at any energy). Working point: tau_analysis/analysis/photon_quality.py, docs/PHOTON_WORKING_POINT_20260928.md ('existing_input_resolved_hpc_v1': accepted neutral MAIN with valid PHOT record, one uniquely owned HPC shower, stored profile acceptance code 1/11/61, HPC energy > 0.5 GeV; rejection codes 6/7/8, 16/17/18, 66/67/68 fail; code -101 merged pi0 and conversions excluded; unknown codes / malformed records make the selection unavailable, never an observed zero; source/fixture checks are for 1994, other years need independent validation).
-->
