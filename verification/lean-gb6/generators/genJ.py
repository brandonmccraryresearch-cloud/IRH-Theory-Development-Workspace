# w-gb6: bucketed Int tables for GB6HJ (emulates stepI/insI/cmpI/filter order exactly); certificate only
exec(open('genI.py').read().split("L2=cmp")[0])
L2=cmp(step(E,[(a,1) for a in E])); S=step(E,L2)
B=[cmp([p for p in S if p[0]%11==i]) for i in range(11)]
L3=[p for b in B for p in b]
cnt=lambda x: sum(c for k,c in L3 if x+k==0)
n=[sum(c*cnt(k) for k,c in b) for b in B]
print("bucket sizes",[len(b) for b in B],"total",len(L3),"n_i",n,"H",sum(n))
lit=lambda L:"[" + ", ".join("(%d, %d)"%(k,c) for k,c in L) + "]"
out="import GB6Core\nset_option maxHeartbeats 4000000\n/-! w-gb6: bucketed literal tables from genJ.py (untrusted certificate; every value is kernel-checked). -/\nnamespace GB6\n"
for i,b in enumerate(B): out+=f"def litB{i} : List (Int × Nat) := {lit(b)}\n"
out+="def litJ3 : List (Int × Nat) := "+" ++ ".join(f"litB{i}" for i in range(len(B)))+"\n"
out+="def nB : List Nat := "+str(n).replace(" ","")+"\nend GB6\n"
open('lean/GB6HJLit.lean','w').write(out)
open('logs_local_genJ.txt','w').write(f"n={n} H={sum(n)}\n")
