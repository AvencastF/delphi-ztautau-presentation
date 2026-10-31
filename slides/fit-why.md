---
class: st pres
---

# Why spin: the two <LaTeX formula="\tau" /> leptons are born entangled

<div class="st-cols st-cols-2">
<div>
<svg viewBox="0 0 420 250" style="width:100%;height:250px" role="img" aria-label="A Z boson decays into two tau leptons whose spins share one state; their decay products fly out along directions that follow the spins.">
<defs><marker id="fw-ar" markerWidth="8" markerHeight="8" refX="6" refY="4" orient="auto"><path d="M0 0 L8 4 L0 8 z" fill="#f0c36e"/></marker>
<marker id="fw-ab" markerWidth="8" markerHeight="8" refX="6" refY="4" orient="auto"><path d="M0 0 L8 4 L0 8 z" fill="#77c9ff"/></marker></defs>
<circle cx="210" cy="120" r="20" fill="#23262b" stroke="#c9e86a" stroke-width="1.6"/><text x="210" y="125" text-anchor="middle" style="font-size:15px" fill="#f0f1f3">Z</text>
<line x1="190" y1="120" x2="90" y2="120" stroke="#bcc2cb" stroke-width="1.6"/><line x1="230" y1="120" x2="330" y2="120" stroke="#bcc2cb" stroke-width="1.6"/>
<circle cx="80" cy="120" r="13" fill="#23262b" stroke="#bcc2cb"/><text x="80" y="124" text-anchor="middle" style="font-size:14px" fill="#f0f1f3">τ⁻</text>
<circle cx="340" cy="120" r="13" fill="#23262b" stroke="#bcc2cb"/><text x="340" y="124" text-anchor="middle" style="font-size:14px" fill="#f0f1f3">τ⁺</text>
<line x1="80" y1="104" x2="80" y2="70" stroke="#f0c36e" stroke-width="2.4" marker-end="url(#fw-ar)"/>
<line x1="340" y1="136" x2="340" y2="170" stroke="#f0c36e" stroke-width="2.4" marker-end="url(#fw-ar)"/>
<path d="M93 96 C150 40 270 40 327 96" fill="none" stroke="#c9e86a" stroke-width="1.6" stroke-dasharray="5 4"/>
<text x="210" y="50" text-anchor="middle" style="font-size:14px" fill="#c9e86a">one shared spin state</text>
<line x1="72" y1="128" x2="22" y2="190" stroke="#77c9ff" stroke-width="2" marker-end="url(#fw-ab)"/><text x="18" y="212" style="font-size:14px" fill="#77c9ff">π⁻</text>
<line x1="348" y1="112" x2="400" y2="40" stroke="#77c9ff" stroke-width="2" marker-end="url(#fw-ab)"/><text x="380" y="32" style="font-size:14px" fill="#77c9ff">π⁺</text>
<text x="210" y="240" text-anchor="middle" style="font-size:13px" fill="#bcc2cb">spins (amber) are hidden; decay directions (blue) are measured</text>
</svg>
</div>
<div>
<div class="kv fit"><h3><span class="tag fit">fit</span> In one sentence each</h3><dl>
<dt>Entangled</dt><dd>the pair has one joint spin state; neither <LaTeX formula="\tau" /> has a spin of its own</dd>
<dt>Bell violation</dt><dd>spin correlations stronger than any explanation with spins fixed at birth allows</dd>
<dt>Why <LaTeX formula="\tau" /></dt><dd>it decays after about 2 mm, and its decay products fly preferentially along its spin</dd>
</dl></div>
<div class="co decision"><b>Goal</b> Measure the full spin state, then test both questions.</div>
</div>
</div>

<div class="st-source">Source: method notes of the spin-fit code; standard quantum-information definitions; schematic picture</div>

<!--
tau_analysis/joint_fit/README.md (spin density matrix, witness, Bell tests); docs/PROJECT_GUIDE.md "Full spin-density-matrix contract" (preserve all 15 coefficients). "About 2 mm": mean decay length gamma c tau = (45.6 GeV / 1.777 GeV) x 87 micrometres = 2.2 mm at the Z pole (derived from PDG tau lifetime 290 fs; textbook values). Entanglement: the two-qubit state is not a product (or mixture of products) of single-tau states; Bell violation: CHSH-type correlation beyond the local-hidden-variable bound (here |C_kk - C_rr| > sqrt 2 for the best combination). Picture schematic: pi as the analyser (analysing power 1). Spin directions are drawn opposite only for illustration.
-->
