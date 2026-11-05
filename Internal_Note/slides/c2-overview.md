---
class: st pres c2
---

# Calibration 2 · Overview: seven steps, a DELPHI-style redo, a final <LaTeX formula="\pi^0" /> step

<div class="st-sub">Steps 1–7: version 2 (raw energy, 3 GeV); version 3 follows DELPHI practice; the final <LaTeX formula="\pi^0" /> step gives the stored calibration v3 (nominal since 2026-11-05). <span class="tag data">data</span> <span class="tag sim">sim</span> 1992–1995, barrel calorimeter (HPC), statistical errors only.</div>

<table class="c2t first-nw">
<thead><tr><th>Step</th><th>What is done</th><th>What it gives</th></tr></thead>
<tbody>
<tr><td class="step">1 · Samples</td><td><LaTeX formula="e^+e^-\gamma" /> and <LaTeX formula="\mu^+\mu^-\gamma" /> in data and simulation, all four years</td><td>photon energy known without the calorimeter</td></tr>
<tr><td class="step">2 · Selection</td><td>two barrel leptons and exactly one isolated barrel photon, <LaTeX formula="E_\gamma\gt3" /> GeV</td><td>3,097 data events, <LaTeX formula="Z\to\tau\tau" /> below 0.05 %</td></tr>
<tr><td class="step">3 · Variable</td><td><LaTeX formula="R=E_\mathrm{HPC}/E_\mathrm{pred}" />, with <LaTeX formula="E_\mathrm{pred}" /> from the three directions</td><td>one number per event</td></tr>
<tr><td class="step">4 · Scale per year</td><td><LaTeX formula="k=" /> peak of <LaTeX formula="R" /> in data / peak in simulation</td><td><LaTeX formula="k" /> = 0.949–1.072, flat against the cuts</td></tr>
<tr><td class="step">5 · Energy dependence</td><td><LaTeX formula="k" /> in bins of <LaTeX formula="E_\mathrm{pred}" /></td><td>1992 rises with energy; 1993–1995 flat</td></tr>
<tr><td class="step">6 · Validation</td><td>scale the simulation and compare again; swap channels; energy points</td><td>data/simulation 0.991–1.014 per year</td></tr>
<tr><td class="step">7 · Result</td><td><LaTeX formula="k(E,\text{year})" /> next to calibration 1; coverage of the <LaTeX formula="\rho" /> photons</td><td>agrees with it in 1993–1995; 44 % of the <LaTeX formula="\rho" /> photons are below 5 GeV</td></tr>
<tr><td class="step">Version 3</td><td>MAIN energy, 0.5 GeV, <LaTeX formula="d^2E" /> isolation; DELPHI comparison</td><td><LaTeX formula="k" /> = 1.016 / 1.038 / 0.988 / 1.041; smearing <LaTeX formula="0.28/\sqrt{E}" /></td></tr>
<tr class="hl"><td class="step">Final <LaTeX formula="\pi^0" /> step</td><td><LaTeX formula="\tau" /> <LaTeX formula="\pi^0\to\gamma\gamma" /> peak and width, 0.5–46 GeV, with the <LaTeX formula="\ell^+\ell^-\gamma" /> shape above 3 GeV; <LaTeX formula="\rho" />-leg closure</td><td>stored v3: <LaTeX formula="(s,b,a)" /> per year; <LaTeX formula="\pi^0" /> peak on the <LaTeX formula="\rho" /> legs 0.995 ± 0.005; accepted as nominal</td></tr>
</tbody>
</table>

<style>
.c2t { font-size: 12.5px !important; }
.c2t td, .c2t th { padding: 2.5px 10px !important; }
</style>

<div class="takeaway"><b>Takeaway</b> <LaTeX formula="\ell^+\ell^-\gamma" /> fixes the per-year scale above 3 GeV (1.016 / 1.038 / 0.988 / 1.041), the <LaTeX formula="\tau" /> <LaTeX formula="\pi^0" /> the slope below and the smearing. Calibration v3 is applied and accepted as nominal; its tensions are systematics.</div>

<div class="st-source">Source: version-2 <LaTeX formula="\ell^+\ell^-\gamma" /> study and its closure (2026-11-03); version-3 report, final-calibration and <LaTeX formula="\rho" />-leg closure reports (2026-11-04); numbers with errors on the later slides</div>

<!--
Calibration-2 rewrite of 2026-11-03b (owner feedback 2026-11-03: "make clear procedure, step 1, step 2, ... and very clear takeaway message"). Run llgamma-v2-20261103: NERSC /pscratch/sd/a/avencast/Ztautau/analysis-runs/1992_1993_1994_1995/llgamma-v2-20261103, job 60747968 (coordinator brief), tau_analysis 5ac249d (configs/analysis_llgamma_v2.yaml, analysis/single_photon.py). Numbers: 3,097 = 1,236 (llg_eeg_iso5) + 1,861 (llg_mumug_iso5) data events (derived sum, artifacts/llgamma-v2-20261103/tables/yields.md). Z_tautau share: max 0.028 % (mumug 1992, 0.1054 / 373.08 weighted events, derived from cutflows/cutflow.csv). k range 0.949-1.072: REPORT.md section 2, llg_eeg_iso5 / llg_mumug_iso5 per year (eeg 1994 0.949, mumug 1993 1.072). k(E,year): epred/REPORT.md section 4 (1992 bins 5-8 0.965 +- 0.019, 17-46 1.043 +- 0.015) and section 4.1 constants (1993 1.043 +- 0.010, 1994 0.958 +- 0.008, 1995 1.023 +- 0.010; exact values in closure/REPORT.md 2.1: 1.0429, 0.9577, 1.0232). After scaling: closure/REPORT.md section 3, comb, after smooth k(E), fit estimator, 5 <= E_pred < 46 GeV: 0.991 / 1.014 / 1.003 / 1.008 (+- 0.017 / 0.013 / 0.009 / 0.014). The owner brief proposed "within 1 %"; 1993 is 1.014 +- 0.013 (1.1 sigma), so the slide gives the range. Coverage: step 7b (rho-polarimeter-step2-20261102/photon_energy_coverage/REPORT.md: 44.0 % data / 46.4 % MC of the used photon objects below 5 GeV). Not applied: owner "not yet" (2026-11-03, relayed in the coordinator brief). Version 3 (added 2026-11-04): artifacts/llgamma-v3-20261104/REPORT.md sections 1, 5.1 (E_pred >= 5 GeV, d2E: 1.016 +- 0.008 / 1.038 +- 0.008 / 0.988 +- 0.005 / 1.041 +- 0.008), 6 (a-only all years d2E 0.281 +- 0.015, summarised as (0.28 +- 0.02)/sqrt(E), no constant term), 7 (Lefebure 1993 1.014, 1995 1.030: +0.024, +0.011; REPORT section 1 says "within 0.02", which 1993 (+0.024) exceeds, so the slide gives the differences; 1994 1.041 vs 0.988, opposite sign), 8 (sub-3 GeV values 0.90-0.95 are an observation, not a calibration point). The v2 takeaway values (1992 line, 1993 1.043, 1994 0.958, 1995 1.023, closure 0.991-1.014) remain on steps 5-7; the takeaway now quotes the version-3 MAIN-energy values (owner request 2026-11-04). Final pi0 step (added 2026-11-05): artifacts/pi0-final-calib-20261104/CALIBRATION_V3_REPORT.md status and section 1 (stored calibration v3: (s, b, a) per year, k(E) = s g(E) from 3 GeV with g the l+l-gamma v4 shape, s g(3)(1 + b ln(E/3 GeV)) below, sigma/E = a/sqrt(E); tau_analysis f362ac7); artifacts/rho-closure-20261104/CLOSURE_REPORT.md v3 section (pi0 peak data/MC on the rho legs all years 0.995 +- 0.005); docs/PROJECT_GUIDE.md owner decision 2026-11-05 (v3 nominal; scale, resolution and conversion variations as systematics). The former 'Not yet applied' / 'below 3 GeV is open' takeaway sentences are superseded by that decision; the version-3 row is no longer highlighted.
-->
