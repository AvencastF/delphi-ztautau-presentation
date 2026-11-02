<script setup lang="ts">
import { computed } from 'vue'
import { useStepMotion } from 'slidev-addon-ztautau/composable/useStepMotion'
import { mixed } from 'slidev-addon-ztautau/composable/tex'
const props = defineProps<{ step: number; identification?: boolean }>()
const { reveal, stage } = useStepMotion(() => props.step, 3, 900)
const topologyDefinitions = [
  { title: 'Topology', text: 'Two narrow, nearly back-to-back decay systems' },
  { title: 'Thrust & hemispheres', text: 'Axis: maximal charged-momentum projection<br/>Division: plane perpendicular to the axis' },
  { title: 'Visible candidates', text: 'Charged tracks + associated neutral objects<br/>Leading track: highest momentum per hemisphere' },
  { title: 'Decay identification', text: 'PID + photons: $e$, $\\mu$, $\\pi$, $\\rho$<br/>This analysis: one charged track per hemisphere' },
]

const candidateDefinitions = [
  { title: 'Electron · $e$', text: 'Electron tag $\\mathrm{ELID}\\ge3$<br/>Muon-tag veto' },
  { title: 'Muon · $\\mu$', text: 'Muon tag $\\mathrm{MUID}\\ge7$<br/>Electron-tag veto' },
  { title: 'Pion · $\\pi$', text: 'Charged hadron · $N_\\gamma=0$' },
  { title: 'Rho · $\\rho$', text: 'Charged hadron · $N_\\gamma=1$ or $2$<br/>$0.5<m(\\mathrm{track}+\\sum\\gamma)<1.04\\,\\mathrm{GeV}$' },
]
const definitions = computed(() => props.identification ? candidateDefinitions : topologyDefinitions)
const diagramReveal = (n: number) => props.identification ? 1 : reveal(n)
const clipId = computed(() => props.identification ? 'candidate-detector-disc' : 'event-detector-disc')
</script>

<template>
  <section class="es" :data-step="step" :class="{ identification }">
    <svg viewBox="0 0 560 340" role="img" aria-label="Tau-pair topology with charged tracks, a thrust axis, perpendicular hemisphere division and visible decay products.">
      <defs><clipPath :id="clipId"><circle cx="280" cy="155" r="112" /></clipPath></defs>
      <g :style="{ opacity: diagramReveal(1) }" :clip-path="`url(#${clipId})`">
        <path d="M0 0 H331 L229 310 H0 Z" fill="#f69cab" fill-opacity=".09" />
        <path d="M331 0 H560 V310 H229 Z" fill="#70dcb2" fill-opacity=".09" />
      </g>
      <circle cx="280" cy="155" r="112" fill="none" stroke="#bcc2cb" stroke-opacity=".3" />
      <circle cx="280" cy="155" r="55" fill="none" stroke="#bcc2cb" stroke-opacity=".12" />
      <g :style="{ opacity: diagramReveal(1) }">
        <line x1="130" y1="105" x2="430" y2="205" stroke="#f0c36e" stroke-dasharray="6 5" stroke-width="1.6" />
        <line x1="322" y1="29" x2="238" y2="281" stroke="#bcc2cb" stroke-opacity=".65" stroke-dasharray="3 4" />
        <foreignObject x="425" y="213" width="125" height="26"><div class="fo axis">Thrust axis</div></foreignObject>
        <foreignObject x="105" y="10" width="150" height="26"><div class="fo pink">Hemisphere 1</div></foreignObject>
        <foreignObject x="330" y="10" width="150" height="26"><div class="fo mint">Hemisphere 2</div></foreignObject>
      </g>
      <path d="M280 155 Q230 133 180 120" fill="none" stroke="#77c9ff" stroke-width="3" />
      <path d="M280 155 Q333 173 380 192" fill="none" stroke="#77c9ff" stroke-width="3" />
      <circle cx="280" cy="155" r="3" fill="#f0f1f3" />
      <g :style="{ opacity: diagramReveal(2) }">
        <circle cx="180" cy="120" r="7" fill="#17191c" stroke="#77c9ff" stroke-width="1.6" />
        <circle cx="380" cy="192" r="7" fill="#17191c" stroke="#77c9ff" stroke-width="1.6" />
        <path d="M175 114 L146 75 H55" fill="none" stroke="#77c9ff" stroke-opacity=".65" />
        <foreignObject x="25" y="46" width="145" height="26"><div class="fo">Leading track</div></foreignObject>
        <path d="M387 188 L421 153 H540" fill="none" stroke="#77c9ff" stroke-opacity=".65" />
        <foreignObject x="408" y="125" width="145" height="26"><div class="fo">Leading track</div></foreignObject>
        <g :style="{ opacity: identification ? (step >= 2 ? 1 : 0) : 1 }">
        <g stroke="#baa5ff" stroke-width="1.4" fill="none"><path d="M280 155 L365 226 M280 155 L392 168" stroke-dasharray="3 4" /></g>
        <circle cx="365" cy="226" r="4" fill="#baa5ff" /><circle cx="392" cy="168" r="4" fill="#baa5ff" />
        <path d="M369 230 L402 264 H498" fill="none" stroke="#baa5ff" stroke-opacity=".65" />
        <foreignObject x="402" y="268" width="110" height="26"><div class="fo violet">Photons</div></foreignObject>
      </g>
      </g>
      <g :style="{ opacity: identification ? (step >= 1 ? 1 : 0) : diagramReveal(3) }">
        <foreignObject x="82" y="180" width="112" height="36"><div class="fo decay pink" v-html="mixed(identification ? (step >= 2 ? '$\\pi$ candidate' : '$e$ candidate') : '$\\mu$ candidate')" /></foreignObject>
        <foreignObject x="350" y="70" width="160" height="36"><div class="fo decay mint" v-html="mixed(identification ? (step >= 2 ? '$\\rho$ candidate' : '$\\mu$ candidate') : '$\\rho\\to\\pi^\\pm\\pi^0$')" /></foreignObject>
      </g>
      <foreignObject x="80" y="314" width="400" height="24"><div class="fo legend">Charged tracks <span>· Photons</span> <i>· schematic</i></div></foreignObject>
    </svg>
    <div v-if="identification" class="id-details id-blocks">
      <template v-if="step < 2">
        <h2>Leptonic candidates</h2>
        <section class="id-panel h-one"><h3>H1 · Electron <LaTeX formula="e" /></h3>
          <div class="id-key">ELID · electron-identification levels</div>
          <div class="id-levels"><span><b>3</b>Loose</span><span><b>4</b>Standard</span><span><b>5</b>Tight</span></div>
          <p class="id-rule"><b>Selection</b> Any of these levels · muon-tag veto</p>
        </section>
        <section class="id-panel h-two"><h3>H2 · Muon <LaTeX formula="\mu" /></h3>
          <div class="id-key">MUID · sum of independent muon flags</div>
          <div class="id-levels mu-flags"><span><b>1</b>Very loose</span><span><b>2</b>Loose</span><span><b>4</b>Standard</span><span><b>8</b>Tight</span><span><b>16</b>HCAL</span></div>
          <p class="id-rule"><b>Selection</b> <LaTeX formula="7=1+2+4" />, or a tight / HCAL flag<br/>Electron-tag veto</p>
        </section>
      </template>
      <template v-else>
        <h2>Hadronic candidates</h2>
        <section class="id-panel hadron-id"><h3>Charged-hadron ID</h3>
          <p class="id-rule"><b>Common</b> Lepton vetoes · <LaTeX formula="p>0.05E_{\rm beam}" /></p>
          <div class="id-route"><b>A</b><div><strong>RICH + TPC <LaTeX formula="dE/dx" /></strong><p>Standard (2) or tight (3) pion tag, plus<br/><LaTeX formula="E_{\rm HPC}/p<0.6" /> or certified absent HPC association</p></div></div>
          <div class="id-route"><b>OR B</b><div><strong>Complete HCAL profile</strong><p><LaTeX formula="\langle E_{\rm HCAL}\rangle_{\rm occupied\ layer}\ge3\,\mathrm{GeV}" /></p></div></div>
        </section>
        <section class="id-panel h-one compact-id"><h3>H1 · Pion <LaTeX formula="\pi" /></h3><p>Charged hadron · <LaTeX formula="N_\gamma=0" /></p></section>
        <section class="id-panel h-two compact-id"><h3>H2 · Rho <LaTeX formula="\rho" /></h3><p>Charged hadron · <LaTeX formula="N_\gamma=1" /> or <LaTeX formula="2" /><br/><LaTeX formula="0.5<m(\mathrm{track}+\sum\gamma)<1.04\,\mathrm{GeV}" /></p></section>
      </template>
    </div>
    <div v-else class="es-definitions">
      <div v-for="(item, index) in definitions" :key="item.title" class="es-definition" :class="{ active: stage === index }">
        <h3 v-html="mixed(item.title)" />
        <p v-html="item.text.split('<br/>').map(line => mixed(line)).join('<br/>')" />
      </div>
    </div>
  </section>
</template>

<style scoped>
.es { display:grid; grid-template-columns:1.3fr 1fr; gap:24px; align-items:center; margin-top:12px; }
.es svg { width:100%; height:340px; display:block; }
.fo { font-size:14px; line-height:24px; white-space:nowrap; color:#bcc2cb; text-align:center; }
.fo.axis { color:#f0c36e; }
.fo.pink { color:#f69cab; }
.fo.mint { color:#70dcb2; }
.fo.violet { color:#baa5ff; }
.fo.decay { font-size:17px; }
.fo.legend { font-size:12px; color:#77c9ff; }
.fo.legend span { color:#baa5ff; margin:0 8px; }
.fo.legend i { color:#bcc2cb; font-style:normal; }
.es-definition { padding:12px 0 12px 15px; border-left:2px solid #ffffff15; }
.es-definition.active { border-left-color:var(--nju-amber); }
.es-definition h3 { margin:0 0 5px; font-size:17px; color:var(--nju-blue); font-weight:600; line-height:1.25; }
.es-definition p { margin:0; font-size:13px; line-height:1.5; color:var(--fg-1); }
.es.identification svg { height:290px; }
.es.identification .es-definition { padding-top:8px; padding-bottom:8px; }
.es.identification { grid-template-columns:1fr 1.2fr; gap:26px; margin-top:6px; }
.es.identification svg { height:320px; }
.id-details h2 { font-size:20px; color:var(--nju-amber); margin:0 0 14px; }
.id-details h3 { font-size:16px; color:var(--nju-blue); margin:0 0 6px; }
.id-details p { font-size:13px; line-height:1.5; color:var(--fg-1); margin:4px 0; }
.id-details section { border-top:1px solid var(--nju-line); padding:9px 0; }
.id-details .id-note { margin-top:20px; }
.id-details .id-hadron p { font-size:12.5px; }
</style>
