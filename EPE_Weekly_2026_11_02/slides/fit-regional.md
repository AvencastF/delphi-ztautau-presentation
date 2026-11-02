---
class: st pres tk fit-section fit-regional-explained
---

# Regional statistical contributions

<div class="st-sub">Share of the combined fit variance [%] · each column sums to 100%</div>

<div class="fit-regional-grid">
<div><img class="fit-region-plot" src="/figures/fit/region-budget.svg" alt="Region-by-region fractions of the combined estimator variance for polarisation, diagonal correlations and the witness" /><div class="fit-cov-caption">Charge-conjugate regions grouped</div></div>
<div class="fit-copy">
<h2>Definition</h2>
<p>Fluctuate events in one region;<br/>hold other regions fixed.<br/>Refit with the same combined estimator.</p>
<div class="fit-equation"><LaTeX formula="f_r=\frac{\text{variance from region }r}{\text{total variance}}" /></div>
<h2>Example: witness</h2>
<p><LaTeX formula="\pi\pi" /> fluctuations account for <b>46.5%</b> of the combined <LaTeX formula="W" /> variance.</p>
<h2>Interpretation</h2>
<p>Larger share: stronger statistical influence.<br/>Not the precision loss on removing the region.</p>
</div>
</div>

<!--
Exact decomposition for fixed-weight linear GLS: Cov_r(c_hat)=Sigma F_r Sigma;
for observable O with gradient g, variance_r=g^T Sigma F_r Sigma g.
The one-region fluctuation description defines the same analytic quantity; no extra region toys were run.
Not a standalone-region fit error, nor a leave-one-region-out sensitivity ranking.
-->
