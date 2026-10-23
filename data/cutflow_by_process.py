"""Per-process cumulative cutflow of the inclusive region for the animated cutflow slide (components/CutflowBars.vue).
Reads the frozen 2026-10-12 run's count table copied in data/nersc-all-event-detector-1994-20261012/cutflow.csv and writes
components/cutflow-by-process.json. Z_tautau = sum of the ordered Z_tautau_* sub-samples; Z_ee is kept separately (not stacked).
Signed sums are stored at full precision; the slide shows integers. Usage: python3 data/cutflow_by_process.py (from the deck root).
"""
import csv, json, collections
P = 'data/nersc-all-event-detector-1994-20261012/cutflow.csv'
PROC = ['Z_tautau', 'Z_mumu', 'Z_qq', 'Bhabha', 'yy_ll', 'yy_qq']
order, d = [], collections.defaultdict(lambda: collections.defaultdict(float))
for r in csv.DictReader(open(P)):
    if r['kind'] != 'cumulative' or r['region'] != 'inclusive_1p1p':
        continue
    cut, s = r['cut'], r['sample']
    if cut not in order:
        order.append(cut)
    if s == '1994/data':
        d[cut]['data'] = int(r['n'])
    elif s.startswith('1994/Total MC'):
        d[cut]['total'] = float(r['sumw'])
    elif s.startswith('1994/Z_tautau_'):
        d[cut]['Z_tautau'] += float(r['sumw'])
    else:
        d[cut][s.split('/')[1]] = float(r['sumw'])
rows = []
for cut in order:
    row = {'cut': cut, 'data': d[cut]['data'], 'total': d[cut]['total'], 'Z_ee': d[cut]['Z_ee']}
    row.update({p: d[cut][p] for p in PROC})
    closure = sum(row[p] for p in PROC) - row['total']
    assert abs(closure) < 1e-3 * max(1, abs(row['total'])), (cut, closure)
    rows.append(row)
json.dump({'source': P, 'processes': PROC, 'rows': rows}, open('components/cutflow-by-process.json', 'w'), indent=1)
print(len(rows), 'cuts written; per-process sums close to the Total MC row')
for r in (rows[0], rows[-1]):
    print(r['cut'], {k: round(v) for k, v in r.items() if k != 'cut'})
