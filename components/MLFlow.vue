<script setup lang="ts">
import { useStepMotion } from './useStepMotion'
const props = defineProps<{ step: number }>()
const { motion, running, reveal, stage } = useStepMotion(() => props.step, 3, 900)
const titles = ['Particle tokens: up to 24 reconstructed particles per event', 'The pretrained EveNet body (unchanged) turns tokens into event features', 'Head 1: the 12-class decay-mode classifier', 'Head 2: the neutrino-direction diffusion head, conditioned on 74 event-level quantities through FiLM']
const notes = [
  'Each particle is one token with seven slots: energy, transverse momentum, pseudorapidity, azimuth, two "tag" slots that carry the embedded detector information (electron / muon / hadron identification, dE/dx, calorimeter and lifetime quantities), and the charge. Twelve slots per thrust hemisphere; the leading track is always kept.',
  'The token layout and the transformer body (PET) are those of the pretrained EveNet model, so both heads start from its checkpoint. The owner measured about 10 % better classification with this pretraining than from scratch, which is why the token is not widened.',
  'The classifier outputs probabilities for ten τ-pair decay channels (ee, eμ, eπ, eρ, μμ, μπ, μρ, ππ, πρ, ρρ), an "other τ decays" class and a lepton-pair background class. It is trained on the first conversion with unit event weights.',
  'The neutrino head is a diffusion model that generates, for each leg, the two angles between the τ and the saved leading track. Event-level quantities (lead-track lifetime, branch discriminant, per-leg cone photon counts and masses, …) modulate the head layer-wise through FiLM (feature-wise linear modulation). One sample with 50 diffusion steps is drawn at inference.',
]
</script>

<template>
  <section class="mf" :data-step="step">
    <svg viewBox="0 0 580 250" preserveAspectRatio="xMidYMid meet" role="img" aria-label="Flow from particle tokens and event globals through the shared body to the classifier head and the FiLM-conditioned neutrino head.">
      <!-- tokens -->
      <g>
        <rect v-for="i in 8" :key="i" :x="18" :y="22 + (i - 1) * 22" width="118" height="16" rx="3" fill="#23262b" stroke="#77c9ff" stroke-opacity=".6" />
        <g v-for="i in 8" :key="'t' + i" :transform="`translate(18 ${22 + (i - 1) * 22})`">
          <rect v-for="k in 7" :key="k" :x="2 + (k - 1) * 16.6" y="3" width="14" height="10" :fill="k <= 4 ? '#77c9ff' : k <= 6 ? '#baa5ff' : '#f0c36e'" :fill-opacity="k <= 4 ? .55 : .7" />
        </g>
        <text x="77" y="212" text-anchor="middle" class="sm">[E, p_T, η, φ, tag0, tag1, q] × up to 24</text>
        <text x="77" y="226" text-anchor="middle" class="sm" fill="#baa5ff">tag slots = detector embedding</text>
      </g>
      <!-- body -->
      <g :opacity="reveal(1)">
        <path d="M136 110 H170" stroke="#bcc2cb" stroke-width="1.4" />
        <path d="M136 110 H170" stroke="#fff0ba" stroke-width="2.4" pathLength="100" stroke-dasharray="25 75" :stroke-dashoffset="-motion.cycle * 100" :opacity="running ? .9 : 0" />
        <rect x="172" y="40" width="120" height="140" rx="6" fill="#23262b" stroke="#f0c36e" stroke-opacity=".8" />
        <text x="232" y="98" text-anchor="middle" class="lab">pretrained</text>
        <text x="232" y="116" text-anchor="middle" class="lab">EveNet body</text>
        <text x="232" y="134" text-anchor="middle" class="sm">PET transformer · unchanged</text>
      </g>
      <!-- classifier head -->
      <g :opacity="reveal(2)">
        <path d="M292 80 C330 80 340 62 376 62" fill="none" stroke="#bcc2cb" stroke-width="1.4" />
        <rect x="378" y="32" width="178" height="62" rx="6" fill="#23262b" stroke="#70dcb2" stroke-opacity=".8" />
        <text x="467" y="54" text-anchor="middle" class="lab" fill="#70dcb2">classifier head</text>
        <text x="467" y="70" text-anchor="middle" class="sm">12 classes: 10 τ channels + other τ + lepton pairs</text>
        <text x="467" y="84" text-anchor="middle" class="sm">output: class scores, predicted class</text>
      </g>
      <!-- neutrino head + FiLM -->
      <g :opacity="reveal(3)">
        <path d="M292 140 C330 140 340 160 376 160" fill="none" stroke="#bcc2cb" stroke-width="1.4" />
        <rect x="378" y="128" width="178" height="62" rx="6" fill="#23262b" stroke="#f69cab" stroke-opacity=".8" />
        <text x="467" y="150" text-anchor="middle" class="lab" fill="#f69cab">neutrino-direction head</text>
        <text x="467" y="166" text-anchor="middle" class="sm">diffusion · (δθ, δφ) for τ⁺ and τ⁻</text>
        <text x="467" y="180" text-anchor="middle" class="sm">1 sample × 50 steps at inference</text>
        <rect x="378" y="206" width="178" height="30" rx="4" fill="#23262b" stroke="#baa5ff" stroke-opacity=".8" />
        <text x="467" y="225" text-anchor="middle" class="sm" fill="#baa5ff">74 event-level quantities → FiLM</text>
        <path d="M467 206 V190" stroke="#baa5ff" stroke-width="1.6" />
        <path d="M462 196 L467 190 L472 196" fill="none" stroke="#baa5ff" stroke-width="1.6" />
      </g>
    </svg>
    <div class="mf-text"><h3>{{ titles[stage] }}</h3><p>{{ notes[stage] }}</p><small>Schematic of the two models in the EveNet-Align Ztautau code; token layout from the converter configuration.</small></div>
  </section>
</template>

<style scoped>
.mf { display: grid; grid-template-columns: 1.25fr 1fr; gap: 18px; align-items: center; margin-top: 4px; }
.mf svg { width: 100%; height: 222px; display: block; overflow: visible; }
.sm { font-size: 10px; fill: #bcc2cb; }
.lab { font-size: 12px; fill: #f0f1f3; }
.mf-text h3 { margin: 0 0 8px; font-size: 16px; color: var(--nju-amber); font-weight: 550; line-height: 1.25; }
.mf-text p { margin: 0; font-size: 12.8px; line-height: 1.42; color: var(--fg-0); }
.mf-text small { display: block; margin-top: 10px; font-size: 11px; color: var(--fg-1); }
</style>
