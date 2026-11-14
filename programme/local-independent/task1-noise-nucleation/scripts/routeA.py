"""Route A: full 4D Model B (d4model, N=16, L=pi, dt=0.005) + explicitly
defined conserved band-limited noise, uniform start psi=-0.18.
Noise (per step, added AFTER the deterministic semi-implicit step):
  draw z with Re,Im ~ N(0,1) on the 16^4 Fourier grid, Hermitian-symmetrise
  (same roll/conj map as ModelB.step), then
  dph(k) = sqrt(2*D*dt) * N^2 * sqrt(K2(k)) * filt(k) * z(k),
  filt = 1 for 4 <= K2 <= 16 else 0.
The sqrt(K2) factor is the divergence of a random flux (conserved: k=0 term
is zero, so the spatial mean is exactly unchanged); the band limit keeps the
noise on the pattern-forming modes (shell K2=8 + sidebands) instead of
injecting most power at grid scale (see calibrate_noise.py: white flux noise
gives Fexc ~ 2.4 at D=1e-5 and no shell response). D is a model noise
strength, NOT a physical temperature: no fluctuation-dissipation temperature
is assigned and no physical rate is claimed.
Event: first sample (every `sample` steps) with D4>=0.9 and rms>=0.3,
confirmed at the next sample or by the ordered end state.
Usage: routeA.py D1 D2 ... --reps N --nsteps S --seed0 S0 --out prefix
"""
import sys, json, time, argparse
sys.path.insert(0, "/home/hatch/workspace/research/irh/co-scientist-tasks-2026-11-10/ws-a-core-computations")
import numpy as np, d4model as M
N=16; L=np.pi; DT=0.005
X = np.fft.fftfreq(N, d=L/N)*2*np.pi
KX,KY,KZ,KW = np.meshgrid(X,X,X,X,indexing='ij')
K2 = KX**2+KY**2+KZ**2+KW**2
FILT = ((K2>=4)&(K2<=16)).astype(float)
SQRTK = np.sqrt(K2)*FILT
def symmetrise(z):
    rev = np.roll(z[::-1,::-1,::-1,::-1],1,axis=(0,1,2,3))
    return 0.5*(z+np.conj(rev))
def noise_dph(rng, D):
    z = rng.standard_normal((N,)*4) + 1j*rng.standard_normal((N,)*4)
    z = symmetrise(z)
    return np.sqrt(2*D*DT)*N**2*SQRTK*z
def run_one(mb, D, seed, nsteps, sample):
    rng=np.random.default_rng(seed)
    ph=np.zeros((N,)*4,complex); ph[0,0,0,0]=M.PSIBAR*N**4
    series=[]; t_wait=None; confirmed=False
    t_amp098=None; t_amp04=None; stop_at=None; nsteps_used=None
    for s in range(0, nsteps+1, sample):
        if stop_at is not None and s>=stop_at:
            nsteps_used=s; break
        if s>0:
            for _ in range(sample):
                ph = mb.step(ph)
                ph = ph + noise_dph(rng, D)
                ph = symmetrise(ph)
        a=mb.analyze(ph)
        fld=np.fft.ifftn(ph).real
        series.append({"step":s,"t":s*DT,"d4":a["d4"],"rms":a["rms"],"amp":a["amp"],
                       "Fexc":float(a["Fexc"]),"lock":a["lock"],"ndom":a["ndom"],
                       "psibar":a["psibar"],"max_imag":float(np.abs(np.fft.ifftn(ph).imag).max())})
        if t_amp098 is None and a["amp"]>=0.0098: t_amp098=s*DT
        if t_amp04 is None and a["amp"]>=0.04:
            t_amp04=s*DT; t_wait=t_amp04
        elif t_wait is not None and not confirmed and a["amp"]>=0.04:
            confirmed=True; stop_at=s+250
    nsteps_used = nsteps_used if nsteps_used is not None else nsteps
    fin=series[-1]
    outcome = "growth" if (fin["d4"]>0.9 and fin["rms"]>0.3) else "no-transition"
    return {"D":D,"seed":seed,"nsteps":nsteps,"nsteps_used":nsteps_used,"t_wait_first":t_wait,
            "t_wait_confirmed": (t_wait if confirmed else None),
            "t_amp098_first":t_amp098,"t_amp04_first":t_amp04,
            "outcome":outcome,"final":fin,"series":series}
p=argparse.ArgumentParser(); p.add_argument("Ds",nargs="+",type=float)
p.add_argument("--reps",type=int,default=6); p.add_argument("--nsteps",type=int,default=3000)
p.add_argument("--sample",type=int,default=100); p.add_argument("--seed0",type=int,default=5000)
p.add_argument("--out",default="tables/routeA")
args=p.parse_args()
mb=M.ModelB(N=16,L=np.pi,q02=8.0,r=M.R,dt=DT)
allout={}
for Di,D in enumerate(args.Ds):
    recs=[]; t0=time.time()
    for rep in range(args.reps):
        rec=run_one(mb,D,args.seed0+100*Di+rep,args.nsteps,args.sample)
        recs.append({k:v for k,v in rec.items()})
        print(f"D={D:g} rep {rep} outcome={rec['outcome']} t_amp04={rec['t_amp04_first']} t_amp098={rec['t_amp098_first']} "
              f"final amp={rec['final']['amp']:.4f} d4={rec['final']['d4']:.3f} rms={rec['final']['rms']:.3f} Fexc={rec['final']['Fexc']:.4f} "
              f"psibar={rec['final']['psibar']:.6f} ({time.time()-t0:.0f}s)",flush=True)
    allout[str(D)]={"D":D,"reps":args.reps,"nsteps":args.nsteps,"dt":DT,"records":recs}
    with open(args.out+".json","w") as f: json.dump(allout,f,indent=1)
print("ROUTE A DONE ->",args.out+".json")
