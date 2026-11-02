<script setup>
// Expected precision on the 15 spin coefficients, drawn as the 4x4 spin-density-matrix block
// (1, B+_j / B-_i, C_ij), in the style of the EveNet seminar's DelphiSpinMatrices. Values are the
// expected (Asimov) result of the full-covariance template fit on the combined 1992–1995 simulation:
// central values equal the simulation's own spin state; the uncertainties are statistical only.
import { computed, nextTick, onBeforeUnmount, onMounted, ref, watch } from 'vue'
import { useSlideContext } from '@slidev/client'

const axes = ['n', 'r', 'k']
// diagonal correlations: central value (simulation) and sigma; others: sigma only (central value = simulation)
const B = { minus: { n: 0.031, r: 0.036, k: 0.032 }, plus: { n: 0.031, r: 0.036, k: 0.032 } }
const C = {
  nn: { v: '+0.80', s: 0.11 }, nr: { s: 0.17 }, nk: { s: 0.15 },
  rn: { s: 0.17 }, rr: { v: '-0.81', s: 0.13 }, rk: { s: 0.17 },
  kn: { s: 0.15 }, kr: { s: 0.17 }, kk: { v: '+1.03', s: 0.14 },
}
const paper = [247, 245, 242], warm = [214, 112, 90], cool = [78, 138, 186]
const mix = (a, b, t) => a.map((c, i) => Math.round(c + (b[i] - c) * t))
function fill(entry) {
  if (entry.identity) return 'rgb(230,226,220)'
  if (entry.value == null) return `rgb(${paper.join(',')})`
  const t = Math.max(-1, Math.min(1, entry.value / 1.03))
  return `rgb(${(t >= 0 ? mix(paper, warm, t) : mix(paper, cool, -t)).join(',')})`
}
const rows = computed(() => {
  const head = [{ identity: true, text: '1' }, ...axes.map(j => ({ kind: 'B', text: `B^{+}_{${j}}`, unc: B.plus[j] }))]
  const body = axes.map(i => [
    { kind: 'B', text: `B^{-}_{${i}}`, unc: B.minus[i] },
    ...axes.map((j) => { const c = C[i + j]; return { kind: 'C', text: c.v ?? `C_{${i}${j}}`, value: c.v ? Number(c.v) : null, unc: c.s } }),
  ])
  return [head, ...body]
})
const { $nav, $page, $renderContext } = useSlideContext()
const active = computed(() => $nav.value.currentPage === $page.value && $renderContext.value === 'slide')
const reduced = ref(false), play = ref(false), hover = ref(null)
let media
const preference = () => { reduced.value = !!media?.matches }
async function sync() {
  play.value = false
  if (active.value && !reduced.value) { await nextTick(); requestAnimationFrame(() => { play.value = true }) }
}
onMounted(() => { media = window.matchMedia('(prefers-reduced-motion: reduce)'); media.addEventListener('change', preference); preference(); sync() })
watch(active, sync); watch(reduced, sync)
onBeforeUnmount(() => media?.removeEventListener('change', preference))
const label = ['', 'n', 'r', 'k']
</script>

<template>
  <div class="sm-matrix" :class="{ 'sm-play': play, dim: hover !== null }" role="table" aria-label="Expected precision of the tau-pair spin density matrix, 1992–1995 combined, simulation" @mouseleave="hover = null">
    <div class="sm-row" role="row">
      <span class="sm-corner" />
      <span v-for="(ax, j) in label" :key="'h' + j" class="sm-axis" :class="{ on: hover?.endsWith('-' + j) }" role="columnheader"><LaTeX v-if="ax" :formula="`\\tau^+:\\ ${ax}`" /></span>
    </div>
    <div v-for="(row, i) in rows" :key="'r' + i" class="sm-row" role="row">
      <span class="sm-axis" :class="{ on: hover?.startsWith(i + '-') }" role="rowheader"><LaTeX v-if="label[i]" :formula="`\\tau^-:\\ ${label[i]}`" /></span>
      <div v-for="(e, j) in row" :key="`${i}-${j}`" class="sm-cell" :class="{ identity: e.identity, focus: hover === `${i}-${j}` }" :style="{ background: fill(e), '--d': i * 4 + j }" role="cell" @mouseenter="hover = `${i}-${j}`">
        <span v-if="e.kind" class="sm-tag">{{ e.kind === 'B' ? 'polarisation' : 'correlation' }}</span>
        <span class="sm-val"><LaTeX :formula="e.text" /></span>
        <span v-if="e.unc" class="sm-unc"><LaTeX :formula="`\\pm ${e.unc.toFixed(e.kind === 'B' ? 3 : 2)}`" /></span>
      </div>
    </div>
  </div>
</template>
