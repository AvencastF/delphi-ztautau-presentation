---
class: st pres tk fit-section fit-covariance
---

# Correlated angular fit

<div class="st-sub">Same events · 15 angular projections · one simultaneous fit</div>

<div class="fit-cov-grid">
<section>
<h2><LaTeX formula="V_r" />: covariance within one region</h2>
<img class="fit-cov-image" src="/figures/fit/region-covariance.svg" alt="Normalised 150 by 150 event covariance in the pion-pair region, showing correlations between different angular histograms" />
<div class="fit-cov-caption"><LaTeX formula="\pi\pi" /> simulation · normalised covariance<br/>Each block: <LaTeX formula="10\times10" /> bins · gold: single-angle / product boundary</div>
</section>
<section class="fit-copy">
<div class="fit-equation"><LaTeX formula="(V_r)_{ab}=\operatorname{Cov}(n_{ra},n_{rb})" /></div>
<div class="fit-cov-item"><h2>Diagonal entries</h2><p>Expected statistical variance of each bin.</p></div>
<div class="fit-cov-item"><h2>Off-diagonal blocks</h2><p>Shared events in different angular histograms.<br/><b>Retained in the fit covariance.</b></p></div>

</section>
</div>


<!--
V_r is the expected Poisson event covariance sum_e w_e s_e s_e^T, not MC-template sumw2.
Displayed matrix: covariance_modelC.npz V0_blocks[0], pion-pair region, before redundant-bin removal.
Normalised for display only; the fit uses the unnormalised covariance. Observable order follows bc_names.
Each histogram integrates to the same random region count: 14 exact constraints, 150 to 136 retained bins per region.
Retained bins remain correlated. Independent regions form separate covariance blocks. No Fisher or chi-square formulas needed here.
-->
