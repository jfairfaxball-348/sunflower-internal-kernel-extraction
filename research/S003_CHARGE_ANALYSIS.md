# P001-S003 — heavy-link collision charge: first failed implication and L_AVG counterexample

2026-10-10. **Verdict: NO_GENERAL_PROGRESS / EXACT L_AVG REFUTED (symbolic asymptotic proof; no independent review).** One bounded child mathematical slice only. This disproves the project's *auxiliary colour-palette expectation* as mathematically stated; it does **NOT** refute R3, TIK, or the Erdős–Rado Sunflower Conjecture. No positive extraction theorem, novelty promotion, Lean, manuscript or external action. The charge was explicitly frozen **before this analysis** in [S003_CHARGE_SPEC.md](S003_CHARGE_SPEC.md); N1 sources and limits in [S003_N1.md](S003_N1.md).

## 1. Freeze, recipients and what would count as a charge

For m>=3, use the EXACT pre-colouring lexicographic maximum residual matching certificates, M=288m, good edges G_P(chi) and internally valid b_m(G_P). Define A_m(F) as those E whose ambient residual matching number is >=m at ALL seven proper subsets K of E. Let D_P be good E in A_m(F) whose G_P contains at least one other edge, and R_P be the UNION OF EDGES of all internally m-valid H subset G_P with |H|>=2. The proposed necessary test for an absolute bounded-multiplicity charge was

    E sum_P |D_P| <= B * E sum_P |R_P|            (B_CHARGE)

for an absolute B. A map to distinct recipient edges with max B sources per recipient would imply this inequality. The RHS is NOT the L_AVG capacity functional: the union of all eligible H can be much larger than one optimum H_P, and singletons are deliberately not eligible charge recipients. This is a mechanism diagnostic, not a renamed proof of L_AVG. A failure disproves this specific charge, not every imaginable new proof method.

## 2. One explicit symbolic family sequence

For each integer t>=2, put m=t^2 and N=t^3. Take three pairwise disjoint N-element vertex parts X_1,X_2,X_3, and set

    F_t = { {x_1,x_2,x_3} : x_i in X_i for i=1,2,3 };
    |F_t| = N^3 = t^9,   M=288m=288t^2,
    Q=binom(M,3) <= M^3/6 = (288^3/6)t^6.

These are **complete tripartite transversals**, not a computationally enumerated population. Label the ground set [3N] canonically and follow the fixed lexicographic matching convention. For every E in F_t and every proper K subset E:

- |K|=2: the residual F_t(K) comprises all N distinct third vertices, hence matching number N>=m.
- |K|=1: the residual F_t(K) is the complete bipartite graph on the other two N-vertex parts, hence matching number N>=m.
- K=empty: the residual F_t has N pairwise disjoint diagonal triples, and no matching can exceed N.

Consequently **A_m(F_t)=F_t**, psi(K)=empty for all proper K subset an edge E (indeed every relevant link is rich). Goodness reduces exactly to three distinct vertex colours. F_t itself is internally m-valid at EVERY realised 2-point, 1-point and empty kernel; one can choose m residual witnesses IN F_t, which need not include either selected edge. The failure below comes wholly from the post-colouring exact three-colour palette split, not a deficient ambient family.

## 3. The palette occupancy barrier

For a palette P in binom([M],3), write X_i(P)={x in X_i: chi(x) in P}, and Z_{i,P}=|X_i(P)|. Let B_t be the event that at least one (i,P) has Z_{i,P}>=m. Since vertex colours are independent,

    Z_{i,P} ~ Binomial(N,3/M).

If B_t does NOT occur, each of the three part-sets of vertices whose colours belong to P has fewer than m members, for EVERY palette P. **No G_P contains an m-petal sunflower:** in an m-sunflower of distinct tripartite triples, within each coordinate i all petals' vertices are either identical or pairwise distinct. All three coordinates cannot be identical, so at least one coordinate uses m different vertices from X_i(P), impossible if Z_{i,P}<m. This reasoning includes exact kernels of size 2, size 1 and 0; it does not demand that the selected pair appear in the witnessing sunflower.

Hence on B_t^c, each G_P is m-sunflower-free, so every internally valid subfamily of G_P has at most ONE edge. Therefore

    b_m(G_P) <= 1,   R_P=empty  for every P.

Singleton capacities ARE allowed: occupied palettes may have b_m=1, but those singletons cannot repair a colliding good-edge class by providing a nontrivial internal witness.

## 4. A uniform tail bound and falsification of L_AVG

For a Binomial(N,p), the event Z>=m implies some m-subset is entirely selected, giving

    Pr(Z>=m) <= binom(N,m) p^m <= (e N p/m)^m.

Here p=3/M=1/(96t^2), N=t^3 and m=t^2, hence

    Pr(Z_{i,P}>=m) <= (e/(96t))^(t^2).

By a union bound over 3Q choices,

    q_t := Pr(B_t) <= 3Q (e/(96t))^(t^2) --> 0.

No independence between (i,P) events was assumed. For any colouring, every G_P is a subfamily of F_t, and the palettes partition the good edges, whence

    sum_P b_m(G_P) <= |F_t|.

On B_t^c we sharpen this to <=Q. As a result

    C_m(F_t)/|F_t|
      = E[sum_P b_m(G_P)]/t^9
      <= Q/t^9 + q_t
      <= (288^3/6)*t^(-3)
         + 3*(288^3/6)*t^6*(e/(96t))^(t^2)
      --> 0 as t --> infinity.

The infimum C_m(F)/|F| across m>=3 and nonempty finite triple families is therefore **zero**. There is NO absolute eta>0 satisfying the exact L_AVG statement, notwithstanding E[total good edges]/|F_t| = (M)(M-1)(M-2)/M^3 -->1. This counterexample concerns random colouring's **expectation**, not one exceptional colouring. It uses precisely the fixed M=288m and the demanded independent colour model. It does not show that ANY different colouring, adaptive palette selection or other algorithm fails to prove R3.

## 5. First failed heavy-link charging implication

Every E is ambient saturated. Let D=union_P D_P; with A_m(F_t)=F_t, the only good edges excluded from D are those whose palette is occupied by exactly one good edge. There are at most Q such edges in any colouring. Since psi is empty on relevant links, a triple is good iff rainbow, and therefore

    E|D| >= ((M)(M-1)(M-2)/M^3)*|F_t| - Q,
    liminf E|D|/|F_t| >= 1.

But R_P=empty for all P on B_t^c, while sum_P |R_P|<=|F_t| always (all R_P are within disjoint-palette good classes), hence

    E sum_P |R_P|/|F_t| <= q_t -->0.

Thus no absolute B can satisfy B_CHARGE. **The precise first broken implication is: “ambient residual links of matching number at least m, plus abundant same-palette good-edge collisions, force nontrivial internally m-valid recipient sets in that palette with bounded aggregate loss.”** It is false simultaneously at the pair-singleton, singleton-graph and empty-triple kernel levels, even after averaging over all independent random colourings. High same-palette edge multiplicity cannot stand in for m disjoint residual witnesses.

One cannot rescue the charge by allowing only the original selected pair as witnesses: the definition always allows any sunflower within H, and none exists on B_t^c. Nor by counting R_P with multiplicities: the eligible families themselves are empty on that event. The earlier S001 six-colour bad colouring is not used; this is an independent *random-colouring asymptotic* obstruction that reaches the expectation itself.

## 6. Strict scope and boundary bookkeeping

- m=2: R3 and full TIK are trivial by H=F, because a pair itself is a two-petal sunflower. L_AVG and B_CHARGE deliberately quantify m>=3. The counterexample takes m=t^2>=4; failure on this infinite subsequence refutes an eta uniform across all m>=3. No assertion is made about fixed m.
- F=empty or n<3: G_P empty, b_m(empty)=0; the asserted L_AVG inequality holds as 0>=0 in that isolated case. The counterexample has n=3t^3>=3 and F nonempty.
- Singleton G_P has b_m(G_P)=1 (and empty G_P has 0). An internally valid family with two edges requires an m-sunflower in that same H. Capacities and density inequalities count integers; “>= real target” is equivalent to “>= its ceiling”. No nonzero universal eta exists, so the conditional c=6eta/288^3 conversion is NOT available.
- Goodness is fixed before colouring, and **all** psi(K)=empty on this family; there is no hidden conditioning on matchings selected after colouring.
- No enumeration, sampling, simulation, numerical population, theorem formalisation, external contact or paper was performed. The limits above are symbolic exact inequalities. Cross-checked algebraically within the same assistant; this is NOT independent mathematical scrutiny and not an originality or publication claim.

## 7. Decision and safe continuation

The project's S001 proposed L_AVG sufficient lemma must be **withdrawn as false**, and any approach relying on universal palettewise expected optimal capacity or bounded heavy-link collision charge must not be reused. This is real negative progress in mechanism selection, **NO_GENERAL_PROGRESS toward R3/TIK**, not a pivot to another mathematical target. Full TIK remains SOURCE_POSED_CONJECTURE / STRONG_EVIDENCE_OPEN / NOVELTY_UNCERTAIN, R3 exact literature status STATUS_UNCERTAIN; new positive theorem count zero, Lean NOT_STARTED, publication IDEA. The exact symbolic counterexample deserves independent mathematical scrutiny before any originality-related promotion. A bounded P001-S004 gate may independently challenge/check these estimates and decide whether the fixed palette-partition route should be formally retired; no S004 research is executed now.
