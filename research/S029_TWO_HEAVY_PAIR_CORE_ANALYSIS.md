# P001-S029 — two-original-heavy petal-first pair/singleton/empty gate

**2026-10-11. Exactly ONE bounded proof-first mathematical session.** Fresh owner invocation `sessions/P001-S029/INPUT.md` archived at commit `f0f931d5ac6e743c62eff7a01ded0a9d36176947`, 121 exact UTF-8 bytes, SHA256 `653bdbeaa99d0835ef42fc2506ae4e0fd5407439947c078e071fef95ac168b1a`; frozen quantifiers and integer **C=512** at separately prior commit `54407397e2cd5d2888e418566cbbdebf36e77220`. All claims below are same-assistant symbolic analysis, not independently checked mathematics, source novelty, Lean or a publication. No search or numerical experiment was run.

## 1. Exact original population

For every m>=3 and t>=1, pairwise edge-disjoint COMPLETE m-petal 3-uniform sunflower blocks B_i have original supports S_i, original heavy Q={x:#{i:x in S_i}>m}, and |S_i∩Q|<=2. Every original light x not in Q belongs to <=m original supports. Nothing is repartitioned after selection. We test ONE fixed claim: some H of INDIVIDUAL triples in the original union has |H|>=t/(512m²) with every realised exact two-point, singleton and EMPTY kernel m-witnessed wholly in this H. The selected pair need not belong to its witnesses.

## 2. Genuine positive subpopulation: blocks with an available <=1-Q petal

Partition original blocks into A={i: some E in B_i has |E∩Q|<=1} and B=[t]\\A. This is by ORIGINAL Q, regardless of unselected other petals. **Claim A (proved symbolically):** for every nonempty A there exists internally m-valid H_A with

    |H_A| >= |A| / ((3m-2)(m-1)) >= |A|/(3m²).

Choose one admissible E_i from every A block. Its light part L_i=E_i\\Q has <=3 labels; each belongs to <=m original supports. The representative light-conflict graph therefore has maximum degree <=3(m-1), and greedy independence retains s>=|A|/(3m-2) distinct chosen triples with pairwise disjoint light portions. EACH chosen representative has actual heavy tag either 0 or exactly one q in ORIGINAL Q, even if its ORIGINAL block has two Q vertices elsewhere. Partition s retained reps by tag. When there are h>=m nonempty tag classes, keep all reps in a class of size>=m, otherwise keep one: count >=s/(m-1). The only realised singletons are tags of large classes, with m genuinely light-disjoint residual pairs. EMPTY across classes has an ACTUAL m-disjoint matching using one from each of m distinct tags (tag 0 is one class); two-point and light singleton kernels are absent. When 1<=h<m, keep a largest tag class of size d>=s/(m-1) if d>=m: its reps share exactly their tag or are entirely disjoint, supplying an exact m-sunflower. If d<m, replace everything by ONE entire original complete block: its m petals internally certify its only realised exact kernel, including possible EMPTY, and m>d>=s/(m-1). No union with another channel and no full-original-support thinning.

Hence if |A|>=t/2, the frozen C512 requirement is actually satisfied with |H_A|>=t/(6m²). This is a rigorous extension of S028's *selected petal* argument to original supports with TWO heavy vertices, but only for the A mass. This result is NOT an all-B or all-t positive theorem.

## 3. Exact structure of the unsolved B population

For i in B, ALL m petals contain exactly two ORIGINAL Q vertices. Since their common intersection is their exact sunflower core, it follows that K_i={u_i,v_i} is a pair of Q vertices: with <=2 Q in S_i, no third vertex can be heavy. Each B_i has exactly m distinct original-light third labels z_(i,1),...,z_(i,m). The m-choice bipartite graph (original B-blocks versus available third labels) has left degree m and right degree at most m (each light is in <=m original supports). Hall follows from m|T|<=m|N(T)| for every subset T of blocks. **Therefore a simultaneous injective representative third-label assignment exists for ALL B blocks, even with nonprivate original light**, without deleting any original block or spending an m factor.

Let w_uv be the number of original B blocks whose core is original heavy pair {u,v}; the Hall representatives are distinct triples {u,v,z_i} with ALL their chosen z_i distinct and outside Q. For any subset R of these representatives write a_uv(R) for multiplicity of pair uv, and G_R for the simple graph on Q of pairs with a_uv(R)>0.

**Exact final-H certificate equivalence for these representatives:**
1. Realised 2-kernel {u,v} occurs exactly when a_uv(R)>=2; its in-R codegree is exactly a_uv(R), so each multiplicity must belong to {0,1} union [m,infinity).
2. Realised singleton {u} occurs exactly when the SIMPLE neighbour count deg_G_R(u)>=2; the ACTUAL residual matching number is exactly deg_G_R(u), NOT sum_v a_uv(R), because all residual pairs with the same other heavy v share v; different neighbours and injected distinct light labels give an exact matching. Thus degrees belong to {0,1} union [m,infinity).
3. EMPTY is realised exactly when G_R has two vertex-disjoint edges. The actual triple matching number in R is exactly nu(G_R): a triple matching uses graph vertex-disjoint heavy pairs, and conversely choose a representative for each graph matching edge; third labels are globally injected. Therefore when nu(G_R)>=2 one must have nu(G_R)>=m.

This equivalence includes all exact intersections and uses the FINAL selected reps only, not ambient degree or external witnesses.

## 4. First FALSE quantitative proof step and dense same-family rescue

**FALSE intermediary REP_ONLY_B_512:** For every all-B packing as above, the injected one-representative-per-original-block multigraph admits a subset R of representatives internally m-valid with |R|>=t_B/(512m²). This is NOT the frozen full H claim, since it forbids selecting multiple petals of the same ORIGINAL block.

For EVERY m>=3 take disjoint heavy sets U,V of size m-1 each. For every of the (m-1)² pairs (u,v) in U x V create exactly m-1 distinct ORIGINAL m-petal 2-core blocks

    B_(u,v,j)={{u,v,z_(u,v,j,r)}: 1<=r<=m}, 1<=j<=m-1,

with ALL z globally private. Then t_B=(m-1)^3, all original blocks edge-disjoint and complete; each heavy vertex lies in (m-1)² original supports, >m for m>=3 (m=3:4>3), and all z have support load 1. ORIGINAL Q=U union V exactly, and every original block meets Q in precisely 2 vertices. No symmetry reduction, hidden relabelling, or finite search.

For ANY one-per-block representative selection, each pair uv has at most m-1 available reps. To pass exact two-point certificates, a_uv can only be 0 or 1. As the underlying simple graph is a subgraph of K_(m-1,m-1), every vertex has degree at most m-1: to pass actual singleton matching, its selected degree can only be 0 or 1. Hence selected pairs form a MATCHING; but any matching in K_(m-1,m-1) has size at most m-1<m. If two disjoint pairs are selected, EMPTY is realised and cannot have m disjoint triples, so |R|<=1. One representative is vacuously internally m-valid. At literal m=1026, t_B=1,076,890,625 and t_B/(512m²)=1.99805258... >1 (ceil=2); the intermediary is FALSE. Along m→infinity, t_B/(512m²)~m/512→infinity. The obstruction simultaneously uses unsaturated pair codegree, insufficient DISTINCT hub neighbours and missing true empty matching.

**Dense positive alternate INSIDE THE ORIGINAL SAME F:** Choose one heavy pair (u,v) and retain ALL m petals from each of its m-1 original blocks: |H_good|=m(m-1), all triples have exact common pair {u,v} and globally distinct private third labels, so every distinct selected pair has this exact pair kernel and at least m IN-H petals; no singleton or EMPTY occurs. For m=1026, |H_good|=1,051,650 >> t_B/(512m²). In particular the parametric example is NOT a counterexample to the frozen full C512 inequality, R3 or TIK. It shows why an all-block one-petal-only abstraction destroys crucial same-pair full-petal mass.

## 5. The first still UNPROVED step toward the frozen C512 inequality

If |B|>=t/2, it would suffice to construct a possibly multi-petal H_B from the B blocks with |H_B|>=|B|/(256m²) and every exact kernel internally m-witnessed; one must not simply concatenate independently valid A and B selections. Hall gives unique light *representatives* but NOT internally valid original FULL blocks glued across Q pairs. The foregoing K_(m-1,m-1) control proves that the tempting universal one-representative extraction at order t_B/m² is false; retaining whole saturated pair classes may recover an m factor but generates potential singleton/EMPTY and, with nonprivate light, additional Q-light pair intersections. **There is presently NO collision-aware selection/charging lemma establishing t_B/(256m²) for arbitrary weighted original-Q pair graphs while accounting for extra petals.** No universal extension of C512 is proved or refuted. S024 unrestricted DIRECT_PARTIAL_EDGE_512 and S025 stronger GLOBAL_EDGE_DICHOTOMY_512 remain unproved.

## 6. Exact mandatory controls, low cases and status

- **S018/S019 mixed heavy channels:** In a graph of pair cores, repeated multiplicity does NOT count as distinct singleton neighbours, nor can pair and singleton certifications imply EMPTY: mixed-star examples have nu(H)=3<m. The exact graph certificate separates these tests. Unselected optional heavy petals in A are harmless only because chosen reps have <=1 Q; gluing A and B is not asserted.
- **S022 light collisions:** Hall resolves third-label collisions for pair-core B REPRESENTATIVES only; it never claims whole-block safety. A-filter charges each selected light at original support load <=m once. No projective-plane light-pair with codegree m-1 is silently retained.
- **S023 nested q-plane:** all original blocks are A since each original block has one Q vertex; S028's H>=t/(3m²) applies. Its previously verified petal-first H on a single hub and denser S024 H_good survive; S023 whole-block BSEL negative remains.
- **S024 dense K_N pair graph:** with private third labels and one block per heavy pair, for N>=2m the H consisting of one representative per graph edge has a_uv=1, all positive degrees N-1>=m and nu(G)=floor(N/2)>=m. Thus all binom(N,2) selected triples pass EXACT pair/singleton/EMPTY certificates. This rules out star-only graph arguments.
- **m=2:** H=all original triples works for the entire original finite family, because each pair witnesses itself. **t=0:** H=empty. **1<=t<=512m³:** any ONE complete original block gives m>=t/(512m²) internally valid triples, so the hard frozen quantitative regime is t>512m³. The K_(m-1,m-1) negative has t_B=(m-1)^3<512m³ and is a method obstruction only. No uncontrolled enumeration or external experiment.

**Verdict:** A-mass original-two-heavy petal-first result PROVED SAME-ASSISTANT; exact B Hall graph certificate proved SAME-ASSISTANT; REP_ONLY_B_512 false via parametric symbolic certificate with a dense positive alternate; frozen complete two-original-heavy C512 UNPROVED / UNREFUTED, and all-k TIK/R3 still unproved. No new independent/original project paper theorem, source-intensive N1/N2, Lean, manuscript or external action. Mandatory fifth-session correction audit is NEXT standalone S030, NOT executed here.
