# P001-S039 — Hybrid partial-palette extraction, exact kernel atlas and a genuine intermediate-multiplicity HDSE3 family

Date: 2026-10-12. Proof-first, symbolic, **same-assistant only**, no new experiment and no independent mathematical or novelty review. The exact incoming owner message was separately archived (commit `8d5aef0`), hashed in a second commit (`d63224b`), and the scope was frozen in `3e65319` BEFORE this report. References to S033's rank-two constant are CONDITIONAL on that earlier same-assistant proof. HDSE3, R3 and full every-fixed-k TIK remain **UNPROVED**.

## 1. Complete exact 2+1-partite kernel atlas (no common-palette assumption)

Let V,Z be disjoint and H be any triple family each of whose edges uses two vertices of V and one of Z. For each z in Z let G_z be the simple graph on V whose edges uv correspond to triples uvz in H. Write q_H(uv)=|{z:uv in G_z}|. For each u in V form the bipartite graph B_u with left neighbours v in V\{u}, right palettes z in Z and edges (v,z) iff uvz in H. All graphs and matchings here are formed from **final H**, never the ambient E.

**Theorem A (exact atlas).** H is internally m-valid if and only if the following five tests hold:
1. For every base pair uv, q_H(uv) belongs to {0,1} union [m,infinity).
2. For each z,u, d_{G_z}(u) belongs to {0,1} union [m,infinity).
3. For each z, matching number nu(G_z) belongs to {0,1} union [m,infinity).
4. For each u, matching number nu(B_u) belongs to {0,1} union [m,infinity).
5. The global triple matching nu(H) belongs to {0,1} union [m,infinity).

*Proof.* Two distinct triples uvz and u'v'z' have exactly five possible nontrivial exact intersection kinds. Identical uv with different z yields PAIR {u,v}: its exact residual singleton link size is q_H(uv). Distinct base edges sharing u with the SAME z yield PAIR {u,z}, whose residual singleton link size is d_{G_z}(u). Disjoint base edges with the SAME z yield SINGLETON {z}, whose residual two-set link matching is nu(G_z). Distinct base neighbours AND distinct palettes at a common u yield SINGLETON {u}, whose residual link matching is nu(B_u). Disjoint triples yield EMPTY with residual matching nu(H). The analogous mixed pair {v,z} is included by changing u. Each kernel is realised iff its displayed count/matching is at least 2, and each needs at least m internally selected petals iff that count/matching is at least m. No other exact intersections exist. This includes the EMPTY kernel and DOES NOT require the intersecting pair to be among its witnessing petals. QED.

This is stronger in scope than S037's pair-core/one-shared-palette special test: arbitrary overlapping V base edges and edge-dependent Z_uv are allowed. It is an elementary structural tool, not an independently novel theorem.

## 2. A complete phase diagram and extraction bound for intermediate palette sizes

Let G be any finite simple graph on V and Z disjoint with q=|Z|>=1. The COMPLETE rank-three tensor E=G x Z consists of triples uvz for all uv in G and z in Z.

**Theorem B (validity phase transition).** For nonempty G and m>=2:
- q=1: E is internally m-valid iff G is internally m-valid;
- 2<=q<m: E is ALWAYS internally m-invalid, regardless of G;
- q>=m: E is internally m-valid iff G is internally m-valid (S038 tensor theorem).
The middle interval is empty for m=2. Empty G gives the empty, vacuously valid tensor for all q.

*Proof.* For q=1, the only realised intersections between two distinct tensor triples all include z, and correspond exactly to pair intersections of their two-set bases; a sunflower in E is the corresponding base sunflower with z appended. If 2<=q<m, each original base edge uv gives q distinct triples with realised exact PAIR {u,v}; its residual singleton link is q<m, so E is invalid. For q>=m, use the S038 tensor equivalence (or check Theorem A: q on base pairs; d_G at mixed pairs; nu(G) at z and EMPTY; min(d_G(u),q) for B_u). QED.

**Theorem C (all-q quantitative extraction).** For all m>=2 and all nonempty G x Z, there is internally valid H subset E with
|H|/|E| >= 1/[8 m^2 min(q,m)] >= 1/(8m^3).
More sharply, if q>=m the ratio is >=1/(8m^2).

*Proof.* By S033's same-assistant graph theorem choose internally m-valid G' subset G with |G'|>=|G|/(8m^2). If q>=m, H=G' x Z is valid by S038 and retains the same graph fraction >=1/(8m^2). If 1<=q<m, fix one palette z0 and take H=G' x {z0}; the q=1 case of Theorem B shows validity, and |H|/|E|=|G'|/(q|G|)>=1/(8qm^2). Since q<=m-1, this exceeds 1/(8m^3). For m=2 either choice works, and in fact H=E works for every input. QED.

**Critical limit.** A single q<m complete tensor can never itself be a nonempty 6m-spread family, since an original pair uv has q edges and |E|=q|G|, so the palette vertex z has degree |G|=|E|/q >|E|/(6m). It can still occur as a *local component* inside a globally spread E. This is why Theorem C does NOT resolve HDSE3 by itself.

## 3. Genuine high-degree spread, core-free, intermediate-multiplicity control — disjoint private palette per spoke

For every integer m>=3 set r=216m, L=m^3+1 and q=m-1. For i=1,...,r take a private hub x_i and private leaves a_{ij} (j=1,...,L). Crucially, for **each separate spoke (i,j)** introduce q globally private palette points z_{ijt}, t=1,...,q. Define ORIGINAL
E_m={ {x_i,a_{ij},z_{ijt}}: 1<=i<=r,1<=j<=L,1<=t<=q }.
There are |E_m|=rLq original triples. The palette points for DIFFERENT j are distinct: this avoids disguising a saturated common tensor under a change of base/palette orientation.

**Proposition D.** E_m is nonempty, 6m-spread, robust-core-free and high-degree dominated (HDSE3). Each original edge meets a SAME-E hub of degree Lq>m^3. Its only repeated original pair is {x_i,a_{ij}}, of exact codegree q=m-1 in {2,...,m-1}; every original pair has degree <m. Thus E_m contains NO nonempty full >=m-palette tensor in ANY choice of base/palette coordinates. E_m itself is NOT m-valid, but the SAME ORIGINAL E_m contains
H_m={ {x_i,a_{ij},z_{ij1}} : 1<=i<=r,1<=j<=L }
which is internally valid with |H_m|=rL and exact density 1/(m-1).

*Proof/census.* In ORIGINAL E_m, deg(x_i)=Lq, deg(a_{ij})=q, deg(z_{ijt})=1. Its maximum pair degree is q at {x_i,a_{ij}}; all other pair degrees are 1. Every triple occurs once. Hence the spread ratios at singleton/pair/triple levels are exactly
1/r <=1/(6m),
1/(rL) <=1/(36m^2), and
1/(rLq) <=1/(216m^3).
The second holds because rL=216m(m^3+1)>=36m^2 and the third because Lq>=m^2. The SAME ORIGINAL hub degree Lq=(m^3+1)(m-1)>m^3 for all m>=3. Each triple contains {a_{ij},z_{ijt}} of ORIGINAL pair-degree 1<m, excluding it from any nonempty robust subfamily; therefore robust core is empty. Since ALL E_m pair degrees are <m, any hypothetical nonempty G x Z with |Z|>=m would force some base pair to lie in >=m E_m triples, contradiction. Original E_m is invalid: for every i,j, q=m-1>=2 triples realise exact pair {x_i,a_{ij}} but its original/selected link has only q<m palette petals.

In SELECTED H_m, two triples within one hub i have distinct j and intersect exactly in singleton {x_i}, whose residual link has L>=m mutually disjoint pairs {a_{ij},z_{ij1}}. Triples from different hubs are disjoint; choose one triple from each of r>=m hubs for a true H_m-matching witnessing EMPTY. The realised kernels are ONLY these singletons and EMPTY; no selected pair kernel is realised. Thus H_m is internally m-valid. Its density is rL/(rLq)=1/q. At m=3, q=2 is the first genuinely intermediate class; at m=2 no intermediate class exists and arbitrary F is trivially 2-valid. QED.

This strengthens S038's *linear* HDSE3 no-tensor control by creating many repeated but unsaturated original pairs. It defeats the helper "all original repeated pairs can first be promoted to >=m saturated tensors" but does NOT refute HDSE3: the same family has a 1/(m-1)-density selected repair.

## 4. Exact disjoint-support aggregation (thick palettes)

Let E be a disjoint union of r>=1 nonempty complete graph/palette tensors E_i=G_i x Z_i, with pairwise disjoint ALL vertex supports and q_i=|Z_i|>=m. Write N=|E|. Select in each component H_i=G_i' x Z_i via S033/S038, so H_i is internally valid and |H_i|>=|E_i|/(8m^2).

**Theorem E.** E admits internally valid H with |H|>=N/(8m^3).
If r>=m, the union H=union_i H_i is valid and |H|>=N/(8m^2). Within a component, all kernels are certified by its own H_i. Across components, EMPTY is the ONLY intersection and an m-matching comes from one selected edge of each of m components.
If 1<=r<m, take H_i for the largest original |E_i|>=N/r: it is valid and retains >=N/(8rm^2)>N/(8m^3). No crossing kernels are introduced.

**General gluing rule.** For any pairwise vertex-disjoint nonempty, internally m-valid H_i (not necessarily tensors), union H_i is valid iff r=1 OR the TRUE global matching sum_i nu(H_i)>=m. When r>=2, EMPTY is realised by edges in different components, and the global matching equals that sum; every nonempty exact intersection stays within a component. This rule quantifies the failure of naive independent slice gluing in the regime 2<=r<m.

**Thin-palette arithmetic warning.** Replacing each q_i>=m product extraction by the one-palette thin extraction incurs 1/q_i. For r<m, picking one cluster now proves only N/[8r q_max m^2], potentially O(N/m^4), not the desired uniform N/m^3. It is NOT a counterexample to HDSE3, merely an honest remaining simultaneous-selection/matching mechanism gap. For r>=m, all one-palette components can be unioned and give >=N/(8m^3) directly.

## 5. Adversarial incompatible individually valid fibres and SAME-E repairs

**Singleton collision.** Fix m>=3, a common base hub u, two distinct palette points z_1,z_2, and disjoint groups of m base leaves a_1,...,a_m and b_1,...,b_m. Let
E={u a_j z_1 : j<=m} union {u b_j z_2 : j<=m}.
Each of its individual z-fibres is an internally valid m-star (all intersections are PAIR {u,z_i} with m selected petals). Every base pair has q=1, and every mixed pair condition is good. Yet E is INVALID at exact SINGLETON {u}: B_u consists of two m-edge stars on palette side, with matching exactly 2<m. Its true link has no third palette. The SAME E contains the valid first fibre H of size m=|E|/2; the failure does not refute density. EMPTY is never realised.

**Empty collision.** Let E be two vertex-disjoint complete m-edge {u,z}-pair stars (the same two local patterns but on disjoint vertex supports). Each fibre is valid; their union realises EMPTY and has global matching number exactly 2<m for m>=3. Choosing one star gives valid |H|=|E|/2. This demonstrates the necessity of the last atlas/gluing condition independently of the mixed-singleton obstruction.

**Pair collision.** S038's single missing incidence and the full q=m-1 rectangle show that individually acceptable base-graph selections can fail at realised base PAIR even when every other link is healthy. Theorem A records the correct q_H(uv) 0,1,>=m threshold; a global colour-count average alone is insufficient.

## 6. Multi-front outcome / exact unsolved quantifier

Successful: (i) a complete five-test arbitrary palette-fibre iff; (ii) all-q full-tensor extraction with a sharp validity-phase gap for 2<=q<m; (iii) a SAME-E positive HDSE3 example with genuine original intermediate q=m-1 pairs, strict high-degree and spread, no large tensor; (iv) disjoint-support thick-product m^-3 aggregation and its exact compatibility obstruction.

Attempts NOT completed: deriving a constant-density hybrid *cover* of an arbitrary HDSE3 E by compatible complete rectangles, disjoint local stars and fibre repairs. Neither 6m-spread, core-freeness nor >m^3 SAME-E vertices implies any mass in such a cover. Theorem A gives exact local constraints but no rounding/selection inequality for arbitrary palette incidence systems.

**FIRST MISSING UNIVERSAL IMPLICATION:** For every m>=3 and every nonempty 6m-spread, core-free triple E with each edge incident to a vertex of SAME-E degree>m^3, construct a final-H family satisfying the five kernel tests (or an equivalent general exact-kernel certificate) and |H|>=c_H |E|/m^3 with c_H absolute. A genuine negation must have m^3 max_valid_m(E_m)/|E_m| ->0; none of the examples here or in S038 achieves that. Even HDSE3 would imply only rank-three R3 via S033/S036; the every-fixed-k TIK target would remain independently unproved.

All source/novelty classifications, formal and publication statuses remain unchanged. No N1/N2, Lean, Palomar, correspondence, submission or manuscript. S040 is a FUTURE fifth/tenth correction/strategy audit, not executed in S039.
