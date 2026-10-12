# P001-S034 — DSE_3 via pair-private apex links: a restricted quantitative theorem and a genuine gluing failure

2026-10-12. SAME-ASSISTANT symbolic proof-first research, NOT independent peer review, novelty verification, Lean or publication. Entry independently verified child/parent S033 final-head and postmerge successful Actions jobs; archive commit `93dacbdeaec39b468ff8a198e4c4131488a8fc3f`, input manifest commit `2cd890c3c7d4696a9573cf924f3d828f8616bf28`, frozen gate commit `19bdb5dc4d28f6147d83b8461faea8cea3b70636` precede this report. The immutable full TIK theorem, R3 and DSE_3 remain **UNPROVED**.

## 1. Exact setting

For a triple family F, call an edge e pair-private if it contains a pair `pi(e)` with F-degree exactly one. Fix exactly one such pair per qualifying edge (deterministic if there is a tie). Let c(e) be its third vertex. The pair-private part D* decomposes as an **edge-disjoint** union `D* = disjoint_union_c ( {c} * G_c )`, where G_c consists of the selected pairs. This is an edge partition, NOT a vertex-disjoint partition. Each residual graph G_c is simple. The support `S_c = {c} union V(G_c)` includes both its apex and every vertex it touches. Define Gamma on nonempty apex groups, with adjacency exactly when two such original full supports intersect; let Delta=max degree Gamma.

DSE_3 seeks one absolute c>0 that works for *every* nonempty 6m-spread core-free D at m>=3 with size >=c |D|/m^3 and all realised 2-point, singleton and EMPTY kernels certified by m actual triples IN THE SAME H. It is equivalent to R3 by S033 Theorem D (same-assistant). Theorem B at k=2 supplies a graph subfamily L_c subset G_c, internally valid with |L_c| >= |G_c|/(8m^2). This is not an assertion about compatibility between distinct apexes.

## 2. Restricted positive: the apex-support overlap-colouring lemma

**Theorem S034-A (conditional on rechecked S033 rank-two theorem).** For every m>=3 and every nonempty pair-private D*, with arbitrary overlap graph Gamma of maximum degree Delta, there is a SINGLE internally m-valid triple subfamily H subset D* such that

`|H| >= |D*| / [8 (Delta+1) m^3].`

No spreadness or core-free assumption is required for this *restricted* statement. If D* comprises at least a fraction eta>0 of a target D and Delta<=B independent of m, it gives |H|>=eta |D|/[8(B+1)m^3]. Therefore it certifies the desired exponent for this bounded-overlap, pair-private-mass subclass, NOT arbitrary DSE_3.

**Proof.** Greedily colour Gamma properly using at most Delta+1 colours. Choose one colour class I of apexes whose total original edge mass `W=sum_{c in I}|G_c|` satisfies W>=|D*|/(Delta+1). By construction the full supports S_c for distinct c in I are DISJOINT. For every c in I choose one S033 Theorem B graph extraction L_c subset G_c and lift it to T_c={ {c} union e : e in L_c }. S033 Lemma A0 says T_c is internally m-valid, with |T_c|=|L_c|>=|G_c|/(8m^2).

If |I|>=m, set H=union_{c in I} T_c. All cross-group triples are disjoint, so the ONLY additional realised kernel is EMPTY, witnessed by choosing any one triple from each of m different nonempty components. Every realised nonempty kernel lies within a single T_c and has its original m in-H witnesses there. Therefore |H|>=W/(8m^2), stronger than required.

If 1<=|I|<m, take c0 with maximum |G_c| and H=T_c0, rather than gluing. It is internally valid and |H|>=W/[8 |I| m^2] > W/(8m^3). The EMPTY kernel is either not realised in this single apex lift or, if the underlying graph has an empty realised intersection, it becomes the SINGLETON {c0} and is witnessed by S033 graph-validity. The original graph's singleton intersections become pair kernels {c0,v}; both are certified. The two cases establish the claimed bound. QED.

**Important limitations.** The conflict graph has NO bounded-Delta guarantee from 6m-spreadness, pair-private orientation or C(D)=empty. Using a largest colour class incurs factor Delta+1, so Theorem S034-A alone is NOT DSE_3 or R3. It cannot be applied to the non-pair-private edges D\D*, nor can separately valid colour classes be unioned. The proof uses the ACTUAL support, not just the apex and not just the designated private pair.

## 3. First FALSE candidate: glue independently valid apex outputs

**Theorem S034-B (quantified counterexample to unconditional apexwise gluing, not to DSE_3).** For every integer m>=3 set r=108m^2. For i=1,...,r take disjoint component labels a_i,b_i,x_i and distinct leaves u_{ij},v_{ij}, j=1,...,m. Construct the family D of all 2mr triples
`A_{ij}={a_i,x_i,u_{ij}}`, `B_{ij}={b_i,x_i,v_{ij}}`.

This is a genuinely 6m-spread core-free **pair-private** triple family, and every one of its 2r apex graph stars is internally valid when lifted. Nevertheless their UNION D is NOT internally m-valid.

**Spread calculation (every nonempty T).** |D|=2mr. Max singleton degree is 2m (at x_i), max pair degree m (at {a_i,x_i} or {b_i,x_i}), and every triple has degree 1. The 6m-spread thresholds for these ranks are
`|D|/(6m)=r/3=36m^2 >= 2m`,
`|D|/(36m^2)=r/(18m)=6m >= m`,
`|D|/(216m^3)=r/(108m^2)=1`.
All are satisfied for m>=3, including EVERY pair and singleton, not merely the selected pairs. Each A_{ij} has the F-degree-one private pair {x_i,u_{ij}}, and each B_{ij} the private pair {x_i,v_{ij}}. Thus every edge has a proper pair with residual matching number exactly one in the whole D; no nonempty robust core exists.

**True kernel certificate.** Each apex group `a_i*G_{a_i}` is a complete m-petal sunflower with kernel {a_i,x_i}; similarly for b_i. The corresponding graph G is the m-edge star centred at x_i and itself graph-internally valid. But two differently-apexed triples A_{ij}, B_{ik} meet exactly in {x_i}, so this singleton kernel is realised in the union. The residual triples through x_i split into an a_i-star and a b_i-star. Any matching in the residual link chooses at most one from each star; taking one from each achieves exactly `nu(D({x_i}))=2<m`. The pair kernels {a_i,x_i} and {b_i,x_i} DO have m witnesses; because r disjoint components exist, EMPTY is also realised and has a matching >=r>=m. Hence the FIRST failure is exactly the cross-apex SINGLETON, not a pair or EMPTY error. The naive implication “individually valid lifted graph links imply valid union” is FALSE, even under all DSE_3 hypotheses.

**Same-family dense repair.** Let H contain all A_{ij} and NO B_{ij}. It has |H|=mr=|D|/2. Its only nonempty realised kernels are {a_i,x_i}, each with the m in-H petals; across components the realised EMPTY kernel has a matching r>=m. Every other residual singleton or pair type has value zero or one and is not a realised intersection. So H is fully internally valid. This counterexample invalidates only naive gluing and positively demonstrates that a DSE_3 solution can be much denser than m^-3.

## 4. Why this does not finish the general DSE_3

The first unproved implication of a proposed unrestricted apex route is that every 6m-spread core-free D can either (i) preserve a constant fraction of its edge mass in pair-private apex groups whose *effective simultaneous compatibility cost* is bounded absolutely, OR (ii) extract at the same m^-3 scale directly from high-overlap apex groups, forward-private pair pieces and Lemma E vertex pieces, without losing a new factor m. Theorem S034-A provides only 1/(Delta+1), and pair-private mass can be negligible. No theorem proves either dichotomy. The DSE_3 counterexample target would require a sequence with max_valid(D)*m^3/|D| ->0; none is furnished here.

Theorem A2 permits restarting after a constant-mass loss only if the remaining family fails spreadness, but it does NOT manufacture a constant-mass bounded-overlap colour class. An artificial “one safe apex per vertex” or gluing each graph core without checking x-links merely reinstates the disproved step. Pair-priority deletion's pieces are forward-private, not necessarily private in ORIGINAL D, so Theorem S034-A cannot silently be applied to all pieces.

## 5. Mandatory symbolic stress controls (NO finite enumeration)

| Full test population | Exact outcome for this method |
|---|---|
| S032 full row-palette K_(m+1,m+1), r>=216 | It is 6m-spread and core-free and the ORIGINAL full H=D is valid; forcing a globally private light palette has cap 2/(m+1). Our overlap-colouring bound is merely a lower bound and never asserts that such thinning is necessary, so the dense valid witness is preserved. |
| S031 1024m stars, ONE shared z, dense repair | The shared z is an actual support intersection, never ignored in Gamma. Its documented dense repair remains a valid alternative. Selecting both conflicting apex outputs WITHOUT a singleton check is not licensed. |
| S030 repeated {q,z}, S022 repeated light | Original repeated light link can make a newly realised singleton or a newly realised heavy-light pair. Both are included in support intersections and forbidden by a proper colour class; no unjustified gluing. |
| S029 K_(m-1,m-1), w=m-1 | The original heavy-pair/classes and full-petal rescue remain; an apex-colour lower bound is not a statement that one-per-class representatives are valid. |
| S018/S019 original-Q mixed | Neither source A0/optional-heavy class conditions nor the true empty matching is replaced by individual apex graph checks; the same-family positive alternatives survive and unrestricted mixed branch remains uncovered. |
| FULL S023 nested q-plane, INCLUDING A rescue | Universal whole-block BSEL is still provisionally false while its original A-class individual-edge rescue still works; DSE_3 is about selected individual triples, not preserving all whole blocks. |
| S024 K_N with private thirds | Dense representative extraction H_good with TRUE pair/singleton/EMPTY matching survives; colouring by intersecting supports may lose mass and is not an optimality assertion. |
| N disjoint (m-1)^3 transversals | A single component is m-sunflower-free, so a single edge is valid with ratio (m-1)^-3. For N>=2 and m>=3, choose a matching of size m-1 inside each component: the union has size N(m-1)>=m, all members disjoint, EMPTY witnessed internally and ratio 1/(m-1)^2. For N=1 take one edge. Neither construction refutes DSE_3. |
| Complete K_(N,N,N), N>=6m | It is 6m-spread but not core-free: each realised proper nonempty kernel has residual m-matching, so robust core is the full family. The S033 large-core branch applies; do not falsely label it a DSE_3 instance. |
| m=2, empty D, small nonempty D, arbitrarily large m | At m=2, H=D always works by pair-as-own-witness. Empty D allows empty H. For any single edge, singleton H is valid vacuously; a one-edge fallback alone does not prove a uniform ratio for arbitrarily large |D|. All formulas in §§2–3 are uniform in m>=3. |

All cross-class unions are avoided, and EMPTY is counted explicitly in each positive construction and the counterexample. For the complete tripartite full family, each vertex-link is K_(N,N) and every pair has degree N, so the core claim does not rely on a selected-link surrogate.

## 6. Outcome and provenance

Positive outcome: restricted **APEX_OVERLAP_COLOUR(8)** theorem for all m>=3, exact bound |D*|/[8(Delta+1)m^3]; consequence c=eta/[8(B+1)] when pair-private mass eta and overlap degree B are uniformly bounded. Negative: naive lifted-link gluing is false on an explicit 6m-spread core-free pair-private sequence while the very same family has valid half-density repair. This is a method obstruction only, not a DSE_3/TIK refutation.

**Unproved:** unrestricted pair-private simultaneous selection with Delta-independent density, reduction of forward-private/vertex pieces, DSE_3/R3, all-m C512/B256 and every-fixed-k TIK. S033 graph spread branches remain untested by the auxiliary experiment; this session ran no new research computation. Novelty remains UNCHECKED / NOVELTY_UNCERTAIN; historical JJSW26 source attribution remains, new detailed N1/N2 deferred until complete full TIK proof candidate. No independent referee, Lean, manuscript or publication. S035 is FUTURE mandatory S031–S035 fifth-session correction audit; it was not performed here.
