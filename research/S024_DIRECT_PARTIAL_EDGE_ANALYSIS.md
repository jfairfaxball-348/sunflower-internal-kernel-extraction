# P001-S024 — direct partial-petal rank-three gate: exact plane optimum and failure of local certificate composition

**One bounded proof-first mathematical gate, 2026-10-11.** The fresh owner invocation was archived as `sessions/P001-S024/INPUT.md` in commit `901f86dd2388d09fd47049e35a4a27544c2d6c79`, BEFORE replacement of the incoming handoff. The absolute quantified **DIRECT_PARTIAL_EDGE_512** conjectural gate was independently frozen at `research/S024_FROZEN_GATE.md`, commit `22676de78f62544a9b1916d4860d07542272dbee`, BEFORE the analysis in this report. Everything mathematical below is SAME-ASSISTANT SYMBOLIC reasoning, without an independent mathematical referee, novel-theorem audit, Lean or publication claim.

## 1. What the frozen target actually says

For ALL m>=3 and every edge-disjoint packing of t complete original m-triple sunflower blocks, choose individual triples H inside their packed union with |H|>=t/(512m²), and for each ACTUAL exact pair intersection (size 2,1,0) between distinct selected triples find m EXACT-kernel petals entirely in H. Equivalently this is >=1/(512m³) of all mt packed edges. Neither the original pair need witness its kernel nor the packed source blocks need be kept whole. This is stronger than a collection of separate externally certified extracts and unlike the now-FALSE uniform whole-block BSEL. The frozen universal statement remains **UNPROVED AND UNREFUTED** here. All fixed-k TIK remains unchanged and unproved.

The chosen mechanism was collision-aware multilevel original-block edge transversals: select individual petal(s) to avoid shared light pairs, then try to integrate simultaneously heavy/light singleton residual matchings and global empty-kernel matching. We test the first tempting local-to-global implication with **true exact H** constraints; failure does not imply the frozen global gate is false.

## 2. Exact unrestricted edge-level optimum of S023's three-tier projective plane

Use EXACTLY S023's original indexed family, not a replacement model. Let q>=2 be a prime power, m=q+2, L=q²+q+1=m²-3m+3, and h=g=m-1. Hubs v_a, 1<=a<=h; groups b, 1<=b<=g; plane points p and lines l in each group; uniquely indexed x_(a,b,l), w_(a,b,l) and group-shared z_(a,b,p). Each original complete block is

    B_(a,b,l) = {{v_a,x_(a,b,l),z_(a,b,p)}: p on l}
                union {{v_a,x_(a,b,l),w_(a,b,l)}}.

It has m=q+2 petals, exact 2-core {v_a,x_(a,b,l)}, and x uniquely identifies its block. t=h*g*L=(m-1)²L blocks, |F|=m(m-1)²L distinct triples. The original Q is exactly {v_1,...,v_h}; every z has original support load m-1 and other light vertices load 1. S023 proved optimum ENTIRE-block selection =1; it also exhibited a lower but not optimal valid partial H of gL triples for one hub.

**NEW EXACT OPTIMUM (same-assistant).** Over ALL H subset F, allowing ANY mixture of whole and partial blocks, satisfying the three in-H exact-kernel certificates, the maximum is

    OPT_edge(F,m) = g*(L+m-1) = (m-1)*(m²-2m+2).

No hypothesis of original whole-block retention, one petal/block, private lights or external witnesses is used in this optimum.

**Upper bound, empty first.** Every triple of F contains exactly ONE original hub; different hubs have disjoint sets of non-hub vertices. If H has edges from two different hubs, one such cross-hub pair meets in EXACT EMPTY. Any matching of triples in H must select distinct hubs and hence has cardinality at most h=m-1<m. Therefore EMPTY is actually realised but cannot have its m disjoint witnesses in H. Thus a valid nonempty H must use **one hub only** (or consist of one edge), and no union of nonempty hub outputs can be certified.

**Upper bound, pair second.** Fix the one hub a. In an original block B_(a,b,l), if H selects at least two triples their exact pair intersection is {v_a,x_(a,b,l)}. That pair's total codegree in the WHOLE F is exactly m, all in that particular original block; its exact m-petal in-H witness therefore forces **ALL m triples of this block** into H. Consequently each original block contributes either zero, one, or all m edges.

If TWO entire blocks for distinct lines l,l' in the SAME group (a,b) are selected, their lines meet in one point p, and the selected triples indexed by p have exact intersection {v_a,z_(a,b,p)}. Its ambient F codegree is the number of lines through p, q+1=m-1<m. It cannot be m-witnessed in H, irrespective of other partial blocks. Hence at most ONE entire block per group. There are L blocks in a group, so that group contributes at most m+(L-1)*1=L+m-1 edges. Sum over g groups to obtain |H|<=g(L+m-1). No assumptions were made about singleton or EMPTY witnesses in obtaining this upper bound.

**Construction meets upper bound, all three levels.** Choose arbitrarily ONE line l_b in each group b of ONE fixed hub a_0. Retain the entire B_(a_0,b,l_b), and from each OTHER line l in that group retain ONLY its private-w triple {v_(a_0),x_(a_0,b,l),w_(a_0,b,l)}. Exactly g(L+m-1) triples remain. Every pair of triples from the SAME entire block has exact 2-core {v_(a_0),x_(a_0,b,l_b)} and is witnessed by its m kept distinct petals. Any pair from different original blocks meets in exactly the singleton {v_(a_0)}: all light x's are block-unique; the only nonprivate z's occur in the ONE full block per group, while all other blocks use private w; groups have disjoint light labels. The singleton residual link has an explicit matching comprising the private-w residual pair {x_(a_0,b,l),w_(a_0,b,l)} for EACH of the gL original blocks, hence nu(H({v_(a_0)}))>=gL>=m. EMPTY is UNREALISED because every edge contains v_(a_0). There are no other realised exact intersections. Thus this H is internally m-valid and attains the upper bound.

**Exact density, not a counterexample to R3.** The maximum actual retained ratio on this F is

    OPT_edge/|F| = (L+m-1)/(m*(m-1)*L)
                = (1/[m(m-1)])*(1+(m-1)/L)
                >= 1/[m(m-1)] >= 1/m².

For comparison, m³*OPT_edge/|F| >=m, so this sequence CANNOT refute R3/TIK's m^-3 density. Nor does OPT_edge/t tend in the dangerous way: OPT_edge/(t/m²)=m²(L+m-1)/[(m-1)L] >=m. At q=2, m=4, L=7, t=63, |F|=252 and OPT_edge=30, whereas at most ONE of the 63 ENTIRE original blocks can be kept, giving four whole-block edges. This example is an exact improvement over S023's gL Hall-based positive; the constructive private-w choice needs NO Hall matching.

## 3. FIRST FALSE IMPLICATION — separate hub certificates do NOT compose

**False LOCAL_HUB_UNION:** If for each original heavy hub v_a one individually constructs an in-H valid edge-level family H_a, then their union is valid after only checking each hub's local 2/1-intersection certificates.

The construction above works for EVERY hub a separately, and each H_a includes gL>=m independently usable residual {x,w} pairs, every realised 2-core is fully m-witnessed, and EMPTY is absent within H_a. Nevertheless for h=m-1>=3 hubs,

    H_union = union_(a=1)^h H_a

has REAL cross-hub exact EMPTY intersections, yet nu(H_union)=h=m-1<m. Upper bound: every triple contains one of h hubs. Lower bound: choose one private-w triple from each hub, disjoint across hubs. All 2-point and singleton kernels remain correctly witnessed in their originating hub; EMPTY is the exact FIRST failed test. This refutes the local-to-global implication with quantifiers for every prime-power q>=2, even when all local choices are optimal. It does not refute DIRECT_PARTIAL_EDGE_512, since choosing ONE hub is an even denser globally valid alternative.

Crucially the S023 proof of whole-block BSEL failure is NOT reused as a supposed impossibility of partial selection; we have calculated the actual partial optimum.

## 4. Complementary dense graph-core control — always restricting to star forests is also false

A converse tempting edge-transversal repair is to mandate that one representative per original pair-core block forms a vertex-disjoint union of monochannel stars/matchings, thereby avoiding global intersection complexity. This is an unduly strong topological restriction.

For any fixed m>=3 and N>=2m, let the original hub support graph be K_N. For each e={u,v} choose m globally private symbols z_(e,1),...,z_(e,m) and make complete original block B_e={{u,v,z_(e,j)}:1<=j<=m}. Blocks are edge-disjoint and simple; t=binom(N,2), |F|=m*t. Select just one individual triple per block:

    H_K = {{u,v,z_(e,1)}: e={u,v} in E(K_N)}.

**True 2/1/EMPTY tests:** No 2-point kernel is realised by two different H_K edges because any hub pair e occurs only once, and private z never recurs. Two incident graph edges meet in exactly one hub u; at u the link pairs {v,z_(uv,1)} for all v!=u are pairwise disjoint, with matching N-1>=m. Two graph-disjoint edges meet in exact EMPTY; H_K has matching floor(N/2)>=m from a matching of K_N. Hence **ALL t individual representatives are internally m-valid**, a fraction 1/m of original F, far ABOVE the t/(512m²) goal.

In contrast, any selected representative family whose support graph is a vertex-disjoint star forest (or any acyclic graph) uses at most N-1 original pair-core blocks. For fixed m and N->infinity,

    (N-1) / [t/(512*m²)] = 1024*m²/N -> 0.

Therefore a proposed universal 'star-forest-only representatives achieve t/(512m²)' intermediary is FALSE. The graph m-core + matching certificate, not only isolated stars, is mathematically necessary to capture these dense instances. Again the proposed unrestricted DIRECT_PARTIAL_EDGE_512 gate remains unrefuted because H_K itself works spectacularly.

## 5. Other required exact stress tests, and the first genuine missing step

- **S022 original-Q-empty light-pair projective plane:** two complete line blocks realise a light PAIR {x,z} with total codegree m-1; independent local block choices are unsafe. A one-per-copy whole-block selection remains valid with >=t/(3m³) under the separately proven Q-empty support-load bound. No universal edge-level density conclusion follows by treating the shared light pair as private.
- **S022 saturated heavy pairs / light singleton:** two different heavy pair-core channels can both be m-saturated and have EMPTY already certified by an independent empty-core block, while a repeated light singleton ell has actual residual matching exactly TWO. Keeping one channel plus the empty-core block gives >half the blocks; selecting arbitrary independent representatives across channels without light-aware controls would recreate that singleton failure.
- **S022 light pair / heavy singleton / EMPTY:** each original heavy singleton is genuinely witnessed and an empty-core block genuinely supplies m disjoint triples, but shared light pair has ambient codegree TWO<m. Keep either one channel plus the empty block for a >half valid alternative.
- **S018 contaminated optional hub b:** combined channels yield true heavy pair codegrees N, but singleton b matching TWO and EMPTY matching TWO; a single channel keeps HALF and is fully valid. No local channel union.
- **S019 mixed saturated pair-active star:** even when pair codegrees and singleton residual matchings pass, realised EMPTY has actual matching THREE<m; the mN P-block-only output keeps m/(m+2)>=2/3 and is valid. No pair=>singleton=>empty inference.

These are symbolic controls inherited from their named reports, NOT fresh bounded enumeration or an independently verified computation. They demonstrate that even after individual petal choice there are TWO mutually independent global bottlenecks: **(i) simultaneous heavy and light exact pair/singleton certificate control at the level of actual selected triples; (ii) actual empty-kernel m-matching whenever disparate mandatory hub groups coexist**. S023 opt shows that discarding hub groups can be affordable in one stress case; the K_N control shows that a forced hub/star discard can lose an unbounded fraction at fixed m in a different stress case. The **FIRST MISSING QUANTIFIED STEP** for the frozen general t/(512m²) theorem is therefore a structural dichotomy with an explicit t/m² budget: find, for arbitrary overlapping original block labels, EITHER a collision-aware large single-core edge selection where EMPTY is absent, OR a broadly spread incidence selection whose realised singleton links have TRUE m matchings and whose support has a TRUE m-edge matching for EMPTY, all while preventing new under-saturated EXACT 2-pairs. The isolated-hub-local UNION implication and forest-only branch are individually false. Neither false intermediary proves a counterexample to the global dichotomy or the frozen gate.

For reference, the inherited full <=2-original-Q NONPRIVATE whole-block fallback t/(378m^5) retains only >=t/(378m^4) original triples (since it keeps full blocks), which misses the new desired >=t/(512m²) by TWO powers of m. One cannot claim the weaker inequality solves the frozen direct target. S021 private-light whole-block t/[126(m-1)^3] and S022 Q-empty restricted result remain scoped and intact. No new universal edge-level inequality was proved.

## 6. Boundaries, provenance and stop

m=2: take H=F for the ORIGINAL all-k TIK, since any selected pair is its own 2-petal exact sunflower. t=0: H empty. For 1<=t<=512m², one triple of any original block is vacuously internally valid and meets |H|>=t/(512m²); a complete original block is also internally valid. For q=2 the specific S023 test has m=4 and admits the exact 30/252 edge-retention above. All calculations and incidence/matching certificates in this S024 report are symbolic; NO new numerical search, source-intensive N1/N2, Lean, paper, correspondence, submission, outreach or other external work.

**S024 result:** NEW exact edge-level optimum on the S023 obstruction; rigorously scoped FALSE local-hub-union and star-forest-only intermediaries; positive dense K_N graph-core control. **DIRECT_PARTIAL_EDGE_512 remains UNPROVED, NOT REFUTED.** The general rank-three R3 and full every-fixed-k TIK remain UNPROVED/UNREFUTED. Universal whole-block BSEL remains provisionally refuted per S023. Original Q was never relabelled. Independent mathematics review absent; no originality promotion, formal result, manuscript, publication or alteration to parent mathematical S001. Required S005/S010/S015/S020 audits remain completed; the mandatory S025 fifth-session correction audit is a **separate future invocation**, NOT run here. The next handoff is prepared for S025 only.
