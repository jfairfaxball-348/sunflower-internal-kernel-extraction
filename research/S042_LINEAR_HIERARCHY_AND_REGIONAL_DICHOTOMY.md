# P001-S042 — all-rank LINEAR TIK extraction, bounded-codegree extension, and a decisive regional mass-dichotomy obstruction

Date: 2026-10-13. One separately owner-invoked P001-S042, exact archived input commit `aeda624f3e14b3f83fb07a3767ae699e45b2d674`, separately hashed manifest `b86979e68ce6801dfc7923a0755f800b8874ee22`, mathematical freeze `9b9ba624bbd32bed4cb80161489ef3758d95b7b7` BEFORE this report. **SAME-ASSISTANT SYMBOLIC proof; NOT independently reviewed, originality-audited, formalised or published.** No new finite mathematical experiment. S042's ambitious universal HDSE3 and full original every-k TIK fronts remain UNPROVED.

## 1. Original exact quantifier and linear rank theorem

An internally m-valid family H means for **every** exact kernel K=A∩B of distinct A,B∈H, including K=∅, there are m different edges E_1,...,E_m∈H with all pairwise intersections **exactly K**; the witnessing edges need not include A,B. Equivalently ν(H(K))≥m for all realised K. The full unrestricted TIK conjecture asks for c_k>0 independent of m,n,F with |H|≥c_k|F|/m^k.

A k-family is **linear** if distinct edges have intersection of cardinality at most one. This is a restriction of INPUT F, not an edge-pair condition that can be assumed after selection.

**THEOREM S042-A (all ranks, linear input, quantified).** For every k≥1 and m≥2, every finite linear k-uniform family F contains internally m-valid H⊆F satisfying

    |H| >= |F| / [2^(k-1) k^k m^k].                           (A)

In particular every arbitrary linear triple family admits |H|≥|F|/(108m³), and the m-exponent is exactly the original target exponent IN THIS CLASS. No spreadness, high-degree cap, bounded vertex cover, disjoint regions, complete palettes or fixed ground size is assumed. The proof below is existential; no algorithmic runtime claim is made.

**Base k=1.** If |F|≥m, take F (all distinct singleton edges, only EMPTY is realised for |F|≥2 and F has m disjoint edges). If |F|<m, take one edge; for F empty take empty. At k=1 the stated c_1=1 works.

**Base k=2.** Every simple graph is linear as a 2-family. Use the detailed SAME-ASSISTANT S033 graph extraction theorem |H|≥|F|/(8m²), with its separate low-degree orientation, graph m-core, singleton and EMPTY verification. This is c_2=1/[2^(2-1) 2²]=1/8. The current all-k restricted result therefore inherits that same-assistant graph proof, not independent verification of it.

**Inductive step k≥3.** Suppose S042-A holds for linear rank (k-1) with c_(k-1)=1/[2^(k-2)(k-1)^(k-1)]. Put e=|F|; if e=0 return H=empty. Set

    p_k = (1/k)((k-1)/k)^(k-1)=(k-1)^(k-1)/k^k.             (B)

Let Δ be the maximum ORIGINAL vertex degree in F.

**High-degree alternative.** If Δ > e/(2km), choose a vertex v of original degree Δ. In linear F all edges containing v have pairwise exact intersection {v}. If Δ≥m, take ALL those Δ edges: their only realised kernel is {v}, supplied by any m selected edges in the star, and EMPTY does NOT occur. Size Δ>e/(2km)≥c_k e/m^k. If Δ<m, then e<2kmΔ<2km², and one edge gives valid singleton H of size 1>e/(2km²)≥c_k e/m^k (k≥3,m≥2). No outside-F petals have been used.

Now assume **low original maximum vertex degree** Δ≤e/(2km).

**Case C: dense vertex m-core.** Iteratively remove a current vertex whose positive degree lies in 1,...,m-1, together with all its current incident edges. Let C be the final k-uniform edge family; every nonisolated vertex in C has degree ≥m, and C remains linear. If |C|≥e/2, take H=C. Every distinct selected pair intersects either at exactly a vertex x, and its degree deg_C(x)≥m supplies m edges through x whose pairwise intersection is exactly {x} (by linearity), OR at EMPTY. For EMPTY take any maximal selected matching M. Its union of ≤k|M| vertices meets every C-edge, so

    |C| ≤ k|M| Δ(F).

Hence |M|≥ |C|/(kΔ(F))≥(e/2)/(k·e/(2km))=m. Therefore if EMPTY is realised, a genuine matching of m C-edges witnesses it. Thus C is internally valid with |H|≥e/2≥c_k e/m^k. This works whether the original robust core C(F) is empty or not: the vertex m-core is a different object.

**Case D: low-degree peeled majority.** Otherwise D=F\C has |D|>e/2. At each peeling step assign every deleted edge to its first deleted endpoint v. At that moment at most m-1 incident edges are removed, so each vertex is the assigned apex of at most m-1 ORIGINAL D-edges; give those outgoing edges distinct labels j∈{1,...,m-1}. The label assignment is an exact partition D=⊔_{j=1}^{m-1} D_j, including possibly empty classes. A vertex can occur in other edges with different assigned apices; this will be dealt with rather than assumed away.

Independently colour EACH ground vertex RED with probability 1/k and BLUE with probability (k-1)/k. An oriented edge e={a(e)}∪S(e) is **good** if its assigned apex a(e) is RED and all its remaining k-1 vertices S(e) are BLUE. The probability is exactly p_k in (B), irrespective of overlaps across different edges. Linearity of expectation gives one deterministic colour assignment with at least p_k|D| good edges; no independence of good-edge events is needed. Fix that assignment, and choose one label class j containing at least

    t ≥ p_k|D|/(m-1)                                        (C)

good edges. For this class every RED apex occurs in at most ONE edge, and no apex is BLUE. Delete the RED apex of each good class-j edge; obtain a (k-1)-uniform BLUE base family G.

For k≥3, **G is a set with exactly t distinct edges**: two distinct original edges having identical (k-1)-subsets would share k-1≥2 vertices, violating ORIGINAL linearity. Moreover G is itself linear: pairwise BLUE-base intersections are subsets of the original pair intersections, hence have size ≤1. Select the inductively guaranteed internally valid J⊆G with |J|≥c_(k-1)t/m^(k-1). Restore to each g∈J its UNIQUE previously assigned RED apex a(g), yielding H⊆F. RED apices across this chosen class are all distinct and are outside every BLUE base. Therefore, for **every pair** of selected edges,

    (g∪{a(g)}) ∩ (h∪{a(h)}) = g∩h,    for g≠h.             (D)

The same equality holds for EVERY pair of m witness edges lifted from a sunflower in J. Thus each realised kernel K of H, whether K=EMPTY or a singleton (or generally any base kernel), occurs in J and has the same m witness petals after lifting, **all inside the final H**. This is a private-labelled lifting equivalence, distinct from an invalid naive union of overlapping local stars.

Finally, from (C), |D|>e/2, and 1/(m-1)≥1/m,

    |H| ≥ c_(k-1) p_k |D| / [(m-1)m^(k-1)]
         ≥ (c_(k-1)p_k/2) e/m^k
         = e/[2^(k-1)k^k m^k].

The last equality follows by direct cancellation of (k-1)^(k-1). Case D proves the induction step. Together with high-degree and Case C, this proves S042-A at every fixed k.

**Constants:** c_1=1, c_2=1/8, p_3=4/27, c_3=(1/8)(4/27)/2=1/108; c_4=(1/108)(27/256)/2=1/2048. In general c_k=1/(2^(k-1) k^k). When m=2, H=F already works for ANY input, so all inequalities are conservative. A one-edge selected H is vacuously valid; never identify it with a two-edge partial matching for m>2.

## 2. All-ranks bounded original pair-codegree extension

For a nonempty k-family F let B=max_{u≠v} d_F({u,v}), with B≥1 for k≥2.

**THEOREM S042-B (bounded pair-degree).** For every k≥2, m≥2, if original F has all pair degrees ≤B, there is an internally m-valid H⊆F with

    |H| ≥ |F| / {[1+binom(k,2)(B-1)] 2^(k-1) k^k m^k}.       (E)

**Proof.** Build a simple CONFLICT graph whose vertices are original k-edges, with adjacency precisely when two DISTINCT original edges meet in ≥2 ground vertices. For each fixed original edge e, every conflicted e' shares at least one pair P⊂e, and each such P belongs to at most B-1 other original edges. Therefore conflict-degree ≤binom(k,2)(B-1), without requiring the different pair classes to be disjoint. Greedily properly colour the graph with at most Q=1+binom(k,2)(B-1) colours. Its largest independent colour class L⊆F has |L|≥|F|/Q, and by definition L is a LINEAR k-family. Apply S042-A to L and keep H⊆L⊆F. Witnesses are in H; an original intersecting pair discarded from F imposes no condition on H. This proves (E).

For triples Q=3B-2 and bound |H|≥|F|/[108(3B-2)m³]. For every FIXED k and B, the exact target m^-k exponent is established on a broad high-overlap class, even with unbounded vertex degrees and arbitrarily high fractional transversal. But B growing as m would add an unwanted factor m: this proof has NOT solved the intermediate pair-codegree [2,m-1] HDSE3 stratum. Exponent in B is a method loss, not an asserted extremal necessity.

## 3. Quantified failure of the proposed TWO-WAY regional mass dichotomy in genuine HDSE3, with SAME-E full positive rescue

S041's general theorem needs a bounded-cover global core plus bounded-local-cover vertex-disjoint islands, whereas S042's owner prompt asks whether such a decomposition can be forced on arbitrary ORIGINAL high-degree spread core-free triples. The following exact same-E construction rules out a universal TWO-WAY ORIGINAL MASS CAPTURE by those options, while preserving the all-link positive extraction via another mechanism.

Fix m≥2 and n=3^d arbitrarily large compared with m³. Let V=F_3^d and let E=all affine lines as 3-sets {x,x+v,x+2v} with v≠0. Every unordered pair of points determines a UNIQUE third point and a UNIQUE affine line. Therefore E is a linear Steiner triple system with

    |E|=n(n-1)/6,    d_E(x)=(n-1)/2 for each x,
    d_E({x,y})=1 for each x≠y.                              (F)

Use d chosen so that n≥40m³ (certainly n can tend to infinity faster than m). All HDSE3 hypotheses are satisfied:
- ORIGINAL 6m-spread at a vertex: d_E(x)/|E|=3/n≤1/(6m), since n≥18m;
- at any pair: d_E(xy)/|E|=6/[n(n-1)]≤1/(36m²), since n(n-1)≥216m²;
- at any full triple: 1/|E|≤1/(216m³), since n(n-1)≥1296m³;
- SAME ORIGINAL high degree: each edge meets a vertex of degree (n-1)/2>m³;
- robust core EMPTY: every edge has a contained original pair xy of degree 1<m, so no nonempty robust subfamily can certify that pair's nonempty link.

**SAME-E RESCUE STRONGER THAN NECESSARY:** E itself is internally m-valid for n≥40m³. Its distinct edges meet only at singleton vertices or EMPTY. Every realised singleton {x} has degree (n-1)/2≥m, and because the system is linear, all chosen edges through x intersect pairwise at exactly {x}. A maximal matching M satisfies |E|≤3|M| Δ(E), hence |M|≥n/9≥m. Thus EMPTY, whenever realised, also has m wholly-IN-E petals. Consequently maxvalid_m(E)=|E|, so m³ maxvalid/|E|=m³, NOT a counterexample to HDSE3.

**DECISIVE NEGATIVE against the bare two-branch S041-type mass cover:** Let B≥1 be fixed independent of m,n, and consider ANY collections of original subfamilies D_0,D_1,...,D_r⊆E (even omitting the requirement of disjoint edge families), with τ*(D_0)≤Bm and τ*(D_i)≤B (i≥1), and pairwise vertex-disjoint supports of D_i for positive i. For any original subfamily D supported on s vertices, linearity implies each x has d_D(x)≤(s-1)/2: different triples through x use DISJOINT pairs of other vertices. By original mass/cover counting,

    |D| ≤ τ*(D) Δ(D) ≤ τ*(D)(s-1)/2.                  (G)

Thus |D_0|≤Bm(n-1)/2, while Σ_i |D_i|≤(B/2)Σ_i s_i≤Bn/2. For the total **original mass counted once** even if D_0 overlaps island edge sets,

    |D_0 ∪ (∪_i D_i)|/|E|
      ≤ [Bm(n-1)/2+Bn/2] / [n(n-1)/6]
      = 3B [m/n+1/(n-1)] → 0 as n/m→∞.              (H)

Hence NO fixed B and positive universal captured-mass fraction γ can force the bare alternatives "global τ*≤Bm captures γ mass" OR "vertex-disjoint τ*≤B islands capture γ mass" on all HDSE3 inputs. Indeed these two channels together capture o(|E|) in the SAME ORIGINAL E as n/m→∞. Any purported universal regional dichotomy NEEDS a genuinely third, overlapping certificate route; the two-branch mass-cover mechanism alone is FALSE, not merely unproved. This does NOT falsify S041's CONDITIONAL theorem (which assumes an actual complete partition) and does NOT falsify HDSE3: the SAME E is FULLY valid. S042-A gives an independent constructive-existential explanation for all linear inputs, not just this Steiner example.

## 4. Ambitious universal fronts and exact remaining gap

Attempted universal local-to-global charge: direct one-apex lifts preserve nonempty kernels within a lift, but when multiple original high-degree apices are combined, the cross-lift intersections may be PAIR {u,v}, SINGLETON {u} or EMPTY with 2..m-1 actual selected matching. S039's five selected-H tests still demand pair palette counts, mixed pairs, palette vertex graphs, base vertex link bipartite matching, and global triple matching. The red/private-label construction bypasses this difficulty ONLY after low-degree peeling AND ORIGINAL pairwise intersections ≤1 (or after losing a 1/B factor to conflict-colouring). It does not convert arbitrary original degree >m³ into m-degenerate oriented mass.

Attempted universal original-mass regional dichotomy: (H) demonstrates that the naive two capture alternatives fail even on genuine 6m-spread, core-free, high-degree input. The third overlapping certificate can succeed spectacularly (E itself!), but the current red/private-label argument has no constant-mass extraction for arbitrary pair codegree B≈m without paying 1/B. Likewise S041's core/island conditions are not guaranteed.

The project does NOT assert HDSE3, rank-three R3, nor unrestricted every-k TIK from these restricted theorems. S036's HDSE3⇒R3 reduction stays conditional; rank-three alone never implies all ranks.

**FIRST MISSING UNIVERSAL IMPLICATION:** remove the extra 1/B conflict-colouring loss as B reaches m-1 while keeping all five exact final-H link tests; OR find a direct high-degree/nonlinear local-to-global theorem controlling saturated pair cores and EMPTY matchings at original mass m^-3. The extended nonprivate S023, S029–S032, S037–S041 geometries remain outside a blanket linearization, though their SAME-ORIGINAL families have their previously established positive rescues. No valid HDSE3 counterexample sequence with m³ maxvalid/|E|→0 is known or claimed.

## 5. Quantifier integrity and named controls

- EMPTY is explicitly matched in the large vertex core by greedy matching, the high-degree star never realises EMPTY, the singleton selection is vacuous, and the private-apex lift transfers EMPTY witnesses EXACTLY from the BLUE base. Never use witnesses in original F\H.
- k=1 and k=2 are separately based; the induction step requires k≥3 so that (k-1)-subsets of distinct original edges are different under linearity. Using this step for k=2 would be invalid because BLUE singleton bases can repeat.
- m=2 any F works; the inequalities hold but are weaker. For m≥3 no two disjoint selected edges may stand alone without an m-matching.
- S023 affine/projective plane whole-BSEL failure does not touch S042-A since its ORIGINAL triple blocks share pairs within components. The disjoint-plane valid partial-edge rescue persists.
- S024 dense K_N private thirds and S029 bipartite private thirds are linear only after selecting one distinct private third per base edge; that is a valid scoped control and not a claim the entire packed input is linear.
- S030/S031 repeated lights, S032 rows, S034 twins, S037 common palette, S038 full tensor, S039 intermediate partial palettes and S040 mixed star products can contain pairs of triples sharing TWO vertices. They cannot be called LINEAR without checking the exact original pair census; S042-B may incur a factor B. The already recorded SAME-E positive repairs of these families remain intact.
- S035 large fractional-cover structures may be linear or nonlinear; (H) supplies an explicit high-cover linear HDSE3 example that evades S041 regional mass capture while already being entirely valid.
- No finite sample/experiment was run. This is a universal symbolic induction and a parametric symbolic F_3^d construction; no seed, dedup or CPU claim is made.
- Existing literature JJSW26 §6 attribution and uncertain novelty are unchanged. SAME-ASSISTANT report, no independent referee, source-intensive new N1/N2 (owner deferred pending complete ORIGINAL TIK candidate), Lean, Palomar, paper, correspondence, submission or publication. S045 next compulsory fifth audit; S043 only FUTURE.
