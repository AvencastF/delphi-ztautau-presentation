<script setup lang="ts">
import { useStepMotion } from './useStepMotion'
const props = defineProps<{ step: number }>()
const { reveal, stage } = useStepMotion(() => props.step, 3, 900)
const titles = ['Charged tracks of one event', 'Thrust axis of the charged tracks', 'Two geometric hemispheres, H0 and H1', 'One-prong topology: a leading track per hemisphere, neutrals counted per side']
const notes = [
  'The event is viewed in the plane transverse to the beam. Only accepted charged tracks enter the thrust computation.',
  'The thrust axis maximises the summed projected momentum. Its orientation is fixed by making its largest absolute component positive, so H0 and H1 are a geometric labelling, not τ⁺ / τ⁻.',
  'H0 collects tracks with p·axis < 0, H1 those with p·axis ≥ 0. Both must contain at least one charged track (cut 1). The angle between any H0 track and any H1 track must exceed 160° (cut 4).',
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
        <text x="168" y="44" class="lab" fill="#f69cab">H0 · p·axis &lt; 0</text>
        <text x="318" y="44" class="lab" fill="#70dcb2">H1 · p·axis ≥ 0</text>
        <path d="M250 150 A30 30 0 0 1 310 150" fill="none" stroke="#bcc2cb" stroke-opacity=".6" />
        <text x="280" y="112" text-anchor="middle" class="sm">opening angle &gt; 160°</text>
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
        <text x="380" y="252" class="sm" fill="#baa5ff">2 neutral objects in H1 (≤ 3 allowed) · 0 in H0</text>
      </g>
    </svg>
    <div class="hs-text"><h3>{{ titles[stage] }}</h3><p>{{ notes[stage] }}</p><small>Schematic, not a reconstructed event. Charged tracks blue, neutral objects violet.</small></div>
  </section>
</template>

<style scoped>
.hs { display: grid; grid-template-columns: 1.15fr 1fr; gap: 18px; align-items: center; margin-top: 4px; }
.hs svg { width: 100%; height: 300px; display: block; overflow: visible; }
.sm { font-size: 10.5px; fill: #bcc2cb; }
.lab { font-size: 12px; fill: #f0f1f3; }
.hs-text h3 { margin: 0 0 8px; font-size: 17px; color: var(--nju-amber); font-weight: 550; line-height: 1.25; }
.hs-text p { margin: 0; font-size: 13.5px; line-height: 1.45; color: var(--fg-0); }
.hs-text small { display: block; margin-top: 10px; font-size: 11px; color: var(--fg-1); }
</style>
