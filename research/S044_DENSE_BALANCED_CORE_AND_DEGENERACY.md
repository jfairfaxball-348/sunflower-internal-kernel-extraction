# P001-S044 — dense nonlinear m-core rescue and bounded-degeneracy original-mass extraction

Date 2026-10-13. The third separately committed FROZEN gate is `10f184054d8e39845968073798a77aaf64919874`, after separately archived exact owner instruction `d8d6927472ef98238b9c4b06fc7b4b966a28cbbc` and SHA256 manifest `3ec8a9dbdc8998b92d67f8c784d761e3e3dc33c5`. This is an original-mass **scoped SAME-ASSISTANT symbolic analysis**, neither independent review nor originality certification. No computation or new detailed N1/N2. Full every-fixed-k TIK, R3 and HDSE3 remain **UNPROVED**.

## 0. Exact semantics and prior frontier

For every exact pair intersection K of two distinct edges of the FINAL H, including EMPTY, require m different edges IN H pairwise intersecting exactly K. In triples this requires saturated PAIR degree >=m for each realised pair, m-matching in each realised singleton link, and m-edge whole-family matching if EMPTY is realised. For an ORIGINAL triple family with all pair degrees <m, every m-valid H with >=2 edges must itself be LINEAR; one may not declare a nonlinear m-core valid. S043 treats original low-apex-outdegree peeled mass; dense ORIGINAL vertex m-cores can instead dominate.

S033 establishes the SAME-ASSISTANT rank-two exact bound c_2=1/8, which is a dependency of Theorem A. Theorem B below does NOT depend on S033 and checks every witness directly.

## 1. A bounded original apex-degeneracy theorem (nonlinear triples)

**THEOREM S044-A.** Let m>=3 and let F be any finite ORIGINAL 3-uniform family with |F|=e and EVERY original pair codegree <=m-1. Suppose there exists an apex assignment a(T) in T for each T in F such that each ground vertex is assigned at most d edges, d<=A m, for some fixed real A>=1. Then an internally m-valid H subset F exists satisfying

    |H| >= e/[54(A+1)m^3].                                  (A1)

In particular this applies with NO restriction on original maximum vertex degree when an iterative minimum-positive-current-degree vertex deletion removes all edges at threshold floor(A m), i.e., when the ORIGINAL hypergraph has bounded vertex degeneracy in that precise peeling sense. It also applies when max original vertex degree <=A m, without peeling. It covers original vertex m-cores of degeneracy between m and A m.

**Proof.** Direct each T to its assigned a(T). Independently make vertices RED with probability 1/3, BLUE otherwise. An edge is good if its assigned apex is RED and its other two vertices BLUE. Expectation gives a colouring with g>=4e/27 good edges. Create a bipartite graph Q with RED apices on the left, unordered BLUE base pairs on the right, and one incidence for each good original T. Left maximum degree <=d<=Am; right maximum degree <=m-1 by the ORIGINAL pair-codegree hypothesis; Q is simple. A greedy maximal matching deletes at most d+(m-1)-1<= (A+1)m incidences per matched incidence, hence |M|>=g/[(A+1)m].

Distinct matched triples have PRIVATE red apices and distinct blue bases; blue bases may share blue vertices. Identifying M's distinct bases with edges of a simple graph G, the S033 exact graph theorem gives an internally m-valid graph J subset G of size at least |G|/(8m^2). Lift each graph edge g to g union its distinct private RED apex. For each two lifted edges the intersection is EXACTLY their BLUE-base intersection; this equality applies also to every pair among any m graph sunflower witnesses. So realised singleton/EMPTY kernels in final H have m whole lifted H-witnesses and no PAIR kernel can occur. Thus |H|>= (4/27)e/[8(A+1)m^3]=e/[54(A+1)m^3]. The empty family is trivial. For m=2 take H=F without assumptions. QED.

**Limitation:** when degeneracy d/m is unbounded, (A1)'s coefficient goes to zero. Applying this to an arbitrary high-degree original core with d≫m does NOT establish R3.

## 2. Dense balanced nonlinear vertex-core theorem

Put n=the number of nonisolated ORIGINAL vertices of nonempty F, e=|F|, m>=3, and Q=3m-2.

**THEOREM S044-B.** Assume

    (i) all ORIGINAL pair-codegrees <=m-1;
    (ii) e >= 2 Q m n;
    (iii) ORIGINAL maximum vertex degree Delta(F) <= A e/n, for some A>=3.

Then there exists internally m-valid H subset F with

    |H| >= e/[4 A Q^2 m] >= e/[36 A m^3].                   (B1)

The bound uses the WHOLE ORIGINAL e; no assumption that F is originally linear, 6m-spread, vertex-m-degenerate, a product, or a union of disjoint supports. The final H is linear. For fixed A this closes the exact m^-3 exponent on this quantitatively dense BALANCED nonlinear core stratum.

**Proof.** Form the conflict graph on ORIGINAL triple edges: join two edges when they share >=2 vertices. For an edge T each of its three pairs lies in at most m-2 other triples, so the conflict degree <=3(m-2), and greedy proper colouring uses at most 3m-5 <= Q classes. Use Q=3m-2 as a conservative bound. A largest independent class L is a LINEAR triple family with |L|>=e/Q. Peel vertices of *CURRENT* degree 1,...,m-1 from L and delete their incident edges. Each vertex is peeled at most once and deletes <=m-1 edges, so D=L minus C satisfies |D|<mn. Hypothesis (ii) implies

    |C| >= e/Q-mn >= e/(2Q).                               (B2)

C is still LINEAR and has min positive vertex degree >=m. Split on n.

**(a) n < 6 A Q m.** Counting 3|C| incidences over at most n original vertices, some x has deg_C(x)>=3|C|/n > [3e/(2Q)]/[6A Q m]=e/(4A Q^2 m). Since x is nonisolated in C, deg_C(x)>=m. Retain H=all C-edges through x. By LINEARITY any two distinct selected triples meet exactly {x}; any m selected edges witness {x} IN H. EMPTY and PAIR are not realised. Hence H is valid and obeys (B1).

**(b) n >= 6 A Q m.** For a maximal matching M in C, all C edges meet the at most 3|M| covered vertices. Thus |C|<=3|M|Delta(F)<=3|M|A e/n. By (B2),

    |M| >= |C|/(3Delta(F)) >= n/(6 A Q) >= m.                (B3)

Retain H=C. Its realised intersections are exactly EMPTY or singleton vertices. Every realised singleton {x} has C-degree >=m, and all C-edges through x are pairwise exactly singleton-intersecting because C is linear. For EMPTY, the m disjoint edges of M are witnesses IN H. No PAIR is realised. Consequently C is internally m-valid and |H|>=e/(2Q)>=e/(4A Q^2 m) (since A>=3, Q>=1, m>=3). Finally Q<=3m gives e/(4 A Q^2 m)>=e/(36 A m^3). QED.

**GENUINELY NONLINEAR positive control on SAME ORIGINAL F (no enumeration).** Let t be an integer >=ceil(6Qm/(m-1)), let X,Y,Z be disjoint copies of Z/tZ, and fix S={0,1,...,m-2} subset Z/tZ. Define

    F(t,m)={ {x_X,y_Y,z_Z} : z=x+y+s mod t, x,y in Z/tZ, s in S }.

Distinct s give distinct triples, so e=t^2(m-1); n=3t; every ORIGINAL vertex has degree t(m-1)=3e/n; every cross-part pair has codegree m-1; no same-part pair lies in an edge. Thus (i) holds and A=3, while e/n=t(m-1)/3>=2Qm by choice of t. For m>=3, F itself is NOT internally valid: two triples with the same (x,y) have pair intersection {x,y}, but there are only m-1 ORIGINAL triples through that pair, so even F has no m-petal certificate there. Nevertheless S044-B proves H subset SAME F with |H|>=e/(108m^3) and exact all-level final-H witnesses. The construction has an ORIGINAL vertex m-core containing all edges; S043's peeling set D=empty, so this is genuinely outside the S043 peeled-majority theorem. It need not satisfy 6m spread at the chosen minimal t; no HDSE3 implication is claimed from that example.

## 3. Saturated pair coexistence: exact first failed assembly step

Take m>=3, N>=m, and r=m-1 disjoint vertex-support components indexed i=1,...,r. Component i consists of all N triples {u_i,v_i,z_(i,j)}, j=1,...,N, with entirely distinct supporting vertices across i. Each E_i is itself internally m-valid (only realised pair kernel {u_i,v_i}, with N whole petals). The full union has realised EMPTY from cross-component edges, but maximum whole-edge matching is r=m-1, hence **the union is NOT internally m-valid**. Thus the tempting implication “all saturated pair classes individually valid => their union valid” is FALSE, even with pair classes supported on disjoint vertex sets. A SAME-ORIGINAL positive rescue retains a largest full component, a 1/(m-1) fraction of E; this is much better than the target m^-3. With >=m components the whole union is valid. This method-negative does NOT disprove HDSE3/R3/TIK. In particular no invented sequence with m^3 maxvalid_m(E)/|E| ->0 is asserted.

For mixed B<m and B>=m pair channels one can select just one channel, but without a quantitative ORIGINAL mass theorem for its final internally valid extraction, a global original mass m^-3 does NOT follow. Naive union additionally introduces new singleton/EMPTY/pair exact kernels; each must be rechecked in the FINAL H. The first missing coexistence implication is a quantitatively guaranteed partition into internally compatible saturated-pair and sparse-pair strata retaining a constant original-mass fraction after certification.

## 4. Global HDSE3, rank induction and hostile boundary

- S044-A covers a bounded-degeneracy ORIGINAL m-core; S044-B covers high-density balanced ORIGINAL vertex m-core with pair degrees below m. Neither covers all large nonlinear core when degeneracy d≫m, density e/(mn)≪m, degree balance Delta/(e/n)≫1, or saturated original pair codegrees >=m.
- S036 remains a correct conditional HDSE3=>R3 reduction based on S033. **No universal HDSE3 H was proved.** In particular neither density nor degree balance in S044-B is entailed by the general 6m-spread, core-free, >m^3-degree-on-each-edge hypotheses.
- The rank-k conditional private-apex lift of S043 needs bounded original (k-1)-fibre and apex load. The S044-B **linearisation** consumes up to O(m) in rank3 but the star/linear-core rescue recovers it only using degree balance/density; it is NOT a free rank-k induction for all k.
- m=2: take H=F at any rank; this is not evidence of m>=3 universal behaviour.
- S042 affine Steiner F_3^d is already fully valid and linear, so it is NOT a counterexample; on the dense branch S044-B also works whenever size and balance assumptions hold.
- S043 apex-base K_(m-1,m-1) is too sparse for B and lies in the low-degree orientation A branch; its TRUE same-E maxvalid=1 does not attack m^-3.
- The S023/S024 projective incidence and S029-S032 shared/row constructions remain METHOD obstructions with SAME-F rescues as previously recorded. No assertion that they satisfy B's high density and balance simultaneously is made.
- S034 twins, S035 fractional covers, S037-S039 partial palettes/tensors, S040 star forests and S041 islands also do not supply a same-E HDSE3-negative sequence. Their separate exact repairs and precise past assumptions are preserved.
- All positive statements here use true final-H witnesses, not witnesses merely present in F outside H; not a proof of originality, publication readiness, or the complete source-posed TIK conjecture.

**FIRST UNIVERSAL UNPROVED IMPLICATION:** for arbitrary ORIGINAL 6m-spread/core-free rank3 E in which each edge touches an E-degree >m^3 vertex, including low-density/unbalanced nonlinear vertex cores and original pair fibres 2,...,m-1 or saturated >=m, prove |H|>=c|E|/m^3 with every exact final-H PAIR, singleton and EMPTY kernel witnessed; or find a genuine SAME-E counterexample sequence. There is no complete rank3 proof, hence no full every-k proof. S045 is the next MANDATORY fifth-session correction audit, FUTURE ONLY.
