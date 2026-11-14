"""Analyse Route A: per-D transition fractions, waiting times (first amp>=0.04,
confirmed at next sample), pre-transition stationary amplitude vs OU
prediction amp_rms = 0.012*sqrt(D), conservation and final-state checks.
Writes tables/routeA_summary.json + .csv."""
import json, glob
import numpy as np
rows=[]
for f in sorted(glob.glob("tables/routeA_*.json")):
    if "summary" in f: continue
    d=json.load(open(f))
    for D,blk in d.items():
        recs=blk["records"]
        tt=np.array([r["t_amp04_first"] for r in recs if r["t_amp04_first"] is not None],dtype=float)
        # pre-transition stationary amp: samples before first amp>=0.04 (or all if none)
        pre=[]
        for r in recs:
            s=r["series"]
            before=[q["amp"] for q in s if r["t_amp04_first"] is None or q["t"]<r["t_amp04_first"]]
            pre += before[1:]  # skip t=0
        psimax=max(abs(r["final"]["psibar"]+0.18) for r in recs)
        rows.append({"D":float(D),"n":len(recs),
          "n_transited":int(len(tt)),"frac":float(len(tt)/len(recs)),
          "waiting_times":tt.tolist(),
          "mean_wait":float(tt.mean()) if len(tt) else None,
          "median_wait":float(np.median(tt)) if len(tt) else None,
          "pre_amp_mean":float(np.mean(pre)) if pre else None,
          "pre_amp_std":float(np.std(pre)) if pre else None,
          "pre_amp_n":len(pre),
          "ou_pred_amp_rms":0.012*np.sqrt(float(D)),
          "psibar_max_dev":float(psimax),
          "final_amp":[r["final"]["amp"] for r in recs],
          "final_rms":[r["final"]["rms"] for r in recs],
          "final_d4":[r["final"]["d4"] for r in recs]})
        print(f"D={D}: transited {len(tt)}/{len(recs)} wait={tt.tolist()} "
              f"pre-amp mean={np.mean(pre):.4f} std={np.std(pre):.4f} OU pred rms={0.012*np.sqrt(float(D)):.4f} "
              f"psibar dev max={psimax:.2e}")
rows=sorted(rows,key=lambda r:r["D"])
json.dump(rows,open("tables/routeA_summary.json","w"),indent=1)
with open("tables/routeA_summary.csv","w") as f:
    f.write("D,n,n_transited,frac_transited,mean_wait,median_wait,pre_amp_mean,pre_amp_std,ou_pred_amp_rms,psibar_max_dev\n")
    for r in rows:
        f.write(f"{r['D']},{r['n']},{r['n_transited']},{r['frac']},{r['mean_wait']},{r['median_wait']},{r['pre_amp_mean']},{r['pre_amp_std']},{r['ou_pred_amp_rms']},{r['psibar_max_dev']}\n")
print("wrote tables/routeA_summary.json/.csv")
