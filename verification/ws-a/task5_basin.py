"""Task 5 — basin of the full 24-mode D4 pattern under Model B.

14 runs, 6000 steps each, L = pi, q0^2 = 8.0, psibar = -0.18:
 - random noise starts, seeds 1-6, amp 0.05;
 - partial-pattern starts hex6, fcc12, sq4, sq8 at A*;
 - perturbed full-pattern starts: phase RMS dphi in {0.1, 0.5, 1.0} rad,
   and amplitude +-20% (pairwise, so the field stays real).
Phases are assigned antisymmetrically (phi_{-n} = -phi_n) and amplitudes
pairwise (|ph[n]| = |ph[-n]|) so every seed is a real field.
Dominant modes are identified data-first from the final spectrum
(mags > 0.5 max) and matched against the sub-pattern index sets.
Protocol difference vs the manuscript's annealed run (damped-wave
dynamics, q0^2 = 7.5) is stated in the report.
"""
import sys, json, time
import numpy as np

sys.path.insert(0, ".")
import d4model as M

NSTEP = 6000
SAMPLE_EVERY = 250
ROOTS = M.ROOTS

# index sets of the sub-patterns in the ROOTS ordering. NOTE: SUBPATTERNS
# holds SCALED shell vectors (2,2,0,0); Fourier-space seeding and ROOTS
# indexing need the UNSCALED labels in SUBPATTERN_LABELS.
SUB_IDX = {}
for nm, vs in M.SUBPATTERN_LABELS.items():
    SUB_IDX[nm] = set(ROOTS.index(tuple(v)) for v in vs)
SUB_IDX["full24"] = set(range(24))


def antisym_phases(rng, delta):
    """phases with phi_{-n} = -phi_n (real field)."""
    ph = np.zeros(24)
    done = set()
    for i, n in enumerate(ROOTS):
        if i in done:
            continue
        j = ROOTS.index(tuple(-np.array(n)))
        if j == i:
            ph[i] = 0.0
        else:
            v = rng.normal(0.0, delta)
            ph[i] = v
            ph[j] = -v
        done.add(i)
        done.add(j)
    return ph


def pairwise_amps(rng, frac):
    """per-pair amplitude factors in [1-frac, 1+frac], equal on +-n."""
    f = np.ones(24)
    done = set()
    for i, n in enumerate(ROOTS):
        if i in done:
            continue
        j = ROOTS.index(tuple(-np.array(n)))
        v = rng.uniform(1 - frac, 1 + frac)
        f[i] = v
        f[j] = v
        done.add(i)
        done.add(j)
    return f


def identify(mags):
    """Dominant-mode index set and best sub-pattern match (overlap)."""
    dom = set(np.where(mags > 0.5 * mags.max())[0].tolist()) \
        if mags.max() > 0 else set()
    best = None
    for nm, s in SUB_IDX.items():
        inter = len(dom & s)
        score = inter / max(len(dom), 1) * inter / max(len(s), 1)
        if best is None or score > best[1]:
            best = (nm, score, inter, len(dom), len(s))
    return dom, best


def run_case(mb, ph, tag):
    a0 = mb.analyze(ph)
    series = [{"step": 0, "d4": a0["d4"], "ndom": a0["ndom"],
               "lock": a0["lock"], "Fexc": a0["Fexc"], "rms": a0["rms"]}]
    t0 = time.time()
    for s in range(1, NSTEP + 1):
        ph = mb.step(ph)
        if s % SAMPLE_EVERY == 0:
            a = mb.analyze(ph)
            series.append({"step": s, "d4": a["d4"], "ndom": a["ndom"],
                           "lock": a["lock"], "Fexc": a["Fexc"],
                           "rms": a["rms"]})
    a = mb.analyze(ph)
    dom, best = identify(a["mags"])
    dt = time.time() - t0
    print(f"[{tag}] D4={a['d4']:.3f} ndom={a['ndom']} lock={a['lock']:.3f} "
          f"Fexc={a['Fexc']:.6f} rms={a['rms']:.3f} "
          f"dominant={sorted(dom)} best={best[0]} "
          f"(overlap {best[2]}/{best[4]}) in {dt:.0f}s", flush=True)
    return {"tag": tag,
            "final": {k: a[k] for k in ("d4", "ndom", "lock", "Fexc",
                                       "rms", "amp", "psibar")},
            "dominant_modes": sorted(dom),
            "best_subpattern": {"name": best[0], "overlap": best[2],
                                "sub_size": best[4],
                                "dom_size": best[3]},
            "series": series}


def main():
    mb = M.ModelB(N=16, L=np.pi, q02=8.0, r=M.R, dt=0.005)
    rng = np.random.default_rng(20261110)
    cases = []
    for seed in range(1, 7):
        cases.append((f"noise_seed{seed}",
                      mb.seed_noise(amp=0.05, seed=seed)))
    for nm in ["hex6", "fcc12", "sq4", "sq8"]:
        cases.append((f"partial_{nm}",
                      mb.seed_subset(M.SUBPATTERN_LABELS[nm],
                                     amp=M.A_STAR)))
    for dphi in [0.1, 0.5, 1.0]:
        cases.append((f"full_phase_dphi{dphi}",
                      mb.seed_full(phases=antisym_phases(rng, dphi))))
    # amplitude +-20%: build via seed_full then rescale mode pairs in
    # Fourier space (keeps the field real: rescale +-n pairs together)
    ph = mb.seed_full()
    fac = pairwise_amps(rng, 0.2)
    for i, n in enumerate(ROOTS):
        ph[mb.gidx(n)] *= fac[i]
    cases.append(("full_amp_pm20pct", ph))
    out = []
    for tag, ph0 in cases:
        out.append(run_case(mb, ph0, tag))
        # save incrementally: a service restart must not lose finished runs
        with open("tables/task5_basin.json", "w") as f:
            json.dump(out, f, indent=1)
    print("TASK 5 DONE", flush=True)


if __name__ == "__main__":
    main()
