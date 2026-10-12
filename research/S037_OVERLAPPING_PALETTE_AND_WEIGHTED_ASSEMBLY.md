# P001-S037 — overlapping high-degree links: exact palette compatibility and weighted assembly

Date 2026-10-12. One owner-invoked S037 mathematical session. Exact owner input was archived at \`b9b9d7588bf37edd6d4a240043a0455dcc1525fc\`, SHA256 \`f19536cc72c22ee3417531f9327f1cf9477ecb1123539be080b2546ca73b172b\`; the proof gate was committed at \`0f0d41b35071fea6d7d8388dd675e458be72ce14\` BEFORE this report. All below is **same-assistant, symbolic proof only**. S033 rank-two T2 and link/core reductions remain unrefereed. HDSE3, R3, C512/B256 (all m) and every-fixed-k TIK remain **UNPROVED**.

## 0. Immutable question and result boundary

For each fixed k, TIK asks for H subset F with |H|>=c_k |F|/m^k (c_k only depends on k), with every realised exact pairwise intersection of distinct H-edges, including EMPTY, an m-petal sunflower **entirely in H**. For m>=3, HDSE3 asks the m^-3 conclusion just for 6m-spread, core-free triple families E in which EVERY edge touches a same-E vertex of degree >m^3. S036 gives R3 iff HDSE3, conditionally on S033, with c3=min(1/13824,c_H/4). This session does NOT establish any universal c_H.

Positive outcomes: (A) an exact **overlap-tolerant pair-core/palette incidence criterion**; (B) a completely algebraic 6m-spread core-free **high-degree, no-pair-private** family with strong overlapping links where naïve same-E unions are invalid but an explicit final-H selection retains 1/(m-1)^2; (C) an absolute m^-3 **weighted-average-conflict** assembly theorem under explicitly stated quantitative low-cover and balance assumptions, improving S036's use of maximum conflict degree. These are scoped lemmas, not a solution of the unrestricted conjecture.

## 1. Theorem A: exact pair-core/palette incidence criterion

Let P_i={a_i,b_i}, i in I, be pairwise disjoint 2-sets, and let Z be disjoint from all P_i. For an arbitrary finite simple bipartite graph G subset I x Z set

 H_G = {P_i union {z} : (i,z) in G}.

Define deg_G on both parts and nu(G) as the ordinary bipartite maximum matching number. For every m>=2,

**H_G is internally m-valid if and only if**:

1. each i with deg_G(i)>=2 has deg_G(i)>=m;
2. each z with deg_G(z)>=2 has deg_G(z)>=m;
3. nu(G) is either <=1 or >=m.

**Proof.** Two distinct H triples with the same i and different z meet exactly in P_i; those are the ONLY realised pair kernels. Their residual H_G(P_i) consists of distinct singleton z's, so its matching number is deg_G(i). Two triples with distinct i and the same z meet exactly in {z}; these are the ONLY realised singleton kernels. Because P_i are mutually disjoint, the residual link at z has matching number exactly deg_G(z). Finally two triples are disjoint precisely when their incidences (i,z) have distinct i AND distinct z, equivalently a size-two matching in G; a disjoint set of m selected triples is exactly an m-matching in G. Therefore EMPTY is realised iff nu(G)>=2, and EMPTY is certified iff nu(G)>=m. These exhaust every pairwise intersection, and all witnesses belong to this SAME H_G. QED.

For G=K_(r,L), with r,L>=m, all three conditions hold. H_G consists of r pair-core stars on a COMMON palette Z. Its exact realised kernels are P_i (r choices), {z} (L choices), and EMPTY, all certified: deg(P_i)=L; nu(H_G({z}))=r; nu(H_G)=min(r,L)>=m. In particular, **original support overlap of all r stars does not imply incompatible union**: the shared singletons are not defects once they have >=m disjoint actual selected petals.

The criterion applies to the specific architecture P_i disjoint. It does NOT claim that arbitrary overlapping high-degree links can be reduced to this architecture with constant mass.

## 2. Theorem B: parametric truly overlapping, pair-nonprivate HDSE3 control

Fix any integer m>=3. Put s=m-1>=2, r=216m^2, q=m^4 and L=sq. Take mutually disjoint s-sets A_i and B_i, for i=1,...,r; take ONE common L-set Z disjoint from ALL A_i,B_i. Define

 E = union_{i=1}^r { {a,b,z} : a in A_i, b in B_i, z in Z }.

Thus E is a SIMPLE triple family of |E|=r s^2 L original edges; all r complete-product blocks have massive ORIGINAL support overlap on the entire common palette Z.

**(i) E is 6m-spread.** Each a in A_i or b in B_i has degree sL and each z in Z has degree rs^2. Their largest degree-to-mass ratios are 1/(rs), 1/L respectively; both are <=1/(6m), because rs>=6m and L>=6m. Each pair {a,b} with a,b in the same i has degree L and each {a,z} or {b,z} degree s; thus max pair degree L and its ratio <=1/(rs^2)<=1/(36m^2). Every triple is unique and |E|=216m^2 s^3 m^4>=216m^3. These are ALL possible nonempty T of cardinality 1,2,3, so E satisfies all 6m-spread inequalities.

**(ii) E is core-free, genuinely nonprivate and high-degree dominated.** Every E-edge {a,b,z} contains {a,z} of E-codegree exactly s=m-1<m. No robust subfamily containing this edge could have m disjoint residual witnesses for this proper nonempty kernel. Hence C(E)=empty. Every pair contained in E has E-degree either L or s, both >=2: there is not a single pair-private triple. Every edge touches a with d_E(a)=sL=s^2 m^4>m^3 (and likewise b), satisfying exactly the SAME-family high-degree condition in HDSE3. The Z-vertices are shared across the blocks and may themselves be very heavy.

**(iii) Natural independent-apex assembly fails on the exact SAME E.** For each i fix b_i^* in B_i. For each a in A_i, the standalone pair-core star S_(i,a)={{a,b_i^*,z}:z in Z} is internally m-valid: its only realised kernel is {a,b_i^*}, which has L>=m genuine petals. But their indiscriminate union U over all i and a is INVALID: for each i,z the pair {b_i^*,z} is realised by s>=2 distinct U edges and has exactly s=m-1 residual singleton a petals, fewer than m. Some separate cross-block singleton and EMPTY certificates may be abundant; they do not repair this PAIR failure. This refutes ONLY a gluing helper, never HDSE3 itself.

**(iv) A dense SAME-E rescue with overlapping palettes.** Choose ONE a_i^* in A_i and ONE b_i^* in B_i for each i and set

 H = {{a_i^*, b_i^*, z}: 1<=i<=r, z in Z} subset E.

This is H_G from §1 with G=K_(r,L). It retains |H|=rL edges, so |H|/|E|=1/s^2=1/(m-1)^2 >=1/m^3. Every realised exact PAIR {a_i^*,b_i^*} is certified by L selected thirds; every realised singleton {z} by r disjoint selected core-pairs; EMPTY by m edges with distinct cores and distinct z, since r,L>=m. No original ambient witness is substituted. The full E is itself NOT internally m-valid because {a,z} has 2..m-1 petals. Hence the repair is nontrivial.

All formulae hold symbolically for every integer m>=3, including m=3; nothing here is a finite check extrapolated to all m. The example shows simultaneously why (a) no private pairs, (b) unbounded genuine support overlap, and (c) many heavy vertices do not imply HDSE3 failure, and why the actual *type and multiplicity* of cross-kernels matters more than a support conflict clique.

## 3. Theorem C: weighted-average-conflict low-cover cluster assembly

Let m>=2, eta in (0,1], B>=1. Let D0 subset D be partitioned into nonempty, edge-disjoint triple clusters D_i with W=|D0|>=eta|D|, and tau*(D_i)<=Bm for each i. By S035's conditional rank-two lift, select for each D_i an internally m-valid **one-apex** H_i subset D_i with

 |H_i| >= |D_i|/(8B m^3).

One-apex H_i may realise PAIR and singleton kernels but cannot realise EMPTY. Define w_i=|D_i|, V_i=union of vertices of H_i (the ACTUAL output support), and J the graph on clusters where i~j iff V_i intersects V_j. Let d_i=deg_J(i) and

 phi = 1 + (sum_i w_i d_i)/W,  so phi>=1.

Assume the **explicit weighted balance hypothesis** max_i w_i <= W/(m phi). Then there exists ONE internally m-valid H subset D with

 |H| >= eta |D|/(8B phi m^3).

**Proof.** Put a uniform random total ordering on the cluster indices and retain each vertex i that comes before ALL its J-neighbours. The retained indices form an independent set: adjacent indices cannot both be earlier than each other. Its expected ORIGINAL cluster mass is sum_i w_i/(d_i+1). By weighted Cauchy-Schwarz/Jensen,

 sum_i w_i/(d_i+1) >= W^2/(sum_i w_i(d_i+1)) = W/phi.

Thus some independent set I has sum_(i in I) w_i >= W/phi. By balance, if it had <=m-1 members, its mass would be <m W/(m phi)=W/phi, contradiction. Therefore |I|>=m. All selected supports V_i are pairwise disjoint. Set H=union_(i in I) H_i. Distinct clusters introduce ONLY the exact EMPTY intersection. There are >=m nonempty output clusters, so choose one edge from each of m different clusters to certify EMPTY by genuine pairwise disjoint H-edges. All realised nonempty kernels remain internal to one H_i and keep their in-H certificates. Hence H is internally m-valid and

 |H|=sum_(i in I)|H_i| >=sum_(i in I)w_i/(8B m^3)>=W/(8B phi m^3)>=eta|D|/(8B phi m^3).

QED.

**Strict extension of S036's numeric conflict statistic.** If max degree(J)<=Delta, then phi<=Delta+1; S036 used Delta+1 and a corresponding max-mass cap on COMPLETE original supports. Here only the weight-averaged ACTUAL-output support degree matters; arbitrarily high maximum degree can coexist with phi=O(1), and the balance hypothesis uses the correspondingly larger threshold W/(m phi). For instance, a support-conflict STAR on N clusters with N-1 leaves carrying equal masses and a negligibly weighted centre has maximum degree N-1, while phi is asymptotically 2. With N>>m and a small central weight the balance condition can hold. This is a **conditional improvement**, not an assertion that every HDSE3 family admits such a decomposition.

**Failure of universal application.** In Theorem B, if clusters are the r complete-product blocks D_i, every ORIGINAL support contains the full common Z and J=K_r even AFTER the one-pair-core H_i selections. Consequently phi=r, so the theorem cannot yield an absolute coefficient. Nevertheless Theorem B supplies a valid overlapping union of those SAME H_i with density 1/s^2. This is precisely the structural regime invisible to support-disjoint coloring: the cross singleton {z} is saturated, not hostile.

## 4. Unsuccessful proof routes and exact remaining quantified implication

1. **Naïve high-degree link lifting and union:** FALSE as a universally valid method by Theorem B(iii). Each hub graph selection can be internally valid while its union creates a PAIR kernel with 2..m-1 petals. The SAME original E has the dense valid solution (iv).
2. **Blanket support-overlap conflict graph:** too crude; Theorem B(iv) has J=K_r and still a dense compatible union. Theorem C improves maximum to weighted-average interference when genuine support disjointness can be found, but phi=O(1) and balance are NOT proved consequences of 6m-spreadness/core-freeness/high-degree.
3. **Fractional cover duality:** S035 supplies density 1/(8m² tau*(E)) when tau*(E)=O(m), but S035's transversal copies show tau*(E)/m arbitrarily large; there is no justified conversion from the dual cover alone to a universal c_H.
4. **Maximal matching and degree cutoff:** S036 solves a 12m-spread input unless >half mass persists on heavy (>m^3) vertices; precisely the HDSE3 class. Matching-only extraction on that remaining class loses uncontrolled mass if maximum degree is unbounded. Theorem B shows even a highly overlapping heavy class can be solved by a global kernel design rather than matching/isolating all supports.
5. **Weighted overlap-energy without balance:** local-minimum independent sets may have fewer than m clusters and may realise a new EMPTY kernel lacking witnesses; S036's (m-1) disjoint independently valid pair-core stars are a symbolic invalid-gluing example. No universal mass-to-compatible-family theorem has been established.

**FIRST UNIVERSAL UNPROVED STEP:** For every integer m>=3 and every finite nonempty 6m-spread core-free triple E in which each original E-edge meets a same-E vertex of degree >m^3, prove existence of H subset E with |H|>=c_H |E|/m^3 and exact all-kernel in-H certificates, for some absolute c_H>0 independent of m and E. Equivalently, find a universal mechanism guaranteeing enough *compatible* high-degree links, including overlapping-but-saturated singleton/pair channels, OR produce E_m with m^3 max_valid_m(E_m)/|E_m|→0. No such proof or genuine counterexample is found here. Theorem B is not a counterexample because it has max_valid fraction >=1/(m-1)^2.

## 5. Boundary and predecessor stress

- S032 row-palette r>=216: original H=D valid; private-petal thinning loses 2/(m+1). No change.
- S031 shared-z / S030 {q,z} / S022 repeated-light: local certificates can be cross-contaminated; do not glue as though supports disjoint. S018/S019 mixed channels retain their published-in-repo same-assistant positive alternatives.
- S029 K_(m-1,m-1), weighted pair cores: keep original triple mass, not one representative per block. Theorem A complements, does not replace, those weighted-link tests.
- Full S023 projective-plane A rescue and S024 K_N valid partial-petal output: still valid SAME-family controls, not newly refuted.
- S034 r=108m² twin stars: pair-private singleton contamination with half-density repair; new Theorem B is **pair-nonprivate** and fails instead at selected PAIR kernels before its dense cross-saturated repair.
- S035 disjoint transversal copies: honest m-valid matching, tau*/m unbounded; S036 bridged copies, giant disjoint pair-stars: honest valid controls, do not assert a counterexample.
- Complete K_(N,N,N), N>=6m: it is robust-core, not HDSE3; do not misuse it as a core-free stress.
- m=2: every H=E is valid because the original selected pair itself supplies two petals at its exact intersection; HDSE3 only needs the hard m>=3 case. Empty E: H=empty. Singleton/small E: no realised intersections, but selecting one edge cannot universally certify a scale-independent density for arbitrary huge E.
- All reported certificate proofs refer to the TRUE final H. No new finite experimental population, random search, CAS/SAT/ILP, Lean or formal computation was run. The random-order argument in §3 is a finite probabilistic existence PROOF, not a sampled experiment.

## 6. Interpretation and mandatory discipline

S037 adds a checkable exact overlapping-palettes compatibility class and an average-conflict conditional assembly tool, **not a universal HDSE3/R3 theorem**. The graph-link T2 dependency and R3 reduction were previously proved only by this same assistant and need independent scrutiny before any strong promotion. Even a future full rank-three proof would not settle every-fixed-k TIK. No fresh N1/N2 was done under explicit owner proof-first instruction; no new originality, independently reviewed theorem, Lean, Palomar, arXiv, manuscript, contact or publication status is asserted. Next S038 is prepared but MUST NOT be executed in S037; S040 is the next mandatory fifth/tenth progress correction audit.
