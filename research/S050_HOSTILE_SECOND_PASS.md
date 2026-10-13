# P001-S050 — hostile SAME-ASSISTANT proof pass, AFTER proof and mandatory audit

Date 2026-10-13. Executed AFTER frozen gate commit 0a03d77e, main mathematical proof commit dd99bc89 and fifth/tenth audit commit 6b1f70c4. This is a *separate record*, but still the SAME assistant, NOT an independent mathematical referee, external novelty audit, numerical experiment, Lean proof or publication review.

## A. Quantifier/size attack on rainbow reduction

- For a k-set, exactly k! out of k^k independent equiprobable vertex labellings make all k colors distinct. E X=(k!/k^k)|F|. The expectation guarantees >=not just an approximate fraction but at least the real threshold (integer size rounds upwards). No correlations among edge events are assumed. For k=3 this is 6/27=2/9. PASS.
- The partite subset consists exclusively of ORIGINAL WHOLE edges. If some H subset G is m-valid, its exact intersections and witnesses inside H are identical when viewed as a subfamily of original F; no ambient-only petal substitution. PASS.
- The 'if and only if' statement is about the existence of a uniform *constant depending only on k* for the unrestricted vs restricted theorem. Reverse is restriction; forward multiplies c^part by p_k>0 independent of n,m,e. PASS. It does NOT prove either conjecture by itself.
- For original 6m-spread D and |G|>=2|D|/9: d_G(T)<=d_D(T)<=|D|/(6m)^s and |D|<=9|G|/2. Need 9/[2*6^s] <=1/(4/3)^s, i.e. (9/2)(2/9)^s<=1, true for s=1 equality and s=2,3 strictly. PASS.
- Robust-corefree is downward closed under subfamilies, because a robust positive subfamily G' of G is also positive robust in D with same internal links. PASS.
- HIGH DEGREE trap: an edge with d_D(x)>m³ may have d_G(x) <<m³. No inheritance of the original S036 high-degree normalisation was claimed. PASS. Even if G were m-spread and corefree, this would not by itself prove HDSE3 or R3.

## B. Attempted falsification of five-type full F criterion

All triples are genuinely exactly-one-hub and rainbow A/B/C. Two distinct edges of SAME hub either meet in {a,x} for graph incident edges, or in {a} for graph-disjoint edges: there is no duplicate residual edge. Two DIFFERENT hubs can share at most the two ordinary B,C vertices, giving ordinary PAIR, one ordinary singleton, or EMPTY. This is exhaustive. PASS.

- If K={a,x}, every petal has hub a and x; distinct third vertices give a star, maximum exactly deg_{G_a}(x). If degree 1, no pair triggers; a family of a single edge needs no certificate. PASS.
- If K={a}, residual ordinary edges form a matching and maximum sunflower is nu(G_a). Only a pair of residual-disjoint edges triggers. PASS.
- If K={b,c}, hubs must be distinct, and maximum is h(bc). Proper base PAIRs of different ordinary parts only. PASS.
- If K={x}, petals cannot repeat a hub, since then they'd share hub a as well; they cannot repeat ordinary neighbour y, since then they'd share y. Conversely every matching of hub-versus-neighbour incidence graph J_x yields m distinct WHOLE triples with exact {x}. An arbitrary pair of distinct hub incidences that have the same y triggers ordinary PAIR, not singleton, so the trigger condition with a!=a' AND y!=y' is essential. PASS.
- If K=EMPTY, petals are exactly disjoint original triples and nu(F)>=m is necessary/sufficient ONLY if a pair of disjoint triples realises it. PASS.
- Implications use FINAL rather than original quantities when the criterion is applied to a selected H. For checking all ORIGINAL F, quantities coincide with original. PASS.

The corollary with J_x matching gap 1-or->=m is sufficient because a singleton trigger is equivalent to a matching of size >=2, and then the gap forces >=m. It is NOT necessary for every non-triggered graph degree/matching to be >=m. PASS.

## C. S050-C adversarial census and precise SAME-F rescue

Original m hubs, x, one y0, m-1 z_j: n=m+1+m=2m+1 and e=m+(m-1)=2m-1. All edges are distinct and rainbow. Every G_a is an internally m-valid GRAPH: G_a1 is a star of degree m, other G_ai have one edge only. r(x)=r(y0)=m; all r(zj)=1. Ordinary base h(xy0)=m, h(xzj)=1. PASS.

The J_x graph has hubs a1,...,am on left and residual neighbours y0,z1,...,z_(m-1) on right; each hub connects to y0 and ONLY a1 also connects to z_j. Any matching of size >=3 would require >=2 different hubs paired to z_j, impossible; matching (a1,z1),(a2,y0) gives nu(J_x)=2. The actual triggering pair {a1,x,z1},{a2,x,y0} has exact K={x}; invalid when m>=3. PASS.

H={{ai,x,y0}:all m hubs} contains precisely m WHOLE edges, every intersection is exactly {x,y0}, and H itself is a sunflower of m petals. All other kernels including EMPTY are absent. Ratio m/(2m-1)>1/2. PASS. Hence cannot call this negative helper an R3 failure.

For t=216m³ mutually vertex-disjoint copies: e=t(2m-1), n=t(2m+1). Original maximum vertex degree 2m-1 and maximum pair codegree m, so 6m-spread requires t>=6m for vertices, t(2m-1)>=36m³ for pairs and t(2m-1)>=216m³ for triples; all hold. Each edge has a pair of original codegree1, so core-free. The selected rescues H across all t copies have an EMPTY sunflower from one WHOLE edge of each of m different components; no within-component hidden singleton is created. SAME-F fraction stays m/(2m-1). PASS. Original maximum vertex degree 2m-1 <=m³ for m>=3: no qualifying high-degree hub per edge, so this control does NOT claim HDSE3 normalisation. PASS.

## D. Hostile test of proposed rank induction and purported full-target progress

Coning by the fixed k-3 vertices preserves exact pair intersections under union with T, so the triple singleton-{x} failure becomes singleton T union {x} failure in every k>=3. Within a hub, coned star/singleton links are still internally m-valid; their union is not. Thus a naive independent TIK_(k-1) application-and-union is refuted, NOT every-k TIK. PASS.

The first missing estimate is really simultaneous valid FINAL-H five-certificate packing at absolute C/m³ on arbitrary tripartite ORIGINAL F. This is R3 rewritten (by Partite theorem + exact IFF), not an achieved stronger theorem or a weaker assumption that would imply R3 for free. It does NOT resolve original low-degree owner loss, G_a partial link matching, or global EMPTY. PASS with emphatic LIMITATION. Previous S049 log(e), D and M are NOT removed from that theorem.

## E. Audit status and host checks

S046 matching-or-link bound follows an earlier cover/link argument, S047 complete-product and SAT robust kernels are restricted, S048 q dependent, S049 D/M logarithmically depend on ORIGINAL e. The new partite lemma says the one-hub representation is available after a constant original-mass selection but DOES NOT imply local high degrees, so no previous restricted hypothesis was smuggled into R3. The S050 fifth/tenth record preserves every earlier correction and calls the next route certificate-packing, not another micro-lemma. No robust original-mass theorem, genuine SAME-F counterexample, independent reviewer, originality audit, formal Lean, manuscript or publication.

**HOSTILE SAME-ASSISTANT VERDICT:** claims S050-A/B/C as exactly scoped elementary symbolic propositions survive this pass. Universally quantified HDSE3, R3 and all-fixed-k TIK remain UNPROVED; literature/novelty status unchanged. This is not machine proof or independent scientific verification. S051 requires a new owner invocation and remains FUTURE.
