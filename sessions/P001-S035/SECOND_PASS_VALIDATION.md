# P001-S035 — SECOND PASS (same assistant, not independent review)

1. Fractional LP constraints sum over ORIGINAL whole D, no double counting: |D|<=sum w_x d_D(x)<=tau* max d_D(x). Finiteness implies optimum exists for nonempty D (or use an epsilon-optimal cover and take limit).
2. Residual D({x}) is a SIMPLE graph, because each triple contains a unique unordered residual pair. S033 graph guarantee applies for m>=2, no spread/core condition. Exact lift maps graph singleton {v} to triple pair {x,v}, graph EMPTY to triple singleton {x}. Triple EMPTY impossible when x is in every selected edge; no self-witness substitution.
3. A maximal matching endpoints form cover, hence tau*<=tau<=3nu. Inverting the positive denominators gives both mass inequalities in correct direction. For tau*<=Bm, coefficient 1/(8B) independent of all variable parameters except fixed B.
4. For 6m-spread nonempty D: |D|<=tau*Delta1 and Delta1<=|D|/(6m), hence tau*>=6m. For an s-edge maximal matching, cover size at most 3s implies |D|<=3s Delta1<=s|D|/(2m), hence s>=2m.
5. For N disjoint K_(s,s,s), s=m-1>=2: exact degrees are s²,s,1. N>=ceil(216m³/s³) implies Ns³>=216m³, Ns²>=36m², Ns>=6m (since s<m). Each edge contains pair of ambient codegree s<m, so no robust core. But s>=2, so no private pairs. Per component s disjoint triples give fractional cover lower s, one part gives upper s; aggregate tau*=Ns. Per component maximum matching s, so nu=Ns.
6. Take matching of size s in EACH copy; selected H is globally a matching, all its pairwise exact intersections EMPTY, and |H|=Ns>=m, so EMPTY has an in-H matching, ratio Ns/(Ns³)=1/s². For N~m², tau*/m diverges; still no DSE3 refutation. For N=729, m=3 is tight in triple spread count: 729*8=216*27; all m>=3 work.
7. The S034 colour alternative cannot be unioned with the S035 common-x lift. Select whichever has larger certified size; `max` only. For empty D, H empty; m=2, H=D.
8. S033 ML/star-forest proof rechecked logically in correction audit, but previously frozen finite graph experiments still did NOT exercise spread branches. No new numeric mathematical testing carried out. No independent mathematical referee or novelty audit.

**VERDICT:** restricted transversal and matching inequalities survive SAME-ASSISTANT pass; claimed global tau*=O(m) is rigorously false; full DSE3/R3/TIK remains UNPROVED.
