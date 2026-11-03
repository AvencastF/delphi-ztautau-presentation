---
class: st pres c2
---

<script setup>
import ZoomablePlot from 'slidev-addon-ztautau/components/ZoomablePlot.vue'
</script>

# Calibration 2 · Step 6b: before and after, per energy bin

<div class="st-sub">Data/simulation peak ratio of <LaTeX formula="R" /> in each <LaTeX formula="E_\mathrm{pred}" /> bin, both channels. Same events as the calibration.</div>

<div class="st-fig" style="height:225px"><ZoomablePlot src="/figures/photon-calibration/closure/k_after_vs_epred.png" alt="peak ratio per E_pred bin per year: before, after binned k, after k(E)" /></div>
<div class="st-cap">Blue: before. Red: after <LaTeX formula="k(E)" /> (the result). Green: after the binned <LaTeX formula="k" /> (closes by construction).</div>

<table class="c2t num first-nw" style="margin-top:6px">
<thead><tr><th><LaTeX formula="\chi^2" /> to 1 over the bins (<LaTeX formula="p" />)</th><th>1992</th><th>1993</th><th>1994</th><th>1995</th></tr></thead>
<tbody>
<tr><td>Before</td><td>15.8/4 (0.00)</td><td>26.0/5 (0.00)</td><td>34.6/5 (0.00)</td><td>6.7/4 (0.15)</td></tr>
<tr class="hl"><td>After <LaTeX formula="k(E)" /></td><td>4.2/4 (0.38)</td><td>7.8/5 (0.17)</td><td>6.3/5 (0.28)</td><td>1.3/4 (0.86)</td></tr>
</tbody>
</table>

<div class="takeaway"><b>Takeaway</b> After scaling, every year is consistent with 1 across 5–46 GeV (<LaTeX formula="p\ge0.17" />); largest single bin: 1993 at 12–17 GeV, <LaTeX formula="1.065\pm0.028" />.</div>

<div class="st-source">Source: closure study of the version-2 <LaTeX formula="\ell^+\ell^-\gamma" /> run (2026-11-03), section 5</div>

<!--
artifacts/llgamma-v2-20261103/closure/REPORT.md section 5 (comb, fit estimator): chi2 to 1 (p) before 15.8/4 (0.00), 26.0/5 (0.00), 34.6/5 (0.00), 6.7/4 (0.15); after_bin 0.1/4, 0.3/5, 0.7/5, 0.1/4 (by construction: same bins, events and estimator); after_smooth 4.2/4 (0.38), 7.8/5 (0.17), 6.3/5 (0.28), 1.3/4 (0.86). Truncated mean after smooth: 3.0/4 (0.56), 5.1/5 (0.41), 9.5/5 (0.09), 3.1/4 (0.55). Largest single-bin residuals after smooth: 1993 12-17 GeV 1.065 +- 0.028 (the constant does not follow the k = 1.113 bin), 1994 25-46 0.965 +- 0.015, 1992 5-8 1.022 +- 0.020 and 12-17 0.961 +- 0.025. Figure closure/k_after_vs_epred.png (before / after bin / after smooth, per year and all). Same-sample closure: a consistency check of the procedure, not an independent validation (section 7).
-->
