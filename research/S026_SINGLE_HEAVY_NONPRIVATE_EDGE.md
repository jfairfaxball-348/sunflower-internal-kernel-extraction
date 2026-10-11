# P001-S026 — one original-heavy hub, arbitrary nonprivate light: direct edge bound

**2026-10-11; ONE bounded proof-first mathematical gate.** Fresh incoming literal archived in a distinct child commit `a8fb51a8bf8fb9ecfc3ffee5c937dcda9018e730`; quantified ONE_HEAVY_NONPRIVATE_EDGE_9 frozen separately at `2d7732b770450f4d2d4f1d4df3b513f2f01bfb77` BEFORE this proof report. **Result: the exact frozen inequality is PROVED SYMBOLICALLY UNDER ITS RESTRICTED HYPOTHESES, same-assistant only**, not independently peer reviewed, novelty screened, Lean-verified or a completed project paper theorem. There is no new N1/N2 under owner proof-first direction.

## 1. Exact population, target, original loads

Fix integer m>=3, t>=1, and edge-disjoint COMPLETE original m-triple sunflower blocks B_1,...,B_t in a simple triple family F; each original exact kernel K_i has size 0, 1 or 2. Write S_i for union of the m triples in B_i. Fix ORIGINAL Q={v: number of i with v in S_i >m} and suppose **Q={a} globally**. Every other vertex x has original support load <=m; non-Q vertices need NOT be private, and pairs of blocks may overlap in many original light vertices. Blocks are allowed to omit a, contain a compulsorily in their kernel, or contain a in one optional petal. The latter is unique: distinct petals outside K_i are disjoint.

The frozen ONE_HEAVY_NONPRIVATE_EDGE_9 claim asks for a selected family H of INDIVIDUAL triples from the packed union with

    |H| >= t/(9*m^2)

and every *realised exact* intersection of two distinct triples in H equal to an m-petal sunflower kernel inside that SAME H. For realised exact 2-cores, count distinct third labels in H; for singleton kernels, check an actual residual-link matching of size m; for EMPTY, either show it is absent or exhibit m disjoint triples in H. No prescribed selected pair need be used in its own witness.

## 2. Charge shared LIGHT collisions once, by original supports

Construct a simple conflict graph G with vertex set the t ORIGINAL blocks. Put ij in G precisely when S_i and S_j share a vertex different from a. A full m-petal triple block has support size at most 3m (kernel 0: 3m; kernel 1: 1+2m; kernel 2: 2+m). Each non-a vertex lies in at most m original supports because Q={a}, so each original block has at most

    D = 3m(m-1)

distinct conflicting other blocks. No invalid independence assumption on original light supports is made. Greedily delete a chosen vertex and all its neighbours, obtaining an independent block subpacking I with

    |I| >= t/[3m(m-1)+1] >= t/(3m^2).

Between ANY different blocks of I, their full supports can now intersect **only at a**. This is original-support filtering done ONCE, not an uncharged after-the-fact cleanup. Original Q is never recomputed on I.

## 3. Three disjoint ORIGINAL a-channels, one certified final H

Partition I into disjoint classes:
- I_0: a absent from the entire original block support;
- I_M: a lies in the original sunflower kernel, hence in every petal (mandatory);
- I_O: a lies in exactly one petal, not in the original kernel (optional).

Let r=max(|I_0|,|I_M|,|I_O|), selecting one largest class T of r blocks. Then

    r >= |I|/3 >= t/(9m^2).

If r < m, choose ANY ONE complete original block B in T. Its union H=B has m distinct triples; the only exact pairwise intersection within H is K_B, witnessed by the SAME m petals. Thus no unsupported light pair, singleton or EMPTY is realised. Its edge count m>=r>=t/(9m²). The mandatory/optional split is not needed to amalgamate subcritical channels.

If r >=m, take ALL original complete blocks of the single class T as H. Edge-disjointness gives |H|=mr >=t/(9m), hence >=t/(9m²). We now check every cross-block exact intersection and every original within-block kernel.

**T=I_0 (a absent).** Supports of different retained blocks are fully disjoint. Cross-block intersections are exactly EMPTY. At least m blocks remain, so choose one triple from each of any m distinct blocks: they are pairwise disjoint, providing a TRUE final-H EMPTY witness. The original complete m-petal block witnesses each within-block kernel exactly; no new cross-block nonempty kernel exists.

**T=I_M (a compulsory).** Every retained triple contains a. For two distinct retained blocks, their triples intersect EXACTLY at {a}, because other supports are mutually disjoint. Choosing one triple from each of m distinct retained blocks gives m triples sharing precisely a and otherwise disjoint: their residual pairs form a matching of size m in FINAL H({a}). EMPTY is ABSENT, not silently supposed witnessed. Every exact 2/1 original kernel within a complete block is still witnessed by that block's m petals. No distinct non-a light vertex can occur in two selected blocks, so no cross-block light pair or singleton appears.

**T=I_O (a optional).** In every original block precisely ONE of its m triples contains a, and at least m-1>=2 other triples avoid a. Again all non-a supports of distinct retained blocks are disjoint. Cross-block exact intersections are either {a} (both a-containing triples) or EMPTY (at least one avoids a). For singleton {a}, take each unique a-containing triple from m distinct blocks; the two non-a vertices per triple are in disjoint supports, so these triples form an exact a-core m-sunflower in H, i.e. a TRUE residual-link m-matching. For EMPTY, take one a-avoiding original triple from each of m distinct blocks; all are disjoint, a TRUE H m-matching. All original within-block kernels remain certified by their complete blocks. No other cross-block exact pair intersection is possible.

These three cases exhaust the selected family. A within-block exact intersection, including when original K_i is EMPTY or singleton, remains certified because the entire original block is retained. Cross-block light intersections were ruled out by ORIGINAL support independence, not by assuming private light in the unfiltered population. This proves every exact realised 2-point, singleton and EMPTY kernel has m exact petals IN FINAL H.

## 4. Density arithmetic, scope, and stress controls

The **one** permitted support-conflict loss costs at most 3m² blocks and the **one** channel split costs at most 3; their product gives 9m². We never invoke S021 on a graph-filtered subfamily, union incompatible channels or spend a second uncharged m². The final result is a whole-block construction, but that is merely a VALID selection method under the strict singleton-Q hypothesis, not a revival of the universally FALSE whole-block BSEL.

Boundaries: m=2 belongs to the original TIK trivial case H=F; t=0 H=empty is valid outside the Q={a} hypothesis (t=0 forces Q empty). For m>=3 the above is quantified over every t>=1 satisfying Q={a}; small r returns a whole block automatically. No numerical experiment, enumeration, randomness, unpinned population or external source work occurred.

**Original-Q sanity checks:** S023's nested plane has |Q|=m-1 (one original Q *per block*, not one global Q); it is NOT in the frozen population and still REFUTES unrestricted whole-block BSEL. Its true partial edge H remains a dense countercontrol to any attempted R3 negative. S018/S019 have multiple heavy-Q hubs and their full mixed-channel unions can fail residual singleton and EMPTY matching; our final H uses exactly ONE channel, never their false unions. S022 Q-empty valid bound and S021 restricted private-light positive remain unchanged. The current positive proof does not extend to original |Q|>=2: selecting separate hub outputs can make EMPTY realised without m disjoint edges; the h=m-1 nested-plane stress also has shared light pair codegree m-1. Merely summing per-hub densities is invalid.

**What this achieves:** in the exact Q={a} nonprivate-light original population, |H|>=t/(9m²), strictly stronger than frozen S024 t/(512m²) NUMERICALLY, with true internal exact kernels. It is a NEW recorded scoped same-assistant extraction inequality but **zero independently established/original project paper theorems**. The full arbitrary-Q DIRECT_PARTIAL_EDGE_512, stronger S025 GLOBAL_EDGE_DICHOTOMY_512, R3 c*m^-3|F| and every-fixed-k TIK remain UNPROVED/UNREFUTED. Universal whole-block BSEL remains provisionally REFUTED. Novelty remains uncertain; no independent proof reviewer, formal verification, N1/N2, manuscript or submission.

## 5. FIRST remaining quantitative bridge and future scope (not S027 execution)

For arbitrary many original heavy hubs, even when EACH original block support meets Q once, a maximal hub class argument loses a factor proportional to |Q| and the local single-hub H outputs cannot simply be united (actual EMPTY matching may be below m). The next independent gate must either prove a collision-aware multi-hub direct-edge lower bound with a final-H matching certificate, or find the first missing/false implication with a parametric certificate and dense valid alternate. It must explicitly include the S023 nested plane with |Q|=m-1, distinguish one-global-hub from one-hub-per-block, and avoid entire-block BSEL as a premise. **No additional session is executed here; S027 handoff only.**

**Evidence boundary:** All mathematical arguments here are same-assistant symbolic. Hosted GitHub integrity tests, if green, check files, metadata and semantic fixtures, not this universal restricted combinatorial argument. Actual outgoing CI must be observed after the FINAL PR head, and child merged-main PUSH separately, before any parent status registration.