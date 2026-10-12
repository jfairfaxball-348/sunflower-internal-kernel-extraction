# P001-S033 — second-pass validation (SAME ASSISTANT; NOT independent peer review)

Scope: every positive claim of [the S033 report](../../research/S033_LINK_REDUCTION_AND_RANK_TWO.md) is re-derived below, where possible by a different formulation. No reviewer other than the same assistant has examined these arguments, and no formal verification exists.

## A0 / Theorem A, via the link formulation of [TARGET.md](../../research/TARGET.md)
- Let E↦T∪E map H' to H. For every K' disjoint from T, the residual families agree: H(T∪K') = {E\K' : E∈H', K'⊆E} = H'(K'). So ν(H(T∪K')) = ν(H'(K')).
- Every exact intersection in H has the form T∪K' with K' ∈ I(H'), because members of L avoid T. So I(H) = {T∪K' : K' ∈ I(H')}.
- Hence "∀K∈I(H): ν(H(K)) >= m" is equivalent to the same statement for H'. This confirms A0 independently of the explicit sunflower lift.
- Theorem A arithmetic re-derived: d(T) > (λm)^-j |F| and |H'| >= a_{k-j}(m) d(T) give the stated bound. For |T|=k, d(T)=1 forces |F| < (λm)^k. No dependence on n.
- Corollary A1's c_0=1 term reproduces the single-edge case. CONFIRMED.

## Theorem B, re-derived by case
- **ML** checked by an explicit split of the at-least-3-edge configurations between {u,w} and an M-edge xy:
  - u~x, u~y, w~x gives the augmenting path w-x-y-u;
  - u~x, u~y, w~y gives w-y-x-u;
  - the symmetric cases follow likewise.
  So deg u + deg w <= 2|M|. With deg >= δ this forces |M| >= δ. The hypothesis |M| < ⌊n/2⌋ guarantees two unmatched vertices. CONFIRMED.
- **Star forests,** second formulation. In class ℓ, colour each vertex by depth parity. S_p consists of the out-edges of parity-p vertices. Each parity-p vertex has at most one S_p-edge, and its other end is its parent, of parity 1-p. So S_p is a union of stars centred at parity-(1-p) vertices, with pairwise distinct parity-p leaves. Distinct centres give disjoint stars. The 2(m-1) forests partition D, because each D-edge has one tail, one label and one tail parity. CONFIRMED.
- **Acyclicity:** heads are deleted strictly later or never, so following parents terminates. CONFIRMED.
- **Branch kernels re-listed:**
  - big-star union: centres (>= m) and EMPTY (one edge from each of m disjoint stars);
  - single big star: centre only;
  - matching: EMPTY only, with ν=|H| >= m;
  - m-core: vertices of degree >= m and EMPTY via ML (n_C >= 2|C|/Δ >= 2m);
  - (N1) star: centre only.
  Distinct graph edges never meet in two vertices, so there are no 2-point kernels.
- **Constants:** the minimum of the branch ratios, compared exactly: 1/(8(m-1)²) >= 1/(8m²) and 1/(4m²) >= 1/(8m²). The (N1) single-edge case: d(v) <= m-1 and e < 2m d(v) give e < 2m². The fallback: e < 8m(m-1)² and a matching of size > m give ratio > 1/(8(m-1)²). CONFIRMED.
- **m=2:** H=F, because the intersecting pair witnesses itself. CONFIRMED.

## Proposition C / Theorem D / Lemma E
- **Union-closure:** ν(G(T)) is monotone in G. **Deletion invariance:** cur ⊇ C at every step. **Terminal robustness:** no bad T remains. CONFIRMED.
- **EMPTY in the core:** k|M| covering vertices, each of degree <= |F|/(λm), give |M| >= λmγ/k >= m. CONFIRMED.
- **Core-freeness of D:** C(D) is robust as a subfamily of F, so C(D) ⊆ C(F)∩D = ∅. CONFIRMED.
- **Theorem D:** the four branches (F non-spread / large core / D non-spread / D spread core-free) are exhaustive. The constants (1-γ)β_k m^-k, γ and (1-γ)δ_k are re-derived. **k=3 numerics:** β_3 = min{1/216, 1/36, 1/48} = 1/216, and with γ=1/2 this gives m^-3/432. CONFIRMED.
- **Lemma E:** at a vertex step every L-degree equals a current pair degree >= m. ML plus ν <= m-1 gives |V(L)| <= 2m-1, so |L| <= C(2m-1,2) = (2m-1)(m-1). CONFIRMED.

## Stress re-check
- **Row-palette spreadness thresholds** recomputed: vertices r >= 6, pairs r >= 36, triples r >= 216. Every triple contains a pair of F-degree 1 ({v_j,z} or the private-palette pairs), so the core is empty. H=F is valid by S032 §4, a result not re-proved here.
- **S029 privacy** re-read from the S029 report: "ALL z globally private".
- **Transversal family:** non-spread branch, consistent with a_k <= (m-1)^-k.

## Negative findings and limits preserved
- The frozen auxiliary check exercised only the m=2, (N1) and (N2) branches of Theorem B. The spread branches were NEVER computationally exercised; their correctness rests on the written proof only.
- DSE_3 is neither proved nor refuted.
- The literature status of Theorem B and of the reductions is UNCHECKED (N1 deferred). Such reductions may be standard; no novelty is claimed.
- No result here proves R3, C512, B256 or every-k TIK.
