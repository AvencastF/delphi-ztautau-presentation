<script setup lang="ts">
import { useStepMotion } from './useStepMotion'
import { mixed } from './tex'
const props = defineProps<{ step: number }>()
const { reveal, stage } = useStepMotion(() => props.step, 3, 900)
const titles = ['Charged tracks of one event', 'Thrust axis of the charged tracks', 'Two geometric hemispheres, H0 and H1', 'One-prong topology: a leading track per hemisphere, neutrals counted per side']
const notes = [
  'The event is viewed in the plane transverse to the beam. Only accepted charged tracks enter the thrust computation.',
  'The thrust axis maximises the summed projected momentum. Its orientation is fixed by making its largest absolute component positive, so H0 and H1 are a geometric labelling, not $\\tau^+$ / $\\tau^-$.',
  'H0 collects tracks with $\\vec p\\cdot\\hat a\\lt 0$, H1 those with $\\vec p\\cdot\\hat a\\ge 0$. Both must contain at least one charged track (cut 1). The angle between any H0 track and any H1 track must exceed $160^\\circ$ (cut 4).',
  'The leading track is the highest-momentum charged track of its hemisphere; the "1-1" cuts require exactly one charged track per side. Neutral objects (photons, here on the right) are counted per hemisphere: at most 3 on each side (cut 18).',
]
</script>

<template>
  <section class="hs" :data-step="step">
    <svg viewBox="0 0 560 300" role="img" aria-label="Sketch of a tau-pair event: charged tracks, thrust axis, two hemispheres, leading tracks and neutral objects.">
      <circle cx="280" cy="150" r="128" fill="none" stroke="#bcc2cb" stroke-opacity=".25" />
      <circle cx="280" cy="150" r="3" fill="#f0f1f3" />
      <text x="280" y="292" text-anchor="middle" class="sm">interaction point · view along the beam</text>
      <!-- tracks: left one-prong, right one-prong + photons -->
      <path d="M280 150 Q230 128 170 108" fill="none" stroke="#77c9ff" stroke-width="3" />
      <path d="M280 150 Q333 168 392 196" fill="none" stroke="#77c9ff" stroke-width="3" />
      <!-- thrust axis -->
      <g :opacity="reveal(1)">
        <line x1="128" y1="100" x2="432" y2="200" stroke="#f0c36e" stroke-dasharray="6 5" stroke-width="1.6" />
        <path d="M420 190 L432 200 L418 203" fill="none" stroke="#f0c36e" stroke-width="1.6" />
        <text x="438" y="214" class="sm" fill="#f0c36e">thrust axis</text>
      </g>
      <!-- hemisphere plane -->
      <g :opacity="reveal(2)">
        <line x1="238" y1="22" x2="322" y2="278" stroke="#bcc2cb" stroke-opacity=".7" stroke-width="1.4" />
        <path d="M238 22 L322 278 L152 278 L152 22 Z" fill="#f69cab" fill-opacity=".07" />
        <path d="M238 22 L322 278 L408 278 L408 22 Z" fill="#70dcb2" fill-opacity=".07" />
        <foreignObject x="160" y="32" width="150" height="18"><div xmlns="http://www.w3.org/1999/xhtml" class="fo lab" style="text-align:left;color:#f69cab" v-html="mixed('H0 · $\\vec p\\cdot\\hat a\\lt 0$')" /></foreignObject>
        <foreignObject x="312" y="32" width="150" height="18"><div xmlns="http://www.w3.org/1999/xhtml" class="fo lab" style="text-align:left;color:#70dcb2" v-html="mixed('H1 · $\\vec p\\cdot\\hat a\\ge 0$')" /></foreignObject>
        <path d="M250 150 A30 30 0 0 1 310 150" fill="none" stroke="#bcc2cb" stroke-opacity=".6" />
        <foreignObject x="200" y="100" width="160" height="18"><div xmlns="http://www.w3.org/1999/xhtml" class="fo sm" style="text-align:center;" v-html="mixed('opening angle $\\gt 160^\\circ$')" /></foreignObject>
      </g>
      <!-- leading tracks + neutrals -->
      <g :opacity="reveal(3)">
        <circle cx="170" cy="108" r="7" fill="none" stroke="#f0f1f3" stroke-width="1.6" />
        <text x="160" y="92" text-anchor="end" class="lab">leading track H0</text>
        <circle cx="392" cy="196" r="7" fill="none" stroke="#f0f1f3" stroke-width="1.6" />
        <text x="404" y="188" class="lab">leading track H1</text>
        <g stroke="#baa5ff" stroke-width="1.4" fill="none">
          <path d="M280 150 L372 232" stroke-dasharray="3 4" /><path d="M280 150 L400 170" stroke-dasharray="3 4" />
        </g>
        <circle cx="372" cy="232" r="4" fill="#baa5ff" /><circle cx="400" cy="170" r="4" fill="#baa5ff" />
        <foreignObject x="330" y="240" width="230" height="18"><div xmlns="http://www.w3.org/1999/xhtml" class="fo sm" style="text-align:left;color:#baa5ff" v-html="mixed('2 neutrals in H1 ($\\le 3$ allowed) · 0 in H0')" /></foreignObject>
      </g>
    </svg>
    <div class="hs-text"><h3>{{ titles[stage] }}</h3><p v-html="mixed(notes[stage])" /><small>Schematic, not a reconstructed event. Charged tracks blue, neutral objects violet.</small></div>
  </section>
</template>

<style scoped>
.hs { display: grid; grid-template-columns: 1.15fr 1fr; gap: 18px; align-items: center; margin-top: 4px; }
.hs svg { width: 100%; height: 300px; display: block; overflow: visible; }
.sm { font-size: 10.5px; fill: #bcc2cb; }
.lab { font-size: 12px; fill: #f0f1f3; }
.hs-text h3 { margin: 0 0 8px; font-size: 17px; color: var(--nju-amber); font-weight: 550; line-height: 1.25; }
.hs-text p { margin: 0; font-size: 13.5px; line-height: 1.45; color: var(--fg-0); }
.fo { line-height: 18px; white-space: nowrap; color: #bcc2cb; }
.fo.lab { font-size: 12px; color: #f0f1f3; }
.fo.sm { font-size: 10.5px; }
.hs-text small { display: block; margin-top: 10px; font-size: 11px; color: var(--fg-1); }
</style>
