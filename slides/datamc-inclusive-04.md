---
class: st pres
---

<script setup>
import NJUPlot from '../components/NJUPlot.vue'
</script>

# Inclusive sample: event kinematics and radiative vetoes

<div class="st-sub">Inclusive τ-pair sample after all 18 cuts <span class="id">inclusive_1p1p</span> · H0 / H1 = geometric thrust hemispheres, not τ charge · points: data, stack: simulation by true process</div>

<div class="fig2x2">
<div><div class="st-fig"><NJUPlot src="/figures/datamc/inclusive/inclusive_1p1p-selected-visible_tautau_mass-rate_lin.svg" alt="visible τ-pair mass [GeV]" /></div><div class="st-cap">visible τ-pair mass [GeV]<span class="badge g">χ²/dof 37.3/49</span></div></div>
<div><div class="st-fig"><NJUPlot src="/figures/datamc/inclusive/inclusive_1p1p-selected-erad_over_ebeam-rate_lin.svg" alt="radiative EM energy / E_beam" /></div><div class="st-cap">radiative EM energy / E_beam<span class="badge a">χ²/dof 44.0/20</span></div></div>
<div><div class="st-fig"><NJUPlot src="/figures/datamc/inclusive/inclusive_1p1p-selected-prad_over_pbeam-rate_lin.svg" alt="radiative track momentum / p_beam" /></div><div class="st-cap">radiative track momentum / p_beam<span class="badge a">χ²/dof 51.5/20</span></div></div>
<div><div class="st-fig"><NJUPlot src="/figures/datamc/inclusive/inclusive_1p1p-selected-exclusive_pair_code-rate_lin.svg" alt="child assignment code" /></div><div class="st-cap">child assignment code<span class="badge g">χ²/dof 16.8/12</span></div></div>
</div>

<div class="st-source">Source: archived data/MC plot set with the neutral rule applied to the frozen 2026-10-06 selection production</div>

<!--
Figures: artifacts/exclusive-neutral-le3-plots-20261007/plots/ (job 59429001, source 4ae9ef3, neutral count <=3 per hemisphere applied to saved histograms). Black points = 1994 data; stack = signed luminosity-normalised simulation by true process, Z_ee excluded; lower panel = data / simulation. Inclusive sample 23,073 data / 23,198.93 MC. chi2/dof from agreement.json ("Total MC", status ok), statistical only, diagnostic.

-->
