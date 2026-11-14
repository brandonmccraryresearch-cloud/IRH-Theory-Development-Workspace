#!/usr/bin/env python3
"""Independent-integrator cross-check (second machine route).

Evolves the SAME localized seed with the ws-a semi-implicit spectral
Model B solver (d4model.ModelB, sim6 scheme) instead of the field-test
ETD2 Galerkin solver. Two geometries:
  (a) L=2*pi, N=16, dt=0.005, 6000 steps (t=30) -- same box as Task 3;
  (b) L=pi,   N=16, dt=0.005, 6000 steps (t=30) -- Task 4 geometry, to
      confirm the cross-check harness reproduces Task 4 growth there.
Diagnostics are computed from scratch here (shell = physical
k=(2,2,0,0) permutations, read at fft-array indices k mod N), NOT via
d4model.analyze, whose root labels assume L=pi.
Classification mirrors Task 4: growth = shell_frac>0.9 and rms>0.3;
decay = shell_frac<0.2 and rms<0.1; else marginal. Sampled every 250 steps.
Usage: python crosscheck_d4model.py --box 2pi --radii 1.2 2.7 --out .
"""
import argparse, csv, json, sys, time
from pathlib import Path
import numpy as np

sys.path.insert(0, "/home/hatch/workspace/research/irh/co-scientist-tasks-2026-11-10/ws-a-core-computations")
import d4model as M

NSTEP = 6000
SAMPLE_EVERY = 250


def shell_labels(n, L):
    # FFT-array index of physical k=(2,2,0,0) perms: index = k * L / (2*pi).
    # L=2*pi -> index (2,2,0,0) = M.SHELL; L=pi -> index (1,1,0,0) = M.ROOTS.
    vecs = M.SHELL if abs(L - 2 * np.pi) < 1e-9 else M.ROOTS
    labs = []
    for g in vecs:
        labs.append(tuple(int(x) % n for x in g))
    return labs


def diag(mb, ph, labs):
    p = np.abs(ph) ** 2
    pnz = p.sum() - p[(0,) * 4]
    sh = sum(p[lab] for lab in labs)
    d4 = float(sh / pnz) if pnz > 0 else 0.0
    fld = np.fft.ifftn(ph).real
    rms = float(np.sqrt(((fld - fld.mean()) ** 2).mean()))
    fexc = float(mb.free_energy(ph) - mb.free_energy(
        np.where(np.indices(ph.shape) == 0, ph, 0) if False else _uniform(mb, ph)))
    return dict(d4=d4, rms=rms, Fexc=fexc, mean=float(fld.mean()))


def _uniform(mb, ph):
    pu = np.zeros_like(ph)
    pu[(0,) * 4] = ph[(0,) * 4]
    return pu


def run(mb, labs, radius, amp_fac, tag):
    ph = mb.seed_droplet(radius, amp=amp_fac * M.A_STAR)
    d0 = diag(mb, ph, labs)
    series = [dict(step=0, **d0)]
    t0 = time.time()
    for s in range(1, NSTEP + 1):
        ph = mb.step(ph)
        if s % SAMPLE_EVERY == 0:
            series.append(dict(step=s, **diag(mb, ph, labs)))
    d = diag(mb, ph, labs)
    el = time.time() - t0
    outcome = ("growth" if (d["d4"] > 0.9 and d["rms"] > 0.3)
               else "decay" if (d["d4"] < 0.2 and d["rms"] < 0.1)
               else "marginal")
    print(json.dumps(dict(tag=tag, box_L=float(mb.L), radius=radius,
                          amp_fac=amp_fac, outcome=outcome,
                          d4_init=round(d0["d4"], 4), rms_init=round(d0["rms"], 4),
                          d4=d["d4"], rms=d["rms"], Fexc=d["Fexc"],
                          elapsed_seconds=round(el, 1))), flush=True)
    return dict(tag=tag, box_L=float(mb.L), radius=radius, amp_fac=amp_fac,
                outcome=outcome, final=d, initial=d0, series=series,
                elapsed_seconds=el)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--box", choices=["2pi", "pi"], required=True)
    ap.add_argument("--radii", type=float, nargs="+", required=True)
    ap.add_argument("--alpha", type=float, default=1.0)
    ap.add_argument("--out", default=".")
    args = ap.parse_args()
    out = Path(args.out)
    out.mkdir(parents=True, exist_ok=True)
    L = 2 * np.pi if args.box == "2pi" else np.pi
    mb = M.ModelB(N=16, L=L, q02=8.0, r=M.R, dt=0.005)
    labs = shell_labels(16, L)
    rows = []
    for r in args.radii:
        rows.append(run(mb, labs, r, args.alpha, f"xcheck_{args.box}"))
    with open(out / f"crosscheck_{args.box}.json", "w") as f:
        json.dump(rows, f, indent=1)
    print("CROSSCHECK DONE", flush=True)


if __name__ == "__main__":
    main()
