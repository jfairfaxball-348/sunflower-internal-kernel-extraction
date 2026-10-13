# P001-S045 — unbalanced dense nonlinear core, all-rank extraction and honest universal gap

2026-10-13. FROZEN gate `8e53ba0083fd155df6065f9fdfd44f4ca77ac471` committed BEFORE this proof report; exact owner archive `95239faea3b2f3f1d6772dedcc804b9d2d31e776`, separate hash manifest `8d0803af1b41903dc93ffff89239ffc1f9a34980`. **SAME-ASSISTANT symbolic mathematics, not novelty certified, independently peer reviewed, formalised or published.** No new finite experiment or detailed N1/N2. This is a substantial SCOPE-RESTRICTED original-mass result, NOT a resolution of unrestricted HDSE3/R3/all-k TIK.

## 1. EXACT original target and internally selected semantics

For each fixed rank k>=1 the unchanged TIK statement seeks some c_k>0 independent of m,n,F with H subset F, |H|>=c_k|F|/m^k for EVERY m>=2 and k-uniform original F, and with every realised exact K=A∩B (distinct A,B in FINAL H, including K=EMPTY) witnessed by m distinct whole edges **IN H** whose pairwise intersections equal exactly K. The witnessing m petals need not include A or B. The theorem below imposes strong original density and bounded pair multiplicity: a quantified SUBCLASS result, not any full-k induction.

## 2. New exact linear-core dichotomy with NO degree balance

**LEMMA S045-A (linear positive m-core dichotomy, every k>=2).** Let C be a finite LINEAR k-uniform family, m>=2, such that every nonisolated vertex has C-degree >=m. If C is nonempty, some internally m-valid H subset C has

    |H| >= |C|/[k(m-1)].                                      (A)

**Proof.** If C has a whole-edge matching M of cardinality >=m, retain H=C. The only possible intersections of distinct H edges are singleton vertices and EMPTY, since C is LINEAR. Every realised singleton x has d_C(x)>=m and ANY m C-edges through x pairwise meet EXACTLY in {x}; if EMPTY occurs, M supplies m disjoint whole H-edges. No pair or higher kernel can occur. Thus C itself is internally valid.

Otherwise choose a MAXIMAL whole-edge matching M with |M|<=m-1 (maximum <m entails any maximal matching <m). Every C-edge meets V(M), whose size is k|M|<=k(m-1). Therefore |C|<=sum_{x in V(M)}d_C(x), and some x in V(M) has d_C(x)>=|C|/[k(m-1)]. Since x is nonisolated, also d_C(x)>=m. Retain H=ALL C-edges containing x. By ORIGINAL LINEARITY of C, every two selected H-edges have exact intersection {x}; any m retained edges witness {x} pairwise exactly. EMPTY, pairs and larger kernels do NOT occur. Thus H is internally valid and satisfies (A), including the case where the only possible witness type is singleton. No degree-balance, maximum-degree or spreadness is used. QED.

**THEOREM S045-B (all-rank dense bounded-pair-codegree extraction, ORIGINAL mass).** Fix k>=2,m>=2. Let F be a nonempty simple k-uniform family, e=|F|, n=number of nonisolated ORIGINAL vertices, B=max original PAIR codegree >=1, and

    Q=1+binom(k,2)(B-1).

There is H subset F, internally m-valid, with

    |H| >= max{1, [e/Q-(m-1)n]/[k(m-1)]}                    (B1)

(the second real bound may be negative). In particular, whenever

    e >= 2Q(m-1)n,                                         (B2)

there is such H with

    |H| >= e/[2kQ(m-1)].                                   (B3)

If ORIGINAL B<=m-1, then Q<=binom(k,2)m and (B2) implies

    |H| >= e/[k^2(k-1)m^2].                                (B4)

For triples, with the exact Q=3B-2,

    e >= 2(3B-2)(m-1)n   ==>  |H|>=e/[6(3B-2)(m-1)].
    B<=m-1               ==>  |H|>=e/(18m^2).              (B5)

**Proof.** Construct the conflict graph on distinct ORIGINAL F-edges: e_1~e_2 iff |e_1∩e_2|>=2. Every original edge contains binom(k,2) pairs; each pair appears in <=B-1 OTHER edges, so graph maximum degree <=binom(k,2)(B-1). Its greedy proper colouring into <=Q classes yields some class L subset ORIGINAL F, LINEAR, with |L|>=e/Q. On this selected L repeatedly peel a CURRENT vertex of degree 1,...,m-1, deleting all its CURRENT incident edges; the peeled edge set has cardinality <=(m-1)n because each original vertex is peeled at most once. The terminal selected C subset L is LINEAR and has min positive C-degree >=m, with

    |C|>=|L|-(m-1)n>=e/Q-(m-1)n.                            (B6)

If C is nonempty apply Lemma A. If C is empty or (B6) nonpositive, choose any single ORIGINAL F-edge; as a singleton final H, it realises NO intersection kernels and is vacuously internally m-valid. This establishes (B1) including the 1-edge fallback. Under (B2), e/Q-(m-1)n>=e/(2Q)>0, so C nonempty and (B3) follows. Under B<=m-1, Q<=binom(k,2)m and m-1<=m, giving (B4). For k=3 substitute Q=3B-2 and Q<=3m to obtain (B5). At EVERY selection stage only ORIGINAL whole F-edges are retained. The final-H PAIR/higher kernels are ABSENT because H subset C subset L is LINEAR. EMPTY is witnessed by an m-matching INSIDE H when H=C, otherwise EMPTY is ABSENT from the singleton-star H. A realised singleton is witnessed by m H-star edges, either in the C core or in H itself. There is no reliance on witnesses outside H. QED.

**Comparison to S044-B.** S044-B required (for B<m) e>=2(3m-2)mn AND Delta(F)<=A e/n (fixed A) to achieve e/(36A m^3). S045-B uses the WEAKER density threshold e>=2(3B-2)(m-1)n, imposes NO maximum-degree balance, works at every k>=2 even if B>=m, and in B<m triples gives >=e/(18m^2). Thus the S044-B case is subsumed quantitatively. This is not a proof that the original unrestricted low-density case can be treated identically.

## 3. A genuinely nonlinear HIGHLY UNBALANCED 6m-spread HDSE3 SAME-F control

Fix EACH integer m>=3. Put t=10m^3, N=m^5 and r=m-1. Let X,Y,Z be disjoint copies of Z/tZ and take the original CYCLIC bulk

    F_bulk={ {x_X,y_Y,z_Z}: z=x+y+s mod t, s=0,...,m-2 }.

Let U be a disjoint N-point vertex set, add an additional hub h, and let G be ANY simple r-regular graph on U. This exists for all m>=3: if r is even take the circulant neighbours +/-1,...,+/-r/2 modulo N; if r is odd, N is even and one may add the antipodal neighbour N/2 to neighbours +/-1,...,+/-(r-1)/2. Take

    F_hub={ {h,u,v}: uv in E(G) },  F=F_bulk disjoint-union F_hub.

This is a parametric algebraic construction, NOT a new numerical experiment or a random search. Exact census:

    e=|F|=(m-1)[100m^6+m^5/2],
    n=3t+N+1=30m^3+m^5+1,
    B=max_PAIR_degree=m-1.
    degrees_bulk=10m^3(m-1) on X,Y,Z;
    d_F(h)=m^5(m-1)/2;  d_F(u)=m-1 on U.

For m>=3, n<=5m^5 and e>=100(m-1)m^6 >= 2(3m-5)(m-1)n (indeed RHS <=30(m-1)m^6 <= e). Hence S045-B applies with Q=3m-5, providing a **FINAL internally m-valid H subset THE SAME F** of size

    |H| >= e/[6(3m-5)(m-1)] >= e/(18m^2).               (C1)

This F is GENUINELY NONLINEAR: two original bulk edges with fixed (x,y) but distinct s meet in PAIR {x,y}; only m-1 original edges contain this pair. Thus the ENTIRE original F is NOT internally valid: no m-petal in-F pair certificate exists for this realised pair. The same pair defect also occurs in the hub component via {h,u} with degree r=m-1. Yet the theorem's selected H avoids all pair intersections by linearisation and obtains genuine in-H EMPTY/singleton certificates.

It also satisfies HDSE3's exact HYPOTHESES:
- 6m-spread: max vertex d_F(x)<= e/(6m) (specifically d_F(h)<=e/(200m) and independently 10m^3(m-1)<=e/(6m) for every bulk vertex; the stronger 200m bound is NOT asserted for bulk vertices); max PAIR degree m-1<=e/(36m^2); 1<=e/(216m^3) for each present triple.
- Robust core FREE: every original F triple contains a pair of original degree at most m-1, so no nonempty original subfamily can have m disjoint residual petals at all contained PAIR links.
- EACH original bulk edge contains vertices of ORIGINAL degree 10m^3(m-1)>m^3; EACH hub triple contains h with degree m^5(m-1)/2>m^3.
- GLOBALLY UNBALANCED: Delta(F) n/e >= [m^5(m-1)/2]*m^5/[(m-1)101m^6]=m^4/202 ->infinity. Thus NO fixed A bounds Delta(F)<=A e/n on this same-E sequence, and S044-B cannot be invoked with an absolute A. The theorem closes this fresh highly unbalanced population quantitatively with the correct same-original-family mass.

For m=2, H=F for ANY input because any realised pair already supplies its own two-edge 2-sunflower; the displayed control is purposely m>=3.

## 4. Universality attempts, honest obstruction

This DOES NOT close arbitrary HDSE3. The newly sufficient density hypothesis e>=2Q(m-1)n is NOT forced by 6m-spread, core-free or each-edge-touches-degree>m^3. At B about m, it requires e/n of order m^2, while HDSE3 permits original vertex m-cores with average original degree only of order m to m^2 and arbitrarily uneven degree distribution. Without the density hypothesis the simple conflict-colour selection L may have all or almost all its e/Q edges removed by low-current-degree peeling; the inequality (B6) may be negative. The first missing step is therefore an ORIGINAL-mass `m^{-3}` extraction on this SPARSE NONLINEAR VERTEX m-CORE, with simultaneous SATURATED PAIR-class / sparse-pair coexistence, not a further balance improvement on the already-solved dense core.

S043's peeled-apex route does save one factor m when many ORIGINAL edges themselves peel at vertex degree <m, but the dense surviving ORIGINAL core may have pairdegree 2,...,m-1 and many edges without an assignment of apex load O(m). Applying S043 to the peeled fraction of the LINEARISED class spends Q=Theta(m) before S043's m^-3 factor, returning e/m^4 rather than desired e/m^3. No unproved factor is suppressed.

S036's verified-as-SAME-ASSISTANT reduction HDSE3=>R3 relies on full 6m-spread/corefree/high-degree cases; S045 only handles a dense part. The all-k formula (B4) is a direct dense-class theorem **not** an unrestricted induction and cannot imply original full every-fixed-k TIK from k=3. S023/S024 projective-plane whole-BSEL obstructions, S029–S032 row/collision failures, S034 twins, S035 high fractional cover, S037–S041 palette/atlas/island examples remain failures of specified sufficient mechanisms unless their SAME-ORIGINAL maxvalid ratio truly tends to zero. In particular S042 affine Steiner is LINEAR AND internally m-valid; S043 private-base K_(m-1,m-1) obstruction has an internally valid singleton rescue; S044 m-1 disconnected saturated pair-stars have a valid full single-component 1/(m-1) rescue. No HDSE3 or full R3 counterexample is claimed. No new detailed N1/N2, Lean, manuscript, independent mathematics referee or external act.

**STRONGEST PROVED-SYMBOLIC S045 ADVANCE:** arbitrary max-vertex-degree unbalanced, rank-k ORIGINAL-mass dense pair-codegree theorem (B1–B4), quantitatively stronger than S044-B, with a genuinely 6m-spread/core-free/nonlinear/degree-unbalanced SAME-original rank-three control (C1).

**FIRST STILL-UNPROVED UNIVERSAL IMPLICATION:** replace the dense original e>=Theta_k(Bmn) hypothesis by a universal lower-bound mechanism that either certifies ORIGINAL low-density, high-hub nonlinear core mass at |E|/m^3 with exact PAIR, singleton and EMPTY petals all IN final H, or isolates a genuine SAME-E adverse sequence with m^3 maxvalid_m(E)/|E| tending to zero. Neither is established here. P001-S046 must be prepared FUTURE ONLY and NOT executed.
