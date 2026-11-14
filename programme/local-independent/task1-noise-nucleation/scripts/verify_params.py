"""Light independent re-verification of Task-4 parameters used by Task 1.
Routes: (a) analytic Landau values via d4model; (b) ODE barrier recomputed
from the saved profile npz by two quadratures (trapezoid on solver grid,
Simpson on a uniform interpolant grid); (c) kappa moment identity:
sum_g (g.n)^2 = 48 |n|^2 over the 24 scaled roots -> kappa/2 = 96;
(d) deterministic ModelB: seeded full pattern stays ordered (200 steps),
uniform state stays uniform (200 steps)."""
import sys, json
sys.path.insert(0, "/home/hatch/workspace/research/irh/co-scientist-tasks-2026-11-10/ws-a-core-computations")
import numpy as np, d4model as M
from scipy.integrate import simpson
out={}
out["python"]="Python 3.11.16 (conda env jacobian-conjecture-2d)"
out["numpy"]=np.__version__
re=M.r_eff(-0.18); ue=M.u_eff(-0.18)
Astar,Fmin,ex=M.stationary_minimum(-0.18)
out["r_eff"]=re; out["u_eff"]=ue; out["A_star"]=Astar; out["Fmin_one_mode"]=Fmin
# spinodal: r_eff=0 -> 3 psibar^2 -2 psibar -0.35 = 0
out["spinodal_psibar"]=float(np.roots([3,-2,-0.35])[1])
out["r_eff_at_-0.10"]=M.r_eff(-0.10)
# barrier-top (small stationary root) of f_mod
coeff=[3384.0,-192*ue,24*re,0.0]
roots=np.roots(coeff)
out["stationary_roots"]=[float(x.real) for x in roots if abs(x.imag)<1e-8]
out["f_at_small_root"]=float(M.f_mod(0.009800590186,-0.18))
# kappa moment: sum over scaled shell of (g.n)^2 for n=(1,0,0,0) and n=(1,1,0,0)/sqrt2
for n in [(1,0,0,0),(1,1,0,0)]:
    s=sum((np.dot(np.array(g),np.array(n,float)))**2 for g in M.SHELL)
    out[f"sum_g_dot2_{n}"]=float(s)
# ODE barrier from profile
prof=np.load("/home/hatch/workspace/research/irh/co-scientist-tasks-2026-11-10/ws-a-core-computations/tables/task4_ode_profile.npz")
r,A,dA=prof["r"],prof["A"],prof["dA"]
V=np.array([M.f_mod(a,-0.18,M.R) for a in A])
integrand=2*np.pi**2*r**3*(0.5*192.0*dA**2+V)
out["ode_DeltaF_trap"]=float(np.trapezoid(integrand,r))
rg=np.linspace(0,55,5501)
Ag=np.interp(rg,r,A); dAg=np.interp(rg,r,dA)
Vg=np.array([M.f_mod(a,-0.18,M.R) for a in Ag])
ig=2*np.pi**2*rg**3*(0.5*192.0*dAg**2+Vg)
out["ode_DeltaF_simpson_dense"]=float(simpson(ig,x=rg))
idx=np.where(A<Astar/2)[0]
out["ode_Rc"]=float(r[idx[0]])
out["ode_A0"]=float(A[0])
# deterministic ModelB checks (200 steps)
mb=M.ModelB(N=16,L=np.pi,q02=8.0,r=M.R,dt=0.005)
ph=mb.seed_full()
for _ in range(200): ph=mb.step(ph)
a=mb.analyze(ph)
out["seeded_full_200steps"]={"d4":a["d4"],"rms":a["rms"],"Fexc":float(a["Fexc"])}
ph=np.zeros((16,)*4,complex); ph[0,0,0,0]=M.PSIBAR*16**4
for _ in range(200): ph=mb.step(ph)
a=mb.analyze(ph)
out["uniform_200steps"]={"d4":a["d4"],"rms":a["rms"],"amp":a["amp"],"Fexc":float(a["Fexc"])}
print(json.dumps(out,indent=1))
json.dump(out,open("tables/verify_params.json","w"),indent=1)
