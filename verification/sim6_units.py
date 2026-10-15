"""Faithful II.8 / II.6 tests with the paper's q0^2 = 8.0.

Key correction: the paper tunes q0^2 = 8.0 with the D4 shell ON q0.
With shell modes k = (2pi/L)n, |n|^2 = 2, this requires (2pi/L)^2 * 2 = 8,
i.e. L = pi. Then ONLY the D4 shell is linearly unstable:
  |n|^2=0: w2 = -0.35+64    = 63.65 stable
  |n|^2=1: w2 = -0.35+16    = 15.65 stable
  |n|^2=2: w2 = -0.35            unstable (D4 shell)
  |n|^2=4: w2 = -0.35+64    = 63.65 stable (harmonics damped)
Using L=16 (= q0^2 0.308) instead leaves the mean and harmonics unstable,
which corrupted the earlier runs. This script uses L = pi.

Tests:
  A. II.8 attractor: seed 24 modes at A*=0.0776 in phase, psibar=-0.18,
     Model B and Model A. Expect amplitude unchanged (4 s.f.), D4 power 1.0.
  B. II.6 noise quench: damped wave from noise, u=1 vs u=0. Measure D4
     shell fraction, dominant-mode count, triad phase locking <cos S>.
"""
import numpy as np, math, itertools, sys

N = 16
L = math.pi
X = np.fft.fftfreq(N, d=L/N) * 2 * math.pi
KX, KY, KZ, KW = np.meshgrid(X, X, X, X, indexing='ij')
K2 = KX**2 + KY**2 + KZ**2 + KW**2
q02 = 8.0
r, u, v, gamma, dt = -0.35, 1.0, 1.0, 1.0, 0.02
omega2 = r + (q02-K2)**2
A_STAR, PSIBAR = 0.0776, -0.18
vecs = []
for i,j in itertools.combinations(range(4),2):
    for s1 in (1,-1):
        for s2 in (1,-1):
            n=[0,0,0,0]; n[i]=s1; n[j]=s2; vecs.append(tuple(n))
vset = set(vecs)
triads = []
for ia, ib in itertools.combinations(range(24),2):
    need = tuple(-vecs[ia][d]-vecs[ib][d] for d in range(4))
    if need in vset:
        ic = vecs.index(need)
        if ic > ib: triads.append((ia,ib,ic))
def gidx(n): return tuple(x % N for x in n)
n2 = np.round(K2/(2*X[1])**2).astype(int) if False else None
kfac = (2*math.pi/L)**2
n2 = np.round(K2/kfac).astype(int)

print("linear w2 by shell:", {s: round(float(omega2[n2==s].mean()),3)
      for s in range(7) if (n2==s).sum()}, flush=True)

def free_energy(psi_hat):
    p = np.fft.ifftn(psi_hat).real
    quad = 0.5*np.sum(np.fft.ifftn(omega2*psi_hat).real*p)/N**4
    return quad + np.mean(-u/3*p**3 + v/4*p**4)

def analyze(psi_hat):
    amps = np.array([psi_hat[gidx(n)]/N**4 for n in vecs])
    mag = np.abs(amps); pha = np.angle(amps)
    p = np.abs(psi_hat)**2
    pnz = p.sum() - p[0,0,0,0]
    d4 = float((mag**2).sum()/(pnz/N**8))
    ndom = int((mag > 0.5*mag.max()).sum())
    S = np.array([pha[a]+pha[b]+pha[c] for a,b,c in triads])
    lock = float(np.mean(np.cos(S)))
    pb = float(psi_hat[0,0,0,0].real/N**4)
    fld = np.fft.ifftn(psi_hat).real
    rms = float(np.sqrt(((fld-fld.mean())**2).mean()))
    F = free_energy(psi_hat)
    # excess over the uniform state (the paper's F convention)
    pu = np.zeros_like(psi_hat); pu[0,0,0,0] = psi_hat[0,0,0,0]
    Fexc = F - free_energy(pu)
    return pb, mag.mean(), d4, ndom, lock, rms, Fexc

def test_attractor(conserved_B, steps, dt_use=0.02):
    """Seeded II.8 test. conserved_B=True -> true Model B; False -> Model A."""
    ph = np.zeros((N,)*4, complex)
    ph[0,0,0,0] = PSIBAR*N**4
    for n in vecs: ph[gidx(n)] = A_STAR*N**4
    den = 1.0 + dt_use*K2*omega2          # Model B semi-implicit
    denA = 1.0 + dt_use*omega2            # Model A semi-implicit
    filt = (K2 < 200).astype(float)       # kill stiff high-k nonlinear noise
    tag = "ModelB" if conserved_B else "ModelA"
    print(f"[{tag} attractor]", "seed: A=0.07760 D4=1.0000 rms=0.3802", flush=True)
    for step in range(1, steps+1):
        p = np.fft.ifftn(ph).real
        nl = filt*(u*np.fft.fftn(p*p) - v*np.fft.fftn(p*p*p))
        if conserved_B:
            ph = (ph + dt_use*K2*nl)/den
        else:
            ph = (ph + dt_use*nl)/denA
        if step in (500, 1500, steps):
            pb,A,d4,ndom,lock,rms,F = analyze(ph)
            print(f"  t={step*dt_use:5.1f} psibar={pb:+.5f} <A>={A:.5f} D4={d4:.4f} "
                  f"modes={ndom}/24 rms={rms:.4f} Fexc={F:.6f}", flush=True)

def test_quench(uu, steps, seedn=1):
    """II.6-style noise quench with the damped wave equation."""
    rng = np.random.default_rng(seedn)
    psi = 1e-2*rng.standard_normal((N,)*4); psi -= psi.mean()
    ph = np.fft.fftn(psi); vh = np.zeros_like(ph)
    # low-pass filter: RK4 needs dt*w < 2.8; w^2 = (8-K2)^2, so keep K2<64
    filt = (K2 < 64).astype(float)
    ph *= filt; vh *= filt
    for step in range(1, steps+1):
        def rhs(a, b):
            af, bf = a*filt, b*filt
            p = np.fft.ifftn(af).real
            nl = filt*(uu*np.fft.fftn(p*p) - v*np.fft.fftn(p*p*p))
            return bf, -gamma*bf - omega2*af + nl
        k1p,k1v = rhs(ph, vh)
        k2p,k2v = rhs(ph+dt/2*k1p, vh+dt/2*k1v)
        k3p,k3v = rhs(ph+dt/2*k2p, vh+dt/2*k2v)
        k4p,k4v = rhs(ph+dt*k3p, vh+dt*k3v)
        ph += dt/6*(k1p+2*k2p+2*k3p+k4p)
        vh += dt/6*(k1v+2*k2v+2*k3v+k4v)
        ph *= filt; vh *= filt
    pb,A,d4,ndom,lock,rms,F = analyze(ph)
    print(f"[quench u={uu}] D4={d4:.4f} dominant={ndom}/24 <cos triad>={lock:.3f} "
          f"rms={rms:.4f} Fexc={F:.6f}", flush=True)

if __name__ == "__main__":
    which = sys.argv[1] if len(sys.argv) > 1 else "all"
    if which in ("all", "attractor"):
        test_attractor(True, 6000, 0.005)
        test_attractor(False, 1500)
    if which in ("all", "quench"):
        test_quench(1.0, 2500)
        test_quench(0.0, 2500)
