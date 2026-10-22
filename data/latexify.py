"""One-off converter: replace Unicode/ASCII math substitutes in the visible text of hand-written slides
with <LaTeX formula="..." /> components. Presenter notes, id tags, attributes, <script>/<style> blocks and
existing LaTeX components are left untouched. Usage: python3 data/latexify.py slides/a.md [...]
"""
import re, sys


def L(f):
    return '<LaTeX formula="' + f + '" />'


CH = {'eμ': r'e\mu', 'eπ': r'e\pi', 'eρ': r'e\rho', 'μμ': r'\mu\mu', 'μπ': r'\mu\pi', 'μρ': r'\mu\rho',
      'ππ': r'\pi\pi', 'πρ': r'\pi\rho', 'ρρ': r'\rho\rho'}
GREEK = {'τ': r'\tau', 'π': r'\pi', 'ρ': r'\rho', 'μ': r'\mu', 'γ': r'\gamma', 'σ': r'\sigma', 'θ': r'\theta',
         'φ': r'\phi', 'η': r'\eta', 'χ': r'\chi', 'δ': r'\delta', 'Δ': r'\Delta', 'ℓ': r'\ell'}


def num(s):
    return s.replace('−', '-').replace(',', '{,}')


RULES = [
    # processes and particle combinations
    (r'Z → ττ', lambda m: L(r'Z\to\tau\tau')), (r'Z → ee', lambda m: L(r'Z\to ee')),
    (r'Z → μμ', lambda m: L(r'Z\to\mu\mu')), (r'Z → qq̄', lambda m: L(r'Z\to q\bar q')),
    (r'γγ → ℓℓ', lambda m: L(r'\gamma\gamma\to\ell\ell')), (r'γγ → hadrons', lambda m: L(r'\gamma\gamma\to') + ' hadrons'),
    (r'γγ', lambda m: L(r'\gamma\gamma')),
    (r'e⁺e⁻', lambda m: L('e^+e^-')), (r'τ⁺τ⁻', lambda m: L(r'\tau^+\tau^-')), (r'τ⁺', lambda m: L(r'\tau^+')),
    (r'τ⁻', lambda m: L(r'\tau^-')), (r'−τ⁺', lambda m: L(r'-\tau^+')),
    # spin observables
    (r'B⁺_([rnk])', lambda m: L('B^+_' + m.group(1))), (r'B⁻_([rnk])', lambda m: L('B^-_' + m.group(1))),
    (r'\bC_([rnk]{2})\b', lambda m: L('C_{' + m.group(1) + '}')), (r'\bB_i\b', lambda m: L('B_i')),
    (r'\bC_ij\b', lambda m: L('C_{ij}')), (r'\bh_i\b', lambda m: L('h_i')),
    # kinematic variables
    (r'\(δθ, δφ\)', lambda m: L(r'(\delta\theta,\delta\phi)')), (r'\|cos θ\|', lambda m: L(r'|\cos\theta|')),
    (r'cos θ', lambda m: L(r'\cos\theta')), (r'\|Σ p⃗_T\|', lambda m: L(r'|\textstyle\sum\vec p_T|')),
    (r'√\(p₁² \+ p₂²\)', lambda m: L(r'\sqrt{p_1^2+p_2^2}')), (r'√s', lambda m: L(r'\sqrt{s}')),
    (r'\|z0\(H0\) − z0\(H1\)\|', lambda m: L(r'|z_0(\mathrm{H0})-z_0(\mathrm{H1})|')),
    (r'\|Δz0\|', lambda m: L(r'|\Delta z_0|')), (r'\|d0\|', lambda m: L(r'|d_0|')), (r'\|z0\|', lambda m: L(r'|z_0|')),
    (r'\bd0\b', lambda m: L('d_0')), (r'\bz0\b', lambda m: L('z_0')),
    (r'p / p_beam|p/p_beam', lambda m: L(r'p/p_\mathrm{beam}')), (r'\bp_beam\b', lambda m: L(r'p_\mathrm{beam}')),
    (r'\bE_beam\b', lambda m: L(r'E_\mathrm{beam}')), (r'\bE/p\b', lambda m: L('E/p')), (r'\bp_T\b', lambda m: L('p_T')),
    (r'χ²/dof', lambda m: L(r'\chi^2/\mathrm{dof}')), (r'χ²/ndf', lambda m: L(r'\chi^2/\mathrm{ndf}')),
    (r'χ²/10', lambda m: L(r'\chi^2/10')), (r'χ²', lambda m: L(r'\chi^2')),
    (r'ΔR &lt; ([\d.]+)', lambda m: L(r'\Delta R\lt ' + m.group(1))), (r'ΔR', lambda m: L(r'\Delta R')),
    (r'm\(track \+ γ\)', lambda m: L(r'm(\mathrm{track}+\gamma)')),
    (r'Σw', lambda m: L(r'\textstyle\sum w')),
    # numbers with uncertainties, comparisons and units
    (r'([+−-]?\d[\d.]*) ± ([\d.]+)', lambda m: L(num(m.group(1)) + r'\pm' + m.group(2))),
    (r'(&lt;|&gt;|≤|≥|<|>) ?(\d[\d.,]*) ?(GeV|mm|°)',
     lambda m: L({'&lt;': r'\lt ', '&gt;': r'\gt ', '≤': r'\le ', '≥': r'\ge ', '<': r'\lt ', '>': r'\gt '}[m.group(1)] + num(m.group(2))
                 + {'GeV': r'\,\mathrm{GeV}', 'mm': r'\,\mathrm{mm}', '°': r'^\circ'}[m.group(3)])),
    (r'(&lt;|&gt;|≤|≥) ?(\d[\d.,]*)', lambda m: L({'&lt;': r'\lt ', '&gt;': r'\gt ', '≤': r'\le ', '≥': r'\ge '}[m.group(1)] + num(m.group(2)))),
    (r'(\d[\d.]*) ?pb⁻¹', lambda m: L(m.group(1) + r'\,\mathrm{pb}^{-1}')), (r'pb⁻¹', lambda m: L(r'\mathrm{pb}^{-1}')),
    (r'(\d[\d.]*)°', lambda m: L(m.group(1) + r'^\circ')), (r'\[°\]', lambda m: '[' + L(r'^\circ') + ']'),
    (r'(\d[\d.]*) → (\d[\d.]*)(°?)', lambda m: L(m.group(1) + (r'^\circ' if m.group(3) else '') + r'\to ' + m.group(2) + (r'^\circ' if m.group(3) else ''))),
    (r'−(\d[\d.]*)', lambda m: L('-' + m.group(1))),
    (r' × ', lambda m: ' ' + L(r'\times') + ' '), (r'(\d)×', lambda m: m.group(1) + L(r'\times')),
    (r'≈', lambda m: L(r'\approx')), (r' ÷ ', lambda m: ' / '), (r' → ', lambda m: ' ' + L(r'\to') + ' '),
]
for k, v in CH.items():
    RULES.append((r'(?<![\w\\])' + k + r'(?![\w])', (lambda f: (lambda m: L(f)))(v)))
for k, v in GREEK.items():
    RULES.append((k, (lambda f: (lambda m: L(f)))(v)))
COMPILED = [(re.compile(p), f) for p, f in RULES]

PROTECT = re.compile(r'(<!--.*?-->|<script.*?</script>|<style.*?</style>|<span class="id">.*?</span>|<LaTeX [^>]*/>|<[^>]+>|^---\n.*?\n---\n)', re.S | re.M)


def convert_text(t):
    out = t
    for rx, f in COMPILED:
        parts = PROTECT.split(out)
        out = ''.join(p if (i % 2 == 1) else rx.sub(f, p) for i, p in enumerate(parts))
    return out


def convert(src):
    parts = PROTECT.split(src)
    return ''.join(p if i % 2 == 1 else convert_text(p) for i, p in enumerate(parts))


if __name__ == '__main__':
    for f in sys.argv[1:]:
        s = open(f).read()
        n = convert(s)
        if n != s:
            open(f, 'w').write(n)
            print('converted', f)
