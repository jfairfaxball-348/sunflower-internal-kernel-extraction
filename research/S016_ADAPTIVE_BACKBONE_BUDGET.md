# P001-S016 — quantitative fixed-backbone weighted deletion fails; dense adaptive control

**One bounded proof-first child gate, 2026-10-11.** The immutable paper target is TIK for EACH fixed k>=1, retaining c_k*m^(-k) of any k-uniform family with every exact pair intersection, including empty, witnessed by m distinct petals IN THE RETAINED FAMILY. Rank-three R3, arbitrary whole-block BSEL, and the private-light <=2-original-heavy-support case remain stepping stones and are **not proved or refuted** here. This is a same-assistant symbolic mathematical check, not independent proof review, source verification, novelty or publication.

## Exact unrestricted slice and the proposed joint budget

Fix every integer m>=3 and any finite pairwise edge-disjoint family B_1,...,B_t of COMPLETE m-petal triple sunflower blocks with kernel sizes 0/1/2. Original support loads determine Q={v: #{i:v in V_i}>m}. Every block meets Q in <=2 vertices and each vertex outside Q is block-private. Q can be arbitrarily large, overlapping and unbounded in load. No hub-disjointness or homogeneous kernel-type hypothesis is imposed on the QUANTIFIED statement. A selection always retains WHOLE original blocks.

As in S012, A_e denotes the class of blocks containing at least one triple containing both endpoints of the original-Q heavy pair e; classes A_e are disjoint, and A0 consists of pair-inactive blocks. Let p_e(J) be the number of selected genuine e-core blocks and a_e(J) be the number of selected noncore e-active blocks. Because every noncore active block contributes exactly one e-containing triple and different blocks are edge-disjoint, the **actual** final codegree is

    d_H(e) = m*p_e(J) + a_e(J).

Thus a heavy pair cannot be realised with d_H(e) in {2,...,m-1}. S012 PAIR_FILTER retains all A0, all A_e with e-core blocks, and all A_e with |A_e|>=m; it compresses a class with no e-core and size 1<=s<=m-1 to exactly ONE block. Call its output J0. Class weights give the rigorous, globally summed inequality

    |J0| = |A0| + sum_e (|A_e| for uncompressed classes, 1 for compressed classes)
         >= |A0| + sum_e |A_e|/(m-1) >= t/(m-1).

This is PAIR-ONLY, not simultaneous certification. The heavy-singleton condition is the **actual** S011 residual matching: if {v} is realised, either a selected original singleton-core {v} block certifies it or nu(G_v)=f_v(J)+|D_v(J)|>=m, where free block residuals must account for optional other-heavy endpoints. The empty condition is either unrealised, protected by a selected complete original empty-core block, or certified by >=m disjoint mandatory original-Q core footprints C_i=K_i intersect Q. A selected block's load never substitutes for either matching.

Consider a natural **single joint pair/channel/core budget candidate**. After the pair filter, choose a feasible m-block *mandatory-core matching backbone* M subset J0 consisting of blocks with nonempty original cores and pairwise disjoint footprints C_i. The attempted weighted repair would keep M and delete any other whole blocks or entire heavy-pair classes to protect residual singleton channels, while keeping the final heavy-pair codegrees safe and preserving the backbone's genuine empty certificate. Its first quantified required implication is frozen as:

**FIXED_BACKBONE_BUDGET(C):** There is an absolute finite C>0 such that for ALL m>=3, ALL such packings, ALL S012 J0, and EVERY specified M subset J0 of size m with pairwise disjoint mandatory heavy-core footprints (and nonempty cores), there exists J with M subset J subset J0 satisfying ALL three final S011 exact tests simultaneously and

    |J| >= |J0|/(C*m^2).

The factor m^2 after the pair-only loss <=m-1 would yield |J|>=t/(C*m^2*(m-1))>=t/(C*m^3), so this is a GENUINELY QUANTITATIVE sufficient bridge if proved. It explicitly allows deleting entire previously saturated A_e classes. It is considerably stronger than optimising the backbone jointly with the weights. **The implication is FALSE for every finite C**, already with a selected genuine empty-core block and all 0/1/2 original kernel sizes present. It is not a claim about an optimally chosen M.

## Parametric fully symbolic construction

Fix arbitrary m>=3 and arbitrary N>=m+1, to be allowed to tend to infinity at FIXED m. Take 2m heavy symbols a_1,...,a_m and b_1,...,b_m. All unspecified vertices in the following complete blocks are mutually distinct light vertices used in precisely ONE original block; within a block the common core symbols are repeated as dictated by its sunflower.

1. For each i=1,...,m and j=1,...,N, introduce an exact pair-core block P_(i,j) with kernel {a_i,b_i} and triples {a_i,b_i,x_(i,j,r)}, r=1,...,m. There are mN of these **large-weight classes**.
2. For each i introduce one exact pair-core *anchor* L_i with kernel {a_i,u_i}, where u_i is light: triples {a_i,u_i,y_(i,r)}, r=1,...,m. There are m anchors. Their mandatory original-Q footprints are C(L_i)={a_i}; these form a true m-block disjoint-core matching M={L_1,...,L_m}.
3. For i=1,...,m-1 introduce a complete pair-core *bridge* R_i with core {b_i,b_(i+1)}, triples {b_i,b_(i+1),z_(i,r)}. There are m-1 bridges, linking the originally heavy support graph across ALL m gadgets; it is not confined to isolated hub components.
4. Introduce TWO complete empty-core blocks X_1,X_2. Each has exactly one triple {b_m,b_1,w_s}, and its other m-1 triples consist of three fresh private light vertices, disjoint across its own petals. Its only original-Q support is {b_m,b_1}. The pair-active class e*={b_m,b_1} thus has exactly TWO noncore active blocks and NO e*-core block. This class is genuinely short and unsaturated for every m>=3.
5. Introduce an all-light complete singleton-core block T with private core {c} and m triples {c,d_r,e_r}; introduce an all-light complete empty-core block E with m mutually disjoint private triples. They ensure ORIGINAL block kernel sizes 0,1,2 are all present. E can give an actual empty witness independently of M.

All displayed triples are distinct; the blocks are pairwise edge-disjoint and complete m-petal sunflowers of their claimed exact core types. Each support meets Q in <=2 hubs and every nonhub belongs to one block. Indeed r(a_i)=N+1>m, r(b_i)=N+2>m for 2<=i<=m-1, and r(b_1)=r(b_m)=N+3>m. Thus Q is EXACTLY {a_i,b_i:1<=i<=m}. The original hub interaction graph is connected by the b-bridges; loads are unbounded as N grows.

The exact counts and PAIR_FILTER accounting are

    t = mN + m + (m-1) + 2 + 2 = mN+2m+3,
    A0 = {L_1,...,L_m,T,E}, |A0|=m+2,
    |A_{ {a_i,b_i} }|=N  (all e-core),
    |A_{ {b_i,b_(i+1)} }|=1  (one e-core, i<m),
    |A_{e*}|=2  (NO e*-core).

Every pair-active class except e* stays completely, and e* is compressed from TWO noncore blocks to ONE. The resulting S012 J0 has

    |J0| = |A0| + mN + (m-1) + 1 = mN+2m+2 = t-1.

Its true e-codegrees are mN at {a_i,b_i}, m at each bridge pair, and 1 at e*. Consequently no realised heavy pair has codegree 2,...,m-1. Notice the A0 mass m+2 was fully retained; none has been silently discarded. Both M and E survive the filter, so J0 has BOTH a genuine m-disjoint mandatory-core-footprint matching and an entire original empty-core m-sunflower. The empty test is strongly protected already: the first failure of the frozen implication is NOT absence of empty matching.

## Actual residual-link obstruction and unbounded weighted deletion

For ANY proposed J with M subset J subset J0, suppose that one large pair-core block P_(i,j) survives. Then the selected L_i has triples {a_i,u_i,y}, while P_(i,j) has triples {a_i,b_i,x}; one such pair of triples intersects in EXACTLY {a_i}. Thus {a_i} is realised. There is no original singleton-core {a_i} block anywhere in this construction. The only selected blocks containing a_i are its mandatory L_i and zero or more P_(i,j); the b-bridges and X,T,E do not contain a_i. In the actual link graph G_{a_i}(J), all residual pairs from L_i share the light vertex u_i and all residual pairs from P_(i,j) share the heavy vertex b_i, with other vertices private. Therefore

    f_{a_i}(J)=1,    D_{a_i}(J)={b_i},
    nu(G_{a_i}(J))=1+1=2<m.

This is the exact S011 matching, not the selected block degree N+1 or a local certificate. Optional hub endpoints in X are irrelevant because X has no a_i. The singleton fails even if E is selected and gives an actual empty m-matching. Hence NO P_(i,j) may survive in ANY fully valid selection containing M. Every one of the m genuinely saturated heavy-pair classes must be deleted ENTIRELY. As J is restricted to J0, at most the m anchors, m-1 bridges, one X, and T,E can survive, giving the rigorous upper bound

    max_{valid J subset J0, M subset J} |J| <= 2m+2.

Since |J0|=mN+2m+2, for every fixed m>=3 and any finite C one may take N so large that (2m+2)<|J0|/(C*m^2). Hence **FIXED_BACKBONE_BUDGET(C) is false for every finite C**, and the loss in a repair that locks this M is at least |J0|-(2m+2)=mN, although the initially protected matching contains only m anchor blocks. This is a failure of quantitative **weighted** charging: one mandatory light-core/free-channel anchor at a_i incurs the cost N of a whole e-core class; no O(m^2) multiplicative fallback can pay for all m locked anchors. The example does NOT force retaining any original heavy pair class, and small unsaturated-class compression was carried out correctly.

## A fully valid, density-positive whole-block alternative

Drop ALL L_i anchors and all bridges and X blocks. Select instead EVERY P_(i,j), together with T and E. Call the whole-block selection J_good. Its size is

    |J_good|=mN+2 >= (mN+2m+3)/2 = t/2
    for every N>=m+1.

All heavy pairs {a_i,b_i} realised in H_good have true codegree mN, and light-containing exact pairs are certified by original selected complete blocks. No heavy singleton {a_i} or {b_i} is realised: every selected triple containing either hub contains BOTH a_i and b_i, so two such triples never intersect only at one of them. The singleton core of T is witnessed by its own m petals. Empty is realised by triples in different i-gadgets and certified by E's m disjoint triples; independently, the mandatory footprints {a_i,b_i}, i=1,...,m, are pairwise disjoint, so choosing one private petal from each gives a genuine selected m-matching. Thus ALL FINAL S011 tests pass simultaneously in H_good, including exact empty.

For fixed m and N->infinity, the anchored maximum normalised ratio is at most (2m+2)*m^3/(mN+2m+3)->0, BUT the *unconstrained* valid maximum is at least |J_good|>=t/2, so max_valid |J|*m^3/t>=m^3/2. **This is not a refutation of any absolute gamma, private-light BSEL, universal BSEL, R3 or TIK.** It is solely a sharp logical warning that the compulsory footprint matching cannot be preselected independently of high-weight pair classes and singleton-channel dependencies.

## What was and was not proved

The one proof attempt tried to combine S012's exact weighted class accounting, an m-footprint empty matching, and a single later controlled singleton-channel deletion step. The first quantified bridge demanded retention of an arbitrary already-feasible matching M with a further <=C*m^2 density loss. The parametric construction disproves THIS budget: locking a low-weight core matching destroys almost all potentially retainable blocks, even though a different core matching inside the high-weight e-core classes yields almost all mass. The correct future obligation must **optimise or avoid the backbone jointly with the pair-class weights and true channels**, not sequentially lock it, and must handle arbitrary original Q (including empty-core controls) without class-preservation restrictions.

At t=0 the empty selection works. For 1<=t<=3m^3 one complete original block retains 1>=t/(3m^3) and is internally valid. At m=2 the original full TIK has H=F. These boundaries are unaffected. S006 vertex-disjoint and S007 low-load positives; S008/S009 entire-union valid controls; S010/S011 >=half-density controls and exact certificates; S012 pair-only >=t/(m-1); S013 A0-protected conditional gamma; S014 exact >half mixed-cycle; S015 >=t/(m-1) star with its fifteenth audit remain intact. No five-session audit is due at S016 (the next is S020), and no new detailed N1/N2 is performed under the owner's proof-first policy. No full all-k TIK proof candidate, independent maths review, original theorem, Lean, manuscript, programme mathematical S001, outreach or publication. S017 prepared as a FUTURE separate fresh invocation only.
