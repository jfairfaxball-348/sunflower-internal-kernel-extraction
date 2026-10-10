# P001-S001 — rank-three colour-certificate feasibility

Date: 2026-10-10. Outcome: **MECHANISM_OBSTRUCTION_AND_REMAINING_LEMMA**.
R3 remains unresolved here and its exact literature status remains **STATUS_UNCERTAIN**.
There is no new extraction theorem, originality claim, formal verification, construction-complexity claim or publication claim.

## 1. Obligation and source gate

For every integer m>=2 and finite F contained in binom([n],3), seek H contained in F with |H|>=c*m^(-3)|F|, for one absolute c>0, such that every exact intersection K of distinct members of H satisfies nu(H(K))>=m. All links and witnesses in this conclusion belong to the final H. The selected pair need not belong to its witnessing sunflower.

The focused N1 audit is in [S001_N1.md](S001_N1.md). No inspected source settles this exact statement. The general source-posed question retains STRONG_EVIDENCE_OPEN / NOVELTY_UNCERTAIN; a no-hit does not establish rank-three openness. This permits this bounded mechanism analysis, not research-result promotion. The known internal bound is (24m)^(-8); JJSW26 Theorem 1.7 gives (600m)^(-3) with ambient witnesses. No change of target is made.

## 2. Three levels that must hold simultaneously

| Realised K | Residual family in H | Exact requirement |
|---|---|---|
| {x,y} | distinct singletons | d_H(x,y)>=m whenever d_H(x,y)>=2 |
| {x} | simple graph | nu(H({x}))>=m whenever that graph has two disjoint edges |
| empty | triples H | nu(H)>=m whenever H has two disjoint triples |

The singleton trigger is not merely degree at least two: two residual graph edges must be disjoint to realise exactly {x}. The pair trigger is automatically two distinct residual singletons. A graph with arbitrarily many edges can still have matching number one (a star), so large link cardinality cannot replace matching. The usual maximal-matching cover has size at most 2(m-1) in a bad graph link, and at most 3(m-1) at the empty kernel. These are elementary controls, not discoveries. For an arbitrary graph, the analogous internal condition is that vertices of degree at least two have degree at least m, and a realised empty intersection requires an m-matching. The Chvatal–Hanson threshold controls sunflower-free graphs, not simultaneous extraction.

## 3. What the colour certificates actually give

This is a rank-three replay and bookkeeping of JJSW26 Lemma 2.1 with ell=0, not a new lemma. For every K of size 0,1,2 choose, before colouring, a maximum matching of F(K). Set psi(K) to the union of its residual edges when its size is <m; otherwise set psi(K)=empty. If F(K) is empty, its union is empty. For a bad nonempty link, psi(K) hits every residual edge and has size at most (3-|K|)(m-1).

Use M=288m colours, the source's value for k=3, ell=0, independently and uniformly on vertices. Call E good if E is rainbow and, for each proper K subset E, colours of psi(K) outside E are disjoint from the three colours of E. Write G_P(chi) for all good edges with the same three-colour palette P.

For a fixed E, the sum of cover-size bounds over its seven proper subsets is at most
3(m-1)+3*2(m-1)+3*(m-1)=12(m-1).
A union bound gives bad probability at most [3+36(m-1)]/M<1/2. Hence
E_chi sum_P |G_P(chi)| >= |F|/2.
There are Q=binom(288m,3) palettes. Some colouring and palette therefore give |G_P|>=|F|/(2Q)>=3|F|/(288^3*m^3). This is the familiar external-selection step, with loose constants sufficient for bookkeeping.

Why an ambient-bad kernel is excluded: take E in G_P containing K, and v in (E minus K) intersect psi(K). Any other E' in G_P containing K has a vertex of the same colour as v. If v were outside E', E' would violate goodness. Thus v belongs to every such E', so K cannot be their exact pair intersection. The conclusion is nu(F(K))>=m for realised K in G_P. It says nothing about nu(G_P(K)) for a kernel that was ambient-good, since its psi(K) was empty.

## 4. An explicit failure of largest-palette selection and constant repair

For each m>=3 take three disjoint sets X_1,X_2,X_3 of size m and let F_m be all transversals {x_1,x_2,x_3}. Its size is m^3. Every subset K of a transversal with |K|<3 has residual matching number exactly m: use a diagonal matching across the remaining parts; no matching can be larger than a remaining part. Thus every relevant psi(K) is empty, independently of maximum-matching choices. F_m itself is internally valid at all three levels.

Choose one exceptional vertex e_i in each part. Colour the other m-1 vertices of X_i with colour i and colour e_i with colour i+3, for i=1,2,3. This uses only six of the M colours, which is allowed. Every transversal is rainbow and good. Palette {1,2,3} is the unique largest class
G_m=(X_1 minus {e_1}) times (X_2 minus {e_2}) times (X_3 minus {e_3}),
with |G_m|=(m-1)^3. Every other nonempty palette fixes at least one exceptional coordinate and has size at most (m-1)^2.

G_m has no m-petal sunflower. In any sunflower, the coordinate in a fixed part must either be the same in all petals or distinct in all petals. Indeed, equality in two petals places that vertex in the common kernel and hence in every petal. There are only m-1 vertices per part, so all coordinates must be constant across m petals, contradicting their distinctness. This is the standard transversal obstruction, reused here as a mechanism control.

Consequently every internally valid H subset G_m has size at most one: any two distinct edges would require an m-petal sunflower in H, impossible in G_m. A singleton is valid, so the maximum is exactly one. The best repair fraction is (m-1)^(-3), tending to zero. Therefore the assertion that EVERY output of the good-colouring/largest-palette step admits an m-independent positive repair fraction is false, even when every ambient edge is good.

The failure simultaneously reaches all three levels. Each realised pair has m-1 singleton witnesses; each realised singleton has a complete bipartite residual link with matching number m-1; the global matching number is m-1. For m>=3 these kernels are realised. For m=3 this is the eight-triple family on three parts of size two inside the 27-triple family on parts of size three.

This is NOT a counterexample to R3 or to existence of a better colouring. The original F_m is valid. Even the single repaired edge has |H|/|F_m|=m^(-3), so this example does not force a worse final exponent. In particular it would be incorrect to multiply worst-case losses and claim the resulting exponent is an unavoidable lower bound: on this example the initial palette loss is only a constant. The correct conclusion is the failure of an unconditional constant-factor repair lemma. Its originality is neither asserted nor audited as an independent contribution.

## 5. Density budget and failed alternatives within this route

| Stage | Proven size accounting | Limitation |
|---|---|---|
| Certificate goodness | expected total good mass >= |F|/2 | expectations do not imply simultaneous retained matchings |
| Select one palette | divide by at most Q=binom(288m,3) | already spends an m^(-3) worst-case factor |
| Repair inside that palette | universal constant fraction unavailable | Section 4 disproves it for arbitrary permissible outputs |
| Reapply external lemma | each pass gives only an additional guaranteed factor (600m)^(-3) | no uniform pass count or compensation estimate established |
| Add ambient witnesses | may restore one matching | added edges create further kernels; no closure-size or density control established |

Repeated restriction eventually reaches a vacuously valid singleton, but termination is not a uniform retention proof. Recomputing certificates inside a changing retained family makes them depend on that family and invalidates applying the fixed-certificate expectation as if they were chosen before colouring. No monotonic witness-preservation argument has been supplied.

A further elementary diagnostic: fix K of size s, a fixed palette P containing its distinct core colours, and t disjoint residual witnesses in F(K). Before goodness filtering, and conditional only on those core colours, each residual witness has the required remaining colours with probability (3-s)!/M^(3-s). The count is binomial because residual witnesses are disjoint. Its mean is t*(3-s)!/M^(3-s). Thus even reaching mean m by this fixed-palette argument calls for ambient t at scales m^2, m^3, m^4 for s=2,1,0 respectively. These are diagnostic expectations, not necessary conditions for R3, not a guarantee after goodness filtering, and not valid conditional estimates for a palette selected from the data. Simply inflating the ambient parameter also increases M in the source method; no repair is proved by this calculation.

## 6. One precise remaining averaging lemma (L_AVG)

The failed all-colourings repair assertion should not be retried. A sufficient, strictly unproved route is the following joint averaging statement.

For a finite family G, define b_m(G) to be the maximum cardinality of an internally m-valid subfamily of G, with b_m(empty)=0. Fix maximum matchings defining psi above before colouring (for definiteness the lexicographically first maximum matching in the labelled ground set). For M=288m and the resulting G_P(chi), ask whether there exists an absolute eta in (0,1] such that, for all m>=3 and all finite triple families F,

    E_chi [ sum_{P in binom([M],3)} b_m(G_P(chi)) ] >= eta * |F|.    (L_AVG)

No algorithm for b_m and no efficient choice of certificates is asserted. This is an exact mathematical quantity. This statement controls aggregate optimal retained sizes across palettes; it does not require preserving a fixed fraction of each class. It is sufficient for R3, not claimed necessary or equivalent. Its truth, novelty and useful accessibility are all unestablished. A no-progress verdict on it would be acceptable.

Conditional density calculation: a colouring attains at least its average. For that colouring some palette has b_m(G_P)>=eta|F|/Q. Taking an optimal H in that palette gives

    |H| >= eta|F|/binom(288m,3) >= [6*eta/288^3] * m^(-3) * |F|.

Thus c=6*eta/288^3 would suffice. The denominator estimate uses Q<=M^3/6. The known estimate controls sum |G_P|, not sum b_m(G_P); replacing these quantities is exactly the unproved step. For the six-colour construction in Section 4, the sum of capacities equals eight while |F_m|=m^3; therefore even L_AVG cannot be replaced by a claim for EVERY colouring with many good edges. Randomness/joint selection and density compensation matter.

## 7. Boundaries, verification and stop

If F is empty, choose H empty. If m=2, take H=F; the selected pair itself witnesses its kernel. Any nonempty F admits a singleton, which is valid but supplies the target size only when the numerical lower bound is at most one. Cardinality inequalities are literal: an integer |H|>=r is equivalent to |H|>=ceil(r). The conditional averaging calculation automatically respects this, since the finite maximum is an integer; eta<=1 makes its proposed c small enough for the m=2 control. If n<3, F is necessarily empty.

All examples here were constructed and checked symbolically; no new population was enumerated. Only pre-existing semantic fixtures may run. The checks used in this session do not verify these mathematical arguments formally. The same assistant rechecked the coordinates, matchings, quantifiers and constants; no independent mathematical review was obtained and no new theorem is promoted. N2 and independent scrutiny remain mandatory if an actual extraction theorem is later achieved. The bounded S001 analysis ends here. L_AVG is a proposed S002 obligation, not an executed successor.
