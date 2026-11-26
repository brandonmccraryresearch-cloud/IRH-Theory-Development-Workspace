\\ v-ka (verifier) EXP-1314 C-1314a: own residue derivation + quadrature in PARI/GP
\p 60
default(seriesprecision, 30);
print("pari_version=", version());
\\ closed form (verifier's own derivation): z=alpha+i beta, z^2 = a + i sqrt(r)
cf(r,a,x) = my(z=sqrt(a+I*sqrt(r)), al=real(z), be=imag(z)); Pi*exp(-be*x)*(al*cos(al*x)+be*sin(al*x))/(2*al*be*(al^2+be^2));
\\ residue route: roots of P(k)=r+(a-k^2)^2 in the upper half plane, 2 pi i sum e^{ikx}/P'(k)
res(r,a,x) = my(P=r+(a-'k^2)^2, dP=deriv(P,'k), R=polroots(P), s=0, nu=0); for(j=1,#R, if(imag(R[j])>0, nu++; s+=exp(I*R[j]*x)/subst(dP,'k,R[j]))); if(nu!=2, error("UHP root count ",nu)); 2*Pi*I*s;
\\ quadrature route: 2*int_0^oo cos(kx)/P(k) dk, PARI oscillatory endpoint
quad(r,a,x) = 2*intnum(t=0,[+oo, x*I], cos(t*x)/(r+(a-t^2)^2));
alb(r,a) = my(z=sqrt(a+I*sqrt(r))); [real(z),imag(z)];
check(r,q,kp2) = {
  my(a=q-kp2, ab=alb(r,a), al=ab[1], be=ab[2], xs=[0, 3/10, 1, Pi/(2*al), Pi/al, 5/2, 3*Pi/al], out);
  print("case r=",r," q0^2=",q," kperp^2=",kp2," a=",a," alpha=",al," beta=",be, " check alpha^2-beta^2-a=", al^2-be^2-a, " 2ab-sqrt(r)=", 2*al*be-sqrt(r));
  for(i=1,#xs, my(x=xs[i], c=cf(r,a,x), rs=res(r,a,x), qd=if(x==0, 2*intnum(t=0,[+oo,1],1/(r+(a-t^2)^2)), quad(r,a,x)));
    printf("  x=%.12g closed=%.25g |res-closed|=%.3g imag(res)=%.3g |quad-closed|=%.3g\n", x, c, abs(rs-c), abs(imag(rs)), abs(qd-c)));
  my(gpi=cf(r,a,Pi/al), pred=-Pi*exp(-Pi*be/al)/(2*be*(al^2+be^2)));
  printf("  Ghat(pi/alpha)=%.30g  -pi e^{-pi b/a}/(2b(a^2+b^2))=%.30g diff=%.3g sign=%d\n", gpi, pred, gpi-pred, sign(gpi));
  printf("  R-O candidate +pi e^{-pi b/a}/(2b(a^2+b^2))=%.30g  (Ghat - that)=%.6g\n", -pred, gpi+pred);
  \\ first positive zero of Ghat: al x + atan(al/be)... solve numerically
  my(x0=solve(x=1e-9, Pi/al, cf(r,a,x))); printf("  first zero x0=%.15g  (pi - atan(alpha/beta))/alpha=%.15g\n", x0, (Pi-atan(al/be))/al);
  \\ Hankel RP test on the half line, times t_i=i*dt
  my(n=8, dt=Pi/(4*al), H=matrix(n,n,i,j, cf(r,a,(i+j)*dt)), ev=mateigen(H,1)[1]);
  printf("  Hankel[Ghat(t_i+t_j)] n=%d dt=pi/(4alpha): min eig=%.6g max eig=%.6g\n", n, vecmin(real(ev)), vecmax(real(ev)));
}
check(35/100, 8, 0);
check(35/100, 8, 4);
check(35/100, 8, 12);
check(1, 1, 0);
check(1/1000, 8, 2);
check(50, 3, 0);
\\ controls through the same 1D Hankel pipeline
ctl(name, f) = { my(n=8, dt=1/2, H=matrix(n,n,i,j, f((i+j)*dt)), ev=real(mateigen(H,1)[1])); printf("control %s: Hankel min eig=%.6g max=%.6g\n", name, vecmin(ev), vecmax(ev)); }
\\ positive: FT of 1/(k^2+m^2) = pi e^{-m x}/m ; negative: 1/(k^2+1)-1/(k^2+4) -> pi e^{-x} - pi e^{-2x}/2
ctl("pos 1/(k^2+1)", x->Pi*exp(-x));
ctl("pos mix 1/(k^2+1)+3/(k^2+9)", x->Pi*exp(-x)+Pi*exp(-3*x));
ctl("neg 1/(k^2+1)-1/(k^2+4)", x->Pi*exp(-x)-Pi*exp(-2*x)/2);
\\ seeded random counterexample search (own seed), sign at pi/alpha by residues AND quadrature
setrand(20261125); nneg=0; nq=0; mx=0;
for(j=1,200, my(r=random(10^6)/10^5+1/10^4, q=random(10^6)/10^5+1/10^4, kp2=random(2*10^6)/10^5, a=q-kp2, ab=alb(r,a), x=Pi/ab[1], rs=real(res(r,a,x)), qd=quad(r,a,x)); nq++; if(rs<0 && qd<0, nneg++); mx=max(mx, abs(rs-qd)/abs(rs)));
printf("random search: tested=%d negative_by_both=%d max_rel(res vs quad)=%.3g\n", nq, nneg, mx);
print("V-KA-GP-DONE");
quit;
