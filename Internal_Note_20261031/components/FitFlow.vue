<script setup lang="ts">
// The whole spin-fit chain as one click-driven animation (pattern of MLFlow.vue / useStepMotion.ts).
// Each click moves the highlight to the next stage and shows one sentence for a general audience.
import { useStepMotion } from 'slidev-addon-ztautau/composable/useStepMotion'
import { mixed } from 'slidev-addon-ztautau/composable/tex'
const props = defineProps<{ step: number }>()
const N = 8
const { motion, running, stage, reveal } = useStepMotion(() => props.step, N - 1, 700)
const boxes = [
  { t: 'Selected events', s: '1992–1995, 18 cuts' },
  { t: 'ML reconstruction', s: 'decay class + $\\tau$ directions' },
  { t: 'Regions and histograms', s: '16 decay pairs × 15 histograms' },
  { t: 'Simulation templates', s: 'prediction for any spin state' },
  { t: '$\\chi^2$ fit', s: 'data vs prediction, full covariance' },
  { t: '15 coefficients', s: 'values $\\pm$ covariance matrix' },
  { t: 'Derived quantities', s: 'witness, concurrence, Bell' },
  { t: 'Hypothesis tests', s: 'fake experiments $\\to$ p-value' },
]
const notes = [
  'Start from the $\\tau$-pair candidates that pass the 18 cuts at all eight energy points: 56,472 data events, and the simulation scaled to the same luminosity.',
  'The classifier names the decay of each $\\tau$ ($\\pi$, $\\rho$, $e$, $\\mu$ or other); the neutrino model reconstructs each $\\tau$ direction, which defines the axes in which the spin is read.',
  'Events are sorted by their reconstructed decay pair into 16 regions. In each region 15 angular histograms of 10 bins are filled, one per spin coefficient: 2,400 numbers in all.',
  'The simulation predicts every one of the 2,400 bins for any choice of the 15 coefficients, by reweighting the same simulated events. Detector effects are included automatically.',
  'The fit finds the 15 coefficients whose prediction best matches the data. Because every event enters all 15 histograms, their correlations are taken into account.',
  'The result is 15 numbers with errors and their correlations: the complete spin state of the $\\tau$ pair.',
  'Single numbers follow from the 15: the entanglement witness, the concurrence (how much entanglement) and the Bell combination.',
  'Thousands of fake experiments from a world without entanglement show how often chance alone would look like our result: that frequency is the p-value.',
]
const X = (i: number) => 14 + (i % 4) * 216
const Y = (i: number) => (i < 4 ? 14 : 112)
// how strongly box i is highlighted: 1 at the current stage, fading over one step
const on = (i: number) => Math.max(0, 1 - Math.abs(motion.stage - i))
</script>

<template>
  <section class="ff" :data-step="step">
    <svg viewBox="0 0 880 190" preserveAspectRatio="xMidYMid meet" role="img" aria-label="Spin-fit chain in eight stages, from selected events to hypothesis tests.">
      <!-- connectors -->
      <g fill="none" stroke="#bcc2cb" stroke-width="1.4">
        <path v-for="i in 3" :key="'a' + i" :d="`M${X(i - 1) + 196} 46 H${X(i) - 2}`" :opacity=".35 + .65 * reveal(i)" />
        <path d="M818 78 V95 H110 V110" :opacity=".35 + .65 * reveal(4)" />
        <path v-for="i in 3" :key="'b' + i" :d="`M${X(i + 3) + 196} 144 H${X(i + 4) - 2}`" :opacity=".35 + .65 * reveal(i + 4)" />
      </g>
      <path d="M818 78 V95 H110 V110" fill="none" stroke="#fff0ba" stroke-width="2.4" pathLength="100" stroke-dasharray="18 82" :stroke-dashoffset="-motion.cycle * 100" :opacity="running && stage >= 4 ? .9 : 0" />
      <!-- boxes -->
      <g v-for="(b, i) in boxes" :key="i" :transform="`translate(${X(i)} ${Y(i)})`" :opacity=".38 + .62 * reveal(i)">
        <rect width="196" height="64" rx="6" fill="#23262b" :stroke="on(i) > .02 ? '#f0c36e' : '#77c9ff'" :stroke-opacity=".45 + .55 * on(i)" :stroke-width="1 + 1.6 * on(i)" />
        <rect width="196" height="64" rx="6" fill="#f0c36e" :fill-opacity=".14 * on(i)" />
        <text x="10" y="17" class="num">{{ i + 1 }}</text>
        <foreignObject x="4" y="14" width="188" height="22"><div xmlns="http://www.w3.org/1999/xhtml" class="fo lab" v-html="mixed(b.t)" /></foreignObject>
        <foreignObject x="4" y="36" width="188" height="20"><div xmlns="http://www.w3.org/1999/xhtml" class="fo sm" v-html="mixed(b.s)" /></foreignObject>
      </g>
    </svg>
    <div class="ff-text">
      <h3>Stage {{ stage + 1 }} of {{ N }} · <span v-html="mixed(boxes[stage].t)" /></h3>
      <p v-html="mixed(notes[stage])" />
      <small>Today every stage runs on simulation: the "data" in stages 4–8 are pseudo-data equal to the simulation (Asimov). No real-data spin fit yet.</small>
    </div>
  </section>
</template>

<style scoped>
.ff { margin-top: 2px; }
.ff svg { width: 100%; height: 196px; display: block; overflow: visible; }
.num { font-size: 10px; fill: #f0c36e; }
.fo { line-height: 20px; white-space: nowrap; text-align: center; }
.fo.lab { font-size: 13.5px; color: #f0f1f3; font-weight: 550; }
.fo.sm { font-size: 11px; color: #bcc2cb; }
.ff-text { border-top: 1px solid var(--nju-line); margin-top: 6px; padding-top: 8px; min-height: 96px; }
.ff-text h3 { margin: 0 0 6px; font-size: 16px; color: var(--nju-amber); font-weight: 550; line-height: 1.25; }
.ff-text p { margin: 0; font-size: 14px; line-height: 1.42; color: var(--fg-0); max-width: 820px; }
.ff-text small { display: block; margin-top: 8px; font-size: 11px; color: var(--fg-1); }
</style>
