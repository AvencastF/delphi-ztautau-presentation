---
class: st pres tk tk-academic
---

# Parallel reconstruction, common spin analysis

<div class="reco-common"><strong>Selected events</strong><span>Two thrust hemispheres · charged tracks · neutral clusters · detector PID</span></div>
<div class="reco-branches"><span><LaTeX formula="\downarrow" /></span><span><LaTeX formula="\downarrow" /></span></div>
<div class="reco-grid">
<section class="reco-traditional">
<header><h2>Conventional method</h2><span>Reference reconstruction</span></header>
<div class="reco-stage"><label>Decay classification</label><h3>Cut-based particle identification</h3><p><LaTeX formula="e,\mu,\pi,\rho" /> tags · photon multiplicity<br/>Visible invariant mass</p></div>
<div class="reco-stage"><label>Neutrino reconstruction</label><h3>Analytical kinematic constraints</h3><div class="reco-equation"><LaTeX formula="p_\tau^2=m_\tau^2,\quad (p_\tau-p_{\rm vis})^2=0" /></div><p><LaTeX formula="E_\tau=E_{\rm beam}" /> · back-to-back <LaTeX formula="\tau^+\tau^-" /><br/>Hadronic single-neutrino decays · two solutions</p></div>
</section>
<section class="reco-ml">
<header><h2>EveNet</h2><span>Focus of the following studies</span></header>
<div class="reco-stage"><label>Decay classification</label><h3>Learned event-level probabilities</h3><p>Joint information from both hemispheres<br/>Decay-pair classes + residual/background classes</p></div>
<div class="reco-stage"><label>Neutrino reconstruction</label><h3>Conditional diffusion</h3><div class="reco-equation"><LaTeX formula="(\delta\theta_-,\delta\phi_-,\delta\theta_+,\delta\phi_+)" /></div><p>Directions relative to the leading tracks<br/>Particle features + event-level conditions</p></div>
</section>
</div>
<div class="reco-branches"><span><LaTeX formula="\downarrow" /></span><span><LaTeX formula="\downarrow" /></span></div>
<div class="reco-common reco-output"><strong>Decay rest frames</strong><span>Spin analysers <LaTeX formula="\longrightarrow" /> detector response <LaTeX formula="\longrightarrow" /> forward-folded SDM fit</span></div>

<!--
Both approaches are developed in parallel; ML is the focus of the following performance slides. The analytical constraints shown apply to hadronic single-massless-neutrino legs, with equal beam-energy tau energies and no ISR recoil; both kinematic branches are retained. This is not a claim of an exact single-neutrino solution for leptonic decays. Current source: tau_analysis/docs/PROJECT_GUIDE.md and Internal_Note. Parallel-path design informed by ICHEP talk p5 and CCNU_Seminar/slides/delphi-transfer.md; older talk performance numbers and targets are not used.
-->
