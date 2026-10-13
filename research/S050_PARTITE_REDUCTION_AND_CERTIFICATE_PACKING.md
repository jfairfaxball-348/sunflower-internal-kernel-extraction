# P001-S050 — partite normalisation, exact low-richness certificates and the universal packing gap

Date 2026-10-13. This is ONLY owner-invoked S050, archived input first commit d3180124, independent hash manifest second e0d73aec, frozen gate third 0a03d77e **BEFORE** this symbolic proof. All proofs below are SAME-ASSISTANT, not independent peer review, novelty verification, Lean/formal verification or publication. No new experiment and no detailed N1/N2. Mandatory fifth/tenth correction audit is a SEPARATE S050 record. P001-S051 not executed.

## 0. Unchanged target, exact semantics and first deliverables

TIK_k: for every fixed k>=1 exists c_k>0 such that every ORIGINAL finite k-uniform F, and m>=2, has ONE FINAL H subset F with |H|>=c_k|F|/m^k, such that EACH exact intersection K=U∩V of two distinct edges of FINAL H (including EMPTY) is the common exact intersection of m distinct WHOLE edges all IN FINAL H. The triggering pair need not be petals. m=2 is trivial H=F. An arbitrary high-degree or matching method is not a proof of TIK_k.

This session proves (A) an all-rank constant-fraction partite reduction, with a precise rank-three spread/corefree corollary; (B) a complete exact kernel-certificate test for arbitrary one-hub TRIPARTITE triples with no local richness; and (C) a low-richness same-original countercontrol showing that even individually valid graph links and 1-or-m ordinary multiplicity gaps do NOT make their union valid. These are structural reductions and exact tests, NOT the conjectured m^-3 extraction.

## 1. Theorem S050-A — all ranks have a constant-mass multipartite normal form

**Statement.** For every fixed k>=1 and every finite ORIGINAL k-uniform F with e edges, there is a partition V=A_1 disjoint union ... disjoint union A_k (empty classes allowed) such that the ORIGINAL rainbow subfamily G={E in F: |E∩A_i|=1 for EACH i} satisfies

    |G| >= p_k e,       p_k=k!/k^k >0.                       (A1)

Consequently, TIK_k with constant c_k is logically EQUIVALENT (with constants adjusted by p_k) to TIK_k restricted to arbitrary k-partite families: a partite-only guarantee c_k^part |G|/m^k implies the full guarantee p_k c_k^part e/m^k. NO hypothesis of bounded chromatic conflict or rich links is necessary to obtain the k-partite normal form, though neither hypothesis follows afterwards. For k=3, p_3=6/27=2/9 and every G edge has EXACTLY ONE selected hub in A_1, with a bipartite graph G_a between A_2 and A_3. Thus unrestricted R3 is equivalent to its arbitrary tripartite/one-hub graph version. This corrects any impression that one hub per selected triple intrinsically requires a quantitative orientation theorem.

**Proof.** Independently give each ground vertex a label uniform in [k]. An original k-edge has its k labels all different with probability k!/k^k. If X counts ORIGINAL edges whose labels are all distinct, E X =p_k e by linearity (dependencies irrelevant). Some deterministic labeling therefore gives X>=p_k e. Its rainbow edge set G is a subset of F, of cardinality X, and the vertex classes are its k color classes. If an internally m-valid H subset G exists, its WHOLE edges and all its sunflower petals also belong to F, and its pair intersections are exactly the same because H has not changed. Hence size >=c_k^part|G|/m^k>=p_k c_k^part e/m^k. The reverse implication is restriction of the quantified unrestricted theorem to the partite subclass. There is no union of differently colored candidates. QED.

**Normalisation inheritance, precisely limited.** Let k=3 and D be 6m-spread in the S033 sense: d_D(T)<=|D|/(6m)^|T| for every nonempty T of size 1,2,3. Taking the specific G subset D with |G|>=2|D|/9 gives

    d_G(T)<=d_D(T)<=|D|/(6m)^|T|
            <= |G|/[ (4m/3)^|T| ]                 (A2)

since |D|/|G|<=9/2 and (9/2)(2/9)^s<=1 for s>=1. Thus G is (4m/3)-spread, in particular m-spread. If D is robust-corefree, G is robust-corefree, because any nonempty robust subfamily of G is also a robust subfamily of D (links/matching certificates for the same subfamily are unchanged). If every ORIGINAL D edge met some D-vertex of degree>m^3, each G edge retains that fact **as a statement about degree in D**, NOT necessarily degree in G. No after-selection high-degree conclusion is asserted. The precise S036 HDSE3 high-degree-normalized hypothesis therefore is NOT automatically inherited.

This is a quantified constant-mass reduction from unrestricted ORIGINAL family to partite ORIGINAL subfamily. It is NOT an all-rank TIK induction: no cross-hub valid-H packing bound has been supplied.

## 2. Theorem S050-B — exact low-richness FINAL certificate iff for ANY one-hub triples

Let A,B,C be disjoint, m>=3, and let ORIGINAL F be any finite set of triples {a,b,c} with a in A, b in B, c in C. Write G_a for the simple bipartite graph on B union C with bc in E(G_a) iff {a,b,c} in F. The supports, degree spectra and repeated bases can be arbitrary. Let h(bc)=#{a:bc in G_a}. For each ordinary x in B union C define a BIPARTITE INCIDENCE GRAPH J_x with left vertices the active hubs a through x, right vertices the possible ordinary neighbours y of x, and an incidence edge a-y for each ORIGINAL triple {a,x,y}. Its matching number nu(J_x) is the largest exact-{x} sunflower size possible in F (each selected petal has a different hub AND different neighbour). Let nu(F) mean a matching of disjoint WHOLE triples.

**EXACT IFF.** The ENTIRE ORIGINAL F is internally m-valid if and only if all five implications hold (untriggered kernels require no witnesses):

1. For every a and x, if deg_{G_a}(x)>=2 then deg_{G_a}(x)>=m. This certifies the realised PAIR kernel {a,x}.
2. For every a, if nu(G_a)>=2 then nu(G_a)>=m. This certifies the realised hub SINGLETON {a}.
3. For every ordinary base bc, if h(bc)>=2 then h(bc)>=m. This certifies the realised ordinary PAIR {b,c}.
4. For every ordinary x, if there exist two hub incidences a-y and a'-y' in J_x with a!=a' and y!=y', then nu(J_x)>=m. This certifies the realised ordinary SINGLETON {x}. (Nu(J_x)>=2 is equivalent to the trigger.)
5. If nu(F)>=2 then nu(F)>=m. This certifies the realised EMPTY kernel.

**Proof — necessity.** Distinct triples in the same hub have intersection {a,x} exactly when their ordinary graph edges share x, and {a} exactly when those residual edges are disjoint. Any exact-{a,x} petals must all use a and x but different ordinary neighbours: maximum deg_{G_a}(x). Any exact-{a} petals all use a but pairwise disjoint residual edges: maximum nu(G_a). Distinct triples in different hubs meet in a residual PAIR bc precisely when they have the same base; an exact-{b,c} petal is forced to be one of h(bc) different lifted triples. They meet exactly in an ordinary singleton x precisely when their residual edges meet at x but not in the second ordinary vertex; a sunflower with exact kernel {x} uses distinct hub vertices (otherwise petals share that hub) and distinct residual neighbours (otherwise petals share that neighbour). This is EXACTLY a matching in J_x. Finally, an exact EMPTY sunflower is exactly a matching of WHOLE triples in F. Whenever a corresponding trigger exists, its maximum sunflower size must be >=m. Necessity follows.

**Sufficiency.** Every intersection between two distinct selected triples is EXHAUSTIVELY of one of the five types above: same-hub {a,x} or {a}, different-hub ordinary {b,c} or {x} or EMPTY. The witness constructed by each matching/degree/count condition consists of m distinct WHOLE triples IN F meeting pairwise EXACTLY at the given kernel. Therefore F itself is internally m-valid. No local min-positive degree, matching>=2m, log(e), bounded conflict coloring, ambient-petal assistance, or bipartite complete-product premise was used beyond the tripartite setup. QED.

**Relationship with S049-A, no originality inflation.** S049-A's local min-positive degree>=m and matching>=2m hypotheses directly supply conditions 1 and 2, and r(x) either 1 or >=m plus Hall supplies condition 4; its h gap supplies condition 3; and its distinct-hub matching supplies condition 5. S050-B is a LOWER-RICHNESS exact diagnostic, not a deduction that arbitrary F has a large satisfying subfamily. It is a self-contained sharpening of the structural criterion, not an independent literature-firstness claim.

**Low-richness full-validity corollary.** If every G_a has all positive degrees in {1} union [m,infinity) and matching number in {1} union [m,infinity); every positive h(bc) in {1} union [m,infinity); every J_x has matching number in {0,1} union [m,infinity); and nu(F) is in {0,1} union [m,infinity), then H=F is internally m-valid, regardless of original e, log(e), conflict graph q or link minimum positive degree. This does NOT guarantee that an arbitrary input can be made to satisfy the certificate gaps at m^-3 cost.

## 3. Theorem S050-C — sharp low-richness failure of blind link-gluing, SAME-F >=half rescue

For each m>=3, take m hubs a_1,...,a_m, one ordinary x, one y_0 and m-1 further ordinary neighbours z_1,...,z_(m-1), all distinct; make part B={x}, part C={y_0,z_1,...,z_(m-1)}. Define ORIGINAL F_m to consist of

    {a_i,x,y_0}  (1<=i<=m), and
    {a_1,x,z_j}  (1<=j<=m-1).

These 2m-1 WHOLE triples are all distinct. n=2m+1, |F_m|=2m-1; each original edge has exactly one hub and is tripartite. The graph G_(a_1) is a star of degree m, so is internally m-valid (its ONLY realised graph kernel is {x}, m whole graph edges witness); each G_(a_i), i>1, is a singleton and hence vacuously internally valid. The lifted single-hub triples individually are internally valid. All ordinary ORIGINAL multiplicities r(x)=r(y_0)=m and r(z_j)=1, h(xy_0)=m and h(xz_j)=1: EVERY positive original r and h is 1 or >=m, as in S049-A's gap condition. Every hub graph matching is only 1: the strong S049-A hypothesis is absent.

**FULL F_m is nevertheless INVALID:** pick {a_1,x,z_1} and {a_2,x,y_0}; their exact intersection is {x}. Any exact-{x} sunflower must use different hubs and different neighbours. In J_x, only hub a_1 permits a z_j, while every other hub permits ONLY y_0, so nu(J_x)=2<m. Hence the realised singleton {x} has no m-petal certificate. This invalidates the naive all-rank instruction "apply lower-rank TIK within every hub and union", even when the unthinned original links are individually valid and both ordinary multiplicity spectra have the apparent 1-or-m gap.

**SAME ORIGINAL positive rescue:** Let H_m={{a_i,x,y_0}:1<=i<=m} subset F_m. Then |H_m|=m, |H_m|/|F_m|=m/(2m-1)>1/2, and every pair of distinct H_m edges meets EXACTLY in {x,y_0}; all m selected WHOLE edges themselves form the required m-petal sunflower. No singleton x, hub PAIR or EMPTY is realised. Therefore this is only a counterexample to blind gluing, NOT to R3, HDSE3 or TIK.

**Spread/corefree stress without claiming HDSE3:** Take t=216m^3 disjoint copies of F_m. ORIGINAL e=t(2m-1), n=t(2m+1), max vertex degree=2m-1, max pair codegree=m and every edge has an original pair of codegree 1 (the hub/neighbour pair). The ORIGINAL disjoint union is 6m-spread for m>=3: t>=6m handles vertex; t(2m-1)>=36m^3 handles pair (m <=e/(36m²)); and t(2m-1)>=216m³ handles triples. It is robust-corefree because each original edge has a degree-1 pair. The union of the t selected SAME-F rescues H_m is valid: within copies only ordinary base PAIR kernels with m petals; across copies only EMPTY, with m disjoint WHOLE petals chosen from m separate copies. Fraction remains m/(2m-1)>1/2. HOWEVER no edge is forced to touch a vertex of original degree>m³, so this is not a high-hub HDSE3 example. It demonstrates that one-hub, bipartite, spread and corefree need not entail the S049 local richness.

## 4. New strategy/architecture assault, first still-missing quantified bound

By S050-A, there is NO requirement to prove a constant-mass "orient every edge to exactly one hub" lemma: rainbow tripartisation already retains >=2e/9 for ANY original triple family, without changing edges. The missing rank-three statement can be expressed EQUIVALENTLY as:

> There exists an absolute C>0 such that for every m>=3 and every finite tripartite triple family F, one can choose ONE H subset F with |H|>=C|F|/m³ such that **all five final-H implications (1)–(5) of S050-B** hold simultaneously.

This is a NONCIRCULAR exact target formulation in terms of five numerically computable link/matching conditions, but proving its quantified existence is JUST AS HARD as R3; the reformulation alone supplies no mass bound. It is a promising direct "five-certificate packing" architecture distinct from S049's random three-owner high-richness filter: one should select a large H while imposing the five conditions, rather than hope post-selection local degrees survive a Chernoff event.

**Why S049's random ownership is not yet a universal construction:** A given retained edge has probability >=m^-3, but in low-positive-degree original links (as small as 1) event "a permitted active {a,x} has final degree 2,..,m-1" is not exponentially rare; the union bound B2 cannot be extended with an absolute e-independent constant by the same proof. As the F_m stress control shows, original r/h gap and internally valid individual fibres also do NOT suffice: J_x matching is essential. No mass-preserving deterministic repair of all five gaps was proved.

**All-rank bridge:** the multipartite result in S050-A works for every fixed k with p_k>0, but the rank-(k-1) to rank-k induction still needs cross-hub compatibility for every residual kernel and global EMPTY. Coning the countercontrol F_m by a fixed set T of size k-3 on all triples gives a k-partite k-uniform family whose one-hub residual links are internally valid (lifts of stars/singletons), while the union realises kernel T union {x} but has no m-petal witness there. So "independently extract in each link and union" is FALSE for all k>=3. This only disproves that helper, not TIK_k. For m=2 H=F; k=1 take all disjoint singletons when at least m, otherwise one (c_1=1); k=2 the previously recorded S033 graph theorem gives c_2=1/8, subject to same-assistant rather than formal/referee validation.

**What was NOT achieved:** no uniform C>0 for the five-certificate packing inequality; no universal HDSE3 estimate; no R3 proof or counterexample; no c_k all-rank induction; no proof that S049's D=64m²(m+ln(64m³(e+1))) and M=64m³(m+ln(64m³(e+1))) can be removed from its weighted-owner EXISTENCE theorem while retaining e/(2m³). The new partite reduction changes the ranking of obstacles, not the original conjecture.

## 5. Controls and anti-counterexample discipline

- S023/24 planes and S029–S032 palette/row families: rainbow restriction keeps >=2/9 original mass but does not certify the retained graph links as locally rich or final-valid. No source family replaced by a fictitious product.
- S034/35 twins/fractional covers: the exact transversal/matching hypotheses remain and are not implied by partiteness; original-to-final mass factors retained.
- S037–S041 palettes/islands and S042 affine Steiner: complete tensors and global compatible products remain VALID positive controls, not guaranteed structural partitions.
- S043 K_(m-1,m-1), S044 saturated PAIR stars and S045 dense unbalanced families: sparse links can fall below m, so S049-B does not subsume these; dense S045 already has its separate quantitative theorem.
- S046 sparse bridge: e=r(m^4+1), near-full SAME-E H; S047 cyclic shared base: e=2r m^4 and H=e/2, despite 50% incompatible lifts; S048 K_t conflict: original H=F valid despite unbounded q; S049 duplicated rich KNN r=h=2: original INVALID at PAIR, H=e/2 positive. S050-C is ANOTHER low-richness helper failure with SAME-F >1/2 rescue, not a universal counterexample.
- An actual HDSE3 refutation would require a sequence of ORIGINAL normalized high-degree families F_m satisfying m^3 maxvalid_m(F_m)/|F_m| ->0. NO SUCH SEQUENCE is produced here. All stated witnesses lie in the final selected families, and all ratios refer to the same original input.

**Verdict:** two proved reductions/characterisations, one valid same-F negative helper and explicit universal first failed implication. The real work remains the low-richness *simultaneous five-certificate packing* at O(m³) mass cost for tripartite originals, followed by independent every-rank rank-step technology. Previous scoped results are not publication/novelty promoted.
