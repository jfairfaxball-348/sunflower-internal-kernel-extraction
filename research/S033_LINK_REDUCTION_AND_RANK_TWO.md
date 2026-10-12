# P001-S033 — link reduction for every k, rank-two TIK, robust-core/degenerate-spread reduction, and the exact rank-three frontier

2026-10-12. This is a SAME-ASSISTANT proof-first report. It is not independent review, formalisation, an originality claim or publication. Provenance:
- archive `7bbba4e1` (20107 bytes, SHA256 `1b504b82…409c`);
- manifest `27ff9d1e`;
- frozen gate [S033_FROZEN_GATE.md](S033_FROZEN_GATE.md) at `39d21bce`, committed BEFORE this report.

The only computation is the pre-frozen auxiliary check of §3.6. Statuses: TIK (every k) UNPROVED; R3 UNPROVED; universal whole-block BSEL provisionally REFUTED; C512/B256 all-m UNPROVED. The positive results below are restricted to the precise statements given.

## 0. Headline

1. **Theorem A (Link Reduction, every k).** Proving TIK_k only needs families that are λm-spread, for any fixed λ, provided TIK holds in all lower uniformities. Any non-spread T gives an internally valid lift of a lower-rank valid link family, at cost λ^-|T| m^-|T|, which is exactly the m^-k scale.
2. **Theorem B (rank two).** TIK holds for k=2 with c_2=1/8: every graph F has internally valid H with |H| >= |F|/(8m²) for every m>=2. With k=1 (c_1=1) this gives TIK for k<=2. The attributed internal bound specialises at k=2 to (2^k k m)^(-2^k)=(8m)^-4. No novelty, literature or "first" claim is made: N1 is deferred and the statement may well be classical or elementary.
3. **Theorem D (Degenerate-Spread Reduction, every k).** Given TIK_{<k}, TIK_k is EQUIVALENT to an m^-k bound restricted to families that are simultaneously λm-spread (λ=2k) and core-free. Core-free means the union-closed robust core is empty. Consequence: full TIK ⇔ for every k, DSE_k(2k) holds.
4. **Lemma E (rank-three pieces).** In the core-free part, pair-priority deletion decomposes the edges into two kinds of piece. Pair pieces have <= m-1 edges with a common pair. Vertex pieces have a common vertex x whose link graph has <= 2m-1 vertices and minimum degree >= m, hence fewer than (2m-1)(m-1) edges.
5. **Honest frontier.** R3 ⇔ DSE_3: every nonempty 6m-spread core-free triple family D has valid H with |H| >= c m^-3 |D|. DSE_3 is UNPROVED. It is NOT a sparse leftover. The S032 row-palette family is spread and core-free for r >= λ³, yet H=F is internally valid. Every programme B-class construction (S029–S032) is also core-free, because private light thirds create pairs of degree 1. The essential obstruction is precisely that validity is not union-closed: value-1 certificates are allowed but are destroyed by unions.

None of these is a proof of R3, C512, B256 or every-k TIK.

## 1. Bottleneck reconstruction and routes

The S029–S032 packed-block route spends a factor of m on each heavy/light certificate type, and then needs one more m-saving (B256) that no allocation lemma has supplied. The attributed general internal bound (JJSW26 Thm 1.5) pays one factor of m per subset of [k], giving exponent 2^k. The target pays one factor of m per uniformity level. Hence the central question: **can every factor of m be charged to one level of the link hierarchy?**

Routes pursued:
- **Route E (higher-uniformity reduction), §2:** succeeds as a reduction.
- **Route D (dense/degenerate dichotomy), §4–§5:** succeeds as a reduction.
- **Route C (direct link-based selection), §3 and §6:** at k=2 it completes the problem; at k=3 it identifies the first unproved implication.
- **Routes A/IV (B256 allocation), §7:** not advanced. The spread normalisation is inapplicable to arbitrary packed-block populations, and no new allocation lemma was found.

Route B (certificate-first) appears only as the obstruction of §6.3.

## 2. Theorem A — Link Reduction

**Definitions.**
- d_F(T)=#{A∈F : T⊆A}, and F(T) is the residual link.
- For λ>=1, F is **λm-spread** if d_F(T) <= (λm)^-|T| |F| for every nonempty T with |T| <= k. For |T|=k this forces |F| >= (λm)^k whenever F is nonempty.
- s_k(m,λ) is the infimum of the best ratio over nonempty λm-spread k-uniform families.

**Lemma A0 (lifting).** Let |T|=j<k, let L=F(T), and let H' ⊆ L be internally m-valid. Then H={T∪E : E∈H'} ⊆ F is internally m-valid and |H|=|H'|.
*Proof.* Edges of L avoid T, so (T∪E_1)∩(T∪E_2)=T∪(E_1∩E_2). The map E↦T∪E is injective. If E_1∩E_2=K' is realised in H', it has m pairwise disjoint residuals R_i in H'(K'), and the T∪K'∪R_i are m distinct members of H with pairwise intersection exactly T∪K'. Every realised kernel of H has this form, including T itself, which arises from the empty kernel of H'. ∎

**Theorem A.** For every k>=2, m>=2 and λ>=1:
a_k(m) >= min{ (λm)^-k , min_{1<=j<=k-1} (λm)^-j a_{k-j}(m) , s_k(m,λ) }.

*Proof.* Let F be nonempty.
- If F is λm-spread, the ratio is at least s_k.
- Otherwise there is a nonempty T with d_F(T) > (λm)^-|T| |F|, so d_F(T) >= 1.
  - If |T|=k then |F| < (λm)^k, and the single member T gives ratio > (λm)^-k.
  - If 1<=j=|T|<=k-1, the finite family L=F(T) has an internally valid H' with |H'| >= a_{k-j}(m)|L|, since a is an infimum of attained maxima. Lemma A0 gives |H| >= a_{k-j}(m) d_F(T) > (λm)^-j a_{k-j}(m)|F|. ∎

**Corollary A1.** Suppose TIK_j holds with constants c_j for all j<k (c_0:=1). Let β_k(λ)=min_{1<=j<=k} λ^-j c_{k-j}. Then a_k(m) >= min{β_k(λ) m^-k, s_k(m,λ)}. Hence TIK_k ⇔ s_k(m,λ) >= c m^-k for some c>0 and any one fixed λ. The converse holds because s_k >= a_k.

**Corollary A2 (constant-fraction renormalisation).** If G ⊆ F with |G| >= γ|F| and G is not λm-spread, then F has valid H with |H| >= γ β_k(λ) m^-k |F|. This is Theorem A applied to G, using only its non-spread branch. Therefore at any proof step that loses only a constant factor, the current subfamily may be assumed spread. This is unavailable after losing a factor of m.

## 3. Theorem B — rank two

**Lemma ML (matching).** A graph L on n non-isolated vertices with minimum degree δ has ν(L) >= min(δ, ⌊n/2⌋).
*Proof.* Let M be a maximum matching with |M| < min(δ, ⌊n/2⌋). Then n-2|M| >= 2, so there are two unmatched vertices u and w. They are non-adjacent, and all their neighbours are matched, since otherwise M grows. Take an M-edge xy. If u and w together sent three or more edges to {x,y}, then one of them, say u, would see both x and y while w sees, say, x. Then w-x-y-u is M-augmenting. So each M-edge receives at most two edges from {u,w}, and 2δ <= deg u + deg w <= 2|M| < 2δ, a contradiction. ∎

**Theorem B.** For every m>=2 and every graph F (a finite set of 2-sets) there is an internally valid H ⊆ F with |H| >= |F|/(8m²). For m=2 it is H=F.

*Proof.* Fix m>=3, e=|F|>=1 and λ=2. In a graph the realised kernels are the vertices v with deg_H(v) >= 2, which need deg_H(v) >= m, and EMPTY, which needs ν(H) >= m.

**(N) Non-spread.**
- (N1) Some vertex has d(v) > e/(2m). If d(v) >= m, take the star at v. Its kernel is {v} with deg >= m, leaves have degree 1, and the ratio exceeds 1/(2m). If d(v) < m, then e < 2m², and one edge gives ratio > 1/(2m²).
- (N2) Otherwise, if e < 4m² (the pair condition fails), one edge gives > 1/(4m²).

From now on F is 2m-spread: Δ <= e/(2m) and e >= 4m².

**(I) m-core.** Repeatedly delete a vertex of current degree in [1,m-1] together with its current edges, orienting each deleted edge out of the deleted vertex. The remaining edge set C is the largest subgraph with minimum degree >= m on its vertices. If |C| >= e/2, take H=C:
- every realised vertex kernel has degree >= m;
- C has n_C >= 2|C|/Δ >= 2m non-isolated vertices, so ML gives ν(C) >= m and EMPTY is witnessed;
- the ratio is >= 1/2.

**(II) Sparse: |D| > e/2, where D=F\C.**
- Every deleted vertex has out-degree <= m-1. Each edge is oriented from an earlier-deleted vertex to a later-deleted or never-deleted one, so the orientation is acyclic.
- Label each vertex's out-edges with distinct labels 1..m-1. Each label class is a rooted forest: each vertex has <= 1 out-edge, pointing to its parent.
- Split each class by the parity of the child's depth. Each part is a vertex-disjoint union of stars (centres have the other parity; a leaf has a unique parent).
- This partitions D into 2(m-1) star forests. Let S be the largest, so |S| > e/(4(m-1)).
- A star with >= m leaves is *big*; the others are *small*.

Cases:
- (IIa) Big stars carry >= |S|/2 > e/(8(m-1)) edges.
  - If there are >= m big stars, take H = all big stars. Centres have degree >= m, leaves degree 1, and EMPTY is witnessed by one edge from each of m vertex-disjoint stars. Ratio > 1/(8(m-1)).
  - If there are b <= m-1 big stars, take the largest one: ratio > 1/(8(m-1)²). Its only kernel is the centre, and EMPTY is unrealised.
- (IIb) Small stars carry > e/(8(m-1)) edges. Then there are s > e/(8(m-1)²) small stars. Take M = one edge per small star; it is a matching.
  - If s >= m, H=M is valid (only EMPTY is realised and ν=|M|) with ratio > 1/(8(m-1)²).
  - If s < m, then e < 8m(m-1)². Spreadness gives a greedy maximal matching of size >= e/(2Δ-1) > m. Take it: ratio >= m/e > 1/(8(m-1)²).

**Constants.** min{1/(2m), 1/(2m²), 1/(4m²), 1/2, 1/(8(m-1)), 1/(8(m-1)²)} >= 1/(8m²) for m>=3. ∎

**§3.6 Frozen auxiliary check.** `experiments/s033_t2_check.py` implements exactly this case analysis and validates every output with `semantics.internal_by_links` and 8m²|H| >= |F|.
- Run once on the complete frozen population of 64 labelled graphs (the gate's "at most 66" count included 2 disjoint-copy items that are defined only for m>=3). Result: **ALL 64 PASS in 0.01 s**.
- **Recorded negative/limitation finding:** every frozen graph falls into the m=2, (N1) or (N2) branches. The spread branches (I), (IIa) and (IIb) were NEVER exercised, because they need e >= 4m² and Δ <= e/(2m).
- Per the stop rule the population was not extended. The proof of (I)/(II) therefore rests SOLELY on the written argument and its second pass.

## 4. Robust core and Theorem D

**Robust core.** C(F) is the largest G ⊆ F such that ν(G(T)) >= m for every nonempty T properly contained in an edge of G. The property is union-closed, because ν(G(T)) is monotone in G, so C(F) is the union of all such G. **Core-free** means C(F)=∅. The core is obtained by any order of deleting all edges ⊇ T for a "bad" T (1 <= ν(cur(T)) <= m-1):
- a member of a robust G is never deleted, because cur ⊇ G;
- the terminal family is robust.

**Proposition C.** If F is λm-spread, γ∈(0,1], λ >= k/γ and |C(F)| >= γ|F|, then H=C(F) is internally valid.
*Proof.* Nonempty realised kernels T satisfy T ⊊ A∈C, so ν(C(T)) >= m. For EMPTY, a maximal matching M of C covers every edge of C with k|M| vertices, each of F-degree <= |F|/(λm). Hence |M| >= λm|C|/(k|F|) >= m. ∎

**Theorem D.** Fix k>=2, γ∈(0,1), λ >= k/γ, and assume TIK_j (constants c_j) for j<k. Let δ_k(m,λ) be the infimum of the best ratio over nonempty λm-spread core-free k-uniform families. Then
a_k(m) >= min{ (1-γ) β_k(λ) m^-k , γ , (1-γ) δ_k(m,λ) }.
Hence, given TIK_{<k}: TIK_k ⇔ δ_k(m,λ) >= c m^-k.

*Proof.* Use Corollary A1 when F is not spread, and Proposition C when the core is large. Otherwise D=F\C(F) has |D| > (1-γ)|F|. D is core-free, because C(D) is robust in F, so C(D) ⊆ C(F)∩D=∅. If D is not spread, apply Corollary A2. Otherwise apply the definition of δ_k to D. The converse holds because δ_k >= a_k. ∎

**Numerical instance (k=3, γ=1/2, λ=6; c_1=1, c_2=1/8).** β_3=min{6^-3, 6^-2·1, 6^-1·(1/8)}=1/216, so
a_3(m) >= min{ m^-3/432 , δ_3(m,6)/2 }.
**R3 ⇔ DSE_3 := [δ_3(m,6) >= c m^-3].** Combined with Theorem B and c_1=1: full TIK ⇔ for every k>=3, DSE_k(2k) holds (inductively).

## 5. Lemma E — rank-three deletion pieces

Delete with **pair priority**:
- while some pair P has 1 <= d_cur(P) <= m-1, delete the current edges ⊇ P (a *pair piece*);
- otherwise, while some vertex x has 1 <= ν(cur(x)) <= m-1, delete the current edges ∋ x (a *vertex piece*).

The process ends at C(F), and F\C(F) is partitioned into pieces.
- A pair piece has <= m-1 edges with a common pair, and distinct thirds.
- At a vertex step no bad pair exists, so the link graph L=cur(x) has minimum degree >= m on its vertex set. By ML, min(m, ⌊|V(L)|/2⌋) <= ν(L) <= m-1. Hence m+1 <= |V(L)| <= 2m-1 and |L| <= (2m-1)(m-1) < 2m².
- In a vertex piece, a vertex y∈V(L) together with m of its L-neighbours gives a COMPLETE m-petal sunflower with kernel {x,y}. It uses more than 1/(2m) of the piece.
∎

## 6. Route C/D attempt on DSE_3 — what holds, and the first unproved implication

**6.1 Pair branch.** Take one edge from each pair piece (cost <= m-1). The deleting pair κ(e) is then contained in no LATER-deleted edge, but it may lie in earlier-deleted representatives. So the representatives are only "forward-private". No ordering argument analogous to the graph depth-parity in §3 was found that makes the realised vertex and EMPTY kernels controllable. The graph proof works because each edge has ONE head. A triple has TWO non-deleting vertices. Both may collide across pieces, exactly the S030/S031 light-collision phenomenon (HL/LS).

**6.2 Vertex branch.** Taking one complete block per vertex piece costs < 2m. The packed-block interface (C512: t/(512m²) out of tm block edges, i.e. m^-3 of block mass) would then give only m^-4 of the piece mass. **So C512, even if proved, would not close the vertex branch of DSE_3 through this naive interface.** An m-saving must come from cross-piece cooperation, for example pair pieces through x that raise ν(H(x)).

**6.3 The essential obstruction (proved observation, not a counterexample).** Internal validity is not union-closed. A pair of H-degree 1 or a vertex with ν(H(x))=1 is allowed, but the union of two valid families can raise such a value to 2..m-1. The robust core captures exactly the union-closed part, and DSE_3 contains everything else. Explicitly:
- **S032 row-palette** (r copies of K_(m+1,m+1); |F|=rm(m+1)²).
  - Spreadness: d(u_i)=d(v_j)=m(m+1)=|F|/(r(m+1)), d(z) <= m, d(u_i v_j)=m, d(u_i z)=m for z∈Z_i, and every other pair has degree <= 1. The three 6m-spread conditions are:
    - vertices: r(m+1) >= 6m, true for r >= 6;
    - pairs: m <= |F|/(36m²), i.e. r(m+1)² >= 36m², true for r >= 36;
    - triples: |F| >= 216m³, i.e. r(m+1)² >= 216m², true for r >= 216.
    So it is 6m-spread for every r >= 6³.
  - Core-freeness: every triple contains a pair of F-degree 1 ({v_j,z} for z∈Z_i; {u_i,z*} for the private palette). So C(F)=∅.
  - Yet H=F is internally valid (S032 §4). **DSE_3 contains dense valid families; it is not a sparse case.**
- **S029 K_(m-1,m-1), S031 1024m stars, S030 repeated light, S024 K_N with private thirds:** every B triple {u,v,z} with a private or near-private light z has d({u,z}) or d({v,z}) <= 1 < m, so these are core-free too. DSE_3 inherits all programme B-class difficulties. The reductions remove only the non-spread and robust-core regimes.

**FIRST UNPROVED IMPLICATION (exact).** For every m>=3 and every nonempty 6m-spread core-free triple family D, there should exist internally valid H ⊆ D with |H| >= c m^-3 |D| for an absolute c. This is DSE_3. By Theorem D it is EQUIVALENT to R3. Neither a proof nor a counterexample was obtained. No sub-lemma in §6.1–6.2 is claimed false. Only the two naive interfaces are shown inadequate: one-head ordering, and block-then-C512 (which gives m^-4).

## 7. Routes A/IV (B256) and Level III

No new allocation lemma; B256 and C512 for unbounded m remain UNPROVED and unrefuted. Theorem A/D does NOT apply to the packed-block statement, which quantifies over arbitrary packings and original Q rather than over spread subfamilies. The packed-block reduction to R3 (Girão–Illingworth–Scott–Wood Lemma 9 decomposition with conditional c=min(1/54,γ/2)) is unchanged. S031's t/(4m³) and S032's m<=129 / m<=66 statements are unchanged.

## 8. Adversarial stress table (symbolic)

| Population | Where it falls | Outcome |
|---|---|---|
| (m-1)^k transversal | non-spread (d(x)=|F|/(m-1)) | A: link → K_(m-1,m-1) → one edge; agrees with a_k <= (m-1)^-k |
| N disjoint transversals | spread for large N, core-free (codegree m-1) | one edge per copy, ν=N; ratio (m-1)^-3; DSE_3 instance, valid |
| S032 row-palette | spread (r>=216), core-free | H=F valid; shows DSE_3 is not sparse |
| S031 1024m star family | core-free (private light) | its S031/S032 dense alternatives remain valid; no new claim |
| S030 {q,z}; S022 repeated light | core-free | HL obstruction unchanged |
| S029 K_(m-1,m-1), w=m-1 | core-free | full-pair rescue m(m-1) unchanged |
| S018/S019 mixed | core-free (mixed private) | unchanged valid alternatives |
| full S023 q-plane | A-class; unchanged | direct-petal A bound unchanged |
| S024 dense K_N heavy graph, private thirds | core-free (d({u,z})=1) | its all-representatives valid output (fraction 1/m) unchanged; DSE_3 instance |
| complete 3-partite K^(3)_(N,N,N), N>=6m | |F|=N³, d(x)=|F|/N, d(xy)=|F|/N², so 6m-spread; every pair degree N>=m and every vertex link K_(N,N) has ν=N>=m, so robust core = F | Prop C: H=F |
| k=2 K_N, stars, matchings, K_(m-1,m-1) copies | all Theorem B branches | proved; aux check covered N-branches only |
| m=2; F empty; |F|<(λm)^k | trivial / non-spread | H=F; H=∅; one edge |

## 9. Single family, budget, kernels
- Every output in Theorems A and B and Proposition C is ONE selected subfamily, not a union of independent alternatives.
- In Theorem B, each branch selects one family and every kernel is checked: vertex kernels and EMPTY. Pair kernels do not exist for k=2, because distinct edges cannot share two vertices.
- Powers of m:
  - Theorem A: exactly (λm)^-j times the inductive m^-(k-j);
  - Theorem B: m^-1 from the out-degree classes, times m^-1 from the big/small split or the few-stars fallback;
  - Theorem D: no m loss beyond Theorem A.
- EMPTY is handled explicitly in every branch.

## 10. Implications and next frontier
- TIK is proved here, SAME-ASSISTANT, for k<=2 only.
- Every-k TIK reduces exactly to the degenerate-spread classes DSE_k.
- R3 ⇔ DSE_3.
- The most valuable next obligation is **DSE_3**. Preferred entry: the *pair-private apex decomposition*. Each triple with a pair of F-degree 1 is written e = c(e) ∪ π(e), where π(e) is the private pair and c(e) the apex, so that F is an edge-disjoint union over apexes c of c * G_c. The task is then to design a simultaneous TIK_2-type selection inside the links G_c that controls cross-apex vertex links (ν(H(x))∈{0,1}∪[m,∞)) and EMPTY. The S032 row-palette and S031 families are mandatory controls.
- The pair-private class is NOT claimed to exhaust DSE_3: the vertex pieces of Lemma E and forward-private pair pieces remain.

Status: NO_NOVELTY_CLAIM / NOVELTY_UNCERTAIN; literature status of the k=2 theorem and of the reductions is UNCHECKED (N1 deferred by owner rule, not a claim of openness). No Lean, manuscript, correspondence or publication.
