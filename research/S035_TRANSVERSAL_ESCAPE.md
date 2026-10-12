# P001-S035 — quantified transversal escape for DSE3, and why it is not universal

2026-10-12. **SAME-ASSISTANT symbolic proof-first mathematics**; no independent referee, new N1/N2, Lean, originality or publication claim. Input archive commit `030fa97641fee1749654759cd40badcfecedd4d4`, manifest `a08028f7ae1c33709c0782a8d1b4385b018da699`, frozen gate `dcf499a8779bb248506bea8910e4ab779ebfedc4` all precede this report. The unchanged TIK, unrestricted DSE_3/R3, C512/B256 (all-m) remain **UNPROVED**.

## 1. Exact definitions and certificate condition

For finite triple family D, `d_D(x)` is number of triples containing x, `nu(D)` its maximum matching cardinality, `tau(D)` its minimum integral vertex cover, and `tau*(D)` is the minimum of sum_x w_x subject to w_x>=0 and sum_{x in e}w_x>=1 for every e in D. For nonempty D all are positive. Write `valid_m(H)` iff for each **exact** intersection K of two DISTINCT H members, the residual link H(K) has matching number >=m. K may be a pair, singleton or EMPTY. Never substitute D(K) for H(K).

Use S033's SAME-ASSISTANT rank-two extraction theorem `T2`: for any graph G and m>=2 an internally valid L subset G with |L|>=|G|/(8m²). Its proof and the unexercised spread-branch numerical checks are re-audited in the companion correction audit; it is not independently reviewed.

## 2. Positive theorem S035-A — fractional transversal escape

**Theorem (conditional only on the proved-on-paper T2 lemma).** For every m>=2 and every nonempty finite 3-uniform family D, there exists an internally m-valid **single subfamily** H subset D satisfying

`|H| >= |D| / (8 m² tau*(D)) >= |D| / (8 m² tau(D)) >= |D| / (24 m² nu(D)).`

In particular, for ANY fixed real B>0, if `tau*(D)<=Bm`, then `|H|>=|D|/(8B m³)`, with the constant independent of m, |D|, apex support-overlap Delta and pair-private mass. The claim applies also when D has no degree-one pair at all and to forward-private or vertex-piece edges; it needs neither 6m-spreadness nor core-freeness, but the absolute m^-3 conclusion requires the **extra quantitative** cover assumption.

**Proof.** Let (w_x) be an optimal fractional cover, supported on the union of the triples. Sum the edge inequalities:
`|D| <= sum_{e in D}sum_{x in e} w_x = sum_x w_x d_D(x) <= tau*(D) max_x d_D(x)`.
Therefore there exists x with `d_D(x)>=|D|/tau*(D)`. Its residual link G=D({x}) is a simple graph on other vertices. Apply T2 to G, obtaining internally m-valid L with `|L|>=d_D(x)/(8m²)`. Lift L by adjoining x to **every** graph edge; H={e union {x}:e in L}. The lifting bijection preserves exact intersections after adding x: any realised graph singleton {v} corresponds to triple pair {x,v}; any realised graph EMPTY corresponds to triple singleton {x}. Both residual matching certificates are exactly those supplied by L. No exact EMPTY kernel occurs in H, because every triple contains x; no other realised kernels are possible. Thus H is valid and has the displayed mass.

Since integral covers give feasible fractional covers, `tau*<=tau`. Endpoints of any maximal matching (in particular a maximum matching of nu edges) meet every edge, giving `tau<=3nu`. Substitution yields the final inequalities. For m=2 one may simply take H=D, which is internally valid by the original selected pair witnessing itself. For D empty take H empty, without division by zero. QED.

**Hybrid without forbidden gluing.** For the pair-private subfamily D* and full-support conflict degree Delta defined in S034, choose the BETTER of the separate valid outputs of S035-A and S034-A; this certifies
`|H| >= max{|D|/(8m² tau*(D)), |D*|/[8(Delta+1)m³]}`.
This is the maximum of two alternatives, NOT their union. If D*=empty the second term is 0. Still no absolute ratio for arbitrary large tau* and negligible private mass.

## 3. Spread imposes a LOWER, not an upper, transversal budget

**Lemma S035-B.** Every nonempty 6m-spread triple family D has `tau*(D)>=6m` and `nu(D)>=2m`.

**Proof.** The singleton spread inequality says `Delta_1=max_x d_D(x)<=|D|/(6m)`. The same double counting in §2 gives `|D|<=tau*(D)Delta_1`, so `tau*>=6m`. For a maximum (indeed any maximal) matching M of size s, its 3s vertices form a vertex cover. Thus `|D|<=3s Delta_1<=s|D|/(2m)`; divide by |D|>0 to obtain s>=2m. QED.

This eliminates any claim that a 6m-spread system can be handled by a cover of size o(m). The positive S035-A regime is B>=6 and is real, but 6m-spreadness does not give an upper bound on B.

## 4. FALSE universal shortcut — core-free spread does not force tau*=O(m)

For m>=3 put s=m-1, and take N disjoint labelled copies of the complete 3-partite transversal family `K^(3)_(s,s,s)`; call their union D_{m,N}. Choose integer `N>=max(m,ceil(216m³/s³))`. Then:
- `|D|=Ns³`, maximum singleton degree s², maximum pair degree s, each triple degree 1.
- The 6m-spread inequalities are `Ns>=6m`, `Ns²>=36m²`, `Ns³>=216m³`; the choice of N implies all three. Thus every nonempty set T of sizes 1,2,3 is covered. 
- Every pair contained in a triple has link size s<m, so no robust subfamily containing that triple can exist: `C(D)=empty`. Moreover each pair has D-degree s>=2, so **there are NO pair-private edges**.
- In each component, an s-edge matching gives `tau*>=s` (sum the s disjoint edge constraints), and selecting one of the three vertex parts gives an integral cover s. Thus `tau*(D)=tau(D)=Ns`; `nu(D)=Ns`.
- Choosing s pairwise disjoint triples from **each** component yields a globally disjoint H of `Ns` triples. Since `Ns>=m`, its only realised kernel is EMPTY, with a true in-H matching of size Ns. Thus H is valid, and `|H|/|D|=1/s²>=1/m³`. (A single edge per component also works, but is weaker.)

Choose `N_m=m²+ceil(216m³/(m-1)³)`. Then `tau*(D_{m,N_m})/m=N_m(m-1)/m ->infinity`. This **refutes** the attempted general implication `6m-spread + core-free => tau*<=Bm for some absolute B`. It refutes neither DSE3 nor R3: the SAME families possess an m-valid extraction far denser than c/m³. No selected-pair kernel is accidentally claimed to need m witnesses beyond EMPTY because H is a matching.

**Genuinely nonprivate bounded-budget DSE3 witness.** For every m>=3 take N=729 copies. Since `729(m-1)³ >=216m³`, the whole family is 6m-spread, core-free and pair-nonprivate. It has `tau*=729(m-1)<=729m`. Theorem S035-A therefore certifies the universal m^-3 coefficient 1/5832 **on this entire nonprivate population**, though the explicit matching H has substantially better 1/(m-1)² density. This shows the subcase is not vacuous or merely S034's private-pair overlap colouring under another name.

## 5. The first still-unproved quantified implication

The attempted global route would need:
`for all m>=3, all nonempty 6m-spread core-free D with tau*(D)/m unbounded, there exists internally m-valid H with |H|>=c |D|/m³`
for some absolute c independent of m and D, accounting for all forward-private pair pieces, nonprivate edges, Lemma E vertex pieces, all exact pair/singleton kernels AND global EMPTY. Neither S035-A nor S034-A establishes it. Replacing tau* with nu changes nothing: nu/m can also grow unbounded (same D_{m,N} example). No statement that every high-cover system decomposes into compatible low-cover subsystems at constant total mass has been proved. Applying §2 separately to pieces and *uniting* outputs would repeat S034's false singleton-gluing step.

The only new positive is the **conditional bounded-fractional-cover class** (and its bounded-matching corollary), with no Delta/private-mass restriction. This does not close DSE3/R3 or the whole every-k TIK theorem.

## 6. Mandatory symbolic controls (no new research computation)

| Frozen population | Actual status under S035-A / precise kernel guard |
|---|---|
| S032 row-palette K_(m+1,m+1), r>=216; global-private 2/(m+1) cap | Original D itself is fully valid; S035 makes NO global-privacy restriction and hence cannot contradict full-density H. Many apex overlaps do not enter theorem; no union attempted. |
| S031 r=1024m shared-z stars and dense repair | A selected single-x lift contains no EMPTY intersection. Original shared z creates a singleton on unsafe unions; dense repaired selection still exists in D. No invented extra-petal guarantee. |
| S030 repeated {q,z}; S022 repeated light | Two individually safe components may create an invalid exact PAIR or singleton if glued; S035 returns one link lift and never glues. |
| S029 K_(m-1,m-1), w=m-1 | The rep-only obstruction and one full-block rescue persist. Weighted original edge mass is not confused with representative number. |
| S018/S019 mixed channels | Exact singleton residual and global EMPTY failures of naive mixed unions remain. Every S035 output is a SINGLE common-apex lift, which checks pair and singleton and has no EMPTY realised. |
| FULL S023 nested q-plane including A rescue | Whole-block BSEL remains provisionally refuted; S035 is an **individual-edge** bound, does not require keeping original whole blocks and does not discard A rescue. |
| S024 private-third K_N dense graph | Its good representative output remains available; low cover is only sufficient, not a necessary condition. |
| N disjoint (m-1)^3 transversals | §4 covers complete 6m-spread core-free population and witnesses EMPTY with Ns≥m. No bound tau*=O(m) independent of N. |
| Complete K_(N,N,N), N>=6m | 6m-spread but robust core is whole D; NOT a core-free DSE example. S033 Proposition C covers it. |
| S034 r=108m² twin stars | All-apex union has invalid {x_i} matching 2<m despite pair and EMPTY passing; the same-family half-density alternate remains valid. Theorem S035 never licenses union. |
| m=2, empty D, small D, degenerate H, arbitrarily large m | H=D for m=2; empty family selects empty; a one-edge H vacuously valid. The theorem's absolute density in small-cover regime uses T2, not unsupported single-edge fallback. Bounds are uniform all m>=2 and literal cardinalities. |

## 7. Final evidence boundary

This is a symbolic restricted positive theorem and a quantified **method** counterexample, both only SAME-ASSISTANT scrutinised. No analytic DSE3 counterexample with `m³ max_valid(D)/|D| ->0`; §4 has the opposite lower bound. S033 T2 and robust-core reductions have not been independently refereed. Detailed new N1/N2 deferred by owner instruction, not originality clearance. No Lean, publication, correspondence or parent mathematical S001 execution. S036 FUTURE only.
