# P001-S021 — three-channel short-pair compression saves the missing m factor

**One bounded proof-first S021 gate, 2026-10-11. Same-assistant symbolic proof; NO independent referee, novelty verification, Lean or paper.** The S021 frozen target was committed independently at 13b740c62cb11f2bef1807cb2b657a7ebe14ab91 BEFORE this proof: |J| >= t/(200m^3) for the original private-light <=2-original-Q-support triple-block slice. We prove the stronger **PRIVATE_LIGHT_126**: for every m>=3 and every allowed packing,

    |J| >= t/[126(m-1)^3] >= t/(126m^3),

with every realised exact heavy pair, singleton and EMPTY kernel m-witnessed in the SAME final selected H. This is a restricted lemma, NOT universal BSEL, R3 or the paper's all-fixed-k TIK theorem. The original Q stays fixed.

## 1. Frozen universe and a single compatible-channel architecture

Fix m>=3, disjoint as edge sets COMPLETE original m-petal 3-sunflower blocks B_i, i=1,...,t, with original kernel sizes 0/1/2, all non-Q vertices block-private, at most two original heavy vertices from Q in each block support, Q={v: original support block multiplicity(v)>m}. Write the S020 **disjoint** t=a+x+z+y: A0 no heavy-pair-active triple, X_hh original Q-Q pair-core, E00 two Q hubs OPTIONAL and original core Q footprint empty, M exactly one mandatory original Q hub and one optional original Q hub. An active block has one unique active original heavy pair e. The only noncore pair-active blocks are E00 and M. For e={u,v} the exact final codegree is d_H(e)=m p_e+a_e, counting retained e-core blocks and e-active noncore blocks, respectively. In the E00/M-only branches below, p_e=0; every e appears in zero, one, or >=m retained triples. Light-containing exact pair intersections are automatically certified inside the unique original complete block by privacy.

For EACH unordered original heavy pair e, consider **three** disjoint noncore channels: E_e (all E00 at e), M_(u->v) (M with mandatory source u), and M_(v->u) (M with mandatory source v). Let n_e=sum of their original block counts (possibly zero); choose ONE dominant channel L_e of size r_e>=n_e/3, using a deterministic tie-break if desired. Thus the original noncore total z+y=sum_e n_e. Keep original types and Q; no pair can appear as two labels in a final branch. Split the e with n_e>0 into HIGH r_e>=m and SHORT 1<=r_e<m. HIGH is divided by label into H_E (dominating E00) and H_M (dominating oriented M). SHORT contains EVERY remaining pair, regardless of its original 0/1/2-way mix: its original total satisfies n_e<=3(m-1). Define T_E=sum_(H_E) n_e, T_M=sum_(H_M) n_e, T_short=sum_(SHORT) n_e. Therefore t=a+x+T_E+T_M+T_short. This is a *bookkeeping identity*, not a union of selected output branches.

For HIGH E, retain r_e complete original E00 blocks per e and use S019's saturated-only weighted simple-graph lemma. The separate fully valid candidate has

    |J_E| >= (sum_(H_E) r_e)/[6(m-1)^2] >= T_E/[18(m-1)^2].

For HIGH M, retain r_e original entire M blocks of the chosen ONE direction per e, weighted q_e=r_e>=m. The directed weighted lemma of S020 applies WITHOUT any short-class compression, giving another separately valid candidate

    |J_M| >= (sum_(H_M) r_e)/[12(m-1)^3] >= T_M/[36(m-1)^3].

No assertion that J_E and J_M can be united: their incompatible original core footprints would spoil EMPTY. S018 independently gives J_A0>=a/[12(m-1)^3], and S017's clean original heavy-heavy pair-core branch gives J_X>=x/[6(m-1)^3]. The only new missing contribution is T_short; we prove it below with NO reserved empty matching and NO assumed hub-load bound.

## 2. NEW unweighted, three-channel, directed-footprint selection lemma

**Lemma SHORT_GRAPH_18.** Let G be an arbitrary finite SIMPLE graph with N edges. Each edge is tagged exactly one of E (two optional hubs, mandatory original-Q core footprint EMPTY), M(u->v) (compulsory tail u, optional head v), or M(v->u). For every m>=3 there is an edge set S of cardinality

    |S| >= N/[18(m-1)^2]

such that the following ONE final-block selection is valid: represent each selected edge by ONE complete original block of the indicated channel with all non-Q vertices globally block-private, and keep these complete blocks. Every realised exact heavy pair, singleton and EMPTY kernel of the resulting H is internally m-witnessed. G need not bound total |V|, degrees, hub loads, or contain a preselected matching. N=0 permits empty. This lemma is **UNWEIGHTED** (one block representative per distinct pair) and is the m-saving absent from S020's general weighted directed lemma.

**Intrinsic all-kernel certificates for four graph outputs.** A single edge means exactly one original complete block and is automatically valid. A **monochannel star** with >=m arms is valid in each of the three cases:
- M-out (all original mandatory source is the star centre): every triple of every selected block contains that centre, so EMPTY is ABSENT. The centre gets >=m genuine Q-free residual-pair blocks, and each leaf occurs in one centre-containing triple only.
- M-in (the centre is optional; distinct leaves are mandatory sources): the centre's residual pairs are constrained to >=m DISTINCT source hubs, giving actual f+|D|>=m. One Q-clean petal per leaf-source block gives m disjoint original mandatory source footprints, hence actual EMPTY m-matching.
- E star (both hubs optional): the centre's residual-pair matching uses its >=m DISTINCT other-Q neighbours, and one wholly Q-free petal from each of m original E00 blocks is an actual EMPTY m-matching (or a retained empty-core block already certifies it).

A **graph matching of >=m edges** is valid: all original Q supports of the matching edges are mutually disjoint, and one clean original petal per selected block yields m actual disjoint triples. Every graph degree is one, so no new cross-block singleton is realised. A selected **minimum-degree-m core with graph matching >=m** is also valid: the matching witnesses EMPTY, all nonisolated heavy vertex degrees are >=m, and S011 gives actual f_v+|D_v|>=deg_G(v)>=m, because M-out contributes one FREE block per incident edge and E/M-in contributes one DISTINCT constrained neighbour per incident edge. Finally a **vertex-disjoint forest of tagged monochannel stars** (each reduced to one edge or >=m arms) with >=m nonempty components is valid: every centre has distinct graph degree 1 or >=m; one clean selected triple from each of m different components has pairwise disjoint original Q mandatory footprints. A vertex of graph degree ONE has either exactly one selected v-triple (if optional) or one original M block whose own singleton {v} is certified when its core is {v}, or is unrealised when its core is {v,private light}. Thus deg 1 introduces no unsupported heavy singleton. In ALL outputs one block is retained per e, so d_H(e)=1 or 0 and no new heavy pair e is realised; any light pair is internally certified by its original block.

**Proof of SHORT_GRAPH_18 (no assumption on the labelled graph).** If N=0 choose empty. Iteratively peel vertices of surviving DISTINCT graph degree <m, assigning their incident edges to peeled set R; remaining m-core edges C have degree >=m at all incident core vertices. Hence N=|C|+|R|.

CASE C: |C|>=N/2. If the core graph has matching number >=m, keep all C: valid by the core/matching certificate, |S|=|C|>=N/2. Otherwise the endpoints of a maximal core matching (size at most m-1) cover C, at most 2(m-1) vertices. Some one vertex star therefore has >=|C|/[2(m-1)]>=N/[4(m-1)] EDGES. Partition its arms into E, M-in, M-out with respect to this centre; the largest monochannel group has at least N/[12(m-1)] arms. If it has >=m arms, keep that star and exceed the target. If it has <m arms, N<12(m-1)^2 and retaining ONE edge already gives >=N/[18(m-1)^2].

CASE R: |R|>N/2. Orient each peeled edge from the vertex at its deletion time. Each peeling vertex emits at most m-1 outgoing edges. Give its outgoing peeled edges different slots 1,...,m-1. Each slot forms an outdegree-at-most-one directed pseudoforest; a proper 3-colouring of the underlying pseudoforest exists (in fact the peeling orientation is acyclic). Partition each slot by the colour of the arrow HEAD; each part is a disjoint forest of stars because a head of the chosen colour cannot be the tail of another same-head-colour edge, and other tails have outdegree <=1. Thus R decomposes into at most 3(m-1) unlabelled star forests; one has >=|R|/[3(m-1)]>N/[6(m-1)] edges. In each of its star components, choose the largest of the THREE ORIGINAL tags E, M-in, M-out measured relative to that star centre, retaining at least 1/3 of its arms. The resulting vertex-disjoint collection of monochannel stars has total RAW size

    B > N/[18(m-1)].

If it has at least m nonempty star components, compress each component with 1<=d<m to ONE arm and retain all d>=m arms. Every component survives, all selected centres have degree 1 or >=m, and total S>=B/(m-1)>N/[18(m-1)^2]. The m disjoint original Q footprints in different components certify EMPTY.

If it has fewer than m components, choose a largest RAW monochannel component, of size d>=B/(m-1)>N/[18(m-1)^2]. If d>=m, retain it as one valid monochannel large star, meeting the bound. If d<m, then N<18(m-1)^3, and instead work in the ORIGINAL G: if G has matching number >=m, choose ANY m matching edges, giving m>N/[18(m-1)^2], fully valid. If G has matching number <m, endpoints of a maximal matching give a vertex cover of size <=2(m-1), so some ORIGINAL vertex star contains >=N/[2(m-1)] edges. Choose its heaviest among the THREE original types, at least N/[6(m-1)] edges. If >=m keep the monochannel star, exceeding the target; if <m then N<6(m-1)^2 and ONE original edge suffices: 1>N/[6(m-1)^2]>=N/[18(m-1)^2]. Exhausts all cases.

All m-matching or centre-star choices are made **after** knowing the graph branch, never prelocked. The peeling arrow is only a graph decomposition device and is NOT confused with the original mandatory-tail orientation. The 3 tags of an edge are frozen from the selected ORIGINAL block. No weighted load or count of hubs enters the proof.

## 3. Apply to every short ORIGINAL class, including mixed orientations

For each SHORT e choose exactly ONE original complete block from its dominant label L_e, then form the corresponding labelled SIMPLE graph G_short with precisely N_short=#SHORT edges. It has an original Q vertex for each original Q hub; different selected e have disjoint classes, and no two edges represent the same heavy pair. All selected representatives are noncore pair-active, so the lemma's true in-H tests apply. Every SHORT class has n_e<=3(m-1), hence

    N_short >= T_short/[3(m-1)].

Applying SHORT_GRAPH_18 selects a single fully valid final subfamily J_short with

    |J_short|>=N_short/[18(m-1)^2]
             >=T_short/[54(m-1)^3].

The factor m was saved by using UNWEIGHTED graph structure for short original e classes rather than applying S020's arbitrary-weight directed-graph extraction to weight-one compressed edges. Crucially mixed orientations and simultaneous E00/M classes sharing the same e are never falsely merged: one dominant label represents each e (>=one-third of its original mass), and only one block of that e is retained in the SHORT branch. No short class is called free-to-delete: the explicit at-most-3(m-1) weight loss appears in this inequality.

## 4. One final selection and the m^-3 density budget

The five valid candidate J's are ALTERNATIVES, not a union: J_A0, J_X, J_E, J_M, J_short. We may weaken all denominators to a common (m-1)^3 (because m>=3 and m-1>=1). Hence

    max_valid >= max{a/12, x/6, T_E/18, T_M/36, T_short/54} /(m-1)^3
              >= (a+x+T_E+T_M+T_short)/[(12+6+18+36+54)(m-1)^3]
               = t/[126(m-1)^3] >= t/(126m^3) > t/(200m^3).

No output selection ever combines the distinct A0/X/E/M candidates. The NEW J_short does permit its OWN E and M channels only via a single labelled graph and joint certificate argument; it is not the false S019 all-channel star closure. This is the first recorded same-assistant full t/m^3 lower bound for this PARTICULAR restricted private-light slice, **not a proof of unrestricted rank-three BSEL or any all-k TIK theorem**. Previous t/(48m^4) bound is preserved as a weaker true result.

## 5. Exact negative controls (symbolic, not a new experiment)

S018 two contaminated channels, m>=3,N>m: all original B_i^a (core {a,x_i}, contaminated optional b) together with all B_i^c (core {c,z_i}, optional b), t=2N, Q={a,b,c}. Full union: each heavy pair {a,b},{b,c} has EXACT codegree N>=m (so PAIRS pass). Heavy singletons a,c have true f=N. However b is realised and actual f_b=0, D_b={a,c}, nu(G_b)=2<m; EMPTY is realised and mandatory original Q footprints {a},{c} yield true nu(H)=2<m. The full union FAILS; select all a-only blocks (size N=t/2), then b singleton and EMPTY absent, pair/singleton tests pass. Dominant M edges in new J_short do not unite both e channels without a graph certificate.

S019 mixed saturated star, m>=4,N>=m+1: all mN pair-core P_{i,l} at {v,a_i}, together with 2N heavy-light pair-core R_{j,l} at {b_j,light} having optional v. Full union: for e={v,a_i}, d_H(e)=mN; for e={v,b_j}, d_H(e)=N; all >=m. At v true f=0, |D|=m+2>=m; at each b_j true f=N>=m, a_i singletons unrealised. EMPTY is realised but true matching number is precisely 3<m (Q compulsory footprints {v,a_i}, {b_1},{b_2}). Thus full union FAILS EMPTY despite pair/singleton success. Selecting all mN P blocks is fully internally valid, EMPTY absent and v matching exactly m; density m/(m+2)>=2/3. Our proof never uses the invalid MIXED_STAR_CLOSURE; X and M are only separate candidates. Both controls are dense positive alternatives, not fixed-m max_valid*m^3/t ->0 counterexamples.

No new finite enumeration, scripts, stochastic trials or numerical search were run; these are full symbolic realised-kernel audits inherited from S018/S019/S020. Hosted CI tests only target semantics and metadata, not the new universal SHORT_GRAPH_18 proof; independent proof review is still MISSING.

## 6. Boundaries, earlier audits and exact remaining paper gap

t=0: empty J. 1<=t<=3m^3: ONE original complete block gives 1>=t/(3m^3)>=t/(126m^3) and internally certifies its own sole exact kernel. m=2: for original all-k TIK take H=F (the two selected edges themselves form an exact 2-petal sunflower). Original Q, every full original block, exact realised heavy-pair formula, actual singleton f+|D|, and genuine EMPTY matching/absence are preserved. No ambient F witness is substituted.

All S006–S020 positive restricted lemmas, negatives, dense controls, and mandatory S005/S010/S015/S020 audits remain in their original scope; no S025 audit is due now. The new proof depends on S011 exact identities, S017 X submass, S018 A0 submass, S019 saturated E00 and S020 directed saturated-M cases; each is same-assistant and could require independent proof-strength re-audit. The frozen t/(96m^3) from S020 is NOT established by constant 1/126, although S021's separately frozen t/(200m^3) is met. The currently unproved next step is to remove **block privacy of all non-Q vertices** (original light block load may be 2,...,m) while retaining t/(C m^3) and all exact final 2/1/0 certificates, even when at most two original Q hubs occur in every block support; additionally one ultimately must handle blocks with THREE Q hubs and then unrestricted k. This is not a TIK proof candidate and does not trigger detailed new N1/N2, Lean, manuscript, publication, contact or parent mathematical S001. Project original-theorem counter remains zero; a restricted same-assistant combinatorial lemma is not an independently verified published new theorem.
