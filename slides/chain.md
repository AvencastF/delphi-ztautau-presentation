---
class: st pres
clicks: 5
---

<script setup>
import ChainFlow from '../components/ChainFlow.vue'
</script>

# The 1994 chain: five stages, four file hand-overs

<div class="st-sub">Click through. Each stage reads the previous stage's files on NERSC.</div>

<ChainFlow :step="$clicks" />

<div class="legend"><span class="tag data">data</span> archived DELPHI events · <span class="tag sim">simulation</span> our own Monte Carlo · <span class="tag sel">selection</span> cuts and decay identification · <span class="tag ml">ML</span> EveNet models · <span class="tag decision">decision</span> owner choice · <span class="tag open">open</span> not established</div>

<ul class="bl" style="margin-top:4px; font-size:12.5px">
<li><b>Code:</b> <a href="https://github.com/AvencastF/delphi-sim-pipeline/tree/feature/nersc-long-production">simulation pipeline</a>, <a href="https://github.com/AvencastF/delphi-edm4hep/tree/3e40698">converter</a>, <a href="https://github.com/AvencastF/delphi-ztautau-ana">analysis</a>, <a href="https://github.com/UW-EPE-ML/EveNet-Align">EveNet-Align</a></li>
<li><b>Formats:</b> longDST (DELPHI summary tape) <LaTeX formula="\to" /> EDM4hep ROOT <LaTeX formula="\to" /> Parquet tables</li>
</ul>

<div class="st-source">Source: the 1994 runbook, chain overview and identity table</div>

<!--
docs/RUNBOOK_1994.md sections 0-4 and 7. Stage 1: long_production (no git) + delphi-sim-pipeline branch feature/nersc-long-production revision 8168fd7; frozen build builds/tau-extra-20260923-v1 (sim 290537a, converter 3e40698); campaigns prod-20260923-v1 (9,314,096 events) and tau-extra-20260923-v1 (2,440,800 derived). Stage 2: delphi-edm4hep 3e40698, 132 files / 828,850 events. Stage 3: tau_analysis revision 7e28092, job 59709781, frozen run all-event-detector-1994-20261012 (3,085,534 rows, 46.4 GB, 513 columns). Stage 4: EveNet-Align branch Ztautau-dev HEAD c248cb0 + uncommitted v4/v5; classifier v1 epoch 29; neutrino v5 jobs 60075055/60075238/60079489/60080986; output skim-cls-nu-v5. Container docker.io/jingyucms/delphi-sim@sha256:bc8a844b..., key4hep 2026-04-08. Project directory /pscratch/sd/a/avencast/Ztautau. The analysis and EveNet-Align repositories returned HTTP 404 anonymously on 2026-10-23; links point at repository roots.
-->
