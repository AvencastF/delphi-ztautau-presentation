<template>
  <section class="qe-landscape">
    <div class="qe-established">
      <h3>At the LHC</h3>
      <article class="qe-row">
        <div class="qe-process"><LaTeX formula="t\bar t" /><span class="qe-spin-label">Two qubits</span></div>
        <div><b class="qe-observed">Entanglement observed</b><p>Dilepton measurement at ATLAS.<br>Different kinematics probe different quantum observables.</p><small>Nature · 2024</small></div>
      </article>
      <article class="qe-row">
        <div class="qe-process"><LaTeX formula="H\to ZZ^*" /><span class="qe-spin-label">Spin-<LaTeX formula="1" /> pair</span></div>
        <div><b>Entanglement measurement</b><p>ATLAS hypothesis test under SM assumptions.</p><small>Physical Review Letters · 2026</small></div>
      </article>
      <article class="qe-row">
        <div class="qe-process"><LaTeX formula="H\to WW^*" /><span class="qe-spin-label">Spin-<LaTeX formula="1" /> pair</span></div>
        <div><b>Studies ongoing</b><p>Experimental programme in progress.</p></div>
      </article>
    </div>
    <div class="qe-opportunity">
      <h3>Spin correlations in <LaTeX formula="\tau^+\tau^-" /> production</h3>
      <div class="qe-study">
        <h4>Phenomenological studies</h4>
        <p>Spin tomography, entanglement and Bell sensitivity studied in simulated <LaTeX formula="pp\to\tau^+\tau^- X" /> events.</p>
        <small>Zhang et al., JHEP 04 (2026) 190</small>
      </div>
      <div class="qe-study">
        <h4>Proposed measurement with DELPHI</h4>
        <p>We propose a measurement of spin and quantum correlations in <LaTeX formula="Z\to\tau^+\tau^-" /> at the <LaTeX formula="Z" /> pole using archived DELPHI data.</p>
      </div>

    </div>
  </section>
</template>

<style scoped>
.qe-landscape { display:grid; grid-template-columns:1.1fr 1fr; gap:36px; margin-top:22px; height:350px; }
.qe-landscape h3 { margin:0 0 16px; font-size:17px; font-weight:600; color:var(--fg-1); }
.qe-row { display:grid; grid-template-columns:116px 1fr; gap:14px; padding:12px 0; border-top:1px solid var(--nju-line); }
.qe-row:first-of-type { padding-top:18px; }
.qe-process { font-size:21px; color:var(--fg-0); }
.qe-process > .qe-spin-label { display:block; font-size:11px; color:var(--fg-1); margin-top:8px; }
.qe-row b { font-size:15px; font-weight:600; color:var(--fg-0); }
.qe-row b.qe-observed { color:var(--nju-mint); }
.qe-row p { font-size:13px; line-height:1.4; margin:5px 0; color:var(--fg-1); }
.qe-row small { font-size:10px; color:var(--fg-1); }
.qe-opportunity { padding:0 0 0 28px; border-left:1px solid var(--nju-line); }
.qe-study { border-top:1px solid var(--nju-line); padding:22px 0 30px; }
.qe-study h4 { font-size:15px; font-weight:600; margin:0 0 8px; color:var(--fg-0); }
.qe-study p { font-size:13px; line-height:1.4; margin:0 0 8px; color:var(--fg-1); }
.qe-study small { font-size:10px; color:var(--fg-1); }
</style>
