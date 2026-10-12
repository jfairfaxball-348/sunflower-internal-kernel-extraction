# P001-S039 — adversarial second pass from exact link semantics

**Scope.** This is a new same-assistant reconstruction after the proof report was committed, not independent expert review or formal verification. A correction was made to the first submitted draft of Proposition D: a SHARED z_it palette for all leaves would hide a saturated tensor after relabelling, invalidating the asserted "no full tensor" claim. The corrected committed report uses globally private z_ijt per SPOKE and is stress-tested below. This transparent counterexample-to-our-own-intermediary is preserved, not silently forgotten.

## I. Census re-derived from first principles

Let H be any 2+1-partite selected hypergraph. For distinct triples:
- same base edge, distinct colours => pair uv; its link has q_H(uv) isolated singleton petals;
- same colour and overlapping base edges => mixed pair uz and degree d_Gz(u);
- same colour and disjoint base edges => singleton z, matching nu(G_z);
- different colours and distinct base-neighbours at u => singleton u, whose link is the bipartite B_u and whose disjoint petal matching is nu(B_u);
- completely disjoint triples => EMPTY and global nu(H).
These are disjoint intersection categories, and every incidence in each counted link is an actual triple in H. Realisation is value >=2; exact m certification is value >=m. Accordingly the five 0/1/or >=m tests are individually necessary and jointly sufficient. No kernel witnessed in original E but not H is counted. The m=2 case permits value2 so every family is valid.

## II. Tensor proof recomputed and role of q

For a single colour, triple (uv,z) has intersection (uv intersect u'v') union {z}; exact kernel and matching requirements coincide with graph validity, INCLUDING graph EMPTY mapping to selected singleton {z}. For 2<=q<m, choose ANY graph edge uv and two palette colours: pair uv is realised, q<m original tensor extensions => invalid no matter whether G is a valid graph. For q>=m the S038 theorem restores validity iff graph validity. The selector G'×{z0} has |G'|/(q|G|)>=1/(8qm²) if q<m; G'×Z has |G'|/|G|>=1/(8m²) if q>=m. Therefore uniform 1/[8m² min(q,m)] is exact as a **proved lower bound**, not a claimed optimal density. For q=1 and q=m there is no gap.

An original single full tensor with q<m is not 6m-spread since deg_E(z)=|G|=|E|/q>|E|/(6m); this is why local unsaturated tensors in a MANY-component / edge-dependent palette regime cannot be promoted to a universal HDSE3 theorem.

## III. Recalculation of the corrected non-tensor HDSE3 model

Input at m>=3: r=216m hubs, L=m³+1 leaves/hub, q=m-1 private palette points PER leaf; |E|=rLq. The only repeated original pair is (hub,leaf) with d_E=q<m. In particular no pair has >=m extensions, so there is NO nonempty full >=m product in ANY orientation: a product base edge would violate that maximum codegree. Original degrees: hub Lq, leaf q, palette vertex 1. Maximum vertex =Lq; maximum pair=q, every triple degree1. Divide by |E|: 1/r, 1/(rL), 1/(rLq); compare to (6m)^-1,(6m)^-2,(6m)^-3 respectively. All pass for m>=3. Hub degree Lq>m³ proves the required ORIGINAL (not selected) high-degree condition. The robust core is empty because EVERY edge has at least one proper pair with ORIGINAL degree1, hence any robust selected subfamily would have too small a link there.

Original E invalid: q=2,...,m-1 extensions of each hub-leaf pair. Selected H uses a single chosen palette vertex from each spoke, for all rL spokes. Two H triples at the same hub involve DIFFERENT leaves and different private palette vertices, so exact kernel is singleton hub (NOT the PAIR incorrectly claimed by the uncorrected draft); the residual L edges are disjoint and L>=m. Cross-hub triples have EMPTY and r>=m disjoint petals. No other pair exists. |H|/|E|=1/q. Both ORIGINAL and SELECTED bounds are algebraic for all m>=3. No finite enumeration performed. At m=3: q=2, L=28, r=648; inequalities hold by the symbolic formulas.

The original draft's shared-palettes choice had deg_E(hub,palette)=L>=m, allowing a full tensor on graph edges (hub,palette) and leaf palette of size L. The revised per-spoke palette fixes this exact loophole. The family remains a HIGH-DEGREE spread positive control and is NOT a theorem counterexample.

## IV. Aggregation and two independent collision mechanisms

Disjoint-support H_i have nu(union H_i)=sum nu(H_i). For >=2 nonempty components EMPTY is necessarily realised and needs that total >=m. All other intersections stay componentwise, so this is an iff under individually valid inputs. For >=m thick rectangles, choose 1 edge/component as witnesses for EMPTY, retain sum |E_i|/(8m²). For fewer than m components, choose the heaviest complete thick tensor (no realised EMPTY outside); ratio >=1/[8(m-1)m²] >1/(8m³). No unsupported simultaneous-witness argument is used.

The two same-E collision controls have distinct defects:
- two different palette stars around SAME base hub each of size m: fibre PAIR links have m and are valid, but selected B_hub matching is exactly 2<m, so singleton hub fails; all triples share hub, so EMPTY does not arise; choosing one fibre gives 1/2 valid fraction;
- two vertex-disjoint such stars: each component valid, union global matching exactly2<m, so EMPTY fails; no mixed-hub singleton issue, and one component provides 1/2 valid fraction.
Both require m>=3. For m=2 their union is automatically valid. No false universal HDSE3 or rank-three disproof is inferred.

## V. Quantitative review and end frontier

The positive density bounds 1/(8m³) cover arbitrary complete graph×palette products (all q) and disjoint unions of thick products. The private-spoke HDSE3 example has density 1/(m-1), so m³ max_valid(E)/|E| >=m³/(m-1) rather than tending to zero. The gluing examples have selected fraction >=1/2. None of these is a counterexample to HDSE3 or TIK. Conversely no theorem forces a constant proportion of arbitrary 6m-spread core-free high-degree E into the covered structural classes, and the atlas is a test rather than an extraction algorithm.

S033 graph constant and rank-three equivalence remain same-assistant assumptions, not an independent check. Full every-k TIK, R3, HDSE3 and all-m C512/B256 remain unproved. Novelty unchecked, no experiments, no Lean, no publication. Mandatory S040 progress/correction and tenth-session strategy audit is FUTURE ONLY.
