# w-n7 EXP-1313 numeric cross-check: independent root enumeration + random/grid sampling of
# B(k)=sum_{alpha in D4}(1-cos(k.alpha)); prints computed objects only.
import itertools, sys, numpy as np
roots = [v for v in itertools.product((-1,0,1), repeat=4) if sum(x*x for x in v) == 2]
R = np.array(roots, dtype=float)
print("n_roots", len(roots))
def B(K):  # K: (n,4)
    return (1.0 - np.cos(K @ R.T)).sum(axis=1)
rng = np.random.default_rng(np.random.SeedSequence([1313, 7]))  # seed keyed (EXP-1313, N7)
nrand = 2_000_000
best = -1.0; bestk = None; cnt = 0
for _ in range(20):
    K = rng.uniform(-np.pi, np.pi, size=(nrand // 20, 4))
    v = B(K); cnt += len(v)
    i = int(np.argmax(v))
    if v[i] > best: best = float(v[i]); bestk = K[i].copy()
assert cnt > 0
print("random_count", cnt, "random_max", repr(best), best.hex(), "argmax", [repr(float(x)) for x in bestk])
n = 41
g = np.linspace(-np.pi, np.pi, n)
G = np.array(np.meshgrid(g, g, g, g, indexing="ij")).reshape(4, -1).T
vg = B(G); assert len(vg) > 0
j = int(np.argmax(vg)); m = float(vg[j])
print("grid_count", len(vg), "grid_max", repr(m), m.hex(), "n_grid_points_within_1e-9_of_max", int((vg > m - 1e-9).sum()))
print("B(0,0,pi,pi)", repr(float(B(np.array([[0, 0, np.pi, np.pi]]))[0])))
# local refinement from best random point (scipy)
from scipy.optimize import minimize
r = minimize(lambda x: -B(x[None, :])[0], bestk, method="Nelder-Mead", options=dict(xatol=1e-12, fatol=1e-14, maxiter=20000))
print("refined_max", repr(float(-r.fun)), "at", [repr(float(x)) for x in r.x])
# closed form check B = 24 - 4 sum_{i<j} c_i c_j at random points
K = rng.uniform(-10, 10, size=(10000, 4)); c = np.cos(K)
cf = 24 - 4 * sum(c[:, i] * c[:, j] for i in range(4) for j in range(i + 1, 4))
d = float(np.max(np.abs(cf - B(K)))); print("closed_form_count", len(K), "max_abs_diff", repr(d))
print("numpy", np.__version__, "python", sys.version.split()[0])
print("DONE n7_xcheck")
