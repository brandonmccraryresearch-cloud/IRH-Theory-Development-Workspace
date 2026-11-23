"""Bisect the late-onset Model B instability: run the shipped sim6 Model B
attractor with monitoring every 100 steps (rms, max|psi|, psi-bar, <A>),
stop at first non-finite value. Usage: python bisect_instability.py DT TMAX
"""
import math
import sys
import time

sys.path.insert(0, __file__.rsplit('/', 1)[0])
import numpy as np

import irh_models as M

dt = float(sys.argv[1]) if len(sys.argv) > 1 else 0.005
tmax = float(sys.argv[2]) if len(sys.argv) > 2 else 30.0
steps = int(tmax / dt)

grid = M.Grid(16, math.pi)
K2 = grid.K2
q02, r, u, v, psibar, a_star = 8.0, -0.35, 1.0, 1.0, -0.18, 0.0776
omega2 = r + (q02 - K2) ** 2
vecs = M.d4_roots()
analyze, _ = M.make_analyzer(grid, q02, r, u, v, vecs)
ph = np.zeros((16,) * 4, complex)
ph[0, 0, 0, 0] = psibar * 16 ** 4
for n in vecs:
    ph[grid.gidx(n)] = a_star * 16 ** 4
den = 1.0 + dt * K2 * omega2
filt = (K2 < 200).astype(float)
t0 = time.time()
print(f"dt={dt} tmax={tmax} steps={steps}")
for step in range(1, steps + 1):
    p = np.fft.ifftn(ph).real
    nl = filt * (u * np.fft.fftn(p * p) - v * np.fft.fftn(p * p * p))
    ph = (ph + dt * K2 * nl) / den
    if step % 100 == 0 or step == steps:
        t = step * dt
        p = np.fft.ifftn(ph).real
        ok = bool(np.isfinite(p).all())
        d = analyze(ph) if ok else None
        print(f"t={t:6.2f} finite={ok} rms={float(np.sqrt(((p - p.mean()) ** 2).mean())) if ok else float('nan'):.6f} "
              f"max|psi|={float(np.abs(p).max()) if ok else float('nan'):.6f} "
              f"psibar={d['psibar'] if d else float('nan'):+.6f} <A>={d['amp'] if d else float('nan'):.6f} "
              f"D4={d['d4'] if d else float('nan'):.4f}", flush=True)
        if not ok:
            print(f"BLOW-UP first seen at t={t} (step {step}); elapsed {time.time() - t0:.0f}s")
            break
else:
    print(f"stable through t={tmax}; elapsed {time.time() - t0:.0f}s")
