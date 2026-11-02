---
class: st pres
---

# From decays to numbers: each decay is a spin analyser

<div class="st-sub">Axes per <LaTeX formula="\tau" />: <LaTeX formula="k" /> along its flight, <LaTeX formula="r" /> perpendicular to it in the plane of beam and <LaTeX formula="\tau" />, <LaTeX formula="n" /> out of that plane.</div>

<div class="st-cols st-cols-2">
<div>
<svg viewBox="0 0 380 190" style="width:100%;height:190px" role="img" aria-label="Helicity frame: k along the tau direction, r in the production plane, n normal to it.">
<defs><marker id="fo-a" markerWidth="8" markerHeight="8" refX="6" refY="4" orient="auto"><path d="M0 0 L8 4 L0 8 z" fill="#c9e86a"/></marker></defs>
<line x1="20" y1="150" x2="360" y2="150" stroke="#6b7280" stroke-width="1.2" stroke-dasharray="4 4"/><text x="300" y="168" style="font-size:13px" fill="#bcc2cb">beam</text>
<line x1="150" y1="150" x2="300" y2="70" stroke="#bcc2cb" stroke-width="1.6"/><text x="306" y="66" style="font-size:16px" fill="#f0f1f3">τ</text>
<line x1="210" y1="118" x2="282" y2="80" stroke="#c9e86a" stroke-width="2.4" marker-end="url(#fo-a)"/><text x="262" y="102" style="font-size:17px" fill="#c9e86a">k</text>
<line x1="210" y1="118" x2="172" y2="46" stroke="#c9e86a" stroke-width="2.4" marker-end="url(#fo-a)"/><text x="160" y="56" style="font-size:17px" fill="#c9e86a">r</text>
<line x1="210" y1="118" x2="236" y2="160" stroke="#c9e86a" stroke-width="2.4" marker-end="url(#fo-a)"/><text x="244" y="170" style="font-size:17px" fill="#c9e86a">n</text>

</svg>
<table class="num first-nw">
<thead><tr><th>Decay</th><th><LaTeX formula="\pi\nu" /></th><th><LaTeX formula="\rho\nu" /></th><th><LaTeX formula="e\nu\nu" /></th><th><LaTeX formula="\mu\nu\nu" /></th></tr></thead>
<tbody><tr><td>Analysing power</td><td>1.00</td><td>0.41</td><td><LaTeX formula="-0.33" /></td><td><LaTeX formula="-0.34" /></td></tr></tbody>
</table>
<div class="st-cap">How strongly the decay direction follows the spin (1 = perfectly; sign = along or against).</div>
</div>
<div>
<div class="tiles tiles-2" style="margin-top:0">
<div class="tile ml" style="border-top-color:#c9e86a"><b>6</b><span>polarisations <LaTeX formula="B" />: each <LaTeX formula="\tau" /> along <LaTeX formula="n,r,k" /></span></div>
<div class="tile ml" style="border-top-color:#c9e86a"><b>9</b><span>correlations <LaTeX formula="C_{ij}" />: <LaTeX formula="\tau^-" /> axis <LaTeX formula="i" /> with <LaTeX formula="\tau^+" /> axis <LaTeX formula="j" /></span></div>
</div>
<div class="co ok"><b>15 numbers</b> describe the spin state of the pair completely.</div>
<div class="co ok"><b>Read out</b> Averages of decay-angle products, divided by the analysing powers.</div>
<div class="co decision"><b>Goal</b> All 15; entanglement and Bell tests follow from them.</div>
</div>
</div>

<div class="st-source">Source: method notes of the joint-fit code and of the legacy fit (analysing powers); schematic frame</div>

<!--
tau_analysis/joint_fit/README.md (model, tests) and artifacts/joint-fit-20261031/step2/combined-ml/witness_summary.md. Spin density matrix rho = 1/4 (1x1 + sum_i B_A,i sigma_i x 1 + sum_j B_B,j 1 x sigma_j + sum_ij C_ij sigma_i x sigma_j); rho construction as coded in the legacy compute_full_density_matrix: k->sigma_x, r->sigma_y, n->sigma_z, B_B on the first factor, B_A on the second (step2 summary). Per-event estimators B_i = 3<h_i>, C_ij = 9<h-_i h+_j> with the charged track as analyser; analysing powers pi 1, rho 0.41, e -0.33, mu -0.34 (legacy average values; the step-2 reweighting uses them: exact for the analytic f-model, approximate for real rho/lepton kinematics). Helicity frame: k along the tau flight direction, r in the production plane, n normal to it (previous slide text). Derived quantities: witness W = C_nn - C_rr + C_kk - 1 (owner decision 2026-10-31: headline entanglement test); concurrence (|C_nn - C_rr| + C_kk - 1)/2; Bell |C_kk - C_rr| > sqrt 2; magic -log2((1 + sum c^4)/(1 + sum c^2)). The axis sketch is schematic.
-->
