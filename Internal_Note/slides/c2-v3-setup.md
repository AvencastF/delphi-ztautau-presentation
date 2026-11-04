---
class: st pres c2
---

# Calibration 2 · Version 3: selection, a hidden 0.5 GeV floor, yields

<div class="st-sub">Version-2 leptons and acceptance; one HPC photon, MAIN energy above <LaTeX formula="T" /> = 0.5–3 GeV; isolation <LaTeX formula="d^2E\gt10" /> or <LaTeX formula="\ge5^\circ" />.</div>

<div class="st-cols st-cols-2" style="gap:14px">
<div>
<table class="c2t num first-nw">
<thead><tr><th>Raw cluster <LaTeX formula="E" /> [GeV]</th><th>0.3–0.5</th><th>0.5–1</th><th>1–2</th><th>3–6</th><th><LaTeX formula="\gt15" /></th></tr></thead>
<tbody><tr><td>MAIN / raw</td><td>1.68</td><td>1.44</td><td>1.23</td><td>1.07</td><td>0.99</td></tr></tbody>
</table>
<div class="co warn" style="margin-top:6px"><b>Hidden floor</b> Hard-coded raw <LaTeX formula="E\gt0.5" /> GeV kept 4,951 of 12,338 photons at MAIN 0.5–1 GeV.</div>
<div class="co ok"><b>Re-run</b> Saved skim, login node, no Slurm job.</div>
</div>
<div>
<table class="c2t num first-nw">
<thead><tr><th><LaTeX formula="T" /> = 0.5 GeV, <LaTeX formula="d^2E" /></th><th><LaTeX formula="ee\gamma" /> data / sim.</th><th><LaTeX formula="\mu\mu\gamma" /> data / sim.</th></tr></thead>
<tbody>
<tr><td>1992</td><td>835 / 934.9</td><td>1051 / 1019.5</td></tr>
<tr><td>1993</td><td>867 / 953.4</td><td>1025 / 1113.0</td></tr>
<tr><td>1994</td><td>1625 / 1753.1</td><td>2073 / 2181.8</td></tr>
<tr><td>1995</td><td>842 / 862.2</td><td>899 / 1049.6</td></tr>
<tr class="hl"><td>all</td><td>4169 / 4503.7</td><td>5048 / 5364.0</td></tr>
<tr><td>ratio, purity</td><td><LaTeX formula="0.926\pm0.015" />, 0.9998</td><td><LaTeX formula="0.941\pm0.014" />, 0.9998</td></tr>
</tbody>
</table>
<div class="co open" style="margin-top:6px"><b>Photon definition</b> 98-160 adds conversions, merged showers: about 20 % more. Unchanged.</div>
</div>
</div>

<div class="takeaway"><b>Takeaway</b> 0.5 GeV MAIN is the floor of the stored photons. Version 3: 9,217 data events (<LaTeX formula="3\times" /> version 2), purity 0.9998, rate 6–7 % low.</div>

<div class="st-source">Source: version-3 <LaTeX formula="\ell^+\ell^-\gamma" /> calibration report (2026-11-04), sections 2–4, and its yield table</div>

<!--
artifacts/llgamma-v3-20261104/REPORT.md (2026-11-04; source commit tau_analysis 45fb0ea, local = GitHub origin/main = NERSC checkout, file hashes verified; Opus subagent on the NERSC login node from the saved v2 skim, audited by the coordinating session; no Slurm job). Section 2: v2 skim region llg_presel_wide keeps photon_associations, the raw detector payload, leading-track indices, beam energy, thrust axis and every cut variable; recomputing single_photon.values and the v2 cut decisions reproduces all 20 v2 region bits in 1,747,712 rows and all 236,981 stored pass flags with zero mismatches; extraction 240 s / 0.7 GB, fits 668 s / 0.14 GB. Hidden floor: the photon working point hard-coded E_raw > 0.5 GeV on the cluster energy (v2's 3 GeV was the config cut photon_e3), keeping 4,951 of 12,338 photons with MAIN energy in (0.5, 1] GeV. MAIN/raw 1.68 at raw 0.3-0.5 GeV, 1.44 at 0.5-1, 1.23 at 1-2, 1.07 at 3-6, 0.99 above 15 GeV. PHOT records start at raw 0.300 GeV (MAIN ~ 0.48 GeV). New config key objects.photon_quality.hpc_energy_min_gev (default 0.5 = frozen working point; v3 sets 0); in a full production floor 0 also changes selected-photon counts and the pi/rho categories (e/mu categories do not use photons). Section 3: analysis/photon_quality.py resolved_hpc_pass(kind, profile, hpc_energy, hpc_energy_min); analysis/single_photon.py single_photon_main_energy (|p| of the photon MAIN particle), single_photon_main_e_over_epred, single_photon_isolation_d2e = min over the two leading tracks of (dphi^2 + dtheta^2/tan^2 theta_gamma) * E_MAIN [deg^2 GeV]; configs/analysis_llgamma_v3.yaml (20 regions: v2 cut lists, then llg_<ch>_e<T>_{d2e,iso5}, T = 0.5, 1, 2, 3 GeV on the MAIN energy). Section 4 selection: two tracks, one per hemisphere, opposite charge, 0.035 < |cos theta| < 0.72, vertex cuts, p/p_beam > 0.33, E_vis/sqrt(s) > 0.8; ee: ELID + HPC E/p >= 0.6 on both legs; mumu: MUID; exactly one PHOT/HPC candidate. Yields: tables.md "Yields per region" llg_eeg_e0p5_d2e 835/934.9 (0.893+-0.032), 867/953.4 (0.909+-0.033), 1625/1753.1 (0.927+-0.024), 842/862.2 (0.977+-0.036), all 4169/4503.7 (0.926+-0.015), purity 0.9998, Z_tautau 1.05 weighted events; llg_mumug_e0p5_d2e 1051/1019.5 (1.031+-0.034), 1025/1113.0 (0.921+-0.030), 2073/2181.8 (0.950+-0.022), 899/1049.6 (0.857+-0.030), all 5048/5364.0 (0.941+-0.014), purity 0.9998, Z_tautau 1.31. v2-like (3 GeV, 5 deg): eeg 1355/1405.0 (0.964+-0.027), mumug 2053/2079.9 (0.987+-0.023). Sample size (derived): 9,217 = 4,169 + 5,048; v2 final sample 3,097 (1,236 + 1,861, step 2b) -> 2.98x (eeg 3.4x, mumug 2.7x); against the v2-like regions of this run 9,217/3,408 = 2.7x. REPORT.md section 1 says "4-5x the v2 sample"; that factor is not reproduced from the yield tables, so the slide gives the derived 3x. Rate deficit 6-7 % at 0.5 GeV, 0.96-0.99 at 3 GeV, sits below 2 GeV of MAIN energy, not investigated, does not enter k. Photon definition (REPORT section 3, "Photon definition against DELPHI 98-160"): ours resolved HPC, MAIN code 1/11/61, exactly one owned HPC shower; theirs PXPHOT good codes (21/47; -1, -11, -21, -23, -24, -50, -51, -53, -61, -101) or E > 6 GeV with any code but -49; barrel single-candidate ee/mumu data: +725/+855 conversions (code 53), +169/+186 merged showers, +152/+91 other codes above 6 GeV on 5,377/6,194 working-point photons, about +20 %; conversions are 13-14 % of working-point photons in data, 18-19 % in MC. Not changed (code level).
-->
