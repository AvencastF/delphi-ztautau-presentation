---
class: st pres c2
---

# Calibration 2 · Overview: a photon energy scale from radiative dilepton events in seven steps

<div class="st-sub">Each later slide is one step; its title says which. <span class="tag data">data</span> <span class="tag sim">sim</span> 1992–1995, barrel calorimeter (HPC), statistical errors only.</div>

<table class="c2t first-nw">
<thead><tr><th>Step</th><th>What is done</th><th>What it gives</th></tr></thead>
<tbody>
<tr><td class="step">1 · Samples</td><td><LaTeX formula="e^+e^-\gamma" /> and <LaTeX formula="\mu^+\mu^-\gamma" /> in data and simulation, all four years</td><td>photon energy known without the calorimeter</td></tr>
<tr><td class="step">2 · Selection</td><td>two barrel leptons and exactly one isolated barrel photon, <LaTeX formula="E_\gamma\gt3" /> GeV</td><td>3,097 data events, <LaTeX formula="Z\to\tau\tau" /> below 0.05 %</td></tr>
<tr><td class="step">3 · Variable</td><td><LaTeX formula="R=E_\mathrm{HPC}/E_\mathrm{pred}" />, with <LaTeX formula="E_\mathrm{pred}" /> from the three directions</td><td>one number per event</td></tr>
<tr><td class="step">4 · Scale per year</td><td><LaTeX formula="k=" /> peak of <LaTeX formula="R" /> in data / peak in simulation</td><td><LaTeX formula="k" /> = 0.949–1.072, flat against the cuts</td></tr>
<tr><td class="step">5 · Energy dependence</td><td><LaTeX formula="k" /> in bins of <LaTeX formula="E_\mathrm{pred}" /></td><td>1992 rises with energy; 1993–1995 flat</td></tr>
<tr><td class="step">6 · Validation</td><td>scale the simulation and compare again; swap channels; energy points</td><td>data/simulation 0.991–1.014 per year</td></tr>
<tr><td class="step">7 · Result</td><td><LaTeX formula="k(E,\text{year})" /> next to calibration 1</td><td>agrees with it in 1993–1995</td></tr>
</tbody>
</table>

<style>
.c2t { font-size: 14.5px !important; }
.c2t td, .c2t th { padding: 7px 10px !important; }
</style>

<div class="takeaway"><b>Takeaway</b> Simulated photon energies must be scaled by <LaTeX formula="k(E,\text{year})" />: 1992 rising (0.965 at 5–8 GeV, 1.043 above 17 GeV), 1993 1.043, 1994 0.958, 1995 1.023. After scaling, data/simulation peaks agree to 0.991–1.014 per year. Not yet applied to the <LaTeX formula="\rho" /> analysis.</div>

<div class="st-source">Source: version-2 <LaTeX formula="\ell^+\ell^-\gamma" /> study, its energy-binned study and its closure study (2026-11-03); the numbers are repeated with their errors in steps 2–7</div>

<!--
Calibration-2 rewrite of 2026-11-03b (owner feedback 2026-11-03: "make clear procedure, step 1, step 2, ... and very clear takeaway message"). Run llgamma-v2-20261103: NERSC /pscratch/sd/a/avencast/Ztautau/analysis-runs/1992_1993_1994_1995/llgamma-v2-20261103, job 60747968 (coordinator brief), tau_analysis 5ac249d (configs/analysis_llgamma_v2.yaml, analysis/single_photon.py). Numbers: 3,097 = 1,236 (llg_eeg_iso5) + 1,861 (llg_mumug_iso5) data events (derived sum, artifacts/llgamma-v2-20261103/tables/yields.md). Z_tautau share: max 0.028 % (mumug 1992, 0.1054 / 373.08 weighted events, derived from cutflows/cutflow.csv). k range 0.949-1.072: REPORT.md section 2, llg_eeg_iso5 / llg_mumug_iso5 per year (eeg 1994 0.949, mumug 1993 1.072). k(E,year): epred/REPORT.md section 4 (1992 bins 5-8 0.965 +- 0.019, 17-46 1.043 +- 0.015) and section 4.1 constants (1993 1.043 +- 0.010, 1994 0.958 +- 0.008, 1995 1.023 +- 0.010; exact values in closure/REPORT.md 2.1: 1.0429, 0.9577, 1.0232). After scaling: closure/REPORT.md section 3, comb, after smooth k(E), fit estimator, 5 <= E_pred < 46 GeV: 0.991 / 1.014 / 1.003 / 1.008 (+- 0.017 / 0.013 / 0.009 / 0.014). The owner brief proposed "within 1 %"; 1993 is 1.014 +- 0.013 (1.1 sigma), so the slide gives the range. Not applied: owner "not yet" (2026-11-03, relayed in the coordinator brief).
-->
