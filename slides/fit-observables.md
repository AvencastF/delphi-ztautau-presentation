---
class: st pres
---

# What is measured: the spin state of the <LaTeX formula="\tau" /> pair, 15 numbers

<div class="st-sub">Helicity frame: <LaTeX formula="k" /> along the <LaTeX formula="\tau" /> flight direction, <LaTeX formula="r" /> in the production plane, <LaTeX formula="n" /> normal to it.</div>

<div class="st-cols st-cols-2">
<div>
<div class="kv fit"><h3><span class="tag fit">fit</span> Spin density matrix</h3>
<div style="margin:4px 0 8px"><LaTeX formula="\rho=\tfrac14\Big(\mathbb 1\otimes\mathbb 1+\textstyle\sum_i B_{A,i}\,\sigma_i\otimes\mathbb 1+\sum_j B_{B,j}\,\mathbb 1\otimes\sigma_j+\sum_{ij}C_{ij}\,\sigma_i\otimes\sigma_j\Big)" /></div>
<dl>
<dt>Polarisations</dt><dd><LaTeX formula="B_{A,i},\,B_{B,i}" />, 6 numbers</dd>
<dt>Correlations</dt><dd><LaTeX formula="C_{ij},\ i,j\in\{n,r,k\}" />, 9 numbers</dd>
<dt>Read out by</dt><dd>decay-product directions, weighted by each channel's analysing power</dd>
</dl></div>
</div>
<div>
<table class="first-nw">
<thead><tr><th>Derived quantity</th><th>Definition</th><th>Meaning</th></tr></thead>
<tbody>
<tr><td>Witness</td><td><LaTeX formula="W=C_{nn}-C_{rr}+C_{kk}-1" /></td><td><LaTeX formula="W\gt 0" />: entangled</td></tr>
<tr><td>Concurrence</td><td><LaTeX formula="\tfrac12\big(|C_{nn}-C_{rr}|+C_{kk}-1\big)" /></td><td>amount of entanglement</td></tr>
<tr><td>Bell</td><td><LaTeX formula="|C_{kk}-C_{rr}|" /></td><td><LaTeX formula="\gt\sqrt2" />: violates Bell</td></tr>
<tr><td>Magic</td><td><LaTeX formula="-\log_2\frac{1+\sum c^4}{1+\sum c^2}" /></td><td>non-stabiliser content</td></tr>
</tbody>
</table>
<div class="co decision"><b>Goal</b> All 15 coefficients; the derived quantities follow from them.</div>
</div>
</div>

<div class="st-source">Source: method notes of the joint-fit code and the hypothesis-test study (2026-10-31)</div>

<!--
tau_analysis/joint_fit/README.md (model, tests) and artifacts/joint-fit-20261031/step2/combined-ml/witness_summary.md: W = C_nn - C_rr + C_kk - 1 (owner decision 2026-10-31: headline entanglement test; every separable two-qubit state has sum_i |C_ii| <= 1; the SM sign pattern C_nn > 0, C_rr < 0, C_kk > 0 picks this face). Closed-form concurrence of the X-state part (|C_nn - C_rr| + C_kk - 1)/2 (joint_fit/model_b.py conc_closed; = W/2 for the SM sign pattern; = -2 E_formula). Bell: |C_kk - C_rr| > sqrt 2 (best nominal combination of the six). lambda_min(rho^T_B) (E) is the cross-check. Magic: legacy compute_magic (quantum/observables_builder.py), -log2((1 + sum c^4)/(1 + sum c^2)) over the 15 B/C values (joint_fit/model_c.py). rho construction as coded in the legacy compute_full_density_matrix: k->sigma_x, r->sigma_y, n->sigma_z, B_B on the first factor, B_A on the second (step2 summary); the slide shows the generic form. Per-event estimators B_i = 3<h_i>, C_ij = 9<h-_i h+_j> with the charged track as analyser; analysing powers: pi 1, rho 0.41, e -0.33, mu -0.34 (legacy average values). The legacy concurrence (eigenvalues of R instead of their square roots, differs from Wootters) is superseded by the closed form / Wootters (joint-fit step 1).
-->
