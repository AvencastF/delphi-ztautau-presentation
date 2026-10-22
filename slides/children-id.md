---
class: st pres
---

# Ten children: identifying each τ decay

<div class="st-sub">Child = inclusive sample + both legs identified as a given pair. "Residual" and "conflict" events stay inclusive-only.</div>

<div class="st-cols st-cols-3">
<div class="kv sel"><h3>Electron</h3><dl><dt>Tag</dt><dd>DELPHI electron tag <span class="id">ELID</span> ≥ 3</dd><dt>Conflict</dt><dd>two positive lepton tags</dd></dl></div>
<div class="kv sel"><h3>Muon</h3><dl><dt>Tag</dt><dd>DELPHI muon word <span class="id">MUID</span> ≥ 7</dd><dt>Momentum</dt><dd>no threshold</dd></dl></div>
<div class="kv sel"><h3>Charged hadron</h3><dl><dt>Veto</dt><dd>neither lepton tag, p &gt; 5 % E_beam</dd><dt>(a)</dt><dd>pion-like tag <span class="id">RPROCO 2/3</span>, HPC E/p &lt; 0.6</dd><dt>(b)</dt><dd>HCAL ≥ 3 GeV per hit layer</dd></dl></div>
<div class="kv sel"><h3>Photon</h3><dl><dt>Object</dt><dd>neutral with unique HPC shower &gt; 0.5 GeV</dd><dt>Nearby</dt><dd>ΔR &lt; 0.3 to the leading track</dd></dl></div>
<div class="kv sel"><h3>π</h3><dl><dt>Rule</dt><dd>charged hadron, no nearby photon</dd></dl></div>
<div class="kv sel"><h3>ρ</h3><dl><dt>Rule</dt><dd>charged hadron + 1–2 nearby photons</dd><dt>Mass</dt><dd>0.5 &lt; m(track + γ) &lt; 1.04 GeV</dd></dl></div>
</div>

<div class="co warn" style="margin-top:10px"><b>Caveat</b> Legacy tags are references, not calibrated working points; nothing here is an efficiency.</div>

<div class="st-source">Source: the selection hand-over note of 2026-10-07 (frozen definitions)</div>

<!--
tau_analysis/docs/EXCLUSIVE_DECAY_HANDOFF_20261007.md "Canonical configuration and frozen definitions"; regions inclusive_1p1p_{ee,emu,epi,erho,mumu,mupi,murho,pipi,pirho,rhorho} = parent + exclusive_pair_X equals 1. Electron: valid ELID >= 3 within supported domain; competing unknown muon tag prevents exclusive assignment. Muon: numeric MUID >= 7, not a bit mask. Hadron: both lepton vetoes, finite strict p/(ECMS/2) > 0.05, (a) RPROCO pion code 2 or 3 with measured associated HPC E/p < 0.6 or certified HPC absence, or (b) uniquely associated complete HCAL profile with mean energy per occupied layer >= 3 GeV (HCNC precedence, producer type 4, layers 1-4, header energy / distinct occupied layers). Photon: resolved PHOT-associated neutral MAIN / unique HPC, HPC energy > 0.5 GeV, profiles 1/11/61, excluding conversion, merged, secondary. rho: MAIN track energy used; one photon = neutral system, not a pi0; rho energy = charged MAIN energy + HPC photon energies. Code: analysis/exclusive_id.py, photon_quality.py, strict_id.py.
-->
