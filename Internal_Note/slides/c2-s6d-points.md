---
class: st pres c2
---

<script setup>
import ZoomablePlot from 'slidev-addon-ztautau/components/ZoomablePlot.vue'
</script>

# Calibration 2 · Step 6d: the three energy points of 1993 and 1995

<div class="st-sub"><LaTeX formula="k" /> per <LaTeX formula="\sqrt{s}" /> point, both channels, isolation <LaTeX formula="\ge5^\circ" />, before scaling. One <LaTeX formula="k" /> per year assumes the points agree.</div>

<div class="st-cols st-cols-12" style="gap:16px">
<div>
<table class="c2t num first-nw">
<thead><tr><th>Year</th><th>89.4 GeV</th><th>91.2 GeV</th><th>93.0 GeV</th><th><LaTeX formula="p" /></th></tr></thead>
<tbody>
<tr><td>1993</td><td><LaTeX formula="1.037\pm0.031" /></td><td><LaTeX formula="1.058\pm0.013" /></td><td><LaTeX formula="1.091\pm0.039" /></td><td>0.55</td></tr>
<tr><td>1995</td><td><LaTeX formula="1.065\pm0.051" /></td><td><LaTeX formula="1.037\pm0.015" /></td><td><LaTeX formula="1.017\pm0.022" /></td><td>0.61</td></tr>
</tbody>
</table>
<div class="st-cap"><LaTeX formula="p" />: three points against their weighted mean, 2 dof (truncated mean: 0.97 in both years).</div>
<div class="co ok"><b>Points</b> Off-peak and peak runs share one scale.</div>
</div>
<div class="st-fig" style="height:235px"><ZoomablePlot src="/figures/photon-calibration/v2/k_per_point.png" alt="k per energy point for 1993 and 1995, both selections" /></div>
</div>

<div class="takeaway"><b>Takeaway</b> The three energy points of 1993 and of 1995 agree (<LaTeX formula="p=0.55" />, <LaTeX formula="0.61" />), so one <LaTeX formula="k" /> per year is justified.</div>

<div class="st-source">Source: energy-binned study of the version-2 <LaTeX formula="\ell^+\ell^-\gamma" /> run (2026-11-03), section 6</div>

<!--
artifacts/llgamma-v2-20261103/epred/REPORT.md section 6, iso5 comb k fit per point (data events): 1993 all 1.058 +- 0.012, 89.4 1.037 +- 0.031 (97), 91.2 1.058 +- 0.013 (464), 93.0 1.091 +- 0.039 (112); 1995 all 1.037 +- 0.013, 89.4 1.065 +- 0.051 (94), 91.2 1.037 +- 0.015 (394), 93.0 1.017 +- 0.022 (117). Consistency of the three points (chi2 about the weighted mean, 2 dof): 1993 fit 1.2 (p 0.55), trunc 0.1 (0.97); 1995 fit 1.0 (0.61), trunc 0.1 (0.97); per channel smallest p 0.16. Figure epred/k_per_point.png (1993, 1995; iso5 and iso5_e1p5). Values are energy-integrated (all E_pred), before scaling; 1992 and 1994 have one point.
-->
