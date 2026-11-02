<script setup lang="ts">
// Adapted from CCNU_Seminar/NJUAnimatedEveNet: shell opening and attention/data-flow animation.
import { computed } from 'vue'
import { useStepMotion } from 'slidev-addon-ztautau/composable/useStepMotion'
const props = defineProps<{step:number}>()
const scene = 'core'
const { motion, running } = useStepMotion(() => props.step, 1, 1600)
const ambient = computed(() => ({cycle:motion.cycle}))
const clamp = (v:number) => Math.max(0,Math.min(1,v))
const smooth = (v:number) => v*v*(3-2*v)
const mix = (a:number,b:number,t:number) => a+(b-a)*t
const unpack = computed(() => smooth(clamp((motion.stage-.12)/.78)))
const reveal = (s:number,offset=0) => clamp((motion.stage*3-s+1-offset)/(1-offset))
const kick = (i:number) => running.value ? (1+Math.sin(motion.cycle*Math.PI*2-i*.6))/2 : 0
const travel = (offset=0) => running.value ? clamp((((motion.cycle+offset)%1)-.06)/.68) : 1
const spark = (offset=0) => running.value ? Math.sin(travel(offset)*Math.PI) : 0
const colors=['#77c9ff','#f0c36e','#baa5ff','#70dcb2','#f69cab']
const names=['Classification','','','','Direction diffusion']
const caption='EveNet adaptation: particle attention, classification and FiLM-conditioned direction diffusion'
const eveNetLogo=`${import.meta.env.BASE_URL}evenet-logo-gold.svg`
const rings=[{x:278,y:170,r:66,label:'Particle features',color:colors[0],stage:1},{x:487,y:146,r:48,label:'Event context',color:colors[3],stage:2}]
const attentionPoints=Array.from({length:24},(_,i)=>{const group=Math.floor(i/8),angle=(i%8)*2.4;return {x:[-28,27,2][group]+Math.cos(angle)*(10+i%3*3),y:[-19,-13,29][group]+Math.sin(angle)*(10+i%4*2),group}})
const localEdges=attentionPoints.flatMap((p,i)=>attentionPoints.map((q,j)=>({p,q,i,j})).filter(({q,j})=>j>i&&p.group===q.group&&Math.hypot(p.x-q.x,p.y-q.y)<23))
const globalEdges=[0,3,6,9,12,15,18,21].map(i=>({p:attentionPoints[i],q:attentionPoints[(i+11)%24]}))
const attentionMix=computed(()=>running.value?.5+.5*Math.sin(motion.cycle*Math.PI*2):.55)
const headY=[90,112,172,306,306]
const routes=['M535 146 C598 146 588 90 686 90','','','','M344 170 H357 Q368 170 368 191 V287 Q368 306 390 306 H686']
const particles=Array.from({length:24},(_,i)=>({x:80+Math.cos(i*2.4)*(18+i*1.5),y:170+Math.sin(i*2.4)*(18+i*1.5)}))
</script>
<template>
  <div class="njua" :data-scene="scene" :data-step="step" :data-progress="motion.stage" :data-looping="running" :data-cycle="ambient.cycle">
    <svg viewBox="0 0 880 370" role="img" :aria-label="caption">
      <!-- Distinct schematic operations: local/global attention and token contextualization. -->
      <g v-for="(ring,k) in rings" :key="ring.label" :style="{opacity:scene==='core' ? unpack : 1}">
        <text v-if="scene !== 'core'" :x="ring.x" :y="82" text-anchor="middle" class="strong">{{ ring.label }}</text>
        <g :transform="`translate(${ring.x} ${ring.y}) scale(${ring.r/55})`">
          <g v-if="k===0" class="pet-attention">
            <ellipse v-for="(c,i) in [{x:-28,y:-19},{x:27,y:-13},{x:2,y:29}]" :key="i" :cx="c.x" :cy="c.y" rx="26" ry="24" :stroke="colors[0]" fill="none" stroke-dasharray="2 4" :opacity=".18+.25*(1-attentionMix)" />
            <line v-for="(e,i) in globalEdges" :key="`g${i}`" :x1="e.p.x" :y1="e.p.y" :x2="e.q.x" :y2="e.q.y" :stroke="colors[0]" :opacity=".12+.5*attentionMix" stroke-width="1" />
            <line v-for="(e,i) in localEdges" :key="`l${i}`" :x1="e.p.x" :y1="e.p.y" :x2="e.q.x" :y2="e.q.y" :stroke="colors[0]" :opacity=".22+.55*(1-attentionMix)" stroke-width="1.4" />
            <circle v-for="(p,i) in attentionPoints" :key="i" :cx="p.x" :cy="p.y" :r="3+kick(i)*.7" :fill="colors[0]" />
            <circle v-for="(e,i) in globalEdges" :key="`signal${i}`" :cx="mix(e.p.x,e.q.x,travel(i*.09))" :cy="mix(e.p.y,e.q.y,travel(i*.09))" r="1.9" fill="#e4eaf1" :opacity="spark(i*.09)*attentionMix" />
          </g>
          <g v-else class="object-attention">
            <rect x="-58" y="-52" width="116" height="114" rx="8" class="housing" />
            <g v-for="i in 6" :key="i">
              <line v-for="j in 6" :key="j" x1="-31" :y1="-38+(i-1)*14" x2="31" :y2="-38+(j-1)*14" :stroke="colors[3]" :opacity=".06+.2*kick(i+j)" stroke-width=".8" />
              <rect x="-47" :y="-43+(i-1)*14" width="16" height="10" rx="2" :fill="i>4 ? colors[2] : colors[0]" />
              <rect x="31" :y="-43+(i-1)*14" width="16" height="10" rx="2" :fill="colors[3]" :opacity=".65+.35*kick(i)" />
              <line x1="31" :y1="-38+(i-1)*14" x2="0" y2="49" :stroke="colors[3]" :opacity=".12+.2*kick(i)" stroke-width=".8" />
            </g>
            <rect x="-9" y="42" width="18" height="13" rx="3" :fill="colors[3]" stroke="#e4eaf1" stroke-width="1" />
          </g>
        </g>
      </g>
      <g v-if="scene === 'core'" :style="{opacity:unpack}">
        <path d="M131 170 H201" class="wire" />
        <g v-for="(p,i) in particles" :key="i">
          <circle :cx="p.x" :cy="p.y" r="3" fill="#aebdcd" :style="{opacity:1-reveal(1)*.65}" />

        </g>
        <path d="M20 324 H324 Q403 324 403 236 V183 Q403 160 429 160" class="wire" stroke-dasharray="3 5" />
        <rect v-for="i in 8" :key="i" :x="22+i*20" y="315" width="10" :height="18+kick(i)*7" rx="2" :fill="colors[2]" />
        <path d="M350 170 C392 170 393 146 430 146" class="wire" />
        <g v-for="i in [0,4]" :key="i" :style="{opacity:.12+.88*reveal(i<3?2:3)}">
          <path :d="routes[i]" class="wire" />
          <path :d="routes[i]" :stroke="colors[i]" fill="none" pathLength="100" stroke-dasharray="100" :stroke-dashoffset="100*(1-reveal(i<3?2:3,i%3*.16))" stroke-width="2" />
          <path :d="routes[i]" stroke="#fff" fill="none" pathLength="100" stroke-dasharray="4 96" :stroke-dashoffset="-100*(ambient.cycle+i*.17)" stroke-width="4" :style="{opacity:.75*reveal(i<3?2:3)}" />
          <circle cx="698" :cy="headY[i]" :r="7+2*kick(i*4)" :fill="colors[i]" />
          <text x="719" :y="headY[i]+5" :fill="colors[i]" class="head-name">{{ names[i] }}</text>
          <text x="719" :y="headY[i]+24" class="small">{{ i===0 ? "12 classification outputs" : "1 sample · 50 steps" }}</text>
        </g>
        <g :style="{opacity:reveal(3)}">
          <path d="M316 324 H420 V270 H561 V293" fill="none" :stroke="colors[2]" stroke-dasharray="3 5" stroke-width="1.2" />
          <text x="535" y="257" text-anchor="middle" class="tiny">84 conditions + diffusion time: FiLM</text>
          <g v-for="i in [4]" :key="`decoder${i}`">
            <rect x="488" :y="headY[i]-13" width="146" height="26" rx="5" fill="#23262b" :stroke="colors[i]" stroke-width="1.2" />
            <text x="561" :y="headY[i]+4" text-anchor="middle" class="decoder-label" :fill="colors[i]">Conditioned decoder</text>
          </g>
        </g>
      </g>
      <g v-if="scene === 'core'" :style="{opacity:unpack}">
        <text x="77" y="61" text-anchor="middle" class="label">PARTICLES</text>
        <text x="278" y="61" text-anchor="middle" class="strong">PET particle features</text>
        <text x="278" y="83" text-anchor="middle" class="tiny">Learns relations between particles</text>
        <text x="487" y="49" text-anchor="middle" class="strong">Event context</text>
        <text x="487" y="71" text-anchor="middle" class="tiny">Object encoder</text>
        <text x="278" y="253" text-anchor="middle" class="small">Local + global attention</text>
        <text x="510" y="226" text-anchor="middle" class="small">Object context + event summary</text>
        <text x="87" y="358" text-anchor="middle" class="small">Event conditions</text>
      </g>

      <!-- The shell opens on the single click; the same ambient clock keeps data flowing. -->
      <g v-if="scene==='core'" class="model-shell" :style="{opacity:1-unpack, pointerEvents:unpack>.99?'none':'auto'}">
        <text x="22" y="69" class="label">EVENT INPUT</text>
        <circle v-for="(p,i) in particles" :key="i" :cx="p.x" :cy="p.y" :r="3+kick(i)" fill="#d8e3ef" />
        <path d="M133 170 H201 M20 324 H173 Q190 324 190 292 V250 H201" class="wire" />
        <path d="M133 170 H201 M20 324 H173 Q190 324 190 292 V250 H201" stroke="#c3ceda" fill="none" stroke-width="3" pathLength="100" stroke-dasharray="9 91" :stroke-dashoffset="-ambient.cycle*100" :style="{opacity:.8}" />
        <text x="22" y="352" class="small">84 event conditions</text>
        <g v-for="i in 2" :key="i" :transform="`translate(0 ${(i===1?-1:1)*unpack*145})`">
          <path :d="i===1?'M201 180 V87 L223 65 H617 L639 87 V180 Z':'M201 180 V273 L223 295 H617 L639 273 V180 Z'" fill="#23262b" />
          <path :d="i===1?'M201 178 V87 L223 65 H617 L639 87 V178':'M201 182 V273 L223 295 H617 L639 273 V182'" fill="none" stroke="#9aa7b8" stroke-width="1.5" />
          <path :d="i===1?'M211 124 V93 L229 75 H280 M560 75 H611 L629 93 V124':'M211 236 V267 L229 285 H280 M560 285 H611 L629 267 V236'" fill="none" stroke="#c3ceda" stroke-width="3" :style="{opacity:.5+.5*kick(i*8)}" />
          <line v-for="j in 9" :key="j" :x1="294+j*25" :x2="304+j*25" :y1="i===1?83:277" :y2="i===1?83:277" stroke="#778391" />
          <path :d="i===1?'M225 110 H260 L278 128 H325 M615 110 H580 L562 128 H515':'M225 250 H260 L278 232 H325 M615 250 H580 L562 232 H515'" fill="none" stroke="#586370" stroke-width="1" />
        </g>
        <g :style="{opacity:1-clamp(unpack*2)}">
          <image :href="eveNetLogo" x="300" y="120" width="64" height="64" aria-label="EveNet logo" />
          <foreignObject x="382" y="125" width="175" height="58"><div xmlns="http://www.w3.org/1999/xhtml" class="evenet-wordmark gradient-animated njua-brand njua-brand-shell">EveNet</div></foreignObject>
          <text x="420" y="196" text-anchor="middle" class="small">Pretrained particle representation</text>
          <g v-for="i in 16" :key="i"><rect :x="300+i*14" y="215" width="6" :height="4+kick(i)*10" :fill="colors[(i-1)%5]" rx="1" /></g>
        </g>
        <g v-for="i in [0,4]" :key="i" :style="{opacity:.75+.25*kick(i*4)}">
          <path :d="`M639 180 C668 180 665 ${headY[i]} 695 ${headY[i]}`" class="wire" />
          <path :d="`M639 180 C668 180 665 ${headY[i]} 695 ${headY[i]}`" :stroke="colors[i]" fill="none" stroke-width="2.5" pathLength="100" stroke-dasharray="10 90" :stroke-dashoffset="-100*(ambient.cycle+i*.16)" />
          <circle cx="702" :cy="headY[i]" :r="5+kick(i*4)*2" :fill="colors[i]" />
          <text x="720" :y="headY[i]+5" class="small" :style="{fill:colors[i]}">{{ ['Decay-pair probabilities','','','','Tau-direction diffusion'][i] }}</text>
        </g>
      </g>
    </svg>
    <div class="njua-footer"><div class="njua-caption" aria-live="polite">Same pretrained checkpoint; two separately fine-tuned models</div><span class="njua-note">Schematic</span></div>
  </div>
</template>

<style scoped>
.njua-brand { display:inline-block; width:100%; text-align:center; font-size:18px; line-height:28px; font-weight:550; }
.njua-brand-shell { text-align:left; font-size:43px; line-height:58px; font-weight:650; }
.njua { width:100%; margin-top:10px; }
.njua[data-scene="core"] { margin-top:10px; }
.njua[data-scene="core"] svg { height:285px; }
svg { display:block; width:100%; height:285px; overflow:visible; fill:#e4eaf1; }
svg text { font-family:inherit; font-size:17px; }
svg .strong { font-size:18px; font-weight:550; }
svg .decoder-label { font-size:13px; font-weight:550; }
svg .head-name { font-size:16px; font-weight:550; }
svg .small { font-size:13px; fill:#a8b5c7; }
svg .tiny { font-size:11px; fill:#a8b5c7; }
svg .label { font-size:10px; letter-spacing:1.2px; fill:#a8b5c7; }
.wire { fill:none; stroke:#6f859b; stroke-width:1.3; }
.housing { fill:#101827; stroke:#728298; stroke-opacity:.28; stroke-width:1; }
.socket { fill:#101827; stroke:#a0aec1; stroke-width:1.5; }
.njua-footer { display:flex; align-items:baseline; justify-content:space-between; gap:24px; margin-top:16px; padding-top:14px; border-top:1px solid #ffffff18; }
.njua-caption { font-size:15px; font-weight:450; letter-spacing:-.02em; line-height:1.35; }
.njua-note { flex-shrink:0; color:#a8b5c7; font-size:11px; }
.njua-brand-shell { font-size:39px; }
.njua-footer { margin-top:3px; padding-top:8px; }
</style>
