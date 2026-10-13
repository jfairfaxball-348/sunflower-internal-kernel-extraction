# P001-S042 — hostile mathematical second pass (independent reconstruction of arguments, SAME assistant)

Date 2026-10-13. This check was written AFTER the mathematical report commit `fbfa5aae547e4e63ca845f9f37bfc20754d1ff0b`. It is an independent-of-report-lines reconstruction by the SAME ASSISTANT, **not** a second human reviewer, a Lean proof, new N1/N2, or a finite computation.

## 1. Derive the induction from scratch; seek counterexamples

Define m-valid exactly from FINAL selected family: every realised pair intersection K (including ∅) has a selected m-sunflower at K. For a linear F, any two different edges through vertex v intersect precisely at {v}. Hence an all-through-v star with ≥m edges is m-valid; a nonempty singleton is vacuously m-valid. No claim that the union of separately valid arbitrary stars is valid.

Fix k≥3, e>0. Either original Δ>e/(2km), in which case Δ≥m gives a valid large star or Δ<m forces e<2km², when one edge exceeds e/(2km²) and hence e/[2^(k-1)k^k m^k]. The last inequality uses k≥3, m≥2 and 2^(k-1)k^k≥2k. No conflict with the lower-rank statement when k=2: k=2 MUST use S033 separately.

If Δ≤e/(2km), peel all current vertices of degrees 1..m-1 and let C remain. Each surviving positive degree is ≥m. If |C|≥e/2, any maximal matching M of C makes all C-edges meet the k|M| vertices it covers; count each degree in ORIGINAL F by at most Δ, yielding e/2≤|C|≤k|M|Δ≤k|M|e/(2km), hence |M|≥m. Thus EMPTY is witnessed in C if realised; any vertex intersection is witnessed by ≥m edges through that vertex, pairwise exact singleton due to linearity. C valid. Note it is a VERTEX m-core, and not S033's robust core; a core-free linear triple system may nevertheless have C=F.

If |D|=e-|C|>e/2, each peeled edge receives a FIRST deletion apex a(e) with at most m-1 outgoing edges at that apex; per-apex proper outgoing labels j exist and produce m-1 classes. Colour all ground vertices red with probability 1/k. For each oriented edge good event `a(e) red and remaining k-1 blue` has probability (1/k)(1-1/k)^(k-1) exactly p_k. *Dependencies between events do not invalidate expectation*. Fix a colouring achieving expected mass, then one label j contains ≥p_k|D|/(m-1) good edges.

Hostile challenge A: A red apex could be used as a blue base elsewhere, introducing wrong lifted kernels. Impossible in good class: all bases are BLUE, all apices RED.

Hostile challenge B: Two good edges could have the SAME red apex, destroying the lift's exact intersection equality. Impossible by distinct outgoing labels j at every apex.

Hostile challenge C: Deleting red apices could produce duplicate (k-1)-edges; then naive cardinality t would be false. For k≥3, such a duplicate would imply original edges intersect in k-1≥2 vertices, directly contradicting linearity. **This is WHY k=2 is a separate base, and WHY the proof does not extend to arbitrary nonlinear triples without a loss.** The bases are themselves linear: intersection of their blue parts is included in intersection of original edges.

Hostile challenge D: If J in bases is valid only for kernels involving its intersecting pairs, could lifted H introduce a NEW kernel not realised in J? For every two lifted edges, distinct red apices and red/blue separation give exact set equality of intersections with the corresponding blue bases. Thus I(H)=I(J) as SETS of BLUE kernels, including empty, and each m-base-sunflower transfers to m ORIGINAL good edges sharing that exact kernel; all petals remain inside final H.

Hostile challenge E: A peeled vertex might already lie in earlier deleted edges and so have >m-1 total incidence. Correct, but the outgoing label condition counts ONLY edges whose apex is that vertex, which are precisely the at-most m-1 current edges deleted at its own step. Earlier incoming edges never share its outgoing red-apex identity, and red/blue separation prevents confusing these roles in H.

Size algebra from scratch: t≥p_k(e/2)/(m-1); inductive m-valid J has ≥c_(k-1)t/m^(k-1); using m-1≤m, obtain c_(k-1)p_k e/(2m^k). Since p_k=(k-1)^(k-1)/k^k and c_(k-1)=1/[2^(k-2)(k-1)^(k-1)], output c_k=1/[2^(k-1)k^k]. k=3: p=4/27, 1/8 ×4/27×1/2=1/108. k=4: p=27/256, (1/108)×27/512=1/2048. Test m=2 directly: original F itself valid for ANY k, so all bounds valid.

## 2. Recheck bounded-codegree reduction without hidden structural assumption

Two distinct original k-edges conflict only if they have at least one common pair P, and each of the binom(k,2) pairs in a fixed edge lies in ≤B-1 other original edges. Thus max conflict degree ≤binom(k,2)(B-1). Proper greedy colouring of a *finite* graph into ≤1+max degree classes is elementary; one has ≥e/Q edges. Every class is linear by construction. Apply the independently reconstructed linear theorem to that class and use selected-H witnesses, not ambient F. For k=3 Q=3B-2. This is a theorem with fixed-B constants, NOT a B-independent HDSE3 theorem if B≈m. For B=1, Q=1 exactly recovers the linear bound, so no phantom factor appears. For m=2 the stronger F itself works.

## 3. Recheck SAME-E affine Steiner obstruction AND positive rescue

Let n=3^d, d≥1, all 3-point affine lines in F_3^d. Each pair x≠y lies on exactly one line (x,y,-x-y), so each edge is unique and any two edges share ≤1 vertex. Counting ordered distinct pairs gives 6e=n(n-1), so e=n(n-1)/6. Each vertex lies on (n-1)/2 lines by pairing all other vertices with the unique third, so Δ=(n-1)/2. Original pair degree always 1. For m≥2 and n≥40m³ all explicit HDSE3 tests hold:
- 3/n ≤1/(6m) (requires n≥18m);
- 6/[n(n-1)]≤1/(36m²) (requires n(n-1)≥216m²);
- 6/[n(n-1)]≤1/(216m³) (requires n(n-1)≥1296m³);
- (n-1)/2>m³.
All follow from n≥40m³ for m≥2. Robust-core emptiness is EVEN STRONGER than merely low original degree at one selected pair: every edge contains three pairs, each with original degree 1<m, so no robust edge can exist.

For an arbitrary subfamily D with support s, each vertex x participates in at most (s-1)/2 triples (linearity means the other TWO vertices are disjoint across edges through x). Fractional cover inequality is |D|≤Δ(D)τ*(D), with τ*(D)≥1 for nonempty D; empty D contributes zero. If D0 has τ*≤Bm, n-support bound |D0|≤Bm(n-1)/2. For island D_i with τ*≤B and disjoint support sizes s_i, |D_i|≤B(s_i-1)/2, and Σs_i≤n, so Σ_i|D_i|≤Bn/2. A UNION mass is at most the sum even if D0 and islands overlap as edge sets. Dividing by e gives 3B[m/n+1/(n-1)], which tends to 0 along n=3^d→∞ for fixed m,B and also along n/m→∞ with B fixed. Hence no fixed positive γ works for two channels together, even on fully HDSE3-compliant input.

Hostile challenge: Could E have EMPTY realised but no in-E m-matching? A maximal matching covers all edges through at most 3|M| vertices, each degree ≤Δ, so e≤3|M|Δ, giving |M|≥n/9. Since n≥40m³, |M|≥m. Any singleton kernel {x} has (n-1)/2≥m in-E lines through x, which are pairwise exactly-x intersecting. Thus H=E fully valid. In particular the negative concerns only the TWO-BRANCH REGIONAL COVER mechanism; it is NOT a TIK/HDSE3 counterexample, and no unearned limit m³ maxvalid/e→0 is asserted (ratio is exactly 1).

Hostile challenge: S041's theorem assumes a COMPLETE partition, not a claim that every E admits it. We are not refuting S041-A/B. We are refuting ONLY the proposed universal guarantee of fixed original mass captured by low-τ* global core AND/OR vertex-disjoint bounded-τ* islands. Any broader three-way dichotomy with explicit direct-overlap certificate may still be true, as H=E demonstrates.

## 4. Previously known difficult geometries and first missing implication

S023 plane-based whole-block negative has repeated pairs and is not globally linear. Its S024 partial-edge rescue remains possible. The private-third graphs S029/K_N are linear if (and only if) each third is globally distinct: our lift explanation supports their already known positive controls. The S030/S031 light collisions and S032 row palettes may contain same-base pairs with codegree≥2; the proof does NOT erase those via the recolouring. S038 common tensor and S039 intermediate per-spoke q=m-1 carry q>1 original pair degree, and conflict colouring may lose q; their original SAME-E valid selections are already recorded. S041 m-1 bipartite apex islands have pair degrees m-1, not a counterexample to linear theorem. For fixed pair multiplicity B bounded, S042-B includes arbitrarily overlapping singleton structures and high τ*, genuinely outside simple disjoint island hypotheses.

**Verdict:** no logical counterexample to the stated S042-A/B or quantified (H) was found in this second reconstruction. Evidence level is SAME ASSISTANT symbolic reasoning, not an independent referee. New mathematical results remain scoped, unrestricted HDSE3/R3/TIK UNPROVED, publication/theorem novelty statuses unchanged. FIRST OPEN rank-three bridge: selection with no B loss when 2≤original pair codegree≤m-1 (and saturated ≥m interacting classes), preserving final PAIR/singleton/EMPTY certificates. S043 must remain future, S045 next correction audit. No finite experiment, Lean, manuscript, outside contact or parent mathematical S001.
