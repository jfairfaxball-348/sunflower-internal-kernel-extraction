# TIK — exact proposed target

Status: **SOURCE_POSED_CONJECTURE**. Source: JJSW26, Section 6. No proof is claimed.

For every integer k >= 1 there exists a real c_k > 0 such that for all integers m >= 2 and n >= k and every finite family F contained in binom([n],k), there exists H contained in F with

\[
|H|\ge c_k m^{-k}|F|
\]

and for all distinct A,B in H there exist **m distinct** S_1,...,S_m in **H** satisfying

\[
S_i\cap S_j=A\cap B\qquad(1\le i<j\le m).
\]

Only k may affect c_k. The ground set, family and m may not. Families are sets, not multisets. The empty family is allowed. Empty kernels count. The witnesses need not include A or B. No common projected intersection pattern, global partition, or polynomial-time procedure is required. Cardinality inequality is literal, equivalently using the ceiling of its right side; a nonempty F therefore requires nonempty H. When |H| <= 1 the pair condition is vacuous.

## Equivalent formulation

For K of size less than k define the residual link
\[
H(K)=\{E\setminus K:E\in H,\ K\subseteq E\}.
\]
It consists of distinct nonempty (k-|K|)-sets. Let nu denote the maximum number of pairwise disjoint members. Define I(H) as the set of A intersect B over **distinct** A,B in H. The condition is exactly
\[
\forall K\in I(H),\quad \nu(H(K))\ge m.
\]
Indeed, removing K from an exact-kernel sunflower gives a matching; adding K back reverses this and preserves distinctness. In particular H(empty)=H. Replacing H(K) by F(K) is the weaker external version and is not equivalent.

For nonempty F define a_k(m) as the infimum, over finite k-uniform F, of the maximum ratio |H|/|F| among internally valid H. TIK is equivalent to `inf_{m>=2} m^k a_k(m) > 0` for each fixed k. A finite example can constrain a constant; refuting TIK requires a family sequence forcing that infimum to zero.

## Boundary checks

- m=2: H=F works because A and B themselves witness their intersection. This is known directly from the definition.
- k=1: if |F|>=m take H=F; otherwise take one member (or empty when F is empty). Thus c_1=1 works. This elementary observation is background, not a discovery claim.
- If F itself is a sunflower with at least m members, H=F works.
- The complete k-partite transversal family with m-1 vertices per part is m-sunflower-free, of size (m-1)^k. Any internally valid H has at most one member. This forces a_k(m) <= (m-1)^(-k), so the desired m exponent cannot be improved in general. This is the standard source construction, not a counterexample to TIK.

## R3 — the single successor objective

Investigate TIK for k=3 and **all m>=2**, with one positive constant c independent of m,n,F. The intended bound is |H|>=c m^(-3)|F|. Known general internal bound specialises to (24m)^(-8); external bound to (600m)^(-3). Neither is a new result here.

In triples there are exactly three levels: for each realised pair K, its residual singleton link must have at least m members; for each realised singleton K, its residual graph must have a matching of size m; if the empty intersection is realised, H itself must have an m-edge matching. All three conditions must be checked in the final H. The R3 objective has not been attempted during bootstrap. It is a scoped investigation, not a claim that rank three is independently confirmed open or is the first unresolved rank.

## P001-S001 status

R3 was investigated through the authorised colour-certificate route. Unconditional constant-fraction repair of arbitrary largest good palette outputs fails; this is not a refutation of R3. [Analytical record](R3_FEASIBILITY.md) isolates L_AVG, an unproved sufficient averaging condition with explicit conditional density budget. R3 exact literature status remains STATUS_UNCERTAIN; no extraction theorem is claimed.

## P001-S002 status

The frozen L_AVG sufficient route was analysed, not established or refuted for general F. [L_AVG_FEASIBILITY.md](L_AVG_FEASIBILITY.md) proves an elementary lower expectation for sunflower-free F with constant 573599/663552, where `b_m(G_P)` is only zero or one. Unbounded ambient sunflower links invalidate this counting route for arbitrary families. Exact R3 literature status **STATUS_UNCERTAIN**; full TIK baseline unchanged. No new extraction theorem, N2, formalisation or publication. Single successor: heavy-link collision charging P001-S003.

## P001-S005 five-session correction status

Mandatory substantive-session audit S001–S005 is complete. Exact L_AVG/B_CHARGE methods are RETIRED on provisionally analytically supported AI-only negative evidence, not independent review; S002's sunflower-free restricted estimate survives. No positive R3 bound has been obtained, and exact R3 literature status stays STATUS_UNCERTAIN. No publishable independent theorem candidate justified by bounded N1; the only prepared successor is a **human A/B/C programme decision gate**, not an active proof route. Full TIK semantics, quantifiers and source-posed status unchanged. See [S005 audit](S005_PROGRESS_CORRECTION_AUDIT.md).

## P001-S006 scoped result
Block-selection lemma BSEL universal arbitrary-packing status UNPROVED / NOVELTY_UNCERTAIN. Only elementary restricted result for vertex-disjoint complete blocks, gamma=1, AI-only and not originality-promoted. Conditional BSEL=>R3 c=min(1/54,gamma/2) arithmetic checked but premise not proved. Retired prior palette methods unaffected; TIK and R3 status unchanged. [Specification](S006_BLOCK_COMPATIBILITY_SPEC.md), [analysis](S006_BLOCK_COMPATIBILITY_ANALYSIS.md). S007 human decision only.

## P001-S007 owner-directed continuation
The owner authorised technical research-method selection without repeated human decisions and explicitly deferred detailed novelty/prior-art reviews until a **complete proof candidate for the paper TIK target**. [S007's bounded-load block lemma](S007_LOW_LOAD_REDUCTION.md) yields gamma=1/3 only if every ground vertex belongs to at most m packed blocks; its same-assistant elementary proof does NOT imply general BSEL, R3 or TIK. High-load interaction remains the main unsolved subproblem, and S008 is only prepared. Full target, existing source statuses and publication stage unchanged.

## P001-S008 proof-first high-load status
The precise proposed HUB_RES high/low sufficient reduction requiring >=eta*t/m^3 compatible blocks all sharing ONE globally high-load vertex is refuted by a symbolic q-component family of whole pair-core and singleton-core sunflower blocks. The complete packing is nonetheless internally m-valid for all three realised types of pair intersection (2-point, singleton, empty). See [S008 high-load analysis](S008_HIGH_LOAD_RESERVOIR_ANALYSIS.md). This is NOT a counterexample to universal BSEL, R3 or TIK. New paper theorem count 0; no detailed novel/prior-art gate by owner instruction. S009 investigates a two-heavy-vertex-per-block multi-hub slice, NOT yet executed.
