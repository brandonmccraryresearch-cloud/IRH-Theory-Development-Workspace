# v-n7 verifier-authored cross-check (EXP-1313). Not derived from the author's n7_xcheck.py.
# Roots built as pairs (i<j) x signs (s,t) -- a different construction from itertools-filter.
# (1) exact sympy identity sum_alpha cos(k.alpha) = 2[(sum c)^2 - sum c^2], c_i = cos k_i
# (2) exact max: B = 24 - 2[(sum c)^2 - sum c^2] is multilinear in c on [-1,1]^4 => extrema at the
#     16 vertices; enumerate them exactly; plus exact B at named points
# (3) numerics: scipy differential_evolution (several seeds) + uniform sampler (assert count > 0)
import sys, itertools, hashlib, platform
import sympy as sp
import numpy as np
from scipy.optimize import differential_evolution
args = dict(a.split("=", 1) for a in sys.argv[1:])
NS = int(args.get("nsample", "1000000"))
print("python", platform.python_version(), "sympy", sp.__version__, "numpy", np.__version__)
import scipy; print("scipy", scipy.__version__)
roots = []
for i in range(4):
    for j in range(i + 1, 4):
        for s in (1, -1):
            for t in (1, -1):
                v = [0, 0, 0, 0]; v[i] = s; v[j] = t; roots.append(tuple(v))
print("n_roots", len(roots), "n_distinct", len(set(roots)))
print("norms", sorted(set(sum(x * x for x in r) for r in roots)))
# completeness among all integer vectors with |entries|<=2 (norm 2 forces |entries|<=1)
allnorm2 = [v for v in itertools.product(range(-2, 3), repeat=4) if sum(x * x for x in v) == 2]
print("int_norm2_in_box2", len(allnorm2), "equal_sets", set(allnorm2) == set(roots))
k = sp.symbols("k0:4", real=True)
S = sum(sp.cos(sum(k[m] * r[m] for m in range(4))) for r in roots)
c = [sp.cos(x) for x in k]
target = 2 * ((sum(c)) ** 2 - sum(x ** 2 for x in c))
diff = sp.simplify(sp.expand(sp.expand_trig(S) - target))
print("identity_residual", diff)
Bc = lambda cc: 24 - 2 * ((sum(cc)) ** 2 - sum(x * x for x in cc))
verts = list(itertools.product((-1, 1), repeat=4))
vals = sorted(set(Bc([sp.Integer(x) for x in v]) for v in verts))
print("vertex_values", vals, "vertex_max", max(vals),
      "argmax_vertices", [v for v in verts if Bc([sp.Integer(x) for x in v]) == max(vals)])
Bk = lambda kk: sum(1 - sp.cos(sum(kk[m] * r[m] for m in range(4))) for r in roots)
for name, pt in [("0,0,pi,pi", (0, 0, sp.pi, sp.pi)), ("pi,pi,pi,pi", (sp.pi,) * 4),
                 ("0,0,0,0", (0, 0, 0, 0)), ("pi,0,0,0", (sp.pi, 0, 0, 0)),
                 ("0,0,pi/2,pi/2", (0, 0, sp.pi / 2, sp.pi / 2))]:
    print("exact_B", name, sp.nsimplify(sp.simplify(Bk(pt))))
R = np.array(roots, dtype=float)
def Bn(x):
    return float(np.sum(1.0 - np.cos(R @ np.asarray(x, dtype=float))))
best = []
for sd in (11, 22, 33):
    r = differential_evolution(lambda x: -Bn(x), [(-np.pi, np.pi)] * 4, seed=sd, tol=1e-12,
                               polish=True, maxiter=2000)
    best.append(-r.fun)
    print("DE seed", sd, "max", repr(float(-r.fun)), float(-r.fun).hex(), "x", [repr(float(t)) for t in r.x])
seed = int(hashlib.sha256(b"v-n7|uniform-sampler").hexdigest()[:8], 16)
rng = np.random.Generator(np.random.PCG64(seed))
X = rng.uniform(-np.pi, np.pi, size=(NS, 4))
V = np.sum(1.0 - np.cos(X @ R.T), axis=1)
count = int(V.size)
assert count > 0
print("sampler seed", seed, "count", count, "max", repr(float(V.max())), float(V.max()).hex(),
      "n_above_32_plus_1e-12", int(np.sum(V > 32 + 1e-12)))
print("VN7PY_DONE")
