# P001-S019 — pair-active weighted optional-channel sublemma; mixed-star obstruction

**2026-10-11; one bounded proof-first child session.** Same-assistant symbolic derivation, NOT independent mathematical review, novelty certification, all-k TIK proof or paper. The immutable original TIK theorem is for EACH fixed k>=1, ALL m>=2 and every k-uniform F: an in-family H of size >=c_k*m^(-k)|F| must contain m exact petals entirely in H for EVERY exact intersection of two distinct H-edges (EMPTY included); witnesses need not be that pair. Rank-three R3, universal BSEL and this private-light two-original-heavy-support packing are strictly auxiliary.

## I. ONE quantitative t-based target frozen BEFORE the attack

The commit research/S019_FROZEN_GATE.md froze **PAIR_ACTIVE_96** at child commit 2840db9db21be207568e3fbad5380eaef17fa89f, after verbatim owner invocation archive commit f7d1ddeaa35cb68d225819cd544f14b7c0c1e62c and BEFORE the present report. Quantifiers: any m>=3 and arbitrary complete edge-disjoint m-triple-sunflower packing of t blocks of original core size 0,1,2, with Q={v: original block incidence r(v)>m}, at most two Q vertices per block support, all non-Q vertices block-private, and original pair-inactive A0 satisfying |A0|<t/2. Claim under TEST, not assumed: a WHOLE-block J with |J|>=t/(96*m^3) that simultaneously passes all exact 2/1/0 kernel tests in its own H. This candidate is NOT proved or refuted in S019. Original Q labels remain frozen. Since S018 already proves |J|>=t/(24m^3) for |A0|>=t/2, a proof of this candidate would yield the desired quantitative bound for this entire private-light slice, but still NOT universal BSEL/R3/all-k TIK without more work.

## II. A pair-active two-OPTIONAL-hub quantitative result

Define E00 as the original blocks i whose support meets Q in EXACTLY two hubs e={u,v}, whose ORIGINAL core K_i meets Q in EMPTY, and whose unique heavy pair e occurs together in a selected triple. Such a block is pair-active, and its original core is necessarily either EMPTY or a singleton private light vertex. Its two original Q hubs appear together in precisely ONE triple, with m-1 other completely Q-free petals; its light vertices remain block-private. Write T00=|E00|, and s_e=#E00 blocks with hub-pair e. Distinct e index disjoint classes and sum s_e=T00.

**Proved restricted joint bounds (same-assistant):** For every m>=3 there is a set J of WHOLE blocks drawn SOLELY from E00, in whose final union every realised exact pair, singleton and EMPTY is m-witnessed, with

    |J| >= T00 / [6*m*(m-1)^3] >= T00/(6*m^4).

For T_sat=#E00 blocks in classes having s_e>=m, choosing ONLY those saturated classes yields the STRONGER fully certified

    |J| >= T_sat / [6*(m-1)^2].

These are bounds on precisely defined submasses; neither is an absolute t-based estimate when the corresponding numerator may be zero.

**Pair compression.** For every nonempty E00 class e independently retain q_e=s_e blocks when s_e>=m, otherwise ONE block when 1<=s_e<m. Then q_e in {1} union [m,infinity), and q_e>=s_e/(m-1). Encode each e as an edge of a SIMPLE original-Q graph G, with weight q_e (not parallel graph degree). Its total weight W=sum q_e>=T00/(m-1). There is no e-core contribution because K_i meets Q in EMPTY, so any eventually selected e has exact pair codegree d_H(e)=a_e equal to its selected block weight, namely either 1 or >=m. Every pair containing a private light vertex is automatically witnessed within its original complete block.

**Weighted distinct-neighbour degree lemma.** Any finite simple graph with nonnegative/positive edge weights W and integer m>=3 admits a nonempty (if W>0) edge set E' with weight S>=W/[6(m-1)^2] and degrees in {0,1} union [m,infinity), counting DISTINCT neighbours. Proof: iteratively peel vertices with surviving degree <m. If the surviving m-core has weight >=W/2, keep all its edges. Otherwise the peeled edges have weight >W/2, and each vertex has <=m-1 outgoing edges oriented from its peeling time. Label these at most m-1 outgoing slots; each slot is an outdegree<=1 pseudoforest, properly vertex-3-colourable. Assign edges by head colour to at most 3(m-1) disjoint-star-forest layers. Choose a heaviest layer of weight >W/[6(m-1)]. In each component star, keep ALL arms if its number d>=m, and otherwise keep its single heaviest arm (at least 1/(m-1) of its component weight). This gives S>W/[6(m-1)^2], and every surviving star centre has degree 1 or >=m, all leaves degree 1; components are vertex-disjoint. The m-core case has all degrees >=m. We use a SIMPLE graph: repetition of the same hub pair can increase pair codegree but cannot falsely increase a heavy singleton matching.

**Every exact kernel in the SAME final J.** Select the corresponding q_e complete original E00 blocks for each e in E'. Then heavy pairs are either absent, appear in ONE triple, or have >=m truly distinct third vertices from their selected class. For original hub v, its residual link consists of pairs {u,x} for neighbours u of v in the selected SIMPLE graph, with x private to each block, and no v-triple occurs outside its own e. Consequently f_v=0, D_v=the selected distinct graph-neighbour set N_G(v), and the ACTUAL S011 matching nu(G_v)=|D_v|=degree(v). A heavy singleton {v} is realised precisely when at least TWO distinct e-neighbours occur; the degree lemma makes it >=m. Private light singleton intersections are either unrealised or the original light singleton-core block supplies its m disjoint residual petals. No selected original block has a mandatory Q footprint (C_i=empty). If S=|J|>=m, choose one Q-free original petal from each of m DIFFERENT selected blocks; all its vertices are block-private light, so this is an ACTUAL m-disjoint-triple matching for EMPTY (whether or not empty is realised). If 1<=S<m, instead take ONE complete original block, which by itself satisfies every realised exact kernel, including an EMPTY original core, with its own original m petals. This small-S fallback is part of the same final selection, never added to a conflicting subfamily.

**Quantitative accounting.** If S>=m: |J|=S>=W/[6(m-1)^2]>=T00/[6(m-1)^3]>=T00/[6m(m-1)^3]. If 1<=S<m: W<=6(m-1)^2 S<6m(m-1)^2, so T00<6m(m-1)^3 and choosing one original block gives |J|=1>=T00/[6m(m-1)^3]. If T00=0 take empty. For the saturated-only subgraph all edge weights s_e>=m, so any nonempty selected edge set automatically has S>=m; there is no pair compression or small-S loss, and |J|>=T_sat/[6(m-1)^2]. This explicitly isolates the extra m-loss from numerous short noncore e-classes; the proof DOES NOT quietly turn it into m^-3.

## III. Earliest attempted full-star composition implication is FALSE

The natural next bridge after m-core peeling is the following precise **MIXED_STAR_CLOSURE** implication (SUBSIDIARY, not another frozen quantitative gate): If selected original-Q pair-active classes form a simple star with centre v and >=m DISTINCT neighbours, all their heavy pair classes are saturated (actual d_H(e)>=m), and every realised heavy singleton residual link already has an ACTUAL m-matching, then their whole-block union is internally valid. It would allow a weighted high-star branch without separately solving EMPTY. It is FALSE for every m>=4.

**NEW parametric symbolic example (distinct from S014–S018).** Fix m>=4 and N>=m+1, to be arbitrarily large at FIXED m. Take original Q symbols v,a_1,...,a_m,b_1,b_2. Every light symbol used below is distinct globally except its repetition within the one sunflower block that owns it.

For each i=1,...,m and l=1,...,N introduce a full genuine heavy-heavy pair-core block

    P_(i,l) = { {v,a_i,x_(i,l,r)} : 1<=r<=m }.

For j=1,2 and l=1,...,N introduce a complete heavy-light pair-core block

    R_(j,l) = { {b_j,y_(j,l),v} }
              union { {b_j,y_(j,l),z_(j,l,r)} : 1<=r<=m-1 }.

Each core is respectively {v,a_i} or {b_j,y_(j,l)}; all m triples in each block are distinct, the block intersections equal the stated original exact core, all original blocks are edge-disjoint, and every support contains exactly TWO original hubs. The sole v-containing R petal is OPTIONAL heavy contamination: v is NOT in the R core. Original loads are r(v)=(m+2)N, r(a_i)=N, r(b_j)=N, all >m. Every x,y,z is block-private, hence Q is EXACTLY {v,a_1,...,a_m,b_1,b_2}, with no post-selection relabeling. The original active graph is the STAR with m+2 neighbours and ALL t=(m+2)N blocks are pair-active, A0=0.

**TRUE pair tests in the ENTIRE J_all=[t].** For e_i={v,a_i}, p_e=N, a_e=0, d_H(e_i)=mN>=m; for h_j={v,b_j}, p_e=0, a_e=N, d_H(h_j)=N>=m. All other heavy pairs have codegree zero. A realised pair containing a private light belongs to its unique original complete pair-core block and has m original in-H petals. Thus ALL exact pair intersections pass, including the previously noncore saturated e={v,b_j} classes.

**TRUE singleton tests in J_all.** At v, all residual pairs are constrained to the distinct other-heavy endpoints a_1,...,a_m,b_1,b_2. Hence f_v=0, D_v={a_1,...,a_m,b_1,b_2}, and nu(G_v)=m+2>=m; {v} is realised. At b_j, the N different R pair-core blocks provide N FREE residual blocks, one from each private-light y_(j,l), so f_(b_j)=N, D_(b_j)=empty, and the genuinely realised {b_j} has nu(G_(b_j))=N>=m. Every a_i only occurs together with v, so singleton {a_i} is UNREALISED and requires no certificate. Private-light singleton kernels are likewise absent unless original singleton-core (there are none). Thus ALL realised singleton intersections pass.

**TRUE EMPTY test in J_all: FAILS.** Empty is realised by a P triple and an R non-v petal with disjoint original hubs/private lights. EVERY selected P triple contains v; EVERY R_(1,l) triple contains b_1; EVERY R_(2,l) triple contains b_2. Thus ANY set of disjoint selected triples contains at most ONE P triple, ONE R_1 triple, and ONE R_2 triple, hence nu(H)<=3. Conversely choose one P triple and one non-v R_1 and one non-v R_2 petal to obtain THREE truly disjoint triples. Therefore nu(H)=3<m, for EVERY m>=4. There is NO empty-core block; mandatory ORIGINAL Q-core footprints are {v,a_i} on P and {b_1},{b_2} on R, with pairwise disjoint-core matching maximum 3. The ALL-PAIR/ALL-SINGLETON SATURATED STAR therefore fails exactly EMPTY.

**Internally valid DENSE whole-block control.** Take J_good=ALL mN P blocks, discarding both R classes. Every triple now contains v, so EMPTY is genuinely ABSENT. Heavy pair {v,a_i} has exactly mN petals; heavy singleton {v} is realised across different i and has ACTUAL f_v=0, |D_v|=m, hence nu(G_v)=m; all a_i singletons absent and light kernels automatic. Thus ALL 2/1/0 tests PASS in J_good, and

    |J_good|=mN = [m/(m+2)]*t >= (2/3)*t.

In particular max_valid*m^3/t >= m^4/(m+2)>0 at every fixed m; the family emphatically does NOT refute any absolute gamma/BSEL/R3/TIK. S011 already showed the *conceptual necessity* of separately checking EMPTY; this is a NEW precise star-of-saturated-pair-active-classes parametric obstruction to the stronger mixed compulsory/optional star consolidation, with m+2 distinct channels, pair and singleton tests all passing, and a dense control, NOT an assertion that the conceptual obstacle is novel.

## IV. Exactly where PAIR_ACTIVE_96 remains open

Write t=|A0|+|X_hh|+T_sat+T_short+T_mixed, with disjoint assignment: X_hh is S018 clean heavy-heavy pair-core mass, T_sat/T_short are the E00 classes above, and T_mixed is all remaining pair-active mass, including heavy compulsory/optional orientations, contaminated heavy-light pair cores and singleton-heavy cores. For a partition keep X_hh and E00 disjoint. Existing valid options show

    max_valid >= |A0|/[12(m-1)^3],
    max_valid >= |X_hh|/[6m^3],
    max_valid >= T_sat/[6(m-1)^2],
    max_valid >= T00/[6m(m-1)^3].

These selections may NOT be united automatically. If T_mixed is a large fraction, the displayed bounds can all be zero; if T_short dominates, the best new uniform submass bound is order m^-4, not the required absolute times m^-3. MIXED_STAR_CLOSURE's failed EMPTY implication prevents promoting weighted centre-star mass into a certified class-free branch. Needed NEXT is an explicit bounded-loss joint rule that simultaneously handles short unsaturated active pairs and mixed compulsory/optional centre directions, and either eliminates EMPTY or produces m truly disjoint ORIGINAL Q mandatory-core footprints, without prelocking them. This is a quantitative gap, not a proof of PAIR_ACTIVE_96 or TIK.

## V. Boundaries, inheritance and limitations

m=2: full original TIK trivially H=F, because the two selected edges themselves form a 2-petal exact sunflower at their intersection. t=0 gives J empty. For 1<=t<=3m^3 (m>=3) one complete original block J has |J|=1>=t/(3m^3) and exactly witnesses its own core. The new obstruction uses m>=4; m=3 has no counterexample from nu(H)=3. S006 disjoint-support gamma=1, S007 bounded load 1/3, S008/S009 fully valid high-hub controls, S010/S011 singleton/empty structural checks and dense controls, S012 pair-only filter, S013 protected A0, S014/S015 negative-class gates and exact fifth/tenth/fifteenth audits, S016 fixed-backbone failure with dense alternative, S017 SAFE_SPINE(12) and S018 A0_MAJORITY_24 and its contaminated optional-b two-channel noncomposability are all retained, NOT generalised. Next mandatory fifth-session progress/correction audit is S020, not S019. Parent mathematical S001 UNEXECUTED. No unbounded computation, Lean, manuscript, external action, detailed new N1/N2 or publication claim. The new claims are same-assistant mathematical reasoning; CI only checks structure and semantic fixtures, not an independent proof referee.
