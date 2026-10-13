# P001-S046 — density-free matching/link envelope and a sparse, connected, mixed-PAIR HDSE3 method obstruction

Date: 2026-10-13. This is SAME-ASSISTANT symbolic proof-first analysis of exactly one child S046. Gate: `research/S046_FROZEN_GATE.md`, committed at `a1ac5a47ba71153a33a3b630765e6a5c41f58188` BEFORE this proof. Original exact owner archive `4ef2c8aad7aeb2e2962406dec60d8380383ca7b2`, independent SHA256 manifest `76e0465a72fe61bb0347fd7284c96cc80bbfa861`. This does NOT prove unrestricted HDSE3, rank-three R3 or every-fixed-k TIK, and does not claim independent mathematics verification, new N1/N2, novelty, formalisation or publication.

## 0. Unchanged statement and kernel discipline

For each fixed k, TIK seeks c_k>0 so EVERY original finite k-family F, EVERY m>=2 has an H subset F with |H|>=c_k|F|/m^k. For EACH realised intersection K of distinct final H-edges, including EMPTY, there must be m distinct whole edges of FINAL H pairwise intersecting exactly K. Witnesses need NOT include triggering pair. m=2 is trivial with H=F. Empty F has H empty.

The S033 rank-two graph theorem c_2=1/8 is used below as a previously reported SAME-ASSISTANT mathematical input; no new independent review is inferred. All fractions below use ORIGINAL e=|F|, never an ambient inflated family.

## 1. A density-free *parameterised* matching-or-rich-link envelope

**Proposition A, all ranks conditional on lower-rank TIK.** Fix k>=2, m>=2, nonempty original k-uniform F, e=|F| and s=nu(F)>=1 (maximum cardinality of a vertex-disjoint whole-edge matching). If TIK_(k-1) holds with constant c_(k-1), then F contains a final internally m-valid H with

    |H| >= c_(k-1) e/[k s m^(k-1)].                     (A1)

When s>=m one can alternatively take a maximum matching and therefore

    maxvalid_m(F) >= max{s, c_(k-1)e/[k s m^(k-1)]}.   (A2)

For k=3, the S033 graph bound gives, for EVERY original 3-family without any codegree or density assumption,

    maxvalid_m(F) >= e/(24 s m^2),                     (A3)
    and if s>=m, maxvalid_m(F) >= max{s,e/(24s m^2)}. (A4)

In particular, for fixed A>=1, **s<=A m** entails a final internally valid rank-three H with |H|>=e/(24A m^3) on the ORIGINAL F, including arbitrarily saturated original PAIR channels, e/n=Theta(m), nonlinear vertex m-cores and arbitrary high hubs. In the other direction, **s>=max{m,c e/m^3}** makes the maximum matching itself an m-valid H of size >=c e/m^3. This is an exact parameterised subclass/envelope, NOT the missing general implication.

**Proof.** Let M be a maximum matching of s whole original edges. Its union U has exactly ks vertices and meets EVERY F-edge: an F-edge disjoint from U would augment M. Thus e<=sum_(x in U)d_F(x), so some x in U has d_F(x)>=e/(ks). The residual (k-1)-uniform link L=F(x) has exactly d_F(x) original edges. Apply the assumed lower-rank internal theorem to L to select an internally m-valid J subset L with |J|>=c_(k-1)d_F(x)/m^(k-1). Lift J by adjoining x to EVERY selected residual edge, obtaining whole original k-edges H. Every final pair intersection equals {x} union an exact J pair-intersection; for each realised residual kernel K' the m witnesses in J lift to m WHOLE distinct edges IN H with pairwise exact intersection {x} union K'. The residual EMPTY case becomes the singleton {x}; NO global EMPTY can occur since every H-edge contains x. This proves (A1), including mixed PAIR and singleton kernels in rank three. If s>=m, H=M is also internally m-valid: all pairs have exact EMPTY intersection, with any m M-edges its witnesses. Thus (A2). Take c_2=1/8 for (A3)-(A4). No original pair-degree bound was required. QED.

**Near-spread-saturation corollary.** Independently of the matching number, if an original triple family has Delta(F)>=e/(C m) for a fixed C>=6, direct S033 link lifting gives |H|>=e/(8C m^3). This genuinely includes 6m-spread HDSE3 inputs whose largest vertex lies between e/(Cm) and the spread ceiling e/(6m). It does not cover Delta(F)=o(e/m). The same conclusion at rank k needs TIK_(k-1), not merely rank-three R3.

**Honest dependency:** The exact fractional-cover lift e/[8 tau*(F)m^2] was already recorded in S035/S041. The inequality tau*(F)<=3nu(F) yields a version of (A3). The new point here is the *explicit matching OR link output*, exact original-mass threshold and hostile quantification of what it cannot do; it is a synthesis/refinement of earlier ingredients, not a claim of an independently new general mathematical theorem. We therefore do NOT increment the project's independently proved paper theorem counter.

## 2. NEW quantified SAME-ORIGINAL HDSE3 control in the precise sparse nonlinear mixed-PAIR gap

Fix EACH integer m>=3 and set r=216m^4. For i in Z/rZ, let h_i be a hub, and for j=1,...,m^2 let U_(i,j) and V_(i,j) be pairwise disjoint m-vertex sets, disjoint also from every hub. Define the ORIGINAL bulk B_i to contain ALL m^2 edges {h_i,u,v} with u in U_(i,j), v in V_(i,j), for each j. Then |B_i|=m^2*m^2=m^4. Choose one u_i in U_(i,1), one v_i in V_(i,1). Add ONE connecting bridge edge

    b_i={h_(i+1),u_i,v_i}

(indices modulo r). Set the ORIGINAL family E= (union_i B_i) union {b_i : i in Z/rZ}. These are all distinct original triples, and the family is **connected** in the vertex–edge incidence graph: b_i joins the support of block i to hub i+1, making a cycle through all blocks. No finite experiment is used: this is a deterministic algebraic family for every m.

**Exact census.**

    |E|=e=r(m^4+1),     n=r(2m^3+1),     nu(E)=r,
    tau*(E)=r,          B=max_PAIRdegree=m, 
    Delta(E)=m^4+1,     minimum positive vertex degree=m.
    e/n=(m^4+1)/(2m^3+1)=Theta(m),
    Delta(E)*n/e=2m^3+1 ->infinity.

Every h_i has degree m^4+1: its m^4 bulk edges plus bridge b_(i-1). Every ordinary base vertex has degree m, with the 2r designated u_i,v_i of degree m+1. Hence the ORIGINAL vertex m-core is ALL of E, there is NO low-vertex-degree peeling mass. Every original edge includes exactly ONE hub; hubs form a vertex cover of size r. Taking a bulk edge from each i gives r disjoint original triples, so nu(E)=r. The usual inequality nu<=tau*<=tau and the hub cover give tau*(E)=r. This is global high-transversal, not a small-cover S035 positive shortcut.

**Saturated AND unsaturated original PAIR channels coexist.** Every {h_i,u} with u in the same block i has original degree m; every normal base pair {u,v} has degree one, except the designated pair {u_i,v_i} which has exact ORIGINAL degree TWO, appearing in bulk edge {h_i,u_i,v_i} and bridge {h_(i+1),u_i,v_i}. Other bridge hub/base pairs have degree one. Thus B=m, actual PAIR values 1,2,m coexist, with the 2 channel inside 2,...,m-1 for EVERY m>=3. The ORIGINAL E is NOT internally m-valid: the two distinct triples at {u_i,v_i} realise that pair and only TWO original petals can possibly contain it, fewer than m. This is not a counterexample to existence of a good H.

**Genuine 6m-spread, core-free, high-degree dominated HDSE3.** As r=216m^4, d_E(x)<=m^4+1=e/r<=e/(6m). Every pair has d_E(P)<=m<=e/(36m^2), and every triple has d_E(T)=1<=e/(216m^3), for all m>=3. The inequalities follow directly from e=r(m^4+1) and r>=216m. EVERY original edge contains a hub of degree m^4+1>m^3. EVERY original triple contains its base pair {u,v}, of original degree <=2<m; hence no nonempty E-subfamily can have the required m-matching in EVERY proper nonempty link. The robust core C(E) is EMPTY. In particular E is a genuine ORIGINAL 6m-spread/core-free/high-degree HDSE3 input with sparse nonlinear vertex m-core, highly unbalanced degree sequence, globally large fractional cover and mixed saturated/unsaturated pairs.

**A genuinely SAME-E near-full internally valid rescue.** Retain H=union_i B_i, discarding only the r bridge triples. Then

    |H|=r m^4= e*m^4/(m^4+1),                        (B1)
    |H|/e = 1 - 1/(m^4+1) ->1.

Prove EVERY exact realised pair intersection IN FINAL H:
- If two chosen triples from the SAME block i share one base vertex u (or v), their intersection is PAIR {h_i,u} (or {h_i,v}). The m triples through this pair, obtained using every vertex of its opposite m-side in a single K_(m,m), are WHOLE edges IN H, pairwise intersecting EXACTLY that pair.
- If two chosen triples from the SAME block i have disjoint bases, their intersection is SINGLETON {h_i}. The m edges formed from one perfect matching of any K_(m,m) within that block witness exactly {h_i}, all in final H.
- If two chosen triples lie in different blocks, their intersection is EMPTY. Choose one bulk triple from EACH of m different blocks; they are vertex disjoint and lie wholly in final H.
There are no other cases. Thus H has valid saturated PAIR, singleton and EMPTY certificates **jointly and exactly**, with no ambient-only witnesses.

**SHARP method-negative on this SAME E, not TIK-negative.** Any H that is itself a whole-edge matching has size at most nu(E)=r. Any H whose entire edge set shares any fixed vertex has size at most Delta(E)=m^4+1. Yet

    m^3 nu(E)/e = m^3/(m^4+1) ->0,
    m^3 Delta(E)/e = m^3/r=1/(216m) ->0.       (B2)

Consequently NO universal route restricted to selecting EITHER a matching OR a single vertex-link lift can guarantee c e/m^3 on all HDSE3 families, for any absolute c>0. That is a precise obstruction to the TWO-OUTPUT METHOD ONLY. The SAME original E admits the much larger final H in (B1), so it is emphatically NOT a counterexample to HDSE3, R3 or TIK.

## 3. Multi-front universal attempts and FIRST unproved implication

- **Adaptive peeling/density-free:** E has minimum original active degree m and e/n=Theta(m), far below S045's density threshold e>=2(3B-2)(m-1)n=Theta(m^2 n); S045 linearise-then-core inequality is negative. The S043 original vertex low-degree peeled class is EMPTY. Neither route can recover E's B1 guarantee from their stated premises.
- **Saturated/unsaturated PAIR preservation:** Keeping ALL of original E is mathematically false because its exact degree-2 base PAIR is realised. Deleting just bridges produces valid H with essentially full mass, but nothing guarantees that arbitrary 6m-spread core-free F has a sparse bad bridge set, or that selected regions assemble without new PAIR/singleton/EMPTY obligations.
- **High vertex / matching dichotomy:** Both alone fail at m^-3 on E by (B2), although graph-link extraction (A1) is completely sound as a *local* output and rank3 matching is sound as an EMPTY-only output. The missing theorem must preserve/assemble compatible mass from MANY hubs or build an alternative selected pattern, not only select one hub or a matching.
- **All ranks:** (A1) is conditional on known TIK_(k-1). It is not an induction establishing that hypothesis. An R3 theorem alone would not imply every-k TIK. The exact rank-k dense S045 theorem still needs density.

**FIRST genuinely unproved implication:** For EVERY nonempty ORIGINAL 6m-spread, robust-corefree triple E with each edge meeting original vertex degree >m^3, including arbitrarily high tau*(E)/m and saturated PAIR coexistence, construct m-valid final H retaining c|E|/m^3 with an absolute c, without assuming the bad pair channels are a negligible edge set or that hub regions have bounded conflict graph. This is precisely HDSE3. Through S036 it would imply rank3 R3; all-k needs an additional rank-lifting proof. No asymptotic SAME-F HDSE3 counterexample has been produced.

Controls respected: S023/24 planes, S029–S032 shared rows, S034/35 twin/covers, S037–S041 palettes/islands, S042 affine Steiner, S043 K_(m-1,m-1), S044 cyclic and m-1 pair-star union, S045 unbalanced bulk+hub. Our construction is not classified as a theorem counterexample; both ORIGINAL invalidity and SAME-E dense rescue are explicitly proved. No new detailed N1/N2 or computational experiment, and no paper/formal/external action.
