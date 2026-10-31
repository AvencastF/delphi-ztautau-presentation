---
class: st pres
---

# Caveats, and what comes next

<div class="st-cols st-cols-2">
<div>
<h3 style="margin:0 0 6px;font-size:15px;color:var(--nju-coral)">What these numbers are not yet</h3>
<div class="co open"><b>Simulation only</b> No data fit yet.</div>
<div class="co open"><b>Statistics only</b> No systematic uncertainties.</div>
<div class="co warn"><b>Reference <LaTeX formula="C_{kk}=1.03" /></b> Slightly unphysical: a systematic.</div>
<div class="co warn"><b>Fixed part</b> 12.6 % of events: no spin model.</div>
<div class="co warn"><b>Off-peak</b> Pooled with one average reference.</div>
<div class="co open"><b>Luminosity</b> Uncertified.</div>
</div>
<div>
<h3 style="margin:0 0 6px;font-size:15px;color:var(--nju-blue)">Next steps toward data</h3>
<ol class="steps" style="font-size:14.5px">
<li><b>Covariance</b> at the fitted point</li>
<li><b>Systematics</b> as nuisance parameters</li>
<li><b>Control regions</b> away from signal observables</li>
<li><b>Unblinding plan</b> witness and Bell tests fixed in advance</li>
</ol>
<div class="co decision"><b>Concurrence</b> Standard definition adopted.</div>
</div>
</div>

<div class="st-source">Source: caveat sections of the fit studies (2026-10-30/31) and the project rules; simulation only, statistics only</div>

<!--
artifacts/joint-fit-20261031/{summary.md, step2/*/summary.md, modelB/*, modelC/*}: Caveats. Statistics only: MC template statistics not included in the joint-fit models (legacy MC-stat study: ~1-2 %), no response/background/normalisation/analysing-power systematics; Asimov and toys use the MC reference as truth. C_kk(ref) = 1.0146 (1994) / 1.0307 (combined) > 1, rho at the reference has eigenvalue -0.010 / -0.013; unbinned reference identical; treatment as analysing-power systematic per the owner's brief (2026-10-31), not studied yet. The step-2 reweighting uses legacy average analysing powers (rho 0.41, e -0.33, mu -0.34): exact for the analytic f-model, approximate for real rho/lepton kinematics. Fixed: Ztautau_others 11.7 % + non-tau 0.9 % of MC (owner decision: no analysing power invented for 'other'). Legacy concurrence (step 1): uses eigenvalues of R instead of their square roots, differs from Wootters; slides quote the closed-form concurrence (|C_nn - C_rr| + C_kk - 1)/2. Pooled 1992-1995: one MC reference = luminosity-weighted average over sqrt s. Luminosity: run-quality tables (docs/PROJECT_GUIDE.md 2026-10-26), user-supplied, uncertified.
Next steps: data fit should use C_Vfit (V at the fitted point) or iterate (modelC summaries); coverage over many injected states; control regions per AGENTS.md (calibration and validation independent; do not tune spin correlations using signal observables); pre-registration of W and Bell before unblinding: proposed (owner's brief for this deck), not yet a recorded decision. These steps are proposals; no order has been decided by the owner.
-->
