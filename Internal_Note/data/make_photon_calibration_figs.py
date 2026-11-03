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
           ('llg_eeg_iso5', 'single_photon_track_angle_min'), ('llg_mumug_iso5', 'single_photon_track_angle_min')]
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
