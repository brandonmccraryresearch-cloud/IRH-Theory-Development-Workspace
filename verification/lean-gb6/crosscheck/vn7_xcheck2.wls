(* v-n7 verifier-authored Wolfram cross-check (EXP-1313). key=value args: label=... *)
args = Association[Rule @@@ (StringSplit[#, "=", 2] & /@ Select[Rest[$ScriptCommandLine], StringContainsQ[#, "="] &])];
Print["label=", Lookup[args, "label", "none"], " version=", $Version];
roots = Flatten[Table[Module[{v = ConstantArray[0, 4]}, v[[i]] = s; v[[j]] = t; v],
    {i, 1, 4}, {j, i + 1, 4}, {s, {1, -1}}, {t, {1, -1}}], 3];
Print["nroots=", Length[roots], " distinct=", Length[DeleteDuplicates[roots]]];
all2 = Select[Tuples[Range[-2, 2], 4], Total[#^2] == 2 &];
Print["norm2_box2=", Length[all2], " sameset=", Sort[all2] === Sort[roots]];
ks = {k1, k2, k3, k4};
B = Total[1 - Cos[ks . #] & /@ roots];
cs = Cos /@ ks;
Print["identity_residual=", FullSimplify[TrigExpand[Total[Cos[ks . #] & /@ roots]] - 2 (Total[cs]^2 - Total[cs^2])]];
cv = {c1, c2, c3, c4}; m = Maximize[{24 - 2 (Total[cv]^2 - Total[cv^2]), And @@ Thread[-1 <= cv <= 1]}, cv];
Print["Maximize_poly_in_c=", m];
Print["B(0,0,pi,pi)=", B /. Thread[ks -> {0, 0, Pi, Pi}], " B(pi,pi,pi,pi)=", B /. Thread[ks -> {Pi, Pi, Pi, Pi}]];
nm = NMaximize[{B, And @@ Thread[-Pi <= ks <= Pi]}, ks, Method -> "DifferentialEvolution", WorkingPrecision -> 30];
Print["NMaximize=", nm];
Print["VN7WL_DONE"];
