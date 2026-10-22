---
class: st pres
---

# Known residual disagreements, recorded and not tuned away

<div class="st-sub">Shape comparisons after normalisation; statistical only, diagnostic. From the 2026-10-07 audit scan.</div>

<table class="lg">
<thead><tr><th>Variable</th><th>Where</th><th>Size (χ²/dof)</th><th>Reason on record</th></tr></thead>
<tbody>
<tr><td>Hadron-calorimeter mean per layer</td><td>inclusive H0 / H1</td><td><span class="badge r">364.9/59</span> <span class="badge r">501.8/59</span></td><td>response mismodelled; measured for 65 % / 63 % of events only</td></tr>
<tr><td>Hadron-source category</td><td>inclusive H0 / H1</td><td><span class="badge r">154.7/6</span> <span class="badge r">297.4/6</span></td><td>follows from the calorimeter mismatch; feeds hadron ID (b)</td></tr>
<tr><td>Leading-track momentum</td><td>inclusive H0 / H1</td><td><span class="badge g">48.0/45</span> <span class="badge g">61.7/45</span></td><td>within statistics</td></tr>
<tr><td>Leading-track cos θ</td><td>inclusive H0 / H1</td><td><span class="badge a">56.6/36</span> <span class="badge g">45.9/36</span></td><td>mild; angular splits pending</td></tr>
<tr><td>Pion-channel composition</td><td>ππ, πρ, eπ, μπ</td><td>matching 0.18–0.44</td><td>ρ with unidentified photons accepted as π</td></tr>
</tbody>
</table>

<div class="st-cols st-cols-2" style="margin-top:10px">
<div class="co ok"><b>Rates</b> Child data/MC within 0.95–1.09; shapes are the problem.</div>
<div class="co decision"><b>Rule</b> No retuning of the selection before calibration and systematics exist.</div>
</div>

<div class="st-source">Source: the selection hand-over note and the 2026-10-07 audit's rate/shape scan</div>

<!--
EXCLUSIVE_DECAY_HANDOFF_20261007.md "Result and physics limits"; artifacts/exclusive-final-audit-20261007/README.md, rate-shape-scan.json. HCAL mean unavailable for 9,383/26,631 H0 and 9,864/26,631 H1 data events (35.2 % / 37.0 %). Combined E/p 30,384 measured entries. 317 events per hemisphere invalid nearby-photon inputs; diphoton mass only with exactly two photons. Tails: 79 data events with visible mass > 100 GeV; 47 H0 / 32 H1 diphoton entries > 1 GeV. 220 scalar comparisons; no multiple-comparison correction, no systematics.
-->
