# P001-S041 — weighted regional extraction and a genuinely overlapping core–islands theorem

**Date:** 2026-10-13. Exactly one separately invoked P001-S041, frozen at commit \`ff3510b5831454c97e8e34d27036e4366c2117c1\`, after separately archiving the exact 235-byte invocation and SHA256 manifest. SAME-ASSISTANT symbolic mathematics, not independent proof review or novelty clearance. No new finite mathematical experiment, source-intensive N1/N2, Lean, manuscript or external act.

## 1. Target and mathematical boundary

For each fixed k>=1, find c_k>0 such that any finite k-family F contains an internally m-valid H of at least c_k|F|/m^k for all m>=2, where every *realised exact pair intersection*, including EMPTY, has m distinct whole petals **in H**. This full every-k TIK is UNPROVED. The same-assistant S033 rank-two result c_2=1/8 and S036 reduction HDSE3 ⇔ rank-three R3 are inputs, not independent endorsements. The S040 restricted complete/disjoint star-forest product theorem has constant 1/3 at exponent 3.

The research objective was to break beyond complete palettes and disjoint star forests, while attempting general HDSE3 and a uniformity-level mechanism. The main positive below removes *every* palette-completeness requirement, tolerates arbitrary within-island overlap, allows unrestricted overlaps **between one global core and all islands**, and quantifies the exact original-mass bound. The cost is a clear mass-structure assumption; it is **not** a universal overlap theorem.

For any nonempty k-uniform D let τ*(D) be the fractional vertex-cover number: minimise Σ_x w_x over w_x>=0 with Σ_{x∈e}w_x>=1 for every e∈D. For D=∅ put n(D)/τ*(D)=0 by convention. From double counting,
    |D| <= Σ_x w_x d_D(x) <= Δ(D) Σ_x w_x,
so **Δ(D)>=|D|/τ*(D)**. This is an ORIGINAL-D degree bound; it does not certify an H-link.

Assume TIK at rank k-1 with constant c_{k-1}>0, for k>=2. A *lift* at vertex x of D means take a valid rank-(k-1) subfamily J'⊆D(x) and form J={e∪{x}:e∈J'}. Every selected edge contains x; all exact intersections in J are {x}∪K where K was a realised intersection in J'. Every witnessing petal is in J. EMPTY is not realised in J. Thus J is internally valid and, by the fractional-cover inequality, one may choose it with
    |J| >= c_{k-1}|D|/[τ*(D) m^(k-1)].
The vertex may be chosen after examining ORIGINAL D; correctness is checked only in the final lifted J. This claim is vacuous for empty D.

## 2. Main weighted original-mass theorem — not a complete rectangle

**Theorem S041-A (regional star-link aggregation; every uniformity, conditional on rank k-1).**
Let k>=2, m>=2. Suppose an arbitrary finite k-family F is partitioned as
    F=F_0 ⊔ (⊔_{i∈I} F_i),
with the ground-vertex supports of F_i and F_j disjoint for distinct positive indices i≠j. No separation is assumed between F_0 and any F_i: F_0 can share any number of vertices or arbitrarily many edges' vertices with all islands. Within each F_i, there are **no** completeness, star-forest, product, graph-colouring, degree, original pair-codegree, or overlap restrictions. Write
    A = |F_0|/τ*(F_0) (zero if empty),
    W = Σ_{i: F_i≠∅}|F_i|/τ*(F_i).
There exists an internally m-valid H⊆F with
    |H| >= [c_{k-1}/m^(k-1)] max{A, W/m}.             (1)
Every exact realised intersection in the final H has m petals wholly in H.

*Proof.* On F_0, if nonempty, the single-apex lift gives a valid J_0 with |J_0|>=c_{k-1} A/m^(k-1). Do not combine J_0 with islands: cross-core intersections are arbitrary and could be invalid.

For each nonempty island F_i choose the original high-degree apex and a valid J_i as above. Thus
    |J_i| >= c_{k-1} |F_i|/[τ*(F_i)m^(k-1)].
The J_i have disjoint *whole* supports (because their ORIGINAL F_i do). Let r be the number of nonempty islands, and J=∪J_i. If J contains an m-edge matching, J is internally m-valid: any nonempty realised kernel comes from a pair inside one J_i and has its witnesses there; any crossing pair intersects EXACTLY in EMPTY, which is witnessed by the m disjoint selected edges in J. Consequently |J|>=c_{k-1}W/m^(k-1).

If ν(J)<m, then r≤m-1, since one edge from each island is a matching. Take an island i with maximal |F_i|/τ*(F_i)>=W/r. Its own J_i is valid, of size at least c_{k-1}W/[r m^(k-1)] >=c_{k-1}W/m^k. This selection does NOT introduce crossing EMPTY kernels. The case r=0 has W=0. In every case an island-only valid selection has size >=c_{k-1}W/m^k. Choosing between it and J_0 gives (1). No union of incompatible core and islands is asserted. QED.

**Corollary S041-B (genuine overlap, absolute coefficient).**
Fix B>=1. If τ*(F_0)≤Bm when F_0≠∅, and τ*(F_i)≤B for every nonempty island, then
    |H| >= c_{k-1}|F|/(2B m^k).                      (2)
Indeed A>=|F_0|/(Bm), W>=Σ_i|F_i|/B, so (1) gives c_{k-1}max(|F_0|,Σ|F_i|)/(B m^k), and the maximum is at least |F|/2.

At rank THREE, S033's same-assistant c_2=1/8 yields the unconditional-on-further-TIK-ranks structural bound
    |H| >= |F|/(16B m^3).                            (3)
This is conditional only on the correctness of S033's already reported rank-two graph proof, not on any unproved rank-three or all-k hypothesis.

The structure is much more general than complete star-forest×palette products. E.g. take an arbitrary number r of regional families F_i each of the form {x_i,a,z} with an **arbitrary** bipartite incidence graph between private a,z (no rectangle completion and arbitrarily many edges that share x_i). Let a separate F_0 consist of arbitrary triples {t,x_i,b} touching a common t (and potentially many x_i), with no repeated triples. The islands have τ*=1, F_0 has τ*≤1, and its support overlaps **every** island; the number of crossing original-support conflicts tends to infinity with r. The theorem gives 1/(16m³) without any bounded conflict graph or disjoint support for the full F. All direct selected witnesses come from the chosen one channel, so overlapping core/island H fibres are never falsely glued.

**Scope comparison.** S040 proves 1/(3m³) for disjoint complete star-forest×palette components of unrestricted transversal number. S041-B has a weaker constant 1/(16B), but covers wholly partial palettes, arbitrary internal star overlap, arbitrary non-product islands, and a globally overlapping bounded-fractional-cover core. Neither theorem implies the other: S040 components can have unbounded τ*, while S041 allows unlimited non-rectangular overlaps and an overlapping core. This is a genuine new scoped class/mass statement **within the project**, not a novelty or publication claim.

## 3. Sharp exponent and a necessary aggregation cost (SAME-ORIGINAL-F)

For all m>=2 take r=m-1 distinct island apices x_i. For each i introduce private sets Y_i,Z_i, each of size m-1, all supports pairwise disjoint, and define
    F_i = { {x_i,y,z}: y∈Y_i, z∈Z_i }, F_0=∅.
Then τ*(F_i)=1, |F|=(m-1)^3. **Every internally m-valid H⊆F has at most one edge.**

Proof: each F_i consists of triples all containing x_i. Two distinct selected triples in a common island either share a pair {x_i,y} or {x_i,z}, whose TOTAL ORIGINAL codegree is only m-1<m, or share only {x_i}, whose residual bipartite matching is at most m-1 (all available Y_i and Z_i have size m-1). In every case the exact selected kernel has fewer than m possible petals even in ORIGINAL F_i; hence H cannot contain two edges from the same island. Two edges in different islands are disjoint, but every matching in the ORIGINAL union has at most m-1 edges because every edge uses one of x_1,...,x_(m-1). Thus realised EMPTY would have fewer than m possible witnesses. So H has ≤1; a singleton is valid. The proof covers m=2 (a single edge).

This demonstrates the exponent m^-3 in (3) is sharp even if every island has integral vertex cover 1, and explains why one cannot generally glue fewer than m locally valid selections without paying for the missing EMPTY matching. It does NOT refute HDSE3, R3 or TIK, since its optimum ratio is exactly 1/(m-1)^3 and therefore m³·opt/|F| does not tend to zero.

## 4. The two universal fronts attempted, and the first missing implication

**Unrestricted HDSE3.** S036's restricted ORIGINAL E is 6m-spread, robust-core-free, and every ORIGINAL edge touches a SAME-E vertex with E-degree >m³. A high original degree supplies a sizeable single-apex rank-two valid lift, but obtaining a *constant fraction of all E mass at cost m^-3* needs coherent access to many apices. For a 2+1-partite selected H, S039's exact five requirements remain distinct: base PAIR multiplicity, mixed PAIR degree, palette SINGLETON graph matching, base SINGLETON bipartite matching, and global EMPTY matching. Selectors cannot pre-certify these using ambient-E links. The S039 thin per-spoke, S037 shared palette and S023 plane controls show that thresholding original pair multiplicity or insisting on large nonoverlapping whole blocks is not sufficient. No unrestricted m^-3 simultaneous pair/singleton/EMPTY allocation was proved in S041.

**All-k rank step.** Formula (1) works for *every k* assuming TIK at k-1, so it exhibits exactly one extra factor m in a wide structured class. A **universal** induction would need a fixed-B decomposition/certificate for an arbitrary k-family, or a competing selection preserving arbitrary overlapping-link certificates at full original mass. No such decomposition has been derived. In particular a rank-three theorem, if obtained, would not automatically establish all k.

**FIRST MISSING IMPLICATION.** For arbitrary original 6m-spread core-free high-degree E, show an absolute constant c>0 simultaneous all-link selection, *or* a quantitative decomposition/charging principle forcing either τ*(F_0)=O(m) with a fixed share of ORIGINAL E mass, or an ORIGINAL vertex-disjoint island subpopulation carrying fixed mass whose local τ* values are O(1), without assuming those alternatives. Formula (1) is conditional on an actual, independently certified partition, and offers no evidence every HDSE3 input satisfies it. The S035 high-transversal observation invalidates inferring bounded covers just from spreadness.

## 5. Required boundary/status ledger

- **m=2:** H=F is valid for arbitrary F, independent of structural hypotheses. All displayed lower bounds remain true but weaker.
- **EMPTY:** union of selected independent islands is used only when its ACTUAL ν>=m; otherwise pick one island. Cross-core gluing is expressly not attempted.
- **Singleton and PAIR:** every selected island/core component is a one-apex lift of rank-(k-1) internally valid J', with exact selected kernels and entirely in-H witnesses. No selected graph fibration has to be complete.
- **Original versus selected:** weights, degrees, τ* and mass computed on ORIGINAL F_0/F_i; realised kernels, witnesses and matchings checked only on FINAL H.
- **Corrected antecedents:** S023 whole-block negative≠R3; S039 first no-tensor control had a hidden alternate-orientation tensor and was corrected to private-per-spoke; S040 disjoint support/completeness hypotheses are not silently imported.
- **Evidence:** symbolic SAME-ASSISTANT mathematical report only, independent second pass separate, no mathematical finite experiment, no N1/N2, no Lean, zero independent paper theorems, universal HDSE3/R3/all-k TIK all UNPROVED, no parent mathematical S001 or publication.
