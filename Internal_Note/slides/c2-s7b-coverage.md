---
class: st pres c2
---

<script setup>
import ZoomablePlot from 'slidev-addon-ztautau/components/ZoomablePlot.vue'
</script>

# Calibration 2 · Step 7b: does 5–46 GeV cover the <LaTeX formula="\rho" /> analysis? No.

<div class="st-sub">Energy of every photon object the <LaTeX formula="\pi^0" /> builder uses in the <LaTeX formula="\rho" /> legs (ML <LaTeX formula="\rho" /> regions, 1992–1995). Shaded: the calibrated range.</div>

<div class="st-fig" style="height:215px"><ZoomablePlot src="/figures/photon-calibration/coverage/photon_energy_spectrum.png" alt="photon-object energy per pi0 category, data and simulation, calibrated range shaded" /></div>

<table class="c2t num first-nw" style="margin-top:6px">
<thead><tr><th>Category (share of objects)</th><th>Median <LaTeX formula="E" /> [GeV]</th><th>Objects <LaTeX formula="\lt3" /> GeV</th><th>Objects <LaTeX formula="\lt5" /> GeV</th><th>Legs with a photon <LaTeX formula="\lt5" /> GeV</th></tr></thead>
<tbody>
<tr><td>pair, two photons (39 %)</td><td>2.8</td><td>54 % / 54 %</td><td>77 % / 78 %</td><td>96 % / 97 %</td></tr>
<tr><td>merged shower (7 %)</td><td>12.7 / 13.3</td><td>0 / 0</td><td>0 / 0</td><td>0 / 0</td></tr>
<tr><td>single photon (54 %)</td><td>10.2 / 9.4</td><td>19 % / 20 %</td><td>30 % / 33 %</td><td>30 % / 33 %</td></tr>
<tr class="hl"><td>all usable legs</td><td>6.1 / 5.7</td><td>30 % / 31 %</td><td>44 % / 46 %</td><td>41 % / 44 %</td></tr>
</tbody>
</table>
<div class="st-cap">data / simulation. Generator level: 53 % of the <LaTeX formula="\pi^0" /> photons in true <LaTeX formula="\rho" /> legs are below 5 GeV; this is the physics of the soft <LaTeX formula="\pi^0" />, not the reconstruction.</div>

<div class="takeaway"><b>Takeaway</b> Nearly half of the photons used by the <LaTeX formula="\rho" /> <LaTeX formula="\pi^0" /> are below 5 GeV, 30 % even below the 3 GeV <LaTeX formula="\ell\ell\gamma" /> threshold. Calibration 2 covers only the merged showers and the hard single photons; a low-energy photon calibration is required.</div>

<div class="st-source">Source: photon-energy coverage study of the <LaTeX formula="\rho" />-polarimeter step 2 legs (2026-11-03); photon objects rebuilt from the calibration-pass object table</div>

<!--
artifacts/rho-polarimeter-step2-20261102/photon_energy_coverage/{REPORT.md, coverage.json, photon_energy_spectrum.png, pi0_energy_spectrum.png, true_energy_spectrum.png} (photon_energy_coverage.py sha256 cbd65ca8..., NERSC login node, 15 s, 1.3 GB; inputs rho_legs.npz 3f6af4d4..., full/legs_pi0.npz 8254f9f8..., calib2b/full/calib_objects.npz 583e1b7f...). Legs: ML rho regions as in rho_legs.json; data kind 0, MC Z_tautau kind 1 with rho_legs.weight (expected-data weights); usable = pair + merged + single with found == 1 (879,461 legs). Photon-object energy = calib_objects photons.e_main (MAIN energy, the energy the builder uses; pair energies pre-fit). Fractions (all years, weighted, data / MC): pair objects < 3 GeV 53.8 / 54.3 %, < 5 77.1 / 77.6 %, < 8 91.1 / 91.3 %; merged 0 / 0 (every merged shower has E >= 5.00 GeV, an apparent 5 GeV threshold of the upstream merged-pi0 reconstruction), < 8 19.9 / 16.0 %; single < 3 18.9 / 20.4 %, < 5 30.3 / 32.6 %; all usable objects < 3 29.5 / 31.1 %, < 5 44.0 / 46.4 %, < 8 57.7 / 59.7 %; legs with any object < 5 GeV: pair 96.4 / 97.0 %, single 30.3 / 32.6 %, all 41.2 / 43.7 %. Medians: pair 2.78 / 2.75, merged 12.7 / 13.3, single 10.2 / 9.4, all 6.1 / 5.7 GeV. Shares of objects (derived from MC category fractions pair 0.210 x 2 photons, merged 0.102, single 0.585 over 0.210 x 2 + 0.102 + 0.585 = 1.107: 38 %, 9 %, 53 %; data 39 / 7 / 54 % from the report's object counts; the slide rounds). Reconstructed E_pi0 < 5 GeV: 27.8 / 28.2 % of usable legs. Generator: 53 % of generator pi0 photons of true-rho legs and 19 % of generator pi0 energies below 5 GeV. Weighting by |h|^2 moves every fraction < 1 point. HPC photons only (class phot_pass): 43.8 / 48.1 % below 5 GeV; track conversions (about 20 % of objects): 60-64 % below 5 GeV and not covered by an HPC shower scale in any case. Caveat: calibration 2 is measured on the raw HPC shower energy (single_photon.py: hpc_energy_gev), whereas the pi0 builder uses the MAIN energy (median response to truth 1.05 vs 0.88 for the raw shower, step-2 report section 1); the relation between the two scales has not been established, so even inside 5-46 GeV k cannot be applied to the pi0 without that check. Builder threshold 0.5 GeV: softer photons are absent from the spectra. Per-year values vary by 1-3 points (coverage.json).
-->
