# P001-S014 — unprotected saturated pair classes: exact cycle obstruction and sharp half-density control

**ONE frozen, bounded S014 mathematical gate (2026-10-10).** Original target remains TIK for EVERY fixed k: for every k-uniform F and m>=2 select H of size >=c_k m^(-k)|F|, c_k depending only on k, with every exact intersection of two distinct selected sets witnessed by an m-petal sunflower **inside H**, including empty. Rank-three R3 / universal whole-block BSEL are auxiliary; the arbitrary private-light <=2-heavy BSEL remains **UNPROVED AND UNREFUTED**. No detailed new N1/N2, independent review, Lean or paper.

## Frozen implication to test — NONEMPTY_SATURATED_CLASS_REPAIR (NSCR)

For all m>=3 and all finite pairwise edge-disjoint COMPLETE m-triple blocks B_i of kernel size 0,1,2, with original heavy set Q={v: block load(v)>m}, every support meeting Q in <=2 vertices and every other vertex globally block-private, partition as in S012 into active classes A_e and pair-inactive A0. Suppose **each nonempty A_e contains a block whose exact core is e**, and the packing contains an exact EMPTY-core block. Proposed bridge NSCR: there exists an internally m-valid final whole-block selection J intersecting every nonempty A_e in at least one of its e-core blocks; the empty witness may be retained as desired. Thus no *entire* saturated active class needs to be dropped in repairing heavy singleton compatibility.

This deliberately tests the first proposed nonempty-class-preservation implication, BEFORE claiming any gamma-density consequence. It requires true S011 link matching, not r_J(v), and a real in-H empty matching. **NSCR IS FALSE** for all m>=3. The counterexample and exact optimum below are symbolic for arbitrarily large q,N, not an unfrozen finite search. This is NOT a negative to a universal gamma bound.

## Exact mixed-core symbolic construction (parametric, including arbitrarily overlapping high hubs)

Freeze arbitrary integer m>=3, arbitrary **even** integer q>=2m+4, and arbitrary integer N>=m+1. Indices i are modulo q. Introduce distinct hubs h_0,...,h_{q-1} and cycle edges e_i={h_i,h_{i+1}}. All subsequently introduced symbols are mutually distinct LIGHT vertices, private to the displayed original block.

For EACH i in {0,...,q-1} and a in {1,...,N}, construct a complete e_i-core block P_{i,a} consisting of the m distinct triples {h_i,h_{i+1},x_{i,a,j}} (1<=j<=m). Construct exactly one singleton-core block S of m triples {h_0,p_j,r_j} (1<=j<=m). Construct exactly one empty-core block E: one triple {h_0,h_1,y}, and m-1 triples {u_j,v_j,w_j} (2<=j<=m), with all these light symbols pairwise distinct. E's m triples are pairwise disjoint. There are exactly

    t=Nq+2

entire, complete, pairwise edge-disjoint blocks; all three kernel sizes 0,1,2 occur. Original block loads are r(h_0)=2N+2, r(h_1)=2N+1 and r(h_i)=2N for 2<=i<q, all >m, while all lights have load 1. Thus Q={h_0,...,h_{q-1}} exactly. Every block has <=2 original heavy vertices, even E, and hubs overlap around the whole q-cycle with arbitrarily large loads. No original-Q relabelling or hub-disjointness assumption was used.

The S012 partition is A_{e_0}={P_{0,a}:1<=a<=N} union {E}; A_{e_i}={P_{i,a}:1<=a<=N} for 1<=i<q; A0={S}. Each nonempty A_e includes N genuine e-core blocks, so S012 PAIR_FILTER selects ALL t original blocks. The S013 protections fail: P1 fails at every h_i with i>=1 because A0 has neither a singleton-core at h_i nor an A0 incident block; P2 fails because A0 has no empty-core block and its only compulsory heavy-core footprint is {h_0}, yielding u0+|W0|=1<m. The example is therefore OUTSIDE the protected lemma, rather than contradicting it.

## Actual three-level certificates of the full union

For H_all=union of every block, the only realised 2-point heavy kernels are the cycle edges e_i. Their TRUE in-H codegrees are d_H(e_0)=Nm+1 and d_H(e_i)=Nm for i>=1, all >=m. Every realised pair kernel containing a globally private light vertex is automatically certified by the original complete block, as in S011. E itself supplies a true m-matching of pairwise disjoint triples, so the empty kernel is both realised and internally certified: nu(H_all)>=m.

At each h_i with i>=2, every residual link edge comes from P_{i-1,a} or P_{i,a}, and contains respectively partner hub h_{i-1} or h_{i+1}. Therefore S011's EXACT identity gives f_{h_i}=0, D_{h_i}={h_{i-1},h_{i+1}}, and

    nu(H_all({h_i})) = f_{h_i}+|D_{h_i}| = 2 < m.

The singleton {h_i} is actually realised by a triple on e_{i-1} and another on e_i. At h_1 the single E edge is also constrained to partner h_0 and adds no new independent link partner: f_{h_1}=0, D_{h_1}={h_0,h_2}, again nu=2<m. At h_0 the selected singleton-core S supplies m independent residual pairs, certifying any realised {h_0}. All pair and empty tests PASS in H_all; exact heavy singleton tests FAIL for every hub except h_0. Repeating any P_{i,a} class N times increases original block load and pair codegree, but never its two-neighbour singleton matching rank. No ambient witnesses or fictitious degree-to-matching inference appear.

## Sharp class-support deletion necessity and exact optimum

Let J be ANY internally m-valid whole-block subcollection (it may include or omit S and E). Define its pair-core support graph G_J on hubs by the cycle edges e_i for which at least one P_{i,a} belongs to J. For every h_i with i !=0, if both incident cycle edges belong to G_J, the selected union realises singleton {h_i}. No singleton-core block at such a hub exists; S011 gives f_{h_i}=0 and |D_{h_i}|=2, even if E is selected (at h_1 its extra pair is constrained to h_0 already). Consequently nu(H_J({h_i}))=2<m and J is INVALID. Thus every vertex outside h_0 has degree at most ONE in G_J.

For even q, such a subgraph of a q-cycle has at most q/2 edges: if deg_G(h_0)<=1 it is a matching; if deg_G(h_0)=2, the two incident edges use three vertices, and the other edges constitute a matching on at most q-3 vertices, giving at most 2+floor((q-3)/2)=q/2 edges. Hence at least q/2 WHOLE e-core active classes contain no selected P-block, and

    |J| <= N*(q/2)+2.

This shows NSCR false EVEN with no density requirement: it insists on >=1 e-core block from ALL q classes. The result forbids the proposed 'repair without dropping an entire saturated pair class', not arbitrary selective retention and not universal gamma.

The upper bound is ATTAINED. Let J_good retain ALL N P-blocks on each alternating edge e_0,e_2,...,e_{q-2}, and also S and E. Then |J_good|=Nq/2+2. Different retained e-classes are vertex-disjoint at hub level, and all other support vertices are private. Every actual heavy pair on an alternating e_i has at least Nm>=m distinct third vertices; E adds one to e_0. The ONLY potentially realised heavy singleton is {h_0}, directly certified by the m residual disjoint S-petals; every other hub belongs to at most one retained e-class and E's exceptional e_0 petal has the SAME partner, so no singleton is realised there. E supplies the actual empty-kernel m-matching. Light kernels automatically have their original in-H complete block certificates. Thus all exact realised pair/singleton/empty kernels in H_good pass the S011 tests, establishing the **exact maximum** over all valid whole-block J:

    max_valid |J| = Nq/2+2 = (t+2)/2 > t/2 >= t/(2m^3).

No deficient class is left with 2,...,m-1 pair-carrying triples: an alternating class is retained completely, a deleted P-class loses all its P-blocks, and the only non-core e_0-active E has its corresponding full saturated e_0 class retained. The selection spans q/2 independent pair-active classes and both other core types; it is NOT selection of a single hub or proof by choosing one block type only.

## Boundary and non-implications

For t=0 take J=empty. For 1<=t<=3m^3 one complete block is always fully internally valid and provides |J|>=t/(3m^3), unrelated to NSCR. The original full TIK at m=2 has H=F. The symbolic family is valid for EVERY fixed m>=3 and unbounded even q,N. It is a negative ONLY to NSCR/class-preservation, while being a **positive** exact >half-density control. In particular max_valid |J| m^3/t is bounded below by m^3/2, NOT tending to zero: it cannot refute even restricted private-light BSEL.

S013's conditional protected-A0 lemma, S012 pair-only lemma, S011 true certificates, S006/S007 positives, S008/S009 fully-valid high-hub families, and S010/S011 half-density controls are all retained. **First missing implication:** an arbitrary mixed-core private-light two-heavy packing still needs a quantitative multi-class *preserve-or-drop* refinement that either neutralises every deficient singleton or supplies genuinely independent true link residuals, while simultaneously preserving/deliberately avoiding actual empty-kernel matching. This result proves that preservation of EVERY already-saturated class is too strong, even when pair and empty tests pass. It does not prove or refute a general extraction rate gamma.

No complete private-light BSEL, universal BSEL, R3, full all-k TIK, original result/novelty determination, independent mathematical scrutiny, Lean, paper or external act has been obtained. One standalone S015 handoff is prepared but not executed.
