---
class: st pres
---

<script setup>
import ZoomablePlot from 'slidev-addon-ztautau/components/ZoomablePlot.vue'
</script>

# Appendix · photon calibration: closure per channel (step 6a)

<div class="st-sub">The combined <LaTeX formula="k(E)" /> applied to each channel's simulation; <LaTeX formula="5\le E_\mathrm{pred}\lt46" /> GeV, same events, statistical errors only.</div>

<div class="st-cols st-cols-2" style="gap:14px">
<div><div class="st-fig" style="height:250px"><ZoomablePlot src="/figures/photon-calibration/closure/after-R_comb_years_summary.png" alt="R per year, both channels: before (left) and after k(E) (right), pipeline style" /></div><div class="st-cap">Per year, both channels: before (left), after (right)</div></div>
<div><div class="st-fig" style="height:250px"><ZoomablePlot src="/figures/photon-calibration/closure/after-R_eeg_all.png" alt="eeg R all years before and after scaling" /></div><div class="st-cap"><LaTeX formula="ee\gamma" />, all years: before (left), after (right); <LaTeX formula="\mu\mu\gamma" /> in the closure study</div></div>
</div>

<table class="sm num first-nw" style="margin-top:6px">
<thead><tr><th>Peak ratio, before <LaTeX formula="\to" /> after <LaTeX formula="k(E)" /></th><th>1992</th><th>1993</th><th>1994</th><th>1995</th></tr></thead>
<tbody>
<tr><td><LaTeX formula="ee\gamma" /></td><td><LaTeX formula="0.992\to 0.995\pm0.026" /></td><td><LaTeX formula="1.047\to 1.003\pm0.019" /></td><td><LaTeX formula="0.946\to 0.990\pm0.014" /></td><td><LaTeX formula="1.036\to 1.012\pm0.017" /></td></tr>
<tr><td><LaTeX formula="\mu\mu\gamma" /></td><td><LaTeX formula="0.996\to 0.990\pm0.025" /></td><td><LaTeX formula="1.072\to 1.030\pm0.024" /></td><td><LaTeX formula="0.970\to 1.012\pm0.013" /></td><td><LaTeX formula="1.028\to 1.004\pm0.024" /></td></tr>
</tbody>
</table>

<div class="st-source">Source: closure study of the version-2 <LaTeX formula="\ell^+\ell^-\gamma" /> run (2026-11-03), sections 3 and 6</div>

<!--
Figures changed 2026-11-03c to the pipeline-style before/after plots of closure/after_plots (after-R_comb_years_summary.png, after-R_eeg_all.png); the earlier overlay figures closure_R_eeg/mumug.png remain in public/figures. 
artifacts/llgamma-v2-20261103/closure/REPORT.md section 3 (eeg and mumug tables, comb calibration applied): eeg before 0.992 +- 0.026 / 1.047 +- 0.020 / 0.946 +- 0.014 / 1.036 +- 0.018, after smooth 0.995 +- 0.026 / 1.003 +- 0.019 / 0.990 +- 0.014 / 1.012 +- 0.017; mumug before 0.996 +- 0.025 / 1.072 +- 0.025 / 0.970 +- 0.012 / 1.028 +- 0.024, after smooth 0.990 +- 0.025 / 1.030 +- 0.024 / 1.012 +- 0.013 / 1.004 +- 0.024. The 1994 eeg - mumug difference (0.024) is unchanged by a common k. Figures closure/closure_R_eeg.png, closure_R_mumug.png (R in 0.04 bins; data points, MC before dashed, after k(E) red, after binned k dotted green; MC normalised to data in 0.6 < R < 1.4).
-->
