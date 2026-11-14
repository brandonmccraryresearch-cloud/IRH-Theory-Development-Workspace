"""Figures for Route A (full 4D Model B + conserved band noise)."""
import json
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
rows=json.load(open("tables/routeA_summary.json"))
alld={}
for f in ["tables/routeA_pilot.json","tables/routeA_pilot2.json","tables/routeA_scan.json","tables/routeA_scan2.json"]:
    import os
    if os.path.exists(f):
        d=json.load(open(f))
        for D,blk in d.items(): alld.setdefault(float(D),[]).extend(blk["records"])
fig,axs=plt.subplots(2,2,figsize=(10,8))
ax=axs[0,0]
Ds=np.array([r["D"] for r in rows]); fr=np.array([r["frac"] for r in rows])
ax.semilogx(Ds,fr,"o-")
for r in rows:
    for t in r["waiting_times"]: ax.plot(r["D"],0,"",)  # no-op keep
ax.set_xlabel("noise strength $D$"); ax.set_ylabel("fraction transited (amp $\\geq 0.04$)")
ax.set_title("(a) Transition fraction vs $D$"); ax.set_ylim(-0.05,1.05)
ax=axs[0,1]
for D in sorted(alld):
    r=alld[D][0]
    t=np.array([q["t"] for q in r["series"]]); a=np.array([q["amp"] for q in r["series"]])
    ax.plot(t,a,label=f"$D={D:g}$ (first rep)")
ax.axhline(0.0098,color="k",ls="--",lw=1,label="barrier top $A_{small}=0.0098$")
ax.axhline(0.04,color="C3",ls="--",lw=1,label="event amp $=0.04$")
ax.axhline(0.0776,color="k",ls=":",lw=1,label="$A^*=0.0776$")
ax.set_xlabel("time $t$"); ax.set_ylabel("mean shell amplitude")
ax.legend(fontsize=7,loc="lower right"); ax.set_title("(b) Transition paths: shell amplitude vs time")
ax=axs[1,0]
# one row per D (scan rows preferred; pilot D=3 row duplicated in summary)
seen={}
for r in rows:
    if r["D"] not in seen or "scan" in str(r.get("source","")): seen[r["D"]]=r
uu=sorted(seen.values(),key=lambda r:r["D"])
Ds2=np.array([r["D"] for r in uu]); pre=np.array([r["pre_amp_mean"] for r in uu])
ou=np.array([r["ou_pred_amp_rms"] for r in uu])
ax.loglog(Ds2,pre,"o-",label="measured pre-transition mean amp (scan)")
ax.loglog(Ds2,ou,"k--",label="OU prediction $0.012\\sqrt{D}$ (rms)")
ax.loglog(Ds2,0.886*ou,"k:",label="OU mean $|a| = 0.886\times$ rms")
ax.set_xlabel("$D$"); ax.set_ylabel("shell amplitude"); ax.legend(fontsize=8)
ax.set_title("(c) Stationary fluctuations vs $D$ (before transition)")
ax=axs[1,1]
for D in sorted(alld):
    for r in alld[D][:1]:
        t=np.array([q["t"] for q in r["series"]]); f=np.array([q["Fexc"] for q in r["series"]])
        ax.plot(t,f,label=f"$D={D:g}$")
ax.axhline(-0.00773,color="k",ls=":",lw=1,label="ordered $F_{exc}=-0.00773$")
ax.set_xlabel("time $t$"); ax.set_ylabel("$F_{exc}$ (density)")
ax.legend(fontsize=8); ax.set_title("(d) Free-energy density along paths")
fig.tight_layout(); fig.savefig("figures/routeA_waiting_times.png",dpi=150)
print("saved figures/routeA_waiting_times.png")
