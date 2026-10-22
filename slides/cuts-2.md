---
class: st pres
---

# Ordered cuts 10–18: published-preselection cuts, radiative vetoes, neutrals

<div class="st-sub">Cuts 11–15 follow the DELPHI paper's neural-network preselection; HPC = barrel electromagnetic calorimeter.</div>

<table class="lg">
<thead><tr><th>#</th><th>Cut</th><th>Requirement</th><th>Meaning</th></tr></thead>
<tbody>
<tr><td>10</td><td>Visible transverse momentum</td><td>&gt; 0.4 GeV</td><td>|Σ p⃗_T| of the visible particles</td></tr>
<tr><td>11</td><td>Eligible single-prong hemisphere</td><td>≥ 1</td><td>one-track side with leading |cos θ| &lt; 0.732</td></tr>
<tr><td>12</td><td>Acollinearity</td><td>&gt; 0.5°</td><td>leading tracks not exactly back to back</td></tr>
<tr><td>13</td><td>Calorimeter-boundary evidence</td><td>pass</td><td>HPC crossing info present when PEmax &gt; 0.8 E_beam</td></tr>
<tr><td>14</td><td>PEmax veto, unknown kept</td><td>pass</td><td>fails only on an explicit veto</td></tr>
<tr><td>15</td><td>One track on each side</td><td>true</td><td>exactly one charged track per hemisphere</td></tr>
<tr><td>16</td><td>Radiative EM energy</td><td>&lt; 1 E_beam</td><td>quadrature sum of cone shower energies</td></tr>
<tr><td>17</td><td>Radiative momentum</td><td>&lt; 1 p_beam</td><td>√(p₁² + p₂²) of the leading tracks</td></tr>
<tr><td>18</td><td>Neutral multiplicity</td><td>≤ 3 per side</td><td>reconstructed neutrals; missing count fails</td></tr>
</tbody>
</table>

<div class="st-source">Source: the selection configuration file, the paper-preselection code and the neutral-baseline code</div>

<!--
Config keys / variables: 10 transverse / pt min 0.4; 11 nn_one_prong / nn_eligible_count min 0 (strict, i.e. >0); 12 nn_acol / nn_acol_pass equals 1 (acollinearity > 0.5 deg for 1-1 topology, other known topologies pass); 13 nn_boundary_no_pe / nn_boundary_no_pe_pass equals 1 ("HPC boundary decision without PEmax veto"; deferred when PEmax unknown); 14 nn_pe_keep_unknown / nn_keep_unknown_pass equals 1; 15 nn_is_1p1p / nn_is_1p1p equals 1; 16 exclusive_erad / erad_over_ebeam max 1 (EMNC cone energies, quadrature, / E_beam); 17 exclusive_prad / prad_over_pbeam max 1 (p_beam = sqrt(E_beam^2 - m_e^2)); 18 neutral_hemisphere_limit / neutral_hemisphere_all_count_max max 3 inclusive (analysis/neutral_baseline.py; owner decision 2026-10-09; no muon-specific neutral rule; supersedes the 2026-10-07 rule). Code: analysis/paper_nn.py lines 127-158, analysis/physics.py. Saved output: inclusive region defines the skim incl. residual/conflict; every Z_tautau row saved with region_mask; bit 0 = inclusive_1p1p.
-->
