<script setup lang="ts">
// One pretrained event model, two task heads. Click 0: inputs. Click 1: the shared body. Click 2: the two heads.
import { useStepMotion } from 'slidev-addon-ztautau/composable/useStepMotion'
import { mixed } from 'slidev-addon-ztautau/composable/tex'
const props = defineProps<{ step: number }>()
const { motion, running, reveal, stage } = useStepMotion(() => props.step, 2, 800)
const titles = [
  'Input: the event as a list of particles',
  'A transformer pretrained on hundreds of millions of simulated collider events',
  'Two heads, fine-tuned on half of the DELPHI simulation',
]
const notes = [
  'Every reconstructed particle enters as one token: energy, momentum components, charge and the detector identification flags. Event-level quantities such as the collision energy and the year are added as conditions.',
  'The body is the EveNet foundation model: a transformer trained on large simulated LHC samples to produce general-purpose event representations. Starting from it, rather than from random weights, gives a better classifier for the same DELPHI training sample.',
  'The classification head assigns the event to one of the ten $\\tau$ decay pairs or to a background class. The regression head predicts the two angles between each $\\tau$ and its leading track. The other half of the simulation is kept for evaluation and for the fit.',
]
const particles = [220, 250, 280, 310, 340]
</script>

<template>
  <section class="th" :data-step="step">
    <svg viewBox="0 0 560 250" role="img" aria-label="Diagram: particle tokens enter a shared pretrained transformer body with two output heads, decay-mode class and tau direction.">
      <!-- inputs -->
      <g>
        <foreignObject x="10" y="8" width="150" height="18"><div xmlns="http://www.w3.org/1999/xhtml" class="fo lab" style="text-align:left;color:#77c9ff" v-html="mixed('particle tokens')" /></foreignObject>
        <g v-for="(y, i) in particles" :key="i" :transform="`translate(14 ${y - 190})`">
          <rect width="128" height="22" rx="4" fill="#23262b" stroke="#77c9ff" stroke-opacity=".6" />
          <foreignObject x="4" y="2" width="120" height="18"><div xmlns="http://www.w3.org/1999/xhtml" class="fo sm" v-html="mixed(['$E,\\;\\vec p,\\;q$ · track · $\\mu$ tag', '$E,\\;\\vec p,\\;q$ · track · $e$ tag', '$E,\\;\\vec p$ · photon', '$E,\\;\\vec p$ · photon', '$E,\\;\\vec p,\\;q$ · track'][i])" /></foreignObject>
          <line x1="128" y1="11" x2="170" y2="11" stroke="#77c9ff" stroke-opacity=".5" />
        </g>
        <rect x="14" y="190" width="128" height="22" rx="4" fill="#23262b" stroke="#f0c36e" stroke-opacity=".7" />
        <foreignObject x="18" y="192" width="120" height="18"><div xmlns="http://www.w3.org/1999/xhtml" class="fo sm" style="color:#f0c36e" v-html="mixed('conditions: $\\sqrt s$, year, …')" /></foreignObject>
        <line x1="142" y1="201" x2="170" y2="201" stroke="#f0c36e" stroke-opacity=".5" />
      </g>
      <!-- body -->
      <g :style="{ opacity: .3 + .7 * reveal(1) }">
        <rect x="172" y="22" width="160" height="196" rx="8" fill="#23262b" stroke="#baa5ff" :stroke-width="1 + reveal(1)" />
        <g v-for="k in 4" :key="k">
          <rect x="190" :y="40 + (k - 1) * 42" width="124" height="30" rx="4" fill="#baa5ff" :fill-opacity=".10 + .08 * Math.sin(motion.cycle * Math.PI * 2 + k) * (running ? 1 : 0)" stroke="#baa5ff" stroke-opacity=".5" />
          <foreignObject x="190" :y="46 + (k - 1) * 42" width="124" height="18"><div xmlns="http://www.w3.org/1999/xhtml" class="fo sm" style="color:#f0f1f3" v-html="mixed(['attention', 'attention', 'attention', 'attention'][k - 1] + ' block ' + k)" /></foreignObject>
        </g>
        <foreignObject x="172" y="222" width="160" height="22"><div xmlns="http://www.w3.org/1999/xhtml" class="fo lab" style="color:#baa5ff" v-html="mixed('EveNet body · pretrained')" /></foreignObject>
      </g>
      <!-- heads -->
      <g :style="{ opacity: reveal(2) }">
        <path d="M332 80 H372" stroke="#bcc2cb" stroke-width="1.4" fill="none" /><path d="M332 160 H372" stroke="#bcc2cb" stroke-width="1.4" fill="none" />
        <rect x="374" y="52" width="172" height="58" rx="6" fill="#23262b" stroke="#70dcb2" stroke-width="1.4" />
        <foreignObject x="378" y="56" width="164" height="22"><div xmlns="http://www.w3.org/1999/xhtml" class="fo lab" style="color:#70dcb2" v-html="mixed('classification head')" /></foreignObject>
        <foreignObject x="378" y="78" width="164" height="30"><div xmlns="http://www.w3.org/1999/xhtml" class="fo sm" style="white-space:normal;line-height:14px" v-html="mixed('decay pair: $ee,\\,e\\mu,\\,e\\pi,\\,e\\rho,\\,\\mu\\mu,\\ldots,\\rho\\rho$, or background')" /></foreignObject>
        <rect x="374" y="132" width="172" height="58" rx="6" fill="#23262b" stroke="#f69cab" stroke-width="1.4" />
        <foreignObject x="378" y="136" width="164" height="22"><div xmlns="http://www.w3.org/1999/xhtml" class="fo lab" style="color:#f69cab" v-html="mixed('regression head')" /></foreignObject>
        <foreignObject x="378" y="158" width="164" height="30"><div xmlns="http://www.w3.org/1999/xhtml" class="fo sm" style="white-space:normal;line-height:14px" v-html="mixed('$(\\delta\\theta,\\delta\\phi)$ between each $\\tau$ and its leading track')" /></foreignObject>
      </g>
    </svg>
    <div class="th-text">
      <h3 v-html="mixed(titles[stage])" />
      <p v-html="mixed(notes[stage])" />
      <small v-html="mixed('Schematic. One model per task for all four years; training and evaluation halves of the simulation are disjoint.')" />
    </div>
  </section>
</template>

<style scoped>
.th { display: grid; grid-template-columns: 1.2fr 1fr; gap: 18px; align-items: center; margin-top: 2px; }
.th svg { width: 100%; height: 260px; display: block; overflow: visible; }
.fo { line-height: 18px; white-space: nowrap; color: #bcc2cb; text-align: center; }
.fo.lab { font-size: 12.5px; color: #f0f1f3; font-weight: 550; }
.fo.sm { font-size: 11.5px; }
.th-text h3 { margin: 0 0 10px; font-size: 19px; color: var(--nju-amber); font-weight: 550; line-height: 1.25; }
.th-text p { margin: 0; font-size: 15px; line-height: 1.5; color: var(--fg-0); min-height: 120px; }
.th-text small { display: block; margin-top: 10px; font-size: 12px; color: var(--fg-1); }
</style>
