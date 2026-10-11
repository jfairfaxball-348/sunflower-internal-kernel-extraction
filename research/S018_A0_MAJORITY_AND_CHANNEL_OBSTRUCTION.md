# P001-S018 — quantitative pair-inactive majority and contaminated active-channel incompatibility

**S018 only, proof-first; same-assistant symbolic analysis, not independent mathematical verification.** The paper target remains EVERY fixed k, all m>=2, |H|>=c_k m^(-k)|F|, and every exact intersection of two distinct retained k-edges (including EMPTY) witnessed by m petals wholly IN H. R3, BSEL and the private-light two-original-heavy-support setting remain auxiliary. No full TIK proof, new source/open-status conclusion, originality, Lean, algorithmic-efficiency theorem or paper is claimed.

## Frozen ONE quantitative t-based inequality, prior to proof

Fix m>=3 and ANY finite edge-disjoint packing B_1,...,B_t of complete m-petal sunflower blocks of triples, each with exact core size 0,1,2. Set V_i=union B_i; fix the ORIGINAL Q={v: number of original blocks containing v >m}, with at most two Q vertices per V_i and every v outside Q block-private. A block i is **pair-active** when some triple of B_i contains two vertices of Q; otherwise i belongs to A0. These are S012's original A0 and Ae classes; they are NOT defined by the selected subfamily. Put a=|A0|.

**A0_MAJORITY_24 (frozen):** FOR EVERY such packing with a>=t/2 there is a subset J of COMPLETE original blocks with

    |J| >= t/(24*m^3),

and in the SAME selected H=union_(i in J) B_i, EVERY exact realised pair, singleton and empty kernel has m exact in-H petals. The rule must choose jointly between original-mandatory-Q-core groups and original-Q-optional weighted incidence skeletons, not lock a matching or preserve all original pair-active classes. Q is never recomputed.

We prove the stronger unconditional **A0_SUBMASS_12**, for every packing without a majority assumption,

    max_valid(J) >= a/[12*(m-1)^3] >= a/(12*m^3).

This is not a bound in terms of all t when a can be zero; A0_MAJORITY_24 follows by a>=t/2. The positive gate tackles singleton-core heavy blocks, pair-inactive empty-core blocks, pair-inactive optional-heavy support and Q-overlaps, but not general pair-active Ae interactions.

## S011 exact test, and disjoint split of A0

All selected blocks have complete in-H witnesses for their own original cores. Since A0 contains NO triple with two original Q vertices, a selection solely inside A0 has d_H(e)=m p_e+a_e=0 for every original-heavy pair e subset Q; any realised pair containing a light vertex is witnessed inside its sole block, by private-lightness. Remaining obligations are TRUE heavy singleton link matchings and empty.

Partition A0 into U and V by mandatory original core footprint C_i=K_i intersect Q:
- U comprises C_i={v} for some v in Q. Here EVERY triple of B_i contains v and NO triple contains any other Q: a second Q would make the block pair-active. Its original kernel is either {v} or {v,light}.
- V comprises C_i=empty, including all original empty-core blocks and every nonempty all-light core (possibly with one/two optional Q vertices in distinct petals). Each original Q vertex lies in at most one triple of each V-block, so selected v-residual pairs from different blocks are FREE and pairwise disjoint in light vertices. In every V-block at most two of the m petals meet Q, hence at least one **clean** triple using only block-private light vertices (m>=3).

These are the ONLY two cases in A0: a pair-inactive core cannot contain two hubs. Neither case restricts |Q|, hub degree, original core size among 0/1/2, nor the overlap graph.

## Branch U: exact singleton and empty tests with >=|U|/[m(m-1)]

Group U into disjoint full-block classes U_v by their mandatory hub v; put s_v=|U_v|. Form a **safe full class** T_v as follows:
- if U_v contains an original singleton-core {v} block, retain ALL U_v (that complete singleton-core block certifies v);
- else if s_v>=m, retain ALL U_v (one genuinely disjoint FREE residual pair can be chosen from each selected distinct block, and f_v=s_v>=m, D_v=empty);
- else if 1<=s_v<m retain exactly ONE arbitrary whole original block (v singleton then is absent unless its own kernel were {v}, excluded here).

Always |T_v|>=s_v/(m-1). In each class all selected triples contain v, so EMPTY is absent; only possible heavy singleton is v, certified as above; heavy-heavy pairs never occur; any realised light pair is an original core with its full m petals. Thus each T_v independently passes all THREE final tests.

Let q be the number of nonempty U_v. If q>=m, retain the UNION of all T_v. The mandatory hubs of these classes are distinct and there is no other Q in their supports, so one triple from each of m classes is an ACTUAL vertex-disjoint m-matching inside H: empty certified, and cross-group singleton/pair kernels do not arise except EMPTY. Retention >=|U|/(m-1). If 1<=q<m, retain a heaviest T_v, so |J_U|>=|U|/[q(m-1)]>=|U|/(m-1)^2>=|U|/[m(m-1)]. EMPTY is genuinely absent. If q=0 choose empty. Hence always

    |J_U| >= |U|/[m(m-1)]

with every realised pair, singleton and EMPTY certified in the selected union, not in the ambient family.

## Branch V: weighted optional-hub incidence graph with >=|V|/[6(m-1)^3]

For each i in V, form a graph edge representing its set S_i=V_i intersect Q of optional original heavy hubs: if |S_i|=2 join those hubs (parallel edges ALLOWED, each ORIGINAL block separately represented); if |S_i|=1 join the hub to a NEW dummy used by no other block; if |S_i|=0 join two NEW private dummies. This finite LOOPLESS multigraph G has exactly |V| distinct edges. The dummies are *graph-only*, not new ambient triple vertices. Original Q labels never change. For any selected V subcollection, the graph degree of v in Q is EXACTLY the number of selected blocks containing v (one optional v-triple per block). Each such block contributes one FREE residual pair at v, so the ACTUAL S011 singleton residual matching is f_v=deg_G(v), D_v=empty. For deg 0 or 1, singleton v is unrealised; for deg>=m it is realised and correctly m-matched.

**Degree-selection lemma, proved for arbitrary loopless multigraphs:** For m>=3, every E-edge multigraph has a nonempty (if E>0) edge subgraph S of size >= E/[6(m-1)^2] where every vertex has degree either 0,1 or >=m (edge multiplicity counted). Iteratively peel vertices of remaining degree <m, recording each removed edge once and orienting it outward from the vertex that caused its removal. Let C be the remaining m-core and R the peeled edges.
* If |C|>=E/2, keep C: every nonisolated degree is >=m; the edge bound follows.
* Otherwise |R|>E/2. Each peeling vertex emitted at most m-1 edges. Assign slots 1,...,m-1 to its outgoing edges; in each slot the resulting directed multigraph has outdegree at most one and hence its underlying graph is a pseudoforest (parallel two-cycles cause no problem). Properly 3-colour each slot pseudoforest. For each of the three HEAD colours, its directed edges form a disjoint union of stars: heads of that colour are centres, and each tail of another colour has at most one outgoing edge in the slot. Hence R partitions into at most 3(m-1) star forests. Keep a largest one, of size >E/[6(m-1)]. For each component star with d<m arms keep ONE arm; for d>=m retain all d. This loses at most a factor m-1 and yields |S|>E/[6(m-1)^2], with star-centres degree 1 or >=m and leaves degree 1. It is crucial that parallel ORIGINAL blocks are counted as separate graph edges, not collapsed into one neighbour-weight.

Apply the lemma to V. If |S|>=m, select all corresponding WHOLE original V-blocks. Each original heavy singleton is either absent (degree<=1) or has a TRUE free residual matching of size deg>=m; no heavy pair can arise, and light pair cores are automatic. EMPTY is certified by choosing one Q-free clean petal from each of m selected distinct V-blocks: their non-Q vertices are globally block-private and hence these m triples are ACTUALLY disjoint. If ANY selected original block is empty-core, its own m petals give the same conclusion. If 1<=|S|<m, choose ONE of its original whole blocks instead. Its only realised pair intersection is its original exact core, witnessed by that block's m petals, including the empty-core case. In this small-S branch |V|/[6(m-1)^2]<=|S|<m, whence 1>=|V|/[6(m-1)^3]. Thus in either case

    |J_V| >= |V|/[6(m-1)^3]

with all pair/singleton/empty tests valid inside the SAME H. E=0 gives the empty selection. No numerical search, randomness, global hub matching, or fixed matching backbone was used.

## Quantitative conclusion, all boundaries, and precise deficit

Choose the larger of the TWO fully certified selections J_U,J_V (not their unjustified union). For m>=3, m(m-1)<=6(m-1)^3, so

    |J| >= max(|U|/[m(m-1)], |V|/[6(m-1)^3])
        >= (|U|+|V|)/[12(m-1)^3]
        = |A0|/[12(m-1)^3]
        >= |A0|/(12*m^3).

When |A0|>=t/2 this proves FROZEN A0_MAJORITY_24: |J|>=t/(24m^3), with absolute 1/24 independent of Q,m,n,t. The literal integer inequality is maintained by choosing entire blocks. For t=0 choose J empty; for 1<=t<=3m^3 selecting one complete original block gives 1>=t/(3m^3). For m=2, original exact TIK uses H=F. This proof has not used an arbitrary original-Q m-matching, does not assume hub-disjointness, a bounded original heavy load, a single original core size or all-class retention.

As a further immediate **partial** estimate, let X_hh be the clean original pair-core blocks whose two core vertices BOTH lie in Q. Then X_hh lies outside A0, is disjoint from A0 and S017's clean-spine graph proof alone gives |J_X|>=|X_hh|/(6m^3). Choosing the better selection yields

    max_valid(J) >= (|A0|+|X_hh|)/(24m^3).

It is NOT the desired t bound: the pair-active remainder t-|A0|-|X_hh| still includes contaminated optional-heavy pair-core blocks, heavy-touching singleton/empty-core blocks, and noncore Ae with compressed short classes. S012 PAIR_FILTER still supplies >=t/(m-1) blocks with PAIR certificates only. No joint m^-2 loss for the leftover Ae classes is proved. The original exact data d_H(e)=m p_e+a_e, f_v+|D_v|, and disjoint mandatory original-Q footprints must all be recomputed after any choice. This is the FIRST remaining quantitative gap, not a proof-by-restatement of the full conjecture.

## New explicit contaminated-channel noncomposability, with DENSE valid control

For EVERY fixed m>=3 and arbitrarily large N>m, choose distinct original hubs a,b,c. For i=1,...,N create a complete m-triple pair-core block

    B_i^a = { {a,x_i,b} } union { {a,x_i,y_(i,j)} : 1<=j<=m-1 },

and a disjoint symmetric block

    B_i^c = { {c,z_i,b} } union { {c,z_i,w_(i,j)} : 1<=j<=m-1 }.

All x_i,z_i,y_(i,j),w_(i,j) are distinct private light vertices. The exact original cores are {a,x_i} and {c,z_i}; the b-containing petals are genuinely OPTIONAL original-heavy contamination. Every block has precisely two Q vertices in full support, Q={a,b,c} since r(a)=r(c)=N>m and r(b)=2N>m; no light vertex occurs in two blocks. The packing is edge-disjoint, t=2N, |A0|=0, W=Z=0 and |X_hh|=0. Original pair-active classes A_{ab} and A_{bc} each have N noncore members, are saturated by N>=m true third vertices but contain NO pair-core block with core {a,b} or {b,c}. Thus ordinary S012 PAIR_FILTER retains both entire classes.

Each single class ALONE is a fully internally valid N-block selection: the original light-containing 2-cores have exactly m in-H triples; its heavy pair {a,b} (or {b,c}) has N in-H third vertices; its heavy singleton a (or c) has f=N genuinely disjoint FREE residual petals and D=empty; b singleton is UNREALISED because all b-containing triples in that one class also contain a (or c); every triple meets the fixed core hub, so EMPTY is UNREALISED.

But their UNION is **NOT** internally valid, despite both heavy-pair tests being correct: d_H({a,b})=N>=m and d_H({b,c})=N>=m. For a and c, true singleton matching N>=m. Heavy singleton {b} IS realised between an a-block b-petal and a c-block b-petal, while its entire residual link consists of stars with centres a and c, so f_b=0, D_b={a,c}, and nu(H({b}))=2<m. EMPTY is also realised by taking an a-side and c-side triple with disjoint private lights; every triple contains a OR c, so its actual full triple matching number is exactly 2<m. There is no original empty-core block, and mandatory original-Q footprints are only {a} and {c}, so the disjoint-core maximum is 2. Pair, singleton and empty tests have thus been calculated on the SAME actual union. This refutes naive composability of independently certified *PAIR-ACTIVE* Ae class extractions, NOT the frozen A0-majority implication (its hypothesis fails), and NOT absolute gamma/BSEL/R3/TIK.

**Dense control:** select all N original B_i^a and no c-side blocks. Then |J_good|=N=t/2; its pair kernels {a,x_i} and {a,b} have m and N witnesses, true singleton a has f_a=N, singleton b is absent, and empty is absent. This is a full TRUE whole-block valid selection. In particular max_valid*m^3/t >=m^3/2 for every N; no fixed-m vanishing-ratio obstruction to gamma has been produced. This example is new relative to S014/S015's saturated ORIGINAL e-core class-preservation failures, S016's prescribed matching budget and S017's benign one-heavy singleton-core W=Z=0 control: its original pair cores are heavy-light, its incompatible pair classes are saturated solely by one contaminated petal PER block, and both singleton and empty matching fail when independently valid heavy-pair channels are united.

## Scope and unchanged inherited results

S006 disjoint-support gamma=1 and S007 low-load gamma=1/3 persist. S008/S009 full-valid high-load controls, S010/S011 >=half-density controls and S011 exact structural identities, S012 PAIR_FILTER, S013 protected A0, S014/S015 class failures and 15th audit, S016 fixed-backbone failure with dense alternative, S017 SAFE_SPINE(12) all remain intact. The next mandatory fifth-child audit is S020, NOT S018. No exhaustive search, numerical solver, palette, Lean, N1/N2, originality promotion, manuscript or external action. All present mathematics is SAME-ASSISTANT and structural hosted CI tests are NOT independent mathematical proof review. No absolute gamma for the arbitrary private-light slice, universal BSEL, R3, or full every-fixed-k TIK is proved or refuted. Parent mathematical S001 is UNEXECUTED. One future standalone S019 handoff ONLY; it is NOT executed.
