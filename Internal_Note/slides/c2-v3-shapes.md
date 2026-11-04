---
class: st pres c2
---

<script setup>
import ZoomablePlot from 'slidev-addon-ztautau/components/ZoomablePlot.vue'
</script>

# Calibration 2 · Version 3: data/simulation shapes at 0.5 GeV, <LaTeX formula="d^2E" /> isolation

<div class="st-sub">All years, simulation not scaled. Panels: <LaTeX formula="R=E_\mathrm{MAIN}/E_\mathrm{pred}" />, raw <LaTeX formula="R" />, <LaTeX formula="E_\mathrm{MAIN}" />, <LaTeX formula="E_\mathrm{pred}" />, <LaTeX formula="d^2E" />, angle to the nearer track. Badges: statistical <LaTeX formula="\chi^2" />.</div>

<div class="st-cols st-cols-2" style="gap:14px">
<div><div class="st-fig" style="height:215px"><ZoomablePlot src="/figures/photon-calibration/v3/datamc_llg_eeg_e0p5_d2e.png" alt="eeg, 0.5 GeV, d2E isolation: six data/MC variables" /></div><div class="st-cap"><LaTeX formula="ee\gamma" />: <LaTeX formula="R" /><span class="badge a">183 / 100</span> raw <LaTeX formula="R" /><span class="badge g">143 / 100</span> <LaTeX formula="d^2E" /><span class="badge g">114 / 95</span></div></div>
<div><div class="st-fig" style="height:215px"><ZoomablePlot src="/figures/photon-calibration/v3/datamc_llg_mumug_e0p5_d2e.png" alt="mumug, 0.5 GeV, d2E isolation: six data/MC variables" /></div><div class="st-cap"><LaTeX formula="\mu\mu\gamma" />: <LaTeX formula="R" /><span class="badge a">233 / 100</span> raw <LaTeX formula="R" /><span class="badge a">208 / 100</span> <LaTeX formula="d^2E" /><span class="badge g">84 / 95</span></div></div>
</div>

<table class="c2t num first-nw" style="margin-top:6px">
<thead><tr><th><LaTeX formula="\chi^2/\mathrm{dof}" />, all years</th><th><LaTeX formula="E_\mathrm{MAIN}" /></th><th><LaTeX formula="E_\mathrm{pred}" /></th><th>angle to track</th><th>rate data/sim.</th></tr></thead>
<tbody>
<tr><td><LaTeX formula="ee\gamma" /></td><td>313 / 167 <span class="badge a">1.87</span></td><td>253 / 93 <span class="badge a">2.72</span></td><td>165 / 90 <span class="badge a">1.83</span></td><td><LaTeX formula="0.926\pm0.015" /></td></tr>
<tr><td><LaTeX formula="\mu\mu\gamma" /></td><td>248 / 164 <span class="badge a">1.51</span></td><td>187 / 93 <span class="badge a">2.01</span></td><td>129 / 90 <span class="badge g">1.43</span></td><td><LaTeX formula="0.941\pm0.014" /></td></tr>
</tbody>
</table>

<div class="takeaway"><b>Takeaway</b> The MAIN-energy <LaTeX formula="R" /> peaks at 0.95–1.0 in data and simulation; the <LaTeX formula="R" /> disagreement is the width, not the position. The 6–7 % rate deficit sits below 2 GeV and does not enter <LaTeX formula="k" />.</div>

<div class="st-source">Source: data/simulation figures and the <LaTeX formula="\chi^2" /> table of the version-3 <LaTeX formula="\ell^+\ell^-\gamma" /> calibration (2026-11-04), report section 4</div>

<!--
Figures artifacts/llgamma-v3-20261104/figures/datamc_llg_eeg_e0p5_d2e.png and datamc_llg_mumug_e0p5_d2e.png (plot_v3.py sha256 f2140cef32d08733..., copied unchanged by data/make_photon_calibration_figs.py into public/figures/photon-calibration/v3/). Six panels per region: R = E_MAIN/E_pred, R_raw = E_HPC/E_pred, E_MAIN [GeV], E_pred [GeV], d^2 E_MAIN [deg^2 GeV], angle to nearer track [deg]; MC normalised to luminosity (rate mode); stack Bhabha or Z_mumu + Z_tautau. chi2/dof from tables.md "Data/MC chi2/dof per region" (pipeline outputs.agreement, rate mode, Total MC; * = p < 0.001), column all: llg_eeg_e0p5_d2e single_photon_main_e_over_epred 183/100*, single_photon_e_over_epred 143/100, single_photon_main_energy 313/167*, single_photon_epred 253/93*, single_photon_isolation_d2e 114/95, single_photon_track_angle_min 165/90*; llg_mumug_e0p5_d2e 233/100*, 208/100*, 248/164*, 187/93*, 84/95, 129/90. Badge colours per dof (green <= 1.5, amber <= 3, red > 3): 1.83 a, 1.43 g, 1.20 g; 2.33 a, 2.08 a, 0.88 g; E_MAIN 1.87 a / 1.512 a, E_pred 2.72 a / 2.01 a, angle 1.83 a / 1.43 g (derived ratios). Per year (tables.md): eeg R_MAIN 164/100*, 187/100*, 130/100, 182/100*; mumug 217/100*, 263/99*, 193/100*, 249/100*. Rate: tables.md yields, eeg 4169/4503.7 = 0.926 +- 0.015, mumug 5048/5364.0 = 0.941 +- 0.014; at 3 GeV, 5 deg 0.964 / 0.987 (REPORT.md section 4). REPORT.md section 1: "its R peaks at 0.95-1.0 in both data and MC (the raw cluster energy peaked at 0.93)"; section 4: "As in v2, the R disagreement is the width (section 6), not the position"; the deficit "sits below 2 GeV of MAIN energy and is not investigated here (it does not enter k, which is a peak position)".
-->
