<script setup lang="ts">
// Decorative chapter backgrounds in the EveNet seminar language: linked spin spheres,
// a barrel detector, reconstruction streams, a concentrating fit surface, a future ring.
// Illustrative motifs only — not a detector model, measured event, or factorization of rho.
import { computed, onBeforeUnmount, onMounted, ref, watch } from 'vue'
import { useSlideContext } from '@slidev/client'

const props = defineProps<{ scene: 'spin' | 'delphi' | 'reconstruct' | 'fit' | 'outlook' }>()
const canvas = ref<HTMLCanvasElement>()
const { $nav, $page, $renderContext } = useSlideContext()
const reduced = ref(false)
const hidden = ref(false)
const active = computed(() => $nav.value.currentPage === $page.value && $renderContext.value === 'slide' && !reduced.value && !hidden.value)

let media: MediaQueryList | undefined
let frame = 0
let last = 0
let time = 0
let ctx: CanvasRenderingContext2D | null = null

type P = [number, number, number]

function project(p: P, t: number): [number, number, number] {
  const turn = 0.46 + Math.sin(t * 0.045) * 0.06
  const [x, y, z] = p
  const a = x * Math.cos(turn) + z * Math.sin(turn)
  const b = -x * Math.sin(turn) + z * Math.cos(turn)
  const c = y * 0.64 - b * 0.768
  const d = y * 0.768 + b * 0.64
  const q = 860 / (860 + d)
  return [756 + (a * 0.89 + c * 0.456) * q * 1.25, 275 + (-a * 0.456 + c * 0.89) * q * 1.25, d]
}
function point(r: number, a: number, z: number): P {
  return [r * Math.cos(a), r * Math.sin(a), z]
}
function line2(points: number[][], color: string, width = 1) {
  if (!ctx || points.length < 2) return
  ctx.beginPath()
  points.forEach((p, i) => (i ? ctx.lineTo(p[0], p[1]) : ctx.moveTo(p[0], p[1])))
  ctx.strokeStyle = color
  ctx.lineWidth = width
  ctx.stroke()
}
function path(points: P[], t: number, color: string, width = 1) {
  line2(points.map(p => project(p, t)), color, width)
}
function dot(x: number, y: number, r: number, color: string) {
  if (!ctx) return
  ctx.beginPath()
  ctx.arc(x, y, r, 0, Math.PI * 2)
  ctx.fillStyle = color
  ctx.fill()
}

function spin(t: number) {
  if (!ctx) return
  const spheres: [number, number, number][] = [[605, 138, 132], [872, 362, 169]]
  for (let j = 0; j < 2; j++) {
    const [cx, cy, r] = spheres[j]
    const turn = t * 0.075 * (j ? -1 : 1)
    const sph = (a: number, b: number) => {
      const x = r * Math.cos(a) * Math.cos(b)
      const y = r * Math.sin(b)
      const z = r * Math.sin(a) * Math.cos(b)
      return [cx + x * Math.cos(turn) + z * Math.sin(turn), cy + y * 0.86 + (z * Math.cos(turn) - x * Math.sin(turn)) * 0.37]
    }
    for (let k = 1; k < 11; k++) {
      const b = -Math.PI / 2 + k * Math.PI / 11
      line2(Array.from({ length: 91 }, (_, i) => sph(i / 90 * Math.PI * 2, b)), j ? 'rgba(240,195,110,.23)' : 'rgba(119,201,255,.29)', 0.8)
    }
    for (let k = 0; k < 12; k++) line2(Array.from({ length: 91 }, (_, i) => sph(k * Math.PI / 6, i / 90 * Math.PI * 2)), j ? 'rgba(240,195,110,.2)' : 'rgba(119,201,255,.22)', 0.7)
    const a = t * 0.19 + (j ? Math.PI : 0)
    const b = 0.42 * Math.sin(t * 0.15)
    const tip = sph(a, b)
    line2([[cx, cy], tip], j ? 'rgba(255,220,159,.65)' : 'rgba(157,217,255,.65)', 1.6)
    ctx.beginPath()
    ctx.arc(tip[0], tip[1], 3, 0, Math.PI * 2)
    ctx.fillStyle = j ? '#d9b97d' : '#88bad7'
    ctx.fill()
  }
  for (let k = 0; k < 19; k++) {
    const ps = Array.from({ length: 81 }, (_, i) => {
      const u = i / 80
      const envelope = Math.sin(Math.PI * u)
      const a = u * Math.PI * 3 + t * 0.22 + k * 0.11
      return [605 + 267 * u + Math.sin(a) * envelope * (28 + k * 2), 138 + 224 * u + Math.cos(a) * envelope * (32 + k * 1.8)]
    })
    line2(ps, k % 2 ? 'rgba(240,195,110,.16)' : 'rgba(119,201,255,.18)', 0.7)
  }
  line2([[742, 248], [668, 189], [605, 138]], 'rgba(119,201,255,.6)', 1.2)
  line2([[742, 248], [798, 304], [872, 362]], 'rgba(240,195,110,.6)', 1.2)
  ctx.beginPath()
  ctx.arc(742, 248, 4, 0, Math.PI * 2)
  ctx.fillStyle = 'rgba(246,226,187,.65)'
  ctx.fill()
}

function detector(t: number) {
  if (!ctx) return
  const panels: { p: P[], depth: number, lit: number }[] = []
  const radius = 188
  for (const z0 of [-300, -270, -230, -190, -150, -110, 110, 150, 190, 230, 270, 300]) {
    const z = z0 + (z0 < 0 ? -1 : 1) * (16 + Math.sin(t * 0.11) * 8)
    for (let i = 0; i < 52; i++) {
      const a = i * Math.PI * 2 / 52
      const b = (i + 0.88) * Math.PI * 2 / 52
      const r = radius + (Math.abs(z0) > 260 ? 14 : 0)
      const ps = [point(r, a, z), point(r, b, z), point(r - 22, b, z), point(r - 22, a, z)]
      panels.push({ p: ps, depth: project(ps[0], t)[2], lit: (Math.cos(a - 0.7) + 1) / 2 })
    }
  }
  panels.sort((a, b) => b.depth - a.depth)
  for (const panel of panels) {
    ctx.beginPath()
    panel.p.forEach((p, i) => {
      const v = project(p, t)
      if (i) ctx!.lineTo(v[0], v[1])
      else ctx!.moveTo(v[0], v[1])
    })
    ctx.closePath()
    const l = Math.round(25 + panel.lit * 14)
    ctx.fillStyle = `rgb(${l + 3},${l + 2},${l})`
    ctx.fill()
    ctx.strokeStyle = `rgba(188,174,150,${0.09 + panel.lit * 0.2})`
    ctx.lineWidth = 0.65
    ctx.stroke()
  }
  for (let i = 0; i < 26; i++) {
    const a = i * Math.PI * 2 / 26
    path([point(radius + 4, a, -320), point(radius + 4, a, 320)], t, 'rgba(149,161,171,.2)', 0.7)
  }
  for (const z of [-60, -30, 0, 30, 60]) path(Array.from({ length: 81 }, (_, i) => point(118, i * Math.PI * 2 / 80, z)), t, 'rgba(119,201,255,.16)', 0.65)
  const phase = (t % 12) / 12
  path(Array.from({ length: 60 }, (_, i) => [0, 0, -550 + i * 1100 / 59] as P), t, 'rgba(180,197,212,.22)', 0.8)
  for (const sign of [-1, 1] as const) {
    const z = sign * (1 - phase) * 500
    path([[0, 0, z], [0, 0, z + sign * 65]], t, 'rgba(179,214,244,.55)', 1.5)
  }
  for (const side of [-1, 1] as const) {
    const vertex: P = [side * 86, side * 48, side * 18]
    path([[0, 0, 0], vertex], t, side < 0 ? 'rgba(119,201,255,.7)' : 'rgba(240,195,110,.7)', 1.7)
    const v = project(vertex, t)
    ctx.beginPath()
    ctx.arc(v[0], v[1], 5, 0, Math.PI * 2)
    ctx.strokeStyle = side < 0 ? 'rgba(157,217,255,.7)' : 'rgba(255,224,165,.7)'
    ctx.lineWidth = 1.1
    ctx.stroke()
    const branch: P[] = Array.from({ length: 48 }, (_, i) => {
      const u = i / 47
      return [vertex[0] + side * u * 210, vertex[1] + side * u * 70, vertex[2] + u * 40] as P
    })
    path(branch, t, side < 0 ? 'rgba(119,201,255,.4)' : 'rgba(240,195,110,.4)', 1.2)
    const offset = Math.floor((phase * 0.9) * 40)
    path(branch.slice(offset, offset + 7), t, 'rgba(255,229,184,.8)', 1.8)
  }
  const origin = project([0, 0, 0], t)
  const light = ctx.createRadialGradient(origin[0], origin[1], 0, origin[0], origin[1], 90)
  light.addColorStop(0, 'rgba(255,223,166,.16)')
  light.addColorStop(0.3, 'rgba(119,201,255,.045)')
  light.addColorStop(1, 'rgba(0,0,0,0)')
  ctx.fillStyle = light
  ctx.fillRect(origin[0] - 90, origin[1] - 90, 180, 180)
  ctx.beginPath()
  ctx.arc(origin[0], origin[1], 2.4, 0, Math.PI * 2)
  ctx.fillStyle = 'rgba(255,231,188,.75)'
  ctx.fill()
}

function reconstruct(t: number) {
  if (!ctx) return
  const cx = 746
  const cy = 276
  const palette = ['119,201,255', '186,165,255', '240,195,110', '255,145,181', '112,220,178']
  const glow = ctx.createRadialGradient(cx, cy, 10, cx, cy, 260)
  glow.addColorStop(0, 'rgba(186,165,255,.14)')
  glow.addColorStop(0.5, 'rgba(240,195,110,.04)')
  glow.addColorStop(1, 'rgba(240,195,110,0)')
  ctx.fillStyle = glow
  ctx.fillRect(cx - 260, cy - 260, 520, 520)
  const turn = t * 0.06
  const sphere = (a: number, b: number, r = 132) => {
    const x = r * Math.cos(b) * Math.cos(a + turn)
    const z = r * Math.cos(b) * Math.sin(a + turn)
    const y = r * Math.sin(b)
    return [cx + x * 0.9 + y * 0.32, cy + y * 0.9 - x * 0.28 + z * 0.23]
  }
  for (let k = 0; k < 16; k++) {
    const b = -Math.PI / 2 + (k + 1) * Math.PI / 17
    line2(Array.from({ length: 91 }, (_, i) => sphere(i / 90 * Math.PI * 2, b)), `rgba(186,165,255,${0.1 + 0.12 * Math.cos(b)})`, 0.7)
  }
  for (let k = 0; k < 24; k++) {
    const a = t * 0.09 + k * 0.26
    const stream = (u: number) => {
      const spread = (k - 11.5) * 9
      const blend = u * u * (3 - 2 * u)
      return [220 + u * (cx - 220), 520 + (cy - 520) * blend + spread * (1 - u) ** 1.6]
    }
    line2(Array.from({ length: 61 }, (_, i) => stream(i / 60)), `rgba(${palette[k % 5]},.18)`, 0.75)
    const phase = (t * 0.11 + k * 0.07) % 1
    const p = stream(phase)
    dot(p[0], p[1], 1.5, `rgba(${palette[k % 5]},.85)`)
  }
  const heads = [[938, 168, '119,201,255'], [938, 384, '240,195,110']] as const
  for (const [ex, ey, color] of heads) {
    const branch = (u: number) => [cx + u * (ex - cx), cy + (ey - cy) * (u * u * (3 - 2 * u))]
    line2(Array.from({ length: 61 }, (_, i) => branch(i / 60)), `rgba(${color},.35)`, 1.1)
    const p = branch((t * 0.14) % 1)
    dot(p[0], p[1], 2.2, `rgba(${color},.9)`)
    dot(ex, ey, 4, `rgba(${color},.85)`)
  }
}

function fit(t: number) {
  if (!ctx) return
  const focus = 0.5 - 0.5 * Math.cos(t * Math.PI / 10)
  const width = 100 - 46 * focus
  const height = (x: number, z: number) => {
    const primary = Math.exp(-((x - 35) ** 2 + (z + 15) ** 2) / (2 * width ** 2)) * (100 + 145 * focus)
    const secondary = Math.exp(-((x + 140) ** 2 + (z - 55) ** 2) / (2 * 70 ** 2)) * (65 - 25 * focus)
    return primary + secondary
  }
  const view = (x: number, z: number) => [735 + x * 0.95 + z * 0.42, 365 + z * 0.48 - x * 0.13 - height(x, z)]
  for (let z = -240; z <= 240; z += 12) {
    const ps = Array.from({ length: 71 }, (_, i) => view(-350 + i * 10, z))
    const next = Array.from({ length: 71 }, (_, i) => view(350 - i * 10, z + 12))
    ctx.beginPath()
    ;[...ps, ...next].forEach((p, i) => (i ? ctx!.lineTo(p[0], p[1]) : ctx!.moveTo(p[0], p[1])))
    ctx.closePath()
    ctx.fillStyle = 'rgba(27,28,31,.76)'
    ctx.fill()
    line2(ps, z > -90 && z < 90 ? 'rgba(240,195,110,.47)' : 'rgba(119,201,255,.24)', 0.8)
  }
  for (let x = -350; x <= 350; x += 17) line2(Array.from({ length: 61 }, (_, i) => view(x, -240 + i * 8)), 'rgba(183,199,210,.18)', 0.65)
}

function outlook(t: number) {
  if (!ctx) return
  const cx = 760
  const cy = 280
  for (let k = 0; k < 7; k++) {
    const r = 70 + k * 28
    const rot = t * 0.04 * (k % 2 ? -1 : 1)
    const dash = k % 2 ? [4, 8] : []
    ctx.beginPath()
    for (let i = 0; i <= 120; i++) {
      const a = rot + i / 120 * Math.PI * 2
      const x = cx + r * Math.cos(a)
      const y = cy + r * 0.42 * Math.sin(a)
      if (i) ctx.lineTo(x, y)
      else ctx.moveTo(x, y)
    }
    ctx.strokeStyle = `rgba(${k > 3 ? '240,195,110' : '119,201,255'},${0.08 + 0.04 * k})`
    ctx.lineWidth = 1
    ctx.setLineDash(dash)
    ctx.stroke()
    ctx.setLineDash([])
  }
  for (const side of [-1, 1] as const) {
    const end = [cx + side * 210, cy + side * 70]
    line2([[cx, cy], end], side < 0 ? 'rgba(119,201,255,.55)' : 'rgba(240,195,110,.55)', 1.5)
    const u = (t * 0.12 + (side < 0 ? 0 : 0.5)) % 1
    dot(cx + (end[0] - cx) * u, cy + (end[1] - cy) * u, 2.2, side < 0 ? 'rgba(186,229,255,.9)' : 'rgba(255,228,170,.9)')
    dot(end[0], end[1], 3.5, side < 0 ? 'rgba(119,201,255,.8)' : 'rgba(240,195,110,.8)')
  }
  const core = ctx.createRadialGradient(cx, cy, 0, cx, cy, 70)
  core.addColorStop(0, 'rgba(255,231,188,.45)')
  core.addColorStop(1, 'rgba(255,231,188,0)')
  ctx.fillStyle = core
  ctx.fillRect(cx - 70, cy - 70, 140, 140)
}

function render(t: number) {
  if (!ctx) return
  ctx.clearRect(0, 0, 980, 551)
  if (props.scene === 'spin') spin(t)
  else if (props.scene === 'delphi') detector(t)
  else if (props.scene === 'reconstruct') reconstruct(t)
  else if (props.scene === 'fit') fit(t)
  else outlook(t)
}
function tick(stamp: number) {
  if (!active.value) return
  if (stamp - last >= 33) {
    time += last ? Math.min((stamp - last) / 1000, 0.1) : 0
    last = stamp
    render(time)
  }
  frame = requestAnimationFrame(tick)
}
function sync() {
  cancelAnimationFrame(frame)
  last = 0
  render(time)
  if (active.value) frame = requestAnimationFrame(tick)
}
function motionChange() {
  reduced.value = !!media?.matches
}
function visibility() {
  hidden.value = document.hidden
}

onMounted(() => {
  const c = canvas.value
  if (!c) return
  const dpr = Math.min(window.devicePixelRatio || 1, 2)
  c.width = 980 * dpr
  c.height = 551 * dpr
  ctx = c.getContext('2d')
  ctx?.scale(dpr, dpr)
  media = window.matchMedia('(prefers-reduced-motion: reduce)')
  media.addEventListener('change', motionChange)
  document.addEventListener('visibilitychange', visibility)
  motionChange()
  visibility()
  sync()
})
watch(active, sync)
onBeforeUnmount(() => {
  cancelAnimationFrame(frame)
  media?.removeEventListener('change', motionChange)
  document.removeEventListener('visibilitychange', visibility)
})
</script>

<template>
  <div class="tk-chapter-scene" :data-scene="scene" aria-hidden="true">
    <canvas ref="canvas" />
    <template v-if="scene === 'spin'">
      <div class="tk-scene-label tau-p"><LaTeX formula="\tau^+" /></div>
      <div class="tk-scene-label tau-m"><LaTeX formula="\tau^-" /></div>
      <div class="tk-scene-label z"><LaTeX formula="Z" /></div>
      <div class="tk-scene-label rho"><LaTeX formula="\rho_{\tau^+\tau^-}" /></div>
    </template>
    <template v-if="scene === 'reconstruct'">
      <div class="tk-scene-label head-a">decay mode</div>
      <div class="tk-scene-label head-b">direction</div>
    </template>
    <div class="tk-chapter-shade" />
  </div>
</template>

<style scoped>
.tk-chapter-scene { position: absolute; inset: 0; z-index: 0; overflow: hidden; pointer-events: none; }
.tk-chapter-scene canvas { display: block; width: 100%; height: 100%; opacity: .88; }
.tk-chapter-shade {
  position: absolute; inset: 0;
  background:
    linear-gradient(90deg, rgba(12,13,15,.97) 0%, rgba(12,13,15,.82) 34%, rgba(12,13,15,.4) 64%, rgba(12,13,15,.06) 100%),
    linear-gradient(0deg, rgba(12,13,15,.94), transparent 22%, transparent 86%, rgba(12,13,15,.2));
}
.tk-scene-label { position: absolute; color: #d9bd8e; opacity: .55; font-size: 26px; line-height: 1; pointer-events: none; }
.tau-p { left: 60%; top: 21%; color: #99cee9; }
.tau-m { left: 87%; top: 65%; }
.z { left: 75%; top: 39%; font-size: 20px; }
.rho { left: 84%; top: 8%; font-size: 32px; }
.head-a { left: 88%; top: 24%; font-size: 13px; letter-spacing: .08em; text-transform: uppercase; color: #99cee9; }
.head-b { left: 88%; top: 66%; font-size: 13px; letter-spacing: .08em; text-transform: uppercase; }
@media print { .tk-chapter-scene canvas { opacity: .5; } }
</style>
