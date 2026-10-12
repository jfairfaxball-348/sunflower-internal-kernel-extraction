# P001-S036 — heavy-degree reduction for R3 (SAME-ASSISTANT)

Unchanged semantics: for every realised exact A∩B, including EMPTY, require m distinct sunflower petals entirely in final H. All assertions depending on S033 graph theorem or robust-core reduction are conditional on that same-assistant proof, not independent review. DSE3/R3/TIK remain unproved.

## Theorem A: a matching or a dense high-degree core-free residual

For every m>=3 and nonempty 12m-spread core-free triple D, either (i) an internally m-valid MATCHING H satisfies |H|>=|D|/(6m^3); or (ii) a subfamily E of size >|D|/2 is 6m-spread, core-free, and every E-edge touches an E-vertex of degree >m^3.

Proof. Let X={x:d_D(x)>m^3} and L={e in D:e misses X}. Every L-vertex has d_L(x)<=m^3. Endpoints of a maximal matching M_L cover all L, so |L|<=3m^3 nu(L)<=3m^3 nu(D). Independently d_D(x)<=|D|/(12m), and endpoints of a maximum D-matching cover D, giving |D|<=3nu(D)|D|/(12m), hence nu(D)>=4m. Thus its maximum matching M is internally valid: every pair intersects EXACTLY at EMPTY and any m of M witness EMPTY in M. If |L|>=|D|/2 then |M|>=|D|/(6m^3).

Otherwise set E=D minus L, retaining >half of D. Every e of E meets some x in X. EVERY original edge through x is retained, so d_E(x)=d_D(x)>m^3. For a nonempty j-set T, j=1,2,3, d_E(T)<=d_D(T)<=|D|/(12m)^j<=2|E|/(12m)^j<=|E|/(6m)^j. Core-free is hereditary because a robust E-subfamily would be a robust D-subfamily. QED.

More generally if nonempty 6m-spread D has eta|D| edges all whose original vertex degrees are <=B m^3, the same matching argument gives a FINAL m-valid H of size >=eta|D|/(3B m^3), using nu(D)>=2m. In particular Delta_1(D)<=B m^3 is a solved high-transversal class with c=1/(3B), irrespective of tau*(D)/m.

## Corollary B: a precise reduced universal problem

HDSE3(c_H) asks for |H|>=c_H|E|/m^3 for EVERY nonempty 6m-spread core-free triple E in which every edge touches an E-vertex of degree >m^3, with exact in-H kernels. S033 T2 and its link/robust-core reductions imply: R3 if and only if HDSE3 holds for some absolute c_H>0. Explicitly HDSE3(c_H) gives c_3=min(1/13824,c_H/4).

Proof. R3 trivially implies the restriction. Conversely take arbitrary nonempty triple F, m>=3. Apply S033 link reduction at lambda=24. If F fails 24m spread, a rich proper link of rank two or one lifts T2 or rank-one validity with F-fractions >1/(192m^3) or >1/(576m^3); a failed triple-degree condition yields a singleton >1/(13824m^3). If F is spread, form robust C(F). If |C|>=|F|/2, its nonempty kernels have true internal witnesses by definition and nu(C)>=4m from |C|<=3nu(C)|F|/(24m), so EMPTY also has true m witnesses; H=C retains >=half.

Otherwise D=F minus C has |D|>|F|/2, is core-free by union-closure/maximality of C, and is 12m-spread by the 24-to-12 slack. Apply Theorem A. Its matching case retains >|F|/(12m^3). Otherwise E subset D is 6m-spread/core-free/high-degree, with |E|>|F|/4; apply HDSE3 to retain >c_H|F|/(4m^3). The minimum is min(1/13824,c_H/4), independent of m,n. For m=2 simply take H=F. QED.

**Critical caveat:** ordinary 6m-spread does not necessarily survive a half-mass deletion as 6m-spread. The exact 24 -> 12 -> 6 slack is why the reduction works. This is a reduction, NOT a proof of HDSE3.
