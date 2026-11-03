---
class: st pres
---

# Appendix · photon calibration: <LaTeX formula="\chi^2" /> of selection v2 (excerpt)

<div class="st-sub">Pipeline statistical <LaTeX formula="\chi^2/\mathrm{dof}" /> against the total simulation. For <LaTeX formula="R" />, 73–95 of 100 bins have small expectation: not a shape-quality number without rebinning.</div>

<table class="sm num first-nw">
<thead><tr><th>Region</th><th><LaTeX formula="R" />, all</th><th>1992</th><th>1993</th><th>1994</th><th>1995</th><th><LaTeX formula="E_\mathrm{pred}" />, all</th><th><LaTeX formula="E_\gamma" />, all</th></tr></thead>
<tbody>
<tr><td><span class="id">eeg_iso20</span></td><td>235/97</td><td>194/79</td><td>214/81</td><td>241/82</td><td>198/78</td><td>75/44</td><td>56/39</td></tr>
<tr><td><span class="id">eeg_iso10</span></td><td>237/97</td><td>213/86</td><td>227/87</td><td>299/89</td><td>191/83</td><td>71/47</td><td>58/39</td></tr>
<tr><td><span class="id">eeg_iso5</span></td><td>233/97</td><td>228/91</td><td>265/90</td><td>291/91</td><td>245/91</td><td>85/47</td><td>56/39</td></tr>
<tr><td><span class="id">eeg_iso10_e1p5</span></td><td>244/99</td><td>223/93</td><td>230/92</td><td>232/95</td><td>200/87</td><td>81/47</td><td>62/41</td></tr>
<tr><td><span class="id">mumug_iso20</span></td><td>147/83</td><td>170/61</td><td>145/64</td><td>139/72</td><td>212/70</td><td>42/40</td><td>32/39</td></tr>
<tr><td><span class="id">mumug_iso10</span></td><td>189/95</td><td>184/72</td><td>174/73</td><td>122/83</td><td>212/75</td><td>47/46</td><td>36/39</td></tr>
<tr><td><span class="id">mumug_iso5</span></td><td>241/97</td><td>167/81</td><td>225/85</td><td>164/93</td><td>197/87</td><td>58/47</td><td>29/39</td></tr>
<tr><td><span class="id">mumug_iso10_e1p5</span></td><td>184/98</td><td>221/88</td><td>181/87</td><td>169/93</td><td>176/86</td><td>45/46</td><td>38/41</td></tr>
<tr><td><span class="id">mumug_wide_iso10</span></td><td>204/95</td><td>128/76</td><td>177/78</td><td>136/84</td><td>225/78</td><td>57/46</td><td>38/40</td></tr>
</tbody>
</table>


<div class="st-source">Source: version-2 <LaTeX formula="\ell^+\ell^-\gamma" /> study report, section 5 (from the pipeline agreement files); full table in the study folder</div>

<!--
Run llgamma-v2-20261103: NERSC /pscratch/sd/a/avencast/Ztautau/analysis-runs/1992_1993_1994_1995/llgamma-v2-20261103, job 60747968 (coordinator brief), tau_analysis 5ac249d (configs/analysis_llgamma_v2.yaml, configs/plotting_llgamma_v2.yaml, analysis/single_photon.py); study artifacts/llgamma-v2-20261103/REPORT.md, peak_fits.json, tables/yields.md, tables/chi2_table.md, epred/REPORT.md, epred/k_epred.json (NERSC login node, light python only). REPORT.md section 5 (= tables/chi2_table.md, built from plots/llgamma-v2-<region>/agreement.json and year-*/agreement.json, 'Total MC', Gaussian chi2 with data variance and finite-MC sumw2, statistical only, within-event cross-bin covariance omitted). All R entries p < 0.001; E_pred all-years p < 0.001 only for eeg_iso5; E all-years none. Full table: 37 variables x 13 regions x 5 groups (tables/chi2_table.md/.json). Variables with p < 0.001 per region listed in REPORT.md section 5 (e.g. llg_eeg_iso5: acollinearity, evis_over_ecm, neutral_candidate_count_sum, neutral_constituent_energy_hemi0/1, neutral_constituent_phi_hemi1, photonid_candidate_nearest_track_angle_hemi1, single_photon_e_over_epred, single_photon_epred, single_photon_track_angle_min).
-->
