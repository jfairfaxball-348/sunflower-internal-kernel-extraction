# P001-S006 — deterministic block-interaction feasibility

**Outcome C — RESTRICTED_BSEL_ONLY.** One proof architecture (vertex-support overlap graph and deterministic block selection) only. Universal BSEL NOT proved/refuted. No experiments, random computations, colour/palette mechanisms, Lean or independent mathematical scrutiny.

## Three exact cross-block obstructions

**Pair kernel.** Fix m>=3 and a symbol a. Let B1 be m triples {a,p_i,q_i}, i=1,...,m, all residual pairs disjoint; let B2 be {a,p_1,r_1}, plus {a,u_j,v_j} for j=2,...,m, all remaining vertices private and disjoint. Both are complete singleton-kernel sunflowers; edge-disjoint. But a B1 edge and B2 edge intersect in {a,p_1}; exactly TWO union triples contain this pair, so no m-sunflower with exact pair kernel. Whole union incompatible.

**Singleton kernel and greedy obstruction.** For every t>=m take t blocks B_i, each an EMPTY-kernel m-matching of triples. Each contains one special edge {x,a_i,b_i} and m-1 completely private disjoint triples, all vertices except x globally distinct. An s-block union has realised singleton x iff s>=2, and its residual graph at x has matching number exactly s. Its empty kernel already has an m-matching inside any one block. Thus valid choices have EXACTLY s=0, s=1 or s>=m. Inclusionwise one-block maximal compatible selection may have size ONE though all t blocks are compatible. This refutes one-at-a-time GREEDY EXTENSION as sufficient, NOT BSEL.

**Empty kernel.** Take s=2,...,m-1 vertex-disjoint blocks with NONEMPTY individual kernel. Cross-block pairs realise empty; every triple in any fixed block shares its kernel, so a matching uses <=1 edge per block; maximum matching size =s<m, and the selected union is incompatible. Empty witnesses may not be silently borrowed from ambient family.

## Elementary restricted positive proposition (rigorous argument, not novelty claimed)

If different blocks additionally have pairwise VERTEX-DISJOINT supports, exact BSEL is true with gamma=1.

*Proof.* t=0: select empty. For 1<=t<m choose one complete block. It witnesses all its own pair intersections; |J|=1>=t/m^3. For t>=m select ALL t blocks. Every intra-block pair intersection is its block core and witnessed by its m petals; all cross-block intersections are empty. Select one arbitrary triple from each of any m distinct blocks; disjoint supports give an m-matching entirely in the union, witnessing empty. Thus all realised kernels are certified and |J|=t>=t/m^3. QED. This is an elementary special case, not R3, no original theorem claim, no N2.

## First unresolved implication in the ONE architecture

Join two indices whenever block vertex supports intersect. An independent set gives disjoint blocks, but the overlap graph can have arbitrary degree/chromatic number: all t blocks in the singleton construction share x while all t are jointly compatible. The naive bound t/(Delta+1) can be only one despite t arbitrary. Independently, choosing 2,...,m-1 disjoint blocks with nonempty kernels can fail the empty requirement. A density-preserving GROUP SELECTION/CLOSURE estimate would have to retain >=gamma*t/m^3 blocks and simultaneously create EVERY newly realised exact pair, singleton and empty sunflower. No such estimate established. Do not reattempt as renamed L_AVG/B_CHARGE or adjust the quantifiers.

## Symbolic controls

Complete tripartite F=X1×X2×X3 with |Xi|=N divisible by m and N>=m: for each pair (x1,x2), group third vertices into blocks of m; entire family is packed into complete pair-kernel blocks. Selecting all gives pair-link third vertices N, singleton-link matching N, empty matching N: a positive TEST of this packing, not universal proof. Standard transversal F with |Xi|=m-1 contains no m-sunflower, so t=0 and BSEL vacuous; its size (m-1)^3 is compatible with Girão remainder. No finite enumeration/simulation was performed. Every selected pair need not witness its own kernel.

**Final status:** C—RESTRICTED_BSEL_ONLY (elementary gamma=1 for vertex-disjoint blocks). Exact universal BSEL UNPROVED, NOVELTY_UNCERTAIN; full TIK/R3 unchanged. No automatic second proof architecture, repair or new mathematical pivot. S007 requires fresh human decision.
