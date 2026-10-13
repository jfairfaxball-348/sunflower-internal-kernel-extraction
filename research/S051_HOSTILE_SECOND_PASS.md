# P001-S051 — independent-in-commit, SAME-ASSISTANT hostile proof check AFTER proof

Date 2026-10-13. This hostile review is authored after mathematical proof commit f33b09c7dda293960cde692f102c060c025181c6. It is NOT an independent person, formal Lean check or novelty audit.

## 1. Countermodel arithmetic and witness check

A. ORIGINAL one-component count: m bases + (m-1) defects + mL private =mL+2m-1. SAME ORIGINAL repair deletes exactly (m-1), H=mL+m and ratio 1-(m-1)/(mL+2m-1)>1-1/L (because denominator >L(m-1)). PASS.

B. All G_ai have nu=L+1. For i>1 they have L+1 disjoint edges (private+base). For i=1 also only one central x-edge can be used among base and defects, in addition to L private, hence matching cannot exceed L+1. PASS. Large MATCHING is distinct from minimum positive DEGREE; S049-A min-degree fails on all private vertices (degree1). No claim of S049-A contradiction.

C. Defect d1 vs base b2 (m>=3) share x but not hub nor other ordinary neighbor; exactly {x}. In J_x, all i>=2 share the SINGLE neighbor y0, only hub a1 can match a z_j, so nu=2. Other private edges contain no x. Hence {x} is a triggered kernel with no m petals. PASS.

D. In repaired P, same hub base/private/private pair share precisely hub ai; choose base plus any m-1 privates for petals at {ai}. Different-hub base/base share pair {x,y0}; there are m bases as petals. Different-hub base/private or private/private are disjoint, with p_(i,1) for i=1..m supplying m WHOLE disjoint petals. A private edge from same hub as a base shares hub, already case {ai}. Thus no final ordinary singleton {x} and no hub/ordinary PAIR trigger. EMPTY witnessed in each component and across copies. PASS.

E. Normalized ORIGINAL F has maximum d1=L+m, d2=m, d3=1; private pair for each edge verified: base b_i contains {ai,y0} exactly once; defect contains {a1,zj} once; private contains {ai,u_i,l} once. Robust core C(F)=empty follows from necessary m matching in proper pair-link of EVERY edge of a robust subfamily. PASS.

F. With t=216m^3 and e0=mL+2m-1, check d1 <=L+m <=e0 (m>=3), and e=t e0 so e/(6m)=36m² e0 >=e0. d2<=m <= e/(36m²)=6m e0; d3=1<= e/(216m³)=e0. Original high-hub d(ai)>=L+1>=m^4+1>m³. PASS. All coordinates remain strictly tripartite even in disjoint union. Spreading is about ORIGINAL family, not after repair; no spurious post-selection inheritance.

G. Union of t P components: exact cross-component kernels are EMPTY; one component contains m disjoint private edges. Validity preserved. Near-total ratio remains exactly the one-component ratio. No R3/HDSE3 counterexample: maxvalid_m(F)>=|H|> (1-m^-4)|F|, so m³ maxvalid_m(F)/|F| diverges rather than tends to zero. PASS.

## 2. Normalisation sharpness and all-k checks

For F_n=all k-sets on n vertices, each rainbow edge chooses exactly one of n_i vertices in every part; count=product n_i. Balanced upper bound (n/k)^k and binomial asymptotic produce limsup <=k!/k^k, matching S050-A expectation lower bound. This proves optimality of rainbow restriction ONLY; does not imply any optimality of c_k. PASS.

Coning by fixed T: intersections T union K; any hypothetical m petals of T union {x} project to m distinct triples with exact {x} in Q, impossible. Conversely lifting valid repaired P preserves all petals, including EMPTY residual kernels (which become T). PASS. No false general-k spread claim. m=2 H=F separately; lower-rank k1/k2 historical results not overclaimed.

## 3. Hostile checks against universal overstatement

- The specimen is a counterexample to the precise sufficiency shortcut 'very rich hub-link MATCHINGS + 1-or-m ordinary r/h + HDSE3 normalisation implies original full family internally valid'. It is NOT a counterexample to five EXACT final certificate criterion, since nu(J_x)=2 violates it.
- The positive repair is not assumed to be a general repair algorithm. No mass charging argument valid for arbitrary ORIGINAL tripartite F was supplied. In particular there is no c independent of n,e,m establishing an all-tripartite m^-3 theorem.
- S049-B's log(e) is a sufficient technical threshold, not proven necessary or removable. The specimen's private degree 1 disqualifies its premises.
- Same-assistant symbolic derivation cannot establish novelty or independent mathematical verification. All statuses stay OPEN/UNCERTAIN.

**Hostile verdict:** The scoped constructions and rainbow sharpness survive this pass. Universal five-certificate packing, HDSE3, R3 and full TIK are **UNPROVED**, as is the Erdős–Rado conjecture.
