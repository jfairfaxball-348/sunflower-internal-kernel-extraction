# P001-S043 — nonlinear pair-fibre matching saves an entire m on the peeled stratum

Date 2026-10-13. One separately owner-invoked S043. Exact INPUT archive commit `e5ef47f70efe02a4ccbb239f3753e0bdf9507b88`, separately hashed manifest commit `7861521adc993a6288dd8fe00d9e3be660d85d0d`, independently committed FROZEN gate `1fdad4b6f72a713b72eb36bf385abf60b42584f2` BEFORE this report. **SAME-ASSISTANT symbolic argument, NOT an independently refereed theorem, prior-art/originality audit, Lean, manuscript or publication.** No new finite experiments, no new detailed N1/N2.

## Target and result scope

For every exact realised intersection K of two distinct retained k-edges, including EMPTY, the FINAL selected H must contain m whole edges pairwise intersecting EXACTLY K (witnesses need not include original pair). The unqualified all-k TIK bound c_k|F|/m^k, rank-three R3 and HDSE3 are **NOT PROVED** here.

**THEOREM S043-A (nonlinear bounded fibre / peeled-majority theorem, k=3).** Let m>=3, F any finite family of triples with e=|F|>0 and ORIGINAL maximum pair multiplicity

    max_{x≠y} d_F({x,y}) <= m-1.                               (1)

Suppose ORIGINAL maximum vertex degree Delta(F)<=e/(6m). Repeatedly remove any current vertex with degree in 1,...,m-1 and all its current incident triples; write D for all removed triples and C for the final vertex m-core. If |D|>=e/2, then an internally m-valid H⊆D⊆F exists with

    |H| >= |D|/(108m^3) >= e/(216m^3).                         (2)

No completeness, disjoint-support, bounded transversal, original linearity, restriction on shared blue vertices, or bound on the number of apices is imposed. ORIGINAL pair multiplicities may be 2,...,m-1. This removes the additional 1/(3B-2) from S042's generic conflict-colouring **for this exact peeled stratum**, rather than proving it for arbitrary F.

**Proof (indeed a stronger oriented-class lemma).** Direct each triple of D to its FIRST deleted vertex a(T); every vertex is the apex of at most m-1 removed triples because its current positive degree when peeled is <=m-1. For each T={a,b,c} independently colour vertices RED with probability 1/3 and BLUE with probability 2/3. Call T good when its directed apex a is RED and its other two vertices b,c BLUE. Its good-event probability is (1/3)(2/3)^2=4/27, regardless of dependence among edge events. Hence by expectation, there exists a single deterministic colouring with a set D_good of size

    g >= (4/27)|D|.                                           (3)

Build the simple bipartite incidence graph Q. Left vertices are RED apices a; right vertices are UNORDERED BLUE BASE PAIRS {b,c}; each good T contributes the edge (a,{b,c}). No duplicate bipartite edge exists because F consists of distinct 3-sets. Every left degree is <=m-1, by first-deletion-apex orientation. Every right degree is <=m-1, by the ORIGINAL pair multiplicity (1), even though the corresponding good edges may have DIFFERENT apices and thus be highly nonlinear. Consequently Q has maximum degree <=m-1 on BOTH sides. A greedy maximal matching M in Q contains at least

    |M| >= g/[2(m-1)-1] = g/(2m-3) >= g/(2m).                 (4)

The first inequality counts all Q-edges removed by one greedy matching edge: at most (m-1)+(m-1)-1. For each matched pair (a,{b,c}), retain only its ORIGINAL triple {a,b,c}. All matched triples have PAIRWISE DISTINCT red apices and PAIRWISE DISTINCT blue base pairs, even though the blue pairs may SHARE BLUE VERTICES. They define a simple ordinary graph G whose edges are those matched blue pairs, with |G|=|M|; a unique red apex a(g) is attached to each g∈G.

Apply S033's all-graph rank-two internal TIK theorem with constant c_2=1/8 to G, obtaining internally m-valid J⊆G with |J|>=|G|/(8m²). Define H={g∪{a(g)}:g∈J}. Every apex is RED and every graph-base vertex BLUE, and all apices are distinct. Hence FOR ANY two distinct g,h∈J,

    [g∪{a(g)}] ∩ [h∪{a(h)}] = g∩h.                           (5)

Equation (5) also applies to EVERY pair among the m edges of each witnessing graph sunflower. Therefore each realised H-kernel (a singleton blue vertex or EMPTY; no two H-edges share a pair) is a realised J-kernel with m pairwise exact witnesses IN J; their distinct apex-labelled lifts are m witnesses wholly IN H. PAIR kernels are absent, not falsely externally certified. In particular if EMPTY is realised it has an m-matching of whole selected triples because the lifted graph matching remains disjoint. Thus H is internally m-valid.

By (3),(4) and S033 T2,

    |H| >= [4|D|/27]/[(2m-3)8m²]
         >= |D|/(108m³) >= e/(216m³).                       (6)

All quantifiers are for the FINAL H. QED.

**Corollary S043-B (high vertex degree complement).** For any triple F (no pair assumption), if Delta(F)>e/(6m), choose its maximum-degree vertex v and apply S033 rank-two theorem to ORIGINAL graph link F(v). Lift the graph selection by v, which preserves EXACT kernels and never realises EMPTY. Then

    |H| >= Delta(F)/(8m²) > e/(48m³).                       (7)

Consequently **under (1)**, S043-A+B establish >=e/(216m³) whenever EITHER Delta>e/(6m) OR Delta<=e/(6m) AND the vertex-peeling residual C has |C|<=e/2. This is a substantial ORIGINAL mass class but not a universal dichotomy: when low original Delta and |C|>e/2, the present proof does NOT settle it.

**General rank step (conditional, not full TIK).** For fixed k>=3 suppose unrestricted rank-(k-1) TIK has constant c_(k-1)>0. Let D be any k-family admitting an assignment e↦a(e)∈e such that each ground vertex is an assigned apex of at most m-1 edges, and let ORIGINAL degree of every (k-1)-subset of D be <=m-1. Colour each vertex red with probability 1/k. Each edge is good with probability p_k=(k-1)^(k-1)/k^k when apex red and remaining k-1 vertices blue. Match distinct red apices to distinct blue (k-1)-bases in their bipartite incidence graph, of maximum degree <=m-1 on both sides. Obtain a set G of at least p_k|D|/(2m-3) distinct blue (k-1)-edges with private red apices, and apply rank-(k-1) TIK. Exact-apex lift gives

    |H| >= [c_(k-1) p_k/(2m-3)] |D|/m^(k-1)
          >= [c_(k-1)p_k/2] |D|/m^k.                        (8)

This consumes ONE m on the rank step even when ORIGINAL edges share multiple vertices. For k=3, c_2=1/8 and (8) gives 1/108. For k>=4 it is a valid conditional implication ONLY; it does not assume or establish the missing unrestricted lower rank hypotheses. m=2: H=F holds for ANY uniformity and any input; all bounds are conservative.

## Why the method cannot be applied blindly to the dense survivor

**SAME-E decisive method-negative with full positive rescue.** Let E be S042's all affine lines of F_3^d, n=3^d>=40m³. E is ORIGINAL linear (all pair degrees 1<m), 6m-spread, robust-core-free and high-degree (each x has degree (n-1)/2>m³), yet E ITSELF is internally m-valid: singleton stars have degree >=m and a maximal matching has >=n/9>=m members. The vertex m-core peeling has D=empty and C=E, so (2) does not cover it. Any attempt to replace the peeled-apex condition by an arbitrary orientation and take ONE edge per distinct red apex can retain at most n triples, whereas

    |E|=n(n-1)/6,  (n)/(|E|/m)=6m/(n-1) -> 0.              (9)

So a universal *single-matching-private-apex projection* cannot promise a constant multiple of |E|/m on the entire original dense-core mass, even on a fully valid HDSE3 family. This is a genuine negative about a METHOD, NOT a refutation of HDSE3/R3/TIK; SAME E is its own successful third-certificate rescue. It explains why separately using nonprivate high-degree singleton stars or a dense linear m-core is necessary.

**Saturated opposite end.** When a blue base pair has B>=m original fibres, Q's right degree bound fails. The simplest SAME-E positive repair is all triples {u,v,z_i}, with N>=m distinct z_i: all share EXACT {u,v}, so their whole union is internally valid. Matching Q captures at most one projected base, but the TRUE saturated pair-star can retain N original edges. Thus neither deleting all saturated fibres nor declaring their method incompatibility an HDSE3 counterexample is permitted.

**Parametric m>=3 adversarial lower-bound for Q matching (not a TIK negative).** Take disjoint apices a_1,...,a_(m-1), disjoint base pairs {b_j,c_j} for j=1,...,m-1, and all triples {a_i,b_j,c_j}. Orient each toward a_i. Max apex and pair-base degrees are exactly m-1, and Q=K_(m-1,m-1) has (m-1)^2 incidences but matching only m-1. The matching loss of a factor order m in (4) cannot universally be replaced by an absolute constant. In this specific ORIGINAL E any internally m-valid H has at most one edge: same-i pair has singleton matching <=m-1, same-j pair has exact pair codegree m-1, and distinct-i,j triples are disjoint but original maximum whole-edge matching <=m-1. Thus the SAME-E optimum is 1, satisfying rather than refuting the target m^-3 scale because |E|=(m-1)^2. This example is neither 6m-spread nor high-degree HDSE3. S029/031/032 more elaborate families preserve their previous SAME-E repairs.

## Other fronts and exact first missing universal implication

- **Original pair multiplicity 2,...,m-1:** solved at exponent three on oriented low-outdegree / peeled-majority mass (no complete palettes or separated islands). Do not claim all low-pair-degree families solved: an ORIGINAL dense vertex m-core can dominate even when pair multiplicities are <m, and taking C whole would realise unsaturated PAIR intersections. In fact if all original pair degrees <m, any internally valid H of size>=2 must be LINEAR. An arbitrary vertex m-core is not necessarily such an H.
- **Arbitrary original high-degree HDSE3:** high individual vertex degree permits an m^-2 link lift but aggregating across many original apices is unproved in the dense nonlinear m-core. S036 HDSE3⇒R3 remains conditional. Affine lines defeat the necessity of private apex matching but have valid whole-family rescue; high-degree hard examples S023/S024,S029-32,S034-35,S037-41 are not mathematical HDSE3 counterexamples.
- **Unrestricted all-k:** (8) is a true conditional link-level m-saving, but a universal rank step for all k requires handling dense survivor edges and also original (k-1)-fibres >=m. Never infer all-k from k=3.
- **FIRST UNPROVED implication:** for 6m-spread robust-core-free ORIGINAL high-degree triple E in which max pair degree <=m-1 AND a majority remains in a vertex m-core with small global Delta, extract a LINEAR final internally m-valid subfamily of Omega(|E|/m³) using a dense-overlap certificate (OR find same-E family with m³ maxvalid(E)/|E|→0). More generally handle saturated/intermediate pair levels jointly without assuming cluster/palette completeness. The S042 Steiner positive control shows why a universal two-channel core/island/private-apex decomposition is false.
- **No science status promotion:** JJSW26 source-posed target unchanged; R3 separate attribution remains STATUS_UNCERTAIN, novelty uncertain; no COMPLETE unrestricted original TIK proof, no new detailed N1/N2, no independent math/novelty review, Lean, Palomar, manuscript, correspondence, submission or publication; zero independently cleared paper theorems.

A SEPARATE SAME-ASSISTANT hostile second pass is required after this report is committed.
