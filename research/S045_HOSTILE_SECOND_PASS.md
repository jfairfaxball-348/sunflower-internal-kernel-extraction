# P001-S045 — SECOND hostile SAME-ASSISTANT mathematical review (AFTER proof/audit commits)

Date 2026-10-13. The separately committed main mathematical proof is `19c64d77568cf91ef2507379b8c5eab4cd611da4`; the mandatory S045 progress/correction audit is separately committed `5f13c72485166ec3d66573e968205389b98354c6`. This hostile pass is AFTER both, not an independent human/machine formal proof certificate. No fresh numerical experiment or detailed N1/N2.

## 1. Attack Lemma S045-A (linear min-positive m-degree)

**Possible fatal flaw tested:** from a maximal matching |M|<m, do the covered k(m-1) vertices necessarily contain an x with d_C(x)>=|C|/[k(m-1)]? YES, each C-edge meets the endpoint union V(M) by maximality, and |C|<=sum_{v in V(M)}d_C(v). C is simple k-uniform, V(M) covers every edge; no hidden external witness. Distinguish MAXIMUM <m from an arbitrary chosen nonmaximum maximal matching: if nu(C)<m then every maximal matching has <m; use a maximum matching if desired. Every nonisolated x in C has d_C(x)>=m, so the selected star's singleton intersection is truly witnessed. For k>=2, C LINEAR ensures two star edges cannot share an additional vertex; all star intersections are EXACTLY {x}. EMPTY cannot arise within that star. If nu(C)>=m, C itself is valid: each realised singleton has >=m in-C petals, and the selected matching supplies exactly EMPTY whenever EMPTY is realised. Higher-order PAIR kernels absent. PASS as exact SAME-ASSISTANT symbolic check.

**Singleton fallback:** H with one edge has no pair of distinct selected edges, hence valid even for m>2. Do not incorrectly infer two selected disjoint edges would be valid for m>2. PASS.

## 2. Attack greedy conflict linearisation and density factors

An original k-edge has binom(k,2) contained PAIRS, each with at most B-1 other ORIGINAL edges, hence <=binom(k,2)(B-1) distinct conflict neighbours by UNION BOUND. Greedy proper coloring <=Q and a class L>=e/Q always exists; it is LINEAR. Each ground vertex can be peeled at most once and removes no more than m-1 CURRENT edges, so total deletions <=(m-1)n independent of ordering. For e>=2Q(m-1)n, C>=e/(2Q)>0. Theorem A yields e/[2kQ(m-1)]. If B<=m-1 and k>=2, Q<=binom(k,2)m (since 1<=binom(k,2)*2 for k>=3; for k=2 Q=1 and inequality also holds), and (m-1)<=m, so e/[k²(k-1)m²]. In triples B=m-1 gives Q=3m-5, and e/[6Q(m-1)]>=e/(18m²). The scalar 1-edge fallback verifies the max{1,...} lower bound in (B1). PASS.

**Hostile test for k=2 and m=2:** k=2 simple original graph B=1 Q=1, argument is valid but far weaker than S033. For m=2 every original F, including nonlinear rank-k and no-matching cases, is internally 2-valid because the two intersecting edges themselves witness exact kernel. Theorem is conservative and does not require its density assumption to assert m=2 validity. PASS.

**STRATEGIC strength caution:** For k=3, e/n>=Theta(Bm) is a strong premise, NOT implied by 6m-spread; retaining e/m² on dense inputs is not a full TIK proof. A rich linear m-core does not imply that the ORIGINAL family F is internally valid; the selected H is either C or one star. PASS.

## 3. Attack explicit HDSE3 control and uncover one exposition correction

Bulk pairs cross between X,Y,Z have EXACT degree m-1 (not just <=), and a hub pair {h,u} has degree r=m-1; a pair {u,v} in hub triples has codegree 1. Thus original B=m-1. Graph existence check: when r odd m even, N=m^5 EVEN; the antipodal circulant edge is distinct from the short +-shifts because r<N. Each u has degree r. Hence e=(m-1)(100m^6+m^5/2) integer, n=30m^3+m^5+1. For m>=3, n<=5m^5 and e>=100(m-1)m^6, so density e>=2(3m-5)(m-1)n indeed holds.

6m-spread exact inequalities:
d(h)=(m-1)m^5/2 <=e/(200m) <=e/(6m);
d(bulk)=10(m-1)m^3 <=e/(6m) for every m>=3;
d(u)=m-1 <=e/(6m).
All pair degrees <=m-1<=e/(36m²); triple degree 1<=e/(216m³). EVERY edge hits >m³-degree vertex: bulk degree 10m³(m-1), hub degree (m-1)m^5/2. No robust m-core can contain a triple with an original PAIR degree <m. The original F is invalid: for m>=3 two distinct bulk edges with same X,Y pair have exact pair K and only m-1 ambient triples through K, so no possible in-F m-witness. Selected H from the theorem has all required in-H witnesses.

**Correction required to the proof REPORT (no quantitative theorem change):** the shorthand sentence `d_F(h)<=e/(200m), bulk degrees are also smaller` is ambiguously false if read as `d(bulk)<=e/(200m)` for small m (e.g. m=3). Only the 6m vertex-spread inequality is needed for bulk. Replace that clause with separate exact estimates, not a blanket 200m assertion. Mathematical conclusion unaffected.

Degree-imbalance lower bound `Delta(F)n/e>=m^4/202` follows from d(h)>=m^5(m-1)/2, n>=m^5 and e<=(m-1)101m^6. Diverges; no fixed A. PASS after clarification.

## 4. Named countercontrols and SAME-ORIGINAL discipline

- S023/S024 planes and S029–S032 shared/row constructions: method negatives do NOT falsify this theorem, whose density premise and ORIGINAL pair B must be checked separately; no hypothetical final-H witnesses from discarded blocks may be used.
- S034/S035 twins/cover examples, S037–S041 partial palette, star forest and local islands: no false inference from their failed local certificates to universal TIK. Full selected H is either LINEAR CORE or STAR, certified by Lemma A. Cases outside dense B2 are explicitly NOT asserted.
- S042 affine Steiner is LINEAR and often already internally m-valid; hostile to universal two-branch ORIGINAL mass covers but not a counterexample to S045.
- S043 link K_(m-1,m-1) and S044 union of m-1 pair-stars both have SAME-F valid rescues, not genuine HDSE3-negative sequences. S044 cyclic F(t,m) falls under S045 stronger dense argument.
- No E_m with m³ maxvalid_m(E_m)/|E_m|->0 was constructed, so no HDSE3, R3, universal all-k or BSEL falsification is claimed.

## 5. First unproved implication after hostile review

The dense e>=2Q(m-1)n condition loses precisely the case where linear conflict-colour survivors of size e/Q can be peeled to little/nothing. Fixing the factor Q=Theta(m) for ORIGINAL sparse nonlinear PAIR coexistence, while preserving in-final-H singleton and EMPTY matchings, remains the earliest unproved bridge. Separately, even hypothetical R3 completion would not automatically prove all fixed ranks. The mathematical status is **SCOPED SAME-ASSISTANT SYMBOLIC ARGUMENT**, not externally or formally verified. Successful GitHub tests check record integrity; they do not constitute proof review.

No new experimental population, seed, CPU or certificate; no N1/N2/Lean/Palomar/manuscript/outreach. S046 remains FUTURE unexecuted.
