#!/usr/bin/env python3
"""Independent seed-construction check (no integration).

1. d4model (ws-a) seed_droplet at its own operating box L=pi, N=16:
   reproduce Task-4 step-0 diagnostics (d4, rms) with d4model.analyze AND
   with a from-scratch FFT shell-power computation.
2. Same construction at L=2*pi, N=16 in d4model, shell read at the
   (2,2,0,0)-permutation indices.
3. This task's build_seed (run_critical_seed.py) at L=2*pi, N=18:
   shell fraction before projection (full FFT) vs after |k_i|<=4 projection.
Prints numbers; no files written except stdout.
"""
import sys
import numpy as np

sys.path.insert(0, "/home/hatch/workspace/research/irh/co-scientist-tasks-2026-11-10/ws-a-core-computations")
import d4model as M


def shell_frac_d4model(ph, labels):
    """labels: list of integer fft-array index tuples for the shell modes."""
    n = ph.shape[0]
    p = np.abs(ph) ** 2
    pnz = p.sum() - p[(0,) * 4]
    sh = sum(p[tuple(x % n for x in lab)] for lab in labels)
    # ph is unnormalised fftn: power per mode = |ph_k|^2 / N^8
    return float(sh / pnz)


# --- 1. d4model at L=pi, N=16 (Task 4 geometry) ---
mb = M.ModelB(N=16, L=np.pi, q02=8.0, r=M.R, dt=0.005)
for radius in (0.6, 0.8):
    ph = mb.seed_droplet(radius, amp=M.A_STAR)
    a = mb.analyze(ph)
    # ROOTS are unscaled (1,1,0,0); fft index = label mod 16
    sf = shell_frac_d4model(ph, M.ROOTS)
    fld = np.fft.ifftn(ph).real
    print(f"d4model L=pi R={radius}: analyze d4={a['d4']:.6f} rms={a['rms']:.6f} "
          f"amp={a['amp']:.6f} | independent shell_frac={sf:.6f} "
          f"rms_check={float(np.sqrt(((fld-fld.mean())**2).mean())):.6f}")

# --- 2. d4model seed at L=2*pi, N=16 ---
mb2 = M.ModelB(N=16, L=2 * np.pi, q02=8.0, r=M.R, dt=0.005)
for radius in (0.6, 1.2, 2.4):
    ph = mb2.seed_droplet(radius, amp=M.A_STAR)
    fld = np.fft.ifftn(ph).real
    rms = float(np.sqrt(((fld - fld.mean()) ** 2).mean()))
    # shell at physical k=(2,2,0,0) perms: fftfreq index = k (L=2pi => k integer)
    sf = shell_frac_d4model(ph, M.SHELL)
    print(f"d4model L=2pi R={radius}: independent shell_frac={sf:.6f} rms={rms:.6f} "
          f"mean={float(fld.mean()):.6f}")

# --- 3. this task's build_seed, before/after projection ---
sys.path.insert(0, "/home/hatch/workspace/research/irh/co-scientist-tasks-2026-11-10/local-independent/task3-critical-seed")
import importlib.util
spec = importlib.util.spec_from_file_location(
    "field_study",
    "/home/hatch/workspace/research/irh/co-scientist-tasks-2026-11-10/4d-field-test/run_field_study.py")
fmod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(fmod)
spec2 = importlib.util.spec_from_file_location(
    "run_critical_seed",
    "/home/hatch/workspace/research/irh/co-scientist-tasks-2026-11-10/local-independent/task3-critical-seed/run_critical_seed.py")
rcs = importlib.util.module_from_spec(spec2)
spec2.loader.exec_module(rcs)
m = fmod.Field(18, 4)
for radius in (0.6, 1.2, 2.4, 2.7):
    y, info = rcs.build_seed(m, fmod.KSTAR, 1.0, radius)
    # unprojected: rebuild phi in real space via inverse of projected? Instead
    # recompute raw field: use y with mask removed is not available, so rebuild
    # the real-space seed here with the same formula on the same grid.
    n = 18
    xs = np.linspace(0.0, 2 * np.pi, n, endpoint=False)
    X = np.meshgrid(xs, xs, xs, xs, indexing="ij")
    d2 = sum((x - np.pi) ** 2 for x in X)
    env = 0.5 * (1.0 - np.tanh(4.0 * (np.sqrt(d2) - radius)))
    pat = np.zeros_like(X[0])
    for g in fmod.KSTAR:
        pat += np.cos(g[0] * X[0] + g[1] * X[1] + g[2] * X[2] + g[3] * X[3])
    psi = -0.18 + rcs.A_STAR * env * pat
    psi += (-0.18 - psi.mean())
    phi = psi + 0.18
    yraw = m.fft(phi)  # unmasked
    praw = np.sum(m.weight * np.abs(yraw) ** 2)
    a_raw = m.coefficients(yraw)
    sh_raw = float(np.sum(np.abs(a_raw) ** 2))
    pproj = float(np.sum(m.weight * np.abs(y) ** 2))
    a_proj = m.coefficients(y)
    sh_proj = float(np.sum(np.abs(a_proj) ** 2))
    print(f"task3 L=2pi R={radius}: raw shell_frac={sh_raw/praw:.6f} rms={float(np.sqrt(np.mean(phi**2))):.6f} "
          f"| projected shell_frac={sh_proj/pproj:.6f} power_retained={pproj/praw:.6f} "
          f"r_eq={info['r_eq']:.4f}")
print("VERIFY_SEED DONE")
