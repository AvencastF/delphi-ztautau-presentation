"""Generate the data/MC plot slides: main deck (inclusive 4 slides, two per-year slides, one slide per child) and the
appendix (every remaining figure, 4 per slide). Run from the deck root. Captions = variable name +
chi2/dof badge (green <=1.5, amber <=3, red >3 per dof) from the agreement.json files of the 1992-1995 run-quality rerun
(plots job 60340876), copied to data/nersc-all-years-rq-20261026/plots/. Overlay figures (shape per year) carry no chi2.
second 2026-10-31 revision: figures from public/figures/datamc-1992-1995/ (all years, all eight energy points), replacing the
1994-only le3 artifact figures."""
import os, json
F='public/figures/datamc-1992-1995/'
AG='data/nersc-all-years-rq-20261026/plots'
SRC='Source: data/MC plots of the 1992–1995 run-quality rerun (selection job 60333695, plots job 60340876)'
NOTE='Full-precision values are in SOURCES.md and the data folder. Figures: NERSC /pscratch/sd/a/avencast/Ztautau/analysis-runs/1992_1993_1994_1995/all-years-rq-20261026/plots/{all-years-baseline, all-years-children, all-years-children-inclusive_1p1p_<child>}/ (selection job 60333695, tau_analysis 67bffe7; plots job 60340876, recipes plotting_all_years_baseline.yaml / plotting_all_years_children.yaml), copied to public/figures/datamc-1992-1995/ (MANIFEST.md). Black points = 1992-1995 data after the run selection (status 0 + run quality); stack = signed simulation normalised per (year, process, point) to the run-quality luminosity, Z_ee excluded; lower panel = data / simulation. Inclusive sample 56,472 data / 57,520.06 MC (0.982). chi2/dof from agreement.json ("Total MC", status ok; Gaussian chi2 with data variance and finite-MC sumw2), statistical only, diagnostic. Luminosities user-supplied, uncertified.'
import re as _re
def m(t): return _re.sub(r'\$([^$]+)\$', lambda g: '<LaTeX formula="'+g.group(1).replace('"','')+'" />', t)
AGDIR={'inclusive':'all-years-baseline','ee':'all-years-children'}
def badge(ch,var,sub=''):
    d=AGDIR.get(ch,f'all-years-children-inclusive_1p1p_{ch}')+(f'/{sub}' if sub else '')
    if ch=='overlay': return '<span class="badge n">shape, no '+m('$\\chi^2$')+'</span>'
    try:
        a=json.load(open(f'{AG}/{d}/agreement.json'))['comparisons'][var]['Total MC']
        if 'correlated' in str(a.get('status')): return '<span class="badge n">no '+m('$\\chi^2$')+': correlated entries</span>'
        if a.get('status')!='ok' or not a['dof']: return '<span class="badge n">no '+m('$\\chi^2$')+'</span>'
        r=a['chi2']/a['dof']; c='g' if r<=1.5 else 'a' if r<=3 else 'r'
        return f'<span class="badge {c}">'+m('$\\chi^2/\\mathrm{dof}$')+f' {a["chi2"]:.1f} / {a["dof"]}</span>'
    except Exception: return '<span class="badge n">no '+m('$\\chi^2$')+'</span>'
def fig(path,cap,ch,var,sub=''):
    alt=_re.sub(r'[$\\{}^_]','',cap)
    return f'<div><div class="st-fig"><NJUPlot src="/figures/datamc-1992-1995/{path}" alt="{alt}" /></div><div class="st-cap">{m(cap)}{badge(ch,var,sub)}</div></div>'
HEAD="---\nclass: st pres\n---\n\n<script setup>\nimport NJUPlot from '../components/NJUPlot.vue'\n</script>\n"
def slide(fname,title,sub,cells,note_extra=''):
    md=HEAD+f"\n# {m(title)}\n\n<div class=\"st-sub\">{m(sub)}</div>\n\n<div class=\"fig2x2\">\n{chr(10).join(cells)}\n</div>\n\n<div class=\"st-source\">{SRC}</div>\n\n<!--\n{NOTE}\n{note_extra}\n-->\n"
    open(f'slides/{fname}','w').write(md)
IL={'leadtrack_hemi0_p':r'H0 leading-track $p$ [GeV]','leadtrack_hemi1_p':r'H1 leading-track $p$ [GeV]','leadtrack_hemi0_p_over_pbeam':r'H0 leading-track $p/p_\mathrm{beam}$','leadtrack_hemi1_p_over_pbeam':r'H1 leading-track $p/p_\mathrm{beam}$','leadtrack_hemi0_costheta':r'H0 leading-track $\cos\theta$','leadtrack_hemi1_costheta':r'H1 leading-track $\cos\theta$','visible_tautau_mass':r'visible $m_{\tau\tau}$ [GeV]','exclusive_pair_code':r'child assignment code','erad_over_ebeam':r'$E_\mathrm{rad}/E_\mathrm{beam}$','prad_over_pbeam':r'$p_\mathrm{rad}/p_\mathrm{beam}$','exclusive_e_over_p':r'EM-calorimeter $E/p$ per track','exclusive_nearby_photon_count':r'identified photons, $\Delta R\lt 0.3$','exclusive_hemi0_hcal_mean':r'H0 HCAL mean per hit layer [GeV]','exclusive_hemi1_hcal_mean':r'H1 HCAL mean per hit layer [GeV]','exclusive_hemi0_hadron_source':r'H0 hadron-source category','exclusive_hemi1_hadron_source':r'H1 hadron-source category','exclusive_hemi0_nearby_photon_energy':r'H0 nearby photon $E$ [GeV]','exclusive_hemi1_nearby_photon_energy':r'H1 nearby photon $E$ [GeV]','exclusive_hemi0_hadron_photon_mass':r'H0 $m(\mathrm{track}+\gamma)$ [GeV]','exclusive_hemi1_hadron_photon_mass':r'H1 $m(\mathrm{track}+\gamma)$ [GeV]','exclusive_hemi0_nearby_diphoton_mass':r'H0 $m_{\gamma\gamma}$ [GeV]','exclusive_hemi1_nearby_diphoton_mass':r'H1 $m_{\gamma\gamma}$ [GeV]','exclusive_hemi0_reason':r'H0 identification outcome','exclusive_hemi1_reason':r'H1 identification outcome','neutral_combined_all_count':r'all neutrals per hemisphere','neutral_combined_all_dr03_count':r'all neutrals, $\Delta R\lt 0.3$','neutral_combined_identified_photon_count':r'identified photons','neutral_combined_failed_photon_count':r'non-photon neutrals','neutral_combined_identified_photon_dr01_count':r'identified photons, $\Delta R\lt 0.1$','neutral_combined_identified_photon_dr05_count':r'identified photons, $\Delta R\lt 0.5$','neutral_combined_failed_photon_dr03_count':r'non-photon neutrals, $\Delta R\lt 0.3$'}
def ifig(v): 
    p=f'inclusive/inclusive_1p1p-selected-{v}-rate_lin.svg'; assert os.path.exists(F+p),p
    return fig(p,IL[v],'inclusive',v)
isub=r'1992–1995, all eight points · inclusive $\tau\tau$ sample, all 18 cuts <span class="id">inclusive_1p1p</span> · H0 / H1 = thrust hemispheres · points: data, stack: simulation'
main_inc=[('datamc-inclusive-01.md','Inclusive sample: leading-track kinematics',['leadtrack_hemi0_p_over_pbeam','leadtrack_hemi1_p_over_pbeam','leadtrack_hemi0_costheta','leadtrack_hemi1_costheta']),
 ('datamc-inclusive-02.md','Inclusive sample: calorimeter response',['exclusive_e_over_p','exclusive_hemi0_hcal_mean','exclusive_hemi1_hcal_mean','exclusive_hemi0_hadron_source']),
 ('datamc-inclusive-03.md','Inclusive sample: neutrals and photons',['neutral_combined_all_count','neutral_combined_identified_photon_count','exclusive_hemi0_nearby_photon_energy','exclusive_hemi0_hadron_photon_mass']),
 ('datamc-inclusive-04.md','Inclusive sample: event kinematics and radiative vetoes',['visible_tautau_mass','erad_over_ebeam','prad_over_pbeam','exclusive_pair_code'])]
used=set()
for f,t,vs in main_inc:
    slide(f,t,isub,[ifig(v) for v in vs]); used.update(vs)
rest=[v for v in IL if v not in used]
app_inc=[]
for i in range(0,len(rest),4):
    vs=rest[i:i+4]; f=f'appendix-inclusive-{i//4+1:02d}.md'
    slide(f,f'Appendix · inclusive sample ({i//4+1}/{(len(rest)+3)//4})',isub,[ifig(v) for v in vs]); app_inc.append(f)
# per-year views: shape overlays (ratio to 1994) and per-year absolute comparisons
def ofig(v):
    p=f'overlay-year/inclusive_1p1p-selected-{v}-overlay.svg'; assert os.path.exists(F+p),p
    return fig(p,IL[v]+', shape per year','overlay',v)
def yfig(y,v):
    p=f'year-{y}/inclusive_1p1p-selected-{v}-rate_lin.svg'; assert os.path.exists(F+p),p
    return fig(p,f'{y}: '+IL[v],'inclusive',v,f'year-{y}')
ysub=r'Inclusive sample · overlays: each year normalised to unit area, ratio panel to 1994, data and simulation separately'
slide('datamc-years-1.md','Year by year: do the shapes change between 1992 and 1995?',ysub,[ofig(v) for v in ['leadtrack_hemi0_p_over_pbeam','leadtrack_hemi0_costheta','exclusive_e_over_p','exclusive_hemi0_hcal_mean']],'Overlays: plots/all-years-baseline/overlay-year/*.svg and overlay.json (overlay_by year, reference 1994, normalisation in-range signed sumw per group, statistical errors only). No chi2 is computed for overlays.')
slide('datamc-years-2.md','Year by year: radiative energy and visible mass',r'Top: shapes per year (ratio to 1994). Bottom: absolute data/simulation for 1992 and 1995, the two years flagged on 2026-10-26',[ofig('erad_over_ebeam'),ofig('visible_tautau_mass'),yfig('1992','erad_over_ebeam'),yfig('1995','erad_over_ebeam')],'Per-year figures: plots/all-years-baseline/year-YYYY/; chi2 from year-YYYY/agreement.json. PROJECT_GUIDE 2026-10-27: neutral-shower inputs (erad_over_ebeam, EMNC energies) mismodelled in 1992 and in the 1995 peak period.')
app=[]
slide('appendix-years-01.md','Appendix · per year: H0 leading-track momentum',r'Absolute data/simulation per year, inclusive sample',[yfig(y,'leadtrack_hemi0_p_over_pbeam') for y in ['1992','1993','1994','1995']]); app.append('appendix-years-01.md')
slide('appendix-years-02.md','Appendix · per year: radiative energy, 1993 and 1994',r'Absolute data/simulation per year, inclusive sample',[yfig(y,'erad_over_ebeam') for y in ['1993','1994']]); app.append('appendix-years-02.md')
children=['ee','emu','epi','erho','mumu','mupi','murho','pipi','pirho','rhorho']
pretty={'ee':'$ee$','emu':r'$e\mu$','epi':r'$e\pi$','erho':r'$e\rho$','mumu':r'$\mu\mu$','mupi':r'$\mu\pi$','murho':r'$\mu\rho$','pipi':r'$\pi\pi$','pirho':r'$\pi\rho$','rhorho':r'$\rho\rho$'}
species={'ee':('$e$','$e$'),'emu':('$e$',r'$\mu$'),'epi':('$e$',r'$\pi$'),'erho':('$e$',r'$\rho$'),'mumu':(r'$\mu$',r'$\mu$'),'mupi':(r'$\mu$',r'$\pi$'),'murho':(r'$\mu$',r'$\rho$'),'pipi':(r'$\pi$',r'$\pi$'),'pirho':(r'$\pi$',r'$\rho$'),'rhorho':(r'$\rho$',r'$\rho$')}
# all-years child yields after the last cut (data, signed MC without Z_ee), from data/aggregate_allyears.py (aggregated.md)
import csv as _csv, collections as _col
def _child_yields():
    a=_col.defaultdict(lambda: [0,0.0]); last={}
    for r in _csv.DictReader(open('data/nersc-all-years-rq-20261026/cutflows/cutflow.csv')):
        if r['kind']!='cumulative' or not r['region'].startswith('inclusive_1p1p_'): continue
        ch=r['region'][15:]; last[ch]=r['cut']
    for r in _csv.DictReader(open('data/nersc-all-years-rq-20261026/cutflows/cutflow.csv')):
        if r['kind']!='cumulative' or not r['region'].startswith('inclusive_1p1p_'): continue
        ch=r['region'][15:]
        if r['cut']!=last[ch]: continue
        rest=r['sample'].split('/',1)[1]
        if rest=='data': a[ch][0]+=int(r['n'])
        elif rest.startswith('Total MC') or rest.startswith('Z_ee/'): continue
        else: a[ch][1]+=float(r['sumw'])
    return {k:(v[0],f'{v[1]:.6f}') for k,v in a.items()}
yields=_child_yields()
CL={'track_p_over_pbeam':r'$p/p_\mathrm{beam}$','track_p':r'$p$ [GeV]','track_costheta':r'$\cos\theta$','track_e_over_p':r'EM-calorimeter $E/p$','track_hcal_mean':r'HCAL mean per hit layer [GeV]','neutral_all_count':r'all neutrals','neutral_identified_photon_count':r'identified photons','neutral_failed_photon_count':r'non-photon neutrals','neutral_all_dr03_count':r'all neutrals, $\Delta R\lt 0.3$','rho_mass':r'$m_\rho$ candidate [GeV]','rho_energy':r'$E_\rho$ candidate [GeV]','rho_p':r'$p_\rho$ candidate [GeV]','rho_costheta':r'$\rho$ candidate $\cos\theta$','photon_energy':r'nearby photon $E$ [GeV]','photon_p':r'nearby photon $p$ [GeV]','photon_mass':r'nearby photon mass [GeV]','photon_costheta':r'nearby photon $\cos\theta$','neutral_energy':r'neutral-system $E$ [GeV]','neutral_mass':r'neutral-system mass [GeV]','neutral_count':r'photons in neutral system','neutral_costheta':r'neutral-system $\cos\theta$','neutral_p':r'neutral-system $p$ [GeV]','truth_species':r'true species (simulation)','track_charge':r'track charge','track_energy':r'track $E$ [GeV]','track_mass':r'track mass [GeV]'}
EV={'visible_tautau_mass':r'visible $m_{\tau\tau}$ [GeV]','erad_over_ebeam':r'$E_\mathrm{rad}/E_\mathrm{beam}$','prad_over_pbeam':r'$p_\mathrm{rad}/p_\mathrm{beam}$','identified_order_state':'candidate-ordering state'}
# four most informative per child: p/p_beam of both candidates + two channel-specific
main_vars={'ee':['candidate0_track_e_over_p','candidate1_track_e_over_p'],'emu':['candidate0_track_e_over_p','candidate1_track_hcal_mean'],'epi':['candidate1_track_e_over_p','candidate1_track_hcal_mean'],'erho':['candidate1_rho_mass','candidate1_photon_energy'],'mumu':['candidate0_track_hcal_mean','candidate1_track_hcal_mean'],'mupi':['candidate1_track_e_over_p','candidate1_track_hcal_mean'],'murho':['candidate1_rho_mass','candidate1_photon_energy'],'pipi':['candidate0_track_hcal_mean','candidate1_track_e_over_p'],'pirho':['candidate1_rho_mass','candidate1_photon_energy'],'rhorho':['candidate0_rho_mass','candidate1_rho_mass']}
def clabel(var,s0,s1):
    if var in EV: return EV[var]
    cand=int(var[9]); rest=var[11:]
    return f'cand. {cand} ({s0 if cand==0 else s1}): {CL[rest]}'
for ch in children:
    s0,s1=species[ch]; same=s0==s1
    order=('order by charge: cand. 0 negative, cand. 1 positive' if same else f'order by species: cand. 0 = {s0}, cand. 1 = {s1}')
    d=F+f'children-{ch}/'; allv=[f.split('-selected-')[1].replace('-rate_lin.svg','') for f in sorted(os.listdir(d)) if f.endswith('.svg')]
    def cf(var):
        p=f'children-{ch}/inclusive_1p1p_{ch}-selected-{var}-rate_lin.svg'; assert os.path.exists(F+p),p
        return fig(p,clabel(var,s0,s1),ch,var)
    mv=['candidate0_track_p_over_pbeam','candidate1_track_p_over_pbeam']+main_vars[ch]
    sub=f'1992–1995 · child {pretty[ch]} <span class="id">inclusive_1p1p_{ch}</span> · {order} · yield <span class="nw">{yields[ch][0]:,} data</span> / <span class="nw">{int(round(float(yields[ch][1]))):,} simulated</span>'
    slide(f'datamc-child-{ch}.md',f'Child {pretty[ch]}: four most informative variables',sub,[cf(v) for v in mv],f'Exact signed MC yield {yields[ch][1]} (Z_ee excluded). Four variables chosen: p/p_beam of both candidates plus the two channel-specific calorimeter / photon variables.')
    rest=[v for v in allv if v not in mv]
    for i in range(0,len(rest),4):
        f=f'appendix-child-{ch}-{i//4+1:02d}.md'
        slide(f,f'Appendix · child {pretty[ch]} ({i//4+1}/{(len(rest)+3)//4})',sub,[cf(v) for v in rest[i:i+4]]); app.append(f)
app=app_inc+app
open('data/appendix-order.txt','w').write('\n'.join(app)+'\n')
print('main+appendix regenerated; appendix slides:',len(app))
