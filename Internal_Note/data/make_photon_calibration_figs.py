"""Copy / convert the photon-calibration figures into public/figures/photon-calibration/ and collect the
chi2/dof values shown in the badges (data/photon-calibration/badges.json). PNG inputs are copied unchanged;
PDF inputs are rasterised with Ghostscript (png16m, 200 dpi; no SVG converter is installed on this Mac).
Writes data/photon-calibration/manifest.tsv (deck path, origin path, sha256 of the copy).
Run from the deck root: python3 data/make_photon_calibration_figs.py"""
import hashlib, json, os, shutil, subprocess, sys
A = '/Users/avencastmini/ZtautauLEP/artifacts'
OUT = 'public/figures/photon-calibration'
S2, S2B = f'{A}/rho-polarimeter-step2-20261102', f'{A}/rho-polarimeter-step2b-calibration-20261102'
V1, V2 = f'{A}/llgamma-selection-20261103', f'{A}/llgamma-v2-20261103'
V3 = f'{A}/llgamma-v3-20261104'
figs = []  # (deck path, origin)
for f in ['mgg_by_year_pair', 'ptau_before_after', 'scale_functions_and_efficiency']:
    figs.append((f'step2b/{f}.png', f'{S2B}/plots/{f}.png'))
for v in ['e_pi0_usable', 'cos_star_merged', 'v_k_cone_usable', 'n_cand_usable']:
    figs.append((f'step2b/before-datamc_{v}.png', f'{S2}/plots-full/datamc_{v}.png'))
    figs.append((f'step2b/after-datamc_{v}.png', f'{S2B}/plots-calibrated/datamc_{v}.png'))
V1_PLOTS = [('llg_eeg_gh0', 'photon_candidate_energy'), ('llg_mumug_gh0', 'photon_candidate_energy'),
            ('llg_eeg', 'photonid_candidate_nearest_track_angle_hemi0'), ('llg_mumug', 'photonid_candidate_nearest_track_angle_hemi0'),
            ('llg_eeg', 'lead_hpc_e_over_p_hemi0'), ('llg_eeg', 'lead_hpc_e_over_p_hemi1'),
            ('llg_eeg', 'evis_over_ecm'), ('llg_mumug', 'evis_over_ecm')]
for reg, var in V1_PLOTS:
    figs.append((f'v1/{reg}-{var}.png', f'{V1}/plots/{reg}-selected-{var}-rate_lin.pdf'))
V2_MAIN = [('llg_eeg_iso5', 'single_photon_e_over_epred'), ('llg_mumug_iso5', 'single_photon_e_over_epred'),
           ('llg_mumug_iso5', 'single_photon_epred'), ('llg_eeg_iso5', 'single_photon_hpc_module_distance'),
           ('llg_eeg_iso5', 'single_photon_energy'), ('llg_mumug_iso5', 'single_photon_energy'),
           ('llg_eeg_iso5', 'single_photon_track_angle_min'), ('llg_mumug_iso5', 'single_photon_track_angle_min'),
           # added 2026-11-03b (calibration-2 rewrite, step 2c): final-selection electron E/p and visible energy
           ('llg_eeg_iso5', 'lead_hpc_e_over_p_hemi0'), ('llg_eeg_iso5', 'evis_over_ecm'), ('llg_mumug_iso5', 'evis_over_ecm')]
V2_REGIONS = [(f'llg_{ch}_{s}', 'single_photon_e_over_epred') for ch in ('eeg', 'mumug')
              for s in ('iso20', 'iso15', 'iso10', 'iso10_2nd', 'iso10_e2', 'iso10_e1p5')]
V2_YEARS = [(f'llg_{ch}_{s}', y) for ch in ('eeg', 'mumug') for s in ('iso5', 'iso10') for y in (1992, 1993, 1994, 1995)]
for reg, var in V2_MAIN + V2_REGIONS:
    figs.append((f'v2/{reg}-{var}.png', f'{V2}/plots/llgamma-v2-{reg}/{reg}-selected-{var}-rate_lin.pdf'))
for reg, y in V2_YEARS:
    figs.append((f'v2/year-{y}/{reg}-single_photon_e_over_epred.png',
                 f'{V2}/plots/llgamma-v2-{reg}/year-{y}/{reg}-selected-single_photon_e_over_epred-rate_lin.pdf'))
for f in ['study/peak_ratio_vs_cuts.png', 'epred/k_vs_epred_iso5.png', 'epred/k_per_point.png', 'epred/width_ratio_vs_epred_iso5.png']:
    figs.append((f'v2/{os.path.basename(f)}', f'{V2}/{f}'))
# added 2026-11-03b: before/after closure of the l+l-gamma scale (artifacts/llgamma-v2-20261103/closure/REPORT.md)
for f in ['closure_R_comb', 'closure_R_eeg', 'closure_R_mumug', 'k_after_vs_epred']:
    figs.append((f'closure/{f}.png', f'{V2}/closure/{f}.png'))
# added 2026-11-03c: before/after R in the pipeline plot style (closure/after_plots/REPORT.md) and the
# photon-energy coverage of the rho-leg pi0 (rho-polarimeter-step2-20261102/photon_energy_coverage/REPORT.md)
for f in ['R_comb_years_summary', 'R_eeg_all', 'R_mumug_all', 'R_comb_all']:
    figs.append((f'closure/after-{f}.png', f'{V2}/closure/after_plots/{f}.png'))
for f in ['photon_energy_spectrum', 'pi0_energy_spectrum', 'true_energy_spectrum']:
    figs.append((f'coverage/{f}.png', f'{S2}/photon_energy_coverage/{f}.png'))
# added 2026-11-04: version-3 l+l-gamma calibration (MAIN energy, 0.5 GeV, DELPHI d2E isolation;
# llgamma-v3-20261104/REPORT.md); chi2/dof of the data/MC badges are in its tables.md (no agreement.json copied locally)
for f in ['datamc_llg_eeg_e0p5_d2e', 'datamc_llg_mumug_e0p5_d2e', 'k_fit_vs_epred', 'width_ratio_fit_vs_epred',
          'resolution_excess_variance']:
    figs.append((f'v3/{f}.png', f'{V3}/figures/{f}.png'))
# added 2026-11-05: final pi0 step of the stored calibration v3 (pi0-final-calib-20261104/CALIBRATION_V3_REPORT.md)
# and the rho-leg closure of the v3 production skim (rho-closure-20261104/CLOSURE_REPORT.md, v3 section)
P3, RC3 = f'{A}/pi0-final-calib-20261104', f'{A}/rho-closure-20261104/v3'
for f in ['k_years_v3', 'smear_v3', 'closure_odd_summary', 'mgg_odd_closure_AB']:
    figs.append((f'pi0-v3/{f}.png', f'{P3}/figures/{f}.png'))
for f in ['mgg_pair_before_after', 'summary_ratios']:
    figs.append((f'rho-closure-v3/{f}.png', f'{RC3}/figures/{f}.png'))

rows = []
for dst, src in figs:
    out = f'{OUT}/{dst}'
    os.makedirs(os.path.dirname(out), exist_ok=True)
    if src.endswith('.png'):
        shutil.copyfile(src, out)
    else:
        subprocess.run(['gs', '-q', '-dNOPAUSE', '-dBATCH', '-dSAFER', '-sDEVICE=png16m', '-r200',
                        '-dTextAlphaBits=4', '-dGraphicsAlphaBits=4', f'-sOutputFile={out}', src], check=True)
    size = os.path.getsize(out)
    assert size < 2_000_000, (out, size)
    rows.append((dst, src, hashlib.sha256(open(out, 'rb').read()).hexdigest(), hashlib.sha256(open(src, 'rb').read()).hexdigest()))
os.makedirs('data/photon-calibration', exist_ok=True)
with open('data/photon-calibration/manifest.tsv', 'w') as fh:
    fh.write('deck_path\torigin\tsha256_copy\tsha256_origin\n')
    for r in rows: fh.write('\t'.join(r) + '\n')

# chi2/dof for the badges ('Total MC', Gaussian chi2 with data variance and finite-MC sumw2, as stored by the renderer)
badges = {}
v1 = json.load(open(f'{V1}/agreement_table.json'))['regions']
for reg, var in V1_PLOTS:
    a = v1[reg]['variables'][var]['all']
    badges[f'v1/{reg}/{var}'] = {k: a[k] for k in ('chi2', 'dof', 'p_value', 'small_expected_bins', 'status')}
def v2a(reg, year=None):
    p = f'{V2}/plots/llgamma-v2-{reg}/' + (f'year-{year}/' if year else '') + 'agreement.json'
    return json.load(open(p))['comparisons']
for reg, var in V2_MAIN + V2_REGIONS:
    a = v2a(reg).get(var, {}).get('Total MC')
    badges[f'v2/{reg}/{var}'] = a and {k: a.get(k) for k in ('chi2', 'dof', 'p_value', 'small_expected_bins', 'status')}
for reg, y in V2_YEARS:
    a = v2a(reg, y).get('single_photon_e_over_epred', {}).get('Total MC')
    badges[f'v2/{reg}/year-{y}/single_photon_e_over_epred'] = a and {k: a.get(k) for k in ('chi2', 'dof', 'p_value', 'small_expected_bins', 'status')}
json.dump(badges, open('data/photon-calibration/badges.json', 'w'), indent=1)
print(len(rows), 'figures;', len(badges), 'badges')
