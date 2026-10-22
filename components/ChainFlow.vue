<script setup lang="ts">
import { useStepMotion } from './useStepMotion'
const props = defineProps<{ step: number }>()
const { motion, running, stage, reveal } = useStepMotion(() => props.step, 5, 800)
const stages = [
  { title: '1 · Monte-Carlo production', what: 'Generate events, simulate the DELPHI detector (DELSIM), reconstruct (DELANA), write the long summary format (longDST) and convert it to EDM4hep ROOT files.', who: 'production scripts + simulation pipeline', id: 'campaign tags prod-20260923-v1, tau-extra-20260923-v1' },
  { title: '2 · Real-data conversion', what: 'Convert the archived 1994 leptonic longDST data with the same converter, keeping a unique event identity per event.', who: 'EDM4hep converter', id: '132 files, 828,850 events' },
  { title: '3 · Event selection', what: 'Apply the 18 ordered cuts, identify the decay of each τ, and write one Parquet table per physics process.', who: 'tau analysis framework', id: 'frozen run of 2026-10-12' },
  { title: '4 · Machine learning', what: 'Classify the τ-pair decay mode and predict the direction of each τ (the part the neutrinos take away).', who: 'EveNet-Align, two fine-tuned models', id: 'classifier v1 · neutrino model v5' },
  { title: '5 · Spin fit (future)', what: 'Extract all 15 spin-density-matrix coefficients from the reconstructed τ directions and decay products.', who: 'fit program, downstream', id: 'out of scope for this report' },
]
</script>

<template>
  <section class="chain" :data-step="step">
    <div class="chain-row">
      <template v-for="(s, i) in stages" :key="i">
        <svg v-if="i" class="chain-arrow" viewBox="0 0 30 24" aria-hidden="true" :style="{ opacity: reveal(i) }">
          <path d="M2 12 H26 M20 5 L27 12 L20 19" />
          <path d="M2 12 H26" class="pulse" pathLength="100" stroke-dasharray="20 80" :stroke-dashoffset="-motion.cycle * 100" :opacity="running ? .9 : 0" />
        </svg>
        <div class="chain-stage" :class="{ future: i === 4 }" :style="{ opacity: .15 + .85 * reveal(i), transform: `translateY(${(1 - reveal(i)) * 10}px)` }">
          <h3>{{ s.title }}</h3>
          <p>{{ s.what }}</p>
          <small><b>{{ s.who }}</b><br><i>{{ s.id }}</i></small>
        </div>
      </template>
    </div>
    <div class="chain-foot"><span>Stage {{ Math.max(1, stage) }} of 5</span><small>Each arrow is a file hand-over on NERSC: EDM4hep ROOT files after stages 1–2, Parquet tables after stage 3, the same tables with added ML columns after stage 4.</small></div>
  </section>
</template>

<style scoped>
.chain { margin-top: 8px; }
.chain-row { display: grid; grid-template-columns: 1fr 26px 1fr 26px 1fr 26px 1fr 26px 1fr; gap: 4px; align-items: stretch; }
.chain-stage { border: 1px solid var(--nju-line); background: rgba(201,210,221,.035); padding: 9px 10px; min-height: 150px; transition: none; }
.chain-stage.future { border-style: dashed; }
.chain-stage h3 { margin: 0 0 6px; font-size: 13.5px; color: var(--nju-blue); font-weight: 550; line-height: 1.2; }
.chain-stage p { margin: 0; font-size: 11px; line-height: 1.38; color: var(--fg-0); }
.chain-stage small { display: block; margin-top: 7px; font-size: 10px; color: var(--fg-1); line-height: 1.35; }
.chain-stage small b { color: var(--nju-amber); font-weight: 550; }
.chain-arrow { width: 26px; height: 24px; align-self: center; fill: none; stroke: #bcc2cb; stroke-width: 1.4; }
.chain-arrow .pulse { stroke: #fff0ba; stroke-width: 2.4; }
.chain-foot { display: flex; gap: 14px; align-items: baseline; border-top: 1px solid var(--nju-line); margin-top: 8px; padding-top: 6px; font-size: 11px; color: var(--fg-1); }
.chain-foot span { color: var(--nju-amber); white-space: nowrap; }
</style>
