# w-gb6: emulate GB6HI tables (DI1, stepI, insI, cmpI) exactly; emit Lean literals (certificate, kernel-checked)
def intRange(r): return [i-r for i in range(2*r+1)]
def box(r,d): return [[]] if d==0 else [[x]+v for x in intRange(r) for v in box(r,d-1)]
D4=[v for v in box(1,4) if sum(x*x for x in v)==2]
enc=lambda v: v[0]+13*v[1]+169*v[2]+2197*v[3]
E=[enc(v) for v in D4]
step=lambda L,D:[(k+a,c) for (k,c) in D for a in L]
def ins(q,D):
    for i,p in enumerate(D):
        if p[0]==q[0]: return D[:i]+[(p[0],p[1]+q[1])]+D[i+1:]
    return D+[q]
def cmp(D):
    acc=[]
    for p in reversed(D): acc=ins(p,acc)
    return acc
L2=cmp(step(E,[(a,1) for a in E])); L3=cmp(step(E,L2))
H=sum(c*sum(c2 for k2,c2 in L3 if k+k2==0) for k,c in L3)
print("E distinct",len(set(E)),"L2",len(L2),sum(c for _,c in L2),"L3",len(L3),sum(c for _,c in L3),"H",H)
lit=lambda L:"[" + ", ".join("(%d, %d)"%(k,c) for k,c in L) + "]"
open('lean/GB6HILit.lean','w').write("import GB6Core\nset_option maxHeartbeats 4000000\n/-! w-gb6: Int-keyed literal tables from genI.py (untrusted certificate; kernel-checked by evaluation). -/\nnamespace GB6\ndef litI2 : List (Int × Nat) := "+lit(L2)+"\ndef litI3 : List (Int × Nat) := "+lit(L3)+"\nend GB6\n")
