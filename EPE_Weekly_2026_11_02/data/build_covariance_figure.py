"""Normalised archived event covariance, pion-pair region; no fit."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
D=Path(__file__).resolve().parents[1]
a=np.load(D.parents[1]/'artifacts/joint-fit-20261031/modelC/combined-ml/covariance_modelC.npz')
v=a['V0_blocks'][0]; sd=np.sqrt(v.diagonal()); corr=np.divide(v,np.outer(sd,sd),out=np.zeros_like(v),where=np.outer(sd,sd)>0)
labels=[rf'$x_{i}^+$' for i in 'nrk']+[rf'$x_{i}^-$' for i in 'nrk']+[rf'$x_{i}^+x_{j}^-$' for i in 'nrk' for j in 'nrk']
plt.rcParams.update({'font.size':10,'text.color':'#e6e8ed','axes.labelcolor':'#e6e8ed','xtick.color':'#bec5cf','ytick.color':'#bec5cf','axes.edgecolor':'#68707a','svg.fonttype':'path'})
fig,ax=plt.subplots(figsize=(5.5,4.3));im=ax.imshow(corr,vmin=0,vmax=1,cmap='Blues',interpolation='nearest')
ax.set_xticks(np.arange(15)*10+4.5,labels,rotation=90,fontsize=9);ax.set_yticks(np.arange(15)*10+4.5,labels,fontsize=9);ax.tick_params(length=0)
for k in range(1,15):
 ax.axhline(k*10-.5,color='#536170',lw=.25);ax.axvline(k*10-.5,color='#536170',lw=.25)
ax.axhline(59.5,color='#d5b56d',lw=1.5);ax.axvline(59.5,color='#d5b56d',lw=1.5)
c=fig.colorbar(im,ax=ax,pad=.025,fraction=.04);c.set_label(r'$V_{ab}/\sqrt{V_{aa}V_{bb}}$');c.outline.set_visible(False)
fig.savefig(D/'public/figures/fit/region-covariance.svg',bbox_inches='tight',pad_inches=.08,transparent=True)
