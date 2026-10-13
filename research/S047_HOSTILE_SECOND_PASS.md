# P001-S047 — separate SAME-ASSISTANT hostile validation AFTER proof commit

2026-10-13. This adversarial pass was authored **after** commit `7becde9a2af626ef8a32bd90dc2a988ad686d96a` of `research/S047_MULTIHUB_GRAPH_CELL_EXTRACTION.md`. It is NOT an independent referee, formal proof, literature novelty screen or CI proof certification.

## Attack on the stated S047-A theorem

1. **Duplicated triples / false mass.** Arbitrary overlap of saturated and low ordinary vertex supports does not imply edge-disjoint whole triples. The theorem **explicitly assumes F_i are edge-disjoint**. A chosen hub a_C belongs to every A_i in its LOW component, so if graph edges repeated there, the same original triple would repeat, violating this assumption. Thus selected LOW mass is exactly g=Σ|G_i|, not merely ≤g. Without edge-disjoint presentation the displayed original-mass argument CANNOT simply be reused. PASS under the stated hypothesis; do not drop it silently.

2. **Saturated cell all proper subsets.** For each triple {a,x,y}, witnesses for EMPTY take m disjoint graph edges and **different hubs**. For vertex {x}, they take m different hubs and m different y-neighbours, so their only common vertex is x; identical reasoning for {y}. Pair {x,y} uses distinct hubs, pair {a,x}/{a,y} uses distinct graph neighbours with a fixed. {a} uses a graph matching. These cover exactly the 7 proper subsets of a 3-set including EMPTY. PASS. Saturated cells hence can have arbitrary ordinary support conflicts, subject to whole-edge distinctness: any cross intersection is a proper subset of a saturated selected edge. This is an already-standard *robust-core-type* mechanism, not a claimed fundamentally new universal gluing principle.

3. **LOW components graph may cease to be bipartite.** Overlapping bipartite G_i with inconsistent partitions may create odd cycles. The proof of the actual L_C invariants invokes **only** active degree >=m and matching number >=m of the union, which hold because each input G_i separately does. It does NOT apply any bipartite-specific theorem to the union. PASS; bipartiteness is a presentation premise, not required after union.

4. **Cross-LOW pairing.** Different components have disjoint **ordinary** vertex supports by the definition of connected components in the overlap graph, not because the original hubs are disjoint. If hubs coincide, exact cross kernel is singleton {hub} and a matching of m base graph edges in one component lifts to m exact petals. If hubs differ, the kernel is EMPTY. When ≥m distinct component-assigned hubs exist, take one full triple from each of m distinct-hub components, ensuring ordinary disjointness. PASS.

5. **Naive union when fewer than m hubs.** The proof *does not* merge L groups with an unverified EMPTY kernel. It selects only the largest one-hub group. That group has no EMPTY kernel and retains >=g/(m-1) triples. Quantitative loss is at most two powers (one to choose a hub in each low cell, one to avoid EMPTY), giving e/(m-1)^2. If at least one saturated cell exists its internal m-matching allows the full union, hence only a single 1/(m-1) loss. PASS.

6. **Edges of SAT and LOW intersect in large kernels.** An exact intersection of two distinct k=3 edges has size at most 2. It is a proper subset of SAT edge, with the complete exact SAT robust certificate already chosen. This covers EMPTY, singleton and PAIR without requiring L to be robust. PASS.

7. **m=2 and empty original inputs.** For m=2 every F is internally 2-valid because any realised pair itself supplies its two exact petals. For empty F select empty H and inequalities 0>=0. S047-A explicitly states m>=3; trivial boundaries survive. PASS.

## Attack on the high-hub cycle with 50% bad-pair mass

- r hub vertices, r*m² disjoint K_(m,m) bases with 2m vertices each give n=r(1+2m³). Each cell has TWO hub copies of m² edges, so e=2rm⁴, not r(m⁴+1). Half the edges have the competing second hub and deleting them incurs exactly 50% cost.
- Every hub h_i has edges from m² cells of block i and m² cells of block i−1, giving 2m⁴. Every ordinary vertex meets m edges per hub and precisely two hubs, giving 2m. Pair hub/ordinary has m edges; every ordinary base pair has two (one per hub). No hidden hub–hub pair occurs. Original E invalid for m>=3 at duplicated base pair. Ordinary pair-degree 2<m guarantees robust core empty for ANY subfamily.
- One original whole triple per i oriented to h_i with separate bases gives matching r. Each triple meets a hub from only r hubs, so ν(E)=r; integer hub cover r gives τ*≤r and fractional cover ≥ν=r. Correct.
- Spread: 2m⁴≤e/(6m) since r≥6m; m≤e/(36m²)=rm²/18; 1≤e/(216m³)=rm/108, all for m>=3 and r=216m⁴. All edges meet degree 2m⁴>m³; density e/n→m, and min original degree 2m. PASS.
- FINAL oriented H contains r m⁴ WHOLE triples. Same hub h_i, two distinct selected triples share exactly h_i plus at most one ordinary base point, because the bases are K_(m,m) and all cells have separate ordinary supports. PAIR {h_i,x}/{h_i,y}: m neighbours in that cell. Singleton {h_i}: m-matching in that cell. Different hubs h_i,h_j have disjoint ordinary cell supports and distinct hubs, so EMPTY; choose one whole edge from each of m distinct i. PASS. The construction is a positive original-mass rescue, **not** a disproof of HDSE3.

## Attack on the claimed counterexample to automatic gluing

Two one-hub K_(m,m) cells share only x and have distinct hubs a,b. A pair of edges through x from different cells intersects EXACTLY in {x}. Their final-H x-link consists of triples using ONLY a or b, so a sunflower with EXACT singleton x can have at most 2 petals (pairwise distinct hubs needed), even though each local cell has m-matching and degree m. Adding m private-disjoint hub cells gives an m-edge matching to certify EMPTY but no added x-triple. Thus even globally certified EMPTY does not repair the x-singleton defect. PASS. Deleting one of the two shared-x cells and keeping the private cells produces a valid SAME-F positive rescue; this is strictly a method counterexample.

## Remaining rigorous boundary

The theorem is a **new in-project restricted sufficient-structure proof**, not externally originality-certified, not unrestricted HDSE3/R3/full TIK, and not an experimental counterexample. It inherits complete graph-cell products, LOW overlap-component common hubs, and pairwise edge-disjoint cell decomposition. Arbitrary core-free triples need not have such a presentation and can have unsupported PAIR/singleton kernels. No implication that this captures Ω(e/m) ORIGINAL high-hub mass has been proved. All prior hard controls S023–S046 must remain in the unresolved list; no new detailed N1/N2 unless actual every-fixed-k TIK is proved. Local checkout not available (github.com DNS failure); local validations NOT RUN, actual hosted FINAL HEAD + merged-main PUSH remain mandatory.
