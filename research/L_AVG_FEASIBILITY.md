# P001-S002 — L_AVG aggregate palette-capacity feasibility

Date: 2026-10-10. Session outcome **RESTRICTED_SUNFLOWER_FREE_BOUND_GENERAL_L_AVG_UNRESOLVED**. This is ONE bounded analytical check of the exact fixed-certificate distribution. L_AVG for arbitrary F, R3, and full TIK are neither proved nor disproved. No new extraction theorem, formal proof or publication is claimed. See [focused N1](S002_N1.md).

## 1. Exact expression and controlled interpretation

Fix all maximum link matchings **before** colouring, lexicographically to remove choice ambiguity. Let M=288m and define psi(K), good E, G_P and b_m exactly as in [R3_FEASIBILITY Section 6](R3_FEASIBILITY.md). Put C_m(F)=E_chi sum_P b_m(G_P(chi)). L_AVG asks inf over m>=3 and nonempty F of C_m(F)/|F| >0. This definition is a way to express the target, NOT a proof or a bound. There are Q=binom(M,3) palettes. If L_AVG held with eta, choosing chi then P would give a single internally valid H of size >= eta|F|/Q >= (6eta/288^3)m^-3|F|. One cannot replace C_m with E sum_P |G_P|.

For each palette slice H subset G_P, all three tests must hold in **H**: each realised 2-point K has at least m third vertices; each realised singleton has an m-matching in its residual graph; if empty is realised, H has an m-matching of triples. The witnesses need not contain the selected pair. An arbitrary union of slices need not be valid.

## 2. Positive elementary calculation for the SUNFLOWER-FREE subcase only

Assume F contains **no** m-petal sunflower of any exact kernel and m>=3. Then:
* Any pair {x,y} occurs in at most m-1 edges of F, since m distinct third vertices give a pair-kernel sunflower.
* For each vertex x, its simple residual link graph L_x has maximum degree <=m-1 and maximum matching size <=m-1 (otherwise a sunflower with kernel x). Endpoints of a maximal matching cover all edges, hence |L_x|<=2(m-1)^2. This counts degree_F(x).
* A maximum matching of triples in F has size <=m-1 (otherwise empty-kernel sunflower). Its <=3(m-1) vertices cover F, giving |F|<=6(m-1)^3.

Fix E in F, condition on its three colours being distinct. For any other E', exact probability of the same palette is 1/M when |E cap E'|=2, 2/M^2 when the intersection has size 1, and 6/M^3 when disjoint. Overcounting by the bounds above gives

    Pr[exists E' != E with palette(E')=palette(E) | E rainbow]
      <= 3(m-2)/M + 12(m-1)^2/M^2 + 36(m-1)^3/M^3
      <= 3/288 + 12/288^2 + 36/288^3 =: delta.

Here a non-rainbow E' cannot have the same three-colour palette as rainbow E, so collision is well-defined. The certificate good-edge union bound from Section 2 of R3_FEASIBILITY, with 7 proper subsets and sum of cover sizes <=12(m-1), gives

    Pr[E good] >= 1 - [3+36(m-1)]/M > 7/8.

Thus `Pr[E is good and its palette is unique among all of F] >= 7/8-delta`. A good edge whose palette is unique among all of F contributes one distinct palette with b_m(G_P)>=1. The indicators for such edges have no duplicate palette, so pointwise

    sum_P b_m(G_P) >= #{good edges with unique F-palette}.

Taking expectations proves, for sunflower-free F,

    C_m(F) >= (7/8-delta)|F|
           = (573599/663552)|F| > 0.8644 |F|.

In fact each nonempty G_P has b_m(G_P)=1 in this subcase, because F has no m-sunflower and any internally m-valid subfamily with two edges would require one; so capacity equals the number of occupied good palettes. This last equality is NOT asserted for general F.

The calculation is a limited **elementary restricted-case estimate**, not claimed novel, independently scrutinised or formalised. It is consistent with existing sunflower-free extremal thresholds; none of the general project's mathematical status counters is advanced.

## 3. The exact failed step for arbitrary F

The upper bounds on pair codegrees, singleton degrees and total |F| are consequences of the **absence** of m-sunflowers. They collapse in families rich in m-sunflowers. For example, complete tripartite transversals on N vertices in each part with N arbitrarily larger than m have pair codegree N, singleton-link size N^2 and |F|=N^3. The preceding collision union bound may exceed 1 as N/m grows; it cannot supply a constant proportion of unique palettes. Yet for N>=m this ambient family itself is internally valid. A collision is therefore NOT automatically a loss of palettewise capacity: once same-palette links have m disjoint witnesses, large colour classes can be good rather than bad.

The missing step is a **density-sensitive dichotomy/charging estimate**: high palette multiplicity must pay for m internally disjoint residual witnesses at *every realised exact kernel of the final selected slice*, or be bounded as deletable mass. A proposed statement that 'there are enough internal witnesses in each dense palette' would only restate L_AVG unless accompanied by an explicit charge with bounded overlap and an absolute constant. Pair singleton links, one-point graph matching links and empty-kernel triple matching must be controlled **simultaneously**. The psi(K)=empty convention at ambient-matching-good kernels provides no certificate of their survival after colouring.

This analysis does not retry S001's failed universal all-colourings palette repair. Its adverse six-colour example has tiny aggregate capacity for ONE colouring but does not address random-colouring expectation. The restricted positive bound is not extended by multiplying worst-case losses.

## 4. Edge conditions, constants and safeguards

For empty F (including n<3), all G_P empty, b=0, and the desired inequality reads 0>=0. If F consists of one edge, psi(K) outside E is empty for its proper K; C_m(F)=Pr(E rainbow)=(M)_3/M^3, with optimal capacity one whenever rainbow. It exceeds 7/8 for m>=3. The full TIK/R3 case m=2 is trivial by H=F: any selected pair itself forms a two-petal sunflower. L_AVG was expressly quantified only for m>=3; the extension to m=2 is not silently asserted.

For arbitrary nonempty F, any singleton H is internally valid, but a singleton cannot meet a required real-valued density bound when eta|F|/Q>1. All size inequalities are literal, equivalently with ceiling. If L_AVG had been established, the maximal cardinality b_m(G_P), an integer, automatically respects that rounding. No algorithmic way of finding an optimal b_m is inferred. The lower bound 7/8 for good edges, while slightly stronger than the earlier loose 1/2, is only a union bound and does not imply L_AVG.

No new experimental population, random trials, enumeration, Lean, manuscript or external action was authorised or performed. Existing semantic fixtures remain the only mathematical computation. These paper calculations were checked within the same assistant only; no independent human/mathematical review or N2 is claimed.

**Verdict:** L_AVG for all F remains an exact, unproved sufficient route. S002 isolates a valid sparse/sunflower-free boundary and the unproved high-link charging obligation, then STOPS. R3 STATUS_UNCERTAIN, full TIK SOURCE_POSED_CONJECTURE / STRONG_EVIDENCE_OPEN / NOVELTY_UNCERTAIN.
