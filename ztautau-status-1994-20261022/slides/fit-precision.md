---
class: st pres
---

<script setup>
import ZoomablePlot from 'slidev-addon-ztautau/components/ZoomablePlot.vue'
</script>

# Appendix · spin fit: precision of the final model and simulation size

<div class="st-cols st-cols-21">
<div>
<div class="st-fig" style="height:205px"><ZoomablePlot src="/figures/fit/modelC-sigma-ratio.png" alt="sigma ratio final over legacy per coefficient" /></div>
<div class="st-cap"><b>Error ratio</b> final / legacy model per coefficient, 1992–1995 (filled triangles: same pseudo-experiments)</div>
<table class="num first-nw" style="margin-top:8px">
<thead><tr><th>Final / legacy error</th><th>1992–1995</th><th>1994</th></tr></thead>
<tbody>
<tr><td>Six polarisations <LaTeX formula="B" /></td><td>0.936–0.953</td><td>0.940–0.960</td></tr>
<tr><td><LaTeX formula="C_{nn},\ C_{rr},\ C_{kk}" /></td><td>0.975 · 0.966 · 0.945</td><td>0.992 · 0.961 · 0.961</td></tr>
<tr><td><LaTeX formula="C_{nr},\ C_{rn}" /></td><td>1.066 · 1.065</td><td>1.017 · 1.013</td></tr>
</tbody>
</table>
</div>
<div>
<div class="co ok"><b>Gain</b> Correlations between the 15 histograms are used, not ignored.</div>
<div class="co warn"><b><LaTeX formula="C_{nr},C_{rn}" /></b> Real correlation (−0.35) the legacy fit ignored.</div>
<div class="co ok"><b>Simulation size</b> 45× data: errors grow 1.2 % with all of it.</div>
<div class="co decision"><b>Half kept</b> Held-out half: about 2 %; not yet in the fit.</div>
</div>
</div>

<div class="st-source">Source: final-model error comparison (2026-10-31) and the 1994 simulation-statistics study (2026-10-25); simulation only, statistics only</div>

<!--
sigma_C/sigma_A (GLS / HESSE), artifacts/joint-fit-20261031/modelC/combined-ml/summary.md: B_An .953, B_Ar .939, B_Ak .937, B_Bn .950, B_Br .939, B_Bk .936, C_nn .975, C_nr 1.066, C_nk .960, C_rn 1.065, C_rr .966, C_rk .983, C_kn .960, C_kr .988, C_kk .945 (median 0.960). 1994 (modelC/1994_91p2-ml): B .940-.960, C_nn .992, C_nr 1.017, C_nk .960, C_rn 1.013, C_rr .961, C_rk .994, C_kn .960, C_kr .987, C_kk .961. C_nr-C_rn GLS correlation -0.35 combined (-0.22 1994); unprofiled sigma_C/sigma_A = 1.00 (0.99). Toys confirm (C toy / A toy 0.936-0.991; C_nr/C_rn 1.07).
MC statistics: artifacts/legacy-fit-mcstat-20261025/mcstat.md and verdict.md.part (legacy fit, Barlow-Beeston-lite per bin, 1994): 1994 Z->tautau MC ~45x data (fit-selection MC/data 45.0, 3,049,200 rows); with all MC the inflation is ~1.1-1.2 % (analytical full-MC legacy fit 1.011 for B_An; v5 scaled to 100 % predicted 1.0115); the 20 % held-out cohort of the October study inflates by 5.4-5.8 %; inflation follows sqrt(1 + k), k = sum w^2 / sum w. Current fits use the hold half (f ~ 0.50): docs/PROJECT_GUIDE.md 2026-10-27 owner note "half of 1994 behind the expected data inflates the fit sigma by ~2 %". MC template statistics are not included in any of the joint-fit models (statistics-only = data statistics). Figure: modelC/combined-ml/sigma_ratio_C_over_A.png; mcstat_inflation.png in the appendix.
-->
