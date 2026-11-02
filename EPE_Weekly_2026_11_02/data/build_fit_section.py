"""Render archived Model C results; no fitting or new pseudo-experiments."""
from pathlib import Path
import json
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
D=Path(__file__).resolve().parents[1]
P=D.parents[1]/'artifacts/joint-fit-20261031/modelC/combined-ml'
O=D/'public/figures/fit';O.mkdir(exist_ok=True)
a=np.load(P/'covariance_modelC.npz',allow_pickle=True)
t=np.load(P/'toys_modelC_sm.npz')
r=json.load(open(P/'results_modelC.json'))
C=a['C']; ref=a['reference']; sig=np.sqrt(C.diagonal()); names=a['bc_names'].tolist()
labels=[r'$B^+_'+x[-1]+'$' for x in names[:3]]+[r'$B^-_'+x[-1]+'$' for x in names[3:6]]+[r'$C_{'+x[2:]+'}$' for x in names[6:]]
plt.rcParams.update({'font.size':12,'text.color':'#e6e8ed','axes.labelcolor':'#e6e8ed','xtick.color':'#bec5cf','ytick.color':'#bec5cf','axes.edgecolor':'#68707a','axes.facecolor':'none','figure.facecolor':'none','savefig.transparent':True,'svg.fonttype':'path'})
def save(fig,name):fig.savefig(O/name,bbox_inches='tight',pad_inches=.12);plt.close(fig)
# Exact independent-region contribution to covariance of the combined estimator.
Fs=[]
for i in range(16):
 k=np.asarray(a['keep_local'][i],int);ix=a['region_flat_index'][i][k]
 X=a['T'].reshape(15,-1).T[ix];V=a['V0_blocks'][i][np.ix_(k,k)]
 Fs.append(X.T@np.linalg.solve(V,X))
assert np.allclose(sum(Fs),a['F'],rtol=1e-8,atol=1e-7)
parts=np.array([C@F@C for F in Fs]);assert np.allclose(parts.sum(0),C)
groups=[[0],[1,2],[3],[4],[5],[6,7],[8,9],[10,11],[12,13],[14,15]]
glabs=[r'$\pi\pi$',r'$\pi\rho+\rho\pi$',r'$\rho\rho$',r'$ee$',r'$\mu\mu$',r'$e\mu+\mu e$',r'$\pi e+e\pi$',r'$\pi\mu+\mu\pi$',r'$\rho e+e\rho$',r'$\rho\mu+\mu\rho$']
q=np.array([0]*6+[1,0,0,0,-1,0,0,0,1.])
vecs=[np.eye(15)[i] for i in [2,5,6,10,14]]+[q]
frac=np.array([[sum(v@parts[i]@v for i in g)/(v@C@v)*100 for v in vecs] for g in groups])
fig,ax=plt.subplots(figsize=(8.2,4.0));im=ax.imshow(frac,aspect='auto',cmap='YlGnBu',vmin=0,vmax=50)
ax.set_xticks(range(6),[labels[i] for i in [2,5,6,10,14]]+['$W$']);ax.xaxis.tick_top();ax.set_yticks(range(10),glabs)
for i in range(10):
 for j in range(6):ax.text(j,i,f'{frac[i,j]:.1f}',ha='center',va='center',fontsize=11,color='#17202a' if frac[i,j]<28 else 'white')
ax.tick_params(length=0);save(fig,'region-budget.svg')
fig,axs=plt.subplots(1,2,figsize=(10,3.2),gridspec_kw={'width_ratios':[1,1.5]})
for ax,inds in zip(axs,[range(6),range(6,15)]):
 ax.errorbar(list(inds),ref[list(inds)],yerr=sig[list(inds)],fmt='o',color='#d5b56d',capsize=4,ms=5);ax.axhline(0,color='#68707a',lw=.7);ax.set_xticks(list(inds),[labels[i] for i in inds],rotation=45);ax.grid(axis='y',alpha=.15);ax.spines[['top','right']].set_visible(False)
axs[0].set_title('Polarisation',color='#e6e8ed');axs[1].set_title('Spin correlations',color='#e6e8ed');save(fig,'sdm-errors.svg')
pulls=t['C_delta']/sig
width=pulls.std(0,ddof=1);mean=pulls.mean(0)
fig,axs=plt.subplots(2,1,figsize=(9,3.6),sharex=True)
for ax,y,target,label in [(axs[0],mean,0,'Pull mean'),(axs[1],width,1,'Pull width')]:
 ax.axhline(target,color='#b8bdc5',lw=1);ax.errorbar(range(15),y,yerr=1/np.sqrt(2000) if target==0 else 1/np.sqrt(3998),fmt='o',color='#d5b56d',capsize=3);ax.set_ylabel(label);ax.grid(axis='y',alpha=.15);ax.spines[['top','right']].set_visible(False)
axs[1].set_xticks(range(15),labels,rotation=40);save(fig,'modelc-pulls.svg')
cs=ref+t['C_delta']; vals=[t['C_W'],t['C_Bell'],-np.log2((1+(cs**4).sum(1))/(1+(cs**2).sum(1)))]
fig,axs=plt.subplots(1,3,figsize=(11,3.0))
for ax,v,name,bound in zip(axs,vals,['$W$','$|C_{kk}-C_{rr}|$',r'$\mathcal{M}_2$'],[0,np.sqrt(2),0]):
 ax.hist(v,bins=34,color='#89a8c1',alpha=.8,density=True);ax.axvline(bound,color='#e09b7d',ls='--',lw=1.6);ax.set_xlabel(name);ax.set_ylabel('Toy density');ax.spines[['top','right']].set_visible(False)
 axs[0].set_xlim(-.1,2.5)
save(fig,'modelc-qis-toys.svg')
# Actual archived response, not a legacy illustration.
fig,ax=plt.subplots(figsize=(6.5,3.3));x=np.arange(10)/5-.9; mu=a['mu0'][14,0];slope=a['T'][14,14,0]
for dc,col in [(-.3,'#89a8c1'),(0,'#d5b56d'),(.3,'#df987e')]:ax.stairs(mu+dc*slope,np.linspace(-1,1,11),color=col,label=rf'$\Delta C_{{kk}}={dc:+.1f}$',lw=1.8)
ax.errorbar(x,mu,np.sqrt(mu),fmt='.',color='#eeeeee',label='Asimov',ms=5)
ax.set_xlabel(r'$x_k^+x_k^-$');ax.set_ylabel('Expected events / bin');ax.legend(frameon=False,fontsize=10);ax.spines[['top','right']].set_visible(False);save(fig,'modelc-template.svg')
out={'source':str(P),'reference':ref.tolist(),'sigma':sig.tolist(),'region_variance_percent':frac.tolist(),'region_groups':[a['regions'][g].tolist() for g in groups],'fisher_closure_max_abs':float(np.max(abs(sum(Fs)-a['F']))),'pull_width_range':[float(width.min()),float(width.max())],'derived':r['derived']['C'],'yield':float(a['mu0'][0].sum())}
(D/'data/fit-section.json').write_text(json.dumps(out,indent=2))
print('Validated Fisher closure; yield',out['yield'],'pull widths',out['pull_width_range'])
