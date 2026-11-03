---
class: st pres
---

# Appendix · photon calibration: selection variants (step 2a)

<div class="st-sub">Same preselection and lepton identification. New event-level photon variables remove the side split; isolation is now to the nearer of both tracks. One run, all variants.</div>

<table class="num first-nw">
<thead><tr><th>Variant (each also: one candidate, <LaTeX formula="E_\gamma\gt3" /> GeV unless stated)</th><th><LaTeX formula="ee\gamma" /> data / sim. (ratio)</th><th><LaTeX formula="\mu\mu\gamma" /> data / sim. (ratio)</th></tr></thead>
<tbody>
<tr><td>Isolation <LaTeX formula="\ge20^\circ" /></td><td>599 / 662.6 (0.904)</td><td>980 / 973.4 (1.007)</td></tr>
<tr><td>Isolation <LaTeX formula="\ge15^\circ" /></td><td>732 / 783.1 (0.935)</td><td>1,144 / 1,152.3 (0.993)</td></tr>
<tr><td>Isolation <LaTeX formula="\ge10^\circ" /></td><td>904 / 958.8 (0.943)</td><td>1,412 / 1,418.0 (0.996)</td></tr>
<tr class="hl"><td>Isolation <LaTeX formula="\ge5^\circ" /></td><td>1,236 / 1,277.1 (0.968)</td><td>1,861 / 1,881.2 (0.989)</td></tr>
<tr><td><LaTeX formula="\ge10^\circ" />, <LaTeX formula="E_\gamma\gt2" /> GeV</td><td>1,114 / 1,168.3 (0.954)</td><td>1,705 / 1,728.5 (0.986)</td></tr>
<tr><td><LaTeX formula="\ge10^\circ" />, <LaTeX formula="E_\gamma\gt1.5" /> GeV</td><td>1,244 / 1,322.5 (0.941)</td><td>1,922 / 1,962.1 (0.980)</td></tr>
<tr><td><LaTeX formula="\ge10^\circ" />, tracks <LaTeX formula="|\cos\theta|\lt0.9" /></td><td>—</td><td>1,794 / 1,833.2 (0.979)</td></tr>
</tbody>
</table>
<div class="st-cap">All years; ratio statistical errors 0.024–0.039 (all in SOURCES). A further variant keeps events whose other candidates are all below 1 GeV.</div>

<div class="st-cols st-cols-2" style="margin-top:8px">
<div class="kv sel"><h3>Photon variables (exactly one resolved photon)</h3><dl>
<dt>Energy</dt><dd>stored HPC shower, uncalibrated</dd>
<dt>Direction</dt><dd><LaTeX formula="|\cos\theta_\gamma|" /> in <LaTeX formula="(0.035,0.72)" />, <LaTeX formula="\phi_\gamma" /></dd>
<dt>Module distance</dt><dd>to the nearest <LaTeX formula="15^\circ" /> HPC boundary</dd>
</dl></div>
<div class="kv sel"><dl>
<dt>Isolation</dt><dd>angle to the nearer track</dd>
<dt>Prediction</dt><dd><LaTeX formula="E_\mathrm{pred}" /> and <LaTeX formula="R=E_\mathrm{HPC}/E_\mathrm{pred}" /></dd>
<dt>Second candidate</dt><dd>highest other HPC energy</dd>
</dl></div>
</div>

<div class="st-source">Source: the <LaTeX formula="\ell^+\ell^-\gamma" /> selection configuration (version 2), its selection note (section 9) and the yield table of the version-2 run</div>

<!--
tau_analysis/configs/analysis_llgamma_v2.yaml (5ac249d), 20 regions: llg_presel_wide (v1 presel with lead_abs_costheta_max < 0.9, defines the saved skim) -> llg_presel (+ barrel_tracks < 0.72, same cut set as v1, barrel cut last) -> llg_eeg (id_ee, eop_hemi0, eop_hemi1, one_resolved_photon, photon_barrel single_photon_abs_costheta max 0.72, photon_off_crack min 0.035) / llg_mumug (id_mumu, one_resolved_photon, photon_barrel, photon_off_crack); children llg_<ch>_iso20/15/10/5 (one_photon_candidate, photon_e3 single_photon_energy min 3, photon_isoNN single_photon_track_angle_min min NN inclusive), _iso10_e2 / _iso10_e1p5 (photon_e2 / photon_e1p5, iso10), _iso10_2nd (second_below_1 single_photon_second_candidate_energy_max max 1, photon_e3, iso10; disjoint from iso10: >= 2 candidates); llg_mumug_wide (parent llg_presel_wide) and llg_mumug_wide_iso10. Variables analysis/single_photon.py: single_photon_energy, _costheta, _abs_costheta, _phi, _hpc_module_distance (hpc_boundary.distance_deg at the photon direction phi, straight line from the nominal origin), _track_angle_min, _epred, _e_over_epred, _second_candidate_energy_max; valid only with selected_photon_count == 1 and two hemisphere-leading tracks; invalid never zero. Yields: artifacts/llgamma-v2-20261103/tables/yields.md (= REPORT.md section 6; rates-by-group region_events, data events / MC weighted, ratio +- stat): eeg iso20 599/662.6 (0.904+-0.039), iso15 732/783.1 (0.935+-0.036), iso10 904/958.8 (0.943+-0.033), iso5 1236/1277.1 (0.968+-0.029), iso10_e2 1114/1168.3 (0.954+-0.030), iso10_e1p5 1244/1322.5 (0.941+-0.028); mumug iso20 980/973.4 (1.007+-0.034), iso15 1144/1152.3 (0.993+-0.031), iso10 1412/1418.0 (0.996+-0.028), iso5 1861/1881.2 (0.989+-0.024), iso10_e2 1705/1728.5 (0.986+-0.025), iso10_e1p5 1922/1962.1 (0.980+-0.024), wide_iso10 1794/1833.2 (0.979+-0.024). Uncertified luminosity. The _2nd regions are not in the yield table. Owner decision 2026-11-03 after reviewing llgamma-20261103: samples pure, photon-track angle well modelled down to 0-5 deg, threshold can be lowered, statistics limit the study (about 600 eeg and 980 mumug). Run llgamma-v2-20261103: NERSC /pscratch/sd/a/avencast/Ztautau/analysis-runs/1992_1993_1994_1995/llgamma-v2-20261103, job 60747968 (coordinator brief), tau_analysis 5ac249d (configs/analysis_llgamma_v2.yaml, configs/plotting_llgamma_v2.yaml, analysis/single_photon.py); study artifacts/llgamma-v2-20261103/REPORT.md, peak_fits.json, tables/yields.md, tables/chi2_table.md, epred/REPORT.md, epred/k_epred.json (NERSC login node, light python only).
-->
