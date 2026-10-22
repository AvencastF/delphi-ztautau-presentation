---
class: st pres
---

# Conventions used in every plot

<div class="st-cols st-cols-2">
<div>
<ul class="bl">
<li><b>Inclusive:</b> H0 / H1 are geometric, not <LaTeX formula="\tau" /> charges</li>
<li><b>Mixed children:</b> cand. 0 = first species in the name</li>
<li><b>Same species:</b> cand. 0 negative, cand. 1 positive</li>
<li><b>Same-sign pairs:</b> kept, ordering state "unavailable"</li>
</ul>
</div>
<div>
<ul class="bl">
<li><b>Neutral counts:</b> all, photons, non-photons, per side</li>
<li><b>Cones:</b> <LaTeX formula="\Delta R\lt 0.1" /> / 0.3 / 0.5</li>
<li><b>True species:</b> stored link first, <LaTeX formula="\Delta R\lt 0.05" /> fallback</li>
</ul>
</div>
</div>

<div class="co warn"><b>Spin</b> H0/H1 is no charge assignment; ML uses <LaTeX formula="\tau^+" /> first.</div>

<div class="st-source">Source: the selection hand-over note (particle diagnostics and neutral-count definitions)</div>

<!--
EXCLUSIVE_DECAY_HANDOFF_20261007.md "Canonical configuration", "Identified-particle diagnostics", "Neutral-count diagnostics" (owner definition 2026-10-07): inclusive arrays two entries per event H0 then H1; children four scalar counts per candidate; "failed photon ID" = every reconstructed neutral not selected by the resolved PHOT/unique-HPC working point incl. objects without PHOT tag. Histogram truth labels unordered; cutflow tau sub-samples ordered (epi and pie both present). Truth matching: structurally valid stored sDST_TBL_RecoToGen association first, fallback unique charge-compatible generator leaf at dR<0.05; matching never filters events. Thrust axis orientation: largest absolute component positive (physics.py).
-->
