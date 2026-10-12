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
