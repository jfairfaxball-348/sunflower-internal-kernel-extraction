# P001-S044 — separate SAME-ASSISTANT hostile validation (NOT independent referee)

2026-10-13. Performed AFTER separately committed S044 proof report `c2694bd91d6db59248622ff9fbe8c97a97473c7a` and refinement `3b5de65fb31064528c899804a92c48212e8dab44`. This is a new adversarial reasoning pass, not a fresh finite experiment or human-independent verification.

## A. Kill attempts against S044-A

1. **Unbounded original vertex degrees:** Allowed ONLY when an apex assignment has max load <=A m. One cannot infer an assignment from original pair codegree bound; dense Steiner (pairdegree=1) may require max assignment load >>m. Thus the theorem cannot be accidentally read as universal.
2. **Projected bases overlap at one BLUE vertex:** Not a counterexample. The bipartite matching only asserts bases are distinct and red apices private; overlapping BLUE bases are ordinary adjacent GRAPH edges passed to S033. Their singleton graph kernels lift exactly. Two distinct bases cannot yield a lifted PAIR kernel since they are distinct 2-sets and the red vertices are all distinct.
3. **Original pair overlap B=m-1:** Right degree of Q is at most m-1, left at most d. Maximal matching covers <=d+m-2 good incidences; using (A+1)m is safe. Example S043 K_(m-1,m-1) shows the matching step may spend order m; one must not remove it.
4. **m=2:** Direct H=F since each selected pair itself gives two exact petals; neither red matching nor core steps are needed. e=0 gives H empty.
5. **Witness-in-H check:** If two lifted triples intersect at EMPTY, graph J has m disjoint blue bases; their private red apices are distinct and absent from all blue bases, so all m lifted triples are pairwise disjoint IN H. If intersection is a BLUE singleton, the same transfer verifies m petals with exactly that singleton. No pair kernel is realised. One cannot use a sunflower in ambient G outside selected J.
6. **Dependence:** S044-A relies on S033 T2, a prior SAME-ASSISTANT proof; no independent mathematical certification is claimed.

## B. Kill attempts against S044-B

1. **Conflict colouring:** For a fixed triple T, each of its 3 original pairs has <=m-2 OTHER triples. Degree of conflict graph <=3(m-2), colour number <=3m-5 <=Q=3m-2 for m>=3. Each class is linear and simple. The conservative Q avoids a misplaced +3.
2. **Original vs selected population:** Density e>=2Qmn and degree balance Delta(F)<=A e/n refer to ORIGINAL F and its n nonisolated original vertices. Colour L size>=e/Q; at most n vertices peel once each, removing <=m-1 L edges. Therefore |C|>=e/Q-(m-1)n>=e/(2Q). The argument would FAIL if one silently substituted e_L and its n_L into ORIGINAL hypotheses.
3. **Small-n branch:** The average degree of C is 3|C|/n, and a nonisolated vertex of an m-core has degree >=m. Selecting its entire C-star realises ONLY singleton {x}, with m exact petals since C is linear. It does not realise EMPTY and does not need a matching.
4. **Large-n branch:** A maximal C-matching M has |C|<=3|M|Delta(F), so |M|>=n/(6AQ)>=m. In H=C, a realised singleton x has deg_C(x)>=m and its link is a matching due to linearity. EMPTY, if realised, has actual m whole members of M. Pairs cannot be realised. No unchecked link survives.
5. **Quantitative arithmetic:** Q=3m-2<3m; |H|>=e/(4AQ^2m)>e/(36A m^3) in small-n branch. In large-n branch |C|>=e/(2Q), far larger than e/(4AQ^2m) since 2AQm>=1. A>=3 is natural because Delta>=3e/n for every nonempty triple family. The constant c(A)=1/(36A) is independent of m only if A itself is fixed.
6. **Strength limitation:** S044-B does not solve all bounded original PAIR-degree families: density threshold is Theta(m^2) average degree, and max vertex degree / e/n must be bounded. Choosing A growing with m destroys uniform TIK constant.

## C. Explicit nonlinear HDSE3 check (SAME E, original population)

For t=10m^3, m>=3, X,Y,Z copies of Z/tZ, S={0,...,m-2}, E={(x,y,x+y+s)}:
- Each (x,y) determines m-1 unique z. The other two cross-part pair types similarly determine m-1 fibres (solve the group equation for y or x); within a part no pair belongs to an edge. e=t^2(m-1), n=3t, deg(x)=t(m-1), Delta=3e/n, so A=3.
- e>=2Qmn is equivalent to t(m-1)>=6Qm. For m>=3 and t=10m^3 this holds (at m=3 left 540, right 126; asymptotically the left grows cubic vs quadratic).
- For 6m-spread: d(vertex)/e=1/t, d(pair)/e=1/t^2 and d(triple)/e=1/[t^2(m-1)] meet respectively (6m)^-1,(6m)^-2,(6m)^-3. The third inequality is t^2(m-1)>=216m^3 and holds already at m=3. Every edge contains three vertices of degree t(m-1)>m^3. Any nonempty robust subfamily would require m petals at one of its original pairs, impossible because every edge's cross-part pair has entire ORIGINAL fibre m-1. Thus E is robust-core-free.
- E is NOT internally valid: choose two distinct shifts at fixed x,y (possible m>=3); their exact selected pair kernel {x,y} has only m-1 ambient petals. Hence E exhibits a *true nonlinear ORIGINAL HDSE3* need for extraction. The S044-B proof supplies a valid SAME-E H of cardinality at least e/(108m^3); this proves NO universal HDSE3 claim.

## D. Hostile named-method controls and coexistence

- S023/S024 projective-plane whole-block obstruction has a dense SAME-E partial-edge rescue. S029-S032 bipartite/shared/row examples, S034 twins, S035 high-cover, S037-S039 partial palettes/tensors, S040 star forests, S041 islands: none is silently assumed to obey density+bala​nce (A fixed) of S044-B; every earlier same-original-family repair survives. No cross-class union is asserted valid.
- S042 affine Steiner lines have pairdegree 1 and entire input fully valid: S044-B is compatible but does not produce a new same-E negative. S043 K_(m-1,m-1) apex-base incidences match at most m-1, and the maximal internally valid family is one edge; e=(m-1)^2 so this does not refute m^-3. It does not satisfy S044-B's large density.
- For m>=3, r=m-1 disjoint saturated pair stars each internally valid yield union matching number r<m, though EMPTY is realised. Pair-wise separately valid is NOT union-valid. The largest component retains fraction 1/(m-1) on SAME original E, so it fails as a target counterexample sequence; any assertion m^3 maxvalid/|E|->0 would be false.
- All FULL ORIGINAL F nonlinearity, colour collisions, singleton and EMPTY are distinguished. A GLOBAL universal HDSE3/R3 proof would require a new theorem for the sparse/unbalanced dense core and overlapping saturated PAIR strata; this report contains no such implication.

## E. Conclusion and independent-work status

The stated constants and explicit control withstand this SAME-ASSISTANT symbolic pass subject to the unrefereed S033 rank-two dependency. **Scoped advance survives; universal HDSE3/R3/TIK remains UNPROVED.** No numerical experiments (therefore no fictitious population/resources), no new detailed N1/N2, external independent scrutiny, Lean, Palomar, manuscript or publication. The standalone P001-S045 correction audit remains FUTURE, NOT EXECUTED.
