---
class: st pres
---

# What these numbers are not yet

<div class="st-cols st-cols-2">
<div>
<div class="co open"><b>Simulation only</b> No data fit yet.</div>
<div class="co open"><b>Statistics only</b> No systematic uncertainties.</div>
<div class="co warn"><b>Reference <LaTeX formula="C_{kk}=1.03" /></b> Slightly unphysical; an analysing-power systematic.</div>
<div class="co warn"><b>Fixed part</b> 12.6 % of events carry no spin model.</div>
</div>
<div>
<div class="co decision"><b>Concurrence</b> Legacy definition replaced by the standard one.</div>
<div class="co warn"><b>Off-peak</b> Points pooled with one average reference.</div>
<div class="co open"><b>Luminosity</b> Simulation weights use uncertified luminosities.</div>
<div class="co decision"><b>Before unblinding</b> Pre-register the witness and Bell tests.</div>
</div>
</div>

<div class="st-source">Source: caveat sections of the fit studies (2026-10-30/31) and the project rules; simulation only, statistics only</div>

<!--
artifacts/joint-fit-20261031/{summary.md, step2/*/summary.md, modelB/*, modelC/*}: Caveats. Statistics only: MC template statistics not included in the joint-fit models (legacy MC-stat study: ~1-2 %), no response/background/normalisation/analysing-power systematics; Asimov and toys use the MC reference as truth. C_kk(ref) = 1.0146 (1994) / 1.0307 (combined) > 1, rho at the reference has eigenvalue -0.010 / -0.013; unbinned reference identical; treatment as analysing-power systematic per the owner's brief (2026-10-31), not studied yet. The step-2 reweighting uses legacy average analysing powers (rho 0.41, e -0.33, mu -0.34): exact for the analytic f-model, approximate for real rho/lepton kinematics. Fixed: Ztautau_others 11.7 % + non-tau 0.9 % of MC (owner decision: no analysing power invented for 'other'). Legacy concurrence (step 1): uses eigenvalues of R instead of their square roots, differs from Wootters; reproduces the legacy 0.8054 exactly; slides now quote the closed-form concurrence (|C_nn - C_rr| + C_kk - 1)/2. Pooled 1992-1995: one MC reference = luminosity-weighted average over sqrt s; legacy pooled response with constant weight sumw/N (spread 0.3 % rms); model C uses the pooled reference too. Luminosity: run-quality tables (docs/PROJECT_GUIDE.md 2026-10-26), user-supplied, uncertified; residual 3.1 % / 2.3 % data deficit in 1994/1995. Pre-registration of W and Bell as the test axes before unblinding: proposed (owner's brief for this deck), not yet recorded as a decision in the project guide. AGENTS.md: keep all 15 coefficients; do not tune spin correlations on signal observables.
-->
