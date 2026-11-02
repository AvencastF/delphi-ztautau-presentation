---
class: st pres
---

# Why reweighted simulation: the detector is inside the prediction

<div class="st-sub">The same simulated events predict every reconstructed bin for any spin state. No unfolding.</div>

<svg viewBox="0 0 880 120" style="width:100%;height:120px" role="img" aria-label="Simulated event: true decay angles give a weight for the chosen spin state; the reconstructed event fills the histograms with that weight.">
<g style="font-size:13px" fill="#f0f1f3" text-anchor="middle">
<rect x="10" y="20" width="250" height="70" rx="6" fill="#23262b" stroke="#f0c36e"/><text x="135" y="48">simulated event</text><text x="135" y="70" style="font-size:11px" fill="#bcc2cb">true decay angles known</text>
<rect x="315" y="20" width="250" height="70" rx="6" fill="#23262b" stroke="#c9e86a"/><text x="440" y="48">weight for a spin state</text><text x="440" y="70" style="font-size:11px" fill="#bcc2cb">how its angles respond to each coefficient</text>
<rect x="620" y="20" width="250" height="70" rx="6" fill="#23262b" stroke="#77c9ff"/><text x="745" y="48">reconstructed histograms</text><text x="745" y="70" style="font-size:11px" fill="#bcc2cb">filled with that weight</text>
</g>
<g stroke="#bcc2cb" stroke-width="1.6" fill="none"><path d="M262 55 H310 M302 49 L310 55 L302 61"/><path d="M567 55 H615 M607 49 L615 55 L607 61"/></g>
</svg>

<div class="st-cols st-cols-3" style="margin-top:8px">
<div class="co ok"><b>No unfolding</b> Efficiency, resolution, mis-identification: all included.</div>
<div class="co ok"><b>Linear</b> Straight line in each coefficient: solved exactly.</div>
<div class="co ok"><b>Checked</b> Against the legacy one-observable-per-coefficient fit.</div>
</div>

<div style="margin-top:6px;font-size:13px;color:var(--fg-1)">Prediction: <LaTeX formula="\mu(\mathbf c)=\mu_{\mathrm{MC}}+\textstyle\sum_{m=1}^{15}(c_m-c_m^{\mathrm{MC}})\,T_m" />, with <LaTeX formula="T_m" /> the reweighted template of coefficient <LaTeX formula="m" />.</div>

<div class="st-source">Source: method notes of the joint-fit code, final model (owner decision 2026-10-31); simulation only</div>

<!--
tau_analysis/joint_fit/README.md "Model C" (owner decision 2026-10-31: target model): mu(delta) = H_MC + sum_m delta_m T_m, H_MC = sum_i w_i s_i, T_m = sum_{i floating} w_i X_im / f_eff,i s_i, f_eff = max(f(Omega_i; c_ref), 0.02) (floor; no reco row affected, min f(c_ref) 0.059 (1994) / 0.028 (combined)); floating rows = Z->tautau with matched finite truth and both channels in {pi, rho, e, mu}; fixed = non-tau backgrounds and Ztautau_others. Reference = legacy MC reference (C_kk = 1.015 for 1994, 1.031 combined). chi2 = (n - mu)^T V^-1 (n - mu); V_ab = sum_i w_i 1[i in a] 1[i in b] (Poisson per event), block-diagonal over 16 regions (150 x 150), 2176 of 2400 bins kept (exact null space), no ridge. GLS: F = X^T V^-1 X, Cov = F^-1, closed form; iminuit MIGRAD/HESSE agrees to 4.9e-5 (relative sigma). For data: V at the fitted point (C_Vfit) or iterated.
History: model A = legacy forward folding (ForwardFoldingProcessor, byte-identical copy of lep_tree_ana; one observable per coefficient through response matrices at the SM point); model B = reweighted templates with a product Poisson likelihood (exact closure, invalid errors); model C = B's templates + full covariance. "Agrees with the legacy fit": model A reproduced by the new numpy code to 1e-11 events; model C errors 0.94-0.99 of model A for 13 coefficients, C_nr/C_rn 1.07 (appendix: three models compared, precision).
-->
