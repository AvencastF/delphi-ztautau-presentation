---
class: st pres
clicks: 3
---

<script setup>
import TauAmbiguity from '../components/TauAmbiguity.vue'
</script>

# The <LaTeX formula="\tau" /> direction is ambiguous from kinematics alone

<div class="st-sub">Click through: visible leg <LaTeX formula="\to" /> cone <LaTeX formula="\to" /> two mirror solutions <LaTeX formula="\to" /> the ML prediction.</div>

<TauAmbiguity :step="$clicks" />

<div class="st-source">Source: version-5 neutrino evaluation on held-out simulation; geometry schematic</div>

<!--
artifacts/neutrino-ml-v5-20261021/eval/summary.md: branch-sign accuracy inclusive analytical 0.593, analytical_best 0.912, nu 0.740; direction error medians per leg (e, mu, pi, rho): analytical 2.09/1.96/1.52/1.41, nu 1.17/1.09/0.89/1.03, best 1.38/1.28/0.69/0.77 deg. 200,755 held-out Z->tautau events.
-->
