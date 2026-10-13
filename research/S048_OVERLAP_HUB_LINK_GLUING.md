# P001-S048 — overlapping hub links: a colourable all-rank bridge and an unbounded-conflict rank-three gluing theorem

Date 2026-10-13. One owner-invoked P001-S048. SAME-ASSISTANT proof-first analysis, NOT independent peer review, originality certification, formalisation, or manuscript. The exact owner invocation was committed separately as INPUT (7cafb070), SHA256 manifest (aa1e547f), frozen multi-front gate (0816dbe) **before** this analysis. No finite experiments or detailed N1/N2.

## 0. Target and first missing implication

The unchanged FULL TIK target requires, for each fixed k, an absolute c_k>0 such that each ORIGINAL k-uniform F, each m>=2, admits H subset F of size >=c_k|F|/m^k. For every exact realised K=E∩E' of two distinct edges of FINAL H, **including empty**, m distinct WHOLE petals in FINAL H must intersect pairwise exactly at K. The triggering pair need not be witnesses. k=1 elementary; m=2 H=F. R3 and HDSE3 are only stepping stones.

The current all-rank source-posed conjecture, universal rank-three R3, and spread/core-free HDSE3 remain UNPROVED. We attack three originally mixed requirements (new singleton kernels, PAIR saturation, and EMPTY matching) without asserting that arbitrary F admits our hypotheses.

## 1. The hub-support conflict theorem: NO complete products or bipartiteness (all ranks, conditional on lower rank)

**Definitions.** Let k>=2, m>=2. Partition the ground set as A disjoint union X. Assume each ORIGINAL k-edge contains **exactly one hub** a∈A. Then F is uniquely the disjoint union of F_a={{a}∪e:e∈G_a}, with an arbitrary ORIGINAL (k−1)-uniform link G_a on X. Do NOT require disjoint ordinary supports, saturated pairs, complete hub×base-cell product, bipartiteness, or graph min degree. Different G_a may have identical residual edges; the WHOLE F_a are nevertheless distinct because their hubs differ.

For each active a let V_a be the union of vertices in residual edges G_a. Define an **ordinary-support conflict graph** J with the active hubs as vertices and ab an edge when V_a∩V_b≠∅. Let an explicit proper colouring of J use q>=1 colours. q may depend on F and m. A colour class has pairwise disjoint ordinary supports.

**THEOREM S048-A (conditional rank-k bridge).** If TIK_(k−1) holds with constant c_(k−1), there is an internally m-valid FINAL H⊆F with

    |H| >= c_(k−1) |F| / [q m^(k−1) (m−1)]
          >= c_(k−1) |F| / (q m^k).                            (A1)

If the colour class selected below contains at least m nonempty hub links, the stronger lower bound c_(k−1)|F|/(q m^(k−1)) holds. For k=3, S033 gives c_2=1/8, so the **unconditional** scoped conclusion is

    |H| >= |F|/[8 q m^2 (m−1)] >= |F|/(8q m^3).          (A2)

Thus for a fixed q bound, a whole infinite class of arbitrary nonbipartite, incomplete triple fibres satisfies the exact R3 exponent. This is NOT a bound for arbitrary F, because J can have arbitrarily large chromatic number and the decomposition may not exist.

**Proof.** Partition the active hubs into q colour classes; pick a class C with total ORIGINAL weight Σ_(a∈C)|G_a| >= |F|/q. Within each a∈C apply the rank-(k−1) TIK hypothesis to G_a to obtain internally valid L_a⊆G_a with |L_a|>=c_(k−1)|G_a|/m^(k−1). Positive weight implies every active L_a is nonempty. Lift L_a to H_a={{a}∪e:e∈L_a}⊆F_a; the map is injective. For distinct edges of a single H_a, every exact intersection is {a}∪K, where K is a realised exact intersection in L_a, including possibly K=EMPTY; the rank-(k−1) sunflower witness in L_a lifts to m WHOLE edges of H_a whose exact kernel is {a}∪K. (If L_a is a singleton there are no triggering pairs.)

Any two different hubs a,b∈C have V_a∩V_b=∅ by proper colouring, so WHOLE edges in H_a and H_b have intersection EMPTY, not a PAIR or an ordinary singleton. If there are >=m nonempty H_a, take H=union_(a∈C) H_a. For EMPTY choose one WHOLE edge from each of m different hub families: their hubs differ and their ordinary supports are disjoint, hence the m edges are fully disjoint. All within-hub kernels are already witnessed in one H_a. If there are h between 1 and m−1 nonempty H_a, take **only the largest** one: it is internally valid, and EMPTY is never realised because all its edges contain a. In either case |H| >= Σ_(a∈C)|L_a|/(m−1) >= c_(k−1)|F|/[q m^(k−1)(m−1)]. For m=2 one can take H=F directly; F=EMPTY gives H=EMPTY. QED.

**Necessity of quantitative condition.** If J is a clique of t arbitrarily large hubs (for example all residual links use the same ordinary vertex x), this colouring bound alone loses t, not an absolute constant. Such a clique can nevertheless have H=F (below). Proper colouring is a SUFFICIENT compatibility strategy, not a structural normal form for arbitrary HDSE3.

## 2. Rich link improvement, useful with q as large as O(m²)

For rank 3, suppose in addition every active ordinary graph G_a (possibly nonbipartite) has minimum positive degree >=m and matching number ν(G_a)>=m.

**COROLLARY S048-B.** In the same proper q-colouring, H can be chosen with

    |H| >= |F|/[q(m−1)].                                      (B1)

If the heaviest colour class has >=m active hubs, |H|>=|F|/q. Thus q<=C m² for a fixed constant C suffices for |H|>=|F|/(C m³), and q<=C m gives an m^-2 bound. This is a positive class with potentially UNBOUNDED conflict-graph degrees and chromatic number as a function of m, but it does NOT assert q<=Cm² generally.

**Proof.** Each complete ORIGINAL single-hub F_a is internally valid: within a hub, distinct triples with residual ordinary graph edges sharing v have exact kernel {a,v}, witnessed by m edges through v from degree>=m; residual disjoint edges have kernel {a}, witnessed by an m-edge graph matching. No EMPTY is realised within F_a. Choose heaviest colour class and lift FULL original G_a rather than a TIK2 thinning. As in A, if >=m hubs occur, union their FULL families and certify EMPTY by choosing one edge per hub; otherwise choose largest hub. The largest has at least a 1/(m−1) fraction of the class's >=|F|/q ORIGINAL triples. All count equalities are for sets of distinct original whole triples. QED.

Neither A nor B assumes an edge-disjoint hub×graph-cell product: the unique single-hub decomposition guarantees distinct whole triples. Graphs can be incomplete or nonbipartite. The assumption exactly one marked hub per triple is restrictive and explicitly retained.

## 3. Unbounded-chromatic linear ordinary-base overlap: FULL mass survives

A bounded colouring of J is NOT necessary. Here the conflict graph may be complete on arbitrarily many hubs.

**THEOREM S048-C (linear overlap and singleton multiplicity gap).** Let m>=3. Let F=disjoint_union_(a∈A) {{a,x,y}:xy∈E(G_a)} be any finite ORIGINAL triple family on A disjoint from ordinary set X with exactly one hub per edge. Let the active hubs be A* (those G_a with edges). Assume:

(i) every active ordinary graph G_a is simple, has minimum positive degree >=m and matching number >=2m;

(ii) for all distinct active hubs a,b, the ordinary support intersection |V(G_a)∩V(G_b)|<=1;

(iii) for EVERY ordinary vertex x, its number r(x)=|{a∈A*:x∈V(G_a)}| is either 0, 1, or >=m (i.e. NEVER 2,...,m−1).

If |A*|>=m then **H=F itself is internally m-valid**. If 1<=|A*|<m then a single richest original hub fibre H=F_a is internally m-valid and

    |H| >= |F|/|A*| >= |F|/(m−1).                         (C1)

In all cases, there is SAME-ORIGINAL H of size >=|F|/(m−1). This allows unbounded J chromatic number and unbounded hub overlap-degree; it is much stronger than an m^-3 bound on this precise subclass. It does not handle repeated ordinary base PAIRs across different hubs (excluded by (ii)) or intermediate r(x) (excluded by (iii)).

**Proof with exact final kernels.** If |A*|<m choose a fibre F_a of maximum size; as in B its only possible realised kernels are {a,v}, certified by degree>=m, and {a}, certified by graph matching>=2m. EMPTY never occurs. This proves C1.

Now |A*|>=m and choose H=F. Distinct triples using the SAME hub a have exact kernel {a,v} when their ordinary graph edges meet at v, or {a} when residual edges are disjoint. The min-positive-degree hypothesis supplies m distinct WHOLE petals for {a,v}; the matching supplies m WHOLE petals for {a}. Distinct triples with DIFFERENT hubs cannot share two ordinary vertices by (ii), so their exact kernel is either the ordinary singleton {x} or EMPTY. If {x} occurs, x belongs to >=2 active hubs and hence r(x)>=m by (iii). Choose m different hubs a_1,...,a_m with x in their graph supports, and for each choose any ORIGINAL graph edge {x,y_i} in G_(a_i). Each lifted triple {a_i,x,y_i} is in F. Different hubs share at most x in their ordinary supports, so all the a_i are different and the y_i are pairwise different and unequal to other hubs. Thus these m WHOLE edges meet pairwise EXACTLY at x. (No requirement that the original triggering pair be selected as petals.)

To certify EMPTY, pick m distinct active hubs, any order a_1,...,a_m. In each G_(a_j) fix a graph matching of size >=2m. Greedily select one edge from it that avoids all at most 2(j−1) ordinary vertices used by previous selections. Each forbidden ordinary vertex belongs to **at most one** edge of this matching, so at most 2(j−1)<2m matching edges are blocked; a choice remains. The chosen m ordinary edges are pairwise disjoint, and the corresponding WHOLE triples have different hubs, hence are pairwise disjoint. This m-matching lives inside FINAL F and certifies EMPTY if realised (in fact even if not). All possible rank-three exact kernels are covered; there is no cross-hub PAIR under (ii). QED.

**Why the singleton-gap is genuine.** For two hubs a,b with complete K_(m,m) links meeting only at x (S047's negative), r(x)=2<m, their union realises singleton x but ν(F(x))<=2, so it fails internal m-validity even though each fibre is internally valid; if m disjoint supporting hubs elsewhere certify EMPTY, the failure persists. Dropping (iii) without a repair would be wrong. The SAME original instance has a rescue by choosing one of the incompatible fibres. This is a counterexample only to BLIND union, not to R3 or TIK.

**Why >=2m matchings matter to the proof.** The greedy EMPTY construction must avoid up to 2(m−1) previously used ordinary vertices in a given residual matching. Matching number >=m alone does not justify that particular greedy inference. The stronger hypothesis is intentionally stated; no claim that 2m is optimal or necessary.

## 4. Original spread/core-free/high-hub positive control with UNBOUNDED conflict chromaticity

For each integer m>=6, put t=216m^4, N=m². Take t hubs a_1,...,a_t. For each hub a_i form a complete bipartite ordinary graph K_(N,N) whose left part contains **the SAME ordinary vertex x**, and whose remaining 2N−1 ordinary vertices are private to i. Define ORIGINAL F to contain precisely each whole triple {a_i,u,v} with uv an edge of G_i. Different hub supports meet exactly at x; J is the complete graph K_t and has chromatic number t→∞. Each residual G_i has min degree N>=m and matching N>=2m (m>=2). r(x)=t>=m, every other vertex has r=1. Thus by C, the WHOLE original F, without thinning, is internally m-valid, despite all t conflicting ordinary-support pairs.

Direct original census (no experiment):
  e=|F|=tN²;  n=|A∪X|=1+2tN;
  d_F(a_i)=N², d_F(x)=tN, d_F(v)=N for private ordinary vertices;
  max original pair codegree=N (hub/ordinary pairs), ordinary base pairs have codegree 1;
  ν(F)=τ*(F)=t (one hub cover upper bound, and t vertex-disjoint whole triples avoiding x give matching lower bound);
  e/n=tN²/(1+2tN)=Theta(m²), τ*/m=216m³→∞.

It is connected through x; every edge has an original proper ordinary base PAIR of degree 1<m, so the robust core is EMPTY. Every edge touches a hub of original degree N²=m⁴>m³, and also x when its base uses x. It satisfies all ORIGINAL 6m-spread inequalities:
  max_v d(v)=tN <=e/(6m) because N=m²>=6m;
  max_pair d(P)=N <=e/(36m²) because tN>=36m²;
  d(T)=1 <=e/(216m³) because tN²>=216m³.
It therefore lies in the genuinely hard-normalised 6m-spread/core-free/high-hub domain, and H=F certifies all final PAIR/singleton/EMPTY kernels. This is a **POSITIVE CONTROL**, not a proof of HDSE3: the deliberate multiplicity gap and linear ordinary-support intersections are special, and its original PAIR codegrees are 1 and N rather than the full arbitrary mixed 2..m−1 spectrum. S047's mixed-codegree half-rescue and all other named controls remain distinct.

## 5. Direct unrestricted and rank-k attacks: first missing step

**A direct HDSE3 proof was attempted structurally.** One might split an arbitrary robust-corefree 6m-spread ORIGINAL F by selecting for each triple a high-degree hub and taking its graph link. But arbitrary links need not have local min degree m or ν>=2m. Worse, even if most edges can be placed into rich fibres, two different hubs may have ordinary supports overlapping in MANY vertices and with repeated ordinary PAIR bases, creating exact cross-hub PAIR kernels with residual codegrees 2,...,m−1. Neither conflict colouring with q=O(1) (or O(m²) in the rich case), nor support-linearisation with only O(m³) total loss, nor the singleton multiplicity gap is guaranteed by 6m-spread/corefree. These are precisely new hypotheses, not consequences of the normalisation. The PAIR degrees >=m in ORIGINAL F also do not automatically survive selection inside FINAL H. So no unconditional c|F|/m³ was proved, and no SAME-F asymptotic maxvalid/m³ counterexample constructed.

**Rank-k partial gluing from A.** For a fixed q, S048-A inductively gives an m^-k bound for one-distinguished-hub families with q-colourable ordinary-support conflict, conditional only on the known rank-(k−1) TIK statement. This *does not* prove TIK_k for arbitrary F; the induction breaks at the requirement that an arbitrary k-family contain a constant fraction of such a hub-colourable decomposition. The S033 spread/corefree reductions cannot create a bounded chromatic conflict graph. Nor does proving HDSE3 imply the every-k theorem without separate DSE_k steps. Full TIK remains OPEN/UNPROVED under the programme's source-status distinction.

**Symbolic controls and boundaries:** S023/S024 geometrical petal systems and S029–S032 row overlap have no automatic distinguished one-hub partition; S034/S035 twin pairs and S037–S041 palettes may create repeated ordinary PAIRs forbidden by C; the S042 affine Steiner linearity alone does not guarantee high graph matching or r gap. S043 K_(m−1,m−1) fails min-positive-degree>=m for B/C. S044 saturated PAIR stars cannot simply be oriented into a conflict-sparse subclass. S045 dense unbalanced cases may already be valid via an entirely different theorem. S046 rare bridges and S047 50%-bridges show method failures admitting SAME-F rescue; S047 shared-x two-hub union pinpoints the missing r gap here. No contrary universal inference made.

**Status:** scoped SAME-ASSISTANT elementary extraction/gluing theorems A/B/C proved conditionally on their explicit hypotheses; precise witnesses, original count and matching arguments above. Unrestricted HDSE3, R3, universal every-fixed-k TIK UNPROVED; novel/open status NOT freshly authenticated; no detailed N1/N2, independent referee, Lean/Palomar, manuscript, outreach, submission or publication. Hostile second pass to be separately committed AFTER this proof.
