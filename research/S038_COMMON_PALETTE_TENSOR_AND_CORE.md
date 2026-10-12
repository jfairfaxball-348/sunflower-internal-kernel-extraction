# P001-S038 — saturated common-palette tensor extraction, robust-core exactness, and the remaining unsynchronised HDSE3 gap

2026-10-12. One explicitly owner-invoked, proof-first S038 session. Exact owner invocation (126 UTF-8 bytes, SHA256 \`f19536cc72c22ee3417531f9327f1cf9477ecb1123539be080b2546ca73b172b\`) was independently archived and hashed BEFORE the FROZEN S038 gate commit \`3025f51ade48e9f6c347cc0b1c08a04b9cefccb6\`. All mathematical arguments below are SAME-ASSISTANT symbolic reasoning, unrefereed and without an originality claim. No new finite search/experiment was run.

**Headline:** a fully shared palette is a genuine *rank-stable* mechanism: full Cartesian petal tensoring preserves internal m-sunflower validity **if and only if** in every uniformity. It therefore transfers any lower-rank extraction bound to a higher-rank **structured product** with no additional m-loss. In rank three the existing same-assistant S033 graph constant supplies an m^-2, rather than m^-3, extraction on every complete graph/palette product, with arbitrary overlapping base graph edges and all shared palette supports. A separate exact rank-three **robust-core formula** characterises which of those products are core-free. These results include S037's 6m-spread, high-degree, fully overlapping, no-pair-private original control as a special case. They do NOT establish a dense complete product inside an arbitrary HDSE3 input, so universal HDSE3, R3 and all-fixed-k TIK remain OPEN IN THIS PROJECT.

## 1. Precise definitions and first theorem: tensor equivalence in EVERY rank

Fix integers m>=2, k>=1. Let G be a simple finite k-uniform family on V, and let Z be disjoint from V with q=|Z|>=m. Define the **full common-palette tensor**
\[
T_Z(G)=\{A\cup\{z\}:A\in G,\ z\in Z\}.
\]
Its edges are distinct, all of rank k+1, and |T_Z(G)|=q|G|. The word "full" means every base edge occurs with EVERY palette point, not just a large proportion.

**THEOREM A (exact tensor equivalence).** For each m>=2 and q>=m,
\[
T_Z(G)\text{ is internally }m\text{-valid}\quad\Longleftrightarrow\quad
G\text{ is internally }m\text{-valid}.
\]
This includes G=empty and G with only one member; no empty-kernel exception is silently discarded.

**Proof, forward.** If G has fewer than two edges, G is vacuously valid. Otherwise let A≠B in G and put K=A∩B (possibly EMPTY). Fix z in Z. The two distinct tensor edges A+z and B+z have exact intersection K+z. Since T_Z(G) is m-valid, it contains m distinct sunflower members with that exact kernel. Every one contains z, hence every one has palette coordinate z. Their distinct base projections form m distinct members of G meeting pairwise exactly in K. Thus every realised K of G is witnessed inside G, even K=empty.

**Proof, reverse.** Any distinct tensor edges A+z and B+w fall into exactly these exhaustive cases:
1. A=B and z≠w: intersection is all of A. The m edges A+z_i for m different z_i∈Z give an in-tensor m-sunflower with kernel A.
2. A≠B and z=w: intersection is (A∩B)+z. Since G is valid, take its m base sunflower petals A_i with exact kernel A∩B. All A_i+z are distinct selected tensor edges with exact kernel (A∩B)+z.
3. A≠B and z≠w: intersection is K=A∩B. Take m base petals A_i from G with kernel K and m distinct palette coordinates z_i. Then the tensor edges A_i+z_i meet pairwise exactly in K (their outside-K base parts are disjoint and their palette points are distinct). In particular this treats EMPTY without an ambient witness.
Every realisable pair intersection is therefore certified in the FINAL tensor. QED.

**Corollary A1 (density-preserving extraction).** If G'⊆G is internally m-valid and |G'|>=α|G|, then H=T_Z(G')⊆T_Z(G) is internally valid and |H|/|T_Z(G)|=|G'|/|G|>=α. The theorem supplies an exact bidirectional *validity* correspondence for whole tensors; it does NOT say every valid subfamily of a tensor must itself be a full tensor.

**Corollary A2 (iterated common palettes).** For disjoint palettes Z_1,...,Z_t each of size at least m, any full iterated product G×Z_1×...×Z_t is m-valid iff G is m-valid. A valid base extraction keeps precisely the same original-product density in every higher uniformity k+t. Induct on t using Theorem A at each rank. This is an infinite structural class, NOT a solution of unrestricted TIK at those higher ranks.

## 2. Quantitative rank-three extraction with arbitrary base-graph overlap

Let G be ANY finite simple graph (not necessarily a matching, triangle-free, bounded degree, low-cover, or split into pairwise disjoint cores) and q>=m. S033 Theorem B gives, by an earlier same-assistant symbolic proof that still needs independent scrutiny, an internally m-valid graph G'⊆G with
\[
|G'|\ge |G|/(8m^2).
\]
By Corollary A1, \[
H=G'\times Z\subseteq E=G\times Z,\qquad |H|\ge |E|/(8m^2).
\]
All exact pair/singleton/EMPTY kernels in H are internally certified by Theorem A. This exponent 2 does NOT prove R3: E must be a *complete synchronised common-palette* product, an additional strong assumption not guaranteed by HDSE3.

**Independent rank-three kernel audit for graph base.** Write G'=(V,E'). In H=E'×Z, possible realised kernels, with certificate size stated exactly, are:
- base pair {u,v} from two palette coordinates on a common base edge: codegree q≥m;
- mixed pair {u,z} from two different base edges incident at u at a common z: residual singleton-link cardinality d_G'(u), which is either 0/1 (not realised) or ≥m by graph validity;
- singleton {z} from disjoint base edges at a common z: residual matching ν(G'), either ≤1 (not realised) or ≥m;
- singleton {u} from distinct base edges sharing u at distinct palette coordinates: residual bipartite link is K_(d_G'(u),q), hence matching min(d_G'(u),q)≥m if realised;
- EMPTY from disjoint base edges and distinct palettes: global matching size min(ν(G'),q), thus ≥m whenever EMPTY is realised.
No other intersection types occur. This independently reproduces tensor sufficiency for rank three. For graph G' itself, validity is equivalent to each positive degree being 1 or at least m when ≥2, and ν(G')≤1 or ≥m. The matching number of a graph with no disjoint pair is ≤1; the exceptional possibility is essential.

**Method-level exponent sharpness.** If G=K_(m-1,m-1), for m>=3, every internally valid **base-graph subgraph** G' has at most one edge: every vertex degree of G' is at most m-1, hence must be ≤1, so G' is a matching, but ν(G')≤m-1 forces ν(G')≤1. Thus the best full-tensor-form selection H=G'×Z retains exactly 1/(m-1)^2 of E. This shows no uniform o(m^-2) loss for the product-preserving method. It does NOT upper bound arbitrary non-product H⊆E.

## 3. Exact robust-core formula for graph/palette products

Fix m>=2, q>=m and any finite simple graph G. Denote by C_m(G) its *ordinary graph m-core*: the largest edge subgraph with all nonisolated vertices of degree at least m, obtained by iterative deletion of vertices with current degree in {1,...,m-1}. Let ν(C_m(G)) be its graph matching number (zero if empty). Let C_3(E) be the **robust core** of E=G×Z in S033's exact sense: the largest triple subfamily whose link at every nonempty proper subset T of a selected edge has matching ≥m.

**THEOREM B (core formula).**
\[
C_3(G\times Z)=
\begin{cases}
C_m(G)\times Z,&\nu(C_m(G))\ge m,\\
\varnothing,&\nu(C_m(G))<m.
\end{cases}
\]
In particular **G×Z is core-free iff ν(C_m(G))<m**. This is true even when the entire E is already internally m-valid: robust nonempty-kernel certificates are stronger than realised-kernel-only validity.

**Proof of upper inclusion.** Let R⊆E be *any robust* triple family. For a fixed z define its base fibre graph R_z={uv:uv+z∈R}⊆G. For every selected uv+z∈R, robustness at {u,z} and {v,z} demands at least m distinct third vertices in R; equivalently d_(R_z)(u),d_(R_z)(v)≥m. Hence each nonisolated R_z has minimum degree≥m and is contained in C_m(G). Robustness at singleton {z} demands ν(R_z)≥m as soon as R_z is nonempty. Consequently if ν(C_m(G))<m then every R_z is empty and R=empty. In all cases R⊆C_m(G)×Z. These are SAME R-fibre certificates, not ambient G degrees.

**Proof of reverse inclusion.** If ν(C_m(G))≥m, set R=C_m(G)×Z. Each selected triple uv+z has exactly the following four kinds of nonempty proper subsets T:
- {u,v}: R-link q distinct singleton palette residuals, matching q≥m;
- {u,z} or {v,z}: R-link d_C(u) or d_C(v) distinct singleton residuals, each ≥m;
- {z}: R-link is C, matching ν(C)≥m;
- {u} or {v}: R-link is the complete bipartite graph between the corresponding neighbours in C and Z, matching min(d_C(u),q)≥m.
So R is robust. Union-maximality and the previous upper inclusion force C_3(E)=R. QED.

**Corollary B1 (exact spread checklist).** With g=|G|>0, Δ=max graph degree, q=|Z|, E=G×Z has |E|=gq and is 6m-spread **if and only if** all of
\[
\Delta/g\le 1/(6m),\quad q\ge6m,\quad g\ge36m^2,\quad
\Delta/(qg)\le1/(36m^2),\quad qg\ge216m^3
\]
hold. Proof is an exhaustive original-E codegree census: d_E(u)=q d_G(u), d_E(z)=g, d_E(uv)=q if uv∈G, d_E(uz)=d_G(u), and every triple has degree 1; other subsets have degree 0. This is an exact criterion, not a sufficient approximation.

**Corollary B2 (positive HDSE3 subclass).** Suppose the five explicit conditions of B1 hold, ν(C_m(G))<m, and g>m^3. Then E is 6m-spread, core-free by Theorem B, and EACH E-edge touches its palette vertex z of SAME-E degree exactly g>m³. It therefore satisfies *every* hypothesis of HDSE3. Yet S033 graph extraction and Theorem A provide internally valid H⊆E with |H|>=|E|/(8m²)>=|E|/(8m³). This proves the desired conclusion on a genuinely high-degree, potentially very overlapping, core-free subclass with stronger exponent. No universal product decomposition is claimed.

**Recovering S037's all-shared nonprivate control.** Its original E is exactly G×Z where G is a disjoint union of r=216m² copies of K_(s,s), s=m-1, and q=sm^4. Here C_m(G)=empty (maximum degree s<m), g=rs²>m³, and all B1 inequalities hold. One base edge per K_(s,s) block yields a graph matching of r≥m and an explicit H=(those r edges)×Z. Thus H is internally valid with fraction exactly 1/s²; this recovers S037's positive result from a unified base-graph mechanism, while the general graph extraction also applies to non-disjoint base cores. Every ORIGINAL E pair has codegree q or s≥2, but E is core-free since s<m.

## 4. Failure modes tested by exact symbolic counterexamples, not HDSE3 refutations

**C1: a SINGLE missing tensor incidence can destroy internal validity.** Fix m>=3, base graph G=star K_(1,m+1) with central x and leaves v_0,...,v_m, and Z of exactly m palette points z_0,...,z_(m-1). G is internally m-valid (its centre is its sole realised kernel). By Theorem A, full F=G×Z is m-valid, |F|=m(m+1). Remove ONE original edge {x,v_0,z_0}, obtaining E. The pair {x,v_0} is realised in E by m-1≥2 remaining edges but has only m-1<m third-coordinate petals IN E, so E is INVALID. This defeats naive "almost-full products are automatically compatible" even at 1/[m(m+1)] relative missing density. The SAME E has a dense correct repair:
\[
H=(G-\{xv_0\})\times Z,\quad |H|=m^2,\quad
|H|/|E|=m^2/[m(m+1)-1].
\]
The remaining graph is K_(1,m), internally valid, and Theorem A certifies H at PAIR, singleton and EMPTY levels; EMPTY is not realised since all selected triples contain x. Missing-incidence failure does NOT show a density obstruction to TIK/HDSE3 and E is not asserted to be a spread high-degree input.

**C2: palette size m cannot be dropped in the lifting proof.** Take a one-edge base graph G, and only q=m-1 palette choices, with m>=3. G is vacuously valid, while G×Z has 2..m-1 edges pairwise intersecting in the same base pair, whose in-family link has only q<m petals. This only refutes a weaker threshold hypothesis; the q>=m theorem stands.

**C3: S037's huge support-clique is not a density negative.** Treating each K_(s,s)×Z block as an independently selected cluster yields original and selected support overlap in ALL q palette vertices. The support-conflict graph is complete and phi=r, so the S037 weighted-average-disjoint-support bound is uninformative. The graph tensor theorem nonetheless keeps 1/s² by saturating the mixed {z} channels. The obstacle is *structural synchronization*, not the number of overlapping supports.

**C4: no universal HDSE3 proof from maximal matching alone.** As S036 already shows, a maximal matching covers triples but charges their potentially >m³ original vertex degrees; the explicit B2 class has arbitrarily large palette vertices of degree g>m³ and still admits dense in-H extraction. Charging heavy vertices without recognizing their shared certified channels cannot guarantee the target density.

## 5. Routes pursued, adversarial boundaries, and exact unproved implication

**Successful:** (A) all-rank full-palette equivalence; (B) rank-three m^-2 extraction conditional only on S033's same-assistant graph proof; (C) exact robust core and spread/high-degree algebraic classification of graph/full-palette HDSE3 inputs. These encompass genuinely overlapping base edges, do not need fractional-cover balance, and preserve all original versus selected counts.

**Failed as universal extrapolation:** (D) "nearly-full" palette incidence automatically keeps validity (C1 disproves); (E) low-overlap support coloring as a universal device (S037 complete-overlap controls); (F) m-core/degree saturation of each fibre without a full common palette, because a single missing base-edge/palette incidence creates an underfull realised pair. Uncontrolled partial-fibre pruning might cost powers of m; there is no proved global bound. No computational exploration was used; these are symbolic proofs/counterexamples.

**Remaining quantified HDSE3 challenge:** for *every* nonempty 6m-spread core-free triple E whose every edge meets a SAME-E degree >m³ vertex, prove an internally m-valid H with |H|≥c_H|E|/m³, or construct a genuinely contrary E_m with m³ max_valid(E_m)/|E_m|→0. Nothing in Theorems A/B implies arbitrary E contains any constant-mass G×Z, even after weighting, much less synchronised q>=m palettes. That **product mass capture/synchronization or an alternative non-product mechanism** is the first missing universal step. R3 follows from HDSE3 only under the same-assistant S033/S036 foundational reductions. No proof for all k, novelty certification or independent mathematical review is claimed.

## 6. Named controls and small parameters

- m=2: every finite family is internally 2-valid (its two selected edges witness their own intersection); the exact tensor proof and core formula still work. C1/C2 failures explicitly require m>=3.
- Empty G: tensor empty, both sides valid; the robust core is empty. A single base edge: tensor is valid iff q>=m, and its graph m-core is empty; no false automatic nonempty robust core.
- S029 K_(m-1,m-1): product-preserving exponent sharpness above; not a TIK refutation.
- S018/S019 mixed, S022 repeated light, S030 {q,z}, S031 shared-z, S032 row palette, S034 twin-star: generally NOT full common-palette tensors, so applying A1 to their whole mass would be unjustified. Their recorded controls and same-family rescues remain unchanged.
- S023 complete projective plane/A partial-edge rescue, S024 dense K_N private thirds: neither is declared decomposable into a full common-palette product at fixed mass; no previous method negativity is upgraded to a full negative.
- S035 disjoint complete-transversal and S036 bridged, giant-star controls: compatibility without a single common palette shows the tensor lemma is not a necessary form for all valid H.
- S037 shared-palette r-block E is exactly in B2, remains a positive same-original-family control; its invalid all-apex star lift and its dense rescue both stand.

The next child session **S039** is separately FUTURE and unexecuted. S040 is the next fifth/tenth progress correction audit. No detailed N1/N2 absent a full every-fixed-k TIK candidate, no Lean, Palomar, manuscript, correspondence, submission or external action.
