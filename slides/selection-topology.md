---
class: st pres
clicks: 3
---

<script setup>
import HemisphereSketch from '../components/HemisphereSketch.vue'
</script>

# How an event is split: thrust axis, hemispheres, leading tracks

<div class="st-sub">Click through. H0 / H1 are geometric hemispheres; the leading track is the highest-momentum track per side.</div>

<HemisphereSketch :step="$clicks" />

<div class="st-source">Source: the analysis code (thrust and hemisphere variables) and the selection hand-over note</div>

<!--
tau_analysis/analysis/physics.py function variables: thrust of accepted charged tracks; H0 = p.axis < 0, H1 = p.axis >= 0; axis orientation: largest absolute component positive; leading track = highest |p| per hemisphere. Handoff: H0/H1 are not tau charge labels. Sketch is schematic.
-->
