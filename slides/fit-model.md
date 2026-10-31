---
class: st pres
---

# The fit model: reweighted simulation, linear in the 15 coefficients

<div class="st-sub">No unfolding. The simulation itself predicts every reconstructed bin for any spin state.</div>

<div class="st-cols st-cols-2">
<div>
<div class="kv fit"><h3><span class="tag fit">fit</span> Expectation</h3>
<div style="margin:2px 0 8px"><LaTeX formula="\mu(\mathbf c)=\mu_{\mathrm{MC}}+\textstyle\sum_{m=1}^{15}(c_m-c_m^{\mathrm{MC}})\,T_m" /></div>
<dl>
<dt>Base</dt><dd>all simulated events, binned as reconstructed</dd>
<dt>Templates <LaTeX formula="T_m" /></dt><dd>the same events, each weighted by how its true decay angles respond to coefficient <LaTeX formula="m" /></dd>
<dt>Fixed part</dt><dd>other modes and non-<LaTeX formula="\tau" /> background</dd>
</dl></div>
</div>
<div>
<div class="kv fit"><h3><span class="tag fit">fit</span> Likelihood</h3>
<div style="margin:2px 0 8px"><LaTeX formula="\chi^2=(\mathbf n-\mu)^{\mathsf T}\,V^{-1}(\mathbf n-\mu)" /></div>
<dl>
<dt>Covariance <LaTeX formula="V" /></dt><dd>full bin-to-bin, because each event fills all 15 histograms</dd>
<dt>Solution</dt><dd>closed form; errors exact for a linear model</dd>
<dt>For data</dt><dd><LaTeX formula="V" /> recomputed at the fitted point</dd>
</dl></div>
</div>
</div>

<div class="co ok" style="margin-top:10px"><b>Reference</b> Validated against the legacy forward-folding fit: one observable per coefficient through response matrices.</div>

<div class="st-source">Source: method notes of the joint-fit code, final model (owner decision 2026-10-31); simulation only</div>

<!--
tau_analysis/joint_fit/README.md "Model C" (owner decision 2026-10-31: target model): mu(delta) = H_MC + sum_m delta_m T_m, H_MC = sum_i w_i s_i, T_m = sum_{i floating} w_i X_im / f_eff,i s_i, f_eff = max(f(Omega_i; c_ref), 0.02) (floor; no reco row affected, min f(c_ref) 0.059 (1994) / 0.028 (combined)); floating rows = Z->tautau with matched finite truth and both channels in {pi, rho, e, mu}; fixed = non-tau backgrounds and Ztautau_others. Reference = legacy MC reference (C_kk = 1.015 for 1994, 1.031 combined). V_ab = sum_i w_i 1[i in a] 1[i in b] (Poisson per event), block-diagonal over 16 regions (150 x 150), exact 14-dim null space per block handled by dropping one bin per observable k >= 1 (2176 of 2400 bins kept), no ridge, condition numbers ~5e3. GLS: F = X^T V^-1 X, Cov = F^-1, delta_hat = F^-1 X^T V^-1 r0. Data fit: V at the fitted point (C_Vfit, one iteration) or iterated.
History: model A = legacy forward folding (ForwardFoldingProcessor, byte-identical copy of lep_tree_ana; 16 regions x 15 observables, each coefficient from its own observable through a response matrix built at the SM point; product Poisson likelihood); reproduced by the new numpy code to 1e-11 events. Model B = reweighted templates with a product Poisson likelihood over all 15 histograms: exact closure but counts each event up to 15 times (pull widths up to 2.3) -> invalid errors. Model C = B's templates + GLS with the full covariance.
-->
