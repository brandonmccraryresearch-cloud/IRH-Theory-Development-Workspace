#!/usr/bin/env python
"""Task 7 (local-independent): discriminating 3D D4 peak ratios.

Recomputation ONLY from the prior-programme sources listed in REPORT.md:
  * 3d-projections/*.csv + geometry_parameters_and_checks.json
  * ws-a-core-computations task1_report.md / tables (slice multiplicities,
    recomputed here from d4model ROOTS for the e4/d1111 directions only)
No Co-scientist output, no browser, no network, no RNG (seed pinned: none used).
Run: ~/miniconda3/envs/jacobian-conjecture-2d/bin/python task7_compute.py
"""
import csv, json, math, os
import numpy as np
import pandas as pd
from scipy.spatial import cKDTree
from scipy.optimize import brentq

PY = "3.11.16"
HERE = os.path.dirname(os.path.abspath(__file__))
PROG = "/home/hatch/workspace/research/irh/co-scientist-tasks-2026-11-10"
SRC3 = os.path.join(PROG, "3d-projections")
WSA = os.path.join(PROG, "ws-a-core-computations")
OUT = HERE
SEED = 20261114  # pinned; no RNG is used in this script (recorded for provenance)

def sinc(z):
    # sinc(z)=sin(pi z)/(pi z), sinc(0)=1; numpy route
    return np.sinc(z)

def sinc_math(z):
    # independent pure-math route
    if z == 0.0:
        return 1.0
    return math.sin(math.pi * z) / (math.pi * z)

def main():
    lat = pd.read_csv(os.path.join(SRC3, "lattice_peak_intensities.csv"))
    fld = pd.read_csv(os.path.join(SRC3, "field_mode_intensities.csv"))
    fft = pd.read_csv(os.path.join(SRC3, "fft_detected_peaks.csv"))
    win = pd.read_csv(os.path.join(SRC3, "window_sensitivity.csv"))
    with open(os.path.join(SRC3, "geometry_parameters_and_checks.json")) as f:
        geom = json.load(f)

    checks = []

    # ---- Route 2 check: sinc^2 ideal for irrational CPS, math vs numpy ----
    cps = lat[lat.operation == "irrational_cut_and_project"].copy()
    # t_star and h give ideal = sinc^2(2 h t*); DC rows have t*=0 -> 1
    ideal_np = sinc(2 * cps["h"].values * cps["t_star"].fillna(0).values) ** 2
    ideal_m = np.array([sinc_math(2 * float(h) * float(t)) ** 2
                        for h, t in zip(cps["h"], cps["t_star"].fillna(0))])
    d = np.max(np.abs(ideal_np - ideal_m))
    stored = cps["I_infinite_DC_normalized"].values
    d2 = np.max(np.abs(ideal_np - stored))
    checks.append(("sinc2 math-vs-numpy maxdiff", float(d)))
    checks.append(("sinc2 recomputed-vs-stored maxdiff", float(d2)))
    assert d < 1e-12 and d2 < 1e-9, (d, d2)

    # ---- Route 2 check: ratios recomputed with pure csv module ----
    rows_csv = {}
    with open(os.path.join(SRC3, "lattice_peak_intensities.csv")) as f:
        for r in csv.DictReader(f):
            if r["operation"] in ("rational_exact_lattice_section",
                                  "rational_finite_source_projection"):
                rows_csv[(r["operation"], int(r["L"]), float(r["h"]), r["label"])] = \
                    float(r["I_finite_DC_normalized"])
    # pandas route for the same cells
    def probe(op, L, h, label):
        s = lat[(lat.operation == op) & (lat.L == L) & (lat.h == h) &
                (lat.label.str.startswith(label))]
        assert len(s) == 1, (op, L, h, label, len(s))
        return float(s["I_finite_DC_normalized"].iloc[0])
    for key, v in rows_csv.items():
        op, L, h, label = key
        pv = probe(op, L, h, label.split("_")[0] + "_" + label.split("_")[1]) \
            if False else None
    # direct comparison on the named probes below (pandas vs csv dict)
    probes = [("rational_exact_lattice_section", 7, 0.0, "FCC_111_allowed"),
              ("rational_exact_lattice_section", 7, 0.0, "FCC_100_forbidden"),
              ("rational_finite_source_projection", 3, 6.0,
               "FCC_111_allowed_simple_cubic_joint_infinite_limit")]
    for op, L, h, lab in probes:
        pv = float(lat[(lat.operation == op) & (lat.L == L) & (lat.h == h) &
                       (lat.label == lab)]["I_finite_DC_normalized"].iloc[0])
        assert abs(pv - rows_csv[(op, L, h, lab)]) == 0.0
    checks.append(("pandas-vs-csv probe values identical", 0.0))

    # ---- Atomic probe ratios (FCC section vs Z3 projection) ----
    def sec(L, label):
        return probe("rational_exact_lattice_section", L, 0.0, label)
    def proj(H, label):
        s = lat[(lat.operation == "rational_finite_source_projection") &
                (lat.L == 3) & (lat.h == float(H))]
        s = s[s.label.str.startswith(label)]
        assert len(s) == 1
        return float(s["I_finite_DC_normalized"].iloc[0])
    atomic = []
    for L in (3, 5, 7):
        i111, i200, i220, i311 = sec(L, "FCC_111_allowed"), sec(L, "FCC_200_allowed"), \
            sec(L, "FCC_220_allowed"), sec(L, "FCC_311_allowed")
        i100, i110 = sec(L, "FCC_100_forbidden"), sec(L, "FCC_110_forbidden")
        atomic.append(dict(obj="FCC_section", L=L, H=None, I111=i111, I200=i200,
                           I100=i100, I110=i110, I311=i311,
                           A1=i111 / i200, A2=i311 / i111, A3=i100 / i111, A4=i110 / i111))
    for H in (2, 4, 6):
        i111, i200 = proj(H, "FCC_111_allowed"), proj(H, "FCC_200_allowed")
        i311 = proj(H, "FCC_311_allowed")
        i100, i110 = proj(H, "FCC_100_forbidden"), proj(H, "FCC_110_forbidden")
        atomic.append(dict(obj="Z3_projection", L=3, H=H, I111=i111, I200=i200,
                           I100=i100, I110=i110, I311=i311,
                           A1=i111 / i200, A2=i311 / i111, A3=i100 / i111, A4=i110 / i111))
    atomic_df = pd.DataFrame(atomic)

    # ---- Irrational CPS ratios (per h, L=7 finite + ideal) ----
    cps_rows = []
    for h in (0.35, 0.7, 1.4):
        for L in (3, 5, 7):
            cc = lat[(lat.operation == "irrational_cut_and_project") &
                     (lat.L == L) & (lat.h == h)].copy()
            nd = cc[cc.q_norm > 1e-9].copy()
            # distinct Friedel pairs: keep one of each +-q pair (q1>0, or tie-break)
            nd["key"] = [tuple(np.round(np.abs(v), 9)) for v in
                         nd[["q1", "q2", "q3"]].values]
            nd = nd.sort_values("I_infinite_DC_normalized", ascending=False)
            nd = nd.drop_duplicates("key")
            top = nd["I_infinite_DC_normalized"].values
            topf = nd["I_finite_DC_normalized"].values
            rep = cc[(cc.g1 == 0) & (cc.g2 == 1) & (cc.g3 == -1) & (cc.g4 == 0)]
            assert len(rep) == 1
            rep_ideal = float(rep["I_infinite_DC_normalized"].iloc[0])
            rep_finite = float(rep["I_finite_DC_normalized"].iloc[0])
            cps_rows.append(dict(
                h=h, L=L, N=int(cc["N"].iloc[0]),
                C1_ideal=float(top[0] / top[1]),
                C1_finite=float(topf[0] / topf[1]),
                C2_ideal=float(top[0] / rep_ideal),
                C2_finite=float(topf[0] / rep_finite),
                C3_top_over_median10_ideal=float(top[0] / np.median(top[:10])),
                C3_top_over_median10_finite=float(topf[0] / np.median(topf[:10])),
                frac_ge05=float((nd["I_infinite_DC_normalized"] >= 0.5).mean()),
                frac_ge01=float((nd["I_infinite_DC_normalized"] >= 0.1).mean()),
                n_ge05=int((nd["I_infinite_DC_normalized"] >= 0.5).sum()),
                n_ge01=int((nd["I_infinite_DC_normalized"] >= 0.1).sum()),
                n_pairs=len(nd),
                top_ideal=float(top[0]), second_ideal=float(top[1]),
                top_finite=float(topf[0]),
                mean_abs_finite_minus_ideal=float(
                    np.mean(np.abs(cc["I_finite_DC_normalized"] -
                                   cc["I_infinite_DC_normalized"])))))
    cps_df = pd.DataFrame(cps_rows)

    # ---- CPS strong-peak separations ----
    sep_rows = []
    for h in (0.35, 0.7, 1.4):
        cc = lat[(lat.operation == "irrational_cut_and_project") &
                 (lat.L == 7) & (lat.h == h)]
        for thr in (0.5, 0.1):
            pts = cc[cc.I_infinite_DC_normalized >= thr][["q1", "q2", "q3"]].values
            dnn = cKDTree(pts).query(pts, k=2)[0][:, 1]
            sep_rows.append(dict(h=h, thr=thr, n=len(pts),
                                 nn_min=float(dnn.min()),
                                 nn_median=float(np.median(dnn))))
    sep_df = pd.DataFrame(sep_rows)

    # ---- Field-mode ratios ----
    field_rows = []
    for op in ("rational_field_section", "irrational_field_section",
               "irrational_field_slab_average"):
        for L in (4, 8):
            for w in ("rectangular", "hann"):
                f = fld[(fld.operation == op) & (fld.L == L) & (fld.window == w)]
                ex = f["I_exact_coefficient_squared"].values
                fw = f["I_finite_window_at_exact_q"].values
                ratio = fw / ex
                # analytic modes with exact power 0 do not occur; guard anyway
                field_rows.append(dict(
                    operation=op, L=L, window=w, n_modes=len(f),
                    exact_max=float(ex.max()), exact_min=float(ex.min()),
                    exact_max_over_min=float(ex.max() / ex.min()) if ex.min() > 0 else np.nan,
                    finite_over_exact_min=float(ratio.min()),
                    finite_over_exact_median=float(np.median(ratio)),
                    finite_over_exact_max=float(ratio.max()),
                    n_finite_over_exact_outside_10pct=int(((ratio < 0.9) | (ratio > 1.1)).sum())))
    field_df = pd.DataFrame(field_rows)

    # rational field named ratios (exact, window-independent)
    rf = fld[(fld.operation == "rational_field_section") & (fld.L == 4) &
             (fld.window == "rectangular")]
    dc = float(rf[rf.q_norm == 0]["I_exact_coefficient_squared"].iloc[0])
    axis = float(rf[(rf.q_norm == 1.0)]["I_exact_coefficient_squared"].iloc[0])
    half = float(rf[(rf.q_norm > 0.86) & (rf.q_norm < 0.87)]
                 ["I_exact_coefficient_squared"].iloc[0])
    checks.append(("rational field F1 halfdiag/axis", half / axis))
    checks.append(("rational field DC/axis", dc / axis))
    assert half / axis == 4.0 and dc / axis == 4.0

    # ---- FFT-detected ratio spread ----
    fft_rows = []
    for (op, L, w), g in fft.groupby(["operation", "L", "window"]):
        fft_rows.append(dict(operation=op, L=L, window=w, n_detected=len(g),
                             I_max=float(g["I_fft"].max()),
                             I_min=float(g["I_fft"].min()),
                             detected_max_over_min=float(g["I_fft"].max() / g["I_fft"].min()),
                             median_offset=float(g["distance_to_nearest_exact_mode"].median()),
                             max_offset=float(g["distance_to_nearest_exact_mode"].max())))
    fft_df = pd.DataFrame(fft_rows)

    # ---- Task 1 slice recomputation (e4, d1111): projected-root multiplicities ----
    sys_path = os.path.join(WSA)
    import sys
    sys.path.insert(0, sys_path)
    import d4model as M
    roots = np.array(M.SHELL, dtype=float)  # scaled roots, |g|^2 = 8
    assert len(roots) == 24
    slice_rows = []
    for name, n in [("e4", np.array([0., 0, 0, 1])),
                    ("d1111", np.array([1., 1, 1, 1]) / 2)]:
        P = roots - np.outer(roots @ n, n)
        # group by rounded position
        keys = [tuple(np.round(v, 9)) for v in P]
        from collections import Counter
        cnt = Counter(keys)
        mults = sorted(cnt.values())
        slice_rows.append(dict(direction=name, distinct=len(cnt),
                              max_mult=max(mults), min_mult=min(mults),
                              n_mult2=sum(1 for m in mults if m == 2),
                              n_mult1=sum(1 for m in mults if m == 1),
                              mult_ratio_max_over_min=float(max(mults) / min(mults))))
    slice_df = pd.DataFrame(slice_rows)
    assert slice_df[slice_df.direction == "e4"]["distinct"].iloc[0] == 18
    assert slice_df[slice_df.direction == "d1111"]["distinct"].iloc[0] == 18

    # ---- Atom regeneration: irrational CPS at FCC probe q's (independent route) ----
    B = np.array(geom["irrational_basis_B"], dtype=float)  # 4x3, columns are basis vecs? stored rows x 4, cols 3
    # geometry JSON stores B as list of 4 rows x 3 cols: B[i,j]; y = B^T x
    nvec = np.array(geom["irrational_normal"], dtype=float)
    probes_q = {"DC": (0., 0., 0.), "111": (0.5, 0.5, 0.5), "200": (1., 0., 0.),
                "220": (1., 1., 0.), "311": (1.5, 0.5, 0.5),
                "100": (0.5, 0., 0.), "110": (0.5, 0.5, 0.)}
    regen_rows = []
    for (L, h) in [(3, 0.7), (5, 0.7), (7, 0.35), (7, 0.7), (7, 1.4)]:
        Mbound = int(math.ceil(math.sqrt(3 * L * L + h * h))) + 1
        pts = []
        rng = range(-Mbound, Mbound + 1)
        for x1 in rng:
            for x2 in rng:
                for x3 in rng:
                    for x4 in rng:
                        if (x1 + x2 + x3 + x4) % 2 != 0:
                            continue
                        x = np.array([x1, x2, x3, x4], dtype=float)
                        t = float(nvec @ x)
                        if abs(t) > h + 1e-9:
                            continue
                        y = B.T @ x
                        if np.max(np.abs(y)) > L + 1e-9:
                            continue
                        pts.append(y)
        Y = np.array(pts)
        N = len(Y)
        # verify N against window_sensitivity.csv
        wrow = win[(win.operation == "irrational_cut_and_project") &
                   (win.L == L) & (win.h == h)]
        assert len(wrow) == 1
        N_src = int(wrow["N"].iloc[0])
        checks.append((f"CPS regen N L={L} h={h} (regen {N} vs source {N_src})",
                       float(N - N_src)))
        assert N == N_src, (L, h, N, N_src)
        vals = {}
        for name, q in probes_q.items():
            qv = np.array(q)
            ph = np.exp(-2j * math.pi * (Y @ qv))
            vals[name] = float(abs(ph.mean()) ** 2)
        regen_rows.append(dict(L=L, h=h, N=N,
                               I111=vals["111"], I200=vals["200"], I100=vals["100"],
                               I110=vals["110"], I220=vals["220"], I311=vals["311"],
                               suppress_111=1.0 / vals["111"] if vals["111"] > 0 else np.nan,
                               suppress_200=1.0 / vals["200"] if vals["200"] > 0 else np.nan,
                               suppress_100=1.0 / vals["100"] if vals["100"] > 0 else np.nan,
                               R111_over_200=vals["111"] / vals["200"],
                               R100_over_111=vals["100"] / vals["111"],
                               R110_over_111=vals["110"] / vals["111"],
                               R311_over_111=vals["311"] / vals["111"]))
    regen_df = pd.DataFrame(regen_rows)

    # ---- Resolution kernel widths (numeric, 1D) ----
    # rect: |sinc(2 L d)|^2 ; hann: |sinc(z)+0.5(sinc(z-1)+sinc(z+1))|^2, z=2Ld
    def rect_pow(d, L):
        return float(np.sinc(2 * L * d) ** 2)
    def hann_pow(d, L):
        z = 2 * L * d
        k = np.sinc(z) + 0.5 * (np.sinc(z - 1) + np.sinc(z + 1))
        return float(k ** 2)
    def hann_k(d, L):
        z = 2 * L * d
        return float(np.sinc(z) + 0.5 * (np.sinc(z - 1) + np.sinc(z + 1)))
    kern_rows = []
    for L in (4, 8):
        # first zero: rect at d=1/(2L) (analytic, sinc zero); hann: first zero
        # of the SIGNED kernel K (K^2 cannot change sign, so brentq on K^2 is
        # invalid there). K_hann(z)=0 at z=2 by sinc(2)=sinc(1)=sinc(3)=0.
        fwhm_r = 2 * brentq(lambda d: rect_pow(d, L) - 0.5, 1e-6, 1 / (2 * L) - 1e-9)
        fwhm_h = 2 * brentq(lambda d: hann_pow(d, L) - 0.5, 1e-6, 0.99 / L)
        hz = brentq(lambda d: hann_k(d, L), 0.6 / L, 1.4 / L)
        checks.append((f"hann first zero L={L} (expect 1/L={1 / L})", float(hz)))
        assert abs(hz - 1 / L) < 1e-9
        kern_rows.append(dict(L=L, rect_first_zero=1 / (2 * L), rect_fwhm=float(fwhm_r),
                              hann_first_zero=float(hz), hann_fwhm=float(fwhm_h),
                              rect_bin_spacing=1 / (2 * L)))
    kern_df = pd.DataFrame(kern_rows)

    # ---- Line profile through closest irrational field-mode pair ----
    # pair: q_a=(0.072283,-0.104884,-0.240828) and its Friedel partner is far;
    # closest pair in the 24-mode set: modes at +- (0.5,0.5,0.5)-type? Use the
    # two modes separated by 0.27244: g=(0.5,0.5,0.5,0.5) q=(0.072283,-0.104884,-0.240828)
    # and g=(0.5,0.5,0.5,-0.5) q=(-0.229229,-0.531285,-0.763061) is not it.
    # Find the actual closest pair from the field table instead.
    ir = fld[(fld.operation == "irrational_field_section") & (fld.L == 8) &
             (fld.window == "rectangular")][["q1", "q2", "q3"]].values
    dm = cKDTree(ir).query(ir, k=2)
    i0 = int(np.argmin(dm[0][:, 1])); j0 = int(dm[1][i0, 1])
    qa, qb = ir[i0], ir[j0]
    sep_pair = float(np.linalg.norm(qa - qb))
    checks.append(("closest irrational field-mode pair separation", sep_pair))
    sgrid = np.linspace(-0.6, 0.6, 481)
    mid = (qa + qb) / 2
    direc = (qb - qa) / sep_pair
    prof = {}
    for L in (4, 8):
        for wname, kfun in (("rectangular", rect_pow), ("hann", hann_pow)):
            amp = np.zeros_like(sgrid)
            for qm in (qa, qb):
                # distance along the line from each mode centre
                dline = np.abs(sgrid - np.array([np.dot(qm - mid, direc)] * len(sgrid)))
                # amplitude kernel is 1D along the profile direction only as an
                # approximation: use the separable kernel evaluated at the
                # 3D offset projected on the line (upper bound on leakage)
                # exact separable evaluation below in the figure script via K3
                amp += np.array([math.sqrt(max(kfun(abs(s - np.dot(qm - mid, direc)), L), 0.0))
                                 for s in sgrid])
            prof[(L, wname)] = (sgrid, np.array(amp) ** 2,
                                float(np.dot(qa - mid, direc)),
                                float(np.dot(qb - mid, direc)))
    np.savez(os.path.join(OUT, "line_profile_data.npz"),
             qa=qa, qb=qb, sep_pair=sep_pair,
             **{f"s_{L}_{w}": v[0] for (L, w), v in prof.items()},
             **{f"I_{L}_{w}": v[1] for (L, w), v in prof.items()})

    # ---- Save tables ----
    atomic_df.to_csv(os.path.join(OUT, "discriminant_table_atomic.csv"), index=False)
    cps_df.to_csv(os.path.join(OUT, "discriminant_table_cps.csv"), index=False)
    field_df.to_csv(os.path.join(OUT, "discriminant_table_field.csv"), index=False)
    fft_df.to_csv(os.path.join(OUT, "discriminant_table_fft.csv"), index=False)
    sep_df.to_csv(os.path.join(OUT, "peak_separations.csv"), index=False)
    regen_df.to_csv(os.path.join(OUT, "cps_fcc_probe_intensities.csv"), index=False)
    kern_df.to_csv(os.path.join(OUT, "resolution_kernel_widths.csv"), index=False)
    slice_df.to_csv(os.path.join(OUT, "task1_slice_ratios.csv"), index=False)
    # combined discriminant table (the deliverable table)
    comb = []
    for _, r in atomic_df.iterrows():
        tag = f"{r['obj']} L={int(r['L'])}" + (f" H={int(r['H'])}" if pd.notna(r['H']) else "")
        comb.append(dict(discriminant="A1 I(111)/I(200)", definition="atomic probe intensities, DC-normalised", case=tag, value=float(r["A1"])))
        comb.append(dict(discriminant="A2 I(311)/I(111)", definition="atomic probe intensities, DC-normalised (negative control)", case=tag, value=float(r["A2"])))
        comb.append(dict(discriminant="A3 I(100)/I(111)", definition="forbidden/allowed atomic probe ratio", case=tag, value=float(r["A3"])))
        comb.append(dict(discriminant="A4 I(110)/I(111)", definition="forbidden/allowed atomic probe ratio", case=tag, value=float(r["A4"])))
    for _, r in cps_df.iterrows():
        tag = f"CPS h={r['h']} L={int(r['L'])}"
        comb.append(dict(discriminant="C1 I_top/I_2nd (ideal)", definition="strongest / second distinct Friedel pair, sinc^2 ideal", case=tag, value=float(r["C1_ideal"])))
        comb.append(dict(discriminant="C1 I_top/I_2nd (finite)", definition="strongest / second distinct Friedel pair, finite atoms", case=tag, value=float(r["C1_finite"])))
        comb.append(dict(discriminant="C2 I_top/I_rep (ideal)", definition="strongest / representative g=(0,1,-1,0) candidate, |q|=1.411", case=tag, value=float(r["C2_ideal"])))
        comb.append(dict(discriminant="C2 I_top/I_rep (finite)", definition="strongest / representative g=(0,1,-1,0) candidate, finite atoms", case=tag, value=float(r["C2_finite"])))
        comb.append(dict(discriminant="C3 I_top/median(top 10) (ideal)", definition="strongest / median of 10 strongest distinct pairs", case=tag, value=float(r["C3_top_over_median10_ideal"])))
        comb.append(dict(discriminant="C4 frac I>=0.5", definition="fraction of 288 non-DC candidates with ideal I>=0.5", case=tag, value=float(r["frac_ge05"])))
        comb.append(dict(discriminant="C4 frac I>=0.1", definition="fraction of 288 non-DC candidates with ideal I>=0.1", case=tag, value=float(r["frac_ge01"])))
    for _, r in regen_df.iterrows():
        tag = f"CPS-regen h={r['h']} L={int(r['L'])}"
        comb.append(dict(discriminant="C5 I(111)/I(200) at FCC probes", definition="CPS atoms evaluated at FCC probe q, DC-normalised", case=tag, value=float(r["R111_over_200"])))
        comb.append(dict(discriminant="C5 I(100)/I(111) at FCC probes", definition="CPS atoms evaluated at FCC probe q, DC-normalised", case=tag, value=float(r["R100_over_111"])))
    for _, r in field_df.iterrows():
        if r["operation"] == "rational_field_section":
            comb.append(dict(discriminant="F1 max/min field-mode power", definition="rational field: half-diagonal (4) / axis (1) mode powers", case=f"rational field L={int(r['L'])} {r['window']}", value=4.0))
        elif r["operation"] == "irrational_field_section":
            comb.append(dict(discriminant="F1 max/min field-mode power", definition="irrational field section: all 24 modes coefficient 1, power 1", case=f"irrational field L={int(r['L'])} {r['window']}", value=float(r["exact_max_over_min"])))
        else:
            comb.append(dict(discriminant="F2 slab max/min mode power", definition="irrational slab-averaged field (h=0.7): max/min exact mode power", case=f"slab field L={int(r['L'])} {r['window']}", value=float(r["exact_max_over_min"])))
    for _, r in fft_df.iterrows():
        comb.append(dict(discriminant="D1 FFT detected max/min power", definition="grid-detected FFT peak powers, same case", case=f"{r['operation']} L={int(r['L'])} {r['window']}", value=float(r["detected_max_over_min"])))
    pd.DataFrame(comb).to_csv(os.path.join(OUT, "discriminant_table.csv"), index=False)

    with open(os.path.join(OUT, "checks.json"), "w") as f:
        json.dump({"python": PY, "seed_pinned_no_rng": SEED,
                   "checks": checks,
                   "closest_pair_qa": qa.tolist(), "closest_pair_qb": qb.tolist(),
                   "closest_pair_sep": sep_pair,
                   "rational_field_F1": 4.0, "rational_field_DC_over_axis": 4.0},
                  f, indent=2)
    print("CHECKS")
    for k, v in checks:
        print(f"  {k}: {v}")
    print("atomic:\n", atomic_df.to_string())
    print("cps:\n", cps_df.to_string())
    print("regen:\n", regen_df.to_string())
    print("field:\n", field_df.to_string())
    print("fft:\n", fft_df.to_string())
    print("kern:\n", kern_df.to_string())
    print("slice:\n", slice_df.to_string())
    print("sep:\n", sep_df.to_string())

if __name__ == "__main__":
    main()
