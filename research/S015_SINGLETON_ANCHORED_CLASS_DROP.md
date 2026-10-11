# P001-S015 — singleton-protected preserve-every-class is false: mandatory-core empty obstruction

**ONE bounded proof-first mathematical gate, 2026-10-11.** The immutable paper target remains the exact every-fixed-`k` TIK with \(|H|\ge c_km^{-k}|F|\), all exact intersections including empty witnessed by `m` distinct sets of **the selected H**, and constants dependent ONLY on `k`. R3, universal BSEL, and the private-light at-most-two-original-heavy whole-block BSEL are auxiliary and remain unproved/unrefuted. No detailed new N1/N2, original-paper theorem claim, Lean, manuscript, contact, submission, or independent proof review.

## Quantified attempt and first false implication

For all integers `m>=3`, all `t>=0`, and every pairwise edge-disjoint packing of `t` COMPLETE `m`-triple sunflower blocks of kernel size `0,1,2`, write `V_i` for whole supports, `r(v)=#{i:v in V_i}`, `Q={v:r(v)>m}`. Assume `|V_i intersect Q|<=2` and each vertex outside Q occurs in only one block. No restriction on the number/overlap/load of Q. Partition into S012's unique heavy-pair active classes `A_e` and the pair-inactive `A0`.

Freeze **SINGLETON_ANCHORS_KEEP_ALL_CLASSES (SAKAC)**, a strong preserve-or-drop intermediary: IF (a) every nonempty `A_e` has an entire original `e`-core block, and (b) for EVERY `v in Q` the pair-inactive `A0` contains a complete singleton-core `{v}` block, THEN there exists a selection `J` of WHOLE original blocks with `|J|>=t/m^3`, every realised exact pair/singleton/empty kernel internally `m`-witnessed, and at least one original `e`-core block retained from EVERY nonempty `A_e`. In particular, its proposed preliminary implication asserts that having all singleton anchors prevents any need to drop an entire saturated pair-core class; the global empty matching would somehow be repairable without dropping classes.

**SAKAC IS FALSE for every m>=4** — even WITHOUT its density condition. This is the earliest false implication of this one tested class-preservation mechanism. It does NOT disprove arbitrary preserve-OR-DROP or an absolute-density `gamma` in any of the three BSEL levels.

## Explicit parametric test: saturated overlapping clique plus all hub anchors

Fix ANY integer `m>=4`, set `q=m-1>=3`, and choose arbitrary `N>=m+1` (unbounded at fixed m). Take hubs `X={h_1,...,h_q}`. All auxiliary vertices mentioned next are mutually distinct block-private **light** vertices.

* For every unordered `e={h_u,h_v}` of X and every `a=1,...,N`, construct a whole `e`-core block `P_{e,a}` of `m` triples `{h_u,h_v,x_{e,a,j}}`, `j=1,...,m`.
* For every `v in X`, construct one `A0` singleton-core block `S_v` of `m` triples `{v,y_{v,j},z_{v,j}}`, `j=1,...,m`.

These are all distinct triples in complete edge-disjoint prescribed blocks, of the TWO nonempty kernel sizes; empty-core blocks are ALLOWED by the general quantifier but are absent in this counterexample (including one would defeat the intended global-empty obstruction). Every P support meets Q in exactly two hubs and every S support in exactly one. Since `r(h_v)=N(q-1)+1>m` and every private light has load 1, the ORIGINAL set Q is exactly X. Arbitrarily large N produces arbitrarily large t and heavy loads, while hub supports overlap on the full `K_q`. Here

`t=N*binom(q,2)+q`, `A_e={P_{e,a}:1<=a<=N}`, and `A0={S_v:v in X}`.

Both SAKAC hypotheses hold: each `A_e` has N genuine `e`-core blocks; every heavy hub has an actual complete pair-inactive singleton-core `S_v`, so the S013 condition P1 holds strongly. S013 P2 does **not** hold: there is no selected empty-core block, every A0 mandatory heavy core is one of the q distinct singleton footprints, and `q=m-1<m`.

## All-local certificates pass in the full union but empty fails

Choose every block. For each heavy pair `e`, the final codegree is exactly `d_H(e)=mN>=m`; private-light pair intersections are certified by their own complete block. Each heavy singleton `{v}` is realised among triples from two distinct `e` classes, and S_v's m pairwise disjoint residual pairs give the TRUE `nu(H({v}))>=m`. For every private light, S011 supplies all singleton/pair certificates automatically when realised.

The empty intersection is realised: e.g. one triple from S_u and one from S_v with `u!=v` are disjoint. But **every triple contains at least one of the q hubs**, so any matching of triples has at most q members. Exactly q are available by choosing one triple from each of the q distinct S_v blocks with private residual vertices. Therefore `nu(H)=q=m-1<m`. Equivalently S011's true mandatory-core matching number is exactly m-1: all `C_i=K_i intersect Q` are singleton or pair subsets of X, and the singleton footprints `{v}` show the maximum q. Pair and singleton validity do NOT imply empty validity.

## Why even one e-core block in EVERY class is impossible

Let J be ANY subcollection containing at least one P_{e,a} from each of the `binom(q,2)` saturated original classes; it may retain or delete ANY anchors S_v. At a given hub v there are q-1=m-2 DISTINCT other-heavy partners, all witnessed by retained pair-core petals. As q-1>=2, the singleton `{v}` is genuinely realised (choose one triple on `{v,u}` and one on `{v,w}` with distinct u,w). If S_v is omitted, every residual edge in the link of v contains one of those q-1 partner hubs, so S011 gives its ACTUAL residual matching rank exactly q-1=m-2<m. Therefore EVERY S_v is mandatory in any internally valid selection preserving all e-classes. Yet even after retaining all q anchors, all selected triples still contain at least one vertex of X, while two distinct S anchors realise empty and `nu(H)<=q=m-1<m`. Contradiction.

Thus NO internally valid J can retain a pair-core block from each saturated class. This strengthens the location of S014's class-preservation failure in a **different** dimension: S014 had a true empty-core matching and lacked unprotected singleton links, while here ALL singleton hubs are perfectly protected and the global empty matching is the independent obstruction. It is not a new refutation of the already-known S011 general local-to-global fallacy; it specifically refutes the additional class-retention prescription of this S015 intermediary.

## Mandatory density-positive selection — do not confuse with BSEL failure

Fix any hub h_1, select ALL N pair-core blocks for EVERY edge `{h_1,h_j}` with j=2,...,q, and select the entire S_{h_1} singleton-core block, omitting every other original block. Call the selection J_star. It retains

`|J_star|=N(q-1)+1>=t/q=t/(m-1)>=t/m^3`.

Every selected triple contains h_1, so the empty intersection is **absent** and no empty matching is required. Every realised heavy pair `{h_1,h_j}` has true final codegree mN. The only realised heavy singleton is `{h_1}`, certified by the selected S_{h_1} m residual pairs (alternatively q-1 partners alone are insufficient). Each other heavy hub h_j occurs with the same partner h_1 in every retained triple, so no singleton `{h_j}` is realised. Light pairs/singletons, when realised, are supported by their own complete original block. Thus J_star is entirely internally m-valid and retains a strong `>=1/(m-1)` proportion, at fixed m for arbitrarily large N. This gives `m^3 max_valid|J|/t >=m^3/(m-1)`, not a tending-to-zero sequence.

As a second consistency check, the same graph would become globally empty-certified if one additionally selected an entire empty-core block disjoint from all other supports. That extra assumption is precisely why S013 P2 cannot be silently dropped.

## Exact limitation and next mathematical obstacle

One bounded attempted quantitative intermediary with gamma=1 was tested; its **retain-every-class** obligation fails, not the `gamma*t/m^3` existence objective after arbitrary class deletion. Any successful unconditional preserve-or-drop strategy must coordinate THREE final invariants, not run S012 pair filtering and A0 singleton anchoring as independent stages:

1. Heavy pair e: final codegree `d_H(e)` is 0/1 or >=m (no 2,...,m-1 unprotected noncore remnant).
2. Heavy singleton v: either there is an actual selected singleton-core v block, or the realised link has TRUE `f_v+|D_v|>=m`; with absent singleton no condition.
3. Empty: either absent, an entire selected empty-core block certifies it, or there are >=m **pairwise disjoint mandatory-heavy-core footprints** in selected J.

No absolute gamma, arbitrary private-light BSEL, universal BSEL, R3 or every-k TIK is proved/refuted. S006/S007 restricted positives, S008/S009 all-valid full unions, S010/S011 at-least-half controls, S012 exact PAIR_FILTER, S013 P1+P2 protected gamma, S014 exact >half mixed q-cycle optimum all remain unchanged. For t=0 use empty J; for 1<=t<=3m^3 choose one whole block and get >=t/(3m^3); for m=2 the original paper TIK has H=F. No unrecorded computation or experimental extrapolation: all statements above are symbolic for every declared m,N. Same-assistant proof, not independently reviewed mathematics or originality evidence. Prepare exactly one standalone S016 successor, DO NOT execute it; parent mathematical S001 still unexecuted.
