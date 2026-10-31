---
class: st pres
clicks: 7
---

<script setup>
import FitFlow from '../components/FitFlow.vue'
</script>

# The whole fit in eight steps

<div class="st-sub">Click through: from selected events to 15 numbers and a p-value.</div>

<FitFlow :step="$clicks" />

<div class="st-source">Source: the spin-fit chain as run on 1992–1995 simulation (fit inputs 2026-10-30, final fit model 2026-10-31); schematic</div>

<!--
Stages and numbers: selection all-years-rq-20261026 (56,472 data events in the inclusive sample); ML all-years v1 (classifier + neutrino model, hold half); fit inputs artifacts/legacy-fit-ml-allyears-20261030 (slim-by-point, 16 regions, legacy fit cut flags_valid > 0, theta_cm > 0.6, m_tautau > 80 GeV); histograms 16 regions x 15 observables x 10 bins = 2,400 bins (fit-inputs slide); templates and chi2 = model C (tau_analysis/joint_fit, owner decision 2026-10-31: target model; GLS with the full bin-to-bin covariance); derived quantities and hypothesis tests: artifacts/joint-fit-20261031/modelC/*/summary.md and step2/*. Asimov: pseudo-data equal to the simulation; no real-data spin fit has been run.
-->
