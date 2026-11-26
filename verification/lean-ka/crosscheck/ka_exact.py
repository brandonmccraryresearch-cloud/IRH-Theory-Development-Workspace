"""EXP-1314 C-1314a (run 13, w-ka), SymPy/mpmath route.
Disordered-phase Swift-Hohenberg two-point function G(s) = 1/(r + (q0^2 - s)^2), s = |k|^2, r > 0.
(1) monotonicity: dG/ds and the values G(q0^2/2), G(q0^2);
(2) poles in k4 at fixed k_perp: k4^2 = a +- i sqrt(r), a = q0^2 - |k_perp|^2;
(3) reflected kernel Ghat(x) = int_R dk4 e^{i k4 x} G by residues (upper half plane, x > 0),
    parametrised by z = alpha + i beta (alpha, beta > 0), z^2 = a + i sqrt(r);
(4) closed form vs mpmath quadrature at sample points;
(5) exact value at x = pi/alpha;  (6) random counterexample search over (r, q0^2, |k_perp|^2).
Prints computed objects only.  key=value args: seed=<str> nsamp=<int>.
"""
import sys, hashlib, json
import sympy as sp
import mpmath as mp

A = dict(a.split("=", 1) for a in sys.argv[1:])
print("versions sympy", sp.__version__, "mpmath", mp.__version__, flush=True)

s, r, q2, x, k = sp.symbols("s r q0sq x k", real=True)
al, be = sp.symbols("alpha beta", positive=True)
G = 1 / (r + (q2 - s) ** 2)
dG = sp.factor(sp.diff(G, s))
print("dG/ds =", dG, flush=True)
print("G(q0^2/2) - G(q0^2) =", sp.simplify(G.subs(s, q2 / 2) - G.subs(s, q2)), flush=True)
print("factor:", sp.factor(sp.simplify(G.subs(s, q2 / 2) - G.subs(s, q2))), flush=True)

a = sp.symbols("a", real=True)
rp = sp.symbols("rp", positive=True)
sol = sp.solve(sp.Eq(rp + (a - k ** 2) ** 2, 0), k)
print("poles k4 (r=rp>0):", sol, flush=True)

# parametrisation: a = alpha^2 - beta^2, sqrt(r) = 2 alpha beta  <=>  z^2 = a + i sqrt r, z = alpha + i beta
z = al + sp.I * be
zb = al - sp.I * be
den = (k - z) * (k + z) * (k - zb) * (k + zb)
chk = sp.expand(den - (rp + (a - k ** 2) ** 2).subs({rp: (2 * al * be) ** 2, a: al ** 2 - be ** 2}))
print("denominator identity residual (should be 0):", sp.simplify(chk), flush=True)
f = sp.exp(sp.I * k * x) / den
res1 = sp.residue(f, k, z)
res2 = sp.residue(f, k, -zb)
Ghat = sp.simplify(sp.expand_complex(2 * sp.pi * sp.I * (res1 + res2)))
closed = sp.pi * sp.exp(-be * x) * (al * sp.cos(al * x) + be * sp.sin(al * x)) / (2 * al * be * (al ** 2 + be ** 2))
print("Ghat by residues =", Ghat, flush=True)
print("Ghat - closed form (simplify):", sp.simplify(sp.expand_complex(Ghat - closed)), flush=True)
print("UHP check: Im z =", be, " Im(-conj z) =", sp.im(-zb), flush=True)
at = sp.simplify(closed.subs(x, sp.pi / al))
print("closed form at x = pi/alpha:", at, flush=True)
print("closed form at x = 0:", sp.simplify(closed.subs(x, 0)), flush=True)
print("d/dx closed at 0:", sp.simplify(sp.diff(closed, x).subs(x, 0)), flush=True)

# alpha, beta from (r, a)
def ab(rv, av):
    m = mp.sqrt(av ** 2 + rv)
    return mp.sqrt((m + av) / 2), mp.sqrt((m - av) / 2)

mp.mp.dps = 30
def ghat_quad(rv, av, xv):
    g = lambda kk: mp.cos(kk * xv) / (rv + (av - kk ** 2) ** 2)
    Kc = mp.mpf(40) + (mp.sqrt(av) * 3 if av > 0 else 0)
    pts = [mp.mpf(0)]
    if av > 0:
        sa = mp.sqrt(av)
        w = rv / (2 * sa) if sa > 0 else 1
        pts += sorted(set([sa - 20 * w, sa - 5 * w, sa - w, sa, sa + w, sa + 5 * w, sa + 20 * w]))
        pts = [p for p in pts if p >= 0]
    # oscillation-period subdivision up to Kc
    step = mp.pi / xv
    p = pts[-1]
    while p + step < Kc:
        p += step; pts.append(p)
    pts.append(Kc)
    pts = sorted(set(pts))
    body = mp.quad(g, pts, maxdegree=8)
    tail = mp.quadosc(g, [Kc, mp.inf], omega=xv)
    return 2 * (body + tail)

def ghat_closed(rv, av, xv):
    a_, b_ = ab(rv, av)
    return mp.pi * mp.e ** (-b_ * xv) * (a_ * mp.cos(a_ * xv) + b_ * mp.sin(a_ * xv)) / (2 * a_ * b_ * (a_ ** 2 + b_ ** 2))

rows = []
for (rv, q0s, kp2) in [("0.35", "8", "0"), ("0.35", "8", "4"), ("0.35", "8", "8"), ("0.35", "8", "12"), ("2", "8", "0"), ("0.01", "1", "0")]:
    rv, q0s, kp2 = mp.mpf(rv), mp.mpf(q0s), mp.mpf(kp2)
    av = q0s - kp2
    a_, b_ = ab(rv, av)
    for xv in [mp.mpf("0.3"), mp.mpf("1.1"), mp.pi / a_, mp.mpf("2.5")]:
        if mp.pi * b_ / a_ > 30 and xv == mp.pi / a_:
            continue
        cq = ghat_quad(rv, av, xv); cc = ghat_closed(rv, av, xv)
        rows.append((float(rv), float(q0s), float(kp2), float(xv), mp.nstr(cq, 15), mp.nstr(cc, 15), mp.nstr(abs(cq - cc) / abs(cc), 3)))
for rw in rows:
    print("quad-vs-closed r=%s q0sq=%s kperp2=%s x=%s quad=%s closed=%s reldiff=%s" % rw, flush=True)

# exact value at x = pi/alpha with interval arithmetic for the record point
iv = mp.iv
iv.dps = 30
for (rv, q0s, kp2) in [("0.35", "8", "0"), ("0.35", "8", "4"), ("0.35", "8", "12")]:
    R = iv.mpf(rv); av = iv.mpf(q0s) - iv.mpf(kp2)
    m = iv.sqrt(av ** 2 + R)
    a_ = iv.sqrt((m + av) / 2); b_ = iv.sqrt((m - av) / 2)
    val = -iv.pi * iv.exp(-iv.pi * b_ / a_) / (2 * b_ * (a_ ** 2 + b_ ** 2))
    print("interval Ghat(pi/alpha) r=%s q0sq=%s kperp2=%s : [%s, %s]  alpha=[%s,%s] beta=[%s,%s]" % (
        rv, q0s, kp2, mp.nstr(val.a, 12), mp.nstr(val.b, 12), mp.nstr(a_.a, 12), mp.nstr(a_.b, 12), mp.nstr(b_.a, 12), mp.nstr(b_.b, 12)), flush=True)

# random counterexample search: quadrature value at x = pi/alpha must be < 0 (a positive value would refute)
seed = A.get("seed", "EXP-1314|C-1314a|search")
nsamp = int(A.get("nsamp", "60"))
import random
rnd = random.Random(int.from_bytes(hashlib.sha256(seed.encode()).digest()[:8], "big"))
mp.mp.dps = 20
nneg = 0; npos = 0; worst = None; cnt = 0
for i in range(nsamp):
    rv = mp.mpf(10 ** rnd.uniform(-2, 1)); q0s = mp.mpf(rnd.uniform(0.5, 12)); kp2 = mp.mpf(rnd.uniform(0, float(q0s)))
    av = q0s - kp2
    a_, b_ = ab(rv, av)
    xv = mp.pi / a_
    if mp.pi * b_ / a_ > 30:   # value ~exp(-30) or smaller: below quadrature resolution; covered by the exact formula
        continue
    cq = ghat_quad(rv, av, xv); cc = ghat_closed(rv, av, xv)
    cnt += 1
    if cq < 0: nneg += 1
    else: npos += 1
    rel = abs(cq - cc) / abs(cc)
    worst = rel if worst is None else max(worst, rel)
assert cnt > 0
print("search samples", cnt, "quad<0:", nneg, "quad>=0:", npos, "max rel diff quad vs closed", mp.nstr(worst, 3), flush=True)

# positive / negative 1D controls of the same reflected-kernel test
mp.mp.dps = 30
m1, m2 = mp.mpf(1), mp.mpf(2)
kpos = lambda xv: mp.pi * mp.e ** (-m1 * xv) / m1                     # int e^{ikx}/(k^2+m^2)
kneg = lambda xv: (mp.pi * mp.e ** (-m1 * xv) / m1 - mp.pi * mp.e ** (-m2 * xv) / m2)
ts = [mp.mpf(j) / 4 for j in range(1, 9)]
Mp = mp.matrix([[kpos(ti + tj) for tj in ts] for ti in ts]); Mn = mp.matrix([[kneg(ti + tj) for tj in ts] for ti in ts])
ep = mp.eigsy(Mp)[0]; en = mp.eigsy(Mn)[0]
print("control pos 1/(k^2+1): min eig of [K(t_i+t_j)] =", mp.nstr(min(ep), 6), flush=True)
print("control neg 1/(k^2+1)-1/(k^2+4): min eig =", mp.nstr(min(en), 6), flush=True)
print("DONE", flush=True)
