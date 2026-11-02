---
class: st pres tk
clicks: 4
---

<script setup>
import AnalysisChain from '../components/AnalysisChain.vue'
</script>

# Backup · the analysis in five stages

<div class="st-sub">The same chain runs for all eight data-taking points; it was developed on 1994 first.</div>

<AnalysisChain :step="$clicks" />

<div class="tk-foot">Simulation: PYTHIA 8 (signal, <LaTeX formula="Z" /> decays), BHWIDE (Bhabha), two-photon generators; preserved DELPHI full simulation and reconstruction, one detector description per year.</div>

<!--
Stage 1: 334 files, 2,395,361 converted data events (lepton streams 1992-1995); run-by-run lookup in the DELPHI luminosity tables and run-quality records. Stage 2: 17 simulation campaigns, 42,741,000 generated / 38,440,229 converted events (14,442,298 Z->tautau); seven processes (Z->tautau, ee, mumu, qq with PYTHIA 8.315; gamma gamma -> ll, hadrons; Bhabha with BHWIDE 1.05); detector descriptions of 1992, 1993, 1994 and 1995; DELSIM + reconstruction via the preserved DELPHI software in a container. Stage 3: 18 cuts, 56,472 data events in the inclusive sample vs 57,520 expected (0.982). Stage 4: all-years classifier and direction model fine-tuned from the EveNet checkpoint on half of the simulation (the "training half"); the other half is used for evaluation and the fit. Stage 5: full-covariance reweighted-template fit, 16 regions x 15 observables x 10 bins.
-->
