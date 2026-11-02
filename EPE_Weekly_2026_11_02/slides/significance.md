---
class: st pres tk fit-section fit-qis-summary
---

# Quantum-correlation sensitivity

<div class="st-sub">Asimov reference · statistical only · 2,000 reference toys / 20,000 toys per null test</div>

<div class="fit-qis-methods">
<div><b>Covariance propagation</b><LaTeX formula="\sigma_O^2=\mathbf g_O^T\Sigma\mathbf g_O,\quad\mathbf g_O=\nabla_{\mathbf c}O" /><small><LaTeX formula="\Sigma" />: full coefficient covariance; gradient at the reference.</small></div>
<div><b>Null-test calibration</b><LaTeX formula="q=\chi^2_{\rm null}-\chi^2_{\rm free},\quad p=P_{H_0}(q\ge q_{\rm A})" /><small><LaTeX formula="q_{\rm A}" />: Asimov statistic; significance from the null tail.</small></div>
</div>

<table class="fit-table">
<thead><tr><th>Observable</th><th>Asimov <LaTeX formula="\pm\sigma_{\rm prop}" /></th><th><LaTeX formula="\sigma_{\rm toys}" /></th><th>Null hypothesis</th><th>Toy tail / interval</th><th>Expected <LaTeX formula="Z" /></th></tr></thead>
<tbody>
<tr><th>Witness <LaTeX formula="W" /></th><td><LaTeX formula="1.641\pm0.220" /></td><td>0.224</td><td><LaTeX formula="W\le0" /></td><td>0 / 20,000<br/><small>Calibrated extrapolation</small></td><td><LaTeX formula="7.00\,\sigma" /></td></tr>
<tr><th>Bell <LaTeX formula="\mathcal B" /></th><td><LaTeX formula="1.844\pm0.189" /></td><td>0.190</td><td><LaTeX formula="\mathcal B\le\sqrt2" /></td><td>265 / 20,000<br/><small><LaTeX formula="p=1.325\%" /></small></td><td><LaTeX formula="2.22\,\sigma" /></td></tr>
<tr><th>Magic <LaTeX formula="\mathcal M_2" /></th><td><LaTeX formula="0.196\pm0.181" /></td><td>0.190</td><td>Calibration pending</td><td><LaTeX formula="[-0.205,\,0.540]" /><br/><small>Reference-toy 95% interval</small></td><td>—</td></tr>
</tbody>
</table>

<div class="fit-qis-definitions">
<section><h2>Entanglement witness</h2><LaTeX formula="W=C_{nn}-C_{rr}+C_{kk}-1" /><p>Exact linear propagation.<br/><LaTeX formula="W&gt;0" /> certifies entanglement.</p></section>
<section><h2>Restricted Bell test</h2><LaTeX formula="\mathcal B=|C_{kk}-C_{rr}|" /><p>Locally linear; fixed sign.<br/>Fixed helicity axes; not optimised CHSH.</p></section>
<section><h2>Quantum magic</h2><LaTeX formula="\mathcal M_2=-\log_2\frac{1+\sum_m c_m^4}{1+\sum_m c_m^2}" /><p>Nonlinear; numerical gradient.<br/>Physical-state and null treatment pending.</p></section>
</div>
<div class="fit-band">Toy and propagated widths agree closely; expected witness sensitivity exceeds the restricted Bell sensitivity.</div>

<!-- Merged previous slides31–32. All numerical results and distinctions retained; source is archived combined-ml Model C. -->
