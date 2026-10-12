# P001-S036 — compatible high-transversal cluster assembly and quantified controls

2026-10-12. SAME-ASSISTANT only; conditional on S033 T2 and S035 fractional-cover lift. TIK, DSE3, R3 remain UNPROVED.

## Theorem C (balanced-cluster high-cover assembly)

Let m>=2, B>=1, Delta>=0, eta in (0,1], and suppose D0 subset D has |D0|>=eta|D|. Partition D0 into nonempty edge-disjoint triple clusters D_i, each tau*(D_i)<=Bm. Let V_i be the COMPLETE original support of D_i, and form conflict graph J on i with ij an edge iff V_i intersects V_j. Assume maximum degree(J)<=Delta AND original cluster masses |D_i|<=|D0|/[m(Delta+1)]. Then a SINGLE internally m-valid H subset D exists with

 |H|>=eta |D|/[8B(Delta+1)m^3].

Proof: greedily properly color J in <=Delta+1 colors. A class I carries original mass W>=|D0|/(Delta+1), and must contain at least m clusters: otherwise the individual mass cap would give W<(m)|D0|/[m(Delta+1)]. Apply S035 one-apex lift separately to every D_i in I. It selects H_i subset D_i with |H_i|>=|D_i|/[8m^2 tau*(D_i)]>=|D_i|/(8Bm^3); exact triple pairs and singleton kernels are inherited from graph T2 in H_i and triple EMPTY is unrealised within one apex output. Different chosen V_i are vertex DISJOINT. Therefore every new cross-cluster intersection is EXACTLY EMPTY, and choosing one member from EACH of any m clusters supplies a true global in-H m-matching. All nonempty kernels remain locally witnessed within their original H_i. Thus H=union H_i is valid, |H|>=W/(8Bm^3)>=eta|D|/[8B(Delta+1)m^3]. QED.

If >=m cluster supports are mutually disjoint then Delta=0 and no balancing cap is needed: use all clusters. More generally for vertex-disjoint supports, union of internally valid nonempty cluster outputs is internally valid iff there is only ONE output or its TOTAL matching number is >=m; if >=2 outputs, EMPTY is realised and its matching number is the sum of matching numbers of the disjoint parts. Bounded interference and the balanced cap are UNPROVED as universal consequences of 6m-spread/core-freeness.

## False gluing shortcut with positive SAME-D repair

Let m>=3 and s=m-1. Take s disjoint L-edge pair-core stars D_i={{a_i,b_i,z_ij}:1<=j<=L}, L>=m. Each D_i is independently internally valid, witnessed at exact pair {a_i,b_i}. Their union realises EMPTY, yet nu(D)=s<m, so is INVALID. One whole star D_1 is internally valid and retains 1/s of the same original D. This example is NOT claimed 6m-spread/core-free and does not satisfy the >=m or balance assumptions.

## Connected high-cover SAME-D control

For m>=3 let s=m-1 and N=1000m^2. Take pairwise disjoint s-vertex parts A_i,B_i,C_i and all s^3 tripartite triples D_i=A_i x B_i x C_i, 1<=i<=N. Choose a_i in A_i, and add bridges {a_i,a_(i+1),z_i}, 1<=i<N, with distinct new z_i. Set D=union D_i plus bridges. |D|=Ns^3+(N-1); maximal singleton degree <=s^2+2, pair degree <=s<m, triple degree 1. For all m>=3, Ns^3>=6m(s^2+2), >=36m^2s and >=216m^3; thus D is 6m-spread. EVERY triple has an original pair of degree <m so robust C(D)=empty. Bridges make the edge-intersection graph CONNECTED. Choosing an s-matching from EACH D_i yields H a true matching of Ns>=m distinct triples, internally m-valid ONLY at EMPTY, with fraction
 Ns/[Ns^3+N-1] > s/(s^3+1) >=1/m^3.
tau*(D)>=nu(D)>=Ns, hence tau*(D)/m unbounded. Removing just N-1 bridges retains >8/9 of original mass as N vertex-disjoint clusters, each tau*=s<=m, so cluster assembly still works. Connectivity is NOT an obstruction; no DSE3 refutation.

As a complementary HIGH-DEGREE control take r=36m^2 disjoint pair-core stars of L>>m^3 triples each. The whole D is 6m-spread (L>=6m), core-free through private leaf pairs, has tau*/m=r/m unbounded and |D|/nu(D)=L>>m^3. Yet H=D is internally valid: PAIR sunflower witnesses L>=m per component, and EMPTY has r matching representatives. Therefore the high-degree-only frontier cannot be declared false or true merely from concentration.
