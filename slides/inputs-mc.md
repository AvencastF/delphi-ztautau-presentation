---
class: st pres
---

# Simulation: seven processes, 1994 detector description

<div class="st-sub">Generator <LaTeX formula="\to" /> DELSIM/DELANA <LaTeX formula="\to" /> longDST <LaTeX formula="\to" /> EDM4hep, 1,000 events per chunk, 128 workers per node.</div>

<table class="num">
<thead><tr><th>Process</th><th>Generator · physics</th><th>Converted events</th><th><LaTeX formula="\sigma" /> [pb] (scan)</th></tr></thead>
<tbody>
<tr><td><LaTeX formula="Z\to\tau\tau" /> <span class="id">Z_tautau</span></td><td>PYTHIA 8.315, s-channel <LaTeX formula="\tau" /> pairs</td><td>608,400 + 2,440,800</td><td><LaTeX formula="1464.3\pm2.5" /></td></tr>
<tr><td><LaTeX formula="Z\to ee" /> <span class="id">Z_ee</span></td><td>PYTHIA 8.315, s-channel only</td><td>612,900</td><td><LaTeX formula="1468.7\pm2.5" /></td></tr>
<tr><td><LaTeX formula="Z\to\mu\mu" /> <span class="id">Z_mumu</span></td><td>PYTHIA 8.315</td><td>613,800</td><td><LaTeX formula="1472.8\pm2.5" /></td></tr>
<tr><td><LaTeX formula="Z\to q\bar q" /> <span class="id">Z_qq</span></td><td>PYTHIA 8.315, five flavours</td><td>2,528,099</td><td><LaTeX formula="30355.0\pm51.2" /></td></tr>
<tr><td><LaTeX formula="\gamma\gamma\to\ell\ell" /> <span class="id">yy_ll</span></td><td>PYTHIA 8.315, <LaTeX formula="Q^2\lt 1\,\mathrm{GeV}^2,\ W\ge 5\,\mathrm{GeV}" /></td><td>103,500</td><td><LaTeX formula="618.7\pm1.3" /></td></tr>
<tr><td><LaTeX formula="\gamma\gamma\to" /> hadrons <span class="id">yy_qq</span></td><td>PYTHIA 8.315, resolved–resolved only</td><td>927,000</td><td><LaTeX formula="5559.4\pm15.8" /></td></tr>
<tr><td>Bhabha <span class="id">Bhabha</span></td><td>BHWIDE 1.05, s + t + interference</td><td>3,920,397</td><td><LaTeX formula="18814.7\pm101.5" /></td></tr>
</tbody>
</table>

<div class="co warn" style="margin-top:10px"><b><LaTeX formula="Z\to ee" /> excluded</b> from every stack: it overlaps the Bhabha sample by construction.</div>

<div class="st-source">Source: the September-23 campaign publication receipt, the generator review and the sample list; weight ceilings and chunk counts in the notes</div>

<!--
Display precision on the slide: cross sections to 0.1 pb; full-precision values below, in SOURCES.md and tau_analysis/configs/1994.yaml.
long_production/docs/analysis-ready-1994-publication.json (files: Z_qq 2809, Z_ee 681, Z_mumu 682, Z_tautau 676, yy_qq 1030, yy_ll 115, Bhabha 4356; 10,349 valid chunks, 9,314,096 converted, 4 chunks no_output: 000021, 001791, 004461, 004631). tau-extra-20260923-v1: 2,712,000 generated, 2,440,800 derived (12,583,746 - 828,850 - 9,314,096). Generator weight ceilings (long_production/configs/catalog.json max_generated_event_weight): Z_tautau 0.025 (campaign sized under earlier 0.1), Z_qq 0.5, Z_ee 0.1, Z_mumu 0.1, yy_qq 0.25, yy_ll 0.25, Bhabha 0.2. Cross sections tau_analysis/configs/1994.yaml, scan job 58779300. Tune Monash 2013 (Tune:ee=7), lepton ISR/FSR on, no beam spread. Z_ll card disabled. GENERATOR_CONFIG_REVIEW.md: Bhabha leptons 5-175 deg, E>1 GeV.
-->
