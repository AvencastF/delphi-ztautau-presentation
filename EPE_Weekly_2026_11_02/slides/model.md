---
class: st pres tk tk-academic
clicks: 1
---

# EveNet: adaptation to DELPHI

<div class="ev-animation-input"><span><b>Up to 24 particles</b> · 12 per hemisphere</span><LaTeX formula="[E,p_T,\eta,\phi,t_0,t_1,q]" /><span>Tag slots: PID · calorimeter · lifetime</span></div>
<DelphiAnimatedEveNet :step="$clicks" />
<div class="ev-animation-details"><div><b>FiLM conditioning</b><span>Feature-wise linear modulation<br/>Lifetime · cone photons / masses · branch discriminant · <LaTeX formula="\sqrt{s}" /> · year</span></div><div><b>Diffusion target</b><span><LaTeX formula="(\delta\theta,\delta\phi)" /> per <LaTeX formula="\tau" /><br/>Relative to the saved leading track</span></div></div>
<div class="ev-publication">Hsu, T.-H., Zhou, B., Liu, Q. <i>et al.</i> Foundation model for particle collision data analysis.<br/><i>Nat Mach Intell</i> (2026). <a href="https://doi.org/10.1038/s42256-026-01322-9" target="_blank" rel="noopener noreferrer">doi:10.1038/s42256-026-01322-9</a></div>

<!--
Animation adapted from EveNet-Presentation/CCNU_Seminar/components/NJUAnimatedEveNet.vue, core scene: shell opening, local/global attention, object encoder and flowing signals. Unused assignment, segmentation and self-supervised heads removed. The two paths denote separate fine-tunings, not shared trained weights. Diffusion bypasses the classifier object encoder. DELPHI FiLM and inputs: Internal_Note/components/MLFlow.vue. Up to24 particles,12/hemisphere;12 classes=10 unordered pairs+other tau+lepton background;84 event quantities;1sample50steps. Geometric links and signal motion are schematic, not learned attention weights or actual inference. Publication citation supplied by user, verified in preceding revision.
-->
