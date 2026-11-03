---
class: st pres c2
---

<script setup>
import ZoomablePlot from 'slidev-addon-ztautau/components/ZoomablePlot.vue'
</script>

# Calibration 2 · Step 6a: before and after scaling the simulation

<div class="st-sub">Simulated photon energy <LaTeX formula="\times\,k(E)" />, data untouched; both channels, <LaTeX formula="5\le E_\mathrm{pred}\lt46" /> GeV. Closure on the same events, statistical errors only.</div>

<div class="st-cols st-cols-21" style="gap:16px">
<div class="st-fig" style="height:300px"><ZoomablePlot src="/figures/photon-calibration/closure/closure_R_comb.png" alt="R per year: data, simulation before, after k(E), after binned k" /></div>
<div>
<table class="c2t num first-nw">
<thead><tr><th>Year</th><th><LaTeX formula="k" /> applied</th><th>Before</th><th>After</th></tr></thead>
<tbody>
<tr><td>1992</td><td><LaTeX formula="0.9812+0.0636\ln\frac{E}{10\,\mathrm{GeV}}" /></td><td><LaTeX formula="0.994\pm0.017" /></td><td><LaTeX formula="0.991\pm0.017" /></td></tr>
<tr><td>1993</td><td>1.0429</td><td><LaTeX formula="1.057\pm0.013" /></td><td><LaTeX formula="1.014\pm0.013" /></td></tr>
<tr><td>1994</td><td>0.9577</td><td><LaTeX formula="0.960\pm0.009" /></td><td><LaTeX formula="1.003\pm0.009" /></td></tr>
<tr><td>1995</td><td>1.0232</td><td><LaTeX formula="1.032\pm0.014" /></td><td><LaTeX formula="1.008\pm0.014" /></td></tr>
</tbody>
</table>
<div class="st-cap">Data/simulation peak ratio of <LaTeX formula="R" />. <LaTeX formula="E" /> = simulated photon energy, clipped to 5–46 GeV.</div>
<div class="co ok"><b>Figure</b> Dashed: before. Red: after <LaTeX formula="k(E)" />. Green: after binned <LaTeX formula="k" />.</div>
<div class="co warn"><b>Width</b> Not corrected: data stay <LaTeX formula="1.09" />–<LaTeX formula="1.44\times" /> wider.</div>
</div>
</div>

<div class="takeaway"><b>Takeaway</b> Before: 0.960–1.057. After scaling: 0.991–1.014, each year within <LaTeX formula="1.1\sigma" /> of 1; 1992 needs its <LaTeX formula="k(E)" />.</div>

<div class="st-source">Source: closure study of the version-2 <LaTeX formula="\ell^+\ell^-\gamma" /> run (2026-11-03), sections 2.1 and 3</div>

<!--
artifacts/llgamma-v2-20261103/closure/REPORT.md and closure.json (closure.py, sha1 46a9915e..., NERSC login node, wall 187 s, max RSS 110 MB; rows epred_rows.npz, 119,987 rows; calibration input epred/k_epred.json). Selection iso5 region bits; data = data; MC = Bhabha + Z_tautau (eeg), Z_mumu + Z_tautau (mumug); comb = both channels summed. Closure domain 5 <= E_pred < 46 GeV. Correction MC only: R_MC' = k R_MC (E_MC' = k E_MC), no smearing. Section 2.1 smooth calibrations (comb, k_fit): 1992 line a + b ln(clip(E,5,46)/10), a = 0.9812 +- 0.0107, b = 0.0636 +- 0.0179, cov(a,b) = -9.2e-5, p(slope) = 0.0004; 1993 constant 1.0429 +- 0.0100 (chi2 7.8/4); 1994 0.9577 +- 0.0075 (3.1/4); 1995 1.0232 +- 0.0104 (1.7/3). E = the MC photon's measured (uncalibrated) energy, not E_pred (deliberate: E_pred does not exist outside l+l-gamma). Section 3 comb, fit estimator: before (domain) 0.994 +- 0.017 / 1.057 +- 0.013 / 0.960 +- 0.009 / 1.032 +- 0.014; after smooth k(E) 0.991 +- 0.017 / 1.014 +- 0.013 / 1.003 +- 0.009 / 1.008 +- 0.014; after bin k(E_pred) 0.997 +- 0.017 / 1.011 +- 0.013 / 0.999 +- 0.009 / 1.012 +- 0.014; all years before 0.997 +- 0.006 -> 1.007 +- 0.006 (smooth); truncated mean before -> bin / smooth 0.987 -> 0.997 / 0.992; 1.060 -> 1.013 / 1.017; 0.965 -> 1.002 / 1.007; 1.038 -> 1.023 / 1.015. Largest residual in sigma: 1993 smooth (1.014 - 1) / 0.013 = 1.1 (derived). Width ratio after smooth per year: 1.202, 1.090, 1.435, 1.398 (range 1.09-1.44 shown); the report quotes 1.09-1.58 per year and channel. Figure closure/closure_R_comb.png: R in 0.04 bins, MC normalised to data in 0.6 < R < 1.4 (shape comparison only). Caveat (section 7): same-sample closure; the per-bin closure of the binned version is by construction. The all-years 'before' (0.997) is close to 1 only because per-year offsets of opposite sign cancel.
-->
