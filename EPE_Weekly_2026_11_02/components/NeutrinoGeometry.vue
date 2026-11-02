<template>
<div class="nu-geometry">
<svg viewBox="0 0 440 300" role="img" aria-label="Schematic: two analytical tau-direction branches, ML continuous direction, visible momentum and inferred missing momentum">
<defs><marker id="nu-vector-blue" markerWidth="7" markerHeight="7" refX="6" refY="3" orient="auto"><path d="M0 0 L6 3 L0 6" fill="#77c9ff"/></marker><marker id="nu-vector-purple" markerWidth="7" markerHeight="7" refX="6" refY="3" orient="auto"><path d="M0 0 L6 3 L0 6" fill="#baa5ff"/></marker><marker id="nu-vector-green" markerWidth="7" markerHeight="7" refX="6" refY="3" orient="auto"><path d="M0 0 L6 3 L0 6" fill="#70dcb2"/></marker></defs>
<path d="M40 174 L300 128 L408 194 L146 242 Z" fill="#77c9ff09" stroke="#77c9ff33"/>
<line x1="80" y1="194" x2="337" y2="63" stroke="#f0c36e" stroke-width="2" stroke-dasharray="6 5"/>
<line x1="80" y1="194" x2="350" y2="270" stroke="#f0c36e" stroke-width="2" stroke-dasharray="6 5"/>
<line x1="80" y1="194" x2="287" y2="169" stroke="#77c9ff" stroke-width="3" marker-end="url(#nu-vector-blue)"/>
<line x1="80" y1="194" x2="348" y2="89" stroke="#baa5ff" stroke-width="3" marker-end="url(#nu-vector-purple)"/>
<line x1="287" y1="169" x2="348" y2="89" stroke="#70dcb2" stroke-width="2.5" marker-end="url(#nu-vector-green)"/>
<circle cx="80" cy="194" r="4" fill="white"/>
<foreignObject x="278" y="28" width="150" height="25"><div class="geo-label gold">Analytical A</div></foreignObject>
<foreignObject x="282" y="271" width="150" height="25"><div class="geo-label gold">Analytical B</div></foreignObject>
<foreignObject x="126" y="91" width="165" height="25"><div class="geo-label purple"><LaTeX formula="\vec p_\tau^{\,\rm ML}" /> · continuous direction</div></foreignObject>
<foreignObject x="187" y="176" width="130" height="25"><div class="geo-label blue"><LaTeX formula="\vec p_{\rm vis}" /></div></foreignObject>
<foreignObject x="343" y="124" width="95" height="30"><div class="geo-label green"><LaTeX formula="\vec p_{\rm miss}" /></div></foreignObject>
<text x="28" y="256" fill="#a8b5c7" font-size="11">Leading-track plane</text>
<text x="12" y="18" fill="#a8b5c7" font-size="11">Schematic · momentum vectors, not an event display</text>
</svg>
</div>
</template>
<style scoped>
svg{width:100%;height:270px} svg text{font-size:11px !important;font-family:inherit !important;}.geo-label{font-size:12px;color:#e4eaf1}.gold{color:#f0c36e}.purple{color:#baa5ff}.blue{color:#77c9ff}.green{color:#70dcb2}
</style>
