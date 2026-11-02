---
class: st pres tk
---

<script setup>
import ZoomablePlot from 'slidev-addon-ztautau/components/ZoomablePlot.vue'
</script>

# Backup · more data/simulation comparisons, 1992–1995

<div class="st-sub">Points: data; stack: simulation. <LaTeX formula="\chi^2/\mathrm{dof}" /> badges are statistical and diagnostic: green <LaTeX formula="\le 1.5" />, amber <LaTeX formula="\le 3" />, red above.</div>

<div class="fig2x2">
<div><div class="st-fig"><ZoomablePlot src="/figures/datamc/lead-p-over-pbeam-h1.svg" alt="leading-track momentum over beam momentum, second hemisphere" /></div><div class="st-cap">Leading-track <LaTeX formula="p/p_\mathrm{beam}" />, second hemisphere<span class="badge a"><LaTeX formula="\chi^2/\mathrm{dof}" /> 101.8 / 42</span></div></div>
<div><div class="st-fig"><ZoomablePlot src="/figures/datamc/lead-costheta-h0.svg" alt="leading-track polar angle, first hemisphere" /></div><div class="st-cap">Leading-track <LaTeX formula="\cos\theta" />, first hemisphere (thrust-axis orientation convention)<span class="badge a"><LaTeX formula="\chi^2/\mathrm{dof}" /> 102.2 / 37</span></div></div>
<div><div class="st-fig"><ZoomablePlot src="/figures/datamc/pirho-rho-mass.svg" alt="rho candidate mass in the pi-rho channel" /></div><div class="st-cap"><LaTeX formula="\rho" /> candidate mass, <LaTeX formula="\pi\rho" /> channel<span class="badge a"><LaTeX formula="\chi^2/\mathrm{dof}" /> 18.7 / 11</span></div></div>
<div><div class="st-fig"><ZoomablePlot src="/figures/datamc/hcal-mean-h0.svg" alt="hadron-calorimeter mean energy per layer, first hemisphere" /></div><div class="st-cap">Hadron-calorimeter energy per layer: a known response mismodelling<span class="badge r"><LaTeX formula="\chi^2/\mathrm{dof}" /> 384 / 60</span></div></div>
</div>

<div class="tk-foot">Inclusive sample after all cuts unless the channel is named. Statistical uncertainties only.</div>

<style>
.tk .fig2x2 .st-fig { height: 160px; }
.tk .fig2x2 .st-cap { font-size: 11.5px; }
</style>
