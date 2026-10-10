# P001-S004 — adversarial analytical check of S003 (single bounded gate)

**Verdict: PROVISIONAL_ANALYTICALLY_SUPPORTED.** The exact S003 inequalities survive the challenges below. This is another check **by the same AI assistant**, not independent mathematical scrutiny: no separately authorised independent person or mathematically independent external verification examined the proof. No originality, N2, positive R3 theorem, formalisation, publication or algorithm claim. **Decision D022: RETIRE the exact fixed-colouring L_AVG and B_CHARGE routes.** This decision does not imply the impossibility of a different route, nor refute R3 or TIK.

## A. Frozen statement and exact quantifier audit

The proposed universal L_AVG asserted one real eta>0 for *all* integers m>=3, n>=3 and every finite nonempty simple 3-uniform F, using lex-first **pre-colouring** maximum residual matchings, independent vertex colours chi:[n]->[M] with M=288m, good (rainbow and certificate-avoiding) edges G_P indexed by **unordered** three-element colour palettes P, and b_m(G)=maximum cardinality of a subfamily H subset G internally m-valid. Each realised exact intersection K of two distinct edges of H must have an m-petal sunflower **within H** of exact kernel K. Selected pair need not participate; K=empty is included. b_m(empty)=0 and singleton b_m=1.

A single infinite sequence m=t² (t integer >=2) with C_m(F_t)/|F_t| ->0 refutes an absolute eta. It need not cover m=3 or every fixed m. It says nothing by itself about the positive internal extraction conjecture, because L_AVG was a sufficient, not necessary, device.

## B. Alternative link-level verification (not independent review)

Let X_1,X_2,X_3 be pairwise disjoint of size N=t³, F_t all N³ transversals. Label [3N] and take m=t² <= N. For each proper K of an edge E:
- |K|=2: residual link has N singletons in the remaining part; its matching number is exactly N.
- |K|=1: residual link is the complete bipartite graph on two N-parts; a perfect matching gives nu=N and part-size caps nu at N.
- K=empty: N diagonal disjoint transversals form a matching, and any matching uses distinct vertices of X_1, so nu=N.

The fixed matching tie-break is immaterial: because N>=m every such psi(K) **is empty by definition**, before colouring. This covers all seven proper subsets per E. Goodness therefore reduces exactly to E rainbow. Each realised pair intersection of distinct ambient transversals is of size 0, 1 or 2 and is supported by m residual edges in F_t; so **F_t is internally m-valid**. This is a direct proof using the exact three residual-link types, not an appeal to ambient witnesses for a selected smaller H.

## C. Conditional-probability stress test and sunflower obstruction

For any *fixed* unordered P of three colours and each part X_i, set Z_{i,P}=#{x in X_i:chi(x) in P}. The colours are iid uniform independently over vertices, hence **unconditionally** Z_{i,P}~Bin(N,3/M). Do not condition on E rainbow or on data-dependent palette choice: such conditioning would change the law. Z variables for different P share colours and can be dependent; the proof never treats them as independent.

For an m-sunflower of tripartite triples, in each coordinate the m vertices are either identical or pairwise distinct: if two petals share a coordinate vertex, exact equality of all pairwise intersections forces all petals to share that coordinate. Distinct petals force at least one varying coordinate. Thus any sunflower whose edges all use a palette P requires Z_{i,P}>=m for at least one part. This statement covers kernel sizes 2, 1 and 0; it also implies the **stronger link-level check** for a palette slice: any realised pair K has <m potential third vertices; any realised singleton K has a residual bipartite matching <=min_{j!=i} Z_{j,P}<m; and a realised empty K has matching <=min_i Z_{i,P}<m, on the good event B_t^c. These are upper bounds; whether the indicated intersections are realised is irrelevant to absence of m-sunflowers.

Define B_t={exists i in {1,2,3}, P in binom([M],3) with Z_{i,P}>=m}. Then on B_t^c every G_P (even the larger family of all transversals with all vertex colours in P) is m-sunflower-free. Consequently every internally m-valid H subset G_P has at most 1 edge: if |H|>=2, pick two edges; their exact intersection demands an m-sunflower **in H**. Hence b_m(G_P)<=1, R_P=empty. Goodness filtering cannot increase sunflower existence.

## D. Exact tail/union estimate and expectation audit

For a fixed (i,P), an m-subset of X_i all landing in P has probability p^m with p=3/M. If Z>=m, at least one of binom(N,m) subsets succeeds. Thus without Chernoff or conditioning:
  Pr(Z>=m) <= binom(N,m) (3/M)^m <= (e N (3/M)/m)^m.
With N=t³, m=t², M=288t², the parenthesis is **e/(96t)**. There are Q=binom(M,3) palettes and exactly 3Q tested (i,P) pairs; by union bound, with **no independence assumption between tests**,
  Pr(B_t) <= q_t := 3Q(e/(96t))^(t²).
Since Q <= (288³/6)t^6 and (e/(96t))^(t²) decays faster than any inverse power, q_t ->0. For small t the RHS may be a loose bound (even >1); no step assumes it is a probability itself.

The good G_P partition rainbow edges, so pointwise sum_P b_m(G_P) <= sum_P |G_P| <= |F_t|. On B_t^c each b_m <=1, so sum<=Q. Therefore
  C_m(F_t)/|F_t| <= Q/t^9 + Pr(B_t)
  <= (288³/6)t^(-3) + (288³/2)t^6 (e/(96t))^(t²) ->0.
The inequality is nonnegative and uniform over all pre-colouring lex-first choices (which here all give psi=empty). For any claimed eta>0 some integer t>=2 violates C_m(F_t)>=eta|F_t|. The existence of an optimal b_m for finite slices is automatic; none is algorithmically computed. Real-valued lower bounds retain literal ceiling semantics.

## E. Frozen B_CHARGE pressure test

For this F_t, A_m(F_t)=F_t. All good edges are rainbow, with exact probability rho_M=M(M-1)(M-2)/M³ per ambient transversal. A rainbow edge is in exactly one palette, and there are at most Q occupied palettes that have exactly one good edge. Therefore deterministically sum_P |D_P| >= #rainbow edges - Q, and
  E sum_P |D_P| / t^9 >= rho_M - Q/t^9 ->1.
On B_t^c all R_P are empty. In any colouring the R_P lie in disjoint G_P, so sum_P |R_P|<=|F_t|. Therefore
  E sum_P |R_P| /t^9 <= Pr(B_t) <=q_t ->0.
For any finite fixed B, the putative inequality E sum|D_P|<=B E sum|R_P| eventually fails. This checks **the frozen union-of-recipient-edges**, not a substituted b_m capacity, and respects the nontrivial |H|>=2 requirement. The claim is neither an allocation algorithm nor a universal ban on different charges.

## F. Challenge matrix, boundary cases and limitations

| Suspected weakness | Result |
|---|---|
| Tie-break may change psi | Every relevant link has nu=N>=m, so psi=empty regardless of tie-break |
| Pair/singleton/empty links conflated | Exact nu=N in ambient F_t; all three have <m matchings/sunflowers in relevant sparse palette slices |
| Random P selected after observing chi | Tail is for *each fixed* P, then union over all palettes; no data-dependent conditioning |
| E rainbow condition biases Z | The occupancy event uses unconditional vertex colours; G_P is a subset of P-coloured transversals |
| Sunflower may fix every coordinate | Then all petals identical, contradicting distinctness |
| Palette events correlated | Union bound requires none of their independence |
| Expected capacity may be huge on B_t | Capped pointwise by |F_t|, already accounted for |
| Charge recipients counted repeatedly | Defined R_P as union; palette classes disjoint; no multiplicity inflation |
| Fixed m / m=2 | Statement m>=3; subsequence m=t²>=4 refutes uniform eta, not each fixed m; original target m=2 trivially H=F |
| Empty F or n<3 | Only empty F for n<3; C=0 and target lower bound 0; irrelevant to nonempty asymptotic obstruction |
| Ceilings / tiny H | b=0 for empty, 1 for singleton; two or more internally valid edges require an m-sunflower inside H |
| Original F_t m-valid? | Yes: all three ambient residual-link matchings attain N>=m; palette-slice invalidity does not transfer back |

**No precise invalid step located.** This is a bounded adversarial inspection of a previous assistant-derived argument. It does **not** constitute independent proof review, new external mathematics, N2, simulation, theorem formalisation, proof of literature novelty, or publication-quality certification.

**Governance:** D022 permanently retires the precise L_AVG/B_CHARGE colour-palette capacity route *as stated*. Preserve S002's sunflower-free restricted calculation as separate background; do not retroactively call that false. No automatic replacement technique is authorised in S004. Prepare only the unexecuted P001-S005 five-substantive-session progress/correction audit and human-governed route assessment.
