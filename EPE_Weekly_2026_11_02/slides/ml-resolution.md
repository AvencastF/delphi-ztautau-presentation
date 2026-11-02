---
class: st pres tk tk-academic
---

# Neutrino: reconstruction resolution

<div class="st-sub">1992–1995 held-out simulation · method-valid events · smaller error is better</div>
<NeutrinoResolutionCharts />
<div class="nu-metric-defs"><section><h2>Median: typical error</h2><p>Half the reconstructed directions lie<br/>within this angle of the true direction.</p></section><section><h2>84% containment: tail size</h2><p>84% of reconstructed directions lie<br/>within this angle of the true direction.</p></section><section><h2>RMS: momentum spread</h2><p><LaTeX formula="\tau^-" /> residual spread about its mean.<br/>Evaluated within <LaTeX formula="[-6,6]\,\mathrm{GeV}" />.</p></section></div>


<!--
Source artifacts/ml-all-years-v1-20261027/nu-eval-hold-metrics.json angle.inclusive and four_momentum.inclusive.{analytical,nu}.minus; table angular values match nu-eval-hold.md. RMS calculated from weighted histogram bin centres about their weighted mean in evaluate_neutrino.py residual_stats, P4_EDGES linspace(-6,6,61). It is a bounded histogram standard deviation, not unbounded root mean squared residual. All values rounded2decimals. Method-valid leg counts differ, e.g. pi analytical336964 vsML596279; do not infer matched-event causal decomposition. Hybrid is same analytical population. Existing source does not supply individual-neutrino resolution. No invented distributions or Gaussian fits. Historical1994 target-frame study (Internal_Note/ml-nu-compare) found little added-cone-global gain; do not attribute performance solely to FiLM.
-->
