---
class: st pres
---

# Known residual disagreements, recorded and not tuned away

<div class="st-sub">All years together unless a year is named; absolute comparison, statistical only, diagnostic.</div>

<table class="lg">
<thead><tr><th>Variable</th><th>Where</th><th>Size (<LaTeX formula="\chi^2/\mathrm{dof}" />)</th><th>Reason on record</th></tr></thead>
<tbody>
<tr><td>Hadron-calorimeter mean per layer</td><td>inclusive H0 / H1</td><td><span class="badge r">384 / 60</span> <span class="badge r">682 / 60</span></td><td>response mismodelled, every year</td></tr>
<tr><td>Hadron-source category</td><td>inclusive H0 / H1</td><td><span class="badge r">549 / 7</span> <span class="badge r">898 / 7</span></td><td>follows from the calorimeter; feeds hadron ID</td></tr>
<tr><td>Photon-pair mass near a track</td><td>1992 · 1994 · 1995, H1</td><td><span class="badge r">999 / 50</span> <span class="badge a">77 / 50</span> <span class="badge r">645 / 50</span></td><td>neutral showers mismodelled in 1992 and 1995</td></tr>
<tr><td>Radiative EM energy</td><td>1992 · 1994 · 1995</td><td><span class="badge r">188 / 20</span> <span class="badge r">65 / 20</span> <span class="badge r">61 / 20</span></td><td>same neutral-shower issue</td></tr>
<tr><td>Leading-track <LaTeX formula="p/p_\mathrm{beam}" />, <LaTeX formula="\cos\theta" /></td><td>inclusive H0</td><td><span class="badge a">74 / 42</span> <span class="badge a">102 / 37</span></td><td>mild; includes the 1.8 % rate deficit</td></tr>
<tr><td>Pion-channel composition</td><td><LaTeX formula="\pi\pi" />, <LaTeX formula="\pi\rho" />, <LaTeX formula="e\pi" />, <LaTeX formula="\mu\pi" /></td><td>matching 0.17–0.43</td><td><LaTeX formula="\rho" /> with unidentified photons taken as <LaTeX formula="\pi" /></td></tr>
</tbody>
</table>

<div class="st-cols st-cols-2" style="margin-top:10px">
<div class="co open"><b>Neutrals</b> 1992 and 1995 photon variables need calibration first.</div>
<div class="co decision"><b>Rule</b> No retuning of the selection before calibration and systematics exist.</div>
</div>

<div class="st-source">Source: agreement tables of the 1992–1995 plots (job 60340876), inclusive and per year; project guide (2026-10-26/27)</div>

<!--
chi2/dof from data/nersc-all-years-rq-20261026/plots/all-years-baseline/agreement.json (all years) and year-YYYY/agreement.json ("Total MC", Gaussian chi2 with data variance and finite-MC sumw2, absolute normalisation). Exact: hcal_mean H0 384.0/60, H1 682.0/60 (1994 439.7 / 861.9; 1992 762.6 / 539.8; 1995 651.6 / 919.6); hadron_source H0 549.3/7, H1 898.2/7; nearby_diphoton_mass H1 1992 998.5/50, 1994 76.8/50, 1995 645.1/50 (H0 700.6 / 68.4 / 557.0; all years H0 113.8, H1 143.0); erad_over_ebeam all 182.9/20, 1992 188.3, 1994 65.4, 1995 60.7; leadtrack_hemi0_p_over_pbeam 73.9/42, hemi1 101.8/42; leadtrack_hemi0_costheta 102.2/37, hemi1 99.3/37; visible_tautau_mass 129.1/49. Badge thresholds per dof as elsewhere (76.8/50 = 1.54 -> amber). Neutral counts and E/p: no independent-bin chi2 (correlated entries). Matching fractions: confusion slide (pipi 0.173, pirho 0.328, epi 0.423, mupi 0.429).
docs/PROJECT_GUIDE.md 2026-10-27: "the neutral-shower inputs (erad_over_ebeam, EMNC energies) that the 2026-10-26 plots show mismodelled in 1992 and the 1995 peak period stay in the inputs for this first training". Rate deficit all years 0.982 (1.8 %). The 2026-10-22 version listed the 1994-only values of the 2026-10-07 audit (HCAL 364.9 / 501.8 per 59 dof).
-->
