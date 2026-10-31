---
class: st pres
---

# Three fit models on identical pseudo-data: why the final one

<div class="st-sub">Combined 1992–1995, ML reconstruction. Same simulated events, same pseudo-experiments.</div>

<table class="lg">
<thead><tr><th>Model</th><th>Closure on injected states</th><th>Error validity (pull widths)</th><th>Witness <LaTeX formula="Z" /></th><th>Bell <LaTeX formula="Z" /></th></tr></thead>
<tbody>
<tr><td>Legacy forward folding</td><td>biased: cross-talk up to <LaTeX formula="0.58\,\sigma" /></td><td>0.975–1.027</td><td>6.88</td><td>2.21</td></tr>
<tr><td>Reweighted, Poisson per histogram</td><td>exact</td><td><span class="tag open">invalid</span> up to 2.3</td><td>5.14</td><td>1.68</td></tr>
<tr class="hl"><td>Reweighted, full covariance</td><td>exact</td><td>0.972–1.026</td><td>7.00</td><td>2.22</td></tr>
</tbody>
</table>

<div class="st-cols st-cols-3" style="margin-top:14px">
<div class="co warn"><b>Legacy</b> Fixed yields and response at the reference: spin-dependent acceptance leaks between coefficients.</div>
<div class="co warn"><b>Poisson</b> Each event counted up to 15 times: errors look small, real spread is larger.</div>
<div class="co ok"><b>Final</b> Exact, valid errors, 1–6 % smaller than legacy on 13 of 15.</div>
</div>

<div class="st-source">Source: model comparison of 2026-10-31 (legacy, Poisson-template and full-covariance models), combined 1992–1995; simulation only, statistics only</div>

<!--
artifacts/joint-fit-20261031/modelC/combined-ml/summary.md (A/B/C table, W and Bell tests), modelB/combined-ml/summary.md, step2/combined-ml/summary.md. Model names: A = legacy ForwardFoldingProcessor (as reproduced by joint_fit), B = MC-reweighted linear templates with product Poisson likelihood over the 15 histograms, C = B's templates with GLS and the full bin-to-bin covariance (owner decision 2026-10-31: target model). Closure: A on step-2 pseudo-data fitted/injected C_kk 0.96-1.01, B_Ak 1.09, cross-talk up to 0.58 sigma_A at c0(W) (B_Ak) and 0.23 sigma at C_kk +-2 sigma; C on its own pseudo-data 2.9e-12 sigma_A over 20 points. Pulls: A step-1 toys 0.975-1.027; B 2.29 (C_kk), 2.16/2.13 (B_Ak/B_Bk) in 1994, C_diag 2.19-2.26 combined; C 0.972-1.026 (2000 SM toys). Calibrated Z(q_A) witness: A 6.877, B 5.141, C 7.002; Bell A 2.206, B 1.680, C 2.215 (Z_A 2.219, toy count 2.22). sigma_C/sigma_A (HESSE) 0.936-0.988 for 13 coefficients, C_nr 1.066 / C_rn 1.065 (genuine C_nr-C_rn correlation -0.35 that A ignores). Witness Z values are extrapolations beyond the toy range (0/20000 or 0/40000 null toys reach q_A).
-->
