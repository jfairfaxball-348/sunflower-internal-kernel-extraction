# P001-S000 source and frontier audit

Date: 2026-10-10. Decision: retain TIK as a **source-posed question with STRONG_EVIDENCE_OPEN**. Its mathematical novelty verdict is **NOVELTY_UNCERTAIN**. No inspected result establishes the precise internal extraction statement. An exhaustive October citation audit and independent expert confirmation have not been obtained; no stronger open-status label is justified.

## The closest published boundaries

See SOURCES.json for stable URLs, versions and reading scope. Formulas use this project's k for uniformity and m for petals.

| Source and locator | Bound / scope | Witness location | Comparison with TIK |
|---|---|---|---|
| JJSW26 Theorem 1.5, attributing Füredi's 1983 semilattice lemma | retained fraction (2^k k m)^(-2^k), with partiteness and a common projected pattern | retained family | supplies a weaker quantitative internal theorem |
| JJSW26 Theorem 1.7(a),(b); proof Section 4.1 | retained fraction (25*2^k*k*m)^(-k), plus an intersection-closed enlargement of each local intersection family | original family | correct exponent, insufficient witness membership |
| JJSW26 Theorem 1.6; Section 4.2, Lemmas 4.1–4.2 | full semilattice fraction <= k! 2^(-binom(k,ceil(k/2))) | obstruction to the full stronger package | common projected pattern is the obstruction; TIK does not ask for it, and permits arbitrary c_k |
| JJSW26 Theorem 1.2 and Lemma 2.1, Sections 2–3 | for no L-sunflower, intersection-avoiding fraction Omega_k(m^(-k+b-a)); certificate lemma explicit in TARGET/source register | original-family hypothesis | conditional avoidance of sizes is different from simultaneously retaining witnesses for every realised kernel |
| VC25 Theorems 1.2 and 1.4 | existence above (C m (log d+log* k))^k for d>=2; sharp (m-1)^k at VC dimension 1 | one sunflower inside input | existence does not give a large family with all intersections internally supported |

Here a=min{i>=0:i not in L}, b=min{i>=a:i in L or i=k}. The quantitative form of Füredi's result is read in the later primary paper, not independently reconstructed from the 1983 original.

## Proof mechanisms actually inspected

JJSW26 Section 2 converts failure of an m-matching in a residual link into a hitting set of at most (k-|K|)(m-1) vertices. Random colouring keeps at least half the edges satisfying local colour-separation certificates; a class of palettes provides the quantitative subfamily. For a bad kernel, the retained sets containing it must share an additional vertex, which prevents that exact intersection. Section 4.1 applies Lemma 2.1 at ell=0 and closes intersections; its contradiction uses the **original** link's certificate. It provides no survival estimate for a matching after restriction. Section 4.2 constructs incompatible projected patterns on disjoint blocks, using finite-field subspaces; this limits the stronger homogeneous conclusion, not TIK alone.

The independently authored KUP25 survey, Section 0.6.3, Theorem 55 and following proof, reproduces the external-witness boundary. Its rendered statement contains apparent typographical issues (a missing prime in the size inequality, and a local intersection definition including the distinguished member); the published JJSW26 statement controls. The survey is corroboration of scope, not an October open-status certificate.

## Recent developments

RAO26, first published 7 January 2026, Section 1.1 and Lemma 2/Section 3, reviews the general (C m log k)^k existence bound and proves a robust sunflower lemma. A robust sunflower is a probabilistic containment structure, not the all-pair internal extraction condition. Its applications and robust lower bound must not be advertised as P001 output.

VC26, arXiv:2609.18995v1, Theorem 1.1, gives (50dm)^k for k-uniform VC dimension <=d. Lemmas 2.3–2.7 use traces, entropy, spread and an intersection-graph matching bound. This yields one sunflower after choosing a core; it does not retain a fixed fraction of an arbitrary large family with all realised cores supported. The fetched abstract and HTML label the submission 17 July 2026 despite the 2609 identifier: retain identifier/version and record that metadata discrepancy without inventing a corrected date.

SHANG26, arXiv:2609.30263v1, Theorems 1.1 and 1.3 and Corollary 1.4, strengthens the bounded-VC spread/robust theory and gives ordinary existence at (C m log(d+1))^k. The actual HTML theorem statements, definitions and application were read through a direct public download after the search browser could not open them. This is a preprint claim, not a journal-acceptance or independently re-proved claim. No simultaneous internal extraction conclusion appears in the inspected statements. The full proof has not been independently certified.

SMALL26, arXiv:2609.06175v1, Lemma 2.3 and Theorem 4.2, studies sunflower-free thresholds. With CH(D,q)=Dq+floor(D/2)floor(q/ceil(D/2)), it records f(1,m)=m-1 and f(2,m)=CH(m-1,m-1). For m>=4 its triple bound is (m-1)(c_m+3h_m-1)/2, where h_m=CH(m-1,m-1), c_m=max{CH(m-1,m-2),3(m-1)}. These are **existence thresholds**, not extraction ratios. Finite computer-assisted endpoints were not rerun and are not adopted as project verification.

## Small ranks and exact-status limitations

The cases m=2 and k=1 are immediate, documented in TARGET.md. At k=2 the internal condition says: any vertex supporting two retained edges must have retained degree >=m, and any pair of disjoint retained edges requires a retained matching of size m. This graph characterisation follows directly from the link equivalence. The known f(2,m) formula addresses only whether a graph has some star or matching. It does not itself prove a uniform fraction extraction guarantee.

No inspected source singles out the precise k=2 or k=3 internal m^(-k) extraction case as either solved or open. Their individual literature statuses remain **STATUS_UNCERTAIN**, not 'confirmed open'. A restricted k=3 result with unbounded m and improved exponent would be mathematically relevant if genuinely new; a fixed (k,m) positive constant or a rediscovered existence bound would not suffice for a paper. Further low-rank attribution is a mandatory part of R3's own N1 gate, not a licence to claim originality now.

## Obstructions and significance

Internal validity is not hereditary under deletion. For m=3, keep only two edges of a three-edge star: the common centre has an ambient sunflower but no internal three-petal witness. Naively iterating the external lemma both changes the bad-kernel population and compounds density losses; termination alone gives no m^(-k) bound. Adding witnesses may introduce additional intersections that themselves need witnesses. A high cardinality link may still have too small a matching. Empty kernels require a global matching, not just large local degrees.

The transversal construction in TARGET.md proves the exponent barrier but does not disprove the target. Theorem 1.6 obstructs the stronger projected-pattern conclusion. Neither should be used as a fake negative result against TIK.

The nearest source-named application requiring internal witnesses is recursive embedding in Turan problems for expansions of trees (JJSW26 Section 6, reference 32). Any quantitative gain there must be proved separately. No direct computing, industrial, quantum or headline-conjecture consequence has been established for P001.

## Research decision

Do not launch an all-ranks proof, broad enumeration, or a manuscript. Freeze only R3: one bounded analytical investigation of rank-three extraction via **internal residual-link matching retention**. This is a more manageable mechanism test than the all-k target; a successful non-routine all-m rank-three theorem could be a substantive restricted contribution. Its publishability and newness remain conditional. Require a density estimate that survives the interaction between pair links, singleton links and the empty link. Accept an explicit method obstruction or a precisely isolated unproved lemma as an honest session outcome. No R3 proof attempt was performed in P001-S000.

## P001-S001 refresh

See [focused N1](S001_N1.md) for the exact rank-three/graph-link recheck and source-access limits. No inspected result settles R3; individual rank status stays STATUS_UNCERTAIN. The analytical [colour-certificate obstruction](R3_FEASIBILITY.md) affects a proof shortcut only and does not change full-target STRONG_EVIDENCE_OPEN or NOVELTY_UNCERTAIN.

## P001-S032 restricted current mathematical frontier (not new N1)
The S032 original <=2-Q compulsory B analysis proves an exact final-family HH/HL/HS/LS/EMPTY certificate check. It does NOT prove quantitative construction for arbitrary weighted peeled B components at |B|/(256m²). S031 guaranteed bound remains order m^-3; C512 arithmetic from it covers only m<=129, not unbounded m. A new original K_(m+1,m+1) row-palette family shows global light-private extra-petal retention can lose 2/(m+1) fraction despite original full F being internally valid; this is METHOD-ONLY. See [frozen gate](S032_FROZEN_GATE.md) and [report](S032_SIMULTANEOUS_LIGHT_ALLOCATIONS.md). Complete all-fixed-k TIK and R3 unresolved, original source status and novelty unchanged, N1/N2 deferred.

## P001-S033 current mathematical frontier (not new N1)
- **Proved, SAME-ASSISTANT:** the link reduction (every k); TIK_2 with c_2=1/8; the robust-core and degenerate-spread reduction. The exact frontier is DSE_3 ⇔ R3.
- **DSE_3 is not a sparse remainder.** It contains the internally valid S032 row-palette family and the core-free S029, S031 and S024 controls. Validity is not union-closed: value-1 certificates are allowed but are destroyed by unions.
- **Comparison only:** at k=2 the attributed general internal bound specialises to (8m)^-4. This is not a literature check, and no claim is made that the k=2 result is new.
- Source: [S033 report](S033_LINK_REDUCTION_AND_RANK_TWO.md).

## P001-S035 — high-cover DSE3 frontier
The new [S035 mathematical record](S035_TRANSVERSAL_ESCAPE.md) gives a genuine **restricted** DSE3 m^-3 extraction on tau*(D)<=Bm (without Delta/pair-private assumptions); it follows a single-apex rank-two lift. But 6m-spread core-free families may have tau*/m unbounded, e.g. disjoint (m-1)^3 transversals with N growing, all of which nevertheless have valid m^-2-density matching alternatives. Mandatory [S035 audit](S035_PROGRESS_CORRECTION_AUDIT.md) checks all previous fifth/tenth results and verifies S033 reductions remain a conditional architecture rather than a complete TIK proof. The unreduced high-cover/high-matching piece is S036's FUTURE target. Source/novelty and parent S001 statuses unchanged.

## P001-S037 frontier update — overlap-saturation, not support-disjointness alone
The S036 equivalence R3 iff high-degree-only HDSE3 remains conditional on S033. S037's exact pair-core/palette incidence iff isolates the genuine PAIR/singleton/EMPTY channel requirements for overlapping links and constructs a same-E 6m-spread core-free, all-pair-nonprivate high-degree common-palette family whose support conflict graph is a huge clique yet which has a valid selected density 1/(m-1)². The weighted average actual-support conflict bound eta/[8B phi m³] is restricted by low per-cluster cover and max cluster mass W/(m phi). A universal saturated-overlap aggregation theorem is the FIRST unproved implication; S038 will investigate, FUTURE only. Full every-fixed-k TIK, R3 and C512/B256 unproved; no novelty or formalisation promotion.

## P001-S038 — exact common-palette tensor versus linear HDSE3 frontier
All-rank full common-palette tensoring with at least m colours preserves internal validity iff base validity; rank-two SAME-ASSISTANT c2=1/8 yields rank-three H>=E/(8m²) on arbitrary graph×common-palette products. Exact graph m-core criterion determines robust core of such products. S037's fully overlapping no-pair-private example is covered. However a fully 6m-spread, core-free, >m³-high-degree *linear* hub-star E is itself m-valid and contains no nonempty m-palette tensor, disproving compulsory tensor mass capture. No general decomposable constant-mass assumption follows. The unsolved HDSE3 step concerns **partial and intermediate kernel multiplicity**. Original vs selected mass and exact in-H pair/singleton/EMPTY checks remain obligatory. No universal R3/TIK proof, genuine negative, novelty or formalisation.


## P001-S039 — exact partial-palette frontier (no new N1)
The five-condition 2+1-partite kernel atlas is exact for any edge-dependent palette incidence. A complete G×Z tensor has a phase gap at 2<=q<m (whole E invalid), yet selecting a single colour of a valid base graph yields >=|E|/(8qm²), while for q>=m full tensor extraction yields >=|E|/(8m²); therefore all-q structured bound >=|E|/(8m³), conditional on S033 graph theorem. A private-PER-SPOKE q=m-1 hub construction has ALL original pair degrees <m, is nevertheless genuinely 6m-spread/core-free/high-degree-dominated, and retains a same-E valid 1/(m-1) fraction. Disjoint-support thick rectangles have m^-3 aggregation; singleton/EMPTY gluing obstruction persists for arbitrary overlap. No universal structural-mass capture, HDSE3, R3 or all-k TIK proof or counterexample. Report and fresh corrected second pass are at [S039](S039_HYBRID_PALETTE_ATLAS_AND_EXTRACTION.md). S040 mandatory fifth/tenth strategic and correction audit remains FUTURE. Novelty and original attribution unchecked.

## P001-S040 — complete thin/thick disjoint star-forest palette bridge (no new N1)
A SAME-ASSISTANT symbolic theorem proves internally witnessed |H|≥|E|/(3m³) for ANY disjoint-support union of complete star-forest-graph × nonempty palette products, allowing arbitrary q_i and both 2≤q_i<m and q_i≥m. The proof partitions ORIGINAL mass into large-star, small-star/many-colour-or-many-stars, and simultaneous small/star-thin channels; it avoids false union-closure and certifies global EMPTY by combining at least m disjoint selected triples or taking one entire valid component. S039 required q_i≥m for its disjoint aggregate with arbitrary base graphs; the new result trades graph generality for thin-palette coverage. No theorem captures a constant portion of arbitrary HDSE3 mass in complete disjoint rectangles, so universal HDSE3/R3/all-k TIK still unproved. Mandatory S040 fifth/tenth audit completed. Exact proofs at research/S040_STAR_FOREST_PALETTE_BRIDGE.md and research/S040_PROGRESS_AND_STRATEGIC_AUDIT.md. N1/N2 deferred; originality/status not promoted.

## P001-S041 — weighted original-mass regional extraction without complete products (no new N1)
Same-assistant S041 proves a conditional every-rank theorem for F partitioned into a general overlapping core F0 and islands Fi with mutually vertex-disjoint whole supports: |H|>=c_(k-1)m^(-(k-1)) max{|F0|/tau*(F0), m^-1 sum |Fi|/tau*(Fi)}. If tau*(F0)<=Bm, each tau*(Fi)<=B, then H>=c_(k-1)|F|/(2Bm^k); rank-three S033 c2=1/8 yields 1/(16Bm³). All partially occupied palettes and arbitrary island internal overlap permitted, and F0 may overlap every island; certified final kernels. S040 has larger 1/3 coefficient for its incomparable complete disjoint star-forest products. Sharp island construction (m-1) one-apex K_(m-1,m-1) clusters gives mass (m-1)^3 and maxvalid=1, confirming exponent 3 without refuting TIK. **NO** proof arbitrary original HDSE3 E has any such bounded-cover original-mass partition. FIRST MISSING universal implication remains unrestricted simultaneous pair/singleton/EMPTY selection or a valid absolute mass dichotomy. Detailed new N1/N2 deferred, independent review absent, full R3/HDSE3/all-k TIK unproved. S042 FUTURE only.

## P001-S042 — all-rank linear exponent and nonlinear frontier
The SAME-ASSISTANT [S042 result](S042_LINEAR_HIERARCHY_AND_REGIONAL_DICHOTOMY.md) proves the original m^-k exponent for ALL ORIGINAL linear rank-k inputs with c_k=1/(2^(k−1)k^k), including c3=1/108. An exact conflict-colouring reduces ORIGINAL bounded pair-degree B to linear input at extra factor 1/[1+binom(k,2)(B−1)]. The affine F_3^d Steiner E satisfies genuine high-degree 6m-spread core-free HDSE3, H=E itself valid, yet bounded-cover global core and disjoint bounded-cover islands capture ≤3B[m/n+1/(n−1)] original mass, which tends to zero. Therefore an unconditional TWO-WAY regional mass premise is FALSE; S041's GIVEN-partition theorem survives. FIRST missing implication: nonlinear multi-link selection with no fatal 1/B≈1/m cost for original pair degree 2..m−1 and >=m, with final in-H pair/singleton/EMPTY certificates. Universal HDSE3/R3/TIK remain UNPROVED, novelty and independent mathematical review absent.

## P001-S046 frontier
[S046 proof-first report](S046_SPARSE_MIXED_PAIR_ENVELOPE_AND_RESCUE.md) and [hostile same-assistant second pass](S046_HOSTILE_SECOND_PASS.md) quantify original rank3 s-matching/graph-link mass max{ s (s>=m), e/(24s m²)} and prove c3=1/(24A) for s<=Am, no original PAIR cap/density. A new connected 6m-spread robust-corefree/high-hub ORIGINAL low-density (e/n=Theta(m)) family with PAIR 2/m, min degree m, tau*≈m⁴ has near-full SAME-E final-H rescue but all MATCHINGS and all COMMON-VERTEX selected families are individually o(e/m³). It kills the universal either-one-hub-or-matching method ONLY. Full HDSE3/R3/TIK missing: compatible many-hub glued selection with non-negligible pair/empty conflicts. No novelty or independent mathematics certification.

## P001-S047 frontier — non-negligible multi-hub conflict with exact selected kernels
[S047 graph-cell theorem](S047_MULTIHUB_GRAPH_CELL_EXTRACTION.md) yields >=e/(m-1)^2 for original edge-disjoint hub×m-rich-graph cells with LOW ordinary-overlap components sharing one hub (arbitrary SAT cell overlap); >=e/(m-1) with SAT or >=m assigned LOW hubs. A connected ORIGINAL corefree 6m-spread high-hub dual-lift cyclic E has half original edges in conflicting PAIR channels, yet SAME-E H=e/2 exact internally valid. Two individually valid LOW K_mm cells sharing ordinary x but distinct hubs break the union at singleton {x} even with independent global EMPTY matching. First missing universal bridge: preserve ORIGINAL e/m^3 mass across arbitrary LOW non-common-hub base overlaps and incomplete link fibres, with in-H pair/singleton/EMPTY certificates. Full HDSE3/R3/all-k TIK UNPROVED; no independent novelty or proof review.
