"""Task 1 — three-dimensional projections of the D4 standing wave.

Computes, for rational and irrational viewing directions nhat:
  (a) the standing-wave slice Fourier signature: projections of the 24 shell
      vectors onto nhat^perp, grouped with multiplicities (exact);
  (b) the finite-window lattice projection: D4 points in a ball of radius 5,
      orthogonally projected, with structure factor S(q) evaluated at the
      exact predicted Bragg positions P(g*), g* in the dual lattice D4*;
  (c) the icosahedral verdict: |Aut(D4)| by exact enumeration (SymPy
      rationals); 5 does not divide it, so no projection direction yields
      exact icosahedral symmetry.
Figures + peak tables to figures/ and tables/.
"""
import sys, json, csv, math, itertools
import numpy as np
import sympy as sp

sys.path.insert(0, ".")
import d4model as M

PHI = (1 + math.sqrt(5)) / 2
DIRS = {
    "e4 (0,0,0,1) rational": np.array([0., 0, 0, 1]),
    "d110 (1,1,0,0)/sqrt2 rational": np.array([1., 1, 0, 0]) / math.sqrt(2),
    "d1111 (1,1,1,1)/2 rational": np.array([1., 1, 1, 1]) / 2,
    "d1110 (1,1,1,0)/sqrt3 rational": np.array([1., 1, 1, 0]) / math.sqrt(3),
    "phi1 (1,phi,0,0) irrational": np.array([1., PHI, 0, 0]) / math.sqrt(1 + PHI ** 2),
    "phi4 (1,phi,phi^2,phi^3) irrational":
        np.array([1., PHI, PHI ** 2, PHI ** 3]) / math.sqrt(1 + PHI ** 2 + PHI ** 4 + PHI ** 6),
    "sqrt (1,sqrt2,sqrt3,sqrt5) irrational":
        np.array([1., math.sqrt(2), math.sqrt(3), math.sqrt(5)]) / math.sqrt(11),
}

# --- (c) Aut(D4) order, exact enumeration (integer arithmetic) ---
# An automorphism of the D4 root system is determined by the images of a
# basis of simple roots, and must preserve their Gram matrix. Enumerate all
# quadruples of roots with the simple-root Gram matrix: the count is
# |Aut(D4)|. (A generator-based attempt with a single Hadamard triality map
# gave only 384 = 192 x 2: that map is an order-2 diagram automorphism, not
# the full S3 triality. The enumeration below does not depend on generators.)
simple = [(1, -1, 0, 0), (0, 1, -1, 0), (0, 0, 1, -1), (0, 0, 1, 1)]
def dot(a, b):
    return sum(x * y for x, y in zip(a, b))
GRAM = [[dot(simple[i], simple[j]) for j in range(4)] for i in range(4)]
roots_list = M.ROOTS
# candidates for each image, pruned by the Gram conditions incrementally
count_aut = 0
for r1 in roots_list:
    if dot(r1, r1) != GRAM[0][0]:
        continue
    for r2 in roots_list:
        if dot(r2, r2) != GRAM[1][1] or dot(r1, r2) != GRAM[0][1]:
            continue
        for r3 in roots_list:
            if (dot(r3, r3) != GRAM[2][2] or dot(r1, r3) != GRAM[0][2]
                    or dot(r2, r3) != GRAM[1][2]):
                continue
            for r4 in roots_list:
                if (dot(r4, r4) != GRAM[3][3] or dot(r1, r4) != GRAM[0][3]
                        or dot(r2, r4) != GRAM[1][3]
                        or dot(r3, r4) != GRAM[2][3]):
                    continue
                count_aut += 1
print(f"|Aut(D4)| = {count_aut} (expect 1152 = |W(F4)| = 192 x 6)")
assert count_aut == 1152
assert 1152 % 5 != 0
# the Hadamard map preserves the root set (it is one diagram automorphism)
T = sp.Matrix([[1, 1, 1, 1], [1, 1, -1, -1],
               [1, -1, 1, -1], [1, -1, -1, 1]]) / 2
roots_sp = [sp.Matrix(a) for a in M.ROOTS]
root_set = set(tuple(map(int, a)) for a in M.ROOTS)
assert all(tuple(map(int, T * r)) in root_set for r in roots_sp)
OUT = {"Aut_D4_order": count_aut, "five_divides_order": False}

# --- dual lattice D4* (for Bragg positions) ---
# D4* = {y : y.x in Z for all x in D4} = Z^4 union (Z^4 + (1/2,1/2,1/2,1/2)).
def dual_points(Rmax):
    m = int(math.ceil(Rmax)) + 1
    pts = []
    for x in itertools.product(range(-m, m + 1), repeat=4):
        v = np.array(x, dtype=float)
        if np.linalg.norm(v) <= Rmax + 1e-9:
            pts.append(v)
        v2 = v + 0.5
        if np.linalg.norm(v2) <= Rmax + 1e-9:
            pts.append(v2)
    # dedupe
    uniq = []
    seen2 = set()
    for p in pts:
        key = tuple(np.round(p, 9))
        if key not in seen2:
            seen2.add(key)
            uniq.append(p)
    return np.array(uniq)

DUAL = dual_points(3.5)
print(f"dual-lattice vectors with |g*| <= 3.5: {len(DUAL)}")

# --- finite-window lattice points ---
PTS = M.d4_lattice_points(5.0)
print(f"D4 points in ball R=5: {len(PTS)}")

results = {}
for name, nhat in DIRS.items():
    proj, basis = M.project_points(PTS, nhat)
    # (a) standing-wave slice: project the 24 shell vectors
    shell = np.array(M.SHELL, dtype=float)
    n = np.asarray(nhat, dtype=float); n = n / np.linalg.norm(n)
    pshell = shell - np.outer(shell @ n, n)
    # group identical projections (tolerance 1e-9), in the hyperplane basis
    coords = pshell @ basis
    groups = {}
    for c in coords:
        key = tuple(np.round(c, 9))
        groups[key] = groups.get(key, 0) + 1
    sig = sorted(groups.items(), key=lambda kv: -kv[1])
    # (b) structure factor at predicted Bragg positions q = 2*pi*P(g*)
    pdual = DUAL - np.outer(DUAL @ n, n)
    qcoords = 2 * np.pi * (pdual @ basis)
    # evaluate S(q) directly at every candidate, then cluster: the
    # finite window (ball R=5) broadens each peak to width ~2*pi/10, so
    # candidates within 0.6 of a stronger peak are the same peak.
    cand = []
    for q in qcoords:
        if np.linalg.norm(q) > 2 * np.pi * 3.5 + 1e-9:
            continue
        ph = np.exp(1j * (proj @ q))
        cand.append((q, float(abs(ph.sum()) ** 2 / len(proj))))
    cand.sort(key=lambda t: -t[1])
    peaks = []  # (q, S) cluster centres, strongest first
    for q, s in cand:
        if all(np.linalg.norm(q - p[0]) > 0.6 for p in peaks):
            peaks.append((q, s))
    Smax = peaks[0][1] if peaks else 0.0
    # projected-lattice test: greedily take the shortest projected vectors
    # that increase the rank; what fraction of projected points lie on the
    # lattice they generate? (1.0 => periodic lattice; < 1 => aperiodic.)
    lat_frac = None
    norms = np.linalg.norm(proj, axis=1)
    order = np.argsort(norms)
    basis3 = []
    for idx in order:
        v = proj[idx]
        if np.linalg.norm(v) < 1e-9:
            continue
        if len(basis3) == 0:
            basis3.append(v)
        elif np.linalg.matrix_rank(np.array(basis3 + [v])) > len(basis3):
            basis3.append(v)
        if len(basis3) == 3:
            break
    if len(basis3) == 3:
        B = np.array(basis3)
        try:
            coef = np.linalg.solve(B.T, proj.T).T
            lat_frac = float((np.abs(coef - np.round(coef)).max(axis=1)
                              < 1e-6).mean())
        except np.linalg.LinAlgError:
            lat_frac = None
    # projected-lattice shortest vectors (from projected D4 points near origin)
    norms = np.linalg.norm(proj, axis=1)
    nz = norms[(norms > 1e-9)]
    results[name] = {
        "n_points": len(proj),
        "slice_distinct_peaks": len(groups),
        "slice_groups": [(list(map(lambda x: round(float(x), 4), k)), v)
                         for k, v in sig],
        "slice_max_mult": max(v for _, v in sig),
        "shortest_projected_norm": float(nz.min()) if len(nz) else None,
        "lattice_fraction": lat_frac,
        "lattice_basis": [[round(float(x), 4) for x in v] for v in basis3],
        "n_peaks_S_gt_half_max": sum(1 for _, s in peaks if s > 0.5 * Smax),
        "n_peaks_S_gt_tenth_max": sum(1 for _, s in peaks if s > 0.1 * Smax),
        "top_bragg": [(round(float(np.linalg.norm(q)), 3), round(s, 3))
                      for q, s in peaks[:12]],
        "S_max": Smax,
    }
    print(f"\n{name}: {len(proj)} pts, slice peaks {len(groups)} distinct, "
          f"max mult {results[name]['slice_max_mult']}, "
          f"shortest |P(x)| = {results[name]['shortest_projected_norm']:.4f}, "
          f"lattice frac = {results[name]['lattice_fraction']}, "
          f"S_max = {results[name]['S_max']:.1f}, "
          f"#peaks >0.5max = {results[name]['n_peaks_S_gt_half_max']}, "
          f"#peaks >0.1max = {results[name]['n_peaks_S_gt_tenth_max']}")

with open("tables/task1_projections.json", "w") as f:
    json.dump(results, f, indent=1, default=str)

# peak table CSV (standing-wave slice signatures)
with open("tables/task1_slice_peaks.csv", "w", newline="") as f:
    w = csv.writer(f)
    w.writerow(["direction", "peak_index", "q1", "q2", "q3", "multiplicity",
                "|P(g)|^2"])
    for name, r in results.items():
        for i, (k, v) in enumerate(r["slice_groups"]):
            w.writerow([name, i] + [f"{x:.4f}" for x in k] + [v,
                        f"{sum(x * x for x in k):.4f}"])
with open("tables/task1_bragg.csv", "w", newline="") as f:
    w = csv.writer(f)
    w.writerow(["direction", "|q|", "S(q)"])
    for name, r in results.items():
        for q, s in r["top_bragg"]:
            w.writerow([name, q, s])

# --- figures ---
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

def scatter_proj(ax, proj, title, s=1.5):
    ax.scatter(proj[:, 0], proj[:, 1], s=s, c="k", alpha=0.7)
    ax.set_aspect("equal")
    ax.set_title(title)
    ax.set_xlabel("e1"); ax.set_ylabel("e2")

fig, axes = plt.subplots(1, 2, figsize=(11, 5))
for ax, key in zip(axes, ["e4 (0,0,0,1) rational",
                          "phi1 (1,phi,0,0) irrational"]):
    proj, _ = M.project_points(PTS, DIRS[key])
    scatter_proj(ax, proj, f"projected D4 points, R=5\n{key}")
fig.tight_layout()
fig.savefig("figures/task1_projection_scatter.png", dpi=150)

# structure-factor heatmaps via binned FFT: 3D histogram -> FFT -> |.|^2,
# slice through q3 = 0.
def sq_slice(proj, box=12.0, nb=96):
    H, edges = np.histogramdd(proj, bins=nb,
                              range=[(-box / 2, box / 2)] * 3)
    F = np.fft.fftshift(np.fft.fftn(np.fft.ifftshift(H)))
    S = np.abs(F) ** 2
    q = np.fft.fftshift(np.fft.fftfreq(nb, d=box / nb)) * 2 * np.pi
    return S[:, :, nb // 2], q

fig, axes = plt.subplots(1, 2, figsize=(11, 5))
for ax, key in zip(axes, ["e4 (0,0,0,1) rational",
                          "phi1 (1,phi,0,0) irrational"]):
    proj, _ = M.project_points(PTS, DIRS[key])
    S2, q = sq_slice(proj)
    vmax = np.percentile(S2, 99.9)
    ax.imshow(np.log10(S2 + 1), extent=[q[0], q[-1], q[0], q[-1]],
              origin="lower", cmap="viridis", vmin=0, vmax=np.log10(vmax + 1))
    ax.set_title(f"log10 S(q), q3=0 slice\n{key}")
    ax.set_xlabel("q1"); ax.set_ylabel("q2")
fig.tight_layout()
fig.savefig("figures/task1_structure_factor.png", dpi=150)

# standing-wave slice real-space patterns on a 2D section of the hyperplane
def wave_slice(nhat, L=6.0, ngrid=200):
    n = np.asarray(nhat, dtype=float); n = n / np.linalg.norm(n)
    A = np.eye(4); A[:, 0] = n
    Q, _ = np.linalg.qr(A)
    basis = Q[:, 1:]  # 4x3
    # 2D section spanned by basis[:,0], basis[:,1]
    u = np.linspace(-L / 2, L / 2, ngrid)
    U, V = np.meshgrid(u, u)
    X = (U[..., None] * basis[:, 0] + V[..., None] * basis[:, 1])
    psi = np.zeros_like(U)
    for g in M.SHELL:
        psi += np.cos(X @ np.array(g, dtype=float))
    return U, V, psi

fig, axes = plt.subplots(1, 2, figsize=(11, 5))
for ax, key in zip(axes, ["e4 (0,0,0,1) rational",
                          "phi1 (1,phi,0,0) irrational"]):
    U, V, psi = wave_slice(DIRS[key])
    ax.imshow(psi, extent=[-3, 3, -3, 3], origin="lower", cmap="RdBu_r",
              vmin=-24, vmax=24)
    ax.set_title(f"standing-wave slice Psi, 2D section\n{key}")
    ax.set_xlabel("u"); ax.set_ylabel("v")
fig.tight_layout()
fig.savefig("figures/task1_wave_slice.png", dpi=150)

print("TASK 1 DONE")
