<script setup lang="ts">
import { useStepMotion } from './useStepMotion'
const props = defineProps<{ step: number }>()
const { reveal, stage } = useStepMotion(() => props.step, 3, 900)
const titles = ['What is measured: the visible decay product', 'Two-body kinematics put the τ on a cone', 'The pair constraint leaves two mirror solutions', 'The ML model predicts the direction directly']
const notes = [
  'Each τ decays to a visible charged particle (plus photons for a ρ) and one or two neutrinos that escape. Only the visible leg\'s momentum is measured.',
  'With E_τ = E_beam and the τ mass fixed, the angle between the visible leg and the τ direction is determined by the visible energy, so the τ lies on a cone around the leg.',
  'Requiring the two τ to be back to back intersects the two cones in two points. The analytical solver must pick one branch: the default choice is right 59.3 % of the time inclusive (50 % in ee, eμ, ππ), the best possible choice 91.2 %.',
  'The neutrino model predicts, for each leg, the small angles (δθ, δφ) between the τ and the saved leading track in the detector frame, from the full particle list and 74 event-level quantities. It picks the correct branch 74.0 % of the time and has a median direction error of 0.89–1.17° per leg type.',
]
</script>

<template>
  <section class="ta" :data-step="step">
    <svg viewBox="0 0 560 300" role="img" aria-label="Sketch of the two-fold ambiguity of the tau direction from one visible decay product, and the machine-learning prediction near the true direction.">
      <circle cx="280" cy="160" r="3" fill="#f0f1f3" />
      <text x="280" y="292" text-anchor="middle" class="sm">interaction point · one of the two τ legs shown in detail</text>
      <!-- visible leg -->
      <line x1="280" y1="160" x2="470" y2="100" stroke="#77c9ff" stroke-width="3" />
      <text x="478" y="96" class="lab" fill="#77c9ff">visible leg (track)</text>
      <!-- cone -->
      <g :opacity="reveal(1)">
        <line x1="280" y1="160" x2="470" y2="36" stroke="#f0c36e" stroke-opacity=".8" stroke-dasharray="5 4" />
        <line x1="280" y1="160" x2="480" y2="166" stroke="#f0c36e" stroke-opacity=".8" stroke-dasharray="5 4" />
        <ellipse cx="474" cy="101" rx="14" ry="66" fill="none" stroke="#f0c36e" stroke-opacity=".8" transform="rotate(-8 474 101)" />
        <text x="372" y="190" class="sm" fill="#f0c36e">cone: opening angle fixed by E_visible, E_beam, m_τ</text>
      </g>
      <!-- two solutions -->
      <g :opacity="reveal(2)">
        <line x1="280" y1="160" x2="466" y2="50" stroke="#f69cab" stroke-width="2.2" />
        <line x1="280" y1="160" x2="478" y2="150" stroke="#f69cab" stroke-width="2.2" />
        <circle cx="466" cy="50" r="5" fill="#f69cab" /><circle cx="478" cy="150" r="5" fill="#f69cab" />
        <text x="420" y="34" class="lab" fill="#f69cab">solution A</text>
        <text x="486" y="166" class="lab" fill="#f69cab">solution B</text>
        <!-- other leg back to back, faint -->
        <line x1="280" y1="160" x2="94" y2="270" stroke="#f69cab" stroke-opacity=".35" stroke-width="1.5" />
        <line x1="280" y1="160" x2="82" y2="170" stroke="#f69cab" stroke-opacity=".35" stroke-width="1.5" />
        <text x="60" y="150" class="sm">τ⁺ and τ⁻ back to back</text>
      </g>
      <!-- truth and ML -->
      <g :opacity="reveal(3)">
        <line x1="280" y1="160" x2="470" y2="56" stroke="#70dcb2" stroke-width="2" stroke-dasharray="2 3" />
        <circle cx="470" cy="56" r="4" fill="#70dcb2" />
        <text x="480" y="60" class="lab" fill="#70dcb2">true τ</text>
        <circle cx="462" cy="62" r="6" fill="none" stroke="#baa5ff" stroke-width="2" />
        <circle cx="462" cy="62" r="2" fill="#baa5ff" />
        <text x="372" y="78" text-anchor="end" class="lab" fill="#baa5ff">ML prediction (δθ, δφ)</text>
        <text x="372" y="92" text-anchor="end" class="sm">median error 0.89–1.17° · correct branch 74 %</text>
      </g>
    </svg>
    <div class="ta-text"><h3>{{ titles[stage] }}</h3><p>{{ notes[stage] }}</p><small>Schematic geometry; the percentages are the v5 evaluation on 200,755 held-out simulated Z → ττ events.</small></div>
  </section>
</template>

<style scoped>
.ta { display: grid; grid-template-columns: 1.15fr 1fr; gap: 18px; align-items: center; margin-top: 4px; }
.ta svg { width: 100%; height: 270px; display: block; overflow: visible; }
.sm { font-size: 10.5px; fill: #bcc2cb; }
.lab { font-size: 12px; fill: #f0f1f3; }
.ta-text h3 { margin: 0 0 8px; font-size: 17px; color: var(--nju-amber); font-weight: 550; line-height: 1.25; }
.ta-text p { margin: 0; font-size: 13.5px; line-height: 1.45; color: var(--fg-0); }
.ta-text small { display: block; margin-top: 10px; font-size: 11px; color: var(--fg-1); }
</style>
