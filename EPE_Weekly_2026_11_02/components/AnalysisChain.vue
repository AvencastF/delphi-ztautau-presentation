<script setup lang="ts">
// The analysis in five stages, one click each (pattern of the status deck's ChainFlow / useStepMotion).
import { useStepMotion } from 'slidev-addon-ztautau/composable/useStepMotion'
import { mixed } from 'slidev-addon-ztautau/composable/tex'
const props = defineProps<{ step: number }>()
const N = 5
const { motion, running, stage, reveal } = useStepMotion(() => props.step, N - 1, 700)
const boxes = [
  { t: 'Archived data', s: '1992–1995 · 2.4 M events', c: '#77c9ff' },
  { t: 'New simulation', s: 'full detector · 38 M events', c: '#f0c36e' },
  { t: 'Event selection', s: '18 cuts · 56,472 events', c: '#70dcb2' },
  { t: 'ML reconstruction', s: 'decay modes · $\\tau$ directions', c: '#baa5ff' },
  { t: 'Spin fit', s: '15 coefficients · tests', c: '#c9e86a' },
]
const notes = [
  'DELPHI recorded $e^+e^-$ collisions at the $Z$ pole from 1989 to 1995. The archived 1992–1995 lepton-pair streams are converted to a modern event format: 2.4 million events, each run matched to the luminosity and detector-quality records of its year.',
  'No suitable legacy simulation survives, so we generate our own: PYTHIA 8 for the signal and the $Z$ backgrounds, dedicated generators for Bhabha and two-photon events, then the preserved DELPHI detector simulation and reconstruction with the detector description of each year. Eight energy-point samples, 38 million events.',
  'A cut-based preselection isolates back-to-back, low-multiplicity $\\tau$-pair candidates with one charged track per hemisphere and rejects $Z\\to ee$, $Z\\to\\mu\\mu$, hadronic and two-photon events: 56,472 data events, with simulation agreeing to 2 % in rate.',
  'Two neural networks, fine-tuned from the EveNet foundation model on half of the simulation: one names the decay mode of each $\\tau$, one reconstructs each $\\tau$ flight direction, which fixes the axes in which the spin is read.',
  'Events are sorted into 16 decay-pair regions and 15 angular distributions per region are compared with simulation templates. One fit returns all 15 spin coefficients with their covariance; entanglement and Bell tests follow.',
]
const X = (i: number) => 4 + i * 174
const on = (i: number) => Math.max(0, 1 - Math.abs(motion.stage - i))
</script>

<template>
  <section class="ac" :data-step="step">
    <svg viewBox="0 0 870 108" preserveAspectRatio="xMidYMid meet" role="img" aria-label="Five stages: archived data, new simulation, event selection, machine-learning reconstruction, spin fit.">
      <g fill="none" stroke="#bcc2cb" stroke-width="1.4">
        <path v-for="i in 4" :key="i" :d="`M${X(i - 1) + 164} 54 H${X(i) - 2}`" :style="{ opacity: .3 + .7 * reveal(i) }" />
      </g>
      <path d="M168 54 H866" fill="none" stroke="#fff0ba" stroke-width="2" pathLength="100" stroke-dasharray="6 94" :stroke-dashoffset="-motion.cycle * 100" :style="{ opacity: running ? .55 : 0 }" />
      <g v-for="(b, i) in boxes" :key="i" :transform="`translate(${X(i)} 14)`" :style="{ opacity: .4 + .6 * reveal(i) }">
        <rect width="164" height="80" rx="6" fill="#23262b" :stroke="b.c" :stroke-opacity=".45 + .55 * on(i)" :stroke-width="1 + 1.6 * on(i)" />
        <rect width="164" height="80" rx="6" :fill="b.c" :fill-opacity=".12 * on(i)" />
        <text x="10" y="17" class="num" :fill="b.c">{{ i + 1 }}</text>
        <foreignObject x="4" y="24" width="156" height="24"><div xmlns="http://www.w3.org/1999/xhtml" class="fo lab" v-html="mixed(b.t)" /></foreignObject>
        <foreignObject x="4" y="50" width="156" height="22"><div xmlns="http://www.w3.org/1999/xhtml" class="fo sm" v-html="mixed(b.s)" /></foreignObject>
      </g>
    </svg>
    <div class="ac-text">
      <h3>Stage {{ stage + 1 }} of {{ N }} · <span v-html="mixed(boxes[stage].t)" /></h3>
      <p v-html="mixed(notes[stage])" />
    </div>
  </section>
</template>

<style scoped>
.ac { margin-top: 6px; }
.ac svg { width: 100%; height: 112px; display: block; overflow: visible; }
.num { font-size: 10px; }
.fo { line-height: 22px; white-space: nowrap; text-align: center; }
.fo.lab { font-size: 15px; color: #f0f1f3; font-weight: 550; }
.fo.sm { font-size: 12px; color: #bcc2cb; }
.ac-text { border-top: 1px solid var(--nju-line); margin-top: 10px; padding-top: 12px; min-height: 120px; }
.ac-text h3 { margin: 0 0 10px; font-size: 20px; color: var(--nju-amber); font-weight: 550; line-height: 1.25; }
.ac-text p { margin: 0; font-size: 16.5px; line-height: 1.55; color: var(--fg-0); max-width: 860px; }
</style>
