<script setup lang="ts">
import { computed } from 'vue'
import { useStepMotion } from './useStepMotion'
const props = defineProps<{ step: number }>()
// Cumulative counts of the frozen 2026-10-12 selection run (cutflows/cutflow.csv, "Total MC (Z_ee excluded)" row).
const rows = [
  ['all converted events', 828850, 2698666.249335, 'input'],
  ['both hemispheres have a charged track', 334830, 1732900.217561, 'hemispheres'],
  ['leading tracks inside |cos θ| < 0.94', 322437, 1673443.487097, 'acceptance'],
  ['at most 6 charged tracks', 266778, 340365.020668, 'multiplicity'],
  ['hemispheres more than 160° apart', 199915, 194466.083756, 'isolation'],
  ['leading-track |z0| < 45 mm', 193935, 190401.269830, 'z_origin'],
  ['leading-track |d0| < 15 mm', 188524, 185417.412265, 'd_origin'],
  ['one leading track within |d0| < 3 mm', 187655, 185042.790106, 'one_close'],
  ['|Δz0| of the two leading tracks < 30 mm', 187008, 184589.375092, 'relative_z'],
  ['visible energy > 8 GeV', 184876, 182368.007559, 'energy'],
  ['visible transverse momentum > 0.4 GeV', 173851, 169339.151477, 'transverse'],
  ['at least one barrel single-prong hemisphere', 123843, 120069.367913, 'nn_one_prong'],
  ['acollinearity > 0.5° (1-1 topology)', 61620, 59078.423330, 'nn_acol'],
  ['HPC boundary evidence present when required', 60141, 57740.096872, 'nn_boundary_no_pe'],
  ['PEmax veto not explicitly failed', 48707, 46785.405998, 'nn_pe_keep_unknown'],
  ['exactly one charged track per hemisphere', 33739, 32862.683621, 'nn_is_1p1p'],
  ['radiative electromagnetic energy < E_beam', 32531, 31795.685713, 'exclusive_erad'],
  ['radiative track momentum < p_beam', 26631, 25780.069403, 'exclusive_prad'],
  ['at most 3 neutral objects per hemisphere', 23073, 23198.931168, 'neutral_hemisphere_limit'],
] as const
const { motion, stage } = useStepMotion(() => props.step, rows.length - 1, 700)
const lmin = Math.log10(10000), lmax = Math.log10(3e6)
const bar = (n: number) => Math.max(0.02, (Math.log10(Math.max(n, 10000)) - lmin) / (lmax - lmin))
const interp = (col: 1 | 2) => {
  const s = Math.max(0, Math.min(rows.length - 1, motion.stage)); const i = Math.floor(s), t = s - i
  const a = rows[i][col] as number, b = rows[Math.min(i + 1, rows.length - 1)][col] as number
  return Math.exp(Math.log(a) + (Math.log(b) - Math.log(a)) * t)
}
const data = computed(() => interp(1)), mc = computed(() => interp(2))
const fmt = (n: number) => Math.round(n).toLocaleString('en-US')
const current = computed(() => rows[stage.value])
</script>

<template>
  <section class="cf" :data-step="step">
    <div class="cf-bars">
      <div class="cf-bar"><span class="cf-label">1994 data</span><div class="cf-track"><div class="cf-fill data" :style="{ width: `${bar(data) * 100}%` }" /></div><span class="cf-num">{{ fmt(data) }}</span></div>
      <div class="cf-bar"><span class="cf-label">signed MC total</span><div class="cf-track"><div class="cf-fill mc" :style="{ width: `${bar(mc) * 100}%` }" /></div><span class="cf-num">{{ mc.toLocaleString('en-US', { maximumFractionDigits: 0 }) }}</span></div>
      <div class="cf-axis"><span>10⁴</span><span>10⁵</span><span>10⁶</span><span>logarithmic scale</span></div>
    </div>
    <div class="cf-now"><b>{{ stage === 0 ? 'Before any cut' : `After cut ${stage} of 18` }}</b> · {{ current[0] }} <i>({{ current[3] }})</i> · data / MC = {{ (current[1] / current[2]).toFixed(4) }}</div>
    <ol class="cf-list">
      <li v-for="(r, i) in rows.slice(1)" :key="i" :class="{ done: i + 1 <= stage, now: i + 1 === stage }"><span>{{ r[0] }}</span><em>{{ fmt(r[1]) }}</em></li>
    </ol>
  </section>
</template>

<style scoped>
.cf { margin-top: 4px; display: grid; grid-template-columns: 1fr 1.05fr; gap: 18px; align-items: start; }
.cf-bars { grid-column: 1; }
.cf-bar { display: grid; grid-template-columns: 96px 1fr 84px; gap: 8px; align-items: center; margin: 8px 0; font-size: 12px; }
.cf-label { color: var(--fg-1); }
.cf-track { height: 18px; background: rgba(201,210,221,.08); border: 1px solid var(--nju-line); position: relative; }
.cf-fill { height: 100%; }
.cf-fill.data { background: #f0f1f3; }
.cf-fill.mc { background: #77c9ff; }
.cf-num { text-align: right; font-variant-numeric: tabular-nums; color: var(--fg-0); font-weight: 550; }
.cf-axis { display: grid; grid-template-columns: 96px 1fr 1fr 1fr; font-size: 10px; color: var(--fg-1); margin-top: -2px; }
.cf-axis span:first-child { grid-column: 2; }
.cf-axis span:last-child { text-align: right; }
.cf-now { grid-column: 1; margin-top: 10px; border-left: 2px solid var(--nju-amber); padding-left: 10px; font-size: 12.5px; line-height: 1.4; color: var(--fg-0); }
.cf-now b { color: var(--nju-amber); font-weight: 550; }
.cf-now i { color: var(--fg-1); font-size: .9em; }
.cf-list { grid-column: 2; grid-row: 1 / span 2; margin: 0; padding-left: 20px; font-size: 10.6px; line-height: 1.32; color: var(--fg-1); columns: 1; }
.cf-list li { display: flex; justify-content: space-between; gap: 8px; opacity: .45; padding: 1px 0; border-bottom: 1px solid rgba(190,201,214,.08); }
.cf-list li.done { opacity: 1; color: var(--fg-0); }
.cf-list li.now { color: var(--nju-amber); }
.cf-list em { font-style: normal; font-variant-numeric: tabular-nums; }
</style>
