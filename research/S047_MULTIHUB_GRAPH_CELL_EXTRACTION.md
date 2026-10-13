# P001-S047 — multi-hub graph-cell extraction with genuinely positive conflicting bridge mass

2026-10-13. **One owner-invoked S047, proof FIRST, SAME-ASSISTANT mathematics.** Archived exact owner text commit `3705bcce7c95abfb80c49205d84e378587df09c8`, separate SHA256 manifest `33c45c5fa4a802905695393c01ab9d5b106f2690`, FROZEN mathematical gate `e2eb0d6785fc4f70c93cedf0d831421122d4ec81` BEFORE this proof. No new finite computation, detailed N1/N2, Lean, publication or outreach. This proves a **structured subclass**, NOT universal HDSE3/R3 or every-k TIK.

## A. Exact unchanged full target

For each fixed rank k, every ORIGINAL finite k-uniform family F and every m>=2 should admit an H subset F with |H|>=c_k|F|/m^k, and each exact kernel of any two **distinct final H edges** (including EMPTY) has m distinct WHOLE sunflower petals **in final H**. Witnesses need not contain the trigger pair. For m=2 take H=F. R3/HDSE3 remains a stepping stone and alone does not imply all-k.

## B. A multi-hub cell theorem, allowing arbitrary high hub overlap and mixed original pair saturation

Fix m>=3. Let A be a finite set of hub vertices, disjoint from a finite set of ordinary vertices. An ORIGINAL triple family F is given as an **edge-disjoint** union F=disjoint_union_i F_i, where:

* G_i is a nonempty *bipartite* simple graph on ordinary vertices, every nonisolated vertex has G_i-degree >=m, and matching number nu(G_i)>=m. Its bipartition may vary between cells; only its undirected graph matters below.
* A_i is a nonempty subset of hub vertices; F_i consists of **all original triples** {a,x,y} with a in A_i and xy in E(G_i). No new triples may be invented. F_i and F_j are edge-disjoint as sets of whole triples; their vertex supports need NOT be disjoint.
* Call i SATURATED when |A_i|>=m and LOW when 1<=|A_i|<=m-1. Make the ordinary-base-overlap graph on LOW cells: i~j when V(G_i) intersects V(G_j), and take transitive components C. **Only** for each such C require a common hub a_C in intersection_(i in C) A_i. NO bound on number of cells per C, number of hubs per cell, high-hub incidence degrees, cycles, or on overlaps of saturated cells with anything. In particular SATURATED cells can share arbitrary base vertices and graph edges, provided whole triples remain distinct.

**THEOREM S047-A (quantitative, exact final-H).** Under these assumptions there exists an internally m-valid H subset F with

    |H| >= |F|/(m-1)^2.                                  (1)

If at least one SATURATED cell occurs, then the stronger bound holds:

    |H| >= |F|/(m-1).                                    (2)

If no saturated cell occurs but the low overlap components can be assigned common hubs a_C using at least m distinct hubs, bound (2) also holds. Both formulas retain ORIGINAL F mass; they do not apply to arbitrary triples lacking the structural presentation.

### Proof, including EVERY realised kernel

**Robust saturated cells.** For saturated cell i, put S_i=F_i. For EVERY original edge T={a,x,y} in S_i, **EVERY proper subset K of T**, whether or not realised inside S_i, has an exact m-petal sunflower wholly in S_i:
- K={a,x} or {a,y}: use m distinct ordinary neighbours of x or y in G_i, holding a fixed.
- K={x,y}: use m distinct hubs from A_i on that fixed base edge.
- K={a}: choose a matching of m distinct graph edges in G_i, lifting all through fixed a.
- K={x} (respectively {y}): choose m distinct hubs AND m distinct graph neighbours of x (resp. y), bijectively, making all triples meet exactly x (resp. y).
- K=EMPTY: choose m disjoint graph edges and m distinct hubs, bijectively; all m triples are fully disjoint.
There are no other proper subsets of a three-element edge. Thus any union S of SATURATED cells is internally m-valid even when their ordinary bases overlap arbitrarily: a realised K=T∩T' is a proper subset of T, which is in some S_i, and the preceding certificate lies already inside S_i⊆S. Whenever S is nonempty it has a WHOLE m-edge matching. This is robust-core-type behaviour; we do **not** mistake it for the universal core-free case.

**Low cell orientation with genuine nonprivate base overlaps.** For each LOW overlap component C, choose its common hub a_C and retain all triples {a_C,x,y} from every i in C. Call their union L_C. All such triples are in original F_i. Every L_C edge has hub a_C; its residual graph is the union of G_i in C. For every active ordinary vertex, this union has degree >=m (one G_i already does), and it has matching number >=m (one G_i already does). Consequently every realised exact intersection of two distinct L_C triples is either {a_C,v} (witnessed by m edges with that hub and m distinct neighbours of v), or {a_C} (witnessed by a graph matching of size m). No EMPTY intersection occurs within L_C. Different LOW components have **disjoint ordinary supports by definition**. If their assigned hubs coincide, their cross intersections are exactly {a_C}, already m-certified inside either component; if their assigned hubs differ, their cross intersections are EMPTY. Let L=union_C L_C.

For a pair with one selected edge in SATURATED S and one in L, the exact pair intersection is a proper subset of the selected edge in S (unless equal edges, which are not distinct); the SATURATED robust certificate therefore covers **every** such cross intersection, including EMPTY and pairs. Cross SATURATED/SATURATED intersections are similarly covered. Thus H=S union L is internally m-valid provided the EMPTY intersections between distinct-hub LOW components are certified.

**EMPTY matching and three exhaustive output cases.** If S is nonempty, its m-edge matching certifies EMPTY globally; use H=S union L. If S is empty but at least m distinct chosen hubs occur among LOW components, choose one whole triple from a component assigned to each of m distinct hubs. Those components have disjoint ordinary supports, so these m triples are pairwise vertex-disjoint; use H=L. Otherwise S is empty and fewer than m different hubs occur. Group the LOW L_C by assigned hub and retain only the largest group (by number of whole triples). All its triples contain one hub, so EMPTY is not realised and pair/singleton certificates above remain valid. The selected group is internally m-valid. This handles in-H witnesses, not merely preselection ambient matches.

**Quantitative ORIGINAL edge count.** Write s=sum_(i SAT)|A_i||E(G_i)|, t=sum_(i LOW)|A_i||E(G_i)|, and g=sum_(i LOW)|E(G_i)|. The F_i edge-disjoint assumption implies |F|=s+t. Since every LOW |A_i|<=m-1, t<=(m-1)g. For each selected LOW component we retain **exactly** sum_(i in C)|E(G_i)| distinct whole triples: edge-disjointness of F_i prohibits duplication under the common hub. Likewise S has exactly s triples and is disjoint from L. In the first two output cases, |H|=s+g>=s+t/(m-1)>=|F|/(m-1). In the final output case, L is partitioned into q<=m-1 common-hub groups, so the largest has >=g/q>=g/(m-1)>=t/(m-1)^2=|F|/(m-1)^2. QED.

**Falsification boundary.** We explicitly require complete hub×graph products, min active G-degree >=m, nu(G_i)>=m, whole-edge disjoint cell presentation, and a common hub in each LOW ordinary-overlap component. Nothing here proves that arbitrary HDSE3 mass admits such a presentation/decomposition with O(m)-factor retention. Saturated cells are robust, so positive SAT mass is not a solution to the robust-core-free hard case. For m=2, H=F is valid regardless of structure.

## C. Connected original HDSE3 positive-control with NON-NEGLIGIBLE bad-PAIR mass

For every m>=3 let r=216m^4, with hubs h_i (i modulo r). For EACH i and j=1,...,m^2 take disjoint ordinary sets X_(i,j) and Y_(i,j), each of cardinality m, disjoint from every other cell's base. Define ORIGINAL E by including **both** hub lifts, for every x∈X_(i,j), y∈Y_(i,j):

    {h_i,x,y} and {h_(i+1),x,y}.                         (3)

No other triple is in E. Unlike S046's one-rare-bridge construction, EXACTLY ONE HALF of EVERY cell's original mass is in its second hub lift: removing all such competing edges discards half, **not o(e)**. The incidence graph is connected via the cyclic hub–cell incidence pattern, with unbounded conflicts and all r hubs linked through m^2 shared bases per neighbouring pair.

Direct census on the SAME original E:

    e=2r m^4;                  n=r(1+2m^3);
    d_E(h_i)=2m^4;             d_E(x)=2m for every ordinary x;
    max original PAIR degree=m, attained by {h_i,x};
    each ordinary base pair {x,y} has ORIGINAL codegree exactly 2;
    nu(E)=tau*(E)=r;           e/n=2m^4/(1+2m^3)=Theta(m).

Every triple contains exactly one hub and its base pair codegree 2<m; thus E is ORIGINAL-invalid (two triples on that base pair realise an unsaturated exact PAIR) and is robust-core-free (every edge has the original proper base-pair link size ≤2<m). The ordinary min positive degree is 2m, so naive vertex peeling at <m removes nothing. Every edge meets hub degree 2m^4>m^3. A hub vertex cover has size r, while taking one {h_i,x_i,y_i} from any private cell of block i for each i gives r disjoint triples, hence nu=tau*=r.

The ORIGINAL 6m-spread inequalities all hold: max d(x)=2m^4<=e/(6m) because r>=6m; max d(P)=m<=e/(36m^2)=r m^2/18; max d(T)=1<=e/(216m^3)=r m/108. Thus this genuinely lies in the spread/corefree/high-original-hub HDSE3 class, with large tau*/m, original mixed pair codegrees 2 and m, and sparse e/n≈m.

Orient every cell (i,j) to h_i and retain ALL m² complete K_(m,m) lifts there. The selected H has

    |H|=r m^4=e/2.                                       (4)

Every within-one-hub pair has exact PAIR {h_i,x}/{h_i,y} (m opposite-side petals) or exact singleton {h_i} (m graph-matching petals); cross-hub pairs have EMPTY (m disjoint edges from distinct hub blocks). **All m whole petals live in FINAL H.** No degree-2 ordinary base pair is realised across two selected edges, because it was assigned just one hub. This is a SAME-E rescue of a POSITIVE, 50% conflicting bridge fraction. It is NOT an HDSE3/R3/TIK counterexample.

For this family e/m^3=2rm, but a sole common-hub selection has size<=2m^4 and a matching has size<=r; both are o(e/m^3) as m grows (2m^4/(2rm)=m³/r=1/(216m), and r/(2rm)=1/(2m)). Multi-hub assembly is essential for this control.

## D. Hostile architectural attack and the first missing implication

**WHY the LOW overlap hypothesis matters.** Take two original cells with G_1=G_2=K_(m,m), disjoint hub sets A_1={a}, A_2={b}, and ordinary bases sharing exactly one vertex x but no others. Each whole local one-hub family is internally valid: graph degree m and matching m. Their union realises the exact singleton {x} between edges with different hubs. Yet in the FINAL union the link at x has an ordinary matching number at most TWO: any whole triple containing x uses hub a or b, so no m-edge sunflower with singleton x when m>=3. Add m additional private, mutually disjoint, one-hub K_(m,m) cells on distinct new hubs if desired; then the union has an m-edge global matching certifying EMPTY, but still fails singleton {x}. The SAME original family has an easy valid rescue: discard one of the two overlapping cells, keeping all other cells, a fraction (m+1)/(m+2) in the equal-size instance. Thus **blind gluing of locally valid multi-hub links fails even when EMPTY is safe**; this is a METHOD counterexample, not HDSE3.

The exact new local positive theorem does not control general interlaced low-base overlaps lacking a shared hub, arbitrary incomplete hub×graph fibres, original high-degree cells with graph link min-degree <m, or rank-k higher-kernel interactions. To deduce universal HDSE3, a new lemma would need to extract a positive ORIGINAL fraction of an arbitrary high-degree 6m-spread core-free E into robust saturated blocks and/or LOW overlap-components orientable to common hubs, with total loss O(m) (or another compatible scheme), **without assuming** this presentation. No such lemma was proved. S036 then links HDSE3 to R3; no rank3⇒all-k induction is established.

S023/24 planes, S029–S032 shared-row/light controls, S034/35 twin/fractional covers, S037–S041 mixed palettes/islands, S042 affine Steiner, S043 K_(m−1,m−1), S044 saturated pair-star, S045 dense degree, and S046 connected rare-bridge control remain untouched. No universal negative or theorem claim beyond the stated restricted model. A separate hostile SAME-ASSISTANT second-pass record must follow this proof commit.
