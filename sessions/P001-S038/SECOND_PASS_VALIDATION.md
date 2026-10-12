# P001-S038 — independent-of-report-lines same-assistant adversarial reconstruction

**Scope:** symbolic independent second pass, not independent mathematician/referee and not executable numerical evidence. The mathematical report was previously frozen/committed; this note re-derives its claims from definitions rather than relying on its proof text. Novelty unchecked. HDSE3/R3/TIK still unproved.

## 1. Exhaustive two-coordinate intersection partition

For distinct (A,z),(B,w) with base k-sets A,B and palette singletons z,w, disjoint ground sets give (A+z)∩(B+w)=(A∩B) ∪ ({z} if z=w else empty). Equal A forces different palette points (since triples distinct), hence one case with kernel A. Unequal A permits same or different palette, hence K+z or K with K=A∩B. There is no fourth case, including when K=empty. Base sunflower witnesses lift in the SAME selected product: for K+z fix z; for K use distinct palette points; for A use a single fixed A with m distinct palette points. This checks all m pair intersections, no use of ambient F and no assumption selected pair itself belongs to witness sunflower. Necessity uses same z to force any witness of K+z to project into the base z-fibre; distinctness of projected petals follows because the palette point is fixed.

## 2. Robust formula reconstructed from the six proper subset types

A rank-three edge {u,v,z} has nonempty proper subsets exactly u,v,z, uv,uz,vz. For any robust selected R and its fibre R_z, the mixed pairs uz and vz each force ≥m graph neighbours. Thus R_z is itself a minimum-degree-at-least-m subgraph of original G; no edge can escape iterative ordinary graph m-core C. The singleton z forces ν(R_z)≥m; if ν(C)<m then every fibre is empty. Conversely if ν(C)≥m, C×Z has uv-link matching q, uz/vz-link matching d_C(u)/d_C(v), z-link matching ν(C), u/v-link matching min(q,d_C(u/v)). Each is ≥m because q≥m, δ(C)≥m, ν(C)≥m. Consequently C×Z is robust and maximal. **Important:** the ordinary base m-core need not itself have ν≥m: G=K_(m+1) has δ=m but ν=floor((m+1)/2)<m for m>=3. The formula correctly gives an EMPTY robust triple core in that case. (For m=3, K4: δ=3, matching 2.) E=K4×Z may nevertheless be internally valid only if G valid; G at m=3 has empty intersection from two disjoint edges and matching 2<m, so not valid. No implication from core-free to valid.

## 3. Spread and high-degree checked without substituting selected degrees

Original E edge count gq. For base u, deg_E(u)=q d_G(u); for palette z, deg_E(z)=g. An original base pair uv has degree q, mixed pair uz has degree d_G(u), and each original triple degree 1. Divide each by gq and apply thresholds 1/(6m),1/(36m²),1/(216m³). There are exactly five nonredundant bounds: Δ/g, 1/q, 1/g, Δ/(qg), 1/(qg). No uncontrolled union bound and no hidden m. High-degree condition at an edge {u,v,z} is AUTOMATIC for g>m³ because SAME ORIGINAL E has deg_E(z)=g. It is not claimed from deg_H(z).

## 4. Graph extraction / equality / constants

S033's previous graph bound is at |G'|/|G|≥1/(8m²). Every base edge produces exactly q distinct tensor edges, and no two different pairs (base,palette) produce the same tensor edge because V∩Z=empty. Hence |H|/|E|=(q|G'|)/(q|G|)=|G'|/|G| when G nonempty; for empty G the desired inequality is 0≥0. No loss for picking a shared palette. In m^-3 form, 1/(8m²)≥1/(8m³) for all m>=2, but ONLY for the tensor subclass. Nothing proves G×Z of positive fraction in an arbitrary HDSE3 family.

For G=K_(m-1,m-1), if a base graph H' is m-valid, any positive H'-degree d is ≤m-1 and must equal 1 (otherwise a realised singleton has 2≤d<m); hence H' is a matching. Its matching number ≤m-1, so if it had ≥2 edges, EMPTY is realised with <m witnesses. Therefore |H'|≤1 and the best tensor-preserving ratio is 1/(m-1)². This is **not** a maximum-valid-ratio upper bound for arbitrary non-tensor H inside original E.

## 5. New counterexample stress reconstructed

Take G star with m+1 leaves, |Z|=m (m≥3). Its tensor includes for base e_0 exactly m triples and therefore certifies pair e_0; deleting one triple leaves m-1≥2 e_0-fibre triples. Their pair intersection is e_0 and its selected residual singleton link has only m-1 points. Failure is genuine PAIR, regardless of whether other kernels are saturated; it is not a graph-base failure. The repair deleting **all** remaining e_0-fibre triples leaves precisely m complete star base edges times m palette points and is valid by tensor lemma, retaining m²/[m(m+1)-1] of the SAME damaged E. At m=3: original 12, remove one =>11, repair9/11; failed pair has exactly 2 residuals<3. These are formula evaluations, not a new enumerated dataset or a program run.

Threshold |Z|>=m is sufficient for all-k equivalence. For one base edge and q=m-1 with m≥3, failure is at the same base kernel; for m=2 such q=1 creates only one tensor edge and is vacuously valid, so no misleading universal necessity claim that q>=m for all individual G.

## 6. Counterexample and predecessor compatibility

- S037 product G=disjoint union r K_(m-1,m-1): r≥m allows one base edge per block and q≥m. Exact ratio r q/(r(m-1)²q)=1/(m-1)². Every E mixed original pair has degree m-1>=2 and below m; hence the robust core is empty; all original pairs are nonetheless nonprivate.
- Support-conflict graph of all r product blocks is complete because Z is shared. That does NOT contradict the tensor selection; the latter CERTIFIES {z} by an r-matching in the base, whereas disjoint-support coloring discards those positives.
- A matching of fewer than m base edges G is NOT internally valid when it contains 2..m-1 edges (EMPTY realised), even though each individual tensor star is valid. The tensor theorem does not license their union.
- Product construction is inapplicable as a blanket assertion to S018/S019 mixed channels, S022 repeated light, S023 plane, S024 private thirds, S030 shared pair, S031 shared-z, S032 row, S034 twins or S035/S036 transversal/bridged controls, absent a proven full common-palette factor.

**Adversarial conclusion:** scoped statements A/B and their constants survive a fresh all-kernel, ORIGINAL-versus-SELECTED and edge-case review. No independent proof reviewer, new finite mathematical test, Lean, originality check, complete HDSE3/R3 or all-k TIK candidate was obtained. The unproved step is quantitatively capturing a *constant proportion of arbitrary high-degree core-free triple mass* by synchronised products or another compatibility scheme.


## 7. Independent SAME-family HDSE3 no-tensor helper stress

Re-check the r=216m, L=m³+1 private-light hub system without referring to its proposed proof. An E-edge uses exactly one hub and two globally private leaf vertices, so any distinct pair of triples either (a) has the same hub and intersects at that singleton or (b) comes from different hubs and has EMPTY intersection. There cannot be a realised 2-set kernel, and no pair has ORIGINAL multiplicity ≥2. The r hub stars individually give L≥m true final-E disjoint petals for {x_i}; r≥m hub edges form a true matching for EMPTY. Each edge's hub has SAME-E degree L>m³. Its maximum vertex degree is L and total original edges rL; pair and triple maximum degrees are 1, meeting each 6m-spread inequality algebraically (r≥6m, rL≥216m³). A robust subfamily is impossible because a chosen edge has some nonempty proper pair T with link matching 1<m. A nonempty product with palette size ≥m requires pair multiplicity ≥m, contradicting E's linearity. Hence the universal full-tensor-mass intermediary is FALSE, and the SAME family H=E is a density-1 valid control. This adds a genuine HDSE3-class **helper counterexample** without a false conjecture refutation.

**Updated verdict:** Exact tensor/core positive results and linear no-tensor control are compatible. An absolute HDSE3 theorem has not been proved. Full-palette mass capture is not a legitimate compulsory reduction; a non-product allocation mechanism is needed.
