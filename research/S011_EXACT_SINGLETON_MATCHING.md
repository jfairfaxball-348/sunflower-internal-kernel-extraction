# P001-S011 — exact principal-petal matching certificates and the first missing density step

**One bounded mathematical gate, 2026-10-10.** Target remains full TIK for every fixed k. This report proves only elementary, same-assistant **structural identities for an arbitrary already-selected J** in the prescribed private-light two-heavy slice. It refutes one precisely frozen local-to-global certificate; it **does not** prove an absolute density constant, private-light BSEL, universal BSEL, R3, or all-k TIK. No source/novelty upgrade, algorithmic complexity claim, numerical enumeration, Lean, or independent mathematical review.

## Quantifiers and precise setup

Fix every integer m>=3, a finite simple 3-uniform family packed into pairwise edge-disjoint COMPLETE m-petal sunflower blocks B_1,...,B_t, each with kernel K_i of size 0,1,2. Let V_i be its entire support, r(v)=#{i:v in V_i}, Q={v:r(v)>m}. Assume |V_i intersect Q|<=2 for every i; every vertex outside Q appears in **exactly one block** (block load 1). Hub degrees and overlaps are otherwise completely unrestricted. For arbitrary J subset [t], set H=U(J)=union of ENTIRE B_i, i in J. No witnesses outside H, no hub-disjointness, no single-core-size assumption.

For each realised singleton v, G_v(J) is the ACTUAL simple graph of residual pairs A\{v}, A in H containing v. A residual pair can have 0, 1, or 2 original heavy endpoints; the final type occurs in a light singleton-core block and is not discarded. Matching means vertex-disjoint residual edges, NEVER block incidence.

## Exact residual matching lemma (proved structurally)

(A) If v is light (v not in Q), then it belongs to only one original block. If {v} is realised as an exact intersection of two H triples, that block MUST have exact singleton core {v}, and its m residual petals are disjoint. Therefore nu(G_v(J))>=m; this remains true if some of its residual pairs contain TWO heavy endpoints. Otherwise no singleton {v} is realised, so no matching certificate is required at v.

(B) If v is heavy (v in Q), and J includes a singleton-core block with kernel {v}, its m residual petals are disjoint and nu(G_v(J))>=m. Otherwise classify each i in J for which v in V_i:
* When v is NOT in K_i, the m petals of B_i meet v in exactly ONE triple. Its sole residual pair is available.
* When K_i={v,w}, every residual pair of B_i is {w,z_j}, with z_j mutually distinct. Its contribution to any matching is at most one, and any one such pair is available.
No other case is possible: singleton-core {v} was excluded, and empty-core has no v in core. Thus each v-incident block permits at most one residual matching edge. Its available residual edges either have **no other heavy endpoint** (call it a FREE block), or all available residual edges have the **same unique other heavy endpoint** h in Q\{v} (call it an h-CONSTRAINED block). Let f_v(J) be the number of free blocks and D_v(J) the set of distinct h for which an h-constrained block is selected. Then

> **Exact identity:** nu(G_v(J)) = f_v(J) + |D_v(J)|.

Upper bound: every matching has <=1 residual edge per block, and at most one edge across all blocks constrained to a given h; hence <= f_v+|D_v|. Lower bound: select one residual pair from every free block and from one block for each distinct constrained h. Different selected blocks have disjoint **light** vertices by privacy; free pairs contain no other heavy vertex, and constrained representatives contain distinct h. Thus the chosen pairs are pairwise disjoint, proving equality. This is an actual matching inside H, not a degree proxy. A selected pair-core block whose second core vertex is light contributes exactly one FREE block, not m fictitious matching edges.

(C) If a realised 2-point kernel K contains a light vertex, its two witnessing triple edges must come from the ONE block containing that vertex. They therefore intersect exactly in that block's pair core K; that complete block supplies m triples with K. **Only realised K subset Q with |K|=2 need an additional actual codegree >=m test.** It is not automatic for two original hubs jointly appearing in petals of different blocks.

## Exact empty-kernel certificate from mandatory heavy cores

If J includes an EMPTY-core block, its own m vertex-disjoint petals immediately give nu(H)>=m.

Otherwise every selected block has NONEMPTY core K_i. Put C_i=K_i intersect Q (possibly empty, singleton or two heavy vertices). Each B_i has at most two heavy vertices in its full support. Every heavy vertex outside K_i occurs in at most one petal, since petals are disjoint outside the core. Since m>=3, there is at least one **clean petal** of B_i containing no heavy vertex beyond C_i: at most two petals can be contaminated by optional heavy vertices. In that petal, all remaining vertices are light and globally private to B_i.

It follows that

> **Exact identity (no selected empty-core block):** nu(H) = max{|I|: I subset J and C_i intersect C_j is empty for every distinct i,j in I}.

Indeed, any matching of H has at most one triple per selected block (nonempty core), and if it uses blocks i,j their mandatory heavy cores C_i,C_j cannot overlap. Conversely, for any such disjoint-core set I choose one clean petal per block: mandatory heavy cores are disjoint and all light vertices are private across blocks, so these triples are pairwise disjoint in H. This permits many selected blocks with C_i=empty; such blocks are mutually compatible in the core-footprint matching.

Thus the exact **full-three-kernel validity test for an arbitrary final J** is:
1. Every realised pair K subset Q has actual H-codegree >=m (all pairs containing light vertices are automatically certified).
2. Every realised singleton light v is automatically certified; for each realised heavy v either a selected singleton-core {v} block exists or f_v(J)+|D_v(J)|>=m.
3. If empty is realised, either a selected empty-core block exists or the family of mandatory hub-core footprints C_i has an m-element pairwise disjoint subfamily.
These conditions are necessary AND sufficient, by the exact-kernel sunflower/matching equivalence. They are properties of the FINAL H. They require no disjoint-hub hypothesis and allow all 0/1/2 core types.

## One frozen nontrivial local-to-global lemma — FALSE

**EXACT_LOCAL_IMPLIES_EMPTY (refuted).** For every m>=3, every sufficiently large |J| (even |J|>=3m^3) in a private-light two-heavy packing, if ALL realised pair kernels have >=m actual third vertices and ALL realised singleton links have actual m-matchings, then any realised empty kernel also has an m-triple matching. This is a tempting way to turn exact local certificates into full compatibility without a separate hub-core matching analysis.

**Parametric symbolic witness.** Fix any m>=3 and any N>=max(m+1,3m^3). Introduce two hubs a,b. For each i=1,...,N create pair-core block P_i^a with m triples {a,u_i,z_{i,j}}, j=1,...,m, where u_i and all z_{i,j} are private, mutually distinct. For each i create P_i^b with m triples {b,w_i,y_{i,j}}, all w_i and y_{i,j} private and distinct from every symbol on the a side. Blocks are complete pair-core m-sunflowers and edge-disjoint. There are t=2N blocks. Exactly Q={a,b}: r(a)=r(b)=N>m, and every other vertex has block load one; each block meets Q in ONE vertex, hence meets the <=2 rule.

Select ALL blocks. The only realised exact 2-point kernels are {a,u_i} and {b,w_i}, each with codegree exactly m inside its own block. The only realised singleton kernels are {a} and {b}: select triples from two different spokes of the same star. Their actual residual links are N disjoint-in-spokes stars, centered respectively at u_i and w_i, and nu(G_a)=nu(G_b)=N>=m (choose one pair from each spoke; no matching can use two edges of one spoke). No singleton kernel at a private u_i or w_i is realised. Empty is realised by one a-side and one b-side triple. However every H triple contains either a or b, so every triple matching has size at most TWO; one triple from each side gives nu(H)=2<m. Thus the frozen lemma fails for EVERY m>=3 and UNBOUNDED N, even though t>3m^3, all pair certificates are exact and all realised singleton links contain actual m-matchings. The failed step is omitting the independent mandatory-core global matching certificate, **not** hub-degree saturation (S010's different failure).

**Positive density control, not BSEL refutation.** Selecting all N a-side blocks alone is internally valid: all pair kernels certified by their blocks, singleton {a} certified by N distinct free residual pairs, and empty is NOT realised since every retained triple contains a. It retains N=t/2 blocks. Hence this witness cannot disprove any absolute gamma; no attempt to assert a global BSEL negative is justified.

## Boundary checks, density gap, and stop

For t=0 choose J=empty. For 1<=t<=3m^3 choose exactly one complete original block, giving |J|=1>=t/(3m^3); its only realised intersection is its own kernel, with m in-H petals (including empty-core blocks). For m=2 the full TIK target has the trivial H=F witness. For t>3m^3 the **first unproved quantified step** is to extract J with |J|>=gamma*t/m^3 for absolute gamma>0 while satisfying the three exact compressed tests **simultaneously**, not merely locally and not by deleting high-load hubs. The characterization has NO density lower bound and gives no complexity bound; there is no proof of private-light BSEL, unrestricted BSEL, R3 or full TIK.

Historical S006 cross-block obstructions, S006 vertex-disjoint and S007 bounded-load positive proofs, S008 one-hub negative/all-valid control, S009 THIN_Q negative/all-valid mixed-core control, S010 SAT_CROSS negative/positive half-density control, and tenth audit survive without weakening. No palette rerun, unfrozen enumeration or source status promotion. This is AI-only symbolic reasoning, not independent review. ONE next S012 quantitative obligation prepared; not executed here.
