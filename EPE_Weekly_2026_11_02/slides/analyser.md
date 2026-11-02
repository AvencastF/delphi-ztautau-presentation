---
class: st pres tk
---

<script setup>
import Analyser from '../components/Analyser.vue'
</script>

# The spin analyser

<div class="st-sub">The decay product prefers the parent spin.</div>

<Analyser />

<!--
Rate in the tau rest frame: (1/Gamma) dGamma/dcos(theta) = 1/2 (1 + kappa P cos theta). No clicks: the slide loops pi, rho, e, mu every 2 s. Each frame draws that decay (pi: charged pion + neutrino; rho: charged pion + neutral pion + neutrino; e: electron + two neutrinos; mu: muon + two neutrinos) and lights that kappa line. P = 1. Owner decision 2026-11-02: analysing power is kappa. Values used by the fit: pi 1, rho 0.41, e -0.33, mu -0.34 (Internal_Note fit-observables.md). Branching fractions, PDG 2024 tau listings (central values; uncertainties not on the slide): pi nu 10.82 +- 0.05 %; rho row is pi pi0 nu 25.49 +- 0.09 %; e nu nu 17.82 +- 0.04 %; mu nu nu 17.39 +- 0.04 %. https://pdg.lbl.gov/2024/listings/rpp2024-list-tau.pdf Gamma9, Gamma14, Gamma5, Gamma3. Flight length: gamma c tau = (45.6 / 1.777) x 87.0 um = 2.2 mm (PDG tau lifetime 290.3 fs).
-->
