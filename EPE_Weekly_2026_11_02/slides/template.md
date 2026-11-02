---
class: st pres tk tk-academic
---

# Forward-folded template dependence

<div class="st-sub">Illustration: the longitudinal spin correlation</div>


<script setup>
import ZoomablePlot from 'slidev-addon-ztautau/components/ZoomablePlot.vue'
</script>
<div class="tk-split wide"><div><div class="tk-fig" style="height:290px"><ZoomablePlot src="/figures/fit/template-ckk.svg" alt="Reconstructed angular template dependence on C kk in the pion-pair category" /></div><div class="tk-cap"><LaTeX formula="\pi\pi" /> category · reconstructed <LaTeX formula="x_k^-x_k^+" /><br/>Lines: varied <LaTeX formula="C_{kk}" /> · points: reference pseudo-data</div></div><div class="ac-stack"><section><h2>Linear spin response</h2><p>Truth-level reweighting<br/>Reconstructed-bin templates</p></section><section><h2>Detector effects</h2><p>Efficiency · angular resolution<br/>Cross-feed between decay categories</p></section><section><h2>Simultaneous fit</h2><p>All coefficients varied jointly<br/>Correlated histogram uncertainties</p></section></div></div>
<div class="ac-equation ac-compact"><LaTeX formula="\boldsymbol\mu(\mathbf c)=\boldsymbol\mu_{\rm ref}+\sum_{m=1}^{15}(c_m-c_m^{\rm ref})\,\mathbf T_m" /></div>


<div class="tk-foot">Simulation · reference pseudo-data · statistical uncertainties</div>

<!--
Existing template-ckk.svg provenance unchanged. Model C linear template equation from joint_fit/README.md. Fixed components included in mu_ref.
-->
