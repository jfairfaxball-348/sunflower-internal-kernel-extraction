# P001-S012 — quantitative heavy-pair certificate selection; simultaneous matching remains open

**Scope:** ONE bounded private-light, at-most-two-original-heavy-support whole-block session (2026-10-10). This is an elementary same-assistant auxiliary combinatorial argument, **not** a complete private-light BSEL theorem, rank-three R3 or the original every-fixed-k TIK paper theorem. No new detailed N1/N2, independent mathematical review, numerical enumeration, Lean or publication.

## Frozen original problem and selected intermediary

Let m >= 3, let B_1,...,B_t be pairwise edge-disjoint **complete** m-petal sunflower blocks of distinct triples, each with exact kernel cardinality 0, 1 or 2, and V_i its full support. Let Q={v:#{i:v in V_i}>m}. Assume every block meets Q in at most two vertices and every vertex outside Q is *block-private* (appears in exactly one block). No restriction on the number, mutual overlap, or degrees of hubs. A selected J retains EVERY triple of B_i for i in J; its H=U(J) alone must witness every realised exact kernel, with witnesses not required to contain a selected pair. The full S011 certificate is: (i) every realised heavy pair codegree >=m; (ii) every realised heavy singleton has a selected singleton-core block or actual residual matching f_v(J)+|D_v(J)|>=m; and (iii) every realised empty kernel has either a selected empty-core block or m pairwise disjoint mandatory heavy-core footprints. The attempted conclusion is |J|>=gamma*t/m^3 with absolute gamma>0 satisfying **all three** simultaneously.

The bounded frozen intermediary **PAIR_FILTER** asks only: for every such packing, can one select at least t/(m-1) entire blocks so that every *realised two-heavy-vertex pair* in final U(J) has actual codegree >=m? This is stronger in size than the hoped-for t/m^3 at ONE of the three certificates, and is not mislabelled the full density lemma.

## Elementary positive PAIR_FILTER proof, with an explicit bound

For every original unordered heavy pair e={a,b} subset Q, call block i **e-active** if it contains at least one triple containing both a,b. Since |V_i intersect Q|<=2, **each block is active for at most one heavy pair**. Let A_e be the active block indices; these classes are disjoint. A block not active for ANY heavy pair belongs to A_0. Let P_e subset A_e be the indices of blocks whose exact core equals e. If i is active for e and i is not an e-core block, it has **exactly one** triple containing e: two distinct triples containing e would intersect in e, forcing their complete block's kernel to be e. Conversely an e-core block supplies m distinct triples containing e. Different blocks supply distinct triples, by edge-disjointness.

Select whole blocks by the following independent rule for each e:
- if P_e is nonempty, retain all of A_e;
- if P_e is empty and |A_e|>=m, retain all of A_e;
- if P_e is empty and 1<=|A_e|<=m-1, retain exactly ONE arbitrary block from A_e.
Also retain every block in A_0. This is a finite existential choice, not a runtime/complexity claim. It does NOT require hub-disjointness, a single hub, or a common core size.

For every e, a selected e-core supplies m distinct third vertices; otherwise the total number of selected triples containing e is either ZERO/ONE, or at least m (one triple from each of at least m active, edge-disjoint blocks). Therefore if e is *realised as the intersection of two final triples* it has >=m distinct final triples containing e, yielding an exact e-kernel m-petal sunflower **inside H**. No ambient witnesses were used. For any realised pair containing a light vertex, S011 shows its witnessing triples must be in that light vertex's unique block, where the pair is that block's exact core, certified by its m petals. Thus all realised two-point kernels are certified.

For the retained size, every unchanged class retains all of its members. Every reduced class has cardinality s with 1<=s<=m-1, and retains one >=s/(m-1). Summing the disjoint classes A_0 and A_e proves the **literal** bound

    |J| >= t/(m-1) >= t/m^3   (m>=3).

No dependence on |Q|, n, t, degree, core type or overlap appears. Since J is a set of WHOLE blocks, edge-disjointness and the complete-m-petal definition persist. For t=0 the construction retains J=empty. For 1<=t<=3m^3 the traditional one-block construction is already valid at ALL realised kernels and gives 1>=t/(3m^3), independent of PAIR_FILTER. At m=2 the original TIK H=F is trivial, not an inference from this m>=3 lemma. The pair-only coefficient 1 is **not** gamma for simultaneous private-light BSEL.

## Pressure test against exact singleton and empty matching

PAIR_FILTER may select EVERY block in a packing yet the result be INVALID, so it cannot be promoted to the desired all-certificate selection:
1. **Singleton failure:** In the S010 SAT_CROSS family with N>=m+1 pair-core {a,b} and {a,c} blocks, singleton-core {b},{c} blocks and an empty-core block, every active heavy-pair class contains a pair-core block, so PAIR_FILTER selects the complete packing. Nevertheless singleton {a} is realised and its **actual residual graph matching** is exactly 2<m (only compulsory partner hubs b,c). Pair-codegrees and empty matching are correct. The S010 explicit selection retaining N+3 of 2N+3 blocks (>half) remains valid: this is not an absolute BSEL negative.
2. **Empty failure independently of singleton:** In S011's two disjoint N-spoke stars with m>=3,N>=max(m+1,3m^3), each e={a,u_i} or {b,w_i} contains a light vertex, while no heavy-pair e is active (Q={a,b}). PAIR_FILTER therefore selects ALL t=2N blocks. Every realised pair and heavy singleton is internally certified (actual link matching N), but empty is realised and the **actual 3-matching** is 2<m, equivalently all mandatory heavy cores lie among {a},{b}. Keeping one star yields a valid t/2 selection. Thus local pair filtering cannot be used to infer the global matching condition either.

These are symbolic witnesses for the **failed sufficiency of the pair-only selection to finish the theorem**, NOT a parametric refutation of the existence of some other simultaneously valid dense J. They explicitly preserve the S008/S009 all-valid full unions, S006/S007 positive restrictions and S010/S011 half-density controls.

## First remaining quantitative obstruction; exact status

A correct construction has bought at most an m-1 multiplicative loss at the *pair* level. What is NOT proved is that one can retain at least an additional absolute-order m^-2 fraction of those blocks while enforcing **both** S011 actual singleton matching identities and S011 true empty-core footprint matching, **without newly leaving 2,...,m-1 surviving members of a previously saturated active pair class**. Arbitrary deletions may destroy pair certification; selected heavy load is NOT residual matching, and many blocks containing a common heavy partner yield only one singleton residual matching edge. Rebuilding the pair filter can in turn disturb singleton/empty realisation. No composition lemma, robust closure, or absolute gamma for simultaneous all-three selection has been proved. This is the earliest unproved *quantitative* continuation of the tested architecture; the report does not restate the target as proved.

No full private-light BSEL, universal BSEL, R3, full all-k TIK, source novelty, independently established paper theorem, original algorithm, Lean verification, manuscript or application follows. Claim is same-assistant mathematical reasoning only; CI integrity checks do not review its proof. Exactly one separate bounded S013 handoff is left unexecuted.
