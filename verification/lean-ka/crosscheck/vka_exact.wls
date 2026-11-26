(* v-ka (verifier) EXP-1314 C-1314a: own Wolfram derivation. Run: wolframscript -file vka_exact.wls *)
Print["wolfram_version=", $Version];
P[k_, r_, a_] := r + (a - k^2)^2;
(* closed form in terms of alpha, beta with alpha^2-beta^2=a, 2 alpha beta = Sqrt[r] *)
cfab[al_, be_, x_] := Pi Exp[-be x] (al Cos[al x] + be Sin[al x])/(2 al be (al^2 + be^2));
(* parametrise by alpha,beta>0 : a = al^2-be^2, r = 4 al^2 be^2 *)
pab[k_] := (k^2 - (al + I be)^2) (k^2 - (al - I be)^2);
Print["factorisation check P - pab (a=al^2-be^2, r=4al^2be^2): ", Expand[P[k, 4 al^2 be^2, al^2 - be^2] - pab[k]]];
poles = {al + I be, -al + I be};
resSum = 2 Pi I Total[Residue[Exp[I k x]/pab[k], {k, #}] & /@ poles];
Print["residue sum - closed form (FullSimplify, al,be>0, x>0): ",
  FullSimplify[ComplexExpand[resSum - cfab[al, be, x]], al > 0 && be > 0 && x > 0]];
Print["closed form at x=Pi/al: ", FullSimplify[cfab[al, be, Pi/al], al > 0 && be > 0]];
Print["Reduce[closed(Pi/al) < 0, al>0, be>0]: ", TimeConstrained[Reduce[ForAll[{al, be}, al > 0 && be > 0, cfab[al, be, Pi/al] < 0], Reals], 120, "TIMEOUT"]];
Print["R-O candidate equality +Pi E^(-Pi be/al)/(2be(al^2+be^2)) == closed(Pi/al) holds for some al,be>0: ",
  TimeConstrained[Reduce[Exists[{al, be}, al > 0 && be > 0, cfab[al, be, Pi/al] == Pi Exp[-Pi be/al]/(2 be (al^2 + be^2))], Reals], 120, "TIMEOUT"]];
(* numeric: own points, Integrate and NIntegrate vs closed form *)
Do[
  Module[{r = pt[[1]], a = pt[[2]], z, al1, be1, xs},
   z = Sqrt[a + I Sqrt[r]]; al1 = Re[z]; be1 = Im[z];
   xs = {1/4, 1, Pi/al1, 3};
   Do[
    Module[{ex, ni, cl},
     cl = N[cfab[al1, be1, xx], 30];
     ex = TimeConstrained[N[Integrate[Cos[k xx]/P[k, r, a], {k, -Infinity, Infinity}], 30], 60, Indeterminate];
     ni = NIntegrate[Cos[k xx]/P[k, r, a], {k, -Infinity, Infinity}, WorkingPrecision -> 30, Method -> "LevinRule", MaxRecursion -> 30];
     Print["r=", r, " a=", a, " x=", N[xx, 12], " closed=", cl, " |Integrate-closed|=", Abs[ex - cl], " |NIntegrate-closed|=", Abs[ni - cl]]],
    {xx, xs}]],
  {pt, {{7/20, 8}, {7/20, 5}, {7/20, -3}, {2, 1/2}}}];
Print["V-KA-WL-DONE"];
