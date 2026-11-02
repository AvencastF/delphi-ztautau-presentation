---
class: st pres tk
clicks: 18
---

<script setup>
import TalkCutflow from '../components/TalkCutflow.vue'
</script>

# Cutflows

<div class="cf-kicker">1992–1995 data</div>

<TalkCutflow :step="$clicks" />

<!--
Same counts as Internal_Note cutflow-anim.md: components/cutflow-by-process.json from data/nersc-all-years-rq-20261026/cutflows/cutflow.csv (job 60333695). Year ratios are data/total for that year at the current cut (JSON key "years"). Z_ee is not stacked. Start: 2,311,711 data / 7,225,090.6 MC; end: 56,472 / 57,520.1.
-->

<style>
.cf-kicker { margin: 0 0 6px; font-size: 16px; line-height: 1.3; color: var(--fg-0); font-weight: 500; }
</style>
