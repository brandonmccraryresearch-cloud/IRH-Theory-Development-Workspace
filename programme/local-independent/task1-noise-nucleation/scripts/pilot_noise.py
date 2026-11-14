"""Pilot: calibrate conserved-noise increment in full 4D Model B.
Noise defined in task1 script (see routeA.py): per step, real-space flux
J_i ~ N(0,1) per grid point, divergence via spectral derivatives, increment
dpsi_hat = fftn(sqrt(2*D*dt)*div). Measure: mean conservation, per-step rms
increment of psi, and stationary shell rms over 2000 steps at several D.
"""
import sys, time
sys.path.insert(0, "/home/hatch/workspace/research/irh/co-scientist-tasks-2026-11-10/ws-a-core-computations")
import numpy as np, d4model as M
PY = "/home/hatch/miniconda3/envs/jacobian-conjecture-2d/bin/python"
print("python", PY)
mb = M.ModelB(N=16, L=np.pi, q02=8.0, r=M.R, dt=0.005)
N=16; L=np.pi; dt=0.005
X = np.fft.fftfreq(N, d=L/N)*2*np.pi
KX,KY,KZ,KW = np.meshgrid(X,X,X,X,indexing='ij')
Ks=[KX,KY,KZ,KW]
def noise_increment(rng, D):
    div = np.zeros((N,)*4)
    for Ki in Ks:
        J = rng.standard_normal((N,)*4)
        div += np.fft.ifftn(1j*Ki*np.fft.fftn(J)).real
    return np.fft.fftn(np.sqrt(2*D*dt)*div)
rng=np.random.default_rng(12345)
for D in [1e-6, 1e-5, 1e-4, 1e-3]:
    ph0 = np.zeros((N,)*4, complex); ph0[0,0,0,0]=M.PSIBAR*N**4
    dph = noise_increment(rng, D)
    dpsi = np.fft.ifftn(dph).real
    print(f"D={D:g} per-step dpsi rms={dpsi.std():.6f} mean={dpsi.mean():.2e} dph00={dph[0,0,0,0]:.2e}")
# stationary rms under dynamics+noise, uniform start, 2000 steps, sample every 250
for D in [1e-5, 1e-4, 1e-3]:
    rng=np.random.default_rng(7)
    ph = np.zeros((N,)*4, complex); ph[0,0,0,0]=M.PSIBAR*N**4
    t0=time.time()
    for s in range(1,2001):
        ph = mb.step(ph)
        ph = ph + noise_increment(rng, D)
        # re-symmetrise (same map as ModelB.step)
        rev = np.roll(ph[::-1,::-1,::-1,::-1],1,axis=(0,1,2,3))
        ph = 0.5*(ph+np.conj(rev))
        if s%500==0:
            a=mb.analyze(ph)
            print(f"D={D:g} step {s} rms={a['rms']:.4f} d4={a['d4']:.3f} amp={a['amp']:.4f} Fexc={a['Fexc']:.6f} psibar={a['psibar']:.6f}", flush=True)
    print(f"D={D:g} 2000 steps in {time.time()-t0:.0f}s", flush=True)
