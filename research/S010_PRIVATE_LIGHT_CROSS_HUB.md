# P001-S010 — private-light two-heavy cross-hub saturation: quantified false closure

## Exact bounded question and frozen auxiliary mechanism

The continuing paper target is TIK for every fixed k; R3 and the full whole-block BSEL are only auxiliaries. The private-light slice consists of arbitrary edge-disjoint entire m-triple sunflower blocks B_1,...,B_t (m>=3, all core sizes 0/1/2 allowed), supports V_i, global load r(v)=#{i:v in V_i}, original Q={v:r(v)>m}; every V_i contains at most two Q vertices and every v outside Q belongs to **exactly one** block. No assumption of hub-disjointness, common hub, common core size, bounded hub degrees or low-load thinning is made on the general slice. The desired uniform conclusion remains an absolute gamma>0 with some J, |J|>=gamma*t/m^3, whose ENTIRE selected-block union H witnesses every exact pair intersection internally.

We test exactly one potentially useful but weaker, explicitly frozen **cross-hub saturation closure** implication SAT_CROSS:

> For every m>=3 and arbitrary private-light two-heavy packing, for every J subset [t], put H=U(J) and r_J(v)=#{i in J:v in V_i}. Suppose (A) each original heavy hub v in Q meeting selected supports has r_J(v)>=m; (B) each 2-element K realised as an intersection of distinct triples in H has codegree d_H(K)=#{A in H:K subseteq A}>=m; and (C) H contains at least m pairwise disjoint triples, regardless of whether empty is realised. Then H is internally m-valid.

This mechanism is an exact assertion about the **final** H and full prescribed blocks, not a proof of the existence of a dense J. Condition C deliberately overprovides the empty-kernel witness. For a 2-kernel K in a simple 3-uniform family, d_H(K)>=m is exactly an m-petal pair-core sunflower. The asserted missing step is that repeated high-hub block incidences, together with pair and empty certification, force the singleton residual-link **m-matching**. We refute that step parametrically.

## Parametric adversarial construction; all three block-core types

Fix ANY m>=3 and ANY integer N>=m+1. Take three globally distinguished vertices a,b,c. All symbols z^{ab}_{i,j}, z^{ac}_{i,j}, x^b_j,y^b_j, x^c_j,y^c_j, p_j,q_j,s_j below are distinct and outside {a,b,c}; each is owned by one and only one block.

* For i=1,...,N let P^{ab}_i consist of the m triples {a,b,z^{ab}_{i,j}} for j=1,...,m. Each is a complete 2-core sunflower of core {a,b}.
* For i=1,...,N let P^{ac}_i consist of the m triples {a,c,z^{ac}_{i,j}}, j=1,...,m. Each is a complete 2-core sunflower of core {a,c}.
* One singleton-core block S_b consists of m triples {b,x^b_j,y^b_j}, j=1,...,m, and S_c of m triples {c,x^c_j,y^c_j}; their residual pairs are pairwise vertex-disjoint.
* One empty-core block E consists of m mutually vertex-disjoint triples {p_j,q_j,s_j}, j=1,...,m.

The total number of complete edge-disjoint blocks is t=2N+3. Their supports are all distinct as blocks, and every prescribed block has exactly m distinct triples. The heavy loads in the ORIGINAL packing are r(a)=2N, r(b)=r(c)=N+1, all strictly >m. Every other vertex is private to exactly one block and has r=1. Thus Q={a,b,c} exactly. Each P^{ab} support uses only Q vertices a,b; each P^{ac} only a,c; S_b only b; S_c only c; E none. Therefore **every support meets Q in at most two vertices**, all light vertices have block load precisely one, and heavy multiplicities are unbounded as N grows.

Take J=[t], so H=U([t]) is the entire prescribed packing. SAT_CROSS premise (A) holds: selected heavy block loads equal 2N,N+1,N+1 and are >=m. Premise (B) holds: the only 2-point exact intersections are {a,b} and {a,c}, each realised by P blocks and with d_H({a,b})=d_H({a,c})=Nm>=m. Premise (C) holds: the m triples of E are mutually disjoint, hence nu(H)>=m.

All other realised pair intersections, exhaustively, are singleton {a}, singleton {b}, singleton {c}, and empty. Intra-P^{ab} and cross-P^{ab} pairs share exactly {a,b}; analogously P^{ac}. Cross P^{ab}/P^{ac} triples share exactly {a}. Intra S_b and cross S_b/P^{ab} pairs share {b}; S_c gives {c}. Every other cross-type intersection is empty, using complete privacy. The m residual 2-sets of S_b (respectively S_c) give nu(H({b}))>=m and nu(H({c}))>=m. E itself gives nu(H(empty))>=m. Pair intersections {a,b}/{a,c} have m distinct third vertices, witnessed wholly inside each of their complete pair-core blocks.

But the exact residual graph H({a}) consists of Nm edges {b,z^{ab}_{i,j}} and Nm edges {c,z^{ac}_{i,j}}. All edges in the first class meet b; all in the second meet c. Every matching in H({a}) has at most one edge from each class, so nu(H({a}))<=2. Because each class is nonempty, choose one edge from each, disjoint by privacy and b!=c, proving **nu(H({a}))=2<m**. Singleton {a} is actually realised by taking one P^{ab} triple and one P^{ac} triple. Thus H fails internal validity for an exact realised singleton kernel despite SAT_CROSS (A),(B),(C), and despite all other realised kernel levels being internally m-valid. Every witness and failure was computed inside the FINAL H, never borrowed from the ambient F.

This refutes SAT_CROSS for **every m>=3** via an entire N-parametric family (not a finite sample), already at N=m+1. It does **not** refute private-light BSEL, arbitrary BSEL, R3 or TIK.

## Density-positive selection control and quantifiers

Let J_good keep every P^{ab}_i plus S_b, S_c and E, but no P^{ac}_i. Then |J_good|=N+3 and t=2N+3, so |J_good|>=t/2>=t/(2m^3) for m>=3. In its final union every 2-core intersection is {a,b} and is witnessed by a P^{ab} block; singleton {b} and {c} are witnessed by S_b and S_c; empty intersection is witnessed by E. No singleton {a} is realised, because every selected triple containing a also contains b. Hence J_good is internally m-valid. Indeed any J retaining at least one P^{ab} and at least one P^{ac} is invalid at {a}, since the residual graph at a is still a subgraph of the two-star graph with matching number <=2, whereas each class supplies a triple meeting in {a}. So this adversarial packing admits a **constant-density compatible selection** and is intentionally NOT a BSEL counterexample.

For t=0, J=empty is valid and satisfies the literal bound 0. For 1<=t<=3m^3, choose exactly one complete block: its only realised nontrivial kernel is its own block core, and its m distinct triples witness it, so |J|=1>=t/(3m^3). These general boundary observations do not supply any bound for arbitrary t>3m^3. m=2 remains handled separately by TIK's trivial H=F case. For a negative to a universal gamma, a family with m^3 max_J |J|/t ->0 would be necessary; the present construction proves nothing of that kind.

## What actually survives and the next missing implication

The deliberately false step is substituting **hub-degree saturation** for a matching certificate in each realised singleton link. On the a-link, Nm residual edges can collapse onto only TWO competing heavy neighbors b,c: raw edge counts, pair codegrees and global disjoint triples do not raise its matching rank. A future method must certify the exact matching number of each realised H({v}) through mutually disjoint residual pairs, not merely r_J(v)>=m. In this slice, light residual vertices are private across blocks, but their heavy co-endpoints still create a matching bottleneck.

S006's three exact cross-block obstructions, S007 bounded-load positive lemma, S008 false single-hub reservoir with all-valid control, and S009 false THIN_Q with all-valid mixed-core control are unchanged. No claim of a uniform private-light BSEL constant, no all-k TIK candidate, no new independent mathematical review, original theorem, Lean/formal theorem, novelty clearance, paper, or computational enumeration. This is same-assistant symbolic analysis of one auxiliary closure implication, recorded for the tenth-session audit.
