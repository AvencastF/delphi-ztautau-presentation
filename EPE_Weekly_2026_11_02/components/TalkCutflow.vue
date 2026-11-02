<script setup lang="ts">
import { computed } from 'vue'
import { useStepMotion } from 'slidev-addon-ztautau/composable/useStepMotion'
import { mixed, tex } from 'slidev-addon-ztautau/composable/tex'
import flow from '../../Internal_Note/components/cutflow-by-process.json'

const props = defineProps<{ step: number }>()
const labels = [
  'all converted events',
  'both hemispheres have a charged track',
  'leading tracks inside $|\\cos\\theta|\\lt 0.94$',
  'at most 6 charged tracks',
  'hemispheres more than $160^\\circ$ apart',
  'leading-track $|z_0|\\lt 45\\,\\mathrm{mm}$',
  'leading-track $|d_0|\\lt 15\\,\\mathrm{mm}$',
  'one leading track within $|d_0|\\lt 3\\,\\mathrm{mm}$',
  '$|\\Delta z_0|\\lt 30\\,\\mathrm{mm}$ between leading tracks',
  'visible energy $E_\\mathrm{vis}\\gt 8\\,\\mathrm{GeV}$',
  'visible $p_T\\gt 0.4\\,\\mathrm{GeV}$',
  'at least one barrel single-prong hemisphere',
  'acollinearity $\\gt 0.5^\\circ$ (1-1 topology)',
  'HPC boundary evidence present when required',
  'PEmax veto not explicitly failed',
  'exactly one charged track per hemisphere',
  'radiative EM energy $E_\\mathrm{rad}\\lt E_\\mathrm{beam}$',
  'radiative momentum $p_\\mathrm{rad}\\lt p_\\mathrm{beam}$',
  'at most 3 neutral objects per hemisphere',
]
const PROC: Record<string, { color: string, label: string }> = {
  Z_tautau: { color: '#0072B2', label: 'Z\\to\\tau^+\\tau^-' },
  Z_mumu: { color: '#ffbb78', label: 'Z\\to\\mu^+\\mu^-' },
  Z_qq: { color: '#aec7e8', label: 'Z\\to q\\bar q' },
  Bhabha: { color: '#ff9896', label: '\\text{Bhabha}' },
  yy_ll: { color: '#c5b0d5', label: '\\gamma\\gamma\\to\\ell^+\\ell^-' },
  yy_qq: { color: '#c49c94', label: '\\gamma\\gamma\\to q\\bar q' },
}
const years = ['1992', '1993', '1994', '1995'] as const
type Row = Record<string, number | string>
const rows = flow.rows as Row[]
const byYear = flow.years as Record<string, Row[]>
const procs = flow.processes as string[]
const { motion, stage } = useStepMotion(() => props.step, rows.length - 1, 700)
const lmin = Math.log10(10000), lmax = Math.log10(3e6)
const bar = (n: number) => Math.max(0.02, (Math.log10(Math.max(n, 10000)) - lmin) / (lmax - lmin))
const pos = computed(() => { const s = Math.max(0, Math.min(rows.length - 1, motion.stage)); const i = Math.floor(s); return { i, j: Math.min(i + 1, rows.length - 1), t: s - i } })
const val = (key: string, logInterp: boolean) => {
  const { i, j, t } = pos.value
  const a = Math.max(0, rows[i][key] as number), b = Math.max(0, rows[j][key] as number)
  if (logInterp && a > 0 && b > 0) return Math.exp(Math.log(a) + (Math.log(b) - Math.log(a)) * t)
  return a + (b - a) * t
}
const data = computed(() => val('data', true))
const total = computed(() => val('total', true))
const parts = computed(() => {
  const v = procs.map(p => ({ p, n: val(p, false) }))
  const sum = v.reduce((s, x) => s + x.n, 0) || 1
  const L = bar(total.value) * 100
  return v.map(x => ({ ...x, w: x.n > 0 ? Math.max(0.35, L * x.n / sum) : 0 }))
})
const fmt = (n: number) => Math.round(n).toLocaleString('en-US')
const ratioOf = (row: Row) => {
  const d = row.data as number, t = row.total as number
  return t > 0 ? (d / t).toFixed(3) : '—'
}
const current = computed(() => rows[stage.value])
const ratio = computed(() => ratioOf(current.value))
const yearRatio = (y: string) => ratioOf(byYear[y][stage.value])
const zee = computed(() => fmt(current.value.Z_ee as number))
</script>

<template>
  <section class="cf" :data-step="step">
    <div class="cf-bars">
      <div class="cf-bar"><span class="cf-label">data</span><div class="cf-track"><div class="cf-fill data" :style="{ width: `${bar(data) * 100}%` }" /></div><span class="cf-num">{{ fmt(data) }}</span></div>
      <div class="cf-bar"><span class="cf-label">simulation</span><div class="cf-track stack"><div v-for="s in parts" :key="s.p" class="cf-seg" :style="{ width: `${s.w}%`, background: PROC[s.p].color }" :title="`${s.p}: ${fmt(s.n)}`" /></div><span class="cf-num">{{ fmt(total) }}</span></div>
      <div class="cf-axis"><span v-html="tex('10^4')" /><span v-html="tex('10^5')" /><span v-html="tex('10^6')" /><span>log scale</span></div>
      <ul class="cf-legend">
        <li v-for="s in parts" :key="s.p"><i :style="{ background: PROC[s.p].color }" /><span v-html="tex(PROC[s.p].label)" /><em>{{ fmt(s.n) }}</em></li>
      </ul>
      <div class="cf-note">Bar length: log of the signed total. Segments: each process's share of it. <span v-html="tex('Z\\to e^+e^-')" /> not stacked (overlaps Bhabha): {{ zee }} here.</div>
      <div class="cf-now">
        <div class="cf-cut"><b>{{ stage === 0 ? 'Before any cut' : `After cut ${stage} of 18` }}</b><span v-html="mixed(labels[stage])" /></div>
        <div class="cf-ratios">
          <div class="cf-ratios-h">data / MC</div>
          <div v-for="y in years" :key="y"><b>{{ y }}</b><em>{{ yearRatio(y) }}</em></div>
          <div><b>all</b><em>{{ ratio }}</em></div>
        </div>
      </div>
    </div>
    <div class="cf-side">
      <div class="cf-list-head"><span>data</span></div>
      <ol class="cf-list">
        <li v-for="(r, i) in rows.slice(1)" :key="i" :class="{ done: i + 1 <= stage, now: i + 1 === stage }"><span v-html="mixed(labels[i + 1])" /><em>{{ fmt(r.data as number) }}</em></li>
      </ol>
    </div>
  </section>
</template>

<style scoped>
.cf { margin-top: 2px; display: grid; grid-template-columns: 1.15fr 1fr; gap: 22px; align-items: start; }
.cf-bar { display: grid; grid-template-columns: 78px minmax(0, 1fr) 96px; gap: 12px; align-items: center; margin: 6px 0; font-size: 12px; }
.cf-label { color: var(--fg-1); }
.cf-track { height: 16px; background: rgba(201,210,221,.08); border: 1px solid var(--nju-line); display: flex; min-width: 0; overflow: hidden; }
.cf-fill { height: 100%; }
.cf-fill.data { background: #f0f1f3; }
.cf-seg { height: 100%; flex: none; }
.cf-seg + .cf-seg { box-shadow: inset 1px 0 0 rgba(23,25,28,.6); }
.cf-num { text-align: right; font-variant-numeric: tabular-nums; color: var(--fg-0); font-weight: 550; white-space: nowrap; }
.cf-axis { display: grid; grid-template-columns: 78px 1fr 1fr 1fr 96px; gap: 12px; font-size: 10px; color: var(--fg-1); margin-top: -2px; }
.cf-axis span:first-child { grid-column: 2; }
.cf-axis span:nth-child(4) { grid-column: 4; text-align: right; }
.cf-legend { list-style: none; margin: 8px 0 0; padding: 0; display: grid; grid-template-columns: 1fr 1fr; gap: 3px 14px; font-size: 11.5px; }
.cf-legend li { display: flex; align-items: center; gap: 6px; white-space: nowrap; }
.cf-legend i { width: 10px; height: 10px; flex: none; border-radius: 2px; }
.cf-legend em { margin-left: auto; font-style: normal; font-variant-numeric: tabular-nums; color: var(--fg-1); }
.cf-note { margin-top: 6px; font-size: 10.5px; color: var(--fg-1); line-height: 1.35; }
.cf-now { margin-top: 10px; border-left: 2px solid var(--nju-amber); padding: 2px 0 2px 10px; display: grid; gap: 3px; }
.cf-cut { display: flex; flex-wrap: wrap; gap: 4px 8px; align-items: baseline; font-size: 13px; line-height: 1.35; color: var(--fg-0); }
.cf-cut b { color: var(--nju-amber); font-weight: 550; }
.cf-ratios { display: grid; gap: 1px; margin-top: 2px; font-size: 13px; font-variant-numeric: tabular-nums; color: var(--fg-0); }
.cf-ratios-h { display: block; color: var(--nju-amber); font-weight: 550; font-size: 12px; letter-spacing: .01em; }
.cf-ratios > div:not(.cf-ratios-h) { display: grid; grid-template-columns: 46px 56px; align-items: baseline; }
.cf-ratios b { color: var(--nju-amber); font-weight: 550; }
.cf-ratios em { font-style: normal; text-align: right; }
.cf-side { min-width: 0; }
.cf-list-head { display: flex; justify-content: flex-end; padding-right: 2px; margin: 0 0 2px; font-size: 11px; font-weight: 600; color: var(--fg-0); }
.cf-list { margin: 0; padding-left: 18px; font-size: 11px; line-height: 1.38; color: var(--fg-1); }
.cf-list li { display: flex; justify-content: space-between; gap: 10px; opacity: .45; padding: 1px 0; border-bottom: 1px solid rgba(190,201,214,.08); }
.cf-list li.done { opacity: 1; color: var(--fg-0); }
.cf-list li.now { color: var(--nju-amber); }
.cf-list em { font-style: normal; font-variant-numeric: tabular-nums; white-space: nowrap; }
</style>
