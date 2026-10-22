"""Write the appendix table slides (full cutflow, classifier, widths, versions, closure). Run from the deck root."""
import csv, collections
P='data/nersc-all-event-detector-1994-20261012/'
rows=[r for r in csv.DictReader(open(P+'cutflow.csv')) if r['kind']=='cumulative' and r['region']=='inclusive_1p1p']
order=[];d=collections.defaultdict(dict)
for r in rows:
    k=r['cut']
    if k not in order: order.append(k)
    if r['sample']=='1994/data': d[k]['data']=int(r['n'])
    elif 'Total MC' in r['sample']: d[k]['mc']=float(r['sumw'])
    elif r['sample'].startswith('1994/Z_tautau_'): d[k]['tau']=d[k].get('tau',0.)+float(r['sumw'])
HEAD="---\nclass: st pres\n---\n"
def row(k):
    cls=' class="hl"' if k=='neutral_hemisphere_limit' else ''
    return f"<tr{cls}><td>{k}</td><td>{d[k]['data']:,}</td><td>{d[k]['mc']:,.6f}</td><td>{d[k].get('tau',0):,.3f}</td></tr>\n"
def tbl(keys,n):
    body=''.join(row(k) for k in keys)
    return HEAD+f"""
# Appendix · full inclusive cutflow ({n}/2)

<div class="st-sub">Cumulative counts of the frozen 2026-10-12 run; cut names as in the configuration; exact signed sums.</div>

<table class="num">
<thead><tr><th>After cut</th><th>Data</th><th>Total MC, no Z_ee (signed Σw)</th><th>of which Z → ττ</th></tr></thead>
<tbody>
{body}</tbody>
</table>

<div class="st-source">Source: count table of the frozen 2026-10-12 selection run</div>

<!-- data/nersc-all-event-detector-1994-20261012/cutflow.csv (Total MC row verbatim; Z_tautau = sum of ordered sub-samples). -->
"""
open('slides/appendix-cutflow-1.md','w').write(tbl(order[:10],1)); open('slides/appendix-cutflow-2.md','w').write(tbl(order[10:],2))
cls="""ee|0.643±0.002|0.946±0.001|0.755±0.004|0.909±0.003|0.999|0.983±0.034|1.043±0.031
emu|0.707±0.001|0.963±0.001|0.922±0.001|0.962±0.001|0.999|0.954±0.024|0.977±0.021
epi|0.576±0.002|0.859±0.001|0.416±0.002|0.835±0.002|0.994|0.967±0.024|1.076±0.029
erho|0.255±0.001|0.878±0.001|0.699±0.002|0.834±0.001|0.988|0.994±0.031|0.979±0.018
mumu|0.765±0.002|0.967±0.001|0.840±0.004|0.952±0.002|0.999|1.086±0.033|1.048±0.030
mupi|0.635±0.002|0.871±0.001|0.434±0.002|0.829±0.002|0.994|0.986±0.023|1.026±0.028
murho|0.280±0.001|0.885±0.001|0.718±0.002|0.841±0.001|0.988|1.026±0.029|0.968±0.017
pipi|0.516±0.004|0.766±0.003|0.181±0.002|0.746±0.004|0.995|1.005±0.033|1.091±0.057
pirho|0.236±0.002|0.802±0.001|0.338±0.002|0.747±0.002|0.985|1.022±0.030|1.000±0.024
rhorho|0.106±0.001|0.799±0.001|0.551±0.004|0.750±0.001|0.983|1.028±0.053|0.953±0.022"""
def tds(cells): return ''.join('<td>'+c+'</td>' for c in cells)
body=''.join('<tr>'+tds(l.split('|'))+'</tr>\n' for l in cls.splitlines())
open('slides/appendix-classifier.md','w').write(HEAD+f"""
# Appendix · classifier evaluation of 2026-10-15, all channels

<div class="st-sub">Earlier epoch-27 checkpoint, training events included (optimistic). Efficiency w.r.t. the true channel; purity on the simulation stack.</div>

<table class="sm num">
<thead><tr><th>Channel</th><th>eff. cuts</th><th>eff. ML</th><th>purity cuts</th><th>purity ML</th><th>AUC</th><th>data/MC cuts</th><th>data/MC ML</th></tr></thead>
<tbody>
{body}</tbody>
</table>

<div class="st-source">Source: classifier evaluation summary of 2026-10-15</div>

<!-- /Users/avencastmini/Downloads/skim-cls-eval/summary.md; checkpoint epoch=27_train=0.1167_val=0.5280.ckpt; mc_split all. -->
""")
def best(vals,low=True):
    f=[float(v) for v in vals]; b=min(f) if low else max(f)
    out=''
    for v in vals:
        out+= '<td><span class="best">'+v+'</span></td>' if float(v)==b else '<td>'+v+'</td>'
    return out
w="""ee|0.291|0.312|0.315|0.289|0.235|0.237|0.244|0.243|0.267|0.284|0.281|0.262|0.55|0.50|0.51|0.56
emu|0.279|0.297|0.300|0.281|0.224|0.230|0.229|0.225|0.253|0.279|0.280|0.254|0.57|0.51|0.50|0.57
mumu|0.258|0.278|0.276|0.259|0.204|0.212|0.210|0.204|0.232|0.265|0.267|0.229|0.61|0.54|0.53|0.63
epi|0.202|0.212|0.219|0.203|0.168|0.141|0.153|0.170|0.202|0.212|0.219|0.203|0.67|0.64|0.63|0.67
mupi|0.190|0.195|0.203|0.186|0.154|0.124|0.130|0.150|0.186|0.195|0.203|0.186|0.70|0.67|0.65|0.71
erho|0.246|0.310|0.308|0.251|0.218|0.238|0.243|0.215|0.229|0.278|0.276|0.229|0.61|0.48|0.48|0.61
murho|0.236|0.284|0.289|0.238|0.199|0.224|0.223|0.199|0.215|0.264|0.270|0.216|0.63|0.51|0.49|0.63
pipi|0.146|0.135|0.145|0.142|0.105|0.080|0.082|0.104|0.146|0.135|0.145|0.142|0.78|0.77|0.73|0.77
pirho|0.185|0.221|0.241|0.182|0.156|0.141|0.160|0.157|0.185|0.221|0.241|0.182|0.70|0.60|0.55|0.70
rhorho|0.222|0.315|0.289|0.223|0.197|0.240|0.253|0.201|0.208|0.285|0.278|0.210|0.64|0.46|0.44|0.63"""
body=''
for l in w.splitlines():
    c=l.split('|'); body+='<tr><td>'+c[0]+'</td>'+best(c[1:5])+best(c[5:9])+best(c[9:13])+best(c[13:17],False)+'</tr>\n'
open('slides/appendix-widths.md','w').write(HEAD+f"""
# Appendix · spin-observable resolution, all channels and versions

<div class="st-sub">Columns per version v2 / v3 / v4 / v5; best value per row in green (smallest width, largest correlation).</div>

<table class="sm num">
<thead><tr><th rowspan="2">Channel</th><th colspan="4">median 68 % width</th><th colspan="4">C_kk width</th><th colspan="4">C_nn width</th><th colspan="4">corr. C_nn</th></tr>
<tr><th>v2</th><th>v3</th><th>v4</th><th>v5</th><th>v2</th><th>v3</th><th>v4</th><th>v5</th><th>v2</th><th>v3</th><th>v4</th><th>v5</th><th>v2</th><th>v3</th><th>v4</th><th>v5</th></tr></thead>
<tbody>
{body}</tbody>
</table>

<div class="st-source">Source: version comparison table of the v5 archive</div>

<!-- artifacts/neutrino-ml-v5-20261021/compare_versions.md "Observable residuals per truth channel". -->
""")
ba="""ee|0.676|0.659|0.661|0.683|+0.007 ± 0.007
emu|0.694|0.673|0.673|0.687|−0.007 ± 0.005
mumu|0.717|0.698|0.702|0.706|−0.011 ± 0.006
epi|0.701|0.686|0.682|0.700|−0.002 ± 0.006
mupi|0.713|0.704|0.704|0.717|+0.003 ± 0.006
erho|0.745|0.667|0.671|0.739|−0.006 ± 0.004
murho|0.751|0.690|0.686|0.753|+0.002 ± 0.004
pipi|0.762|0.755|0.736|0.764|+0.003 ± 0.011
pirho|0.771|0.698|0.709|0.768|−0.003 ± 0.005
rhorho|0.773|0.673|0.693|0.771|−0.002 ± 0.004"""
body=''
for l in ba.splitlines():
    c=l.split('|'); body+='<tr><td>'+c[0]+'</td>'+best(c[1:5],False)+'<td>'+c[5]+'</td></tr>\n'
de="""e|1.16 / 2.32|1.35 / 2.77|1.35 / 2.75|1.17 / 2.35
μ|1.08 / 2.18|1.27 / 2.65|1.27 / 2.63|1.09 / 2.21
π|0.90 / 2.08|0.97 / 2.46|1.01 / 2.48|0.89 / 2.07
ρ|1.01 / 2.02|1.38 / 2.89|1.36 / 2.80|1.03 / 2.07"""
body2=''
for l in de.splitlines():
    c=l.split('|'); body2+='<tr><td>'+c[0]+' legs</td>'+tds(c[1:])+'</tr>\n'
open('slides/appendix-versions.md','w').write(HEAD+f"""
# Appendix · model versions 2–5: branch accuracy and direction error

<div class="st-cols st-cols-2">
<div>
<table class="sm num">
<thead><tr><th>Correct branch</th><th>v2</th><th>v3</th><th>v4</th><th>v5</th><th>v5 − v2</th></tr></thead>
<tbody>
{body}</tbody>
</table>
</div>
<div>
<table class="sm num">
<thead><tr><th>Median / 84th pct. [°]</th><th>v2</th><th>v3</th><th>v4</th><th>v5</th></tr></thead>
<tbody>
{body2}</tbody>
</table>
<div class="co ok" style="margin-top:8px"><b>Per channel</b> π in ππ 0.78 / 0.61 / 0.68 / 0.75; ρ in ρρ 0.98 / 1.44 / 1.33 / 1.00.</div>
</div>
</div>

<div class="st-source">Source: version comparison table of the v5 archive</div>

<!-- artifacts/neutrino-ml-v5-20261021/compare_versions.md and README.md. -->
""")
cl="""B⁻_r|+0.001|−0.068 ± 0.039, σ 0.149 (−0.46)|−0.079 ± 0.040, σ 0.157 (−0.50)|−0.085 ± 0.039, σ 0.150 (−0.57)|−0.166 ± 0.061, σ 0.267 (−0.62)
B⁻_n|−0.009|−0.017 ± 0.040, σ 0.155 (−0.11)|−0.021 ± 0.042, σ 0.167 (−0.12)|−0.032 ± 0.041, σ 0.160 (−0.20)|+0.081 ± 0.072, σ 0.319 (+0.25)
B⁻_k|−0.186|−0.021 ± 0.047, σ 0.196 (−0.11)|−0.092 ± 0.048, σ 0.202 (−0.46)|−0.066 ± 0.047, σ 0.196 (−0.34)|−0.118 ± 0.061, σ 0.264 (−0.45)
B⁺_r|−0.005|−0.088 ± 0.040, σ 0.154 (−0.57)|−0.146 ± 0.041, σ 0.159 (−0.92)|−0.125 ± 0.040, σ 0.154 (−0.81)|−0.179 ± 0.063, σ 0.274 (−0.65)
B⁺_n|−0.027|−0.025 ± 0.039, σ 0.151 (−0.17)|−0.039 ± 0.041, σ 0.159 (−0.25)|−0.059 ± 0.040, σ 0.156 (−0.38)|+0.049 ± 0.068, σ 0.302 (+0.16)
B⁺_k|−0.132|−0.026 ± 0.046, σ 0.188 (−0.14)|−0.050 ± 0.046, σ 0.189 (−0.27)|−0.007 ± 0.045, σ 0.186 (−0.04)|−0.051 ± 0.058, σ 0.249 (−0.20)
C_rr|−0.728|−0.051 ± 0.062, σ 0.230 (−0.22)|−0.012 ± 0.066, σ 0.256 (−0.05)|−0.072 ± 0.062, σ 0.233 (−0.31)|+0.056 ± 0.092, σ 0.393 (+0.14)
C_rn|+0.027|+0.058 ± 0.071, σ 0.280 (+0.21)|+0.043 ± 0.073, σ 0.294 (+0.15)|+0.061 ± 0.072, σ 0.287 (+0.21)|−0.082 ± 0.130, σ 0.586 (−0.14)
C_rk|−0.050|−0.049 ± 0.078, σ 0.319 (−0.15)|+0.018 ± 0.080, σ 0.330 (+0.05)|+0.037 ± 0.076, σ 0.307 (+0.12)|+0.058 ± 0.118, σ 0.524 (+0.11)
C_nr|+0.040|+0.059 ± 0.075, σ 0.305 (+0.19)|+0.027 ± 0.080, σ 0.331 (+0.08)|−0.015 ± 0.077, σ 0.314 (−0.05)|+0.169 ± 0.158, σ 0.719 (+0.24)
C_nn|+0.747|+0.117 ± 0.059, σ 0.215 (+0.55)|+0.079 ± 0.062, σ 0.228 (+0.34)|+0.074 ± 0.058, σ 0.207 (+0.36)|−0.029 ± 0.084, σ 0.349 (−0.08)
C_nk|+0.023|−0.019 ± 0.076, σ 0.306 (−0.06)|−0.050 ± 0.078, σ 0.315 (−0.16)|−0.038 ± 0.077, σ 0.309 (−0.12)|−0.251 ± 0.126, σ 0.564 (−0.44)
C_kr|−0.055|−0.175 ± 0.079, σ 0.322 (−0.54)|+0.043 ± 0.079, σ 0.321 (+0.13)|−0.018 ± 0.076, σ 0.307 (−0.06)|+0.073 ± 0.118, σ 0.520 (+0.14)
C_kn|+0.017|+0.050 ± 0.077, σ 0.312 (+0.16)|+0.062 ± 0.077, σ 0.313 (+0.20)|+0.038 ± 0.076, σ 0.307 (+0.12)|+0.115 ± 0.120, σ 0.534 (+0.22)
C_kk|+1.064|−0.157 ± 0.070, σ 0.279 (−0.56)|−0.117 ± 0.066, σ 0.256 (−0.46)|−0.007 ± 0.063, σ 0.243 (−0.03)|−0.032 ± 0.087, σ 0.368 (−0.09)
concurrence|0.718|+0.165 ± 0.185, σ 0.684 (+0.24)|+0.167 ± 0.211, σ 0.724 (+0.23)|+0.155 ± 0.234, σ 0.661 (+0.23)|−0.064 ± 0.183, σ 1.026 (−0.06)"""
lines=cl.splitlines()
for n,chunk in enumerate([lines[:8],lines[8:]],1):
    body=''.join('<tr>'+tds(l.split('|'))+'</tr>\n' for l in chunk)
    open(f'slides/appendix-closure-{n}.md','w').write(HEAD+f"""
# Appendix · ππ closure, all observables ({n}/2)

<div class="st-sub">bias ± MC error, σ at the full 1994 yield, (pull). Truth = half-B moments.</div>

<table class="sm">
<thead><tr><th>Observable</th><th>truth</th><th>ML v5</th><th>ML v4</th><th>ML v3</th><th>analytical</th></tr></thead>
<tbody>
{body}</tbody>
</table>

<div class="st-source">Source: closure table of the v5 archive</div>

<!-- artifacts/neutrino-ml-v5-20261021/closure_v5.md verbatim. -->
""")
print('appendix tables ok')
