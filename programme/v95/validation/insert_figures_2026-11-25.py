"""One-off edit script (2026-11-25): insert the eight record-computed figures into
IRH_v95_draft.tex and apply the two content fixes. Run once on the HEAD 3ab787d text;
the three existing-figure text references (fig:causal, fig:nr, fig:chain) were added by a
separate small edit recorded in CHANGELOG.md. Every replacement must match
exactly once, or the script stops without writing."""
import sys
p = sys.argv[1]
tex = open(p).read()

def rep(old, new):
    global tex
    n = tex.count(old)
    if n != 1:
        sys.exit(f"anchor found {n} times: {old[:80]!r}")
    tex = tex.replace(old, new)

def fig(path, label, cap):
    return ("\\begin{figure}[htbp]\n\\centering\n"
            f"\\includegraphics[width=\\textwidth]{{figs/{path}}}\n"
            f"\\caption{{{cap}}}\n\\label{{{label}}}\n\\end{{figure}}\n")

CAP1 = (r"The $24$ roots $\Phi=\{\pm e_i\pm e_j\}$ of $D_4$ as the vertices of the $24$-cell. "
 r"(a) Orthogonal projection onto the Coxeter plane of $W(F_4)$, the eigenplane of the Coxeter element $s_1s_2s_3s_4$ for the eigenvalue $e^{2\pi i/12}$ (order $12$); the roots fall on two rings of $12$. "
 r"(b) Stereographic projection of $\Phi/\sqrt2\subset S^3$ from the pole $-c$, $c=\tfrac12(1,1,1,1)$, the centre of an octahedral cell; edges are drawn as the images of great-circle arcs. Stereographic projection preserves circles and angles but not lengths, so vertices near the pole appear far out. "
 r"(c) For a fixed root $\alpha$, the number of roots $\beta$ at each inner product: $1,8,6,8,1$ at $\alpha\cdot\beta=2,1,0,-1,-2$. "
 r"Grey lines in (a) and (b) are the $96$ pairs with $\alpha\cdot\beta=1$ ($60^\circ$). Each root also has $8$ partners at $120^\circ$ ($\alpha\cdot\beta=-1$), and each such pair closes a zero-sum triad with $-(\alpha+\beta)$, which gives the $T=24\cdot8=192$ ordered triads of Section~\ref{sec:selection}. "
 r"Markers and colours mark the three $16$-cells (roots supported on coordinate pairs $\{12,34\}$, $\{13,24\}$, $\{14,23\}$). Exact computation from $\Phi$; no simulation data.")

CAP2 = (r"The binary tetrahedral group $2T$ in $S^3$ and its decomposition into Hopf fibres. The group consists of the $24$ unit Hurwitz quaternions $\pm1$, $\pm\mathbf i$, $\pm\mathbf j$, $\pm\mathbf k$ and $\tfrac12(\pm1\pm\mathbf i\pm\mathbf j\pm\mathbf k)$. "
 r"For a unit pure quaternion $u$, the Hopf map $q\mapsto quq^{-1}$ has the great circles $q\,e^{\theta u}$ as fibres, and $g,g'\in2T$ lie on one fibre if and only if $g^{-1}g'\in2T\cap\{e^{\theta u}\}$. "
 r"(a) $u=\mathbf i$: $2T\cap\{e^{\theta\mathbf i}\}=C_4$, so $2T$ lies on $6$ fibres of $4$ elements, over the $6$ vertices of an octahedron in the base $S^2$ (inset). "
 r"(b) $u=(\mathbf i+\mathbf j+\mathbf k)/\sqrt3$: the intersection is $C_6$, and $2T$ lies on $4$ fibres of $6$, the four Clifford-parallel great hexagons, over the vertices of a regular tetrahedron. "
 r"For a generic axis such as $(\mathbf i+\mathbf j)/\sqrt2$ the intersection is $\{\pm1\}$ and the fibres hold $2$ elements each ($12$ fibres; not drawn). "
 r"Each panel is a stereographic projection to $\mathbb R^3$ from a pole chosen, by a seeded search, to maximise the distance to the drawn fibres; circles stay circles, lengths are distorted. Colour identifies the fibre and its base point. "
 r"The Gauss linking number of every pair of drawn fibres, computed numerically on the projected curves, is $1$. Exact computation; the figure illustrates group structure and makes no physical claim.")

CAP3 = (r"The relaxed $D_4$ crystal $\psi(\mathbf x)$ on three-dimensional slices $x_4=0,\ \pi/8,\ \pi/4,\ 3\pi/8$ of the four-dimensional cell. "
 r"Top row: the isosurface $\varphi=\psi-\bar\psi=0.6$ (density maxima) in the cube $[0,\pi]^3$. Bottom row: $\varphi$ on the plane $x_3=0$ of the same slices, diverging scale centred at $\varphi=0$, with the $0.6$ contour overlaid. "
 r"State: run 13 (K-B1) relaxed state \texttt{st2\_p1\_N16} on the $L=\pi$ cell, $N=16^4$, $r=-0.35$, $\bar\psi=-0.18$, $u=v=1$, $q_0^2=8$, $w_6=0$, excess free energy $-0.007727623603413392$. "
 r"Its $24$ dominant Fourier modes all lie on $|\mathbf k|^2=q_0^2=8$ with common amplitude $A=0.07768174836386046$; the largest harmonic is $3.4\times10^{-4}$. "
 r"Each slice is evaluated exactly from the stored Fourier coefficients (trigonometric interpolation of the solver's own spectral representation, $16\to48$ points per axis) and reproduces the grid values to $9\times10^{-16}$; the isosurfaces use marching cubes, a linear interpolation on the $48^3$ grid. No smoothing is applied. "
 r"This is the state from which the phonon values of Section~\ref{sec:phonons} are computed (those values \grade{F2/I1}); the rendering adds no claim of its own.")

CAP4 = (r"The $D_4$ band of run 12 (gap G-A19, relaxed full field, $L=\pi$, $N=16^4$, $u=v=1$, $q_0^2=8$, $w_6=0$, no detuning), drawn cell by cell from the record table with no interpolation. "
 r"The window is $r=-0.6+0.00875\,k$, $\bar\psi=-0.6+0.01\,j$ ($k,j=0,\dots,80$; $6561$ points). The record computed only $\bar\psi\in[-0.38,0.08]$ ($3807$ points), and the hatched strips were not computed; the band count treats them as outside the band, and no band point lies on the computed edges. "
 r"(a) Lowest relaxed state at each point among the frozen competitor set of the record: disordered, hex6, fcc12 or the full $24$-mode $D_4$ state. The $D_4$ state wins at $758$ points, $758/6561=11.5531\%$, for $\bar\psi\in[-0.33,0.05]$. "
 r"(b) Margin $F_{D_4}-F_{\text{best non-}D_4}$ where the $D_4$ state exists; diverging scale centred at $0$, with separate linear scales for the two signs (range $-0.00612$ to $+0.0493$); the black contour is the margin zero. "
 r"Dashed curve: the exact line $r_{\rm eff}=r-2\bar\psi+3\bar\psi^2=0$, below and right of which the uniform state is linearly unstable. Star: operating point $(\bar\psi,r)=(-0.18,-0.35)$. "
 r"Band fraction \grade{F3/I1}; this is a finite-box, finite-grid statement.")

CAP5 = (r"Long-wavelength phonons of the relaxed $D_4$ crystal. Run 13, K-B1; state \texttt{st2\_p1\_N24} with $L=\pi$, $N=24^4$, $r=-0.35$, $\bar\psi=-0.18$, $w_6=0$; Bloch Hessian on the Galerkin ball $|\mathbf n|^2\le32$, Feshbach-reduced. "
 r"Markers are the recorded eigenvalues $\lambda(\mathbf q)$ at $|\mathbf q|=0.005,\dots,0.16$ along six directions; $\omega=\sqrt{\lambda}$ is the frequency of the wave equation \eqref{eq:dw} with the damping taken to zero. Branches are assigned by the recorded longitudinal fraction of the polarisation. "
 r"(a) $\omega$ against $|\mathbf q|$: three transverse and one longitudinal branch per direction, with the lines $\omega=c_T|\mathbf q|$, $\omega=c_L|\mathbf q|$ for the relaxed values $c_T^2=5.332526$, $c_L^2=15.996363$, and the optical level $\sqrt{0.3423}$ (dotted). "
 r"(b) $\lambda/(c^2|\mathbf q|^2)$ for each branch: all six directions tend to $1$ together, so the dispersion is isotropic at order $q^2$; the spread at larger $|\mathbf q|$ is the $O(q^4)$ anisotropy through $P_6$. "
 r"(c) The two dispersion cones over the $(q_1,q_2)$ plane, with the in-plane data along $(1,0,0,0)$ and $(1,1,0,0)$; $c_L/c_T=1.731985$, against $\sqrt3=1.732051$. "
 r"Relaxed values \grade{F2/I1}; one-mode ratio $\sqrt3$ \grade{B, [MV]4D/I1}. Scope: the $L=\pi$ crystal at one point of the band, at zero damping; at the damping $\gamma=1.2$ of the quenches these modes are overdamped below $q\approx0.15$ (longitudinal) and $0.26$ (transverse).")

CAP6 = (r"Standard and rotated $D_4$ states in the box $L=3\pi$ (run 13, gap G-D3, point $P_1=(r,\bar\psi)=(-0.35,-0.14)$). "
 r"Grey dots: the $312$ vectors of the unstable shell $|\mathbf n|^2=18$ ($24$ of type $(3,3,0,0)$, $96$ of $(4,1,1,0)$, $192$ of $(3,2,2,1)$). "
 r"Coloured markers: the $24$ occupied wavevectors of three recorded end states, coloured by type, with lines joining pairs at $\mathbf n\cdot\mathbf n'=9$ ($60^\circ$). "
 r"(a) The axis-aligned star (run \texttt{P1\_N32\_s2}). (b) A rotated system of $8$ vectors of type $(4,1,1,0)$ and $16$ of type $(3,2,2,1)$ (\texttt{P1\_N24\_s1}). (c) A mixed system, $6+6+12$ (\texttt{P1\_N24\_s5}). "
 r"All three panels use one fixed lab-frame projection, the Coxeter plane of Figure~\ref{fig:d4cell}, so only (a) shows the $12$-fold picture; (b) and (c) are the same root system seen at a rotated angle. "
 r"(d) The off-diagonal Gram values of the three sets are identical, $96\times9$, $72\times0$, $96\times(-9)$, $12\times(-18)$, which is $9$ times the $D_4$ Gram matrix; for each set the script constructs an explicit orthogonal $Q$ with $Q(3\Phi)$ equal to the set, to $2\times10^{-15}$. "
 r"The shell contains exactly $41$ such subsystems ($1$ standard, $24$ of type $8+16$, $16$ of type $6+6+12$); this census and the shell count $312$ are \grade{F2/I1} in the record and were recomputed here in integer arithmetic, and the Gram identity is exact arithmetic on the plotted sets. "
 r"Free energies against $F_{D_4}$: $-5.6\times10^{-13}$ for (b) and $+6.7\times10^{-11}$ for (c), both at $N=24$, where aliasing of the cubic term breaks the degeneracy at this level; $-2.2\times10^{-16}$ for (a) at $N=32$, where the degeneracy is \grade{F2/I1}. "
 r"The selection fraction $29/30$ of Section~\ref{sec:gd3} \grade{F2/I1} is not plotted here.")

CAP7 = (r"The full-field critical droplet (run 13, gap G-A10) at $r=-0.35$, $\bar\psi=-0.18$, $q_0^2=8$, $u=v=1$, conserved dynamics. "
 r"(a)--(c) The stationary point in the box $L=32\pi$ ($6/\pi$ points per unit length, $97^4$ parity-reduced grid, $dx=\pi/6$). The stored field is even about every coordinate plane through the centre, so the mirror unfolding used here is exact. "
 r"(a) $\varphi=\psi-\bar\psi$ on the plane $x_3=x_4=0$, diverging scale centred at $0$; the dashed circle has radius $R_{\rm eq,\infty}=10.465$. "
 r"(b) Isosurface $\varphi=0.5$ on the hyperslice $x_4=0$, coloured by distance from the centre, with the quarter $x_1>0$, $x_2<0$ removed; the droplet is a crystallite of density maxima, not a smooth bubble. "
 r"(c) Raw grid values along the axis $(1,0,0,0)$ and the diagonal $(1,1,1,1)/2$. "
 r"(d) Barrier $\Delta F^*(L)$ for the $11$ boxes $L=12\pi,\dots,32\pi$ (residuals below $4\times10^{-11}$), with the extrapolation $\Delta F^*_\infty=119.06\pm0.03$ (band). The envelope-model saddle $550.93$ is a saddle of the radially restricted model only and lies far off scale. "
 r"(e) Equivalent radius $R_{\rm eq}(L)$, tending to $\approx10.465$. "
 r"Values \grade{F2/I1}; Hessian index $1$ certified only at $12\pi$ and $16\pi$; the rate is open.")

CAP8 = (r"Hessian spectrum of the relaxed $D_4$ state on the doubled box $L=2\pi$ at $(r,\bar\psi)=(-0.35,-0.18)$ (run 13, point 1 of three, $N=16^4$). "
 r"(a) The lowest $12$ eigenvalues in each of the $32$ symmetry cosets, sorted by $|a|$, where $a\in\{0,1\}^4$ is the parity class of the wavevector; odd cosets are the subharmonic sector that the $L=\pi$ cell cannot represent. Values above $1.9$ are given as numbers. "
 r"The only eigenvalues below zero are the $4$ translation zero modes, $\lambda\approx-1.05\times10^{-7}$ at $N=16$ (at most $3\times10^{-11}$ in magnitude at $N=24$). "
 r"The smallest nonzero eigenvalue is $0.3423000506$, in a cluster of $9$ in coset $0$; the odd sector has no negative eigenvalue and its minimum is $1.0417619866$ ($\times8$, in the cosets with $|a|=3$). "
 r"(b) The gap cluster magnified: at $N=16$ it splits $6+3$ by $8.8\times10^{-8}$; at $N=24$ the split closes to $0.34230009257$ ($\times9$). Only the lowest $12$ eigenvalues per coset were recorded, so (b) shows $8$ of the $9$ cluster members; the multiplicity $9$ is from the full-spectrum summary of the record. "
 r"\grade{F2/I1}; a finite-box statement at three points (this figure shows point 1), not continuum stability over the Brillouin zone.")

# --- Fig. d4cell: Section 3.1, after the design paragraph
rep(r"The normalised roots of $D_4$ form a 5-design, and no set of 24 points on $S^3$ forms a 6-design~\cite{ref5}." "\n",
    r"The normalised roots of $D_4$ form a 5-design, and no set of 24 points on $S^3$ forms a 6-design~\cite{ref5}." "\n\n"
    r"Figure~\ref{fig:d4cell} draws the $24$ roots as the vertices of the $24$-cell. In panel (a) the two rings of $12$ show the $12$-fold symmetry of the Coxeter plane; panel (c) gives the count that the triad term of Section~\ref{sec:selection} uses, eight partners at $120^\circ$ for every root." "\n\n"
    + fig("fig01_d4_24cell.pdf", "fig:d4cell", CAP1))

# --- Fig. 2thopf: Section 11, after the Q8 coset paragraph
rep(r"The $8+8+8$ splitting of the 24-cell is the coset decomposition of a group." "\n",
    r"The $8+8+8$ splitting of the 24-cell is the coset decomposition of a group." "\n\n"
    r"The group also sits on the Hopf fibration of $S^3$. Figure~\ref{fig:2thopf} shows the $24$ elements on Hopf fibres for two axes: on $6$ fibres of $4$ elements for the axis $\mathbf i$, and on $4$ fibres of $6$ for the body diagonal. The reader should note that the fibre size is the order of the cyclic subgroup of $2T$ about the axis, so the picture is a statement about subgroups and carries no physical content." "\n\n"
    + fig("fig02_2T_hopf.pdf", "fig:2thopf", CAP2))

# --- Fig. band: replace the old phase diagram in Section 5.2
rep(r"\lbl{Prediction} Figure~\ref{fig:phase} shows the result of minimising over a frozen set of competitors in the window $\bar\psi\in[-0.6,0.2]$, $r\in[-0.6,0.1]$. The full $24$-mode pattern is the ground state on a contiguous band along the boundary with the disordered phase, spanning roughly $-0.33\lesssim\bar\psi\lesssim0.05$. Lower-symmetry sub-patterns occupy the region of higher tension.",
    r"\lbl{Prediction} Figure~\ref{fig:band} shows the result of minimising over a frozen set of competitors in the window $\bar\psi\in[-0.6,0.2]$, $r\in[-0.6,0.1]$. The full $24$-mode pattern is the ground state on a contiguous band along the boundary with the disordered phase, spanning roughly $-0.33\lesssim\bar\psi\lesssim0.05$. Lower-symmetry sub-patterns occupy the region of higher tension. In panel (a) the reader should look at where the band sits relative to the dashed line $r_{\rm eff}=0$: most of it, including the operating point, lies on the side where the uniform state is linearly stable, so most of the band is reached only across a barrier (Section~\ref{sec:nucleation}). Panel (b) shows that the margin by which $D_4$ wins is a few thousandths at most, largest at deep quench and low $\bar\psi$.")
old_fig = ("\\begin{figure}[htbp]\n\\centering\n\\includegraphics[width=0.8\\linewidth]{figs/fig04.png}\n"
           "\\caption{Phase diagram in the plane of baseline tension $\\bar\\psi$ and quench depth $r$. The full 24-mode $D_4$ state occupies a contiguous band along the boundary with the disordered phase.}\n"
           "\\label{fig:phase}\n\\end{figure}\n")
rep(old_fig, fig("fig04_phase_band.pdf", "fig:band", CAP4))

# --- Content fix (ii): Section 5.3
rep(r"Adding a sextic term $\tfrac{w_6}{6}HA^6$ to the one-mode free energy reduces the one-mode band from $11.60\%$ at $w_6=0$ to $8.36\%$ at $w_6=0.2$.",
    r"Adding a sextic term $\tfrac{w_6}{6}HA^6$ to the one-mode free energy reduces the one-mode band, computed on a $161\times161$ grid of the same window with the competitors hex6, fcc12, sq4 and sq8, from $11.60\%$ at $w_6=0$ to $8.36\%$ at $w_6=0.2$. The value $11.60\%$ is that one-mode $161\times161$ number of Section~\ref{sec:band}; it is not the canonical full-field value $11.5531\%$ of \eqref{eq:band} on the $81\times81$ grid, nor the one-mode value $11.5226\%$ on that grid.")

# --- Fig. hessian: Section 6, after the odd-sector paragraph
anchor8 = r"The sharpest remaining problem for the stability question is a certified, interval-enclosed bound on the Bloch spectrum over the whole Brillouin zone." "\n"
rep(anchor8, anchor8 + "\n"
    r"Figure~\ref{fig:hessian} shows the spectrum at the first of the three points, coset by coset. The thing to look for is that nothing except the four translation modes falls below zero, and that the lowest odd-sector level, at $1.04$, sits well above the even-sector gap at $0.3423$." "\n\n"
    + fig("fig08_hessian_ladder.pdf", "fig:hessian", CAP8))

# --- Fig. droplet: Section 7.2, after the barrier paragraph
anchor7 = r"The earlier expectation that the full-field value would refine the envelope value by one to ten per cent is refuted." "\n"
rep(anchor7, anchor7 + "\n"
    r"Figure~\ref{fig:droplet} shows the droplet. Panels (a)--(c) show that it is a small crystallite of density maxima rather than a smooth bubble, and panels (d) and (e) show the barrier and radius levelling off as the box grows, which is what the extrapolation \eqref{eq:barrier} rests on." "\n\n"
    + fig("fig07_nucleation_saddle.pdf", "fig:droplet", CAP7))

# --- Content fix (i): Section 7.2 thin-wall factors
rep(r"Against the envelope saddle these differ by a factor of about $15$; against the full-field droplet the factors are $119.06/36.95\approx3.2$ and $119.06/138.12\approx0.86$.",
    r"Against the envelope saddle they differ by factors of $550.93/36.95\approx14.9$ and $550.93/138.12\approx4.0$; against the full-field droplet the factors are $119.06/36.95\approx3.2$ and $119.06/138.12\approx0.86$.")
rep(r"The amplitude-equation barrier is about $15$ times the thin-wall value; the full-field barrier is within a factor of about $3.2$.",
    r"The amplitude-equation barrier is about $15$ times the first thin-wall estimate and about $4.0$ times the second; the full-field barrier is about $3.2$ times the first and $0.86$ times the second.")

# --- Figs. d4field and phonons: Section 8, after the relaxed-crystal paragraph
anchor5 = r"its limit as $\mathbf{q}\to0$ is $2.99977$ \grade{F2/I1}. The record number is explained, not wrong." "\n"
rep(anchor5, anchor5 + "\n"
    r"Figure~\ref{fig:d4field} shows the relaxed crystal itself on four three-dimensional slices; what the reader should see is the density maxima at the corners of the cube at $x_4=0$ shrinking as $x_4$ grows while a new maximum appears at the centre, which is how a four-dimensional lattice looks in three-dimensional sections. Harmonics are too small to see: the largest is $3.4\times10^{-4}$, against a mode amplitude of $0.078$. Figure~\ref{fig:phonons} shows its long-wavelength spectrum. In panel (b) every branch, in all six directions, tends to the same limit, which is the isotropy at order $q^2$; panel (c) shows the two separate cones whose ratio is $c_L/c_T=1.731985$." "\n\n"
    + fig("fig03_d4_field_slices.pdf", "fig:d4field", CAP3) + "\n"
    + fig("fig05_phonons.pdf", "fig:phonons", CAP5))

# --- Fig. rotd4: Section 4.4, after the P1/P2 paragraph
anchor6 = r"the fraction above is the record (gap G-D3)." "\n"
rep(anchor6, anchor6 + "\n"
    r"Figure~\ref{fig:rotd4} shows three recorded end states at $P_1$ against the $312$-vector shell. The point to look at is panel (d): the three sets look unrelated in the fixed projection of panels (a)--(c), but their inner products coincide, so each is the $D_4$ root system scaled by $3$ and rotated." "\n\n"
    + fig("fig06_L3pi_shells.pdf", "fig:rotd4", CAP6))

open(p, "w").write(tex)
print("edits applied")
