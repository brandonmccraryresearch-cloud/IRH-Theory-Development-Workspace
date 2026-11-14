#!/usr/bin/env python3
"""Exact 24-wavevector Galerkin Model B study. Run: python3 run_study.py --out PATH
Python >=3.10; numpy, scipy, matplotlib. No manuscript source code is assumed.
The retained star is k=2*(+-e_i+-e_j); the fixed zero mode is mean=-0.18.
No spatial FFT, aliasing, off-shell modes, noise during evolution, or annealing.
"""
import os
for _key in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):
    os.environ[_key] = '1'
import argparse, csv, hashlib, itertools, json, platform, time
from pathlib import Path
import numpy as np
import scipy
from scipy.integrate import solve_ivp
from scipy.optimize import least_squares
from scipy.stats import norm
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

DEFAULTS = dict(r=-0.35, u=1., v=1., mean=-0.18, q0_squared=8.,
    box_length=2*np.pi, mobility=1., replicates=20, master_seed=931241110,
    t_final=400., rtol=2e-9, atol=2e-11, max_step=.5,
    occupancy_relative=.10, occupancy_absolute=1e-6, full_cv_max=.05,
    full_lock_min=.95, stationary_rhs_max=1e-7, equivalence_tolerance=1e-5,
    pattern_rms_noise_6_12=.01, checkpoint_dt=2.)

class Model:
    def __init__(self, p):
        self.p=p
        self.K=np.array([k for k in itertools.product([-1,0,1], repeat=4)
                         if sum(x*x for x in k)==2], dtype=int)
        self.N=24
        self.lookup={tuple(k):i for i,k in enumerate(self.K)}
        self.neg=np.array([self.lookup[tuple(-k)] for k in self.K])
        self.pos=np.array([i for i in range(24) if i<self.neg[i]])
        pairs=[]; triples=[]
        for k in self.K:
            pairs.append([(i,j) for i in range(24) for j in range(24)
                          if np.array_equal(self.K[i]+self.K[j],k)])
            triples.append([(i,j,self.lookup[tuple(k-self.K[i]-self.K[j])])
                            for i in range(24) for j in range(24)
                            if tuple(k-self.K[i]-self.K[j]) in self.lookup])
        self.pairs=np.array(pairs); self.triples=np.array(triples)
        self.triads=np.array([(i,j,l) for i in range(24) for j in range(i+1,24)
                             for l in range(j+1,24)
                             if np.all(self.K[i]+self.K[j]+self.K[l]==0)])
        self.alpha=p['r']+(p['q0_squared']-8)**2-2*p['u']*p['mean']+3*p['v']*p['mean']**2
        self.beta=p['u']-3*p['v']*p['mean']
        self.A=(8*self.beta+np.sqrt((8*self.beta)**2-4*141*p['v']*self.alpha))/(282*p['v'])
        self.target_rms=np.sqrt(24)*self.A
        self.perms=self.symmetries()

    def symmetries(self):
        """Full Aut(D4), including triality: 1152 root permutations."""
        matrices=[]
        for i in range(3):
            M=np.eye(4,dtype=int); M[[i,i+1]]=M[[i+1,i]]; matrices.append(M)
        M=np.eye(4); M[0,0]=-1; matrices.append(M)
        matrices.append(np.array([[1,1,1,1],[1,1,-1,-1],
                                  [1,-1,1,-1],[1,-1,-1,1]])/2)
        generators=[np.array([self.lookup[tuple(np.rint(M@k).astype(int))]
                              for k in self.K]) for M in matrices]
        identity=tuple(range(24)); seen={identity}; queue=[identity]
        for perm in queue:
            for g in generators:
                nxt=tuple(g[list(perm)])
                if nxt not in seen: seen.add(nxt); queue.append(nxt)
        assert len(queue)==1152
        return np.array(queue)

    def products(self,a):
        p=self.pairs; t=self.triples
        p2=np.sum(a[...,p[:,:,0]]*a[...,p[:,:,1]],axis=-1)
        p3=np.sum(a[...,t[:,:,0]]*a[...,t[:,:,1]]*a[...,t[:,:,2]],axis=-1)
        return p2,p3

    def rhs(self,t,y):
        a=y.reshape(-1,24); p2,p3=self.products(a)
        return (-8*self.p['mobility']*(self.alpha*a-self.beta*p2+self.p['v']*p3)).ravel()

    def energy(self,a):
        p2,p3=self.products(a)
        return (.5*self.alpha*np.sum(abs(a)**2,axis=-1)
                -self.beta/3*np.real(np.sum(np.conj(a)*p2,axis=-1))
                +self.p['v']/4*np.real(np.sum(np.conj(a)*p3,axis=-1)))

    def diagnostics(self,a):
        amp=abs(a); power=np.sum(amp**2,axis=-1); maxamp=amp.max(axis=-1)
        threshold=np.maximum(self.p['occupancy_absolute'], self.p['occupancy_relative']*maxamp)
        occupied=amp>=threshold[...,None]
        occupancy=np.sum(occupied,axis=-1)
        cv=np.std(amp,axis=-1)/np.maximum(np.mean(amp,axis=-1),1e-30)
        z=np.prod(a[...,self.triads],axis=-1)
        weight=np.sum(abs(z),axis=-1)
        lock=np.divide(np.sum(z.real,axis=-1),weight,
                       out=np.full_like(weight,np.nan),where=weight>1e-24)
        active=np.all(occupied[...,self.triads],axis=-1)
        phase=np.divide(z.real,abs(z),out=np.full_like(z.real,np.nan),where=abs(z)>1e-24)
        count=active.sum(axis=-1)
        lock_active=np.divide(np.nansum(np.where(active,phase,np.nan),axis=-1),count,
                             out=np.full_like(weight,np.nan),where=count>0)
        rhs=self.rhs(0,a.ravel()).reshape(a.shape)
        full=(occupancy==24)&(cv<=self.p['full_cv_max'])&(lock>=self.p['full_lock_min'])
        return dict(occupancy=occupancy, amplitude_cv=cv, triad_lock=lock,
            active_triad_lock=lock_active, active_triads=count, modulation_power=power,
            shell_power_fraction=np.where(power>1e-24,1.,np.nan),
            excess_energy=self.energy(a), rhs_rms=np.sqrt(np.mean(abs(rhs)**2,axis=-1)),
            full_pattern=full, mean_error=np.zeros_like(power))

    def translation_residual(self,a,b):
        """Relative L2 min over translations; unit-root phases cover scaled-star torus.
        Multistart wrapped linear phase fits, followed by complex residual minimization.
        This is a numerical equivalence test, not a certified global optimizer.
        """
        support=abs(b)>max(1e-8,1e-5*abs(b).max())
        K=self.K[support]; phase=np.angle(a[support]*np.conj(b[support]))
        rng=np.random.default_rng(441)
        best=np.inf
        starts=[np.zeros(4)]+list(rng.uniform(-np.pi,np.pi,(12,4)))
        scale=max(np.linalg.norm(a),1e-20)
        for x in starts:
            # Circular residual avoids branch-cut discontinuities.
            fit=least_squares(lambda x: np.r_[np.cos(K@x)-np.cos(phase),
                                             np.sin(K@x)-np.sin(phase)],x,
                              max_nfev=100,ftol=1e-11,xtol=1e-11,gtol=1e-11)
            r=np.linalg.norm(a-b*np.exp(1j*(self.K@fit.x)))/scale
            best=min(best,r)
            if best<self.p['equivalence_tolerance']: break
        return float(best)

    def equivalent(self,a,b):
        if np.linalg.norm(a)<1e-6 or np.linalg.norm(b)<1e-6:
            return (np.linalg.norm(a)<1e-6 and np.linalg.norm(b)<1e-6), 0.
        scale=max(np.linalg.norm(a),1e-20)
        # Permutations differing only on degenerate amplitudes can differ in phase;
        # retain every candidate, stopping at the first successful phase match.
        diff=np.linalg.norm(abs(b[self.perms])-abs(a)[None,:],axis=1)/scale
        candidates=np.flatnonzero(diff<5*self.p['equivalence_tolerance'])
        best=np.inf
        for i in candidates:
            r=self.translation_residual(a,b[self.perms[i]])
            best=min(best,r)
            if r<self.p['equivalence_tolerance']: return True,r
        return False,float(best)


def random_real(m,rng):
    a=np.zeros(24,complex)
    a[m.pos]=(rng.normal(size=12)+1j*rng.normal(size=12))/np.sqrt(2)
    a[m.neg[m.pos]]=a[m.pos].conj()
    return a/np.linalg.norm(a)


def seeds(m):
    families=['random_weak','random_matched','six_noisy_1pct','twelve_noisy_1pct',
              'full_noise_5pct','full_noise_25pct','full_noise_100pct']
    # An A2 star from alpha,beta,alpha+beta; D3 consists of roots in x4=0.
    alpha=np.array([1,-1,0,0]); beta=np.array([0,1,-1,0])
    six={tuple(k) for k in (alpha,beta,alpha+beta,-alpha,-beta,-alpha-beta)}
    base6=np.array([float(tuple(k) in six) for k in m.K],complex)
    base12=(m.K[:,3]==0).astype(complex)
    base24=np.ones(24,complex)
    basemap={'six_noisy_1pct':base6,'twelve_noisy_1pct':base12}
    states=[]; manifest=[]
    sequence=np.random.SeedSequence(m.p['master_seed'])
    children=sequence.spawn(len(families)*m.p['replicates']+3)
    counter=0
    for family in families:
        for rep in range(m.p['replicates']):
            child=children[counter]; counter+=1
            seed=int(child.generate_state(1)[0]); rng=np.random.default_rng(seed)
            z=random_real(m,rng)
            if family.startswith('random'):
                a=z*(.05 if family=='random_weak' else m.target_rms)
                perturb=None
            else:
                base=basemap.get(family,base24); base=base/np.linalg.norm(base)
                perturb=(.01 if family in basemap else
                         {'full_noise_5pct':.05,'full_noise_25pct':.25,'full_noise_100pct':1.}[family])
                a=base+perturb*z
                a=a/np.linalg.norm(a)*m.target_rms
            perm=m.perms[rng.integers(len(m.perms))]
            shift=rng.uniform(-np.pi,np.pi,4)
            a=a[perm]*np.exp(1j*m.K@shift)
            states.append(a)
            manifest.append(dict(run_id=f'{family}_{rep:02d}',family=family,replicate=rep,
                seed=seed, perturbation_relative_rms=perturb, is_control=False))
    for family,base in [('six_exact_control',base6),('twelve_exact_control',base12),
                         ('full_exact_control',base24)]:
        a=base/np.linalg.norm(base)*m.target_rms
        states.append(a)
        manifest.append(dict(run_id=family,family=family,replicate=0,seed=None,
                             perturbation_relative_rms=0.,is_control=True))
    return np.array(states),manifest


def write_csv(path,rows):
    with open(path,'w',newline='') as f:
        w=csv.DictWriter(f,fieldnames=list(rows[0])); w.writeheader(); w.writerows(rows)


def wilson(k,n):
    z=norm.ppf(.975); den=1+z*z/n; mid=(k/n+z*z/(2*n))/den
    half=z*np.sqrt(k/n*(1-k/n)/n+z*z/(4*n*n))/den
    return max(0.,mid-half),min(1.,mid+half)


def self_tests(m):
    rng=np.random.default_rng(91); a=random_real(m,rng)*m.target_rms
    d=random_real(m,rng); eps=1e-6
    p2,p3=m.products(a); mu=m.alpha*a-m.beta*p2+m.p['v']*p3
    fd=(m.energy(a+eps*d)-m.energy(a-eps*d))/(2*eps)
    exact=np.real(np.vdot(mu,d))
    rhs=m.rhs(0,a).reshape(24)
    diss=np.real(np.vdot(mu,rhs)); predicted=-8*np.sum(abs(mu)**2)
    # Direct quadrature uses unscaled roots on a 5^4 grid. Degree <=4;
    # no nonzero summed coordinate can be divisible by 5, so integration is exact.
    x=np.array(list(itertools.product(2*np.pi*np.arange(5)/5,repeat=4)))
    field=np.real(np.exp(1j*x@m.K.T)@a)
    quad=.5*m.alpha*np.mean(field**2)-m.beta/3*np.mean(field**3)+m.p['v']/4*np.mean(field**4)
    symerr=abs(m.energy(a[m.perms[731]])-m.energy(a))
    trans=a*np.exp(1j*m.K@rng.uniform(-np.pi,np.pi,4))
    eq,res=m.equivalent(trans,a)
    full=np.full(24,m.A,complex)
    results=dict(ordered_triads=int(24*m.pairs.shape[1]),ordered_quartets=int(24*m.triples.shape[1]),
        unordered_triads=len(m.triads),automorphisms=len(m.perms),alpha=m.alpha,beta=m.beta,
        analytic_amplitude=m.A,analytic_excess_energy=float(m.energy(full)),
        full_stationary_rhs_rms=float(np.sqrt(np.mean(abs(m.rhs(0,full))**2))),
        gradient_fd_absolute_error=float(abs(fd-exact)),quadrature_energy_error=float(abs(quad-m.energy(a))),
        dissipation_identity_error=float(abs(diss-predicted)),symmetry_energy_error=float(symerr),
        translated_state_equivalence=bool(eq),translation_test_residual=res)
    assert abs(fd-exact)<1e-8 and abs(quad-m.energy(a))<1e-12
    assert symerr<1e-12 and eq
    return results


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--out',default=str(Path(__file__).resolve().parent))
    ap.add_argument('--replicates',type=int,default=20)
    ap.add_argument('--t-final',type=float,default=400.)
    ap.add_argument('--rtol',type=float,default=DEFAULTS['rtol'])
    ap.add_argument('--atol',type=float,default=DEFAULTS['atol'])
    ap.add_argument('--max-step',type=float,default=DEFAULTS['max_step'])
    ap.add_argument('--seed',type=int,default=DEFAULTS['master_seed'])
    ap.add_argument('--skip-equivalence',action='store_true',help='Skip numerical symmetry clustering')
    args=ap.parse_args(); out=Path(args.out); out.mkdir(parents=True,exist_ok=True)
    p=DEFAULTS.copy(); p.update(replicates=args.replicates,t_final=args.t_final,
        rtol=args.rtol,atol=args.atol,max_step=args.max_step,master_seed=args.seed)
    m=Model(p); tests=self_tests(m)
    initial,manifest=seeds(m); n=len(initial)
    with open(out/'seed_manifest.json','w') as f: json.dump(manifest,f,indent=2)
    np.savez_compressed(out/'initial_states.npz',coefficients=initial,wavevectors=2*m.K)
    ts=np.unique(np.r_[0,np.geomspace(.01,2,25),np.arange(2,p['t_final'],p['checkpoint_dt']),p['t_final']])
    start=time.perf_counter()
    sol=solve_ivp(m.rhs,(0,p['t_final']),initial.ravel(),method='DOP853',t_eval=ts,
        rtol=p['rtol'],atol=p['atol'],max_step=p['max_step'])
    assert sol.success,sol.message
    trajectory=sol.y.T.reshape(-1,n,24)
    elapsed=time.perf_counter()-start
    final=trajectory[-1]; diag=m.diagnostics(trajectory)
    np.savez_compressed(out/'trajectories.npz',times=ts,coefficients=trajectory,wavevectors=2*m.K,
                        **{k:v for k,v in diag.items()})
    rows=[]; representatives=[]; clusters=[]
    # Uniform endpoints form one class, not a cloud distinguished by negligible residuals.
    for i,record in enumerate(manifest):
        row=record.copy()
        for k,v in diag.items():
            item=v[-1,i].item(); row[k]=item
        row['initial_occupancy']=int(diag['occupancy'][0,i])
        row['initial_excess_energy']=float(diag['excess_energy'][0,i])
        row['max_saved_energy_increase']=float(max(0,np.diff(diag['excess_energy'][:,i]).max()))
        row['conjugacy_error']=float(np.max(abs(final[i,m.neg]-final[i].conj())))
        row['stationary']=bool(row['rhs_rms']<=p['stationary_rhs_max'])
        if row['modulation_power']<1e-12:
            row['outcome']='uniform'; row['occupancy']=0; row['shell_power_fraction']=None
            row['amplitude_cv']=None; row['triad_lock']=None; row['active_triad_lock']=None
            row['active_triads']=0
        elif row['full_pattern']: row['outcome']='full24'
        elif row['occupancy']==6: row['outcome']='six_mode'
        elif row['occupancy']==12: row['outcome']='twelve_mode'
        else: row['outcome']='other'
        if not row['stationary']: row['outcome']='unresolved_'+row['outcome']
        group=None; residual=None
        if not args.skip_equivalence:
            for j,rep in enumerate(representatives):
                ok,res=m.equivalent(final[i],rep)
                if ok: group=f'S{j+1:02d}'; residual=res; break
            if group is None:
                representatives.append(final[i]); group=f'S{len(representatives):02d}'; residual=0.
        row['symmetry_class']=group; row['equivalence_residual']=residual
        clusters.append(group); rows.append(row)
    write_csv(out/'basin_outcomes.csv',rows)
    summary=[]
    for family in dict.fromkeys(r['family'] for r in rows):
        rr=[r for r in rows if r['family']==family]; nn=len(rr)
        successes=sum(r['outcome']=='full24' for r in rr)
        lo,hi=wilson(successes,nn)
        s=dict(family=family,n=nn,full24=successes,full24_fraction=successes/nn,
               wilson95_low=None if rr[0]['is_control'] else lo,
               wilson95_high=None if rr[0]['is_control'] else hi,
               uniform=sum(r['outcome']=='uniform' for r in rr),
               six_mode=sum(r['outcome']=='six_mode' for r in rr),
               twelve_mode=sum(r['outcome']=='twelve_mode' for r in rr),
               other=sum(r['outcome']=='other' for r in rr),
               unresolved=sum(not r['stationary'] for r in rr),
               symmetry_classes=';'.join(sorted(set(str(r['symmetry_class']) for r in rr))))
        for metric in ['occupancy','amplitude_cv','triad_lock','excess_energy','modulation_power']:
            values=np.array([r[metric] for r in rr],float)
            values=values[np.isfinite(values)]
            s[metric+'_mean']=float(np.mean(values)) if len(values) else None
            s[metric+'_sd']=float(np.std(values,ddof=1)) if len(values)>1 else None
            s[metric+'_min']=float(np.min(values)) if len(values) else None
            s[metric+'_max']=float(np.max(values)) if len(values) else None
        summary.append(s)
    write_csv(out/'basin_summary.csv',summary)
    trace_rows=[]
    for ti,t in enumerate(ts):
        for i,record in enumerate(manifest):
            row=dict(run_id=record['run_id'],time=float(t))
            row.update({k:v[ti,i].item() for k,v in diag.items()})
            trace_rows.append(row)
    write_csv(out/'diagnostic_traces.csv',trace_rows)
    np.savez_compressed(out/'symmetry_representatives.npz',coefficients=np.array(representatives),
                        wavevectors=2*m.K,automorphism_permutations=m.perms)
    p.update(model='exact 24-wavevector Galerkin truncation; fixed zero mode',
        solver='scipy.integrate.solve_ivp DOP853',n_runs=n,nfev=sol.nfev,elapsed_seconds=elapsed,
        python=platform.python_version(),numpy=np.__version__,scipy=scipy.__version__,
        matplotlib=matplotlib.__version__,unit='dimensionless; energy is excess density F/V',
        full_success='stationary, occupancy=24, amplitude CV<=0.05, signed triad lock>=0.95',
        shell_fraction_warning='1 by construction for every nonzero retained state; undefined at uniform',
        symmetry_group='Aut(D4), 1152 elements, plus continuous torus translations',
        script_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),validation=tests,
        source_sections='McCrary v93.1 I.2-I.3 and II.7-II.9; gap-memo G1',
        initial_distributions='Circular Gaussian directions normalized to fixed real-space modulation RMS; not unrestricted random fields',
        uniform_power_threshold=1e-12,
        phase_lock_definition='sum Re(a_i a_j a_l) / sum |a_i a_j a_l| over 32 unordered zero-sum triads',
        amplitude_cv_definition='population SD of all 24 |a_k| divided by their mean',
        occupancy_definition='|a_k| >= max(1e-6,0.1*max_j |a_j|); uniform power<1e-12 overrides occupancy to zero',
        stability_note='Stationarity is not stability. Exact partial controls can lie on invariant saddle subspaces.')
    with open(out/'parameters.json','w') as f: json.dump(p,f,indent=2,allow_nan=False)
    make_figure(m,manifest,rows,summary,ts,diag,out)
    print(json.dumps(dict(runs=n,nfev=sol.nfev,elapsed_seconds=elapsed,validation=tests,
                          summary=[{k:s[k] for k in ['family','n','full24','uniform','six_mode','twelve_mode','other','unresolved','symmetry_classes']} for s in summary]),indent=2))


def make_figure(m,manifest,rows,summary,ts,diag,out):
    families=list(dict.fromkeys(r['family'] for r in rows if not r['is_control']))
    labels=['Random\nRMS .05','Random\nmatched RMS','6 modes\n+1% noise','12 modes\n+1% noise',
            'Full\n+5% noise','Full\n+25% noise','Full\n+100% noise']
    colors=plt.get_cmap('tab10')(np.arange(len(families)))
    fig,ax=plt.subplots(2,3,figsize=(15,9),constrained_layout=True)
    rng=np.random.default_rng(1)
    for j,family in enumerate(families):
        idx=[i for i,r in enumerate(rows) if r['family']==family]
        xx=j+rng.uniform(-.18,.18,len(idx))
        ax[0,0].scatter(xx,[rows[i]['occupancy'] for i in idx],s=23,color=colors[j],alpha=.65)
        ax[0,1].scatter(xx,[rows[i]['amplitude_cv'] if rows[i]['outcome']!='uniform' else np.nan for i in idx],s=23,color=colors[j],alpha=.65)
        ax[0,2].scatter(xx,[rows[i]['triad_lock'] if rows[i]['outcome']!='uniform' else np.nan for i in idx],s=23,color=colors[j],alpha=.65)
        ss=next(s for s in summary if s['family']==family)
        ax[1,0].errorbar(j,ss['full24_fraction'],yerr=[[ss['full24_fraction']-ss['wilson95_low']],
                            [ss['wilson95_high']-ss['full24_fraction']]],fmt='o',color=colors[j],capsize=4)
        E=diag['excess_energy'][:,idx]
        ax[1,1].plot(ts,np.median(E,axis=1),color=colors[j],label=labels[j].replace('\n',' '))
        ax[1,1].fill_between(ts,np.min(E,axis=1),np.max(E,axis=1),color=colors[j],alpha=.12)
        P=diag['modulation_power'][:,idx]
        ax[1,2].plot(ts,np.median(P,axis=1),color=colors[j])
        ax[1,2].fill_between(ts,np.min(P,axis=1),np.max(P,axis=1),color=colors[j],alpha=.12)
    for axis in [ax[0,0],ax[0,1],ax[0,2],ax[1,0]]:
        axis.set_xticks(range(len(families)),labels,fontsize=8); axis.grid(axis='y',alpha=.2)
    ax[0,0].set(ylabel='Occupied signed wavevectors / 24',ylim=(-1,25),title='A  Final occupancy (10% threshold)')
    ax[0,1].set(ylabel='SD(|a|) / mean(|a|)',title='B  Final amplitude variation')
    ax[0,1].axhline(.05,color='k',ls=':',lw=1)
    ax[0,2].set(ylabel='Weighted signed cos(triad phase)',ylim=(-.05,1.05),title='C  Final triad phase locking')
    ax[0,2].axhline(.95,color='k',ls=':',lw=1)
    ax[1,0].set(ylabel='Full-pattern frequency (Wilson 95% CI)',ylim=(-.04,1.04),
                title=f'D  Conditional outcomes; n={m.p["replicates"]} each')
    ax[1,1].set(xlabel='Model B time',ylabel='Excess free-energy density',title='E  Median and full replicate range')
    ax[1,1].axhline(float(m.energy(np.full(24,m.A))),color='k',ls=':',lw=1)
    ax[1,1].set_xscale('symlog',linthresh=.1); ax[1,1].legend(fontsize=7,loc='best')
    ax[1,2].set(xlabel='Model B time',ylabel='Modulation power = sum |a_k|²',title='F  Shell power (absolute, not fraction)')
    ax[1,2].set_xscale('symlog',linthresh=.1)
    fig.suptitle('24-mode truncation only: fixed mean −0.18, r=−0.35, q₀²=8, u=v=1\n'
                 'Shell fraction is 100% by construction, not evidence for D₄ selection. Uniform states omitted from B/C.',fontsize=12)
    fig.savefig(out/'basin_figure.png',dpi=180)
    fig.savefig(out/'basin_figure.svg')
    plt.close(fig)

if __name__=='__main__': main()
