---
class: st pres c2
---

<script setup>
import ZoomablePlot from 'slidev-addon-ztautau/components/ZoomablePlot.vue'
</script>

# Calibration 2 · Version 3: resolution — the extra smearing of the simulation

<div class="st-sub">Top: width ratio <LaTeX formula="\sigma_\mathrm{data}/\sigma_\mathrm{sim}" /> of the <LaTeX formula="R" /> peak. Bottom: excess <LaTeX formula="(\sigma/\mu)^2_\mathrm{data}-(\sigma/\mu)^2_\mathrm{sim}" /> fitted to <LaTeX formula="(a/\sqrt{E})^2+b^2" />; dashed: DELPHI 98-160, <LaTeX formula="0.2/\sqrt{E}" />.</div>

<div class="st-fig" style="height:110px"><ZoomablePlot src="/figures/photon-calibration/v3/width_ratio_fit_vs_epred.png" alt="sigma_data / sigma_MC versus E_pred per year and all years" /></div>
<div class="st-fig" style="height:110px;margin-top:2px"><ZoomablePlot src="/figures/photon-calibration/v3/resolution_excess_variance.png" alt="excess relative variance data minus MC versus mean MAIN energy, with fits and the DELPHI 0.2/sqrt(E) curve" /></div>

<table class="c2t num first-nw" style="margin-top:6px">
<thead><tr><th>Sample</th><th>all, <LaTeX formula="d^2E" /></th><th>all, <LaTeX formula="5^\circ" /></th><th>1992</th><th>1993</th><th>1994</th><th>1995</th></tr></thead>
<tbody>
<tr><td><LaTeX formula="a" /> [<LaTeX formula="\sqrt{\mathrm{GeV}}" />]</td><td><LaTeX formula="0.293\pm0.025" /></td><td><LaTeX formula="0.262\pm0.025" /></td><td>0 (UL 0.13)</td><td><LaTeX formula="0.22\pm0.06" /></td><td><LaTeX formula="0.20\pm0.05" /></td><td><LaTeX formula="0.47\pm0.05" /></td></tr>
<tr><td><LaTeX formula="b" /></td><td>0 (UL 0.038)</td><td>0 (UL 0.042)</td><td><LaTeX formula="0.075\pm0.014" /></td><td><LaTeX formula="0.062\pm0.021" /></td><td><LaTeX formula="0.058\pm0.017" /></td><td>0</td></tr>
<tr><td><LaTeX formula="\chi^2/\mathrm{ndf}" /></td><td>9.8/7</td><td>10.5/7</td><td>20.4/6</td><td>2.6/7</td><td>10.8/7</td><td>6.7/7</td></tr>
<tr class="hl"><td><LaTeX formula="a" /> only (<LaTeX formula="\chi^2" />)</td><td><LaTeX formula="0.281\pm0.015" /> (10.1/8)</td><td><LaTeX formula="0.257\pm0.015" /> (10.6/8)</td><td><LaTeX formula="0.154\pm0.040" /> (27.3/7)</td><td><LaTeX formula="0.286\pm0.028" /> (4.8/8)</td><td><LaTeX formula="0.258\pm0.021" /> (13.8/8)</td><td><LaTeX formula="0.347\pm0.031" /> (12.5/8)</td></tr>
</tbody>
</table>
<div class="st-cap">Per-year columns: <LaTeX formula="d^2E" />. A constant alone fails for all years (<LaTeX formula="b" /> = 0.076, 44.5/8).</div>

<div class="takeaway"><b>Takeaway</b> Data are <LaTeX formula="1.1" />–<LaTeX formula="1.5\times" /> wider than simulation above 3 GeV. The excess is a pure stochastic term, <LaTeX formula="\sigma/E=(0.28\pm0.02)/\sqrt{E}" /> with no constant: DELPHI's form, 40 % larger. Per year <LaTeX formula="a" /> and <LaTeX formula="b" /> are not separated.</div>

<div class="st-source">Source: version-3 <LaTeX formula="\ell^+\ell^-\gamma" /> calibration report (2026-11-04), section 6, and its resolution table</div>

<!--
artifacts/llgamma-v3-20261104/REPORT.md section 6: sigma_data/sigma_MC of the GaussExp core is 1.1-1.5 in almost every bin above 3 GeV, every year, both isolations (figures/width_ratio_fit_vs_epred.png: v3 d2E red, v3 5 deg green, v2 raw blue/purple; open = truncated). Excess (sigma/mu)^2_data - (sigma/mu)^2_MC fitted to (a/sqrt(E))^2 + b^2 with E the mean MAIN energy of the bin (figures/resolution_excess_variance.png; dashed (0.2/sqrt(E))^2 from DELPHI 98-160). Table copied from REPORT section 6 (and tables.md "Resolution"): all years d2E a 0.293 +- 0.025, b 0 (95 % UL 0.038; fitted -0.0008 +- 0.0014), 9.8/7 (p 0.2), a only 0.281 +- 0.015 (10.1/8), b only 0.076 (44.5/8, p 4.5e-07); all years 5 deg 0.262 +- 0.025, b 0 (UL 0.042), 10.5/7, a only 0.257 +- 0.015 (10.6/8), b only 0.069 (37.7/8); 1992 d2E a 0 (UL 0.13; fitted -0.0127 +- 0.0186, 95 % UL 0.134), b 0.075 +- 0.014, 20.4/6, a only 0.154 +- 0.040 (27.3/7), b only 0.068 (20.8/7); 1993 0.22 +- 0.06 (tables 0.223 +- 0.060), 0.062 +- 0.021, 2.6/7, a only 0.286 +- 0.028 (4.8/8), b only 0.088 (6.1/8); 1994 0.20 +- 0.05 (0.202 +- 0.046), 0.058 +- 0.017, 10.8/7, a only 0.258 +- 0.021 (13.8/8), b only 0.082 (15.6/8); 1995 0.47 +- 0.05 (0.470 +- 0.050), b 0 (fitted -0.0085 +- 0.0035), 6.7/7, a only 0.347 +- 0.031 (12.5/8), b only 0.079 (28.9/8). Summary value (REPORT section 1): extra MC smearing sigma/E = (0.28 +- 0.02)/sqrt(E), no constant term (all years, both isolations). "40 % larger" (REPORT section 7: "same form, 40 % larger"; 0.28/0.2 = 1.4, derived). Whether 98-160's sigma is absolute or relative is not stated in that note. Per year (REPORT section 6): 1993, 1994 accept either form; 1992 prefers a constant 7 %; 1995 a large stochastic term. Caveat: core widths are Hessian errors of fits that describe MC poorly at MC precision, as in v2. Intrinsic HPC resolution not measured here (E_pred resolution enters R).
-->
