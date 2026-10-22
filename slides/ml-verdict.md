---
class: st pres
---

<script setup>
import NJUPlot from '../components/NJUPlot.vue'
</script>

# Machine-learning verdict, as recorded 2026-10-21/22

<div class="st-cols st-cols-2">
<div>
<div class="co ok"><b>Equal</b> v5 = v2 within statistics on every metric.</div>
<div class="co ok"><b>Better</b> v5 beats v3 and v4 on e, μ, ρ legs and every branch accuracy.</div>
<div class="co warn"><b>Exception</b> π legs in ππ: v5 0.75° vs v3 0.61°.</div>
<div class="co warn"><b>Not supported</b> FiLM did not exploit the cone photon information.</div>
<div class="co decision"><b>Decisions</b> v5 baseline (10-21); classifier retrain on shared inputs pending (10-22).</div>
<div class="co open"><b>Open</b> Closure only; no test part, no systematics, no data validation.</div>
</div>
<div>
<div class="st-fig" style="height:150px"><NJUPlot src="/figures/ml/v5/10_overview.svg" alt="v5 overview per channel" /></div><div class="st-cap">Overview per channel, version 5: bias, width, correlation, branch accuracy</div>
<div class="st-fig" style="height:150px;margin-top:6px"><NJUPlot src="/figures/ml/v2/10_overview.svg" alt="v2 overview per channel" /></div><div class="st-cap">The same overview for version 2</div>
</div>
</div>

<div class="st-source">Source: verdict section of the v5 archive and the 1994 runbook (ML stage)</div>

<!--
artifacts/neutrino-ml-v5-20261021/README.md "Verdict": direction errors agree within 0.02 deg per leg type and channel; branch accuracies within +-0.011 (largest 1.8 sigma, mumu -0.011 +- 0.006); residual widths and correlations within 0.005; pipi closure sigma equal to v4 or better (1.00-1.11), equal to v3 within +-4 % except C_kk (v3 0.87 of v5). Option: channel-specific cone-target model for pipi (owner decision, not demonstrated). docs/RUNBOOK_1994.md section 4: skim-cls-nu replaces skim-cls-nu-v5 once the shared-input classifier is accepted. Concurrence bias +0.165 +- 0.185 compatible with zero at split statistics. Analyser legs e, mu, rho not corrected for analysing power.
-->
