---
class: st pres tk tk-candidate-definitions
clicks: 2
---

<script setup>
import EventSketch from '../components/EventSketch.vue'
</script>

# Defining the four visible decay candidates

<div class="st-sub">Exclusive identification in each hemisphere · leading track and nearby photons</div>

<EventSketch :step="$clicks" identification />

<div class="candidate-common hadron-common" v-if="$clicks >= 2">
<div><b>Calorimeters</b><span>HPC: electromagnetic · HCAL: hadronic</span></div>
<div><b>Nearby photon</b><span>Selected HPC shower · <LaTeX formula="E_\gamma>0.5\,\mathrm{GeV}" /> · <LaTeX formula="\Delta R<0.3" /></span></div>
</div>
<div class="tk-foot">DELPHI Collaboration, <a href="https://opendata.cern.ch/record/80502/files/skelana.pdf" target="_blank" rel="noopener noreferrer">SKELANA manual</a>; implemented exclusive-candidate selection.</div>

<!--
Source checked live: tau_analysis/analysis/exclusive_id.py classify_leg and classify_event main_legacy_lines (numeric_ge7, final_hadron=True), hadron_inputs; photon_quality.py; docs/EXCLUSIVE_DECAY_HANDOFF_20261007.md.
Electron requires valid supported ELID>=3 and known nonpositive muon tag; muon numeric MUID>=7 and known nonpositive electron tag. Two positive tags = conflict; invalid/ambiguous competing tags = residual. Explicit absent tag records operationally nonpositive; missing/unknown not equivalent to absence.
Charged hadron requires both lepton vetoes, p/Ebeam>0.05, and either RPROCO pion code2/3 plus associated HPC E/p<0.6 (or certified HPC absence with valid track momentum), or complete uniquely associated HCAL profile with mean energy per occupied layer>=3GeV. The compact slide label 'hadron-tag/calorimeter selection' refers to this full predicate; detailed thresholds remain in backup-id.
Photon selected PHOT neutral with unique HPC shower, allowed profile, E_HPC>0.5GeV and DeltaR<0.3 relative to leading track; conversion/merged/secondary exclusions as source. Pion N_gamma=0 measured; rho1–2 selected nearby photons and 0.5<m(track+photons)<1.04GeV. One photon is not asserted to resolve a pi0. Diagram is an illustrative mu-rho pair, reused from topology slide, not all four assignments at once.
-->
