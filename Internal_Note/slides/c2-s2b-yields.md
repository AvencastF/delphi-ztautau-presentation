---
class: st pres c2
---

# Calibration 2 · Step 2b: yields per year and purity

<div class="st-sub">Final selection. Simulation = signal process plus <LaTeX formula="Z\to\tau\tau" />, luminosity-weighted; ratio with statistical error. Luminosity uncertified.</div>

<table class="c2t num first-nw">
<thead><tr><th>Year</th><th><LaTeX formula="ee\gamma" /> data / sim.</th><th>Ratio</th><th><LaTeX formula="\mu\mu\gamma" /> data / sim.</th><th>Ratio</th><th><LaTeX formula="Z\to\tau\tau" /> in sim. [%]: <LaTeX formula="ee\gamma" /> / <LaTeX formula="\mu\mu\gamma" /></th></tr></thead>
<tbody>
<tr><td>1992</td><td>217 / 244.6</td><td><LaTeX formula="0.887\pm0.063" /></td><td>363 / 373.1</td><td><LaTeX formula="0.973\pm0.054" /></td><td>0.024 / 0.028</td></tr>
<tr><td>1993</td><td>274 / 277.9</td><td><LaTeX formula="0.986\pm0.063" /></td><td>399 / 403.8</td><td><LaTeX formula="0.988\pm0.052" /></td><td>0.013 / 0.026</td></tr>
<tr><td>1994</td><td>477 / 502.8</td><td><LaTeX formula="0.949\pm0.045" /></td><td>762 / 750.2</td><td><LaTeX formula="1.016\pm0.039" /></td><td>0.016 / 0.025</td></tr>
<tr><td>1995</td><td>268 / 251.7</td><td><LaTeX formula="1.065\pm0.069" /></td><td>337 / 354.1</td><td><LaTeX formula="0.952\pm0.054" /></td><td>0.014 / 0.010</td></tr>
<tr class="hl"><td>All</td><td>1,236 / 1,277.1</td><td><LaTeX formula="0.968\pm0.029" /></td><td>1,861 / 1,881.2</td><td><LaTeX formula="0.989\pm0.024" /></td><td>0.017 / 0.023</td></tr>
</tbody>
</table>

<div class="st-cols st-cols-2" style="margin-top:10px">
<div class="co ok"><b>Purity</b> <span class="tag sim">sim</span> <LaTeX formula="Z\to q\bar q" />, two-photon and cross-channel: zero events in every year.</div>
<div class="co ok"><b>Rates</b> Every per-year ratio within <LaTeX formula="1.8\sigma" /> of 1; not a calibration input.</div>
</div>

<div class="takeaway"><b>Takeaway</b> 3,097 data events in all, essentially pure (<LaTeX formula="Z\to\tau\tau" /> below 0.05 %, nothing else), with rates as simulated in every year and channel.</div>

<div class="st-source">Source: yield table and count table of the version-2 <LaTeX formula="\ell^+\ell^-\gamma" /> run, isolation <LaTeX formula="\ge5^\circ" /> regions</div>

<!--
artifacts/llgamma-v2-20261103/tables/yields.md (= REPORT.md section 6; rates-by-group region_events, data events / Total MC (Z_ee excluded) weighted, ratio +- stat), regions llg_eeg_iso5 and llg_mumug_iso5. Process split from cutflows/cutflow.csv (cut photon_iso5, cumulative sumw): eeg Bhabha 244.5908 / 277.8475 / 502.7602 / 251.6919 (all 1,276.8903), Z_tautau 0.0586 / 0.0353 / 0.0818 / 0.0352 (0.2109); mumug Z_mumu 372.9773 / 403.7137 / 750.0109 / 354.1073 (all 1,880.8092), Z_tautau 0.1054 / 0.1057 / 0.1870 / 0.0352 (0.4333). Z_tautau share [%] = Z_tautau / Total MC x 100 (derived): eeg 0.024 / 0.013 / 0.016 / 0.014 / 0.017; mumug 0.028 / 0.026 / 0.025 / 0.010 / 0.023. Z_qq, yy_ll, yy_qq, and Bhabha in mumug / Z_mumu in eeg: 0 rows. Z_ee (overlaps Bhabha, not stacked) sumw in eeg iso5: 202.63 / 218.42 / 431.94 / 206.79. Total 3,097 = 1,236 + 1,861 (derived). Largest per-year deviation: eeg 1992 (1 - 0.887) / 0.063 = 1.8 sigma (derived). Luminosities user-supplied, uncertified; rates are not used by the calibration (k is a peak-position ratio).
-->
