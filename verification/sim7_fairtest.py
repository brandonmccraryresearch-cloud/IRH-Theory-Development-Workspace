"""II.6 exact fair test, v93.0 parameters (now fully specified).
Damped wave on 16^4, L=2π (k=n integer), q0^2=7.5, r=-0.35, u=v=1, γ=1.2, Δt=0.05.
D4 shell: scaled roots (±2,±2,0,0), |k|^2=8, 24 modes, T=192.
Competitor: full integer shell |k|^2=7, 64 modes, T=0.
Linear penalties both 0.25 -> exactly degenerate; only the cubic term breaks the tie.
Semi-implicit spectral scheme for: ψ_tt + γ ψ_t = -δF/δψ.
"""
import numpy as np, itertools, sys, time

N = 16
n1d = np.fft.fftfreq(N, d=1.0/N)  # 0..7,-8..-1 (k=n since L=2π)
KX, KY, KZ, KW = np.meshgrid(n1d, n1d, n1d, n1d, indexing='ij')
K2 = KX**2 + KY**2 + KZ**2 + KW**2

q02 = 7.5
r, u, v, gamma, dt = -0.35, 1.0, 1.0, 1.2, 0.05

# shells
d4 = []
for i, j in itertools.combinations(range(4), 2):
    for s1 in (1, -1):
        for s2 in (1, -1):
            g = [0, 0, 0, 0]; g[i] = 2*s1; g[j] = 2*s2; d4.append(tuple(g))
assert len(d4) == 24
comp = []
for i in range(4):
    for s in itertools.product((1, -1), repeat=4):
        g = [0, 0, 0, 0]
        g[i] = 2*s[0]
        idx = 1
        for k in range(4):
            if k != i:
                g[k] = s[idx]; idx += 1
        comp.append(tuple(g))
assert len(comp) == 64
assert all(sum(x*x for x in g) == 7 for g in comp)

def gidx(g):
    return tuple(x % N for x in g)

d4_idx = [gidx(g) for g in d4]
comp_idx = [gidx(g) for g in comp]
# sanity: penalties
print("penalty D4:", (q02-8)**2, " penalty comp:", (q02-7)**2, flush=True)

def shell_power(ph, idxs):
    p = sum(abs(ph[i])**2 for i in idxs)
    tot = (np.abs(ph)**2).sum() - abs(ph[0,0,0,0])**2
    return float(p/tot)

def run(u_val, steps, r_val, seed=0, anneal=False, noise_amp=0.0):
    rng = np.random.default_rng(seed)
    omega2 = r_val + (q02-K2)**2
    ph = np.zeros((N,)*4, complex)
    p0 = 0.05*rng.standard_normal((N,)*4)
    ph = np.fft.fftn(p0)
    ph_prev = ph.copy()
    # semi-implicit damped wave:
    # (ψ^{n+1}-2ψ^n+ψ^{n-1})/dt² + γ(ψ^{n+1}-ψ^{n-1})/2dt = -ω²ψ^{n+1} + NL^n
    for step in range(1, steps+1):
        rr = r_val
        if anneal:
            rr = -0.05 + (-0.45+0.05)*step/steps
            omega2 = rr + (q02-K2)**2
        p = np.fft.ifftn(ph).real
        nl = u_val*np.fft.fftn(p*p) - v*np.fft.fftn(p*p*p)
        if noise_amp > 0:
            nl = nl + noise_amp*np.fft.fftn(rng.standard_normal((N,)*4))*(1-step/steps)
        denom = 1.0 + gamma*dt/2.0 + dt**2*omega2
        ph_new = (2*ph - ph_prev*(1.0-gamma*dt/2.0) + dt**2*nl)/denom
        ph_prev, ph = ph, ph_new
    return ph

t0=time.time()
ph = run(1.0, 6000, -0.35, seed=1)
d4f = shell_power(ph, d4_idx); cf = shell_power(ph, comp_idx)
print(f"[triad ON, direct quench] D4={d4f:.3f} competitor={cf:.3f}  (paper: 0.84 D4)", flush=True)

ph = run(0.0, 6000, -0.35, seed=1)
d4f = shell_power(ph, d4_idx); cf = shell_power(ph, comp_idx)
print(f"[triad OFF control]      D4={d4f:.3f} competitor={cf:.3f}  (paper: 0.44/0.56)", flush=True)

ph = run(1.0, 14000, -0.35, seed=2, anneal=True, noise_amp=0.5)
d4f = shell_power(ph, d4_idx); cf = shell_power(ph, comp_idx)
print(f"[triad ON, annealed]     D4={d4f:.3f} competitor={cf:.3f}  (paper: 1.00 D4)", flush=True)
print(f"elapsed {time.time()-t0:.0f}s", flush=True)
