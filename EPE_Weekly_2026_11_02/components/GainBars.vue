<script setup lang="ts">
// Expected concurrence uncertainty per energy point: cut-based vs ML reconstruction (expected, simulation).
// Click 0: cut-based bars. Click 1: ML bars. Click 2: the combined fit.
import { useStepMotion } from 'slidev-addon-ztautau/composable/useStepMotion'
import { mixed } from 'slidev-addon-ztautau/composable/tex'
const props = defineProps<{ step: number }>()
const { reveal, stage } = useStepMotion(() => props.step, 2, 900)
const points = [
  { l: '1992 · 91', cut: 0.58, ml: 0.25 },
  { l: '1993 · 89', cut: 2.12, ml: 0.74 },
  { l: '1993 · 91', cut: 0.69, ml: 0.28 },
  { l: '1993 · 93', cut: 2.20, ml: 0.71 },
  { l: '1994 · 91', cut: 0.34, ml: 0.16 },
  { l: '1995 · 89', cut: 2.36, ml: 0.71 },
  { l: '1995 · 91', cut: 0.74, ml: 0.29 },
  { l: '1995 · 93', cut: 2.19, ml: 0.66 },
  { l: 'combined', cut: 0.21, ml: 0.10, comb: true },
]
// log scale 0.08 .. 3
const X0 = 70, X1 = 560, Y0 = 250, Y1 = 20
const lo = Math.log10(0.08), hi = Math.log10(3)
const yOf = (v: number) => Y0 - ((Math.log10(v) - lo) / (hi - lo)) * (Y0 - Y1)
const slot = (X1 - X0) / points.length
const xOf = (i: number) => X0 + i * slot + 10
const w = slot / 2 - 10
const ticks = [0.1, 0.2, 0.5, 1, 2]
const titles = ['Conventional reference', 'EveNet reconstruction', 'Combined sensitivity']
const notes = [
  'Independent fits at eight energy points. Larger uncertainties in the off-peak samples.',
  'Reduced uncertainty at every energy point. Classification and direction reconstruction varied together.',
  'Concurrence uncertainty: $0.21\\to0.10$. Legacy-fit comparison; statistical uncertainties only.',
]
</script>

<template>
  <section class="gb" :data-step="step">
    <svg viewBox="0 0 580 304" role="img" aria-label="Bar chart of the expected concurrence uncertainty per energy point, conventional vs machine-learning reconstruction, log scale.">
      <line :x1="X0" :y1="Y0" :x2="X1" :y2="Y0" stroke="#bcc2cb" stroke-opacity=".6" />
      <g v-for="t in ticks" :key="t">
        <line :x1="X0" :y1="yOf(t)" :x2="X1" :y2="yOf(t)" stroke="#bcc2cb" stroke-opacity=".12" />
        <text :x="X0 - 8" :y="yOf(t) + 4" text-anchor="end" class="ax">{{ t }}</text>
      </g>
      <text :x="X0 - 50" :y="(Y0 + Y1) / 2" class="ax" :transform="`rotate(-90 ${X0 - 50} ${(Y0 + Y1) / 2})`" text-anchor="middle">uncertainty on the concurrence</text>
      <g v-for="(p, i) in points" :key="p.l">
        <rect :x="xOf(i)" :y="Y0 - (Y0 - yOf(p.cut)) * Math.min(1, 1)" :width="w" :height="(Y0 - yOf(p.cut))" fill="#77c9ff" :fill-opacity="p.comb ? .35 + .6 * reveal(2) : .9" />
        <rect :x="xOf(i) + w + 2" :y="Y0 - (Y0 - yOf(p.ml)) * reveal(1)" :width="w" :height="(Y0 - yOf(p.ml)) * reveal(1)" fill="#baa5ff" :fill-opacity="p.comb ? .35 + .6 * reveal(2) : .9" />
        <text :x="xOf(i) + w / 2" :y="yOf(p.cut) - 5" text-anchor="middle" class="ax" style="font-size:10px">{{ p.cut.toFixed(2) }}</text>
        <text :x="xOf(i) + w * 1.5 + 2" :y="yOf(p.ml) - 5" text-anchor="middle" class="ax" style="font-size:10px" :style="{ opacity: reveal(1) }">{{ p.ml.toFixed(2) }}</text>
        <text :x="xOf(i) + w + 1" :y="Y0 + 16" text-anchor="middle" class="ax" :class="{ b: p.comb }">{{ p.l }}</text>
        <rect v-if="p.comb" :x="xOf(i) - 6" :y="Y1 - 6" :width="2 * w + 14" :height="Y0 - Y1 + 28" rx="5" fill="none" stroke="#f0c36e" stroke-dasharray="4 4" :style="{ opacity: reveal(2) }" />
      </g>
      <foreignObject :x="X0" :y="Y0 + 28" width="160" height="24"><div xmlns="http://www.w3.org/1999/xhtml" class="fo" v-html="mixed('year · $\\sqrt{s}$ [GeV]')" /></foreignObject>
      <g transform="translate(300 284)">
        <rect width="12" height="12" fill="#77c9ff" /><text x="18" y="10" class="lg">conventional</text>
        <rect x="110" width="12" height="12" fill="#baa5ff" :style="{ opacity: .3 + .7 * reveal(1) }" /><text x="128" y="10" class="lg" :style="{ opacity: .3 + .7 * reveal(1) }">machine learning</text>
      </g>
    </svg>
    <div class="gb-text">
      <h3 v-html="mixed(titles[stage])" />
      <p v-html="mixed(notes[stage])" />
    </div>
  </section>
</template>

<style scoped>
.gb { display: grid; grid-template-columns: 1.3fr 1fr; gap: 18px; align-items: center; }
.fo { font-size: 11px; color: #bcc2cb; line-height: 18px; white-space: nowrap; }
.gb-text h3 { margin: 0 0 10px; font-size: 19px; color: var(--nju-amber); font-weight: 550; line-height: 1.25; }
.gb-text p { margin: 0; font-size: 15px; line-height: 1.5; color: var(--fg-0); min-height: 110px; }
</style>
