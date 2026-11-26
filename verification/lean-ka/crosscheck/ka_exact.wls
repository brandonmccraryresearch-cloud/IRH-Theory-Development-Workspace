(* EXP-1314 C-1314a second engine (Wolfram). key=value args: r=<decimal> a=<decimal>  *)
args = Association[Rule @@@ (StringSplit[#, "="] & /@ Rest[$ScriptCommandLine])];
Print["version ", $Version];
rr = ToExpression[Lookup[args, "r", "0.35"]]; aa = ToExpression[Lookup[args, "a", "8"]];
rr = Rationalize[rr, 0]; aa = Rationalize[aa, 0];
Print["r=", rr, " a=", aa];
(* symbolic: monotonicity *)
G[s_] := 1/(r + (q - s)^2);
Print["dG/ds = ", Factor[D[G[s], s]]];
Print["Reduce[dG/ds>0 && r>0 && q>0 && 0<=s<q]: ", TimeConstrained[Reduce[ForAll[{r, q, s}, r > 0 && q > 0 && 0 <= s < q, D[G[s], s] > 0], Reals], 120]];
(* poles and residues for symbolic alpha, beta > 0 *)
den = (k - (al + I be)) (k + (al + I be)) (k - (al - I be)) (k + (al - I be));
Print["den - (r+(a-k^2)^2) with a=al^2-be^2, r=(2 al be)^2 : ", Simplify[Expand[den - ((2 al be)^2 + (al^2 - be^2 - k^2)^2)]]];
res = 2 Pi I (Residue[Exp[I k x]/den, {k, al + I be}] + Residue[Exp[I k x]/den, {k, -al + I be}]);
closed = Pi Exp[-be x] (al Cos[al x] + be Sin[al x])/(2 al be (al^2 + be^2));
Print["residue sum - closed form: ", FullSimplify[ComplexExpand[res - closed], al > 0 && be > 0 && x > 0]];
Print["closed at x=Pi/al: ", FullSimplify[closed /. x -> Pi/al, al > 0 && be > 0]];
(* direct Fourier integral at the numeric point, symbolic in x>0 *)
ft = Integrate[Cos[k x]/(rr + (aa - k^2)^2), {k, -Infinity, Infinity}, Assumptions -> x > 0];
m = Sqrt[aa^2 + rr]; alv = Sqrt[(m + aa)/2]; bev = Sqrt[(m - aa)/2];
cl = closed /. {al -> alv, be -> bev};
Do[Print["x=", xv, " Integrate=", N[ft /. x -> xv, 20], " closed=", N[cl /. x -> xv, 20], " NIntegrate=",
   NIntegrate[Cos[k xv]/(rr + (aa - k^2)^2), {k, -Infinity, Infinity}, Method -> "LevinRule", WorkingPrecision -> 25, PrecisionGoal -> 12, MaxRecursion -> 30]],
  {xv, {3/10, 11/10, 5/2}}];
xs = Pi/alv;
Print["x=Pi/alpha=", N[xs, 20], " closed=", N[cl /. x -> xs, 25], " Integrate=", N[ft /. x -> xs, 25]];
Print["exact sign of closed at Pi/alpha: ", Sign[FullSimplify[cl /. x -> xs]]];
Print["first positive zero of closed: ", N[(Pi - ArcTan[alv/bev])/alv, 20]];
Print["W1314_DONE"];
