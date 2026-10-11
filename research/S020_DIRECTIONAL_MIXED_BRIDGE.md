# P001-S020 — directed mixed-channel joint extraction and a complete private-light m^-4 bridge

**One bounded S020 proof-first gate, 2026-10-11.** This is a SAME-ASSISTANT symbolic argument, neither independently refereed nor novelty-certified. Exact paper target unchanged: for every fixed k>=1 there is c_k>0 dependent ONLY on k such that every k-uniform F, m>=2, has H subset F of size >=c_k m^-k |F| in which EVERY exact realised pair-intersection (EMPTY included) has m distinct in-H sunflower petals; they need not include the selected pair. No all-k TIK, R3, universal BSEL, or private-light m^-3 BSEL proof follows.

## I. ONE frozen quantitative target, before proof

The separately committed research/S020_FROZEN_GATE.md fixes **PAIR_ACTIVE_96_RETEST**, the unrestricted original-private-light two-Q-support t/(96m^3) full-2/1/0 whole-block assertion, UNPROVED. It encompasses the S019 restricted A0<t/2 PAIR_ACTIVE_96 candidate and preserves S018's true A0-majority branch. This session does not change or prove the frozen m^-3 estimate. Original Q={v: original support block load(v)>m} is always fixed. All blocks are pairwise EDGE-DISJOINT complete m-petal 3-sunflowers with kernel size 0,1,2; every support has at most two original-Q vertices and every light vertex is block-private.

## II. Exhaustive original-Q partition, not a composability claim

For each original heavy pair e={u,v}, a block is e-active iff at least one of its triples contains both u and v; every block is active for at most ONE e. Partition the t original complete blocks disjointly into:

* A0: no e-active triple.
* X_hh: e-active original pair core K_i={u,v} with BOTH original Q hubs compulsory.
* E00: e-active with mandatory Q-core footprint K_i intersect Q empty; both hubs OPTIONAL, each present in the same unique triple.
* M: e-active with mandatory original-Q-core footprint EXACTLY one of {u},{v}, the other original hub OPTIONAL. Thus the block's original exact core is either that singleton hub or a pair {hub, private light}; it has one triple containing both hubs and m-1 triples with only its mandatory Q hub.

No cases omitted: all active supports have exactly e as their two original Q vertices, and K_i intersect Q has cardinality 0,1 or 2; cardinality 2 forces the exact 2-core e. Denote a=|A0|, x=|X_hh|, z=|E00|, y=|M|, so t=a+x+z+y. The original heavy Q is NOT recomputed in any chosen J. Different valid branch selections below are ALTERNATIVES; they are NOT united without joint compatibility.

## III. NEW directed weighted lemma and exact m-petal tests

**Oriented graph lemma (same-assistant proof).** For m>=3 let G be any finite SIMPLE graph with each edge directed one way and assigned positive integer weight q_e in {1} union [m,infinity). Let W=sum_e q_e. There exists an edge subset E' of weight at least W/[12(m-1)^3] such that (i) every vertex has distinct-neighbour degree in {0,1} union [m,infinity), and (ii) either the selected directed edges have at least m DISTINCT tail vertices (sources), or they ALL share just ONE tail vertex. The empty G gives empty E'. We do not insist on any fixed matching/backbone.

**Proof.** Iteratively peel vertices of surviving undirected DISTINCT degree less than m; write C for remaining m-core edges and R for peeled edges. If W_C>=W/2 and C has graph matching number >=m, retain C: degrees >=m, and the m independent edges have m distinct tails. If W_C>=W/2 and nu(C)<m, endpoints of a maximal matching cover C, using at most 2(m-1) vertices. The largest vertex-star carries >=W_C/[2(m-1)]>=W/[4(m-1)] weight. Pick the heavier of edges oriented OUT of its centre and edges oriented INTO its centre (at least half the star weight). If that group has at least m DISTINCT arms retain it, otherwise retain its heaviest single arm (weight >=group/(m-1)). Result is a single oriented star of weight >=W/[8(m-1)^2], certainly >=W/[12(m-1)^3]. An outgoing star has exactly one source; incoming m-star has >=m sources; one arm has one source. Every selected centre has degree 1 or >=m; leaves degree 1.

If instead W_R>W/2, direct each peeled edge by PEEL-TIME (a SECOND auxiliary orientation, unrelated to the original mandatory-tail direction). At most m-1 outgoing peel edges per vertex, so split those edges by outgoing peel slot into <=m-1 functional pseudoforests. Each pseudoforest is properly 3-colourable; partition edges further by the HEAD colour of the peel orientation. This partitions R into <=3(m-1) vertex-disjoint-star forests. Pick the heaviest forest, weight >W/[6(m-1)]. For EVERY component star choose its heavier ORIGINAL mandatory-tail orientation relative to its star centre (weight >= half); if that orientation has at least m arms keep all, otherwise keep its heaviest arm (>=1/(m-1) of that orientation weight). The retained disjoint union of directed one-orientation stars has weight >W/[12(m-1)^2]. If there are >=m nonempty star components, take all: their Q vertex sets are disjoint, hence at least m distinct original tail hubs, and degrees are 1 or >=m. If there are at most m-1 components, keep the heaviest one, weight >W/[12(m-1)^3], and it has one tail or >=m tails by its original orientation. This proves both assertions, including W small: a nonzero retained star always exists.

**Mixed mandatory/optional block encoding.** Partition M by original unordered active pair e. For each e, let s_e^u blocks have mandatory u and optional v, and s_e^v vice versa. Select only a dominant direction of size r_e=max(s_e^u,s_e^v)>= (s_e^u+s_e^v)/2. If 1<=r_e<m retain ONE of those original whole blocks; otherwise retain ALL r_e. The directed weighted simple edge is from the mandatory source to the optional sink, with q_e in {1} union [m,infinity), q_e>=r_e/(m-1). Total graph weight W>=y/[2(m-1)]. Apply the lemma and retain its selected edge classes, i.e. EXACTLY q_e original whole blocks per retained e. The final J is taken SOLELY from M, and

    |J| >= W/[12(m-1)^3] >= y/[24(m-1)^4].

**All realised exact 2/1/0 kernels of this SAME final J:**

1. For each original-heavy pair e, NO selected M-block is an e-core. Exactly ONE e-triple occurs in each chosen e-block, so actual d_H(e)=m*p_e+a_e=q_e in {1} union [m,infinity), or 0 if e unselected. Thus every realised e has m distinct in-H third vertices. Any pair containing a private-light vertex belongs to its unique original block; it is realised between two triples only when it is the block's original exact pair core, for which all m original petals remain.
2. For original-heavy vertex v, every selected block with v as mandatory source provides an ACTUAL Q-free residual link pair: choose one of its m-1 petals not containing its optional other hub. Such Q-free pairs from distinct blocks have private light vertices and are mutually disjoint. Every selected block with v as OPTIONAL sink has v in one triple only and the residual pair consists of its mandatory other hub plus a private light; all incoming classes from a given neighbour constrain to that neighbour. If an original singleton-core {v} block is retained it already certifies v. Otherwise S011's EXACT identity reads f_v+|D_v| = (# selected v-mandatory blocks)+(# distinct incoming neighbours) >= undirected degree(v). Whenever degree(v)>=m this is a true m-matching. At degree(v)=1, if v is optional its only residual pairs all contain its unique mandatory partner, so singleton {v} is UNREALISED; if v is mandatory with q_e>=m then f_v>=m; if mandatory with q_e=1 then only one complete original block contains v, so its own original singleton core certifies v or the singleton {v} is UNREALISED. Degree zero means no v. Original light singletons are protected by their unique block as in S011.
3. Every selected mixed block has ORIGINAL compulsory Q footprint consisting of its one mandatory source. If the graph has >=m distinct selected source hubs, take one block for each of m source hubs and one of its m-1 clean petals (m>=3). Their original mandatory heavy cores are pairwise disjoint and all other vertices light and block-private, giving m ACTUALLY disjoint H triples: true EMPTY certificate. If the selected graph has just ONE source hub then every H triple contains that hub; EMPTY is genuinely ABSENT. No ambient F petal, changed Q, prelocked matching or classwise composability is used.

The result covers all of M, even when M=y and A0=X_hh=E00=0, with a **new all-kernel y/(24(m-1)^4) submass guarantee**. The one extra factor (m-1) comes solely from short/noncore e-class compression after discarding the minority orientation. It is NOT the t/m^3 result.

## IV. NEW complete m^-4 bound for this full private-light slice; exact missing m^-3 bridge

Combine PREVIOUS same-assistant positive branches (without union):

    J_A0 >= a/[12(m-1)^3]                  (S018);
    J_X  >= x/[6(m-1)^3]                   (S017 clean heavy-heavy submass);
    J_E  >= z/[6*m*(m-1)^3]                (S019 E00, plus saturated E00 >=T_sat/[6(m-1)^2]);
    J_M  >= y/[24(m-1)^4]                  (new S020).

All four are valid whole-block selections separately with exact same-J pair/singleton/empty witnesses. Using m>=3, weaken their denominators respectively to 12m^4, 6m^4, 6m^4 and 24m^4. Pick the largest branch. Since t=a+x+z+y, the elementary budget identity gives

    max_valid >= t/[(12+6+6+24)*m^4] = t/(48*m^4).

This covers *every* private-light <=2-original-Q-support packing in the S011 model, not just a positive-numerator subpopulation. It does NOT satisfy the frozen t/(96m^3) gate: for variable m, 1/(48m^4) is smaller than 1/(96m^3) when m>2. A direct m^-3 bridge needs, for EVERY such packing, a true joint J with at least gamma*t/m^3 for some absolute gamma; on M and E00 short classes an extra factor m is presently spent. Merely summing incompatible branch outputs is invalid. Precisely still missing: a compression/selection lemma giving the short noncore mass >=c*(y_short+z_short)/m^3 with all three final tests, or another universal argument bypassing that loss, without preselecting EMPTY backbone. No such lemma is proved or refuted here.

## V. Negative controls and honest bounded finite check

**S019 m+2 saturated mixed star:** all P (mandatory core {v,a_i}) plus R (mandatory {b_j}, optional v) have heavy pairs d(v,a_i)=mN and d(v,b_j)=N, all heavy singleton certificates true (f_v+|D_v|=m+2, f_b=N), but realised EMPTY has true nu(H)=3<m for m>=4. The new proof would NEVER unite X_hh P with M R without testing EMPTY. Select all P: mN/(m+2)N=m/(m+2)>=2/3, exact pair and singleton pass and EMPTY absent; R-only one-source b_j classes are also valid alternatives. The original Q is fixed.

**S018 two contaminated N-channel stars:** all blocks have exact heavy-pair codegrees N, singleton a,c true f=N, but at optional b actual f_b+|D_b|=2<m and realised EMPTY has nu(H)=2<m; union INVALID. Selecting one of the two directed arcs (all N blocks) is valid, fraction 1/2, singleton b unrealised and EMPTY absent. Directed star peeling chooses one incoming arm rather than keep both when 2<m. Original Q unchanged.

**Bounded illustration only:** independent of the source code and NOT a universal proof, a locally executed Python+NetworkX finite m=4,N=5 check enumerated actual pair intersections and singleton residual link matchings, plus the exact mandatory-Q footprint DP for EMPTY. S019 all 30 blocks: pairs pass, singletons pass, EMPTY nu=3, invalid; 20 P blocks: all pass, EMPTY absent. S018 all 10 blocks: pairs pass, singleton b matching=2, EMPTY matching=2, invalid; 5 one-side blocks: all pass, EMPTY absent. These finite controls do not verify the directed-graph lemma or asymptotic constants. Full repository local Python validator/unit tests were NOT executable because github.com DNS resolution blocked checkout; required hosted workflows verify integrity fixtures, not the full analytical proof.

## VI. Edges, controls, evidence and exact limitations

m=2: in the PAPER TIK take H=F, since any two distinct edges are already a 2-petal exact sunflower on their intersection. t=0: J empty. For 1<=t<=3m^3, select ONE original complete block, |J|=1>=t/(3m^3), all its own exact intersections witnessed, independent of heavy loads. S006 vertex-disjoint and S007 bounded global block-load positives, S008/S009 dense-all-valid negative-route controls, S010/S011 distinct singleton/empty obstructions, S012 PAIR_FILTER, S013 conditional protection, S014/S015 class-preservation negatives and dense controls, S016 fixed-M budget failure and dense alternative, S017 SAFE_SPINE(12), S018 A0_MAJORITY_24, S019 E00/MIXED_STAR controls remain intact. Mandatory S005, S010 and S015 audits remain authoritative; the S020 fifth/correction audit is a separate committed record.

This is a new same-assistant restricted m^-4 selection argument, not a claimed source-original theorem, mathematically independently checked proof, R3/internal m^-3 BSEL, or every-fixed-k TIK proof. No new detailed N1/N2, Lean, manuscript, publication, formal verification, communication, external action or parent mathematical S001.
