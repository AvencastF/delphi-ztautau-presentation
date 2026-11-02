<script setup lang="ts">
// Why the tau direction is hard: visible leg -> cone -> two mirror solutions -> the ML prediction.
import { useStepMotion } from 'slidev-addon-ztautau/composable/useStepMotion'
import { mixed } from 'slidev-addon-ztautau/composable/tex'
const props = defineProps<{ step: number }>()
const { reveal, stage } = useStepMotion(() => props.step, 3, 900)
const titles = ['Visible decay system', 'Hadronic two-body constraint', 'Mirror solutions', 'EveNet direction prediction']
const notes = [
  'Charged track and associated photons. Missing neutrino momentum.',
  '$E_\\tau=E_\\mathrm{beam}$; one massless neutrino. Allowed direction on a cone around the visible momentum.',
  'Back-to-back constraint; two branches when real solutions exist. Conventional branch accuracy: 59 %.',
  'Conditional diffusion of the direction offsets. Correct branch: 72 %; pion median error: $0.88^\\circ$.',
]
</script>

<template>
  <section class="ab" :data-step="step">
    <svg viewBox="0 0 560 300" role="img" aria-label="Sketch of the two-fold ambiguity of the tau direction from one visible decay product, and the machine-learning prediction near the true direction.">
      <circle cx="280" cy="160" r="3" fill="#f0f1f3" />
      <foreignObject x="120" y="280" width="320" height="18"><div xmlns="http://www.w3.org/1999/xhtml" class="fo sm" v-html="mixed('interaction point · one $\\tau$ shown in detail')" /></foreignObject>
      <line x1="280" y1="160" x2="470" y2="100" stroke="#77c9ff" stroke-width="3" />
      <foreignObject x="474" y="86" width="90" height="18"><div xmlns="http://www.w3.org/1999/xhtml" class="fo lab" style="color:#77c9ff;text-align:left" v-html="mixed('visible track')" /></foreignObject>
      <g :style="{ opacity: reveal(1) }">
        <line x1="280" y1="160" x2="470" y2="36" stroke="#f0c36e" stroke-opacity=".8" stroke-dasharray="5 4" />
        <line x1="280" y1="160" x2="480" y2="166" stroke="#f0c36e" stroke-opacity=".8" stroke-dasharray="5 4" />
        <ellipse cx="474" cy="101" rx="14" ry="66" fill="none" stroke="#f0c36e" stroke-opacity=".8" transform="rotate(-8 474 101)" />
        <foreignObject x="300" y="178" width="260" height="18"><div xmlns="http://www.w3.org/1999/xhtml" class="fo sm" style="text-align:left;color:#f0c36e" v-html="mixed('cone: opening angle fixed by $E_\\mathrm{vis}$, $E_\\mathrm{beam}$, $m_\\tau$')" /></foreignObject>
      </g>
      <g :style="{ opacity: reveal(2) }">
        <line x1="280" y1="160" x2="466" y2="50" stroke="#f69cab" stroke-width="2.2" />
        <line x1="280" y1="160" x2="478" y2="150" stroke="#f69cab" stroke-width="2.2" />
        <circle cx="466" cy="50" r="5" fill="#f69cab" /><circle cx="478" cy="150" r="5" fill="#f69cab" />
        <foreignObject x="400" y="24" width="80" height="18"><div xmlns="http://www.w3.org/1999/xhtml" class="fo lab" style="color:#f69cab" v-html="mixed('solution A')" /></foreignObject>
        <foreignObject x="484" y="156" width="80" height="18"><div xmlns="http://www.w3.org/1999/xhtml" class="fo lab" style="color:#f69cab;text-align:left" v-html="mixed('solution B')" /></foreignObject>
        <line x1="280" y1="160" x2="94" y2="270" stroke="#f69cab" stroke-opacity=".35" stroke-width="1.5" />
        <line x1="280" y1="160" x2="82" y2="170" stroke="#f69cab" stroke-opacity=".35" stroke-width="1.5" />
        <foreignObject x="30" y="138" width="170" height="18"><div xmlns="http://www.w3.org/1999/xhtml" class="fo sm" style="text-align:left" v-html="mixed('the other $\\tau$, back to back')" /></foreignObject>
      </g>
      <g :style="{ opacity: reveal(3) }">
        <line x1="280" y1="160" x2="470" y2="56" stroke="#70dcb2" stroke-width="2" stroke-dasharray="2 3" />
        <circle cx="470" cy="56" r="4" fill="#70dcb2" />
        <foreignObject x="480" y="48" width="70" height="18"><div xmlns="http://www.w3.org/1999/xhtml" class="fo lab" style="text-align:left;color:#70dcb2" v-html="mixed('true $\\tau$')" /></foreignObject>
        <circle cx="462" cy="62" r="6" fill="none" stroke="#baa5ff" stroke-width="2" />
        <circle cx="462" cy="62" r="2" fill="#baa5ff" />
        <foreignObject x="250" y="66" width="200" height="18"><div xmlns="http://www.w3.org/1999/xhtml" class="fo lab" style="text-align:right;color:#baa5ff" v-html="mixed('network prediction')" /></foreignObject>
        <foreignObject x="190" y="84" width="260" height="18"><div xmlns="http://www.w3.org/1999/xhtml" class="fo sm" style="text-align:right" v-html="mixed('correct side 72 % · median error $0.9$–$1.2^\\circ$')" /></foreignObject>
      </g>
    </svg>
    <div class="ab-text">
      <h3 v-html="mixed(titles[stage])" />
      <p v-html="mixed(notes[stage])" />
      <small v-html="mixed('Schematic geometry. Percentages: 2.4 million simulated $Z\\to\\tau\\tau$ events of 1992–1995 not used in training.')" />
    </div>
  </section>
</template>

<style scoped>
.ab { display: grid; grid-template-columns: 1.15fr 1fr; gap: 18px; align-items: center; margin-top: 2px; }
.ab svg { width: 100%; height: 280px; display: block; overflow: visible; }
.fo { line-height: 18px; white-space: nowrap; color: #bcc2cb; text-align: center; }
.fo.lab { font-size: 13px; color: #f0f1f3; }
.fo.sm { font-size: 11.5px; }
.ab-text h3 { margin: 0 0 10px; font-size: 19px; color: var(--nju-amber); font-weight: 550; line-height: 1.25; }
.ab-text p { margin: 0; font-size: 15px; line-height: 1.5; color: var(--fg-0); min-height: 120px; }
.ab-text small { display: block; margin-top: 10px; font-size: 12px; color: var(--fg-1); }
</style>
