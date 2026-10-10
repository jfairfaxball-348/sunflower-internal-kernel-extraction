# P001-S007 — bounded-load block selection and remaining unrestricted obstruction

## Authority and objective
The owner instructed on 2026-10-10 to keep working toward the paper theorem (full TIK) and not spend sessions on detailed prior-art/novelty checks before a complete proof. This supersedes the S006-prepared S007 human technical-choice gate. Exactly one bounded **mathematical** session: test an independent high/low vertex-incidence strategy, without claiming the unrestricted BSEL, R3 or TIK. **No new N1/N2 run.** The previously read Girão sunflower decomposition and exact BSEL specifications are used only as existing project background, not falsely claimed new work.

## Exact auxiliary lemma (restricted BSEL with bounded vertex block multiplicity)
Let m>=3, and let B_1,...,B_t be ANY edge-disjoint prescribed complete m-petal sunflower blocks of triples; block kernels may have cardinality 0, 1, or 2. Write V_i for the union of vertices in all m triples in B_i, so |V_i|<=3m. Assume the **global vertex block multiplicity**
\[
r(v):=|\{i:v\in V_i\}|\le m\qquad\text{for every vertex }v.
\]
Then there exists J subset [t] with |J| >= t/(3m^3) such that H=union_{i in J} B_i is internally m-sunflower-valid for EVERY exact pair intersection realised by H, including the empty kernel. This statement concerns the whole prescribed blocks; it does not require A or B to be witnessing petals, and has no dependence on n or t.

### Complete elementary proof
For t=0 choose J empty. For 1<=t<=3m^3 choose one arbitrary whole block. Any two distinct triples in a complete sunflower block have the block's exact core K, witnessed by its own m petals. No other pair type occurs. Moreover 1>=t/(3m^3).

For t>3m^3 form the finite simple conflict graph G on [t], joining i and j if V_i intersects V_j. Since any support V_i has at most 3m vertices and each vertex lies in at most m blocks, the number of neighbours of i is at most 3m(m-1). Thus the greedy independent-set bound gives
\[
\alpha(G)\ge\frac{t}{3m(m-1)+1}\ge\frac{t}{3m^2}>m.
\]
Choose any independent set J of at least this size. Different selected blocks now have vertex-disjoint supports. A pair of triples inside a block has that block's exact core, witnessed by its m triples. A pair in different blocks has empty intersection, witnessed by taking ONE arbitrary triple from each of m distinct selected blocks; those m triples are vertex-disjoint. Hence every realised exact kernel is internally m-witnessed. Furthermore |J|>=t/(3m^2)>=t/(3m^3). QED.

The argument is also valid for a **subpacking of low-load blocks** L subset [t]: if its induced global vertex multiplicity is <=m, then a valid whole-block subcollection of cardinality at least |L|/(3m^3) exists. In particular, if |L|>=delta*t for some fixed delta>0, it yields at least (delta/3)m^-3*t compatible original blocks. No such positive delta is known for *every* packing.

## Independent pressure test — why the lemma is not the paper result
Take t arbitrary blocks of m triples each, ALL with common pair core {a,b}, and otherwise all third vertices distinct. Then r(a)=r(b)=t, which can far exceed m; yet selecting all t blocks is internally valid because every pair intersection is {a,b}, witnessed by any m triples. Therefore **high vertex load is not an obstruction in itself** and a proof must exploit compatible high-load reservoirs rather than delete every high-load block.

Conversely, the low-load argument's independent-set strategy deliberately discards all overlaps; it does not establish that a constant fraction of arbitrary blocks can be retained after enforcing the singleton-link and empty-link requirements. There is no implication from this restricted result to universal BSEL unless one first proves an entirely missing positive-density low-load reduction or a high-load compatibility mechanism. Trivial single-block survival for small t is necessary to cover the integer ceiling; it does not resolve large t.

## Status and consequence
**One restricted, elementary, same-assistant on-paper auxiliary argument only; NO unrestricted BSEL, NO R3, NO full TIK; no claim of originality or publishability and no independent review.** The missing case is packings where a large fraction of blocks touch vertices occurring in >m blocks, possibly with mixed kernel sizes and cross-block pair/vertex/empty intersections. Conditional BSEL=>R3 from S006 remains conditional. Parent headline and paper target unchanged.

Next one bounded S008 mathematical proof obligation: an exact high-load vertex-reservoir selection mechanism that *jointly* enforces pair-link degree, singleton-link matching and empty matching for the final selected whole-block union. Source/novelty checks remain deferred until a complete TIK proof candidate; method selection does not require another human A/B/C decision. Stop without executing S008.
