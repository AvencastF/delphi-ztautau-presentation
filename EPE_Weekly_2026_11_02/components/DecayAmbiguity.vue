<script setup lang="ts">
import {computed} from 'vue'
import {useStepMotion} from 'slidev-addon-ztautau/composable/useStepMotion'
const props=defineProps<{step:number}>()
const {motion,reveal,stage}=useStepMotion(()=>props.step,3,1000)
const names=['Two kinematic solutions','Identical momenta','Displaced tracks','Conditional inference']
const project=(v:number[])=>[190+155*v[0]+90*v[2],180-105*v[1]-55*v[2]]
const n=[.7,.5,Math.sqrt(.26)]
const a=project(n), b=project([n[0],-n[1],n[2]]), mean=[(a[0]+b[0])/2,(a[1]+b[1])/2]
const axes=[[1,0,0],[.35,0,Math.sqrt(1-.35**2)]]
const cones=axes.map(v=>{const c=v.reduce((s,x,i)=>s+x*n[i],0),r=Math.sqrt(1-c*c),u=[0,1,0],w=[-v[2],0,v[0]];const pts=Array.from({length:81},(_,i)=>project(v.map((x,j)=>c*x+r*(Math.cos(i*Math.PI/40)*u[j]+Math.sin(i*Math.PI/40)*w[j]))));return {pts,path:pts.map((p,i)=>`${i?'L':'M'}${p[0]},${p[1]}`).join(' ')+'Z',axis:project(v)}})
const showGeometry=computed(()=>1-reveal(2))
const meanPoint=(p:number[])=>p.map((v,i)=>v+(mean[i]-v)*reveal(1))
</script>
<template>
<div class="da">
<div class="da-stages"><span v-for="(name,i) in names" :key="name" :class="{current:stage===i,done:stage>i}">{{i+1}} · {{name}}</span></div>
<div class="da-layout">
<div class="da-visual">
<svg viewBox="0 0 480 320" role="img" :aria-label="names[stage] + ', schematic geometry'">
<defs><marker id="da-arrow" markerWidth="7" markerHeight="7" refX="6" refY="3" orient="auto-start-reverse"><path d="M0 0L6 3L0 6" fill="context-stroke"/></marker></defs>
<g :opacity="showGeometry">
<path d="M53 205 L316 105 L435 175 L169 276Z" fill="#ffffff06" stroke="#ffffff20"/>
<text x="48" y="294" class="small">Visible-momentum plane</text>
<g v-for="(cone,k) in cones" :key="k" :stroke="k?'#f0c36e':'#77c9ff'">
<path :d="cone.path" fill="none" stroke-width="1.7" opacity=".65"/>
<line v-for="j in [0,20,40,60]" :key="j" x1="190" y1="180" :x2="cone.pts[j][0]" :y2="cone.pts[j][1]" opacity=".2"/>
<line x1="190" y1="180" :x2="cone.axis[0]" :y2="cone.axis[1]" stroke-width="2" stroke-dasharray="5 5"/>
</g>
<line x1="190" y1="180" :x2="a[0]" :y2="a[1]" stroke="#70dcb2" stroke-width="2.5"/>
<line x1="190" y1="180" :x2="b[0]" :y2="b[1]" stroke="#70dcb2" stroke-width="2.5"/>
<circle v-for="(p,i) in [a,b]" :key="i" :cx="p[0]" :cy="p[1]" r="5" fill="#70dcb2"/>
<text :x="a[0]+10" :y="a[1]-7" class="label green">A</text><text :x="b[0]+10" :y="b[1]+12" class="label green">B</text>
<circle cx="190" cy="180" r="4" fill="#e4eaf1"/>
<foreignObject x="215" y="20" width="250" height="28"><div class="mathlabel"><LaTeX formula="\hat n_\tau^{A,B}" />: mirror solutions</div></foreignObject>
<g :opacity="reveal(1)">
<line :x1="a[0]" :y1="a[1]" :x2="b[0]" :y2="b[1]" stroke="#baa5ff" stroke-dasharray="3 4"/>
<circle v-for="(p,i) in [a,b]" :key="i" :cx="meanPoint(p)[0]" :cy="meanPoint(p)[1]" r="6" fill="#baa5ff"/>
<line x1="190" y1="180" :x2="mean[0]" :y2="mean[1]" stroke="#baa5ff" stroke-width="2"/>
<text :x="mean[0]+12" :y="mean[1]+4" class="small purple">mean</text>
</g>
</g>
<g :opacity="reveal(2)">
<text x="24" y="28" class="small">Side view · normal to the mirror plane</text>
<line x1="42" y1="170" x2="450" y2="170" stroke="#ffffff44" stroke-dasharray="4 4"/>
<text x="315" y="190" class="small">Mirror plane</text>
<rect x="70" y="90" width="365" height="22" rx="8" fill="#77c9ff" :opacity=".12*reveal(3)"/>
<line x1="65" y1="101" x2="440" y2="101" stroke="#77c9ff" stroke-width="2.5" marker-end="url(#da-arrow)"/>
<line x1="65" y1="239" x2="440" y2="239" stroke="#f0c36e" stroke-width="2" stroke-dasharray="6 5" :opacity="1-.65*reveal(3)"/>
<line x1="115" y1="170" x2="288" y2="101" stroke="#baa5ff" stroke-width="3" marker-end="url(#da-arrow)"/>
<line x1="115" y1="170" x2="288" y2="239" stroke="#f0c36e" stroke-width="2" stroke-dasharray="5 5" :opacity="1-.65*reveal(3)"/>
<circle cx="115" cy="170" r="4" fill="#fff"/><circle cx="288" cy="101" r="5" fill="#baa5ff"/>
<line x1="115" y1="170" x2="115" y2="101" stroke="#70dcb2" stroke-width="3" marker-end="url(#da-arrow)"/>
<line x1="115" y1="170" x2="115" y2="239" stroke="#f0c36e" stroke-width="2" stroke-dasharray="3 4" :opacity="1-.65*reveal(3)"/>
<text x="270" y="80" class="label blue">Measured track</text>
<text x="270" y="267" class="small gold">Reflected track hypothesis</text>
<text x="27" y="193" class="small">Production point</text>
<foreignObject x="47" y="119" width="60" height="28"><div class="mathlabel green"><LaTeX formula="b_\perp" /></div></foreignObject>
<foreignObject x="167" y="119" width="100" height="28"><div class="mathlabel purple"><LaTeX formula="\tau" /> flight</div></foreignObject>
<text x="32" y="307" class="small">Same track momentum · different spatial displacement</text>
</g>
</svg>
<div class="da-visual-caption" v-if="stage<2"><span class="blue">Visible leg 1 cone</span><span class="gold">Reflected leg 2 cone</span><span class="green">Allowed directions</span></div>
<div class="da-visual-caption" v-else><span class="blue">Track position</span><span class="purple">Decay displacement</span><span class="green">Normal IP component</span></div>
</div>
<div class="da-copy">
<template v-if="stage===0"><h2>Kinematics gives two directions</h2><p>Hadronic decays · one massless neutrino per leg<br/>Beam-energy taus · back-to-back approximation</p><div class="da-eq"><LaTeX formula="\cos\alpha=\frac{2E_\tau E_{\rm vis}-m_\tau^2-m_{\rm vis}^2}{2|\vec p_\tau||\vec p_{\rm vis}|}" /></div><p>Two cone intersections when real solutions exist<br/><strong>Reflection through the visible-momentum plane</strong></p></template>
<template v-else-if="stage===1"><h2>Momenta do not select the side</h2><p>Same visible energies, masses and momenta<br/><strong>Opposite out-of-plane components</strong></p><div class="da-callout"><b>Symmetric targets + squared loss</b><div class="da-eq"><LaTeX formula="\tfrac12(\hat n_A+\hat n_B)\cdot\hat n_\perp=0" /></div><span>Conditional mean lies in the mirror plane</span></div><p>Signed transverse angular information is diluted.<br/>Diffusion can retain both modes; it need not average them.</p></template>
<template v-else-if="stage===2"><h2>Track displacement supplies the sign</h2><p>Finite <LaTeX formula="\tau" /> flight displaces the decay point.<br/>Impact parameter: production point to closest track point.</p><div class="da-eq"><LaTeX formula="b_\perp=\vec b\cdot\hat n_\perp=\vec L\cdot\hat n_\perp" /></div><p>Reflection flips <LaTeX formula="\vec b\cdot\hat n_\perp" />.<br/>The full impact-parameter vector need not reverse.</p><div class="da-callout"><b>Two tracks, shared production point</b><span>Signed spatial information distinguishes mirror hypotheses.</span></div></template>
<template v-else><h2>Geometry conditions the prediction</h2><p>Signed impact parameters · uncertainties · availability<br/>Kinematics + detector information <LaTeX formula="\longrightarrow" /> FiLM</p><div class="da-eq"><LaTeX formula="D=(\vec b_- - \vec b_+)\cdot\hat n_\perp" /></div><p>Finite resolution and vertex uncertainty:<br/><strong>probabilistic preference, not a perfect branch tag</strong></p><table><thead><tr><th>Correct side</th><th>Inclusive</th><th><LaTeX formula="\pi\pi" /></th></tr></thead><tbody><tr><td>Analytical default</td><td>59.1%</td><td>50.1%</td></tr><tr><td>EveNet</td><td>72.4%</td><td>73.5%</td></tr></tbody></table><div class="da-cohort">1992–1995 held-out simulation · method-valid events</div></template>
</div>
</div>

</div>
</template>
<style scoped>
.da{margin-top:17px}.da-stages{display:grid;grid-template-columns:repeat(4,1fr);gap:14px;font-size:12px;color:#75818f}.da-stages span{border-top:2px solid #ffffff15;padding-top:9px}.da-stages .current{color:#baa5ff;border-color:#baa5ff}.da-stages .done{color:#c2c9d1;border-color:#baa5ff66}.da-layout{display:grid;grid-template-columns:1.1fr 1fr;gap:22px;align-items:start;margin-top:22px;min-height:354px}.da-visual svg{width:100%;height:300px;overflow:visible}.da svg text{font-family:inherit!important;letter-spacing:0!important}.da svg .small{font-size:11px!important;fill:#a8b5c7}.da svg .label{font-size:14px!important}.da .blue{color:#77c9ff;fill:#77c9ff}.da .gold{color:#f0c36e;fill:#f0c36e}.da .green{color:#70dcb2;fill:#70dcb2}.da .purple{color:#baa5ff;fill:#baa5ff}.mathlabel{font-size:13px;line-height:26px;color:#dbe2eb}.mathlabel.green{color:#70dcb2}.mathlabel.purple{color:#baa5ff}.da-visual-caption{display:flex;justify-content:space-around;gap:8px;font-size:10px;margin-top:12px}.da-copy h2{font-size:21px!important;color:#baa5ff;margin:0 0 18px!important;line-height:1.2}.da-copy p{font-size:14px!important;line-height:1.65!important;margin:13px 0!important}.da-eq{font-size:17px;color:#f0c36e;margin:20px 0}.da-callout{padding:12px 14px;border-left:2px solid #70dcb2;background:#70dcb206;font-size:13px}.da-callout b{display:block;color:#70dcb2;margin-bottom:7px}.da-callout .da-eq{margin:12px 0}.da-callout>span{display:block;line-height:1.5}.da-copy table{font-size:14px;width:100%;border-collapse:collapse;margin-top:12px}.da-copy th,.da-copy td{padding:9px 5px;border-bottom:1px solid #ffffff22;text-align:right}.da-copy th:first-child,.da-copy td:first-child{text-align:left}.da-copy tbody tr:last-child{color:#70dcb2}.da-cohort{font-size:10px;color:#a8b5c7;margin-top:10px}.da-bottom{border-top:1px solid #ffffff22;padding-top:14px;margin-top:5px;display:flex;justify-content:space-between;align-items:center;font-size:16px;color:#c3ccda}.da-bottom>span{font-size:10px;color:#a8b5c7}
</style>
