"""Body word count per slide: strips presenter notes, front-matter, script blocks, table cells, figure captions,
source footers, tags/ids inside .id spans count as words (they are visible). Usage: python3 data/wordcount.py [limit]"""
import re, sys, glob
limit=int(sys.argv[1]) if len(sys.argv)>1 else 70
order=[l.split('./slides/')[1].strip() for l in open('slides.md') if l.startswith('src:')]
rows=[]
for i,f in enumerate(order,1):
    s=open('slides/'+f).read()
    s=re.sub(r'^---.*?---\n','',s,count=1,flags=re.S)
    s=re.sub(r'<!--.*?-->','',s,flags=re.S)
    s=re.sub(r'<script.*?</script>','',s,flags=re.S)
    s=re.sub(r'<style.*?</style>','',s,flags=re.S)
    s=re.sub(r'<t[dh][^>]*>.*?</t[dh]>','',s,flags=re.S)
    s=re.sub(r'<div class="st-cap">.*?</div>','',s,flags=re.S)
    s=re.sub(r'<d[td]>.*?</d[td]>','',s,flags=re.S)  # key-value card entries count as structured, like table cells
    s=re.sub(r'<span class="tag[^"]*">.*?</span>','',s,flags=re.S)
    s=re.sub(r'<div class="legend">.*?</div>','',s,flags=re.S)
    s=re.sub(r'<div class="st-source">.*?</div>','',s,flags=re.S)
    s=re.sub(r'<[^>]+>',' ',s)
    s=re.sub(r'^#.*$','',s,flags=re.M)
    words=[w for w in re.split(r'\s+',s) if re.search(r'[A-Za-z0-9α-ωτμπρ]',w)]
    rows.append((i,f,len(words)))
over=[r for r in rows if r[2]>limit and not f.startswith('ch-')]
for r in rows: print(f'{r[0]:3d} {r[2]:4d} {r[1]}' + ('  <-- over' if r[2]>limit and not r[1].startswith('ch-') and not r[1].startswith('appendix-divider') else ''))
print('slides',len(rows),'over budget',len(over))
