# P001-S030 — collision-aware compulsory-two-heavy extraction gate

**2026-10-11, one bounded proof-first session.** Literal fresh owner message archived BEFORE replacing NEXT at `fc7d32642815bf04fb8873ec4d5e30b2378e9403`, 121 UTF-8 bytes, independently computed SHA256 `653bdbeaa99d0835ef42fc2506ae4e0fd5407439947c078e071fef95ac168b1a`. Frozen universal C=512, exact support population and mandatory fifth audit at `f92963f361192bb5f849fe0d443f1f2477990f01` BEFORE this report. All mathematical proofs/certificates below are **same-assistant symbolic**, not independently refereed, computational, novel or formal. No enumeration/search/experiment run.

## 1. Quantifiers and precise deficit

For m>=3 and t>=1, take t edge-disjoint COMPLETE original m-petal 3-sunflower blocks B_i of exact core size 0,1,2; their ORIGINAL full supports S_i determine r(x)=#{i:x in S_i}, Q={x:r(x)>m}. Fix Q and t. Every S_i meets Q in at most two labels, all non-Q labels belong to <=m original supports. Frozen numerical target: individual-edge H from their union with |H|>=t/(512m²) and every realised exact kernel of any two final H triples (two-point, singleton, EMPTY) witnessed by an actual m-petal sunflower **within H**. The witnessing pair is not required to be the selected intersecting pair.

S029 A={blocks admitting some <=1-Q petal} gives |H_A|>=|A|/((3m-2)(m-1))>=|A|/(3m²). Hence if |A|>=t/2 frozen C512 is achieved. For B=[t]\\A, every original block is pair-core {u,v} with u,v in Q and m distinct light thirds. If |B|>=t/2, it is enough to prove a B-only selection |H_B|>=|B|/(256m²). NEVER combine independent A and B outputs without checking all new final-H kernels. This report does not establish that B-only bound in full.

## 2. Hall injection and exact representative semantics

For every B block choose one of its m original third labels; any light label belongs to at most m ORIGINAL block supports. For T subset of B blocks, m|T| incidences into their possible light labels and at most m incidences per label imply |N(T)|>=|T|. Hall grants an injection z_i (one third for each B block). Any selected representative triple {u_i,v_i,z_i} therefore has a globally distinct light label. Let G be the simple selected Q-pair graph and a_uv the number of selected representatives for pair uv. Exactly:

* A realised pair kernel uv iff a_uv>=2, requiring a_uv>=m.
* A realised singleton q iff its number of DISTINCT neighbours in G is >=2, requiring deg_G(q)>=m: residual link matching number is that SIMPLE degree, not sum a_qv.
* EMPTY realised iff nu(G)>=2, requiring nu(G)>=m; graph matching and triple matching coincide because thirds are injected.

Thus selected a_uv must be 0,1 or >=m; selected graph degrees 0,1 or >=m; and nu(G) 0,1 or >=m. These tests apply ONLY to injected one-petal representatives, not to later full-petal lifts.

## 3. Positive weighted-star selection: |H_q| >= W_q/(m-1)

**Lemma (S030, proved symbolically).** Let w_qv be original B-block multiplicities, and W_q=sum_v w_qv. For every q incident to at least one B block there is an internally m-valid H_q entirely from B with |H_q|>=W_q/(m-1), no need for block-private light.

Let d be the number of DISTINCT neighbours v with w_qv>0. If d>=m, take for every pair with 1<=w_qv<m EXACTLY ONE injected representative, and for every pair with w_qv>=m ALL w_qv injected representatives. Each retained pair has codegree 1 or >=m. Its only possible singleton is {q}, and its residual link has a matching of d>=m pairs on distinct v and distinct injected z. Every triple contains q, so EMPTY does not occur; there are no other singleton/light-pair kernels. The edge count is at least sum_v w_qv/(m-1)=W_q/(m-1), because 1>=w_qv/(m-1) in the short classes.

If 1<=d<m, choose a pair qv of largest weight w*=max_v w_qv >=W_q/d >=W_q/(m-1). If w*>=m, retain the w* injected representatives on that pair: exact common core {q,v}, codegree w*>=m, no singleton or EMPTY. If w*<m, choose all m petals from ONE original qv block. Its common exact pair is internally certified and m>w*>=W_q/(m-1). The bound follows. For W_q=0 the empty result is vacuous. This lemma is a genuine multi-petal selection in its small-class branch.

**Immediate quantitative regime:** if some q has W_q>=|B|/(256m), the S030 B-only numeric threshold follows. No interpretation of light loads as selected degree is used.

## 4. Positive dense SIMPLE-graph 2m-core selection

**Lemma (S030, proved symbolically).** Let C be any nonempty induced or edge subgraph of the simple original B pair graph with minimum positive degree >=2m, and T_C=sum_(uv in E(C)) w_uv. Keep exactly one Hall-injected representative from each short pair 1<=w_uv<m, but all w_uv representatives of saturated pairs w_uv>=m. This gives |H_C|>=T_C/(m-1). Pair kernels are codegree 1 or >=m, every realised heavy singleton has >=2m DISTINCT neighbours with distinct third labels, and no light singleton/pair is realised.

For EMPTY, any graph of minimum degree >=2m has matching number >=m. Otherwise endpoints of a maximum matching of size <=m-1 give a vertex cover of at most 2m-2; a vertex outside the cover must have all neighbours inside it, contradicting its degree >=2m (there must be an outside vertex since min degree demands at least 2m+1 vertices). Hall injection converts a graph m-matching to m pairwise disjoint selected triples. All actually realised 2/1/EMPTY kernels therefore have internal witnesses. In particular if the 2m-core of the original pair graph carries T_C>=|B|/2, the S030 B-only target holds with room to spare, as |H_C|>=|B|/[2(m-1)].

No assumption that original w_uv itself counts as a singleton matching degree has been made.

## 5. Another genuinely covered regime: small heavy-pair matching number

Let nu be the matching number of the SIMPLE original B pair graph. If nu<m, endpoints of any maximal matching (size at most m-1) form a vertex cover of size <=2(m-1). Each B block meets that cover, hence some q in it has W_q>=|B|/[2(m-1)]. The weighted-star lemma gives

    |H_B|>=|B|/[2(m-1)^2] >=|B|/(2m²) >=|B|/(256m²).

If instead nu>=m AND nu>=|B|/(256m²), take one Hall-injected representative corresponding to each pair in a maximum simple graph matching. These nu triples are pairwise disjoint, so EMPTY is their sole realised intersection and the same >=m triples witness it. Thus this also meets the numerical bound. The hard residual regime requires nu>=m but nu<|B|/(256m²).

## 6. FIRST false shortcut: Hall injectivity does NOT license complete-petal lifting

For EVERY m>=3 and d>=m, take one hub q and d neighbours v_1,...,v_d. For every i create m+1 distinct original m-petal pair-core blocks with core {q,v_i}; all their third vertices private EXCEPT a single label z occurring in exactly one petal of one qv_1 block and one petal of one qv_2 block. No triple repeats. Original support loads: r(q)=d(m+1)>m, r(v_i)=m+1>m, r(z)=2<=m, all other thirds load 1; therefore ORIGINAL Q={q,v_1,...,v_d}, every original B block meets Q in exactly two hubs, and t_B=d(m+1). Both occurrences of z can be avoided by selecting a different private third in each of the two affected blocks. This produces Hall-injected representatives globally distinct in light, with a_qv_i=m+1>=m for every pair, degree_G(q)=d>=m and nu(G)=1. The resulting H_rep of exactly t_B edges is genuinely internally valid (pair cores and singleton q pass; EMPTY absent).

**FALSE LIFT_ALL:** replacing those valid representatives by ALL m petals of EACH corresponding original block preserves internal validity. The lifted H_full contains {q,v_1,z} and {q,v_2,z}, intersecting in exact pair {q,z}. Its exact H_full({q,z}) has ONLY the two distinct thirds v_1,v_2, so codegree=2<m; the lifted family is INVALID, despite original Hall injectivity and the entirely valid weighted star representatives. This is a parametric original-two-Q obstruction to blindly multiplying representative mass by m in a pair-core proof. The SAME original F has valid H_rep with d(m+1) edges and valid H_pair consisting of all m(m+1) petals on core {q,v_1}. Both exceed d(m+1)/(256m²) (H_rep already equals t_B). The example does not disprove C512.

At d=m, all original r(v_i)=m+1 and z load two; at literal m=3 the offending H_full pair {q,z} has only 2<3 witnesses. No search was needed.

## 7. Exact uncovered step and a quantified dense valid alternate

The three covered B regimes (one big weighted star; sufficient 2m-core mass; or matching big enough) do NOT yet give a universal B lower bound. The first **UNPROVED** step is a quantitative collision-aware multi-petal *assembly across the peeled (<2m-degenerate) residual graph*, when its original block weight is large but no single star or simple matching contains t_B/(256m²) representatives. S029's REP_ONLY_B_512 is already FALSE and cannot supply this step; lifting complete blocks is separately FALSE as shown above.

To show the remainder is not merely empty, fix m>=3, r=N=1024m, and take r disjoint copies of K_(m-1,N) as heavy pair graphs. For EACH graph edge create w=m-1 complete original m-petal pair-core blocks with globally private light labels. Then t_B=rN(m-1)^2. Each centre on the m-1 side belongs to N(m-1)>m original supports; each leaf on the N side belongs to (m-1)^2>m supports for m>=3, so Q comprises all graph vertices exactly. Original 2m-core is EMPTY (leaf degree m-1<2m). The simple pair matching number is nu=r(m-1), while

    [t_B/(256m²)] / nu = N(m-1)/(256m²)=4(m-1)/m >1.

The largest W_q is N(m-1) at a centre; the proven star bound W_q/(m-1)=N, yet

    [t_B/(256m²)]/N = 4(m-1)^2/m >1.

This refutes a **specific naive sufficient assertion**: simply taking the largest of the NUMERIC guaranteed star output, simple-matching output and 2m-core output always meets the B target. It does **NOT** upper-bound every possible star selection or disprove the full B target.

Indeed in the SAME ORIGINAL FAMILY choose ONE centre in each of the r components and ONE Hall-injected representative from each of its N distinct leaf pairs. Private light labels and disjoint component Q vertices yield a star forest of r components, each with centre degree N>=m, each pair multiplicity one, and global graph matching >=r>=m, so all realised singleton and EMPTY kernels have true in-H m-witnesses; no realised 2-point pair. This H_good contains rN edges, strictly larger than t_B/(256m²). Moreover entire pair blocks may also be exploited because light here is private. Thus the example is a METHOD obstruction and a dense positive control, not a counterexample to C512.

The desired missing lemma needs to charge the peeled graph at O(m²) original-B-blocks per kept individual edge while assembling several centres, maintaining exact residual singleton degrees and either avoiding EMPTY or producing m disjoint heavy cores, AND controlling repeated light if any whole-petal blocks are retained. Neither the Hall graph criterion nor the two positive lemmas above proves such a universal assembly. **Full two-Q C512 remains UNPROVED/UNREFUTED**; no mathematical theorem for all three-Q supports, R3, or full every-fixed-k TIK.

## 8. Mandatory adversarial controls and boundaries

* S018/S019 contaminated optional hubs and mixed stars: independent pair/singleton certificates do not imply EMPTY; S019 actual empty matching 3<m. Our weighted-star selections have universal common q, so EMPTY absent; our 2m-core selection explicitly proves graph m-matching; the disjoint component control explicitly has r>=m matching. NO unverified union of competing channels.
* S022 repeated-light families: Hall injection resolves ONLY ONE label per original block. LIFT_ALL above shows why optional petals can create pair {q,z} with codegree 2; S022's light-pair/empty negative controls stay in force.
* S023 complete nested q-plane is in A (one original Q per block), with established S028 partial-petal >=t/(3m²) and S024 exact optimum, despite FALSE universal whole-block BSEL; no replacement of its restricted proof by this B graph analysis.
* S024 dense K_N private-third pair graph (N>=2m+1): min degree N-1>=2m and graph matching floor(N/2)>=m, so H_C includes one representative on each pair and certifies all 2/1/EMPTY kernels. This protects high-degree graph cores against unjustified star-only pruning.
* S029 K_(m-1,m-1) w=m-1 controls: simple nu=m-1<m, so the new *small-matching* lemma applies. Full original m(m-1) petals on any one pair are valid, while only one selected representative can survive under REP_ONLY_B conditions. The present proof does not relabel REP_ONLY as valid.
* Literal m=2: for arbitrary original packing union F, every two distinct final triples themselves are a two-petal exact sunflower with their own intersection, so H=F. Literal t=0: take empty H. For m>=3, 1<=t<=512m³, ONE complete original block with m petals suffices since m>=t/(512m²). Stronger A/B lemmas do not need this fallback except in their described short cases.

No numerical search; the finite-parametric populations, symbol counts, original loads, explicit formulae, and H certificates are symbolic. No new detailed N1/N2, originality claims, independent external proof review, Lean, manuscript, outreach, parent mathematical S001, or P001-S031 execution. See separate mandatory S030 correction audit.
