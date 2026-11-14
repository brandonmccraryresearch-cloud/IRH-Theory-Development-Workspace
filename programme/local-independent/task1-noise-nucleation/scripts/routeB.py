"""Route B (final): collective-coordinate Langevin in RADIAL DILATION lam
of the ODE critical profile, starting from the UNIFORM state.
A_lam(rho) = A_c(rho/lam); lam=1 saddle (E=555.20), lam<1 contracts,
lam>1 dilates (documented unstable direction, critical-droplet sec.5).
E(lam) precomputed on a grid (trapezoid, kappa=192, V=f_mod) and splined;
Langevin: gamma dlam/dt = -E'(lam) + sqrt(2*gamma*T) eta, gamma = metric
at lam=1 = 2*pi^2 int rho^3 (rho A_c')^2 drho. Event: first lam>=1.10.
Deterministic checks: lam0=0.98 decays, lam0=1.02 grows (RK4, E' from spline).
"""
import sys, json, math, argparse, time
sys.path.insert(0, "/home/hatch/workspace/research/irh/co-scientist-tasks-2026-11-10/ws-a-core-computations")
import numpy as np, d4model as M
from scipy.interpolate import UnivariateSpline
KAPPA=192.0
prof=np.load("/home/hatch/workspace/research/irh/co-scientist-tasks-2026-11-10/ws-a-core-computations/tables/task4_ode_profile.npz")
r=prof["r"]; A=prof["A"]; dA=prof["dA"]
def V_of(a): return np.array([M.f_mod(x,-0.18,M.R) for x in np.atleast_1d(a)])
w = 2*np.pi**2 * r**3
def profile_at(lam):
    x=r/lam
    return (np.interp(x,r,A,left=A[0],right=0.0),
            np.interp(x,r,dA,left=dA[0],right=0.0)/lam)
def E_of(lam):
    Al,dAl=profile_at(lam)
    return float(np.trapezoid(w*((0.5*KAPPA*dAl**2)+V_of(Al)), r))
gamma = float(np.trapezoid(w*(r*dA)**2, r))
# --- precompute E grid (cache) ---
import os
cache="tables/routeB_Egrid.npz"
if os.path.exists(cache):
    z=np.load(cache); lams=z["lam"]; Es=z["E"]
else:
    lams=np.concatenate([[0.0],np.linspace(0.02,1.60,158)])
    Es=np.array([E_of(l) if l>0 else 0.0 for l in lams])
    np.savez(cache,lam=lams,E=Es,gamma=np.array([gamma]))
    print("E grid computed", flush=True)
spl=UnivariateSpline(lams,Es,s=0.5,k=3)
print(f"gamma={gamma:.4f} E_spline(1)={float(spl(1.0)):.4f} E'(1)={float(spl.derivative()(1.0)):.3f} E''(1)={float(spl.derivative(2)(1.0)):.1f}")
print(f"E(0.2)={float(spl(0.2)):.2f} E(0.5)={float(spl(0.5)):.2f} E(1.4)={float(spl(1.4)):.2f}")
# small-lam fit E ~ a lam^2 + b lam^4 on [0.05,0.30]
m=(lams>=0.05)&(lams<=0.30)
coef=np.polyfit(lams[m]**2, Es[m], 2)  # Es = b*(lam^2)^2 + a*(lam^2) + c
a_fit, b_fit = coef[1], coef[0]
print(f"small-lam fit: a={a_fit:.1f} b={b_fit:.1f} c={coef[2]:.3f} -> E''(0)~{2*a_fit:.1f}")
Epp0=2*a_fit; Epp1=float(spl.derivative(2)(1.0))
dE=float(spl(1.0))-0.0
pref=2*math.pi*gamma/math.sqrt(Epp0*abs(Epp1))
print(f"Kramers: dE={dE:.2f} pref={pref:.3f} tau(T)={pref:.3f}*exp({dE:.2f}/T)")
# deterministic separatrix check with spline drift
Ep=spl.derivative()
def det_run(l0,tmax=600.0,dt=0.05):
    l=l0; t=0.0
    while t<tmax:
        k1=-float(Ep(l))/gamma; k2=-float(Ep(l+0.5*dt*k1))/gamma
        k3=-float(Ep(l+0.5*dt*k2))/gamma; k4=-float(Ep(l+dt*k3))/gamma
        l+=dt*(k1+2*k2+2*k3+k4)/6; t+=dt
        if l<0.02 or l>1.6: break
    return l,t
for l0 in [0.98,1.02]:
    print(f"deterministic lam0={l0} -> lam={det_run(l0)[0]:.4f} at t={det_run(l0)[1]:.1f}",flush=True)
p=argparse.ArgumentParser(); p.add_argument("Ts",nargs="+",type=float)
p.add_argument("--reps",type=int,default=20); p.add_argument("--tmax",type=float,default=1500.0)
p.add_argument("--dt",type=float,default=0.02); p.add_argument("--seed0",type=int,default=3000)
p.add_argument("--start",type=float,default=0.10); p.add_argument("--out",default="tables/routeB")
args=p.parse_args(); dt=args.dt
allout={"meta":{"gamma":gamma,"dE":dE,"prefactor":pref,"Epp0":Epp0,"Epp1":Epp1,
                "dt":dt,"start_lam":args.start,"route":"radial dilation of ODE critical profile"}}
for Ti,T in enumerate(args.Ts):
    rng=np.random.default_rng(args.seed0+100*Ti)
    recs=[]; paths=[]; t0=time.time()
    sig=math.sqrt(2*T/gamma*dt)
    for rep in range(args.reps):
        lam=args.start; t=0.0; t1=None; t110=None; path=[(0.0,lam)]
        nsteps=int(args.tmax/dt)
        for i in range(nsteps):
            lam += -(float(Ep(lam))/gamma)*dt + sig*rng.standard_normal()
            if lam<0.0: lam=-lam
            t+=dt
            if t1 is None and lam>=1.0: t1=t
            if t110 is None and lam>=1.10:
                t110=t; break
            if i%250==0: path.append((t,lam))
        recs.append({"rep":rep,"t_cross1":t1,"t_cross110":t110,"lam_end":float(lam)})
        if rep<5: paths.append({"rep":rep,"T":T,"path":path})
        print(f"T={T:g} rep {rep} t1={t1} t110={t110} lam_end={lam:.3f}",flush=True)
    allout[str(T)]={"T":T,"reps":args.reps,"tmax":args.tmax,"dt":dt,"start_lam":args.start,
                    "kramers_tau":pref*math.exp(dE/T),"records":recs,"paths":paths}
    done=sum(1 for x in recs if x["t_cross110"] is not None)
    tt=[x["t_cross110"] for x in recs if x["t_cross110"] is not None]
    print(f"T={T:g}: transited {done}/{args.reps} mean tau110={np.mean(tt) if tt else None} median={np.median(tt) if tt else None} ({time.time()-t0:.0f}s)",flush=True)
with open(args.out+".json","w") as f: json.dump(allout,f,indent=1)
print("ROUTE B DONE ->",args.out+".json")
