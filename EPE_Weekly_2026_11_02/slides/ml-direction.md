---
class: st pres tk tk-academic
clicks: 3
---

# Neutrino: resolving the ambiguity

<DecayAmbiguity :step="$clicks" />

<!--
Three-click explanation: 0 two hadronic single-neutrino cone constraints at beam energy and back-to-back tau pair; 1 equal-weight mirror ambiguity and squared-loss conditional mean (not diffusion mode collapse); 2 finite flight and track displacement, only normal component necessarily flips under mirror reflection; 3 conditional inference and measured full-model branch accuracy. Cone geometry is computed as intersecting unit-sphere small circles; second visible cone is reflected to express both constraints on the same tau direction. Displacement illustration is a separate side-view schematic, not an event or measured resolution. b=L-(L.u)u, so b.n=L.n when u lies in the mirror plane. Source: converter/features.py impact_vector and lead_track_globals; D uses unit normal. The full-model performance is not an IP-only ablation. Removed hybrid and truth-aided rows as requested. The simplistic claims that only IP can ever distinguish solutions, every IP component flips, and diffusion must average the targets are not asserted. Detector numerical resolution/lifetime figures and year-dependent causal attribution are omitted without supporting analysis. Branch values: nu-eval-hold.md / metrics JSON, analytical .591/.501; nu .724/.735, inclusive/pipi respectively, method-valid cohorts. Public geometry reference: Physics of tau leptons, CERN-PPE/95-147 (https://cds.cern.ch/record/290480/files/ppe-95-147.pdf); DELPHI lifetime study hep-ex/0410010. No footnotes on slide.
-->
