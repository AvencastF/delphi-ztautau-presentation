<script setup lang="ts">
// Four decay illustrations and four angular distributions. Every 2 s, while this
// slide is on screen, one mode is lit: its particles, its kappa line, and its table row.
import { computed, onBeforeUnmount, onMounted, ref, watch } from 'vue'
import { useSlideContext } from '@slidev/client'
import { mixed } from 'slidev-addon-ztautau/composable/tex'

type Part = { tex: string, deg: number, len: number, color: string, dash: boolean, marker: string }
type Mode = { id: string, decay: string, br: string, kappa: string, k: number, color: string, parts: Part[] }

const CX = 150, CY = 118, TAU_R = 20
const NU = '#8b939e'
// The fan under the tau is only a layout, so the particles can be read. It is not
// the decay angle: that distribution is the line in the middle plot.
const modes: Mode[] = [
  {
    id: 'pi', decay: '\\pi\\nu', br: '10.82\\,\\%', kappa: '1.00', k: 1, color: '#77c9ff',
    parts: [
      { tex: '\\pi^-', deg: 200, len: 48, color: '#77c9ff', dash: false, marker: 'blue' },
      { tex: '\\nu_\\tau', deg: 145, len: 40, color: NU, dash: true, marker: 'gray' },
    ],
  },
  {
    id: 'rho', decay: '\\rho\\nu', br: '25.49\\,\\%', kappa: '0.41', k: 0.41, color: '#f0c36e',
    parts: [
      { tex: '\\pi^-', deg: 220, len: 46, color: '#f0c36e', dash: false, marker: 'gold' },
      { tex: '\\pi^0', deg: 145, len: 44, color: '#f0c36e', dash: false, marker: 'gold' },
      { tex: '\\nu_\\tau', deg: 180, len: 34, color: NU, dash: true, marker: 'gray' },
    ],
  },
  {
    id: 'e', decay: 'e\\nu\\nu', br: '17.82\\,\\%', kappa: '-0.33', k: -0.33, color: '#70dcb2',
    parts: [
      { tex: 'e^-', deg: 180, len: 48, color: '#70dcb2', dash: false, marker: 'mint' },
      { tex: '\\bar\\nu_e', deg: 225, len: 40, color: NU, dash: true, marker: 'gray' },
      { tex: '\\nu_\\tau', deg: 135, len: 40, color: NU, dash: true, marker: 'gray' },
    ],
  },
  {
    id: 'mu', decay: '\\mu\\nu\\nu', br: '17.39\\,\\%', kappa: '-0.34', k: -0.34, color: '#d2b4ff',
    parts: [
      { tex: '\\mu^-', deg: 180, len: 48, color: '#d2b4ff', dash: false, marker: 'mu' },
      { tex: '\\bar\\nu_\\mu', deg: 225, len: 40, color: NU, dash: true, marker: 'gray' },
      { tex: '\\nu_\\tau', deg: 135, len: 40, color: NU, dash: true, marker: 'gray' },
    ],
  },
]

const index = ref(0)
const reduced = ref(false)
const { $nav, $page, $renderContext } = useSlideContext()
const playing = computed(() => $nav.value.currentPage === $page.value && $renderContext.value === 'slide' && !reduced.value)
let timer: ReturnType<typeof setInterval> | undefined
let media: MediaQueryList | undefined

function arm() {
  if (timer) clearInterval(timer)
  timer = undefined
  if (playing.value) timer = setInterval(() => { index.value = (index.value + 1) % modes.length }, 2000)
}
function onMotion() { reduced.value = !!media?.matches }
onMounted(() => {
  media = window.matchMedia('(prefers-reduced-motion: reduce)')
  media.addEventListener('change', onMotion)
  onMotion()
  arm()
})
onBeforeUnmount(() => { if (timer) clearInterval(timer); media?.removeEventListener('change', onMotion) })
watch(playing, arm)

const mode = computed(() => modes[index.value])
function end(deg: number, len: number) {
  const r = deg * Math.PI / 180
  return { x: CX + len * Math.sin(r), y: CY - len * Math.cos(r) }
}
function shaft(deg: number, len: number) {
  const a = end(deg, TAU_R + 3)
  const b = end(deg, TAU_R + 3 + len)
  return { x1: a.x, y1: a.y, x2: b.x, y2: b.y }
}
function labelAt(deg: number, len: number) {
  const p = end(deg, TAU_R + len + 14)
  const r = deg * Math.PI / 180
  const up = Math.cos(r) > 0.8
  const left = up || Math.sin(r) < -0.15
  const w = 72
  return { x: left ? p.x - w : p.x + 4, y: p.y - 12, w, align: left ? 'right' : 'left' }
}

const X0 = 54, X1 = 262, Y0 = 208, Y1 = 78
const px = (c: number) => X0 + ((c + 1) / 2) * (X1 - X0)
const py = (v: number) => Y0 - v * (Y0 - Y1)
const curve = computed(() => {
  const k = mode.value.k
  const pts: string[] = []
  for (let i = 0; i <= 48; i++) {
    const c = -1 + (2 * i) / 48
    pts.push(`${px(c).toFixed(1)},${py(0.5 * (1 + k * c)).toFixed(1)}`)
  }
  return 'M' + pts.join(' L')
})
</script>

<template>
  <section class="an" :data-i="index">
    <div class="an-col">
      <div class="an-stage">
      <svg viewBox="20 8 250 220" role="img" aria-label="Decay products relative to the tau spin. The picture changes with the highlighted decay.">
        <defs>
          <marker id="mk-gold" markerWidth="6" markerHeight="6" refX="5" refY="3" orient="auto"><path d="M0 0 L6 3 L0 6 z" fill="#f0c36e" /></marker>
          <marker id="mk-blue" markerWidth="6" markerHeight="6" refX="5" refY="3" orient="auto"><path d="M0 0 L6 3 L0 6 z" fill="#77c9ff" /></marker>
          <marker id="mk-white" markerWidth="6" markerHeight="6" refX="5" refY="3" orient="auto"><path d="M0 0 L6 3 L0 6 z" fill="#f0f1f3" /></marker>
          <marker id="mk-violet" markerWidth="6" markerHeight="6" refX="5" refY="3" orient="auto"><path d="M0 0 L6 3 L0 6 z" fill="#baa5ff" /></marker>
          <marker id="mk-mint" markerWidth="6" markerHeight="6" refX="5" refY="3" orient="auto"><path d="M0 0 L6 3 L0 6 z" fill="#70dcb2" /></marker>
          <marker id="mk-mu" markerWidth="6" markerHeight="6" refX="5" refY="3" orient="auto"><path d="M0 0 L6 3 L0 6 z" fill="#d2b4ff" /></marker>
          <marker id="mk-gray" markerWidth="6" markerHeight="6" refX="5" refY="3" orient="auto"><path d="M0 0 L6 3 L0 6 z" fill="#8b939e" /></marker>
          <marker id="mk-axis" markerWidth="6" markerHeight="6" refX="5" refY="3" orient="auto"><path d="M0 0 L6 3 L0 6 z" fill="#9aa3af" /></marker>
        </defs>
        <g v-for="(part, i) in mode.parts" :key="mode.id + i">
          <line
            :x1="shaft(part.deg, part.len).x1" :y1="shaft(part.deg, part.len).y1"
            :x2="shaft(part.deg, part.len).x2" :y2="shaft(part.deg, part.len).y2"
            :stroke="part.color" stroke-width="1.45"
            :stroke-dasharray="part.dash ? '3 3' : undefined"
            :marker-end="`url(#mk-${part.marker})`"
          />
          <foreignObject :x="labelAt(part.deg, part.len).x" :y="labelAt(part.deg, part.len).y" :width="labelAt(part.deg, part.len).w" height="20">
            <div xmlns="http://www.w3.org/1999/xhtml" class="fo sm" :style="{ color: part.color, textAlign: labelAt(part.deg, part.len).align }" v-html="mixed(`$${part.tex}$`)" />
          </foreignObject>
        </g>
        <circle :cx="CX" :cy="CY" :r="TAU_R" fill="#23262b" stroke="#f0c36e" stroke-width="1.35" />
        <foreignObject :x="CX - 22" :y="CY - 13" width="44" height="26"><div xmlns="http://www.w3.org/1999/xhtml" class="fo tau" v-html="mixed('$\\tau^-$')" /></foreignObject>
        <line :x1="CX" :y1="CY - TAU_R - 2" :x2="CX" :y2="CY - TAU_R - 40" stroke="#f0c36e" stroke-width="1.6" marker-end="url(#mk-gold)" />
        <foreignObject :x="CX + 8" :y="CY - TAU_R - 44" width="56" height="18"><div xmlns="http://www.w3.org/1999/xhtml" class="fo sm" style="color:#f0c36e;text-align:left" v-html="mixed('spin')" /></foreignObject>
      </svg>
      </div>
      <p class="an-cap" v-html="mixed('$\\tau$ rest frame. Mean flight $\\gamma c\\tau \\approx 2.2$ mm at $45.6$ GeV.')" />
    </div>

    <div class="an-col">
      <div class="an-stage">
      <svg viewBox="0 0 300 280" role="img" aria-label="Angular distribution of the highlighted decay.">
        <defs>
          <marker id="mk-axis" markerWidth="6" markerHeight="6" refX="5" refY="3" orient="auto"><path d="M0 0 L6 3 L0 6 z" fill="#9aa3af" /></marker>
        </defs>
        <line :x1="X0" :y1="Y0" :x2="X1 + 14" :y2="Y0" stroke="#9aa3af" stroke-width="1.15" marker-end="url(#mk-axis)" />
        <line :x1="X0" :y1="Y0" :x2="X0" :y2="Y1 - 18" stroke="#9aa3af" stroke-width="1.15" marker-end="url(#mk-axis)" />
        <line :x1="px(0)" :y1="Y0" :x2="px(0)" :y2="Y0 + 5" stroke="#9aa3af" stroke-width="1" />
        <path :d="curve" fill="none" :stroke="mode.color" stroke-width="2" />
        <foreignObject :x="X0 - 22" :y="Y0 + 8" width="32" height="18"><div xmlns="http://www.w3.org/1999/xhtml" class="fo sm" v-html="mixed('$-1$')" /></foreignObject>
        <foreignObject :x="px(0) - 8" :y="Y0 + 8" width="24" height="18"><div xmlns="http://www.w3.org/1999/xhtml" class="fo sm" v-html="mixed('$0$')" /></foreignObject>
        <foreignObject :x="X1 - 8" :y="Y0 + 8" width="28" height="18"><div xmlns="http://www.w3.org/1999/xhtml" class="fo sm" v-html="mixed('$+1$')" /></foreignObject>
        <foreignObject :x="X0 + 52" :y="Y0 + 26" width="140" height="18"><div xmlns="http://www.w3.org/1999/xhtml" class="fo sm" v-html="mixed('$\\cos\\theta$')" /></foreignObject>
        <foreignObject :x="X0 - 26" :y="Y1 - 6" width="24" height="18"><div xmlns="http://www.w3.org/1999/xhtml" class="fo sm" v-html="mixed('$1$')" /></foreignObject>
        <foreignObject :x="X0 - 26" :y="Y0 - 18" width="24" height="18"><div xmlns="http://www.w3.org/1999/xhtml" class="fo sm" v-html="mixed('$0$')" /></foreignObject>
        <foreignObject :x="X0 + 12" y="20" width="190" height="22">
          <div xmlns="http://www.w3.org/1999/xhtml" class="fo lab" :style="{ color: mode.color, textAlign: 'left' }" v-html="mixed(`$\\kappa=${mode.kappa}$, $P=1$`)" />
        </foreignObject>
      </svg>
      </div>
      <p class="an-cap" v-html="mixed('$\\dfrac{1}{\\Gamma}\\dfrac{d\\Gamma}{d\\cos\\theta} = \\tfrac12\\,(1 + \\kappa P\\cos\\theta)$')" />
    </div>

    <div class="an-col">
      <div class="an-stage">
      <table class="an-table num">
        <thead>
          <tr>
            <th>Decay</th>
            <th>Branching fraction</th>
            <th v-html="mixed('$\\kappa$')" />
          </tr>
        </thead>
        <tbody>
          <tr v-for="(row, i) in modes" :key="row.id" :class="{ on: i === index }" :style="{ '--mode': row.color }">
            <td v-html="mixed(`$${row.decay}$`)" />
            <td v-html="mixed(`$${row.br}$`)" />
            <td v-html="mixed(`$${row.kappa}$`)" />
          </tr>
        </tbody>
      </table>
      </div>
      <p class="an-cap" v-html="mixed('The $\\rho$ fraction is $\\tau\\to\\pi\\pi^0\\nu$.')" />
    </div>
  </section>
</template>

<style scoped>
.an { display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 40px; align-items: start; margin-top: 18px; }
.an-col { display: grid; grid-template-rows: 330px auto; justify-items: center; min-width: 0; }
.an-stage { height: 330px; width: 100%; display: flex; align-items: center; }
.an svg { width: 100%; height: 100%; display: block; overflow: visible; }
.fo { line-height: 17px; white-space: nowrap; color: #bcc2cb; text-align: center; }
.fo.lab { font-size: 13px; color: #f0f1f3; }
.fo.sm { font-size: 12px; }
.fo.tau { font-size: 13px; color: #f0f1f3; line-height: 26px; text-align: center; }
.an-cap { margin: 8px 0 0; font-size: 13px; line-height: 1.35; color: var(--fg-1); text-align: center; }
.an-table { width: 100%; font-size: 15px; }
.an-table th, .an-table td { text-align: right; }
.an-table th:first-child, .an-table td:first-child { text-align: left; }
.an-table tbody td { color: var(--mode); }
.an-table :deep(.katex) { color: inherit; }
.an-table tr.on td { background: color-mix(in srgb, var(--mode) 18%, transparent); font-weight: 600; }
</style>
