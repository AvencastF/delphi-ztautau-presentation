<script setup lang="ts">
import charts from '../data/neutrino-resolution.json'
const x = (v:number, max:number) => 48 + 205*v/max
const y = (i:number) => 40+53*i
</script>
<template>
<div class="nr-web">
<div class="nr-legend"><span><i class="classic"/>Analytical default</span><span><i class="ml"/>EveNet</span></div>
<div class="nr-panels">
<section v-for="(chart,k) in charts" :key="chart.title">
<h3>{{chart.title}} <small>[<LaTeX :formula="chart.unit" />]</small></h3>
<svg viewBox="0 0 280 258" role="img" :aria-label="chart.title + ': analytical default versus EveNet'">
<g v-for="tick in chart.ticks" :key="tick"><line :x1="x(tick,chart.limit)" :x2="x(tick,chart.limit)" y1="20" y2="227" stroke="#ffffff12"/><text :x="x(tick,chart.limit)" y="248" text-anchor="middle" class="tick">{{tick}}</text></g>
<g v-for="(row,i) in chart.rows" :key="row.label">
<foreignObject x="0" :y="y(i)-12" width="35" height="25"><div class="nr-label"><LaTeX :formula="row.label" /></div></foreignObject>
<line :x1="x(row.a,chart.limit)" :x2="x(row.b,chart.limit)" :y1="y(i)" :y2="y(i)" stroke="#ffffff55" stroke-width="2"/>
<circle :cx="x(row.a,chart.limit)" :cy="y(i)" r="4.5" fill="#f0c36e"><title>Analytical: {{row.a.toFixed(4)}}</title></circle>
<circle :cx="x(row.b,chart.limit)" :cy="y(i)" r="4.5" fill="#77c9ff"><title>EveNet: {{row.b.toFixed(4)}}</title></circle>
<text :x="x(row.a,chart.limit)" :y="y(i)-11" text-anchor="middle" class="value classic-text">{{row.a.toFixed(2)}}</text>
<text :x="x(row.b,chart.limit)" :y="y(i)+20" text-anchor="middle" class="value ml-text">{{row.b.toFixed(2)}}</text>
</g>
<line x1="48" x2="253" y1="227" y2="227" stroke="#ffffff44"/>
</svg>
</section>
</div>
</div>
</template>
<style scoped>
.nr-web{margin-top:15px}.nr-legend{display:flex;justify-content:center;gap:30px;font-size:13px;margin-bottom:15px}.nr-legend span{display:flex;align-items:center;gap:8px}.nr-legend i{width:9px;height:9px;border-radius:50%;display:inline-block}.classic{background:#f0c36e}.ml{background:#77c9ff}.nr-panels{display:grid;grid-template-columns:1fr 1fr 1.1fr;gap:20px}.nr-panels section{border-top:1px solid #ffffff25;padding-top:10px}.nr-panels h3{font-size:16px!important;line-height:1.3;margin:0 0 8px!important;font-weight:550;color:#e4eaf1}.nr-panels small{font-size:12px;color:#a8b5c7}.nr-panels svg{display:block;width:100%;height:250px}.nr-panels svg text{font-family:inherit!important;letter-spacing:0!important}.nr-panels .tick{font-size:11px!important;fill:#a8b5c7}.nr-panels .value{font-size:13px!important;font-weight:550}.classic-text{fill:#f0c36e}.ml-text{fill:#77c9ff}.nr-label{font-size:15px;color:#e4eaf1;text-align:center;line-height:25px}
</style>
