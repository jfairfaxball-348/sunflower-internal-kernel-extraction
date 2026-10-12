# P001-S031 — sparse weighted multi-star assembly and its remaining m loss

**2026-10-12; ONE bounded proof-first gate.** The exact 126-byte owner invocation has SHA256 `f19536cc72c22ee3417531f9327f1cf9477ecb1123539be080b2546ca73b172b`, checked separately by hashlib and sha256sum. Archive remote commit `1da15440c3e2815f83cf512a4e866e6b4de96fb7` precedes frozen gate remote commit `59d9c0986527d0fdb64cc036553721f88792faed`, which precedes this report and NEXT replacement. Local preliminary archive/freeze hashes are recorded separately, not substituted for remote hashes. All mathematics here is SAME-ASSISTANT symbolic reasoning, not independent mathematical review, novelty clearance or formal verification. No mathematical search or new finite experiment was run.

## 1. Fixed population and actual outcome

Original t edge-disjoint complete m-petal triple-sunflower blocks determine original supports S_i, r(x)=#{i:x in S_i}, Q={x:r(x)>m}; every S_i meets Q in at most two vertices. Original light vertices may recur in up to m original supports. Q is not recomputed after selecting edges or peeling graphs. For m>=3, S029 partitions blocks into A (some petal has <=1 Q) and B (all petals have two Q; necessarily a compulsory Q-pair core with m distinct light thirds). Let T=|B|. Original w_uv counts B blocks with exact pair core uv; the SIMPLE graph G records positive w_uv. Its degrees count distinct neighbours.

The frozen full C512 target is |H|>=t/(512m²), with EVERY exact realised final-H pair, singleton and EMPTY intersection internally witnessed by m distinct petals. A sufficient all-B target is T/(256m²).

**New positive, weaker than the frozen target for unbounded m:**

    D_m = 2(2m-1)(m-1)²,
    |H_R| >= T_R/D_m                         (peeled residual),
    |H_B| >= T/[D_m+(m-1)] > T/(4m³)         (all B),
    |H| >= t/[(m-1)(4m²-3m+1)] > t/(4m³)    (whole <=2-Q slice).

Every output is checked in the SAME final H. This improves the prior generic two-Q nonprivate fallback t/(378m^4) **individual edges** by one m power, but remains one power short of t/(512m²) for growing m. It proves the frozen numerical inequality for 3<=m<=128 (and m=2 directly), not for all m. The all-B T/(256m²) holds from this bound for m<=64. No R3 or every-k TIK follows. A dense-large-star conditional below does meet the target for all m in its stated regime.

## 2. Hall representatives and a two-colour sparse decomposition

Hall gives globally injective light z_i, one chosen original petal {u_i,v_i,z_i} per B block, since each block offers m labels and each light belongs to at most m original blocks. The exact S029 representative criterion is: pair multiplicities 0,1 or >=m; SIMPLE vertex degrees 0,1 or >=m; and graph matching number 0,1 or >=m. This criterion applies only to these selected representatives. Any full original block used instead must be checked on its own.

Peel G at degree <2m until the 2m-core C remains. Partition ORIGINAL pair edges into core edges and peeled edges R, with weights T_C and T_R, so T=T_C+T_R. Orient each R edge from the vertex at whose deletion it was removed. At that step there are at most 2m-1 surviving distinct neighbours, hence outgoing degree <=2m-1. Give outgoing edges different slots 1,...,2m-1.

Each slot's orientation is acyclic by the strict deletion ordering, and outdegree is at most one. Its underlying graph is a FOREST: an undirected cycle has as many edges as vertices, and outdegree<=1 would force outdegree one at every cycle vertex, hence a directed cycle, contradicting the order. Equivalently every finite subgraph of the slot has a sink and at most |V|-1 edges. Thus use TWO proper vertex colours, rather than the three required for an arbitrary functional pseudoforest in S017.

For each slot and head colour, select its directed edges whose heads have that colour. A centre of that colour cannot be a tail in the same layer (proper colouring); all other vertices have outdegree <=1. Therefore the layer is a union of VERTEX-DISJOINT stars. These layers partition R into at most L=2(2m-1) weighted star forests. If T_R>0 some forest P has original weight U>=T_R/L. This is a partition of original pair edges with their original w, not a weight-to-degree substitution.

## 3. Collision-safe assembly with an explicit D_m budget

Let P have h nonempty star components of raw original weights W_j, and centres q_j with d_j distinct neighbours. Component vertex sets are disjoint in Q. All representative light labels used anywhere remain globally injected.

**If h>=m:** Build a representative-only output in EVERY component.

* If d_j>=m, for each pair of weight 1<=w<m retain ONE Hall representative, and for each pair w>=m retain ALL its w Hall representatives. Pair multiplicities are 1 or >=m; the centre degree d_j>=m, leaf degrees one. Retain at least W_j/(m-1) edges.
* If 1<=d_j<m, choose a pair of largest original weight w*>=W_j/d_j>=W_j/(m-1). If w*>=m retain all w* representatives of that pair; otherwise retain ONE representative. Pair multiplicity is >=m or one, centre and leaf graph degree one. The latter case satisfies W_j<=d_j w*<=(m-1)², so one edge is at least W_j/(m-1)². The former case is also at least that bound.

Every component survives and retains >=W_j/(m-1)². The selected graph is a vertex-disjoint union of stars, each centre degree one or >=m, with pair multiplicity one or >=m. Its matching number is EXACTLY h: take one pair edge per component, and a star cannot contribute two disjoint pair edges. Hence h>=m gives a genuine matching of m selected triples for EMPTY, with distinct Q endpoints and globally distinct injected lights. No light singleton or Q-light pair is realised. Within each centre, the true residual singleton matching is its distinct selected neighbour count; parallel representatives never add neighbours. This certifies ALL final kernels and retains >=U/(m-1)².

**If 1<=h<m:** Choose a raw largest component j, so W_j>=U/h>=U/(m-1). Apply S030's weighted-star lemma to this component's ORIGINAL B blocks: it returns >=W_j/(m-1)>=U/(m-1)² edges. If its degree is large it uses safe injected representatives; if short, it chooses a single pair (saturated reps) or ONE original complete block. All its selected triples contain q_j, so EMPTY is absent. It is not combined with the other components. A one-block fallback is entirely valid at its sole exact pair kernel. No lifting of full blocks across components is used.

Thus EVERY residual has an internally m-valid H_R of size

    |H_R| >= U/(m-1)² >= T_R/[2(2m-1)(m-1)²] = T_R/D_m.

The two losses after decomposition are explicit: short pair multiplicity compression and short-star compression (or the small-number-of-components choice). This is a fully quantified lower bound, not a proof that this particular bound is sharp for all allowed families.

## 4. Full B and A/B budget; a genuinely solved dense-star subcase

S030 gives a separately valid H_C>=T_C/(m-1) using the simple 2m-core, actual singleton neighbours, and its independent graph m-matching. Choose the larger of H_C and H_R; DO NOT unite them. If a,b>=0 and certified outputs have sizes >=a/p and >=b/q, their maximum is >=(a+b)/(p+q). Therefore

    |H_B| >= T/[D_m+(m-1)].

Similarly S029 supplies H_A>=|A|/a_m, a_m=(3m-2)(m-1). Choosing ONE of H_A,H_B gives

    |H| >= t/[a_m+D_m+(m-1)]
         = t/[(m-1)(4m²-3m+1)].

The denominator equals 4m³-7m²+4m-1<4m³ for m>=3. Thus for m<=128 it is <512m², giving the frozen C512. For B alone, D_m+(m-1)<4m³, so m<=64 gives the B threshold. These are bounded-m consequences, not a constant independent of unbounded m. The full certified-denominator/target-denominator ratio tends to m/128. At m>=129 the assertion of C512 from this bound alone is UNPROVED; that does not mean C512 is false.

**Useful all-m sufficient multi-star regime:** If some peeled star forest has U>=T_R/L, all its nonempty component stars have d_j>=m, and h>=m, the first construction retains >=U/(m-1), hence

    |H_R| >= T_R/[2(2m-1)(m-1)] > T_R/(4m²).

If T_R>=T/2 this is >T/(8m²), safely above T/(256m²); if instead T_C>=T/2 the old core branch solves the target. This explicitly captures a large-star forest, but such a forest with enough raw weight is NOT guaranteed by the decomposition for every residual. The missing implication is precisely the all-residual m saving while handling both short weighted stars and too few components. Conditional progress is not a universal mass cover.

## 5. First FALSE augmentation step: correct EMPTY and pair cores still do not license full petals

Attempted shortcut: after finding a vertex-disjoint forest of individually valid representative stars with h>=m, replace representatives by ALL petals of their original pair blocks to gain an m factor. Even if within each component no repeated light occurs, and the augmented family passes every heavy-pair and heavy-singleton test and global EMPTY, the assertion of full validity is FALSE.

Freeze the required stress family for EVERY m>=3: r=N=1024m disjoint copies of K_(m-1,N), with w=m-1 complete original m-petal pair-core blocks on EACH pair. Light thirds are globally private except ONE label z in one petal of one block on a chosen arm in component 1 and one petal of one block on a chosen arm in component 2. Those two heavy pairs are disjoint; no original triple repeats. Original counts are

    T = rN(m-1)²,
    r(centre)=N(m-1)>m,
    r(leaf)=(m-1)²>m,
    r(z)=2<=m;

all other light loads are one. ORIGINAL Q is exactly all bipartite endpoints, every block has exactly two compulsory Q vertices, the 2m-core is empty, and the original simple matching number is r(m-1). Within each component choose ONE centre and every one of its N leaf pairs. Avoid z by choosing private Hall representatives; each original block has at least m-1 private choices, all distinct except the deliberately omitted shared z.

The representative forest retaining all w reps on every chosen pair has short codegree w=m-1 and would be invalid. Correct pair compression selects ONE rep per chosen pair: H_good has rN edges, pair multiplicity one, centre degree N>=m, leaf degree one, and true EMPTY matching r>=m. This is internally valid in the SAME original F, and

    |H_good| / [T/(256m²)] = 256m²/(m-1)² >256.

The original single-star guarantee and simple-matching shortcut remain insufficient: target/nu=4(m-1)/m>1; target/N=4(m-1)²/m>1. The multi-star alternate actually resolves this stress family, rather than treating it as a counterexample to the universal bound.

Now lift H_good to ALL m petals of ALL w original blocks on every chosen pair. This H_full has rmN(m-1) edges. Each chosen Q-pair has m(m-1)>=m distinct thirds. Each selected centre has true singleton residual matching N>=m; each leaf has its single Q partner so no heavy singleton is realised there. EMPTY has matching exactly r: one triple per component, avoiding z, and every triple uses its component's chosen centre. These tests all pass.

But the two z-containing triples from components 1 and 2 intersect in EXACT singleton {z}. Their final residual link H_full({z}) is exactly TWO disjoint heavy pairs, so its matching number is 2<m. No other selected edge contains z. Thus full-petal cross-component augmentation is INVALID, despite correct heavy pairs, distinct heavy neighbours, and an actual global m-matching. This sharpens S030's within-centre bad PAIR {q,z}: here there is no within-component light-pair collision; the first failure is an actual LIGHT SINGLETON across the assembled stars. It is a method-only negative, not a new refutation of C512, R3 or TIK.

**A dense, genuinely multi-petal rescue in that same F:** Keep H_full except delete the TWO z-containing triples. Every selected pair then has either m(m-1) or m(m-1)-1 petals; for m>=3 the latter is >=m. All remaining light labels are globally private, all centre degrees remain N, and one private triple per component gives EMPTY matching r. Exact pairs, heavy singletons, and EMPTY are certified, light singleton {z} disappears. The valid size rmN(m-1)-2 far exceeds the target. This specific repair works because affected pair classes have spare petals; no universal spare-petal deletion budget for arbitrary weighted residuals has been proved.

## 6. Other mandatory controls and boundaries

* S029 single K_(m-1,m-1), w=m-1: original endpoints have load (m-1)²>m; rep-only valid optimum remains one. Its simple matching <m triggers S030's full-petal single-pair/weighted-star bound T/[2(m-1)²]. The S031 h<m branch may use ONE complete original block; it does not falsely assert representative-only universality. All petals on one pair give m(m-1) valid edges. This control remains a true counterexample to REP_ONLY_B_512, not to C512.
* S030 within-centre repeated z: full lift creates exact PAIR {q,z} with 2<m thirds; S031's intercomponent z control instead creates singleton matching 2. Both are checked, neither is excused by correct graph degree or EMPTY.
* S018 actual two contaminated channels: pair codegrees N>=m, actual singleton b matching 2<m and EMPTY matching 2<m; one entire a channel is valid at density one half. S019 mixed saturated star: pairs and singletons pass but EMPTY matching 3<m; its pair-core-only branch has valid fraction m/(m+2)>=2/3. Those mixed original blocks may lie in A rather than pure B; no B theorem is asserted for their whole union. Our A/B alternatives are never joined.
* S022 repeated-light/projective-plane light-pair failures remain. Hall fixes only the chosen representative labels. S031 uses full petals only in a SINGLE original block, or in the explicitly audited same-family rescue, never as a general lift.
* Full S023 nested plane: original blocks have one Q hub, so they are in A, not the B graph remainder. S028/S029 A extraction still gives >=t/(3m²); S024 exact dense direct-petal optimum and S023 universal whole-block BSEL refutation are preserved.
* S024 dense private-third K_N: for N>=2m+1 it is wholly a 2m-core; safe injected representatives certify heavy singleton degree N-1 and EMPTY matching floor(N/2)>=m, keeping all original pair representatives. Sparse forest decomposition is not forced on this dense graph. N=2m also has a valid full representative output by direct graph tests, even though it is not a 2m-core.
* m=2: all original triples work because two distinct selected edges witness their exact own intersection. t=0: empty H. For m>=3 and 1<=t<=512m³, a single original complete block gives m>=t/(512m²). T=0 or T_R=0 omits the empty branch. Literal ceilings are respected because every displayed positive inequality is a cardinality bound, with nonempty original populations returning at least one edge/block.

## 7. Status and remaining quantified obligation

S030 restricted star/core/small-matching/large-matching results are preserved. S031 now supplies a FULL-mass nonprivate ORIGINAL <=2-Q fallback >t/(4m³) selected individual edges, including a verified-by-reasoning sparse assembly; no independent reviewer has certified this. The target remains t/(512m²) for ALL m, and full B T/(256m²) is still UNPROVED/UNREFUTED. A statement that the safe assembly alone provides that m saving is unsupported; indiscriminate full-petal augmentation is explicitly false, with dense same-F controls.

The next bounded obligation should establish a simultaneous allocation of extra light petals to weighted star components with an O(m²) original-blocks-per-kept-edge budget, or identify its first exact false step under frozen quantifiers. It must control light singleton matching as well as Q-light pairs, original heavy neighbours, and global EMPTY. No fixed original matching backbone, no preserving every class by fiat, no rep-only substitution, and no universal lift. S032 is FUTURE ONLY.

All S005/S010/S015/S020/S025/S030 mandatory audits were read and retain their scope; next scheduled fifth audit S035. No new detailed N1/N2 by owner policy, no novelty or openness promotion, no Lean/manuscript/publication or external action, no parent mathematical S001. Immutable all-k TIK and unrestricted R3 remain unproved; universal whole-block BSEL remains refuted provisionally by S023. Hosted tests check integrity/semantics only, not the foregoing universal symbolic mathematics.
