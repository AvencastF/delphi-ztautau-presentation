---
class: st pres
---

# Ordered cuts 1–9: topology and tracking

<div class="st-sub">Bounds are strict unless marked <LaTeX formula="\le" />; an undefined variable fails. <LaTeX formula="d_0" />, <LaTeX formula="z_0" /> = impact parameters from the beam spot.</div>

<table class="lg">
<thead><tr><th>#</th><th>Cut</th><th>Requirement</th><th>Meaning</th></tr></thead>
<tbody>
<tr><td>1</td><td>Both hemispheres populated</td><td>true</td><td>at least one charged track on each side</td></tr>
<tr><td>2</td><td>Barrel acceptance</td><td><LaTeX formula="\lt 0.94" /></td><td>smaller <LaTeX formula="|\cos\theta|" /> of the two leading tracks</td></tr>
<tr><td>3</td><td>Low multiplicity</td><td><LaTeX formula="\le6" /></td><td>charged tracks in the event</td></tr>
<tr><td>4</td><td>Back-to-back isolation</td><td><LaTeX formula="\gt 160^\circ" /></td><td>smallest angle between an H0 and an H1 track</td></tr>
<tr><td>5</td><td>Longitudinal origin</td><td><LaTeX formula="\lt 45\,\mathrm{mm}" /></td><td>larger <LaTeX formula="|z_0|" /> of the leading tracks</td></tr>
<tr><td>6</td><td>Transverse origin</td><td><LaTeX formula="\lt 15\,\mathrm{mm}" /></td><td>larger <LaTeX formula="|d_0|" /> of the leading tracks</td></tr>
<tr><td>7</td><td>One track near the beam</td><td><LaTeX formula="\lt 3\,\mathrm{mm}" /></td><td>smaller <LaTeX formula="|d_0|" /> of the leading tracks</td></tr>
<tr><td>8</td><td>Common vertex in z</td><td><LaTeX formula="\lt 30\,\mathrm{mm}" /></td><td><LaTeX formula="|z_0(\mathrm{H0})-z_0(\mathrm{H1})|" /> of the leading tracks</td></tr>
<tr><td>9</td><td>Visible energy</td><td><LaTeX formula="\gt 8\,\mathrm{GeV}" /></td><td>energy sum of accepted charged and neutral particles</td></tr>
</tbody>
</table>

<div class="st-source">Source: the selection configuration file and the analysis code</div>

<!--
tau_analysis/configs/analysis_exclusive_decay.yaml (selection.cuts; region inclusive_1p1p). Config keys / code variables: 1 hemispheres / hemispheres equals 1; 2 acceptance / lead_abs_costheta_min max 0.94; 3 multiplicity / ncharged max 6 inclusive; 4 isolation / isolation min 160; 5 z_origin / lead_abs_z0_max max 45; 6 d_origin / lead_abs_d0_max max 15; 7 one_close / lead_abs_d0_min max 3; 8 relative_z / delta_z0 max 30; 9 energy / evis min 8. Semantics tau_analysis/analysis/config.py:154-161 (max/min strict unless inclusive: true). Definitions analysis/physics.py (variables): charged = accepted MAIN flag 0, track, |q|=1; evis = sum over accepted charged+neutral candidates, invalid if any unknown candidate.
-->
