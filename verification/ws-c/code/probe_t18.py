"""Probe the t=18 anomaly: print Parseval-consistent diagnostics at t=17, 17.5, 18.
If <A> explodes while rms stays 0.38, the analyze() diagnostic itself is at
fault; if Parseval holds, the shell really blew up and rms must follow.
"""
import math
import sys

sys.path.insert(0, __file__.rsplit('/', 1)[0])
import numpy as np

import irh_models as M

dt = 0.005
grid = M.Grid(16, math.pi)
K2 = grid.K2
q02, r, u, v, psibar, a_star = 8.0, -0.35, 1.0, 1.0, -0.18, 0.0776
omega2 = r + (q02 - K2) ** 2
vecs = M.d4_roots()
ph = np.zeros((16,) * 4, complex)
ph[0, 0, 0, 0] = psibar * 16 ** 4
for n in vecs:
    ph[grid.gidx(n)] = a_star * 16 ** 4
den = 1.0 + dt * K2 * omega2
filt = (K2 < 200).astype(float)
targets = {3400: 17.0, 3500: 17.5, 3600: 18.0}
for step in range(1, 3601):
    p = np.fft.ifftn(ph).real
    nl = filt * (u * np.fft.fftn(p * p) - v * np.fft.fftn(p * p * p))
    ph = (ph + dt * K2 * nl) / den
    if step in targets:
        t = targets[step]
        p = np.fft.ifftn(ph).real
        amps = np.array([ph[grid.gidx(n)] / 16 ** 4 for n in vecs])
        mag = np.abs(amps)
        parseval = float((np.abs(ph) ** 2).sum() / 16 ** 8)  # = mean(p^2)
        print(f"t={t}: rms={float(np.sqrt(((p - p.mean()) ** 2).mean())):.6f} "
              f"mean(p^2)={float((p ** 2).mean()):.6f} parseval={parseval:.6f} "
              f"max|ph|={float(np.abs(ph).max()):.3e} <A>={float(mag.mean()):.6f} "
              f"max|A|={float(mag.max()):.6f} psibar={float(ph[0,0,0,0].real / 16**4):+.6f} "
              f"finite={bool(np.isfinite(p).all())}", flush=True)
