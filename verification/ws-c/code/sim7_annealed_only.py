"""Re-run ONLY the sim7 annealed leg (triad ON, anneal, seed=2, noise 0.5).
The full sim7 run's first two legs were already captured (D4=0.771 triad ON,
D4=0.211 triad OFF); this closes the baseline. Verbatim logic from sim7.
"""
import sys
sys.path.insert(0, '/home/hatch/workspace/research/IRH-Theory-Development-Workspace/verification')
import sim7_fairtest as S

ph = S.run(1.0, 14000, -0.35, seed=2, anneal=True, noise_amp=0.5)
d4f = S.shell_power(ph, S.d4_idx)
cf = S.shell_power(ph, S.comp_idx)
print(f"[triad ON, annealed]     D4={d4f:.3f} competitor={cf:.3f}  (paper: 1.00 D4, independent repro: 0.895)", flush=True)
