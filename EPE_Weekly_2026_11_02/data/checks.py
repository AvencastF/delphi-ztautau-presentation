"""Deck checks for Ztautau_Spin. Run from the deck root: python3 data/checks.py [word limit]

1. Body word count per slide (limit 70 by default). Excluded, as in the status deck: presenter notes,
   front-matter, <script>/<style>, table cells, captions (.tk-cap / .st-cap), key-value entries, tags and
   labels, legends, the .tk-foot footer, and headings. Text inside deck-local animated components is not
   counted (it is shown one stage at a time).
2. Leftover Unicode / ASCII math substitutes in the visible slide body (outside <LaTeX .../>, .id spans,
   notes, scripts and styles).
"""
import re, sys

limit = int(sys.argv[1]) if len(sys.argv) > 1 else 70
order = [l.split('src:', 1)[1].strip() for l in open('slides.md') if l.startswith('src:')]
bad = re.compile(r'[τπρμγσθφηχδΔℓ⁺⁻²¹⁴⁵⁶√→±−×÷≈≤≥°₁₂]|&lt;|&gt;|Σ|\bp_beam|\bE_beam|\bC_[rnk]{2}\b|\^')

def body(s):
    s = re.sub(r'^---.*?---\n', '', s, count=1, flags=re.S)
    s = re.sub(r'<!--.*?-->', '', s, flags=re.S)
    s = re.sub(r'<script.*?</script>', '', s, flags=re.S)
    s = re.sub(r'<style.*?</style>', '', s, flags=re.S)
    return s

over = 0; hits_total = 0
for i, f in enumerate(order, 1):
    name = f.rsplit('/', 1)[-1]
    raw = open(f).read()
    s = body(raw)
    # --- LaTeX check on the visible body ---
    t = re.sub(r'<LaTeX [^>]*/>', '', s)
    t = re.sub(r'<span class="id">.*?</span>', '', t, flags=re.S)
    t = re.sub(r'<[^>]+>', '', t)
    hits = [l.strip()[:110] for l in t.splitlines() if bad.search(l)]
    # --- word count ---
    w = re.sub(r'<t[dh][^>]*>.*?</t[dh]>', '', s, flags=re.S)
    w = re.sub(r'<div class="(?:tk-cap|st-cap|tk-foot|st-source|legend|st-sub|sm-legend|tk-flow|tk-primer|tk-years|tk-stat\b[^"]*|tk-note)"[^>]*>.*?</div>', '', w, flags=re.S)
    w = re.sub(r'<d[td]>.*?</d[td]>', '', w, flags=re.S)
    w = re.sub(r'<span class="(?:tag|tk-label|badge)[^"]*">.*?</span>', '', w, flags=re.S)
    w = re.sub(r'<[^>]+>', ' ', w)
    w = re.sub(r'^#.*$', '', w, flags=re.M)
    words = [x for x in re.split(r'\s+', w) if re.search(r'[A-Za-z0-9]', x)]
    n = len(words)
    is_bridge = name.startswith('ch-') or name.startswith('backup-divider') or name in ('cover.md', 'end.md')
    flag = '  <-- over' if n > limit and not is_bridge else ''
    if flag: over += 1
    print(f'{i:3d} {n:4d} {name}{flag}')
    for h in hits: print('      latex?', h)
    hits_total += len(hits)
print(f'slides {len(order)}, over {limit} words: {over}, latex substitutes: {hits_total}')
