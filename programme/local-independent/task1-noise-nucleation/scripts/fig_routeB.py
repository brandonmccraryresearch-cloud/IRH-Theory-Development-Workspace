"""Figures for Route B (collective-coordinate Langevin, dilation lam)."""
import json, glob
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from scipy.interpolate import UnivariateSpline
# --- E(lam) curve from cached grid ---
z=np.load("tables/routeB_Egrid.npz"); lams=z["lam"]; Es=z["E"]
spl=UnivariateSpline(lams,Es,s=0.5,k=3)
ll=np.linspace(0,1.6,321)
# --- waiting times ---
rows={}
for f in sorted(glob.glob("tables/routeB_T*.json")):
    d=json.load(open(f))
    for T,blk in d.items():
        if T=="meta": continue
        rows[float(T)]=blk
fig,axs=plt.subplots(2,2,figsize=(10,8))
# (a) E(lam) with saddle
ax=axs[0,0]; ax.plot(ll,spl(ll),color="C0"); ax.axvline(1.0,color="k",ls="--",lw=1)
ax.axhline(0,color="k",lw=0.7); ax.plot([1.0],[float(spl(1.0))],"ro",ms=5)
ax.annotate("saddle $\\lambda=1$\n$E=555.2$",xy=(1.0,555),xytext=(1.15,420),fontsize=9,
            arrowprops=dict(arrowstyle="->",lw=0.8))
ax.set_xlabel("$\\lambda$ (radial dilation of critical profile)"); ax.set_ylabel("$E(\\lambda)$")
ax.set_title("(a) Energy along the dilation path")
# (b) waiting-time histograms (log x)
ax=axs[0,1]
for T,blk in rows.items():
    tt=np.array([r["t_cross110"] for r in blk["records"] if r["t_cross110"] is not None])
    ax.hist(np.log10(tt),bins=8,alpha=0.45,label=f"$T={T:.0f}$",density=True)
ax.set_xlabel("$\\log_{10} \\tau$ (waiting time to $\\lambda\\geq1.10$)")
ax.set_ylabel("density"); ax.legend(fontsize=8); ax.set_title("(b) Waiting-time distributions (20 reps each)")
# (c) Arrhenius: log mean tau vs 1/T
ax=axs[1,0]
Ts=np.array(sorted(rows)); means=np.array([np.mean([r["t_cross110"] for r in rows[T]["records"]]) for T in Ts])
meds=np.array([np.median([r["t_cross110"] for r in rows[T]["records"]]) for T in Ts])
x=1/Ts
A=np.vstack([x,np.ones_like(x)]).T
slope,inter=np.linalg.lstsq(A,np.log(means),rcond=None)[0]
xx=np.linspace(x.min()*0.9,x.max()*1.05,50)
ax.plot(xx,slope*xx+inter,"k--",lw=1,label=f"fit slope $={slope:.0f}$")
logtt=[np.log(np.array([r["t_cross110"] for r in rows[T]["records"]])) for T in Ts]
se=np.array([lt.std(ddof=1)/np.sqrt(len(lt)) for lt in logtt])
ax.errorbar(x,np.log(means),yerr=se,fmt="o",capsize=3,label="mean $\pm$ SE of $\log\tau$")
# Kramers line
ax.plot(xx,np.log(11.617)+555.04*xx,"C1:",lw=1.2,label="Kramers $11.6\\,e^{555/T}$")
ax.set_xlabel("$1/T$"); ax.set_ylabel("$\\log \\langle\\tau\\rangle$")
ax.legend(fontsize=8); ax.set_title("(c) Arrhenius fit: slope $567\\approx\\Delta F^*=555$")
# (d) aligned median transition paths
ax=axs[1,1]
grid=np.linspace(-30,2,65)
for T,blk in rows.items():
    curves=[]
    for p in blk["paths"]:
        t=np.array([q[0] for q in p["path"]]); lam=np.array([q[1] for q in p["path"]])
        tc=[r["t_cross110"] for r in blk["records"] if r["rep"]==p["rep"]]
        if not tc or tc[0] is None: continue
        curves.append(np.interp(grid,t-tc[0],lam,left=np.nan,right=np.nan))
    if curves:
        med=np.nanmedian(np.array(curves),axis=0)
        ax.plot(grid,med,label=f"$T={T:.0f}$ (n={len(curves)})")
ax.axhline(1.0,color="k",ls="--",lw=1); ax.axvline(0,color="k",ls=":",lw=1)
ax.set_xlabel("$t-t_{\\mathrm{cross}}$ (time from $\\lambda=1.10$ crossing)")
ax.set_ylabel("$\\lambda$"); ax.legend(fontsize=8)
ax.set_title("(d) Median paths, aligned at crossing")
fig.tight_layout(); fig.savefig("figures/routeB_waiting_times.png",dpi=150)
print("saved figures/routeB_waiting_times.png")
