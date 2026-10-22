import re,glob,sys
bad=re.compile(r'[τπρμγσθφηχδΔℓ⁺⁻²¹⁴⁵⁶√→±−×÷≈≤≥°₁₂⃗̄]|&lt;|&gt;|Σ|\bp_beam|\bE_beam|\bC_[rnk]|\bp_T|\^')
files=sys.argv[1:] or sorted(glob.glob('slides/*.md'))
tot=0
for f in files:
    s=open(f).read()
    s=re.sub(r'<!--.*?-->','',s,flags=re.S); s=re.sub(r'<LaTeX [^>]*/>','',s); s=re.sub(r'<span class="id">.*?</span>','',s)
    s=re.sub(r'<script.*?</script>|<style.*?</style>','',s,flags=re.S)
    s=re.sub(r'<[^>]+>','',s); s=re.sub(r'^---\n.*?\n---\n','',s,flags=re.S)
    hits=[l.strip()[:120] for l in s.splitlines() if bad.search(l)]
    if hits: tot+=len(hits); print('##',f); [print('   ',h) for h in hits[:8]]
print('remaining lines:',tot)
