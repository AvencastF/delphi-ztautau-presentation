<script setup>
// Title-page scene: the landing page's decorative Z -> tau+ tau- canvas (gh-pages/assets/tau-scene.js),
// ported to a Vue component. Purely illustrative: not a detector model, not a measurement, not a
// simulation. Ring radii, track shapes, decay topologies, spin arrows and the resonance curve are drawn
// for visual effect only. Animates only while this slide is the current, visible, motion-allowed slide.
import { computed, onBeforeUnmount, onMounted, ref, watch } from 'vue'
import { useSlideContext } from '@slidev/client'

const canvas = ref(null)
const { $nav, $page, $renderContext } = useSlideContext()
const active = computed(() => $nav.value.currentPage === $page.value && $renderContext.value === 'slide')

const W = 980, H = 551, VX = 700, VY = 300
const AMBER = '240,195,110', AMBER_HI = '255,228,170', BLUE = '119,201,255', BLUE_HI = '186,229,255'
const VIOLET = '186,165,255', MINT = '112,220,178', CORAL = '246,156,171', STEEL = '190,201,214'
const FONT = '"DM Sans", "Avenir Next", "Segoe UI", Helvetica, Arial, sans-serif'
const TOPOLOGY_PERIOD = 5.2, CROSSFADE = 0.9, STATIC_TIME = 1.6

const RINGS = [
  { r: 30, alpha: 0.09 }, { r: 52, alpha: 0.07 }, { r: 84, alpha: 0.07, dash: [2, 5] }, { r: 122, alpha: 0.06 },
  { r: 168, alpha: 0.055 }, { r: 210, alpha: 0.06, segments: 24, gap: 0.035 }, { r: 252, alpha: 0.05, segments: 24, gap: 0.035 },
  { r: 304, alpha: 0.04, segments: 16, gap: 0.05 },
]
const TOPOLOGIES = [
  { charged: [{ a: -0.16, len: 128, bend: 7 }], neutral: [{ a: 0.3, len: 138 }] },
  { charged: [{ a: -0.3, len: 120, bend: 9 }], neutral: [{ a: 0.14, len: 136 }, { a: 0.42, len: 112 }] },
  { charged: [{ a: -0.4, len: 112, bend: 8 }, { a: -0.12, len: 132, bend: -6 }, { a: 0.14, len: 120, bend: 7 }], neutral: [{ a: 0.44, len: 128 }] },
]
function mulberry32(seed) {
  return function () {
    seed |= 0; seed = (seed + 0x6d2b79f5) | 0
    let t = Math.imul(seed ^ (seed >>> 15), 1 | seed)
    t = (t + Math.imul(t ^ (t >>> 7), 61 | t)) ^ t
    return ((t ^ (t >>> 14)) >>> 0) / 4294967296
  }
}
const rand = mulberry32(19940822)
const FIELD = Array.from({ length: 96 }, () => ({
  x: rand() * (W + 40), y: rand() * H, r: 0.6 + rand() * 1.1, a: 0.05 + rand() * 0.13,
  vx: 3 + rand() * 7, vy: (rand() - 0.5) * 3, tw: rand() * Math.PI * 2, warm: rand() < 0.35,
}))
const smoothstep = x => { const u = Math.min(1, Math.max(0, x)); return u * u * (3 - 2 * u) }
function lineShape(E) { const M = 91.19, G = 2.495, s = E * E; return (s * G * G) / ((s - M * M) ** 2 + (s * s * G * G) / (M * M)) }

let ctx = null, frame = 0, last = 0, time = STATIC_TIME, reduced = false, hidden = false, media, dpr = 1, ro

function stroke(points, color, width, dash) {
  if (!ctx || points.length < 2) return
  ctx.beginPath(); points.forEach((p, i) => (i ? ctx.lineTo(p[0], p[1]) : ctx.moveTo(p[0], p[1])))
  ctx.strokeStyle = color; ctx.lineWidth = width; ctx.setLineDash(dash || []); ctx.stroke(); ctx.setLineDash([])
}
function dot(x, y, r, color) { ctx.beginPath(); ctx.arc(x, y, r, 0, Math.PI * 2); ctx.fillStyle = color; ctx.fill() }
function label(text, x, y, color, size, align) {
  ctx.font = `500 ${size || 11}px ${FONT}`; ctx.textAlign = align || 'center'; ctx.textBaseline = 'middle'; ctx.fillStyle = color; ctx.fillText(text, x, y)
}
function field(t) {
  const span = W + 40
  for (const p of FIELD) {
    const x = ((p.x + p.vx * t) % span) - 20
    const y = p.y + p.vy * t * 0.2 + Math.sin(t * 0.21 + p.tw) * 4
    const a = p.a * (0.7 + 0.3 * Math.sin(t * 0.6 + p.tw))
    dot(x, ((y % H) + H) % H, p.r, `rgba(${p.warm ? AMBER : STEEL},${a.toFixed(3)})`)
  }
}
function rings(t) {
  for (const ring of RINGS) {
    const color = `rgba(${STEEL},${ring.alpha})`
    if (ring.segments) {
      const step = (Math.PI * 2) / ring.segments, rot = t * 0.004
      for (let k = 0; k < ring.segments; k++) {
        ctx.beginPath(); ctx.arc(VX, VY, ring.r, rot + k * step + ring.gap, rot + (k + 1) * step - ring.gap)
        ctx.strokeStyle = color; ctx.lineWidth = 1; ctx.stroke()
      }
    } else {
      ctx.beginPath(); ctx.arc(VX, VY, ring.r, 0, Math.PI * 2); ctx.strokeStyle = color; ctx.lineWidth = 0.8
      ctx.setLineDash(ring.dash || []); ctx.stroke(); ctx.setLineDash([])
    }
  }
  for (let k = 0; k < 24; k++) {
    const a = (k / 24) * Math.PI * 2 + t * 0.004
    stroke([[VX + Math.cos(a) * 214, VY + Math.sin(a) * 214], [VX + Math.cos(a) * 248, VY + Math.sin(a) * 248]], `rgba(${STEEL},.035)`, 0.8)
  }
}
function resonance(t, pulse) {
  const E0 = 87.6, E1 = 94.8, x0 = 560, x1 = 960, base = 526, height = 112
  const ex = E => x0 + ((E - E0) / (E1 - E0)) * (x1 - x0)
  const ey = E => base - lineShape(E) * height
  const curve = Array.from({ length: 121 }, (_, i) => { const E = E0 + (i / 120) * (E1 - E0); return [ex(E), ey(E)] })
  const fill = ctx.createLinearGradient(0, base - height, 0, base)
  fill.addColorStop(0, `rgba(${AMBER},.08)`); fill.addColorStop(1, `rgba(${AMBER},0)`)
  ctx.beginPath(); curve.forEach((p, i) => (i ? ctx.lineTo(p[0], p[1]) : ctx.moveTo(p[0], p[1])))
  ctx.lineTo(x1, base); ctx.lineTo(x0, base); ctx.closePath(); ctx.fillStyle = fill; ctx.fill()
  stroke(curve, `rgba(${AMBER},.34)`, 1.2)
  stroke([[x0, base], [x1, base]], `rgba(${STEEL},.22)`, 0.8)
  for (let E = 88; E <= 94; E++) stroke([[ex(E), base], [ex(E), base + 4]], `rgba(${STEEL},.22)`, 0.8)
  label('√s [GeV]', x1, base + 14, `rgba(${STEEL},.42)`, 10, 'right')
  const points = [{ E: 89.4, text: '89.4', color: CORAL }, { E: 91.2, text: '91.2', color: AMBER }, { E: 93.0, text: '93.0', color: CORAL }]
  for (const p of points) {
    const x = ex(p.E), y = ey(p.E)
    stroke([[x, y + 5], [x, base]], `rgba(${p.color},.16)`, 0.8, [2, 3])
    const peak = p.E === 91.2, r = peak ? 3 + pulse * 1.2 : 2.6
    ctx.beginPath(); ctx.arc(x, y, r + 3, 0, Math.PI * 2); ctx.strokeStyle = `rgba(${p.color},${peak ? 0.22 + pulse * 0.25 : 0.24})`; ctx.lineWidth = 0.9; ctx.stroke()
    dot(x, y, r, `rgba(${p.color},.78)`); label(p.text, x, y - 15, `rgba(${p.color},.62)`, 10)
  }
}
function beams(t) {
  const y = VY
  stroke([[0, y], [VX - 8, y]], `rgba(${STEEL},.2)`, 0.9); stroke([[W, y], [VX + 8, y]], `rgba(${STEEL},.2)`, 0.9)
  const period = 3.4
  for (let k = 0; k < 2; k++) {
    const u = ((t / period + k * 0.5) % 1 + 1) % 1
    const fade = Math.sin(Math.PI * Math.min(1, u * 1.08)) ** 0.6
    const lx = u * (VX - 8), rx = W - u * (W - VX - 8)
    const left = ctx.createLinearGradient(lx - 46, y, lx, y)
    left.addColorStop(0, `rgba(${BLUE_HI},0)`); left.addColorStop(1, `rgba(${BLUE_HI},${(0.7 * fade).toFixed(3)})`)
    stroke([[lx - 46, y], [lx, y]], left, 1.6); dot(lx, y, 1.8, `rgba(${BLUE_HI},${(0.85 * fade).toFixed(3)})`)
    const right = ctx.createLinearGradient(rx + 30, y, rx, y)
    right.addColorStop(0, `rgba(${AMBER_HI},0)`); right.addColorStop(1, `rgba(${AMBER_HI},${(0.7 * fade).toFixed(3)})`)
    stroke([[rx + 30, y], [rx, y]], right, 1.6); dot(rx, y, 1.8, `rgba(${AMBER_HI},${(0.85 * fade).toFixed(3)})`)
  }
  label('e⁻', 520, y - 12, `rgba(${BLUE_HI},.5)`, 12); label('e⁺', 940, y - 12, `rgba(${AMBER_HI},.5)`, 12)
}
function zGlow(pulse) {
  const R = 74 + pulse * 18
  const glow = ctx.createRadialGradient(VX, VY, 0, VX, VY, R)
  glow.addColorStop(0, `rgba(255,232,180,${(0.5 + pulse * 0.25).toFixed(3)})`)
  glow.addColorStop(0.16, `rgba(${AMBER},${(0.22 + pulse * 0.12).toFixed(3)})`)
  glow.addColorStop(0.55, `rgba(${CORAL},.05)`); glow.addColorStop(1, `rgba(${CORAL},0)`)
  ctx.fillStyle = glow; ctx.fillRect(VX - R, VY - R, R * 2, R * 2)
}
function hitsAlong(points, alpha) {
  for (let i = 1; i < points.length; i++) {
    const r0 = Math.hypot(points[i - 1][0] - VX, points[i - 1][1] - VY), r1 = Math.hypot(points[i][0] - VX, points[i][1] - VY)
    for (const ring of RINGS) if (r0 < ring.r && r1 >= ring.r) dot(points[i][0], points[i][1], 1.5, `rgba(${MINT},${(0.55 * alpha).toFixed(3)})`)
  }
}
function decayFan(D, dir, topo, alpha, colorHi) {
  if (alpha <= 0.01) return
  for (const nu of topo.neutral) {
    const a = dir + nu.a, E = [D[0] + Math.cos(a) * nu.len, D[1] + Math.sin(a) * nu.len]
    const g = ctx.createLinearGradient(D[0], D[1], E[0], E[1])
    g.addColorStop(0, `rgba(${VIOLET},${(0.8 * alpha).toFixed(3)})`); g.addColorStop(0.7, `rgba(${VIOLET},${(0.3 * alpha).toFixed(3)})`); g.addColorStop(1, `rgba(${VIOLET},0)`)
    stroke([D, E], g, 1.3, [5, 5])
  }
  for (const ch of topo.charged) {
    const a = dir + ch.a, ux = Math.cos(a), uy = Math.sin(a)
    const E = [D[0] + ux * ch.len, D[1] + uy * ch.len]
    const C = [(D[0] + E[0]) / 2 - uy * ch.bend * 2, (D[1] + E[1]) / 2 + ux * ch.bend * 2]
    const pts = Array.from({ length: 33 }, (_, i) => { const s = i / 32, m = 1 - s; return [m * m * D[0] + 2 * m * s * C[0] + s * s * E[0], m * m * D[1] + 2 * m * s * C[1] + s * s * E[1]] })
    stroke(pts, `rgba(${colorHi},${(0.82 * alpha).toFixed(3)})`, 1.35); hitsAlong(pts, alpha)
    dot(E[0], E[1], 2.2, `rgba(${colorHi},${(0.75 * alpha).toFixed(3)})`)
  }
  dot(D[0], D[1], 2, `rgba(${colorHi},${(0.9 * Math.max(alpha, 0.4)).toFixed(3)})`)
}
function topologyMix(t, offset, shift) {
  const lt = t + offset, k = Math.floor(lt / TOPOLOGY_PERIOD), f = lt - k * TOPOLOGY_PERIOD
  const mix = smoothstep((f - (TOPOLOGY_PERIOD - CROSSFADE)) / CROSSFADE), n = TOPOLOGIES.length
  return [{ topo: TOPOLOGIES[(((k + shift) % n) + n) % n], alpha: 1 - mix }, { topo: TOPOLOGIES[(((k + shift + 1) % n) + n) % n], alpha: mix }]
}
function spinArrow(c, axis, phase, color) {
  const ux = Math.cos(axis), uy = Math.sin(axis), a = 22, b = 10
  ctx.beginPath(); ctx.ellipse(c[0], c[1], a, b, axis, 0, Math.PI * 2); ctx.strokeStyle = `rgba(${color},.28)`; ctx.lineWidth = 0.8; ctx.setLineDash([2, 3]); ctx.stroke(); ctx.setLineDash([])
  const vx = Math.cos(phase) * a * ux - Math.sin(phase) * b * uy, vy = Math.cos(phase) * a * uy + Math.sin(phase) * b * ux
  const tail = [c[0] - vx * 0.55, c[1] - vy * 0.55], tip = [c[0] + vx, c[1] + vy]
  stroke([tail, tip], `rgba(${color},.95)`, 2)
  const len = Math.hypot(vx, vy) || 1, hx = vx / len, hy = vy / len, s = 6
  ctx.beginPath(); ctx.moveTo(tip[0] + hx * 1.5, tip[1] + hy * 1.5)
  ctx.lineTo(tip[0] - hx * s - hy * s * 0.6, tip[1] - hy * s + hx * s * 0.6); ctx.lineTo(tip[0] - hx * s + hy * s * 0.6, tip[1] - hy * s - hx * s * 0.6)
  ctx.closePath(); ctx.fillStyle = `rgba(${color},.95)`; ctx.fill(); dot(c[0], c[1], 1.6, `rgba(${color},.9)`)
}
function tauPair(t) {
  const axis = -0.52 + 0.05 * Math.sin(t * 0.07), spin = t * 0.55, flight = 118
  const taus = [
    { dir: axis, color: AMBER, hi: AMBER_HI, name: 'τ⁻', spin, offset: 0, shift: 0 },
    { dir: axis + Math.PI, color: BLUE, hi: BLUE_HI, name: 'τ⁺', spin: spin + Math.PI, offset: TOPOLOGY_PERIOD / 2, shift: 2 },
  ]
  for (const tau of taus) {
    const ux = Math.cos(tau.dir), uy = Math.sin(tau.dir), D = [VX + ux * flight, VY + uy * flight]
    for (const layer of topologyMix(t, tau.offset, tau.shift)) decayFan(D, tau.dir, layer.topo, layer.alpha, tau.hi)
    const g = ctx.createLinearGradient(VX, VY, D[0], D[1]); g.addColorStop(0, `rgba(${tau.color},.95)`); g.addColorStop(1, `rgba(${tau.color},.7)`)
    stroke([[VX, VY], D], g, 1.9)
    const u = (t / 2.2) % 1, pulseA = Math.sin(Math.PI * u)
    dot(VX + ux * flight * u, VY + uy * flight * u, 2.1, `rgba(${tau.hi},${(0.85 * pulseA).toFixed(3)})`)
    const c = [VX + ux * flight * 0.56, VY + uy * flight * 0.56]
    spinArrow(c, axis, tau.spin, tau.hi); label(tau.name, c[0] - uy * 30, c[1] + ux * 30, `rgba(${tau.hi},.75)`, 14)
  }
}
function scene(t) {
  const pulse = 0.5 + 0.5 * Math.sin((t * Math.PI * 2) / 4.2)
  field(t); rings(t); resonance(t, pulse); beams(t); zGlow(pulse); tauPair(t); dot(VX, VY, 2.6, 'rgba(255,240,206,.95)')
}
function render(t) {
  const el = canvas.value
  if (!ctx || !el) return
  ctx.setTransform(dpr, 0, 0, dpr, 0, 0)
  const cssW = el.clientWidth || W, cssH = el.clientHeight || H
  ctx.clearRect(0, 0, cssW, cssH)
  const scale = Math.max(cssW / W, cssH / H)
  ctx.save(); ctx.translate((cssW - W * scale) * 0.55, (cssH - H * scale) * 0.35); ctx.scale(scale, scale); scene(t); ctx.restore()
}
function tick(stamp) {
  if (reduced || hidden || !active.value) return
  if (stamp - last >= 33) { time += last ? Math.min((stamp - last) / 1000, 0.1) : 0; last = stamp; render(time) }
  frame = requestAnimationFrame(tick)
}
function sync() {
  cancelAnimationFrame(frame); last = 0
  if (reduced) time = STATIC_TIME
  render(time)
  if (!reduced && !hidden && active.value) frame = requestAnimationFrame(tick)
}
function resize() {
  const el = canvas.value
  if (!el) return
  dpr = Math.min(window.devicePixelRatio || 1, 2)
  const cssW = el.clientWidth || W, cssH = el.clientHeight || H
  el.width = Math.round(cssW * dpr); el.height = Math.round(cssH * dpr)
  ctx = el.getContext('2d'); sync()
}
const onMotion = () => { reduced = !!media?.matches; sync() }
const onVisibility = () => { hidden = document.hidden; sync() }
onMounted(() => {
  media = window.matchMedia('(prefers-reduced-motion: reduce)')
  media.addEventListener('change', onMotion)
  document.addEventListener('visibilitychange', onVisibility)
  ro = new ResizeObserver(resize); ro.observe(canvas.value)
  if (document.fonts?.ready) document.fonts.ready.then(() => sync())
  reduced = !!media.matches; hidden = document.hidden; resize()
})
watch(active, sync)
onBeforeUnmount(() => {
  cancelAnimationFrame(frame); media?.removeEventListener('change', onMotion)
  document.removeEventListener('visibilitychange', onVisibility); ro?.disconnect()
})
</script>

<template>
  <div class="tk-scene" aria-hidden="true"><canvas ref="canvas" /></div>
</template>
