---
class: st pres
---

# Calibration 2: selection v1, preselection (cuts 1–12)

<div class="st-sub">Region <span class="id">llg_presel</span>, same for both channels. HPC = barrel electromagnetic calorimeter. Every threshold is a proposed working value, not tuned.</div>

<table class="first-nw">
<thead><tr><th>#</th><th>Cut</th><th>Requirement</th><th>Meaning</th></tr></thead>
<tbody>
<tr><td>1</td><td>Two good tracks</td><td><LaTeX formula="=2" /></td><td>accepted charged tracks</td></tr>
<tr><td>2</td><td>One track per side</td><td>true</td><td>both thrust hemispheres hold a track</td></tr>
<tr><td>3</td><td>Opposite charge</td><td>true</td><td>the two leading tracks</td></tr>
<tr><td>4</td><td>Tracks in the barrel</td><td><LaTeX formula="|\cos\theta|_\mathrm{max}\lt0.72" /></td><td>both tracks in the HPC barrel</td></tr>
<tr><td>5</td><td>Tracks off the <LaTeX formula="90^\circ" /> gap</td><td><LaTeX formula="|\cos\theta|_\mathrm{min}\gt0.035" /></td><td>HPC gap at <LaTeX formula="\theta=90^\circ" /></td></tr>
<tr><td>6–9</td><td>Track origin</td><td><LaTeX formula="|z_0|\lt45,\ |d_0|\lt15,\ |d_0|_\mathrm{min}\lt3,\ \Delta z_0\lt30" /> mm</td><td><LaTeX formula="\tau" />-selection values; cosmics, beam gas</td></tr>
<tr><td>10–11</td><td>Track momenta</td><td><LaTeX formula="p/p_\mathrm{beam}\gt0.33" /> both</td><td>about 15 GeV; removes <LaTeX formula="\tau\tau" />, two-photon</td></tr>
<tr><td>12</td><td>Visible energy</td><td><LaTeX formula="E_\mathrm{vis}/\sqrt{s}\gt0.8" /></td><td>full-energy three-body state; removes <LaTeX formula="\tau\tau" />, two-photon, beam-axis radiation</td></tr>
</tbody>
</table>


<div class="st-source">Source: the <LaTeX formula="\ell^+\ell^-\gamma" /> selection configuration (version 1) and its selection note (2026-11-03)</div>

<!--
tau_analysis/configs/analysis_llgamma.yaml (commit db00c4a), selection.cuts, region llg_presel (parent input), in this order: two_tracks ncharged equals 2; hemispheres equals 1; opposite_charge os equals 1; barrel_tracks lead_abs_costheta_max max 0.72 (owner value ~0.72); tracks_off_crack lead_abs_costheta_min min 0.035 (lower edge of the paper electron acceptance, docs/DELPHI_POLARISATION_SELECTION.md); z_origin lead_abs_z0_max max 45; d_origin lead_abs_d0_max max 15; one_close lead_abs_d0_min max 3; relative_z delta_z0 max 30 (mm, beam-spot impact parameters, invalid if beam-spot error code != 0); p_hemi0 / p_hemi1 leadtrack_hemi{0,1}_p_over_pbeam min 0.33 (0.33 p_beam = 15.0 GeV at 91.2, 14.8 at 89.4, 15.3 at 93.0 GeV); visible_energy evis_over_ecm min 0.8 (charged MAIN energy + EM showers not linked to a charged MAIN, / sqrt(s)). Thrust axis from charged tracks only. A cut fails when its variable is invalid (missing is never zero). calibration: true (raw-row calibration: data sqrt(s), track momenta, track-linked HPC showers; neutral photon showers not modified). save_all_signal false. tau_analysis/docs/LLGAMMA_SELECTION_20261103.md sections 2-3; 'Every threshold below is a proposed working value; none has been tuned'. No coplanarity variable exists, so no coplanarity cut.
-->
