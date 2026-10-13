# P001-S051 — normalized rich-link failure with near-total SAME-F rescue; sharp partite reduction

2026-10-13. Exactly one S051, archive-first commit 2297d362, digest-manifest-second f383fdd5, frozen gate THIRD 82121fa3 before this proof. SAME-ASSISTANT symbolic mathematics only; no independent mathematical review, novelty clearance, Lean or publication.

## Immutable target

For each fixed k>=1 one c_k>0 such that every ORIGINAL finite k-uniform F, m>=2, contains ONE FINAL H subset F with |H|>=c_k |F|/m^k; every realised exact K=E∩E' in H, INCLUDING EMPTY, has m WHOLE petals in FINAL H meeting pairwise EXACTLY at K. Triggering E,E' need not be petals. m=2 H=F. S033 k=1 and c_2=1/8 remain historical. R3/HDSE3 alone cannot settle all-k TIK or the programme's Erdős–Rado headline.

## Theorem A: rich hub-link matching PLUS original 6m-spread/core-free/high-hub PLUS all r/h gaps DO NOT guarantee internal validity

Fix m>=3, L>=m^4. One ORIGINAL tripartite 3-family Q has hubs a_i (1<=i<=m), ordinary B-vertices x,u_(i,l), and C-vertices y0,z_j (1<=j<=m-1),v_(i,l), with private u/v vertices distinct for every (i,l), 1<=l<=L. The EXACT WHOLE triples are:

- BASE b_i = {a_i,x,y0}, 1<=i<=m;
- DEFECT d_j = {a_1,x,z_j}, 1<=j<=m-1;
- PRIVATE p_(i,l) = {a_i,u_(i,l),v_(i,l)}, 1<=i<=m,1<=l<=L.

Thus e0=|Q|=mL+2m-1; all original triples are distinct. Each ORIGINAL hub-link graph G_(a_i) has matching EXACTLY L+1, consisting of its L private edges plus b_i, while defect edges reuse x. Hence links are arbitrarily matching-rich, including >m^3. For ordinary vertices the positive number of distinct incident hubs r is m at x and y0 and 1 on all z/private vertices. For ordinary bases the positive number of incident hubs h is m at (x,y0), 1 at each (x,z_j) and each private base. Therefore EVERY positive r and h belongs to {1} union [m,infinity).

Nevertheless Q is NOT internally m-valid: d_1 and b_2 intersect EXACTLY at {x}; the hub-versus-neighbour incidence graph J_x has hub a1 attached to y0 and all z_j, and any other hub attached solely to y0. Its maximum matching is EXACTLY 2 <m. Thus no m distinct WHOLE triples meet pairwise EXACTLY at {x}.

**SAME-ORIGINAL repair:** delete only DEFECT edges and select P={b_i : i<=m} union {p_(i,l):i<=m,l<=L}. Its size is mL+m, so
    |P|/|Q|=(mL+m)/(mL+2m-1)=1-(m-1)/(mL+2m-1)>1-1/L.
All FINAL exact pair kernels are ONLY:
(1) {a_i}, triggered by two edges of hub i, certified by the m whole petals b_i,p_(i,1),...,p_(i,m-1);
(2) {x,y0}, triggered by base edges of different hubs, certified by b_1,...,b_m;
(3) EMPTY, triggered by edges in distinct hubs whenever one is private, certified by the m mutually disjoint private triples p_(i,1), 1<=i<=m.
No hub-ordinary PAIR or ordinary singleton is triggered in P. Therefore P is internally m-valid, with witnesses ENTIRELY INSIDE P. It is a near-full rescue, not an R3 counterexample.

**Genuinely normalized ORIGINAL HDSE3 stress:** take t=216m^3 VERTEX-DISJOINT copies of Q and call the union F. Its ORIGINAL mass e=t(mL+2m-1). Original maximum vertex degree <=L+m (a1 has L+m, others L+1, x has 2m-1, y0 has m); max PAIR degree <=m; max triple degree=1. The 6m-spread inequalities hold because:
  d_F(v)<=L+m<=e/(6m) [t>=6m, e0>=L+m];
  d_F(pair)<=m<=e/(36m^2) [t>=216m^3,e0>=1];
  d_F(edge)=1<=e/(216m^3) [t=216m^3,e0>=1].
Every ORIGINAL edge has an original private PAIR of degree 1: choose {a_i,u_(i,l)} for p_(i,l), {a_i,y0} for b_i, and {a1,z_j} for d_j. Since m>=3, no robust subfamily containing any edge can have >=m link-matching at its private pair; hence robust core C(F) is EMPTY. Every edge meets its original hub a_i of degree >=L+1>m^3, so the high-ORIGINAL-degree S036 normalization is met. All original hub links remain matching-rich and r/h gaps remain 1-or-m.

ORIGINAL F is INVALID at {x} in each copy, yet H=union of the t SAME-F repaired P copies is internally m-valid. Inside each copy the exact kernels are {a_i},{x,y0},EMPTY with preceding in-H petals. Across disjoint copies ONLY EMPTY occurs, already witnessed by m private whole edges within one copy. Consequently |H|/|F|=(mL+m)/(mL+2m-1)>1-1/L>=1-m^-4. NO asymptotic HDSE3 counterexample: this is a strengthened NEGATIVE for the insufficient helper conjunction (large hub-link matchings + r/h gap + genuine spread/corefree/high-original-hub), with a positive near-total H on the SAME ORIGINAL input.

S049-A is NOT contradicted: its minimum POSITIVE link degree >=m fails at private vertices and at hub a_i (i>1) on x. S049-B also requires enormous minimum positive degrees D; matching richness alone cannot replace it. The defect is exactly ordinary singleton hub-versus-neighbour matching nu(J_x)=2, distinct from ordinary r(x)=m.

## Theorem B: S050 rainbow normal form p_k=k!/k^k is asymptotically sharp

S050-A proves every ORIGINAL k-family has a rainbow k-partite ORIGINAL subfamily of >=p_k mass. For F_n=all k-subsets of an n-set, ANY ordered k-partition with class sizes n_1,...,n_k retains exactly product_i n_i rainbow edges. AM-GM gives product_i n_i<=(n/k)^k; whereas |F_n|=binom(n,k)=(n^k/k!)(1+O_k(1/n)). Thus max rainbow fraction <=(k!/k^k)(1+O_k(1/n)). No universal constant >p_k is possible via exact k-colour rainbow retention. k=3 gives optimal 2/9 asymptotically. This sharpness is about the reduction, NOT about the existence/size of internally witnessed final H.

## All-k and first missing implication

For k>=3 cone each triple in Q or F by a common disjoint (k-3)-set T. The invalid original kernel {x} lifts to T union {x}, for which an m-petal witness would project to a nonexistent exact-{x} witness in Q. The SAME-F near-full repair P also cones to an internally m-valid H, with exact kernels T union K and lifted WHOLE petals. No claim of k-spread/corefree of these cones. This reinforces S050-C's failure of naive per-link union induction without refuting all-k TIK.

S050's five FINAL necessary-and-sufficient tests remain the correct unrestricted tripartite certificate specification. The universal quantitative implication still missing is: for EVERY ORIGINAL tripartite F and EVERY m>=3, select ONE H subset F of >=c|F|/m^3 for c>0 absolute while satisfying simultaneously same-hub PAIR degree gaps, hub singleton graph matching gaps, ordinary PAIR multiplicity gaps, ordinary singleton J_x matching gaps, and global EMPTY whole-matching gap. Theorem A shows original r/h gaps, very rich hub matchings and even HDSE3 normalization DO NOT ensure this without controlling final J_x. It does NOT show that sufficient mass cannot be retained; indeed a near-total valid rescue exists.

No log(e)-free universal strengthening of S049-B is proved. S046 sparse bridges, S047 50% conflict, S049 duplicated bases, S050-C low-richness controls all have SAME-ORIGINAL valid rescues and remain method obstructions. New detailed N1/N2 was correctly deferred. No bounded finite experiment was executed.

**S051 verdict:** Two scoped on-paper additions, not a universal theorem: a genuinely normalized HDSE3 near-full-rescue counterexample to a tempting certificate sufficiency shortcut; and optimality of the partite fraction. Universal HDSE3, R3, every-k TIK and parent sunflower conjecture UNPROVED; novelty unknown, no independent referee, formalisation or external action. S052 to be staged FUTURE ONLY.
