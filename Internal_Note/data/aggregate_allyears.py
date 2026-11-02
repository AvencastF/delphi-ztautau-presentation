"""Aggregate the 1992-1995 run-quality rerun (all-years-rq-20261026) count tables for the cutflow chapter.
Inputs (copied from NERSC, sha256 in public/figures/MANIFEST.md / SOURCES.md):
  data/nersc-all-years-rq-20261026/cutflows/cutflow.csv, exclusive_confusion.csv
Output: data/nersc-all-years-rq-20261026/aggregated.md (milestones per year, children per year, composition table).
Signed MC = sum of sumw over MC samples except Z_ee (overlaps Bhabha). Usage: python3 data/aggregate_allyears.py
"""
import csv, collections
B = 'data/nersc-all-years-rq-20261026/'
YEARS = ['1992', '1993', '1994', '1995']
CH = ['ee', 'emu', 'epi', 'erho', 'mumu', 'mupi', 'murho', 'pipi', 'pirho', 'rhorho']
agg = collections.defaultdict(lambda: collections.defaultdict(float))
tau = collections.defaultdict(lambda: collections.defaultdict(float))
order = []
for r in csv.DictReader(open(B + 'cutflows/cutflow.csv')):
    if r['kind'] != 'cumulative':
        continue
    year, rest = r['sample'].split('/', 1)
    key = (r['region'], r['cut'])
    if key not in order:
        order.append(key)
    if rest == 'data':
        agg[key][(year, 'data')] += int(r['n'])
    elif rest.startswith('Total MC') or rest.startswith('Z_ee/'):
        continue
    else:
        agg[key][(year, 'mc')] += float(r['sumw'])
        if rest.startswith('Z_tautau_'):
            agg[key][(year, 'tau')] += float(r['sumw'])
out = ['# Aggregated count tables, all-years-rq-20261026 (job 60333695)', '',
       'Data = events after run selection (status 0 + run quality); MC = signed sumw, Z_ee excluded. Derived ratios.', '']
out += ['## Cumulative counts per year (every cut, inclusive region)', '', '| cut | ' + ' | '.join(f'{y} data | {y} MC | {y} ratio' for y in YEARS + ['all']) + ' |', '|---|' + '---:|' * 15]
for (reg, cut) in order:
    if reg != 'inclusive_1p1p':
        continue
    a = agg[(reg, cut)]; cells = []
    for y in YEARS + ['all']:
        dn = sum(a[(yy, 'data')] for yy in YEARS) if y == 'all' else a[(y, 'data')]
        mc = sum(a[(yy, 'mc')] for yy in YEARS) if y == 'all' else a[(y, 'mc')]
        cells += [f'{int(dn):,}', f'{mc:,.1f}', f'{dn / mc:.3f}']
    out.append(f'| {cut} | ' + ' | '.join(cells) + ' |')
out += ['', '## Children after the last cut, per year: data / MC (ratio)', '', '| child | ' + ' | '.join(YEARS + ['all']) + ' | Z_tautau share of MC |', '|---|' + '---:|' * 6]
for ch in CH:
    reg = f'inclusive_1p1p_{ch}'
    last = [k for k in order if k[0] == reg][-1]
    a = agg[last]; cells = []
    for y in YEARS + ['all']:
        dn = sum(a[(yy, 'data')] for yy in YEARS) if y == 'all' else a[(y, 'data')]
        mc = sum(a[(yy, 'mc')] for yy in YEARS) if y == 'all' else a[(y, 'mc')]
        cells.append(f'{int(dn):,} / {mc:,.1f} ({dn / mc:.3f})')
    t = sum(a[(yy, 'tau')] for yy in YEARS); m = sum(a[(yy, 'mc')] for yy in YEARS)
    out.append(f'| {ch} (cut {last[1]}) | ' + ' | '.join(cells) + f' | {t / m:.3f} |')
conf = list(csv.DictReader(open(B + 'cutflows/exclusive_confusion.csv')))
truths, recos, tab = [], [], collections.defaultdict(dict)
for r in conf:
    if r['truth'] not in truths: truths.append(r['truth'])
    if r['reco'] not in recos: recos.append(r['reco'])
    tab[r['truth']][r['reco']] = float(r['sumw'])
out += ['', '## Composition (all years): truth (rows) x reco child (columns), signed sumw', '', '| truth \\ reco | ' + ' | '.join(recos) + ' |', '|---|' + '---:|' * len(recos)]
for t in truths:
    out.append(f'| {t} | ' + ' | '.join(f'{tab[t].get(c, 0.0):.2f}' for c in recos) + ' |')
out += ['', '| reco child | all truth sumw | matching truth sumw | matching fraction |', '|---|---:|---:|---:|']
for c in recos:
    tot = sum(tab[t].get(c, 0.0) for t in truths); match = tab.get(c, {}).get(c, 0.0)
    out.append(f'| {c} | {tot:.2f} | {match:.2f} | {match / tot if tot else float("nan"):.3f} |')
out.append(f'\nTotal tau-pair sumw in the inclusive sample (confusion denominator): {sum(sum(v.values()) for v in tab.values()):.2f}')
open(B + 'aggregated.md', 'w').write('\n'.join(out) + '\n')
print('\n'.join(out))
