---
class: st pres
---

<script setup>
import ZoomablePlot from 'slidev-addon-ztautau/components/ZoomablePlot.vue'
</script>

# Calibration 2: <LaTeX formula="ee\gamma" /> versus <LaTeX formula="\mu\mu\gamma" />, and the three energy points

<div class="st-sub">Isolation <LaTeX formula="\ge5^\circ" />. Left: <LaTeX formula="\chi^2" /> of <LaTeX formula="k_{ee\gamma}-k_{\mu\mu\gamma}" /> over the energy bins. Right: <LaTeX formula="k" /> per <LaTeX formula="\sqrt{s}" /> point, channels combined.</div>

<div class="st-cols st-cols-2">
<div>
<table class="sm num first-nw">
<thead><tr><th>Year</th><th><LaTeX formula="\chi^2/\mathrm{dof}" /> (p), fit</th><th>Truncated mean</th></tr></thead>
<tbody>
<tr><td>1992</td><td>2.3/2 (0.32)</td><td>3.8/2 (0.15)</td></tr>
<tr><td>1993</td><td>6.9/2 (0.032)</td><td>2.5/2 (0.29)</td></tr>
<tr><td>1994</td><td>3.5/4 (0.49)</td><td>4.8/4 (0.31)</td></tr>
<tr><td>1995</td><td>3.8/2 (0.15)</td><td>2.2/2 (0.34)</td></tr>
<tr><td>All</td><td>2.1/5 (0.84)</td><td>1.6/5 (0.91)</td></tr>
</tbody>
</table>

<div class="co ok"><b>Channels</b> Differences below <LaTeX formula="2\sigma" /> per year, e.g. 1994: <LaTeX formula="0.949\pm0.011" /> vs <LaTeX formula="0.976\pm0.011" />.</div>
</div>
<div>
<table class="sm num first-nw">
<thead><tr><th>Year</th><th>89.4 GeV</th><th>91.2 GeV</th><th>93.0 GeV</th><th><LaTeX formula="p" /> (const.)</th></tr></thead>
<tbody>
<tr><td>1993</td><td><LaTeX formula="1.037\pm0.031" /></td><td><LaTeX formula="1.058\pm0.013" /></td><td><LaTeX formula="1.091\pm0.039" /></td><td>0.55</td></tr>
<tr><td>1995</td><td><LaTeX formula="1.065\pm0.051" /></td><td><LaTeX formula="1.037\pm0.015" /></td><td><LaTeX formula="1.017\pm0.022" /></td><td>0.61</td></tr>
</tbody>
</table>

<div class="co ok"><b>Points</b> The three points of 1993 and of 1995 agree.</div>
</div>
</div>
<div class="st-fig h150" style="margin-top:6px"><ZoomablePlot src="/figures/photon-calibration/v2/k_per_point.png" alt="k per energy point for 1993 and 1995, both selections" /></div>

<div class="st-source">Source: E_pred-binned study of the version-2 <LaTeX formula="\ell^+\ell^-\gamma" /> run (2026-11-03), sections 5 and 6</div>

<!--
artifacts/llgamma-v2-20261103/epred/REPORT.md section 5 (chi2 of k(eeg) - k(mumug) over the non-truncated bins, common binning, iso5): 1992 2.3/2 (0.32) fit, 3.8/2 (0.15) trunc; 1993 6.9/2 (0.032), 2.5/2 (0.29); 1994 3.5/4 (0.49), 4.8/4 (0.31); 1995 3.8/2 (0.15), 2.2/2 (0.34); all 2.1/5 (0.84), 1.6/5 (0.91). The 1993 fit-based p = 0.032 comes from bins with fit flags (mumug 1993 data k_tail at the boundary; eeg 1993 MC k_tail 0.26-0.27); iso5_e1p5 1993 fit 28.7/3 (< 0.001) vs trunc 1.5/3 (0.68). Per-year all-E ratios iso5 (REPORT.md section 2): 1993 eeg 1.044 +- 0.023, mumug 1.072 +- 0.018 (difference -0.028 +- 0.029, 1.0 sigma, derived); 1994 eeg 0.949 +- 0.011, mumug 0.976 +- 0.011 (difference -0.027 +- 0.016, 1.7 sigma, derived; in 1994 eeg is below mumug in 3 of 4 non-truncated bins, each < 1.5 sigma). Section 6, iso5 comb k fit per point: 1993 all 1.058 +- 0.012, 89.4 1.037 +- 0.031 (97 events), 91.2 1.058 +- 0.013 (464), 93.0 1.091 +- 0.039 (112); 1995 all 1.037 +- 0.013, 89.4 1.065 +- 0.051 (94), 91.2 1.037 +- 0.015 (394), 93.0 1.017 +- 0.022 (117). Consistency of the three points (chi2 about weighted mean, 2 dof): 1993 fit 1.2 (p 0.55), trunc 0.1 (0.97); 1995 fit 1.0 (0.61), trunc 0.1 (0.97); per channel smallest p 0.16. Figure epred/k_per_point.png (1993, 1995; iso5 and iso5_e1p5).
-->
