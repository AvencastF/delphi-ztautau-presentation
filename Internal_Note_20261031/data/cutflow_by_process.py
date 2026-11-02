"""Per-process cumulative cutflow of the inclusive region for the animated cutflow slide (components/CutflowBars.vue).
second 2026-10-31 revision: all years. Reads the count table of the 1992-1995 run-quality rerun (all-years-rq-20261026, job 60333695),
copied to data/nersc-all-years-rq-20261026/cutflows/cutflow.csv (sha256 f825aa04...), and writes components/cutflow-by-process.json
summed over 1992, 1993, 1994 and 1995 (all eight energy points). Z_tautau = sum of the ordered Z_tautau_* sub-samples;
Z_ee is kept separately (not stacked). Per-year rows are written too (key "years") for the milestone table.
Data rows count events after the run selection (luminosity table status 0 + run quality); the "input" row is therefore
smaller than the 2,395,361 converted events. Usage: python3 data/cutflow_by_process.py (from the deck root).
"""
import csv, json, collections
P = 'data/nersc-all-years-rq-20261026/cutflows/cutflow.csv'
PROC = ['Z_tautau', 'Z_mumu', 'Z_qq', 'Bhabha', 'yy_ll', 'yy_qq']
YEARS = ['1992', '1993', '1994', '1995']
order = []
d = {y: collections.defaultdict(lambda: collections.defaultdict(float)) for y in YEARS + ['all']}
for r in csv.DictReader(open(P)):
    if r['kind'] != 'cumulative' or r['region'] != 'inclusive_1p1p':
        continue
    cut, s = r['cut'], r['sample']
    year, rest = s.split('/', 1)
    if cut not in order:
        order.append(cut)
    if rest == 'data':
        key, val = 'data', int(r['n'])
    elif rest.startswith('Total MC'):
        key, val = 'total', float(r['sumw'])
    elif rest.startswith('Z_tautau_'):
        key, val = 'Z_tautau', float(r['sumw'])
    else:
        key, val = rest.split('/')[0], float(r['sumw'])
    for k in (year, 'all'):
        d[k][cut][key] += val
def rows_of(k):
    out = []
    for cut in order:
        c = d[k][cut]
        row = {'cut': cut, 'data': int(c['data']), 'total': c['total'], 'Z_ee': c['Z_ee']}
        row.update({p: c[p] for p in PROC})
        closure = sum(row[p] for p in PROC) - row['total']
        assert abs(closure) < 1e-3 * max(1, abs(row['total'])), (k, cut, closure)
        out.append(row)
    return out
res = {'source': P, 'run': 'all-years-rq-20261026 (job 60333695), years 1992-1995 summed', 'processes': PROC,
       'rows': rows_of('all'), 'years': {y: rows_of(y) for y in YEARS}}
json.dump(res, open('components/cutflow-by-process.json', 'w'), indent=1)
print(len(res['rows']), 'cuts written; per-process sums close to the Total MC rows')
for k in ['all'] + YEARS:
    rr = res['rows'] if k == 'all' else res['years'][k]
    for r in (rr[0], rr[10], rr[15], rr[17], rr[-1]):
        print(k, r['cut'], r['data'], round(r['total'], 1), round(r['Z_tautau'], 1), round(r['data'] / r['total'], 3))
