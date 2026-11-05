---
class: st pres c2
---

<script setup>
import ZoomablePlot from 'slidev-addon-ztautau/components/ZoomablePlot.vue'
</script>

# Calibration 2 · Final <LaTeX formula="\pi^0" /> step (v3): closure on the <LaTeX formula="\rho" /> legs of the production skim

<div class="st-sub">The v3 constants applied in production; 22,219 data and 973,626 simulated <LaTeX formula="\rho" /> legs common to the baseline and v3 skims. Before = no photon calibration; v2 = previous stored calibration.</div>

<table class="c2t num first-nw" style="font-size:12px;width:100%">
<thead><tr><th>Data / simulation</th><th>Before</th><th>v2</th><th>v3</th></tr></thead>
<tbody>
<tr><td><LaTeX formula="\pi^0" /> peak, 1992 / 93 / 94 / 95</td><td>0.943 / 1.011 / 0.990 / 1.015</td><td>0.969 / 0.991 / 1.001 / 0.994</td><td>0.973 / 1.009 / 0.994 / 1.008</td></tr>
<tr class="hl"><td><LaTeX formula="\pi^0" /> peak, all years</td><td><LaTeX formula="0.990\pm0.005" /></td><td><LaTeX formula="0.991\pm0.005" /></td><td><LaTeX formula="0.995\pm0.005" /></td></tr>
<tr><td><LaTeX formula="\pi^0" /> width, all years</td><td><LaTeX formula="1.145\pm0.038" /></td><td><LaTeX formula="0.946\pm0.031" /></td><td><LaTeX formula="0.948\pm0.031" /></td></tr>
<tr><td><LaTeX formula="\pi^0" /> width, 1995</td><td><LaTeX formula="1.049\pm0.073" /></td><td><LaTeX formula="0.838\pm0.058" /></td><td><LaTeX formula="0.829\pm0.058" /></td></tr>
<tr><td><LaTeX formula="\rho" /> mass peak, all years</td><td>1.0040</td><td>1.0025</td><td>1.0022 (<LaTeX formula="\pm" />0.0021)</td></tr>
<tr><td>Knot <LaTeX formula="\pm1\sigma" />: simulated <LaTeX formula="\pi^0" /> peak</td><td>—</td><td><LaTeX formula="\pm4.7" /> MeV</td><td><LaTeX formula="\pm1.9" /> MeV (data error 0.7)</td></tr>
</tbody>
</table>

<div style="display:grid;grid-template-columns:2.1fr 1fr;gap:10px;margin-top:6px">
<div class="st-fig" style="height:118px"><ZoomablePlot src="/figures/photon-calibration/rho-closure-v3/mgg_pair_before_after.png" alt="m_gammagamma of the rho-leg photon pairs per year and all years, data against MC, before (top) and after v3 (bottom)" /></div>
<div class="st-fig" style="height:118px"><ZoomablePlot src="/figures/photon-calibration/rho-closure-v3/summary_ratios.png" alt="pi0 peak, pi0 width and rho peak data/MC per year: before, after v3, after with the knots at plus and minus one sigma, and the DELPHI builder" /></div>
</div>
<div class="st-cap"><b>Left</b> <LaTeX formula="m_{\gamma\gamma}" /> of the <LaTeX formula="\rho" />-leg pairs, before (grey) and after v3 (blue). <b>Right</b> peak, width and <LaTeX formula="\rho" /> mass ratios: before, after, knots <LaTeX formula="\pm1\sigma" />, DELPHI builder. Polarimeter means, categories and spectra unchanged from v2; the <LaTeX formula="\rho" /> legs were not used for tuning.</div>

<div class="takeaway"><b>Takeaway</b> On the <LaTeX formula="\rho" /> legs the <LaTeX formula="\pi^0" /> peak closes to 0.995 ± 0.005 (1992 0.973) with a 2.5× tighter low-energy prior than v2; the width is not improved (0.948, 1995 0.83), an upper bound on "simulation too wide" because these legs are selected on raw energies.</div>

<div class="st-source">Source: <LaTeX formula="\rho" />-leg closure report, v3 section (2026-11-04), and the final-calibration report, section 7; figures of the v3 closure</div>

<!--
artifacts/rho-closure-20261104/CLOSURE_REPORT.md v3 section (production skim analysis-runs/1992_1993_1994_1995/all-years-calib98160-v3-20261104/, job 60828758, 4 nodes, 2.64 node-h, 204 GB, manifest sha256 5bbbb5b1...; tau_analysis f362ac7; config configs/analysis_all_years_photon98160.yaml unchanged; photon_energy on in all 8 blocks with the v3 smear, skip_codes [101]; before pass reused from job 60809570; legs 22,219 data / 973,626 MC common to the baseline and v3 skims, odd-event legs 11,155 / 486,224; closure code as v2, closure.py --parity odd the only change). Table "Before / after v2 / after v3": pi0 mu data/MC 1992 0.943 +- 0.011 / 0.969 +- 0.012 / 0.973 +- 0.012; 1993 1.011 / 0.991 / 1.009 (+- 0.012); 1994 0.990 / 1.001 / 0.994 (+- 0.009); 1995 1.015 / 0.994 / 1.008 (+- 0.011); all 0.990 / 0.991 / 0.995 (+- 0.005); chi2 against 1 per year 6.6/4 (v2 7.6/4). Odd-event legs after v3 0.993 / 1.000 / 0.989 / 1.001, all 0.995 +- 0.008. pi0 sigma data/MC all 1.145 +- 0.038 / 0.946 +- 0.031 / 0.948 +- 0.031; 1992 1.153 / 0.970 / 1.021; 1993 1.256 / 0.967 / 1.036; 1994 1.183 / 0.983 / 0.941; 1995 1.049 +- 0.073 / 0.838 +- 0.058 / 0.829 +- 0.058; odd legs 0.958 +- 0.048. rho fit mu all 1.0040 / 1.0025 / 1.0022 (+- 0.0021); pair / merged / single 0.9899 / 0.9937 / 1.0091 after v3. Spectra chi2 pair / merged / single / candidates 53 / 34 / 60 / 147 (v2 52 / 34 / 56 / 145); category fractions pair 0.922, merged 0.727, single 1.073, fallback 1.010; polarimeter data - MC <v_k> -2.5 sigma, <cos theta*> -2.5, <x_rho> +3.4 (v2 -2.5 / -2.6 / +3.6). Knot +-1 sigma (all v3 knots, fully correlated; v3/code/make_shift_v3.py): MC pi0 peak +1.86 / -1.87 MeV (slide: +-1.9), v2 +4.58 / -4.86 MeV (slide and PROJECT_GUIDE: about +-4.7), data error 0.7 MeV (CALIBRATION_V3_REPORT section 7); <v_k> +-0.09 sigma_data, <cos theta*> -0.39/+0.30, <x_rho> +-0.9, pair fraction +0.36/-0.67, fallback -0.47/+0.68. "2.5x tighter": CALIBRATION_V3_REPORT section 7. DELPHI builder (after-b98160): pi0 mu 0.987 +- 0.008, sigma 0.951 +- 0.061, rho mu 1.0071. Coverage: used rho-leg photons below 3 GeV 30.5 % data / 31.7 % MC. Reading (closure report, calibration report section 7 and 8.8): the rho-leg table comes from the 2026-10-26 rq skim selected on uncalibrated energies, so MC widths after smearing are biased towards "too wide"; not tuned on any closure quantity. Figures artifacts/rho-closure-20261104/v3/figures/mgg_pair_before_after.png and summary_ratios.png (closure_plots.py), copied unchanged to public/figures/photon-calibration/rho-closure-v3/.
-->
