<script setup lang="ts">
import { computed } from 'vue'
import { useStepMotion } from 'slidev-addon-ztautau/composable/useStepMotion'
import { tex, mixed } from 'slidev-addon-ztautau/composable/tex'
const props = defineProps<{ step: number }>()
const { reveal } = useStepMotion(() => props.step, 3, 800)

// R is the coefficient matrix in the Pauli basis, NOT the density matrix in a spin basis.
const matrix = computed(() => {
  const b = props.step === 2 ? '#ffe1a0' : '#f0c36e'
  const c = props.step === 3 ? '#d9f49b' : '#c9e86a'
  return tex(String.raw`R=\begin{pmatrix}
  1 & {\color{${b}}B^+_n} & {\color{${b}}B^+_r} & {\color{${b}}B^+_k} \\
  {\color{${b}}B^-_n} & {\color{${c}}C_{nn}} & {\color{${c}}C_{nr}} & {\color{${c}}C_{nk}} \\
  {\color{${b}}B^-_r} & {\color{${c}}C_{rn}} & {\color{${c}}C_{rr}} & {\color{${c}}C_{rk}} \\
  {\color{${b}}B^-_k} & {\color{${c}}C_{kn}} & {\color{${c}}C_{kr}} & {\color{${c}}C_{kk}}
  \end{pmatrix}`)
})
</script>

<template>
  <section class="spin-expanded">
    <div class="spin-definition"><LaTeX formula="\rho=\frac14\sum_{a,b\in\{0,n,r,k\}}R_{ab}\,\sigma_a\otimes\sigma_b,\qquad\sigma_0=\mathbb{1}" /></div>
    <div class="spin-body">
      <div class="spin-animation">
        <p class="spin-order">Helicity basis <LaTeX formula="(n,r,k)" /></p>
    <svg viewBox="0 -16 560 316" role="img" aria-label="Sketch: a Z decays to a tau pair; each tau carries a spin read along three axes k, r, n.">
      <defs>
        <marker id="ss-li" markerWidth="8" markerHeight="8" refX="6" refY="4" orient="auto"><path d="M0 0 L8 4 L0 8 z" fill="#c9e86a" /></marker>
      </defs>
      <!-- beam line -->
      <line x1="20" y1="150" x2="540" y2="150" stroke="#6b7280" stroke-width="1" stroke-dasharray="4 5" />
      <foreignObject x="7" y="151" width="44" height="36"><div xmlns="http://www.w3.org/1999/xhtml" class="fo sm" v-html="mixed('$e^-$')" /></foreignObject>
      <foreignObject x="509" y="151" width="44" height="36"><div xmlns="http://www.w3.org/1999/xhtml" class="fo sm" v-html="mixed('$e^+$')" /></foreignObject>
      <!-- Z -->
      <circle cx="280" cy="150" r="20" fill="#23262b" stroke="#c9e86a" stroke-width="1.6" />
      <foreignObject x="258" y="135" width="44" height="36"><div xmlns="http://www.w3.org/1999/xhtml" class="fo lab"  v-html="mixed('$Z$')" /></foreignObject>
      <!-- Helicity axes drawn first, behind the tau particle and its label. -->
      <g :style="{ opacity: reveal(1) }">
        <line x1="452" y1="64" x2="522" y2="30" stroke="#c9e86a" stroke-width="1.6" stroke-dasharray="6 5" marker-end="url(#ss-li)" />
        <foreignObject x="517" y="9" width="38" height="36"><div xmlns="http://www.w3.org/1999/xhtml" class="fo axis" v-html="mixed('$k$')" /></foreignObject>
        <line x1="452" y1="64" x2="418" y2="-2" stroke="#c9e86a" stroke-width="1.6" stroke-dasharray="6 5" marker-end="url(#ss-li)" />
        <foreignObject x="391" y="-13" width="38" height="36"><div xmlns="http://www.w3.org/1999/xhtml" class="fo axis" v-html="mixed('$r$')" /></foreignObject>
        <line x1="452" y1="64" x2="476" y2="108" stroke="#c9e86a" stroke-width="1.6" stroke-dasharray="6 5" marker-end="url(#ss-li)" />
        <foreignObject x="471" y="101" width="38" height="36"><div xmlns="http://www.w3.org/1999/xhtml" class="fo axis" v-html="mixed('$n$')" /></foreignObject>

      </g>
      <!-- tau lines -->
      <line x1="298" y1="140" x2="440" y2="70" stroke="#bcc2cb" stroke-width="1.8" />
      <line x1="262" y1="160" x2="120" y2="230" stroke="#bcc2cb" stroke-width="1.8" />
      <circle cx="452" cy="64" r="14" fill="#23262b" stroke="#77c9ff" stroke-width="1.5" />
      <foreignObject x="430" y="50" width="44" height="36"><div xmlns="http://www.w3.org/1999/xhtml" class="fo particle" v-html="mixed('$\\tau^+$')" /></foreignObject>
      <circle cx="108" cy="236" r="14" fill="#23262b" stroke="#f0c36e" stroke-width="1.5" />
      <foreignObject x="86" y="222" width="44" height="36"><div xmlns="http://www.w3.org/1999/xhtml" class="fo particle" v-html="mixed('$\\tau^-$')" /></foreignObject>
      <!-- B highlight -->
      <g :style="{ opacity: reveal(2) }">
        <foreignObject x="30" y="20" width="280" height="40"><div xmlns="http://www.w3.org/1999/xhtml" class="fo lab" style="color:#f0c36e;text-align:left" v-html="mixed('$B^{-}_i,\\; B^{+}_i$')" /></foreignObject>
      </g>
      <!-- C highlight -->
      <g :style="{ opacity: reveal(3) }">
        <foreignObject x="160" y="260" width="300" height="44"><div xmlns="http://www.w3.org/1999/xhtml" class="fo lab" style="color:#c9e86a;text-align:right" v-html="mixed('$C_{ij}=\\langle\\sigma^{-}_i\\,\\sigma^{+}_j\\rangle$')" /></foreignObject>
      </g>
    </svg>
        <p class="spin-caption"><LaTeX formula="k" />: flight · <LaTeX formula="r" />: production plane · <LaTeX formula="n" />: normal</p>
      </div>
      <div class="spin-map">
        <p class="spin-order">Rows: <LaTeX formula="\tau^-" /> · Columns: <LaTeX formula="\tau^+" /></p>
        <div class="spin-matrix" v-html="matrix" />
        <p class="spin-caption">Pauli-basis coefficients of <LaTeX formula="\rho" /> · Order <LaTeX formula="(0,n,r,k)" /></p>
      </div>
    </div>
    <div class="spin-key">
      <div :class="{ active: step === 2 }"><b class="spin-b"><LaTeX formula="B^-_i,\ B^+_i" /> — six polarisations</b><p>Average spin of each particle along each axis.</p></div>
      <div :class="{ active: step === 3 }"><b class="spin-c"><LaTeX formula="C_{ij}" /> — nine correlations</b><p>Joint spin expectation for every pair of axes.</p></div>
    </div>

  </section>
</template>

<style scoped>
.spin-expanded { margin-top:6px; }
.spin-definition { font-size:20px; text-align:center; padding:8px 0 14px; border-bottom:1px solid var(--nju-line); }
.spin-body { display:grid; grid-template-columns:1.1fr 1fr; gap:24px; align-items:center; padding:14px 0 8px; }
.spin-order { font-size:14px; color:var(--fg-1); text-align:center; margin:0 0 12px; }
.spin-matrix { font-size:20px; text-align:center; }
.spin-caption { text-align:center; font-size:12px; color:var(--fg-1); margin:8px 0 0; }
.spin-key { display:grid; grid-template-columns:1.1fr 1fr; gap:24px; }
.spin-key > div { padding:6px 10px; border-left:1px solid transparent; }
.spin-key > div.active { border-color:var(--nju-amber); background:rgba(240,195,110,.045); }
.spin-key b { font-size:16px; font-weight:550; }
.spin-key .spin-b { color:var(--nju-amber); }
.spin-key .spin-c { color:#c9e86a; }
.spin-key p { margin:5px 0 0; font-size:13px; line-height:1.4; color:var(--fg-1); }
.spin-animation svg { display:block; width:100%; height:200px; overflow:visible; }
.sm { font-size: 20px; fill: #bcc2cb; }
.lab { font-size: 22px; fill: #f0f1f3; }
.fo.axis { font-size: 24px; color: #c9e86a; }
.fo { line-height: 28px; white-space: normal; color: #bcc2cb; text-align: center; }
.fo.lab { font-size: 22px; color: #f0f1f3; }
.fo.sm { font-size: 20px; }
.fo.particle { font-size:15px; line-height:28px; color:var(--fg-0); }
</style>
