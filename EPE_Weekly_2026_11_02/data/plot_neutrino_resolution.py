"""Slide resolution summaries from archived all-years hold metrics; no synthetic distributions."""
import json
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
p=Path(__file__).resolve().parents[1]
src=Path('/Users/avencastmini/ZtautauLEP/artifacts/ml-all-years-v1-20261027/nu-eval-hold-metrics.json')
d=json.loads(src.read_text())
plt.rcParams.update({'font.size':11,'axes.spines.top':False,'axes.spines.right':False,'svg.fonttype':'none','font.family':'DejaVu Sans'})
fig,axs=plt.subplots(1,3,figsize=(13,3.8),gridspec_kw={'width_ratios':[1,1,1.1]})
colors=['#b56b0a','#176fab'];methods=['analytical','nu'];labels=['Analytical default','EveNet']
for ax,key,title,lim in zip(axs[:2],['median_deg','q84_deg'],['Typical angular error','84% containment angle'],[2.55,4.65]):
 for method,col,label in zip(methods,colors,labels):
  vals=[d['angle']['inclusive'][method][m][key] for m in ['e','mu','pi','rho']]
  ax.plot(range(4),vals,marker='o',color=col,label=label,lw=1.8,ms=6)
  for i,v in enumerate(vals): ax.annotate(f'{v:.2f}',(i,v),xytext=(0,8 if method=='analytical' else -17),textcoords='offset points',ha='center',fontsize=10,color=col)
 ax.set_xticks(range(4),['$e$','$\\mu$','$\\pi$','$\\rho$']);ax.set_xlabel('True decay mode of the leg');ax.set_ylabel('Angular error [deg]');ax.set_ylim(0,lim);ax.set_xlim(-.3,3.3);ax.set_title(title,fontsize=13,pad=12);ax.grid(axis='y',alpha=.18)
ax=axs[2];xx=np.arange(4)
for method,col,label,offset in zip(methods,colors,labels,[-.18,.18]):
 vals=[d['four_momentum']['inclusive'][method]['minus'][c]['rms'] for c in ['px','py','pz','E']]
 ax.bar(xx+offset,vals,width=.34,color=col,label=label)
 for x,v in zip(xx+offset,vals):ax.text(x,v+.04,f'{v:.2f}',ha='center',fontsize=9,color=col)
ax.set_xticks(xx,['$p_x$','$p_y$','$p_z$','$E$']);ax.set_ylim(0,1.65);ax.set_ylabel('Residual RMS about mean [GeV]');ax.set_title('$\\tau^-$ momentum residuals',fontsize=13,pad=12);ax.grid(axis='y',alpha=.18);ax.set_axisbelow(True)
fig.legend(*axs[0].get_legend_handles_labels(),loc='upper center',ncol=2,frameon=False,bbox_to_anchor=(.5,1.01))
fig.subplots_adjust(left=.055,right=.99,bottom=.19,top=.77,wspace=.36)
fig.savefig(p/'public/figures/ml/resolution-explained.svg',bbox_inches='tight',pad_inches=.15)
