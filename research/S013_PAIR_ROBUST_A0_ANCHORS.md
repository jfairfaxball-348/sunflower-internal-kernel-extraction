# P001-S013 — protected pair-inactive certificates: one quantitative joint-refinement intermediary

**One bounded proof-first child session (2026-10-10).** Exact original aim stays full TIK for EVERY fixed k and witnesses entirely in the retained family, with retention c_k m^(-k), c_k dependent only on k. Rank-three R3 and universal BSEL are auxiliary, and arbitrary private-light two-heavy BSEL is STILL UNPROVED. The earliest missing S012 bridge is simultaneous preservation of the exact S011 singleton and empty matchings without breaking heavy-pair saturation. We freeze and prove ONE explicitly *restricted* certificate-protection lemma. No new detailed N1/N2, original-paper theorem, Lean, numerical search, algorithm claim or independent mathematical review.

## Exact general setting and protected intermediary

For all integers m>=3, any t>=0, take an edge-disjoint packing B_1,...,B_t of COMPLETE m-triple sunflower blocks, kernels of size 0,1,2, supports V_i. Define r(v)=number of original blocks meeting v, Q={v:r(v)>m}. Assume each support meets Q in at most TWO vertices, and each v outside Q appears in at most ONE block (block-private). Supports of heavy hubs may overlap arbitrarily, with unbounded degrees; no common hub or core type. All selections retain entire blocks, and all required m-petal exact-kernel witnesses must lie in final H.

Call a block **pair-inactive** if NONE of its m triples contains two original hubs from Q. Let A0 be all pair-inactive indices. These are exactly the untouched A0 class in S012 PAIR_FILTER, NOT the set of low-load blocks. For each hub v define N0(v)={i in A0:v in V_i}, and s0(v) indicate whether some i in A0 has exact singleton core {v}. For i in A0 with nonempty core put C_i=K_i intersect Q; because no triple has two hubs, C_i is either empty or a singleton. Put u0=# {i in A0:K_i nonempty and C_i=empty} and W0={v in Q: some i in A0 has nonempty core and C_i={v}}.

**FROZEN lemma — A0_PROTECTED_JOINT.** In addition to the general packing conditions assume:

(P1) for EACH v in Q, either s0(v) is true OR |N0(v)|>=m.

(P2) either there is an EMPTY-core original block in A0, OR (if no such block is in A0) u0+|W0|>=m.

Then the **specific, unchanged S012 PAIR_FILTER** selects a J containing A0 and satisfying

    |J| >= t/(m-1) >= t/m^3,

with ALL exact pair intersections realised by its final H=union_{i in J}B_i internally m-sunflower-witnessed: heavy pairs have true >=m final codegree, heavy singletons have ACTUAL final residual graph m-matchings, and a realised empty intersection has an ACTUAL final m-triple matching. Light kernels are automatically certified. Thus the restricted slice admits gamma=1 with the target-normalised t/m^3 bound. The extra P1/P2 conditions are hypotheses, NOT properties known in arbitrary packings.

## Proof, retaining all three certificates simultaneously

1. **True pair saturation and density.** Partition e-active blocks by the unique unordered heavy pair e on some triple; |V_i intersect Q|<=2 makes their A_e classes disjoint. S012 PAIR_FILTER retains ALL A0, every A_e with an original e-pair-core block or >=m e-active blocks, and one arbitrary representative of any remaining A_e (size 1,...,m-1). For a realised heavy e in the selected union, either an e-core contributes m genuine different third vertices, at least m singly e-active retained blocks contribute m different third vertices, or only one e-containing triple survives so e is NOT a two-triple intersection. Therefore all realised heavy pairs have actual codegree >=m. Pairs containing a block-private light vertex are automatically core pairs of a retained complete original block. Every class retains at least 1/(m-1) of its members, hence |J|>=t/(m-1). No later deletions or pair-class-breaking thinning occurs.

2. **Actual heavy singleton m-matchings protected in A0.** For v in Q, if s0(v), an A0 singleton-core {v} block survives, supplying its m disjoint residual pairs INSIDE H. Otherwise each A0 block meeting v has a NON-{v} core and supplies one available residual graph edge containing v. That edge has **no other original hub**: if it contained w in Q\{v}, that block would be {v,w}-active, contradicting membership in A0. Its other residual vertices are light and private to its block. Select one such edge from EACH of any m distinct i in N0(v), guaranteed by P1. All those residual pairs are vertex-disjoint, since their vertices are light and block-private. Thus nu(H({v}))>=m; equivalently S011 has f_v(J)>=m or a selected singleton-v core, with no substitution of block degree for matching rank. Every possible realised heavy singleton is covered, not just those visible before filtering. Light singleton intersections are certified by their own retained complete block as in S011.

3. **Actual empty-kernel m-matching protected in A0.** If A0 contains an empty-core block, its m original disjoint triples remain in H. Otherwise all A0 blocks have nonempty core, and S011's exact mandatory-heavy-core matching identity applies to the A0 subpacking. All mandatory cores C_i have cardinality at most one. Exactly u0 blocks have C_i=empty and are mutually disjoint at compulsory-heavy-core level; additionally we can take one block from EACH distinct v in W0, giving u0+|W0| pairwise disjoint mandatory core footprints. By P2 choose m such blocks and in each choose a petal avoiding optional heavy vertices. This is possible as m>=3 and at most two original-heavy support vertices occur per block, so at most two petals contain optional heavy vertices. All remaining vertices of those clean petals are private light vertices and different blocks have disjoint compulsory heavy cores. They are m disjoint triples INSIDE A0's union and hence H. No local singleton certificates are used as a substitute for this global matching. Thus even if empty is newly realised after PAIR_FILTER, it is certified.

The selected J is the SAME J in all three paragraphs, retaining entire blocks. This proves A0_PROTECTED_JOINT with no restriction on active-class size, overlaps, high hub load, or block-core mixture beyond P1/P2 and privacy. For t=0 take J=empty (conditions vacuous and 0 bound). For 1<=t<=3m^3 the independent one-block fallback also gives >=t/(3m^3) in unrestricted packings; this is NOT a proof of general gamma=1. m=2 full TIK is trivial by H=F, unrelated to the m>=3 lemma.

## Symbolic nonvacuous parametric control: overlapping q-cycle with ALL three core sizes

Freeze m>=3 and q>=m+5. Let X={h_1,...,h_q} be hubs indexed cyclically. Introduce otherwise globally private light vertices for every displayed petal. For EACH unordered NON-cycle hub pair {u,v} (not successive on the q-cycle), create one complete pair-core block P_uv of m triples {u,v,z_{uv,j}}, j=1,...,m. For EACH of the q cycle pairs {u,v}, create TWO distinct complete EMPTY-core blocks D^1_uv,D^2_uv: each contains exactly one triple {u,v,z} and m-1 further triples on globally private light vertices, pairwise disjoint and disjoint from that distinguished triple. For EACH hub v, create one singleton-core block S_v of m triples {v,x_{v,j},y_{v,j}} using only private lights. Finally add one all-light complete EMPTY-core block E of m disjoint light triples.

These blocks are pairwise edge-disjoint complete m-triple sunflowers of all three exact core sizes, every support has <=2 hubs, every nonhub is globally block-private, and the ORIGINAL heavy load of every v is (q-3)+4+1=q+2>m. Thus Q=X exactly and the hubs form an arbitrarily large overlapping interaction graph. The block count is

    t = [binom(q,2)-q] + 2q + q + 1 = binom(q,2)+2q+1.

Here A0 consists EXACTLY of S_v (all q of them) and E, so P1 is protected by each S_v and P2 by E. On each non-cycle pair there is an original pair-core, so PAIR_FILTER keeps P_uv. On each cycle pair its class has exactly TWO non-core active blocks; since 2<=m-1 PAIR_FILTER keeps exactly ONE of D^1_uv,D^2_uv. It retains the q+1 pair-inactive anchors, so

    |J| = t-q = binom(q,2)+q+1 >= t/(m-1).

Every selected realised heavy pair on a non-cycle edge has an exact m-petal pair core; each cycle heavy pair is present in exactly ONE selected triple and therefore is NOT a realised exact two-triple pair intersection. Every realised heavy singleton v has an in-H m-residual-pair matching from S_v; E supplies an in-H m-triple empty-kernel matching. Light intersections are automatic. Hence THIS mixed-core final union is fully valid, with no restricted hub-disjointness or single-core projection.

This reduction is genuinely necessary for the displayed starting packing: the complete original union contains exactly TWO triples containing any fixed cycle pair e, one from each D block, so e is realised but has codegree 2<m. Keeping everything is NOT valid, whereas the stated pair-safe filtered J is. The construction is a positive witness/control of the frozen restricted lemma, not a finite empirical search or a proof of the general case.

## Sharp location of the remaining gap

Nothing proves P1 or P2 for arbitrary pair-inactive classes. S010's high-degree star a has no protected A0 singleton-core or m A0-free-residual-block reservoir, yet its globally dense compatible subfamily retains >half; S011's two N-spoke stars have A0 mandatory heavy cores only {a} and {b}, so u0+|W0|=2<m, yet a one-star compatible half survives by avoiding the empty intersection. Therefore P1/P2 are **sufficient, not necessary** and deleting their absence from the hypothesis would be unjustified. In particular there is still no quantitative method extracting >=gamma*t/m^3 compatible blocks from *arbitrary* unprotected heavy pair-active classes without breaking pair codegrees, creating unmatchable hub singletons or creating empty intersections with no true global matching.

The S006/S007 positives, S008/S009 all-valid controls, S010/S011 >=half-density controls and exact S012 pair-only lemma remain intact. Neither general private-light two-heavy BSEL, universal BSEL, R3 nor all-fixed-k TIK is proved or refuted. Proof is elementary same-assistant symbolic reasoning only; hosted CI is structure/semantic-fixture checking, not independent proof verification. No claims of novelty, publication, theorem formalisation or algorithmic complexity. ONE standalone S014 handoff is prepared and NOT executed.
