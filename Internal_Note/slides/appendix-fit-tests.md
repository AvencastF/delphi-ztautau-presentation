---
class: st pres
---

<script setup>
import ZoomablePlot from 'slidev-addon-ztautau/components/ZoomablePlot.vue'
</script>

# Appendix · spin fit: test statistics under the null hypothesis

<div class="st-sub">Null hypothesis = closest separable (or Bell-local) state, found by a constrained fit to the expected data. Test statistic <LaTeX formula="q=\chi^2_{\mathrm{null}}-\chi^2_{\mathrm{free}}" />.</div>

<div class="st-fig" style="height:185px"><ZoomablePlot src="/figures/fit/modelC-q-null-witness.png" alt="witness test statistic under the null" /></div>
<div class="st-cap"><b>Witness test under the null</b>, 1992–1995: distribution, tail probability and quantiles of <LaTeX formula="q" /> against the textbook <LaTeX formula="\tfrac12\chi^2_1" /> (black); final model in blue</div>

<div class="st-cols st-cols-21" style="margin-top:8px">
<table class="num first-nw">
<thead><tr><th>Null toys, 1992–1995</th><th><LaTeX formula="q=0" /> fraction</th><th><LaTeX formula="P(q\gt 9)" /></th></tr></thead>
<tbody>
<tr><td>Textbook <LaTeX formula="\tfrac12\chi^2_1" /></td><td>0.500</td><td>0.0014</td></tr>
<tr><td>Eigenvalue test, legacy model</td><td>0.217</td><td>0.0075</td></tr>
<tr><td>Witness, legacy model</td><td>0.420</td><td>0.0030</td></tr>
<tr class="hl"><td>Witness, final model</td><td>0.496</td><td>0.0025</td></tr>
</tbody>
</table>
<div>
<div class="co decision"><b>Witness</b> Linear test replaces the eigenvalue test: stable, nearly textbook.</div>
<div class="co ok"><b>Tail</b> Slightly wider, predicted from the covariance shift.</div>
</div>
</div>

<div class="st-source">Source: hypothesis-test studies of 2026-10-31 (eigenvalue and witness tests, legacy and final models); simulation only, statistics only</div>

<!--
Null construction: c0 = argmin chi^2 (or -2lnL) subject to the null (W <= 0; |C_kk - C_rr| <= sqrt 2; for the eigenvalue test lambda_min(rho^T_B) >= 0), on the SM Asimov data; for model C the exact projection c0 = c_hat - g F^-1 a / (a^T F^-1 a). Null pseudo-data: simulation reweighted to c0, event-level Poisson; free and constrained fit per toy. Toys: model A step 2: 40,000 null toys per test (+ 4,000 at two alternative boundary points); model C: 20,000 null toys per test (+4,000 x 2 alternatives).
Numbers (combined): artifacts/joint-fit-20261031/step2/combined-ml/summary.md (lambda_min: q=0 fraction 0.217 +- 0.002, P(q>9) 0.0075; curvature of the separable boundary and noise in the off-diagonal C bias lambda_min low; tail depends on the null point: lowCkk q=0 0.027), witness_summary.md (W, model A: 0.4198, P(q>9) 0.0030; deviation = closure bias of the legacy model, W +0.048 = 0.204 sigma_null; owner decision 2026-10-31: W headline, lambda_min cross-check), modelC/combined-ml/summary.md (W, model C: 0.4959 +- 0.0035, P(q>9) 0.00250, mean q|q>0 1.146, predicted scale s = 1.154 because V is evaluated at c_ref rather than at the generation point; with V at the generation point (oracle) 0.4980, mean 1.007, KS p 0.90: textbook). Bell (model C): q=0 0.4979, mean q|q>0 1.043, KS p 0.16. 1/2 chi2_1 reference P(q>9) = 0.00135. Figure: modelC/combined-ml/q_null_witness_modelC.png; legacy-model version step2/combined-ml/q_null_witness.png (with lambda_min on the same toys) in the appendix.
-->
