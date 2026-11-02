---
class: st pres tk
clicks: 7
---

<script setup>
import FitChain from '../components/FitChain.vue'
</script>

# Backup · from selected events to a p-value

<div class="st-sub">One fit returns all 15 coefficients; the entanglement and Bell tests are derived from them.</div>

<FitChain :step="$clicks" />

<div class="tk-foot">Fit inputs: events assigned to one of the 16 decay pairs with a reconstructed <LaTeX formula="\tau" /> direction; 15 histograms of 10 bins per region.</div>

<!--
Stages: selected events (56,472 data; the fit additionally requires a valid direction solution, |cos theta_cm| cut and visible mass above 80 GeV -> 32,336 simulated events after the fit cut, combined 1992-1995, held-out half scaled by two); network classes and directions; 16 regions (4 x 4 charge-ordered decay pairs) x 15 observables (cos theta_i for the six B, cos theta_i cos theta_j for the nine C) x 10 bins = 2,400 bins; reweighted templates (linear in the coefficients); chi2 with the full bin-to-bin covariance (block-diagonal over regions), solved in closed form (generalised least squares; iminuit agrees to 5e-5); derived quantities W, concurrence, |C_kk - C_rr|; hypothesis tests with 20,000 pseudo-experiments per test from the constrained (null) state. Asimov: pseudo-data equal to the simulation prediction.
-->
