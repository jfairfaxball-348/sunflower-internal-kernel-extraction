# P001-S023 — three-tier projective-plane obstruction to full-block m^-3 extraction

**One S023 proof-first mathematical gate, 2026-10-11. Mathematical result: the frozen LIGHT_AWARE_JOINT_1008 statement is FALSE.** This is a **same-assistant symbolic counterexample**, not independent mathematical verification, originality review, a published theorem, a proof or disproof of rank-three R3 or the all-fixed-k TIK conjecture, a Lean proof, or a new N1/N2 source result. It arises within the ORIGINAL at-most-two-heavy-Q nonprivate-light slice, in fact with **exactly one heavy Q vertex per original block** and all original cores of size TWO. Unlike S022's single projective-plane copy, this **nested three-level construction** yields max_valid*m^3/t -> 0 as m grows. S023's one frozen inequality was committed separately before this analysis at `41021d001f718c1c18cb0afc78e9e74de7e04e89`.

## 1. Fully quantified family and original loads

For each prime power q>=2, set m=q+2, L=q^2+q+1=m^2-3m+3, h=g=m-1. Let PG(2,q) have a set P of L points and a set Lambda of L lines, each line through q+1=m-1 points, each point incident with m-1 lines, and each two lines intersecting in exactly one point.

Create h mutually distinct heavy symbols v_a (1<=a<=h). For every a and every group b (1<=b<=g) make disjoint labelled copies of the point and line symbols; in group (a,b) use light symbols z_(a,b,p) for p in P, x_(a,b,l) and w_(a,b,l) for l in Lambda. All symbols with distinct indicated indices are different, except that z_(a,b,p) is deliberately reused across all lines containing p in its group. For each line l make one ENTIRE m-triple sunflower block

    B_(a,b,l) = { {v_a, x_(a,b,l), z_(a,b,p)} : p lies on l }
                union { {v_a, x_(a,b,l), w_(a,b,l)} }.

Each block has exactly (q+1)+1=m distinct triples and exact 2-core {v_a,x_(a,b,l)}; its m third vertices are distinct. The complete blocks are EDGE-DISJOINT because each x_(a,b,l) identifies one original block uniquely, so F is a simple 3-uniform family with |F|=m*t. Number of original whole blocks:

    t = h*g*L = (m-1)^2*(m^2-3m+3).

Original support multiplicity(v_a)=g*L>m, so ORIGINAL Q={v_1,...,v_h}; every x and w belongs to ONE block support, every z_(a,b,p) to exactly q+1=m-1 supports. Therefore every original non-Q support load <=m, and |support(B_i) intersect ORIGINAL Q|=1 for every i. No relabelling of Q, no multiple edges, no private-light assumption, no outside-H witnesses.

## 2. All possible exact-kernel obstructions in a selected whole-block union

Let J be any subset of original blocks and H_J their ENTIRE-triple union. Every original 2-core {v_a,x_(a,b,l)} is witnessed by the selected block's m petals. Three mutually exclusive escalations prove that |J|>=2 is IMPOSSIBLE if H_J is internally m-witnessed:

**(2-core failure within one (a,b) group.)** If J selects distinct lines l,l' within group (a,b), let p be their unique common projective-plane point. The triples {v_a,x_(a,b,l),z_(a,b,p)} and {v_a,x_(a,b,l'),z_(a,b,p)} have exact intersection {v_a,z_(a,b,p)}. The codegree of this pair in the WHOLE F, hence also in H_J, is exactly q+1=m-1: only lines through p contain it. Therefore NO m distinct triples with this exact 2-core can lie in H_J. A valid J selects at most one line block from each (a,b) group.

**(1-core failure within one heavy hub after pair safety.)** Suppose pair safety holds, so at most one block is selected in each group. If at least two selected blocks share a hub v_a but come from distinct groups, two chosen triples have exact intersection {v_a}. If r_a is the number of such selected blocks, then 2<=r_a<=g=m-1. Every residual pair in H_J({v_a}) has the block-unique light x_(a,b,l), so every residual graph matching uses at most one pair per selected block: nu(H_J({v_a}))<=r_a. Conversely, choose the private-w residual edge {x_(a,b,l),w_(a,b,l)} from each selected block; these are disjoint, so nu(H_J({v_a}))=r_a<m. Thus the realised EXACT singleton {v_a} fails. A valid J selects at most one original block per heavy v_a.

**(EMPTY failure between different hubs after 2/1 safety.)** Suppose at most one selected block per hub. If J uses at least two different hubs v_a,v_a', their triples have exact EMPTY intersection because all light labels in different hub groups are disjoint. Every selected triple contains its unique hub v_a, so a triple matching uses at most one triple from each selected hub. Conversely, select the petal with globally private w from each represented hub; they are disjoint. Hence nu(H_J)=|J|<=h=m-1<m, and realised EMPTY is NOT m-witnessed. Thus no two whole blocks from different hubs can coexist in valid J.

These cases exhaust EVERY way to choose >=2 original blocks. Conversely **one complete block** has the sole realised exact pairwise intersection equal to its own original 2-core, with its m in-H petals, so is valid. Therefore the exact optimum is

    max{|J|: H_J fully exact-2/1/EMPTY internally m-witnessed} = 1.

The three exact matching/codegree failures are actual FINAL-H tests, not approximate graph degree proxies. Case ordering avoids asserting a matching equality outside its necessary pair-safe hypotheses.

## 3. Frozen inequality and universal BSEL are refuted (not TIK)

For the infinite sequence of prime powers q (hence m=q+2 -> infinity),

    m^3*max_valid/t = m^3 / [(m-1)^2*(m^2-3m+3)] -> 0.

Thus for ANY absolute gamma>0 there exists m such that 1 < gamma*t/m^3. The existential universal BSEL from S006 (all edge-disjoint complete m-triple sunflower packings) is FALSE, since this is a valid subcase; the stronger specialised S023 LIGHT_AWARE_JOINT_1008 and earlier frozen S022 t/(1008m^3) hypotheses are also FALSE. This is stronger than S022's GRAPH_ONLY_CONSTANT_REPAIR negative: it bounds the unrestricted optimum over ALL full-block subpackings, not merely repairs of a particular J0.

**Quantifier correction:** an absolute-gamma claim has quantifiers exists gamma>0, for ALL m. Showing max_valid*m^3/t -> 0 along m->infinity is mathematically sufficient to disprove it. A fixed-m sequence is NOT necessary (and the S022 m^-5 fallback gives positive fraction at any fixed m). The earlier handoff's 'fixed-m' wording must not override those quantifiers. Nothing here disproves R3 or TIK, since those may select INDIVIDUAL triples and need not retain entire original blocks.

This family also matches the S021 private-light scope NEGATIVELY only: shared z_(a,b,p) has support load m-1, so S011's block-private f_v+|D_v| identity and S021 PRIVATE_LIGHT_126 cannot be applied. Original Q remains of size h and each block uses ONE, not two, original Q symbols. No contradiction to S022's Q=EMPTY positive. A refutation of BSEL means the historical *conditional* implication BSEL=>R3 remains logically correct but its antecedent is false and the proposed BSEL route must be retired.

## 4. Explicit POSITIVE dense edge-level control — full TIK not harmed

The projective-plane line-point incidence bipartite graph is (q+1)-regular and has L vertices on each side. For any set S of lines, (q+1)|S| incidences land in N(S) points, each of degree q+1, so |N(S)|>=|S|. By Hall, for each group (a,b) there is a BIJECTION phi_(a,b) from lines to points with phi_(a,b)(l) incident to l. Fix ONE hub v_a0. Retain ONE triple from each original block of this hub, using

    H_edge = { {v_a0,x_(a0,b,l),z_(a0,b,phi_(a0,b)(l))} :
               1<=b<=g, l in Lambda }.

There are |H_edge|=gL=(m-1)L>=m distinct triples. Each pair intersects in EXACT {v_a0}: x is block-unique and selected z is unique within each group by the bijection, with different groups globally disjoint. Therefore every selected pair is witnessed by ANY m distinct triples of H_edge with the same exact singleton core {v_a0}; EMPTY and 2-point intersections are UNREALISED. This is a TRUE internally m-witnessed H_edge subset F, although it keeps no complete original block. The literal edge-level fraction is

    |H_edge|/|F| = (m-1)L/[m*(m-1)^2*L] = 1/[m*(m-1)] >= 1/m^2.

This exceeds a hypothetical constant*m^-3 edge-level TIK target by an m factor. It is an explicit substantial valid alternative for the SAME counterexample and prevents any unsupported implication from whole-block BSEL failure to R3/TIK failure. Historical S018 two-channel full-union failure retains t/2 valid original blocks; S019 mixed-star failure retains at least 2t/3; S022's saturated-pair/light-singleton and light-pair/EMPTY stresses each retain >half. All remain true distinct dense WHOLE-BLOCK controls.

## 5. Boundaries, implications, and stop

m=2 original all-k H=F trivial; t=0 empty; 1<=t<=3m^3 one complete block is internally valid and satisfies t/(3m^3). The counterexample needs unbounded m along prime powers; at m=4 (q=2), L=7 and t=63, max_valid=1, consistent with 63/(1008*64)<1. The failure of the absolute constant emerges for sufficiently large m; no numerical enumeration or computational experiment was used. All incidences, counting and true codegrees are symbolic.

BSEL universal and nonprivate-light <=2-Q full-block m^-3 inequalities are now marked **PROVISIONALLY REFUTED BY SYMBOLIC PARAMETRIC COUNTEREXAMPLE**, subject to independent mathematics review; S021 private-light m^-3 and S020 private-light m^-4 remain restricted and unchanged. S022's graph-only failure, Q=EMPTY positive, and m^-5 fallback are unchanged. Full R3 rank-three internal extraction, all-k TIK paper conjecture, parent sunflower headline, novelty and open-source statuses remain UNRESOLVED; zero independent new project paper theorems, Lean, manuscripts or publications. Parent mathematical S001 remains UNEXECUTED. Earlier S005/S010/S015/S020 mandatory audits stand; S025 audit FUTURE only.

**Next logical research step** is direct edge-level retention (partial sunflower blocks), where the preceding |H_edge| construction demonstrates the exact structural escape. ONE independent future P001-S024 proof-first session is prepared, NOT executed here. No detailed N1/N2 before full all-k TIK proof candidate, no outreach or external action.
