"""Bootstrap the Arrhenius slope for Route B (resample waiting times within
each T, refit log(mean tau) vs 1/T, 10000 bootstraps) + CSV export of the
per-T waiting times and the E(lam) curve."""
import json, glob
import numpy as np
rows={}
for f in sorted(glob.glob("tables/routeB_T*.json")):
    d=json.load(open(f))
    for T,blk in d.items():
        if T=="meta": continue
        rows[float(T)]=np.array([r["t_cross110"] for r in blk["records"]])
Ts=np.array(sorted(rows)); x=1/Ts
def slope_of(means): 
    A=np.vstack([x,np.ones_like(x)]).T
    return np.linalg.lstsq(A,np.log(means),rcond=None)[0]
s0,i0=slope_of(np.array([rows[T].mean() for T in Ts]))
rng=np.random.default_rng(4242)
slopes=[]
for _ in range(10000):
    means=np.array([rng.choice(rows[T],size=len(rows[T]),replace=True).mean() for T in Ts])
    slopes.append(slope_of(means)[0])
slopes=np.array(slopes)
print(f"slope={s0:.1f} intercept={i0:.3f}")
print(f"bootstrap slope: median={np.median(slopes):.1f} 16-84%=[{np.percentile(slopes,16):.1f},{np.percentile(slopes,84):.1f}] 2.5-97.5%=[{np.percentile(slopes,2.5):.1f},{np.percentile(slopes,97.5):.1f}]")
print(f"P(slope within 5% of 555.2) = {np.mean(np.abs(slopes-555.2)<0.05*555.2):.3f}")
# CSVs
with open("tables/routeB_waiting_times.csv","w") as f:
    f.write("T,rep,t_cross1,t_cross110\n")
    for fn in sorted(glob.glob("tables/routeB_T*.json")):
        d=json.load(open(fn))
        for T,blk in d.items():
            if T=="meta": continue
            for r in blk["records"]:
                f.write(f"{T},{r['rep']},{r['t_cross1']},{r['t_cross110']}\n")
z=np.load("tables/routeB_Egrid.npz")
with open("tables/routeB_Elam.csv","w") as f:
    f.write("lam,E\n")
    for l,e in zip(z["lam"],z["E"]): f.write(f"{l:.4f},{e:.4f}\n")
print("wrote tables/routeB_waiting_times.csv, tables/routeB_Elam.csv")
json.dump({"slope":float(s0),"intercept":float(i0),
           "bootstrap_median":float(np.median(slopes)),
           "bootstrap_16_84":[float(np.percentile(slopes,16)),float(np.percentile(slopes,84))],
           "bootstrap_2p5_97p5":[float(np.percentile(slopes,2.5)),float(np.percentile(slopes,97.5))]},
          open("tables/routeB_bootstrap.json","w"),indent=1)
