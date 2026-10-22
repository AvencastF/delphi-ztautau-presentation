---
class: st pres
---

<script setup>
import NJUPlot from '../components/NJUPlot.vue'
</script>

# <LaTeX formula="\pi\pi" /> closure test at the full 1994 yield

<div class="st-sub">Half A builds the response, half B is fitted as data. <LaTeX formula="\sigma" /> = expected statistical error; pull = bias / <LaTeX formula="\sigma" />.</div>

<div class="fig-lead">
<div><div class="st-fig"><NJUPlot src="/figures/ml/v5/closure_v5.png" alt="closure bias and sigma per observable" /></div><div class="st-cap">Bias and <LaTeX formula="\sigma" /> per spin observable: ML v5, v4, v3, analytical</div></div>
<div>
<table class="num first-nw">
<thead><tr><th></th><th>ML v5</th><th>ML v3</th><th>analytical</th></tr></thead>
<tbody>
<tr><td><LaTeX formula="\sigma" /> range (15 obs.)</td><td><span class="best">0.149–0.322</span></td><td>0.150–0.314</td><td>0.249–0.719</td></tr>
<tr><td><LaTeX formula="\sigma" /> ratio to v5</td><td>1</td><td>0.87–1.04</td><td>1.32–2.36</td></tr>
<tr><td>largest |pull|</td><td>0.57</td><td>0.81</td><td>0.62</td></tr>
<tr><td>concurr. bias</td><td><LaTeX formula="+0.165\pm0.185" /></td><td><LaTeX formula="+0.155\pm0.234" /></td><td><LaTeX formula="-0.064\pm0.183" /></td></tr>
<tr><td>concurr. <LaTeX formula="\sigma" /></td><td><span class="best">0.684</span></td><td>0.661</td><td>1.026</td></tr>
</tbody>
</table>
<div class="co ok" style="margin-top:8px"><b>Takeaway</b> No v5 pull beyond 0.6; <LaTeX formula="\sigma" /> 1.3–2.4<LaTeX formula="\times" /> smaller than analytical.</div>
</div>
</div>

<div class="st-source">Source: closure table and figure of the v5 archive (all 15 observables in the appendix)</div>

<!--
artifacts/neutrino-ml-v5-20261021/closure_v5.md and closure_v5.png; fits under fits/, job 60080986. v5 largest pulls C_kk -0.56, B+_r -0.57, C_nn +0.55, C_kr -0.54; v4 B+_r -0.92 (sigma range 0.157-0.331, ratio 1.00-1.11); v3 B+_r -0.81; analytical B-_r -0.62. Concurrence = raw Wootters value of fitted coefficients, sigma one-at-a-time in quadrature; v4 +0.167 +- 0.211, sigma 0.724. MC error of the bias 0.04-0.08. The v3 concurrence sigma 0.661 is slightly smaller than v5 (0.684), consistent with its narrower pi-leg resolution.
-->
