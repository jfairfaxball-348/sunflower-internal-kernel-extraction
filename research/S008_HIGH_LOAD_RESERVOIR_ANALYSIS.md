# P001-S008 — High-load single-hub reservoir: exact density counterexample

## One frozen mathematical obligation
Test whether a **single high-load vertex** can supply the density-preserving reservoir needed to complement S007, for every arbitrary prescribed edge-disjoint complete m-petal sunflower-block packing of triples. This is an auxiliary claim, not TIK, R3 or BSEL itself. No fresh detailed literature/novelty investigation by owner instruction.

Let m>=3 and B_1,...,B_t be edge-disjoint m-triple blocks, and V_i their support. Define global vertex block load r(v)=|{i:v in V_i}|, and the low-load subset
L={i: for every v in V_i, r(v)<=m}. Each complete block may have empty, singleton or pair core, and all selections retain entire blocks.

**Precise proposed HUB_RES statement (REFUTED).** There exists an absolute eta>0 such that, for every m>=3 and t>=1 and every such arbitrary packing with |L|<t/2, some vertex v with r(v)>m and some J subset {i:v in V_i} satisfy
(1) |J|>=eta*t/m^3,
(2) H=union_{i in J} B_i is internally m-valid at EVERY distinct-pair exact kernel K=A intersect B, with witnesses among the retained H triples (not necessarily A or B).
In rank three this requires >=m distinct third vertices for every realised 2-point K; a residual graph m-matching for every realised singleton K; and an m-edge 3-uniform matching if empty intersection is realised. No ambient witness substitution is allowed.

This is sufficiently strong to imply universal BSEL **if true**, with S007: if |L|>=t/2, apply S007 to L (its induced block load <=m) and obtain |J|>=t/(6m^3). If |L|<t/2, HUB_RES supplies |J|>=eta*t/m^3. Taking gamma=min(1/6,eta) covers both, t=0 by empty choice. Thus its failure is a meaningful failure of a proposed high/low sufficient mechanism.

## Explicit parametric counterexample (all three kernel levels realised and witnessed)

Fix **any** m>=3 and integer q>=m. For each component g in {1,...,q}, choose completely private core symbols a_g,b_g and additional symbols listed below, all distinct except specified repeated core symbols.

- For i in {1,...,m+1} let B_{g,i} consist of the m distinct triples {a_g,b_g,z_{g,i,j}}, j=1,...,m. All z symbols are distinct across all indices. Each B_{g,i} is an exact pair-core m-sunflower.
- Let B_{g,0} consist of m triples {a_g,x_{g,j},y_{g,j}}, j=1,...,m, with all x,y symbols mutually distinct and outside all other symbols. It is an exact singleton-core m-sunflower.

Blocks are individually complete, mutually edge-disjoint (indeed all triples distinct) and have disjoint vertex supports across distinct components. There are exactly t=q(m+2) blocks. In the COMPLETE packing, r(a_g)=m+2>m, r(b_g)=m+1>m, and all z,x,y vertices have r=1. Thus **L is empty**: every single block meets at least one high-load vertex. Yet for every vertex v, r(v)<=m+2. Any J whose entire blocks share v therefore satisfies |J|<=m+2.

If a universal eta>0 satisfied HUB_RES, choose integer q>=m with q>m^3/eta. The required |J|>=eta*q(m+2)/m^3 is strictly greater than m+2, contradiction. This works with fixed m=3 and unbounded q as well: failure is not merely an m-dependent constant.

## Full internal-validity control (the counterexample is strongly POSITIVE for BSEL)
Let H be the union of ALL q(m+2) prescribed blocks. Every pair of distinct triples has one of exactly three intersections:

1. **2-point:** any two pair-core triples in the same component share {a_g,b_g}. Each B_{g,i} itself contains m triples with exact pair core, giving pair residual singleton link size at least m.
2. **Singleton:** any two singleton-core triples of B_{g,0}, or one such triple and any pair-core triple from that component, intersect in exactly {a_g}. The m residual pairs {x_{g,j},y_{g,j}} in B_{g,0} are pairwise disjoint; the singleton residual graph has matching number at least m.
3. **Empty:** triples from different components are completely disjoint. As q>=m, select one arbitrary triple from each of m distinct components to obtain an m-edge matching in H.

There are no additional pair intersection types, by distinct private symbols. Consequently H is itself internally valid for all realised kernels; J=[t] is feasible and BSEL's requested density holds trivially on this family with gamma=1. All THREE kernel types are nonvacuously realised because q>=m, and all are witnessed **inside H**.

## Diagnosis and exact remaining gap
The false step is not high-load incompatibility or a need to delete heavily used vertices; it is the **global concentration demand** that a large compatible reservoir must lie in the star of ONE heavily loaded vertex. Even all high-load blocks may be spread among arbitrarily many disjoint but mutually compatible hubs. Thus neither HUB_RES nor a high/low dichotomy using a single hub can close universal BSEL, R3 or TIK. S007's bounded-global-load lemma survives unchanged; prior S006 cross-block obstructions survive. The construction is a counterexample to HUB_RES ONLY, NOT a counterexample to unrestricted BSEL, R3 or full TIK.

A small positive gluing observation is *used solely to verify the example*: unions of internally valid, pairwise vertex-disjoint nonempty reservoirs remain internally valid if there are at least m reservoirs, because cross-reservoir exact intersection is empty and can be witnessed by picking one edge from each of m reservoirs. Fewer than m nonempty reservoirs can introduce an unwitnessed empty kernel. This does not provide a general density-preserving decomposition into reservoirs or handle overlapping multi-hub blocks.

**Status:** exact symbolic parametric construction, same-assistant scrutiny only; proposed sufficient lemma REFUTED; universal BSEL and rank-three R3 remain UNRESOLVED; full TIK is unchanged SOURCE_POSED_CONJECTURE. New project paper theorems 0; no novelty promotion, independent mathematical review, Lean, numerical experiment, publication or external contact. No source reopening, palette method or unbounded enumeration.

## One bounded S009 successor
Test two-high-vertex-per-block multiplicity class with arbitrary overlapping hub graph, retaining all three exact kernel levels and whole blocks; seek an absolute gamma*m^-3 block-density theorem or identify a rigorously delimited obstruction. This is a **new unexecuted** mathematical session, not a rerun of the falsified single-hub concentration claim.
