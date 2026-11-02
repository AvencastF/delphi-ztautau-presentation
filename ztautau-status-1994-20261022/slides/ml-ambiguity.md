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

<div class="st-source">Source: all-years neutrino evaluation on the hold half of the 1992–1995 simulation (2026-10-27); geometry schematic</div>

<!--
artifacts/ml-all-years-v1-20261027/nu-eval-hold.md (all years, hold half, mc_split unseen, 2,359,482 Z->tautau events): branch-sign accuracy inclusive analytical 0.591, analytical_best 0.910, nu 0.724 (1994 alone 0.746, nu-eval-year-1994.md); direction error medians per leg (e, mu, pi, rho): analytical 2.07/1.96/1.55/1.43, nu 1.18/1.11/0.88/0.98, best 1.37/1.28/0.71/0.79 deg; 84 condition channels (v5 layout + ecms + year one-hot). The 2026-10-22 version quoted the 1994-only v5 model (analytical 0.593, best 0.912, nu 0.740; nu 1.17/1.09/0.89/1.03 deg; 200,755 held-out events).
-->
