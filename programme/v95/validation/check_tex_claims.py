"""Claim checker for IRH_v95_draft.tex: every load-bearing number in the text is
recomputed or matched against the adjudicated record value; forbidden statements
(retracted, over-graded or known-false claims) must be absent."""
import re, sys, math
from fractions import Fraction as Fr
tex = open(sys.argv[1]).read()
fails = []; passes = 0
def need(cond, msg):
    global passes
    if cond: passes += 1
    else: fails.append(msg)
# exact selection numbers, recomputed
S_D4 = Fr(192**2, 24**3) / Fr(3384, 24**2); S_A4 = Fr(120**2, 20**3) / Fr(1860, 20**2)
need(S_D4 == Fr(64,141) and "64/141" in tex, "S_D4")
need(S_A4 == Fr(12,31) and "12/31" in tex, "S_A4*")
need(S_D4/S_A4 == Fr(496,423) and "496/423" in tex, "ratio")
need(Fr(16,45) == Fr(48**2,12**3)/Fr(540,144) and "16/45" in tex, "bcc")
need(abs(758/6561*100 - 11.5531) < 5e-5 and "11.5531" in tex, "band")
need(abs(756/6561*100 - 11.5226) < 5e-5 and "11.5226" in tex, "one-mode band")
# phonons
need("1.731985" in tex and abs(math.sqrt(15.996363/5.332526) - 1.731985) < 2e-6, "cL/cT relaxed")
need(abs(256*0.0775753**2 - 1.5405892) < 1e-6, "256A^2 one-mode")
need(abs(5.332526*0.2896648 - 1.54465) < 1e-5, "mu relaxed")
# relaxed rho differs from one-mode 48A^2 by harmonics (4e-5 relative); text gives rho as measured
need(abs(48*0.0776817**2/0.2896648 - 1) < 1e-4, "rho ~ 48 A^2 (one-mode)")
# barrier
need("119.06" in tex and abs(550.93057/119.06 - 4.63) < 0.01, "barrier ratio")
need(abs(34*119.06/550.93057 - 7.3) < 0.05, "barrier/noise 7.3")
# r_eff
need(abs(-0.35 + 0.36 + 3*0.0324 - 0.1072) < 1e-12, "r_eff")
# alpha
a = 137 + 1/(28 - math.pi/14)
need(abs(a - 137.0360028219) < 1e-9 and abs((a - 137.035999177)/2.1e-8 - 173.6) < 0.1, "alpha sigma")
# CFL
need(abs(4/3*(math.sqrt(3)/2)**2 - 1) < 1e-15 and abs(16*math.pi**2/3 - 52.64) < 0.01, "CFL")
# content fixes (2026-11-25, figure pass)
need(abs(550.93057/36.95 - 14.9) < 0.05 and abs(550.93057/138.12 - 4.0) < 0.02
     and "550.93/36.95\\approx14.9" in tex and "550.93/138.12\\approx4.0" in tex, "thin-wall factors 14.9 and 4.0 both stated")
need("about $15$ times the first thin-wall estimate and about $4.0$ times the second" in tex, "thin-wall summary sentence covers both routes")
need(re.search(r"one-mode band, computed on a \$161\\times161\$ grid of the same window[^.]*from \$11\.60\\%\$ at \$w_6=0\$", tex) is not None,
     "w6 sentence: 11.60% scoped as one-mode 161x161")
need("not the canonical full-field value $11.5531\\%$" in tex and "one-mode value $11.5226\\%$ on that grid" in tex, "w6 sentence distinguishes 11.5531/11.5226")
# figures: every figure is referenced from the text, and figure grades match the record
labels = re.findall(r"\\label\{(fig:[^}]*)\}", tex)
for lab in labels:
    need(("\\ref{" + lab + "}") in tex, f"figure {lab} not referenced from the text")
def cap(lab):
    i = tex.find("\\label{" + lab + "}"); j = tex.rfind("\\caption{", 0, i); return tex[j:i]
need("\\grade{F3/I1}" in cap("fig:band") and "758/6561=11.5531" in cap("fig:band"), "fig:band grade F3/I1")
need("\\grade{F2/I1}" in cap("fig:phonons") and "\\grade{B, [MV]4D/I1}" in cap("fig:phonons"), "fig:phonons grades")
need("\\grade{F2/I1}" in cap("fig:droplet") and "119.06\\pm0.03" in cap("fig:droplet"), "fig:droplet grade")
need("\\grade{F2/I1}" in cap("fig:hessian") and "0.3423000506" in cap("fig:hessian"), "fig:hessian grade")
need("6.7\\times10^{-11}" in cap("fig:rotd4") and "-5.6\\times10^{-13}" in cap("fig:rotd4"), "fig:rotd4 both N24 offsets")
need("exact" not in cap("fig:rotd4").split("census")[-1][:60], "fig:rotd4 census not graded 'exact'")
# forbidden statements (record-state guards)
forbidden = [
  (r"c_L/c_T\s*=\s*\\sqrt\{?2", "cL/cT = sqrt2 (false: sqrt3)"),
  (r"\babstain", "abstain wording"),
  (r"11\.85\\%(?![\s\S]{0,120}(not reproducible|cannot be reproduced|appeared))", "11.85% cited as a value"),
  (r"three generations (is|are) (derived|predicted)", "generations derived"),
  (r"(?<!mathematics of this section is exact )\\grade\{A", "grade A given to a physical claim (only algebra is A)"),
  (r"Washburn", "Washburn D4* paper cited"),
  (r"\$S\$ is (an|the) (Perelman )?entropy", "S identified with an entropy"),
  (r"90417-6", "wrong GRS DOI"),
  (r"math/0607446", "wrong arXiv id on EKR"),
  (r"(B|reading \(B\)) is the working reading", "(B) still working"),
  (r"\$46\\times|46 times", "barrier factor 46 (false)"),
  (r"differ by a factor of about \$15\$", "thin-wall factor 15 stated for both routes"),
  (r"about \$15\$ times the thin-wall value", "thin-wall summary for one route only"),
  (r"reduces the one-mode band from \$11\.60", "11.60% without grid scope"),
]
bib = tex[tex.find("\\begin{thebibliography}"):]
for pat, msg in forbidden:
    m = re.search(pat, bib if msg.startswith("wrong") else tex, re.I)
    need(m is None, f"FORBIDDEN present: {msg}: ...{tex[max(0,m.start()-60):m.end()+20] if m else ''}...")
print(f"PASS {passes}  FAIL {len(fails)}")
for f in fails: print("FAIL:", f)
sys.exit(1 if fails else 0)
