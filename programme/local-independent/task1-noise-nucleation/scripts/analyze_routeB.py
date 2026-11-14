"""Analyse Route B waiting times: merge per-T files, exponential diagnostics,
Arrhenius fit log(tau) vs 1/T (slope = effective barrier), compare with
Kramers prediction (dE=555.04, prefactor 11.6 spline / 9.4 direct-curvature).
Also: t_cross1 vs t_cross110 lag, and aligned median transition paths."""
import json, glob
import numpy as np
rows=[]
for f in sorted(glob.glob("tables/routeB_T*.json")):
    d=json.load(open(f))
    for T,blk in d.items():
        if T=="meta": continue
        tt=np.array([r["t_cross110"] for r in blk["records"] if r["t_cross110"] is not None])
        t1=np.array([r["t_cross1"] for r in blk["records"] if r["t_cross1"] is not None])
        rows.append({"T":float(T),"n":len(tt),"mean":float(tt.mean()),"median":float(np.median(tt)),
                     "std":float(tt.std(ddof=1)),"cv":float(tt.std(ddof=1)/tt.mean()),
                     "min":float(tt.min()),"max":float(tt.max()),
                     "mean_t1":float(t1.mean()) if len(t1) else None,
                     "frac_transited":len(tt)/blk["reps"],"kramers":blk["kramers_tau"],
                     "t110":tt.tolist(),"t1":t1.tolist()})
        print(f"T={T}: n={len(tt)} mean={tt.mean():.1f} median={np.median(tt):.1f} std={tt.std(ddof=1):.1f} "
              f"CV={tt.std(ddof=1)/tt.mean():.2f} (exponential: CV=1, median/mean=0.693) "
              f"median/mean={np.median(tt)/tt.mean():.3f} Kramers={blk['kramers_tau']:.1f} ratio={tt.mean()/blk['kramers_tau']:.2f}")
# Arrhenius fit on log(mean)
x=np.array([1/r["T"] for r in rows]); y=np.array([np.log(r["mean"]) for r in rows])
A=np.vstack([x,np.ones_like(x)]).T
slope,intercept=np.linalg.lstsq(A,y,rcond=None)[0]
pred=slope*x+intercept
print(f"Arrhenius fit: log(mean tau) = {slope:.1f}*(1/T) + {intercept:.3f}; residuals={np.round(y-pred,3)}")
print(f"  effective barrier from slope = {slope:.1f} (ODE saddle DeltaF* = 555.20)")
print(f"  prefactor from intercept = {np.exp(intercept):.3f} (Kramers 11.6 spline / 9.4 direct)")
# also fit on log(median) (median = tau*ln2 for exponential)
ym=np.array([np.log(r["median"]) for r in rows])
s2,i2=np.linalg.lstsq(A,ym,rcond=None)[0]
print(f"Median fit: slope={s2:.1f} intercept={i2:.3f} prefactor(median/ln2)={np.exp(i2)/np.log(2):.3f}")
json.dump({"rows":rows,"arrhenius_mean":{"slope":float(slope),"intercept":float(intercept),"prefactor":float(np.exp(intercept))},
           "arrhenius_median":{"slope":float(s2),"intercept":float(i2)}},open("tables/routeB_summary.json","w"),indent=1)
