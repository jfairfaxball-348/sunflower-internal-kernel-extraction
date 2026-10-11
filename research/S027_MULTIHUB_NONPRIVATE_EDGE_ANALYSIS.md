# P001-S027 — multi-heavy direct-edge gate and false full-support-thinning intermediary

**One proof-first mathematical gate, 2026-10-11.** Fresh owner invocation archived verbatim (126 UTF-8 bytes, SHA256 `f19536cc72c22ee3417531f9327f1cf9477ecb1123539be080b2546ca73b172b`) at `cc3000a2307b99c3dbfb89e19dc81349eb953953`. Universal numerical C=512 and population frozen in the distinct earlier commit `0913cf4ff31400139d36f0b63f9d9ad7b24fcf6d`. **Result:** refutation of a specific first proof step, **NOT** the frozen MULTIHUB_NONPRIVATE_DIRECT_EDGE_512 inequality. Same-assistant symbolic reasoning only; no independent mathematics review, novelty screen, Lean or paper.

## 1. Correct first step and the FALSE strengthening

Original t distinct edge-disjoint complete m-triple sunflower blocks B_i; m>=3; ORIGINAL Q defined by r(v)=number of block supports containing v>m. Assume 1<=|Q|, each original B_i has <=1 Q vertex, and every light v outside Q has r(v)<=m. A block contains at most 3m distinct lights, so the conflict graph joining two blocks with a shared original light has maximum degree <=3m(m-1). A greedy independent set I therefore exists with |I|>=t/[3m(m-1)+1]>=t/(3m²).

**FALSE full-support-thin-first inference:** for every such population, one can choose an independent I and THEN a FINAL internally valid **individual-edge** H subset union_(i in I) B_i with |H|>=t/(512m²). This is stronger than the correct conflict-independent-set bound; we refute the inference for ANY choice of I, even allowing arbitrary partial petals AFTER thinning. The frozen universal direct edge inequality itself does NOT impose this preprocessing and is NOT refuted.

## 2. Universal parametric S023 projective-plane witness

For each prime power q>=2 let m=q+2, h=g=m-1 and L=q²+q+1=m²-3m+3. Construct h original Q hubs v_a and g disjoint PG(2,q) groups per hub. Within group (a,b), each plane line ell defines a complete original pair-core m-block

    B_(a,b,ell)={{v_a,x_(a,b,ell),z_(a,b,p)}:p on ell}
                 union {{v_a,x_(a,b,ell),w_(a,b,ell)}}.

All x,w are block-private; z_(a,b,p) repeats in q+1=m-1 blocks through p. Blocks have exact core {v_a,x_(a,b,ell)}, are edge-disjoint, and every original block has exactly ONE Q vertex. Each v_a lies in gL>m original supports; all non-Q supports have load <=m, Q={v_1,...,v_h}; total block count t=h*g*L=(m-1)²L.

Two distinct lines in the same (a,b) plane intersect in one point and hence their block light supports overlap. Consequently ANY full-original-light-support independent I has at most ONE block in each (a,b) group; each hub supplies at most g=m-1 retained blocks and there are only h=m-1 possible hubs.

Let H be ANY individually selected triple subfamily of union_(i in I) B_i with all realised exact kernels internally m-witnessed. If H uses two distinct hubs a,c, choose one triple from each: all non-Q symbols from distinct hubs are disjoint, so their exact intersection is EMPTY. Every H triple contains its one hub; hence a matching of H uses at most h=m-1 triples. Thus realised EMPTY is uncertified. Therefore H uses only ONE hub.

If H uses triples from two different retained original blocks of the SAME hub a, the two triples intersect EXACTLY in {v_a} because their full light supports are disjoint. Every residual pair in H({v_a}) contains the block-specific x_(a,b,ell), so a residual matching uses at most one pair per original block. At most g=m-1 such blocks of hub a were kept: nu(H({v_a}))<=m-1<m. Thus realised singleton {v_a} is uncertified. Therefore **H is contained in one original block** and |H|<=m. Conversely the entire one block gives m selected triples and its sole exact pair kernel has the required m witnesses, so the exact maximum for ANY light-support-independent preprocessing plus final partial selection is m.

At the literal admissible prime power q=1024, m=1026, L=1,049,601 and t=1,102,737,050,625. Because 512*m³=552,983,334,912<t, the frozen t/(512m²) lower bound would demand |H|>=2047, but preprocessing forces |H|<=1026. Along q=2^s tending to infinity, t/(512m³) tends to infinity. All counts are exact symbolic identities plus displayed integer arithmetic; no unfrozen numerical experiment or enumeration.

## 3. True dense positive alternative in the ORIGINAL F

As independently of this method already established symbolically in S024, choose ONE hub and in EACH of its g groups retain one ENTIRE line block plus just the private-w triple from every other line. There are

    |H_good|=g*(L+m-1)=(m-1)*(m²-2m+2)

selected triples, equalling 1,076,891,650 at m=1026. All realised 2-point intersections occur within full retained blocks and have their m exact petals. All cross-original-block intersections are EXACTLY singleton {v_a}, witnessed by gL>=m pairwise disjoint private-w residual pairs. EMPTY is NOT realised. This H_good uses mutually overlapping original full light supports: it is lost by the false preliminary step. It far exceeds 2047 and proves that the projective-plane example is NOT a counterexample to the frozen direct edge inequality, R3 or TIK.

## 4. Required stress-test scope and boundaries

S023 q-plane is IN the frozen <=1 original Q/block domain and decisively refutes the THIN-FIRST intermediary; its valid partial H passes exact 2/singleton/EMPTY final-H checks. S018/S019 two-original-Q contaminated and compulsory/optional mixtures are generally OUTSIDE this <=1-Q/block scope; their genuine realised heavy-pair/singleton/EMPTY obstructions remain warnings against gluing separately certified channels but do not refute this frozen domain. S024 dense K_N pair-core population has TWO globally Q vertices per original block for N>=2m+1, also OUTSIDE frozen domain; its valid all-graph representative with singleton graph m-degree and global floor(N/2) m-matching is a necessary later unrestricted control. No false assumption that star forests capture dense K_N.

m=2: H=F works since each original distinct pair witnesses itself. t=0: H=empty; then Q is empty so the positive-Q frozen hypothesis is void. For 1<=t<=512m³, ONE complete original block has m internally valid triples and m>=t/(512m²). The first hard regime t>512m³ requires early **petal-level** choice or light-collision management that does NOT discard entire overlapping original supports. The multi-Q original t, Q, kernel requirements and C=512 remain unchanged.

**Mathematical status:** Frozen MULTIHUB_NONPRIVATE_DIRECT_EDGE_512 **UNPROVED/UNREFUTED**. Only FULL_ORIGINAL_LIGHT_SUPPORT_THIN_FIRST_512 is **PROVISIONALLY REFUTED**. Universal whole-block BSEL still refuted by S023; S026 globally ONE-Q positive t/(9m²), S021 private-light and S022 Q-empty positives remain. Unrestricted S024 DIRECT_PARTIAL_EDGE_512 and S025 GLOBAL_EDGE_DICHOTOMY_512, R3 and every-fixed-k TIK all UNPROVED. The next S028 is prepared, not executed; fifth audit S030 not S027. No parent mathematical S001, originality promotion, independent review, source-intensive N1/N2, Lean, manuscript, correspondence or publication.
