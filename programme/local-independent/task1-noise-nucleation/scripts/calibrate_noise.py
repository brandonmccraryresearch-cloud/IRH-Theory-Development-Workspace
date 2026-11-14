"""Calibrate band-limited conserved noise (Route A), no dynamics.
Definition: per step, draw z with Re,Im ~ N(0,1) on the 16^4 Fourier grid,
Hermitian-symmetrise (same roll/conj map as ModelB.step), then
  dph(k) = sqrt(2*D*dt) * N^2 * sqrt(K2(k)) * filt(k) * z(k),
filt = 1 for 4 <= K2 <= 16, else 0.  (k=0 term is zero: mean exactly conserved.)
Measure: per-step dpsi rms, imag residue, mean, and mode counts.
"""
import sys
sys.path.insert(0, "/home/hatch/workspace/research/irh/co-scientist-tasks-2026-11-10/ws-a-core-computations")
import numpy as np, d4model as M
N=16; L=np.pi; dt=0.005
X = np.fft.fftfreq(N, d=L/N)*2*np.pi
KX,KY,KZ,KW = np.meshgrid(X,X,X,X,indexing='ij')
K2 = KX**2+KY**2+KZ**2+KW**2
filt = ((K2>=4)&(K2<=16)).astype(float)
print("band modes:", int(filt.sum()), "total modes:", N**4, "mean K2 in band:", float(K2[filt>0].mean()))
print("shell modes K2=8:", int((K2==8).sum()))
def dph_draw(rng, D):
    z = rng.standard_normal((N,)*4) + 1j*rng.standard_normal((N,)*4)
    rev = np.roll(z[::-1,::-1,::-1,::-1],1,axis=(0,1,2,3))
    z = 0.5*(z+np.conj(rev))
    return np.sqrt(2*D*dt)*N**2*np.sqrt(K2)*filt*z
rng=np.random.default_rng(20261114)
for D in [0.001,0.003,0.01,0.03,0.1,0.3,1.0]:
    rmss=[]; ims=[]
    for _ in range(20):
        dph=dph_draw(rng,D)
        dpsi=np.fft.ifftn(dph)
        rmss.append(dpsi.real.std()); ims.append(np.abs(dpsi.imag).max())
    print(f"D={D:g} dpsi_rms={np.mean(rmss):.6f} +- {np.std(rmss):.6f}  max|imag|={np.max(ims):.2e}  dph00={dph[0,0,0,0]:.2e}")
