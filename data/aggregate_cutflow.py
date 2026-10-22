"""Aggregate the frozen-run cutflow.csv (tau_analysis) into data vs signed-MC tables.
Usage: python3 aggregate_cutflow.py cutflow.csv exclusive_confusion.csv
Signed MC = sum of sumw over all MC samples except Z_ee (overlaps Bhabha), as in the handoff.
"""
import csv, sys, collections
cut_csv, conf_csv = sys.argv[1], sys.argv[2]
rows = [r for r in csv.DictReader(open(cut_csv)) if r['kind'] == 'cumulative']
def sample_class(s):
    if s == '1994/data': return 'data'
    proc = s.split('/')[1]
    if proc == 'Z_ee': return 'Z_ee'
    return 'tau' if proc.startswith('Z_tautau') else 'bkg'
order = []
agg = collections.defaultdict(lambda: collections.defaultdict(float))
nraw = collections.defaultdict(lambda: collections.defaultdict(int))
for r in rows:
    key = (r['region'], r['cut'])
    if key not in order: order.append(key)
    c = sample_class(r['sample'])
    agg[key][c] += float(r['sumw']); nraw[key][c] += int(r['n'])
print('| region | cut | data | Z_tautau (signed sumw) | other MC excl. Z_ee (signed sumw) | total MC excl. Z_ee | data/MC |')
print('|---|---|---:|---:|---:|---:|---:|')
for key in order:
    a = agg[key]; mc = a['tau'] + a['bkg']
    print(f"| {key[0]} | {key[1]} | {int(a['data'])} | {a['tau']:.3f} | {a['bkg']:.3f} | {mc:.3f} | {a['data']/mc if mc else float('nan'):.4f} |")
print()
# confusion: truth (rows) x reco (cols), weighted sumw
conf = list(csv.DictReader(open(conf_csv)))
truths, recos = [], []
tab = collections.defaultdict(dict)
for r in conf:
    if r['truth'] not in truths: truths.append(r['truth'])
    if r['reco'] not in recos: recos.append(r['reco'])
    tab[r['truth']][r['reco']] = float(r['sumw'])
print('| truth \\ reco | ' + ' | '.join(recos) + ' |')
print('|---|' + '---:|' * len(recos))
for t in truths:
    print(f'| {t} | ' + ' | '.join(f"{tab[t].get(c,0.0):.2f}" for c in recos) + ' |')
print()
print('| reco child | reco marginal sumw (all truth) | matching truth sumw | matching fraction |')
print('|---|---:|---:|---:|')
for c in recos:
    tot = sum(tab[t].get(c, 0.0) for t in truths)
    match = tab.get(c, {}).get(c, 0.0)
    print(f'| {c} | {tot:.3f} | {match:.3f} | {match/tot if tot else float("nan"):.3f} |')
