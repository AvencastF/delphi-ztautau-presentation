<script setup lang="ts">
// The whole spin fit as one click-driven animation, eight stages (adapted from the status deck's FitFlow).
import { useStepMotion } from 'slidev-addon-ztautau/composable/useStepMotion'
import { mixed } from 'slidev-addon-ztautau/composable/tex'
const props = defineProps<{ step: number }>()
const N = 8
const { motion, running, stage, reveal } = useStepMotion(() => props.step, N - 1, 700)
const boxes = [
  { t: 'Selected events', s: '1992–1995, all energies' },
  { t: 'Reconstruction', s: 'decay modes + $\\tau$ directions' },
  { t: 'Regions and histograms', s: '16 decay pairs $\\times$ 15 angles' },
  { t: 'Simulation templates', s: 'prediction for any spin state' },
  { t: '$\\chi^2$ fit', s: 'full covariance, linear' },
  { t: '15 coefficients', s: 'values $\\pm$ covariance' },
  { t: 'Derived quantities', s: 'witness, concurrence, Bell' },
  { t: 'Hypothesis tests', s: 'pseudo-experiments $\\to$ p-value' },
]
const notes = [
  'Start from the selected $\\tau$-pair candidates at all eight energy points, and the simulation scaled to the same luminosity.',
  'The classifier names the decay of each $\\tau$; the conditional diffusion model reconstructs each $\\tau$ direction, which defines the axes $k$, $r$, $n$ in which the spin is read.',
  'Events are sorted by their reconstructed decay pair into 16 regions. In each, 15 angular histograms are filled: $\\cos\\theta_i$ for the polarisations, $\\cos\\theta_i\\cos\\theta_j$ for the correlations. 2,400 bins in total.',
  'The same simulated events predict every bin for any choice of the 15 coefficients, by reweighting each event with its true decay angles. Efficiency, resolution and mis-identification are inside the prediction: no unfolding.',
  'The prediction is linear in the coefficients, so the $\\chi^2$ minimum is found in closed form. The covariance between bins accounts for every event entering all 15 histograms of its region.',
  'The result is 15 numbers with uncertainties and correlations: the complete spin density matrix of the $\\tau$ pair.',
  'Single numbers follow: the entanglement witness $W=C_{nn}-C_{rr}+C_{kk}-1$, the concurrence, and the Bell combination $|C_{kk}-C_{rr}|$.',
  'Constrained witness or Bell null; event-level pseudo-experiments calibrate the tail of the difference between constrained and free minimum chi-squared.',
]
const X = (i: number) => 14 + (i % 4) * 216
const Y = (i: number) => (i < 4 ? 14 : 112)
const on = (i: number) => Math.max(0, 1 - Math.abs(motion.stage - i))
</script>

<template>
  <section class="fc" :data-step="step">
    <svg viewBox="0 0 880 190" preserveAspectRatio="xMidYMid meet" role="img" aria-label="Spin-fit chain in eight stages, from selected events to hypothesis tests.">
      <g fill="none" stroke="#bcc2cb" stroke-width="1.4">
        <path v-for="i in 3" :key="'a' + i" :d="`M${X(i - 1) + 196} 46 H${X(i) - 2}`" :style="{ opacity: .35 + .65 * reveal(i) }" />
        <path d="M818 78 V95 H110 V110" :style="{ opacity: .35 + .65 * reveal(4) }" />
        <path v-for="i in 3" :key="'b' + i" :d="`M${X(i + 3) + 196} 144 H${X(i + 4) - 2}`" :style="{ opacity: .35 + .65 * reveal(i + 4) }" />
      </g>
      <path d="M818 78 V95 H110 V110" fill="none" stroke="#fff0ba" stroke-width="2.4" pathLength="100" stroke-dasharray="18 82" :stroke-dashoffset="-motion.cycle * 100" :style="{ opacity: running && stage >= 4 ? .9 : 0 }" />
      <g v-for="(b, i) in boxes" :key="i" :transform="`translate(${X(i)} ${Y(i)})`" :style="{ opacity: .38 + .62 * reveal(i) }">
        <rect width="196" height="64" rx="6" fill="#23262b" :stroke="on(i) > .02 ? '#f0c36e' : '#c9e86a'" :stroke-opacity=".45 + .55 * on(i)" :stroke-width="1 + 1.6 * on(i)" />
        <rect width="196" height="64" rx="6" fill="#f0c36e" :fill-opacity=".14 * on(i)" />
        <text x="10" y="17" class="num">{{ i + 1 }}</text>
        <foreignObject x="4" y="14" width="188" height="22"><div xmlns="http://www.w3.org/1999/xhtml" class="fo lab" v-html="mixed(b.t)" /></foreignObject>
        <foreignObject x="4" y="36" width="188" height="20"><div xmlns="http://www.w3.org/1999/xhtml" class="fo sm" v-html="mixed(b.s)" /></foreignObject>
      </g>
    </svg>
    <div class="fc-text">
      <h3>Step {{ stage + 1 }} of {{ N }} · <span v-html="mixed(boxes[stage].t)" /></h3>
      <p v-html="mixed(notes[stage])" />
      <small>Exercised on simulation; steps 4–8 use pseudo-data equal to the simulation prediction.</small>
    </div>
  </section>
</template>

<style scoped>
.fc { margin-top: 2px; }
.fc svg { width: 100%; height: 196px; display: block; overflow: visible; }
.num { font-size: 10px; fill: #f0c36e; }
.fo { line-height: 20px; white-space: nowrap; text-align: center; }
.fo.lab { font-size: 13.5px; color: #f0f1f3; font-weight: 550; }
.fo.sm { font-size: 11px; color: #bcc2cb; }
.fc-text { border-top: 1px solid var(--nju-line); margin-top: 6px; padding-top: 8px; min-height: 96px; }
.fc-text h3 { margin: 0 0 8px; font-size: 19px; color: var(--nju-amber); font-weight: 550; line-height: 1.25; }
.fc-text p { margin: 0; font-size: 15.5px; line-height: 1.5; color: var(--fg-0); max-width: 820px; }
.fc-text small { display: block; margin-top: 8px; font-size: 11px; color: var(--fg-1); }
</style>
