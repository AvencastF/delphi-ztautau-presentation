---
class: st pres
clicks: 18
---

<script setup>
import CutflowBars from '../components/CutflowBars.vue'
</script>

# Applying the 18 cuts one after another

<div class="st-sub">Click to apply each cut. White: 1994 data; blue: signed simulation total without <LaTeX formula="Z\to ee" />; log scale.</div>

<CutflowBars :step="$clicks" />

<div class="st-source">Source: count table of the frozen 2026-10-12 selection run; exact signed sums in the data folder</div>

<!--
NERSC analysis-runs/1994/all-event-detector-1994-20261012/cutflows/cutflow.csv rows "1994/data" and "1994/Total MC (Z_ee excluded)", copied to data/nersc-all-event-detector-1994-20261012/ (sha256 00e203ca...). Simulation normalised with the uncertified 46.301362 pb-1. The simulation starts far above the data because the Z_qq and Bhabha samples are much larger than their selected fraction.
-->
