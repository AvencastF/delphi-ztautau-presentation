---
class: st pres
---

# Machine learning, 1992–1995: what is established, what is open

<div class="st-cols st-cols-2">
<div>
<div class="co ok"><b>Classifier</b> Accuracy 0.88 in every year, cut-based 0.39–0.42.</div>
<div class="co ok"><b>Neutrino</b> Correct branch 0.72, best possible 0.91, analytical 0.59.</div>
<div class="co ok"><b>1994</b> At least as good as the 1994-only models.</div>
<div class="co warn"><b>1992–1993</b> Weaker direction: no vertex-detector z readout.</div>
</div>
<div>
<div class="co open"><b>Data/MC</b> 1994 <LaTeX formula="\rho" /> channels 0.94; 1992 <LaTeX formula="\pi\pi" /> 1.24; 1995 <LaTeX formula="ee" /> 0.85.</div>
<div class="co open"><b>Inputs</b> Neutral-shower inputs mismodelled in 1992 and 1995.</div>
<div class="co open"><b>Acceptance</b> Owner checkpoint review; per-point data/MC views.</div>
<div class="co decision"><b>Fits</b> Use the hold half only.</div>
</div>
</div>

<div class="st-source">Source: all-years machine-learning record (2026-10-27) and the project guide (all-years ML, EveNet-Align commit of 2026-10-30)</div>

<!--
artifacts/ml-all-years-v1-20261027/README.md: classifier accuracy 0.875-0.887 per year (cut-based 0.385-0.416); neutrino branch accuracy all years 0.724 (analytical 0.591, best 0.910); 1994 slightly better than v5 on every leg (pi 0.81 vs 0.89 deg) and in branch accuracy (0.746 vs 0.740); 1992/1993 worse (no VD z). Data/MC (ML selection): 1994 rho channels 0.94, 1992 pipi 1.24 +- 0.08, 1995 ee 0.85 +- 0.04 ("inputs/normalisation effects to be understood before acceptance (photon calibration item)", PROJECT_GUIDE 2026-10-27). Not done: owner checkpoint acceptance, per-point views. EveNet-Align b5cc2c2 on Ztautau-dev committed and pushed 2026-10-30, NERSC checkout fast-forwarded. Neutral-shower inputs (erad_over_ebeam, EMNC energies) kept in this first training (PROJECT_GUIDE 2026-10-27). The 2026-10-22 verdict on the 1994-only models is in the appendix ("1994 reference").
-->
