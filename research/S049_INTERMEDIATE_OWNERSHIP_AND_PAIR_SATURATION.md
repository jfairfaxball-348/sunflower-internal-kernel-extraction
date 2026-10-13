# P001-S049 — arbitrary repeated-base saturation criterion and intermediate-multiplicity random ownership

2026-10-13. One owner-invoked S049, SAME-ASSISTANT symbolic mathematics, not independent review, proof-first. Exact user text FIRST commit `ccc3e3286c926a6644b23bbd55aa123b38b2180b`; hash manifest SECOND `5ce32eb6c02ae7bcd4371213755eacc569f5d319`; frozen multi-front gate THIRD `f4bb6f42140dc163e2a8715ae206802db680554a` before this report. No numerical experiment, fresh detailed N1/N2, Lean, correspondence or publication.

## 0. Original target and scope

The FULL TIK source-posed conjecture asks: for EACH fixed k exists c_k>0 such that for EVERY ORIGINAL finite k-uniform F and every m>=2, some FINAL H subset F has |H|>=c_k|F|/m^k, and EVERY exact intersection K of two distinct FINAL H edges (EMPTY included) is the exact common intersection of m distinct WHOLE FINAL H edges. The triggering pair need not be sunflower petals. k=1 and m=2 are elementary. R3/HDSE3 are NOT the all-k statement.

Fix rank three, m>=3, disjoint hub set A and ordinary set X. Assume EVERY ORIGINAL edge contains exactly one vertex of A. Write the ORIGINAL edge-disjoint decomposition F=disjoint_union_(a in A*) F_a, where F_a={{a,x,y}:xy in E(G_a)} and G_a is a nonempty simple ordinary graph. Put e=|F|, t=|A*|, d_a(x)=graph degree, r(x)=number of distinct original hubs whose graph supports include x, and h(xy)=number of distinct original hubs whose graphs include ordinary pair xy. These are distinct WHOLE edges even if their residual base pairs coincide. Put `min^+ degree` for the minimum over nonisolated vertices.

## 1. THEOREM S049-A: exact all-original criterion with ARBITRARY support and repeated base-PAIR overlap

**Statement.** Let every active G_a have min^+ degree >=m and matching number >=2m, and suppose t>=m. Then the WHOLE ORIGINAL F is internally m-valid **IF AND ONLY IF** each positive ordinary-vertex multiplicity r(x) is either 1 or >=m, AND each positive ordinary-PAIR multiplicity h(xy) is either 1 or >=m. No bound whatsoever is imposed on |V(G_a) intersect V(G_b)|, repeated ordinary base pairs, conflict graph chromatic number, graph completeness, or bipartiteness.

If instead 1<=t<m, taking the entire richest original single-hub fibre F_a gives internally valid H with |H|>=e/t>=e/(m-1), REGARDLESS of the multiplicity conditions. Empty F is vacuous; m=2 permits H=F without hypotheses.

**Sufficiency: all exact FINAL kernels.** Set H=F and take distinct triples T,T'. Each has precisely one hub. If they have the SAME hub a, their exact intersection is {a,x} for ordinary residual graph edges meeting at x, or {a} for residual disjoint edges. In the first case use m DISTINCT neighbours of x in G_a: the whole triples through {a,x} meet pairwise EXACTLY there. In the second use m edges of a G_a-matching: the m whole triples meet EXACTLY at a. No EMPTY is realised within a hub.

If T,T' use DIFFERENT hubs a,b, their ordinary edges share 2, 1, or 0 vertices. In the first case exact K={x,y} is an ordinary PAIR. It occurs in >=2 hub fibres, whence h(xy)>=m. Choose m distinct such hubs and the SAME residual pair xy; the resulting m whole triples meet EXACTLY in {x,y}. In the second case K={x}. It occurs at >=2 hubs, hence r(x)>=m. Select ANY m of those hubs. Each has >=m distinct ordinary neighbours of x. The bipartite graph between these m hubs and their ordinary neighbours satisfies Hall: for every nonempty subset S of the m hubs, its neighbourhood has size >=m>=|S|, because even ONE of its hubs has >=m neighbours. Therefore choose m pairwise DISTINCT neighbours y_a, one per hub. The WHOLE triples {a,x,y_a} have distinct hubs and distinct y_a, and meet pairwise EXACTLY at {x}. This Hall argument handles arbitrary repeated ordinary pairs and support intersections; it is the missing S048-C step.

For K=EMPTY (if it occurs), choose m distinct active hubs a_1,...,a_m. For each choose a matching M_i of >=2m ordinary graph edges. Greedily choose one edge of M_i avoiding the at most 2(i-1) ordinary vertices already selected. At most 2(i-1)<2m edges of M_i are forbidden because M_i is a matching. The chosen m WHOLE triples are pairwise disjoint, certify EMPTY in FINAL H, and have different hubs. These cases exhaust all possible proper intersections for distinct triples.

**Necessity under exactly the stated local richness.** If some 2<=h(xy)<m, the distinct WHOLE triples on that residual xy base at two different hubs realise exact PAIR {x,y}. A sunflower with exact pair kernel {x,y} can contain at most one petal per hub, so has at most h(xy)<m petals. Contradiction. If some 2<=r(x)<m, take two distinct active hubs a,b through x. Choose an ordinary neighbour y of x in G_a and z of x in G_b with y != z; this is possible because each has at least m>=3 distinct neighbours. The WHOLE triples {a,x,y} and {b,x,z} meet EXACTLY at singleton {x}. An exact-{x} sunflower has at most one petal per hub; its maximum size is <=r(x)<m. Contradiction. Conversely r=1 and h=1 cannot trigger a cross-hub singleton or PAIR. Necessity and sufficiency are thus exact within this ORIGINAL structural class. No assertions about arbitrary triples or deleted-edge links follow.

For t<m, within a single selected richest F_a all realised kernels are {a,x} and {a}, each certified by local degree/matching; EMPTY never realised. Counting against ORIGINAL e gives >=e/(m-1). This does not assert the union F of <m hubs is valid.

## 2. THEOREM S049-B: ORIGINAL weighted intermediate-multiplicity repair at the EXACT m^-3 scale, under explicit strong link richness

**Statement.** Let m>=3 and an arbitrary ORIGINAL exactly-one-hub triple family F as above, e=|F|>=1. Set
\[
L=ln(64m^3(e+1)),\quad D=64m^2(m+L),\quad M=64m^3(m+L).
\]
Suppose EVERY active original graph G_a has min^+ degree >=D and matching number >=M. No restrictions on r(x), h(xy), ordinary-support overlap, incomplete or nonbipartite graph links, or conflict chromatic number. Then an internally m-valid FINAL subfamily H subset F exists with
\[
|H|\ge |F|/(2m^3).
\]
The constant 1/2 is ABSOLUTE. The premises D,M are much stronger than robust-corefree 6m-spread/high-hub normalisation and depend logarithmically on ORIGINAL e. Therefore this is a genuine scoped m^-3 ORIGINAL-mass theorem, NOT universal HDSE3/R3/TIK. No algorithmic runtime claim is made.

**Independent original ownership variables (NO experiment).** For every ordinary x with intermediate 2<=r(x)<=m-1 independently choose a uniform owner hub among its r(x) ORIGINAL supporting hubs. For each ordinary base pair xy with intermediate 2<=h(xy)<=m-1 independently choose a uniform owner hub among its h(xy) ORIGINAL supporting hubs, independently of ALL vertex choices. Multiplicities 1 and >=m impose no owner restriction. A whole ORIGINAL triple {a,x,y} is retained precisely when a passes x's owner restriction (if any), y's owner restriction (if any), AND xy's owner restriction (if any). Call the random final family F'. No non-original edge is ever introduced. All vertex/pair choices are independent *as variables*; individual edge survival events need not be independent.

Every original triple survives with probability >=(m-1)^(-3)>=m^(-3), because it meets at most three independent restrictions, each with <=m-1 equiprobable possible owners. Thus
\[
\mathbb E|F'|\ge e/m^3. \tag{B1}
\]

**Quantified link degree and matching event.** For every original active incidence (a,x), let B_(a,x) be the event that x is PERMITTED at hub a (r(x)=1 or r(x)>=m, or intermediate x chooses a), but its positive F'-degree in G'_a is <m. CONDITIONAL on permission at x, for distinct ordinary neighbours y of x, the graph-edge survival indicators for xy in hub a depend on different y-owner variables and different base-pair-owner variables, and are therefore mutually INDEPENDENT. Each has conditional success probability at least (m-1)^(-2). So the sum has mean at least d_a(x)/(m-1)^2 >=64(m+L), and a multiplicative Chernoff lower-tail bound gives
\[
\Pr(B_{a,x})\le\exp[-8(m+L)].
\]
(The unconditional event additionally includes the permission of x and cannot have larger probability.)

Fix for each original active a ANY graph matching Q_a of size at least M (choose exactly ceil(M) original matching edges; integer rounding only strengthens bounds). Its distinct base edges have DISJOINT ordinary endpoints and therefore depend on disjoint ownership variables, so their survival events are independent, each with probability >=(m-1)^(-3). Their sum has expectation >=64(m+L), hence
\[
\Pr(\nu(G'_a)<2m)\le \Pr(|Q_a\cap E(G'_a)|<2m)
\le\exp[-8(m+L)].
\]
The inequalities use the standard tail \Pr(X<\mu/2)<=exp(-\mu/8) and \mu/2>=32(m+L)>2m.

There are at most 2e distinct original (a,x) incidences and at most e active hubs. Union bound shows the BAD event B, that any permitted positive link fails min^+ degree>=m or any active hub fails matching>=2m, satisfies
\[
\Pr(B)\le3e\exp[-8(m+L)]< 1/(2m^3). \tag{B2}
\]
The strict final inequality follows directly from L=ln(64m^3(e+1)) and e>=1; in particular no hidden dependence on ambient n or hub count is needed beyond the EXPLICIT ln(e+1) in the richness premises.

**Mass simultaneously with ALL local certificates.** Since 0<=|F'|<=e,
\[
\mathbb E[|F'|\mathbf1_{B^c}]\ge\mathbb E|F'|-e\Pr(B)
\ge e/(2m^3). \tag{B3}
\]
Consequently SOME concrete choice of owners in the GOOD event gives |F'|>=e/(2m^3): its GOOD-event maximum is at least the unconditional expectation in (B3).

**What happens to exact multiplicity gaps?** If original r(x) is intermediate, at most ONE hub can retain an edge at x; if r(x)=1, the same. If original r(x)>=m, x is never ownership-restricted, and on B^c every original supporting hub has final degree >=m. Thus in F' every positive r'(x) is 1 or >=m. Similarly, intermediate ORIGINAL h(xy) allows at most ONE surviving hub; original h(xy)=1 has <=1. If original h(xy)>=m, both its endpoints x,y have original hub multiplicity >=m and are UNRESTRICTED, and the pair xy is also unrestricted; hence ALL h(xy)>=m original lifted triples remain, so h'(xy)=h(xy)>=m. Thus EVERY positive r', h' has the precise 1-or->=m saturation gap required by S049-A, with no assumption of sparse overlaps.

If t>=m ORIGINAL hubs, on B^c each original hub retains a matching >=2m and remains active, so t>=m FINAL hubs. The S049-A theorem certifies EVERY FINAL PAIR, ordinary singleton, hub singleton, and EMPTY in F', yielding H=F' with (B3). If 1<=t<m, bypass random ownership and choose the richest ENTIRE ORIGINAL F_a; its original min degree>=D>=m and matching>=M>=2m, so it is internally valid and retains >=e/t>=e/(m-1)>=e/(2m^3). This proves S049-B for ALL t.

**Precision:** the example is probabilistic but the statement is deterministic existence. It requires no randomized empirical population, seed, deduplication, timeout or finite test. Constants have been deliberately made generous, not optimised. No theorem claims an efficient algorithm or that these richness conditions hold in HDSE3.

## 3. Hostile boundary controls and first missing GENERAL implication

* **S047 two-hub shared x:** r(x)=2<m. With m-rich hub links, the UNION realises singleton {x} but has NO m-petal {x} sunflower; S049-A detects exactly why. Selecting one original hub fibre rescues >=half the two-fibre mass. This is NOT a universal negative.
* **S048 complete hub-conflict positive family:** r(x)=t>=m, all private ordinary vertices have multiplicity one, ordinary base pairs have multiplicity one, local min degree N=m²>=m and matching N>=2m for m>=6. S049-A extends/reproves full ORIGINAL validity without bounding q. Its degree/matching generally do NOT meet enormous S049-B assumptions; B is not needed.
* **Repeated ordinary PAIRs:** if 2<=h(xy)<m, FULL ORIGINAL F is invalid by a *PAIR* obstruction even when r(x),r(y)>=m. If h(xy)>=m, m distinct hub lifts of THAT ORIGINAL xy base directly witness its realised pair kernel. Unlike S048-C, arbitrarily many distinct hubs may share BOTH vertices of an ordinary base pair.
* **Original S047 cyclic 50% bridge:** each cell's base xy has h(xy)=2<m, so the union fails S049-A. Its explicit SAME-ORIGINAL orientation retaining half of F remains available. Link min degree m falls far below S049-B's D; the random high-richness theorem does not silently capture this example.
* **EMPTY:** Q_a local matchings of 2m permit the greedy GLOBAL m-matching only when >=m distinct active hubs; the <m fallback retains a SINGLE WHOLE original hub fibre and therefore never creates EMPTY.
* **m=2 and k=1:** H=F for m=2; k=1 elementary. All restricted theorem inequalities for m>=3 have no bearing on new every-rank TIK.
* **HDSE3 first missing implication:** 6m-spread, core-free, and every original triple touching a >m³-degree vertex DO NOT entail exactly one marked hub per triple, much less all graph links min positive degree D=Theta(m³+m²log e) and matching M=Theta(m⁴+m³log e). The S047 linked K_(m,m) family is an explicit original 6m-spread/core-free/high-hub example with local min graph degree m, disproving this putative richness deduction. A universal decomposition preserving >=c ORIGINAL e at O(m³) total loss, or a low-richness absorption theorem with independently checked final kernels, is still completely missing.
* **Higher k:** For rank k>=4, cross-hub ordinary singleton kernels require disjointness among residual (k-2)-sets, not just selecting one ordinary neighbour from each graph. Hall's simple degree condition no longer suffices; an ORIGINAL hub link may contain many residual edges all meeting one fixed extra vertex. Any induction needs a full matching or hypergraph-link hypothesis *at each residual kernel*, plus an unrestricted original-mass preservation theorem. We do NOT claim TIK_(k-1)=>TIK_k unconditionally.

**Disposition:** S049-A gives an exact criterion eliminating S048's linear-support ban; S049-B supplies a quantified, symbolic e/(2m³) intermediate multiplicity repair with arbitrary repeated base pairs and unbounded conflict chromatic number, at strong explicit ORIGINAL local richness cost. These are SAME-ASSISTANT restricted mathematical proofs only. The full every-fixed-k TIK conjecture, rank3 R3, unconditional HDSE3, general structural reduction, originality, independent review and all publication milestones remain unresolved.

NEXT: a SEPARATE hostile SAME-ASSISTANT proof pass MUST audit the probability independence, Hall, matching, exact K and arithmetic. P001-S050 is FUTURE ONLY and requires a new explicit invocation; it is the mandatory fifth and tenth session strategic correction audit, not part of S049.
