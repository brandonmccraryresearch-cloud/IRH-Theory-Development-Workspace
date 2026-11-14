"""Write the noise-calibration numbers (from calibrate_noise.py output,
recomputed here exactly the same way) to CSV."""
import numpy as np
N=16; L=np.pi; dt=0.005
X=np.fft.fftfreq(N,d=L/N)*2*np.pi
KX,KY,KZ,KW=np.meshgrid(X,X,X,X,indexing='ij'); K2=KX**2+KY**2+KZ**2+KW**2
filt=((K2>=4)&(K2<=16)).astype(float)
def draw(rng,D):
    z=rng.standard_normal((N,)*4)+1j*rng.standard_normal((N,)*4)
    rev=np.roll(z[::-1,::-1,::-1,::-1],1,axis=(0,1,2,3)); z=0.5*(z+np.conj(rev))
    return np.sqrt(2*D*dt)*N**2*np.sqrt(K2)*filt*z
rng=np.random.default_rng(20261114)
with open("tables/noise_calibration.csv","w") as f:
    f.write("D,per_step_dpsi_rms_mean,per_step_dpsi_rms_std,max_abs_imag_psi\n")
    for D in [0.001,0.003,0.01,0.03,0.1,0.3,1.0,3.0,10.0]:
        rm=[]; im=[]
        for _ in range(20):
            dp=draw(rng,D); ps=np.fft.ifftn(dp); rm.append(ps.real.std()); im.append(np.abs(ps.imag).max())
        f.write(f"{D},{np.mean(rm):.6f},{np.std(rm):.6f},{np.max(im):.2e}\n")
        print(f"D={D:g} rms={np.mean(rm):.6f} +- {np.std(rm):.6f}")
